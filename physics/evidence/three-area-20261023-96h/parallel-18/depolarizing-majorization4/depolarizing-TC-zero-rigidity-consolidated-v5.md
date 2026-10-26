# Actual TC-zero rigidity: the entire degenerate pure-state locus and its full channel comparison

Actual `/bin/date` before this freeze: **Sun Oct 25 09:57:42 PDT 2026**. Owner PhysicsDepol4-2 / physics-2. **NEW WRITTEN CANDIDATE**, fresh independent reconstruction and parent disposition pending. ONE consolidated successor after the returned v67-C review and substantive original-primary continuation. No pinned predecessor is edited.

**New whole-locus theorem:** for an ACTUAL pure four-qubit state,

`epsilon=<L²>-6R+8-4C=0`

IFF, up to physical local unitaries and a qubit permutation, the state is one arbitrary pure TWO-qubit state tensor TWO pure single-qubit states. This is a classification of the ENTIRE equality locus, not an imposed input ansatz.

On this whole locus the actual centered Pauli spectrum is

`spec Gamma=(2,2,2,2,delta,0 repeated7)`,

`delta=4-R in[0,2]`.

Thus CLIP and ALL containing ranks2/3/4 hold there, with strict nonproduct containment margin. In fact a direct X3 spectrum proves the ORIGINAL output-majorization comparison for EVERY physical p and EVERY index on this locus and its specified pure-state convex hull.

**The original unrestricted target remains OPEN.** Any actual pure counterexample must now have STRICT epsilon>0; no positive lower cutoff on epsilon is imposed. CLIP and the full remaining d>0 quartics are NOT proved on that strict region.

## 1. Current authority, correction and exact science boundary

The0853 primary scope remains the whole actual low-noise k2/3/4 problem. Its separate ACK was written before that primary push. Actual v67-C Hall review was completed and returned to Main at the09:41:20 observation BEFORE this new primary work.

Current parent sources were actually read completely:

- `depol-rank2-containment-parent-v1.md`,28LF, SHA256 `c923177f2624ceb8d9cd4c93e4d1d79259201ec691ec06bb23a56ccc233b40cf`;
- `depol-polarized-positive-block-parent-v1.md`,26LF, SHA256 `26b13513c72382d57396c344bb184fb57c219258ec456d893cd180e75d631af7`;
- its H-Hermiticity addendum,13LF, SHA256 `26f4344d016be8af54f43d1719eebdb421d4841688272ec816d23429499616e3`.

The author additive H correction has SHA256 `3450b2d4922a345833a1c2c0cd3ff30f8bf14ac2887b3533d2b2cac6a33887f5`. The actual h=Gr is REAL since the local antisymmetric contraction of r with itself vanishes; hence H*=H. The pinned v4 wording “generally NONHERMITIAN” is withdrawn by that additive record. Its block/trace formulas remain correct and simplify; no original bytes or review chronology is changed.

Mandatory v9 and additive v10 were read in their required order for v67, and their existing scope/HOLD remains. V10 does not backdate a new mathematical restriction. No scientific interpreter/eval/arithmetic or symbolic program, enumeration, solver, sampling/interpolation, replay, compile, launch, CLI, nested agent, Git mutation/deletion or GO was used. All deductions below are written exact finite-dimensional algebra; machine operations are source/clock/hash metadata only.

The accepted boundary retains ENERGY/FACE, exact scalar noise elimination, whole rank-two containment and pure BRIDGE. The new theorem below does NOT promote those to arbitrary rank3/4 containment or all-state d>0 quartics.

## 2. Actual fields and why the degenerate locus must be handled structurally

For pure rho=|psi><psi|, S_mu are the twelve local Hermitian Paulis and

`r_mu=<S_mu>`, `R=sum r_mu²`, `L=sum r_mu S_mu`,

`C=|psi^T(sigma_y^tensor4)psi|²`,

`G_(mu,nu)=<S_mu S_nu>`, `Gamma=G-r r^T`,

`Q=I-rho`, `v=QLpsi`, `F=QZQ`, `A=QLQ`, `delta=4-R`.

For any ACTUAL complex rank-k orthogonal projector Pi, k=2,3,4, retain the original unnormalized-identity maps `X_j=sum_(|I|=j)rho_I tensor I_(I^c)` and the SAME-pair coordinates

`a=3k+1-Tr(Pi X1)`, `b=3k+3-Tr(Pi X2)`,

`c=Tr(Pi X3)-(k+3)`, `d=1-Tr(Pi rho)`.

The full low-noise interval remains0<p<2/3, with the physical channel `D_p(A)=(1-p)A+(p/2)Tr(A)I`. No containing-projector assumption is imposed outside the explicitly named containment conclusions.

Z=sum S_mu rho S_mu and actual pure Schmidt duality gives Zpsi=Lpsi. The corrected polarized gradient simplifies EXACTLY to

`g=Q[L²+2ZL-12L-8tilde(rho)]psi`.

Writing kappa=psi^T(sigma_y^tensor4)psi and tilde(q)=Qtilde(psi), this is the more explicit actual-vector equation

`g=(A+2F-3delta I_Q)v-8kappa tilde(q)`.                  (1)

It follows by QL²psi=Rv+Av and QZLpsi=Rv+Fv. This couples the gradient to the BRIDGE vector but is not a scalar coercive inequality.

Indeed for the ACTUAL family

`psi=cos(theta)|0000>+sin(theta)|1100>`, 0<theta<pi/4,

let t=cos(2theta). Then

`R=2+2t²`, `C=0`, `<L²>=6R-8`,

`epsilon=0`, `g=0`, `||v||²=Var L=4t²(1-t²)>0`.

Thus neither `||v||²<=constant*epsilon` nor `||v||²<=constant*||g||²` can hold with a finite uniform constant. This is an actual-state obstruction to those precise gradient-coercivity shortcuts, not a relaxed tuple and NOT a channel counterexample. The entire locus producing this obstruction is now classified rather than discarded.

## 3. Elementary three-qubit cubic-projection lemma, with all complex cases

Let P_std be the LOCAL standard-S3 projector on three copies of ONE qubit, i.e. the orthogonal complement of its symmetric three-copy subspace. For a nonzero three-qubit tensor z define

`T3(z)=(P_std tensor P_std tensor P_std) z^tensor3`,

with the physical-party/copy regrouping understood.

**Lemma CUBIC.** `T3(z)=0` IFF z is BISEPARABLE, meaning it factors across at least one one-qubit-versus-two-qubit cut. Fully product tensors are included.

### 3.1 Zero invariance under actual invertible local changes

For any invertible local2-by2 matrix g, g^tensor3 commutes with copy permutations, hence with P_std. Therefore T3 has zero output before the local GL2 changes iff it has zero output afterward. This is only a ZERO-LOCUS statement; it does NOT assert that covariance eigenvalues, epsilon or the channel target are invariant under nonunitary filters.

If z factors at one physical qubit, that factor's triple power is locally symmetric, so T3(z)=0. This proves one direction for every biseparable tensor.

### 3.2 Complete elementary reduction of a nonbiseparable three-qubit tensor

Represent the first-qubit slices by two2-by2 matrices M0,M1. If every linear combination is singular, the nonzero slices have rank1. For M0=u v^T,M1=x y^T, the mixed determinant coefficient is proportional to `(u wedge x)(v wedge y)`. Its vanishing forces a common left or right factor, giving a physical factor at the second or third qubit. Dependent/zero slices instead factor the first qubit. Thus a nonbiseparable tensor has an invertible slice combination.

Choose that combination as M0, and use invertible changes on the other qubits to make M0=I. The residual changes preserving I act on M1 by similarity, so its COMPLETE2-by2 Jordan alternatives are:

- two distinct eigenvalues: simultaneous diagonal form, then a first-qubit slice change isolates E00 and E11. This is GHZ, `000+111`, up to nonzero scalings;
- a scalar matrix: the first qubit factors, already excluded in the nonbiseparable case;
- one nontrivial Jordan block: subtract the scalar multiple of I and scale the off-diagonal to E01. The tensor is `000+011+101`; flipping the last qubit gives W, `001+010+100`.

These exhaust complex2-by2 matrices. No special real phase, field restriction, unitary Schmidt reduction of a four-level pair or computer classification is used.

### 3.3 Explicit nonzero projection tests for BOTH genuine canonical types

At each physical site let e1,e2,e3 be the weight-one basis of its three copies. Its sum-zero plane is standard-S3. Put

`f=(1,-1,0)`, `h=(1,1,-2)`.

Both lie in that plane. For GHZ^tensor3, the local-weight(1,1,1) component is `sum_j e_j tensor e_j tensor e_j`. Its contraction against f tensor f tensor h is

`1*1*1+(-1)*(-1)*1+0=2`, nonzero.

For W^tensor3, that weight component is the sum over ALL six distinct-copy assignments `(i,j,k)`. The same contraction has only(i,j,k)=(1,2,3),(2,1,3) nonzero; each equals2, so the total is4. Thus T3 is nonzero for BOTH GHZ and W. Invertible zero invariance proves that every nonbiseparable tensor has nonzero T3. This completes CUBIC without importing a numerical catalogue or merely naming a canonical-form theorem.

## 4. TC equality kills every genuine three-party conditional sector

Use the ACTUAL strong three-copy certificate B3=K−4C_hat on the full global symmetric cube, as reconstructed in v3 and the parent. The local central-sector projectors commute with it and the global copy action. On a sector with THREE local standard factors and one local symmetric factor, C_hat=0 and K>=9I, strictly.

Consequently epsilon=<psi^tensor3|B3|psi^tensor3>=0 forces EVERY such m3 sector vector to vanish. There can be no cancellation with another sector because the certificate is block diagonal and PSD on the entire invariant space.

Fix any physical qubit ell and ANY complex linear functional xi on it. The triple bra xi^tensor3 is locally symmetric at ell. Contracting the vanished m3 component therefore yields

`T3((xi_ell tensor I)psi)=0`.

The conditional tensor may vanish; otherwise CUBIC proves it biseparable. Thus for EVERY qubit and EVERY conditional linear combination, the three remaining qubits are biseparable. This retains all complex conditional values, not just two chosen computational slices.

## 5. Conditional-pencil rigidity forces the ACTUAL four-qubit factorization

Fix a qubit ell and write its conditional three-qubit pencil as M(lambda)=A+lambda B. If the slices are dependent or one vanishes, ell factors and the remaining three-qubit tensor is biseparable by §4, giving one possible entangled pair and two singles.

Otherwise A,B are independent. For EVERY complex lambda, M(lambda) is biseparable. There are three possible one-versus-two flattening components. At least one component occurs for infinitely many lambda. Each of that component's finitely many2-by2 flattening minors is a polynomial in lambda of degree at most2, hence vanishes IDENTICALLY. Thus the ENTIRE pencil, including its leading slice B, has rank at most1 across ONE FIXED flattening.

This uses an identity known for ALL lambda, not finite sampling or interpolation. It does not allow the biseparating party to change independently from one parameter value to the next.

Now use the following complete rank-one pencil fact for2-by4 matrices. If two independent rank-one matrices u v^T,x y^T have every combination of rank<=1, then u,x are dependent OR v,y are dependent. Otherwise choose two columns with `v_j y_k-v_k y_j!=0`; their mixed minor is the nonzero product with `det[u,x]`, contradiction.

Apply it to the fixed physical one-qubit-versus-two-qubit flattening of A,B:

- common one-qubit factor: that qubit factors from the ORIGINAL four-qubit psi. Apply §4 to the remaining three-qubit tensor, using a nonzero conditional on that factor. It is biseparable, giving one pair and two singles;
- common two-qubit factor: the ORIGINAL psi factors into two two-qubit tensors, with ell paired with the complementary one-qubit party.

Therefore every epsilon0 state is an ACTUAL product of two two-qubit tensors, allowing product subfactors, after a qubit permutation. No nonunitary filter has been used to pretend the original covariance/channel spectrum is unchanged; invertible changes appeared only in the proof of the zero-projection lemma.

## 6. Exact equality algebra excludes TWO entangled pairs

R,E2 and C are invariant under physical local unitaries. Schmidt-decompose each ACTUAL pair, legitimately using only single-qubit local unitaries within it. Let their squared Schmidt imbalances be x,y in[0,1]. Then

`R=2x+2y`,

`C=(1-x)(1-y)`,

`E2=4x+4y+8xy`.

For the last equation the pair fields have means2x,2y and second moments4x,4y, and the product's cross term is8xy. Direct substitution gives

`epsilon=E2-6R+8-4C=4(1-x)(1-y)=4C`.                  (2)

Hence epsilon0 forces x=1 or y=1: at least one pair is product. Conversely, any one arbitrary pair tensor two pure qubits has x=1 or y=1 in(2), so epsilon0.

This proves the WHOLE claimed classification, including product states, maximally entangled pair endpoints, all three pairings and arbitrary complex phases:

`epsilon=0 iff psi=chi_(ij) tensor a_k tensor b_l`,

up to physical local unitaries/permutation. In particular C=0 and2<=R<=4 on this whole locus. No statement about the larger set g=0 is inferred: g=0 does not imply epsilon0.

## 7. Complete actual covariance spectrum on the entire zero locus

It remains to place the mixed covariance weight correctly, rather than promoting norm/purity to Ky-Fan sums.

Take the actual representative

`psi=(sqrt(mu)|00>+sqrt(nu)|11>)_(12) tensor |00>_(34)`,

mu+nu=1,mu>=nu>=0. Put t=mu−nu, s=2sqrt(mu nu), so t²+s²=1. Then

`R=2+2t²`, `delta=4-R=2(1-t²)`.

The pair's longitudinal centered Gram block is

`(1-t²)*[[1,1],[1,1]]`,

with eigenvalues delta,0. Its transverse four-dimensional block splits by site-symmetric/antisymmetric combinations into

`[[1+s,it],[-it,1-s]]`,

`[[1-s,it],[-it,1+s]]`.

Each has eigenvalues `1±sqrt(s²+t²)=2,0`. The other two physical pure qubits each add covariance spectrum2,0,0. Cross covariance between distinct tensor factors is zero. Thus EXACTLY

`spec Gamma=(2,2,2,2,delta,0 repeated7)`,0<=delta<=2.    (3)

Physical local unitaries rotate the Pauli basis by real orthogonal blocks, so this actual Gram spectrum applies to EVERY state in the classified locus. It is not an arbitrary local U4 Schmidt covariance assertion.

C_psi=QX3Q has the nonzero spectrum Gamma/2 and additional zeros in its fifteen-dimensional space. All its eigenvalues are<=1; its clipped trace is

`Tr min(C_psi,I)=Tr C_psi=4+delta/2>=4`.

For m=k−1<=3 the leading m eigenvalues are EXACTLY m, since four unit eigenvalues are present. As `<psi|X3|psi>=2+R/2=4-delta/2`, every rank-k containing projector obeys

`Tr(Pi X3)<=k+3-delta/2`,

`c<=-delta/2`, k2,3,4.                                 (4)

This is a sharp nonproduct containment margin on the ENTIRE TC-zero locus. It is derived from actual state factorization and the full spectrum, not from the old single-eigenvalue/purity data alone.

## 8. Stronger: the ORIGINAL full comparison on the whole zero locus

The factorization also permits a direct X3 diagonalization for ALL projectors, not just containing ones.

In the34=00 sector, X3 is `rho1 tensor I2+I1 tensor rho2+2rho12`. On the pair basis00,11 this is

`[[4mu,2sqrt(mu nu)],[2sqrt(mu nu),4nu]]`,

with eigenvalues

`lambda±=2±2sqrt(1-3mu nu)`.

The pair01,10 directions each have eigenvalue1. The34=01 and10 sectors each contribute one additional eigenvalue1 from rho12; the34=11 sector is zero. Consequently

`spec X3=(lambda+,1 repeated4,lambda-,0 repeated10)`,

where `0<=lambda-<=1` and `3<=lambda+<=4`. The trace is8, including the product endpoint lambda-=0.

This spectrum is majorized by the product spectrum `(4,1 repeated4,0 repeated11)` at EVERY index: for k1..5 its leading sum is at most4+(k−1), and from k5 onward the reference is the full trace8. Thus the U3 comparison is complete on this actual locus.

The common-order channel composition uses exact named analytic imports:

- U1 at all indices by the local-marginal Kronecker sum;
- X2<=3I+3rho from ENERGY's analytic Choi/swap proof, giving the required U2 leading sums for indices1..5;
- the accepted all-state central U2 bounds at6..10 from `proof-unrestricted-central-indices-v1.md`, SHA256 `10e4689c7ac8586fc920651eade6db37fa60be3b693f73b5f4ec7b6644fe6d23`;
- trace24 for U2 at11..15, X0=I and X4=rho.

Those imports yield X2 majorization at ALL indices. The product T_j share Hamming order. The tensor-channel expansion has nonnegative coefficients for q in[0,1], so Ky-Fan subadditivity/common order combines U1,U2 and the just-proved U3. The exact global spin-flip/transpose spectral identity maps p>1 to q=2−p. Therefore, at these named ordinary-written analytic imports,

`D_p^tensor4(rho) prec D_p^tensor4(|0000><0000|)`

for EVERY physical0<=p<=4/3 on the ENTIRE pure epsilon0 locus.

This full channel conclusion is a low-copy/tensor consequence once actual factorization is established, not a new record for a previously unknown biseparable state family. The new structural contribution is the unrestricted TC-equality classification and the actual mixed-mode placement in(3).

Any mixed state admitting a pure decomposition into these zero-locus states inherits the same channel comparison by original channel linearity/Ky-Fan convexity. The pairings and local unitaries may vary between components. This is only the specified convex hull; it is NOT a claim that a nonlinear mixed-state epsilon value characterizes that hull or that all biseparable/two-pair states are covered.

## 9. Exact remaining unrestricted frontier

A mixed strict channel failure, if one exists, has a pure failing component for the SAME Pi,p because the original trace gap is affine. No such pure component can have epsilon0 by §8. Thus the full original counterexample/proof problem may now be restricted, WITHOUT LOSS, to ACTUAL pure states with

`epsilon>0`,

with no lower positive bound and no finite numerical cutoff. States may approach the classified locus arbitrarily closely.

The remaining obligations are still:

- all-state CLIP `Tr min(C_psi,I)>=4` on this strict epsilon-positive region, equivalently the still-missing rank3/4 containing leading sums;
- for k2, all remaining actual d>0,a>b>0,c>0 quartics D>=0, or a literal physical failing pair and its exact p*;
- for k3/k4, both containment and general d>0 physical quartics on strict epsilon-positive pure inputs.

No actual failure is supplied. A leading output projector is NOT presumed to contain psi. Mixed averaging remains only of ORIGINAL affine traces, never of epsilon,Gamma,D or nonlinear feasible predicates.

The exact obstruction retired by §§2–8 is the attempt to coerce QLpsi by g/epsilon: legitimate nonproduct states in the ENTIRE classified null locus have g0 but QLpsi nonzero. Their extra covariance weight delta is instead localized in one eigenvalue<=2 by actual tensor structure. A future stability argument must control that mixed-mode localization as epsilon increases from0; the new classification does not provide such a quantitative theorem automatically.

**First unproved step:** a uniform ACTUAL-state estimate preserving this low-mode placement for arbitrary strict epsilon>0, sufficient for CLIP or the full rank-two off-face quartic. Neither continuity at epsilon0 nor compactness away from an arbitrarily imposed epsilon cutoff is a proof. The current full low-noise indices k2,3,4 remain OPEN.

## 10. Consolidated ledger, attribution and assurance

|domain of actual states/pairs|new disposition in this successor|not promoted|
|---|---|---|
|all pure states with epsilon0|complete classification as one pair plus two singles|not a classification of all g0 states|
|entire pure epsilon0 locus|full covariance spectrum, CLIP/all containment ranks, and original full all-p comparison at stated analytic imports|not arbitrary strict epsilon>0 inputs|
|specified mixed convex hull|original affine/Ky-Fan extension|no nonlinear averaging or mixed-epsilon criterion|
|strict epsilon>0|exact whole remaining target retained|no CLIP/generalquartic/fullindex closure|

The accepted three-copy positivity/sector constants are imports from the fully read v3 and current parent boundary, not a new independent rediscovery. The three-qubit GHZ/W zero tests and rank-one pencil alternatives are all re-derived above with explicit matrix elements2 and4; no classification catalogue or scientific computation is consumed. Nonunitary local changes classify a polynomial zero set only and never carry covariance spectra across filters.

All new claims are WRITTEN candidates requiring fresh reconstruction. No formal/kernel/human/configured-family/cross-vendor/executable/novelty gate is claimed. Classical three-qubit tensor normal-form ideas and low-copy channel facts are not presented as new mechanisms. Zhang's matched clipping ancestry and public uniform-weight ambiguity remain binding, and no worldwide-priority clearance was performed.

V9/v10, HOLD, exclusive owned-root writes, original cutoff/deadline and all historical evidence qualifications remain unchanged. The H-Hermiticity correction remains additive; old v4/source/packets/checkpoints are untouched. The current artifact is genuinely complete at its equality-locus scope, while the entire strict-positive residual and first unproved stability step remain explicit.
