# v31-E — all-complex pair norm, signed map and relaxed controls: written review

Reviewer: `InfoGuessingRminus-2` / owner `InfoGuessingRminus`. Author: `PhysicsDepol4`. Actual metadata-only `/bin/date` before this review: `Sun Oct 25 04:38:05 PDT 2026`.

## 1. Verdict at the exact frozen scope

**WRITTEN RECONSTRUCTION SUPPORTED: 0 FATAL / 0 MAJOR / 0 substantive MINOR findings at the assigned scope.**

I reconstructed the unrestricted COMPLEX-coefficient two-qubit parity-block bound, its all-state four-qubit Z<=4I consequence, the mixed-versus-pure caveat, the signed-map sufficient Ky-Fan reduction, and the literal relaxed rational controls with their same-point channel gaps. The proofs below are written derivations, not accepted output from the author's historical enumeration.

**The original low-noise k=2,3,4 target remains OPEN.** None of the signed-map obligations SB_2/SB_3/SB_4 or the required multi-eigenvalue Z bounds is proved here. Relaxed PPT points are NOT physical state/projector counterexamples. The supported conclusion is an auxiliary norm lemma and an obstruction to the SPECIFIED relaxation with rank-matched U2 and one scalar Z cut, not an unrestricted depolarizing majorization theorem or a claim that every use of the new operator bound fails.

## 2. Pins, coverage, exposure and no-execution statement

Assignment: v31-E in `peer-review-wave-eighteen-v31.json`, observed SHA256 `73cf8654ddca55870d137b3e447355274c54a733451fa9aa3d1d6a1dc3dcf5d8`. Its exact entry and work rules were read first, together with a complete reread of `parent-evidence-erratum-v7.md` LF1–39. No named scientific GO exists.

Mandatory literal part: `peer-review-wave-v31-depol-complex-pair-norm-sources-part1-v1.md`, observed SHA256 `07c163c06acb2223d6f55cf1649cb89b31253eab4aabdad37fab829bab949385`. ALL325 packet lines were read explicitly in raw ranges1–130,131–250,251–325; no truncated or elided source line remains unread.

Original-source abbreviations below use ORIGINAL LF numbers printed in that packet:

- **N:** `physics/evidence/three-area-20261023-96h/parallel-18/depolarizing-majorization4/low-noise-pair-norm-and-signed-map-v1.md`, complete LF1–265, observed SHA256 `5a067a6fb6c746ab0a47c20df2bc6b025986125dd18b2cda0ab045a82c896a83`.
- **D:** `physics/evidence/three-area-20261023-96h/parallel-18/depolarizing-majorization4/resume-computation-disclosure-v1.json`, complete LF1–46, observed SHA256 `02c1e4117042560aeaccfea1e980907f94599b77646013f06ace91ef1231e7a7`.

For the named inherited DEFINITIONS, I additionally read:

- **P:** `physics/evidence/six-lane-20261016/depolarizing-majorization-n4/frozen-partial-v1/PROOF.md`, observed SHA256 `6789e392dbc70dbed479ba8f307e0eb6c786d735de691d425583ec0d8b2fce8a`; in particular LF7–94 for X_j, channel coefficients, spin flip, E_S and the twirled relaxation. This is NOT a fresh replay of its old LP dual certificates.
- **F:** `physics/evidence/six-lane-20261016/depolarizing-majorization-n4/zlemma-route/FROZEN_STATEMENTS.md`, observed SHA256 `b3db2407c950fc56bdbbe041dce7aa329ed403685886deef6951cec38166b71b`; in particular LF6–22 for the original sufficient Z family and bridge. Its old numerical observations are not verification imports.

ACK: `peer-review-depol-complex-pair-norm-ack-v1.json`, observed SHA256 `735f65da2fdc6200eba1fbb818ec22e8b77ccd77432479f399602e5ae5bee968`.

This is supplied-proof, same-harness, cross-domain review, not blind, cross-vendor, configured dual-family, human, proof-assistant/kernel or novelty acceptance. Earlier run summaries were known, but no older verdict transfers to N. No scientific eval/interpreter, arithmetic program, enumeration, symbolic computation, certificate replay, nested agent or CLI was used in this review. Only written reasoning, source reads and metadata clocks/hashes were performed.

D's enumeration outputs are historical unadmitted observations under the withdrawn parent exception. The parent-origin authorization error is not attributed to the author. No claim of exhaustive optimum, vertex count, computation compliance, or retroactive admission is inferred from those outputs.

## 3. Lemma P2 — complex rotations and literal parity blocks reconstructed

References: N:L25–61.

Let u in C³. The real span of Re u and Im u has dimension at most2, so there is a real unit vector n perpendicular to both. Choose an ORIENTATION-PRESERVING real rotation sending n to the z-axis. The adjoint action of a single-qubit unitary implements this SO(3) rotation on the Pauli vector, and extends complex-linearly to complex coefficients. Thus the transformed coefficient has zero complex z-component, giving

`u dot sigma ~ [[0,alpha],[beta,0]]`.

For transformed components a,b, alpha=a-i b and beta=a+i b. Direct expansion with complex absolute squares gives

`|alpha|²+|beta|²=2(|a|²+|b|²)=2||u||²`.

This uses unitary SIMILARITY, not a nonunitary congruence or a replacement of the operator by a Hermitian one. Apply an independent unitary rotation to the other physical site for v, producing gamma,delta. The tensor product of the two unitaries preserves the norm of the actual two-qubit operator.

In the even basis00,11 and odd basis01,10, the two off-diagonal blocks really are

`C=[[gamma,alpha],[beta,delta]]`,

`D=[[delta,alpha],[beta,gamma]]`.

For example, A applied to01 has even coordinates(gamma,beta); A applied to10 has(alpha,delta). A applied to00 has odd coordinates(delta,beta), and A applied to11 has(alpha,gamma). This directly checks both blocks and their order.

Hence A=[[0,C],[D,0]], and

`A* A=diag(D*D,C*C)`.

Both blocks have the SAME squared Frobenius norm

`F=|alpha|²+|beta|²+|gamma|²+|delta|²`

`=2(||u||²+||v||²)`.

Since each block's operator norm squared is at most its Frobenius norm squared,

`||A||²=max(||C||²,||D||²)<=F`.

This proves P2 for arbitrary complex u,v, including zero/dependent real and imaginary parts and nonnormal non-Hermitian operators. No common real rotation for several independent coefficient vectors was assumed.

N:L105's obstruction to that PARTICULAR multi-vector extension is correct: Re(1,i,0), Im(1,i,0), and Re(0,0,1) span R³, so no single real axis is perpendicular to all. This does not exclude other multi-vector arguments.

## 4. P4, Z1, sharpness and the mixed-state caveat — reconstructed

References: N:L65–105; F:L8–20; P:L14–15.

For a four-qubit coefficient vector w, write S12 and S34 as in N. The two-qubit pair operators act on disjoint tensor factors. Triangle inequality and P2 give

`||L_w||<=sqrt(2S12)+sqrt(2S34)`.

Squaring and using `2sqrt(S12*S34)<=S12+S34` yields

`||L_w||²<=4(S12+S34)`.

For a unit vector psi, the12-column matrix V with columns sigma_a^(i)psi satisfies

`Vw=L_w psi`, `Z(psi)=V V*`.

Therefore its largest squared singular value is at most4. This gives0<=Z(psi)<=4I. A mixed density matrix is a convex combination of pure ones, and Z is a positive linear map, so the same operator bound holds for EVERY mixed input. Rotations in the P2 proof may depend on w: the bound on ||L_w|| is uniform, and ||L_w psi||<=||L_w|| is applied before maximizing over w. No common rotation of the whole Gram family is required for this k1 proof.

At psi=0000, four z-Paulis each contribute the same0000 projector; x and y at site i each contribute the corresponding one-flip projector. Thus

`Z=4|0000><0000|+2 sum_i |e_i><e_i|`,

which proves the stated sharp spectrum4,2,2,2,2,0,... without computation.

Using the single-site Pauli identity on the actual partial-trace maps gives

`Z=2X3-4rho`, hence `X3=2rho+Z/2<=2rho+2I`.

For PURE rho the comparison operator2I+2rho has eigenvalues4,2,...,2. Eigenvalue monotonicity therefore yields lambda1(X3)<=4 and lambdaj(X3)<=2 for j>=2.

The mixed caveat in N:L101 is necessary and correct. For the equal mixture of the two adjacent basis states0000 and1000, X3 is the equal mixture of their diagonal product-state X3 matrices. At either of those two basis strings the two contributing values are4 and1, so both resulting diagonal eigenvalues equal5/2. Thus the pure second-eigenvalue bound2 cannot be asserted for all mixed inputs. The all-state OPERATOR inequality X3<=2rho+2I remains valid.

These estimates do not yield the sums5,6,7 at k2,3,4. Bounding every later pure eigenvalue by2 only gives the weaker envelope4+2(k-1), not the required k+3. No higher Ky-Fan conclusion is inherited from k1.

## 5. Signed B map, positivity, trace and sufficient targets — reconstructed

References: N:L109–133,259; P:L14–15,19–39,43–57.

Use the inherited definitions `X_j=sum_(|S|=j) rho_S tensor I_(S^c)`, with X0=I and X4=rho. The single-qubit identity `sigma_y X^T sigma_y=Tr(X)I-X`, tensored over four qubits, gives the global positive spin flip

`tilde(rho)=I-X1+X2-X3+rho`.

Thus for `B=I-X1+X2`,

`B=X3-rho+tilde(rho)`.

Z>=0 implies X3>=2rho, so B>=rho+tilde(rho)>=0. The trace is exactly

`Tr B=16-4*8+6*4=8`.

For each k=2,3,4, if the stated SB_k bound `K_k(B)<=k+2` were established, then

`X3=B+rho-tilde(rho)<=B+rho`,

and Ky-Fan monotonicity/subadditivity give

`K_k(X3)<=K_k(B)+K_k(rho)<=k+2+1=k+3`.

This is a valid SUFFICIENT route to U3_k. Combined with the separately inherited U2_k certificate and the common Hamming ordering of the product reference matrices, it gives that channel index for p in[0,1]; the inherited p-to2-p spin-flip spectral reflection extends to the remaining physical p up to4/3. I have reconstructed this implication, not replayed the old U2 certificate.

For rho=0000, at a string with z zero bits B's diagonal entry is `1-z+binom(z,2)`. As z runs4,3,2,1,0 these are3,1,0,0,1, with Hamming multiplicities1,4,6,4,1. Hence B has spectrum3,1 repeated5,0 repeated10, giving the sharp product values4,5,6 for SB_2,SB_3,SB_4.

The packet correctly does NOT prove those all-state SB bounds. They are not necessary conditions for the original channel theorem: subtracting tilde(rho) can improve X3, and the whole noise combination can improve further. A failure of SB alone is not a physical channel counterexample.

## 6. Actual twirled relaxation and objective normalization — reconstructed

References: N:L137–163; P:L61–94.

The supplemental frozen definitions remove any ambiguity about E_S. Each local pair has the rank-one normalized Bell projector Phi+ and its rank-three complement. Their tensor-product sector E_S has trace3^(4-|S|). After permutation twirling,

`omega=sum_S (x_|S|/16) E_S`,

and collecting multiplicities gives `d_s=binom(4,s)3^(4-s)=(81,108,54,12,1)`.

Thus omega>=0 and omega<=I/16 mean0<=x_s<=1. The trace condition is d dot x=16k. Its input-side marginal is kI/16, so the inherited `sigma_omega=Tr_output(omega)/k` is I/16; the other partial-trace cap is automatic for these ranks. These are genuinely the inherited RELAXED constraints, not arbitrary new scalar variables.

Under partial transpose, Phi+ becomes swap/2; its complement becomes I-swap/2. On a local symmetric sector the two eigenvalues are both1/2, and on an antisymmetric sector they are-1/2 and3/2. With t antisymmetric sites the grouped generating polynomial is

`(1+z)^(4-t)(3-z)^t`.

Therefore16H is exactly the five coefficient rows printed in N:L147–155. Expanding these elementary polynomials yields

`(1,4,6,4,1)`, `(3,8,6,0,-1)`, `(9,12,-2,-4,1)`,

`(27,0,-18,8,-1)`, `(81,-108,54,-12,1)`.

The actual partial-transpose eigenvalues are y_t/16 with y=Hx; hence both PPT inequalities are precisely0<=y_t<=1.

For the partial-trace subset map Phi_j, a Choi id factor is2Phi+ and a traced factor isI. On a sector with s Bell factors, selecting j id factors contributes `2^j binom(s,j)`. Thus

`t_j=(1/16) sum_s d_s x_s 2^j binom(s,j)`.

The spin-flip Choi factor is I-2Phi+, giving sign(-1)^s, and the B objective is t0-t1+t2=k-t1+t2. All factors of16 and2^j in the packet are consistent.

Every physical `bar(rho) tensor Pi` with rho a state and0<=Pi<=I, Tr Pi=k lies in the original relaxed cone, and twirling preserves its objective. The converse is NOT asserted. Permutation/local-unitary averaging generally destroys the literal product factorization; arbitrary feasible x does not construct any actual rho or Pi.

## 7. Three initial rational points — complete written feasibility and objectives

References: N:L165–197. Put T=16H. Clear the denominators of the three x vectors:

`n2=(5,0,1,16,21)`, denominator21;

`n3=(25,3,9,81,81)`, denominator81;

`n4=(7,3,9,27,27)`, denominator27.

The five components of T n2 are, directly,

`5+6+64+21=96`, `15+6-21=0`,

`45-2-64+21=0`, `135-18+128-21=224`,

`405+54-192+21=288`.

For T n3 they are

`25+12+54+324+81=496`, `75+24+54-81=72`,

`225+36-18-324+81=0`, `675-162+648-81=1080`,

`2025-324+486-972+81=1296`.

For T n4 they are

`7+12+54+108+27=208`, `21+24+54-27=72`,

`63+36-18-108+27=0`, `189-162+216-27=216`,

`567-324+486-324+27=432`.

Dividing these by16 times their corresponding denominators gives exactly all three y vectors in N:L169–171. Every displayed coordinate is between0 and1. Multiplying x by d gives

`w2=(135/7,0,18/7,64/7,1)`,

`w3=(25,4,6,12,1)`,

`w4=(21,12,18,12,1)`.

Their sums are32,48,64, proving the three trace constraints. This is direct point feasibility, not an LP optimum or completeness assertion.

For any such weighted vector w, the objective formulas reduce to

`16t1=2w1+4w2+6w3+8w4`,

`16t2=4w2+12w3+24w4`,

`16t3=8w3+32w4`, `t4=w4`,

`16sflip=w0-w1+w2-w3+w4`.

For the k2 vector, for example, these give `16t1=512/7`, `16t2=144`, `16t3=736/7`, `16sflip=96/7`. For k3 they give112,192,128,16; for k4 they give176,240,128,16. Consequently the objective tuples are precisely

| k | t1 | t2 | t3 | t4 | sflip | k-t1+t2 |
|---|---|---|---|---|---|---|
|2|32/7|9|46/7|1|6/7|45/7|
|3|7|12|8|1|1|8|
|4|11|15|8|1|1|8|

All three t2 values saturate3k+3. Their B objective values exceed4,5,6 respectively. The scalar inequalities t3>=2t4 and B objective>=t4+sflip hold, but this is not the full physical operator system.

The packet correctly discards the initial k2 point once the rank-matched Z1 cut is imposed: `2t3-4t4=64/7>8`. Keeping it unchanged would be invalid. No such mistake is made in N.

## 8. Product-star anchor, convex repair and new norm cut — reconstructed

References: N:L201–221.

The product-star input can be realized by rho=0000 and the rank-two projector onto0000 and1000. Its partial-trace objectives are t1=4+3=7, t2=6+3=9, t3=4+1=5, t4=1, with spin-flip objective0.

The claimed x_star also follows directly from its twirl, not merely those five objectives. At the free projector site the input/output operator is |0><0| tensor I, whose isotropic sector coefficients are1/2 on BOTH Bell and complement sectors. At each of the other three sites |00><00| has coefficients1/2 on the Bell sector and1/6 on its complement. Including sector traces, the weighted layer polynomial16 times the trace contributions is

`(3+z)(1+z)^3=3+10z+12z²+6z³+z⁴`.

Permutation twirling preserves these layer sums, so d_s x_star,s=(3,10,12,6,1), giving exactly

`x_star=(1/27,5/54,2/9,1/2,1)`.

Alternatively clearing its denominator54 gives n_star=(2,5,12,27,54). Direct multiplication yields T n_star=(256,64,0,0,0), hence H x_star=(8/27,2/27,0,0,0), as stated. The product-star point is a physical anchor; the other relaxed points are not thereby made physical.

Now take7/11 of the old k2 point and4/11 of this anchor. The actual coordinate mixture is

`x_new=(49/297,10/297,1/9,2/3,1)`;

linearity gives

`H x_new=(86/297,8/297,0,14/33,6/11)`.

Both endpoints have rank parameter2, so convexity preserves every relaxed constraint and the trace. Weighted coordinates are `(147/11,40/11,6,8,1)`, summing to32. Mixing the objectives gives

`t1=32/11+28/11=60/11`, `t2=9`,

`t3=46/11+20/11=6`, `t4=1`, `sflip=6/11`.

Thus `2t3-4t4=8=4k`. The retained k3/k4 points give12, equal to4k at k3 and below4k at k4. Every FINAL relaxed control therefore satisfies BOTH its rank-matched U2 scalar bound and the rank-matched scalar expectation implied by Z1. This is not a claim to satisfy all operator/simultaneous-rank/actual-state compatibility consequences of Z1.

## 9. Same-point noise eligibility and exact positive relaxed gaps — reconstructed

References: N:L223–249; P:L19–31.

For k=2,3,4, the product reference partial sums are

`K_k(T0)=k`, `K_k(T1)=3k+1`, `K_k(T2)=3k+3`,

`K_k(T3)=k+3`, `K_k(T4)=1`.

For ONE actual or relaxed point, write its map objectives as t_j. The depolarizing coefficients are

`a_j=(1-p)^j p^(4-j)2^(j-4)`.

With `u=p/[2(1-p)]` on0<p<1, direct ratios give

`a1/a3=u²`, `a2/a3=u`, `a4/a3=1/u`.

Subtracting the common-order product target from this SAME point's channel objective therefore gives exactly

`a3[delta3-u²d1-u d2-d4/u]`,

where d1,d2,d4,delta3 are N:L225–227's quantities. No separately optimized projectors or different input states have been combined in this algebra: all t_j come from the same literal feasible x at the same rank.

For the three final points the tuples(d1,d2,d4,delta3) are

`(17/11,0,0,1)`, `(3,0,0,2)`, `(2,0,0,1)`.

At p=1/2, u=1/2 and a3=1/32, so the gaps are exactly

`(1/32)(1-17/44)=27/1408>0`,

`(1/32)(2-3/4)=5/128>0`,

`(1/32)(1-2/4)=1/64>0`.

Since d2=d4=0 in each case and a3>0, the general sign conditions are exactly `u²<11/17`, `u²<2/3`, `u²<1/2`. Each threshold is positive and less than1, giving a nonempty interval within0<p<2/3; no numerical root approximation is needed.

This proves a RELAXATION obstruction at the stated exclusion boundary. No density-matrix amplitudes or rank-k projector factorizing the nonphysical omega have been supplied. These positive gaps neither falsify SB/U3/channel statements nor certify that every possible strengthening derived from Z1 is insufficient. N:L249 explicitly preserves those distinctions.

## 10. Findings, unresolved obligations and assurance

### Findings

- **FATAL: 0** at the assigned written scope.
- **MAJOR: 0** at that scope.
- **Substantive MINOR: 0** at that scope.

The critical complex-coefficient step does not assume A Hermitian; the parity blocks and the independent rotations are correct. The mixed-input extension is made only for the linear operator bound, not the pure second-eigenvalue cap. The initial k2 point's incompatibility with Z1 is explicitly repaired. No physical counterexample is claimed from a PPT relaxation point.

### NOT_RECONSTRUCTED / OPEN boundaries

1. **Original low-noise k2/3/4 inequalities:** N:L95–105,121–133,251–265. OPEN. The new k1 norm bound does not control the required top2/3/4 singular-value sums. None of SB_2,SB_3,SB_4, U3_2/U3_3/U3_4 or a direct target channel inequality has been proved.
2. **Actual-state/projector realization of the relaxed points:** N:L157,195,249. NOT SUPPLIED and not reconstructed. Feasibility in the relaxed omega cone is not factorization as bar(rho) tensor Pi. No physical counterexample or global operator compatibility certificate exists here.
3. **Historical enumeration optima/completeness:** D:L8–40, N:L11. NOT_RECONSTRUCTED and no verification credit. The claimed enumerated vertex counts and B/U3 maxima, including the separate k1 run, were not replayed or accepted. Only the literal feasible witnesses were reconstructed above, which is sufficient for the stated method obstruction and does not establish an exhaustive optimum.
4. **Old U2 duals, high-noise package and central-index theorem:** N:L13–18. Named imports only, not freshly replayed or independently recertified here. Their actual historical assurance/errata boundaries remain binding. The sufficient composition is reconstructed conditionally on those imports.
5. **Zhang prior attribution / novelty:** N:L19–21,265. Keep the matched complementary clipped-tail prior claim and the stated ambiguity about exact uniform-weight support. No fresh public-source priority/novelty resolution or full-public-solution certification was performed by this review.
6. **Broader old Hessian and multi-vector gaps:** N:L105,261–263. NOT CLOSED. The lack of a common axis identifies a barrier to one proposed extension, not impossibility of all multi-vector methods, and no old beta-gap Hessian is transferred to the target constant.

No new scientific computation, replay, GO, native launch, external model or source edit occurred. Both declared sources were fully read, all required elementary/rational identities above were reconstructed in writing, and all unresolved target/import/computation obligations are stated rather than labelled PASS.

## 11. Parent integration sentence

**Support the written all-complex P2/P4 and all-state Z1 auxiliary result, the mixed/pure caveat, the conditional signed-map route and the exact specified-relaxation controls. Preserve OPEN low-noise k2/3/4, physical factorization/global-compatibility gaps, named inherited certificate boundaries and Zhang attribution. No unadmitted arithmetic, full-target, formal/kernel, cross-vendor or novelty acceptance follows.**
