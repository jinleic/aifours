# Sun8 for prime-power PSL(2): a classification-conditional written candidate, with actual-coset exceptional cases

**Status: AUTHOR CANDIDATE, NOT ACCEPTED.** The argument below imports Dickson's subgroup classification in the explicit form in §2. Subject to that import and prospective independent checking, it proves the original eight-actual-coset assertion for every `PSL(2,p^f)` with `f >= 2`, in particular for all four assigned characteristics `p = 2,3,5,7`. For all but `q=4,9` it proves the stronger three-proper-label statement `J_7 <= 2`. The two exceptions are dealt with by actual disjoint cosets; neither has a finite J_7 bound. This does **not** prove Sun8 for all finite simple groups, for general groups, or for normal extensions under both original bounds. Novelty is **UNCLEAR**. No independent review, parent disposition, human check, independent-model-family check, kernel proof, or finite scientific execution has occurred.

Native clock observed before composition: **2026-10-30T15:14:05-0700 PDT**; it is not a file-creation or completion timestamp. The arguments and selected `q=4,8,9` cases are written mathematics, not machine results.

## 1. Original target and basic lemmas

For a group X define `B_7(X) <= r` to mean: in any `r+1` pairwise-disjoint actual left cosets of finite-index subgroups of X, two subgroup indices have gcd at least 8. Repeated subgroups and repeated indices are allowed. Define `J_7(X) <= s` to mean the same gcd conclusion for any `s+1` proper finite-index subgroup labels, with repetitions allowed and **no** disjointness hypothesis. Thus `J_7 <= 2` implies `B_7 <= 2`, while the converse is not asserted.

We use two elementary facts, including in the exceptional actual-coset cases.

**Coprime-index lemma.** If A and B are finite-index subgroups of an arbitrary group X and their indices m,n are coprime, every left A-coset meets every left B-coset. Indeed `t=[X:A intersect B]` is finite, a multiple of both m and n, and at most `mn` by the injective map `x(A intersect B) -> (xA,xB)`. Thus `t=mn` and that map is bijective. Consequently two disjoint actual cosets have noncoprime indices.

**Density lemma.** For finitely many disjoint actual cosets in a finite group, `sum_i 1/[X:U_i] <= 1`. This includes repeated subgroups. (It also holds for general groups via a common finite-index normal core, although only finite groups are needed in §§3–5.)

If one index is 1, its coset is all of X, so it cannot occur in a disjoint family with another member. Thus every subgroup label in a putative bad eight-family is proper.

## 2. Exact classification import and sources

The sole non-elementary import is the list of maximal subgroups of `T=PSL(2,q)`, `q=p^f >= 4`, in M. Giudici, *Maximal subgroups of almost simple groups with socle PSL(2,q)*, arXiv:math/0703685v1 (2007), **Theorems 2.1–2.2**, pages 3–4: <https://arxiv.org/pdf/math/0703685v1>. Giudici explicitly states these theorems as Dickson's classification, not as a proof by the present author. The public primary source is L. E. Dickson, *Linear Groups: With an Exposition of the Galois Field Theory* (1901), Chapter XII, §§249–262, especially the summaries at printed pp. 285–286, §§260–262: <https://archive.org/stream/lineargroupswit00dickgoog/lineargroupswit00dickgoog_djvu.txt>. I inspected the book contents and the OCR synopsis; the displayed maximal-subgroup formulation below is taken from Giudici, not claimed reconstructed from the historical OCR. The modern corroborating statement is A. Beltrán and F. Viudez, *Finite groups whose proper subgroups of order divisible by p are supersolvable*, arXiv:2607.09144v2, Theorem 3.2: <https://arxiv.org/html/2607.09144v2>. It also states that the even-characteristic subfield parameter is greater than 2. A separate GroupNames A5 page was browsed during orientation but is not an imported premise.

Only the following **overinclusive** consequences of the list are used. A proper subgroup lies in a maximal subgroup, so each of its indices is a multiple of a listed maximal index.

* If q is even, a maximal subgroup has order `q(q-1)`, `2(q-1)`, `2(q+1)`, or `q0(q0^2-1)` for `q=q0^r`, r prime, q0 a proper subfield size. For a deliberately harmless overinclusive list we permit `q0=2` even where the actual maximality condition excludes it. Therefore the corresponding indices are respectively
  `q+1`, `(q/2)(q+1)`, `(q/2)(q-1)`, and `(q/q0)(q^2-1)/(q0^2-1)`.
* If q is odd, the Borel and dihedral maximal possibilities have orders `q(q-1)/2`, `q-1`, `q+1`; subfield possibilities are `PSL(2,q0)` for `q=q0^r`, r an odd prime, and `PGL(2,q0)` for `q=q0^2`. Other maximal groups can only be A4, S4 or A5, with the exact q-conditions in Giudici Theorem 2.2. In particular, A4 and S4 are maximal only for prime q; an A5 maximal subgroup for nonprime q can occur only for `q=p^2` and `p == +/-3 (mod 10)`. We include dihedrals even in small cases where the original list excludes them; this only enlarges the list used for necessary divisibility.
* For `q=9` we use the sharper actual maximal list: Borel index 10, `PGL(2,3)` index 15, and A5 index 6, possibly in different conjugacy classes. Giudici's small-q restrictions exclude both dihedral entries as maximal here. The list says every proper subgroup is contained in one of these maximal subgroups; it does not by itself assert the actual-coset conclusions proved in §5.

The standard order formulas used below are `|PSL(2,q)|=q(q^2-1)/(2,q-1)` and `|PGL(2,q0)|=q0(q0^2-1)`. They follow by choosing the first nonzero column, then the second with determinant 1, and quotienting by the scalar center. No proof of Dickson's classification is claimed here.

## 3. Index dichotomy for every nonexceptional prime power

**Claim A.** For `q=p^f`, `f>=2`, `q not in {4,9}`, there are explicit integers A,B greater than 7 such that every proper subgroup index is a multiple of A or of B:

| case | A | B |
|---|---:|---:|
| `q=8` | 9 | 28 |
| `q=2^f`, `f>=4` | `q+1` | 8 |
| `q=p^f`, p odd, `f>=3` | `q+1` | `p^2` |
| `q=p^2`, p odd and `p>=5` | `(q+1)/2` | `p^2` |

**Proof, even q.** The Borel index and split-dihedral index are multiples of `q+1`. The nonsplit-dihedral index is `(q/2)(q-1)` and is divisible by 8 for `f>=4`. If `q=q0^2`, its subfield index is `q0(q+1)`, also divisible by `q+1`. If `q=q0^r`, r odd prime, writing `q0=2^d` gives a subfield index whose 2-part contains `2^{(r-1)d}`. For `f=rd>=4`, this exponent is at least 4: either `r>=5`, or `r=3,d>=2`. It is therefore divisible by 8. For `q=8`, the Borel and split-dihedral indices are 9 and 36, the nonsplit index is 28, and even the overincluded `q0=2` subfield index is 84. These are all multiples of 9 or 28.

**Proof, odd q and `f>=3`.** The Borel index is `q+1`. A dihedral maximal subgroup has order prime to p, so its index is divisible by `p^f`, hence by `p^2`. For an odd-prime-degree subfield `q=q0^r`, `q0=p^d`, the p-part of the index is `p^{f-d}`, with `f-d=(r-1)d>=2`. For a quadratic subfield `q=q0^2`, the p-part of the PGL index is `p^{f/2}`, and `f>=3` forces even `f>=4`, so again it is divisible by `p^2`. The exceptional A4/S4/A5 maximal cases are absent for `f>=3` by the stated import.

**Proof, odd `f=2` and `p>=5`.** The Borel index `q+1` and quadratic-subfield index `p(q+1)/2` are divisible by `(q+1)/2 > 7`. Dihedral indices are divisible by `p^2`. A5 can be maximal only if `p == +/-3 (mod 10)`; for p=5 this condition fails, and for p>=7, p does not divide 60, so an A5 index is also divisible by `p^2`. The A4 and S4 exceptional maximal cases are not present at nonprime q. This proves the table. Each proper subgroup index is a multiple of its containing maximal index, including when the subgroup is not maximal. ∎

By the pigeonhole principle, any three proper subgroup labels, **including repeated labels**, contain two whose indices are divisible by the same one of A,B, so have gcd at least that number, which is >7. Consequently `J_7(PSL(2,q))<=2` and `B_7(PSL(2,q))<=2` throughout Claim A. This is stronger than a projected-shadow assertion: it applies directly to the actual subgroup indices, independently of the chosen actual cosets.

## 4. Elementary perfectness facts for the exceptional cases

We justify the small-index exclusions rather than importing a small-group subgroup table.

For every finite field F_q with `q>=4`, `SL(2,q)` is generated by the upper and lower unipotents `U(s), L(s)`. For example `W(t)=U(t)L(-t^{-1})U(t)` and `W(t)W(-1)=diag(t,t^{-1})`, and ordinary row elimination reduces any determinant-one matrix to a diagonal. Choose `t` with `t^2 != 1`. Then every `U(s)` is the commutator `[diag(t,t^{-1}), U(s/(t^2-1))]`, and similarly every lower unipotent is a commutator. Thus `SL(2,q)`, and its quotient `PSL(2,q)`, are perfect.

A perfect group has no nontrivial homomorphism into a solvable group: its image would be both perfect and solvable. Since S4 is solvable (use `S4 > A4 > V4 > 1`), a perfect group has no proper subgroup of index 2, 3, or 4: its coset action would give a nontrivial homomorphism into S4.

Also A5 is perfect: its 3-cycles generate it, and if c is a 3-cycle, an even permutation interchanging two letters of c and also interchanging the two remaining letters sends c to `c^{-1}`; the corresponding commutator is c. Thus A5 has no subgroups of index 2,3,4. Any group of order 6 is solvable, since its Sylow-3 subgroup is normal and its quotient has order 2.

## 5. The exceptions q=4 and q=9 use actual cosets

### 5.1. `PSL(2,4)`

Let X=`PSL(2,4)`, of order 60. Its perfectness rules out subgroup indices 2,3,4; by Lagrange, the only possible proper indices are among

`5, 6, 10, 12, 15, 20, 30, 60`.

This is an overinclusive index list; it is unnecessary to assert that every displayed index occurs. Consider a pairwise-disjoint family with all index gcds <=7.

* If some index is 5, the coprime-index lemma forces every other index to be divisible by 5. Among indices greater than 5, the possibilities are `10,15,20,30,60`, and there are at most two labels: the four values `10,20,30,60` are all multiples of 10, while 15 contributes at most one. Five index-5 cosets already fill X by density; otherwise there are at most four of them and at most two others. Hence this case has at most six members.
* Suppose index 5 does not occur. Among indices greater than 6, there are at most three labels, since `10,20,30,60` are all multiples of 10 and the only remaining types are 12 and 15. At most six index-6 cosets fit by density, and six fill X. If there are at most four, the total is at most seven. If there are exactly five and three further labels, those three must have indices 12, 15 and one of `10,20,30,60`. Pairwise gcd <=7 excludes 30 and 60, leaving 10 or 20; their total density is at least `1/12+1/15+1/20=1/5 > 1/6`, more than the space remaining after five index-6 cosets. Thus eight members are impossible.

Therefore `B_7(PSL(2,4))<=7`. The index-5 point stabilizer can be repeated as a **label** arbitrarily often, so no finite `J_7` bound holds. This is why the actual disjointness and density argument was necessary.

### 5.2. `PSL(2,9)`

Let X=`PSL(2,9)`, of order 360. The imported maximal list gives maximal indices 6,10,15, and every index-6 subgroup is a maximal A5: a maximal overgroup of such a subgroup has index dividing 6, so it must also have index 6. The group X is perfect by §4.

First, **among pairwise low-gcd labels of indices greater than 6, at most three occur**. At most one index is divisible by 10, and at most one is divisible by 15. Every other index greater than 6 is divisible by 6 but not 5: if a multiple of 6 were divisible by 5 it would be divisible by both 10 and 15. Its subgroup is contained in an index-6 A5, because the other maximal indices 10 and 15 are divisible by 5. Write its index as `6m`; then m is an index in A5 and divides 60. Since 5 does not divide m and m>1, `m in {2,3,4,6,12}`. Perfectness of A5 eliminates 2,3,4, so m is 6 or 12. These remaining original indices are 36 or 72, and at most one label of either kind is possible because their gcd is at least 36. The stated bound of three follows, including all repetitions.

At most six index-6 cosets can be disjoint by density. We now use their **actual arrangement**, not merely their labels.

Take an index-6 subgroup H. It is a maximal A5. Its normalizer is H: a larger normalizer would be X by maximality, making H normal, but X is perfect and `X/H` would have order 6, hence be a nontrivial solvable quotient. In X's action on `X/H`, H fixes only H; every other H-orbit has size at least 5 because A5 has no subgroup of index 2,3,4. Therefore the remaining five points form one H-orbit and the action is 2-transitive.

If H and K are nonconjugate index-6 subgroups, H has no fixed point on X/K: a fixed point would make H a conjugate of K, since both have order 60. Again H has no orbit sizes 2,3,4; six points with no fixed point must form one orbit. Hence `HK=X`, and **every** left H-coset meets every left K-coset. It follows that all subgroups underlying a pairwise-disjoint collection of index-6 cosets belong to the same conjugacy class.

For one such class, use its 2-transitive six-point action. Every relevant coset has the exact form `{g in X: g(x)=y}` for a pair of points `(x,y)`. Two distinct such sets are disjoint exactly when their pairs have the same first coordinate or the same second coordinate. Indeed, if both first coordinates and both second coordinates differ, 2-transitivity supplies an element in both. Any pairwise-disjoint collection of at least three such sets is a single row or a single column: after two distinct cells in a row, a third cell outside that row cannot share both different columns, and similarly for columns.

Thus five disjoint index-6 cosets have as their complement exactly the sixth transporter in that row or column, itself an actual left coset D of an index-6 subgroup K. If two further actual cosets are contained in D, writing their subgroups as `U,V <= K`, their indices in X are `6m,6n` with `m=[K:U]`, `n=[K:V]`. Their low-gcd condition gives `6*gcd(m,n)<=7`, hence `gcd(m,n)=1`. Translating D to K gives two disjoint actual K-cosets of coprime indices, contradicting the coprime-index lemma. So five index-6 cosets leave room for at most one additional member; six leave none. With at most four index-6 cosets and at most three other labels, the total is at most seven.

Therefore `B_7(PSL(2,9))<=7`. Its index-6 A5 is repeatable as a proper **label**, so `J_7` is not finite. Both small exceptions have now been treated as the actual original left-coset problem.

## 6. Normal cuts: a proved consequence and the exact unpaid frontier

The following holds for arbitrary G and normal N, with `Q=G/N`, and is included to preserve the original extension target. It is not an assertion that arbitrary kernels have the stronger bound.

**Conditional extension.** If `B_7(N)<=5` and `J_7(Q)<=2`, then `B_7(G)<=7`. For an eight-family with `gcd(n_i,n_j)<=7`, put `a_i=[Q:pi(U_i)]`, `b_i=[N:U_i intersect N]`; then `n_i=a_i b_i`. At most two a_i exceed 1, because three proper quotient labels would contradict `J_7(Q)<=2` and `gcd(a_i,a_j)` divides `gcd(n_i,n_j)`. At least six quotient image cosets are all of Q; their slices in a common N-fibre are six pairwise-disjoint actual N-cosets of indices b_i with all gcds <=7, contradicting `B_7(N)<=5`. The slices must all be transported by the **same** fibre representative; their subgroups may be conjugated, which preserves their indices and disjointness. This supplies actual extensions with every nonexceptional quotient in Claim A, but not with arbitrary B7-kernels.

**Necessary 6+2 structure under the original kernel bound.** Assume instead `B_7(N)<=7`, `J_7(Q)<=2`, and that an actual bad eight-family exists. Exactly six a_i equal 1 and exactly two exceed 1: with zero or one proper image all eight image cosets have a common quotient point, giving eight bad slices in one N-fibre. Denote the two proper images by A7,A8. They must be disjoint, for otherwise a common point again gives eight bad slices. Consequently

`2 <= d=gcd(a7,a8) <= 7`.

For each `j<=6`, both pairs of images `(Q,A7)` and `(Q,A8)` meet, and the common-fibre slices show `gcd(b_j,b_7)>=2` and `gcd(b_j,b_8)>=2`; these gcds also divide the corresponding original-index gcds and are therefore at most 7. Since `d*e` divides `gcd(n7,n8)<=7`, where `e=gcd(b7,b8)`, either `e=1` and `2<=d<=7`, or `(d,e)` is one of `(2,2),(2,3),(3,2)`. All these are necessary conditions on **actual** cosets, not a realization or a sufficiency theorem. The common fibre may differ between A7 and A8; no simultaneous fibre or Helly property is claimed.

**Exact remaining step.** For a nonexceptional prime-power quotient, rule out or realize an actual eight-family satisfying the preceding 6+2 conditions with `B_7(N)<=7`, genuine coset incidences, subgroup compatibility and all pairwise original-index gcds <=7. The argument here does not do so. Likewise, for quotients 4 and 9 the `J_7<=2` hypothesis fails, so the 6+2 conclusion is not claimed. More generally, neither simple-group results nor this conditional lift establish `B_7(G)<=7` from the two original assumptions `B_7(N), B_7(Q)<=7`, and no converse or gluing of slices is asserted. All non-PSL2 simple groups and unrestricted groups remain outside this candidate.

## 7. Source, experiment, and prospective-gate record

Order actually followed: complete manifest, freeze receipt, parent metadata, actual dispatch receipt and all 15 status-only controls; direct pre-body ACK to Main; complete literal packet LF 1–103 in successive raw windows of at most 20 lines including the ending; then public-source searches/reads and the written derivation. The assigned freeze receipt reports the packet SHA-256 `7e196e7475579438f95040cf2efbf85f6552774080bd7da9566a0aa420296d57`; that is parent-reported metadata, not a claim of a child hash check. Earlier held episodes and all their consumers were NONINPUT. No sister source or review was read. This is an exposure chronology, not a cognitive-separation certificate.

**Child scientific execution: NOT RUN.** No scientific program, solver, enumeration, CAS, test, or numerical experiment was executed. No scientific source file has been authored or run; all displayed numerical arithmetic is part of the written proof. A possible **future, unimplemented** independent finite-source design would construct the two finite groups directly over `F4=F2[t]/(t^2+t+1)` and `F9=F3[t]/(t^2+1)`, represent determinant-one matrices modulo scalar center, enumerate subgroups and actual left cosets with deduplication, and independently check the §5 index and transporter assertions. Such a verifier must include explicit caps and return UNKNOWN on exhaustion, and needs parent admission and audit; no runtime, output, or success is claimed. It would not by itself prove the infinite classification import or the normal-extension frontier.

Before any adoption, independently check: (i) the exact Giudici/Dickson import, including small-q exceptions and p-adic divisibility; (ii) perfectness and each q=4 index/density case; (iii) q=9 maximal-index coverage, cross-class transitivity, same-class 2-transitivity, the five-coset complement and the coprime-index argument; (iv) repeated labels and actual left-coset orientation; and (v) the conditional extension and 6+2 hypotheses. Prospective review and parent disposition have not occurred. No priority or novelty claim is made.
