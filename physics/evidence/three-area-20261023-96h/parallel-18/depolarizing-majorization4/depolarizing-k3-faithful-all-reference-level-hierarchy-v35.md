# Actual k3 continuation v35 — a faithful ALL-reference-level hierarchy for the FULL ORIGINAL channel maximum

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 09:20:56 PDT 2026**. Owner PhysicsDepol4-2. **NEW AUTHOR-WRITTEN global representation/completeness theorem at a NAMED symmetric-extension input, NOT a solution or a launched assay.** Exact ALL-variable conventional mathematics under prospectivev51; no newly chosen state/control/finite-level/numeric/boundary/limit/magnitude viability probe, decimal gloss, scientific interpreter/calculator/eval/CAS/program/enumeration/SDP/solver/replay/CLI/nested agent/GO. The integer reference count r is quantified over ALL positive integers throughout; NO particular new level is constructed/tested for viability.

## 0. Purpose and source trust cut

The state-INDEPENDENT one-reference full-copy certificate is already FALSE on an entangled reference/code sector in OLDv8Section8. V23 repeated it and receives ZERO new-progress credit. The ORIGINAL target is only on actual input-times-Slater-code vectors. This packet changes representation by retaining arbitrarily many SYMMETRIC reference copies, proves nesting and exact convergence back to the ORIGINAL physical maximum, and proves the actual code one-particle step needed to avoid a hidden Slater-realizability gap.

Substantive external input is **Doherty–Parrilo–Spedalieri, Theorem1 in SectionV**, *A complete family of separability criteria*, arXiv:quant-ph/0308032, primary URL https://arxiv.org/pdf/quant-ph/0308032 . Its precise statement is: a finite-dimensional bipartite state has symmetric extensions to EVERY number of copies of ONE subsystem iff it is separable. The theorem explicitly does NOT require PPT for this infinite-level completeness. I actually read the PDF-reader windows1–180 and184–365, including the WHOLE SectionIV symmetric-support restriction and WHOLE SectionV theorem/proof/end. This is a **NAMED published/research input**, not a new formal reproof of quantum de Finetti or of the entire paper. Its underlying exchangeability/deFinetti library remains named. The specialization to the nested optimization problem is proved below.

Source identity limits: the reader includes the canonical arXivv3 stamp5Nov2003; a regenerated body header date is NOT first-publication evidence. No original publisher/PDF-byte/whole-paper/library identity is authenticated. Remaining ordinary inputs are finite-dimensional compactness/partial traces/Ky Fan, explicitly proved fermionic one-particle bounds/convex hull, and the stated Pieri/class-sum facts in §6. No TC/CLIP/NP/PAR or old finite certificate is a premise of this hierarchy theorem.

## 1. Literal operator for EVERY r and EVERY physical p

Let H=(C^2)^tensor4, dimension16. Let A denote a reference copy of H and B=wedge^3H the three-code antisymmetric Hilbert space, dimension560. For EVERY positive integer r use

    V_r=Sym^r H_reference tensor wedge^3 H_code.

In the physical embedding with reference labels a=1..r and code labels b=1,2,3, let F_ab^(i) swap the physical qubit i between those copies. Define

    K_r(p)=(1/r)sum_(a=1)^r sum_(b=1)^3
                tensor_(i=1)^4[(1-p)F_ab^(i)+(p/2)I],
    0<=p<=4/3,                                         (LEVEL)

restricted to V_r. The complete sum commutes with the GLOBAL reference permutations and GLOBAL code permutations, so the symmetric/antisymmetric subspace is invariant. Individual reference-code terms need not preserve the code sign sector; it is the SUM which does. This distinction is not suppressed.

Equivalently let S(p) be the same one-reference sum over the three code labels on A tensor B. Then K_r is the average of S(p) acting on each reference and the SAME code system. S and K_r are Hermitian polynomial functions of p. No positivity of their full relaxed space is assumed, and their factors may have negative coefficients when p>1. The norm bound

    ||K_r(p)||<=3(|1-p|+p/2)^4

is finite and uniform in r on the full compact physical interval. This uses only the norm of an involutory swap and the triangle inequality, not an executed matrix construction.

For an ACTUAL rank-three projector Pi with normalized Slater C_Pi, its one-particle code marginal is Pi/3. Thus for EVERY pure psi,

    <psi^tensor r tensor C_Pi|K_r(p)|psi^tensor r tensor C_Pi>
        =Tr Pi D_p^(tensor4)(|psi><psi|).                (ACTUAL)

The sum over the three code labels cancels the marginal factor1/3; averaging r identical reference marginals cancels1/r. The local swap contraction is exactly the ORIGINAL channel factor `(1-p)id+(p/2)Tr(.)I` at each of its four physical sites, not a substituted coefficient map or independent marginal tuple.

## 2. The true ORIGINAL maximum and the separable reference/code maximum are EQUAL

Define

    beta_true(p)=max_(||psi||=1,rankPi=3)
                         Tr Pi D_p^(tensor4)(|psi><psi|).

Mixed inputs give the SAME maximum: at a fixed Pi the trace is affine in the input, so a pure maximizing input exists. All domains are finite-dimensional compact, hence the maximum is attained. This definition includes EVERY complex actual state/projector, all physical p, with no ansatz or positive cutoff.

The following one-particle fact removes a possible code-decomposability loophole. Let sigma be ANY density on wedge^3H, not necessarily a pure decomposable Slater vector. Its normalized one-code-copy marginal gamma has trace1 and

    0<=3gamma<=I.                                      (PAULI)

Indeed for EVERY unit f in H, the fermionic number operator `n_f=sum_(b=1)^3|f><f|_(b)` has eigenvalues0 or1 on wedge^3H: decompose it as `(f wedge wedge^2 fperp) DIRECTSUM wedge^3 fperp`. Thus `3<f|gamma|f>=Tr(sigma n_f)<=1` for every f.

Every E with0<=E<=I,TrE=3 is a convex combination of rank-three orthogonal projectors. To prove this, diagonalize E. The eigenvalues lie in the cube with sum3. Any nonintegral extreme vector would have at least TWO fractional coordinates (the sum is integer); an opposite small perturbation of those two preserves the cube/sum, contradiction. Hence every extreme has three ones and the rest zeros; the finite-dimensional polytope is their convex hull. Lifting the fixed eigenbasis proves the projector assertion. This is not a claim that every code density is Slater; only its one-particle EFFECT is in this actual projector convex hull.

For a reference/code PRODUCT state rho tensor sigma, the partial-swap formula gives

    Tr[S(p)(rho tensor sigma)]
        =Tr[E D_p^(tensor4)(rho)], E=3gamma.

PAULI and the projector convex hull bound this by beta_true(p), also when rho is mixed. Averaging over any SEPARABLE state on A tensor B preserves that upper bound. Conversely ACTUAL psi/Slater products are separable and realize beta_true. Therefore

    max_(sigma_AB separable)Tr[S(p)sigma_AB]=beta_true(p). (SEP=TRUE)

This proves the indispensable physical application. Merely forcing reference/code separability without checking the arbitrary fermionic code marginal would have left a gap; it is explicitly closed by PAULI and the rank-three effect convex hull.

## 3. Nested compact bosonic-extension sets and monotonicity

Let E_r be the set of one-reference/code marginals of densities supported on V_r=Sym^rH tensor B. It is compact/convex: a continuous partial-trace image of a compact convex state set with a fixed closed support constraint. It contains ALL separable A:B states, by decomposing the reference factors into pure states and taking their r-fold pure powers with the same conditional code factors.

Tracing out one reference from a state supported on Sym^(r+1)H yields support in Sym^rH, so

    E_(r+1) subset E_r.

All reference marginals have the same objective by permutation symmetry. Hence

    beta_r(p):=lambda_max(K_r(p))
       =max_(sigma in E_r)Tr[S(p)sigma],
    beta_true(p)<=beta_(r+1)(p)<=beta_r(p).             (MONO)

This is for ALL positive integers r and ALL physical p. No selected finite reference level is tested or declared successful. The finite eigenvalue maximum is equivalent to the linear maximum over density matrices on V_r; no SDP/program was generated or run.

Every element of intersection_r E_r has symmetric extensions of its A subsystem for EVERY r. Bosonic support is stronger than the permutation invariance in the NAMED DPSTheorem1, so the theorem implies it is separable. The reverse inclusion was constructed above. Therefore

    intersection_(r>=1)E_r=SEP(A:B).                    (INTERSECTION)

No PPT assumption, unsupplied finite-party completeness conjecture or independently chosen h-dependent extension is inserted. The source theorem's hypothesis allows per-r extensions; consistency is its named completeness conclusion, not a missing condition silently imposed on our optimizer family.

## 4. Exact pointwise AND FULL-physical-interval uniform convergence

For a fixed arbitrary p, beta_r decreases and is bounded below. Choose maximizing sigma_r∈E_r; compactness of E_1 gives a convergent subsequence. For every fixed k, eventually r>=k and sigma_r∈E_k. Closedness puts the SAME subsequential limit in EVERY E_k, hence in SEP by INTERSECTION. Continuity of the fixed linear objective and SEP=TRUE show the limiting objective is<=beta_true. MONO gives the opposite inequality, so

    beta_r(p) decreases to beta_true(p).                 (EXACT-LIMIT)

The optimizer subsequence is chosen at this fixed p only; no unjustified common optimizer across uncountably many p is asserted. Uniform convergence is established separately by continuous functions/compactness, not such a choice.

For each finite r, beta_r(p) is continuous as the largest eigenvalue of a finite Hermitian polynomial matrix. Beta_true(p) is continuous because its original state/projector domain is compact and the objective is uniformly continuous jointly in that domain and p. For EVERY eta>0 the sets

    U_r={p in[0,4/3]:beta_r(p)-beta_true(p)<eta}

are open in the compact physical interval, increase with r, and cover it by EXACT-LIMIT. A finite subcover therefore gives ONE r beyond which ALL physical p satisfy the inequality. Thus

    sup_(0<=p<=4/3)|beta_r(p)-beta_true(p)| ->0.          (UNIFORM)

This is a conventional ALL-level convergence proof, not an exploration of a chosen limiting configuration or a numerical convergence observation. It covers p1 and the noise endpoints through polynomial continuity without introducing the singular u=p/[2(1-p)] coordinate.

Let P3_ref(p) be the registered pure-product top-three output sum. With q0=1-p/2,q1=p/2 it is `q0^4+2q0^3q1` for p<=1 and `q1^4+2q1^3q0` for p>=1, continuous at the seam. The REGISTERED product input and its actual top3 projector show beta_true>=P3_ref. Therefore beta_r-P3_ref is a decreasing sequence of nonnegative continuous upper bounds on the TRUE original worst-case excess, converging uniformly to it. In particular,

    max_p[beta_r(p)-P3_ref(p)]
       decreases to max_p[beta_true(p)-P3_ref(p)].       (GLOBAL-EXCESS)

This is an exact faithful representation of the full original all-input/all-noise problem at the named DPS input, not an easier independent-spectrum problem.

## 5. What a finite analytic certificate WOULD establish — and what does NOT follow

For ANY finite positive integer r, a correct proof of

    K_r(p)<=P3_ref(p) I on V_r for EVERY physical p

would prove the WHOLE ORIGINAL k3 conjecture immediately by ACTUAL. But this packet proves NO such finite-level inequality, no positive eigenvalue estimate at a selected level, and no physical counterexample. An upper bound above the reference at a finite level is a relaxed reference/code state, NOT an eligible original witness.

Even if the original conjecture is true, beta_true=P3_ref may be attained at products and beta_r may stay strictly above it at EVERY finite r. UNIFORM convergence gives arbitrary positive-error upper certificates in principle, not an exact finite zero-defect level or algorithmic termination for equality. Infinite symmetric-extension completeness must NOT be relabeled finite polynomial/SOS completeness at a boundary. This is precisely the gap left after moving beyond the already false one-reference operator certificate.

No scientific admission is requested or supplied: dimensions grow with r, no reference level/problem instance/solver/controls/resources were selected and no native/SDP program exists in this work. Any future executable assay would still need its own full pinned-source/resource/control/independent-review gate and separate named GO. The present result is purely written mathematics.

## 6. Constant-polynomial coefficient: exact ALL-r Pieri weight identity

An additional literal identity illustrates which actual constraint is being retained, without choosing a new level for a viability test. The CONSTANT coefficient of the polynomial K_r(p) is

    J_cross/r, J_cross=sum_(a=1)^r sum_(b=1)^3 F_ab^(GLOBAL),
    F_ab^(GLOBAL)=tensor_(i=1)^4 F_ab^(i).

On Sym^rH tensor wedge^3H, the ordinary Pieri rule gives exactly TWO GL(H) shapes, multiplicityONE:

    (r+1,1,1), (r,1,1,1).

The central sum of all transpositions of r+3 labels acts by the sum of box contents. These are respectively `r(r+1)/2-3` and `r(r-1)/2-6`. The reference-internal class sum is r(r-1)/2, while the code-internal class sum is-3. Subtracting the two internal sums leaves J_cross eigenvalues r and-3. Thus for EVERY positive integer r,

    [K_r]_(constant p coefficient)
       =I-(1+3/r)P_(r,1,1,1).                           (PIERI)

The Pieri/class-sum facts are NAMED ordinary representation inputs; the model-specific subtraction/eigenvalue normalization is explicit. No local S4-type projection is incorrectly carried to r+3 copies, and no group-classification/program enumeration is used.

For an ACTUAL psi^tensor r/Slater state, the same constant coefficient equals TrPi rho=1-d by ACTUAL's polynomial identity. Consequently

    <P_(r,1,1,1)>=r d/(r+3).                            (ACTUAL-WEIGHT)

This is an ALL-r physical overlap relation, not an independently chosen isotypic weight. It is derived as a coefficient identity from the registered channel, not a numerical boundary/limit probe. The exact Slater/exterior identity in oldv28 is a base-level special case, not another new result counted from repeating it.

## 7. Source and original-science boundaries

DPSTheorem1 is a genuine substantive named infinite-extension input whose full operative SectionV statement/proof was read. Its quantum de Finetti ancestry and full published/PDF/formal library are NOT newly reconstructed. The proof above supplies all specialized compactness/one-particle/convexity/nesting/continuity/original-map bridges and explicitly does NOT infer a finite exact stopping level. The Schur/Pieri inputs are stated as ordinary representation facts, not a new formal derivation of Young theory.

The recently reread modern registered source2609.37240v1 still states the original exact majorization conjecture and proves exact shifted-logdet/approximate asymptotic results; those results are not substituted for original Fan3. Alhejji–Knill2307.06894v3 has positive prior alignment/overlap/dual framework; all-Schatten ordering does not imply full majorization. This packet is an application of PRIOR extension/fermionic/representation ideas, not a new method/novelty/priority or field-wide status claim. It introduces no external-source theorem as an unacknowledged import.

Original arbitrary-state k3 remains OPEN until an actual finite analytic bound/another exact common-projector argument or eligible physical failure is delivered. The all-input small-noisev30, BISEPv27, state regions and global deficit/exterior couplings retain their separately unreviewed scopes. All F3/ENTIREv22withdrawal/v23duplicateZERO-new-progress, PRIMARY073434/v44, REVIEWv125format/v47, cadence/privateapproxZERO/pause/inventory/orientation/readorder/freeze/clock/admission/source/import records remain permanent. Prospectivev51 permission is not history/provenance absolution. Same18/HOLD/OWNroot/oldpinnedimmutable/Oct27cutoff11:05:38/deadline12:35:38PDT; no interpreter/calculator/eval/CAS/program/SDP/enumeration/solver/replay/CLI/nestedagent/GO/newparameterprobe/decimal/frozenedit/Git/delete/publication/newslot/model/deadlinereset/strongerformal/kernel/human/family/executable/novelty/earlypark/roundcloseout.
