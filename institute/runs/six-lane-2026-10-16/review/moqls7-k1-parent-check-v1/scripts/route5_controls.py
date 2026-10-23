#!/usr/bin/env python3
"""route5_controls.py (parent moqls7-k1-parent-check-v1): claim section 7 controls.
 (a) replay of the pinned lane checker pattern_check.py as a subprocess; output compared with the lane's
     evidence/k1A/pattern_controls.json;
 (b) own exact spot-checks (no lane code):
     C2: the 4x4 QLS printed in Ball-Simoens section 2.4 (vectors over Q(sqrt2), exact integer arithmetic): rows and
         columns ONBs, supports, F1-F4 on the 2-net (rows, columns), all single-coordinate mutations;
     C1: Psi(f) of Ball-Simoens Def. 11 / Thm 6 / Ex. 15 at q=7, H={1,2,4}, f = f0 - m0 x for each undetermined m0,
         on the 3-net (rows, columns, symbol lines of Phi(m), m in M\{0}). Exact arithmetic in Z[w], w = e^{2 pi i/7}:
         a sum of 7 seventh roots of unity vanishes iff every root occurs once. Checks: Psi(f) is a QLS, Psi(f) is
         orthogonal to Phi(m), supports after the inverse Fourier transform (frame = row 0), F1-F4 + frame lemma,
         non-classical (weight > 1 entries), all single-coordinate mutations;
     C3: every lane model (A and B) passes the own F1-F4 evaluator; C4: all single mutations of the weight-4 pattern."""
import itertools, json, os, sys
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mynet, runlib

D = os.path.dirname(HERE)
LANE = os.path.join(D, "inputs", "lane")
OUT = os.path.join(D, "route5")
env = dict(os.environ, TMPDIR=os.path.join(D, "tmp"))
res = {"started": runlib.now()}

# ---------------- (a) replay ----------------
rp = os.path.join(OUT, "pattern_controls.replay.json")
run = runlib.run(["/usr/bin/python3", "-B", os.path.join(LANE, "code", "pattern_check.py"),
                  os.path.join(LANE, "evidence", "nets7_classes.json"), os.path.join(LANE, "evidence", "k1A", "summary.json"),
                  os.path.join(LANE, "evidence", "k1B", "summaryB.json"), rp], OUT,
                 os.path.join(OUT, "pattern_check.replay.stdout"), os.path.join(OUT, "pattern_check.replay.stderr"), env=env)
run["pinned_checker_sha256"] = runlib.sha_file(os.path.join(LANE, "code", "pattern_check.py"))
lane_pc = os.path.join(LANE, "evidence", "k1A", "pattern_controls.json")
run["replay_output_sha256"] = runlib.sha_file(rp) if os.path.exists(rp) else None
run["lane_output_sha256"] = runlib.sha_file(lane_pc)
run["byte_identical"] = run["replay_output_sha256"] == run["lane_output_sha256"]
R = json.load(open(rp))
run["replay_summary"] = {
    "C1": [(r["m0"], r["m"], r["violations"], r["weights"], r["mutations_rejected"], r["mutations"]) for r in R["C1_psi_f"]],
    "C2": R["C2_4x4"], "C3_all_pass": all(not r["violations"] for r in R["C3_models"]), "C3_count": len(R["C3_models"]),
    "C4": R["C4_weight4_mutations"]}
res["a_replay"] = run


# ---------------- generic evaluator (own) ----------------
def lines_of(net, n):
    k = len(net[0])
    return [[p for p in range(len(net)) if net[p][c] == b] for c in range(k) for b in range(n)]


def violations(lines, supp, n, frame_label, allowed=None):
    bad = set()
    for p, k in frame_label.items():
        if supp[p] != {k}:
            bad.add("frame")
    for p, S in supp.items():
        if not S:
            bad.add("F1")
        if allowed is not None and not S <= allowed[p]:
            bad.add("allowed")
    for l in lines:
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                if len(supp[l[i]] & supp[l[j]]) == 1:
                    bad.add("F2")
        for k in range(n):
            cov = [p for p in l if k in supp[p]]
            if not cov:
                bad.add("F3")
            elif len(cov) == 1 and len(supp[cov[0]]) != 1:
                bad.add("F4")
    return sorted(bad)


def mutation_counts(lines, supp, n, frame_label, allowed):
    tot = rejF = rejFA = 0
    for p in sorted(supp):
        if p in frame_label:
            continue
        for k in range(n):
            T = dict(supp)
            T[p] = set(supp[p]) ^ {k}
            tot += 1
            v1 = violations(lines, T, n, frame_label)          # frame + F1-F4 only
            v2 = violations(lines, T, n, frame_label, allowed)  # + allowed (frame lemma)
            rejF += bool(v1)
            rejFA += bool(v2)
    return {"mutations": tot, "rejected_F1F4_frame_only": rejF, "rejected_with_allowed": rejFA}


# ---------------- C2 ----------------
# printed square (Ball-Simoens LF126-131), basis |1>..|4> -> 0..3; entry = (e, integer vector) meaning (1/sqrt2)^e * vec
e1 = lambda k: (0, tuple(1 if t == k else 0 for t in range(4)))
plus, minus = (1, (1, 1, 0, 0)), (1, (1, -1, 0, 0))
Q = [[e1(0), e1(1), e1(2), e1(3)],
     [e1(1), e1(0), e1(3), e1(2)],
     [e1(2), e1(3), plus, minus],
     [e1(3), e1(2), minus, plus]]
def ip(u, v):
    return Fraction(sum(a * b for a, b in zip(u[1], v[1])), 1) / (2 ** Fraction(u[0] + v[0], 2) if (u[0] + v[0]) % 2 == 0 else 1)
def ip_exact(u, v):
    s = sum(a * b for a, b in zip(u[1], v[1]))
    tot = u[0] + v[0]
    assert tot % 2 == 0 or s == 0
    return Fraction(s, 2 ** (tot // 2)) if tot % 2 == 0 else Fraction(0)
onb = True
for i in range(4):
    for a in range(4):
        for b in range(4):
            want = Fraction(1 if a == b else 0)
            onb &= ip_exact(Q[i][a], Q[i][b]) == want and ip_exact(Q[a][i], Q[b][i]) == want
supp2 = {4 * i + j: {k for k in range(4) if Q[i][j][1][k] != 0} for i in range(4) for j in range(4)}
net2 = [(i, j) for i in range(4) for j in range(4)]
L2 = lines_of(net2, 4)
fl2 = {j: j for j in range(4)}
res["C2_own"] = {"rows_cols_orthonormal_exact": onb, "supports": {str(p): sorted(s) for p, s in supp2.items()},
                 "violations": violations(L2, supp2, 4, fl2), "weights": sorted({len(s) for s in supp2.values()}),
                 "mutations": mutation_counts(L2, supp2, 4, fl2, None)}
res["C2_own"]["supports_equal_lane_hardcoded"] = [[supp2[4 * i + j] for j in range(4)] for i in range(4)] == \
    [[{0}, {1}, {2}, {3}], [{1}, {0}, {3}, {2}], [{2}, {3}, {0, 1}, {0, 1}], [{3}, {2}, {0, 1}, {0, 1}]]

# ---------------- C1 ----------------
q = 7
H = {1, 2, 4}
f0 = [x if x in H else 0 for x in range(q)]
isperm = lambda g: sorted(g) == list(range(q))
M0 = [m for m in range(q) if isperm([(f0[x] - m * x) % q for x in range(q)])]
def vanish(exps):            # (1/7) sum_x w^{exps[x]} == 0 exactly iff each residue occurs once
    return sorted(e % q for e in exps) == list(range(q))
c1 = {"M0_undetermined_directions": M0, "cases": []}
for m0 in M0:
    f = [(f0[x] - m0 * x) % q for x in range(q)]
    M = sorted((m - m0) % q for m in M0)
    case = {"m0": m0, "f": f, "f_is_perm": isperm(f), "M": M, "per_m": []}
    # psi_ij(x) = (1/sqrt7) w^{i f(x) + j x}; <psi_ij, psi_kl> = (1/7) sum_x w^{(k-i) f(x) + (l-j) x}
    def inner_zero(i, j, k, l):
        return vanish([(k - i) * f[x] + (l - j) * x for x in range(q)])
    qls = all(inner_zero(i, j, i, l) for i in range(q) for j in range(q) for l in range(q) if l != j) and \
          all(inner_zero(i, j, k, j) for i in range(q) for j in range(q) for k in range(q) if k != i)
    case["Psi_f_rows_cols_orthogonal_exact"] = qls          # norms are 1 trivially: (1/7)*7
    # supports after inverse Fourier: coeff at y = (1/7) sum_x w^{i f(x) + (j-y) x}
    supp = {q * i + j: {y for y in range(q) if not vanish([i * f[x] + (j - y) * x for x in range(q)])}
            for i in range(q) for j in range(q)}
    for m in [m for m in M if m != 0]:
        net = [(i, j, (m * i + j) % q) for i in range(q) for j in range(q)]
        orth = all(inner_zero(i, j, k, l) for i in range(q) for j in range(q) for k in range(q) for l in range(q)
                   if (i, j) != (k, l) and (m * i + j) % q == (m * k + l) % q)
        fm_perm = isperm([(f[x] - m * x) % q for x in range(q)])
        L = lines_of(net, q)
        fl = {j: j for j in range(q)}
        allowed = {}
        for p in range(q * q):
            if p in fl:
                allowed[p] = {fl[p]}
            else:
                ex = set()
                for c in (1, 2):
                    hit = [r for r in range(q) if net[r][c] == net[p][c]]
                    assert len(hit) == 1
                    ex.add(fl[hit[0]])
                allowed[p] = set(range(q)) - ex
        case["per_m"].append({"m": m, "f_minus_mx_is_perm": fm_perm, "Psi_f_orthogonal_to_Phi_m_exact": orth,
                              "violations": violations(L, supp, q, fl, allowed),
                              "weights": sorted({len(s) for s in supp.values()}),
                              "nonclassical(weight>1 entries present)": any(len(s) > 1 for s in supp.values()),
                              "mutations": mutation_counts(L, supp, q, fl, allowed)})
    c1["cases"].append(case)
res["C1_own"] = c1

# ---------------- C3, C4 ----------------
nets, data = mynet.load_nets(os.path.join(LANE, "evidence", "nets7_classes.json"))
SA = json.load(open(os.path.join(LANE, "evidence", "k1A", "summary.json")))
SB = json.load(open(os.path.join(LANE, "evidence", "k1B", "summaryB.json")))
c3 = []
for i, net in enumerate(nets):
    frame, label, allowed = mynet.frame_allowed(net)
    L = lines_of(net, 7)
    for m in SA["classes"][i]["models"]:
        sp = {p: set() for p in range(49)}
        for t in m:
            p, k = t.split(":")
            sp[int(p)].add(int(k))
        c3.append((i, "A", violations(L, sp, 7, label, {p: set(a) for p, a in allowed.items()})))
    for m in SB["classes"][i]["models"]:
        sp = {int(t.split(":")[0]): {int(c) for c in t.split(":")[1]} for t in m}
        c3.append((i, "B", violations(L, sp, 7, label, {p: set(a) for p, a in allowed.items()})))
res["C3_own"] = {"n_models": len(c3), "all_pass": all(not v for _, _, v in c3), "items": c3}
net = nets[6]
frame, label, allowed = mynet.frame_allowed(net)
w4 = {p: ({label[p]} if p in label else set(allowed[p])) for p in range(49)}
res["C4_own"] = mutation_counts(lines_of(net, 7), w4, 7, label, {p: set(a) for p, a in allowed.items()})

# ---------------- verdict ----------------
ok_c1 = all(c["f_is_perm"] and c["Psi_f_rows_cols_orthogonal_exact"] and all(
    pm["f_minus_mx_is_perm"] and pm["Psi_f_orthogonal_to_Phi_m_exact"] and pm["violations"] == [] and
    pm["weights"] == [1, 5] and pm["mutations"]["mutations"] == 294 and pm["mutations"]["rejected_with_allowed"] == 84
    for pm in c["per_m"]) and len(c["per_m"]) == 1 for c in c1["cases"]) and len(c1["cases"]) == 2
ok_c2 = onb and res["C2_own"]["violations"] == [] and res["C2_own"]["mutations"]["mutations"] == 48 and \
    res["C2_own"]["mutations"]["rejected_F1F4_frame_only"] == 48 and res["C2_own"]["supports_equal_lane_hardcoded"]
ok_c3 = res["C3_own"]["all_pass"] and res["C3_own"]["n_models"] == 18
ok_c4 = res["C4_own"]["mutations"] == 294 and res["C4_own"]["rejected_with_allowed"] == 294
res["own_ok"] = {"C1": ok_c1, "C2": ok_c2, "C3": ok_c3, "C4": ok_c4}
res["replay_ok"] = run["exit"] == 0 and run["byte_identical"]
res["route5_pass"] = res["replay_ok"] and all(res["own_ok"].values())
res["finished"] = runlib.now()
with open(os.path.join(OUT, "route5-controls.json"), "x") as f:
    json.dump(res, f, indent=1, default=lambda s: sorted(s) if isinstance(s, set) else str(s))
print(json.dumps({"replay": [run["exit"], run["byte_identical"], run["replay_summary"]], "own_ok": res["own_ok"],
                  "C1": [(c["m0"], [(pm["m"], pm["violations"], pm["weights"], pm["mutations"]) for pm in c["per_m"]]) for c in c1["cases"]],
                  "C2": [res["C2_own"]["violations"], res["C2_own"]["mutations"]], "C4": res["C4_own"]}, default=str))
print("route5_pass", res["route5_pass"])
