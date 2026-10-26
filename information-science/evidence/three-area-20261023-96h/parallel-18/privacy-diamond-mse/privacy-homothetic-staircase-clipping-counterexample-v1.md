# Exact clipped-core obstruction to homothetic-diamond MSE optimality

Owner: InfoResearch96h-2, registered info-1 privacy primary. Last actual pre-write observation: **Sun Oct 25 14:21:46 PDT 2026**. **AUTHOR-WRITTEN CANDIDATE at the named standard facts below; not independently reviewed or parent accepted.** This is a source-facing corollary at ONE exact finite epsilon, not a replacement for the registered all-finite-epsilon theorem or a new mechanism/discovery count.

## 0. Exposure, permanent process history and exact claim boundary

The clipping lead was already explored in written reasoning BEFORE the actual v86-A RETURN and before the14:17:37 primary resumption ACK. `v86-review-primary-interleaving-deviation-v1.json` records that permanent serial-scope **PROCESS MAJOR**; `privacy-primary-source-post-v86-resumption-ack-v1.json` discloses the exposure. A later ACK does not retropreregister, cure or admit that earlier reasoning. V86-A was actually RETURNED before this successor body. Parent explicitly accepted no privacy claim by metadata or its process acknowledgment.

An IMPORTANT correction to that unadmitted exploratory lead is explicit here: the coefficient of gamma^2 in its critical quintic was wrongly written as -10300. Direct differentiation gives **-9994**. The missing term is6*u*M2 in the intermediate coefficient; the correct coefficient is12*u*M2-2*M3. The old polynomial remains immutable historical exposure, but is WITHDRAWN as mathematics. All operative coefficients, signs, fractions and privacy claims are derived below; no exploratory decimal estimate or unverified earlier reduction is an input.

**Exact claim.** Let D={x in R2:|x1|+|x2|<=1}, epsilon=log101, and let F_D be ALL Borel probability laws satisfying

`mu(E)<=101*mu(E+h)` for EVERY Borel E and EVERY h in the full CLOSED D.

There is an explicitly specified clipped-core staircase law mu_clip in F_D with finite squared-Euclidean cost, such that for EVERY gamma in[0,1],

`E_(P_gamma)(Z1^2+Z2^2)-E_(mu_clip)(Z1^2+Z2^2) > 1267/115897500000`,   (C)

where P_gamma is precisely the homothetic-diamond one-parameter staircase family in Geng–Viswanath1312.0655v1 Eq14 at Delta=1. Thus

`inf_(mu in F_D) E_mu ||Z||_2^2 <= E_(mu_clip)||Z||_2^2 < min_gamma E_(P_gamma)||Z||_2^2`.

This proves only this strict comparison. It does NOT identify the global optimum, classify its optimizers, certify novelty/priority, or assert that arbitrary-core staircases are suboptimal.

### Named inputs

- **STD-M:** Tonelli for nonnegative functions, translation-invariance of planar Lebesgue measure, polynomial integration and the usual Borel construction of densities.
- **STD-G:** convex hulls/Minkowski sums, the triangle inequality for the l1 norm, and the elementary vertices of a clipped diamond.
- **STD-S:** the convergent geometric series, its factorial moments and binomial expansion; all moment values used are displayed exactly.
- **STD-A:** elementary differentiation, intermediate value theorem, Descartes' rule counting positive real polynomial roots WITH multiplicity, and exact integer/rational algebra.
- **SOURCE-DEF:** the actual DEFINITION of P_gamma in [Geng–Viswanath1312.0655v1, Eq14/24 and SectionIII](https://arxiv.org/html/1312.0655v1). Its MSE optimality is NOT an imported theorem. The full native1073LF source was previously actually read; the exact family, L1 theorem hypothesis, MSE-suggestion paragraph and normalizer were reread for this successor. Frozen reader snapshot `artifact://30900`, SHA256 `1d8a99ecca8a93314163dd5c5819a54f7e9f4042be016a2f45be8238994955f9`.

No LAW-STD, BRANCH-OLD, CAL, MDA-T6, numerical root/table, formal kernel, scientific computation or another problem-specific research theorem is a correctness premise of (C). Every mathematical label below is **WRITTEN**, not kernel/program checked.

## 1. A full-continuous-D private shell construction

Let K be a compact convex set containing a neighborhood of0. For integers j>=0 put C_j=K+jD, and define

`nu_K(x)=min{j>=0:x in C_j}`.

The sets cover R2 and are closed, so nu_K is finite and Borel. For every h in CLOSED D,

`C_j+h subset C_(j+1)` and `C_j-h subset C_(j+1)`.

Consequently `|nu_K(x+h)-nu_K(x)|<=1` for ALL x,h under consideration. With q=1/101 and finite positive normalizer A_K, the density

`p_K(x)=q^(nu_K(x))/A_K`

satisfies `p_K(x)<=q^(-1)p_K(x+h)` pointwise. Integrating over ANY Borel E proves `mu_K(E)<=101*mu_K(E+h)`. This covers every real displacement in the full closed diamond, not only integer shifts, a boundary generator or selected events.

For the cores below, areas and moments grow polynomially in j. The positive identity

`q^(nu_K(x))=(1-q)*sum_(j>=0) q^j 1_(C_j)(x)`

and Tonelli give the exact normalizer and cost numerator

`A_K=(1-q)*sum q^j area(C_j)`,

`N_K=(1-q)*sum q^j integral_(C_j)(x1^2+x2^2) dx`.

Both converge, and the squared-Euclidean cost is N_K/A_K. An auxiliary geometric J with probabilities `(1-q)q^j` is only a convenient way to write these sums; this is NOT a claim that choosing a uniform point in C_J with those unadjusted mixing probabilities generates p_K.

## 2. Exact polygon geometry and Euclidean moments

For gamma>0 and0<=delta<gamma/2 define

`K_(gamma,delta)=D_gamma intersect {||x||_infinity<=gamma-delta}`,

where D_r={||x||_1<=r}. For delta=0 this is the homothetic diamond D_gamma. For delta>0 it is a genuine eight-sided diamond with its four axis tips clipped.

For every integer j>=0,

`K_(gamma,delta)+jD = D_(gamma+j) intersect {||x||_infinity<=gamma+j-delta}`.   (G)

To check equality rather than assume intersections commute with Minkowski addition, set L=gamma+j. The right side's vertices are the sign changes/coordinate permutations of `(L-delta,delta)`. Each such vertex is its corresponding K_(gamma,delta) vertex plus j times the appropriate signed coordinate axis, hence lies in the left side. Conversely every sum on the left satisfies the two right-side inequalities by triangle inequalities. Taking the convex hull proves (G).

For L>=2delta, subtract four disjoint axis caps from D_L. Each cap has area delta^2. Its Euclidean second moment is

`integral_(L-delta)^L integral_(-(L-x))^(L-x) (x^2+y^2) dy dx`

`=integral_0^delta [2u(L-u)^2+(2/3)u^3] du`

`=L^2 delta^2-(4/3)L delta^3+(2/3)delta^4`.

The full diamond has area2L^2 and Euclidean second moment(2/3)L^4. Hence the EXACT formulas are

`area(C_j)=2L^2-4delta^2`,

`moment(C_j)=(2/3)L^4-4L^2delta^2+(16/3)Ldelta^3-(8/3)delta^4`.          (G2)

This is squared EUCLIDEAN loss. It is not the squared-l1 moment, which would have a different coefficient.

## 3. Exact geometric-moment table and the entire source family

Put u=q/(1-q)=1/100. For J with probabilities(1-q)q^j, factorial moments are `E(J)_k=k!*u^k`; writing raw powers in factorial powers gives:

|n|m_n=E J^n|value at u=1/100|
|---|---|---|
|0|1|1|
|1|u|1/100|
|2|u+2u^2|51/5000|
|3|u+6u^2+6u^3|5303/500000|
|4|u+14u^2+36u^3+24u^4|142953/12500000|

For an arbitrary gamma in[0,1], let T_n(gamma)=E(gamma+J)^n. In particular

`T1=gamma+u`, `T2=gamma^2+2u*gamma+m2`,

`T3=gamma^3+3u*gamma^2+3m2*gamma+m3`,

`T4=gamma^4+4u*gamma^3+6m2*gamma^2+4m3*gamma+m4`.

With delta=0, Section1's density is exactly SOURCE-DEF's Eq14 almost everywhere: its initial plateau is gamma D and subsequent constant plateaux extend to (gamma+j)D. Splitting each unit-radius annulus at k+gamma yields precisely the source's two pieces. The normalizer is `2T2`, which agrees with its Eq24 because `m2=(q+q^2)/(1-q)^2`. Thus for the WHOLE source parameter interval,

`F(gamma)=E_(P_gamma)||Z||_2^2 = T4(gamma)/(3T2(gamma))`.                (F)

At gamma=0 the core has zero area, but the density/sum construction still defines the source endpoint law; T2(0)=m2>0. For n>0, shifting the geometric sum gives `T_n(1)=T_n(0)/q`, so F(1)=F(0). This also accounts for the gamma0/gamma1 alias; no endpoint is omitted.

## 4. Exactly isolating the global homothetic-D minimizer

Differentiating T_n gives n*T_(n-1). Therefore

`F'(gamma)=2[2T3*T2-T1*T4]/(3T2^2)=H(gamma)/(750000*T2^2)`,

where the CORRECT integer polynomial is

`H(gamma)=500000gamma^5+25000gamma^4+10600gamma^3-9994gamma^2-5406gamma+51`.   (H)

For explicit authentication of the corrected coefficient, the coefficients of `h=2T3*T2-T1*T4`, before multiplying by500000, are:

|power|exact symbolic coefficient|value times500000|
|---|---|---:|
|5|1|500000|
|4|5u|25000|
|3|2m2+8u^2|10600|
|2|12u*m2-2m3=(612-10606)/500000|-9994|
|1|6m2^2-m4|-5406|
|0|2m2*m3-u*m4|51|

In descending order the signs are +,+,+,-,-,+, so Descartes gives at most TWO positive roots counted with multiplicity. The EXACT rational sign table is

|argument|H(argument)|sign|
|---|---:|---|
|0|51|positive|
|1/3|-24931/243|negative|
|1|520251|positive|

The intermediate value theorem supplies one root in(0,1/3) and one in(1/3,1). These exhaust all positive roots and are simple. Thus F increases, then decreases, then increases on the positive axis. Define **gamma_star as the UNIQUE real root of H in the rational isolating interval(1/3,1)**. No approximate evaluation, irreducibility/minimal-polynomial/Galois or radical claim is being made.

It remains to compare endpoints, rather than assume the second critical point is globally optimal. Direct exact evaluation gives

`T2(1/3)=5759/45000`,

`T4(1/3)=46782293/1012500000`,

`F(1/3)=46782293/388732500 <121/1000 <1/3`.

The first strict comparison is certified by

`121*388732500-1000*46782293=254339500>0`.

But `F(0)=F(1)=142953/382500>1/3`, since142953>127500. Together with the derivative signs, gamma_star is therefore the UNIQUE GLOBAL parameter minimizer on[0,1]. Write F_star=F(gamma_star). In particular

`1/3<gamma_star<1`, `F_star<121/1000`,

`T2(gamma_star)-F_star >5759/45000-121/1000=157/22500`,

`T1(gamma_star)<101/100`.                                         (B)

Only these coarse EXACT inequalities will be needed. They do not evaluate gamma_star numerically or import the global registered optimal law.

## 5. An actual private law strictly beating EVERY gamma

Set delta=1/1000 and K=K_(gamma_star,delta). Since gamma_star>1/3>2delta, Section2 applies with positive-area core. It contains a neighborhood of0, and Section1 constructs an actual Borel density private for every h in the CLOSED D. Its normalizer and cost numerator, by(G2), are

`A_delta=2T2-4delta^2>0`,

`N_delta=(2/3)T4-4delta^2*T2+(16/3)delta^3*T1-(8/3)delta^4`,

with every T evaluated at gamma_star. Its MSE is `J_delta=N_delta/A_delta`.

Using `(2/3)T4=2F_star*T2`, the exact comparison is

`N_delta-F_star*A_delta`

`=4delta^2[-(T2-F_star)+(4/3)delta*T1-(2/3)delta^2]`

`<4delta^2[-157/22500+101/75000]`

`=-4delta^2*(1267/225000)=-1267/56250000000`.                       (D)

The inequality uses(B) and drops only the NEGATIVE final term; no approximate sign test occurs. Also gamma_star<1 and positive coefficients give

`A_delta<2T2(1)=2*(1+2/100+51/5000)=5151/2500`.

Dividing(D) by the positive normalizer therefore proves the explicit gap

`F_star-J_delta >1267/(56250000000*A_delta)`

`>1267/115897500000`.

Since F(gamma)>=F_star for EVERY gamma in[0,1], this is exactly(C), including both aliased endpoints. Every moment is finite by the convergent polynomial-weighted geometric sums. The mean is0 by the core's sign symmetries, although the objective here is directly the second moment and does not require a separate centering assumption.

This gives an exact finite-epsilon obstruction with an algebraically isolated parameter and rational clipping width. It does not rest on the registered642LF theorem's uniqueness, an old D/R branch classification, a CAL theorem or a numerical table.

## 6. Exact source consequence, prior family attribution and nonclaims

The precise public target is [Geng–Viswanath1312.0655v1 SectionIII](https://arxiv.org/html/1312.0655v1#S3): after its Theorem1 for L1 loss, it conjectures/suggests that the SAME correlated one-parameter family is optimal for squared-Euclidean loss. At epsilon=log101, Delta=1, the actual source-defined family fails that extension by(C). This is NOT a contradiction of its proved L1 theorem, the published2015formal L1 hypotheses, or matching-norm K25/MDA26 theorems. It is not a current-openness or first-counterexample certificate.

Nor is mu_clip a new staircase CONSTRUCTION. K is an origin-box ideal, since decreasing coordinate absolute values preserves both its l1 and linfinity constraints; and K subset D_(gamma_star) subset D. Its successive disjoint shells are exactly the cumulative sets C_j minus C_(j-1). They fit the PRIOR arbitrary-core construction immediately before Theorem13 of [Soria-Comas–Domingo-Ferrer2013, DOI10.1016/j.ins.2013.07.004](https://doi.org/10.1016/j.ins.2013.07.004), complete AM at [UOC](https://openaccess.uoc.edu/handle/10609/152758), actual local sourceLF926–945. The AM's malformed final Theorem13 recurrence is preserved and not silently corrected; its minimality theorem is not a premise. Full privacy was proved independently in Section1.

The source attribution is positive: that paper supplies the broad mechanism family, while the G13 question already supplies the exact mixed-cost comparison problem. This successor removes LAW-STD+BRANCH-OLD from the dependency set of the PRECISE historical-extension counterexample in the earlier481LF dossier Section8.1. It does not remove or settle the dossier's specialist source/priority acceptance gap, nor minimize the dependencies of the separate global theorem.

Two bounded new public queries—`"Geng" "Viswanath" "squared" "staircase" "counterexample"` and `"multidimensional" "staircase" "mean squared" optimal differential privacy`—returned the already-inspected G13/G15, [K25](https://proceedings.mlr.press/v258/kulesza25a.html), [MDA26](https://arxiv.org/abs/2601.14597) and [KHP15](https://arxiv.org/pdf/1504.00065) among other indexes. This is NOT exhaustive forward-citation/version/specialist coverage and NOT evidence that no earlier equivalent counterexample exists. No unread search result is credited as a complete proof read.

**Remaining exact acceptance boundary:** independent full-body mathematical/source reconstruction of THIS later candidate and the481LF dossier, explicit parent treatment of the permanent serial PROCESSMAJOR and the corrected exploratory coefficient, then the separate source-equivalence/priority disposition. Until those occur this is AUTHOR-WRITTEN, with **NOVELTY_UNCLEAR**. Parent adoption of the registered all-law theorem does not auto-adopt this new source corollary or confer priority.

**Machine checks: NONE.** Every displayed integration, polynomial, sign and rational gap is written algebra. No floating-point proof arithmetic, rational calculator, scientific eval/Python restart/JavaScript computation, enumeration, solver, replay, model CLI, nested agent, tests/build/formatter, publication/contact, Git/deletion/config/shared-root write or new GO. Earlier metadata-only source cells and the interleaving history remain separately characterized; no zero-Eval-history or clean-process claim is made. The registered primary/model, original cutoff/deadline and all frozen records are unchanged; this is not completion of the96-hour round.
