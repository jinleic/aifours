# f278 written-mathematics review v1

## 1. Verdict and scope

**FATAL: 0. MAJOR: 0. MINOR: 0.** No mathematical defect was found in the frozen interval theorem or its stated composition with the adopted reductions. The theorem is **SUPPORTED**, with the f261 structural theorem and f273 attained variational reduction retained as explicitly conditional imports, not independently reproved here. This is a review result, not a parent adoption decision.

For every finite epsilon in `[sqrt(2), log(123/23)]`, the written argument establishes `1/2 < V <= 2`, and consequently the actual-V cutoff `ceil(sqrt(2V))` equals 2. The interval has strictly separated endpoints. The conclusion does not establish that optimal levels cannot become coherent earlier, exclude diagonal/one-core optimal laws, locate the scalar minimizer, or establish scalar-pair uniqueness.

The separate, expressly unreviewed checkpoint observation at manuscript LF 69 and the historical word “first” at LF 21 are not certified by this review. They are not premises of the interval theorem. Owner-script PASS A/E is NON-EVIDENCE throughout.

## 2. Frozen identities and complete-read boundary

Identifiers below denote only these exact files:

- **M:** assigned wave directory `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f278-privacy-cutoff-two-regime-existence/manifest-v1.json`.
- **S:** `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261029-cutoff-two-regime-exists-v1.md`.
- **I261:** `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-1-privacy-all-epsilon-optimizer-complementarity-finite-tail-parent-v1.md`.
- **IN1:** `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-1-privacy-n1-completed-parent-read-prospective-acceptance-v1.json`.
- **I273:** `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-1-privacy-n2-coupled-complementarity-variational-reduction-parent-v1.md`.

| ID | Observed SHA-256 | Bytes | LF | Match |
|---|---|---:|---:|---|
| M | a51f154f65030799cb5146535536f9799e1e43ccdbd6a879d36ff33a16268958 | 4237 | 50 | All three match assignment |
| S | a626eb6994d6a98ac1b9585fc5a2e42dcb34026fa104979e01e8681ea849a726 | 6080 | 73 | All three match M |
| I261 | 28335b2def1139d4141a3f62a74ef0f0063f57f2f7500d41d065466267381c97 | 8487 | 44 | All three match M |
| IN1 | 9065e9cdbaaac3925ace542b0e35a3b2ff5afb0ff11bfb9c8291d98cc90d4a3f | 7698 | 111 | All three match M |
| I273 | 51502ed65a16c5fe43da2416ee7e2365dbc1df306d388c9b01dec966012d067c | 4394 | 16 | All three match M |

M was hashed and counted before its body was opened. All four scientific files were hashed and counted before S was opened. Bodies were subsequently displayed in the mandatory order S, I261, IN1, I273. Every declared display, including each actual ending, was complete before mathematical consideration, mathematical note-taking, or comparison of scientific inputs began. The observation `2026-10-30T03:21:38Z` was taken after the final I273 window and marks the start of mathematical reconstruction, not an inferred earlier completion time.

No file referenced inside these inputs was followed unless it was itself one of the manifest-listed files above. In particular, the referenced author scripts, underlying f261/f273 manuscripts and corrections, prior reviews, and checkpoint 018 were not opened.

## 3. Reviewer reconstruction of the load-bearing argument

### 3.1 Full-class projection and integer translates — S LF 27–29

Write `b=exp(-epsilon)`, with `0<b<1`. For either coordinate marginal nu, pull a Borel subset B of the line back to its coordinate cylinder in R². A shift by `h e_j`, `|h|<=1`, belongs to the full closed l1 unit ball. Thus the marginal satisfies `nu(B+h) >= b nu(B)`; this uses neither independence nor a density assumption.

Let `A=(-1/2,1/2)`. Iterating the shifts +1 or -1 gives `nu(A+k) >= b^|k| nu(A)` for every integer k. The open translates are pairwise disjoint. Their omitted endpoints cause no problem: their total mass is at most 1, which is the required direction. Consequently

`1 >= nu(A) sum_(k in Z) b^|k| = nu(A) (1+b)/(1-b)`.

Hence `p(1/2):=nu({|X|>=1/2}) = 1-nu(A) >= C`, where `C=2b/(1+b)`. This remains valid for marginals with atoms at the half-integer endpoints.

### 3.2 Outward tails and the shell integral — S LF 31–33

For r>0, the half-lines `[r,infinity)` and `(-infinity,-r]` are disjoint. Apply privacy with the outward shifts +1 and -1 respectively and add. Their translates are exactly the two tails at r+1, so

`p(r+1) >= b p(r)`.

Induction yields `p(k+1/2) >= b^k C` for k>=0. Since p is nonincreasing, `p(r)>=C` on `[0,1/2]` and `p(r)>=b^k C` on `[k-1/2,k+1/2]`, k>=1, apart from irrelevant shared integration endpoints.

Tonelli applied to `X² = integral_0^infinity 2r 1_{r<=|X|} dr` gives the layer-cake identity even when the second moment is infinite. The inclusive tail convention changes no integral. The initial integral is 1/4, and the kth shell integral is

`(k+1/2)²-(k-1/2)²=2k`.

Therefore

`E X² >= C [1/4 + 2 sum_(k>=1) k b^k] = C [1/4 + 2b/(1-b)²]`.

For completeness, the series identity follows by writing `k=sum_(j=1)^k 1`, interchanging nonnegative sums, and summing the geometric tails. No unlicensed differentiation or convergence assumption is needed.

### 3.3 Adding coordinates and changing variables — S LF 35–39

The bound applies separately to both marginals. Adding their moments, without independence, gives every feasible law the lower bound

`J >= b/(1+b) + 8b²/[(1+b)(1-b)²]`.

Substitute `b=m/(1+m)` and `1-b=1/(1+m)`. The two terms become `m/(1+2m)` and `8m²(1+m)/(1+2m)`. Thus

`V >= L(m) = (m+8m²+8m³)/(1+2m)`

for all b in (0,1). Passing to the infimum preserves the same lower bound. This derivation does not import the narrower ancestral m>=2 statement.

### 3.4 Cubic threshold and epsilon implication — S LF 43–51

For m>0 the denominator `1+2m` is positive, and direct subtraction gives

`L(m)-1/2 = [16m³+16m²-1]/[2(1+2m)]`.

Therefore the stated equivalence is exact. With `p(m)=16m³+16m²-1`, one has `p(0)=-1` and `p'(m)=48m²+32m>0` for m>0. The reviewer’s rational arithmetic is:

- `p(11/50)=(21296+96800-125000)/125000=-863/15625<0`;
- `p(23/100)=(194672+846400-1000000)/1000000=2567/62500>0`.

Continuity and strict monotonicity give existence and uniqueness of the positive root and its strict bracket `(11/50,23/100)`.

For epsilon>0, `m=1/(exp(epsilon)-1)`. If `epsilon<=log(123/23)`, then `0<exp(epsilon)-1<=100/23`, so `m>=23/100`. Accordingly `p(m)>=2567/62500>0`, and `V>=L(m)>1/2`. The strict lower bound survives the closed epsilon endpoint.

### 3.5 Laplace witness and upper endpoint equality — S LF 25

The density factors as the product of two normalized one-dimensional densities `(epsilon/2) exp(-epsilon|x_j|)`. For every h in D, the triangle inequality gives

`f(x) <= exp(epsilon ||h||_1) f(x+h) <= exp(epsilon) f(x+h)`.

Integrating over an arbitrary Borel event proves the required full-class privacy inequality, in the correct direction. Each coordinate second moment is

`epsilon integral_0^infinity t² exp(-epsilon t) dt = 2/epsilon²`,

by two integrations by parts. Thus `J=4/epsilon²` and `V<=4/epsilon²`. This also reconstructs directly the witness imported in I261 LF 11 and 23. When `epsilon>=sqrt(2)`, this upper bound is at most 2, including equality at the lower epsilon endpoint.

### 3.6 Nonemptiness: exact exponential-series certificate — S LF 55–59

Set `x=1415/1000=283/200`. The manuscript’s square comparison is exact:

`x²=2002225/1000000>2`,

so `sqrt(2)<x`. Let `t_k=x^k/k!`. For every j>=0,

`t_(14+j) <= t_14 (x/14)^j`,

because all the subsequent factorial denominators are at least 14 at each step. Since `0<x<14`, summing this geometric majorant proves the displayed bound

`exp(x) <= R := sum_(k=0)^13 t_k + t_14/(1-x/14)`.

Here is a reviewer-owned written rational certificate for the remaining comparison, independent of the owner’s Fraction run. Since `x<3/2`, put `r=3/10`. For k>=4, `t_(k+1)/t_k=x/(k+1)<=r`, and also `x/14<r`. Therefore

`sum_(k=4)^13 t_k + t_14/(1-x/14) <= t_4 [sum_(j=0)^9 r^j + r^10/(1-r)] = t_4/(1-r)`.

Bounding the first four terms and t_4 at 3/2 yields

`R <= 1+3/2+9/8+9/16 + (27/128)/(7/10) = 67/16+135/448 = 2011/448`.

Finally,

`123/23 - 2011/448 = (55104-46253)/10304 = 8851/10304 > 0`.

This proves the manuscript’s exact series comparison, not merely a numerical approximation to the exponential. Monotonicity now gives `exp(sqrt(2))<exp(x)<123/23`, hence `sqrt(2)<log(123/23)`. The interval is nonempty and has positive length.

### 3.7 Cutoff and conditional f273 composition — S LF 21, 63 and 73

The two inequalities give `1<sqrt(2V)<=2`, hence `ceil(sqrt(2V))=2`. Both boundaries are handled: the lower V inequality is strict; the upper V inequality may be equality.

I261 LF 17–19 supplies the eventual-coherence cutoff and attained finite-profile formulation for the same full-class problem. The value-dependent cutoff is the relevant one here. It is not inferred from, or confused with, the coarser uniform Laplace cutoff in I261 LF 17.

I273 LF 5 explicitly retains the full standing hypothesis `1/2<V<=2`; LF 9 adopts the attained implicit reduction `V=min_(a>=0,c>=a+1/2) rho(a,c)` under that hypothesis, conditional on f261. Our independently reconstructed interval bounds verify both parts of the hypothesis. There is no epsilon restriction or other stated dependency in that imported reduction left unchecked by this composition. The definitions and fixed-box theory behind rho are imported at that stated scope, not newly reconstructed from absent source bodies.

The composition does not import I273’s rejected zero-derivative characterization, unsupported corner/kink stationarity, or scalar-pair uniqueness. I273 LF 12 expressly excludes those claims. In particular, a diagonal minimizing pair remains possible: the conclusion that the actual-V cutoff is 2 is not a proof that no optimal law has a one-core representation.

IN1 LF 17–18 and 38 is consistent conditional context, not a premise of the new lower bound. Its sufficient N=1 region is not reversed into a converse. Neither epsilon below its threshold nor failure of a particular trial would by itself prove `V>1/2`; the marginal argument above supplies that proof here.

## 4. LF-located findings and per-claim dispositions

**Findings: none within the frozen theorem scope.** There is no FATAL, MAJOR, or MINOR correction to request. The exact quotations below locate the tested claims; they are audit anchors, not manufactured findings.

| Claim and exact source anchor | Disposition | Grounds and boundary |
|---|---|---|
| S LF 27–29: “P(X∈A) <= (1-b)/(1+b)” | SUPPORTED | Full-class cylinder projection, integer-shift iteration, disjoint open translates; atoms do not invalidate the bound. |
| S LF 31–33: “p(r+1)>=b p(r)” and the displayed shell lower bound | SUPPORTED | Outward half-line shifts plus monotonicity; shell weights and layer cake reconstructed in §3.2. |
| S LF 37–39: “V >= L(m)=(m+8m²+8m³)/(1+2m)” and “ALL b∈(0,1)” | SUPPORTED | Independent coordinate addition and exact variable conversion; no m>=2 restriction used. |
| S LF 43: “L(m)>1/2” iff “p(m)=16m³+16m²-1>0” | SUPPORTED | Positive denominator and exact subtraction. |
| S LF 45–49: “p(11/50) = -863/15625” and “p(23/100) = 2567/62500” | SUPPORTED | Written rational evaluation and strict derivative give the unique positive-root bracket. |
| S LF 51: “ε <= log(123/23)  ⟹  m >= 23/100” | SUPPORTED | Exact inversion of positive quantities; gives strict lower bound at the endpoint too. |
| S LF 25: “cost exactly 4/ε²” and “4/ε²<=2” | SUPPORTED | Direct privacy, normalization and moment reconstruction; also named import I261 LF 11, 23. |
| S LF 55–59: “(1415/1000)² = 2002225/1000000 > 2” and the displayed exponential-series bound | SUPPORTED | §3.6 supplies a completely written rational majorant and strict cross-product comparison. No owner script used. |
| S LF 21 and 63: “1/2 < V <= 2” and “ceil(sqrt(2V))=2” | SUPPORTED | Both bounds hold throughout the closed interval; its endpoints are strictly ordered. Structural use is conditional on I261 LF 17–19. |
| S LF 21: “V=min_(a>=0,c>=a+1/2) rho(a,c)” applies there | SUPPORTED, CONDITIONAL IMPORTS I261 + I273 | I273 LF 5 and 9, including the entire standing range, attainment and corrected-profile dependency. No independent proof of rho’s construction is claimed. |
| N=1 context and the absence of a converse claim; S LF 21 | SUPPORTED AT STATED BOUNDARY | IN1 LF 17–18, 38 is only conditional context. A failed sufficient hypothesis is not used as the proof of the lower bound. No exclusion of all one-core laws follows. |
| S LF 63: no scalar minimizer location, uniqueness, closed form, source equivalence or novelty claim | SUPPORTED AS A SCOPE LIMIT | Consistent with the nonadopted portion of I273 LF 12 and open scope in IN1. |
| S LF 67: “PASS A” and “PASS E” | NON-EVIDENCE | Owner diagnostic status only. Neither scripts nor logs were opened, executed, or relied upon. |
| S LF 69: “ALL 17 monomial coefficients strictly positive” and consequent strict growth of lambda_g | INCONCLUSIVE / EXPRESSLY EXCLUDED FROM THEOREM | Supplementary unreviewed future-extension statement. This packet supplies neither M2/M4 definitions nor the minimization domain/attainment proof needed to reconstruct the complete claim. No additional source was opened to fill that gap. |
| S LF 21: “first certified” | INCONCLUSIVE AS HISTORICAL PRIORITY | Not needed for interval existence; the permitted packet does not establish a priority census. No historical or novelty certification is given. |

The supplementary INCONCLUSIVE entries are not missing prerequisites of any load-bearing step above. They remain unreviewed statements rather than being silently promoted by a zero-defect theorem verdict.

## 5. Complete raw-display coverage receipt

All intervals below are inclusive LF ranges of actual `read` calls using `:raw`. Each call requested at most 15 LF. The windows were displayed sequentially in the order shown; none was elided or substituted by a hash, summary, or later review. Each file’s final window includes its actual ending.

| Input | Every display window, in order | Covered LF |
|---|---|---:|
| M | 1–15; 16–30; 31–45; 46–50 | 50/50 |
| S | 1–15; 16–30; 31–45; 46–60; 61–73 | 73/73 |
| I261 | 1–15; 16–30; 31–44 | 44/44 |
| IN1 | 1–15; 16–30; 31–45; 46–60; 61–75; 76–90; 91–105; 106–111 | 111/111 |
| I273 | 1–15; 16–16 | 16/16 |

Total scientific input coverage is 244/244 LF, plus 50/50 LF of the manifest. No scientific-body rereads or additional scientific display windows occurred.

## 6. Clocks, controls and additive process disclosure

The following are actual `/bin/date -u '+%Y-%m-%dT%H:%M:%SZ'` observations, not reconstructed event timestamps or claims of file creation time:

| Observation | Phase boundary |
|---|---|
| 2026-10-30T03:19:23Z | Before manifest metadata verification |
| 2026-10-30T03:19:24Z | After manifest metadata verification, before manifest body display |
| 2026-10-30T03:19:55Z | Before and after all four scientific input metadata checks; before S body display |
| 2026-10-30T03:20:21Z | After complete S display; before I261 display |
| 2026-10-30T03:20:36Z | After complete I261 display; before IN1 display |
| 2026-10-30T03:21:24Z | After complete IN1 display; before I273 display |
| 2026-10-30T03:21:38Z | After complete I273 display; before mathematical reconstruction |
| 2026-10-30T03:24:00Z | Before review drafting |
| 2026-10-30T03:25:14Z | Before the review-delivery phase |

The metadata commands used `/usr/bin/shasum -a 256` and `/usr/bin/wc -c -l`; both command chains returned exit code 0. Each bash invocation had a 120-second hard timeout. No mathematical subprocess, author code, reviewer control script, build, test, external model, or network operation was executed. There are consequently no mathematical run PASS claims, control-script hashes, timeout acceptances, or intended-negative outcomes to report. All finite comparisons in §3 are written reconstructions; the owner’s computational diagnostics are not borrowed as reviewer controls.

**Administrative packet-whitelist disclosure:** Before the manifest body, higher-priority harness instructions required reading `memory://root/memory_summary.md`, `skill://aifours-written-math-acceptance-protocol`, and `skill://independent-snapshot-review`. The skill reads ran in parallel with the initial manifest metadata command. These were out-of-manifest administrative reads, using their ordinary tool display rather than scientific-packet raw windows. This is disclosed explicitly as an administrative exception to the literal packet-only/manifest-first rule, not hidden under an assertion of no departures. They were not used as mathematical premises. No prior wave review body or other prohibited scientific material was opened. No independent-review CLI or network procedure from those skills was launched.

No mathematical consideration or mathematical notes preceded completion of all declared scientific displays. No oversized scientific-packet window, omitted ending, source-order substitution, frozen-input modification, deletion, backdating, or additional scientific exposure occurred. No frozen manifest, input, disposition, ledger, or README was changed. No control artifacts were created.

## 7. Assurance boundary

This is **same-harness written mathematical review**, including explicit hand reconstruction of the marginal lower bound, the cubic signs, the Laplace witness, the exponential-series comparison, and the conditional composition. I261 and I273 are named imported statements at their stated dependency boundaries. IN1 is conditional context; its prior process qualifications are not erased or reclassified here.

This is not human review, independent-model-family verification, formal proof, kernel checking, execution-based validation of the author’s code, source/book equivalence, historical priority certification, or novelty verification. It does not solve the remaining scalar optimization, its corner/kink normal-cone envelope, scalar-pair uniqueness, or the optimization outside the stated interval. Parent dispositions remain for the parent to compute.
