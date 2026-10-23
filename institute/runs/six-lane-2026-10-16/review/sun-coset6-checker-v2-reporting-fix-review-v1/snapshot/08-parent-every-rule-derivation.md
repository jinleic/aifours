# Sun(6): independent parent derivation of the reduction and every certificate rule

Recorded at 2026-10-18T12:45:43-07:00. Written after reading rules-k6-v1/v2/v3, proof-k6-lemmas-v1, cumulative erratum-v3, the original k5 generic rule proofs and their cumulative corrections, and both whole-composition audits. This is the parent's written re-derivation, not a claim of formal verification. A final parent verdict separately binds the actual finite replay and priority disposition.

## 1. Finite reduction, prime cover and minimality

For arbitrary G with finite-index U_i, let N be the intersection of the six normal cores. Each core has finite index by the finite action on G/U_i. Thus N is normal of finite index and lies in every U_i. Each coset g_iU_i is a full preimage of its image in G/N, so subgroup indices, intersections and disjointness are preserved. It suffices to exclude finite counterexamples.

For finite G, the product formula gives |AB|=|A||B|/|A∩B|. If [G:A],[G:B] are coprime, the integer |AB|/|G| is positive and at most1, and is an integer because [G:A∩B] is divisible by their product. Hence AB=G. Since gA∩hB≠∅ iff g^−1h∈AB, disjoint cosets cannot have coprime indices.

Suppose six disjoint cosets have every pairwise gcd≤5. Each gcd is2,3,4 or5, hence involves one prime in{2,3,5}. Put A_p={i:p divides[G:U_i]}. Every pair lies in exactly one A_p; two distinct A_p meet in at most one vertex, because a shared pair would have gcd≥6. Therefore Σ_p binom(|A_p|,2)=15. If every |A_p|≤5, the only three values from{0,1,3,6,10} summing15 are6,6,3. This requires two4-subsets intersecting in at mostone point on a6-element groundset, impossible. Some prime therefore divides all six indices.

If that prime is2, all gcds are2or4; if3, all are3. Any five cosets would contradict the already accepted Sun(5) theorem. This shortcut avoids a new import of Prop4.5 here. If the prime is5, every gcd is5: write indices5r_i with pairwise coprime r_i≥1. This is the same group's Core5(6) configuration.

Choose a finite counterexample to the **full Sun(6) statement** with least group order. Every proper subgroup then satisfies Sun(6), and the same G carries Core5(6). No argument below applies Sun(6) in G. Only the FH5 six-piece fibre invokes it, in an index5 proper subgroup. Applications to at most5pieces use accepted Sun(≤5).

## 2. Basic index data and triangle rule T

For finite-index subgroups, I_ij=[G:U_i∩U_j] is divisible by lcm(n_i,n_j). Thus α_ij=I_ij/lcm(n_i,n_j) is a positive integer. The product formula gives μ(U_iU_j)=α_ij/gcd(n_i,n_j), where μ=|·|/|G|. Disjointness supplies an element outside that product, so α_ij<gcd(n_i,n_j). In Core5(6), α_ij∈{1,2,3,4} and μ(U_iU_j)=α_ij/5. Equal subgroups and r_i=1 are not excluded.

For a triangle a,b,c, the triple-intersection index is Lτ, with L=lcm(n_a,n_b,n_c)=5r_ar_br_c and integerτ≥1. Each I_xy divides Lτ, giving α_xy divides r_zτ at opposite vertexz. The product formula gives μ(U_y(U_x∩U_z))=τ/(5α_xz). Inclusion in U_yU_x∩U_yU_z boundsτ by each vertex's product of incidentα's. Hence τ must be a multiple of τ_min=lcm_e(α_e/gcd(α_e,r_opp)) and must be≤τ_max, the least vertex product. If τ_min>τ_max, no actual triangle exists. The α4 gcd needs v2(r)=1 versus≥2; α2/3 need only their respective markers. Primes≥5 cannot divideα.

These are necessary constraints, not an assertion that every admissibleτ is realizable.

## 3. Links, K and K2

If U_y(U_x∩U_z) has the same cardinality as U_yU_x, their inclusion is equality, and U_yU_x⊆U_yU_z. Taking inverses gives U_xU_y⊆U_zU_y. Thus at triangle(i,v,j), τ=α_ivα_vj supplies K's required product inclusion. A link witnessed atτ_min is sound for the actualτ: T gives actualτ≥τ_min, while its vertexv bound is≤α_ivα_vj, pinning equality.

Let S be other vertices satisfying, for each i,j∈S, U_vU_i⊆U_jU_i or the reversed alternative. The enlarged cosets g_iU_iU_v are pairwise disjoint. Indeed an intersection would put g_j^−1g_i∈U_jU_vU_i⊆U_jU_i in the first case, contradicting disjointness of g_jU_j and g_iU_i; the other case uses the inverse relation. Each enlargement is rightU_v-invariant and misses g_vU_v: an intersection would imply g_v∈g_iU_iU_v and then the original cosets intersect. Counting gives Σ_i∈S α_iv/5≤1−1/(5r_v)<1, hence the integer sum is≤4. Every K witness with sum≥5 is impossible.

If U_vU_j⊆U_vU_k, invert to U_jU_v⊆U_kU_v and apply K at vertexj to S={v,k}. This yieldsα_vj+α_kj≤4. That is K2, with the orientation used below.

## 4. Ppair and PB

Put X_j=U_vU_j,Y_j=G−X_j. The intersection X_j∩X_k is invariant under leftU_v and right(U_j∩U_k), hence a union of the corresponding double cosets. A double coset AxB has measure [G:A∩xBx^−1]/([G:A][G:B]), a positive integer multiple of1/gcd([G:A],[G:B]). Here the grid unit is u=1/(5gcd(r_v,α_jk)), since r_v is coprime to r_jr_k.

The intersection contains U_v(U_j∩U_k), and inclusion-exclusion also gives its measure≥x_j+x_k−1. Thus the lower bound is u·ceil(max(τ_min/(5α_jk),x_j+x_k−1,0)/u). Its upper bound starts at u·floor(min(x_j,x_k)/u). If equality would force a containment barred by K2, subtractu. At equal sizes both containments must hold. Consequently lo>hi is a genuine contradiction.

EveryY_j misses U_v. Bonferroni gives Σ_j∈S μ(Y_j)−Σ_jk∈S μ(Y_j∩Y_k)≤μ(⋃Y_j)≤1−μ(U_v)<1. Since μ(Y_j∩Y_k)=1−x_j−x_k+μ(X_j∩X_k), substitutinghi lowers the displayed left side. If that conservative value is≥1, PB gives a contradiction. No numerical approximation enters.

## 5. H5, fibre rules and FH5

Supposeα_ab=1 and v≠a,b hasα_va=α_vb=c. Triangle upper bounds giveτ≤c. Divisibility gives c divides r_aτ and r_bτ. For c2or3 one cofactor is coprime toc; for c4 one isodd. Thus c dividesτ andτ=c (c1 is immediate). Therefore U_v(U_a∩U_b)=U_vU_a=U_vU_b=:X, with measurec/5<1.

X is right-invariant underU_a andU_b, hence their generated subgroupW. It containsU_v and equalsU_vW. ThusW≠G. BothU_a,U_b lie inW, so[G:W] dividesgcd(5r_a,5r_b)=5, forcingindex5. AlsoU_aU_b⊆W hasmeasure1/5, soU_aU_b=W. The product formula now gives[U_v:U_v∩W]=c for every equal neighbourv, with the sameW.

For any subgroupH ofindexm, U_l's orbit on the leftH-cosets has t_l=[U_l:U_l∩H] elements,1≤t_l≤m. Its fibre subgroup hasindexλ_l=[H:U_l∩H]=n_lt_l/m. Intersecting g_lU_l with a common H-coset and translating intoH gives disjoint left cosets ofU_l∩H. Apply Sun(s) separately to each subset ofsize s. For s6 requireH<G in the minimal-counterexample frame; for s≤5 use accepted prior cases. IfU_i⊆H, U_iU_l⊆HU_l givesα_il≤t_l whenm5.

FH5 takesH=W. Verticesa,b lie insideH and havet1; v in the equal-neighbour set has prescribedt=c. Every other vertex may havet1..5. Actual coset memberships are arbitraryt-subsets of the five labels. Onlya's singleton is fixed tolabel0, by relabelling the fibre labels—not by assumingHnormal. All other vertices, includingb, retain every permitted subset. An F3 failure or a hereditary Sun failure is impossible for the actual assignment. Those failures persist as more vertices are assigned, so the checker's early pruning is sound. All seven E5 placements are considered.

## 6. RLP and hereditary L9

Translate g_v to1 and putD_j=U_vg_jU_j. IfD_j metU_vU_j, then g_j∈U_vU_j, contradicting the disjoint pair U_v,g_jU_j. HenceD_j⊆Y_j. Double-coset granularity givesμ(D_j)=q_j/5 with1≤q_j≤5−α_vj.

Every rightU_v-cosetC⊆D_j meetsg_jU_j: write a point asu_vw_j withw_j∈g_jU_j. Its piece is A_jw_j, A_j=U_v∩w_jU_jw_j^−1. Fixw0∈C; common right translation byw0^−1 and inversion turn these pieces into disjoint left cosets c_j^−1A_j inU_v, preserving theirindicesd_j=|D_j|/|U_j|=q_jr_j. Every subset of these atmost5pieces satisfies Sun at its own size. Thus every actual support is hereditary-allowed; no Sun(6) is used here.

Letμ(S) be the total normalized mass of the rightcosets with supportS. True equalities areΣ_S∋j μ(S)=q_j/5. Their total is≤1−μ(U_v)<1, becauseU_v itself lies in noD_j. Any exact nonnegativey withΣ_j∈S y_j≤1 for every allowedS givesΣ_S μ(S)≥Σ_j y_jq_j/5. A certificate withobjective≥1 contradicts that strict upper bound. Every admissibleq must have its own certificate; there is no monotonicity shortcut inq.

## 7. XE and N26

XE generalizes H5's product argument: ifU_vU_j=U_vU_k=:X, X is right-invariant underW=⟨U_j,U_k⟩ and equalsU_vW. Sinceμ(X)≤4/5,Wproper anditsindexdividesgcd(5r_j,5r_k)=5. ThereforeWindex5,U_jU_k=W andα_jk=1. No normality assumption is needed.

ForN26, v≠E2, everyα_vj=2, and neighbourα_jk∈{2,4}. Tdivisibility and oddr_v giveτ_vjk≥α_jk. ThusZ_jk=U_v(U_j∩U_k) hasmeasure≥1/5 insideX_j∩X_k. Granularity is1/5; XE excludesX_j=X_k. Sinceboth have measure2/5, theintersection isexactly1/5 andequalsZ_jk.

The repaired neighbour-triangle table is222→{2,4},224→{2,4}or{4},244→{4,8},444→{4,8,12,16}. Atmostone4-edge can be reduced by an oppositeE2, so another4 remains whenever two4-edges exist. This derives the table. No prime≥5 divides theseτ's; only12 contains3. Forv=E3 the testτ_max<3τ_min forbids exactly the problematic444triangle. Thereforegcd(r_v,τ_jkl)=1 for every neighbourtriple, includingarbitraryprimepowers,r_v1andv=E5.

PutW=U_j∩U_k∩U_l andQ=[G:U_v∩W]. Divisibility makesQ a multiple of5r_jr_k·lcm(r_lτ_jkl,r_vτ_vjk). Coprimality forcesQ≥r_v[G:W], soμ(U_vW)≥1/5. Itliesinside thethreeZ's, eachmeasure1/5; hence allthreecoincide. Neighbour-pair connectivity makesalltenZ'sequal. ThefiveX_j then consistof acommonfifth plusfivedisjointpetals eachafifth, total6/5, impossible.

## 8. RPLP

Classify each rightU_v-coset byA={j:C⊆Y_j} andS={j:C⊆D_j}. ThenS⊆A andS is hereditary-allowed. NonemptyA with emptyS **must** be included. EmptyA contributesnothingto theunionofY's andmay beomitted.

Ifτ_min(v,w,j)≥α_vwα_wj, theapexw upperbound pinsτ tothatproduct. T3atv then givesU_v(U_w∩U_j)=X_w⊆X_j, soY_j⊆Y_w. Thus the ordered implication j∈A⇒w∈A removesonlytypesofzero truemass.

For eachq the true nonnegativecolumnmassesx satisfy E1_j:Σ_j∈S x=q_j/5, E2_j:Σ_j∈A x=(5−α_vj)/5, and the two-sidedpairbounds ylo≤Σ_jk∈A x≤yhi. TotalmassΣx=μ(⋃Y_j)<1. For freea,b andnonnegativeu,l, supposeeverycolumn satisfiesΣ_S a+Σ_A b−Σ_pairs(A)u+Σ_pairs(A)l≤1. Multiplyingbyx andsumming gives

Σx ≥ Σ_j a_jq_j/5 + Σ_j b_j(5−α_vj)/5 − Σ u_jk·yhi_jk + Σ l_jk·ylo_jk.

A checkedobjective≥1 contradictsΣx<1. The sameinequalitiesvalidate a scaledinfeasibilityray, so neitheroptimizer correctnessnor LPoptimalityis assumed. Allq, orderedcontainments, columns(includingemptyS)andexactrationalentriesare re-createdbythechecker.

## 9. Universal parameter coverage and closure

Pairwisecoprimer_i allowatmostone even,one3-divisible andone5-divisible cofactor. E2's valuationclass1versus≥2, presence/coincidenceofE3, yield8typesup toS6; typedstabilizersfix eachpresentmarker. Coefficientgcds saturate at thepartner's boundedq/t valuations: atmost2forprime2,1for3and5. Class1E2 isexact. Arbitrarilylarge cofactor valuationsintroduceno furthercase. E5affectsonlyFH5;N26'sτ-tablehandlesitsapparentextra dependence.

The finite checkmustindependentlyenumerateeveryT-consistent labelledpattern, expandstabilizerorbitsfrom(type,rep), andverifyonevalidcertificateperorbit. The engine's opaque `code` label is not a typedrepresentative and is irrelevant. AllT-rejectedlabellings are impossible by§2. Label-equivariance transfers eachverifiedwitnessacrossits orbit, withallE5placementshandled. Ifallorbitsareexcluded, a least-ordercounterexample cannotcarryCore5(6). R1 saysit must; contradiction. ThusSun(6)holds in allfinitegroups, andR0 extendsit to allgroups.

**Imports/trust:** elementarygroupfacts, acceptedSun(≤5), and the actual completefinitecheckerexecution. The parent has not formalized this argument inLean. Correctness, priorityandhumanreviewremainseparate axes.
