# Actual containment: a three-copy covariance inequality closes rank two, with a quantitative off-face bridge

Actual `/bin/date` observation before this freeze: **Sun Oct 25 08:24:43 PDT 2026**. Owner PhysicsDepol4 / physics-2. **NEW WRITTEN CANDIDATE**, separate reconstruction and parent acceptance pending. One consolidated successor; old packets, reviews, checkpoints and receipts remain unchanged.

**New whole-face theorem:** for EVERY actual pure four-qubit psi and EVERY complex rank-two orthogonal projector Pi containing psi,

`Tr(Pi Z(psi))<=6`, hence `c<=0`.                       (C2)

The mixed-state rank-two containment face follows through the ORIGINAL affine trace inequality. No input ansatz, numerical search, common rotation for several complex vectors or relaxed tuple is used.

**New quantitative bridge for a pure input and ANY rank-two Pi:** with R=sum local Bloch-length squares, d=1−<psi|Pi|psi> and L=sum local Bloch vectors dot local Paulis,

`c<=d(1-R)+sqrt(d(1-d) Var_psi(L))`

` <=d(1-R)+sqrt(d(1-d)R(4-R))`.                         (BRIDGE)

This DOES NOT yet prove the d>0 quartic. Rank-three/four containment is also still open. No unrestricted low-noise index is claimed closed.

## 1. Exact authority and inherited frontier

Read completely before continuation:

- `parent-evidence-erratum-v9.md`, SHA256 `b7c92143cda18c88c7c56017859ab3c7f08fa92ef3d00fd85ba29f41ac258034`;
- `ppt-three-ME-depol-faces-parent-v1.md`, complete46LF, SHA256 `77681c87105f3a6199b9a76789bb632e8f7c8b732852383e5d77abbb0d8be7fc`, and its complete36LF receipt;
- the earlier exact quartic parent disposition and actual271LF reconstruction as recorded in the v2 activation.

The current parent pass supports ENERGY/FACE and the quantified v2 domains at their named written boundary, not containment. The actual author v2 pin is `06ce3ebb7cc4287708bf191d6245a0db7c8205422c03a80b4f05e073416c4861`.

Keep the SAME actual-pair coordinates

`a=3k+1-Tr(Pi X1)`, `b=3k+3-Tr(Pi X2)`,

`c=Tr(Pi X3)-(k+3)`, `d=1-Tr(Pi rho)`.

The accepted scalar reduction leaves the physical quartic

`D=27a²d²+18abcd+4b³d-b²c²-4ac³>=0`.

ENERGY/FACE gives b>=3d and excludes actual a=0 or b=0 with c>0. With s=Tr(Pi tilde(rho))>=0, exact inclusion-exclusion gives c=a−b−d−s, so positive excess requires a>b>0.

This packet now addresses the requested ACTUAL containment face. It does not substitute that face for the d>0 quartic. Every new step below is WRITTEN; no scientific eval/interpreter, arithmetic or symbolic program, enumeration, sampling, replay, solver, CLI, extra agent or GO was used. Metadata clocks/hashes and source reading only. V9's process/import corrections remain mandatory.

## 2. Actual centered Pauli frame and the face to be proved

For a pure rho=|psi><psi| write the twelve local Hermitian Paulis as S_mu and let r_mu=<psi|S_mu|psi>, a real vector. Put

`R=sum_mu r_mu²`, `L=sum_mu r_mu S_mu`,

`G_(mu,nu)=<psi|S_mu S_nu|psi>`,

`Gamma=G-r r^T`.

Gamma is the Gram matrix of the ACTUAL centered vectors

`v_mu=(S_mu-r_mu)psi`.

Let Q=I−rho. The Pauli identity gives X3=2rho+Z/2, so on psi-perp

`Q X3 Q=(1/2)sum_mu |v_mu><v_mu|`.

Its nonzero eigenvalues are those of Gamma/2. In particular this keeps the genuine pure-state origin; Gamma is not an independently selected correlation matrix.

For a rank-two containing projector Pi=rho+|phi><phi|, phi is any complex unit vector orthogonal to psi. Then

`Tr(Pi Z)=R+sum_mu |<phi|S_mu|psi>|²`

`          <=R+lambda_max(Gamma)`.

It suffices to prove the uniform coupled inequality

`R+lambda_max(Gamma)<=6`.                              (CG1)

The central new ingredient is an actual THREE-COPY positivity inequality, not a simultaneous single-vector rotation.

## 3. New three-copy pure-state inequality

Define squared global spin-flip overlap

`C=|<psi|sigma_y^tensor4|bar(psi)>|²`.

**Theorem TC (WRITTEN).** Every actual pure four-qubit state satisfies

`<psi|L²|psi>-6R+8>=4C`.                               (TC)

Equivalently, since <L>=R,

`Var_psi(L)>=(R-2)(4-R)+4C`.

The right side may be negative in some lower-R cases; the statement itself includes all0<=R<=4 without division by R,C or a local eigenvalue.

### 3.1 Explicit three-copy permutation operators

Take THREE copies of the physical four-qubit system and the vector Omega=psi tensor psi tensor psi. At physical site i let s_i,t_i,u_i swap copy pairs12,13,23, respectively. They are Hermitian involutions. Write

`V_i=s_i+t_i+u_i`,

`W_ij=s_i s_j+t_i t_j+u_i u_j`.

The three-copy space of ONE qubit has a four-dimensional symmetric subspace and two copies of the two-dimensional standard representation of S3; there is no alternating representation because wedge³(C²)=0. This decomposition can be seen directly by Hamming weights: weights0 and3 give two trivial lines; the three-dimensional weight1 permutation space is one trivial line plus its sum-zero plane; weight2 is identical.

Let A_i project onto the local symmetric subspace. The transposition class sum is therefore

`V_i=3A_i`.

On a standard factor choose the explicit reflection matrices

`s=Z`, `t=-(1/2)Z+(sqrt(3)/2)X`,

`u=-(1/2)Z-(sqrt(3)/2)X`.                              (S3)

They act identically on the two standard multiplicity copies. This is a fixed representation basis on COPY space, not a common physical rotation of several complex Pauli coefficient vectors.

### 3.2 The symmetrized operator representing the left side of(TC)

The qubit swap identity `2s_i-I=sum_alpha sigma_(i,copy1)^alpha sigma_(i,copy2)^alpha` gives

`R=<Omega| sum_i[(2/3)V_i-I] |Omega>`.

For i≠j, the quantity

`f_ij=sum_(alpha,beta) r_i^alpha r_j^beta <sigma_i^alpha sigma_j^beta>`

is the expectation of `(2s_i-I)(2t_j-I)`. Symmetrizing the three identical global copies averages the SIX ordered distinct transposition pairs, giving

`H_ij=(2/3)(V_i V_j-W_ij)-(2/3)(V_i+V_j)+I`.

Thus `<L²>=R+2sum_(i<j)<H_ij>`. Substituting V_i=3A_i, the operator whose Omega expectation is `<L²>-6R+8` is

`K=40I-22sum_i A_i+12sum_(i<j) A_i A_j`

`                   -(4/3)sum_(i<j) W_ij`.             (K)

Every factor and sign comes from the six-copy-permutation average: H_ij is6A_iA_j−(2/3)W_ij−2(A_i+A_j)+I.

Decompose by the set of sites carrying a local standard factor. If there are m such sites, q=4−m sites are locally symmetric. Two symmetric sites contribute W_ij=3I; a symmetric/standard pair contributes zero; standard pairs retain W_ij. Consequently(K) becomes

`K_m=(4m²-6m)I-(4/3)sum_(standard i<j) W_ij`.

From(S3), `W_ij=(3/2)(X_i X_j+Z_i Z_j)`. Define AUXILIARY standard-factor collective spins `J_alpha=(1/2)sum_i sigma_i^alpha`. Then exactly

`K_m=4[m(m-1)I-J_x²-J_z²]`.                           (Km)

These auxiliary Pauli matrices act only on the standard S3 factors.

The elementary bound `J²<=m(m+2)I/4` follows from

`J²=(3m/4)I+(1/2)sum_(i<j) sigma_i dot sigma_j`,

and `sigma_i dot sigma_j<=I`, itself the two-auxiliary-qubit swap identity. Since J_y²>=0, this proves

- m0: K0=0;
- m2: K2>=0;
- m3: K3>=9I;
- m4: K4>=24I.

For m1, K1=−2I, but a single standard factor with all other factors trivial has NO vector invariant under the GLOBAL simultaneous S3 copy permutations. Omega is globally invariant, and the local central-sector projectors commute with that action. Its m1 component is therefore exactly zero. No negative m1 contribution is discarded without this representation reason.

### 3.3 Represent C and control its sole m4 sector

Let P_s=product_i(I−s_i)/2, and similarly P_t,P_u. For a pure pair of four-qubit copies, the four local singlet contractions have squared norm C/16: each normalized singlet contributes its factor1/sqrt2, so the global bilinear spin-flip amplitude is divided by4. Averaging the three identical copy pairs therefore represents C by

`C_hat=(16/3)(P_s+P_t+P_u)`                            (C-hat)

in the Omega expectation.

Every P_s,P_t,P_u vanishes when any local factor is symmetric. Thus C_hat is supported ONLY at m4. On the four standard factors, each is a rank-one product projection, tensored with the identity on standard multiplicity spaces.

Let P_inv be global S3 averaging on those four standard factors and let v=P_inv|---->, where |-> is the s=Z negative eigenvector. The group permutes the three product projections. On the invariant subspace they all become the same vv*; hence

`P_inv C_hat P_inv=16 vv*`.

The SIX exact group matrix coefficients in `<----|D(g)^tensor4|---->` are1,1,1/16,1/16,1/16,1/16. Indeed the two relevant single-factor diagonal values are−1 for s and±1/2 for the other four nonidentity elements; their fourth powers have the stated signs removed. Therefore

`||v||²=(2+4/16)/6=3/8`,

and `P_inv C_hat P_inv<=6I`. This norm statement is unaffected by the standard multiplicity factors.

At m4, K4>=24I, so `K4-4 C_hat>=0` on the global invariant subspace. At m0,m2,m3, C_hat=0 and the bounds above are nonnegative. At m1 there is no global invariant component. Thus the ENTIRE globally invariant Omega space satisfies

`<Omega|K-4 C_hat|Omega>>=0`.

Equations(K),(C-hat) prove(TC). No finite sample, numerical eigenvalue or uncomputed sign table is a premise.

## 4. From three-copy compatibility to the full complex covariance norm

Use the actual pure Pauli sector lengths A_j. The written v2 marginal-purity/spin-flip derivation gives

`A2=R+2+4C`.

For completeness, equality of summed one/triple marginal purities gives `A3=12+R-2A2`; purity gives `A4=3-2R+A2`; global spin flip then yields `C=(A2-R-2)/4`.

The twelve-by-twelve uncentered Gram has diagonal-site contribution12+2R to Tr G². The off-site blocks are real two-qubit correlations, contributing2A2. Hence

`Tr G²=16+4R+8C`.

Because r is real, `r^T G r=<L²>` and `r^T r=R`. Therefore

`Tr Gamma²=Tr G²-2<L²>+R²`.

Using(TC) gives the UNIFORM actual covariance purity bound

`Tr Gamma²<=32-8R+R²=16+(4-R)²`.                       (CP)

Now order the physical local Bloch lengths t1>=t2>=t3>=t4>=0. Off-site Gram entries are real, and same-site imaginary parts are the Pauli commutators. Consequently

`Gamma-Gamma^T=2i blockdiag_i(epsilon_(alpha,beta,gamma) r_i^gamma)`.

Its four nonnegative leading eigenvalues are2t1,2t2,2t3,2t4, including zeros/ties. Gamma^T is positive semidefinite, so Gamma>=Gamma−Gamma^T. Eigenvalue monotonicity—not an invalid positive-part Loewner rule—gives

`lambda_j(Gamma)>=2t_j`, j=1,2,3,4.                   (LOW)

If lambda1>6−R, then6−R>=2 and

`Tr Gamma²>=lambda1²+sum_(j=2)^4 lambda_j²`

` >(6-R)²+4(R-t1²)`

` >=(6-R)²+4(R-1)=32-8R+R²`,

contradicting(CP). The last line uses ONLY t1²<=1. Thus(CG1) follows for every pure input, including all zero/tied local spectra and arbitrary complex amplitudes:

`R+lambda_max(Gamma)<=6`.

The complex Gram eigenvalue maximizes over complex coefficient vectors automatically; no several-vector local rotation is used.

## 5. ENTIRE actual rank-two containment face is closed

For Pi containing pure psi, write `Pi=rho+|phi><phi|`, phi⊥psi. The actual centered frame gives

`Tr(Pi Z)=R+<phi|sum_mu |v_mu><v_mu||phi>`

`          <=R+lambda_max(Gamma)<=6`.

Since X3=2rho+Z/2 and Tr(Pi rho)=1,

`Tr(Pi X3)<=2+6/2=5`, hence c<=0 at k2.               (10)

This holds for EVERY containing complex rank-two projector, not only a leading projector or a basis projector. It closes the full requested k2 containment face.

For mixed rho with d=0 at rank2, every pure component of any positive decomposition lies in Ran(Pi): the nonnegative missing weights sum to zero. Apply(10) at the SAME Pi to each pure component and average the ORIGINAL affine trace. This gives c<=0 for the mixed input as well. No averaging of R,C,Gamma or D is asserted.

Because c<=0, the accepted scalar theorem gives the actual trace comparison for every0<p<2/3 on these containing pairs. This is NOT a full state-level Ky-Fan comparison: an arbitrary leading output projector need not contain the input support.

## 6. Quantitative pure-state rank-two extension to d>0

We now derive(BRIDGE), rather than treating a face theorem as a full low-noise index.

For an arbitrary rank-two Pi put r=1−d. If0<r<1, let u=Pi psi/sqrt r and choose a unit phi in Ran(Pi) orthogonal to u. Then phi⊥psi. Write

`u=sqrt r psi+sqrt d eta`, eta⊥psi, ||eta||=1.

Pi0=rho+|phi><phi| is a genuine rank-two containing projector, so its c0<=0 by §5. Therefore

`c<=<u|X3|u>-<psi|X3|psi>`.

For a pure state, each one-versus-rest Schmidt decomposition gives

`(rho_rest tensor I_i)psi=(rho_i tensor I_rest)psi`.

Thus EXACTLY `X3 psi=X1 psi=(2I+L/2)psi`. In particular

`<psi|X3|psi>=2+R/2`,

`Q X3 psi=(1/2)Q L psi`.

From(CG1), every unit eta⊥psi obeys `<eta|X3|eta><=3-R/2`. Expanding the u expectation and using Cauchy on the ACTUAL off-diagonal vector now gives

`c<=d[(3-R/2)-(2+R/2)]`

`       +2sqrt(rd)*(1/2)sqrt(Var_psi L)`

` =d(1-R)+sqrt(d(1-d)Var_psi L)`.                       (11)

At d=0 this is exactly the containing case. At d=1, choose any orthonormal u,phi basis of Ran(Pi); both are orthogonal to psi, and the same comparison with Pi0 gives c<=1−R, with the square-root term zero. Thus every endpoint is covered without normalizing a zero projection.

Finally `||L||<=sum_i t_i<=2sqrt R`, so `<L²><=4R` and

`Var_psi L<=R(4-R)`.

Substitution proves(BRIDGE) with its displayed domains. It is sharp for a product input in the sense that R4 makes the bound c<=−3d; its off-face penalty is not discarded.

For R>1, a possible positive c therefore additionally requires

`d<R(4-R)/(2R+1)`.

Indeed positivity of the right side of(11)'s weaker final bound requires `sqrt(d(1-d)R(4-R))>d(R-1)`; reversible squaring for d>0 and R>1 gives exactly that condition. It is a necessary actual-pair restriction, NOT a sufficient violation or a quartic proof.

The accepted ENERGY inequality b>=3d and v2's actual R,C energy bounds may be retained jointly with(11). I do NOT claim their combination already implies D>=0 for all d>0; no such elimination has been established here.

## 7. What remains at ranks three/four, and the single actual-state formulation

Let C_psi=Q X3 Q on psi-perp. Its trace is6−R/2. For a rank-k containing projector, m=k−1 and

`Tr(Pi X3)=2+R/2+Tr(P_m C_psi)`.

Thus rank3 and rank4 containment still require, respectively,

`K2(Gamma)<=8-R`, `K3(Gamma)<=10-R`.

The present covariance norm bound proves only the m1 case. Neither the purity bound nor its one-eigenvalue argument is promoted to simultaneous leading sums.

For clarity, simultaneous closure of ALL three containment ranks is exactly equivalent to the one actual-state clipped-trace statement

`Tr(C_psi-I_Q)_+ <=(4-R)/2`,

or `Tr min(C_psi,I_Q)>=4`.                             (CLIP)

Here min denotes applying the scalar function min(x,1) spectrally on psi-perp. If the positive-part rank is1,2 or3, the corresponding containment inequality is exactly the needed bound. If it is at least4, positivity and Tr C_psi=6−R/2 give `Tr(C_psi-I)_+<=Tr C_psi-4=(4-R)/2` automatically. Conversely(CLIP) bounds every leading m1,2,3 shifted sum. Thus(CLIP) keeps genuine state compatibility while eliminating every containing-projector choice; it is NOT YET proved.

This is not a new relaxed tuple or a solution of the original target. The original full d>0 quartic remains separate. The rank2 bridge(11) is one quantified input toward it, not its acceptance.

## 8. Per-index verdict and exact open obligations

|index|new completed actual containment scope|remaining original target|
|---|---|---|
|k2|EVERY actual rank2 Pi with d=0 has c<=0, pure and mixed; quantitative pure off-face bound(11) proved WRITTEN|D>=0 for all remaining actual d>0,a>b>0,c>0 pairs, or actual strict failure; low-noise index OPEN|
|k3|no whole-face closure claimed; actual covariance formulation retained|rank3 d=0 and general d>0 physical quartic remain OPEN|
|k4|no whole-face closure claimed; actual covariance formulation retained|rank4 d=0 and general d>0 physical quartic remain OPEN|

No actual containing counterexample is supplied. No original low-noise index or unrestricted all-p majorization theorem is declared solved.

## 9. Method and assurance qualifications

The exploratory local-concurrence shortcut recorded in checkpoint011 is NOT a premise. Its proposed pointwise inequality has an explicit ACTUAL nonviolating-pair countercontrol there; the three-copy proof bypasses it. CKW/monogamy source leads and their unverified interfaces are not imported to fill any step above. All load-bearing new positivity is derived by the explicit local three-copy permutation representation, collective auxiliary Pauli bound, and exact projected rank-one norm3/8.

The three-copy inequality, covariance-purity bound, rank2 face and quantitative bridge require their own fresh written reconstruction. They are not formal/kernel, human, cross-vendor or novelty acceptance. The finite-dimensional representation and Pauli manipulations are classical tools; no worldwide priority claim is made. Zhang's matched complementary clipping ancestry and the public uniform-weight ambiguity remain binding even though this new actual covariance problem is distinct from the old central proof.

Initial written analysis/source reading after redispatch preceded the first returned new clock08:04:55 PDT; no earlier activation clock or retrospective cadence attestation is invented. Subsequent actual checkpoints011/012 preserve the proof development. Parentv9's execution/coverage/import corrections and all previous errata remain binding. No scientific permission or executable credit follows from this written result.

**Current consolidated frontier:** complete WRITTEN rank2 containment plus(11), ranks3/4 containment and all remaining d>0 quartic obligations still open. A later continuation must address those precise actual-state inequalities or supply a literal physical failure; neither a copied shadow table, a common several-vector rotation, nor a conditional negative quartic at a nonexistent pair is a counterexample.
