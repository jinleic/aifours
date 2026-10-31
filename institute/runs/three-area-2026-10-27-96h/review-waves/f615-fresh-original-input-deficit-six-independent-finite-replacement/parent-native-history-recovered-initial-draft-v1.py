#!/usr/bin/env python3
"""F615 prospective finite author checker. NOT RUN by author.

No file/network/process I/O. Prints a JSON receipt on stdout. Indices in the
receipt are 1-based physical positions in each generated original linear word.
"""
import itertools
import json
import sys
import time

START = time.monotonic()
DEADLINE = START + 52.0
PRIMES = (7, 11, 13)
TYPES = ((7,), (6,), (5, 3), (5, 2), (4, 3), (4, 2),
         (3, 3, 3), (3, 3, 2), (3, 2, 2), (2, 2, 2))
DIRECT_BOUNDS = {(5, 2): 3, (4, 3): 2, (4, 2): 2,
                 (3, 3, 3): 3, (3, 3, 2): 3,
                 (3, 2, 2): 2, (2, 2, 2): 3}
PAIRS = ((0, 1), (0, 2), (1, 2))


class CheckError(Exception):
    def __init__(self, reason, detail=""):
        super().__init__(reason + (": " + str(detail) if detail else ""))
        self.reason = reason


def need(ok, reason, detail=""):
    if not ok:
        raise CheckError(reason, detail)


def tick():
    need(time.monotonic() < DEADLINE, "TIME_BOUND", "52-second cooperative cutoff")


def mul(g, h, p):
    x, e = g
    y, b = h
    return ((x + (y if e == 0 else -y)) % p, e ^ b)


def inv(g, p):
    x, e = g
    return ((-x if e == 0 else x) % p, e)


def product(word, indices, p):
    out = (0, 0)
    for i in indices:
        out = mul(out, word[i], p)
    return out


def cyclic_checks(word, selected, p, counts, wrong_equal=False):
    """Check actual cut products against prefix-conjugation, not equality."""
    selected = sorted(selected)
    original = product(word, selected, p)
    prefix = (0, 0)
    at = 0
    for cut in range(len(word)):
        tick()
        while at < len(selected) and selected[at] < cut:
            prefix = mul(prefix, word[selected[at]], p)
            at += 1
        order = selected[at:] + selected[:at]
        actual = product(word, order, p)
        expected = mul(inv(prefix, p), mul(original, prefix, p), p)
        need(actual == expected, "CUT_CONJUGATION", (cut, actual, expected))
        if wrong_equal:
            need(actual == original, "FALSE_CUT_EQUALITY", cut)
        if original == (0, 0):
            need(actual == (0, 0), "IDENTITY_CUT", cut)
        counts["physical_cuts_checked"] += 1
    return original


def parse(word, p):
    n = len(word)
    need(n > 0, "EMPTY_WORD")
    for x, e in word:
        need(0 <= x < p and e in (0, 1), "LETTER_DOMAIN")
    refs = [i for i, (_, e) in enumerate(word) if e == 1]
    need(bool(refs), "NO_REFLECTIONS")
    gaps = {}
    for j, pos in enumerate(refs):
        nxt = refs[(j + 1) % len(refs)]
        between = []
        i = (pos + 1) % n
        while i != nxt:
            need(word[i][1] == 0, "GAP_NONROTATION")
            between.append(i)
            i = (i + 1) % n
        need(len(between) <= 1, "SINGLETON_GAP", (pos, nxt, between))
        gaps[pos] = between[0] if between else None
    return refs, gaps


def runs(word, refs):
    n = len(refs)
    labels = [word[i][0] for i in refs]
    starts = [i for i in range(n) if labels[i] != labels[(i - 1) % n]]
    need(bool(starts), "CONSTANT_PROJECTION")
    out = []
    for j, start in enumerate(starts):
        end = starts[(j + 1) % len(starts)]
        length = (end - start) % n
        if length == 0:
            length = n
        out.append(tuple(refs[(start + k) % n] for k in range(length)))
    return out


def actual_pair_products(word, triple, rotation, p):
    n = len(word)
    values = []
    for i, j in PAIRS:
        positions = [triple[i], triple[j]]
        if rotation is not None:
            positions.append(rotation)
        positions.sort(key=lambda x: (x - triple[0]) % n)
        value = product(word, positions, p)
        need(value[1] == 0, "PAIR_PARITY")
        values.append(value[0])
    return tuple(values)


def check_local(word, triple, rotation, slot, p, mutation=None):
    a, b, c = (word[i][0] for i in triple)
    actual = actual_pair_products(word, triple, rotation, p)
    if rotation is None:
        predicted = ((a - b) % p, (a - c) % p, (b - c) % p)
        reason = "LOCAL_NO_ROTATION"
    else:
        u = word[rotation][0]
        if slot == 0:
            predicted = ((a - u - b) % p, (a - u - c) % p,
                         (u + b - c) % p)
            reason = "LOCAL_FIRST_SIGN"
            if mutation == "FIRST_SIGN":
                predicted = ((a + u - b) % p,) + predicted[1:]
        else:
            predicted = ((a - b + u) % p, (a - u - c) % p,
                         (b - u - c) % p)
            reason = "LOCAL_SECOND_SIGN"
            if mutation == "SECOND_SIGN":
                predicted = ((a - b - u) % p,) + predicted[1:]
    need(actual == predicted, reason, (actual, predicted))
    return actual


def check_safe_predicate(a, b, c, slot, p, swapped=False):
    """Derive safety from actual ordered products for every u in F_p."""
    sizes = []
    for u in range(p):
        if slot == 0:
            w = [(a, 1), (u, 0), (b, 1), (c, 1)]
            tri, r = (0, 2, 3), 1
        else:
            w = [(a, 1), (b, 1), (u, 0), (c, 1)]
            tri, r = (0, 1, 3), 2
        sizes.append(len(set(actual_pair_products(w, tri, r, p))))
    actual_safe = min(sizes) >= 2
    first, second = b != c, a != b
    predicted = ((second if slot == 0 else first) if swapped
                 else (first if slot == 0 else second))
    need(actual_safe == predicted,
         "SAFE_FIRST_PREDICATE" if slot == 0 else "SAFE_SECOND_PREDICATE")


def partition(word, p, refs, gaps, omit_index, counts):
    f = len(refs)
    need((f - 1) % 3 == 0, "PARTITION_LENGTH")
    omitted = refs[omit_index]
    remaining = [refs[(omit_index + 1 + j) % f] for j in range(f - 1)]
    triples = [tuple(remaining[j:j + 3]) for j in range(0, f - 1, 3)]
    need(len(set(remaining)) == f - 1 and omitted not in remaining,
         "PARTITION_OCCURRENCES")
    inner, unsafe, B, constant = {}, set(), 0, []
    a0 = []
    for k, tri in enumerate(triples):
        labels = tuple(word[x][0] for x in tri)
        values = check_local(word, tri, None, None, p)
        aset = set(values)
        need(bool(aset), "EMPTY_LOCAL_SET")
        a0.append(aset)
        is_constant = labels[0] == labels[1] == labels[2]
        if is_constant:
            constant.append(k)
        for slot in (0, 1):
            potentially_unsafe = ((labels[1] == labels[2]) if slot == 0
                                  else (labels[0] == labels[1]))
            if not is_constant and potentially_unsafe:
                B += 1
            rot = gaps[tri[slot]]
            if rot is not None:
                need(rot not in inner, "INTERIOR_REUSED")
                inner[rot] = (k, slot)
                got = check_local(word, tri, rot, slot, p)
                counts["actual_local_interfaces"] += 1
                counts["actual_pair_products"] += 3
                if not is_constant and potentially_unsafe:
                    unsafe.add(rot)
                if not is_constant and not potentially_unsafe:
                    need(len(set(got)) >= 2, "SAFE_COLLAPSE")
    allrot = {i for i, (_, e) in enumerate(word) if e == 0}
    boundaries = allrot.difference(inner)
    before = gaps[refs[(omit_index - 1) % f]]
    after = gaps[omitted]
    adjacent = {x for x in (before, after) if x is not None}
    need(adjacent <= boundaries, "BOUNDARY_ROTATION")
    return {"word": word, "p": p, "refs": refs, "gaps": gaps,
            "omitted": omitted, "triples": triples, "inner": inner,
            "unsafe": unsafe, "B": B, "constant": constant, "a0": a0,
            "allrot": allrot, "boundaries": boundaries, "adjacent": adjacent,
            "cut": (omitted + 1) % len(word)}


def check_boundary(part, boundaries):
    need(part["adjacent"] <= boundaries, "BOUNDARY_ROTATION")


def validate_rotations(part, selected, protected):
    need(len(selected) == len(set(selected)), "DUPLICATE_POSITION")
    seen = set()
    for rot in selected:
        need(rot in part["allrot"], "NOT_ROTATION")
        if rot in part["inner"]:
            block, _ = part["inner"][rot]
            need(block not in protected, "PROTECTED_INTERIOR")
            need(rot not in part["unsafe"], "UNSAFE_INTERIOR")
            need(block not in seen, "TWO_INTERIOR_SAME_BLOCK")
            seen.add(block)


def validate_selector(part, selected, protected):
    p, word = part["p"], part["word"]
    need(len(selected) == len(set(selected)), "DUPLICATE_POSITION")
    need(len(selected) == 2 * p, "SELECTOR_LENGTH")
    need(all(0 <= x < len(word) for x in selected), "POSITION_DOMAIN")
    s = set(selected)
    need(part["omitted"] not in s, "OMITTED_REFLECTION")
    rotations = [x for x in selected if word[x][1] == 0]
    need(len(rotations) == 2, "ROTATION_COUNT")
    for tri in part["triples"]:
        need(sum(x in s for x in tri) == 2, "BLOCK_PAIR_COUNT")
    validate_rotations(part, rotations, set(protected))


def sumset(a, b, p):
    return {(x + y) % p for x in a for y in b}


def require_full(a, p):
    need(a == set(range(p)), "NOT_FULL_SUMSET")


def candidates(part):
    p = part["p"]
    constants = set(part["constant"])
    nonconstant = [i for i in range(len(part["triples"])) if i not in constants]
    c = len(constants)
    if c == 0:
        yield ()
    elif c == 1:
        for i in nonconstant:
            if len(part["a0"][i]) == 3:
                yield (i,)
        for i, j in itertools.combinations(nonconstant, 2):
            ti, tj = part["triples"][i], part["triples"][j]
            li = [part["word"][x][0] for x in ti]
            lj = [part["word"][x][0] for x in tj]
            api = li[0] != li[1] and li[1] != li[2] and len(part["a0"][i]) == 2
            apj = lj[0] != lj[1] and lj[1] != lj[2] and len(part["a0"][j]) == 2
            if api and apj and len(sumset(part["a0"][i], part["a0"][j], p)) >= 4:
                yield (i, j)
    elif c == 2:
        for i, j in itertools.combinations(nonconstant, 2):
            if len(sumset(part["a0"][i], part["a0"][j], p)) >= 5:
                yield (i, j)


def certificate(part, dp_last, counts):
    p, word = part["p"], part["word"]
    for protected in candidates(part):
        tick()
        if len(part["allrot"]) - (part["B"] + 2 * len(protected)) < 3:
            continue
        blocked = set(part["unsafe"])
        for k in protected:
            tri = part["triples"][k]
            blocked.update(x for x in (part["gaps"][tri[0]], part["gaps"][tri[1]])
                           if x is not None)
        available = sorted(part["allrot"] - blocked)
        need(len(available) >= 3, "PROTECTED_COST_BOUND")
        chosen = None
        for x, y in itertools.combinations(available, 2):
            ix, iy = part["inner"].get(x), part["inner"].get(y)
            if ix is None or iy is None or ix[0] != iy[0]:
                chosen = (x, y)
                break
        need(chosen is not None, "TWO_ROTATION_AVAILABILITY")
        validate_rotations(part, list(chosen), set(protected))
        boundary_sum = sum(word[x][0] for x in chosen if x in part["boundaries"]) % p
        paths = {0: ()}
        for k, tri in enumerate(part["triples"]):
            interior = [x for x in chosen
                        if x in part["inner"] and part["inner"][x][0] == k]
            need(len(interior) <= 1, "TWO_INTERIOR_SAME_BLOCK")
            rotation = interior[0] if interior else None
            slot = part["inner"][rotation][1] if rotation is not None else None
            vals = check_local(word, tri, rotation, slot, p)
            choices = {}
            for pair, value in zip(PAIRS, vals):
                choices.setdefault(value, (tri[pair[0]], tri[pair[1]]))
            need(bool(choices), "EMPTY_LOCAL_SET")
            if k not in part["constant"]:
                need(len(choices) >= 2, "SAFE_COLLAPSE")
            if k in protected:
                need(rotation is None and set(choices) == part["a0"][k],
                     "PROTECTED_SET_CHANGED")
            new = {}
            for total, path in paths.items():
                for value, pair in choices.items():
                    new.setdefault((total + value) % p, path + (pair,))
            paths = new
        require_full(set(paths), p)
        representative = None
        for total in range(p):
            selected = list(chosen)
            for pair in paths[total]:
                selected.extend(pair)
            validate_selector(part, selected, protected)
            ordered_at_cut = sorted(selected, key=lambda x: (x - part["cut"]) % len(word))
            expected = ((boundary_sum + total) % p, 0)
            need(product(word, ordered_at_cut, p) == expected, "EXTRACTED_PRODUCT")
            original = cyclic_checks(word, selected, p, counts)
            need((dp_last[2][original[1]] >> original[0]) & 1,
                 "DP_MISSES_RECONSTRUCTED_PRODUCT")
            counts["full_sumset_reconstructions"] += 1
            if expected == (0, 0):
                need(original == (0, 0), "ORIGINAL_IDENTITY")
                representative = sorted(selected)
        need(representative is not None, "NO_IDENTITY_EXTRACTION")
        need(dp_last[2][0] == (1 << p) - 1, "DP_TWO_ROTATION_NOT_FULL")
        return {"selected": representative, "part": part,
                "protected": protected, "rotations": chosen,
                "available_count": len(available), "boundary_sum": boundary_sum}
    return None


def roll(bits, delta, p):
    d = delta % p
    if d == 0:
        return bits
    return ((bits << d) | (bits >> (p - d))) & ((1 << p) - 1)


def general_group_dp(word, p):
    """All 2p-subwords by exact rotation count and full dihedral product."""
    kmax = 2 * p
    dp = [[[0, 0] for _ in range(kmax + 1)] for _ in range(kmax + 1)]
    dp[0][0][0] = 1
    for processed, (y, b) in enumerate(word):
        tick()
        addrot = 1 if b == 0 else 0
        for k in range(min(processed, kmax - 1), -1, -1):
            for r in range(k + 1):
                if r + addrot > kmax:
                    continue
                for parity in (0, 1):
                    bits = dp[k][r][parity]
                    if bits:
                        delta = y if parity == 0 else -y
                        dp[k + 1][r + addrot][parity ^ b] |= roll(bits, delta, p)
    return dp[kmax]


def assigned_run_labels(lengths, p, variant, forced):
    m = len(lengths)
    labels = []
    for i in range(m):
        banned = set()
        if i:
            banned.add(labels[-1])
        if i + 1 in forced:
            banned.add(forced[i + 1])
        if i == m - 1:
            banned.add(labels[0])
        if i in forced:
            value = forced[i]
            need(value not in banned, "FORCED_LABEL_ADJACENCY")
        else:
            base = (2 * i + 3 * variant + 1) % p
            value = next((base + j) % p for j in range(p)
                         if (base + j) % p not in banned)
        labels.append(value)
    return [labels[i] for i, length in enumerate(lengths) for _ in range(length)]


def generic_projection(p, typ, variant):
    f = 3 * p - 2
    m = f - sum(length - 1 for length in typ)
    positions = [0] + [(j * m // len(typ)) + variant for j in range(1, len(typ))]
    need(len(set(positions)) == len(typ) and max(positions) < m, "GENERIC_PLACEMENT")
    lengths = [1] * m
    for pos, length in zip(positions, typ):
        lengths[pos] = length
    a = (2 + variant) % p
    forced = {0: a}
    if typ == (5, 3):
        forced[positions[1]] = a if variant else (a + 3) % p
    return assigned_run_labels(lengths, p, variant, forced)


def equal_endpoint_projection(p, r, variant):
    s = p - 4 - r
    u, v = 3 * r + 1, 3 * s + 1
    lengths = [5] + [1] * u + [3] + [1] * v
    labels = assigned_run_labels(lengths, p, variant, {0: 0, u + 1: 0})
    return labels, {"r": r, "s": s, "u": u, "v": v, "a_equals_b": True}


def ap_parameters(p, r):
    s = p - 4 - r
    L, M = 3 * r + 2, 3 * s + 2
    need(M % p != 0, "AP_DENOMINATOR")
    d = 1
    e = (-L * pow(M, -1, p)) % p
    need(e != 0 and e != d and e != (-d) % p, "AP_DIRECTIONS")
    return s, L, M, d, e


def seven_ap_projection(p, r):
    s, L, M, d, e = ap_parameters(p, r)
    y = [0]
    for step in [d] * L + [e] * M:
        y.append((y[-1] + step) % p)
    need(y[-1] == 0 and len(y) == 3 * p - 7, "SEVEN_AP_ENDPOINT")
    return [0] * 7 + y[1:-1], {"r": r, "s": s, "d": d, "e": e}


def five_three_ap_projection(p, r):
    s, L, M, d, e = ap_parameters(p, r)
    first = [(i * d) % p for i in range(L + 1)]
    b = first[-1]
    second = [(b + i * e) % p for i in range(M + 1)]
    need(second[-1] == 0, "FIVE_THREE_AP_ENDPOINT")
    return ([0] * 5 + first[1:-1] + [b] * 3 + second[1:-1],
            {"r": r, "s": s, "u": L - 1, "v": M - 1,
             "a_equals_b": b == 0, "d": d, "e": e})


def make_word(p, projection, variant, wrap):
    f = len(projection)
    step = 1 if variant % 2 == 0 else 2
    selected = [(variant + step * k) % f for k in range(p + 1)]
    need(len(set(selected)) == p + 1, "GAP_PLACEMENT_DUPLICATE")
    chosen = set(selected)
    raw, ref_positions = [], []
    for i, label in enumerate(projection):
        ref_positions.append(len(raw))
        raw.append((label, 1))
        if i in chosen:
            raw.append(((3 * i + 2 * variant + 1) % p, 0))
    offset = ref_positions[1] if wrap else 0
    return raw[offset:] + raw[:offset]


def chain(refs, start, end):
    i = refs.index(start)
    out = [start]
    while out[-1] != end:
        i = (i + 1) % len(refs)
        out.append(refs[i])
        need(len(out) <= len(refs) + 1, "CHAIN_CYCLE")
    return out


def differences(word, positions, p):
    return [(word[positions[i + 1]][0] - word[positions[i]][0]) % p
            for i in range(len(positions) - 1)]


def rich_blocks(part):
    return [i for i, a in enumerate(part["a0"]) if len(a) == 3]


def require_phase_chain(parts, chain_positions):
    observed = {tri for part in parts for tri in part["triples"]}
    expected = {tuple(chain_positions[i:i + 3])
                for i in range(len(chain_positions) - 2)}
    need(expected <= observed, "PHASE_CHAIN_COVERAGE")


def require_certificate(part, dp_last, counts):
    cert = certificate(part, dp_last, counts)
    need(cert is not None, "SOURCE_BRANCH_NO_CERTIFICATE")
    return cert


def zero_identity(word, positions, p, dp_last, counts):
    need(len(positions) == 2 * p and len(set(positions)) == 2 * p,
         "ZERO_BRANCH_LENGTH")
    need(all(word[i][1] == 1 for i in positions), "ZERO_BRANCH_ROTATION")
    need(cyclic_checks(word, positions, p, counts) == (0, 0), "ZERO_BRANCH_PRODUCT")
    need(dp_last[0][0] & 1, "DP_MISSES_ZERO_BRANCH")
    return sorted(positions)


def source_branch(word, p, typ, refs, run_list, parts, dp_last, counts):
    by_omit = {part["omitted"]: part for part in parts}
    if typ in DIRECT_BOUNDS:
        good = [part for part in parts if not part["constant"]
                and part["B"] <= DIRECT_BOUNDS[typ]]
        need(bool(good), "DIRECT_PHASE_MISSING", typ)
        return "direct_nonconstant", require_certificate(good[0], dp_last, counts), None
    if typ == (6,):
        a = next(run for run in run_list if len(run) == 6)
        ps = [by_omit[a[i]] for i in (0, 1, 2)]
        need(all(len(q["constant"]) == 1 and q["B"] <= 1 for q in ps),
             "SIX_PHASE_SHAPE")
        y = chain(refs, a[-1], a[0])
        require_phase_chain(ps, y)
        for q in ps:
            if rich_blocks(q):
                return "six_rich", require_certificate(q, dp_last, counts), None
        ds = differences(word, y, p)
        need(ds and ds[0] != 0 and all(x == ds[0] for x in ds), "SIX_AP_CHAIN")
        need(p == 7 and len(y) >= 2 * p, "SIX_AP_SCOPE")
        selected = zero_identity(word, y[:2 * p], p, dp_last, counts)
        return "six_zero_rotation_ap", None, selected
    if typ == (7,):
        a = next(run for run in run_list if len(run) == 7)
        p2, p3, p4 = (by_omit[a[i]] for i in (1, 2, 3))
        need(len(p2["constant"]) == len(p3["constant"]) == 1 and
             p2["B"] <= 1 and p3["B"] <= 1 and
             len(p4["constant"]) == 2 and p4["B"] == 0, "SEVEN_PHASE_SHAPE")
        y = chain(refs, a[-1], a[0])
        require_phase_chain((p2, p3, p4), y)
        for q in (p2, p3):
            if rich_blocks(q):
                return "seven_one_constant_rich", require_certificate(q, dp_last, counts), None
        rich = rich_blocks(p4)
        if len(rich) >= 2:
            return "seven_two_rich", require_certificate(p4, dp_last, counts), None
        need(len(rich) == 1, "SEVEN_ZERO_RICH_IMPOSSIBLE")
        xset = set(y[1:-1])
        xblocks = [(i, tri) for i, tri in enumerate(p4["triples"]) if set(tri) <= xset]
        j = next((j for j, (i, _) in enumerate(xblocks) if i == rich[0]), None)
        need(j is not None, "SEVEN_RICH_NOT_IN_X")
        r, s = j, len(xblocks) - j - 1
        need(r + s == p - 4, "SEVEN_RS")
        ds = differences(word, y, p)
        L, M = 3 * r + 2, 3 * s + 2
        need(len(ds) == L + M and L > 0 and M > 0, "SEVEN_SEGMENT_LENGTH")
        d, e = ds[0], ds[L]
        need(d != 0 and e != 0 and d != e and e != (-d) % p,
             "SEVEN_DIRECTIONS")
        need(ds == [d] * L + [e] * M and (L * d + M * e) % p == 0,
             "SEVEN_TWO_AP_SEGMENTS")
        T = {(-d) % p, (-e) % p, (-d - e) % p}
        need(p4["a0"][rich[0]] == T, "SEVEN_RICH_SET")
        options = []
        if r:
            options.append({(-d) % p, (-2 * d) % p})
        if s:
            options.append({(-e) % p, (-2 * e) % p})
        need(any(len(sumset(T, D, p)) >= 5 for D in options), "SEVEN_AP_GROWTH")
        cert = require_certificate(p4, dp_last, counts)
        need(rich[0] in cert["protected"], "SEVEN_RICH_NOT_PROTECTED")
        counts["seven_one_rich_r0"] += int(r == 0)
        counts["seven_one_rich_s0"] += int(s == 0)
        return "seven_one_rich_ap_growth", cert, None
    need(typ == (5, 3), "UNKNOWN_TYPE")
    a = next(run for run in run_list if len(run) == 5)
    b = next(run for run in run_list if len(run) == 3)
    c1 = chain(refs, a[-1], b[0])
    c2 = chain(refs, b[-1], a[0])
    u, v = len(c1) - 2, len(c2) - 2
    need(u + v == 3 * p - 10, "FIVE_THREE_LENGTH")
    if u % 3 != 1:
        q = by_omit[a[2]]
        need(not q["constant"] and q["B"] <= 3, "FIVE_THREE_DIRECT_PHASE")
        return "five_three_direct", require_certificate(q, dp_last, counts), None
    need(v % 3 == 1, "FIVE_THREE_RESIDUE")
    counts["five_three_exceptional"] += 1
    if word[a[0]][0] == word[b[0]][0]:
        counts["five_three_exceptional_equal_endpoints"] += 1
    r, s = (u - 1) // 3, (v - 1) // 3
    need(r + s == p - 4, "FIVE_THREE_RS")
    ps = [by_omit[a[i]] for i in (0, 1, 2)]
    need(all(len(q["constant"]) == 1 and q["B"] <= 2 for q in ps),
         "FIVE_THREE_PHASE_SHAPE")
    for q in ps:
        if rich_blocks(q):
            return "five_three_rich", require_certificate(q, dp_last, counts), None
    ds1, ds2 = differences(word, c1, p), differences(word, c2, p)
    d, e = ds1[0], ds2[0]
    need(d != 0 and e != 0 and all(x == d for x in ds1) and
         all(x == e for x in ds2), "FIVE_THREE_AP_CHAINS")
    need(d != e and d != (-e) % p, "FIVE_THREE_DIRECTIONS")
    need(((3 * r + 2) * d + (3 * s + 2) * e) % p == 0,
         "FIVE_THREE_ENDPOINT")
    q = by_omit[b[1]]
    need(len(q["constant"]) == 1 and q["B"] == 0, "FIVE_THREE_B_PHASE")
    cert = require_certificate(q, dp_last, counts)
    need(len(cert["protected"]) == 2, "FIVE_THREE_AP_PROTECTION")
    Dd, De = {(-d) % p, (-2 * d) % p}, {(-e) % p, (-2 * e) % p}
    sets = [q["a0"][i] for i in cert["protected"]]
    need((sets[0] == Dd and sets[1] == De) or
         (sets[0] == De and sets[1] == Dd), "FIVE_THREE_AP_BLOCKS")
    need(len(sumset(Dd, De, p)) == 4, "FIVE_THREE_AP_GROWTH")
    counts["five_three_ap_r0"] += int(r == 0)
    counts["five_three_ap_s0"] += int(s == 0)
    return "five_three_two_ap_directions", cert, None


def field_checks(counts):
    for p in PRIMES:
        for d in range(1, p):
            Dd = {(-d) % p, (-2 * d) % p}
            for e in range(1, p):
                De = {(-e) % p, (-2 * e) % p}
                if d != e and d != (-e) % p:
                    need(len(sumset(Dd, De, p)) == 4, "FIELD_TWO_DIRECTIONS")
                    counts["field_Dd_De"] += 1
                if d != e:
                    T = {(-d) % p, (-e) % p, (-d - e) % p}
                    need(len(T) == 3, "FIELD_RICH_SIZE")
                    fail_d = len(sumset(T, Dd, p)) < 5
                    fail_e = len(sumset(T, De, p)) < 5
                    need(fail_d == (e in ((2 * d) % p, (-d) % p)),
                         "FIELD_RICH_D_EXCEPTION")
                    need(fail_e == (d in ((2 * e) % p, (-e) % p)),
                         "FIELD_RICH_E_EXCEPTION")
                    counts["field_rich_direction_pairs"] += 1


def make_cases(p):
    result = []
    for typ in TYPES:
        for variant in (0, 1):
            result.append(("generic_" + "_".join(map(str, typ)) + "_" + str(variant),
                           typ, generic_projection(p, typ, variant), variant,
                           bool(variant), {"family": "generic", "variant": variant}))
    for r, variant in ((0, 2), (p - 4, 3)):
        projection, extra = equal_endpoint_projection(p, r, variant)
        extra["family"] = "five_three_equal_exception"
        result.append(("five_three_equal_r" + str(r), (5, 3), projection,
                       variant, bool(variant % 2), extra))
        projection, extra = seven_ap_projection(p, r)
        extra["family"] = "seven_one_rich_ap"
        result.append(("seven_ap_r" + str(r), (7,), projection,
                       variant, bool(variant % 2), extra))
        projection, extra = five_three_ap_projection(p, r)
        extra["family"] = "five_three_two_ap"
        result.append(("five_three_ap_r" + str(r), (5, 3), projection,
                       variant, bool(variant % 2), extra))
    if p == 7:
        projection = [0] * 6 + [i % p for i in range(1, 3 * p - 7)]
        result.append(("six_zero_ap_explicit", (6,), projection, 3, True,
                       {"family": "six_zero_ap", "a": 0, "d": 1}))
    return result


def expected_rejection(reason, fn, controls):
    try:
        fn()
    except CheckError as exc:
        need(exc.reason == reason, "CONTROL_WRONG_REASON", (reason, exc.reason))
        controls.append(reason)
        return
    raise CheckError("CONTROL_DID_NOT_REJECT", reason)


def control_cases(sample, counts):
    controls = []
    p = 7
    w1 = [(0, 1), (2, 0), (1, 1), (3, 1)]
    w2 = [(0, 1), (1, 1), (2, 0), (3, 1)]
    check_local(w1, (0, 2, 3), 1, 0, p)
    check_local(w2, (0, 1, 3), 2, 1, p)
    expected_rejection("LOCAL_FIRST_SIGN",
                       lambda: check_local(w1, (0, 2, 3), 1, 0, p, "FIRST_SIGN"), controls)
    expected_rejection("LOCAL_SECOND_SIGN",
                       lambda: check_local(w2, (0, 1, 3), 2, 1, p, "SECOND_SIGN"), controls)
    check_safe_predicate(0, 0, 1, 0, p)
    check_safe_predicate(0, 0, 1, 1, p)
    expected_rejection("SAFE_FIRST_PREDICATE",
                       lambda: check_safe_predicate(0, 0, 1, 0, p, True), controls)
    expected_rejection("SAFE_SECOND_PREDICATE",
                       lambda: check_safe_predicate(0, 0, 1, 1, p, True), controls)
    expected_rejection("SINGLETON_GAP",
                       lambda: parse([(0, 1), (1, 0), (2, 0), (1, 1)], p), controls)
    w = [(1, 0), (0, 1), (2, 0), (1, 1), (2, 1), (3, 1)]
    refs, gaps = parse(w, p)
    part = partition(w, p, refs, gaps, 0, counts)
    need(len(part["adjacent"]) == 2, "CONTROL_BOUNDARY_SETUP")
    check_boundary(part, part["boundaries"])
    expected_rejection("BOUNDARY_ROTATION", lambda: check_boundary(part, set()), controls)
    w = [(0, 1), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1)]
    refs, gaps = parse(w, p)
    part = partition(w, p, refs, gaps, 0, counts)
    expected_rejection("TWO_INTERIOR_SAME_BLOCK",
                       lambda: validate_rotations(part, [2, 4], set()), controls)
    expected_rejection("PROTECTED_INTERIOR",
                       lambda: validate_rotations(part, [2], {0}), controls)
    w = [(3, 1), (0, 1), (0, 1), (2, 0), (1, 1)]
    refs, gaps = parse(w, p)
    part = partition(w, p, refs, gaps, 0, counts)
    expected_rejection("UNSAFE_INTERIOR",
                       lambda: validate_rotations(part, [3], set()), controls)
    part = sample["part"]
    selected = sample["selected"]
    expected_rejection("DUPLICATE_POSITION",
                       lambda: validate_selector(part, selected[:-1] + [selected[0]],
                                                 sample["protected"]), controls)
    s = set(selected)
    first, second = part["triples"][:2]
    remove = next(i for i in first if i in s)
    add = next(i for i in second if i not in s)
    bad = [i for i in selected if i != remove] + [add]
    expected_rejection("BLOCK_PAIR_COUNT",
                       lambda: validate_selector(part, bad, sample["protected"]), controls)
    expected_rejection("NOT_FULL_SUMSET", lambda: require_full(set(range(p)) - {0}, p), controls)
    identity_word = [(0, 1)] * (2 * p)
    need(product(identity_word, range(2 * p), p) == (0, 0), "CONTROL_IDENTITY_SETUP")
    bad_word = list(identity_word)
    bad_word[0] = (1, 1)
    def check_identity():
        need(product(bad_word, range(2 * p), p) == (0, 0), "WRONG_PRODUCT")
    expected_rejection("WRONG_PRODUCT", check_identity, controls)
    nonidentity = [(0, 1), (1, 0)]
    cyclic_checks(nonidentity, [0, 1], p, counts)
    expected_rejection("FALSE_CUT_EQUALITY",
                       lambda: cyclic_checks(nonidentity, [0, 1], p, counts, True), controls)
    expected_rejection("INCOMPLETE_TYPE_COVERAGE",
                       lambda: need(set(TYPES[:-1]) == set(TYPES), "INCOMPLETE_TYPE_COVERAGE"),
                       controls)
    return controls


def main():
    counts = {"physical_cuts_checked": 0, "actual_local_interfaces": 0,
              "actual_pair_products": 0, "full_sumset_reconstructions": 0,
              "field_Dd_De": 0, "field_rich_direction_pairs": 0,
              "seven_one_rich_r0": 0, "seven_one_rich_s0": 0,
              "five_three_exceptional": 0, "five_three_exceptional_equal_endpoints": 0,
              "five_three_ap_r0": 0, "five_three_ap_s0": 0}
    field_checks(counts)
    rows, coverage, sample = [], {}, None
    for p in PRIMES:
        for name, typ, projection, variant, wrap, extra in make_cases(p):
            tick()
            word = make_word(p, projection, variant, wrap)
            refs, gaps = parse(word, p)
            need(len(refs) == 3 * p - 2, "WORD_F")
            need(sum(e == 0 for _, e in word) == p + 1, "WORD_R")
            rr = runs(word, refs)
            got_type = tuple(sorted((len(r) for r in rr if len(r) > 1), reverse=True))
            need(got_type == typ, "RUN_TYPE", (typ, got_type))
            odd = sum(len(r) % 2 for r in rr)
            need(odd == 3 * p - 8, "DEFICIT_SIX")
            if wrap:
                need(word[refs[0]][0] == word[refs[-1]][0], "WRAP_NOT_EXERCISED")
            parts = [partition(word, p, refs, gaps, i, counts) for i in range(len(refs))]
            seen = {tri for part in parts for tri in part["triples"]}
            expected = {tuple(refs[(i + j) % len(refs)] for j in range(3))
                        for i in range(len(refs))}
            need(seen == expected, "ALL_PHASE_PHYSICAL_COVERAGE")
            dp_last = general_group_dp(word, p)
            branch, cert, zero = source_branch(word, p, typ, refs, rr, parts, dp_last, counts)
            if extra["family"] == "seven_one_rich_ap":
                need(branch == "seven_one_rich_ap_growth", "SEVEN_SPECIAL_BRANCH")
            if extra["family"] == "five_three_two_ap":
                need(branch == "five_three_two_ap_directions", "FIVE_THREE_SPECIAL_BRANCH")
            if extra["family"] == "six_zero_ap":
                need(branch == "six_zero_rotation_ap", "SIX_SPECIAL_BRANCH")
            if extra["family"] == "five_three_equal_exception":
                need(branch == "five_three_rich", "EQUAL_EXCEPTION_BRANCH")
            row = {"name": name, "p": p, "type": list(typ), "variant": variant,
                   "wrap": wrap, "parameters": extra,
                   "word": [["s" if e else "r", x] for x, e in word],
                   "all_omissions": len(parts), "physical_triple_starts": len(seen),
                   "branch": branch,
                   "dp_identity_rotation_counts": [r for r in range(2 * p + 1)
                                                   if dp_last[r][0] & 1],
                   "dp_two_rotation_exponents": [x for x in range(p)
                                                  if (dp_last[2][0] >> x) & 1]}
            if cert is not None:
                if sample is None:
                    sample = cert
                part = cert["part"]
                row.update({"omitted_position": part["omitted"] + 1,
                            "unsafe_gap_bound_B": part["B"],
                            "protected_cost_B_plus_2h": part["B"] + 2 * len(cert["protected"]),
                            "available_rotation_occurrences": cert["available_count"],
                            "protected_physical_triples": [[x + 1 for x in part["triples"][i]]
                                                           for i in cert["protected"]],
                            "selected_rotation_positions": [x + 1 for x in cert["rotations"]],
                            "identity_positions": [x + 1 for x in cert["selected"]],
                            "sumset_reconstructed": list(range(p))})
            else:
                row["identity_positions"] = [x + 1 for x in zero]
                row["zero_rotation_branch_only"] = True
                row["no_claim_two_rotations_impossible"] = True
            rows.append(row)
            coverage.setdefault((p, typ), []).append(extra)
    need(sample is not None, "NO_CERTIFICATE_SAMPLE")
    for p in PRIMES:
        for typ in TYPES:
            records = coverage.get((p, typ), [])
            generic = {x["variant"] for x in records if x["family"] == "generic"}
            need(generic == {0, 1}, "INCOMPLETE_TYPE_COVERAGE", (p, typ))
    for name in ("seven_one_rich_r0", "seven_one_rich_s0", "five_three_ap_r0",
                 "five_three_ap_s0", "five_three_exceptional_equal_endpoints"):
        need(counts[name] >= len(PRIMES), "MISSING_EXCEPTION_COVERAGE", name)
    controls = control_cases(sample, counts)
    tick()
    return {"status": "PASS", "scope": "finite selected words only; no all-prime proof",
            "elapsed_seconds": round(time.monotonic() - START, 6),
            "primes": list(PRIMES), "counts": counts, "negative_controls": controls,
            "cases": rows,
            "binary_p7_scan": "NOT RUN: optional 2^19 scan not included in bounded source",
            "novelty_family_human_kernel_global_claim": False}


if __name__ == "__main__":
    try:
        print(json.dumps(main(), sort_keys=True))
    except CheckError as exc:
        print(json.dumps({"status": "FAIL_OR_TIMEOUT", "reason": exc.reason,
                          "detail": str(exc),
                          "elapsed_seconds": round(time.monotonic() - START, 6)},
                         sort_keys=True))
        sys.exit(1)
