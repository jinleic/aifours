# w14 physics-3 — complete complement/Kraus/dual-budget review

Reviewer **InfoResearch96h-2**, info-1. Author **PhysicsPPT44-2**, physics-3. Actual native prewrite clock: **Tue Oct 27 15:06:54 PDT 2026**; first duty observation **15:05:28 PDT**.

**Verdict: NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE. 0 FATAL / 0 MAJOR / 0 MINOR.** The universal primal complement theorem, explicit dual TRACE-complement decomposition, same-pair budget and fixed positive-reconstruction cone barrier are SUPPORTED in writing. No conclusion that every PPT state is SN<=2, that every 2BP witness is decomposable, or that an original 4x4 negative state/witness pair exists follows.

## 1. Complete frozen inputs and exposure/assurance boundary

Read the entire manifest first, raw LF1–28: SHA256 `405c9fc4577f1b78d4819fbcbbf7718117e0eba950342f72802cadf67b856aef`, 28LF/2154B.

The SINGLE supplied part was pin-matched and read **raw LF1–251 COMPLETELY through S2|208**, including both context and author endings: `packet-part-1-v1.md`, SHA256 `b9fb8a7f9e1f15bfa70717cacabbdba3d3397bd68953e59bd8ca4bfcb3f257cd`, 251LF/25683B. It includes ALL:

- **S1 CONTEXT:**35LF controls/parent-definition packet, pin `4715d2190da98abb8781bb5713e9c45af51c73dd43e85fd3cc54e5e92351279a`.
- **S2 AUTHOR:**208LF prerequisite derivation, pin `7d00196376108da34c416b8e80f815adfc337d01cb24191f8ad40f6a47d8cdc4`.

All citations below use the supplied OUTER S1/S2 labels. No primary-paper link, linked ACK, old PPT part, N4 material, review/park/checkpoint, construction or author contact was opened. The paper-screen quotes/DOM history in S2 LF15–34 are author-reported source-extraction evidence, not freshly authenticated by this reviewer. Those quoted statements carry no load-bearing premise of the matrix derivation, as the author explicitly says. This review does not certify that browser chronology or prove absence of any other prior result.

**Prior contact/exposure:** the inherited safe round history contains this author's prior privacy/MDA-related review contact and my earlier PPT/complex-rank review exposure. This is not blind or an independent configured-family gate. An exhaustive historical reciprocal-contact/cognition census is not established, and no old body was retrieved to create one. The author's disclosed earlier fixed-reduction/control exposure and every associated finding remain; a correct universal identity does not retrospectively certify its method provenance or cleanse a ZERO consumer. Current checks below use only the frozen definitions and explicitly reconstructed elementary matrix facts. No old instance, selected vector, private guide or prior verdict is input.

Only this requested review output is written. No scientific execution, calculator/CAS/interpreter/Eval, selected state/dimension/boundary probe, enumeration, replay, model CLI, nested agent or other mathematical source was used. The info-1 source-equivalence line remains deferred.

## 2. Exact objects and scope

The supplied original problem is the unrestricted complex 4x4 PPT/SN>=3 state-plus-universal-SR2-separator alternative, or a proof every such PPT state has SN<=2. The candidate proves identities for `A=C^a`, `B=C^b`, arbitrary integers a,b>=2, with a separate a,b>=3 condition for its map-cone barrier. The original 4x4 caller is included; it is not replaced by a proper state/witness ansatz.

C2 is the UNNORMALIZED cone of finite sums of rank-one projectors on complex Schmidt-rank-at-most-two vectors, including zero. W is arbitrary Hermitian and nonnegative on EVERY such vector. Therefore `Tr(WZ)>=0` for any actual C2 decomposition. No real-only vector test, normalization/inverse-marginal assumption or rank-floor theorem is substituted.

Define the actual maps exactly as S2 LF40–46:

`D_A(X)=I_A tensor Tr_A X`, `D_B(X)=Tr_B X tensor I_B`,

`D_0(X)=Tr(X) I_AB`, `R_A=D_A-id`, `R_B=D_B-id`.

All traces are ordinary unnormalized partial traces. These maps act on the SAME input operator. The supplied SN/separator equivalence is a parent definition-side premise, not an independent source-construction authentication by the present review.

## 3. Gate A — alternating rank-two Kraus identity and full complex signs

**S2 LF54–71: SUPPORTED.** In the declared basis let `A_ij=E_ij-E_ji`, i<j. Its image is the two-dimensional coordinate plane, so its rank is exactly two. Direct matrix-unit multiplication for arbitrary COMPLEX X gives

`A_ij X^T A_ij†=X_jj E_ii+X_ii E_jj-X_ij E_ij-X_ji E_ji`.

Summing over unordered pairs contributes `sum_(j!=i)X_jj` to the i-th diagonal and `-X_ij` to EVERY ordered off-diagonal position. Hence

`R_d(X)=Tr(X)I-X=Psi_d(X^T)`,

`Psi_d(X)=sum_(i<j) A_ij X A_ij†=Tr(X)I-X^T`.

The transpose order/signs are correct; no conjugate of an off-diagonal entry was inserted in this complex-linear identity. Psi is CP by its explicit Kraus sum. R itself is NOT claimed CP. The full R identity is basis-invariant; the transposes and Kraus coordinates use the same chosen basis throughout.

If Z is positive on a bipartite space, its finite spectral decomposition and a local map L of rank at most two give a sum of projectors on `(L tensor I)`-images. Each image lies in `im(L) tensor B`, so its coefficient-matrix/Schmidt rank is at most two. With two rank-two local maps both local supports have dimension at most two, again giving rank at most two for every output vector. Zero vectors, singular operators and vanishing terms remain legitimate cone elements. This is a finite explicit decomposition, not an unprovided cone-closure argument.

## 4. Gate B — the three actual primal complements, all PPT cases

**S2 LF75–106: SUPPORTED.** For PPT rho, `rho^(Gamma_A)=(rho^(Gamma_B))^T` is positive because FULL transpose preserves positivity. The previous identity gives the exact operator

`R_A(rho)=sum_(i<j)(A_ij tensor I)rho^(Gamma_A)(A_ij† tensor I)`.

Gate A proves each term positive with Schmidt number at most two; hence the entire one-sided complement is in C2. The Bob-side formula uses its own rank-two matrices and Gamma_B and proves the same result for R_B.

For the additional PPT property, Gamma_B commutes with R_A (the maps are on different factors). It also commutes with R_B: partial trace over B is transpose-invariant and I_B is unchanged. Applying the one-sided argument to the positive PPT operator `rho^(Gamma_B)` proves `R_A(rho)^(Gamma_B)>=0` and likewise the R_B case. No partial transpose of a general positive C2 decomposition is falsely assumed positive.

The double complement has the stronger formula

`R_A R_B(rho)=(Psi_a tensor Psi_b)(rho^T)`

`=sum_(i<j,k<l)(A_ij tensor B_kl)rho^T(A_ij† tensor B_kl†)`.

FULL transpose is positive for EVERY positive rho. Both local images in every summand have dimension at most two, so this proves unconditional C2 membership, without a PPT premise. For PPT rho, commute Gamma_B through both maps and apply that same all-positive-input assertion to `rho^(Gamma_B)` to obtain the additional PPT property.

Expanding the commuting maps uses `D_A D_B=D_B D_A=D_0` and yields

`X_AB=sI_AB-I_A tensor rho_B-rho_A tensor I_B+rho`.

Adding X_A and X_B gives exactly `X_A+X_B+X_AB=sI_AB-rho`. Thus the SOURCE TRACE-COMPLEMENT, not rho itself, is C2 for PPT inputs. All expressions are generally unnormalized; zero outputs remain zero. No division by a trace, rank or eigenvalue appears.

## 5. Gate C — explicit positive operators in the dual TRACE-complement decomposition

**S2 LF110–136: SUPPORTED.** Put `K_A=(Psi_a tensor id)(W)`, `K_B=(id tensor Psi_b)(W)`. For each Kraus congruence and EVERY vector phi,

`<phi,(A_ij tensor I)W(A_ij† tensor I)phi>`

`=<(A_ij† tensor I)phi,W(A_ij† tensor I)phi>>=0`,

because the pulled-back vector has Alice support at most two. Thus each summand and hence K_A is positive. The analogous Bob support argument proves K_B positive.

Transposing the local reduction identity gives

`(R_A W)^(Gamma_A)=K_A`, `(R_B W)^(Gamma_B)=K_B`.

Since Gamma_A followed by FULL transpose equals Gamma_B,

`(R_A W)^(Gamma_B)=K_A^T>=0`.

This is the correct full-transpose step; no positivity-preservation assertion for arbitrary partial transpose is needed.

For `Z_W=R_A R_B(W)`, apply the double rank-two congruence formula to W^T. Full transpose preserves TWO-BLOCK-POSITIVITY: the expectation on v is the corresponding real expectation of W on bar(v), whose Schmidt rank is unchanged. Pullback by `A_ij† tensor B_kl†` gives Schmidt rank at most two for EVERY phi, so each congruence of W^T is positive even though W itself need not be positive. Therefore Z_W is positive.

Finally, the exact superoperator identity

`R_A+R_B+R_A R_B=D_0-id`

gives

`Tr(W)I_AB-W=Z_W+(K_A^T+K_B)^(Gamma_B)`.

BOTH displayed pre-transpose operators are explicitly positive, proving the claimed decomposable TRACE-COMPLEMENT. It is not a decomposition of W and does not imply every 2BP witness is decomposable. The proof does not require an unprovided general dual-cone or decomposability theorem.

## 6. Gate D — same-pair budget, signs and one-way implications

**S2 LF140–161: SUPPORTED.** Let `a0=Tr(Wrho)`, `b_A=Tr(W(I_A tensor rho_B))`, `b_B=Tr(W(rho_A tensor I_B))`, `t=sTr(W)` for the SAME actual pair. These expectations are real. For positive rho the marginal-noise operators and sI are separable positive operators, so W's SR2 positivity implies `b_A,b_B,t>=0`.

Pairing W with the explicit complements gives

`Tr(W X_A)=b_A-a0`, `Tr(W X_B)=b_B-a0`,

`Tr(W X_AB)=t-b_A-b_B+a0`.

The first two are nonnegative for PPT rho, proving the two upper bounds. The last is nonnegative for EVERY positive rho by the unconditional double-complement result, proving the lower bound. Hence exactly

`b_A+b_B-t <= a0 <= min(b_A,b_B)`.

Pairing the decomposable trace-complement with PPT rho also gives `a0<=t`, with the same transpose convention. Thus actual strict negativity requires `b_A+b_B<t`; if the actual pair has `b_A+b_B>=t`, its negativity is excluded. The candidate correctly does not make this strict budget inequality sufficient for negativity, PPT, 2BP or existence of an eligible pair.

All zero cases work directly: rho=0 or W=0 makes the four quantities zero, while singular marginals/zero complement components require no limiting regularization or cancellation. No old fixed witness/state instance is used to establish these universal inequalities.

## 7. Gate E — fixed positive complement-iteration/noise cone barrier

**S2 LF167–187: SUPPORTED for the EXACT stated cone.** Here a,b>=3. The permitted noise additions are specifically nonnegative multiples of the three displayed maps `D_A,D_B,D_0`; this verdict does NOT expand the theorem to arbitrary separable CP/noise maps or state-dependent reconstructions.

On each local Hermitian operator space use the complete direct sum of scalar identity and traceless operators. Their tensor product spans ALL Hermitian bipartite operators; complex-linearity then covers the full complex operator space. From the unnormalized definitions, R_A acts by `a-1` on Alice's identity sector and by `-1` on its traceless sector; R_B analogously uses b-1 and -1. Therefore every nonempty monomial has the four scalar sector actions stated in S2 LF171–176, in the correct A/B order.

Put `mu=min(a-1,b-1)>1`. For any nonempty powers p,q, its identity/identity eigenvalue is `(a-1)^p(b-1)^q>=mu`, whereas its traceless/traceless eigenvalue has absolute value one. For nonnegative coefficients c_(p,q),

`lambda_00>=mu sum c_(p,q)>=mu |sum c_(p,q)(-1)^(p+q)|=mu|lambda_11|`.

D_A,D_B,D_0 have nonnegative identity/identity eigenvalues and zero traceless/traceless action, so their positive additions preserve this inequality. A positive scalar multiple of id has both sector values equal to the same positive scalar, contradicting mu>1. The zero map is not falsely excluded.

The relevant diagonal-sector map space is finite dimensional and closed; both sector eigenvalues are continuous linear coordinate functionals. Thus any superoperator-norm limit still obeys the inequality and cannot equal a positive multiple of id. This is a whole-operator-space proof, not a spectral experiment on selected inputs. The a,b>=3 condition is used essentially at mu>1 and includes the actual 4x4 target.

Every nonempty complement iteration maps PPT inputs to PPT C2 operators: perform the first one-sided step from Gate B, then iterate its PPT-preserving property. The named noise maps send positive inputs to separable operators. Nevertheless the fixed nonnegative map cone cannot reconstruct the identity superoperator. This blocks exactly that fixed-positive-combination mechanism; it does not block state-dependent coefficients, arbitrary other maps or every possible proof of PPT-to-C2.

## 8. Final exact-scope decisions and original limit

- **Alternating rank-two Kraus identity and actual cones:** SUPPORTED, with full complex entries and all zero/singular cases.
- **R_A rho/R_B rho/R_A R_B rho for PPT rho, and unconditional double-complement C2:** SUPPORTED; no SN2 cancellation or illegal partial-transpose positivity assumption.
- **Explicit decomposable `Tr(W)I-W`:** SUPPORTED for every Hermitian 2BP W, not a decomposition of W.
- **Actual joint budget:** SUPPORTED with the exact lower/upper premises and non-converses.
- **Fixed positive-reconstruction barrier:** SUPPORTED only for nonempty complement monomials, the three named noise maps and their norm limits at a,b>=3.

The genuinely missing original implication remains cancellation from the complements to rho, or an actual eligible PPT state and universal complex-SR2 separator with negative expectation. No such object or universal no-go has been obtained. The author's primary-claim screen is explicitly restricted and no source construction is used; no broader publication/SOTA or original-source assertion is newly authenticated by this review.

**0 FATAL / 0 MAJOR / 0 MINOR at the entire frozen supplied scope.** All old process findings, exposure/control histories, Parts24–40/post40/N4/QD ZERO boundaries, N4 UNKNOWN/historical exit unestablished and auxiliary214 STOP remain. Correct universal algebra is not a process cure, noninfluence certificate, novelty claim, configured-family/human/formal/kernel/executable review or parent adoption.

**END COMPLETE w14 REVIEW — manifest, sole part and both source endings read; no author contact or other mathematical source.**
