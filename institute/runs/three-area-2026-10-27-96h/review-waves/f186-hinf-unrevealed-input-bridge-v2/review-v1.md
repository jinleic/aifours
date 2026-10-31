# f186: independent same-harness review of the unrevealed-input bridge v2

Reviewer: `ReviewF186HinfBridgeV2`. Native clock observed immediately before composing this review: **2026-10-29T09:31:06-0700 PDT** (not a file-creation time).

## Disposition and limits

**0 FATAL / 0 MAJOR / 3 MINOR findings; 0 INCONCLUSIVE theorem verdicts.** T1--T8 have same-harness written mathematical support, conditional on the sole adopted research premise and the classical imports stated below. The frozen packet has a literally false admissibility-converse sentence in T1, a classical-import naming shortfall, and an incorrect homogeneity-degree description in T6. I supply the short T1 repair explicitly; I do not accept the false sentence. No source file was modified. A parent may adopt the reconstructed statements with these additive corrections; this review does not itself adopt research results.

This is **not** human review, independent-model-family review, a formal/kernel check, or novelty/priority verification. None of the numerical controls establishes any of the theorems or supplies a missing research premise. No value of kappa, m1, eta_star, or eta_dagger is certified here.

Notation: `P` means the adopted disposition; `V:L` means physical LF line L of the v2 packet. Norms in the normalized problem are L2[0,1] norms. I write kappa for the revealed variational value and kappa(eta) for the adaptive value, avoiding the source's overloading where possible.

| Claim | Verdict and findings | Exact research dependencies |
|---|---|---|
| T1 | **MINOR, supported after the independent-randomization repair below**; R1, R2 | No new research premise; Brownian filtration/scaling and classical disintegration. |
| T2 | **SUPPORTED**; no theorem-specific finding | T1's normalized problem; Lenglart and truncation. |
| T3 | **SUPPORTED with MINOR naming correction R2** | P's deterministic variational formula/density; T1 repair for physical equality; T2's martingale estimate. |
| T4 | **SUPPORTED with MINOR naming correction R2** | P's optimizing law, positive support gap, upper support endpoint and deterministic relaxed optimality; neither author diagnostics nor T6/T7. |
| T5 | **SUPPORTED with MINOR naming correction R2** | Brownian exit-time facts; P only for comparison with kappa<1. |
| T6 | **SUPPORTED with MINOR degree correction R3** | P's support/KKT equalities; Gaussian bridge, integration by parts and conditional Stein identity. |
| T7 | **SUPPORTED with MINOR naming correction R2** | P's uniqueness, continuity/compactness and physical-clock exclusion; T6; Brownian conditional freezing, conditional Jensen and Anderson. |
| T8 | **SUPPORTED**, conditional on the repaired T1 for its physical version | T3 monotonicity, T4 strict region, T7 constant region. No continuity at eta_star is assumed. |

The counts are **distinct findings**, not duplicated for every theorem depending on the same finding.

## Frozen inputs, actual order and provenance

Manifest `manifest-v1.json`: SHA-256 **f28dcbb28a82a7e1db36d571a1809a1db444ec73f81d9507752aa4f8172a93fc**. It was hashed before scientific reading, read in full, and later parsed completely with my own `json.loads` call. Its SHA agrees with the assignment.

| Read order | Input | Full SHA-256 | Bytes / LF |
|---|---|---|---|
| 1 | `dispositions/info-3-revealed-martingale-variational-endpoint-parent-v1.md` | `3847d1eb8fca860226686468a6903e07dbeb9a9cfb678950f83707772c7f6818` | 7193 / 37 |
| 2 | `frontier-20261029-unrevealed-input-bridge-consolidated-v2.txt` | `901ff765009bb6ce1aa515e93a5cef27f07640dd2695db63910aa5bdd2a260b8` | 17877 / 139 |

Both input hashes, byte counts and LF counts were checked before reading, then checked again by my own code against the parsed manifest. Both end in LF. I read P completely first, then V completely as raw LF 1--70 and 70--139 (LF 70 intentionally overlapped). Only after those reads did I begin mathematical interpretation. Later targeted searches checked import names, and a raw reread pinned V:24--28, 76--89, 99--117 and 129--133. No linked/cited-but-unlisted source was followed. There is no certificate/result JSON among the scientific inputs; my generated control result JSON and receipt were each parsed completely by my own code, including all 44 result objects rather than just PASS text.

**Premise boundary.** I condition on P's adopted scalar-law assertions: the revealed value kappa=max F, weak continuity/physical-clock density, unique nu*, positive support gap a>0, upper endpoint 1, non-singleton support, physical-clock exclusion, KKT f<=kappa with equality on support, the stated negative moment, and the bounds sqrt(2/pi)<kappa<1. I did not reopen their unlisted proofs/reviews. P's citations to five earlier packets, f150 and its diagnostics are provenance only, not additional inputs. V's v1 and section-9 diagnostics are not premises and were not opened. f161/f162 and all held material were not opened.

## R1--R3: exact findings and repairs

### R1 — MINOR: false literal converse at V:28; gain identity has a short classical repair

V says: “conversely every G-progressive v defines an admissible w.” This is false for h>0: for 0<Su<h, G_u contains the **whole** pre-h path R, whereas the physical input at time Su may use only F_(Su). For example `v(u)=1_{W_h>0} 1_{0<u<min(eta,1)/2}` is bounded and G-progressive, but its inverse-scaled w is not F-progressive: for 0<s<h, the conditional probability of W_h>0 given F_s is Phi(W_s/sqrt(h-s)), strictly between 0 and 1 almost surely, so the indicator is not F_s-measurable.

This does **not** refute T1's equality of suprema. Here is the repair, using **regular conditional distributions/disintegration, independence of R and B, Fubini, and conditional freezing of Wiener/Itô integrals**. Work on the product of the R and B path spaces and freeze R=rho. Sections v^rho are, for almost every rho, progressive for the R-free delayed B-filtration. Their conditional input/output expectations `D(rho), N(rho)` obey the same E1 or E2 integrability, by Fubini. Conditional freezing of the stochastic integral follows first for simple processes and then by L2 localization; for E1 the Lenglart estimate in T2 gives the required integrable limiting norms. If D(rho)=0 then N(rho)=0. Each R-free v^rho inverse-scales to a genuinely physical admissible w: before h its dependence on rho is just a fixed deterministic parameter, and afterward it depends only on the already observed post-h increments. Consequently

`N(rho) <= (gamma_i(h)/sqrt(S)) D(rho)` almost everywhere.

Integrating establishes that independent initial randomization cannot enlarge the supremal ratio. Together with the immediate physical-to-G inclusion this proves T1's equality. Equivalently, the overall ratio is a D-weighted average of conditional R-free ratios. This also allows a **single common independent randomizer** when comparing different eta in T3; its changing physical path-space description is irrelevant to the value. The repair adds no research premise and is the same kind of conditioning device already used in P, T3 and T7. I classify it MINOR because it is a fully supplied, short classical de-randomization repair, not an unresolved theorem gap. T8's physical interpretation depends on this repair outside T4's explicit-witness range.

### R2 — MINOR: named-at-use import contract is only partly met

V names Lenglart, Dambis--Dubins--Schwarz, optional stopping, dominated convergence, the quantile clock, Brownian bridge, Gaussian IBP, Stein, portmanteau, Anderson and the tower property. It does **not** literally name every classical import at its use. In particular:

* Brownian scaling is used at V:24, in the deterministic-clock J bound at V:44, and in the conditional sqrt(lambda) Brownian representation at V:46, without being named there.
* Cauchy--Schwarz/Jensen and Tonelli underpin V:42 and the derivative domination at V:50; positivity of Brownian tube probabilities underpins V:58 and V:60, but the tube/support fact is unnamed.
* V:66 uses E tau=1 (optional stopping for B_t^2-t), Markov's inequality, submartingale optional sampling for |B|, and later the first two of these inside its explicit constant. The text says “optional stopping” but does not identify these separate uses.
* V:101 uses conditional Itô isometry/Tonelli and **conditional Jensen**; the latter is not named there. “Jensen” at V:121 is a different application. Conditional freezing/disintegration at V:36 and 103--107 and the layer-cake step converting Anderson's set inequality to an inverse-moment inequality at V:121--123 are also implicit.

These are standard and valid in the circumstances; I name them where used in the reconstructions below. This is a genuine MINOR compliance/presentation defect under the manifest, not a new conditional research premise or an unsupported theorem.

### R3 — MINOR: inaccurate homogeneity description at V:76

The clause “all expectations below are of functions homogeneous of degree 0 or -1” is literally inaccurate: e.g. `X Delta Y^(-1/2)` and `Delta^2 Y^(-1/2)` have degree **+1** in (X,Z). The needed global expectations have degree +1 or -1, and both are integrable for a nondegenerate 2D Gaussian with Y comparable to X^2+Z^2. A polar integral near zero has radial factor r^(k+1)dr, finite for k>-2; the Gaussian tail handles infinity. For fixed nonzero z the conditional Stein functions and derivatives are smooth and integrable; that conditional step is not justified by a blanket global claim about degree. Correcting the degree list leaves every identity and sign conclusion intact.

## Independent reconstruction T1--T5

### T1: normalized lagged information, exact gain

**Brownian independent increments and Brownian scaling** give independence of R=(W_r)_(r<=h) and `B_u=(W_(h+Su)-W_h)/sqrt(S)`, with B standard Brownian. **Deterministic linear substitution for Itô integrals**, proved for simple integrands then by localization, gives `v(u)=sqrt(S)w(Su)`, `||v||=||w||` and

`x_(h+Su)=integral_0^u v(r)dB_r = X(u)`.

The state is zero before h, hence ordinary substitution in the time integral gives `||z||=sqrt(S)||X||`. The physical filtration maps into G_u exactly as V states in its forward direction. Since G_u is contained in `sigma(R) join F_u^B`, B is Brownian in that initially enlarged filtration by **independence**, and X is a continuous local martingale with quadratic variation `A(u)=integral_0^u v^2`. E1 implies A(1)<infinity almost surely. The reverse equality of suprema is the R1 **conditional-disintegration** repair, not the source's false pathwise converse. At h=0 R is trivial and the converse is direct. Thus the claimed exact gamma_i(h)=sqrt(S)kappa_i(eta) is reconstructed for both classes.

### T2: E1/E2 equality and finiteness

Apply **Lenglart's domination inequality** to the nonnegative process M^2 dominated by its continuous quadratic variation, with exponent 1/2: `E sup|M| <= 3 E sqrt(<M>_1)`. Localization handles a merely local martingale. For v_n=v1_(|v|<=n), **dominated convergence** gives `E||v-v_n|| -> 0`: the random norm converges to zero and is bounded by ||v||. v_n is bounded, progressive and E2. The **reverse norm triangle inequality**, `||X||<=sup|X|`, linearity of the stochastic integral and Lenglart give

`|E||X(v)||-E||X(v_n)||| <= 3 E||v-v_n||`.

The positive denominators also converge, so each E1 ratio is a limit of E2 ratios. Conversely **Cauchy--Schwarz** gives E2 subset E1. This proves equality and the common upper bound 3. No E2 assumption was smuggled into the E1 argument.

### T3: monotonicity, revealed region and one-sided continuity

Use a common independent randomizer (or eliminate it by R1). Increasing eta shrinks `F_((u-eta)^+)^B`, so the admissible set decreases and kappa(eta) is nonincreasing. **Deterministic Gaussian time change and Brownian scaling**, followed by P's physical-clock weak density and F continuity, give the deterministic supremum kappa at every eta. For eta>=1, **conditional freezing on the independent R** makes v a deterministic path, giving `E[||X|||R]<=kappa||v||` and hence kappa(eta)=kappa.

For eta<1 split at eta. v1 is R-measurable, so the same conditional argument gives `E||X(v1)||<=kappa E||v1||`. X(v2) is zero before eta, so the deterministic norm bound and **Lenglart** give `E||X(v2)||<=3sqrt(1-eta)E||v2||`. **Triangle inequality**, with both input-piece norms bounded by ||v||, proves the upper bound kappa+3sqrt(1-eta); T2 gives the alternative bound 3. Together with the deterministic lower bound this proves T3 and continuity as eta increases to 1. **T1's scaling** gives the stated physical-unit estimate.

### T4: both strict-excess mechanisms, including physical realization

**Quantile-transform theory** gives A*_#Leb=nu*, A*(u)>=a, and A*(u)<1 exactly for u<1-m1. Right continuity and monotonicity give the source's elementary quantile inequalities. Because sup supp nu*=1, the left limit at u=1 is 1, whether or not m1>0. For bounded stopping times sigma,rho of a common Brownian beta, **optional stopping/Itô isometry on their min and max** gives `E|beta_sigma-beta_rho|^2=E|sigma-rho|`. The **reverse L2 triangle inequality, Jensen/Cauchy--Schwarz and Tonelli** therefore give (4.1). Only bounded clocks are needed in these applications; an unrestricted statement for arbitrary nonintegrable stopping times would need extra hypotheses.

For a physical absolutely continuous clock, **Dambis--Dubins--Schwarz**, with an independent continuation after terminal quadratic time, gives X=beta_A and ||v||^2=A(1). The past path X determines its own quadratic variation and, by the continuous-clock inverse, beta up to that quadratic time; flat portions create no ambiguity in Brownian values. A_n is a monotone Lipschitz moving average with A_n(0)=0, squeezed between shifted quantiles. **Dominated convergence** proves almost-everywhere convergence and A_n(1)->1. For deterministic clocks, **Brownian scaling** reduces J(A) to F of a probability law, so J(A)<=kappa.

**Mechanism A.** For eta<1-m1 choose the continuity point u0 and u1 as in V:46; q<=c<1 and mu=kappa(1-c)/2>0. The bounded perturbations lambda=1+epsilon phi are F_q-measurable, so the modified post-c clock values are stopping times. **Independent Brownian increments and conditional Brownian scaling** give the source's joint-law representation with a fresh gamma independent of F_c. Differentiating its square root and using **Cauchy--Schwarz** gives the integrable bound `(integral gamma^2)^(1/2)/(2sqrt(lambda))`. **Dominated convergence and the quotient rule** then give `J'(0)=E[phi(Psihat-mu)]`. Constant lambda gives a deterministic two-sided maximum at 1, so E Psihat=mu.

I reconstructed the conditional bound, not just its sign. Write beta_c=beta_q+D, Hgamma=integral gamma_r du and Kgamma=integral gamma_r^2du over the tail. The part involving `(D+gamma_r)gamma_r` is bounded by C1/sqrt(P_q). For the beta_q Hgamma term, replacing Y* by Y0 in the inverse square root makes the conditional expectation zero by **centering/independence**. The **mean-value theorem** bounds the remainder by `|Y*-Y0|/(2P_q^(3/2))`; expand `Y*-Y0=2(beta_q+D)Hgamma+Kgamma` and use independence of D and gamma. This gives exactly the displayed C2,C3 bound. On the tube event from V:58, P_q>=M^2 and |beta_q|<=2M/sqrt(u1), so |Psihat|=O(1/M). **Positive Brownian tube probabilities** (positive Gaussian density at a>0 followed by positive survival in an open strip) make this an event of positive probability. For large M, Psihat<mu there. Together with E Psihat=mu this forces P(Psihat>mu)>0; selecting its indicator gives a positive derivative.

For physical realization, when `1/n<u0-eta-u1`, monotonicity gives A_n(u0-eta)>=q. Thus the perturbation's indicator is determined by X on [0,u0-eta] and is available at every modified input time. Before u0 the clock is deterministic, so this is a causal, not circular, construction. The resulting inputs are bounded by a deterministic multiple of sqrt(n) and are genuinely R-free admissible E2 inputs. The continuity choice for u0, boundedness and (4.1) prove convergence of both numerator and denominator to the improved relaxed ratio. Therefore a physical ratio exceeds kappa.

**Mechanism B.** For eta<m1 choose u0>eta+1-m1. The clock has already reached 1 before u0-eta, so the whole beta path up to 1 is observed. With w=u0-(1-m1)>0, `P>=w beta_1^2`. **Independent increments at time 1** identify the added energy with sqrt(epsilon phi) times an independent normal zeta. Direct differentiation gives `k''(x)=(1-u0)P/[P+(1-u0)(beta_1+x)^2]^(3/2)`, between zero and (1-u0)/sqrt(P). **Taylor's formula, symmetry/centering of zeta, and dominated convergence** on {phi=1} subset {P>=p0} give `J'(0+)=(1/2)E[phi(Theta-kappa)]`.

On the positive-probability Brownian tube [delta/2,delta] over [a,1], `u0 delta^2/4<=P<=u0 delta^2`, and `Y*<=P(1+(1-u0)/w)`. Hence Theta is at least the displayed constant proportional to 1/delta and exceeds kappa for small delta. Choose phi to be that tube indicator. For large n, A_n(u0-eta)=1, so the ramp approximation is causal, bounded and E2; (4.1) and bounded convergence transfer the strict excess to a physical input. Combining the two mechanisms yields eta<max(m1,1-m1), in particular eta<1/2, equivalently h<T/3. No explicit nu* or numerical diagnostic is used.

### T5: small-lag stopped-input bound

The delayed indicator only depends on X through u-eta; before a decision is available it is identically one. This gives a bounded causal construction. **Dambis--Dubins--Schwarz** identifies the quadratic-time stopping point as `sigma=min(N,tau+theta)`, where r delta=N and r eta=theta=eta^(1/3). Up to the first hit, quadratic time grows at rate r; after the hit it continues exactly the lag eta unless capped by delta. Thus `tau wedge N<=sigma<=tau+theta`.

For **Brownian exit time**, optional stopping of `beta_(t wedge tau)^2-(t wedge tau)` and boundedness of the stopped path give E tau=1. **Submartingale optional sampling** for |beta| at the bounded times tau wedge N and sigma gives `E|beta_sigma|>=E|beta_(tau wedge N)|>=P(tau<=N)`. **Markov's inequality** then gives at least 1-1/N. The elementary square-root subadditivity gives `E sqrt(sigma)<=E sqrt(tau)+sqrt(theta)`. The state is constant after time delta, so `E||X||>=sqrt(1-delta)E|beta_sigma|`, while E||v||=E sqrt(sigma). Substitution proves the stated lower bound. Immediate stopping at eta=0 followed by delta down to zero and N up to infinity gives kappa(0)>=1/E sqrt(tau).

Expanding `(sqrt(tau)-1)^2` using E tau=1 gives the displayed identity for E sqrt(tau). On tau<=1/4 the square is at least 1/4. **Brownian marginal scaling and path continuity** imply P(tau<=1/4)>=P(|Z|>=2). The two tails restricted to [2,5/2] and its reflection give P(|Z|>=2)>=phi(5/2). The elementary bounds e^(25/8)<81 and sqrt(2pi)<3 give phi(5/2)>1/243, hence E sqrt(tau)<1943/1944. In particular kappa(0)>1>kappa. This proof does not need the exit-time Laplace transform used only in my diagnostic.

## T6: full two-atom exclusion reconstruction

Suppose nu*=p delta_a+(1-p)delta_1, 0<p<1 and 0<a<1. P supplies the KKT equalities at a and 1 and the inequality on all t. **Brownian independent increments** give X=B_a, Delta=B_1-B_a independent with variances a and 1-a; Z=X+Delta. The pair (X,Z) is a nondegenerate 2D Gaussian and `Y>=min(p,1-p)(X^2+Z^2)`. The corrected **2D polar integrability** argument in R3 justifies every global expectation below.

1. **Gaussian conditioning/Brownian bridge.** For lambda=(t-a)/(1-a), the conditional mean of B_t is (1-lambda)X+lambda Z and its variance is lambda(1-lambda)(1-a). Multiply the conditional second moment by Y^(-1/2), expand, and insert f(a)=f(1)=kappa. This yields

   `f(t)=kappa+lambda(1-lambda)(Gamma-2kappa)`,
   `Gamma=2E[XZ/sqrt(Y)]+(1-a)E[Y^(-1/2)]`.

2. **Gaussian integration by parts in Delta conditional on fixed X.** Smoothness holds for X!=0. Differentiating Y^(-1/2) gives `-(1-p)Z Y^(-3/2)`. Applying the Gaussian identity once to X times that function, and once to Delta times that function, gives both IBP equations at V:78--79. Their unconditional expectations are finite by the preceding 2D bound. Since X^2-Z^2=-2XDelta-Delta^2, substitution and `Y^(-1/2)=Y Y^(-3/2)` give

   `f(a)-f(1)=(1-a)E[((1-p)XZ-pX^2)Y^(-3/2)]`.

   The KKT equality therefore gives equation (6.1). Substituting it into Gamma-2f(a) cancels the pX^2 term and yields

   `Gamma-2kappa=(1-a)(1-p)E[ZDelta Y^(-3/2)]`.

   This last reduction genuinely needs KKT; off the equality curve the residual equals f(1)-f(a), as independently checked diagnostically.

3. **Conditional Gaussian law and Stein's identity.** Gaussian conditioning gives `X|Z=z ~ N(az,a(1-a))`. For z>0, g_z is smooth with `g'_z(x)=-3px(px^2+(1-p)z^2)^(-5/2)`. Write z-X=(1-a)z-(X-az). Stein's identity `E[(X-az)g_z(X)|z]=a(1-a)E[g'_z(X)|z]` then gives precisely

   `m(z)=(1-a)z E[g_z(X)|z]+3pa(1-a)E[X(px^2+(1-p)z^2)^(-5/2)|z]`.

   The first term is strictly positive. For the second, its integrand is odd and positive on x>0; the positive-mean normal density satisfies density(x)>density(-x) for all x>0. Pairing the two half-lines proves its expectation is strictly positive. **Gaussian symmetry** gives m(-z)=-m(z). Thus Zm(Z)>0 for Z!=0 and its expectation is positive; global integrability follows from degree -1 in two dimensions. Therefore Gamma>2kappa, so f(t)>kappa at every a<t<1, contradicting KKT.

No two-atom law is possible. Because singleton support is excluded by P, with min a and max 1 in the compact support, there must be a third support point in (a,1). Thus the two support points in (a,1] needed by T7 really exist. No diagnostic estimate is used as a premise or as a proof of this fact.

## T7: persistence below eta=1 and pointwise nonattainment

### 1. Conditional second moment and strict comparison target

For 1/2<=eta<1, put c=1-eta<=eta. The whole v2 path is measurable with respect to H=`sigma(R) join F_c^B`, hence with respect to F_eta=`sigma(R) join F_eta^B`; v1 is R-measurable. **Brownian independent increments and conditional freezing of Wiener integrals** make `M(u)=integral_eta^u v2 dB` conditionally centered given F_eta. X1 is constant after eta. **Conditional Itô isometry and Tonelli**, with its cross term zero, give

`E[||X||^2|F_eta]=Y0+integral_eta^1 (1-r)v2(r)^2dr <=Y0+cW`.

**Conditional Jensen for the concave square root** gives (7.1). Conditional second moments are finite almost surely even when unconditional E||v||^2 is infinite; the final norms have finite expectation by Lenglart and the E1 hypothesis. Conditioning on independent R reduces the problem to a deterministic v1 and W measurable with respect to B on [0,c]. If v1=0, the strict bound is sqrt(c)<kappa. Otherwise divide v1 by its positive deterministic norm and W by its squared norm. This normalization is essential and preserves H-measurability.

**Deterministic Gaussian time change** then gives `Y0=integral beta_s^2 nu(ds)` with nu=(A1)_#Leb a physical probability clock law and F(nu)<kappa by P's uniqueness and physical-clock exclusion. In conditioning on B|[0,c], the future integrals are independent of that path; all relevant past information about X1 is beta up to A1(c). Brownian pieces in B|[0,c] not seen by X1 do not reveal future beta increments. This is the **Gaussian independent-increment/conditional-freezing** justification of the source's conditional-law sentence, not an assertion that the two sigma-fields themselves are equal.

### 2. The elementary estimates and their hypotheses

For y>=c, conjugating the square-root difference and using

`sqrt(y+cw)+sqrt(y)>=sqrt(c)(sqrt(1+w)+1)`

gives the sqrt(c) branch of (7.3). For y<c, the lower bound by `sqrt(y)(sqrt(1+w)+1)` gives its c/sqrt(y) branch. These are exactly the two terms of the maximum; w=0 and y=c cause no difficulty. The estimate is valid pointwise, not merely in expectation. Set `Lambda_H=E[max(sqrt(c),c/sqrt(Y0))|H]`; then `Lambda_H<=sqrt(c)+c E[Y0^(-1/2)|H]` whenever the latter is finite.

For (7.4), differentiating `sqrt(cw)-kappa(sqrt(1+w)-1)` gives its unique critical point `w*=c/(kappa^2-c)`. For c<kappa^2 the derivative changes from positive to negative and the function tends to minus infinity, so this is the global maximum; substitution gives kappa-sqrt(kappa^2-c). Independently, square-root subadditivity gives the pointwise bound needed to apply this supremum to psi_H. Thus the source's decomposition is exact, including for H-measurable random W, using **regular conditional expectation and measurability/continuity in w**.

### 3. The uniform conditional inverse moment, with Anderson made explicit

T6 supplies t1<t2 in (a,1]. Choose q0 and r as in V:119. All three mass constraints defining U use **relatively open subsets of [0,1]**: [0,q0), I1 and I2. **Portmanteau's lower semicontinuity** makes U weakly open. Their nu*-masses are positive because the chosen points, and a, are support points. By P's **weak continuity of F, compactness of probabilities on [0,1], and uniqueness**, the maximum on the compact nonempty complement is strictly less than kappa, so d0>0.

For nu in U and c smaller than the lower early-mass threshold, `Leb{u:A1(u)<q0}=nu([0,q0))>c`. Monotonicity of the physical clock forces A1(c)<q0. **Jensen for the square on each interval** gives

`Y0>=nu(I1)Z1^2+nu(I2)Z2^2`,

where Zi=beta_(q0)+Gi and Gi is the normalized interval average of beta_s-beta_(q0). This is a centered jointly Gaussian pair G independent of beta|[0,q0] by **Gaussianity and independent Brownian increments**.

For each fixed conditioning value b=beta_(q0), apply **Anderson's inequality for centered Gaussian measures and symmetric convex sets** to the ellipsoidal superlevel sets of `phi(y)=(nu(I1)y1^2+nu(I2)y2^2)^(-1/2)`. **Layer cake/Tonelli** converts the set inequality into `E phi(G+(b,b))<=E phi(G)`. These expectations are finite by the following rank-two argument, so the possible infinite value at the origin is harmless. Combining it with the Jensen lower bound on Y0 proves the first inequality at V:123.

For Var(G1), split off the common independent Brownian increment over [q0,t1-r], of coefficient exactly one in the normalized average. This gives Var(G1)>=t1-r-q0. G2 contains, with coefficient one, the increment over [t1+r,t2-r], independent of both G1 and its other summands. Thus Var(G2|G1)>=t2-t1-2r. **Gaussian conditional covariance/Schur complement** therefore gives

`det Cov(G)=Var(G1) Var(G2|G1)>=d_min>0`.

Replacing both weights nu(Ii) by min(mu1,mu2) bounds E phi(G) by min(mu1,mu2)^(-1/2)E||G||^(-1). A nondegenerate 2D Gaussian density is at most `1/(2pi sqrt(det))`. Split at the unit disc: outside, ||G||^(-1)<=1; inside, the **polar integral** of ||x||^(-1) is 2pi. Hence `E||G||^(-1)<=1+d_min^(-1/2)`. This proves the stated K0, uniformly over nu in U and over the conditioning value b.

Since A1(c)<q0, **the tower property plus the preceding conditional-law identification** transfers this uniform bound down to H. The point here is residual two-dimensional Gaussian randomness *after* the revealed quadratic-time prefix, not merely an unconditional negative moment from P. This explains why T6 is genuinely load-bearing for T7.

### 4. Strictness, E1, and the revealed region

All of K0,d0 and the early-mass threshold are finite/positive. As c decreases to zero, both sqrt(c)+cK0 and kappa-sqrt(kappa^2-c) tend to zero, so a positive c_dagger satisfying all of V:127's inequalities exists. Put eta_dagger=1-c_dagger, strictly below 1. The bounds are monotone in c, so they persist for 0<c<=c_dagger.

If nu is in U then Lambda_H<=kappa and psi_H(W)<=0, leaving the strict deficit F(nu)-kappa<0. If nu is outside U, the uniform deficit is at least d0, while the possible adaptive increase is strictly less than d0. These prove (7.2) for each nonzero conditional input. On conditional samples where both v1 and W vanish, both sides are zero; a nonzero input has positive probability of a nonzero conditional norm. **Integration of a strictly positive integrable deficit over that event** proves the unconditional strict inequality, without asserting a uniform margin. It uses only E1, hence also E2. Deterministic admissible inputs approach kappa, so the gain equals kappa yet is not attained. For eta>=1 use P's revealed-input strict endpoint instead of attempting to set a negative c in this proof. T1's forward scaling gives the physical strict endpoint at sqrt(T-h)kappa.

## T8: phase transition and precise unresolved boundaries

By T3, `E={eta>=0:kappa(eta)>kappa}` is downward closed; it lies in [0,1). T4 makes it contain [0,b), b=max(m1,1-m1)>=1/2, while T7 makes it disjoint from [eta_dagger,infinity). It is nonempty and bounded. For eta_star=sup E, if eta<eta_star some member of E exceeds eta, so monotonicity forces eta into E; if eta>eta_star it is outside E and the deterministic lower bound forces equality with kappa. This proves the asserted dichotomy **without any continuity assumption at eta_star**. The supremum lies in [b,eta_dagger] subset [1/2,1).

The elementary map h=T eta/(1+eta) is strictly increasing, sends 1/2 to T/3 and has limit T/2 as eta increases to 1. **T1 with R1's repair** therefore proves the physical threshold assertion, not just a statement about the enlarged randomized class. At eta=eta_star itself the present argument does not decide strict excess versus equality. It also says nothing about pointwise nonattainment in (eta_star,eta_dagger), where only the gain value is known. Those omissions are correctly disclosed, not silently filled.

**Important logical corollary, not an additional premise:** nonemptiness of the asserted interval forces `c_dagger<=m1<=1-c_dagger`; in particular m1>0, so T4+T7 do imply an atom of nu* at 1. P did not assert that atom but did not exclude it. I explicitly checked this consequence instead of assuming m1=0 or borrowing the section-9 estimate of about 0.72. The packet's “values unknown” statement is consistent with this qualitative corollary. No numerical value or claim about an atom at a is inferred.

## Independently authored bounded controls and receipts

Executed exactly once via `reviewer-f186-run-controls-v1.py`, stdin DEVNULL, with a **120-second subprocess wall cap**. No author code was executed or imported. The control source, runner, stdout/stderr and complete JSON result are confined to this review-wave directory.

* Observed start: **2026-10-29T16:29:47.821373+00:00**.
* Observed end: **2026-10-29T16:29:49.707942+00:00**.
* Wall time **1.88629779079929 seconds**, exit **0**, timed_out **false**.
* **44 expected outcomes / 0 unexpected**, including **19 intended-reason negative controls**. “Negative” means a deliberately incorrect or hypothesis-violating variant was detected, not that a theorem failed.
* Exact Fraction arithmetic is distinguished from interval arithmetic (60 decimal digits) and ordinary high-precision/float diagnostics. None is a universal or formal proof check.

| Family | Positive cases actually exercised | Intended-reason negative cases |
|---|---|---|
| C1, elementary (7.3) | 565 rational-input interval cases: 472 strictly positive margins, 93 equality cases, 0 bad. | Replacing max by min violates all 472 strict cases; sqrt(c)-only fails on 72 cases and c/sqrt(y)-only on 400. |
| C2, (7.4) | 12 rational stationary points match by enclosing intervals; 60 other points are strictly below the formula. | With kappa=4/5,c=1,w=10^8 the objective is >2000.79996: dropping c<kappa^2 really destroys a finite uniform maximum. |
| C3, Gaussian bridge | 20 exact Fraction Schur-complement computations confirm coefficients, variance and Var(X|Z). | Dropping bridge factor 1-a gives 20/20 mismatches. |
| C4, Stein | Four direct normal integrals agree with the derived conditional Stein expression, including oddness, with largest displayed discrepancy <3e-29. | Omitting derivative coefficient 3 causes discrepancies from about 0.03 to 35.18; m(-z)<0 as expected. |
| C5, Gaussian IBP | Four angular integral instances verify both IBP identities, KKT-difference identity and general off-KKT residual identity; two resolutions agree within about 1.1e-27. | The first IBP identity with its sign flipped fails on all four instances. |
| C6, KKT curve | Four numerical stationary-p instances at a=0.2,0.5,0.8566,0.95 have positive Gamma-2F and the factored identity. At a=0.8566: p approximately 0.143362659, F approximately 0.802138864, Gamma-2F approximately 0.134282878. | Using the KKT-reduced identity at p/2 fails; residual agrees with f(1)-f(a), so KKT was not dispensable. |
| C6, rounded author diagnostic | Independently evaluated the printed pair p=0.1434,a=0.8566: F approximately 0.802138864 and Gamma approximately 1.738545453, consistent with rounded diagnostics at the declared loose tolerance. | No numerical optimum or global bound is claimed; the rounded pair is not exactly stationary. |
| C7, separated intervals | 200 exact Fraction weighted-atom covariance examples meet all three bounds; minimum det/d_min is exactly 4228644187/3119040000. | Coincident averages have determinant zero: two non-separated copies do not supply rank two. |
| C8, inverse moment | Five covariance matrices satisfy the diagnostic 2D bound, e.g. isotropic actual sqrt(pi/2) approximately 1.253314137 <2. | Dropping the +1 tail term fails for covariance 100I; a rank-one inverse-normal analogue has truncated expectation >11.06, not <=2. |
| C9, exit-time constants | Exact rational factorial-tail bound on e and powers, interval phi(2.5)>1/243, exact 1943/1944 arithmetic. Two numerical classical exit-transform computations give E sqrt(tau) approximately 0.93052777544. | e^(25/8)>22, and P(|Z|>=2)<phi(2), showing the deliberately tightened variants fail. |
| C10, mapping/arithmetic | Exact Fraction Lenglart constant 3, 120 rational eta values, monotonic threshold map and eta<1/2 iff h<T/3. | Not a theorem proof, just exact arithmetic. |

C9's extra exit-transform diagnostic uses the **classical Laplace transform E exp(-s tau)=sech(sqrt(2s)) and the survival-series/Catalan evaluation**, not any author code and not a premise of my T5 proof. The angular diagnostics use the independently derived **2D Gaussian polar decomposition**, where the Rayleigh radial moments E R=E R^(-1)=sqrt(pi/2). Anderson's theorem itself is not numerically established by C7/C8; its analytical hypotheses and layer-cake application are checked in the T7 reconstruction.

Artifact bindings:

| Artifact | SHA-256 |
|---|---|
| `reviewer-f186-controls-v1.py` | `d09ba983593fcbde250fc835da5a0fdae54629becc478906dbced5f37bd2a565` |
| `reviewer-f186-run-controls-v1.py` | `42dabf9a7daa71451c085367640b052da1b82721582c2d3848e1f1a4bcd5b9ae` |
| `reviewer-f186-controls-stdout-v1.txt` | `5617fa6da219e5a540c771c544c15fa38328085f117146743dccbc5c7946262e` |
| `reviewer-f186-controls-stderr-v1.txt` (empty) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `reviewer-f186-controls-output-v1.json` | `411b9c9114adff5d936029dd14fd71dc3000ec8f5f191bf2e663f7de37a2bf54` |
| `reviewer-f186-run-receipt-v1.json` | `8f0a17b0f45c01e17665b5a5fd6cccfbe4a42d95ee061611ea51c950e2d20c98` |

The receipt hashes source and runner as well as outputs and records the actual exit/cap. The runner parsed every result and recomputed counts; I independently parsed the output and receipt again and examined each of the 44 result objects. There was no failed/capped scientific control run and no rerun. A cap would have been UNKNOWN, never acceptance.

## Deviations, access and files created

* Before the scientific manifest read, mandatory harness skill routing read `skill://independent-snapshot-review`. This is an administrative file outside the scientific input list, not a scientific premise; the external-model procedure in it was **not** executed because this assignment prohibits it. The manifest remained the first scientific source. I disclose the out-of-list administrative read rather than claim literal zero out-of-list reads.
* Shell commands listed metadata of the owned wave directory and read the clock. Package probes imported mpmath/numpy; scipy and sympy were unavailable and were not installed. Those failed availability probes are not scientific control failures or theorem evidence.
* Short unsaved eval/API probes tested mpmath interval endpoints and rough numerical exit-moment expressions. They were not clock/hash-pinned controls and contribute no acceptance evidence; the actual controls above were independently authored and run with the required receipt.
* No unlisted research source, author source code, sibling review, held payload, external model/API, web search, Git, deletion, publication, author contact or infrastructure change was used. No build/lint/test suite was run. No earlier packet, review, or frozen artifact was edited, and no independent-model or formal check is claimed.
* Source classical-import naming deviations R2 and source mathematical wording issues R1/R3 are preserved explicitly. Other compressed steps were expanded above rather than silently assumed. Exact threshold values, critical-point behavior and out-of-scope laws remain unresolved exactly as stated.

Files created, all under this wave directory:

1. `review-v1.md`
2. `reviewer-f186-controls-v1.py`
3. `reviewer-f186-run-controls-v1.py`
4. `reviewer-f186-controls-stdout-v1.txt`
5. `reviewer-f186-controls-stderr-v1.txt`
6. `reviewer-f186-controls-output-v1.json`
7. `reviewer-f186-run-receipt-v1.json`

The SHA-256 of this review is reported in the final handoff, not embedded self-referentially in its own bytes.
