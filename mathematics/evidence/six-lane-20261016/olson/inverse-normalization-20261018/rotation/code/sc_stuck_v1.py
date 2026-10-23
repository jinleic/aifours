#!/usr/bin/env python3
"""Exploration (not a premise): stuck AP configurations of zero-sum-free odd multisets of Z_(2p).
For every zero-sum-free multiset Y of odd elements (all lengths), take every most frequent value g (a generator),
run the AP process (longest FULL prefix of the sorted g-weights; top M, prefix size nA, jumpers t), and record for
each s = p - M the maximum length L = nA + t of a stuck configuration (t >= 1), the maximum t, and one example.
Tests the conjecture "stuck => L <= p - 1" (equivalently S(p)) and shows how far below p the large-s cases stay.
Usage: sc_stuck_v1.py OUT.jsonl
"""
import json, sys

def rotl(mask, y, n, full):
    y %= n
    return ((mask << y) | (mask >> (n - y))) & full if y else mask

def main():
    out = open(sys.argv[1], "x")
    for p in (11, 13, 17, 19):
        n = 2 * p; full = (1 << n) - 1; odd = [2 * t + 1 for t in range(p)]
        best = {}
        mult = [0] * p
        def analyse():
            L = sum(mult)
            if L == 0:
                return
            m = max(mult)
            for gi in range(p):
                if mult[gi] != m or odd[gi] == p:
                    continue
                g = odd[gi]; ginv = pow(g, -1, n)
                ws = sorted(((odd[t] * ginv) % n, mult[t]) for t in range(p) if mult[t])
                M = 0; nA = 0; jumpers = 0
                for r, c in ws:
                    for _ in range(c):
                        if jumpers == 0 and r <= M + 1:
                            M += r; nA += 1
                        else:
                            jumpers += 1
                if jumpers:
                    s = p - M
                    rec = best.get(s)
                    if rec is None or L > rec["L"]:
                        best[s] = dict(L=L, t=jumpers, nA=nA, M=M,
                                       example=[((odd[t] * ginv) % n, mult[t]) for t in range(p) if mult[t]])
        def dfs(t, A):
            if t == p:
                analyse(); return
            dfs(t + 1, A)
            y = odd[t]; B = A; j = 0
            while not (B >> ((n - y) % n)) & 1:
                B |= rotl(B, y, n, full); j += 1; mult[t] = j
                dfs(t + 1, B)
            mult[t] = 0
        dfs(0, 1)
        rec = dict(p=p, by_s={str(s): best[s] for s in sorted(best)},
                   max_stuck_L=max(v["L"] for v in best.values()) if best else None)
        out.write(json.dumps(rec) + "\n"); out.flush()
        print(json.dumps(rec), flush=True)
    out.close()

if __name__ == "__main__":
    main()
