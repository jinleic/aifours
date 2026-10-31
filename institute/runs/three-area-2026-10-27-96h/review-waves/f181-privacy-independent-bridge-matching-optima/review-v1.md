# f181 — independent bridge / matching-norm optima: same-harness review v1

Reviewer: **ReviewF181PrivacyBridge**. Native clock observed before composing this file: **2026-10-29T09:20:30-0700 PDT** (an observation, not an asserted creation time).

## Verdict and assurance boundary

**0 FATAL / 0 MAJOR / 0 MINOR mathematical findings; no target claim is INCONCLUSIVE.** This is same-harness written scientific support, not parent adoption, a human review, independent-model-family verification, a formal/kernel check, source equivalence, or novelty/priority verification. Standard analysis and geometry imports remain explicit below. A finite control is corroboration, not a substitute for the general proof.

| Target claim | F/M/m | One-sentence verdict and exact dependency |
|---|---:|---|
| Theorem 1 | 0/0/0 | **SUPPORTED:** for every finite ε>0, the all-law L and W=E‖X‖₁² minimizers exist uniquely and are P_gL and P_gJ; the packet's compactness, everywhere-private density, strict radial rearrangement, phase, gap and scalar arguments close without LAW642. |
| Corollary 2 | 0/0/0 | **SUPPORTED:** for every ℓ₁-radial private law, J=(2/3)W≥J(P_gJ), with equality only at P_gJ, using Theorem 1's W-uniqueness and the quadrant-coordinate identity. |
| Corollary 3 | 0/0/0 | **SUPPORTED, unconditional with respect to research premises:** Opt_L={P_gL}, g_L<g_J, and the strict infimum gap and all three stated rational margins follow from Theorem 1 plus independently reconstructed scalar algebra; neither a J optimizer nor LAW642 nor d67 is needed. |
| Corollary 4 | 0/0/0 | **SUPPORTED AS STATED CONDITIONALLY ON THE ADOPTED d67 DISPOSITION:** Corollary 2 upgrades d67's staircase comparison to every ℓ₁-radial private law, with a strict >10⁻⁶ margin over its feasible P_S; no MDA26 or LAW642 import is needed. |
| Proposition 5 | 0/0/0 | **SUPPORTED:** the explicit rounded-core shell is full-closed-D private and its independently recomputed cost lies in the claimed width-10⁻³³ window, proving only Claim A's LAW642-free upper half and the stated improvement over P_S. |

**W is not J in general.** The manifest's shorthand “l1-square cost W=J” is not used as an identity: the candidate correctly defines W=E‖X‖₁² and J=E‖X‖₂², and J=(2/3)W applies here only to ℓ₁-radial densities. Theorem 1 does **not** identify the all-law J minimizer. The lower half V_J>1630066277350703/10¹⁶ and the unique all-law J-optimizer/shell identification are outside this acceptance and remain conditional/unverified. Candidate §7 is an explicitly unfinished roadmap, not an accepted proof of those claims.

## Frozen input checks, actual source order, restrictions and deviations

The manifest was the first file opened and its SHA-256 matched the task: **c37601cd5423af6cc20a53ee02dd7228d6b39cd94006d930f88f5696f68ecd49** (4,126 B; subsequently independently parsed in full as JSON: 25 scalar leaves). Every input's complete hash, byte count and literal LF count was verified before mathematical interpretation; all have zero CR and a final LF.

Actual content-consumption order was:

1. `dispositions/info-1-conditional-rounded-optimum-cost-incompatibility-parent-v1.md`, complete 32 LF / 6,742 B, SHA **2e0a8019b33575781cc9e9c383d12046890821406482f24cec9e83720b1974f4**. This supplies scope, the explicit unverified LAW642 premise, and the binding C′(1)>0 endpoint correction; it is **not** imported as an unconditional optimum theorem.
2. `dispositions/info-1-ln64-nonradial-staircase-gap-parent-v1.md`, complete 59 LF / 6,805 B, SHA **d67b0ac9cbde8c6d1f81f0f407106070ea3cee640984b4d166929b12d6dd6516**. Only its corrected/adopted composite, not the original defective denominator, is the Corollary 4 premise and P_S comparison input.
3. `information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261029-independent-bridge-matching-optima-v1.md`, complete 251 LF / 20,580 B, SHA **58600f53f9e4c554566527d0800870485e4f9f97c262b5a08c9b6cd86d56dddc**. Read LF1–90 then LF91–251, before mathematics. “Candidate LF” below refers to these frozen bytes.

**Process disclosure:** the two dispositions were requested in a parallel read call and returned/consumed in the above order; likewise the two disjoint candidate ranges were requested together and returned/consumed LF1–90 then LF91–251. Thus the semantic input order and mandatory-overlays-before-mathematics rule were preserved, but retrieval calls were not sequential; this is a disclosed procedural deviation, not a later claim of strictly sequential I/O. The initial shell command listed this wave directory and used shell working-directory navigation; an initial hash/LF check used shell record counting before a second literal LF/CR count. No unlisted file contents were opened by those operations. Environment probes found Python 3.14.3 and numpy 2.4.3; sympy and scipy imports failed as unavailable; no package was installed. Pure reviewer-authored Fraction polynomial/Sturm code replaced the unavailable symbolic library. Earlier in-memory development controls ran before the frozen script execution; the reproducible one-shot receipt below is the retained bounded run, not a claim that those scratch cells were themselves frozen in advance. The write tool marked the two reviewer Python scripts executable. There were no author contacts, external models/APIs, web searches, Git commands, deletions, infrastructure changes, or writes outside this wave directory. No LAW642/MDA26 text, held f161/f162 payload, sibling review, or cited-but-unlisted mathematical source was opened/imported/executed. No unlisted skill or memory file was opened under this wave's closed-input restriction.

The displayed PASS A/B blocks are author claims; I did **not** execute or import them. I recomputed their mathematical assertions using my own exact code. There is no input certificate/result JSON other than the manifest; the retained reviewer result and receipt JSON were also fully parsed by reviewer code.

## 1. Theorem 1 — independent reconstruction (candidate LF37–100)

### 1.1 Model, nonempty feasible class, existence and positivity

Use exactly the full **closed** diamond D={h:‖h‖₁≤1}, area |D|=2, and μ(A)≤b⁻¹μ(A+h) for every Borel A and h∈D. Symmetry of D also gives the reversed translate comparison. The product-Laplace density (ε²/4)exp(−ε‖x‖₁) is feasible by |‖x+h‖₁−‖x‖₁|≤1, with finite L and W. A bounded-cost minimizing sequence is tight because μ_n{‖x‖₁>R}≤C/φ(R) and φ(R)→∞. Prokhorov gives a weak subsequential limit. For each fixed h, the inequality on every nonnegative bounded continuous test f passes to the limit since f(·−h) is again bounded continuous. Approximate closed-set indicators by continuous functions and use finite-measure regularity/inner regularity to extend the domination to all Borel sets. This works for each h separately; no countability reduction of D is needed. Bounded-continuous truncations min(φ(‖x‖₁),R) establish lower semicontinuity and attain the infimum. Positivity v=V_φ>0 follows too: an attained zero value would be a point mass at 0, incompatible with the absolute continuity proved next.

### 1.2 Everywhere-defined private density, not an a.e.-only ratio argument

For Borel A, Tonelli gives ∫_Dμ(A+h)dh=∫|D∩(x−A)|dμ(x)≤|A|. Integrating privacy therefore gives 2μ(A)≤b⁻¹|A|. Radon–Nikodym supplies a density ≤1/(2b) a.e. For rational r>0, x↦μ(B_r(x)) is Borel (indeed lower semicontinuous), so the rational-radius limsup defines a Borel f, bounded everywhere by 1/(2b), with f=dμ/dx a.e. by Lebesgue differentiation. The **same fixed ball-radius inequality** holds for every x,h; taking limsup preserves it and gives f(x+h)≥bf(x) everywhere. This avoids an invalid simultaneous selection over uncountably many a.e. exceptional shift sets.

### 1.3 Brunn–Minkowski rearrangement, full-D privacy and strictness

For A_s={f>s}, |A_s|≤1/s, R(s)=√(|A_s|/2) is nonincreasing and right-continuous by continuity from below of superlevel sets as the threshold decreases. Pointwise privacy gives A_s+D⊆A_bs. Apply planar Brunn–Minkowski to a positive-area compact C⊆A_s: |C+D|¹ᐟ²≥|C|¹ᐟ²+√2. Approximate |A_s| from below by such compact sets, obtaining R(bs)≥R(s)+1 when R(s)>0. This uses only the compact-set inequality and Lebesgue inner regularity, not measurability of an arbitrary noncompact sumset.

For p=f#=sup{s>0:‖x‖₁<R(s)}, right-continuity gives the exact level-set equality {p>s}=R(s)D°. Thus p is Borel, equimeasurable with f, and has integral 1. If ‖y−x‖₁≤1 and ‖x‖₁<R(s), then ‖y‖₁<R(s)+1≤R(bs), so p(y)>bs. Taking suprema gives p(y)≥bp(x) at every pair, hence its law is in F even for boundary shifts in closed D.

For |A|=|RD|, split A and RD into their symmetric difference. Outside RD, φ(‖x‖₁)>φ(R); inside it, φ(‖x‖₁)≤φ(R), with equality on the boundary only on a null set. The equal measures of the two difference pieces imply ∫_Aφ≥∫_RDφ, strictly if the symmetric difference has positive measure (the case of infinite outside integral is harmless). Layer cake/Tonelli then gives C_φ(p)≤C_φ(f). For finite equal costs, the nonnegative layer differences vanish for a.e. s, so A_s agrees with R(s)D a.e.; integrating level-set symmetric differences yields f=p a.e. Consequently every minimizer is already this radially nonincreasing, everywhere-private density. This is the load-bearing **strict** rearrangement argument; no all-law optimizer theorem is assumed.

### 1.4 Phase identity and almost-everywhere phase optimality

M=p(0)=sup{s:R(s)>0} is positive and ≤1/(2b). For a∈[bM,M), R_i=R(ab^i)>0 and R_i≥R_0+i→∞, so n_a(x) is finite. These facts also imply p(x)>0 for every finite x. The index changes by at most one under a D-shift, so u_a=b^{n_a} is everywhere-private. All functions are jointly measurable because R is monotone and {n_a≤i}={‖x‖₁<R(ab^i)}.

Fix y=p(x)=Mb^κ, κ≥0, and a=Mb^σ, σ∈(0,1]. Since {p>s}={‖x‖₁<R(s)}, n_a is the least n≥0 with σ+n>κ. The map σ↦σ+n_a is a piecewise integer translation, a measure-preserving bijection onto (κ,κ+1]. Changing variables gives **∫_{bM}^M u_a(x)da=(1−b)y**, including y=M. Nonnegative layer summation gives Z_a=(1−b)Σ_i b^i·2R_i² and N_a=(1−b)Σ_i b^iΦ(R_i). Tonelli plus the identity yields ∫Z_a da=1−b and ∫N_a da=(1−b)C_φ(μ)<∞. Thus Z_a,N_a are finite a.e.; Z_a>0 there. With w(a)=Z_a/(1−b), μ=∫w(a)(u_a/Z_a)da and costs decompose with exactly the same weights. Because every normalized phase is feasible and has cost ≥V_φ, equality of the weighted average forces phase cost V_φ for almost every a. No cancellation of signed/infinite costs is used.

### 1.5 Gap lemma, convergence and admissible perturbations

For any admissible radial phase let H(R)=Φ(R)−2vR², v=V_φ. The weighted sum Σ_i b^iH(R_i) is absolutely convergent since Σ_i b^iΦ(R_i) and Σ_i b^iR_i² are finite, and equals (N−vZ)/(1−b). It is 0 at an optimal phase, ≥0 at every feasible phase. Exact differentiation gives H′(R)=4R(φ(R)−v); H strictly decreases to ρ_v=φ⁻¹(v), then strictly increases.

If gap d=R_{i+1}−R_i>1 and R_{i+1}>ρ_v, choose 0<δ<min(d−1,R_{i+1}−ρ_v). Lower every R_j for j≥i+1 by δ. All gaps remain ≥1, R_0 stays positive, finite costs remain finite, and every modified H term decreases strictly. Absolute convergence justifies summing the decreases, so the new weighted sum is <0, impossible. If R_{i+1}≤ρ_v, then R_i<ρ_v; choose 0<δ<min(d−1,ρ_v−R_i) and raise the finitely many R_0,…,R_i. Their H terms strictly decrease, admissibility and finiteness persist, and again the sum is negative. Thus **every gap is exactly 1**, and every optimal phase is a P_t with t=R_0>0. No assumption that arbitrary radial phases were convex-core shells was introduced.

### 1.6 Scalar roots, endpoints and uniqueness of the law

The independent geometric moments come from E[N^(r)]=r!m^r and Stirling expansion, giving the candidate's T1–T4. Radial integration gives |RD|=2R², Φ₁(R)=4R³/3 and Φ₂(R)=R⁴. Hence C₁(P_t)=2M3/(3M2), C₂(P_t)=M4/(2M2). My exact polynomial class verifies M3′M2−M3M2′=Q and M4′M2−M4M2′=2P as identities in (g,m), not just at selected m.

For all m>0, Q has coefficient signs +,+,+,−,+, exactly two changes; P has +,+,+,(either sign or zero),−,+, again exactly two changes. Endpoint evaluations are the positive values printed at candidate LF92. With x=g+m, v=m(m+1), τ=1+2m and τ²=1+4v, g0=√v−m lies in (0,1); at x=√v the exact expressions are Q=2v³ᐟ²(2√v−τ)<0 and P=−v³ᐟ²<0. IVT gives one root on either side of g0 inside (0,1); Descartes' multiplicity bound 2 makes them the only positive roots, both simple. Derivative signs are therefore +,−,+ on the three intervals.

The unnormalized g=0 density equals b times the g=1 density except at a null boundary set; M2(0)=bM2(1), so **P₀=P₁ as laws**. The larger root g_φ is <1 and C is strictly increasing on (g_φ,∞), in particular **C′(1)>0**. Therefore C(0)=C(1)>C(g_φ), excluding both equal endpoint laws; C′(0)>0 alone would not suffice. The sign pattern also excludes every other t>0. Every optimal phase is consequently the same P_gφ. Mixing equal laws and ∫w=1 proves the claimed **all-law uniqueness**, not merely a unique scalar parameter. No LAW642 or MDA26 statement is used anywhere in this chain.

## 2. Corollaries 2–4 and exact PASS A margins (candidate LF104–120, §9A)

**Corollary 2:** in each quadrant x=(ru,r(1−u)), Jacobian |det|=r. A radial density factors in r and u, so u is uniform on [0,1] independently of r; ∫₀¹[u²+(1−u)²]du=2/3. Thus J=(2/3)W, including the extended-value case. Theorem 1's W-optimum and uniqueness give the bound and equality case. This does not rearrange J over all laws; it applies only to the radial subclass.

**Corollary 3:** independently multiplying gives P=xQ+vR for R=2x³−(1+6v)x+2vτ, and xR+Q=3(x²−v)²−x². At the larger Q root, x_L>√v, z=x_L²/v>1. Squaring the Q-root relation gives v(z²+3)²=4(1+4v)z. Subtracting 12v(z−1)² and using (z²+3)²−16z−12(z−1)²=(z−1)³(z+3) gives 1/v−3(z−1)²/z=(z−1)³(z+3)/(4z)>0. Hence R<0 and P(g_L)<0, so g_L lies between P's roots, in particular g_L<g_J. Because g_J is the unique scalar J(P_g) minimizer, J(P_gL)>J(P_gJ)≥V_J. Theorem 1 gives Opt_L={P_gL}; the restricted J-infimum is an ordinary single finite value, so no restricted-infimum compactness argument or all-law J-optimizer premise is needed. This makes disposition 1's Claim B **unconditional relative to all research-theorem premises**.

For each PASS A instance my own exact code checked the signs, interval ordering, and, additionally, Sturm counts showing the intervals enclose the **larger** roots and no root lies farther right. Because every moment polynomial involved has positive coefficients for g>0, the certified lower bound is exactly

`B = M4(aL)/(3 M2(zL)) − M4(zJ)/(3 M2(aJ)) < J(P_gL)−J(P_gJ)`.

The receipt stores each B as a full exact rational and the exact positive surplus over its requested margin (entries S8); the following decimals are only readable summaries:

| ε | exact requested threshold | independently recomputed B, truncated | true staircase gap, rigorously outward-rounded interval |
|---|---:|---:|---|
| ln 64 | 37/5000 | 0.007441574150253566704392954317 | (0.007441574225515253102757632654, 0.007441574225515253102757632655) |
| ln 32 | 3/500 | 0.006238701177531634492856681226 | (0.006238701177531844339129819242, 0.006238701177531844339129819243) |
| ln 2 | 1/10000 | 0.000143879915280667215408270654 | (0.000143879915280667216560095824, 0.000143879915280667216560095825) |

All strict comparisons hold in exact rational arithmetic. These are strict **lower bounds**, not an assertion that the all-law gap to V_J equals a displayed threshold or equals the staircase gap. No uniform-in-ε constant is claimed.

**Corollary 4:** conditional on the adopted corrected d67 law/cost/feasibility result, use g_J∈(0,1) in its universal staircase comparison. Corollary 2 then gives every radial μ: J(μ)≥J(P_gJ)>J(P_S)+10⁻⁶≥V_J+10⁻⁶. I independently recomputed J(P_S) from the d67 formula and recovered exactly its displayed fraction, about 0.163006872914058237776525884090156365975451804; also its corrected lower-bound fraction equals M4(a)/(3M2(z))−J(P_S) and is >0.0000019549817155603350799>10⁻⁶. This is arithmetic corroboration of the adopted d67 input, not a rereview of its unlisted original packet or reviews. Its old denominator error is not reimported. The MDA26 optional premise that d67 declined to admit is **not** needed because Corollary 2 now supplies the radial step directly.

As a separate consequence (not needed to dispose the stated P_S comparison), Proposition 5 plus Corollary 2 also rule out radial J-optima using P_K: my exact bound `M4(aJ)/(3M2(zJ))−J(P_K)>0.000002200160703450217419881552>10⁻⁶` supplies a d67-free alternative comparator. This does not identify V_J.

## 3. Proposition 5 / PASS B — independent geometry and exact cost (candidate LF126–159, §9B)

### 3.1 Core, octant geometry, distance and privacy

At the given m,t,c, 0<c<t and Y=2t−c+m>c>0. With A=Y²+c², F(c)=Y−m=2t−c, F(t)=t. The arc derivative −y/√(A−y²) decreases to −c/Y=−z>−1, and the line derivative is −1. Thus F is nonincreasing, ≥t≥y, and F(y)+y is nondecreasing to 2t.

An independent useful description of the full core is the convex intersection

`|x₁|+|x₂|≤2t`, `( |x₁|+m )²+x₂²≤A`, and `x₁²+( |x₂|+m )²≤A`.

In octant x₁≥x₂≥0 the circular constraint `(|x₁|+m)²+x₂²≤A` is the tighter of the two, and the line/circle crossing polynomial `(2t−y+m)²+y²−A` has roots c and 2t+m−c>t. Thus the minimum boundary is exactly the claimed arc on [0,c] and line on [c,t]. This verifies the D4-orbit definition and the quadrant down-set property, including across the diagonal. Convexity is not required for distance-Lipschitz privacy, but this description also justifies the independent geometric calculation below.

For x∈Q1, fold a candidate closest k by axis reflections and then replace it by min(k,x) coordinatewise. Down-set closure retains membership in K; the distance cannot increase. Therefore d₁(x,K)=x₁+x₂−max{k₁+k₂:k∈K∩Q1,k≤x}. In octant 1 with x₂≤t, if x₁≤F(x₂) the point is inside. Otherwise the witness (F(x₂),x₂) achieves sum F(x₂)+x₂. For any competing k in octant 1, k₂≤x₂ and monotonicity of F(y)+y bounds its sum by this witness; in octant 2 its sum≤2x₂≤F(x₂)+x₂. For x₂>t, all sums are ≤2t and the witness (t,t)≤x achieves 2t. This proves both stated distance branches, not just a sampled approximation.

Distance to a nonempty compact set is 1-Lipschitz in ‖·‖₁. If ‖h‖₁≤1, ceiling(d₁(x+h,K)) differs from ceiling(d₁(x,K)) by at most 1, including integer-distance and closed-D boundary cases. Thus the Borel shell density ratio is between b and b⁻¹ everywhere, and integration proves privacy for all Borel events. Positive finite normalization follows from the computed area polynomial and geometric decay. No assumed optimizer, shell theorem, branch equation or screen sufficiency is used; even if the rational parameters were motivated elsewhere, their construction and cost here stand on their own.

### 3.2 All layers and an independent polygon/arc computation

K_k=K+kD={d₁≤k}. In octant 1 the distance formula gives y≤x≤F(y)+k for 0≤y≤t, and y≤x≤2t+k−y for t≤y≤t+k/2. Direct polynomial integration verifies the tail area k²/4 and polar second moment k⁴/12+tk³/3+t²k²/2 exactly. The geometric layer identity b^{ceil d}=(1−b)Σ_{k≥0}b^k1_{K_k} is pointwise, so Z_K=E|K_N| and N_K=E∫_{K_N}|x|²dx, including every layer.

For an independent computation distinct from the candidate's slice expansion, I decomposed the octant region as the CCW polygon with vertices

`O`, `P0=(√A−m+k,0)`, `P1=(2t−c+k,c)`, `P2=(t+k/2,t+k/2)`,

plus the circular segment of radius √A centred at C=(k−m,0), angle θ from (√A,0) to (Y,c). Shoelace/polygon polar-moment formulas give the polygon terms. For the segment, subtract triangle (C,P0,P1) from the sector: sector area Aθ/2, polar moment about C A²θ/4, x-first moment Ac/3. Shift its polar moment to the origin using `I_O=I_C+2C_x·M_x+|C|²·area`. My arithmetic works in Q(√A)+Q(√A)θ and verifies exact cancellation of every √A coefficient. The resulting area and moment are polynomials of degree 2 and 4 in k. Newton forward differences plus E[binom(N,j)]=m^j sum them exactly, separately reproducing Z_K and N_K. Their expressions agree **exactly** with the candidate's written §6.3 formula, implemented independently only as a cross-check. In particular |K_k|=|K|+8tk+2k² agrees with mixed-area geometry.

Independently differentiating the two arc antiderivatives gives the integrands √(A−y²) and y²√(A−y²). At c, √(A−c²)=Y>0, so θ=asin(c/√A)=atan(c/Y) with the correct principal branch. All other integral contributions are polynomials. Hence Z_K,N_K are affine rational functions of θ and J=N_K/Z_K is a linear-fractional function, monotone (or constant) on the interval where Z_K>0. Bounding both endpoint ratios is therefore legitimate; no unproved monotonicity sign is needed.

### 3.3 Exact window and margins

I enclosed θ using **both** 40-term positive Euler-series bounds (geometric tail bound) and a separate 40-term alternating Taylor enclosure, intersected as rational intervals. Their intersection is nonempty; Z_K is positive at both endpoints and hence throughout. The result is the following rigorously outward-rounded readable interval:

`0.16300662773507034789418590534579810978603937876852 < J(P_K) < 0.16300662773507034789418590534579810978603937876853`.

In particular, the candidate's exact rational assertions both hold:

`163006627735070347894185905345798/10^33 < J(P_K) < 163006627735070347894185905345799/10^33`,

`339888889366/10^12 < Z_K < 339888889367/10^12`.

Z_K≈0.339888889366123362692915412082. J lies just **1.09786039378…×10⁻³⁴ above** the lower J-window endpoint, so this is a genuinely nontrivial two-sided check, not only the easier upper-half check. The verified cost improvement is `J(P_S)−J(P_K)>0.000000245178987889882339978744>24/10^8`. The exact upper endpoint is below 1630066277350704/10¹⁶, so feasibility alone gives `V_J≤J(P_K)<1630066277350704/10^16`. Neither this upper bound nor its cost window proves J-optimality or a lower bound for arbitrary laws. The printed five-decimal theta-width field in the control JSON is a truncated **0.00000**, not an assertion of zero width; the positive rational interval comparison is the actual check. Likewise per-check decimal strings are summaries; the `values` enclosures use outward rounding.

The separately labelled float quadrature diagnostic used 91 geometric layers and 48-node Gauss–Legendre integration per piece: Z≈0.3398888893661233 and J≈0.1630066277350703, consistent to <10⁻¹³ with the exact computation. The distance formula agreed with brute-force boundary minimization on 600 points within 1.81×10⁻⁶, and 20,000 sampled full-D shifts passed the Lipschitz/index diagnostic. These floats/samples do **not** certify the general geometry or privacy; the preceding proofs do.

## 4. Independently authored bounded controls and receipts

Retained run: `python3 reviewer-run-controls-v1.py`, Python 3.14.3. The runner enforces a 120-second subprocess timeout and exclusive-create outputs; the script also sets a 110-second alarm. Actual start/end **2026-10-29T09:19:45−07:00**, elapsed **0.589 s** at the runner (script 0.527 s), exit **0**, no timeout, empty stderr. A cap would be UNKNOWN, not acceptance; none occurred. **67 positive checks, 13 intended-reason negative controls, 8 labelled float diagnostics, zero failures.** The numbers count named checks; the general proofs above do not infer a universal theorem from sampled m-values or random phases.

Exact controls cover moments and binomial moments; formal sparse-polynomial identities; direct staircase layer sums; diamond moment/radial-factor integration; H′; Descartes/Sturm root controls for 16 rational m-values; all three PASS A selectors, brackets and margins; d67's corrected fractions; full polygon/segment moment reconstruction; exact PASS B angle/window/normalizer/improvement checks; and 1,200 random admissible radial-phase cost comparisons plus a scalar t-grid as finite consistency checks.

All 13 negative cases rejected for the intended reason, not a crash: inflated PASS A margin (`LB<=margin`); bracket around the smaller Q root (`+ to −` crossing); bracket shifted past g_L (`Q(a)>=0`); T2=m+m² mutation (`identity mismatch`); J-window shifted upward 10⁻³³ (`J below window`); θ:=z (`J below window`); doubled tail-area coefficient (`formula mismatch (Z)`); incorrect arc-I1 sign (`formula mismatch (N)`); m:=b (`J below window`); omitting the circular segment (`√A part nonzero`); overlarge claimed improvement (`improvement<=threshold`); d67 a:=z (`JPS mismatch`); and a half-spacing radial construction which has lower apparent L but is inadmissible (`gap<1`). A separate float no-m distance mutation also failed as intended; it is counted among diagnostics, not the 13 exact negative cases.

| Retained artifact | SHA-256 |
|---|---|
| `reviewer-controls-v1.py` | `383a83ba849c789e6cb9b857d4f24a79305e9b01b6b7104bec037f35d1307e01` |
| `reviewer-run-controls-v1.py` | `5b017573c6671172cf1fa2a5f9d60c7456fb9c1b46904b609e387b68c65324f1` |
| `reviewer-controls-v1-result.json` | `8d51ddfe15dff56cc4464b7e871f709a19a10e92b34df407755bf08ee5fb6118` |
| `reviewer-controls-v1-receipt.json` | `02437d7a28e1ddc723fbd45b6fb10a34ffe89a4c03453ba9861a8496d41840b9` |
| `reviewer-controls-v1-stdout.txt` | `d4850b83a5cc54c0c62b38581dc4bd46e77de42bf3b64955c6de5e5a42722dfb` |
| `reviewer-controls-v1-stderr.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

## 5. Imports and final disposition boundary

Explicit standard imports are Radon–Nikodym, Lebesgue differentiation, Tonelli/layer cake and monotone convergence; Lebesgue/finite-Borel measure regularity; planar compact-set Brunn–Minkowski; Prokhorov weak compactness and lower semicontinuity; the fixed-volume strictly increasing radial-cost bathtub comparison; elementary calculus/geometry and polygon moment formulas; IVT and Descartes' rule (with Sturm used additionally for finite controls); geometric-series moments, Newton polynomial expansion, and convergent arctangent-series tail bounds.

Theorem 1 and Corollaries 2–3 have **no conditional research theorem import**. Corollary 4 imports only the **adopted corrected d67 statement**, exactly as scoped, plus Corollary 2. Proposition 5's feasible-law upper bound has **no LAW642 import**; its P_S improvement comparison uses the d67 constant (independently recomputed from the formula in the supplied disposition). No step silently requires LAW642. Named/unlisted source-theorem ancestry, the author's execution history, earlier-file corrections beyond the supplied adopted disposition, and any claim of priority/source equivalence were not authenticated. Conditional LAW642 premises in disposition 1 remain explicit assumptions rather than promoted evidence. Final scope: accept the five statements only at the same-harness written/finite-control assurance level stated here; do not promote them to an all-law J-optimum identification or Claim A's lower half.
