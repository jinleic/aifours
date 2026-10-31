# EG18 source edge: full-Borel bounded/tight existence and the original unrestricted infimum

Owner **InfoResearch96h-2**, original info-1. Actual `/bin/date` BEFORE this write: **Mon Oct 26 06:40:45 PDT 2026**. **NEW AUTHOR-WRITTEN SOURCE-PROOF/APPLICATION CANDIDATE**, not a fresh independent review or parent adoption. All proof arithmetic is exact WRITTEN symbolic integration/measure theory. No scientific interpreter/eval/calculator/CAS/program/enumeration/replay/solver/CLI/nested agent or new GO.

## 0. Exact missing edge and positive PRIOR scope

The current source boundary leaves EG18's unrestricted-infimum interface separately NOT_RECONSTRUCTED. Earlier author prose already suggested the cap/benchmark/tightness specialization. This note does NOT pretend that suggestion was a new discovery; it supplies the COMPLETE proof and the full-Borel closure repair that the suggestion alone did not establish.

Primary source: Ehab ElSalamouny and Sébastien Gambs, [*Optimal noise functions for location privacy on continuous regions*](https://arxiv.org/abs/1805.09571), actual [v1 PDF](https://arxiv.org/pdf/1805.09571v1). Retained reader snapshot `RUN/privacy-source-snapshot-EG18-v1.txt`, SHA256 `ca164571240983d6c1e1c6d26521abe3b32efbc9c213f89fa641b1b35b506c80`,499 rendered logical LF. This hash identifies reader text, NOT original PDF bytes. Current selected complete reads:90–185 and276–321, covering the actual original-law model/density definitions, Theorem1, Theorem8 and its complete proof through the following scope remark. Earlier complete reads remain historical; this is not a newly claimed full499LF reread or all-version/publication audit.

**New WRITTEN source/application conclusion at ordinary classical imports only:**

1. EG18Theorem8's bounded/tight existence conclusion holds for ALL Borel laws/events, at its actual cap/tail/privacy hypotheses, with a correct proof supplied below.
2. Its actual full-Borel setwise-convergence conclusion can be justified under the UNIFORM cap/tail hypotheses, but not by claiming every Borel set has null boundary.
3. For the registered FULL CLOSED diamond sensitivity and squared-Euclidean loss, the original unrestricted ALL-law infimum is EXACTLY the minimum in ONE explicitly specified EG18 bounded/tight class, with no LAW642 value/geometry/uniqueness input.

This closes the named generic-existence/infimum interface as a NEW written candidate, not the explicit value, geometry or equality classification. The framework and compactness/attainment method are positively PRIOR. No new optimum/mechanism/discovery/novelty credit follows.

## 1. Actual source model includes the registered model exactly

EG18Section3.2 explicitly removes the older2016 density regularity assumption and defines a “symmetric” mechanism as a fixed noise PROBABILITY MEASURE independent of the input location. Here “symmetric” means additive/input-independent, NOT rotationally symmetric. Section4/Definition2 and Theorem1 give event translation inequalities for EVERY displacement in `V_X=X-X` and full output/noise space R².

Take the source input domain

    X=(1/2)D,  D={h:|h1|+|h2|<=1},
    ell(0)=0, ell(r)=epsilon for r>0,
    L(r)=r².

Convexity and central symmetry give X-X=D, including its boundary. Conversely every h∈D is exactly the input difference h/2-(-h/2). Thus the source's Theorem1 event condition is precisely

    mu(A)<=exp(epsilon)mu(A+h)
    for EVERY Borel A and EVERY h in FULL CLOSED D.         (DP_D)

The zero shift is only the identity. No density, angular symmetry, prior on X, output cutoff or different loss is inserted. Source regularity means a triangle inequality for ell applied to displacement lengths; the constant-off-zero ell satisfies it because unequal endpoints force at least one unequal adjacent pair. This is not the DIFFERENT convex/differentiable-at0 hypothesis of other metric-privacy theorems.

The source's circularization/planar-Laplace theorems have ADDITIONAL disk/extension/distance-proportional hypotheses and are not imported below. Generic-framework inclusion does not give a disk reduction or the registered explicit finite-epsilon value.

## 2. Exact general bounded/tight full-Borel theorem

Let H⊂R² be ANY specified set of displacement vectors, and let E(h) be a finite nonnegative privacy budget for each h∈H. Let M>0 and alpha:[0,infinity)→[0,1] satisfy alpha(r)→0 as r→infinity. Define K_(M,alpha) to be ALL Borel probability laws mu on R² such that:

    mu has an RN density p with0<=p<=M a.e.;
    mu({|z|2>r})<=alpha(r) for EVERY r>=0;
    mu(A)<=exp(E(h))mu(A+h) for EVERY Borel A, h∈H.        (CLASS)

Let c:R²→[0,infinity] be nonnegative lower-semicontinuous. If CLASS is nonempty and contains one law of finite c-cost, then it contains a finite-cost minimizer of `integral c dmu`.

This is the needed ALL-Borel version of EG18Theorem8. Its specialization is c(z)=L(|z|2). No continuity of E(h), regularity of H, monotonicity/continuity of alpha, density continuity or common pointwise RN representative across uncountably many h is assumed.

**Named ordinary imports:** finite-Radon/Lebesgue outer and inner regularity; RN; Tonelli; Prokhorov/Portmanteau; bounded-continuous weak convergence; C_c approximation of finite-volume Borel indicators in Lebesgue L1; extreme-value/minimizing-subsequence compactness. Their actual uses are given in §§3–5. The specialized cap and infimum application are proved in §§6–7, not quoted from LAW642 or an unreconstructed research theorem.

## 3. Tightness, preservation of the uniform cap and exact tail bounds

The shared tail envelope makes CLASS uniformly tight: for every eta>0 choose r with alpha(r)<eta; the closed Euclidean ball of radius r is compact and leaves at most eta probability outside. Prokhorov therefore supplies weakly convergent subsequences, with probability-law limits.

Suppose mu_n in CLASS converges weakly to mu. For any OPEN set O, Portmanteau and the uniform density cap give

    mu(O)<=liminf_n mu_n(O)<=M |O|.

For any Borel A, outer regularity of Lebesgue measure and mu(A)<=mu(O) for O⊃A give

    mu(A)<=M |A|.

When |A|=infinity the inequality is trivial; for finite |A| use open O approaching that volume. Thus mu is absolutely continuous and has a density<=M a.e. by RN. No assertion about boundaries of arbitrary sets is used.

For each fixed r>=0 the exterior `{|z|2>r}` is OPEN. Portmanteau directly gives

    mu({|z|2>r})<=liminf_n mu_n({|z|2>r})<=alpha(r).

Since r was arbitrary, EVERY exact tail bound survives on the SAME weakly convergent sequence. There is no uncountable-r diagonal, no assumed continuity point of alpha and no replacement by a slightly larger radius.

## 4. Full-Borel setwise convergence, with the actual uniform hypotheses

The retained source proof says that absolute continuity gives zero probability to the boundary of EVERY set, before its Eq11 `mu_n(V)->mu(V)` for all V. If V is interpreted as an arbitrary Borel set, that intermediate boundary assertion is false: take V=Q². Its boundary is allR², so every probability law gives boundary mass1, even though an AC law gives V mass0.

This does NOT refute Theorem8 or even its Eq11 under the full uniform hypotheses. The following supplies a correct alternative argument for Eq11 in the stronger all-Borel scope actually required here.

First take a bounded Borel set A. For every eta>0, regularity supplies psi∈C_c(R²),0<=psi<=1 with

    integral |1_A-psi| dz<eta.

The shared density cap for BOTH mu_n and the newly proved limit mu gives

    |mu_n(A)-mu(A)|
       <=2M eta+|integral psi dmu_n-integral psi dmu|.

Weak convergence sends the last term to0. Taking limsup and then eta↓0 proves mu_n(A)→mu(A) for EVERY bounded Borel A, without any boundary regularity assumption.

For an arbitrary Borel A, fix a closed radius-r ball B_r. Apply the bounded-set conclusion to A∩B_r. The two remaining tails satisfy

    |mu_n(A)-mu(A)|
       <=|mu_n(A∩B_r)-mu(A∩B_r)|+2alpha(r).

Let n→infinity, then r→infinity. Therefore

    mu_n(A)->mu(A) for EVERY Borel A.                    (SETWISE)

The quantifier is “for each arbitrary A on the SAME sequence,” not uniform convergence over all sets and not total-variation convergence. No moving set A_n or compact-family strengthening is claimed.

SETWISE is NOT asserted for arbitrary weakly convergent laws with no common cap/tail hypotheses. Those actual hypotheses are what make this repair work.

## 5. Privacy closure and finite-cost attainment

Fix ANY h∈H and ANY Borel A. SETWISE applies to both FIXED sets A and A+h, so their original inequalities pass to the limit:

    mu(A)<=exp(E(h))mu(A+h).

The subsequence/weak limit was chosen BEFORE the arbitrary h,A; no h-dependent subsequence or uncountable null-set intersection is used. Thus the limit belongs to CLASS.

Alternatively one can pass translated C_c test functions first and invoke Radon order. The SETWISE proof is given here because it repairs the ACTUAL missing step used by the source's Eq11, not because event closure requires a blanket Borel continuity-set assumption.

CLASS is weakly sequentially compact and closed. Choose a minimizing sequence with costs bounded by the finite comparator cost plus1. Its weak subsequential limit is in CLASS. Nonnegative-LSC Portmanteau gives

    integral c dmu<=liminf_n integral c dmu_n.

Feasibility gives the opposite bound by definition of the infimum. Hence equality holds and a finite optimum is attained. No claim of continuity of the unbounded cost, uniform integrability, moment equality or existence on a merely closed NONCOMPACT probability class is needed.

This reconstructs the stated general source theorem at its actual bounded/tight interface. The proof is standard measure theory; its attribution remains PRIOR, not a new compactness or existence principle.

## 6. FULL diamond privacy itself gives the actual universal density cap

Fix finite epsilon>0 and b=exp(-epsilon). If N is a Lebesgue-null Borel set, integrate DP_D over h∈D. Tonelli gives

    |D| mu(N)<=b^(-1)integral_D mu(N+h)dh=0.

Indeed, for each fixed z the translation fiber `{h:z∈N+h}` is null. Since |D|=2, every original feasible law is AC. This includes laws that were NOT assumed to have a density in the unrestricted problem.

Choose a nonnegative Borel density p. For EVERY fixed h∈D, event privacy gives `p(z+h)>=b p(z)` for a.e.z. Joint measurability/Fubini over h∈D then gives for a.e.z

    2b p(z)<=integral_D p(z+h)dh<=1.

Therefore every original feasible law has

    p(z)<=M_epsilon=exp(epsilon)/2 a.e.                 (CAP)

This does not falsely choose one simultaneous pointwise RN exception set for all real h. It is enough for the uniform M in CLASS and in the SETWISE repair.

## 7. ONE bounded/tight source class captures the ENTIRE unrestricted infimum

Use the explicit product-Laplace density

    p0(x,y)=(epsilon²/4)exp(-epsilon(|x|+|y|)).

The norm triangle inequality makes it DP_D for ALL closed-diamond shifts. Its coordinates are centered independent Laplace variables, each with second moment2/epsilon² by two exact integrations by parts. Thus

    J(p0)=U_epsilon=4/epsilon²<infinity.                 (BENCH)

Its cap CAP follows from the already-proved universal bound, so no unverified scalar inequality comparing its peak to M is needed.

Define the EXPLICIT Euclidean tail envelope

    alpha_epsilon(0)=1,
    alpha_epsilon(r)=min(1,U_epsilon/r²) for r>0.

It tends to0. Markov shows that EVERY original feasible law with J<=U_epsilon has this exact tail envelope. In particular p0 belongs to the source class CLASS with

    H=D, E(h)=epsilon for nonzero h and E(0)=0,
    M=M_epsilon, alpha=alpha_epsilon,
    c(z)=|z|2².

By §§2–5, this ONE nonempty class has an actual finite minimum m<=U_epsilon and minimizer mu_*.

Now take ANY law nu feasible for the ORIGINAL unrestricted all-Borel problem:

- If J(nu)<=U_epsilon, CAP and Markov put nu inside the SAME CLASS, so J(nu)>=m.
- If J(nu)>U_epsilon, including infinity, then J(nu)>U_epsilon>=m.

Thus EVERY original feasible law has cost>=m. Conversely mu_* is an original feasible law, since CLASS retains the entire DP_D event condition. Therefore

    inf_(ALL original Borel DP_D laws)J
      =min_(CLASS with stated M_epsilon,alpha_epsilon)J
      =m,                                               (UNRESTRICTED_INF)

and this infimum is attained in the original class. It is not a narrowed density-family optimum: all possibly better original laws were proved to lie in CLASS, and every law outside it is too costly to improve the benchmark.

No LAW642 premise, selected-core ansatz, angular averaging, canonical tail, source circularization theorem, numerical root, uniqueness or finite-parameter approximation is used. This is an independent reconstruction of the GENERIC existence/infimum edge using the earlier source's actual framework and classical facts. It does NOT compute m, classify its optimizers or give the registered explicit full-epsilon value.

## 8. Exact source disposition and remaining boundaries

The new candidate makes the earlier cap/benchmark/tightness suggestion fully literal and corrects the required ALL-Borel setwise/closure proof. If independently adopted, EG18's bounded/tight framework can no longer be left as an opaque unrestricted-infimum barrier for this registered model: ONE explicit parameter class captures the entire original infimum exactly, with a complete proof.

This does not retroactively certify the earlier source-summary wording or every source proof line. In particular “AC implies all Borel boundaries are null” must not be used, and arbitrary weak convergence must not be claimed setwise without the supplied uniform hypotheses. The retained snapshot wording is delimited; no uninspected version, publication-wide falsity or public refutation is asserted.

The exact source comparison remains positive: original all-law modeling, generic density/cap tools, weak compactness and attainment are PRIOR. The source's disk/extension/linear-budget planar-Laplace results still do not supply the registered mixed-cost geometry/value/ALL-law uniqueness. Those remain LAW642's separate adopted scope; original priority/novelty remains UNCLEAR.

This proof is independent of the new I233/II280 joint-limit composition and the new K25 proof union. Their exact bodies/gates are separate. A fresh COMPLETE source/math/dependency/application audit is REQUIRED before parent promotion of this successor; an old source verdict or related compactness argument cannot silently adopt it.

## 9. Permanent process and unchanged round

Exact WRITTEN work only; no scientific execution or machine-checked identity. All firstfive owner findings, SIXTH DISTINCT v111B written-exactness finding, SEPARATE077 continuation failure, v21 category correction, strict auxiliary214STOP/UNADMITTED and every parent/reviewer/source/import/N4UNKNOWN/exit/old-arithmetic qualification remain. No clean cognition/runtime/history or continuous-work census; no stronger human/family/cross-vendor/formal/kernel/executable/novelty/publication assurance.

Only this exclusive root was written; frozen source/parent/other-owner bytes unchanged. No auxiliary graph derivation, model/slot cutover, publication or new GO. Same eighteen owners; science cutoff **2026-10-27T11:05:38-07:00**, delivery **2026-10-27T12:35:38-07:00**; active actual substantive checkpoints at most30minutes. This is not early final-park or round closeout; the registered source/priority residual continues.
