import pathlib, hashlib, json, re, itertools, collections, time, resource, sys

NUMS = re.compile(r"(?:0|[1-9][0-9]*)(?: (?:0|[1-9][0-9]*))*")

class Bad(Exception):
    def __init__(self, code, lf, detail):
        self.code, self.lf, self.detail = code, lf, detail
        super().__init__(code + " at LF " + str(lf) + ": " + detail)

def need(ok, code, lf, detail):
    if not ok:
        raise Bad(code, lf, detail)

def numeric(text, arity, lf):
    need(NUMS.fullmatch(text) is not None, "CANONICAL_DECIMAL", lf, repr(text))
    vals = tuple(map(int, text.split(" ")))
    need(len(vals) == arity, "RECORD_ARITY", lf, "expected " + str(arity) + ", got " + str(len(vals)))
    return vals

def chi(w):
    if w == 7:
        return 7
    if w == 13:
        return 8
    if w % 6 == 3:
        return (w - 1) // 2
    if w % 6 == 1:
        return (w + 1) // 2
    raise ValueError("inadmissible STS order")

def mask(t):
    return sum(1 << x for x in t)

def counts_json(counter):
    return {str(k): v for k, v in sorted(counter.items())}

class Reader:
    def __init__(self, raw, kind):
        try:
            text = raw.decode("ascii")
        except UnicodeDecodeError as exc:
            raise Bad("ASCII", raw[:exc.start].count(b"\n") + 1, "non-ASCII byte")
        need(raw.endswith(b"\n"), "LF_TERMINATOR", raw.count(b"\n") + 1, "missing terminal LF")
        need("\r" not in text, "LF_ONLY", text[:text.find("\r")].count("\n") + 1, "CR byte")
        self.rows = []
        self.i = 0
        self.comments = self.blanks = 0
        self.slots = len(raw.split(b"\n"))
        for lf, line in enumerate(text.split("\n")[:-1], 1):
            if kind in ("S", "M") and line.startswith("#"):
                self.comments += 1
                continue
            if kind == "S" and "#" in line:
                line = line.split("#", 1)[0].rstrip(" ")
            if line == "" and kind == "S":
                self.blanks += 1
                continue
            need(line != "", "UNEXPECTED_BLANK", lf, "blank line not specified for this format")
            self.rows.append((lf, line))
    def end(self):
        return self.i == len(self.rows)
    def peek(self):
        return self.rows[self.i][1] if not self.end() else ""
    def at(self, word):
        return self.peek() == word or self.peek().startswith(word + " ")
    def pop(self):
        need(not self.end(), "TRUNCATED", self.rows[-1][0] if self.rows else 1, "unexpected end")
        row = self.rows[self.i]
        self.i += 1
        return row
    def exact(self, word):
        lf, text = self.pop()
        need(text == word, "FORMAT_MARKER", lf, "expected " + word + ", got " + repr(text))
        return lf
    def head(self, word, arity):
        lf, text = self.pop()
        need(text.startswith(word + " "), "FORMAT_HEADER", lf, "expected " + word + " header, got " + repr(text))
        return numeric(text[len(word) + 1:], arity, lf), lf
    def points(self, arity, v):
        lf, text = self.pop()
        values = numeric(text, arity, lf)
        need(all(0 <= a < v for a in values), "POINT_DOMAIN", lf, repr(values))
        need(len(set(values)) == arity, "REPEATED_POINT", lf, repr(values))
        return tuple(sorted(values)), lf
    def section(self, marker, class_marker, v):
        (x,), lf = self.head(marker, 1)
        need(0 <= x < v, "SECTION_POINT_DOMAIN", lf, str(x))
        classes = []
        while not self.end() and not self.at("POINT") and not self.at("STEMPOINT"):
            (label,), clf = self.head(class_marker, 1)
            triples = []
            while not self.end() and not any(self.at(k) for k in ("POINT", "STEMPOINT", "CLASS", "FRAME")):
                triples.append(self.points(3, v))
            need(bool(triples), "EMPTY_CLASS", clf, class_marker + " " + str(label))
            classes.append({"label": label, "lf": clf, "triples": triples})
        need(bool(classes), "EMPTY_POINT_SECTION", lf, str(x))
        return {"x": x, "lf": lf, "classes": classes}

def parse(raw, kind):
    p = Reader(raw, kind)
    obj = {"kind": kind}
    if kind == "S":
        (v, n, g, s), hlf = p.head("GCDCQS", 4)
        obj.update(v=v, n=n, g=g, s=s, hlf=hlf)
        (obj["colours"],), obj["colours_lf"] = p.head("COLOURS", 1)
        (obj["holefree"],), obj["holefree_lf"] = p.head("HOLEFREE", 1)
    elif kind == "D":
        lf, text = p.pop()
        need(text.startswith("GDD34 FDGDD "), "FORMAT_HEADER", lf, "expected GDD34 FDGDD")
        n, g = numeric(text[len("GDD34 FDGDD "):], 2, lf)
        v, s = n * g, 0
        obj.update(v=v, n=n, g=g, s=s, hlf=lf)
    else:
        (v,), hlf = p.head("MCDSQS", 1)
        n, g, s = 0, 0, 0
        obj.update(v=v, n=n, g=g, s=s, hlf=hlf)
        (obj["colours"],), obj["colours_lf"] = p.head("COLOURS", 1)
    if kind != "M":
        p.exact("GROUPS")
        obj["groups"] = [p.points(g, v) for _ in range(n)]
    else:
        obj["groups"] = []
    obj["stem"] = ((), obj["hlf"])
    if kind == "S":
        p.exact("STEM")
        if s:
            obj["stem"] = p.points(s, v)
    obj["blocks_lf"] = p.exact("BLOCKS")
    blocks = []
    while not p.end() and not p.at("POINT") and not p.at("STEMPOINT"):
        blocks.append(p.points(4, v))
    obj["blocks"] = blocks
    sections = []
    while not p.end() and p.at("POINT"):
        sections.append(p.section("POINT", "FRAME" if kind == "D" else "CLASS", v))
    obj["sections"] = sections
    stem_sections = []
    if kind == "S":
        while not p.end() and p.at("STEMPOINT"):
            stem_sections.append(p.section("STEMPOINT", "FRAME", v))
    obj["stem_sections"] = stem_sections
    need(p.end(), "UNPARSED_RECORD", p.rows[p.i][0] if not p.end() else obj["hlf"], repr(p.peek()))
    obj["syntax"] = {"LF_slots": p.slots, "noncomment_records_consumed": p.i, "comments": p.comments, "ignored_blanks": p.blanks}
    return obj

def partition_classes(sec, derived, expected):
    classes, x = sec["classes"], sec["x"]
    need(len(derived) == expected, "DERIVED_BLOCK_COUNT", sec["lf"], "point " + str(x) + ": " + str(len(derived)) + " vs " + str(expected))
    seen = {}
    for cl in classes:
        for t, lf in cl["triples"]:
            need(x not in t, "DERIVED_CONTAINS_BASE_POINT", lf, str(x))
            need(t not in seen, "DERIVED_PARTITION_DUPLICATE", lf, str(t) + ", first LF " + str(seen.get(t)))
            need(t in derived, "DERIVED_PARTITION_EXTRANEOUS", lf, str(t) + " at point " + str(x))
            seen[t] = lf
    missing = derived - seen.keys()
    need(len(seen) == expected and not missing, "DERIVED_PARTITION_MISSING", sec["lf"], "point " + str(x) + ", listed " + str(len(seen)) + ", missing " + str(min(missing) if missing else None))

def pair_design(derived, domain, pair_allowed, sec, group_of=None):
    pc = collections.Counter()
    for t in derived:
        need(set(t) <= domain, "DERIVED_DOMAIN", sec["lf"], str(t))
        if group_of is not None:
            need(len({group_of[a] for a in t}) == 3, "DERIVED_TRANSVERSAL", sec["lf"], str(t))
        pc.update(itertools.combinations(t, 2))
    positive = 0
    forbidden = 0
    for pair in itertools.combinations(sorted(domain), 2):
        expect = int(pair_allowed(pair))
        need(pc[pair] == expect, "DERIVED_PAIR_MULTIPLICITY", sec["lf"], "point " + str(sec["x"]) + ", pair " + str(pair) + ": " + str(pc[pair]) + " vs " + str(expect))
        positive += expect
        forbidden += 1 - expect
    need(sum(pc.values()) == 3 * len(derived), "PAIR_ACCOUNTING", sec["lf"], "pair incidence total")
    return positive, forbidden

def ppc(cl, code="CLASS_PPC_COLLISION"):
    used = set()
    for t, lf in cl["triples"]:
        overlap = used.intersection(t)
        need(not overlap, code, lf, "class label " + str(cl["label"]) + " at LF " + str(cl["lf"]) + ", repeated points " + str(sorted(overlap)))
        used.update(t)
    return used

def frames(sec, derived, domain, group_sets, own_group=None):
    classes = sec["classes"]
    need(len(classes) == 36, "FRAME_CLASS_COUNT", sec["lf"], str(len(classes)) + " vs 36")
    partition_classes(sec, derived, 648)
    for cl in classes:
        j = cl["label"]
        need(0 <= j < len(group_sets) and j != own_group, "FRAME_LABEL", cl["lf"], "invalid missed-group label " + str(j))
        used = ppc(cl, "FRAME_PPC_COLLISION")
        target = domain - group_sets[j]
        need(used == target and len(cl["triples"]) == 18, "FRAME_PC_DOMAIN", cl["lf"], "label " + str(j) + ": triples " + str(len(cl["triples"])) + ", missing " + str(sorted(target - used)) + ", extra " + str(sorted(used - target)))
    labels = collections.Counter(cl["label"] for cl in classes)
    expected_labels = {j: 9 for j in range(len(group_sets)) if j != own_group}
    need(dict(labels) == expected_labels, "FRAME_LABEL_COUNTS", sec["lf"], repr(dict(labels)))
    return labels

def verify(obj):
    kind, v, n, g, s = (obj[k] for k in ("kind", "v", "n", "g", "s"))
    expected_header = {"S": (74, 4, 18, 2), "D": (90, 5, 18, 0), "M": (74, 0, 0, 0)}[kind]
    need((v, n, g, s) == expected_header, "OBJECT_HEADER", obj["hlf"], repr((v, n, g, s)))
    X = set(range(v))
    if kind in ("S", "M"):
        r = chi(v - 1)
        need(obj["colours"] == r, "COLOURS_CHI", obj["colours_lf"], "got " + str(obj["colours"]) + ", chi(" + str(v - 1) + ") = " + str(r))
    if kind == "S":
        h = g + s - 1
        need(v == n * g + s and (v - 1) % 6 in (1, 3), "CQS_PARAMETERS", obj["hlf"], "inadmissible header")
        free = r - ((v - 1) - h) // 2
        need(obj["holefree"] == free, "HOLEFREE_HEADER", obj["holefree_lf"], "expected " + str(free))
    groups = [set(rec[0]) for rec in obj["groups"]]
    stem = set(obj["stem"][0])
    group_of = {}
    for j, (points, lf) in enumerate(obj["groups"]):
        need(len(points) == g, "GROUP_SIZE", lf, str(j))
        for a in points:
            need(a not in group_of, "GROUP_PARTITION_OVERLAP", lf, str(a))
            group_of[a] = j
    if kind != "M":
        need(not (set(group_of) & stem), "STEM_GROUP_OVERLAP", obj["stem"][1], str(sorted(set(group_of) & stem)))
        need(set(group_of) | stem == X, "POINT_PARTITION", obj["hlf"], "groups and stem do not partition X")
        need(len(stem) == s, "STEM_SIZE", obj["stem"][1], str(len(stem)))
    zones = [G | stem for G in groups]
    def admissible(t):
        if kind == "S":
            return not any(set(t) <= Z for Z in zones)
        if kind == "D":
            return len({group_of[a] for a in t}) == 3
        return True
    expected_blocks = {"S": 15066, "D": 14580, "M": 16206}[kind]
    need(len(obj["blocks"]) == expected_blocks, "BLOCK_COUNT", obj["blocks_lf"], str(len(obj["blocks"])) + " vs " + str(expected_blocks))
    seen_blocks = set()
    for b, lf in obj["blocks"]:
        need(b not in seen_blocks, "DUPLICATE_BLOCK", lf, str(b))
        if kind == "D":
            need(len({group_of[a] for a in b}) == 4, "BLOCK_TRANSVERSAL", lf, str(b))
        seen_blocks.add(b)
    derived = [set() for _ in range(v)]
    multiplicity = collections.Counter()
    first = {}
    for b, lf in obj["blocks"]:
        for t in itertools.combinations(b, 3):
            need(admissible(t), "GLOBAL_FORBIDDEN_TRIPLE", lf, str(t))
            multiplicity[t] += 1
            need(multiplicity[t] == 1, "GLOBAL_TRIPLE_MULTIPLICITY", lf, str(t) + " occurs " + str(multiplicity[t]) + " times; first block LF " + str(first.get(t)))
            first[t] = lf
        for x in b:
            derived[x].add(tuple(a for a in b if a != x))
    covered = forbidden = total = 0
    for t in itertools.combinations(range(v), 3):
        yes = admissible(t)
        need(multiplicity[t] == int(yes), "GLOBAL_TRIPLE_MULTIPLICITY", obj["blocks_lf"], str(t) + " occurs " + str(multiplicity[t]) + ", expected " + str(int(yes)))
        covered += yes
        forbidden += not yes
        total += 1
    sections = obj["sections"]
    expected_points = X - stem if kind == "S" else X
    ids = [sec["x"] for sec in sections]
    need(len(ids) == len(set(ids)) and set(ids) == expected_points, "POINT_SECTIONS", obj["hlf"], "missing, duplicate, or wrong point section")
    if kind == "M":
        need(ids == list(range(v)), "POINT_SECTION_ORDER", obj["hlf"], "MCDSQS point order")
    stem_ids = [sec["x"] for sec in obj["stem_sections"]]
    need(len(stem_ids) == len(set(stem_ids)) and set(stem_ids) == stem, "STEMPOINT_SECTIONS", obj["hlf"], "missing, duplicate, or wrong stem section")
    profiles = collections.defaultdict(collections.Counter)
    aggregated = collections.defaultdict(collections.Counter)
    hole_counts = collections.Counter()
    pair_stats = collections.defaultdict(collections.Counter)
    label_stats = collections.Counter()
    hole_degree_counts = collections.Counter()
    def profile(category, sec):
        sizes = collections.Counter(len(cl["triples"]) for cl in sec["classes"])
        profiles[category][tuple(sorted(sizes.items()))] += 1
        aggregated[category].update(sizes)
    for sec in sections:
        x, classes = sec["x"], sec["classes"]
        if kind in ("S", "M"):
            need(len(classes) == r and [c["label"] for c in classes] == list(range(r)), "CLASS_SEQUENCE", sec["lf"], "expected 37 nonempty CLASS 0..36 sections")
            partition_classes(sec, derived[x], 819 if kind == "S" else 876)
            domain = X - {x}
            hole = (groups[group_of[x]] | stem) - {x} if kind == "S" else set()
            pairs = pair_design(derived[x], domain, lambda p: not set(p) <= hole, sec)
            pair_stats["group" if kind == "S" else "point"][pairs] += 1
            used_classes = [ppc(cl) for cl in classes]
            if kind == "S":
                avoid = sum(not bool(points & hole) for points in used_classes)
                need(avoid == free, "HOLE_AVOIDING_COUNT", sec["lf"], "point " + str(x) + ": got " + str(avoid) + ", expected " + str(free) + "; every CLASS remains a PPC")
                hole_counts[avoid] += 1
                degree = collections.Counter(a for t in derived[x] for a in t)
                for a in hole:
                    need(degree[a] == 27, "HOLE_POINT_DEGREE", sec["lf"], "hole point " + str(a) + ": " + str(degree[a]))
                    hole_degree_counts[degree[a]] += 1
            profile("group" if kind == "S" else "point", sec)
        else:
            gx = group_of[x]
            domain = X - groups[gx]
            partition_classes(sec, derived[x], 648)
            pairs = pair_design(derived[x], domain, lambda p: group_of[p[0]] != group_of[p[1]], sec, group_of)
            pair_stats["point"][pairs] += 1
            labels = frames(sec, derived[x], domain, groups, gx)
            label_stats[tuple(sorted(labels.values()))] += 1
            profile("point", sec)
    for sec in obj["stem_sections"]:
        x = sec["x"]
        domain = X - stem
        partition_classes(sec, derived[x], 648)
        pairs = pair_design(derived[x], domain, lambda p: group_of[p[0]] != group_of[p[1]], sec, group_of)
        pair_stats["stem"][pairs] += 1
        labels = frames(sec, derived[x], domain, groups)
        label_stats[tuple(sorted(labels.values()))] += 1
        profile("stem", sec)
    report = {
        "result": "VALID", "points": v, "group_sizes": [len(G) for G in groups], "stem": len(stem),
        "distinct_blocks": len(seen_blocks), "all_3_subsets": total, "covered_once": covered, "forbidden_absent": forbidden,
        "point_sections": len(sections), "stem_sections": len(obj["stem_sections"]),
        "derived_counts": counts_json(collections.Counter(len(derived[x]) for x in range(v))),
        "class_size_profiles": {key: [{"sizes_to_classes_per_point": counts_json(dict(pro)), "points": count} for pro, count in sorted(value.items())] for key, value in profiles.items()},
        "aggregate_class_sizes": {key: counts_json(value) for key, value in aggregated.items()},
        "pair_counts_per_point": {key: [{"allowed_once": pro[0], "forbidden_absent": pro[1], "points": count} for pro, count in sorted(value.items())] for key, value in pair_stats.items()},
        "holefree_classes_distribution": counts_json(hole_counts),
        "hole_point_degree_distribution": counts_json(hole_degree_counts),
        "frame_label_count_profiles": [{"classes_per_allowed_label": list(pro), "points": count} for pro, count in sorted(label_stats.items())],
        "syntax": obj["syntax"],
        "LF_anchors": {"header": obj["hlf"], "blocks_marker": obj["blocks_lf"], "first_block": obj["blocks"][0][1], "last_block": obj["blocks"][-1][1], "first_point": sections[0]["lf"], "last_point": sections[-1]["lf"], "first_stempoint": obj["stem_sections"][0]["lf"] if obj["stem_sections"] else None},
    }
    if kind == "M":
        report["chi"] = chi(73)
        report["derived_PPC_capacity"] = 73 // 3
        report["counting_lower_bound"] = (876 + 24 - 1) // 24
    return report
