# ROT for avoiders with exactly four odd constant blocks, primes p >= 7 (written), v3

Owner OlsonRotationRigidity.  v3 written after host clock 2026-10-18T05:17:17-07:00; v2 (sha256 878fd123...e741) and
v1 (11d7dd03...e44b) kept unchanged.  Changes from v2, made after the Codex review R/olson-rotation-o3o4-codex-v1.note.md
(sha256 86061f1c...93d9; ACCEPT-WITH-FIXES for p >= 7): (1) the written theorem and the at-most-four corollary are now
stated for primes p >= 7 only; the p = 5 statement is moved to Sec. 5 as a separate PRIOR FINITE CLAIM with source pins
(MAJOR: unsupported p = 5 census scope); (2) kappa = 2, |Z| = 4, Y' = g^(2p-4): all FIVE weight-0 multisets are listed and
g(-g)(3g)(-3g) is excluded explicitly by the preceding restriction (MINOR at v2 lines 68-71).  No other change.
Status [W]; v2 reviewed by Codex as above; v3 itself is unreviewed.
Imports: parent-accepted lowodd scope (R/olson-rotation-lowodd-parent-verdict-v2.md, sha256 0853f4ac...ba29: GRX,
PM*, K1/K2 for ANY cyclic constant-block representation; (D), (Z1), (Z2)); proof-ROT-o3-v3.md (sha256 9b0a37db...ab7,
Codex ACCEPT for p >= 5 in the review above): Lemma INC, the star/triangle analysis; Davenport-alpha (reviewed;
erratum m4); EGZ; pairs bound.  Nothing in Sec. 1-4 uses p = 5 data.

## 1. Reduction

Let w (length 4p-2) avoid with exactly four odd blocks.  Delete one reflection from one odd block and apply PM*
across every even block (Lemma DEL of o3-v3, unchanged): w3 = X_1 S_1 X_2 S_2 X_3 S_3 avoids, has length 4p-3, the
same rotation multiset, and l_1, l_2, l_3 odd.  So it suffices to prove:

**Proposition K3'.**  For p >= 7, if w3 (as above) avoids then X_1 + X_2 + X_3 lies in {c, -c}, c != 0.

## 2. Proof of K3'

F = 2H+3, H <= p-1, kappa := p-1-H, R = 2p-4+2kappa.  Davenport-alpha (N <= 4p-1, F >= 2) gives R + H <= 3p-2, i.e.
kappa <= 3.  GRX (any representation):
(ZP) z = (+,+,+): Phi = 0, delta = 3, C_max = 2H: Y has no zero-sum with length in [2kappa+2, 2p].
(AP_i) z = + on run i only: Phi = 2, delta = 1, C_max = 2H+2: no sub-multiset of Y^(i) := Y(X_i) + Y(-X_i') + Y(-X_i'')
       of even size m in [2kappa, 2p-2], m <= R, has value sum theta_i.  (theta_1 + theta_2 + theta_3 = 0.)
Every zero-sum of Y of length <= 2p has length <= 2kappa.  Weights: after INC, rotations are odd multiples a g of a
generator g = (1,c); normalise c = 1, so a rotation of weight a has value a mod p.  "Value sums" below are integers
read mod p; an interval of n consecutive even integers covers min(n, p) residues.

### kappa = 0
Y is zero-sum-free of length 2p-4: by INC (e = 3) Y = g^(2p-4) or Y = g^(2p-5)(3g).  In the latter case let alpha_i be
the number of value-1 rotations in run i (sum 2p-5) and s_i = +1 iff rho_3 lies in run i.  In (AP_i) (m even in
[0, 2p-4]) the value sums are W0 = all even t in [-beta_i, alpha_i] (beta_i := 2p-5-alpha_i, m = |t|) and
W1 = 3 s_i + (odd t' in [-beta_i, alpha_i]) (m = 1 + |t'|).
 alpha_i even: W0 = even integers of [1-beta_i, alpha_i] (p-2 of them), missing the residues alpha_i+2, alpha_i+4;
 if s_i = -1, W1 = even integers of [-3-beta_i, alpha_i-4] contains -3-beta_i = alpha_i+2-2p and -1-beta_i = alpha_i+4-2p;
 if s_i = +1, W1 = even integers of [3-beta_i, alpha_i+2] contains alpha_i+2 only (alpha_i+4-2p = -beta_i-1 < 3-beta_i).
 alpha_i odd: W0 = even integers of [-beta_i, alpha_i-1] (p-2), missing alpha_i+1, alpha_i+3; s_i = +1: W1 = even
 integers of [4-beta_i, alpha_i+3] contains both; s_i = -1: W1 = even integers of [-2-beta_i, alpha_i-3] contains
 -2-beta_i = alpha_i+3-2p but not alpha_i+1.
So (AP_i) can be avoided only if (alpha_i even and s_i = +1) or (alpha_i odd and s_i = -1).  Exactly one s_i is +1;
hence alpha_i is even for that run and odd for the other two, and sum alpha_i is even; but it equals 2p-5.  Contradiction.

### kappa = 1
|Y| = 2p-2; zero-sums of length <= 2p are pairs, pairwise intersecting (else a zero-sum of length 4).  None: Y = g^(2p-2)
by (Z2).  Triangle (three copies of (1,0)): Y minus two of them is zero-sum-free of length 2p-4 and contains (1,0) = p g,
impossible by INC (e = 3).  Star with centre u: Y - u is zero-sum-free of length 2p-3, so g^(2p-3) or g^(2p-4)(3g) (INC,
e = 2), and u = -g or u = -3g (u pairs with some element); u = -3g with 3g present gives the zero-sum (-3g) g^3 of length
4: excluded.  So Y = g^(2p-3)(-g) (rigid) or Y = g^(2p-4)(3g)(-g).  In the latter case, in (AP_i) (m even in [2, 2p-2])
let E+ / E- be the numbers of rotations of effective weight +1 / -1 (value-1 rotations of run i and the value -1
rotation if it lies outside run i / the others); E+ + E- = 2p-3; the value-3 rotation has effective weight 3 s_i.
 If E+, E- >= 1: W0 = all even t in [-E-, E+] (t = 0 via m = 2), i.e. p-1 consecutive even integers, missing E+ + 2 (E+
 even) or E+ + 1 (E+ odd).  W1 = 3 s_i + (odd t' in [-E-, E+]) contains it: E+ even: [3-E-, E+ + 2] (s = +1) or
 [-3-E-, E+ - 4] containing -E- - 1 = E+ + 2 - 2p (s = -1); E+ odd: [4-E-, E+ + 3] or [-2-E-, E+ - 3] containing
 -2-E- = E+ + 1 - 2p.  So (AP_i) is not avoidable.
 If E+ = 0: W0 = {-(2p-4), ..., -2} misses 0 and 2; W1 = [-(2p-6), 2] (s = +1) or [-2p, -4] (s = -1, containing
 -2p and 2-2p) contains both.  If E- = 0: W0 = {2, ..., 2p-4} misses 0 and -2; W1 = [4, 2p] or [-2, 2p-6] contains both.
So every (AP_i) fails: contradiction.

### kappa = 2
|Y| = 2p; zero-sums of length <= 2p have length 2 or 4; disjoint zero-sums of total length >= 6 are excluded.  (D)
gives a zero-sum Z of length 2 or 4; Y' := Y - Z (length 2p - |Z|).
 |Z| = 4: Y' is zero-sum-free of length 2p-4 (a zero-sum there plus Z has length 6 or 8 <= 2p), so Y' = g^(2p-4) or
 g^(2p-5)(3g); #g >= 2p-5.  For h != g in Z, h = a g: if 2p-a <= #g, h g^(2p-a) is a zero-sum of length <= 2p-2, hence
 <= 4, so h in {-g, -3g}; otherwise a = 3 and #g <= 2p-4.  If 3g is in Y then (3g) g^(2p-3) is excluded, so #g <= 2p-4.
 The weight sum of Z is 0 mod 2p and lies in [-12, 12]: it is 0 (p >= 7).
  Y' = g^(2p-4): Z within {g, -g, -3g, 3g}; 3g in Z forces Z without g.  The weight-0 multisets of size 4 over the four
  values (n1 - n2 - 3 n3 + 3 n4 = 0, n1 + n2 + n3 + n4 = 4) are exactly five: g^2(-g)^2, g^3(-3g), (-g)^3(3g),
  (-3g)^2(3g)^2 and g(-g)(3g)(-3g).  The last contains both 3g and g, so it is excluded by the preceding restriction.
  Z = g^2(-g)^2: Y = g^(2p-2)(-g)^2 (rigid); Z = g^3(-3g): Y = g^(2p-1)(-3g); Z = (-g)^3(3g): Y has the zero-sum
  g^3(-g)^3 of length 6, excluded; Z = (-3g)^2(3g)^2: (-3g)^2 g^6 has length 8: excluded.
  Y' = g^(2p-5)(3g): then #g <= 2p-4 and Z has at most one g; the weight-0 options are g(-g)(3g)(-3g), (-g)^3(3g),
  (3g)^2(-3g)^2, all of which put (3g)^2 and >= 2p-6 copies of g in Y: (3g)^2 g^(2p-6) is a zero-sum of length 2p-4 >= 6:
  excluded.
 |Z| = 2, Z = {u, -u}: the zero-sums of Y' (length 2p-2) are pairs (with Z a length-4 one gives 6) and pairwise intersect;
 as for kappa = 1, Y' is g^(2p-2), g^(2p-3)(-g), g^(2p-4)(3g)(-g) or g^(2p-4)(3g)(-3g).  If u in {g, -g}, Y is rigid or
 contains (3g) g^(2p-3) (length 2p-2 >= 6: excluded).  Otherwise u = a g, a odd in [3, 2p-3]: if 2p-a <= #g then
 u g^(2p-a) has length 2p-a+1 <= 4, u = -3g and -u = 3g; if 2p-a > #g then a = 3 and u = 3g.  Either way 3g and -3g both
 lie in Y; then either #g >= 2p-3 and (3g) g^(2p-3) is a zero-sum, or Y' contains 3g too and (3g)^2 g^(2p-6) is one:
 excluded.
 So the only non-rigid possibility is Y = g^(2p-1)(-3g).  Let alpha_i = number of value-1 rotations in run i (sum 2p-1)
 and h_i = -3 if the value -3 rotation lies in run i, +3 otherwise.  In (AP_i), m even in [4, 2p-2], E+ = alpha_i,
 E- = 2p-1-alpha_i.  If E+, E- >= 3, every even t in [-E-, E+] is a value sum (|t| >= 4: m = |t|; t in {-2, 0, 2}: m = 4
 with (q+, q-) = (1,3), (2,2), (3,1)); these are p consecutive even integers: (AP_i) fails.  So every run has
 alpha_i <= 2 or alpha_i >= 2p-3; as the sum is 2p-1, one run (say 1) has alpha_1 >= 2p-3 and alpha_2 + alpha_3 <= 2.
  alpha_1 = 2p-3: W0 = {0, 2, ..., 2p-4} (t = -2 needs q- = 3 > 2), missing -2; the odd t' realisable with
  m = 1 + q+ + q- in [4, 2p-2] are -1, 1, 3, ..., 2p-3; h_1 + t' contains -2 (h_1 = -3: t' = 1) or 2p-2 (h_1 = 3:
  t' = 2p-5).
  alpha_1 = 2p-2: W0 = {2, ..., 2p-2}, missing 0; t' in {1, 3, ..., 2p-3}; h_1 + t' contains 0 (h_1 = -3) or 2p
  (h_1 = 3).
  alpha_1 = 2p-1 (alpha_2 = alpha_3 = 0): W0 = {4, ..., 2p-2}, missing 0, 2; t' in {3, ..., 2p-3}.  If the -3 rotation
  is in run 1, h_1 + t' covers {0, ..., 2p-6}: (AP_1) fails.  Otherwise it lies in run j in {2, 3}; for the other run
  i' in {2, 3}, (AP_i') has E+ = 0, E- = 2p-1, W0 = {-(2p-2), ..., -4} (missing 0, -2), and the value -3 rotation lies
  outside run i', h = +3, giving 3 - q- for odd q- in [3, 2p-3], i.e. {-(2p-6), ..., 0}, which contains 0 and -2.
 In every case some (AP_i) fails: contradiction.

### kappa = 3
|Y| = 2p+2; zero-sums of length <= 2p have length 2, 4 or 6; disjoint zero-sums with total length in [8, 2p] are
excluded.  Extraction ((D) twice if the first zero-sum is a pair) gives a zero-sum Z of length 4 or 6 with Y' := Y - Z:
|Z| = 6: Y' zero-sum-free of length 2p-4 (INC: g^(2p-4) or g^(2p-5)(3g)); |Z| = 4: the zero-sums of Y' (length 2p-2)
are pairwise-intersecting pairs, so Y' is one of the four multisets listed for kappa = 2.  In all cases #g >= 2p-5.
For h != g, h = a g: if 2p-a <= #g, h g^(2p-a) has length 2p-a+1 <= 2p-2, hence <= 6, so h in {-g, -3g, -5g}; otherwise
a = 3, and (3g) g^(2p-3) excluded means #g <= 2p-4.  Two copies of 3g give (3g)^2 g^(2p-6) (length 2p-4 in [8, 2p] for
p >= 7): at most one 3g.  Let N be the multiset of negative elements -b g (b in {1, 3, 5}); for S within N with
sum_S b <= #g, S g^(sum b) is a zero-sum of length sum_S (b+1).  If T := sum_N (b+1) >= 8, order N by increasing b; the
first prefix S with sum (b+1) >= 8 has sum (b+1) <= 12 <= 2p and sum b <= 10; it is excluded as soon as sum_S b <= #g,
which holds if #g >= 10; if #g < 10 then p = 7, #g = 9 and the bad prefix is {-5g, -5g}, so N consists of copies of -5g;
then |Y| = 16 forces at least six of them (at most one 3g), and (-5g)^4 g^6 is a zero-sum of length 10 in [8, 14].  So
T <= 6 and |N| <= 3.  If 3g is present, #g <= 2p-4 and |Y| <= 2p-4+1+3 < 2p+2; so 3g is absent, #g = 2p+2-|N| >= 2p-1,
#g <= 2p-1 (else g^(2p)), |N| = 3, T <= 6: N = (-g)^3 and Y = g^(2p-1)(-g)^3 is rigid.

So in every case the rotation values lie in {c, -c}.  []

## 3. Theorem ROT-o4

**Theorem ROT-o4.**  For every prime p >= 7, every avoider of length 4p-2 over D_(2p) with exactly four odd maximal
constant reflection blocks has all rotation letters in one {rho_c, rho_-c}, c != 0.  Proof: Sec. 1-2.  []
**Corollary ROT-o<=4.**  For every prime p >= 7, every avoider of length 4p-2 over D_(2p) with at most four odd maximal
constant reflection blocks has all rotation letters in one {rho_c, rho_-c}, c != 0.  Proof: ROT-o2 (parent-accepted),
ROT-o3 (proof-ROT-o3-v3.md, Codex ACCEPT), ROT-o4.  []
This is neither ROT(p) (avoiders with five or more odd blocks are not covered) nor INV*(p) nor ordered Olson.

## 4. Finite-exact aids (not premises)

S(3, 4p-3) has no non-rigid avoider at p = 5, 7 (code/kblock_exact_v2.py; out/kblock2_p5_N17_k3_nr1.jsonl,
out/kblock2_p7_N25_k3_nr1.jsonl); S(4, 4p-2) none at p = 5, 7; zero-pattern spectrum (out/zp_spectrum_p7.jsonl) has no
non-rigid survivor at (o' = 4, kappa = 3), and at kappa = 0, 1, 2 exactly the survivors named above.

## 5. p = 5: a separate prior finite claim (NOT part of the theorem above)

The lane records (olson/README.md Sec. 5.1 row "D10" and Sec. 5.2) that an exhaustive search over all words of length 18
over D_10 found exactly 3,730 normalised avoiders, all RGR; if that claim holds, ROT(5) holds for every number of odd
blocks.  It is a finite claim pending parent provenance audit; nothing was rerun for it in this file.  Source pins
(sha256, computed 2026-10-18 between 05:16:04 and 05:17:17 host clock):
  olson/evidence/groups/D10.L18.avoiders.txt  5c42c86ec53b01899066c07c8db5a4b6789f1f9720f1a80f15210cef6f5234ab
  olson/evidence/groups/D10.tab.json          04166c771800c49d1ff9e88cb84bfe10d112c399446bc2d04d6d2836ea73a321
  olson/code/olson_dfs.cpp                    77edf78d47376520077791e8e3c9968da1a5aafd918e27e76ee7a17f876fa017
  olson/code/olson_dfs_id.cpp                 93b564e47749f23143cb92b7992d2539ea68f9d3c72034f26371ba0e82330cc0
No separate D10 receipt JSON was located in olson/evidence/runs/ (that directory holds order-12 receipts only).  This
slice's own checks only show that the 3,730 listed words are avoiders by a fresh raw DP (code/test_grx_v1.py) and that
the GRX classifier finds no non-rigid avoider in S(k, 18) for k <= 4 and S(k, 17) for k <= 5 at p = 5 (README log); they
do NOT establish exhaustiveness of the D10 list.
