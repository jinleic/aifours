# Registered additive diamond privacy: exact-cost-budget joint order/family limit and sharp nonattainment boundary

Owner **InfoResearch96h-2**, original info-1. Actual `/bin/date` BEFORE this write: **Mon Oct 26 06:33:48 PDT 2026**. **NEW AUTHOR-WRITTEN COMPOSITION CANDIDATE, NOT REVIEWED OR ADOPTED.** This is a new theorem at the explicit UNION of named inputs below. Two separately accepted branch gates do not themselves accept this composition. No prior pinned body is edited.

## 0. Precise gap, result and non-substitution

The complete parent `RUN/privacy-order-infinity-and-joint-tail-recovery-entire-parent-v1.md`, SHA256 `a892ac6a021d7aa30a2c1b13eeee8c6ca08bb50b917c67ac9f97f2d4bd35f990`, adopts TWO separate proofs and expressly warns:

    exact-epsilon family costs V(epsilon)+eta
    DO NOT by themselves give family cost<=V(epsilon),
    nor an automatic order/resolution double limit.

This note supplies the missing joint-limit proof under an EXACT cost budget, rather than silently treating eta slack as free. It uses the already-supported STRICT value monotonicity to create an ACTUAL positive cost margin at a slightly relaxed privacy value; only then does it use recovery. No continuity of V, unproved compactness of a fixed family, uniform resolution rate or source algorithm is substituted.

**New WRITTEN result at the named union:** for EVERY finite C>0, a specified nested union of finite JOINT bin/geometric-tail families recovers r_infty(C) at the EXACT cost bound J<=C, and its finite-order optimal values converge to r_infty(C) along EVERY cofinal order/family sequence. Both iterated value limits agree. ALL vanishing-error family near-minimizers have only all-law infinity-optimal weak cluster laws; at C=V(epsilon), ALL converge weakly and in second moment to the unique LAW642 optimum.

**Crucial surviving distinction, also proved here:** at C=V(epsilon), NO member of the family can be BOTH exact epsilon-private AND cost<=C. The value is an INFIMUM, with privacy approaching epsilon from above; it is not exact-epsilon tight-budget attainment or a finite-alpha pure-DP certificate. This sharp boundary preserves rather than withdraws the parent's warning.

The registered class stays ALL Borel query-output-independent additive laws on R², EVERY shift of the FULL CLOSED unit-l1 diamond D, squared-Euclidean loss. This is a source-family approximation/interface theorem for that same model, not a new optimum, mechanism, lower bound, source priority or model/slot cutover.

## 1. Exact named import union and proof responsibility

### I233 — full-law order/infinity theorem

`privacy-renyi-infinity-full-diamond-bridge-v1.md`,233LF, SHA256 `03ccb06b95b5b3cdbf9b9e120293a6a68c3c8399ff2621c9ee77e1ccdd3df843`, at the COMPLETE parent adoption cited above.

Precisely imported:

- for every finite C>0, P_C={all Borel probability laws with J<=C} is weakly compact;
- every finite-order/infinity infimum r_alpha(C) is attained; e_C=r_infty(C) is finite and STRICTLY positive;
- r_alpha(C) is nondecreasing in alpha and tends to e_C;
- ANY all-law vanishing-error near-minimizer sequence at ANY orders tending to infinity has only infinity-optimal weak cluster laws, with one subsequence for EVERY real shift;
- at C=V(epsilon), e_C=epsilon and its infinity minimizer is the UNIQUE ALL-law optimum mu_epsilon; the corresponding all-law near-minimizer sequences converge weakly with second moments tending to C;
- V is STRICTLY decreasing at finite positive epsilon, at the stated LAW642 compact-core/value/ALL-law-uniqueness input.

These are the exact parent-supported outputs, not newly reconstructed foundations in this note. I233's ordinary divergence/compactness proof and its additional LAW642 specialization remain distinct cuts. No finite-order uniqueness, finite-order pure privacy or rate is imported.

### II280 — independent exact-epsilon recovery theorem

`privacy-finite-joint-bin-geometric-tail-recovery-v1.md`,280LF, SHA256 `d2d7f5533574ede1dfdbe4461975272ca934af00fb9e6834a7999b02c7231e14`, at the SAME complete parent adoption but its SEPARATE independent proof gate.

Precisely imported: for EVERY finite privacy value e>0 and eta>0, a density q in its specified family G is private for EVERY shift in FULL CLOSED D and satisfies

    V(e)<=J(q)<=V(e)+eta.                                  (REC)

Its REC/VALUE proof uses LAW642 existence/finite value/canonical compact-core optimal density, NOT uniqueness. Its law-limit corollary separately uses ALL-law uniqueness. It does NOT use I233, so no cyclic branch dependency arises here.

### LAW642 — exact canonical law and original uniqueness

`privacy-all-law-optimum-self-contained-v1.md`,642LF, SHA256 `957cab2bcf3eff1860ff9f4b5a1e5838708aceaf894a97fdc2c5244c3e7d8e53`, at `RUN/privacy-all-law-self-contained-parent-v1.md`, SHA256 `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`.

For EVERY finite epsilon>0 it supplies finite positive V(epsilon), unique ALL-law optimizer mu_epsilon, and an a.e. canonical density

    f_epsilon(z)=Z^(-1)b^n_S(z), b=exp(-epsilon) in(0,1),
    n_S(z)=min{k>=0 integer:z in S+kD},

with S nonempty compact and Z positive finite. This exact compact-core geometry is used ONLY for §7's nonattainment, while ALL-law uniqueness is also used there and in the tight-budget law limit. A selected symmetric optimizer/uniqueness theorem is insufficient.

### Ordinary facts and scope

Only elementary infimum/monotonicity/squeeze arguments, Borel change of density, finite grid geometry and the extreme-value property of a continuous function on compact S are new standard tools. F_alpha<=F_infty is included in I233's divergence monotonicity. The new budget-margin, all-cofinal joint squeeze, near-minimizer transfer and nonattainment arguments are supplied completely below; they are NOT imported from a parent headline or G25's scalar program.

No new complete233/280/642 proof audit is claimed by reading the parent adoption. The current source reads for exact interfaces were II2801–120/220–280 and I2331–105, plus the actual complete parent disposition; all previously recorded source/review coverage remains unchanged.

## 2. Same concrete family and a genuinely nested finite resolution union

Recall II280's centered half-open cells for integers M,N>=1, delta=1/M:

    C_k=product_(i=1,2)[(k_i-1/2)delta,(k_i+1/2)delta),
    H_N={k in Z²:max(|k1|,|k2|)<=N},
    pi_r(0)=1-sqrt(r),
    pi_r(j)=sqrt(r)(1-r)r^(|j|-1)/2 for j!=0, 0<r<1.

Choose head masses a_k>=0, k∈H_N, and theta>=0, subject to the exact finite normalization

    sum_(k in H_N)a_k+theta(1-[1-r^(N+1/2)]²)=1.

The cellwise-constant density has mass a_k on a head cell and theta pi_r(k1)pi_r(k2) on EVERY exterior cell. Its head is genuinely JOINT, not a product of scalar heads; the infinite tails are present. All its second moments are finite as established by II280's exact COST formula.

For a positive integer n define

    G_n=UNION of those families over1<=M<=n,1<=N<=n,
        with ALL their stated r,a_k,theta parameters allowed.

Then G_n⊂G_(n+1) and union_(n>=1)G_n=G. Each G_n is a FINITE union of finite-dimensional real-parameter families; it is NOT a finite list of densities, finite-bit encoding, fixed rational parameter grid or a claimed compact set. No finite continuous-shift constraint list or executable program is inferred.

For alpha in(1,infinity] define at EXACT finite C>=0

    a_(alpha,n)(C)=inf{F_alpha(q):q in G_n, J(q)<=C},
    a_(alpha,G)(C)=inf{F_alpha(q):q in G, J(q)<=C},
    inf(empty)=infinity.

Privacy is measured by I233's ACTUAL

    F_alpha(mu)=sup_(h∈FULL CLOSED D)D_alpha(mu||tau_h mu),
    tau_h mu(A)=mu(A-h).

F_infty<=e is exactly the original event-level e privacy, using D=-D. Nothing is replaced by finitely many shifts, an endpoint-only scalar overlap rule or a pointwise RN intersection.

## 3. Exact positive cost margin: the missing step before recovery

Fix ANY finite C>0 and put e=e_C=r_infty(C)>0. By I233 choose an infinity-optimal law mu∈P_C. Then F_infty(mu)=e, so it is an actual full-D e-private law. By the ORIGINAL definition of V,

    V(e)<=J(mu)<=C.                                       (VALUE_BOUND)

Take ANY gamma>0. I233's separately supported STRICT V monotonicity gives

    V(e+gamma)<V(e)<=C,
    d_gamma=C-V(e+gamma)>0.                               (MARGIN)

Set eta=d_gamma/2>0, and apply II280's REC at privacy e+gamma, NOT at e. It supplies q_gamma∈G with

    F_infty(q_gamma)<=e+gamma,
    J(q_gamma)<=V(e+gamma)+d_gamma/2
               =C-d_gamma/2<C.                           (TIGHT_REC)

Thus the cost constraint is satisfied EXACTLY, with an actual positive margin, before any infimum limit is taken. This is not the invalid substitution `V(e)+eta<=V(e)`.

No continuity/surjectivity/inverse formula for V has been used. In particular it is unnecessary to assume V(e+gamma) tends to V(e), or that every C is V of a preselected privacy value. VALUE_BOUND and STRICT monotonicity suffice for EVERY C>0.

The finitely many discrete parameters of q_gamma have actual finite values M_gamma,N_gamma. Hence there is a finite n_gamma with q_gamma∈G_n for EVERY n>=n_gamma. For all such n and EVERY alpha>1, I233's order monotonicity gives the UNIFORM-in-alpha upper bound

    a_(alpha,n)(C)<=F_alpha(q_gamma)
                   <=F_infty(q_gamma)<=e+gamma.            (UPPER)

At alpha=infinity the same upper bound holds directly. For small n the cost-feasible family can be empty; the argument does not fabricate a minimizer there.

## 4. Every cofinal order/family value limit and the pure-family infimum

### 4.1 Full lower bound

Every q feasible for a_(alpha,n)(C) is a genuine Borel law in P_C. Therefore

    r_alpha(C)<=a_(alpha,n)(C) for EVERY alpha,n,            (LOWER)

and at alpha=infinity `e<=a_(infty,n)(C)`. No family completeness assertion is used for this direction.

### 4.2 Pure-family value at the exact budget

For ANY gamma>0, UPPER gives `a_(infty,n)(C)<=e+gamma` eventually in n, while LOWER gives>=e for every n. Thus

    lim_(n->infinity)a_(infty,n)(C)
       =a_(infty,G)(C)=e=r_infty(C).                       (PURE_INF)

The equality with the union infimum follows from nestedness and unionG_n=G. It does NOT imply a minimizer exists in any G_n or G; §7 proves nonattainment at the original optimal cost budget.

### 4.3 Joint cofinal convergence — no order requirement

Let n_j be ANY positive integers tending to infinity, and alpha_j be ANY finite real orders>1 tending to infinity. They need not be monotone or related by a chosen rate. Fix arbitrary gamma>0. For sufficiently large j, n_j>=n_gamma, so

    r_(alpha_j)(C)<=a_(alpha_j,n_j)(C)<=e+gamma.

I233 gives `r_(alpha_j)(C)->e`. Hence liminf of the middle values is>=e and limsup is<=e+gamma. Since gamma was arbitrary,

    a_(alpha_j,n_j)(C)->e                              (JOINT)

for EVERY such pair of sequences. The same reasoning applies to a cofinal net of orders/family bounds. The result is not a chosen diagonal, guessed mesh rate or presumed compact-fixed-family minimax interchange.

## 5. Both iterated value limits, with the fixed-family gap retained

For each alpha>1, nestedness makes a_(alpha,n)(C) nonincreasing in n. Its extended limit

    s_alpha=lim_(n->infinity)a_(alpha,n)(C)

exists. LOWER and UPPER give

    r_alpha(C)<=s_alpha<=e.

The upper bound follows by taking n→infinity for EVERY gamma>0, then gamma↓0. Since r_alpha(C)→e,

    lim_(alpha->infinity)lim_(n->infinity)a_(alpha,n)(C)=e.  (ITER1)

For a fixed n, divergence monotonicity makes a_(alpha,n)(C) nondecreasing in alpha. Thus its extended limit

    l_n=lim_(alpha->infinity)a_(alpha,n)(C)

also exists, possibly infinity for small n. LOWER implies l_n>=e. For n>=n_gamma, UPPER is uniform over ALL finite alpha, hence l_n<=e+gamma. Therefore

    lim_(n->infinity)lim_(alpha->infinity)a_(alpha,n)(C)=e.  (ITER2)

**Not silently proved:** `s_alpha=r_alpha(C)` at EVERY fixed finite alpha is NOT needed and is NOT claimed. Nor is `l_n=a_(infty,n)(C)` at EVERY fixed n. G_n has not been proved compact/closed under the needed weak limits; an interchange at a FIXED family cannot be assumed. ITER1/ITER2 concern the OUTER limit over the expanding union and follow from the supplied global squeeze, not those stronger fixed-parameter equalities.

## 6. ALL approximate optimizer choices and the tight-budget law limit

Take ANY cofinal sequences from JOINT, ANY errors zeta_j>=0 tending to0, and ANY laws q_j∈G_(n_j) with J(q_j)<=C and

    F_(alpha_j)(q_j)<=a_(alpha_j,n_j)(C)+zeta_j.             (APPROX)

The values are finite for all sufficiently large j by UPPER. Define, for those indices,

    eta_j=a_(alpha_j,n_j)(C)-r_(alpha_j)(C)+zeta_j>=0.

LOWER gives nonnegativity, and JOINT plus I233 gives eta_j→0. Consequently

    F_(alpha_j)(q_j)<=r_(alpha_j)(C)+eta_j.

This is EXACTLY I233 TheoremA's all-law vanishing-error premise, not a weaker family-relative heuristic. Therefore EVERY weak cluster point of q_j is an r_infty(C)-minimizer for EVERY real shift of FULL CLOSED D on the same subsequence. Weak compactness supplies cluster laws; no density/UI or h-dependent subsequence is added.

At C=V(epsilon), I233 TheoremB with LAW642 ALL-law uniqueness identifies that optimizer as mu_epsilon and gives

    q_j converges weakly to mu_epsilon,
    J(q_j)->V(epsilon).                                  (LAW_LIMIT)

The moment conclusion is not a generic consequence of weak convergence: it uses J(q_j)<=C and the limit's exact J=C to squeeze `C<=liminfJ<=limsupJ<=C`. This is the accepted tight-budget endpoint argument. It does not establish finite-order uniqueness, strong/TV/uniform-density convergence, a rate or convergence of actual solver iterates.

Existence of appropriate approximate choices for every eventually finite infimum is the definition of an infimum. No minimizer in the finite parameter family is asserted. C=0 is separate: every cell-uniform family law has J>=delta²/6>0, so every G_n∩P_0 and G∩P_0 is empty, all family infima are infinity, and I233's all-law r_alpha(0)=infinity agrees in extended values. No infinity-plus-error law selection is made.

## 7. Sharp nonattainment: no finite-bin member IS the original optimal law

### 7.1 Exact canonical quadrant tail

Fix finite epsilon>0, put b=exp(-epsilon), and take LAW642's nonempty compact S. Set

    c=max_(s∈S)(s1+s2),
    B>max(0,max_(s∈S)s1,max_(s∈S)s2).

For ANY x>B and y>B, every point s∈S lies below both coordinates, so

    dist_1((x,y),S)=min_(s∈S)[x+y-s1-s2]=x+y-c.

Since S is compact and D is the CLOSED norm ball, membership in S+kD is equivalent to dist_1(z,S)<=k. Therefore, throughout that quadrant,

    n_S(x,y)=ceil(x+y-c),
    f_epsilon(x,y)=Z^(-1)b^ceil(x+y-c).                    (DIAG_TAIL)

This is an a.e. density identity sufficient for comparison of laws; arbitrary versions on jump lines are irrelevant.

### 7.2 A diagonal jump crosses an actual exterior cell interior

Take ANY q∈G, with its actual finite M,N, delta=1/M and grid cells. Increase B, if needed, so

    B>(N+1/2)delta

as well as the compact-core coordinate bounds above. Choose a positive integer ell so large that `c+ell>2B+4delta`. The line

    x+y=c+ell

then has a nontrivial segment with both coordinates>B+delta. On that bounded segment there are only finitely many intersections with vertical or horizontal grid-boundary lines. Choose a point z0 in the segment away from those intersections. It lies in the INTERIOR of one actual grid cell C_k, and because both coordinates>B>(N+1/2)delta, that cell is outside H_N.

Choose rho>0 sufficiently small that the open coordinate square `z0+(-rho,rho)²` stays inside that cell and the quadrant, and2rho<1/2. This square is split into two positive-area open pieces by the same diagonal. On its lower side `ell-1/2<x+y-c<ell`, so DIAG_TAIL has value `Z^(-1)b^ell`. On its upper side `ell<x+y-c<ell+1/2`, so it has value `Z^(-1)b^(ell+1)`.

These two constants are DISTINCT because0<b<1 and Z>0. But q is constant a.e. on the ENTIRE cell C_k, including both pieces. Thus

    q cannot equal f_epsilon a.e.,
    mu_epsilon is NOT a member of G.                      (NOT_MEMBER)

No grid rationality of c, numerical root, generic-position assumption on S or evaluated scalar parameter is needed. The finite set of cell-boundary intersections is explicitly avoided on a positive-length segment; equality at the diagonal itself is immaterial.

### 7.3 Exact-budget, exact-privacy obstruction

If q∈G had BOTH F_infty(q)<=epsilon AND J(q)<=V(epsilon), its genuine epsilon feasibility would give J(q)>=V(epsilon). It would therefore be an original MSE optimizer, and LAW642 ALL-law uniqueness would force its LAW to equal mu_epsilon, contradicting NOT_MEMBER. Hence

    {q∈G:J(q)<=V(epsilon), F_infty(q)<=epsilon}=empty.    (NO_TIGHT_ATTAIN)

Combined with PURE_INF at C=V(epsilon), this proves

    inf_(q∈G,J<=V(epsilon))F_infty(q)=epsilon,
    but the infimum is NOT attained in G.

Every exact-cost feasible q∈G with finite F_infty therefore has F_infty(q)>epsilon, although such values approach epsilon. The constructive TIGHT_REC candidates were deliberately private at epsilon+gamma; they cannot secretly be exact epsilon-private at that tight cost. This proves the precise surviving obstruction rather than presenting relaxed privacy as exact attainment.

No POSITIVE fixed-n value gap is asserted: lack of an attaining member alone does not prove an infimum is strictly separated. No finite-alpha value/membership classification is inferred from this pure-endpoint obstruction.

## 8. Source-comparison and assurance disposition

This is a complete NEW joint-union proof candidate addressing the parent's composition limit. The correct comparison now has three distinct forms:

- II280: exact epsilon privacy, costs V(epsilon)+eta from ABOVE.
- This theorem: EXACT cost budget C, infinity privacy infimum approached from ABOVE, and all-cofinal finite-order/family VALUE convergence.
- NO_TIGHT_ATTAIN: at C=V(epsilon), no exact-epsilon finite-bin family member attains that cost.

They are compatible and must not be merged into a false exact-epsilon/exact-cost finite-family optimizer theorem. Finite-family-to-finite-alpha accuracy rates, finite continuous-diamond constraint certificates, bit complexity, actual optimizer/accountant programs, source algorithm convergence and numerical implementation remain unproved/unexercised.

Gilani2025's finite-bin/geometric-tail, scalar full-continuous-shift and alpha→infinity methodology remain positive PRIOR. Our G is the EXPLICIT JOINT extension in II280, not the source's actual scalar program relabeled planar. The registered value/core geometry/ALL-law uniqueness are imports from LAW642, not consequences of running or certifying G25's program. No new mechanism/value discovery, worldwide firstness, all-creative-corollary non-equivalence or novelty/publication significance follows. Priority remains UNCLEAR.

A fresh COMPLETE mathematics AND dependency/application audit at the explicit UNION I233+II280+LAW642 cuts is required before parent adoption. Review of I233, II280 or their parent disposition alone cannot promote this successor; the joint proof is new. K25joint457, Q26/DA26216 and square-ceiling/MS25/FMM21184 are separate unreviewed source packets, not hidden inputs here.

## 9. Execution, chronology and original round

All mathematics is exact WRITTEN symbols/fractions/integer products; **NO machine check, scientific interpreter/eval/calculator/CAS/program/enumeration/replay/solver/CLI/nested agent or new GO.** Metadata clocks/hashes/LF and ordinary source reading do not back-convert old probes, tables, arithmetic or approximate private glosses into credit.

The new proof lead and actual named-union boundary were saved BEFORE this body in checkpoint092. This same registered source/priority continuation was already authorized by Main after the actual v112-I RETURN and the separately SENT whole-primary ACK; the latest parent notification continues it. No new model, source acceptance, auxiliary work or live-review interleaving is inferred.

All firstfive owner findings, SIXTH DISTINCT v111B written-exactness finding, SEPARATE077 continuation failure, v21 category correction, strict auxiliary214STOP/UNADMITTED and every parent/reviewer/source/import/N4UNKNOWN/exit/old-arithmetic qualification remain. No clean cognition/runtime/history, continuous-activity census or stronger verification assurance. Exclusive own root only; pinned bodies unchanged. Same eighteen owners, science cutoff **2026-10-27T11:05:38-07:00**, delivery **2026-10-27T12:35:38-07:00**, active substantive actual-clock checkpoints at most30minutes. This is not early final-park or round closeout.
