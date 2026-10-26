# v60-A — complete written reconstruction of rank-two containment, three-copy covariance and the off-face bridge

Actual `/bin/date` observation before creation: **Sun Oct 25 08:35:54 PDT 2026**. Reviewer InfoSPR7-2 / information science; author PhysicsDepol4 / physics. Genuinely cross-domain, same-harness, supplied-proof review. All algebra below is WRITTEN reasoning, not executed arithmetic. No scientific eval/interpreter/program, symbolic computation, enumeration, sampling, replay, solver, CLI or nested agent was used. Metadata clocks/hashes and source reads only; HOLD/v9 remain binding.

## 1. Frozen scope, exposure and literal coverage

Read S1/v9 FIRST, then the exact v60-A assignment in `peer-review-wave-eighteen-v60.json` and the complete `peer-review-wave-eighteen-v60-packet-receipt-v1.json`. The long assignment scope was explicitly recovered with `:raw`. Exposure ACK `peer-review-depol-containment-covariance-ack-v1.json` was written BEFORE the proof body.

ALL supplied parts means the single full part `peer-review-wave-v60-v60-A-part1-v1.md`, freshly observed SHA256 **`06679781c1fa13c4607c34ba1b703e8d7476ebfba3672b24634c61408ed1c37c`**. Complete packet LF1–766 was read in adjacent ranged windows, including every ending. No source line remained truncated. The receipt reports source roundtrip equality and persisted-byte equality before dispatch; I did not independently regenerate the packet.

Complete source coverage:

- **S1:** parent erratum v9, LF1–35, SHA256 `b7c92143cda18c88c7c56017859ab3c7f08fa92ef3d00fd85ba29f41ac258034`.
- **S2 (NEW v3):** `depolarizing-containment-covariance-consolidated-v3.md`, **LF1–330**, freshly observed SHA256 **`8c80174c393ec051401bd5d1951efb3f17b738ba94c79978060360aebd237653`**.
- **S3:** `ppt-three-ME-depol-faces-parent-v1.md`, LF1–46, SHA256 `77681c87105f3a6199b9a76789bb632e8f7c8b732852383e5d77abbb0d8be7fc`.
- **S4:** `depolarizing-actual-pair-compatibility-consolidated-v2.md`, **LF1–332**, SHA256 `06ce3ebb7cc4287708bf191d6245a0db7c8205422c03a80b4f05e073416c4861`.

References below identify S2 original LF unless marked S4. I previously reviewed S4 at v49-A; that serial exposure is disclosed, not described as blindness. S4 was reread completely here. S3 supplies the exact prior ENERGY/FACE boundary; its separate PPT three-ME theorem is background, not a mathematical premise being newly certified by this depolarizing review. Parent supplied reconstruction obligations, not a verdict for v3.

## 2. Verdict and exact accepted written scope

**0 FATAL / 0 MAJOR / 0 MINOR** at the ENTIRE delivered v3 written scope.

Reconstructed:

1. The actual centered frame and nonzero spectral identification of the psi-perpendicular X3 compression with Gamma/2.
2. The complete three-copy inequality TC, including the local S3 decomposition, every factor in K, the absent invariant m1 sector, the rank-one invariant norm3/8 and the C contribution.
3. The actual pure-state covariance-purity bound CP and the FULL COMPLEX covariance norm bound CG1, including all zero/tied local spectra.
4. Every actual rank-two containing complex projector has c<=0, pure or mixed; mixed extension uses the ORIGINAL affine trace only.
5. The arbitrary-rank-two PURE-input off-face BRIDGE, both endpoints d=0,1, its product-input sharpness and the stated necessary positive-excess restriction.
6. The CLIP equivalence for simultaneous pure containment ranks2/3/4, with only its m1 case actually proved.

**No common multivector physical rotation is assumed anywhere.** The two-dimensional X,Z reflection basis in the TC proof is a fixed representation basis on COPY-space standard factors; it is not a simultaneous physical rotation of several complex covariance vectors.

Not accepted or supplied: the rank-two d>0 quartic, rank-three/four containment or d>0 closure, an actual counterexample, a full low-noise index, unrestricted majorization, executable/formal/human/cross-vendor/novelty certification. Zhang ancestry remains binding. These exclusions are part of the verdict, not follow-up promises.

## 3. Actual centered frame and the correct spectral statement

**S2 LF45–73 reconstructed.** Define `v_mu=(S_mu-r_mu)psi`. Because S_mu are Hermitian and r_mu real,

`<v_mu|v_nu>=<psi|S_mu S_nu|psi>-r_mu r_nu=Gamma_(mu,nu)`.

Thus Gamma is an ACTUAL positive Gram matrix, not an arbitrary relaxed Hermitian matrix. The local Pauli twirl gives

`rho_rest tensor I_i=(rho+sum_alpha S_i^alpha rho S_i^alpha)/2`.

Summing four sites yields `X3=2rho+Z/2`, where `Z=sum_mu S_mu rho S_mu`. For `Q=I-rho`, `Q S_mu psi=v_mu`, so

`Q X3 Q=(1/2)sum_mu |v_mu><v_mu|`.

The nonzero eigenvalues of this operator and Gamma/2 agree by the frame maps VV* and V*V. They are **not literally the same-size matrix**: the physical psi-perpendicular space and twelve-vector coefficient space differ in dimension. The source correctly states nonzero spectral agreement at LF59–61.

If `Pi=rho+|phi><phi|`, with COMPLEX unit phi perpendicular to psi, then

`Tr(Pi Z)=sum_mu r_mu^2+sum_mu |<phi|S_mu|psi>|^2`

`          <=R+lambda_max(Gamma)`.

No reality restriction or common choice of maximizing vector is introduced. Proving CG1 therefore suffices for every containing rank-two projector.

## 4. Theorem TC: independent reconstruction of every representation and factor

### 4.1 Local S3 decomposition and V_i=3A_i

**LF93–111.** On three copies of one qubit, Hamming weights0 and3 are each a trivial line. Each of weights1 and2 is the three-dimensional permutation representation: its all-ones line is trivial and its sum-zero plane is standard. Thus the eight-dimensional local space consists of four trivial dimensions and two standard copies. There is NO alternating representation, also consistent with `wedge^3(C^2)=0`.

The sum of three transpositions acts as3 on a trivial factor and as0 on a standard factor. Therefore its operator is exactly `V_i=3A_i`, where A_i is the four-dimensional local symmetric projector. The source's standard matrices

`s=Z`, `t=-Z/2+(sqrt(3)/2)X`, `u=-Z/2-(sqrt(3)/2)X`

have sum zero, square to identity, and are the three standard reflections. The multiplicity spaces are acted on identically, not rotated physical Pauli spaces.

### 4.2 Six-pair symmetrization and K

**LF115–133.** The swap identity `2s_i-I=sum_alpha sigma_(i,1)^alpha sigma_(i,2)^alpha` has expectation t_i^2 on the three-copy product Omega. Averaging the three copy pairs consequently gives

`R=<sum_i[(2/3)V_i-I]>`.

For i!=j, `(2s_i-I)(2t_j-I)` has expectation

`sum_(alpha,beta) r_i^alpha r_j^beta <sigma_i^alpha sigma_j^beta>`:

copy1 contains the two-point correlation, copies2/3 the respective one-point expectations. Global copy permutation averages the SIX ordered DISTINCT transposition pairs. The leading term is

`(4/6)sum_(a!=b) a_i b_j=(2/3)(V_iV_j-W_ij)`.

Each transposition appears twice in each linear term, giving `-(2/3)(V_i+V_j)`, and the constant is I. Therefore

`H_ij=(2/3)(V_iV_j-W_ij)-(2/3)(V_i+V_j)+I`

`     =6A_iA_j-(2/3)W_ij-2(A_i+A_j)+I`.

Since `<L^2>=R+2sum_(i<j)<H_ij>`, the desired left side `<L^2>-6R+8` is the expectation of `-5R_operator+2sum H_ij+8I`. Substituting the printed R operator gives **exactly**

`K=40I-22sum_i A_i+12sum_(i<j)A_iA_j-(4/3)sum_(i<j)W_ij`.

The 40 and−22 constants include all six site pairs; no unrecorded factor two is supplied by a numerical check.

### 4.3 Sector K_m and the absent negative m1 contribution

**LF135–156.** On a fixed local-sector pattern with q=4−m trivial sites, a trivial/trivial pair has W=3I; a trivial/standard pair has W=s+t+u=0. The scalar part reduces as

`40-22q+4q(q-1)=4m^2-6m`.

Thus `K_m=(4m^2-6m)I-(4/3)sum_standard W_ij`. Expanding the three standard reflections cancels the mixed XZ terms and gives

`W_ij=(3/2)(X_iX_j+Z_iZ_j)`.

With auxiliary `J_alpha=(1/2)sum sigma_i^alpha`,

`J_x^2+J_z^2=(m/2)I+(1/2)sum_(i<j)(X_iX_j+Z_iZ_j)`.

Consequently

`K_m=4[m(m-1)I-J_x^2-J_z^2]`.

The auxiliary two-qubit swap identity gives `sigma_i dot sigma_j<=I`, hence

`J^2=(3m/4)I+(1/2)sum_(i<j)sigma_i dot sigma_j`

`    <=m(m+2)I/4`.

Using `J_y^2>=0` gives K0=0, K2>=0, K3>=9I and K4>=24I. At m1 the exact value is−2I, so it CANNOT simply be dropped as positive. The source instead uses the correct invariant argument: Omega is invariant under simultaneous global S3 permutations; each fixed local-sector projection commutes with that action. One standard factor tensored with only trivial factors has no invariant vector, with the multiplicity spaces still trivial. The m1 component of Omega is therefore exactly zero. This closes the potentially negative sector without an extra state assumption.

### 4.4 C-hat, all six coefficients, norm3/8 and positivity

**LF160–182.** Projecting a pair of full four-qubit copies onto four normalized local singlets contracts their bilinear spin-flip amplitude by1/4, hence its squared norm is C/16; the third copy has norm one. Thus

`C_hat=(16/3)(P_s+P_t+P_u)`

has Omega expectation C. The normalization uses the singlet factor1/sqrt2 at EACH of four physical sites.

Each projector vanishes if any local sector is trivial/symmetric. Therefore C_hat is supported only at m4. On the four standard factors each is a rank-one product projection, tensored with identity on their multiplicities. Global averaging P_inv turns the three conjugate product projections into the same `vv*`, with `v=P_inv|---->`, so

`P_inv C_hat P_inv=16vv*`.

The exact SIX group coefficients are independently checked from the reflection matrices. Identity gives1; s gives(−1)^4=1. The other two reflections have diagonal value+1/2 on |->; the two3-cycles have diagonal value−1/2. Taking their fourth powers gives four copies of1/16. Hence

`||v||^2=<----|P_inv|---->=(1+1+4/16)/6=3/8`.

The compressed C_hat has norm `16*(3/8)=6`, including its identity multiplicity factor. At m4, the compressed K4 is at least24I, so `K4-4C_hat>=0` on the global invariant subspace. The other possible invariant sectors have C_hat=0 and nonnegative K; m1 is absent. Operators preserve the local central sectors, so no cross-sector expectation was lost.

It follows that `<Omega|K-4C_hat|Omega>>=0`, giving TC in FULL:

`<L^2>-6R+8>=4C`.

No physical several-vector rotation, finite eigenspectrum or precomputed sign table is used anywhere in this derivation.

## 5. Sector algebra, CP and the full complex bound CG1

**LF186–224 reconstructed.** The supplied v2 pure marginal argument gives A2=R+2+4C; its complete source was reread. Specifically purity and equal one-/three-marginal purities give `A3=12+R-2A2`, `A4=3-2R+A2`; spin flip gives `C=(A2-R-2)/4`.

A same-site three-by-three Gram block is `I+i epsilon r_i`; its contribution to Tr G² is `3+2t_i²`. Summing sites gives12+2R. Every off-site correlation block is real, and each unordered physical pair occurs twice, so its total contribution is2A2. Thus

`Tr G^2=12+2R+2A2=16+4R+8C`.

Centering subtracts rr^T, with real r, `r^TGr=<L^2>` and `||r||^2=R`. Hence

`Tr Gamma^2=16+4R+8C-2<L^2>+R^2`

`             <=32-8R+R^2=16+(4-R)^2`.

This is CP, with every TC factor retained.

For the antisymmetric part, off-site entries cancel because they are real, while same-site Pauli commutators yield

`Gamma-Gamma^T=2i blockdiag_i(epsilon_(alpha,beta,gamma)r_i^gamma)`.

Each block has eigenvalues +2t_i,0,−2t_i. Sorting t1>=t2>=t3>=t4, the four leading eigenvalues are 2t1,...,2t4, including zero/tied cases. Gamma^T is positive semidefinite (the transpose/conjugate of a Hermitian PSD matrix), so

`Gamma>=(Gamma-Gamma^T)`.

Ordinary Hermitian eigenvalue monotonicity gives `lambda_j(Gamma)>=2t_j`, j1–4. The proof does NOT assert the generally invalid Loewner inequality with a positive part.

If lambda1>6−R, then 6−R>=2 because 0<=R<=4. Squaring is therefore strict with the correct sign. Since Gamma is PSD,

`Tr Gamma^2>=lambda1^2+sum_(j=2)^4lambda_j^2`

` >(6-R)^2+4(R-t1^2)`

` >=(6-R)^2+4(R-1)=32-8R+R^2`.

The last step uses ONLY t1²<=1, not a nonexistent constraint such as t1²<=R/4. This contradicts CP and proves

`R+lambda_max(Gamma)<=6`.

All coefficients/eigenvectors may be complex. Zero or tied t_i and covariance eigenvalues cause no division or choice problem.

## 6. Entire rank-two containment, including mixed inputs

**LF228–242 reconstructed.** For any containing Pi, the frame calculation in §3 gives `Tr(Pi Z)<=6`. Since `X3=2rho+Z/2` and `Tr(Pi rho)=1`, `Tr(Pi X3)<=5`, i.e. c<=0 at rank two. Pi is any complex containing plane, not necessarily a leading-output projector.

If a mixed rho has d=0 at the SAME rank-two Pi, every pure component in a positive decomposition has nonnegative missing weight and those weights average to zero. Hence each pure component lies exactly in Ran(Pi). Apply the pure ORIGINAL trace inequality at that fixed Pi and average the linear X3 traces. This proves the mixed containment face. There is NO averaging of R,C,Gamma,TC or the quartic D.

The accepted scalar frontier then gives the corresponding trace comparison on those containing pairs. An arbitrary leading output plane need not contain the input, so this is not a full state-level low-noise Ky-Fan theorem. Source LF242 makes that boundary explicit.

## 7. BRIDGE, endpoints, variance and the exact positive-excess restriction

**LF248–288 reconstructed.** If 0<r=1−d<1, set `u=Pi psi/sqrt r` and choose a complex unit phi in Ran(Pi) perpendicular to u. Because `Pi psi=sqrt r u`, phi is also perpendicular to psi. The decomposition

`u=sqrt r psi+sqrt d eta`

has a genuine unit eta perpendicular to psi. The plane `Pi0=rho+|phi><phi|` is an actual containing rank-two plane, whose c0<=0. Subtracting its ORIGINAL trace gives

`c<=<u|X3|u>-<psi|X3|psi>`.

For every pure one-versus-rest Schmidt decomposition, multiplying psi by its two marginals on opposite sides gives the same vector (each term is multiplied by its Schmidt eigenvalue). This remains true at zero Schmidt eigenvalues without inversion. Summing the four cuts yields

`X3 psi=X1 psi=(2I+L/2)psi`,

`<psi|X3|psi>=2+R/2`, `QX3 psi=(1/2)QL psi`.

CG1 bounds the other diagonal term by `<eta|X3|eta><=3−R/2`. Expanding u and bounding the REAL cross term by its complex modulus gives

`c<=d(1-R)+2sqrt(rd)*(1/2)||QL psi||`

` =d(1-R)+sqrt(d(1-d)Var_psi L)`.

This Cauchy bound is on one ACTUAL off-diagonal vector; it does not rotate a family of covariance vectors. At d=0 containment gives c<=0 directly. At d=1 choose any orthonormal u,phi basis of Ran(Pi); both are perpendicular to psi, compare with Pi0 as above and use the same diagonal bound to obtain c<=1−R. No zero projected vector is normalized.

Finally `||L||<=sum_i t_i<=2sqrt R`, so `<L²><=4R` and, since `<L>=R`, `Var L<=R(4-R)`. This includes R=0,4. It proves the second BRIDGE bound. At R=4 a product input has zero variance, giving c<=−3d; sharpness is physical: after taking psi to0000, choose `u=sqrt(1-d)psi+sqrt d e1`, phi=e2 with two distinct one-excitation vectors. Their X3 trace is5−3d, saturating the bound for every endpoint/interior d.

For R>1, c>0 cannot occur at d=0 by containment. At d>0, a necessary condition for the weaker upper bound to be positive is

`sqrt(d(1-d)R(4-R))>d(R-1)`.

Both sides are nonnegative and the right side positive, so reversible squaring and division by d give

`R(4-R)>d[R(4-R)+(R-1)^2]=d(2R+1)`.

Thus `d<R(4-R)/(2R+1)` exactly. It is necessary, not sufficient, and implies no quartic closure.

## 8. CLIP equivalence and why only m1 is closed

**LF292–310 reconstructed.** On psi-perp let `C_psi=QX3Q>=0`. Its trace is `Tr X3−<psi|X3|psi>=8−(2+R/2)=6−R/2`; equivalently it is half the frame trace12−R. For a containing rank-k Pi with m=k−1,

`Tr(Pi X3)=2+R/2+Tr(P_m C_psi)`.

Containment at m=1,2,3 is therefore respectively

`K_m(Gamma)<=2m+4-R`.

CG1 is ONLY m=1. The one-leading-eigenvalue contradiction does not establish the m=2 or m=3 sums.

All three containing ranks are equivalent to

`Tr(C_psi-I_Q)_+ <=(4-R)/2`,

or `Tr min(C_psi,I_Q)>=4`.

To check both directions, let r_+ be the number of eigenvalues of C_psi exceeding one. If r_+=0 the bound is automatic. If r_+=1,2,3 it is exactly the corresponding shifted leading-sum inequality. If r_+>=4, positivity gives

`Tr(C_psi-I)_+<=Tr C_psi-r_+<=Tr C_psi-4=(4-R)/2`.

Conversely a positive-part trace bound dominates EVERY shifted leading m-sum, proving all three containment inequalities. The spectral identity `Tr min(C,I)=Tr C−Tr(C−I)_+` gives the equivalent clipped form. This is a correct formulation, NOT its proof. Rank-three/four containment remains open.

## 9. Supplied predecessor boundaries and exact findings

S4's ENERGY/FACE inputs match their use: the Choi polynomial is8 times the exactly-two-antisymmetric projector, actual `(rho^T tensor Pi)^Gamma>=0`, hence b>=3d; pure marginal compatibility and exact complex projection geometry give FACE, with the mixed extension affine only. The Pauli sector relation used in CP was rederived above rather than inherited from a machine field. S3's accepted depolarizing scope expressly did NOT include containment, so no prior verdict was silently extended to TC/CG1. Its separate PPT discussion is not imported into the covariance theorem.

| Category / obligation | Disposition |
|---|---|
| FATAL | None in the complete new v3 scope. |
| MAJOR | None in that scope. |
| MINOR | None in that scope. |
| TC, CP, CG1, complete rank-two pure/mixed containment | WRITTEN reconstructed here at explicit algebra/representation boundaries. |
| PURE arbitrary-rank-two BRIDGE and its endpoints/necessary restriction | WRITTEN reconstructed; not a mixed nonlinear extrapolation. |
| CLIP equivalence | Reconstructed as an equivalence; its missing m2/m3 bounds are NOT proved. |
| Rank-two d>0 actual quartic | **NOT_RECONSTRUCTED / still OPEN.** Neither containment nor BRIDGE is promoted to it. |
| Rank-three/four containment and general d>0 | **NOT_RECONSTRUCTED / still OPEN.** |
| Actual counterexample or full low-noise/state-majorization closure | Not supplied or accepted. |
| CKW/monogamy shortcut and exploratory checkpoint011 control | Not a premise; no source lead or historical calculation fills a new proof step. |
| Scalar quartic/noise equivalence | Named prior supported import, not re-proved or executed here. |
| Zhang ancestry and novelty | Retained exactly; no clean priority claim follows from this covariance proof. |
| Formal/kernel, human, configured dual-family, cross-vendor or executable certification | Not performed. |

**Scoped return:** the ENTIRE v3 TC/covariance/rank-two-containment/BRIDGE argument and its CLIP boundary are WRITTEN-SUPPORTED by this actual complete supplied-proof reconstruction. It retains all stated physical quantifiers and does not assume a common multivector rotation. Parent disposition remains separate. No author/shared/pinned file was modified and no historical unadmitted computation gained credit.
