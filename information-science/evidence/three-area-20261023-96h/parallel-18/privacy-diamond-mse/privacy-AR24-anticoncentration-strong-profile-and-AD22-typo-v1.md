# AR24 source interface: TV anti-concentration, strong ALL-shift profile, multivariate projections and the published AD22 testing typo

Owner **InfoResearch96h-2**, original info-1. Actual `/bin/date` BEFORE this write: **Mon Oct 26 07:48:10 PDT 2026**. **NEW AUTHOR-WRITTEN bounded source/math/application candidate**, not reviewed or parent-adopted. Exact WRITTEN symbols/fractions only; no scientific interpreter/eval/calculator/CAS/program/enumeration/replay/solver/CLI/nested agent, machine check or new GO.

## 0. Positive primary source and actual read coverage

Primary source: Jordan Awan and Aishwarya Ramasethu, [*Optimizing Noise for f-Differential Privacy via Anti-Concentration and Stochastic Dominance*](https://www.jmlr.org/papers/v25/23-1624.html), JMLR25(351):1–32,2024; actual [publisher PDF](https://www.jmlr.org/papers/volume25/23-1624/23-1624.pdf). The cover identifies submission12/23, revision11/24 and publication11/24.

Reader artifact35155, SHA256 `d8fb12dbd4c4a02fc1a148d7a3062a48574bb0deac6b3e17cb9cad03ba24a8b2`,95182bytes,800 newline characters/801 logical lines. ACTUAL reads were1–300,418–460 and530–645. These include the actual scalar framework/anti-concentration/log-concave optimality statements, the source's multivariate-projection discussion, and the Lemma36/Theorem16 proof windows through the latter ending. This is NOT a whole801-line/32-page, all-proof, code/sampler/experiment, original-glyph or all-version certificate.

The source contributes POSITIVE PRIOR TV anti-concentration, half-integer CND near-optimality, sub-exponential CND tails, strong-profile log-concave optimality and discrete-sensitivity1 CND results. It ALSO contains an actual multivariate PROJECTION extension with explicit limitations. Its main results are univariate, but calling the ENTIRE paper devoid of multivariate content would be incorrect.

The source does not itself state the registered all-Borel planar full-diamond squared-Euclidean finite-epsilon value/equality theorem in these formal interfaces. That is a bounded literal-model conclusion, not proof that every creative corollary is unrelated or no other prior source gives the result. Priority/novelty remain UNCLEAR.

## 1. ADDITIVE published corroboration of the AD22 testing inequality correction

On PDF page3, **footnote1 explicitly says there is a typo in Awan and Dong2022: the inequality in the definition of T(P,Q) is in the wrong direction.** This is an actual later PRIMARY publication's stated correction, not merely our speculation about reader layout.

The previously delivered212LF `privacy-AD22-full-ROC-impossibility-and-maxdivergence-boundary-v1.md`, SHA256 `f5675d8a0ea1602bacfa5a11b0e757b4d1d463eb5ec6750eab07d9465a749a4a`, explicitly used the STANDARD operational definition

    T(P,Q)(alpha)=1-sup{E_Q phi:
                        0<=phi<=1, E_P phi<=1-alpha}.

Its comparison proof did not assume the erroneous reversed inequality from the older reader text. AR24footnote1 NOW corroborates that convention as a published source correction. This is LATER evidence only: it does NOT retroactively turn the earlier AD22 read into an original-PDF glyph audit, edit the frozen212LF body or certify every AD22 theorem/version.

All new mathematical comparisons in this packet use the explicit operational definition above. In particular T(P,P)=identity and `TV(P,Q)=sup_alpha[alpha-T(P,Q)(alpha)]`; the latter identity is proved directly by setting alpha=1-E_P phi and optimizing over tests, so no opaque ROC convention is imported.

## 2. Exact scalar anti-concentration, including atom endpoints

**Lemma — WRITTEN at elementary event order.** For ANY real-valued random variable Y, s>0 and a∈R,

    P(a-s/2<Y<=a+s/2)<=TV(Y,Y+s).                         (ANTI)

Take the Borel event B=(a+s/2,infinity). Then

    P(Y+s∈B)-P(Y∈B)
       =P(Y>a-s/2)-P(Y>a+s/2)
       =P(a-s/2<Y<=a+s/2).

By the definition of total variation, this difference is bounded by TV. This is the source's basic Lemma3 in a fully explicit half-open-event convention. No density, symmetry or continuity is needed.

For a continuous Y the endpoint choice is immaterial. For arbitrary atoms one must NOT replace the half-open interval by a closed one for free; below we use slightly larger radii and then a limit when needed. This is an anti-concentration theorem, not a proof of a global variance-optimal density.

## 3. Complete comparison under an ACTUAL strong reference shift profile

Let N have a symmetric UNIMODAL Lebesgue density g on R, nonincreasing with |x|; a consistent a.e. representative suffices. Its CDF is continuous, but the DENSITY may jump or have bounded support, including a uniform log-concave CND. Let Y be ANY real-valued competitor satisfying the STRONG condition

    T(Y,Y+s)>=T(N,N+s) for EVERY s>=0.                    (ALL_PROFILE)

Then `|Y-a|` stochastically dominates `|N|` for EVERY center a∈R.

**Proof — WRITTEN, ordinary TV/testing facts only.** For s=2R>0, symmetry/unimodality gives a single density crossing at R:

    g(x)>=g(x-2R) for x<=R,
    g(x)<=g(x-2R) for x>=R.

Therefore

    TV(N,N+2R)
      =integral_(-infinity to R)[g(x)-g(x-2R)]dx
      =F(R)-F(-R)=P(|N|<=R).                             (REF_TV)

A flat crossing interval is harmless. ALL_PROFILE and the operational TV identity give `TV(Y,Y+2R)<=TV(N,N+2R)`. ANTI then bounds every half-open interval(a-R,a+R] by P(|N|<=R).

For a CLOSED competitor interval[a-R,a+R], apply that inequality at R'>R and let R'↓R. The reference CDF is continuous because N has a Lebesgue density, so its central mass converges to P(|N|<=R). At R=0 take R'↓0. Hence

    P(|Y-a|<=R)<=P(|N|<=R) for EVERY a,R>=0.

This is precisely stochastic absolute-noise dominance; expectations of EVERY nonnegative nondecreasing function of the absolute error follow by the classical CDF/layer-cake characterization, including extended infinite expectations. The SAME reference N works for all objectives under the explicitly stronger ALL_PROFILE premise.

**Exact source import boundary:** AR24Theorem16 takes an infinitely divisible family f_s and the associated log-concave CND N, and requires `T(Y,Y+s)>=f_s` for EVERY s>=0. The identification `f_s=T(N,N+s)` for that constructed/scaled CND is a NAMED research input from the AR24Lemma15/36 and AD22 log-concave-CND construction. Its complete derivation from an arbitrary divisible family was NOT reconstructed in this pass. Once that reference-profile identification is supplied, the comparison implication is proved directly above, not inferred from a headline.

No claim is made that ordinary fixed-epsilon step privacy implies ALL_PROFILE, or that a pure-DP CND is variance-optimal among all continuous laws. The source itself explicitly distinguishes those cases, including examples/limitations; their printed numerical examples were NOT replayed or used as verification.

## 4. Exact control: ordinary unit-step pure DP is a STRICTLY larger scalar class

Fix epsilon>0 and b=exp(-epsilon). Consider the normalized scalar density proportional to

    u(x)=b^max(0,ceil(|x|-1/2)).

Its unit-step privacy follows because its integer level changes by at most1 for EVERY |h|<=1, using the absolute-value triangle inequality. Mass and moments are finite by geometric tails. No optimizer claim is made.

Take h=1/4 and A=(5/16,3/8). On A, u=1; on A+h=(9/16,5/8), u=b. Thus the equal-length events give

    mu(A)/mu(A+h)=b^(-1)=exp(epsilon)
                         >exp(epsilon/4).               (CONTROL)

Let N be centered Laplace of rate epsilon, a symmetric log-concave reference. Its shift h likelihood ratios are bounded by exp(epsilon|h|), so its testing profile dominates the pure-DP envelope at privacy epsilon|h|. If this mu satisfied ALL_PROFILE for that Laplace family, it would satisfy the corresponding epsilon/4 pure event inequality at h=1/4, contradicting CONTROL. The equivalence between that pure testing envelope and mutual event domination is the ordinary operational DP/testing characterization; it follows by applying the test inequalities to event indicators and their complements.

This EXACT fractional control prevents silently using AR24Theorem16's all-small-shift hypothesis for the ordinary constant-epsilon neighbor class. It is a scalar source-hypothesis control, not a new registered mechanism, optimum or public source refutation.

The source's half-integer/near-optimal pure-DP CND statements remain POSITIVE PRIOR. They are not upgraded into all-radius/variance optimality without the strong profile, and the integer-valued sensitivity1 theorem is not relabeled a continuous planar theorem.

## 5. Honest multivariate projection interface in the registered norm geometry

Let K be ANY compact convex genuine norm ball in R^d, and let X be an AC random vector. Take a linear functional ell with dual norm `||ell||_(K*)=1`. Compactness gives a norming vector v∈K with ell(v)=1. Then

    {|X-a|_K<=R} subset {|ell(X-a)|<=R}.

The scalar Y=ell(X) is AC by an invertible linear coordinate chart and Fubini, so there is no endpoint atom ambiguity. Applying ANTI at interval length2R gives

    P(||X-a||_K<=R)
      <=TV(ell(X),ell(X)+2R)
      <=TV(X,X+2R v).                                   (DUAL_PROJ)

The last inequality is TV data processing under the measurable map ell, since ell(v)=1. Every normalization is explicit; this does not assume arbitrary Euclidean orthogonal projections are normalized for an unrelated sensitivity norm.

For the original D=l1 ball, a dual-unit functional has l-infinity coefficient norm1; one chooses its actual norming v in D. For the exactly transformed square sensitivity, the dual norm is l1. The full shift2R v, not a unit-coordinate substitute, is what enters DUAL_PROJ.

AR24's Discussion pages20–21 actually gives such a dimension-free projection approach and says it is generally NOT tight because it does not capture dimension; its Gaussian illustration is source context, not an exercised result. The full printed projection/glyph normalization is not certified here; DUAL_PROJ supplies the rigorous explicit dual-pairing version needed for our application.

This source overlap is genuine multivariate content. It does NOT identify the full joint density or registered exact MSE, and no global joint stochastic dominator follows merely from scalar projections. Nor is a weaker projection bound substituted for LAW642's already supported full value. No new numerical lower bound or scientific discovery count is claimed.

## 6. Exact disposition and source assurance limits

This packet provides:

1. actual primary published corroboration of the AD22 testing-inequality typo, additively and prospectively;
2. a complete elementary TV anti-concentration proof with honest atom endpoints;
3. a complete stochastic comparison under the ACTUAL entire reference-shift profile, with the source's divisible-family/CND identification retained as a named NOT_RECONSTRUCTED transitive input;
4. an exact control separating constant-epsilon unit privacy from a log-concave reference's stronger small-shift profile;
5. the norm-correct dual-projection comparison, while preserving the source's actual multivariate extension and its limitations.

No worldwide result absence, all-creative-corollary inequivalence, novelty/priority clearance, whole-paper proof/algorithm/code/experiment certificate, or original full-book/channel conclusion follows. Positive PRIOR anti-concentration/ROC/CND/stochastic-order/geometry methodology remains credited. Original contribution status stays UNCLEAR.

A fresh COMPLETE source/mathematics/dependency/application gate is REQUIRED. The published footnote is later SOURCE evidence, not a retroactive amendment of the212LF proof packet or its freeze. Neither AD22 reconstruction nor the other source gates accepts this new packet automatically. The original registered LAW642/I233/K25 same-norm adoptions retain their precise separate scopes.

## 7. Current unreachable manuscript lead, not an absence claim

For the separate LeDeBlis scalar-access DOI22739334, primary record/API/exportJSON/correctly encoded OAI all returned403. DataCite concept/version metadata and abstract were retrieved; its media route returned no media entries. OpenAlex maps the version to the concept and lists null PDF URLs at both locations; OpenAIRE lists only the same Zenodo landing page. Exact title/author searches did not expose an actual manuscript route. No filename is invented and no formal/Lean claim is certified or rejected from an abstract. That ONE source remains UNREAD/PENDING; the bounded priority audit is not exhaustive or clear.

## 8. Execution, process and unchanged round

The actual AR24 footprint, published typo and complete comparison/projection leads were saved BEFORE this body in checkpoint099. All proof work is exact WRITTEN; no scientific execution or mathematical kernel check. All firstfive owner findings, SIXTH DISTINCT v111B written-exactness finding, SEPARATE077 continuation failure, v21 category correction, auxiliary214 UNADMITTED/strictSTOP and every parent/reviewer/source/import/N4UNKNOWN/exit/old-arithmetic qualification remain. No clean cognition/runtime/history or continuous-work census, stronger human/family/cross-vendor/formal/kernel/executable/novelty/publication assurance or new GO.

Exclusive own root only; frozen sources/ACKs/parents/other-owner bytes unchanged. No auxiliary graph derivation, new model/slot/owner, publication or deadline reset. Same eighteen owners; science cutoff **2026-10-27T11:05:38-07:00**, delivery **2026-10-27T12:35:38-07:00**; active actual substantive checkpoints at most30minutes. This is not early final-park or round closeout; the authorized registered source/proof/priority residual continues.
