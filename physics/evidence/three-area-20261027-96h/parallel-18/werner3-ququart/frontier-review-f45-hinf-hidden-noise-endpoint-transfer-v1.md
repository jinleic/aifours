# f45 — hidden-noise physical endpoint transfer and Hilbert projection necessity

Reviewer **PhysicsResearch96h-2 / physics-1**. Actual native clock before writing: **Wed Oct 28 17:39:17 PDT 2026**. This is a disjoint **same-harness written scientific review**, not human/other-model-family, formal/kernel, novelty or parent adoption. Prior Info-3/w66/w86/w95b review contacts and own physics history are disclosed; this is not a blind or cognition-independence claim.

## 1. Verdict and exact scope

**NO SUBSTANTIVE DEFECT FOUND AT THE EXACT STATED SCOPES. FATAL 0 / MAJOR 0 / MINOR 0.**

- **Hidden-noise theorem:** for every fixed finite-horizon law and plant satisfying the stated finite set of observability-kernel identities, the SAME original regulated output is a deterministic bounded path operator of the actual progressive input. Its literal E1 and E2 gains equal that operator norm; endpoint pointwise strictness transfers exactly according to norm attainment. The identities are **sufficient**, not claimed necessary.
- **Projection theorem:** under finite common gain, strictness for every nonzero progressive E2 input, and an actual E1 endpoint attainer nonzero as a whole time-path almost surely, the adjoint normal equation, zero-output-event constraint and strict nonprogressivity/projection gap are necessary. They are **not sufficient** and do not exclude attainers lacking the full-support hypothesis.
- **Nonvacuity:** the entire displayed two-state family has nonzero possible hidden diffusion, exact endpoint norm one and pointwise strictness without uniform endpoint margin. Its proof is not a replacement performance output or a general synthesis result.

I reconstructed the used E1 localization/output-domain and progressive Hilbert-space facts below, rather than treating a prior status/adoption or an author's numerical output as proof. The author's numerical checks were not rerun or adopted as independent evidence; a separately written bounded physical diagnostic is reported in §8.

## 2. Inputs, actual order and limits

The assignment `review-waves/f45-hinf-hidden-noise-endpoint-transfer/assignment-v1.json`, SHA256 `86cb04bfe7a2215467dd769f735f68fcef92407847da94ebfaa9eac98455faf7`, was read completely FIRST after dispatch. The prior physics-1 scientific step was pinned before this review in `frontier-20261028-pre-f45-physical-certificate-frontier.json`; its ongoing finite CRT job later completed and its actual result was reported separately. It is not a premise of this disjoint review.

The following complete source bodies were read; live SHA256s match the assignment where specified:

| Label | Source | SHA256 | Coverage |
|---|---|---|---|
| H | `frontier-20261028-hidden-noise-physical-endpoint-transfer.txt` | `366928983cb15e3be5a200897f98c9c330e97f5a9c5b32719b07a6c3a5f91f46` | LF1–97 complete |
| A | `frontier-20261028-hilbert-projection-endpoint-candidate.txt` | `cd5541076f0fde5bea86ea6470e1b4bd16e146c78cf5924ea5f13072527a685e` | LF1–108 complete |
| DEF | `info-3-literal-criterion-definitions-v1.md` | `891ab168ce9b2b0c551dfa35b83ae99acef4b7ca5a1c71420e6d9c19f0633fad` | LF1–29 complete |
| LAW | `info-3-linear-preview-class-definitions-v1.md` | `9b72aca5c3434827f43bc81e3fcd3cfc5f72d4ddbf4c7df3943444f10e9151cd` | LF1–11 complete |
| DOM | `output-only-E1-E2-literal-domain-equality-v1.md` | `857ec99cc1be5d4ce2cd204fd7b0b01983d8bb8b3c8e633854b75370fb78da28` | complete through ending |
| REG | `e1-e2-endpoint-progressive-projection-regularizer-v1.md` | `0c9f5686e7b336fa2d910c6176a6c1271919d9cbd6ab66c3a898cd6ef0f9aa1d` | complete through ending |

H/A/DOM/REG are under `information-science/evidence/three-area-20261027-96h/parallel-18/stochastic-hinf-preview/`; DEF/LAW are under the run's `written-releases/`. DEF states the printed expectation of pathwise L2 norms; its book transcription does not certify every adopted technical convention. LAW binds the deterministic stationary linear class and zero extension. H/A explicitly add the E1 local-control interpretation. No old held outcome, source-specific guide or parent status is used as a mathematical premise. I did not contact the author.

The source's gamma is positive; T>h>=0; matrices are arbitrary finite compatible real matrices and state dimension n>=1. The input interval is J=[0,T−h], zero outside J, including the uncharged final window, and output interval I=[0,T]. E1 means progressive pathwise-L2 with finite positive E||w||; E2 additionally has finite E||w||². The same original law and Brownian space are used throughout. No result is asserted for a general nonlinear/time-varying controller, nonzero initial state, absent zero extension or other book-domain interpretation.

## 3. Exact claim ledger

| Source and lines | Disposition |
|---|---|
| H LF7–35: all-matrix hypotheses, h boundaries, deterministic S and strictness claims | Reconstructed §§4–6; sufficient, not necessary |
| H LF39–56: actual physical closed-loop/CH stack/pathwise operator | Reconstructed §5, including localization and all stochastic couplings |
| H LF60–64: E1/E2 literal gain and all gamma/attainment branches | Reconstructed §6; pointwise and uniform distinct |
| H LF68–85: full a>0, T>0, arbitrary real sigma family and exact endpoint | Reconstructed §7; no nonzero-state stability inference |
| A LF7–32: exact finite model, H+ and bounded original E2 map | Reconstructed §§4,9; local output-domain assumptions explicit |
| A LF36–52: two-sided variation, zero-output event and Hilbert adjoint | Reconstructed §10; no progressive normalization assumed |
| A LF56–78: nonzero projection, strict projection gap and progressive-direction consequence | Reconstructed §11; necessity only under H+ |
| H LF87–97 and A LF80–103: author-reported numerical checks | Not used as independent evidence; our separate check is §8 |
| General endpoint/synthesis, absent H+, unrelated controller domains, novelty/formal acceptance | Not proved or asserted by this review |

No historical HELD outcome is promoted by chronology, a favorable verdict, or this new assignment. Candidate source/hypothesis limitations remain.

## 4. Used physical input/output prerequisites, reconstructed

Put S0=T−h and use the actual feedforward window operator

`Rv(t)=L0v(t)+Lh v(t−h)+integral_0^h H(r)v(t−r)dr`.

Zero extension and Minkowski/Cauchy–Schwarz give the pathwise bound

`||Rv||_[0,T] <= (||L0||+||Lh||+sqrt(h)||H||_2)||v||_J`.

At h=0 the taps combine and the integral is absent. All arguments are at or before t, so R preserves progressiveness. Joint measurability plus finite convolution permits an a.e. progressive version; no terminal input norm or future random information is fed to the law.

For E2 inputs, define P=A+BK, Q=A0+B0K, O=D0+D1K. The physical closed loop is

`dx=(Px+B Rw+Cw(t−h))dt+(Qx+B0Rw)dW`,

`z=Ox+D1Rw`.

Itô isometry, time Cauchy–Schwarz and elementary Gronwall give finite E2 state/control/output on [0,T] and bounded linearity of the ACTUAL map T2:H→Y; ordinary finite-dimensional linear-SDE strong existence/uniqueness is the named standard import. The proof retains B0, Q and delay, and does not use an RMS gain as the literal performance criterion.

For E1 inputs, U=||w||_J is finite a.s. Define the progressive energy stop tau_N by accumulated input energy reaching N and `w^N=w*1_(t<tau_N)`, zero outside J. Then `||w^N||_J²<=N` pathwise, so w^N is an actual E2 input. Causality of the same R and strong uniqueness make the local solutions agree before the common stop. On each finite-energy path, some N exceeds total energy and w^N=w throughout J; the patched process is the unique actual nonexplosive local solution, and its original control is pathwise L2 on compact intervals. This pays the used DOM local-solution edge without an unprovided state-energy theorem.

The same truncations also reconstruct the **used** output-gain equality. If G_E2=∞, inclusion E2⊂E1 gives G_E1=∞. If G_E2=g<∞, then `E||Z(v)||<=g E||v||` for every E2 v. Linearity of the same SDE yields the same bound for differences w^N−w^M; dominated convergence gives w^N→w in L1(Omega;L2(J)), so the actual E2 outputs are Cauchy in L1(Omega;L2(I)). On each path the stopping eventually disappears, identifying the limit with the actual patched output. Thus G_E1<=g, while inclusion gives the reverse. No expected E1 state/control energy or separate NR-GAIN bound is inferred.

The progressive E2 subspace H is closed in product L2: it is L2 of the completed progressive sigma-field with respect to dt×P, and an L2 limit has an a.e.-convergent subsequence with a progressive version. Hence its Hilbert orthogonal projection exists. REG's particular regularizer is not needed for the new normal equation or H's deterministic-output theorem, and no unproved output/multiplier commutation is imported.

## 5. Cayley–Hamilton stack pays the ACTUAL hidden-noise caller

Assume H's conditions for all j=0,…,n−1:

`O P^j Q=0`,

`O P^j B0 L0=O P^j B0 Lh=0`, `O P^j B0 H(r)=0` a.e. for h>0. At h=0 use the single combined L0+Lh condition. By linearity and Fubini, `O P^j B0 Rw(t)=0` for a.e. t along every actual admissible path. Thus multiplying the actual SDE by O P^j kills BOTH stochastic terms, not just their expectations.

For the physical state x define `Y_j=OP^j x`, j=0,…,n−1. These are intermediate coordinates of the SAME original state, not changed performance variables. Their exact equations are

`dY_j=Y_(j+1)dt+OP^j(BRw+Cw(t−h))dt` for j<n−1,

and the last row uses Cayley–Hamilton `P^n=Σ_(j=0)^(n−1)c_jP^j`. Hence the stack closes as a finite deterministic linear ODE with the actual random input path as forcing. No invertibility, observability, stability or rank assumption on P is needed; n=1 is included by the same characteristic identity.

For x^d satisfying `(x^d)'=Px^d+BRw+Cw(t−h)` with zero initial state, its OP^j stack has the SAME closed ODE/forcing/initial values. Pathwise deterministic ODE uniqueness gives `Ox=Ox^d`, simultaneously on the finite horizon. E1 inputs are covered by the actual localization/patching of §4, not by taking an unjustified stochastic expectation inside a path-dependent product.

Therefore the original output is, for every actual E1/E2 path,

`z=S w`,

`(Sv)(t)=O integral_0^t exp(P(t−s))[B Rv(s)+C v(s−h)]ds+D1Rv(t)`.

The finite exponential Volterra kernel and bounded R make S a deterministic bounded real L2(J)→L2(I) operator. The hidden components of x may remain stochastic. No claim that physical diffusion itself is zero, that noise is unobservable under every other law, or that these sufficient identities are necessary follows.

## 6. Literal gains, endpoint face and all zero cases

For each path `||Sw||<=||S||||w||`; expectation gives BOTH literal gains <=||S||. Every deterministic nonzero L2 input is progressive E2, so the operator norm supremum gives both gains >=||S||. This holds even if the norm is not attained, since deterministic approximate maximizers suffice.

Let M=||S||. If M>0 and gamma=M:

- A nonzero real norm-attainer is an admissible deterministic E2 disturbance with ratio exactly M, so pointwise strictness fails in both domains.
- If there is no nonzero norm-attainer, every nonzero path has `||Sw||<M||w||`. For any E1 input with positive expected norm, that nonnegative gap is positive with positive probability and is bounded by the integrable M||w||. Its expectation is strictly positive, proving the literal strict ratio for EVERY nonzero E1 input and hence E2 input.

Thus the stated iff and E1/E2 pointwise transfer are exact at the endpoint, without commuting a random amplitude with the stochastic state map. At gamma>M, the same M is a uniform common margin; at gamma<M an actual deterministic near-maximizer violates the inequality. At gamma=M uniform strictness G<gamma fails whether or not the norm is attained. If M=0, every prescribed gamma>0 is uniformly feasible. These cases establish the asserted E1/E2 equivalence for every permitted gamma without claiming a gamma=0 convention.

## 7. Whole nonvacuous two-state family

For arbitrary a>0, finite T>0 and every real sigma, take h=0, u=w and

`dx1=(−a x1+w)dt`, `dx2=(sigma*x2+w)dW`, `z=w−a x1`.

The matrices displayed by H give `OP^jQ=0` and `OP^jB0(L0+Lh)=0` for both required j, for every a,sigma. In particular sigma need not be zero; x2 can carry nontrivial hidden diffusion. For any nonzero deterministic input, if its hidden diffusion coefficient vanished a.e. almost surely, the zero-initial continuous local martingale x2 would be zero and then w would vanish a.e.; hence the channel is genuinely nontrivial for that input.

The actual x1 is absolutely continuous and w=x1'+a x1, z=x1'. Integration by parts gives, on every input path,

`||w||²−||z||²=a*x1(T)²+a² integral_0^T x1²dt`.

For nonzero w the right side is strictly positive: if x1=0 a.e., absolute continuity gives x1'=0 a.e. and w=0. Thus every nonzero E1 path has strict norm ratio below1, and the expected literal inequality is strict for every E1 input.

For the entire deterministic family `v_n=sqrt(2/T)sin(n*pi*t/T)`, all norms are1. With omega_n=n*pi/T, direct integration gives the source's convolution expression and bounds its L2 norm by a constant times `(a+2omega_n)/(a²+omega_n²)`, hence it tends to0. Consequently `||S v_n||→1`. The common gain is exactly1, but no nonzero norm-attainer exists; endpoint pointwise strictness holds and uniform strictness fails. This is a full symbolic family, not a proof that every law has that property.

## 8. Independent bounded physical check — diagnostic only

I wrote `frontier-review-f45-hidden-noise-independent-check.py`, SHA256 `b37781bab07c5457a70ae5dd4b43bd1c3b7db775ffd05a56af1d89108b6507bf`, and ran exactly:

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 frontier-review-f45-hidden-noise-independent-check.py`.

Result `frontier-review-f45-hidden-noise-independent-check-results.json`, SHA256 `4715722e80d3907af7d57b8c9762dbcd51e5141c0bed0a8b86841c56f7ff5a25`: PASS; numpy2.4.3; 4096 paths,192 cells, T=1.1, a=1.3, **sigma=0.7**, seed20261028045; progressive piecewise-constant input `w_i=1+W(t_i)/4`. The per-cell x1/output/input-energy integrals used the analytic exponential formulas evaluated in floating point; the hidden x2 used Euler–Maruyama only.

Observed maximum scaled energy-identity residual `2.057839872182219e−15`; strict sampled paths `4096/4096`; maximum sampled path ratio `0.714474755447748`; mean absolute terminal hidden Euler state `0.8095704067525242`. These are **finite-sample floating-point diagnostics**, not evidence that all E1 paths satisfy the theorem or that the Euler state is an exact SDE sample. The universal proof is §7, not these data. No author checker/results were imported or represented as independent reproduction.

## 9. The actual bounded Hilbert map and full-support assumption

For the fixed original law, H is the progressive product-L2 input Hilbert space on J; Y is the full product-L2 output Hilbert space on I. The standard finite SDE estimate in §4 defines a bounded **actual original-output** linear map `T2:H→Y`. A Hilbert adjoint T2* therefore exists. It is not identified with a BSDE, an anticipating state map or an unprovided martingale representation.

Let gamma>0 be the finite common literal gain; suppose every nonzero E2 input is strictly below gamma, and an actual E1 w attains gamma with `U=||w||_J>0` almost surely. E1 implies U finite a.s. Let z=Z(w), V=||z||_I, `s=w/U`, and `p=z/V` on {V>0}, p=0 otherwise. Then s has unit path norm a.s. and belongs to the full product-L2 space; p has path norm1 on {V>0} and0 otherwise, hence belongs to Y. Neither s nor p is asserted progressive.

For any actual v∈H, w+epsilon v remains E1 and, for sufficiently small real epsilon, has positive expected input norm by the reverse triangle inequality. Linearity and uniqueness of the localized same-law SDE give `Z(w+epsilon v)=z+epsilon T2v`. Since gamma is the finite E1 gain,

`F(epsilon)=gamma E||w+epsilon v||−E||z+epsilon T2v||>=0`, `F(0)=0`.

## 10. TWO-SIDED variation and zero-output event

Because U>0 a.s., the input norm's right and left derivatives both equal `<s,v>_J` pathwise. Every input difference quotient is bounded by ||v||_J, whose expectation is finite. On {V>0}, the output norm derivative is `<p,T2v>_I`; on {V=0}, its right derivative is +||T2v||_I and its left derivative is −||T2v||_I. Output difference quotients are bounded by ||T2v||_I, integrable since T2v∈Y. Dominated convergence justifies both expected derivatives.

Write

`A_v=gamma E<s,v>−E<p,T2v>`,
`B_v=E[1_(V=0)||T2v||]>=0`.

At the minimum, the left derivative `A_v+B_v<=0` and right derivative `A_v−B_v>=0`. Therefore **B_v=0 and A_v=0**, for every v∈H. By Hilbert Riesz/adjoint and the orthogonal projection r=P_prog s,

`T2* p=gamma r` in H,

`E[1_(V=0)||T2v||]=0` for every actual v∈H.

This establishes BOTH conclusions, including the nonsmooth zero-output event, with no differentiation at an unnormalized zero input because H+ excludes that event. If a specific actual v0∈H has `P(||T2v0||>0)=1`, the latter equality forces P(V=0)=0. The candidate correctly makes that extra v0 existence conditional, not automatic.

## 11. Strict projection gap, nonzero r and exact residual

Let tau_N be the progressive input-energy stop of §4 and w_N the stopped actual E2 input. Since U>0 a.s.,

`<s,w_N>_H=E[||w_N||_J²/U]=E[min(U²,N)/U]>0`.

The integrand is bounded by U, so this is finite. If r=P_prog s were zero, its Hilbert inner product with every w_N would be zero, contradicting this positive value. Thus r is a NONZERO actual progressive E2 input.

Apply the normal equation to v=r. Pathwise ||p|| is at most1, and the strict E2 hypothesis applies to r:

`gamma||r||_H²=E<p,T2r> <= E||T2r|| < gamma E||r||_J`.

Cauchy–Schwarz in probability and orthogonal projection contraction give

`0<||r||_H²<E||r||_J<=||r||_H<=1`.

It follows `||r||_H<1`. Because `||s||_(L2(P×J))=1`, Pythagoras gives

`||s−P_prog s||²=1−||r||_H²>0`.

This is a strict product-L2 distance from the progressive subspace, not a uniform lower bound or an admissible normalized-input construction. If s itself were progressive, r=s, `||r||_H=E||r||_J=1`; the normal equation and gain bound then force the actual E2 input s to attain gamma, contradicting the strict E2 hypothesis. No false assumption `Z(w/U)=Z(w)/U` is used.

The exact remaining gap is whether the actual finite-dimensional SDE can support such a nonprogressive normal-equation configuration, and separately whether an endpoint attainer with P(U=0)>0 can exist. The new necessary conditions do not rule either out and are not claimed sufficient.

## 12. Final review disposition

The complete hidden-output stack and fixed-law endpoint theorem, its whole physical example, and the full-support Hilbert-adjoint/projection necessities are supported at their exact hypotheses by the written reconstructions above. **FATAL0 / MAJOR0 / MINOR0.**

No unrestricted physical E1/E2 endpoint theorem, generic nonlinear preview synthesis criterion, optimal controller, E1 global state/control moment bound, book-domain equivalence, all-realization statement or novelty follows. The sample is diagnostic only. Author-reported experiment outputs remain author reports, not independently certified by reproducing their script. Parent must review complete source and this complete return before any disposition; no formal/kernel, independent model-family or human verification has occurred. Existing historical quarantined outcomes are not accepted premises or reclassified as successful.

**END COMPLETE f45 SCIENTIFIC REVIEW — EXACT GIVEN-LAW AND FULL-SUPPORT NECESSITY SCOPES ONLY.**
