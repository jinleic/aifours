# Sigma is impossible: the mixed-corner exclusion theorem — CANDIDATE v1

Frozen at 2026-10-19T17:51:50-0700 under `SCOPE-FREEZE-v1.json` (SHA256 `5bb3f750d277ef53ff42a44868b4a0911a1cc19c88dab967f47fe477be3d1095`). Status: CANDIDATE written mathematics, not reviewed or accepted. Every step is proved by hand in this file. No script, assertion, enumeration, numerical check, CLI or nested agent was used.

**Outcome: GENUINE EXCLUDED FAMILY.**
- Theorem M: no genuine five-set in B3 normal form has all six cells (r,c) ∈ {1,7} × {1,2,3} of square 1 "A-mixed", i.e. with nonzero projection onto V_A = span{e_1,e_2,e_3} AND nonzero projection onto its orthogonal complement.
- Corollary Σ: the subfamily Σ is impossible for every B3 axis and phase, with general interior vectors. Σ is the family of the A/Z-corner candidate [AZ]: the A-parts of square 1 in rows 1 and 7 occupy exactly columns 1, 2, 3. The weaker hypothesis "no A-part in columns 4..7 of rows 1 and 7" is already impossible.

This is not a B3 no-go: configurations with some non-mixed corner cell remain open (section 6). Nothing is claimed for Boolean models, GB, B2 or n=8. GB 15/18 and the UNKNOWNs are unchanged.

## 1. Hypotheses actually used

- **H1.** Q_1,...,Q_5 are genuine pairwise-orthogonal QLS(8) ([PRIM] LF195-225). Rows and columns are ONBs, and for distinct cells x, y and distinct squares s, t, G_s(x,y)G_t(x,y) = 0, where G_s(x,y) := <Q_s(x),Q_s(y)>.
- **H2.** Q_s(0,c) = w_{s,c}e_c with |w_{s,c}| = 1.
- **H4 (part).** q^1 := Q_1(1,0) and q^7 := Q_1(7,0) lie in V_A with full support {1,2,3}, as in the exact P1-B3 template [J]. Column 0 is orthonormal, so <q^7,q^1> = 0.

SB2, the remaining template rows and the axis data of squares 2..5 are not used. Write a^r_d := <e_d,q^r> for r ∈ {1,7} and d ∈ {1,2,3}. All six numbers are nonzero.

- **(F1)** At an interior cell (i,c), coordinate c is absent from every Q_s(i,c), since Q_s(i,c) ⊥ Q_s(0,c) = w e_c.
- **(F2)** At an interior cell z and any coordinate d != c, at most one square has <e_d,Q_s(z)> != 0. Apply H1 to z and (0,d), which share neither row nor column, and use G_s((0,d),z) = conj(w_{s,d})<e_d,Q_s(z)>.

## 2. Lemma 1 (corner lines)

For r ∈ {1,7} and c ∈ {1,2,3}, the A-part P_A Q_1(r,c) lies in the line spanned by

    ℓ_{r,c} := conj(a^r) × e_c,

the cross product in C^3 coordinates (e_1,e_2,e_3), with conj(a^r) := (conj a^r_1, conj a^r_2, conj a^r_3). Explicitly:

    ℓ_{r,1} = (0, conj a^r_3, −conj a^r_2),
    ℓ_{r,2} = (−conj a^r_3, 0, conj a^r_1),
    ℓ_{r,3} = (conj a^r_2, −conj a^r_1, 0).

Every ℓ_{r,c} has support exactly A \ {c}. Moreover:

    (i)  sum_{c=1..3} ℓ_{r,c} ℓ_{r,c}^* = P_A − |q^r><q^r|;
    (ii) <ℓ_{1,c},ℓ_{7,c'}> = −a^1_{c'} conj(a^7_c) != 0   for all c, c' ∈ {1,2,3}.

*Proof.*
- **The line.** Q_1(r,c) ⊥ q^r (same row) and ⊥ e_c (same column, H2). Both q^r and e_c lie in V_A, so P_A Q_1(r,c) is orthogonal to both. They are independent because q^r has full support, so V_A ∩ {q^r,e_c}^⊥ is a line.
- **Spanning vector.** ℓ_{r,c} is orthogonal to both. For example, <q^r,ℓ_{r,1}> = conj(a^r_2)conj(a^r_3) − conj(a^r_3)conj(a^r_2) = 0, and the other cases are the same. Its two possibly nonzero entries are nonzero by full support, so its support is exactly A \ {c}.
- **(i).** Entrywise:
  - the (d,d) entry of the sum is the sum of |a^r_x|^2 over x != d, which is 1 − |a^r_d|^2;
  - the (1,2) entry is conj(a^r_2)·conj(−conj a^r_1) = −a^r_1 conj(a^r_2), coming only from ℓ_{r,3};
  - the (1,3) entry is −a^r_1 conj(a^r_3), coming only from ℓ_{r,2};
  - the (2,3) entry is −a^r_2 conj(a^r_3), coming only from ℓ_{r,1}.

  These are the entries of I_A − a^r (a^r)^*, which represents P_A − |q^r><q^r|.
- **(ii).** conj(ℓ_{1,c}) = a^1 × e_c. The bilinear Lagrange identity (u×v)·(w×z) = (u·w)(v·z) − (u·z)(v·w) gives

      <ℓ_{1,c},ℓ_{7,c'}> = (a^1 · conj a^7) δ_{cc'} − a^1_{c'} conj(a^7_c).

  Here a^1 · conj a^7 = <q^7,q^1> = 0. Full support makes the remaining term nonzero.
QED

## 3. Lemma 2 (pure squares at a mixed corner cell)

Call (r,c) ∈ {1,7} × {1,2,3} **mixed** if A := P_A Q_1(r,c) != 0 and N := (I − P_A)Q_1(r,c) != 0. At a mixed cell:
- each square s ∈ {2,..,5} has Q_s(r,c) = ω e_d for some d ∈ {0,4,5,6,7};
- these four d are distinct;
- N = β e_{δ(r,c)}, where δ(r,c) is the fifth element of {0,4,5,6,7}.

*Proof.*
- By Lemma 1, A is a nonzero multiple of ℓ_{r,c}, whose support is A \ {c}.
- By (F2), no square s >= 2 has a coordinate of A \ {c} at (r,c). By (F1), none has coordinate c. So every Q_s(r,c), s >= 2, is a unit vector in span{e_0,e_4,...,e_7}.
- N also lies in that span and is nonzero.
- By (F2), the five nonempty supports are pairwise disjoint subsets of the 5-set {0,4,5,6,7}, since each coordinate there differs from c. Hence each support is a singleton.
QED

## 4. Lemma 3 (column and cross-row coupling)

Assume (1,c) and (7,c) are both mixed. Then δ(1,c) = δ(7,c) =: δ(c).

Assume further that (1,c) and (7,c') are mixed with c != c' and δ(1,c) != δ(7,c'). Then G_1((1,c),(7,c')) != 0, and no square s >= 2 has unit-parallel vectors at (1,c) and (7,c').

Separately, if (1,c) is **pure-A** (N = 0, so Q_1(1,c) = ω ℓ_{1,c}/||ℓ_{1,c}||), then P_A Q_1(7,c) = 0, and symmetrically with rows 1 and 7 exchanged.

*Proof.*
- **Decomposition.** Write Q_1(r,c) = A_{r,c} + N_{r,c}, with A_{r,c} = z_{r,c} ℓ_{r,c}. For c' arbitrary,

      G_1((1,c),(7,c')) = conj(z_{1,c}) z_{7,c'} <ℓ_{1,c},ℓ_{7,c'}> + <N_{1,c},N_{7,c'}>.

  By Lemma 2, the second term is nonzero only if δ(1,c) = δ(7,c').
- **Equal δ.** For c' = c, column c is orthonormal, so the sum is 0. The first term is nonzero by Lemma 1(ii), since z_{1,c}, z_{7,c} != 0. Hence the second term is nonzero, which forces δ(1,c) = δ(7,c).
- **Cross pairs.** If c' != c and δ(1,c) != δ(7,c'), the sum equals its nonzero first term. Then H1 for the distinct cells (1,c), (7,c'), which share no line, gives G_s((1,c),(7,c')) = 0 for every s >= 2.
- **Pure-A.** If (1,c) is pure-A, then 0 = <Q_1(1,c),Q_1(7,c)> = conj(ω) z_{7,c} <ℓ_{1,c},ℓ_{7,c}>/||ℓ_{1,c}||, so z_{7,c} = 0.
QED

## 5. Theorem M (mixed-corner exclusion) and Corollary Σ

**Theorem M.** In no genuine configuration satisfying H1, H2 and the stated part of H4 are all six cells (r,c) ∈ {1,7} × {1,2,3} mixed.

*Proof.* Suppose all six are mixed.
- **Setup.** By Lemmas 2 and 3, each square s >= 2 has pure vectors e_{d_s(r,c)} at the six cells, with d_s(r,c) ∈ {0,4,5,6,7} \ {δ(c)}. Within row r, the three vectors of square s are orthonormal, so T^r_s := {d_s(r,1), d_s(r,2), d_s(r,3)} has three elements. Within column c, d_s(1,c) != d_s(7,c).
- **Matched pairs.** Call (c,c'), c != c', a matched pair of s if d_s(1,c) = d_s(7,c'). Then |G_s((1,c),(7,c'))| = 1. So:
  - by H1 against square 1, G_1((1,c),(7,c')) = 0, hence δ(c) = δ(c') by Lemma 3;
  - by H1 against any other square t >= 2, square t does not also have (c,c') matched.

  Thus each ordered pair (c,c') is matched by at most one square. Distinct common elements of T^1_s ∩ T^7_s give distinct matched pairs of s, because a coordinate occurs in only one column of each triple.
- **Case analysis on δ.**
  - **(a) δ(1), δ(2), δ(3) pairwise distinct.** No pair can be matched. But T^1_s ∪ T^7_s ⊆ {0,4,5,6,7} gives |T^1_s ∩ T^7_s| >= 3 + 3 − 5 = 1. Contradiction.
  - **(b) Exactly two equal, say δ(c_1) = δ(c_2) != δ(c_3).** Only (c_1,c_2) and (c_2,c_1) can be matched, so at most 2 squares have a matched pair. All 4 need one by (a)'s count. Contradiction.
  - **(c) δ(1) = δ(2) = δ(3) = δ.** Now T^1_s, T^7_s ⊆ {0,4,5,6,7} \ {δ}, which has 4 elements. So |T^1_s ∩ T^7_s| >= 2, and each square needs at least 2 matched pairs, at least 8 in total. Only 6 ordered pairs (c,c') with c != c' exist, each matched at most once. Contradiction.

All cases are impossible. QED

**Corollary Σ.** Let Σ' be the hypothesis that, for both r ∈ {1,7}, square 1's interior row-r vectors have zero A-part in columns 4..7. Σ' is impossible, and hence Σ (which implies Σ') is impossible, for every B3 axis and phase with general interior vectors.

*Proof.* Row r is an ONB containing q^r, so the interior A-parts satisfy

    sum_{c=1..7} P_A|Q_1(r,c)><Q_1(r,c)|P_A = P_A − |q^r><q^r|.

Under Σ', only c ∈ {1,2,3} contribute, with P_A Q_1(r,c) = z_{r,c} ℓ_{r,c}. The three lines are distinct: ℓ_{r,1} has zero first entry, ℓ_{r,2} does not, and so on. Three distinct rank-one projectors on a 2-dimensional space are linearly independent:
- a vanishing real combination has zero trace;
- hence it is an affine dependence of three distinct points on the Bloch sphere, which are never collinear.

So the weights are unique, and Lemma 1(i) gives |z_{r,c}|^2 = 1. Then ||A_{r,c}||^2 = ||ℓ_{r,c}||^2 = 1 − |a^r_c|^2 ∈ (0,1), and ||N_{r,c}||^2 = |a^r_c|^2 > 0. All six corner cells are mixed, contradicting Theorem M. QED

**Correction to [AZ].** [AZ] Theorem L and its closing remark say that Σ "requires the three corner lines to carry a tight frame of the plane P_r, which constrains the amplitudes of q_1^r". The tight frame always exists, with the forced masses 1 − |a^r_c|^2 (Lemma 1(i)). The obstruction to Σ is Theorem M, not an amplitude condition. [AZ] Theorem L is vacuous, because its hypothesis Σ never holds. [AZ] itself is unchanged and remains an unreviewed candidate; this note does not use it.

## 6. Exact remaining obligation

What remains open is every corner pattern with at least one non-mixed cell in {1,7} × {1,2,3}. A non-mixed cell is either:
- **pure-A**: Q_1(r,c) = ω ℓ_{r,c}/||ℓ_{r,c}||. By Lemma 3, the partner cell in the same column is then A-free.
- **A-free**: P_A Q_1(r,c) = 0.

Proved tools that apply to these patterns:
- Lemma 2 holds at every mixed cell;
- Lemma 3 holds for every mixed pair;
- the pure-A ⇒ A-free column rule.

Rows 1 and 7 must still carry A-content P_A − |q^r><q^r|. Hence, in such patterns, some of it lies in columns 4..7 or in pure-A corner cells. Deciding these patterns is the next obligation. No full B3 no-go is claimed.

## 7. Imports and sources

The imports are [PRIM] LF195-225 (definitions) and [J] (template rows: full supports of q^1, q^7). [AZ] is cited only for the definition of Σ and for the correction above. It is not a premise.

- [PRIM] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16/sources/2607.12933v2.raw.txt`, SHA256 `265851e451cc30706b0a4ea1860c5f04568d99be85896c7b049f95c995108df9`.
- [J] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-binding-v1/GBBINDING.json`, SHA256 `d917203deb29a13e212c290e227a001a695765d080a897141d6dc154d79fc673`.
- [AZ] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-az-corner/B3-AZ-CORNER-PURITY-CANDIDATE-v1.md`, SHA256 `52c6b59b39ffd1348e412947ac7c301329d70f645205c0b42adcb656eb36b03d`.
- [TR] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-slot-transitions-core6-corner-sigma-v1.json`, SHA256 `7ff16d5b5b312bb3ca65206cb84f73331ccf3cd7b71cc7f0753687f1e2da26ec`.
- [SC] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-sigma-closure/SCOPE-FREEZE-v1.json`, SHA256 `5bb3f750d277ef53ff42a44868b4a0911a1cc19c88dab967f47fe477be3d1095`.
