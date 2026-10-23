#!/usr/bin/env python3
"""tmax_route_probe_v9 (ContinueOlson).  FALSIFICATION AID for ROUTE-ALL(T) (scope evidence/TMAX-scope-v1.md
858d9a3e...568f); never a premise.  Stdlib only; stdout only; self-stop at BUDGET_S wall seconds (no external timeout).
(T): p prime, 2 <= k <= p-1, 1 <= kappa <= k-1, 2kappa + k >= 2p; Y = R = 2p + 2kappa - k odd elements of C_(2p) (integers
mod 2p) whose longest zero-sum subsequence has length exactly 2kappa.  ROUTE(Y): some c in Z_p^* has E_c = 0, or
E_c <= 2H (= 2p - 2 - 2kappa) and eta_c + a_max,c <= 2p - 1 - k (SHgen weights relative to c: element a has value
x = a mod p; x = 0 -> |b| = p; else r = x/c mod p in [1, p-1], |b| = r if r odd else p - r; light iff |b| = 1).
Mode EXH (p = 7): all multisets of size R.  Mode NORM: Y = Y' + 1^(n+) + {2p - s : s in N}, Y' = L = 2p - k odd
coefficients with sum W = L + 2d <= 2p - 1 (d = e'/2), n+ + n- = 2kappa, s odd in [1, min(2kappa - 1, 2p - 1 - W)],
S(N) = n+ + 2pj (j >= 0), m + n+ <= 2p - 1 (else 1^(2p) is a zero-sum of length 2p > 2kappa).  Pruned (ROUTE true via
c = 1, by E_1 = 2d + 2n+ - 2kappa <= 2H and KETA arithmetic) unless FULL: j = 0 and d + n+ <= p - 1.
Every surviving candidate: ROUTE check, exact DP of the longest zero-sum length (all j >= 1 forms are DP-checked even
when ROUTE holds, to record unbalanced longest Z).  Canonical form = min over unit multipliers of the sorted list."""
import sys, time, json, itertools
BUDGET_S = 280.0
T0 = time.time()
def left():
    return BUDGET_S - (time.time() - T0)

def units(p):
    n2 = 2 * p
    return [u for u in range(1, n2, 2) if u % p != 0]

def canon(p, ys):
    n2 = 2 * p
    return min(tuple(sorted((u * a) % n2 for a in ys)) for u in units(p))

def maxlen(p, ys):
    n2 = 2 * p
    reach = [0] * n2
    reach[0] = 1
    for a in ys:
        new = reach[:]
        for r in range(n2):
            b = reach[r]
            if b:
                new[(r + a) % n2] |= b << 1
        reach = new
    return reach[0].bit_length() - 1

def route(p, k, kappa, ys):
    twoH = 2 * p - 2 - 2 * kappa
    best = None
    for c in range(1, (p - 1) // 2 + 1):
        ci = pow(c, -1, p)
        E = 0; eta = 0; amax = 0
        for a in ys:
            x = a % p
            if x == 0:
                b = p
            else:
                r = (x * ci) % p
                b = r if r % 2 else p - r
            if b > 1:
                E += b - 1; eta += 1; amax = max(amax, b)
        if best is None or E < best[0]:
            best = (E, c, eta, amax)
        if E == 0 or (E <= twoH and eta + amax <= 2 * p - 1 - k):
            return True, (E, c, eta, amax)
    return False, best

def partitions(d, maxpart=None):
    if maxpart is None:
        maxpart = d
    if d == 0:
        yield []
        return
    for first in range(min(d, maxpart), 0, -1):
        for rest in partitions(d - first, first):
            yield [first] + rest

def multisets_sum(n, S, vals):
    # vals: odd values in decreasing order; yields lists of counts aligned with vals
    if not vals:
        if n == 0 and S == 0:
            yield []
        return
    v = vals[0]
    rest = vals[1:]
    vmin = vals[-1]
    nxt = rest[0] if rest else None
    for c in range(min(n, S // v), -1, -1):
        n2_, S2 = n - c, S - c * v
        if not rest:
            if n2_ == 0 and S2 == 0:
                yield [c]
            continue
        if S2 < n2_ * vmin or S2 > n2_ * nxt:
            continue
        for tail in multisets_sum(n2_, S2, rest):
            yield [c] + tail

def cells(p):
    out = []
    for k in range(2, p):
        for kappa in range(1, k):
            if 2 * kappa + k >= 2 * p:
                out.append((k, kappa))
    return out

def exh_cell(p, k, kappa):
    n2 = 2 * p
    vals = list(range(1, n2, 2))
    R = 2 * p + 2 * kappa - k
    inT = set(); fails = []; done = True; cnt = 0
    for combo in itertools.combinations_with_replacement(vals, R):
        cnt += 1
        if cnt % 5000 == 0 and left() < 30:
            done = False
            break
        if maxlen(p, combo) == 2 * kappa:
            cf = canon(p, combo)
            if cf not in inT:
                inT.add(cf)
                ok, info = route(p, k, kappa, combo)
                if not ok:
                    fails.append([list(cf), info])
    return inT, fails, done, cnt

def norm_cell(p, k, kappa, full):
    n2 = 2 * p
    L = 2 * p - k
    twoH = 2 * p - 2 - 2 * kappa
    seen = set(); inT = set(); fails = []; unbal_inT = []
    stats = {"forms": 0, "distinct": 0, "dp": 0, "route_false_inT": 0, "unbal_forms_inT": 0, "complete": True}
    for d in range(0, (k - 1) // 2 + 1):
        W = L + 2 * d
        if W > n2 - 1:
            break
        slack = n2 - 1 - W
        for part in partitions(d):
            if len(part) > L:
                continue
            Yp = [1 + 2 * x for x in part] + [1] * (L - len(part))
            m = L - len(part)
            smax = min(2 * kappa - 1, slack)
            if smax % 2 == 0:
                smax -= 1
            if smax < 1:
                continue
            vals = list(range(smax, 0, -2))
            for nplus in range(0, 2 * kappa):
                if m + nplus > n2 - 1:
                    break
                nminus = 2 * kappa - nplus
                j = 0
                while True:
                    S = nplus + n2 * j
                    if S > nminus * smax:
                        break
                    if S >= nminus and (full or j >= 1 or d + nplus >= p):
                        for counts in multisets_sum(nminus, S, vals):
                            if left() < 15:
                                stats["complete"] = False
                                return stats, inT, fails, unbal_inT
                            stats["forms"] += 1
                            N = [v for v, c in zip(vals, counts) for _ in range(c)]
                            ys = Yp + [1] * nplus + [n2 - s for s in N]
                            cf = canon(p, ys)
                            key = (cf, j >= 1)
                            if key in seen:
                                continue
                            seen.add(key)
                            ok, info = route(p, k, kappa, ys)
                            if ok and not full and j == 0:
                                continue
                            stats["dp"] += 1
                            if maxlen(p, ys) == 2 * kappa:
                                inT.add(cf)
                                if j >= 1:
                                    stats["unbal_forms_inT"] += 1
                                    if len(unbal_inT) < 10:
                                        unbal_inT.append({"Y_norm": sorted(ys), "Yprime": sorted(Yp), "n_plus": nplus,
                                                          "N": N, "j": j, "route": ok, "best": info})
                                if not ok and cf not in [tuple(f["canon"]) for f in fails]:
                                    fails.append({"canon": list(cf), "Y_norm": sorted(ys), "Yprime": sorted(Yp), "e1": 2 * d,
                                                  "n_plus": nplus, "N": N, "j": j, "best_E_c_eta_amax": info, "twoH": twoH})
                    j += 1
    stats["distinct"] = len(seen)
    return stats, inT, fails, unbal_inT

if __name__ == "__main__":
    print(json.dumps({"start": True, "budget_s": BUDGET_S}), flush=True)
    p = 7
    for (k, kappa) in cells(p):
        inT_e, fails_e, done_e, cnt = exh_cell(p, k, kappa)
        st, inT_n, fails_n, unb = norm_cell(p, k, kappa, True)
        print(json.dumps({"p": p, "k": k, "kappa": kappa, "mode": "EXH+NORMFULL", "exh_multisets": cnt, "exh_complete": done_e,
                          "exh_inT": len(inT_e), "exh_route_false": len(fails_e), "norm_stats": st, "norm_inT": len(inT_n),
                          "sets_equal": inT_e == inT_n, "norm_route_false": len(fails_n), "fails_exh": fails_e[:10],
                          "unbal_inT_examples": unb}), flush=True)
    for p in (11, 13, 17):
        for (k, kappa) in cells(p):
            if left() < 20:
                print(json.dumps({"p": p, "k": k, "kappa": kappa, "skipped_budget": True}), flush=True)
                continue
            st, inT_n, fails_n, unb = norm_cell(p, k, kappa, False)
            print(json.dumps({"p": p, "k": k, "kappa": kappa, "mode": "NORM", "s1_auto": kappa <= (2 * p) // 3,
                              "norm_stats": st, "route_false_inT": len(fails_n), "fails": fails_n[:8],
                              "unbal_inT_examples": unb[:3]}), flush=True)
    print(json.dumps({"done": True, "elapsed_s": round(time.time() - T0, 1)}), flush=True)
