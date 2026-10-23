#!/usr/bin/env python3
"""sp_falsify_probe_v13 (ContinueOlson).  FALSIFICATION AID for S(p) (every zero-sum-free sequence of p odd elements of
C_(2p) is SC: some odd generator g gives least positive coefficients summing to <= 2p - 1), equivalently (3-line argument,
see notes) for IDX1-odd(p+1): every all-odd minimal zero-sum sequence of length p + 1 in C_(2p) has index 1.  Never a premise.
Stdlib only; stdout only; self-stop at BUDGET_S.  Complete DFS over zero-sum-free multisets of odd elements (hereditary
pruning by the subset-sum bitmask), canonical: value 1 is a most frequent generator value (valid: the order-2 odd element p
occurs at most once in a zero-sum-free sequence).  At length p every multiset is tested for SC over all generators."""
import time, json
BUDGET_S = 280.0
T0 = time.time()
def left():
    return BUDGET_S - (time.time() - T0)

def run(p, tlimit):
    n2 = 2 * p; FULL = (1 << n2) - 1
    vals = [1] + list(range(3, n2, 2))
    gens = [u for u in range(1, n2, 2) if u % p]
    inv = {u: pow(u, -1, n2) for u in gens}
    st = {"p": p, "complete": True, "zsf_len_p": 0, "sc_len_p": 0, "NON_SC": 0, "examples": [], "zsf_len_pm1": 0,
          "nonsc_len_pm1": 0}
    t1 = time.time(); counts = [0] * len(vals)
    def rot(mask, a):
        a %= n2
        return ((mask << a) | (mask >> (n2 - a))) & FULL
    def is_sc(ms):
        for u in gens:
            iu = inv[u]
            if sum((a * iu) % n2 for a in ms) <= n2 - 1:
                return True
        return False
    def rec(i, mask, total, cap1):
        # mask: bit r set iff r is the sum of a nonempty sub-multiset (bit 0 never set)
        if time.time() - t1 > tlimit or left() < 8:
            st["complete"] = False; return
        if total == p or i == len(vals):
            if total == p - 1 or total == p:
                ms = [v for v, c in zip(vals, counts) for _ in range(c)]
                if total == p:
                    st["zsf_len_p"] += 1
                    if is_sc(ms):
                        st["sc_len_p"] += 1
                    else:
                        st["NON_SC"] += 1
                        if len(st["examples"]) < 5:
                            st["examples"].append(ms)
                elif i == len(vals):
                    st["zsf_len_pm1"] += 1
                    if not is_sc(ms):
                        st["nonsc_len_pm1"] += 1
            return
        a = vals[i]; gen = (a % p != 0)
        maxc = p - total
        if i > 0 and gen:
            maxc = min(maxc, cap1)
        cur = mask; c = 0
        while True:
            counts[i] = c
            rec(i + 1, cur, total + c, c if i == 0 else cap1)
            if not st["complete"]:
                counts[i] = 0; return
            if c >= maxc:
                break
            nxt = cur | rot(cur, a) | (1 << a)
            if nxt & 1:
                break
            cur = nxt; c += 1
        counts[i] = 0
    rec(0, 0, 0, 0)
    st["elapsed_s"] = round(time.time() - t1, 1)
    print(json.dumps(st), flush=True)

if __name__ == "__main__":
    print(json.dumps({"start": True, "budget_s": BUDGET_S}), flush=True)
    for p, tl in ((5, 10.0), (7, 20.0), (11, 60.0), (13, 90.0), (17, 90.0)):
        if left() < 15:
            print(json.dumps({"p": p, "skipped_budget": True}), flush=True)
            continue
        run(p, min(tl, left() - 10))
    print(json.dumps({"done": True, "elapsed_s": round(time.time() - T0, 1)}), flush=True)
