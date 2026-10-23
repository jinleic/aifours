# Structure notes for the candidate optimal CPCW lengths (NOTES, not results; 2026-10-17 00:18 PDT)

Source of the candidate list: Baicheva-Topalova, Axioms 15(1) (2026) 35, Section 3.1: no optimal code found for
k=5, v = 143, 144, 146, 162, 167 and k=6, v = 122, 123, 124, 126 ("we could not find optimal codes ... the question
of the existence of such codes remains open"). Exact numbers below come from `code/structure_notes.py`
(`notes/structure-notes.json`); everything is a necessary condition derived by counting, nothing is searched.

Definitions used: s = floor((v-1)/(k(k-1))); u = v-1-k(k-1)s uncovered nonzero differences; for even v, v/2 is
always uncovered (Axioms Lemma 1: a pair {a, a+v/2} would give v/2 twice); c = number of uncovered +-classes
besides v/2. Q = Z_v^*/{+-1} (prime orders listed = possible prime orders of a multiplier acting on classes).

| v | k | s | u | v/2 forced | c | v | phi | prime orders in Q | index-m counting (m | v, m <= 4) | Axioms Thm 1/2 system |
|---|---|---|---|---|---|---|---|---|---|---|
| 143 | 5 | 7 | 2 | - | 1 | 11*13 | 120 | 2, 3, 5 | none (no small index) | - |
| 144 | 5 | 7 | 3 | 72 | 1 | 2^4 3^2 | 48 | 2, 3 | m=2: the extra uncovered class is EVEN (z=1 forced); m=3,4: z in {0,1} | - |
| 146 | 5 | 7 | 5 | 73 | 2 | 2*73 | 72 | 2, 3 | m=2: the two extra uncovered classes are both odd or both even (z in {0,2}) | - |
| 162 | 5 | 8 | 1 | 81 | 0 | 2*3^4 | 54 | 3 | m=2,3: consistent (z=0) | v = 20*8+2, v = 2 mod 4: (a0,a1,a2) in {(0,4,4), (1,1,6)} |
| 167 | 5 | 8 | 6 | - | 3 | prime | 166 | 83 | none | - |
| 122 | 6 | 4 | 1 | 61 | 0 | 2*61 | 60 | 2, 3, 5 | m=2: consistent | v = 30*4+2, v = 2 mod 4: unique (a0,a1,a2,a3) = (0,1,2,1) |
| 123 | 6 | 4 | 2 | - | 1 | 3*41 | 80 | 2, 5 | m=3: z in {0,1} | - |
| 124 | 6 | 4 | 3 | 62 | 1 | 2^2*31 | 60 | 2, 3, 5 | m=2,4: z in {0,1} | - |
| 126 | 6 | 4 | 5 | 63 | 2 | 2*3^2*7 | 36 | 2, 3 | m=2,3: z in {0,1,2} | - |

Notes
- Index-m counting: a codeword with residue profile r mod m has S_m = sum C(r_j,2) pairs with difference in mZ_v;
  sum of S_m over the s codewords = (usable classes in mZ_v) - z, z = uncovered classes besides v/2 lying in mZ_v.
  Pigeonhole bounds S_m from below (m=2: k=5 >= 4, k=6 >= 6; m=3, k=5: >= 2). The table lists the z values
  compatible with some choice of profiles.
- Axioms Theorem 1 (v = 2 mod 4) / Theorem 2 (v = 0 mod 4) apply only when v = k(k-1)t+2 (here 162 and 122); a_i counts
  codewords with i elements of one parity and k-i of the other (i <= k/2). Re-derived here: for v = 2 mod 4 the
  missing pairs {a, a+v/2} are cross-parity, so (v-2)/4 same-parity and (v-2)/4 cross-parity classes must be covered
  exactly (v = 0 mod 4: (v-4)/4 and v/4). Calibration (`notes/bt-system-calibration.txt`): the same code returns the
  paper's unique solutions (82,5): a = (0,2,2) (Example 3) and (92,6): a = (0,1,0,2) (equation (15)). The 162 and
  122 systems above were solved by exhaustive enumeration with that code.
- Buratti-Stinson (Ars Math. Contemp. 2020) exclude optimal (v,5,1) codes for v = 22 (mod 40) (the parity argument
  of Axioms Corollary 1). 162 = 2 (mod 40), so it is not excluded by that condition; no other parity exclusion was
  derived here. I did not read the Buratti-Stinson paper itself (not saved); their other conditions are unchecked.
- For odd v (143, 167, 123): no index-2 subgroup; 143 and 167 have no subgroup of index <= 4 at all, 123 has index 3.
- Multiplier group orders are only listed (prime orders available in Q); no fixed-point/orbit analysis was done for
  these lengths yet.
