"""P2 of invstar/README.md: Lemma GR0 (Lemma GR with EMPTY rotation runs) versus the raw ordered-product DP.
Random words over D_(2p) with rotations in {rho_1, rho_-1} and constant reflection blocks separated by rotation runs
that may be empty; criterion = ../../../../code/gr_window.py criterion (unchanged), DP = ../../../../code/was_verify.py
dp_has (unchanged; independent of gr_window).  Usage: python3 gr0_check.py SEED NPER
"""
import sys, os, random, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "..", "code"))
import gr_window as grw      # noqa: E402
import was_verify as wv      # noqa: E402


def word(a, b, l, y, p, rng):
    w = []
    for i in range(len(a)):
        rot = [("R", 1)] * a[i] + [("R", p - 1)] * b[i]
        rng.shuffle(rot)
        w += rot + [("F", y[i] % p)] * l[i]
    return w


def rand_case(p, N, rng):
    while True:
        k = rng.randrange(1, 8)
        if 2 * k > N + k:      # blocks need >= 1 letter each
            continue
        l = [1] * k
        r = [0] * k
        for _ in range(N - k):
            if rng.random() < 0.5:
                l[rng.randrange(k)] += 1
            else:
                r[rng.randrange(k)] += 1
        if rng.random() < 0.8:          # force at least one empty rotation run most of the time
            i = rng.randrange(k)
            l[(i + 1) % k] += r[i]
            r[i] = 0
        a = [rng.randrange(0, ri + 1) for ri in r]
        b = [ri - ai for ri, ai in zip(r, a)]
        y = [rng.randrange(p) for _ in range(k)]
        if rng.random() < 0.7:          # maximal blocks: distinct values across empty runs
            for i in range(k):
                if r[i] == 0 and k > 1 and y[i - 1] == y[i]:
                    y[i] = (y[i] + 1 + rng.randrange(p - 1)) % p
        return a, b, l, y


def main():
    seed, nper = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    out = {"seed": seed}
    for p in (5, 7):
        for N in (4 * p - 3, 4 * p - 2, 4 * p - 1):
            st = {"cases": 0, "with_empty_run": 0, "agree": 0, "disagree": 0, "dp_yes": 0, "dp_no": 0}
            for _ in range(nper):
                a, b, l, y = rand_case(p, N, rng)
                c = grw.criterion(a, b, l, y, p)
                d = wv.dp_has(word(a, b, l, y, p, rng), p)
                st["cases"] += 1
                st["with_empty_run"] += any(ai + bi == 0 for ai, bi in zip(a, b))
                st["agree" if c == d else "disagree"] += 1
                st["dp_yes" if d else "dp_no"] += 1
                if c != d:
                    print("DISAGREE", p, N, a, b, l, y, c, d, flush=True)
            out[f"p{p}_N{N}"] = st
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
