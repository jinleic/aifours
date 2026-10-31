# PH7 is impossible at b²/(a-c)²=8/9: the minimum PH order there is exactly 8

**NEW ALL-TOPOLOGY THEOREM CANDIDATE deciding the original math-1 point question, conditional on its named imports.** Written proof; exact SymPy identity checks, an exact integer Bernstein certificate and an independently implemented standard-library replay for the algebraic core; an exact rational regression check of the new symmetrization identity. **Not independently reviewed.** Parent adoption, disjoint scientific review, formal proof and novelty clearance are pending. MathResearch96h-2, original math-1. Actual native clock observed before writing: **Thu Oct 29 05:04:02 PDT 2026**.

## 1. Statement

Fix any c,d>0, put a=c+d and b²=8d²/9 (so z=b²/d²=8/9), and

    H(s)=c(a²+b²)² / [(s+c)((s+a)²+b²)²].

**Theorem.** H has no phase-type representation with at most seven states.

**Corollary.** Together with the retained eight-state construction (`proof-eight-state-cubic-cancellation-v1.md`, SHA256 `e110dd1fa23bdec2f7a2498e98b3dbfe31a645496f2f94641a97e3599b7b137a`, the "upper8" import of the round), the minimum PH order of H at z=8/9 is **exactly 8**. The previously retained lower bound (`proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`) is subsumed.

Only the single critical ratio z=8/9 is decided. The constants below are those of z=8/9; the method's crude system is numerically feasible for z up to at least 0.87 (diagnostic, Section 6), so it does not decide intermediate ratios.

## 2. Imports

1. **PH caller (irreducibility/SCC theorem)** `frontier-20261028-ph7-global-irreducibility-v1.md`, SHA256 `729926c5fa9779ec4b1ca27156f80c4ca80c49c973ca4c7cbf352da614a94b49` (the parent reported an independent reconstruction, f61, 0F/0M/1m). For z>1/2 a PH representation with at most seven states has exactly seven states and an irreducible generator T; `G=(T+cI)/d` is an irreducible 7x7 Metzler matrix with spectral bound0 and

        det(yI-G) = y[(y+1)²+8/9]² (y²+p y+q).

   All non-Perron eigenvalues of irreducible G have negative real part, so **p>0 and q>0**.
2. **Algebraic core:** Sections 3-4 of `frontier-20261029-ph7-critical-no-two-cycle-exclusion-v1.md`, SHA256 `46659f60be21537f02d6ea76ceac3be2b89a7a55c3d2b1e8f249c7c315383745`, which prove the following purely algebraic statement (Lemma C) using the pinned girth-four positivity certificate (Qpol>0, Hpol>0 on all six nonnegative rates; parent-reported review f129, 0F/0M/4m) and a new exact three-parameter certificate (1653 leaves) with an independent stdlib replay.

**Lemma C (no seven positive reals pass the crude system).** For seven positive reals `v_1<=...<=v_7` with elementary sums `e_k`, put `S4=v_1+v_2+v_3+v_4`, `p=e1-4`, `q=e2-4e1+74/9`, `E4=e3-4e2+(74/9)e1-28/3`, `E3=e4-(70/9)e2+(212/9)e1-1007/27`. Then the four conditions

    p>0,   q>0,   E4>=0,   E3-E4*S4>=0

cannot hold simultaneously. (In the cited manuscript the v's are diagonal escape rates, but Sections 3-4 use nothing beyond these four conditions on seven positive reals.)

## 3. Geometric symmetrization

Let `u_i=-G_ii>0`. Define the symmetric matrix S by `S_ii=G_ii` and `S_ij=sqrt(G_ij G_ji)` for i!=j. Let F be the undirected graph of bidirected pairs (`G_ij G_ji>0`).

**Lemma 1 (spectral bound).** All eigenvalues of S are real and negative. Write `0<ut_1<=...<=ut_7` for the eigenvalues of `A:=-S`.

*Proof.* Take c0>=max u_i, P=G+c0 I>=0 irreducible with Perron root c0, and positive right/left Perron vectors r,l. With `Dg=diag(sqrt(l_i/r_i))`, the matrix `M=Dg P Dg^{-1}` has `v=sqrt(l∘r)>0` as both right and left Perron vector, so `M_s=(M+M^T)/2` is nonnegative, symmetric, irreducible and `M_s v=c0 v`; hence `rho(M_s)=c0`. Now `S+c0 I` has the same diagonal as M and off-diagonal entries `sqrt(P_ij P_ji)=sqrt(M_ij M_ji)<=(M_s)_ij`. If `S+c0I != M_s`, strict Perron monotonicity for the irreducible `M_s` gives `lambda_max(S)+c0<c0`. If `S+c0I=M_s`, AM-GM equality forces M symmetric, so G is similar to a symmetric matrix and has real spectrum, contradicting the eigenvalues `-1±i sqrt(8/9)`. □

**Lemma 2 (cover identity).** Call a directed cycle of G *one-way* if it uses an edge whose reverse is absent; for an undirected cycle Γ of F of length>=3 let `w+_Γ, w-_Γ` be the weights of its two orientations in G. Define EXTRA cycles: one-way cycles C with `omega_C=w_C>0`, and virtual cycles Γ with `omega_Γ=(sqrt(w+_Γ)-sqrt(w-_Γ))²>=0`. Every extra cycle has at least three states, and

    det(yI-G) = sum_L prod_{C in L}(-omega_C) det((yI-S)_{V minus cup L}),

over sets L of pairwise vertex-disjoint extra cycles.

*Proof.* Expand both determinants over sets of disjoint directed cycles, each cycle contributing minus its weight and each uncovered state a factor `y+u_i`. 2-cycles have the same weight `G_ij G_ji` in G and S. A directed cycle of length>=3 using only bidirected edges is an orientation of some Γ; in G the two orientations have weights `w±_Γ`, in S both have weight `s_Γ=sqrt(w+_Γ w-_Γ)`. One-way cycles occur only in G. For a fixed set of disjoint underlying cycles, summing over orientations gives `prod_Γ(-(w+_Γ+w-_Γ))=prod_Γ(-(2s_Γ+omega_Γ))` in G versus `prod_Γ(-2s_Γ)` in S. Expanding the product, each Γ either becomes a virtual extra cycle (factor `-omega_Γ`) or reproduces its two S-orientations; regrouping by L gives the identity. □

**Lemma 3 (coefficients).** Since extra cycles have at least three states and two disjoint ones at least six,

    [y^6]=e1(ut),  [y^5]=e2(ut),  [y^4]=e3(ut)-W,
    [y^3]=e4(ut) - sum_{|C|=3} omega_C tr(A_{V minus C}) - C4,

where `W=sum_{|C|=3} omega_C>=0`, `C4=sum_{|C|=4} omega_C>=0`, and `det((yI-S)_U)=det(yI+A_U)` has `y^{|U|-1}` coefficient `tr(A_U)`.

**Lemma 4 (Ky Fan).** For the real symmetric A and any four states J, `tr(A_J)>=ut_1+ut_2+ut_3+ut_4=:S4(ut)`.

## 4. Proof of the theorem

Suppose a PH representation with at most seven states exists. Import 1 gives G with p>0, q>0. Matching Lemma 3 with `y[(y+1)²+8/9]²(y²+py+q)` gives

    p=e1(ut)-4,   q=e2(ut)-4e1(ut)+74/9,
    E4(ut)=W>=0,
    E3(ut)=sum_{|C|=3} omega_C tr(A_{V minus C}) + C4 >= W*S4(ut)=E4(ut)*S4(ut),

using Lemma 4 for every three-state extra cycle and `omega_C>=0`. By Lemma 1 the seven numbers `ut_k` are positive. These are exactly the four conditions of Lemma C, a contradiction. Hence no such representation exists. □

The graph of G was never restricted: 2-cycles, reversible or non-reversible bidirected cycles, one-way cycles of every length and any edge count are covered. The earlier owner candidates `frontier-20261029-ph7-critical-no-two-cycle-exclusion-v1.md` (empty F) and `frontier-20261029-ph7-critical-reversible-bidirected-part-exclusion-v1.md` (SHA256 `60e464a4835e90f30803b1f83b35d197081349d345d796868b3db2210c6f8a7f`, reversible F) are the special cases with no virtual cycles.

## 5. Actual checks

Algebraic core (imported, unchanged): checker `frontier-20261029-ph7-no-two-cycle-reduction-check.py` SHA256 `6c88f6707f9af73b77de262b8704dabe1fafcf968ebe1a705234aee72960c93c` (identities PASS, girth-four digests rebound, 1653-leaf exact cover PASS); certificate `frontier-20261029-ph7-no-two-cycle-residual-certificate-v1.json` SHA256 `45256245ecda8aed8ec18150c642fd70c3665cd9af31c49dc59fb25e367ed6be`; standard-library replay `frontier-20261029-ph7-no-two-cycle-integer-replay.py` SHA256 `abaa152c15444dbe7333465f65fc873533399366bfb9ad870f77281ec10a80a3` (PASS); girth-four certificate SHA256 `b2674b8221205230df969c205c0975486c2079202c896f6d4e37f4c6269e87d8` with checker `8f5fc02b87996bbda2ea8b7af1976b467ef3c9a46c3a9b9274e538eea941e1c4`, replay `ac5b069e3d4d5c108b9b9a6e3df12172f5bc360390f92c119a0af58e48116177`, boundary check `03d2853e583ddb5284eb2d5a35a0bae063ab1b104df40350a5283128359ee204`.

New regression check `frontier-20261029-ph7-symmetrization-identity-check.py`, **90LF/4604B**, SHA256 `ee662d4b790425c5099d3d3793f47da4b5066c4873b0c75e9e0926b45e3acc5f`. It builds eight seeded random rational 7x7 Metzler matrices of densities0.35-0.8 whose bidirected pairs have square products (so S and every omega are rational), enumerates all extra cycles (up to 481, including 21 virtual), and verifies the FULL polynomial identity of Lemma 2 (all eight coefficients) EXACTLY; floating diagnostics confirm `s(S)<=s(G)` and nonnegative Ky Fan slack. It actually printed

    PASS: exact geometric-symmetrization cover identity on all seeded trials

This is regression evidence for the written Lemma 2, not its proof. In the owner kernel (diagnostic only, not a premise) the coefficient identities of Lemma 3 were also confirmed to 1e-14 on 300 random graphs and on a numerically constructed actual realization at z=0.78.

## 6. Scope, diagnostics and review targets

- Decided: the single critical ratio z=8/9 for every c,d>0. Not decided: the minimum order on (0.82042..., 8/9) or elsewhere. Kernel diagnostics (not premises): the crude system of Lemma C with z-dependent constants has feasible points for z up to at least 0.87 (Nelder-Mead from many starts), consistent with the separately constructed PH7 band up to about 0.82042; so the crude method alone cannot reach below roughly 0.87.
- A disjoint full review should reconstruct: Lemma 1 (Perron vectors, AM-GM comparison, strictness); Lemma 2 (orientation pairing and regrouping, sign conventions, the virtual weight); Lemma 3 coefficient extraction; Ky Fan; the matching of p,q,E4,E3; and the whole imported algebraic core (cases a-d, Qpol/Hpol, the three-parameter certificate and its compactification).
- Imports remain separate gates: the irreducibility caller, the girth-four certificate, the retained upper8 and the no-two-cycle core are cited, not re-proved here.
- No formal/Lean/kernel, human, cross-vendor, executable-certificate, novelty or priority acceptance is claimed. Historical holds and process findings are unchanged and are not premises; no historical result is repaired.

END - no PH representation with at most seven states exists at b²/(a-c)²=8/9; with the retained PH8 the minimum order there is exactly 8.
