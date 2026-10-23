# PLAN-v1: independent finite verification of ROT at p = 5 with four odd blocks (frozen before enumeration)

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T08:21:46-07:00.  Purpose: close the only case the parent
verdict withholds for ROT-o4 (R/olson-rotation-o3o4-parent-verdict-v1.md L11, L22-25: "the p = 5 case of ROT-o4 ...
rests only on an unaudited exhaustive D10 census").  No historical census, earlier lane code or earlier output is used
(Sec. 12).  Native enumeration starts only after the parent's GO on this frozen packet.

## 1. Claim

**C5.**  Let w be a word of length 18 over D_10 (p = 5; (v,e)(v',e') = (v + e v', e e'), rho_x = (x,+1),
sigma_y = (y,-1)) with no identity 10-subword in increasing index order, and with exactly four odd blocks in its maximal
cyclic constant-block decomposition (o_F(w) = 4).  Then all rotation letters of w lie in one set {rho_c, rho_-c}, c != 0.

## 2. Reduction to the enumerated domain (proof)

(R1) o_F(w) = 4 gives F >= 4.  Write the maximal cyclic constant-block decomposition R_1 S_1 ... R_n S_n (each maximal
cyclic reflection run cut at every change of value; runs may be empty), with exactly four blocks of odd length.
(R2) Lemma PM* (accepted: R/olson-rotation-lowodd-parent-verdict-v2.md item 2 with erratum M1: any cyclic constant-block
representation, empty runs and equal adjacent values allowed; original-to-reduced direction) applied to an even block
S_i is the move R_i S_i R_(i+1) S_(i+1) -> R_i R_(i+1) sigma_(y_(i+1))^(l_i + l_(i+1)) (l_i even): if the original
avoids, so does the result; the rotation multiset, the length and F are unchanged; the new block has the parity of
S_(i+1); one even block disappears and no odd block disappears.  Apply it while an even block exists.  As four odd
blocks exist, the process stops with EXACTLY four blocks, all odd: an avoider w^ given by a cyclic representation
R_1 S_1 R_2 S_2 R_3 S_3 R_4 S_4 of length 18, l_i odd, runs arbitrary multisets (empty allowed, adjacent values may be
equal), with the rotation multiset of w.  Hence C5 follows from
**C5'.**  Every avoider in the domain D of such 4-block all-odd representations has its rotations in one
{rho_c, rho_-c}, c != 0.
No fusion step is used, so there is no lower-k terminal and neither ROT-o2 nor any normal-form fusion is needed.
(R3) Word classes (elementary).  (a) Identity subwords are invariant under cyclic shift (UV = e iff VU = e).  (b) The
selected rotations of one run multiply to rho_(sum), whatever their order, so a run is a multiset.  (c) From a constant
block sigma_y^l any j in [0, l] letters can be selected and they multiply to sigma_y^(j mod 2).  So solvability depends
only on the class (l_1..l_4; y_1..y_4; the four run multisets); Stage D represents each class by the linear word
R_1 S_1 R_2 S_2 R_3 S_3 R_4 S_4 with every run sorted by value.
(R4) Elementary exclusions (GRX-free; used by Stage D).  H := sum (l_i - 1)/2 = the number of disjoint adjacent equal
pairs inside blocks; R = 18 - F = 14 - 2H.  (i) H >= 5: five such pairs form an identity 10-subword.  So H <= 4.
(ii) P1': if for some j <= H the rotation multiset has a sub-multiset of size 10 - 2j with value sum = 0 (mod 5), choose
it and j pairs: each pair is two adjacent letters with product e, so the selection multiplies to rho_0 = e.

## 3. Domain and exact counts

For H = 0..4: R = 14 - 2H; block-length tuples (l_i = 2a_i + 1, sum a_i = H): C(H+3,3); y-tuples: 5^4 = 625; run-multiset
tuples ("distributions"): C(R+19,19) (multisets of size R over the 20 (run, value) types), of which a rotation multiset
with value counts c_x has prod_x C(c_x+3,3).  Plan-time computation (08:1x, in-memory, recomputed by both stages):

| H | R | multisets C(R+4,4) | survivors of P1'/all-plus (all / non-rigid) | survivor distributions (all / non-rigid) | l-tuples |
|---|---|---|---|---|---|
| 0 | 14 | 3060 | 0 / 0 | 0 / 0 | 1 |
| 1 | 12 | 1820 | 4 / 0 | 17600 / 0 | 4 |
| 2 | 10 | 1001 | 12 / 4 | 13640 / 3520 | 10 |
| 3 | 8 | 495 | 12 / 4 | 7956 / 5376 | 20 |
| 4 | 6 | 210 | 8 / 4 | 1232 / 896 | 35 |

GRX classes (H, distribution, y): total sum_H C(R+19,19) * 625 = 613,973,068,750; enumerated 40,428 * 625 = 25,267,500.
Words up to (R3): total sum_H C(H+3,3) C(R+19,19) * 625 = 1,021,369,625,000; enumerated by Stage D 255,650,000.
Both stages assert, per H, (solved by the filter, counted by formula) + (enumerated) = total, and exit nonzero otherwise.
"Rigid" multiset: all values in one {c, -c}, c != 0 (support {c} or {c, -c}).

## 4. Symmetry reductions

None.  (Stage G checks, as an internal control only, that its avoider set is invariant under y -> y + b, which holds
because (v,e) -> (v + b(1-e)/2, e) is an automorphism of D_10 fixing every rotation.)

## 5. Stage G: GRX classifier (code/grx_p5o4_v1.py, Python 3 + numpy)

GRX (accepted; notes-GRX-v1.md Sec. 1): theta_i = y_(i-1) - y_i, f_i = [z_i != z_(i+1)], Phi = sum f_i,
delta = #{i : l_i != f_i mod 2}, C_max = F - delta, T(z) = sum_(z_i = +1) theta_i; solvable iff some z and even C with
Phi <= C <= C_max, 0 <= 10 - C <= R and T(z) in Sigma_(10-C)(X^z).  With all l_i odd, C_max = 2H + Phi.
For each H and rotation multiset: the all-plus pattern (z = ++++, T = 0, X^z = the multiset) is tested first; if it
solves, every class with that multiset is solved (counted by formula).  Otherwise every distribution and all 625
y-tuples are classified with all 16 patterns (vectorised over y; masks of achievable effective sums per allowed size).
Outputs: grx_summary.json (per-H counts, controls, avoider type census), grx_avoiders.txt (one canonical line
"H=..|dist=..|y=.." per avoider class), grx_survivors.txt, grx_mutations.txt (TC5).

## 6. Stage D: direct DP (code/dp_p5o4_v1.cpp, C++17; separately written, no GRX)

For each H and rotation multiset: P1' (own subset-size/sum DP); if it holds, all its words are solved by (R4)(ii)
(counted by formula).  Otherwise every distribution, every y-tuple and EVERY block-length tuple is built as a word of
length 18 and decided by the ordered DP over D_10: reach[c] = set of products of c selected letters (10-bit masks),
reach[0] = {e}, letters processed in order with c descending; solvable iff e is in reach[10].  A class (H,
distribution, y) is an avoider iff all its block-length tuples avoid; a class with mixed verdicts is recorded in
dp_mixed.txt (GRX predicts none).  Outputs: dp_summary.json, dp_avoiders.txt, dp_survivors.txt, dp_mutations.txt,
dp_mixed.txt, in the same canonical line formats as Stage G.

## 7. Controls (expected outcome in brackets)

Positive: PC-k2, the accepted example rho_1^9 sigma_0^7 rho_-1 sigma_0 (Claude engine note L156) [avoider in G and D];
PC-I, R_1 = rho_1^3, R_2 = R_3 = R_4 = rho_1, y = (0,3,1,4), any l with H = 4 [avoider; plan-time check by an in-memory
raw DP for l = (9,1,1,1), (3,3,3,3), (1,5,3,3)]; PC-II, runs (rho_4, rho_1^9, rho_4, rho_4), y = (0,0,0,0),
l = (1,3,1,1) [avoider, plan-time check]; the avoider set must contain a type I class (H = 4, all rotations equal) and a
type II class (H = 1, counts c^9 (-c)^3).
Corruption (each must fire): TC1 GRX with only the patterns ++++ and ---- [spurious avoiders on non-rigid multisets > 0];
TC2 GRX with C_max := F [some true avoiders flip to solvable]; TC3 DP with the untwisted law (v + v', e e') on every
H = 4 survivor class with l = (9,1,1,1) [verdict differences > 0]; TC4 DP with target length 8 on avoider words
[solvable > 0]; TC5 for the first 3000 avoider classes in canonical order, with l = (2H+1,1,1,1), every one-rotation
value change and every one-block value change, decided by literal GRX in G and by the DP in D [both lists identical,
some mutations solvable].
Validation: 20,000 pseudo-random domain words whose multiset satisfies P1' [all solvable by DP]; for the first 3000
avoider classes, all 18 cyclic shifts and the reversed word with rotations inverted [all avoid].

## 8. Coverage, hashes, comparison (code/compare_p5o4_v1.py)

PASS iff: survivor lists, avoider lists and mutation lists of G and D are byte-identical; no mixed class; no non-rigid
avoider in either stage; per-H coverage holds in both; PC-k2 avoider in both; type I and type II avoider classes present;
G's avoider set is translation invariant; TC1-TC5 fire; the P1' sample has 20,000 words and 0 failures; shift/reversal
failures = 0.  verdict.json records the checks and the SHA-256 of every output file.

## 9. Run protocol

After GO: fresh directory out/run1/ (exist_ok=False).  One process at a time, each through ../code/gate_v1.sh with
projected 300 MB, TMPDIR = p5o4-v1/tmp, PYTHONDONTWRITEBYTECODE=1 (python3 -B):
G: ulimit -t 3600, python3 -B code/grx_p5o4_v1.py out/run1;  D: ulimit -t 3600, code/dp_p5o4_v1 out/run1 (binary built by
clang++ -O2 -std=c++17 -Wall -Wextra from the frozen source; binary hash recorded at launch);  C: ulimit -t 300,
python3 -B code/compare_p5o4_v1.py out/run1.  Any gate failure, CPU-limit stop, nonzero exit or missing file: the result
is UNKNOWN; no partial claim; a rerun uses new versioned code/directories.  All native work ends by 17:57.

## 10. What a PASS establishes

C5' and hence C5 (ROT-o4 at p = 5) as a finite exact statement, conditional on the accepted PM* and on the correctness of
the frozen code.  Stage D alone decides C5' from (R3), (R4) and the DP without GRX; Stage G is an independent second
route through the accepted GRX.  Consequences to be recorded only after review: INV*-FEW (a) at p = 5 with o_F = 4 (with
REFL-few-odd), and OLSON-FEW (a) at p = 5 with o_F <= 4.

## 11. Pre-freeze source checks (no enumeration)

In-memory only (08:1x): 606 domain-type words (random and rigid-type) agree three ways (Stage G's vectorised path,
literal GRX, an independent Python raw DP): 0 mismatches, 6 avoiders; 3000 random and 4000 rigid-type words GRX vs raw
DP: 0 mismatches; PC-I and PC-II found and checked by the raw DP.  dp_p5o4_v1.cpp compiles cleanly with -Wall -Wextra;
it has not been run.  (An eval import of grx_p5o4_v1.py created code/__pycache__/; it is not used by any run.)

## 12. Not relied upon

The historical D10 census and every earlier output; this lane's earlier code (grx.py, rawdp.py, kblock_exact*,
check_*); out/bases_p5_N18.txt; the parent's lowodd RESULT.json.  None is read by the frozen code.
