# Checkpoint 001 — a rational grouped-reference obstruction for W4

Before-creation clock observed: **2026-10-23T12:49:16-07:00**. Evidence state: **CANDIDATE written derivation**, not parent-accepted, numerically tested, finite-verified, or kernel-verified. No scientific program has been run. This is substantive intermediate work toward the unchanged unrestricted W4 target in `selection-v1.md`.

## 1. What changed after selection

The first attack has an explicit finite, rational operator inequality, rather than an invitation to repeat an unconstrained rank-two search. For a maximally entangled reference on two of the three copy slots, the required inverse is elementary and the candidate co-Choi domination splits into **55 exact blocks, each at most 28 by 28**. The central question is whether those blocks are positive semidefinite. It is **not yet answered** here.

A complete proof of this domination would close a universal biseparable-reference family outside the already published fully-product, normal, local-overlap and code-envelope sectors. Section 6 gives an explicit sector-separation example, including its eight hand-derived partial-trace values. A failure of the stronger co-Choi test is not automatically a negative rank-two Werner witness.

## 2. Definitions and the switched order

For one local space `V`, put

`Lambda_V(X)=Tr(X)I_V-(1/2)X`,

`R_V=I_(V⊗V)-(1/2)F_V`.

For any operator map `E`, use

`Jhat(E)=Σ_(a,b) |b><a| ⊗ E(|a><b|)`.

Then `Jhat(Lambda_V)=R_V>0`. Positivity of `Jhat(E)` is complete **copositivity**, not complete positivity. This transpose convention is load-bearing.

For the last two copy slots set `B=V2⊗V3`, `Lambda_B=Lambda_V2⊗Lambda_V3`, and, after the canonical regrouping, `R_B=R_V2⊗R_V3`. Fix a nonzero reference `eta in B`. Define

`A_eta=(<eta|⊗I) R_B (|eta>⊗I)=Lambda_B(|eta><eta|)`,

`L_eta(x)=(<eta|⊗I) R_B (|x>⊗I)=Lambda_B(|x><eta|)`,

`M_eta(|a><b|)=L_eta(a) A_eta^(-1) L_eta(b)^†`.

The equality for `L_eta` follows by expanding the two local swaps. It retains `|x><eta|`, not `|eta><x|`. Since every eigenvalue of `R_B` is at least `1/4`, `A_eta >= (||eta||^2/4)I`; the inverse is always defined. The map `M_eta` is completely positive because its ordinary Choi matrix is a Gram matrix, but its co-Choi matrix need not be positive.

The required switched complement for arbitrary `x` is

`Lambda_B(|x><x|)-M_eta(|x><x|) >= 0`.

The ordinary compression of `R_B` gives the other order, `L_eta(x)^† A_eta^(-1)L_eta(x)`. It does not establish the displayed expression. The imported **two-copy** endpoint theorem does establish the switched expression for each `x`, by applying it to arbitrary rank-two operators with output rays `eta,x` and arbitrary input covectors, then taking the block Schur complement. This proves that `Lambda_B-M_eta` is a positive map. It does **not** prove complete copositivity or permit tensoring it with an arbitrary positive map.

No partial trace has been assumed to preserve rank two.

## 3. A sufficient grouped-reference lemma

Let `C_B=Jhat(Lambda_B)=R_B` and `S_eta=Jhat(M_eta)`. Consider the explicit stronger obligation

**GS(eta):** `-C_B <= S_eta <= C_B`.

This is a sufficient analytical route, not an equivalent reformulation of W4 or of the whole biseparable-reference conjecture.

**Conditional lemma.** If GS(eta) holds, then every rank-at-most-two operator `C` on `V1⊗B` whose range or co-range contains a ray `a⊗eta` has `q_3(C)>=0`.

**Proof.** Local-unitary covariance lets the nonzero first-site vector be `a=|0>`. On that site use the source's one-site maps `Lambda_1,M_0`, with `C_1=Jhat(Lambda_1)>0`, `S_0=Jhat(M_0)`. Its explicit one-site calculation gives `-C_1<=S_0<=C_1`. Thus

`T_1=C_1^(-1/2)S_0 C_1^(-1/2)` and `T_B=C_B^(-1/2)S_eta C_B^(-1/2)`

are Hermitian contractions. Therefore `I-T_1⊗T_B>=0`. Congruence by `C_1^(1/2)⊗C_B^(1/2)` says that

`Lambda_1⊗Lambda_B-M_0⊗M_eta`

is completely copositive, hence positive. The full reference inverse factors as `A_0^(-1)⊗A_eta^(-1)`. Expansion on matrix units shows that applying the positive map to `|x><x|` is exactly the full switched complement

`D_x-L_x A_u^(-1)L_x^† >= 0`, with `u=|0>⊗eta`.

Write any rank-two operator with this range ray as `C=|u><v|+|x><y|`, allowing nonorthogonal covectors. The partial-trace polarization gives `q_3(C)=a+d+2 Re g`, where `a=<v,A_u v>`, `d=<y,D_x y>`, `g=<y,L_x v>`. The switched complement and Cauchy–Schwarz give `|g|^2<=ad`, hence `q_3(C)>=(sqrt(a)-sqrt(d))^2>=0`. Co-range follows from `q_3(C†)=q_3(C)`. The rank-one and scaling cases follow directly. This is the published product-reference argument with one **proved, explicitly stated extra group domination**, not an assumption that positivity tensorizes. End of conditional proof.

The new obligation is GS(eta); the rest is a checked-by-hand reduction using the imported one-site calculation. Until GS is proved and independently checked, no new universal family is established.

## 4. Exact rational data for an entangled reference

Set `V2=V3=C^4`. For `1<=r<=4`, take the unnormalized reference

`Omega_r=Σ_(j=0)^(r-1)|jj>`, and `P_r=Σ_(j=0)^(r-1)|j><j|`.

Scaling eta does not change `M_eta`, so normalization is unnecessary. Direct expansion yields

`A_r=r I_16-(1/2)(P_r⊗I_4+I_4⊗P_r)+(1/4)|Omega_r><Omega_r|`.

For `r>=2`, let `D_r=r I_16-(1/2)(P_r⊗I_4+I_4⊗P_r)`. All its diagonal entries are positive. The rank-one inverse identity gives

`A_r^(-1)=D_r^(-1)-[1/((r-1)(5r-4))]|Omega_r><Omega_r|`.

Indeed `D_r^(-1)Omega_r=Omega_r/(r-1)` and `<Omega_r,D_r^(-1)Omega_r>=r/(r-1)`; substitution into the rank-one inverse formula gives the coefficient shown. For `r=1`, `A_1=(I-P_1/2)⊗(I-P_1/2)` is diagonal and is the already-published product control.

The primary first assay is **r=4**, for which

`A_4=3I_16+(1/4)|Omega_4><Omega_4|`,

`A_4^(-1)=(1/3)I_16-(1/48)|Omega_4><Omega_4|`.

For the matrix-unit reference vector `|ab>`, the required linear operator is

`L_r(ab)=1_(a=b<r) I_16 -(1/2)[1_(b<r) E_ab⊗I_4 + 1_(a<r) I_4⊗E_ba] +(1/4)|ab><Omega_r|`.

Thus, in the ordering `input pair i, output pair p`,

`(S_r)_((i,p),(j,q)) = [L_r(j) A_r^(-1) L_r(i)^†]_(p,q)`.

The reversal of `i,j` is the co-Choi transpose and must not be dropped. All entries are rational. In the r=4 case, **768(C_B+S_4)** and **768(C_B-S_4)** have integer entries; no floating-point or algebraic-number recognition is required to certify their signs.

## 5. Why exact blocks suffice — no guessed sparsity

For every diagonal unitary `U=diag(exp(it_0),...,exp(it_3))`, `Omega_r` is invariant under `U⊗bar U`. Covariance of `Lambda_B` and the definition of `M_r` imply covariance of `M_r` under the same unitary. Consequently both co-Choi matrices commute with

`(U⊗bar U)⊗(U⊗bar U)`.

A basis vector `|a,b,c,d>` has torus character `t_a-t_b+t_c-t_d`. Entries between different weight vectors

`w=e_a-e_b+e_c-e_d in Z^4`

therefore vanish identically. Grouping all 256 basis vectors by their actual integer weight gives the full decomposition. It does not discard cross-weight entries by numerical threshold.

The weight types and block multiplicities are:

| Weight type | Number of blocks | Dimension of each block | Total dimension |
|---|---:|---:|---:|
| 0 | 1 | 28 | 28 |
| `e_i-e_j`, i != j | 12 | 12 | 144 |
| `2e_i-2e_j`, i != j | 12 | 1 | 12 |
| `2e_i-e_j-e_k`, all three distinct, {j,k} unordered | 12 | 2 | 24 |
| Reverse of the previous type | 12 | 2 | 24 |
| `e_i+e_j-e_k-e_l`, all four distinct, each pair unordered | 6 | 4 | 24 |
| **Total** | **55** | **maximum 28** | **256** |

For example, the zero character requires the multisets `{a,c}` and `{b,d}` to coincide, giving `4+2·4·3=28` basis vectors. A single difference has one common cancelled index: the two special cancelled indices each give two orderings, and the other two each give four, giving `4+8=12`. The table counts exhaust all 256 basis vectors.

Exact rational LDL/congruence checks on the full set of these blocks could prove GS(Omega_4). If any block is indefinite, the checker must emit a rational vector with a recomputed exact negative quadratic form. Such a vector falsifies GS, not automatically W4. The full matrix formula and every cross-weight zero should be independently reconstructed by the parent before promotion.

## 6. Strict sector separation, not a claim of a negative witness

Here is a concrete operator showing that the proposed family is not merely the source's fully-product family. Let

`Phi_4=(|00>+|11>+|22>+|33>)/2`,

`u=|0>⊗Phi_4`, `x=(|100>+|211>+|322>)/sqrt(3)`,

`v=|1>⊗Phi_4`, `y=(|200>+|311>+|022>)/sqrt(3)`,

`C=|u><v|+|x><y|`.

Each pair `u,x` and `v,y` is orthonormal, so `rank C=2`, `CC†=P_E`, `C†C=P_F`, where `E=span{u,x}`, `F=span{v,y}`. The subspaces differ (for example `<v,u>=0` while `<v,x>=1/(2sqrt(3))`, so v is not wholly in E), hence C is nonnormal.

Neither E nor F contains a fully product vector. For a vector `alpha u+beta x` with beta nonzero, its three first-site components at labels 1,2,3 contain the independent two-site vectors `|00>,|11>,|22>`, so its Schmidt rank across `1:23` is at least three. For beta zero, u is entangled across `2:3`. The argument for F is the cyclic first-site shift. Thus neither support plane contains a fully product ray.

Every one-site support of E and F is the full C^4: Phi_4 supplies full support at sites 2,3; the first-site supports are respectively `{0}` plus `{1,2,3}` and `{1}` plus `{2,3,0}`. Accordingly each local projector overlap is 4, not at most 2. The one-/two-copy code-envelope condition also fails on every `i:complement` cut, because the minimal one-site support dimension is four, not at most two.

No one-site partial trace vanishes. Hand expansion gives:

| Traced subset J | `||Tr_J C||_HS^2` |
|---|---:|
| empty | 2 |
| {1} | 2/9 |
| {2} | 7/12 |
| {3} | 7/12 |
| {1,2} | 0 |
| {1,3} | 0 |
| {2,3} | 4/3 |
| {1,2,3} | 0 |

For instance `Tr_1 C=(|11><00|+|22><11|)/3`, and `Tr_2 C` consists of `|0><1|⊗I_4/4` plus the three distinct matrix units `|10><20|/3`, `|21><31|/3`, `|32><02|/3`, so its squared norm is `1/4+1/3=7/12`. The third-slot calculation is identical. Tracing 2,3 leaves `|0><1|+(|1><2|+|2><3|+|3><0|)/3`, of squared norm `4/3`.

These give `q_3(C)=2-25/36+1/3=59/36>0`. This is a **written, not independently verified** calibration/coverage example, not a negative Werner witness and not itself a scientific advance. It also excludes the source's local-traceless and crossed locally orthogonal product-code sectors. Its role is to prevent a future GS theorem from being misreported as new if it only restates a listed baseline.

## 7. Current boundary and next bounded question

- W4 for arbitrary complex 64×64 rank-at-most-two operators: **NOT PROVED**.
- Biseparable-reference extension for arbitrary entangled eta: **NOT PROVED**.
- GS(Omega_4): an explicit rational pair of semidefinite inequalities, **UNDECIDED**.
- The conditional bridge, rational formulas, torus decomposition and separation example: **CANDIDATE written derivations**, awaiting parent reconstruction.
- Numerical evidence / exact finite replay / independent model review / Lean kernel proof: **not performed**.

The immediate question is the exact sign of the 55 blocks of `C_B±S_4`, with the r=1 source theorem as positive control and deliberate indefinite matrices as negative controls. A scientific program may be proposed to the parent on a frozen source; **this checkpoint is not authorization to run one**. If the stronger inequality fails, retain the rational obstruction and return to the underlying positive-map/specific-rank-two problem instead of announcing a counterexample to W4.
