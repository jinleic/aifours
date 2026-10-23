"""Independent cross-check of the census DFS (rstar.phi_solutions, the gam/Lemma-S system) against the
theta-domain enumeration of xcheck.py (Lemma GR's Ach from ../../../code/gr_window.py, applied to every proper
cyclic interval pattern of an explicit realisation).  Random MIX_low d-vectors (seeded), both directions
(including d-vectors with no interval-feasible lift).  Usage: python3 xcheck_run.py p kmax N seed
"""
import sys, random, json, time
import rstar, xcheck


def random_d(p, kmax, rng):
    while True:
        k = rng.randrange(4, kmax + 1)
        g = rng.randrange(1, (k - 2) // 2 + 1)
        Bmax = k - 1 - 2 * g
        if Bmax < 1:
            continue
        B = rng.randrange(1, Bmax + 1)
        D = 2 * p - k + 2 * g
        A = D + B
        if A > 2 * p - 1:
            continue
        # choose numbers: n_A antis, n_P pairs, rest aligned
        nP = rng.randrange(0, min(B, k - 1) + 1)
        Banti = B - nP
        nAnti = 0 if Banti == 0 else rng.randrange(1, min(Banti, k - nP - 1) + 1)
        nAl = k - nP - nAnti
        Aal = A - nP
        if nAl < 1 or Aal < nAl or (Banti > 0 and nAnti == 0) or Banti < nAnti:
            continue
        def comp(total, parts):
            cuts = sorted(rng.sample(range(1, total), parts - 1)) if parts > 1 else []
            b = [0] + cuts + [total]
            return [b[i + 1] - b[i] for i in range(parts)]
        al = comp(Aal, nAl)
        an = comp(Banti, nAnti) if nAnti else []
        d = al + [0] * nP + [-c for c in an]
        rng.shuffle(d)
        if rstar.params(d, p) is None:
            continue
        k2, A2, B2, D2, g2 = rstar.params(d, p)
        if (A2, B2, g2) != (A, B, g):
            continue
        return d


def main():
    p, kmax, N, seed = map(int, sys.argv[1:5])
    rng = random.Random(seed)
    t0 = time.time()
    stats = {"p": p, "kmax": kmax, "N": N, "seed": seed, "dvectors": 0, "with_solutions": 0,
             "solutions": 0, "mismatches": 0}
    for _ in range(N):
        d = random_d(p, kmax, rng)
        S1 = set(rstar.phi_solutions(d, p))
        ths = xcheck.interval_feasible_thetas(d, p)
        S2 = {xcheck.lifts(d, th, p) for th in ths}
        stats["dvectors"] += 1
        stats["with_solutions"] += bool(S1)
        stats["solutions"] += len(S1)
        if S1 != S2:
            stats["mismatches"] += 1
            print("MISMATCH", d, sorted(S1)[:3], sorted(S2)[:3], flush=True)
    stats["seconds"] = round(time.time() - t0, 1)
    print(json.dumps(stats), flush=True)


if __name__ == "__main__":
    main()
