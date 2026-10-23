# K63-TWO-ORBIT-v1: written facts about the K6.3 residue survivors (all C-C alpha = alpha* = 3)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T01:35:59-0700.
- **Status:** written analysis requested by the parent (two-orbit obligation). It proves structural facts and refutes
  one candidate lemma; it does **not** close the K6.3 residue. No group enumeration was run.
- **Setting.** K6.3 as in the accepted reduction: C = {i*, c1, ..., c5}, n_c = 6 r_c with r_c pairwise coprime,
  r_(i*) = 2 x (odd) (e* = 2), r_c odd for c != i*; the 3-marker is on d, so 3 does not divide any r_c; n_d is odd
  with 9 | n_d. The survivors of `evidence/probe-v14-exact-K63-r1` (postrun sha256
  3ea305a1588f4210f6a2204c91ee4866d720cc21cd402d41bd4ad44b2b21fcae) have alpha_cc' = alpha*_cc' = 3 for all
  C-pairs. Write mu for Haar measure (mu(G) = 1); G may be taken finite (pass to the quotient by the core of the
  intersection of the U_v; all indices, double cosets and disjointness are preserved).

## 1. Two-orbit structure (proved)
For a C-pair (i, j): alpha_ij = 3 gives mu(U_i U_j) = 3/6 = 1/2, and alpha*_ij = 3 gives
mu(U_i x U_j) = 1/2 for x = g_i^-1 g_j, which lies outside U_i U_j because g_i U_i and g_j U_j are disjoint. Distinct
double cosets are disjoint, so **G = U_i U_j disjoint-union U_i x U_j: exactly two (U_i, U_j)-double cosets, each of
measure 1/2.** Equivalently U_i has exactly two orbits on G/U_j, each of size 3 r_j, and U_j has two orbits of size
3 r_i on G/U_i. [G : U_i cap U_j] = 18 r_i r_j. For i, j != i*, the orbit sizes 3 r_j, 3 r_i are odd.

## 2. Index-2 dichotomy (proved)
Let W = <U_i, U_j>. U_i U_j is contained in W, so mu(W) >= 1/2 and [G : W] is 1 or 2. If [G : W] = 2 then
U_i U_j is contained in W with mu(U_i U_j) = 1/2 = mu(W), so **U_i U_j = W is an index-2 subgroup**; otherwise W = G.
Call (i, j) a *subgroup pair* in the first case.

## 3. Matching lemma among the five odd C-vertices (proved)
For c != i*, v_2(n_c) = 1, so U_c lies in at most one index-2 subgroup (if it lay in two distinct ones it would lie
in their intersection, of index 4, forcing 4 | n_c).
(a) Let (a, b) and (a, c) be subgroup pairs with a odd, U_a U_b = H_1, U_a U_c = H_2. Then U_a lies in H_1 and H_2,
so H_1 = H_2 =: H, and U_a, U_b, U_c all lie in H. Then U_b U_c is contained in H and has measure 1/2, so equals H.
Disjointness gives g_a^-1 g_b, g_a^-1 g_c, g_b^-1 g_c all outside H: three distinct cosets of an index-2 subgroup,
impossible. **So every odd C-vertex lies in at most one subgroup pair (including pairs with i*).** In particular the
subgroup pairs among c1, ..., c5 form a matching, and at least 8 of their 10 pairs satisfy <U_i, U_j> = G.
(b) For i*, v_2(n_(i*)) = 2, so U_(i*) can lie in up to three index-2 subgroups (a codimension-2 subspace lies in three
hyperplanes of the largest elementary abelian 2-quotient); distinct subgroup pairs (i*, a), (i*, b) must use
distinct index-2 subgroups by the argument of (a).
(c) n_d is odd, so U_d lies in no index-2 subgroup (else 2 | n_d); hence U_d H = G for every index-2 subgroup H.

## 4. Descent at a subgroup pair (proved; no contradiction)
If (a, b) is a subgroup pair with H = U_a U_b, then by section 3 no other C-subgroup lies in H (an odd c with U_c in
H would make (a, c) a second subgroup pair; U_(i*) in H would put three subgroups in H), and U_d is not in H. Apply
Lemma L5 with the index-2 subgroup H: g_a and g_b lie in different H-cosets, and every other vertex meets both
H-cosets with local index n_v (t_v = 2). So **each H-coset carries exactly six pieces**, with local indices
(3 r_a or 3 r_b, 6 r_c for the three other odd c, 12 x (odd) for i*, n_d). This is a six-coset system inside H whose
pairwise local gcds are 3 or 6; it does not contradict Sun(6)-type bounds by itself.

## 5. The general "index-2" lemma is false (counterexample, checked by hand)
Claim tested: "if U_i has two orbits of equal odd size on G/U_j and the indices are 6 r with r odd and coprime, then
U_i U_j is a subgroup". **False.** Let G = A_5 x Z_3, A = D_10 x Z_3 (index 6, r = 1), B = S_3 x 1 with
S_3 = <(1 2 3), (1 2)(4 5)> (index 30, r = 5).
- A_5 has six Sylow 5-subgroups with normalisers D_10, so A_5 / D_10 is the set of Sylow 5-subgroups.
- (1 2 3) normalises no Sylow 5-subgroup (D_10 has no element of order 3), so it has two 3-cycles on the six points.
- Each involution of A_5 lies in exactly two of the six D_10 (6 x 5 = 30 incidences, 15 conjugate involutions), so
  (1 2)(4 5) fixes exactly two points; it normalises <(1 2 3)>, so it permutes the two 3-cycles, and it cannot swap
  them (that would leave no fixed point). Hence S_3 has orbits 3 + 3 on A_5 / D_10.
- Since A contains 1 x Z_3, the (A, B)-double cosets of G are (D_10 y S_3) x Z_3: exactly two, each of size 90.
  So alpha = alpha* = [G : A cap B] / lcm(6, 30) = 90 / 30 = 3, orbit lengths 3 (B on G/A) and 15 (A on G/B) are odd,
  r = 1 and 5 are odd and coprime, yet A B (90 elements) is not a subgroup: A_5 x Z_3 has no index-2 subgroup.
Scope of the counterexample: it uses r_B = 5, i.e. it is relevant when the 5-marker sits on a C-vertex, and r_A = 1
(at most one vertex may have w = 1). For two C-vertices with r coprime to 30 the lemma is neither proved nor refuted
here. In either case section 2 shows that a proof of the residue cannot rely on index-2 subgroups alone: at least
8 of the 10 odd pairs have <U_i, U_j> = G.

## 6. Other written observations (proved)
- No two C-subgroups lie in a common index-3 subgroup M (else U_i U_j is contained in M, measure <= 1/3 < 1/2).
- U_d contains a Sylow 2-subgroup P of G (n_d odd); P fixes no point of G/U_c for odd c (|U_c|_2 = |P|/2), and every
  U_d-orbit on G/U_c has size 2 r_c or 4 r_c (alpha, alpha* in {1, 2} on d-edges).

## 7. Exact remaining gap for the K6.3 residue (i* with e* = 2, d with f_d >= 2)
The local rule set (LFC, INV, T, Ppair, RPLP at the true q) admits the three v14 patterns; the facts above restrict
any realisation (two-orbit structure on all 15 C-pairs, subgroup pairs forming a matching, <U_i, U_j> = G on at least
8 odd pairs) but do not exclude it. Closing the residue needs a genuinely global argument (or a realisation, which
would contradict Sun(7)); I have neither. No claim beyond sections 1-6.
