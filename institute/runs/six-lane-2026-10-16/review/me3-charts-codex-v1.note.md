**DISPOSITION: the GLOBAL D2 certificate is not established by this packet.** I found one **FATAL interval-source defect**, two **MAJOR evidence/dependency gaps**, and smaller specification/checker issues. The mathematical assembly is otherwise coherent conditional on L1–L6 and valid interval certificates. This is no counterexample to the conjecture and no gate decision.

I used only static reads and SHA256 hashing inside the snapshot. Present files match their advertised hashes. **Zero leaves were numerically replayed.** SOURCE26 remains a projection of worker claims.

**1. FATAL — SWC coefficients undergo uncertified Python floating-point rounding.**

Locations: [SOURCE16:L28](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/me3-hostile-review-v1/snapshot/16-me3dual_v8.py:28), SOURCE15:L35, SOURCE12:L220. The active SWC binding is SOURCE18:L20.

In
```python
-2 * RE(pk) / j + 3 * (-1) ** j / j
```
the second summand is evaluated entirely using Python integers and `/`, producing a binary float before Arb receives it. Thus the program does not enclose the stated exact coefficient
\[
c_j=\frac{-2\Re(p^j)+3(-1)^j}{j}.
\]

The first discrepancy occurs at \(j=5\):
\[
\operatorname{fl}(-3/5)=-3/5+\epsilon,\qquad
\epsilon=\frac1{5\,2^{53}}>0.
\]
Outward arithmetic applied afterward does not recover this preceding rounding error.

The tails at SOURCE16:L53–54 bound only terms with \(j>20\). They cannot absorb the coefficient perturbation. Fix any interior \(s\), and take physical points \(\delta=h,\ \omega=h/2\). The recurrence gives \(U_4=3h^3\), hence
\[
\widehat\Psi_{20}-\Psi_{20}=-3\epsilon h^3+O(h^5),
\]
whereas the stated analytic tail is \(O(h^{19})\). The leading error makes the implemented \(\Psi\) test more negative. This disproves the claimed error bound for the implemented polynomial; it does not establish that a particular recorded leaf is false.

Repair the expression, for example:
```python
c.append((-2 * RE(pk) + 3 * (-1) ** j) / j)
```
Then independently re-enclose every SWC leaf using exact coefficients. Alternatively, add rigorous bounds for every coefficient error to both normalized tails. Reported sample margins cannot substitute for that repair.

**2. MAJOR — the executable dependency packet is incomplete.**

Locations: SOURCE08:L24, SOURCE17:L17, SOURCE18:L17, SOURCE19:L16, SOURCE20:L14; SOURCE25:L42.

Every driver and coverage checker imports `lane_guard`, but its source is absent. Its advertised hash does not reveal its import-time behavior or implementation of `xopen`. Consequently, the executable path is not fully statically auditable.

The python-flint/FLINT/Arb implementation and build identity are also absent. SOURCE00:L30 and SOURCE01:L15–16 state the intended arithmetic contract, but the packet does not expose the actual comparison, conversion, intersection, or NaN/inf implementations.

Repair: include the missing local dependency and bind the runtime and underlying arithmetic build. Correct Arb arithmetic can remain an explicit trusted import, but the report must distinguish that import from audited Python-binding behavior.

**3. MAJOR — hashes of supplied source do not authenticate the claimed executions.**

Locations: SOURCE00:L140–143; SOURCE25:L23–24,L38–49; SOURCE26:L4.

The snapshot lacks the seven leaf files, actual certificate and coverage reports, launch/audit receipts, freeze receipts, original index, manifest, and index-builder source. SOURCE26 explicitly omits the launch-code hash dictionaries.

Therefore this review cannot establish:

- that the claimed runs loaded these exact transitive implementations;
- that each audit used the correct spec, chart, variable order and allowed outcomes;
- that the claimed compressed and uncompressed leaf hashes match actual records;
- that the actual records tile their domains or satisfy their predicates.

This is missing evidence, not a detected hash mismatch. Repair requires the underlying artifacts and their bindings; the parent’s independent interval replay must establish the numerical assertions.

**4. MINOR — outcome validation is weaker than the checker descriptions imply.**

Locations: SOURCE20:L83–84; SOURCE19:L20,L76–77.

The dual checker accepts any `CERT:` suffix. A hypothetical record containing one root leaf per initial cell, each labelled `CERT:not-a-test`, satisfies its label and tree checks. The primal checker rejects `FAIL` only when the caller excludes it from the command-line allowlist.

These checkers explicitly perform geometry audits, so this does not itself refute an honestly generated certificate. It does mean `tiling_ok` is not semantic validation of a certificate outcome.

Repair: hard-code chart-specific outcome sets, unconditionally reject `FAIL`, bind the primal coordinate order, and check the declared depth bound. Predicate replay remains necessary even after those changes.

**5. MINOR — several universal statements need narrower, accurate quantifiers.**

Locations: SOURCE00:L151–153; SOURCE01:L52–53,L80–89,L99.

- LD1 and LD2 certify the **physical subset** of their padded rectangles. For \(s=1\) and \(\beta>\pi/2\), \(P=1\) but
  \[
  W=d\cos\beta\,e^{i\beta},
  \]
  so \(\beta+\arg P=\beta\) is not an argument of \(W\). The extra factor has negative sign. This padded point is nonphysical; it supplies no counterexample for finite admissible poles.
- Neither LD chart individually covers all \(s\). Their union does.
- SOURCE01:L84’s “\(\alpha\ge0\) iff \(1+\inf\ge0\)” is too strong. The derivative bound is sufficient, not necessary.

Repair the statements to quantify over each box’s intersection with the assigned physical domain, use the union of applicable charts for the universal \(s\) quantifier, and replace “iff” with a sufficient implication.

**Mathematical lemma verdicts**

| Item | Static verdict |
|---|---|
| Lemma D | Valid, conditional on the stated ratio interface |
| RADIAL / SMALL / TRIANGLE | Valid, including zero cases |
| Lemma M continuation | Valid, conditional on L6 and a valid P certificate |
| Global regional decomposition | Covers the full stated D2 domain |
| Final theorem | Unestablished because the numerical premises and dependency closure remain unresolved |

For Lemma D, SOURCE00:L60–83 correctly establishes \(a\ge0\): use the limit for \(\delta>0\), and a period average for \(\delta=0\). Positivity follows from
\[
\kappa y^2-2y+2
=\kappa(y-1/\kappa)^2+2-1/\kappa>0.
\]
The transform identity is
\[
\int_0^\infty q_\theta(t)e^{-zt}\,dt
=\frac{\kappa\theta^2}{z}-\frac{2\theta}{z^2}+\frac2{z^3}
=\theta^3Q_T(\theta z).
\]
A finite combination gives exactly
\[
a+\Re(cW)=(1-\textstyle\sum\lambda_k)a+\sum\lambda_kH(t_k)\ge0.
\]
This holds for **every** \(\theta>0\), with a possibly different finite combination for each \(\theta\). No hull closure or limiting combination is needed.

RADIAL uses \(t=\alpha/\omega\) and \(\lambda=|W|e^{\delta\alpha/\omega}\). SMALL follows because \(0\le\operatorname{Arg}_+W<2\pi\) and \(\delta\ge0\). TRIANGLE uses the spiral points at times \(0,t'\), with residual mass on zero. For \(W=0\), the empty combination suffices.

For Lemma M, SOURCE00:L89–112 and SOURCE08:L52–98 have the correct derivatives and factors:
\[
\frac{c_r}{c}=\phi+\frac{r-i}{1+r^2},\qquad
\zeta_r=-\omega\zeta^2,\qquad
S_r=\frac{2D}{a_1^3}.
\]
Thus DPOS implies the required derivative sign at fixed \((\omega,\phi)\).

The continuation path remains feasible because decreasing \(r\) increases \(\theta_1(r)\), and remains inside P. The first-crossing argument is valid. Strictness at the endpoint follows without requiring \(S_r(0)>0\):
\[
\sigma(r_0)>\sigma(r_0/2)\ge\sigma(0)\ge v_{\cos}.
\]
The INFEAS predicate is also sufficient. On \((\pi,2\pi)\),
\[
g_r'(u)=-(1+r^2)e^{ru}\sin u>0.
\]
If the lower phase already exceeds \(2\pi\), infeasibility follows directly from the conditional bound \(\theta_1(r)<2\pi\).

Finally, conditional L2 supplies an attained cone minimum on an extreme ray. Therefore strictness for each feasible extreme ray implies strictness for each fixed D2 cone. No uniform positive gap across all D2 configurations is required.

**Per-chart verdicts**

“Sound” below refers to the mathematical predicates and active source formulas under the intended arithmetic contract, not to numerical verification of recorded leaves.

| Chart | Verdict and source |
|---|---|
| P | Sound conditional predicates and continuation. SOURCE08:L76–98; SOURCE09:L18–45 |
| G | Sound SMALL, branch-controlled RADIAL/MVF and TRIANGLE logic. SOURCE13:L26–92 |
| SWB | Sound Taylor, derivative and MVF formulas. SOURCE14:L91–156 |
| SWC | Exact mathematics is sound; implemented coefficient enclosure is defective. SOURCE16:L21–73 |
| LW | Sound reciprocal-frequency compactification and SMALL test. SOURCE12:L112–120 |
| LD1 | Sound on the physical domain, including small-\(\beta\) and fallback branches. SOURCE14:L33–72; SOURCE12:L124–135 |
| LD2 | Sound on the physical constrained domain; compactification and SKIPs are sufficient. SOURCE14:L75–88; SOURCE20:L56–65 |

The supporting chart calculations are as follows.

**SWC.** The corrected root in SOURCE16:L24 satisfies
\[
p+\bar p=-A,\qquad p\bar p=B,
\]
so
\[
W=\frac{(1-p\xi)(1-\bar p\xi)}{(1+\xi)^3}.
\]
The logarithm series and recurrence are correct. In particular,
\[
|U_m|\le m|\xi|^{m-1}
\]
follows by factoring \(\bar\xi^m-\xi^m\), and
\[
\Phi=-\omega|\xi|^2\sum_{j\ge2}c_jU_{j-1}.
\]

Uniform convergence is available over the entire stated corner:
\[
B\le\frac{\kappa}{\kappa-1/2}=\frac{100}{39},\qquad
|\xi|\le\frac{\sqrt{13}}{10},\qquad
\sqrt B\,|\xi|\le\frac1{\sqrt3}<1.
\]
For exact coefficients, \(|c_j|\le(2R^j+3)/j\). Combining this with the \(U_m\) bound and summing geometric series gives precisely the two tails in SOURCE01:L60–61. Thus the root correction, recurrence, normalization and analytic tail are justified; finding 1 concerns the implemented finite coefficients.

**SWB.** For \(s\in(0,1)\), factoring the numerator gives
\[
g^{(k)}
=(-1)^{k-1}(k-1)!
\left(v_1^k+v_2^k-3z^{-k}\right),
\]
which yields the stated \(M_4,M_5\) bounds. The endpoint formulas at \(s=0,1\) extend directly.

Taylor expansion along \(\delta-iy\), using real derivatives on the real axis, gives
\[
\frac{\Phi}{\omega}
\le B+\omega_h^2\max(C,0)
+\omega_h^4\left(M_4/24+\delta_hM_5/120\right),
\]
and
\[
\frac{\Im g}{\omega}
\ge-g'-\omega_h^2|g'''|/6-\omega_h^4M_5/120.
\]
The active code implements these sufficient inequalities. Its MVF differentiates the required quantities correctly; for example,
\[
\partial_\delta B=-\delta g'',\qquad
\partial_\delta C=-g'''/3+\delta g^{(4)}/6.
\]
The real-axis \(g\) contains logarithms; its positive-order derivatives used here are rational. Finite denominator-based bounds provide the needed zero exclusion along the Taylor paths.

**G.** Both the naive and componentwise MVF rectangles enclose \(W\); their intersection remains an enclosure. The three branch predicates give nonnegative arguments in the upper, lower or left half-plane. They also establish a continuous logarithm on the actual box image. Coarse intermediate balls can cause failure to decide, which does not invalidate a successful certified enclosure under the intended arithmetic semantics.

For TRIANGLE, the formulas
\[
b=\frac{\Im W}{\Im Z'},\qquad a=\Re W-b\Re Z'
\]
solve \(W=a+bZ'\). The accepted inequalities supply finite nonnegative weights of total mass at most one. The floating-point root finder selects a rational candidate \(\theta'\); its accuracy as a root is unnecessary. Only \(\theta'\ge0\) is needed, which its bracket construction ensures.

**LW.** Substitution of \(\nu=1/\omega\) gives exactly
\[
\zeta=\frac{\nu}{\nu(1+\delta)-i}.
\]
The exponent in SMALL becomes \(-2\pi\delta\nu\). The face \(\nu=0\) has \(W=0\); all finite assigned frequencies have \(\nu>0\).

**LD1/LD2.** For finite physical poles,
\[
0<d\le1/65,\quad 0<\beta<\pi/2,\quad
\zeta=d\cos\beta\,e^{i\beta},\quad
\frac{\delta}{\omega}=\frac{1-d}{\tan\beta}.
\]
The candidate arguments are therefore legitimate when accepted.

For boxes beginning at \(\beta=0\), \(P(0)>0\), and
\[
\alpha(\beta)=\int_0^\beta
\left(1+\Im(P_\beta/P)\right)\,du.
\]
A nonnegative lower derivative bound ensures \(\alpha\ge0\); its upper bound, together with \(\beta/\tan\beta\le1\), proves the ratio bound. The actual zero-starting cells lie below \(\pi/2\).

For fallback boxes intersecting the physical domain,
\[
0\le\frac{\operatorname{Arg}_+W}{\tan\beta}
\le\frac{2\pi}{\tan\beta_l}.
\]
This remains valid when their upper endpoint exceeds \(\pi/2\). Entirely nonphysical boxes need no pole interpretation.

For LD2, setting
\[
\rho_t=s+d\cos\beta,\qquad \chi=s/\rho_t
\]
gives
\[
0<\rho_t\le1/16+1/65=81/1040,
\]
so every required small-\(s\) physical point is represented. Expansion yields the stated \(\widehat P\) and \(W\). The code’s \(\widehat P_\beta\) correctly holds \((\chi,\rho_t)\) fixed. Replacing \(1-d\) by \(1\) is conservative because the physical argument ratio is nonnegative.

Both SKIPs are sufficient. The product minima occur at the corners used by the code, and cosine decreases throughout the padded beta range:
\[
(1-\chi_h)\rho_{t,l}>d_{\max}\cos\beta_l
\]
excludes every physical point of that box.

**Coverage, geometry and arithmetic limits**

The pole partition in SOURCE00:L145–149 covers all \(\delta>0,\omega>0\). Its closed boundaries overlap safely, including \(\delta=64,\omega=640,\omega=1/5,\delta=3/10\), and the P boundaries. LD1 and LD2 jointly cover all \(s\). The G SKIP inequality \(\delta_h\le3\omega_l\) correctly includes equality.

The compactification faces introduce no required extra density cases:

- \(s=0,1\) extend the rational formula; every finite \(\theta>0\) has \(s\in(0,1)\).
- SWC/SWB use normalized extensions at \(\omega=0\), applying RADIAL only for \(\omega>0\).
- \(d=0,\nu=0,\beta=\pi/2,\rho_t=0\), and LD2’s \(\chi=1\) are limiting faces; finite physical poles are represented away from the relevant singular endpoints.

The exact-rational parser and split implementations agree: SOURCE08:L35–40,L102–119; SOURCE17:L29–34,L84–98; SOURCE19:L26–60; SOURCE20:L21–49. Ties choose the lowest index. Refinements are dyadic **relative to rational initial cells**, not necessarily absolute dyadic coordinates.

The DFS stack checks correctly enforce a full finite binary tree per cell. Missing leaves leave open nodes; duplicates, prefix conflicts and nonbinary path characters cannot match the generated expected nodes; missing or reordered cells are rejected. Malformed records cause errors or exceptions rather than a fresh successful report. This is a static algorithm verdict only.

The jet product, quotient, exponential, real/imaginary projection and logarithmic derivative rules are correct. MVF is valid on the actual smooth box functions. Rational midpoint and half-width balls suffice even when those rationals are not exactly representable as point balls.

Successful tests require certified interval ordering, not midpoint comparisons. Under the intended Arb contract, indeterminate quantities must not satisfy the acceptance inequalities. SWB explicitly checks several finite quantities; other paths rely more directly on comparison and transcendental-operation semantics. **Those actual NaN/inf and intersection semantics remain imported and unverified in this packet.**

**Audit inventory**

| Category | Extent |
|---|---|
| Statically audited | SOURCE00–01 assembly; SOURCE05–07 domains/specs; active call paths in SOURCE08–20; SOURCE25–26 provenance claims |
| Hash checked, not independently proved here | Reduction artifacts and controls in SOURCE02–04 and SOURCE21–24 |
| Conditional interfaces | L1–L6, including D1 attainment and the bound \(v_{\cos}<T\) |
| Missing or imported | `lane_guard`; runtime/arithmetic implementation; launch and audit bindings; original index/manifest; raw leaf files and reports; control/replay evidence |
| Numerical verification performed here | None |

The target throughout remains the exact cosine minimum \(v_{\cos}\), attained in D1 and strictly exceeded in every D2 cone conditional on the repaired certificates. The audited decomposition addresses unrestricted D2 damping and frequency.