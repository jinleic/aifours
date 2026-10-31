# f54 — delayed reachable-diffusion characterization

Reviewer **PhysicsResearch96h-2 / physics-1**. Actual native clock before writing: **Wed Oct 28 17:48:46 PDT 2026**. This is a disjoint **same-harness written scientific review**, not formal/Lean-kernel, human/configured-family, novelty or parent adoption. I previously reviewed the sufficient hidden-noise predecessor under f45; that contact is disclosed and its verdict is **not** substituted for the iff proof here. No author contact occurred.

## 1. Exact verdict

**NO SUBSTANTIVE DEFECT FOUND AT THE EXACT STATED FINITE-HORIZON GIVEN-LAW SCOPE. FATAL 0 / MAJOR 0 / MINOR 0.**

For every finite T>h>=0, arbitrary compatible real matrices, one scalar Brownian motion and the explicitly adopted zero-state/zero-extended deterministic stationary linear law, I reconstruct the equivalence:

1. The actual original output is deterministic for **every deterministic L2 input**.
2. The source-defined reachable diffusion subspace D is contained in the output-unobservable subspace N.
3. One deterministic bounded time operator maps **every actual progressive E2 and E1 input path** to the same original output path.

The h>0 range matrix, separation of its two direct atoms from the Hilbert–Schmidt kernel, the tied `BLh+C` term, h=0 coincident-atom boundary, full stochastic necessity induction, actual random-input converse and endpoint strictness are all paid below. This is an iff for the **deterministic-output subclass**, not a necessary condition for E1/E2 endpoint transfer in all stochastic-output laws and not a general controller-synthesis theorem.

## 2. Actual input order, binding and scope

After pinning the prior primary physics step, I read the complete assignment FIRST:

- `review-waves/f54-hinf-delayed-noise-characterization/assignment-v1.json`, SHA256 `44333d737346638a74611b1c709970be43d34d5adf91fd652383685bba484d29`.
- Main candidate `frontier-20261028-delayed-reachable-diffusion-characterization.txt`, SHA256 `52171f6ae7f9659642884edb87e197cb19398e1b3918227e7ee5d16f56b9de06`, **LF1–114 complete**; this matched the assignment.
- Its expressly named h=0 predecessor `frontier-20261028-reachable-diffusion-exact-output-characterization.txt`, SHA256 `f57dd467c5761b986d683f7d16fa5f15061a5dab07d1664825bc6c610d490844`, read complete through ending. It is context for the special case; the h>0 proof below is reconstructed from the new candidate, not transferred from the predecessor/f45 review.
- The registered literal criterion and linear law were read in the immediately preceding f45 duty, at hashes `891ab168ce9b2b0c551dfa35b83ae99acef4b7ca5a1c71420e6d9c19f0633fad` and `9b72aca5c3434827f43bc81e3fcd3cfc5f72d4ddbf4c7df3943444f10e9151cd`; the actual E1 local-output-domain source was read complete at `857ec99cc1be5d4ce2cd204fd7b0b01983d8bb8b3c8e633854b75370fb78da28`. The used E1 localization is reconstructed in §6, not imported as a status-only claim.

The first attempted combined metadata hash command successfully printed the candidate and assignment hashes but used the wrong working directory for the final checkpoint path; I then separately hashed the exact owner-root checkpoint successfully. No source was changed. The pre-f54 physical checkpoint is `frontier-20261028-pre-f54-physical-certificate-frontier.json`, SHA256 `6b01b4b195b52129408faa5ea324ab5d08111ea67fd14aeee3a7d47559676b65`.

Source H below means the **new f54 candidate**, not a historical held source. Prior Info-3/w66/w86/w95b/f45 contacts are disclosed; no author-supplied checker output was reused as independent evidence. Existing historical quarantined outcomes remain unvalidated and are not mathematical premises.

## 3. Claim ledger and exact adopted model

| Candidate lines | Disposition |
|---|---|
| H LF7–33: original finite law, three-way equivalence, literal endpoint | Reconstructed §§4–9; fixed law, actual output and E1/E2 domains retained |
| H LF37–58: h>0 kernel with tied `BLh+C`, atom separation and D0=range Gamma | Reconstructed §§4–5; entire coupled-input operator, no independent channel assumption |
| H LF60–64: h=0 combined atom and reachable-span specialization | Reconstructed §5, including zero/rank-deficient cases |
| H LF66–76: invariant-subspace sufficiency for actual progressive random inputs | Reconstructed §6, including pathwise E1 localization |
| H LF78–86: deterministic-output necessity and all-word induction | Reconstructed §7, including exact null-set/continuity boundaries |
| H LF88–104: exact endpoint and nontrivial delayed example | Reconstructed §§8–9 |
| H LF106: author numerical/Fraction output | Not reused as independent check; separate exact rational diagnostic is §10 |
| H LF108–114: unrestricted visible-noise endpoint, synthesis and source limits | Correctly retained; no broader solution inferred |

Write the fixed actual law as `u=Kx+Rw`, with

`Rw=L0w(t)+Lh w(t−h)+integral_0^h H(r)w(t−r)dr`.

All inputs live on J=[0,S], S=T−h>0, and are zero outside J, including the uncharged final interval. At h=0 combine L0+Lh and omit H. The printed problem itself does not certify these process-space conventions; they are the explicit research interpretation. The original state/output equation is retained, with P=A+BK, Q=A0+B0K, O=D0+D1K and `z=Ox+D1Rw`.

For deterministic v let x_v^d solve `x'=Px+B Rv+C v(t−h)`, zero initial state. Define the **actual** deterministic noise-forcing operator

`(Bcal v)(t)=Qx_v^d(t)+B0 Rv(t)`.

Its range-generated subspace is

`D0=span{integral_0^T phi(t)(Bcal v)(t)dt : v∈L2(J), phi∈L2(0,T)}`.

D is its smallest common P/Q-invariant subspace; N=intersection_(j=0)^(n−1) ker(OP^j). All are actual subspaces of the same finite state space, not abstract independent row variables.

## 4. Exact causal convolution and tied delayed drift coefficient

R is bounded L2(J)→L2(I): shifts are contractions and `||H||_1<=sqrt(h)||H||_2`. It preserves progressiveness because every argument is at or before current time. The finite exponential kernel is bounded on [0,T]. Deterministic Fubini therefore gives, for r>0,

`Kx(r)=exp(Pr) B L0
       +1_(r>=h) exp(P(r−h))(B Lh+C)
       +integral_0^min(h,r) exp(P(r−u)) B H(u)du`,

`KB(r)=Q Kx(r)+1_(r<h)B0 H(r)`.

Indeed the delayed state forcing is `B Lh v(t−h)+C v(t−h)` for the **same v**, so its coefficient is `B Lh+C`. The kernel term follows by interchanging the s/u integrals over `0<=u<=min(h,t−input_time)`. All equalities are L2/a.e.; endpoint representatives at the jumps r=h and input cutoffs have no effect.

Consequently for h>0,

`(Bcal v)(t)=G0v(t)+Ghv(t−h)
             +integral_0^S 1_(s<=t) KB(t−s)v(s)ds`,

`G0=B0L0`, `Gh=B0Lh`.

The finite exponential part of Kx is bounded, its H-convolution is bounded because H∈L1 on [0,h], and B0H is L2. Thus KB∈L2(0,T), and the integral operator's kernel is Hilbert–Schmidt. It is therefore compact. This uses the entire same-input operator; it does not assert independent excitability of the two taps and the regular part.

## 5. Range matrix: atoms, kernel, and h=0

For h>0 let

`Gamma=G0G0^T+GhGh^T+integral_0^T KB(r)KB(r)^T dr`.

I reconstruct `D0=range(Gamma)` by comparing orthogonal complements.

If a row ell annihilates D0, then ell Bcal v=0 in L2(I) for every v: all its pairings with scalar test phi vanish. Take any input-space vector e and any positive-length interval J0 strictly inside (0,S), of length<h. Its shift J0+h is disjoint and remains in [0,T]. For an orthonormal sequence phi_m in L2(J0), the actual inputs e phi_m are weakly null. The Hilbert–Schmidt term tends strongly to zero; the two atom outputs have disjoint support and squared norm

`||ell G0 e||²+||ell Gh e||²`.

The zero operator therefore forces both to vanish for every e. This proves atom separation without pretending the channels are independent controls.

The remaining integral operator is zero. Its kernel has squared L2 norm

`integral_0^T min(S,T−r) ||ell KB(r)||² dr`.

The weight is positive for every 0<r<T, so ell KB=0 a.e. Conversely these three row conditions plainly annihilate Bcal. They are exactly `ell Gamma ell^T=0`, equivalently ell⊥range(Gamma). Finite-dimensional orthogonal complements give `D0=range(Gamma)`, including Gamma=0 and deficient rank; no inverse is used.

For h=0 the two atoms act at the SAME time and first combine: `L=L0+Lh`, `F=BL+C`, `G=B0L`, `KB(r)=Q exp(Pr)F`. Thus

`Gamma=GG^T+integral_0^T Q exp(Pr)F F^T exp(P^T r)Q^T dr`.

Its range is `range(G)+Q span{P^k F:0<=k<n}`. For the nontrivial direction, a row annihilating Qexp(Pr)F for a.e. r annihilates it on (0,T) by continuity and then annihilates every derivative at0; Cayley–Hamilton supplies the converse finite-span inclusion. No separate L0/Lh rank sum is substituted at h=0.

## 6. Sufficiency: ACTUAL random inputs, E2 and E1

For each deterministic v, every row orthogonal to D0 annihilates Bcal v a.e.; this follows directly from the test-function definition. Applying it pathwise to any progressive w with L2 paths shows Bcal w(t,omega)∈D0 for almost all time on each such path; finite-dimensional row bases and Fubini suffice, without a simultaneous null set for all possible inputs.

Let x_w^d be the deterministic ODE solution with the SAME random input path, and eta=x−x_w^d for the actual physical SDE. Then

`d eta=P eta dt+(Q eta+Bcal w)dW`, `eta(0)=0`.

If D⊂N, the forcing lies in D0⊂D and both P,Q preserve D. The linear SDE restricted to D has an actual strong solution; uniqueness identifies it with eta, so eta∈D and Oeta=0. The same original output is therefore

`S v(t)=O integral_0^t exp(P(t−s))[B Rv(s)+C v(s−h)]ds+D1Rv(t)`.

Finite kernels make S bounded L2(J)→L2(I). This proves (ii)→(iii) for E2 inputs without interchanging expectation and a stochastic product.

For E1 inputs, use causal energy stops tau_N and `w^N=w 1_(t<tau_N)`. Their squared energy is bounded by N, so they are actual E2 inputs. Causality/strong uniqueness identify their physical solutions with w before the stop. Each E1 path has finite total input energy a.s., so for sufficiently large N it is identical to an E2-truncated path throughout the finite input interval; the local solutions patch to the actual w solution. The equality `z=S w` follows on that path, and no expected global E1 state/control energy is asserted. (iii)→(i) is immediate for deterministic inputs.

## 7. Necessity: semimartingale induction for EVERY finite P/Q word

Assume (i) for **every** deterministic L2 v. First fix any smooth v compactly supported in (0,S). Its extension is smooth; H∈L2([0,h])⊂L1, so Rv and Bcal v are continuous (ordinary convolution continuity), even though H itself need not be continuous. The physical E2 solution is integrable and has mean x_v^d. Therefore eta=x−x_v^d obeys

`d eta=P eta dt+(Q eta+Bcal v)dW`, `E eta=0`.

Because the original output is deterministic and D1Rv is deterministic, Oeta=0 in time-L2 a.s. The state is continuous, so this is zero for all t on a probability-one event.

Apply uniqueness of the continuous finite-variation/local-martingale decomposition to Oeta=0: `OP eta=0` and `O(Q eta+Bcal v)=0` dt×P-a.e. Since OPeta is continuous, it is zero for every t a.s. Apply the same argument to OPeta, OP²eta, etc. through j=n−1; the finite intersection of these events gives eta(t)∈N throughout [0,T]. No stochastic-integral coefficient is discarded merely because it has zero expectation.

Now fix ANY finite word W in P,Q and induct on its length. If `W eta∈N`, project its SDE onto N-perp. Its zero semimartingale decomposition gives

`Pi W P eta=0`, `Pi(WQ eta+W Bcal v)=0` dt×P-a.e.

Taking expectations in the second identity uses `E eta=0` and deterministic Bcal v to give `Pi W Bcal v=0` a.e. Subtracting gives `Pi WQ eta=0`; the P/Q eta processes are continuous, and Bcal v is continuous for the chosen smooth v, so these conclusions hold at all times as needed. Both WP and WQ extend the word, so the induction covers every finite word. The proof does not assume Q preserves N.

For each fixed word, smooth compact v are dense in L2(J), and Bcal is bounded. Thus `W integral phi Bcal v∈N` for every v,phi by L2 convergence and closedness of N. The span of all finite P/Q words applied to D0 is exactly the minimal P/Q-invariant subspace D. Hence D⊂N, proving (i)→(ii).

Each input/word is treated with its own probability-one event; the deterministic conclusion does not require an uncountable intersection of null sets. This argument also covers zero forcing, zero output, singular/repeated matrices and n=1.

## 8. Exact endpoint and strictness consequence

Under (iii), the pathwise bound gives `E||Sw||<=||S|| E||w||` for both actual domains. Deterministic nonzero L2 inputs are progressive E2 and approximate the operator norm, so both literal gains equal ||S||. This is an expectation-of-path-norm statement, not RMS substitution.

At gamma=||S||>0, a nonzero norm-attainer is an actual deterministic E2 endpoint input and violates pointwise strictness. If S has no nonzero attainer, the gap `gamma||w||−||Sw||` is strictly positive on each nonzero path and integrable; any E1 input with positive expected norm has such paths with positive probability, so its expected gap is strictly positive. Thus pointwise E2↔E1 strictness and the norm-attainment criterion hold. Uniform strictness still fails at the common gain. At S=0, every prescribed gamma>0 is uniformly feasible; at gamma>||S|| there is a common margin, and at gamma<||S|| deterministic near-maximizers violate it. No infinite-horizon or arbitrary-controller extension follows.

## 9. Original delayed example and why it exceeds the earlier sufficient test

For the candidate's physical family, P=0, O=e1^T, B=e1, B0=e2, L0=1, Lh=lambda, C=−lambda e1 and H(r)=eta on [0,h]. Let `Qe1=beta e2`, `Qe2=sigma e2`, `Qe3=kappa e1`, with h>0, T>h and kappa≠0. These formulas retain the same one input in both delayed drift terms.

Then `B Lh+C=0` and direct convolution gives

`Kx(r)=e1[1+eta min(h,r)]`,
`KB(r)=e2[beta(1+eta min(h,r))+eta 1_(r<h)]`.

The current noise atom is e2, so D0=span(e2); P=0 and Qe2=sigma e2 give D=span(e2). Meanwhile N=ker(O)=span(e2,e3) and `OQ=(0,0,kappa)≠0`. Thus the exact new criterion succeeds even though the older stronger OQ=0 condition fails. The original x2 diffusion can be nonzero and the original regulated output retains both x1 and u. The candidate's specified rational values are a member of this symbolic family; no source claim for a different law is inferred.

## 10. Independent exact rational diagnostics and fault controls

I did **not** execute or rely on the author's stated checker. I wrote `frontier-review-f54-delayed-kernel-independent-check.py`, SHA256 `62bb0037ff73b5ba0a6157fff11afc70265a2b55053c6030366020053d6babcc`, and ran:

`python3 frontier-review-f54-delayed-kernel-independent-check.py`

Actual result `frontier-review-f54-delayed-kernel-independent-check-results.json`, SHA256 `4d571540f0497c41ccddf0c6d15a912975d1c503b251005bb379be82a2648b1a`: **PASS**. The checker uses Python Fraction arithmetic, a three-state nilpotent P with P³ checked on all basis vectors, a nontrivial Q, affine kernel H and linear deterministic input. Nine interior rational interpolation nodes integrate the piecewise polynomials exactly (degree<=8 for the Gamma integrand), with interval boundaries split explicitly.

For h=2/5,T=7/5,S=1, the direct original ODE/noise-forcing calculation and the independently assembled atom/kernel formula agree exactly at all six documented rational times; Gamma rank, kernel/atom span rank and joint rank are all **2**. For h=0,T=S=7/5, the same exact comparisons have no mismatch and the three ranks are again **2**. The result JSON records the full chosen matrices, input, time points and exact rational Gamma matrices. These are selected finite diagnostics and **not a proof** of the all-matrix iff; that proof is §§4–7.

Separate deliberate wrong-code controls `frontier-review-f54-delayed-kernel-negative-controls.py`, SHA256 `ed7111e264c2c95a0d72b08a2730d1d320683022394fd7aac8f5b3acdef51beb`, result SHA256 `79601736d87a880b8ab0bc5645df822c501b93ebbefe85d13fe9f7ebd6aba462`, returned PASS: the exact checker detected a flipped delayed-C sign, an omitted delayed noise atom and an omitted coincident h=0 atom. These are in-memory fault controls, not counterexamples to the candidate.

## 11. Final scientific disposition

The candidate's complete three-way iff, explicit noise-range matrix, h boundaries, stochastic induction, actual E1/E2 caller and finite endpoint criterion are supported at their **given-law/scalar-Brownian/zero-extended/local-control** scope. **0 FATAL /0 MAJOR /0 MINOR.** The exact rational diagnostics support implementation sensitivity but do not replace the universal proof.

No all-law visible-noise endpoint-transfer result, general nonlinear/full-information synthesis criterion, controller existence for a prescribed plant, infinite-horizon or nonzero-initial-state result, book-domain equivalence, novelty or priority is established. No parent adoption, independent model-family/human review, formal/Lean-kernel or exhaustive executable proof is claimed. The newer owner direction permits these bounded local checks prospectively; previous quarantined outputs are neither accepted premises nor retrospectively validated.

**END COMPLETE f54 REVIEW — EXACT SCOPE ONLY; ORIGINAL GENERAL ENDPOINT REMAINS OPEN.**
