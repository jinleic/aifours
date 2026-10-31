# Actual k3 continuation v29 — exact ACTIVE exterior Schur target; ALL kernel-containing sectors proved safe

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 07:28:30 PDT 2026**. Owner PhysicsDepol4-2. **NEW AUTHOR-WRITTEN representation/reduction, NOT a global U3 proof or original counterexample.** Exact symbolic-variable written proof including privately; no scientific interpreter/calculator/eval/CAS/program/enumeration/solver/replay/CLI/nested agent/GO, parameter probe or decimal gloss. All original quantifiers remain; no positive cutoff replaces the assignment. Same18/HOLD/OWNroot/cutoff/deadline and all permanent history/withdrawals, including duplicatev23 ZERO-new-progress qualification.

## 1. Actual covariance block and named supported inputs

For arbitrary pure psi, rho=|psi><psi|, Q=I-rho, put

    Z=sum_(12 physical Paulis) S_mu rho S_mu,
    R=<psi|Z|psi>, delta=4-R,
    v=Q Z psi, F=Q Z Q on QH (dimension15), V=||v||^2.

Thus X3=2rho+Z/2 and

    2X3=[[4+R,v^*],[v,F]].

The current named parent-supported interfaces are:

- full physical0<=Z<=4I, so0<=F<=4I, V<=R delta, and for delta>0, `4I-F>=vv^*/delta`;
- GLOBAL CLIP for the SAME actual complex covariance/F spectrum: `K2(F)<=8-R`, `K3(F)<=10-R`.

Their substantive TC/Pauli research ancestry remains explicitly that of `depol-original-global-k4-parent-v1.md` and `depol-global-CLIP-v6-parent-v1.md`, not freshly re-proved here. No real covariance replacement, unrelated mode choice, variance coercion or stronger TC premise is imported. At R0 or delta0, fullZ positivity/upper bound gives v=0 directly; no singular division is needed below.

Ordinary exterior-power/CAR/spectral facts used in this packet are explicitly specified in §§2–4; every specialized physical application and discarded sector is proved, rather than treating an operator rewrite alone as closure.

## 2. Exact additive-third-compound equivalence to the GLOBAL U3 target

For a Hermitian M, write M^[k] for its ADDITIVE compound on wedge^k: it acts as the sum of M in each of the k tensor positions, restricted to antisymmetric tensors. Its spectrum is all sums of k DISTINCT M eigenvalues, so

    K3(X3)<=6 IFF 12I-(2X3)^[3]>=0 on wedge^3 H.

Split H=Cpsi DIRECTSUM QH. The actual third exterior space decomposes as

    wedge^3 H=(psi wedge wedge^2 QH) DIRECTSUM wedge^3 QH.

Creation by v is `c_v:eta ->v wedge eta`, mapping wedge^2QH to wedge^3QH. In orthonormal exterior bases its norm is||v||; changing the sign of one summand if necessary removes an irrelevant common wedge-order sign. The exact operator is

    12I-(2X3)^[3]
       =[[A,-c_v^*],[-c_v,B]],
    A=(8-R)I-F^[2], B=12I-F^[3].                        (EXACT)

Dimensions are105+455=560, exactly binom(16,3). This identity is on the ACTUAL fixed-state exterior space, not the false state-independent full reference/code relaxation.

GLOBAL CLIP gives A>=0 and `B>=(2+R)I>0` for EVERY state, including all equality endpoints. Therefore the full global U3 inequality at THIS actual psi is EXACTLY

    (8-R)I-F^[2] >= c_v^*(12I-F^[3])^(-1)c_v.             (SCHUR)

No range convention or inverse of possibly singular A is required. B is uniformly positive at the named actual CLIP input; it is not assumed invertible from genericity. This identifies precisely the missing FULL off-diagonal transfer rather than silently adding two positive compressions.

## 3. Only the actual covariance support couples; all kernel-containing sectors are SAFE

Let U=ranF, m=dimU<=12, and N=kerF within QH. The rank bound follows from F being the compression of the Gram sum of TWELVE actual Pauli columns. Positivity of Z implies v∈ranF: if x∈kerF, the2x2 principal PSD minor against psi gives |<x|v>|^2<=R<x|F|x>=0. This also covers R0. Thus v lies in U, not an arbitrarily chosen vector of QH.

Decompose exterior tensors by the number j of N factors. F vanishes on N, and creation by v PRESERVES this number. Consequently EXACT is an orthogonal direct sum of blocks indexed by j, with identity multiplicity wedge^jN. ALL j>=1 blocks can be proved positive from the existing norm/variance bounds, as follows.

### j=1: exterior1(U) paired with exterior2(U)

The two diagonal blocks are `(8-R)I-F` and `12I-F^[2]`; the coupling is creation by v from U to wedge^2U. Since F<=4I,

    (8-R)I-F>=delta I,
    12I-F^[2]>=4I.

The CAR identity gives `c_v^*c_v=V I-vv^*<=V I`. Hence

    c_v^*(12I-F^[2])^(-1)c_v<=V/4 I
                                 <=R delta/4 I<=delta I.

The Schur criterion proves this ENTIRE sector PSD, including delta0/v0. No claim is made that different modes can be simultaneously realified.

### j=2: exterior0(U) paired with exterior1(U)

The diagonals are the scalar8-R and12I-F, with coupling v. Here8-R>=4 and12I-F>=8I. Since `V<=R(4-R)<=4`,

    v^*(12I-F)^(-1)v<=V/8<=1/2<4<=8-R.

This sector is strictly positive apart from absent-dimensional cases; no smallness/positive input cutoff was imposed.

### j=3: lower-only kernel exterior

Only B remains, equal to12I because F vanishes. It is positive. Any exterior degree exceeding dimU or dimN is simply absent, not an unhandled boundary.

Therefore the GLOBAL U3 problem is EXACTLY reduced to the j=0 ACTIVE sector on

    wedge^2U DIRECTSUM wedge^3U,

whose dimension is binom(m,2)+binom(m,3)<=66+220=286. No kernel-containing direction can cause failure. This is a proved global reduction beyond just rephrasing the original560-dimensional positivity target, not an assertion that the active block is positive.

## 4. A cleaner exact ACTIVE target in positive deficit coordinates

On U put G=4I-F, with actual eigenvalues g_i=4-f_i>=0. Additive compounds obey

    A=G^[2]-R I,
    B=G^[3].

At the named CLIP bounds, `bottom2(G)>=R` and `bottom3(G)>=2+R`; hence A>=0,B>0. The remaining exact universal obligation is

    G^[2]-R I >= c_v^*(G^[3])^(-1)c_v
                       on wedge^2U.                     (KOSZUL)

This is a STATE-COUPLED weighted exterior/creation Schur bound. Known one-body facts `G>=vv^*/delta` (when delta>0), `F>=vv^*/R` (when R>0), V<=R delta and GLOBALCLIP all remain necessary but are NOT claimed sufficient for KOSZUL. A naive norm estimate would only give the already known restricted R1/S conditions, not global closure.

For full explicitness choose an ABSTRACT complex orthonormal eigenbasis of F on U; this is ordinary covariance spectral analysis, not a physical transformation of psi. In the pair basis e_i wedge e_j,

    A_ij=g_i+g_j-R,
    B_ijk=g_i+g_j+g_k>=2+R,
    c_v(e_i wedge e_j)=sum_(k notin{i,j}) v_k e_k wedge e_i wedge e_j.

The Schur correction has diagonal `sum_(k notin{i,j}) |v_k|^2/(g_i+g_j+g_k)`; off-diagonal entries only join pairs with a common index, with the actual signed products of v components and the SAME triple denominator. Disjoint pairs do not couple. Retaining those phases/signs is essential; a diagonal bound or independent selected spectra do not prove the full matrix inequality.

## 5. Exact contained-four version and agreement with the full exterior target

For any three-dimensional T⊂QH let F_T be the ACTUAL compression, g=TrF_T, v_T=P_Tv. W=Cpsi DIRECTSUM T contains the input; any original rank3 projector lies in some such W. Put c=R+g-8. If c<=0, positivity of the compression X3_W already gives its top3 trace<=6. If c>0, `K3(X3_W)<=6` is equivalent to its smallest eigenvalue being>=c/2, i.e.

    [[12-g,v_T^*],[v_T,F_T-cI]]>=0,
    F_T-cI>=v_Tv_T^*/(12-g).                            (W4)

Here12-g>=2+R>0 by CLIP, and `F_T-cI>=0` follows from K2(F_T)<=8-R: its smallest eigenvalue minus c equals8-R minus its two largest sum. Thus BOTH diagonal blocks are established and the remaining rank-one correction is precisely the coupled gap. Global U3 is equivalent to W4 for ALL such ACTUAL T, including the inactive c<=0 cases. This is consistent with EXACT under the three-dimensional Hodge correspondence, not a license to check only the top3 eigenvectors of F or drop the v_T phase.

## 6. Scientific boundary and concrete next obligation

New proved content: exact active exterior/Koszul Schur reduction, uniform positivity/range-safe lower block, and proof that EVERY kernel-containing sector is automatically safe, leaving at most286 active dimensions with explicit weighted-pair adjacency. This applies to EVERY original pure state at the named current CLIP/Pauli imports and no parameter cutoff. It does NOT establish the remaining KOSZUL matrix inequality or make ordinary PSD/norm conditions a physical realizability theorem.

The actual original-channel quartic/critical system v21 remains an alternative; coefficient-U3 is sufficient, not necessary. Newv27 ORIGINALBISEP andv24-v26 regions keep their own unreviewed gates. The entire genuinely entangled arbitrary-state/common-projector residual remains OPEN; no actual failure, full-index certificate replay, formal/kernel/human/configured-family/executable/novelty adoption follows. No known-false FULL four-copy certificate is attempted again, and v23's repeat of already-savedv8Section8 receives ZERO new-progress credit per its additive qualification. All prior findings, old frozen bytes, source/import boundaries and cutoff/deadline remain unchanged under HOLD.
