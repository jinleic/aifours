#!/usr/bin/env python3
"""Reviewer cross-check of the active-count identity S(prof,n) = sum_i (6 r_i - n) - sum_{i<j} (r_i r_j - n)
(= sum_P [k - C(k,2)], which must be <= |P| = 36 - n) against (i) the prior t=30 disposition's published
values 30 and 33 for n=6, and (ii) the n=7 bridge value 32 > 29.  Also the unconditional t-range for N=46."""
import itertools, json, hashlib, subprocess
def clock(): return subprocess.run(["/bin/date","-u","+%Y-%m-%dT%H:%M:%SZ"],capture_output=True,text=True).stdout.strip()
def S(prof, n): return sum(6*r - n for r in prof) - sum(prof[i]*prof[j] - n for i,j in itertools.combinations(range(4),2))
c0 = clock()
out = {"n6_3333": S((3,3,3,3),6), "n6_2333": S((2,3,3,3),6), "n6_|P|": 30,
       "n7_3333": S((3,3,3,3),7), "n7_|P|": 29,
       "unconditional_t_range_N46": [t for t in range(0,37) if (46-t) <= (36-t)**2 and 46-t >= 2*(36-t)],
       "bridge_alone_leaves": None}
out["bridge_alone_leaves"] = [t for t in out["unconditional_t_range_N46"] if t not in (27,28,29)]
out["k_minus_C_k_2_max_over_k_0..4"] = max(k - k*(k-1)//2 for k in range(5))
c1 = clock()
rec = {"script_sha256": hashlib.sha256(open(__file__,"rb").read()).hexdigest(), "clock_start_utc": c0, "clock_end_utc": c1, **out}
print(json.dumps(rec, indent=1)); json.dump(rec, open(__file__.replace(".py","-receipt.json"),"w"), indent=1)
