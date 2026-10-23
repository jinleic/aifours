#!/usr/bin/env python3
"""Exploration for the Savchev-Chen-type lemma at length p (not a premise; guides a proof).
For zero-sum-free multisets Y of odd elements of Z_(2p) of length L in [p-3, p+1]:
  SC   : some generator g gives representatives a_y in [1, 2p-1] with sum <= 2p-1;
  SAT  : A(Y) (subset sums incl. 0) contains every odd element (Y cannot be extended);
  STUCK: the AP process with g = a most frequent value (every tie tried) stops with >= 1 'jumper'
         (an element whose g-representative exceeds M+1, M = current interval top) - recorded as the minimum
         number of jumpers over the most frequent values.
Prints, per (p, L): counts of (SC, SAT) combinations, the number of multisets with a stuck AP process for EVERY
most-frequent choice, and up to 6 unit-canonical examples of non-SC multisets.
Usage: sc_explore_v1.py OUT.jsonl
"""
import json, sys

def rotl(mask, y, n, full):
    y %= n
    return ((mask << y) | (mask >> (n - y))) & full if y else mask

def main():
    out = open(sys.argv[1], "x")
    for p in (7, 11, 13, 17):
        n = 2 * p; full = (1 << n) - 1; odd = [2 * t + 1 for t in range(p)]
        units = [u for u in odd if u != p]
        oddmask = 0
        for v in odd:
            oddmask |= 1 << v
        stats = {}
        examples = {}
        mult = [0] * p
        def sc(ms):
            for g in units:
                gi = pow(g, -1, n)
                if sum(c * ((v * gi) % n) for v, c in ms.items()) <= n - 1:
                    return True
            return False
        def jumpers(ms, g):
            gi = pow(g, -1, n)
            reps = sorted(((v * gi) % n, c) for v, c in ms.items())
            M = 0
            rest = []
            for r, c in reps:
                for _ in range(c):
                    if r <= M + 1:
                        M += r
                    else:
                        rest.append(r)
            # second pass: extenders may become usable after M grew
            changed = True
            while changed:
                changed = False
                for r in sorted(rest):
                    if r <= M + 1:
                        M += r; rest.remove(r); changed = True; break
            return len(rest)
        def canon(ms):
            best = None
            for u in units:
                img = {}
                for v, c in ms.items():
                    w = (v * u) % n; img[w] = img.get(w, 0) + c
                key = tuple(sorted(img.items()))
                score = (img.get(1, 0), key)
                if best is None or score > best[0]:
                    best = (score, key)
            return [(v if v < p else v - n, c) for v, c in best[1]]
        def dfs(t, A):
            if t == p:
                L = sum(mult)
                if p - 3 <= L <= p + 1:
                    ms = {odd[i]: mult[i] for i in range(p) if mult[i]}
                    s = sc(ms); sat = (A & oddmask) == oddmask
                    m = max(mult)
                    js = min(jumpers(ms, odd[i]) for i in range(p) if mult[i] == m and odd[i] != p) if any(
                        mult[i] == m and odd[i] != p for i in range(p)) else -1
                    key = (L - p, s, sat, js > 0)
                    stats[key] = stats.get(key, 0) + 1
                    if not s:
                        c = tuple(canon(ms))
                        ex = examples.setdefault(L - p, set())
                        if len(ex) < 6:
                            ex.add(c)
                return
            dfs(t + 1, A)
            y = odd[t]; B = A; j = 0
            while not (B >> ((n - y) % n)) & 1:
                B |= rotl(B, y, n, full); j += 1; mult[t] = j
                dfs(t + 1, B)
            mult[t] = 0
        dfs(0, 1)
        rec = dict(p=p, stats={"L-p=%d,SC=%s,SAT=%s,stuck=%s" % k: v for k, v in sorted(stats.items())},
                   nonSC_examples={str(k): sorted(list(v)) for k, v in examples.items()})
        out.write(json.dumps(rec) + "\n"); out.flush()
        print(json.dumps(rec), flush=True)
    out.close()

if __name__ == "__main__":
    main()
