# Obstruction note ROT-PP1: terminal k = p+1 after VAC/P/U/TOP, and the sequence statement at length p+2kappa-1, v1

Owner OlsonAssemblyP. Written after /bin/date 2026-10-19T12:14:59-0700. Companion of proof-ROT-PP1-v2.md (sha256
99143ea503a01a6376bed91a2a7ca8b91591617351f35ce4864117bf2949f1ca). Scope: ROT-PP1-scope-v1.md items (d)-(e) (sha256
698521494bcfbd951f417e182698102e3ba1f49559adc15d6a23d709d93686e0, frozen 11:57:04). The verified sequence facts of Sec. 2 are
CANDIDATE_UNVERIFIED written consequences of accepted statements plus explicit hand verification; Secs. 3-4 describe where
routes stop and are NOT claims that any cell is false or that any avoider exists. No computation, model call, novelty,
priority, Lean or human-review claim. Abbreviations R16/R18/ROT/SR2 as in proof-ROT-PP1-v2.md Sec. 2; EV =
/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/ .

## 1. Coverage at terminal k = p+1 (word level; p >= 7; all CANDIDATE_UNVERIFIED)

| kappa^ | Status after proof-ROT-PP1-v2.md |
| --- | --- |
| 0 | vacuous: Proposition VAC (no admissible normal form of an avoider has k >= p+1 and kappa^ = 0) |
| 1 <= kappa^ < (p-1)/2 | nothing new (Sec. 3) |
| (p-1)/2 <= kappa^ <= p-3 | structure only: Lemmas P, U (dominant pair {a,-a}, a != 0, at most p-2 other letters) |
| p-2 | rotation rigidity: Theorem ROT-PP1-TOP |
| p-1 | not treated here (a separate candidate; nothing from it is used or certified here) |

## 2. The naive sequence statement at the k = p+1 length

NS(p, kappa): every sequence Y of odd elements of C_(2p) with |Y| = p+2kappa-1 and (ZP_kappa) satisfies (S1_kappa).
(This is the rotation-sequence length R = p-1+2kappa at k = p+1.) Under (ZP_kappa) a zero-sum of length > 2kappa has even
length >= 2kappa+2 outside [2kappa+2, 2p], i.e. it is LONG (>= 2p+2); so (S1_kappa) fails iff Y has a long zero-sum.

2.1 NS holds (length comparison with accepted statements):
- 0 <= kappa <= floor(2p/3): Lemma S1-sharp has no length hypothesis (R18/olson-s1sharp-parent-verdict-v1.md:9, item 1).
- floor(2p/3)+1 <= kappa <= p-3 with e := p-kappa satisfying p >= 10e-13: the accepted LS+ band (R18/olson-LSplus-chain-
  parent-verdict-v1.md:9-11) bounds a (ZP_kappa) sequence with a long zero-sum by 3kappa+1 < 3kappa+e-1 = |Y| (e >= 3).
- p = 1 (mod 3), p >= 13, kappa = (2p+1)/3 (then e >= 4): BASE1+ (R18/olson-STAB-delta-parent-verdict-v1.md:17-20, item 3)
  bounds it by 2p+2 < (7p-1)/3 = |Y| (p > 7).
2.2 NS FAILS (explicit sequences; h, g odd generators of C_(2p), i.e. h = Y(c), c != 0; a sub-multiset h^i (3h)^j is a
zero-sum iff i + 3j = 0 (mod 2p), since h has order 2p):
- kappa = p-2, |Y| = 3p-5. E2 = h^(2p-4) (3h)^(p-1) and E3 = h^(p-4) (3h)^(2p-1) (the accepted LS+2 sharpness families,
  R18/olson-STAB-delta-parent-verdict-v1.md:21, item 4; SR2/proof-LSplus-e2-v1.md:24-26). Check of (ZP_(p-2)) (no zero-sum of
  length 2p-2 or 2p): length 2p needs i + 3j = 2p + 2j = 0, i.e. p | j: j = 0 needs i = 2p, j = p needs i = p; length 2p-2
  needs 2j - 2 = 0 (mod 2p), i.e. j = 1 (i = 2p-3) or j = p+1 (i = p-3). For E2 (i <= 2p-4, j <= p-1) and for E3 (i <= p-4,
  j <= 2p-1) every case exceeds an available multiplicity. Long zero-sums: h^(p+3) (3h)^(p-1) in E2 and h^3 (3h)^(2p-1) in E3
  (length 2p+2; coefficient sums 4p and 6p; p+3 <= 2p-4 and 3 <= p-4 as p >= 7).
- kappa = p-1, |Y| = 3p-3. Y := g^(2p-1) (3g)^(p-2). (ZP_(p-1)) forbids only length 2p: i + j = 2p and i + 3j = 2p + 2j = 0
  force p | j, so j = 0 (i = 2p > 2p-1) or j = p > p-2. Long zero-sum: g^(p+6) (3g)^(p-2), length 2p+4, coefficient sum
  p+6+3p-6 = 4p, and p+6 <= 2p-1 as p >= 7.
2.3 NS is undecided by accepted results on U(p) := {kappa : floor(2p/3)+1 <= kappa <= p-3, p < 10(p-kappa)-13, not
(p = 1 (mod 3) and kappa = (2p+1)/3)}, e.g. (p, kappa) = (11, 8), (13, 10), (17, 12), (17, 13) (list as in R18/olson-LSplus-
chain-parent-verdict-v1.md:24). The accepted ONE-SHORT-LS (R18/olson-ONE-SHORT-LS-parent-verdict-v1.md:11, item 1) is stated
for the EXACT length p+2kappa and does not apply at p+2kappa-1. An LS+ bound 3kappa+1 at these cells would imply NS there
(3kappa+1 < p+2kappa-1 for e >= 3).
Remark. At kappa = p-2, NS fails while the word-level Theorem ROT-PP1-TOP holds: the theorem is a word-level replacement in
exactly the cell where no sequence-level (S1) is available (E2 is excluded by Lemma P/U, E3 by Steps 6-9 of the proof).

## 3. Word level, 1 <= kappa^ <= p-3 at k = p+1: where the available routes stop

3.1 Routes through (S1) (the ROT-FB / ROT-KP+ pattern). In the cells of 2.1, (S1_kappa^) holds for the rotation sequence. Let
Z be a longest zero-sum, |Z| = 2t <= 2kappa^; its complement is zero-sum-free of length L = R-2t = p-1+2(kappa^-t).
(O1) Complement length. t <= kappa^-1 gives L >= p+1; t = kappa^ gives L = p-1. The accepted setting (S') of Lemma FB / ROT-FB(a)
     requires 1 <= k <= p-1 and L >= 2p-k >= p+1 (EV/proof-FB-v1.md:11-14); ROT-KP+ (k = p) treats the length-p complement
     through the classical import S(p) on zero-sum-free sequences of p odd elements (R18/olson-KPS-SLZ-parent-verdict-v1.md:8,
     10, items 1 and 3). No accepted statement treats a zero-sum-free complement of p-1 odd elements. Smallest missing input:
     a structure statement for zero-sum-free sequences of p-1 odd elements of C_(2p) that can play the role S(p) plays in
     ROT-KP+, or a word-level substitute for the branch t = kappa^.
(O2) k-domain. For t <= kappa^-1, Lemma FB and Corollary FB-E are accepted only in (S') (k <= p-1); a k = p+1 version would
     have to be re-derived, and the SHgen side condition (K) k <= 2p - eta - a_max - 1 re-checked with k = p+1.
(O3) Empty runs. Theorem SHgen's setting has every run NONEMPTY (ROT/proof-SHgen-v3.md:22-24); Lemma SHgen-E assumes REFL(p)
     for words with o_F <= k, supplied by Corollary REFL-few-odd only when k <= p (ROT/proof-ROT-few-E-v4.md:47-48;
     R16/olson-refl-fewodd-parent-verdict-v1.md:6). At k = p+1 a base word may have o_F = p+1. Smallest missing input: an
     empty-run argument at k = p+1 that avoids REFL beyond o_F <= p (Step 9 of proof-ROT-PP1-v2.md is of this kind but is
     proved only at kappa^ = p-2), or REFL at o_F = p+1.
These are obstacles to these routes; they are not proofs that any particular complement or base word occurs.

3.2 The pairing route of proof-ROT-PP1-v2.md.
(P0) Lemma P needs p-1 disjoint swap pairs, i.e. R >= 2p-2, i.e. kappa^ >= (p-1)/2; it gives nothing for 1 <= kappa^ < (p-1)/2.
(P1) For (p-1)/2 <= kappa^ = p-e <= p-3 (e >= 3) Lemmas P and U hold, and in the notation of proof Sec. 5 (A >= A', b = R-A,
     delta letters outside {a, -a}) the window (W) holds with lambda = p-2-b, Lambda = 2kappa^+1-A' and
     Lambda - lambda = p-2e+3+delta. The steps of the kappa^ = p-2 proof that do not carry over as written:
     - Step 3 (b <= p-1 from CT with n = p-3) is proved only for e = 2.
     - Step 5 (a heavy run) uses Lambda - lambda > lambda, i.e. b + delta > 2e-5.
     - Step 6 (no second heavy set) excludes two disjoint sets P', {h} with e(.) >= Lambda only when b < p-2e+3+2delta; at e = 2
       this follows from b <= p-1 for every delta >= 1, but for e >= 3 it needs delta >= e-1 even granting b <= p-1.
     - Step 9 (empty runs): only |M| <= p-1-b is known, and b can be as small as R-(2p-1) = p-2e, so |M| <= 2e-1. The forced
       elements of M are 2a{1, ..., e-1} from the all-plus pattern (subject to the filler bound n-|J| <= A) and
       tau_i + 2a{1, ..., e} from an empty run R_i; their union has at most 2e-1 elements, so counting alone gives no
       contradiction.
     Smallest missing lemmas for this route: (L1) a replacement for Step 6 when 1 <= delta <= e-2; (L2) a statement on
     arithmetic progressions of difference 2a in the complement of the subset-sum set of b >= p-2e nonzero residues, strong
     enough to combine the all-plus, single-empty-run and empty-pair patterns (with the filler bounds). Neither is claimed
     true here, and no cell is claimed false.

## 4. Preserved failed attempts (exact obstruction; none is a premise)

- (F1) Full coverage from one pattern (the OM'-type step of the k = p and kappa^ = p-1 singleton arguments): by Lemma P every
  non-constant pattern has at most p-2 letters off its dominant signed value, so the omission sums of one pattern cover at
  most p-1 residues. Replaced by the window (W), the heavy run and comparisons between the all-plus, empty-run and empty-pair
  patterns.
- (F2) Expansion to the kappa^ = p-1 cell (replace a heavy of weight 3 by three copies and delete one pair from the triple
  block, as in SHgen's u°(h)): the accepted Lemma FLEXa is stated in SHgen's setting (nonempty runs, condition (K)), and the
  target cell k = p+1, kappa^ = p-1 is not accepted; not used.
- (F3) Block values alone at kappa^ = 1: patterns with m >= 2 admit n = 0, so an avoider needs sum over P of tau_i != 0 for
  every set P of runs with at least two intervals. The block values y_i = i (i = 1, ..., p+1, read mod p) give tau_1 = 0 and
  tau_i = 1 otherwise; a zero tau-sum needs P to contain none or all of the runs 2, ..., p+1, and every such nonempty proper P
  is a single interval. So this constraint alone gives no contradiction at kappa^ = 1 (a statement about block values only;
  no word is constructed).
