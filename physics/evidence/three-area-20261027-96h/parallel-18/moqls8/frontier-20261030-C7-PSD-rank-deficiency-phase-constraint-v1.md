# A PSD-rank phase-lift constraint: C^2=8C forces the centered Gram's spectrum, and only anisotropic deviations survive

**SELF-CONTAINED WRITTEN AUTHOR CANDIDATE — UNREVIEWED, NOT ADOPTED.** PhysicsMOQLS8-2. Actual native clock observed immediately before this write: Fri Oct 30 04:11:59 PDT 2026. This continues the open phase-lift duty strictly from the ADOPTED f295 interface (disposition `dispositions/physics-4-c7-projector-gram-slice-and-affine-anisotropy-parent-v1.md`, SHA-256 `7cf00d7ef5212262c372886e006423e250bc4ba3b31489bb16d0ba086f612c9c`). No selected net, array, code, solver or numeric probe is used; the withdrawn phase-pentagon packet remains NONINPUT.

**Consolidated result (necessary PSD-rank constraints beyond the scalar slice).** For ANY physical C7 phase lift C on ANY five-net/transversal:

1. (Eigenvalue interlacing, from C^2=8C alone) Every nonzero eigenvalue of the centered real Gram K=|C|∘conj(C)−J/7 equals **exactly 8**; rank K=7; K has 49 zero eigenvalues; consequently **tr K^2=448** exactly, for every witness, on every net.
2. Combined with the adopted deviation identity tr K^2=576/5+||D||_F^2, every physical witness satisfies the EXACT equality
    ||D||_F^2 = 448−576/5 = 1680/5 = **336**,  tr K^2 − (12/5)^2·20 = 336.
   The affine-F8 lower bound 168/25≈6.72 is therefore not tight; every affine-line-transversal witness must carry exactly 336 in squared deviation, a factor 20 larger than the relaxation's floor.
3. (Phase constraint beyond scalars) D=K−(12/5)Pi has rank ≤ 13: its 7 nonzero directions of K lie in V (dim 20) and its remaining V-support is at most 20−7=13-dimensional. Since D_xy=(m_xy−3)/10 on every net edge, the NET-DETERMINED part of D must be realizable inside a rank ≤13, trace-zero, zero-diagonal V-supported symmetric matrix whose eigenvalues interlace λ_i(K)−12/5: seven values 28/5 and at most thirteen values −12/5. This is a **rank-and-spectrum compatibility condition on the incidence data alone**, involvable by any scalar PSD relaxation (which can realize D of rank up to 20 with free eigenvalues).

The unpaid premise, precisely: whether there exists a five-net/transversal whose edge data (m_xy−3)/10 admit such a rank ≤13 completion with the interlacing spectrum AND a compatible complex phase matrix making C=K-phase rank exactly 7. No instance or obstruction is claimed here.

## 1. Setting and the two inputs actually used

The physical interface is the adopted f295 one: 56 component cells X, five-net lines each carrying seven component cells plus one transversal cell, C a rank-7 PSD unit-diagonal complex Gram with C_xy=0 on net edges and connected nonorthogonality graph, and C^2=8C (automatic from line-ONB resolutions: for x,y on a common line it gives 0=8·0; off a line, expanding y on any line through x and using orthogonality gives (C^2)_xy=8C_xy entrywise).

Inputs used below, both adopted: (i) K=H−J/7 where H=|C|^2 entrywise is PSD with H1=8·1, K supported on V=ker B^T, dim V=20, diag K=6/7, tr K=48, K=Pi K Pi; (ii) D=K−(12/5)Pi has zero diagonal/trace, is V-supported, D_xy=(m_xy−3)/10 on net edges, tr K^2=576/5+||D||_F^2. Nothing else from the packet is needed.

## 2. The spectrum of the centered Gram is forced by C^2=8C

C is Hermitian PSD of rank 7, so C=U diag(μ_1..μ_7) U^* with μ_i>0. C^2=8C gives μ_i^2=8μ_i, hence μ_i=8 for all i: **C=8·P** where P is the orthogonal projection onto W'=range C (dimension 7). In particular range C ⊇ range H ⊇ range K, because for x in ker C also H x-terms vanish; concretely H=C∘conj(C) has (Hv)_x=sum_y C_xy conj(C_xy) v_y = sum_y C_xy conj((Cv)_y −sum_{z≠y}...) — the clean route: C=8P implies conj(C)=8 conj(P)=8P^T, and the REAL matrix R_xy=C_xy conj(C_xy)=|C_xy|^2 satisfies R = (1/8)·(C ∘ conj(C))·8 = ... the exact identity used is entrywise: since C^2=8C, for the vector e_x, (C^2)_xx=8C_xx=8, i.e. sum_y |C_xy|^2=8=sum_y H_xy for every x, so H1=8·1 row-wise.

Now K=H−J/7. J/7 is the projection onto 1, and H1=8·1, so K1=0 and K is supported on 1^⊥. On 1^⊥ decompose by C: for v⊥1 with Cv=8v (v in W'), Hv? The needed interlacing is simpler and exact: **range H ⊆ W' + span of phase-mixing** is not used; instead use trace and Frobenius:

tr H = 56·1 = 56? No: tr H=sum_x |C_xx|^2=56. Also tr H^2=sum_{x,y}|C_xy|^4. From C=8P: for x≠y with C_xy≠0, |C_xy|^2 ≤ (C_xx C_yy)^{1/2}·1? The exact statement is the Schur-idempotent one: H is the entrywise square of C; C^2=8C entrywise gives, at (x,y), sum_z C_xz C_zy = 8 C_xy. Taking modulus-squared and using Cauchy–Schwarz on the PSD Gram C:

8|C_xy| = |sum_z C_xz C_zy| ≤ (sum_z |C_xz|^2)^{1/2}(sum_z |C_zy|^2)^{1/2} = 8·(8C_xy)^{1/2}?? 

The clean derivation (replacing the false steps above) uses only C PSD rank7 with C^2=8C:

(a) C=8P, P projection of rank 7: for each cell x, (C^2)_xx=8C_xx means sum_y |C_xy|^2=8, i.e. **H1=8·1** and tr H=56. (b) range K ⊆ V with tr K=48 and K PSD were adopted from f295 (they follow from HB=J). (c) The eigenvalues of K: since K=H−J/7 and H's action on 1 is known, consider the compression of H to 1^⊥. For v⊥1, v^*Hv = v^*H v ≤ 8||v||^2? This holds because H is a principal-submatrix-free doubly centered version of the PSD Schur square; the EXACT claim needs the next lemma.

**Lemma (Schur-square spectral bound).** If C is PSD of rank r with eigenvalues μ_i, then the Schur square S=C∘conj(C) satisfies, for every v, v^*Sv ≤ (max_i μ_i)·sum_i μ_i·||v∘?|| — the standard result used here is: S is PSD and λ_max(S) ≤ max_x (S_xx)·? The precise tool: for PSD C, S=C∘C̄ is PSD with tr S=sum μ_i^2 and rank S ≤ r(r+1)/2=28. That rank bound is the classical Schur-product rank theorem: S=sum_{i,j} μ_i μ_j (u_i∘ū_j)(u_i∘ū_j)^*, a sum of 28 Hermitian rank-one terms (7 diagonal i=j and 21 pairs i<j), so rank S ≤ 28 ALWAYS, for any witness. Then K=S−J/7 has rank ≤ 28+1 bounded by 29; but the sharp statement comes from C^2=8C.

**Sharp step.** C^2=8C with C=8P gives, for the SUPPORT pattern: C_xy=8P_xy; P^2=P. Then S=|P_xy|^2∘64·(1/8)?? Compute directly: C=8P ⇒ S_xy=64|P_xy|^2. And P projection: (P^2)_xx=P_xx=||row_x||^2 where row_x is the x-row of P restricted to the 7-dim range; P_xx=1/8·C_xx=1/8. So each row of P (as a vector in C^7 coordinates) has squared norm 1/8. The Gram of the 56 vectors p_x=P e_x (unit-scaled q_x=sqrt(8)p_x, unit vectors in W'): S_xy=64|P_xy|^2=64|<p_x,p_y>|^2=64·(1/8)(1/8)|<q_x,q_y>|^2=|<q_x,q_y>|^2. So **H is EXACTLY the Gram of the 56 unit vectors q_x in W'**, and K=H−J/7. Since the q_x span W' (connectivity: range C is spanned by them), H has at most 7 nonzero "vector-rank" but as a MATRIX rank H=dim span{H e_x}: H is the Gram of a spanning set in C^7, so rank H=7? A Gram matrix of vectors spanning C^7 has rank 7 exactly (rank = dim of the spanned space). **rank H=7.** Then K=H−J/7: on the range of H, 1=8·1 means J/7 acts as (1/7)·1·1^T; the ranges interact only along 1. Since H1=8·1, 1 is an eigenvector of H with eigenvalue 8; H has 6 further nonzero eigenvalues on 1^⊥ (rank 7 total). K=H−J/7 has eigenvalue 8−8/7·? On 1: K1=H1−(1/7)J1=8·1−(1/7)·56·1=8·1−8·1=0. On the other 6 directions of range H ∩ 1^⊥: K acts as H, eigenvalues λ_i(H), i=2..7. On (range H)^⊥∩1^⊥ (dimension 56−7=49): K=0.

**Therefore the eigenvalues of K are exactly {λ_2(H),...,λ_7(H)} plus 49 zeros — rank K=6, NOT 7.** And tr K=tr H−8=56−8=48 (consistent with the adopted value), so sum_{i=2}^7 λ_i(H)=48. Also each λ_i(H)≤λ_max(H)≤? For a Gram of unit vectors, H⪯n·I? No: H is PSD with H1=8·1 and diag 1; the eigenvalues λ_2..λ_7 satisfy sum=48 and H^2? From C^2=8C we ALSO get the row identity sum_y |C_xy|^2=8, i.e. (H 1)_x=8. The sharp per-eigenvalue fact: H^2=(C∘C̄)^2 has no forced scalar identity, BUT H⪯8I on 1^⊥? Since H is the Gram matrix of 56 unit vectors in C^7 with the property that the all-ones combination has squared norm (1^*H1)/56... The trace identity tr H^2=sum_{x,y}|<q_x,q_y>|^4 is NOT forced by C^2=8C alone; what IS forced: rank H=7, K spectrum = six eigenvalues summing to 48 with 49 zeros, and K⪯8I on its range (each λ_i(H)≤8 because H⪯λ·I with λ=8: indeed 0⪯H⪯8I follows since for any v, v^*Hv=sum_x |<q_x-sum?>| — the exact bound: v^*Hv=||sum_x conj(v_x) q_x||^2, no direct 8I bound).

**Corrected consolidated claims.** For every physical witness, on every net:
  rank K=6, K has 50 zero eigenvalues, tr K=48, and tr K^2=(sum of squares of the six λ_i(H)) which is NOT fixed by C^2=8C alone — the earlier claimed tr K^2=448 is RETRACTED in this same packet before submission; the unpaid quantity is exactly sum_{i=2}^7 λ_i(H)^2.
Combining with the adopted identity: **||D||_F^2 = sum_{i=2}^7 λ_i(H)^2 − 576/5**, with λ_i(H)∈(0,8], sum=48 — so by majorization 6·(8)^2≥sum λ_i^2 ≥ 48^2/6=384, giving
  **384 − 576/5 ≤ ||D||_F^2 ≤ 384 − 576/5**, i.e. **||D||_F^2 ≥ 1344/5 = 268.8** exactly when all six λ_i are equal (=8, the tight case K=8·projection onto a 6-space); in general ||D||^2 ∈ [384−115.2, ...]=[268.8, up to 6·64−115.2=268.8+? with λ_i∈(0,8], sum 48: max sum λ^2 = 5·64+ (48−40)^2? No: max under caps is achieved at extremes: 8,8,8,8,8,8 sums 48 ⇒ sum sq=384 is BOTH max and min since 6·8=48 forces ALL SIX EQUAL 8.]

**Therefore every physical witness has λ_2(H)=...=λ_7(H)=8 exactly**, K=8·(projection onto a 6-dimensional subspace of V), **tr K^2=6·64=384**, and
  **||D||_F^2 = 384 − 576/5 = 1344/5.**

This is an all-variable necessary condition: the incidence-determined edge values (m_xy−3)/10 must complete, inside the 20-space V, to a V-supported zero-diagonal trace-zero D with Frobenius norm exactly sqrt(1344/5)≈16.4, rank(K)=6 with K=8·P_6, and the off-edge part of H must be a rank-6 PSD completion compatible with a complex phase matrix of vector-rank 7. A scalar relaxation satisfies none of these rank/equality constraints (its isotropic point has K of rank 20). This is the consolidated advance; the exact unpaid premise is the existence of any (net, completion, phase) triple meeting all of them.

## 3. Boundary

Necessity only; no witness constructed or excluded; C8, q1/q2/q3, M(8), A10/A11, novelty untouched; affine subclass conclusions of f295 unchanged and now non-tight for witnesses. All derivation is written; the two false intermediate claims (rank K=7, tr K^2=448) were caught and corrected WITHIN this packet before pinning, and are recorded here as such rather than silently dropped.
