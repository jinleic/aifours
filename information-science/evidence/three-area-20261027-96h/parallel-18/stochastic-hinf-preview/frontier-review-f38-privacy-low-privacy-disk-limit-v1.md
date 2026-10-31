# f38 — conditional all-law low-privacy disk limit and radial separation

**Verdict: NO_SUBSTANTIVE_DEFECT AT THE EXACT CONDITIONAL SCOPES BELOW — 0 FATAL / 0 MAJOR / 0 MINOR.** Claims A–B depend on the explicitly named LAW642 actual-core/all-law theorem; Claim C additionally depends on the named matching-norm staircase and radial-infimum results. Those imported theorems are not newly re-proved by this review. No global-channel, novelty or stronger-verification claim follows.

Actual native prewrite observation: **Wed Oct 28 17:39:09 PDT 2026**. Reviewer InfoHinfPreview-2 (info-3), author InfoResearch96h-2 (info-1): disjoint slot, same information-science track/same harness. I reviewed this author's f14 and f25 shortly before this assignment; prior topic/source familiarity persists. This is not blind, independent-model, human, formal/kernel or novelty acceptance. No author contact.

## 1. Complete candidate, registered model and actual imports

- Assignment `f38-privacy-low-privacy-disk-limit/assignment-v1.json`, SHA `427faf01f556ec3905686922709a8cce2c0af4fe570481a76047bc9a5c57953d`, read completely FIRST.
- Complete candidate `frontier-20261028-euclidean-low-privacy-disk-limit-v1.md`, SHA `b277d099eb211302b73754a971f63d81dc781f160a5096ad6f30db85de85d7b3`, all 202 LF in exact raw windows 1–60,61–120,121–180,181–202 through ending.
- Registered info-1 envelope SHA `06a76efd7573f3d67971560f0609f97d9af6872e5286aa46abf69fe2ce84d0b` was read completely: ALL Borel query-output-independent additive laws on R², privacy for every Borel set and every shift in the FULL CLOSED unit-l1 diamond, original squared-Euclidean cost. The limit concerns finite ε>0 with b=e^(−ε)↓0; it is not an ε=∞ admissibility assertion.
- LAW642 parent disposition SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, exact theorem LF14–22: at each finite ε the unique all-law squared-Euclidean optimizer has density `p_*=Z^(-1)b^n` with closed levels `S_*+kD`, and actual core

  `S_*={x: ||x||_1<=2t_*, |x|_2²+2m||x||_infinity+T2<=V}`, `m=b/(1−b)`, `T2=m+2m²`, `t_*>0`, `V>T2`.

  Thus S_* is a compact convex positive-area actual core with 0 in its interior, and S_*⊂B2(0,sqrt(V)). I use this explicit already-written-supported theorem as a CONDITIONAL import; I do not re-prove its full 642-LF source or change its prior assurance.
- For the radial comparison ONLY: MDA per-cost parent SHA `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, and angular-infimum parent SHA `5e8fd8ec0cbd42af73a891acff0d8c0073d38e5e3795f558d401f6e5350374b4`. Their exact matching-norm staircase/`V_rad=(2/3)W` scopes are separate from LAW642. All named input hashes matched.

## 2. Full-shift trial laws and uniform layer bounds

For ANY compact S with 0∈S, `n_S(x)=min{k>=0:x∈S+kD}` is finite. If h∈D then `n_S(x+h)<=n_S(x)+1` because D+D=2D; applying the same argument to −h gives the reverse direction. Hence the density proportional to b^n is an ACTUAL Borel law satisfying every original closed-diamond event inequality, not a radial/finite-shift relaxation.

If S⊂B2(0,r), r<=1, then for every integer k>=1,

`kD⊂S+kD⊂(k+sqrt(2)r)D`.

No convexity of S is needed for these inclusions. The l1 diamond has area2 and squared-Euclidean integral2/3: quadrant slicing gives `∫_D x1²=4∫_0^1 x²(1−x)dx=1/3`, with the second coordinate equal by symmetry. Scaling gives area `2k²` and moment `(2/3)k⁴`.

Thus the k=1 level has area `2+O(r)` and moment `2/3+O(r)` uniformly in S. For 0<b<=1/2, the upper k-level area/moment are bounded by fixed multiples of `(k+sqrt(2))²` and `(k+sqrt(2))⁴`, respectively, so their k>=2 weighted tails are O(b²), with constants independent of S. The level identity `b^n=(1−b)∑_(k>=0)b^k1_(S+kD)` follows pointwise from a geometric tail and Tonelli. After the common positive factor cancels, with A=|S| and I=∫_S|x|²,

`J(Q_S)=[I+(2/3)b+O(br+b²)]/[A+2b+O(br+b²)]`.

The numerator/denominator errors have uniform S-independent constants under the stated radius bound. No cancellation of an uncontrolled signed infinite series is required.

## 3. Trial law, actual optimizer's area lower bound, and sharp value

For the actual feasible trial disk of radius `R0 b^(1/4)`, `R0=(4/(3π))^(1/4)`, its area is `2sqrt(π/3)sqrt(b)` and moment `(2/3)b`. Substituting into the uniformly valid layer expression gives the ORIGINAL all-law upper bound

`V <= [2/sqrt(3π)] sqrt(b)+O(b^(3/4))`.

LAW642's *actual* core obeys S_*⊂B2(sqrt V), hence r=sqrt V=O(b^(1/4)) and A<=πV=O(sqrt b). To pay the lower area rather than assume it, the k=1 level contains D, so the numerator of the exact layer ratio is at least `(2/3)b`. The upper bound V<=C sqrt b and denominator A+O(b) then force A>=c sqrt b for small b. The positive constants can depend on fixed ordinary numerical bounds but not on an unchosen profile. The same ratio now yields I=O(b).

For any planar measurable S of area A, subtract the equal disk area's radius squared from the inside/outside moment differences to obtain `I>=A²/(2π)`. Let `x=A/sqrt b` and `Delta=(I−A²/(2π))/b>=0`. The just-proved area and I bounds place x in a compact positive interval and Delta in a bounded nonnegative interval. Dividing the layer formula gives, UNIFORMLY in that range,

`V/sqrt b=f(x)+Delta/x+O(b^(1/4))`, `f(x)=x/(2π)+2/(3x)`.

The unique minimum is at `x0=2sqrt(π/3)` with `f(x0)=2/sqrt(3π)`. Exact algebra gives

`f(x)−f(x0)=(x−x0)²/(2πx)`.

Comparing with the actual trial upper bound forces `x=x0+O(b^(1/8))` and `Delta=O(b^(1/4))`, while both expressions are nonnegative. Therefore

`V=(2/sqrt(3π))sqrt b+O(b^(3/4))`.

This is the actual all-law value ONLY through the stated LAW642 optimizer/core import. It does not identify the trial disk as the exact finite-ε optimizer.

## 4. Quantitative core shape and entire-law total variation

Let B_rho be the centered disk with the SAME area A as the actual S_*, and E=|S_* triangle B_rho|. Subtract rho² times the equal areas inside/outside the disk to get the two nonnegative radial deficits in candidate (17). The area of `{||x|²−rho²|<q}` is at most 2πq for all q>0, including q>=rho². Taking q=E/(4π) leaves at least E/2 of the symmetric difference outside the band, so

`I−A²/(2π)>=E²/(8π)`.

Since b Delta=O(b^(5/4)), E=O(b^(5/8)). Scaling space by b^(−1/4) multiplies area by b^(−1/2), so the scaled core differs from its same-area disk by O(b^(1/8)). Its scaled disk area tends to x0 at that rate, and therefore its radius tends to `R0=sqrt(x0/π)=(4/(3π))^(1/4)` at the same rate. The difference of the two concentric disks has O(b^(1/8)) area. This pays the claimed symmetric-difference convergence of the ACTUAL core, not only a trial sequence.

On the actual core p_*=1/Z. Its layer normalizer is `Z=(1−b)[A+2b+O(br+b²)]`, so Z−A=O(b), and with A=Theta(sqrt b), the actual mass outside S_* is O(sqrt b). Conditional on S_* the law is uniform there. After scaling, both the core area and limiting disk area remain bounded away from zero; the TV distance of their uniform laws is bounded by a constant times their symmetric-difference area. Adding the actual outside mass proves TV=O(b^(1/8)). No pointwise boundary, stronger coupling or rate optimality is claimed.

## 5. Independent radial comparison, all small-m branches

MDA's named per-cost theorem supplies attainment of W=inf E||X||_1² by an actual centered staircase. For m=b/(1−b), gamma∈[0,1], the displayed moment formula `W(Q_gamma)=N/(2D)` follows from |rD|=2r², `∫_(rD)||x||_1²=r⁴` and the geometric moments. A trial gamma=m^(1/4) gives W<=C sqrt m.

For sufficiently small m, D<=gamma²+4m and N>=gamma⁴+m, giving the candidate lower estimate. At an actual minimizing gamma, the upper bound and that lower estimate force `gamma²=Theta(sqrt m)` on BOTH sides: the m term enforces the lower bound and gamma⁴ the upper bound. Uniformly over that compact scaled regime,

`W(Q_gamma)=(gamma²+m/gamma²)/2+O(m^(3/4))`.

AM–GM gives the lower sqrt m up to the stated error, while the same trial gives the upper. Therefore W=sqrt m+O(m^(3/4))=sqrt b+O(b^(3/4)). The separate angular-infimum theorem gives `V_rad=(2/3)W`; subtracting the proved actual V establishes the displayed leading gap and ratio `V/V_rad->sqrt(3/π)<1`. The strict inequality uses π>3, and concerns centered DIAMOND-radial laws only—not every norm, translation, or original arbitrary law.

## 6. Independent exact checks actually run

Reviewer-authored `frontier-review-f38-disk-asymptotic-check.py`, SHA `ec930e51c085a83673098fa53ccf1c182df5d66d03fedb569a95cc1d7543d6bd` (94 LF / 3273 bytes), was executed once with Python 3.14.3 and standard-library Fraction arithmetic:

`python3 frontier-review-f38-disk-asymptotic-check.py`.

Observed output: formal polynomial factorization PASS with residual `(x−y)(3y²−4π)` before imposing `y²=4π/3`; diamond area `2`, Euclidean moment `2/3`. For SYNTHETIC S=rD at r=1/4,1/8,1/16 and b=r⁴, exact closed geometric layer sums passed explicit rational O(br+b²) bounds. Independent radial trials at m=s⁴,gamma=s passed `|W_trial−s²|<=4s³` for s=1/4,1/8,1/16.

Those synthetic cores are NOT the LAW642 optimizer, and three finite checks do not prove uniform big-O, optimum selection or TV convergence. Those are the all-variable written arguments above, conditional on the named inputs. The review did not copy the author's checker or call an external model.

## 7. Verdict boundary and residual

Conditional on the specified same-harness LAW642 theorem, Claims A and B are fully reconstructed at the registered additive/closed-diamond/squared-Euclidean model. Conditional additionally on MDA per-cost and angular-infimum imports, Claim C is reconstructed at the centered-diamond-radial scope. No independent re-proof of LAW642/MDA, status of other primary sources, novelty, formal/kernel, human, configured-family or parent acceptance is implied. No claim about arbitrary nonadditive channels, ε=∞ as an attained probability model, all translated/other-norm radial classes or a sharp O(b^(1/8)) rate is made.

No author contact, external-model/paid API, nested agent, Git push, publication, deletion, secret access or infrastructure mutation occurred. Prior failure/quarantine/process records remain historical and no held result is accepted by association.
