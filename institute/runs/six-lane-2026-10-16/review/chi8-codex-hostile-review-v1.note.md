VERDICT: ACCEPT

The replacement global bound is valid. At \((k,d)=(4,8)\), it supplies the missing \(S_2\) estimate without invalidating KPW’s local Gaussian calculation, small-subgraph conditioning, or marked-edge argument for the other residues.

All seven supplied files match the manifest, including the frozen proof’s stated SHA256. I read the complete proof, KPW Sections 2–4, and the required Wormald and D–SC passages. No other claimant lane or prior parent review was used. Checks ran in memory; the verifier’s main routine, numerical optimizer, and output writer were not invoked.

- **Fatal findings:** none.
- **Major findings:** none.
- **Minor source issue:** KPW LF1251 claims \(2(k-1)^2>k^2\) under \(k\ge3\), although this fails at \(k=3\). At the present \(k=4\), it is \(18>16\), so their Lemma 9 argument works. This does not require a correction to the degree-8 proof.

1. **The exact count, polynomial prefactor, and weak duality are correctly normalized.**

   In [the frozen proof, LF153–214](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/chi8-parent-inputs-v1/PROOF_CHI8.r1.md:153), put \(n_u=nm_u/4\). There are
   \[
   \frac{n!}{\prod_u n_u!}
   \]
   assignments of the labelled colour pairs to vertices. For prescribed \(b_e\), allocating each cell’s labelled points contributes
   \[
   \prod_u\frac{(dn_u)!}{\prod_{v\sim u}b_{uv}!}.
   \]
   Each unordered allowed pair then contributes \(b_e!\) bijections. The allocation denominator contains each \(b_e!\) twice, leaving exactly one:
   \[
   |T(M)|=
   \frac{n!}{\prod_u n_u!}\prod_u(dn_u)!
   \sum_{b\in B(M,n)}\prod_e\frac1{b_e!}.
   \]
   There are **72 unordered allowed pairs**, not 144. The pairing denominator is
   \[
   |P_{n,d}|=\frac{(dn)!}{2^{dn/2}(dn/2)!}.
   \]
   No additional colour-permutation or edge-orientation factor belongs in either expression.

   Applying the stated factorial and multinomial bounds gives the non-exponential factor
   \[
   e^{16}(dn+1)^8
   (dn/2+1)^{72}
   e(dn/2+1)^{1/2}
   =
   e^{17}(dn+1)^8(dn/2+1)^{145/2}.
   \]
   Thus the advertised \(P_d(n)\) is valid uniformly in \(M\).

   Writing \(b_e=n\beta_e\), the coefficients of \(n\log n\) cancel as
   \(d-d/2-d/2=0\); the remaining linear factorial terms cancel as
   \(-d+d/2+d/2=0\). The residual exponent before dualization is
   \[
   \frac{d-1}{4}\sum_um_u\log m_u
   +(1-d)\log4+\frac d2\log d
   -\sum_e\beta_e\log\beta_e.
   \]
   Since \(\sum_{e\ni u}\beta_e=dm_u/4\),
   \[
   -\sum_e\beta_e\log\beta_e
   \le
   \sum_{e=\{u,v\}}e^{\mu_u+\mu_v-1}
   -\frac d4\sum_u\mu_um_u.
   \]
   The sign is correct: the unconstrained edgewise supremum gives an **upper** bound.

   Empty support cells force their incident \(b_e\) to vanish. An empty feasible set contributes zero. Multipliers are needed only on positive cells. They may depend on \(M\) and \(n\), and may become unbounded along sequences: this exact pointwise inequality requires no compactness or uniform boundedness assumption on them.

   The requested \(C\)-normalization agrees with the frozen proof’s \(c\)-normalization. Define
   \[
   \lambda_u=\mu_u+\frac{\log4-1}{2}.
   \]
   At \(d=8\), substituting
   \(\lambda_u=\log C+\tfrac78\log m_u\) gives
   \[
   V=6\log2-4+\frac{C^2E(M)}4-8\log C.
   \]
   Its minimum occurs at
   \[
   C^2=\frac{16}{E(M)},\qquad
   V=-10\log2+4\log E(M).
   \]
   Equivalently, the frozen proof has \(e^{2c-1}=4/E(M)\). There is no scaling discrepancy.

   Finally,
   \[
   E(M)\ge\frac{8+\|M\|_F^2}{2}\ge\frac92,
   \quad
   E(J)=72\,4^{-7/4}=\frac9{\sqrt2},
   \]
   and
   \[
   U(J)=8\log3-12\log2
       =2\log4+8\log(3/4).
   \]

2. **Theorem C follows analytically from the correctly normalized D–SC import.**

   Inclusion–exclusion gives
   \[
   2E=(\sum f)^2-\sum_pR_p^2-\sum_qC_q^2+\sum f_{pq}^2.
   \]
   The difference between the proposed row bound and this expression is exactly
   \[
   2\sum_pR_p^2+\sum f^2-2E
   =
   \left[\sum_qC_q^2-\frac{(\sum f)^2}{4}\right]
   +\frac34\left[4\sum_pR_p^2-(\sum f)^2\right]\ge0.
   \]
   Thus \(E(M)\le\sum_pF(r_p)\).

   In [D–SC’s definitions and Theorem 3.5(ii)](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/chi8-parent-inputs-v1/diaconis-saloffcoste-1996-lsi.layout.txt:1365), the resampling kernel \(K(x,y)=1/4\) has generator \(I-K\), uniform probability measure, and Dirichlet form \(\operatorname{Var}_\pi\). Appendix Theorem A.1 therefore gives
   \[
   \alpha=\frac1{2\log3}.
   \]
   This is the resampling chain, including its diagonal entries; changing to the walk without holding would change the normalization.

   The reversible hypercontractive condition is \(e^{4\alpha t}\ge q-1\). With \(q=8\), self-adjointness and \(L^8\)–\(L^{8/7}\) duality yield
   \[
   \|T_a g\|_2\le\|g\|_{8/7},
   \qquad a=7^{-\log3/2}.
   \]
   For \(g=r^{7/8}\), with norms under the uniform probability measure,
   \[
   F(r)=18\|T_{1/3}g\|_2^2,
   \qquad
   \|g\|_{8/7}^2=4^{-7/4}.
   \]
   Strict admissibility is analytic:
   \[
   a>\frac13
   \iff \log7<2,
   \qquad
   e^2>\sum_{j=0}^{5}\frac{2^j}{j!}=\frac{109}{15}>7.
   \]

   Moreover,
   \[
   \operatorname{Var}_\pi(g)
   =\frac1{32}\sum_{i,j}(g_i-g_j)^2
   \ge\frac{49}{256}|r-U|^2.
   \]
   The mean-value argument remains valid when one endpoint is zero: continuity holds on the closed interval and differentiability is required only inside it.

   Consequently,
   \[
   F(r)\le F(U)
       -\frac{441}{128}(a^2-1/9)|r-U|^2.
   \]
   Summing rows and using \(E(M)>0\) on doubly stochastic matrices proves
   \[
   U(M)\le U(J)-C_8\|M-J\|^2,
   \quad
   C_8=\frac{49\sqrt2}{32}(a^2-1/9)>0.
   \]
   Independent interval arithmetic reproduced
   \(\kappa=0.02343764400316\ldots\) and
   \(C_8=0.01473148178637\ldots\). Their positivity does not depend on those decimal approximations.

3. **The central dependency audit passes, including the local uniformity and epsilon requirements.**

   I traced the arguments in [KPW](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/chi8-parent-inputs-v1/kpw0812.2937v1.layout.txt:569), rather than using the candidate’s grep audit as evidence.

   | KPW location, LF | Actual dependency |
   |---|---|
   | 23–27, 80–81, 105–107, 142 | Published statements involving the threshold; these statements cannot themselves be applied at \((4,8)\). |
   | 168–178 | SSC uses Proposition 2 and the moment identities. Minimality of \(k\) supplies their lower bound; that lower-bound argument is replaced here. |
   | 183–568 | First and cycle moments, Lemmas 3–4: fixed \(d>0\), \(k\ge3\), and parity. No threshold dependence. |
   | 570 | Standing hypothesis for Section 3. Its substantive consequences must be audited separately. |
   | 713–779, 1035–1138 | Lemma 5 and the derivation of (3.7)–(3.9): the discarded global relaxation. |
   | 787–909, 1139–1525 | Lemmas 6–9: linear algebra, phase separation, and local coefficient asymptotics. They do not invoke Lemma 5 or its relaxed bound. |
   | 911–998 | Local calculation (3.10)–(3.14). The degree restriction needed here is \(k^2-2k-d+2>0\), explicitly used at 982–983. |
   | 999–1033 | AN’s inequality (3.15), combined with (3.9), establishes only the discarded \(S_2\) estimate. |
   | 1536–1623 | Theorem 10 needs the first and second moments, their cycle analogues, negligible distant overlaps, and local edge-count concentration. These survive the replacement. |

   In particular, LF912 merely compares the new local asymptotic with (3.9); it does not derive that asymptotic from (3.9). Likewise, Theorem 10 LF1610–1621 reuses the negligible-tail conclusion and local concentration, not the relaxed exponent.

   I independently checked the local coefficient normalization using independent Poisson edge counts \(Z_e\) of mean \(n/18\). Their endpoint-count covariance is
   \[
   \frac n{18}B,\qquad
   B=9I+(J_4-I_4)^{\otimes2},
   \]
   whose eigenvalues are
   \[
   10\ (9\text{ times}),\quad6\ (6\text{ times}),\quad18\ (1\text{ time}).
   \]
   The incidence lattice has index two: the allowed-pair graph is connected and non-bipartite, and endpoint totals must be even. This accounts for the two saddle contributions.

   For \(A=M-J=O(\log n/\sqrt n)\), exponential tilting by \(O(A)\) centers the endpoint counts. The local Fourier calculation then has a positive Gaussian main term; expanding the tilt gives a uniform exponent error \(O(n\|A\|^3)=o(1)\). The coefficient’s quadratic exponent is
   \[
   -\frac{18}{5}n\|A\|^2.
   \]
   The factorial ratio contributes \(+\tfrac72n\|A\|^2\), leaving
   \[
   -\frac n{10}\|A\|^2.
   \]
   Thus the local Gaussian survives at \(d=8\).

   In the nine free coordinates,
   \[
   H=\frac15(J_3+I_3)^{\otimes2},
   \]
   with eigenvalues \(1/5\) four times, \(4/5\) four times, and \(16/5\) once. Hence
   \[
   (H1)=2,\qquad \det H=4^6\,5^{-9}.
   \]
   These reproduce precisely the claimed second-moment constant.

   Both small-epsilon comparisons in Lemma 8 can be satisfied. For example, take \(\varepsilon=10^{-3}\). Since
   \[
   \frac{18}{5}n\|A\|^2
   \le\frac{288}{5}\varepsilon^2\log^2n,
   \]
   one may absorb the Gaussian polynomial factor using
   \(\varepsilon'=(576/5)\varepsilon^2\). Then
   \[
   \varepsilon'=\frac9{78125}
   <\frac1{288}
   =\frac{d}{16k^2(k-1)^2},
   \]
   and it is also smaller than an available Gaussian-tail exponent \(1/12\).

   Finally, the enlarged polynomial is harmless. With
   \(\delta=\varepsilon\log n/(9\sqrt n)\),
   \[
   \frac{S_2}{S_1}
   =
   O\!\left(
   n^{199/2}
   \exp\!\left[-\frac{C_8\varepsilon^2}{81}\log^2n\right]
   \right)\longrightarrow0.
   \]
   No coupling between the positive constant \(C_8\) and a fixed positive \(\varepsilon\) is necessary.

4. **The SSC constants, marked-edge concentration, and all residue transfers check out.**

   The independently recomputed moments are
   \[
   EY\sim16\left(\frac3{4\pi}\right)^{3/2}
       n^{-3/2}(81/64)^n,
   \]
   \[
   EY^2\sim
   \frac{4^4\,3^{12}}{2^{9/2}(4\pi)^3}
       n^{-3}(81/64)^{2n}.
   \]
   Thus
   \[
   \frac{EY^2}{(EY)^2}\longrightarrow(3/\sqrt2)^9.
   \]
   For
   \(\lambda_i=7^i/(2i)\) and
   \(\delta_i=(-1)^i/3^{i-1}\),
   \[
   \lambda_i\delta_i^2=\frac92\frac{(7/9)^i}{i},
   \qquad
   \sum_i\lambda_i\delta_i^2
      =\frac92\log(9/2).
   \]
   This is finite, and its exponential is exactly the moment ratio.

   [Wormald Theorem 4.1, including its conclusion](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/chi8-parent-inputs-v1/wormald1999-models.layout.txt:1561), therefore applies. Only \(\delta_1=-1\). Since a loop makes \(Y=0\) exactly,
   \[
   P(Y>0\mid X_1=0)\to1.
   \]
   The cycle theorem gives
   \[
   P(X_2=0\mid X_1=0)\to e^{-49/4}>0,
   \quad
   P(\mathrm{Simple})\to e^{-63/4}>0.
   \]
   Conditioning on simplicity produces the uniform simple-graph model because every simple graph has \((8!)^n\) pairing preimages.

   Theorem 10 requires no additional degree-dependent inequality. Its marked moments have factors
   \[
   E\widehat Y\sim6^{-\ell}EY,\qquad
   E\widehat Y^2\sim6^{-2\ell}EY^2,
   \]
   and unchanged cycle adjustments.

   Its briefly stated edge-count concentration can also be justified independently. Conditional on the endpoint constraints, the \(Z_e\sim\mathrm{Poisson}(n/18)\) law is proportional to \(\prod_e1/b_e!\). The conditioning probability is bounded below by
   \[
   c\,n^{-8}
   \exp[-(288/5)\varepsilon^2\log^2n].
   \]
   An unconditional Chernoff bound for some
   \(|Z_e-n/18|>K\sqrt n\log n\) decays as
   \(e^{-c_K\log^2n}\), with \(c_K\) made sufficiently large by choosing fixed \(K\). Division preserves superpolynomial decay. The single-colouring argument, including finitely prescribed cycles, works the same way. Multiplying exceptional terms by \(O(n^\ell)\) remains negligible.

   The marked pairing model also retains the cycle limits; choosing finitely many disjoint marked edges changes its marginal weighting asymptotically negligibly. After conditioning on simplicity, the induced-matching requirement fails with probability \(O(1/n)\), by bounded degree. These elementary sampling steps introduce no missing threshold assumption.

   For residues \(r=1,2,3\), the frozen reduction is exact. On the stated high-probability event, the \(8r\) neighbours form an independent set. Adding and ordering a matching creates \(\ell=4r\) distinguished edges whose endpoints induce precisely that matching.

   Each original graph has \((8r-1)!!(4r)!\) matching/order choices. Each output structure has exactly
   \[
   \frac{(8r)!}{(8!)^r}
   =1,\ 12870,\ 9465511770
   \]
   preimages. Reinstating the labelled deleted vertices from an ordered partition gives every preimage and preserves distance at least four and triangle exclusion. Thus conditional uniformity is exact on the **marked structures**, which is the distribution Theorem 10 needs.

   Giving all deleted vertices colour 3 then transfers the colouring, since their neighbours have colours 1 or 2. This proves the upper bound for every residue.

5. **The lower bound is valid, including unbalanced colour classes.**

   The quoted criterion appears as stated at KPW LF67–68; Wormald LF1102–1107 states the corresponding bound on the expected number of all colourings. Here
   \[
   3(2/3)^4=16/27<1.
   \]

   Independently, the same factorial count with arbitrary three-colour proportions \(r_i\), followed by scalar weak duality, bounds the exponential rate by
   \[
   H(r)+4\log\!\left(1-\sum_i r_i^2\right)
   \le\log3+4\log(2/3)=\log(16/27)<0.
   \]
   Summing the polynomially many class-size vectors and conditioning on simplicity proves absence of 3-colourings. The lower bound therefore does not secretly assume balanced colour classes.

6. **The second row proof is a valid interval-assisted proof, distinct from floating-point sanity.**

   The boundary perturbation excludes boundary maximizers. At an interior maximizer, the displayed function \(\psi\) decreases and then increases, so there are at most two coordinate values. The two stated families cover every multiplicity.

   I checked their derivative formulas and replayed the interval calculation in memory. I then checked the subdivisions again using independently constructed rational radii and explicit endpoint containment:

   - Both families cover all 8,000 outer pieces.
   - Family 1 needs exactly 113 centred-form fallback pieces.
   - Minimum outer slacks exceed \(1.8305451\times10^{-6}\) and \(5.5411198\times10^{-4}\).
   - All 400 central intervals per family have strictly negative \(h''\); upper bounds are below \(-0.2086955\) and \(-1.0331062\).
   - The supplied inflated floating-point radii contain every required endpoint.
   - Indeterminate/NaN comparisons reject instead of certifying an inequality.

   Together with the exact central value and derivative, these establish the stronger constant \(1/40\). Proof 1 already supplies an entirely analytic route.

   Independent controls also reproduced the bad-\(c\) mutation and the obstruction to the relaxed exponent:
   \[
   \phi_8((J+I)/2)-\phi_8(J)=0.00741931598\ldots>0,
   \]
   whereas
   \[
   U((J+I)/2)-U(J)=-0.02876421895\ldots<0.
   \]
   The weaker relaxed \(\phi_8\) was not reused. Finite count checks and the worker’s flags were treated as supporting calculations, not proofs.

7. **The remaining reliance and scope are explicit.**

   The general Wormald cycle/SSC theorems and D–SC log-Sobolev/hypercontractivity theorems remain published imports; their relevant statements, hypotheses, and normalizations were checked. KPW’s local and marked-edge extensions were independently justified above.

   The original Molloy–Reed thesis was not supplied or inspected; the independently derived first-moment bound removes any unresolved dependence on that citation. Contextual AM/ACG citations and priority claims were not exhaustively audited.

   The accepted conclusion is the stated specialist result:
   \[
   \boxed{\chi(G_{n,8})=4\quad\text{a.a.s., for every residue }n\bmod4.}
   \]
   It establishes no degree-9 result or general large-degree threshold.