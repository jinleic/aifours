# Arbitrary-core completion bridge; an exact fixed-core obstruction

**WRITTEN AUTHOR CANDIDATE + EXACT FIXED-OBJECT COMPUTATION, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 09:23:12 PDT 2026.

**Result boundary.** Sections 1–3 give a completion criterion for an arbitrary K5,5,5 core, including non-diagonal cores. Section 4 proves that the particular three-quadrant core of the adopted five-transversal QLS(10) has no completion in its designated Z2-quotient embedding. This does **not** use Theorem C or classify other cores. An actual non-diagonal exact core has **NOT BEEN PRODUCED**; consequently no such core has been completed. The original maximal 1-RQLS(10) problem remains OPEN.

## 1. Core data without a covariance hypothesis

Let A, B, C be disjoint sets of size 5. Suppose the 75 unit vectors

- a_ab for (a,b) in A×B;
- b_ac for (a,c) in A×C;
- c_bc for (b,c) in B×C

lie in H = C^10 and form an orthonormal basis at each vertex of K5,5,5. The letters a_ab, b_ac, c_bc denote vectors, not coordinates or phase parameters. No flatness, number field, symmetry, common diagonal action, sector split, or repeated-ray assumption is made.

We seek a Z2-quotient 1-RQLS(10) whose selected contexts R0, C0, T1 are precisely these stars, with A=R0, B=C0, C=T1. The remaining row, column and symbol sets R1, C1, T0 each have size 5.

An *orthogonal perfect matching* of AB is a set of five AB edges meeting every A and B vertex once, whose five vectors are pairwise orthogonal. Define orthogonal perfect matchings of AC and BC similarly. An *orthogonal one-factorization* is a partition of the 25 edges of one pair into five such matchings.

**Necessary first filter.** Each of AB, AC and BC must admit an orthogonal one-factorization.

*Proof.* In the completed array:
- a T0 class meets Q00=R0×C0 in five AB cells, one at each A row and B column;
- a C1 column meets Q01=R0×C1 in five AC cells, one at each A row and C=T1 label;
- an R1 row meets Q10=R1×C0 in five BC cells, one at each B column and C=T1 label.

Each five-set lies in a global orthonormal basis, so it is orthogonal. The five T0 classes, C1 columns and R1 rows partition the respective edge sets. ∎

Thus the missing quadrant is not the first decision: the three required one-factorizations must be found first. Replacing them by predetermined cyclic or affine matchings would impose an additional hypothesis and is not legitimate for an arbitrary core.

## 2. General completion theorem

Choose orthogonal one-factorizations:

- (M_t^AB) indexed by t in T0;
- (M_j^AC) indexed by j in C1;
- (M_i^BC) indexed by i in R1.

Put Z_t=span{a_ab: ab in M_t^AB}, W_j=span{b_ac: ac in M_j^AC}, V_i=span{c_bc: bc in M_i^BC}. These all have dimension 5.

For each missing cell (i,j) define D_ij=(V_i+W_j)^perp, and for a proposed T0 label t define D_ijt=(V_i+W_j+Z_t)^perp.

**Theorem (necessary and sufficient).** A completion with these three one-factorizations exists if and only if there are:

1. a Latin square ell:R1×C1→T0; and
2. unit vectors d_ij in D_ij, with d_ij perpendicular to Z_{ell(i,j)}, such that the five vectors d_ij are orthonormal in every fixed i row, every fixed j column, and every ell-class.

For maximal cardinality one must additionally require all 100 rays (the given 75 and the 25 new ones) to be pairwise non-parallel.

*Necessity.* The five known Q10 vectors in missing row i span V_i, so every missing vector in that row lies in V_i^perp. The analogous C1-column condition gives W_j^perp, and the analogous T0 condition gives Z_{ell(i,j)}^perp. The unknown block's rows, columns and classes must themselves be orthogonal five-sets. The Latin property of the resolution square gives condition 1.

*Sufficiency and explicit placement.* Put AB edge ab in cell (a,b). Put AC edge ac in column j exactly when ac belongs to M_j^AC. Because each M_j^AC is a perfect matching, every such column contains each A row and each C label once; assign this cell its T1 label c. Put BC edge bc in row i exactly when bc belongs to M_i^BC, again with T1 label c. Put d_ij in the missing cell with T0 label ell(i,j), and give AB cells the T0 label indexing their matching. This is a Latin resolution square: the matching properties ensure the three already filled blocks are Latin, and ell ensures the fourth is Latin. The original stars give all R0, C0, T1 bases. Each remaining basis is an orthogonal five-set in V_i, W_j or Z_t together with an orthogonal five-set in its five-dimensional orthogonal complement; hence it is an ONB of H. ∎

This theorem is a reduction, not a claim that its conditions can always be met.

## 3. The forced-line case is a finite exact decision problem

Suppose dim D_ij=1 for every i,j. Choose one unit representative f_ij on each line; cell phases have no effect on the following tests.

- If a D_ij is zero-dimensional, the chosen one-factorizations have no completion.
- Otherwise, first check pairwise orthogonality of the f_ij within rows and columns. If a pair fails, there is no completion.
- For each cell define its allowed-label set A_ij={t: f_ij is perpendicular to Z_t}.
- For each t, declare cells (i,j) and (i',j') incompatible for t when their rays are not orthogonal.

**Finite criterion.** A completion exists exactly when there is a Latin square ell with ell(i,j) in A_ij and no incompatible pair of cells carrying the same t. For maximal cardinality also check the 100-ray non-parallelism condition.

This follows directly from Section 2, since each missing ray is now forced. With algebraic core coordinates, null spaces, orthogonality, non-parallelism and the finite Latin-square search can all be evaluated by exact arithmetic. If some dim D_ij exceeds 1, the forced-line conclusion does not apply: vector choices remain and must not be silently replaced by one selected representative.

## 4. Exact application to the adopted QLS(10) core

Here the input is specifically Q00, Q01 and Q10 of the 100-ray QLS(10) adopted in f163, with the phase literals printed in `frontier-20261029-quantum-mann-dichotomy-addendum-1.md` (SHA-256 `caba356039f35b823d469f11956e771d04b55ca82ed69095e7ea158c0c4f5375`). This is not a claim about every core in a phase family, nor an assertion that this core is identical to the differently phased Theorem B core.

A new certificate establishes the two properties needed for the completion reduction:

- `frontier-20261029-fixed-core-completion-certificate-v1.py`: SHA-256 `befbebb94134a28e20d3e66a236201e598539fed7e1c0a8179163eaadeee39ee`, 173 LF;
- its exclusive-create output `frontier-20261029-fixed-core-completion-certificate-v1.json`: SHA-256 `27ed51f8147a691bd9c6045c545f1171cb109ca889a93287fce1efb2a86f8857`, 1211 LF;
- observed run: Thu Oct 29 09:22:24 PDT 2026; status `EXACT_FIXED_OBJECT_FILTER_PASS_NOT_A_UNIVERSAL_NO_GO`.

**Matching census.** For each edge class, all 120 bijections between its vertex parts were checked by reduction of inner products modulo Phi20=x^8−x^6+x^4−x^2+1. Exactly five orthogonal perfect matchings exist. They partition the edge class, so its orthogonal one-factorization is unique up to ordering:

- AB: the original Q00 cells with s+t=k;
- AC: the original Q01 cells with t=k;
- BC: the original Q10 cells with s=k.

Thus the three necessary one-factorizations force the same grid placement as the adopted QLS(10), up to relabeling R1, C1 and T0. No untested Latin square of order 5 is discarded by this step.

**Forced missing rays.** For each of the 25 missing cells, take the ten known vectors in its BC row-matching and AC column-matching. Their span has rank exactly 9:

- upper bound 9: the corresponding nonzero Q11 vector from the printed data is exactly orthogonal to all ten, checked by Phi20 reduction;
- lower bound 9: a recorded 9×9 minor is nonzero modulo 41 under zeta20↦2. The script verifies 2 has order 20 and satisfies Phi20 modulo 41. A nonzero image of the minor implies that the algebraic-integer minor is nonzero in Q(zeta20). Every minor's row indices, column indices and residue are printed in the output.

Hence every D_ij is one-dimensional. Since the adopted Q11 vector lies on it, every row-and-column completion has exactly the same 25 missing rays as the adopted QLS(10).

**Fixed-core non-completion consequence.** The adopted f163 census states that this full array has exactly five orthogonal transversals, namely the T1 classes. Therefore no T0-class orthogonal transversal can be added. Consequently the chosen 75-ray core cannot be completed to a Z2-quotient 1-RQLS(10) in its designated embedding, even allowing arbitrary completion vectors and arbitrary resolution Latin squares compatible with that embedding.

This last deduction imports only the adopted five-transversal census and the new matching/rank facts. It does not import Theorem C, the m=7 search, a floating residual, or any purported classification of all cores.

## 5. Actual non-diagonal-core frontier

**Status: NOT_PRODUCED.** No exact core outside the adopted diagonal family has been supplied here, and none is claimed by changing its labels or global basis.

The fivefold-covariant numerical searches did find machine-precision cores, but their initially large defects under one particular second translation were misleading: each of six examined cores has a different independent vertex shift preserving its magnitude Gram matrix, after an allowed relabeling of C. These are not evidence for a genuinely non-diagonal core. They were not promoted to exact witnesses.

The unrestricted, Heisenberg and cyclic-three searches did not produce a usable non-diagonal exact object. Their nonzero minima are search failures, not exclusions. No claimed universal obstruction follows. A genuine next input is an actual non-diagonal core with pinned original vectors, followed by all three orthogonal-matching censuses and the intersection test of Sections 1–3. Without that input, claiming a non-diagonal completion would fabricate the missing step.

## 6. Additive claim corrections and limits

- **Weyl(Z10) stays NUMERICAL/OPEN**, as required by Main and the separate erratum `frontier-20261029-group-regular-covariance-no-go-erratum-1.md` (SHA `7236ec32…65150`). A residual of 0.0523 is not an exclusion.
- The 60-digit mpmath Galois-norm replay `frontier-20261029-norm-test-independent-replay-v1.py/.json` is an independently implemented **numerical cross-check**, not an exact zero certificate: that script supplies no rigorous interval or rounding-error enclosure. Earlier descriptions of it as an independent exact/Galois-norm verification are withdrawn, including that interpretation of its reference in the MINOR-fix addendum. The f163 disposition rests on its own exact checkers and parent reconstruction; the new certificate in Section 4 uses integer arithmetic, not that mpmath test.
- The numerical Jacobian nullity 202 minus gauge 199 is only a tangent-space observation. The statement in `frontier-20261029-checkpoint-unrestricted-solvers-v1.json` that it proves "No deformation room exists to gain a sixth transversal" is withdrawn. A numerical tangent count alone proves neither local classification nor a global obstruction.
- Theorem C and the m=7 flat-diagonal search remain outside f163's adopted scope. No inference in this packet requires them.
- Named imports: elementary finite-dimensional linear algebra; the Latin/perfect-matching axioms; cyclotomic polynomial reduction; reduction of a nonzero finite-field minor; and the previously adopted exact five-transversal census. No formal-kernel proof, independent-model-family review or novelty clearance is claimed.
