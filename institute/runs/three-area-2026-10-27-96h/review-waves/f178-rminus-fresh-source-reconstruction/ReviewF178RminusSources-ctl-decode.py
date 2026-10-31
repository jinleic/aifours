#!/usr/bin/env python3
"""ReviewF178RminusSources control 3: independent semantic decoding of every v12c row, availability audit,
and a decoding-consistency identity check (same-harness; not the separate exact-arithmetic slice).

Row semantics are reconstructed by this reviewer from the publisher Theorem 5.2 text, the bundle Section 2 prose
and the certificate's own 'convention' string; no author checker/producer/receipt is read.
Exit 0 iff every positive case holds and every mutation fails for its stated reason.
"""
import collections, hashlib, itertools, json, pathlib, re, sys, time
from fractions import Fraction as F

W = pathlib.Path(__file__).resolve().parent
CERT = W / "parent-input-certificate-v12c.json"
PIN = "6d5dc5c62833243db23870bcc34f3869149bd48e13843bee4ca977cd04eca886"
out = {"control": "decode", "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "cases": []}
ok_all = True


def case(name, expected, actual, reason):
    global ok_all
    passed = expected == actual
    ok_all &= passed
    out["cases"].append({"case": name, "expected": expected, "actual": actual, "as_expected": passed, "reason": reason})


def strict_load(b):
    def hook(pairs):
        ks = [k for k, _ in pairs]
        if len(ks) != len(set(ks)): raise ValueError("duplicate key")
        return dict(pairs)
    def const(c): raise ValueError("non-finite constant " + c)
    return json.loads(b.decode("utf-8"), object_pairs_hook=hook, parse_constant=const)


raw = CERT.read_bytes()
case("certificate SHA-256 pin", PIN, hashlib.sha256(raw).hexdigest(), "byte pin from manifest")
cert = strict_load(raw)
mut = raw.replace(b'"multiplier": "-417/2996"', b'"multiplier": "-417/2996", "multiplier": "0"', 1)
try:
    strict_load(mut); dup_rejected = False
except ValueError:
    dup_rejected = True
case("MUTATION duplicate 'multiplier' key is accepted", False, (not dup_rejected) or mut == raw, "strict parser rejects duplicate keys")

BASE = list("abcdefghij"); n2 = {i + 1: BASE[i] for i in range(10)}; a2 = {v: k for k, v in n2.items()}
NB = {1: [2, 3, 4, 5, 6, 7], 2: [1, 3, 7, 9, 10], 3: [1, 2, 4, 8, 9], 4: [1, 3, 5, 8, 10], 5: [1, 4, 6, 9, 10],
      6: [1, 5, 7, 8, 9], 7: [1, 2, 6, 8, 10], 8: [3, 4, 6, 7, 9, 10], 9: [2, 3, 5, 6, 8], 10: [2, 4, 5, 7, 8]}
GEN = {0: {i + 1: x for i, x in enumerate([8, 10, 7, 6, 9, 3, 4, 1, 2, 5])},
       1: {i + 1: x for i, x in enumerate([1, 5, 6, 7, 2, 3, 4, 8, 9, 10])}}
# Publisher Theorem 5.2 item 1, transcribed by this reviewer (layout lines 939-948); a..j = X1..X10.
PUB = {
    ("b'0",): dict(old=["b"], over=list("adefghij"), before=BASE, vars=BASE + ["b'0"]),
    ("d'1", "e'1"): dict(old=["d", "e"], over=list("abcfghi"), before=BASE, vars=BASE + ["d'1", "e'1", "g'2"]),
    ("g'2",): dict(old=["g"], over=["a", "b", "c", "d", "e'1", "f", "h", "i"], before=BASE + ["d'1", "e'1"], vars=BASE + ["d'1", "e'1", "g'2"]),
    ("f'3", "g'3"): dict(old=["f", "g"], over=list("abcdehij"), before=BASE, vars=BASE + ["f'3", "g'3", "h'4"]),
    ("h'4",): dict(old=["h"], over=["a", "b", "c", "d", "e", "f", "f'3", "i", "j"], before=BASE + ["f'3", "g'3"], vars=BASE + ["f'3", "g'3", "h'4"]),
}
XS = cert["extra_single_copies"]; PR = cert["programs"]
BRANCH_SETS = {tuple(BASE)} | {tuple(p["vars"]) for p in PUB.values()} | {tuple(BASE + [f"s'{k}"]) for k in range(len(XS))} \
    | {tuple(BASE + [f"m{k}.c{j}" for j in range(len(p["steps"]))]) for k, p in enumerate(PR)}


def prog_struct(PR):
    errs = []
    for k, p in enumerate(PR):
        for s, st in enumerate(p["steps"]):
            for e in st["copy"] + st["over"]:
                if isinstance(e, list): errs.append((k, s, "atomic-tuple-entry", e))
                elif isinstance(e, str):
                    mm = re.fullmatch(r"c(\d+)", e)
                    if not mm: errs.append((k, s, "unknown-entry", e))
                    elif int(mm.group(1)) >= s: errs.append((k, s, "over-references-future-copy", e))
                elif not (isinstance(e, int) and 1 <= e <= 10): errs.append((k, s, "bad-int", e))
            if set(map(str, st["copy"])) & set(map(str, st["over"])): errs.append((k, s, "copied-entry-in-over", st["copy"]))
            if len(set(map(str, st["over"]))) != len(st["over"]): errs.append((k, s, "repeated-over", st["over"]))
    for k, (S, T) in enumerate(XS):
        if set(S) & set(T) or not all(isinstance(x, int) and 1 <= x <= 10 for x in S + T): errs.append(("x", k, "bad-extra", S, T))
    return errs


case("program/extra-copy structure: no atomic tuples, no forward refs, copied entry not in over", [], prog_struct(PR), "index availability")
PRm = json.loads(json.dumps(PR)); PRm[0]["steps"][0]["copy"] = [[2, 3]]
case("MUTATION atomic tuple entry passes structure audit", False, prog_struct(PRm) == [], "audit detects list-valued (atomic) entries")
PRm = json.loads(json.dumps(PR)); PRm[0]["steps"][1]["over"] = PRm[0]["steps"][1]["over"] + ["c1"]
case("MUTATION over-set referencing a not-yet-created copy passes", False, prog_struct(PRm) == [], "forward reference")


def I(A, B, Z):
    A, B, Z = set(A), set(B), set(Z)
    return [(1, A | Z), (1, B | Z), (-1, A | B | Z), (-1, Z)]


def mk(terms):
    e = collections.defaultdict(F)
    for c, s in terms:
        if s: e[frozenset(s)] += F(c)
    return {k: v for k, v in e.items() if v}


def bits(mask, L, iss, r):
    if mask < 0 or mask >= (1 << len(L)): iss.append(("mask-range", r))
    return [L[k] for k in range(len(L)) if mask >> k & 1]


def decode(rows, conv=None):
    conv = conv or {}
    iss, dec = [], []
    for m in rows:
        r, w, t = m["row"], F(m["multiplier"]), m["row"][0]
        if t == "mono":
            L, i = r[1], r[2]
            if tuple(L) not in BRANCH_SETS: iss.append(("varlist-not-a-branch", r))
            ex, kind, bv = mk([(1, L), (-1, [x for x in L if x != L[i]])]), "ge", L
        elif t == "cmi":
            L, i, j, K = r[1], r[2], r[3], r[4]
            if tuple(L) not in BRANCH_SETS: iss.append(("varlist-not-a-branch", r))
            Ks = bits(K, L, iss, r)
            if not (0 <= i < j < len(L)) or L[i] in Ks or L[j] in Ks: iss.append(("cmi-not-elemental", r))
            ex, kind, bv = mk(I([L[i]], [L[j]], Ks)), "ge", L
        elif t == "fd":
            v = r[1]; Nv = [n2[u] for u in conv.get("NB", NB)[v]]
            ex, kind, bv = mk([(1, Nv + [n2[v]]), (-1, Nv)]), "eq", BASE
        elif t == "cap":
            ex, kind, bv = mk([(1, [n2[r[1]]])]), "cap", BASE
        elif t == "sym":
            g = conv.get("GEN", GEN)[r[1]]; S = bits(r[2], BASE, iss, r)
            ex, kind, bv = mk([(1, S), (-1, [n2[g[a2[x]]] for x in S])]), "eq", BASE
        elif t == "copy":
            st = tuple(r[1]); P = PUB[st]; Q, U = r[2], r[3]; L = P["vars"]
            Us = bits(U, L, iss, r); Qi = [k for k in range(len(st)) if Q >> k & 1]
            if not 0 < Q < (1 << len(st)): iss.append(("Q-range", r))
            if not set(Us) <= set(P["over"]): iss.append(("copy-U-not-in-over", r))
            ex, kind, bv = mk([(1, Us + [st[k] for k in Qi]), (-1, Us + [P["old"][k] for k in Qi])]), "eq", L
        elif t == "independence":
            st = tuple(r[1]); P = PUB[st]; E = conv.get("E", {}).get(st, P["before"])
            if not set(E) <= set(P["before"]): iss.append(("independence-E-contains-later-variable", r))
            ex, kind, bv = mk([(-c, s) for c, s in I(list(st), [x for x in E if x not in P["over"]], P["over"])]), "eq", P["vars"]
        elif t == "xcopy":
            k, U = r[1], r[2]; S, T = XS[k]; L = BASE + [f"s'{k}"]; Us = bits(U, L, iss, r)
            if not set(Us) <= {n2[x] for x in T}: iss.append(("xcopy-U-not-in-over", r))
            ex, kind, bv = mk([(1, Us + [f"s'{k}"]), (-1, Us + [n2[S[0]]])]), "eq", L
        elif t == "xindependence":
            k = r[1]; S, T = XS[k]; Tn = [n2[x] for x in T]
            ex, kind, bv = mk([(-c, s) for c, s in I([f"s'{k}"], [x for x in BASE if x not in Tn], Tn)]), "eq", BASE + [f"s'{k}"]
        elif t in ("mcopy", "mindependence"):
            k = int(r[1][1:]); s = r[2]; st = PR[k]["steps"][s]; L = BASE + [f"m{k}.c{j}" for j in range(len(PR[k]["steps"]))]
            nm = lambda e: n2[e] if isinstance(e, int) else f"m{k}.{e}"
            over = [nm(e) for e in st["over"]]; ent = [nm(e) for e in st["copy"]]; new = [f"m{k}.c{s}"]
            if t == "mcopy":
                Q, U = r[3], r[4]; Us = bits(U, L, iss, r)
                if Q != 1 or len(ent) != 1: iss.append(("mcopy-Q", r))
                if not set(Us) <= set(over): iss.append(("mcopy-U-not-in-over", r))
                ex = mk([(1, Us + new), (-1, Us + ent)])
            else:
                before = L[:10 + s]
                ex = mk([(-c, q) for c, q in I(new, [x for x in before if x not in over], over)])
            kind, bv = "eq", L
        elif t == "dfz":
            co = conv.get("DFZ", r[1]); A, B, C, D, Z = [bits(x, BASE, iss, r) for x in r[2:7]]
            a, b, c, d, e, f, g, h, i = co
            terms = []
            for coef, (X1, X2, Y) in [(b, (A, B, C)), (c, (A, C, B)), (d, (B, C, A)), (e, (A, B, D)), (f, (A, D, B)),
                                      (g, (B, D, A)), (h, (C, D, [])), (i, (C, D, A))]:
                terms += [(coef * cc, q) for cc, q in I(X1, X2, list(Y) + Z)]
            terms += [(-a * cc, q) for cc, q in I(A, B, Z)]
            blocks = [set(A), set(B), set(C), set(D), set(Z)]
            if any(blocks[x] & blocks[y] for x in range(5) for y in range(x + 1, 5)) or not all(blocks[:4]): iss.append(("dfz-blocks", r))
            ex, kind, bv = mk(terms), "ge", BASE
        else:
            iss.append(("unknown-type", r)); continue
        if any(not k <= set(bv) for k in ex): iss.append(("coordinate-outside-own-branch", r))
        if (kind == "ge" and w > 0) or (kind == "cap" and w < 0): iss.append(("sign", r))
        dec.append((t, w, kind, ex))
    return dec, iss


def identity_residual(dec, orient=None):
    orient = orient or {}
    acc = collections.defaultdict(F)
    for t, w, kind, ex in dec:
        s = orient.get(t, 1)
        for k, v in ex.items(): acc[k] += s * w * v
    acc[frozenset(BASE)] -= 1
    return {k: v for k, v in acc.items() if v}


rows = cert["multipliers"]
dec, iss = decode(rows)
case("all rows decoded; zero availability/branch/sign/elemental issues", (len(rows), []), (len(dec), iss), "per-row audit")
case("exact identity sum(w*row) == h(V) under reviewer decoding", {}, {str(sorted(k)): str(v) for k, v in identity_residual(dec).items()}, "decoding-consistency")
eqt = sorted({t for t, _, kind, _ in dec if kind == "eq"})
solutions = []
for sg in itertools.product([1, -1], repeat=len(eqt)):
    if not identity_residual(dec, dict(zip(eqt, sg))): solutions.append(dict(zip(eqt, sg)))
case("orientation of equality types is uniquely pinned by the identity", 1, len(solutions), f"eq types {eqt}")
caps = sum(w for t, w, kind, _ in dec if kind == "cap")
case("bound == sum of cap multipliers == certificate 'bound'", "716/107", str(caps), f"certificate bound field {cert['bound']}")
case("certificate float fields agree with 716/107 to 1e-12", True,
     abs(cert["bound_float"] - 716 / 107) < 1e-12 and abs(cert["float_objective"] - 716 / 107) < 1e-12, "informational only")
used = collections.Counter()
for m in rows:
    r = m["row"]
    if r[0] in ("mono", "cmi"): used[tuple(r[1])[10:] or ("base",)] += 1
out["branch_row_counts"] = {",".join(k): v for k, v in sorted(used.items())}
out["type_counts"] = dict(collections.Counter(m["row"][0] for m in rows))


def mutated(fn):
    rr = json.loads(json.dumps(rows)); fn(rr); return rr


def first(rr, pred):
    for m in rr:
        if pred(m["row"]): return m
    raise KeyError


def m1(rr):
    m = first(rr, lambda r: r[0] == "copy" and tuple(r[1]) == ("d'1", "e'1")); m["row"][3] |= 1 << 9
d1, i1 = decode(mutated(m1))
case("MUTATION copy row (d'1,e'1) with X10 added to U: flagged", True, any(x[0] == "copy-U-not-in-over" for x in i1), "X10 is the discarded Y of step 1(b)")


def m2(rr):
    m = first(rr, lambda r: r[0] == "mcopy" and r[1] == "m4" and r[2] == 0); m["row"][4] |= 1 << 11
d2, i2 = decode(mutated(m2))
case("MUTATION mcopy m4 step0 with later copy m4.c1 in U: flagged", True, any(x[0] == "mcopy-U-not-in-over" for x in i2), "forward reference")


def m2b(rr):
    m = first(rr, lambda r: r[0] == "copy" and tuple(r[1]) == ("g'2",)); m["row"][3] |= 1 << 10
d2b, i2b = decode(mutated(m2b))
case("MUTATION copy row g'2 with d'1 (a Y-variable of that step) in U: flagged", True, any(x[0] == "copy-U-not-in-over" for x in i2b), "d'1 is in (X4'',X5,X10) of step 1(b)-ii")
d3, i3 = decode(rows, {"E": {("d'1", "e'1"): BASE + ["g'2"]}})
case("MUTATION independence (d'1,e'1) with later g'2 in E: flagged", True, any(x[0] == "independence-E-contains-later-variable" for x in i3), "only earlier variables are independent")
d4, _ = decode(rows, {"GEN": {0: GEN[1], 1: GEN[0]}})
case("MUTATION generator labels swapped: identity holds", False, not identity_residual(d4), "pins convention gen0=g1 (validity unaffected)")
inv = {k: {v: u for u, v in g.items()} for k, g in GEN.items()}
d5, _ = decode(rows, {"GEN": inv})
case("MUTATION g replaced by g^-1: identity holds", False, not identity_residual(d5), "pins h(S)-h(g(S)) direction (validity unaffected)")
d6, _ = decode(rows, {"DFZ": [3, 6, 2, 2, 3, 0, 0, 3, 2]})
case("MUTATION DFZ coefficient b 7->6: identity holds", False, not identity_residual(d6), "exact DFZ tuple 3 7 2 2 3 0 0 3 2 is load-bearing")
d7, _ = decode(rows, {"NB": {**NB, 1: [2, 3, 4, 5, 6]}})
case("MUTATION FD for vertex 1 with N(1) minus 7: identity holds", False, not identity_residual(d7), "FD rows use the full neighbourhood")
d8, _ = decode([m for m in rows if m["row"][0] != "dfz"])
case("MUTATION DFZ row dropped: identity holds", False, not identity_residual(d8), "the one DFZ import is load-bearing")


def m9(rr):
    m = first(rr, lambda r: r[0] == "cmi"); m["multiplier"] = str(-F(m["multiplier"]))
d9, i9 = decode(mutated(m9))
case("MUTATION one cmi multiplier made positive: flagged", True, any(x[0] == "sign" for x in i9), ">=0 rows need nonpositive multipliers")


def m10(rr):
    m = first(rr, lambda r: r[0] == "cap"); m["multiplier"] = str(F(m["multiplier"]) + F(1, 107))
d10, _ = decode(mutated(m10))
case("MUTATION cap multiplier +1/107: identity holds", False, not identity_residual(d10), "cap multipliers fixed by identity")


def m11(rr):
    m = first(rr, lambda r: r[0] == "cmi" and len(r[1]) == 13 and r[1][10] == "d'1"); m["row"][1] = BASE + ["d'1", "e'1", "f'3"]
d11, i11 = decode(mutated(m11))
case("MUTATION cmi row over cross-branch list (d'1,e'1,f'3): flagged", True, any(x[0] == "varlist-not-a-branch" for x in i11), "no cross-branch elemental rows")
# rendering of every decoded row (complete reading of the raw certificate)
lines = []
for (m, (t, w, kind, ex)) in zip(rows, dec):
    terms = " ".join(f"{'+' if v > 0 else '-'}{abs(v) if abs(v) != 1 else ''}h({''.join(sorted(k)) if all(len(x) == 1 for x in k) else ','.join(sorted(k))})"
                     for k, v in sorted(ex.items(), key=lambda kv: (len(kv[0]), sorted(kv[0]))))
    lines.append(f"{json.dumps(m['row'])}\t{m['multiplier']}\t{kind}\t{terms}")
(W / "ReviewF178RminusSources-decoded-rows.tsv").write_text("\n".join(lines) + "\n")
out["decoded_rows_file_sha256"] = hashlib.sha256(("\n".join(lines) + "\n").encode()).hexdigest()
out["finished_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
out["all_as_expected"] = ok_all
(W / "ReviewF178RminusSources-ctl-decode-out.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
print("all_as_expected", ok_all, "cases", len(out["cases"]))
sys.exit(0 if ok_all else 1)
