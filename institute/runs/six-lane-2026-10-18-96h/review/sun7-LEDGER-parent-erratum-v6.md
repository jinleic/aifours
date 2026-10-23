# Closed ledger parent erratum v6 — AFIBRE definitions, order and exact exports (candidate repair)

Recorded 2026-10-20T05:36:54-0700 (`/bin/date`). Read after parent errata v2–v5. Responds to AFIBRE 0F/1M/4m. This is **CANDIDATE_UNVERIFIED** until the separate repair gate. Stable node IDs do not change; no class theorem is weakened or enlarged.

## 1. MAJ-1 — DEF before INV/ROWU; explicit order replaces numeric order
N15 DEF has only N02 as input. Place it immediately after N08. The proposed topological order is **N01,N02,…,N08,N15,N09,N10,N11,N12,N13,N14,N16,N17,…,N59**. All earlier assertions "input number smaller" or "N01,…,N59 is the order" are withdrawn and replaced by "every input precedes its consumer in this explicit order". The graph remains acyclic: moving N15 earlier crosses only N09–N14, none of which is an input of N15. Existing consumers of N15 numbered≥16 remain after it.

Add N15 to N13 and N14 inputs. In INV(a) read "same profiles" as "same labelled index tuple, hence every index-determined invariant"; a profile vocabulary is supplied by its consumer (e.g. N16), not imported backward into N13. Actual inversion preserves the n_i, so every pure index/class/marking predicate is preserved (E6).

## 2. MIN-3 — exact DEF export, with KII proof
N15 exports only: finite seven-coset CE and its labelled index decomposition n_i=2^e_i 3^f_i 5^h_i w_i with gcd(w_i,30)=1; A_2/A_3/A_5, C,E,a,D; P0/P1 and their elementary proofs (README LF33–52); the six class PREDICATES (README LF89–96, without the preceding exhaustiveness assertion); and their conditional gcd matrices. In K7, "unmarked" means e_i=f_i=1,h_i=0, i.e. n_i=6w_i. No R0 clause, R1(7), Sun theorem, elimination or "every CE belongs to the six classes" is part of DEF; those belong to N03/N17/N23.

**KII matrix from P0/P1 only (no R1(7)(II)).** Assume a=2 and write A_5={x,y}. There are five other vertices j. P0(a) and P1(i) force each of x,y to lie in A_2∪A_3: otherwise its pair with any j outside A_5 would have no common2/3/5 prime, contradicting gcd≥2. P1(ii) permits at most one member of A_5 in A_2 and at most one in A_3. Therefore, up to names, x∈A_2∖A_3 and y∈A_3∖A_2; neither can belong to both (then the other would belong to neither). For any j outside A_5, P1(i) on x,j forces j∈A_2 and on y,j forces j∈A_3. Thus the other five vertices are exactly C. Now P1 gives C–C gcd6, x–y gcd5, y–C gcd3, and x–j gcd4 iff both x,j∈E (otherwise2). This is precisely the KII predicate/matrix, with no exhaustiveness or Sun input. All other per-predicate matrices follow immediately from P1(i)/(iii).

## 3. MIN-1 — explicit edge cells
Add N02 to N10 (F7 directly uses L0.3) and to N14 (E1/L0.3). R05's consumer list includes N16. Label N13's VFC use **(V1) only** (the q definition); R14's (V2)–(V4) attribution is not its premise. New inputs:
- N10: N02,N09.
- N13: N02,N03(cons.),N11,N15.
- N14: N02,N12,N15.

## 4. MIN-2 — abstract ROWU transfer only
N14 exports ROW-U-deg only at ME LF27–30 (abstract gcd hypothesis, standard weights, value bound and conclusions(i)–(iii)), and E8 only at LE LF71–78. ME LF26 and LF31–32 (M1/ROW1 verification) and LE LF79–80 (K63-U0 Step1 instance) are owned by the respective consumers, not N14's proof body. Each consumer checks the abstract gcd hypothesis for its own labels. No ROW1/M1 input or false cycle is added to N14.

## 5. MIN-4 — RW literal alignment
N16 export is RW LF10–23 **read only with RWE(3eb93c473858fb34b78802ce49626700db90e2176301a94ca20f90078c5d663c) and RWV(1bc8080a3cdd7ec87e62bdc45b62f4683f2ef0b55809016e64415068cbf32ded)**. Body/discharge ranges: RK7 LF19–24,LF26–28,LF30,LF40–49; LF70 for non-L5 quantities only,LF71–75;LF80 first sentence only. ADD LF21–110 (W2 governs LF106),LF124 first two sentences,LF128–139,LF143–148,LF155. No excluded range is an import. R12 retains only WV LF38/LF48's packing proof (drop the alternative S56 L3/K2 route). R18 follows the just-stated RWE ranges. F20's "no operative consumer" parenthetical applies only to K/P/RPLP: N16's capping export DOES feed N57 through CI62. RW's R0 clause is consumer-side; RWV's theorem takes finite input.

No other incoming edge changes. This proposal does not accept AFIBRE closure, full Sun7 or any runtime.
