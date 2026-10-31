# F563 — Complete WRITTEN review of the corrected composite

**Overall correctness: correct, conditional on the two expressly retained zero-lag imports.**  
**Fresh corrected-composite findings: 0 FATAL / 0 MAJOR / 0 MINOR.**  
**Confidence: 0.96.**

The additive erratum repairs the false fixed-original-space strong-limit assertion without weakening the intended expected-norm conclusions. The deterministic Gaussian characterization, strict deterministic bounds, long-lag reduction, causal burst family, and delay/feasibility conclusions withstand written reconstruction at their stated scope. This is not acceptance of an exact general short-lag gain, attainment classification, original-source equivalence, or controller synthesis.

**Read-only return for parent materialization as this wave’s `review-v1.md`. No repository file was written.**

## 1. Binding, coverage, and process boundary

Reviewed wave:

`f563-corrected-positive-lag-gaussian-limit-and-long-lag-written-review`

Bindings supplied by the user and corroborated by the frozen receipt and parent metadata supply:

- Manifest SHA256: `30d6353f5189839db7bfa38b7c8d7f8d6c0ff89a3b23726e2fc25b69e9103fc1`
- Freeze-receipt SHA256: `02a12878648d67ca7c846ede3b1fe43694ac49ca844a6a1b79e65af4c6e5ffce`
- Literal-packet SHA256: `c271282e91e2f61082674d07ce61802e08c6d91257bd954da55076b4dbc55173`

These are **parent-supplied metadata observations**, not child-executed hashes.

Before reading mathematical packet content, I read the complete manifest, freeze receipt, parent metadata supply, and all twelve status-only controls through their endings, then sent the required direct pre-body ACK to `agent://Main`.

I subsequently read the entire literal packet, **LF1–763**, in ordered raw windows of at most twenty lines, without an omitted ending:

1. **S1:** additive moving-Gaussian erratum, complete source LF1–35, SHA256  
   `507fe621c7528a45a8306a0e9973e3de4c98e7863aaa5c769001b7489b85bfa0`
2. **S2:** complete original f494 author candidate, logical source lines1–701, SHA256  
   `89baa76a5e641fec4d3c4bf243ad430048c35a18642bae601087b18e39e9890a`
3. **S3:** zero-lag matrix E1 composition disposition, complete source LF1–25, SHA256  
   `3fd8129086f29c1d44469ba976d5e9fa35e26be537c49f19dd098b44ef4ee3ba`

S1 was read first and is operative wherever it corrects S2. Mathematical reconstruction began only after the full packet ending.

Only these frozen mathematical inputs were used. Status controls, required process skills, and memory were administrative inputs only. No linked source, prior reviewer body, sibling mathematical return, author code, or held payload was followed. No new selected mathematical instance or private diagnostic was introduced.

**Scientific execution: NOT RUN.** No scientific code, CAS, interpreter, solver, numerical integration, enumeration, replay, build, test, lint, formatter, external-model CLI, or public-source search was used.

## 2. Exact imports and scope

Two load-bearing results remain imports rather than newly established theorems of this review:

1. **Weighted zero-lag E2 inequality.** For the actual matrix law driven by one scalar Brownian motion, the weighted expected-path-norm inequality with constant \(r\), as stated in S2 LF84–101 and retained through S3.
2. **Exact zero-lag gain.** The separate fixed-law result \(L_0=r c_T\), including its lower/sharpness component, as expressly composed in S3 LF11 and qualified in S3 LF25.

The weighted inequality does not itself supply the zero-lag lower family or positive-lag sharpness. S3 explicitly preserves that distinction.

The review also uses the stated standard analytic ingredients—finite-dimensional spectral facts, analyticity of the matrix exponential, Brownian Itô isometry and localization, Gaussian covariance facts, and compactness of probability measures on a compact metric space. Their applications are reconstructed below; no formal/kernel verification is claimed.

The result concerns exactly the displayed finite-horizon given law with zero prehistory, positive finite dimensions, progressive disturbances, and the original Brownian filtration. It does not identify that law with a general source plant or closed-loop controller formulation.

## 3. Per-claim dispositions

| Claim | Disposition | Source |
|---|---|---|
| Fixed-original-space \(L^2\) convergence of the shrinking single burst to one fixed Gaussian | **REFUTED AND WITHDRAWN**, as S1 requires; not an operative claim | S2 LF329–342; S1 LF3–19 |
| Moving single-burst comparison and expected-norm limit | **SUPPORTED** | S1 LF7–19 |
| Causal E1 extension and equality of E1/E2 suprema | **SUPPORTED, conditional on weighted E2 import** | S2 LF127–210 |
| Strict pointwise upper bound \(r c_H\) | **SUPPORTED, conditional on weighted E2 import** | S2 LF212–252 |
| Zero-output classification and stated uncharged-history divergence | **SUPPORTED** | S2 LF254–292 |
| Compact Gaussian maximum \(D_H\) and exact deterministic-input supremum | **SUPPORTED** | S2 LF294–395 |
| Strict bounds \(\kappa c_H<D_H<c_H\) when \(c_H>0\) | **SUPPORTED** | S2 LF397–441 |
| \(L_\tau=D_H\) for \(T/2\le\tau<T\), including all E1 random profiles | **SUPPORTED** | S2 LF443–497 |
| Bounded-Borel causal multi-burst lower family | **SUPPORTED with S1’s moving-law interpretation** | S2 LF499–588; S1 LF21–29 |
| Lag monotonicity, right continuity, and endpoint conclusions | **SUPPORTED; zero-lag limit uses the separate exact-gain import** | S2 LF590–634 |
| Strict feasibility and the long-lag optimizer-representation criterion | **SUPPORTED at the stated nonzero-gain scope** | S2 LF636–674 |
| Exact general short-lag gain, evaluation/attainment of \(D_H\), and actual critical endpoint | **INCONCLUSIVE; expressly unpaid, not newly asserted** | S2 LF670–672, LF692–698 |
| Original-source equivalence, controller synthesis, novelty, human/kernel or independent-family assurance | **NOT ESTABLISHED / OUT OF SCOPE**, consistently with the candidate’s exclusions | S2 LF676–701 |

## 4. Reconstruction of the operative Gaussian correction

### 4.1 Single burst

For the deterministic input in S2 LF320–327, the actual shifted Hilbert output is the stochastic integral of \(F_s a/\sqrt\delta\) over the first applied-noise interval. On the **same original probability space**, the correct comparison is \(F_0a Z_\delta\), where

\[
Z_\delta=\frac{W_{\tau+\delta}-W_\tau}{\sqrt\delta}.
\]

Subtracting these two integrals gives exactly

\[
\mathbb E\|Y_\delta-F_0aZ_\delta\|_{\mathcal H}^{2}
=
\frac1\delta\int_0^\delta\|(F_s-F_0)a\|_{\mathcal H}^{2}\,ds.
\]

Operator-norm continuity of \(F_s\) makes this tend to zero. Since every \(Z_\delta\) has the standard-normal law,

\[
\left|\mathbb E\|Y_\delta\|_{\mathcal H}-\kappa c_H\right|
\le
\left(\mathbb E\|Y_\delta-F_0aZ_\delta\|_{\mathcal H}^{2}\right)^{1/2}
\longrightarrow0.
\]

Thus the lower witness and expected-norm bound survive exactly as intended.

The correction also correctly distinguishes distributional convergence from strong convergence on the original space. For nested widths, S1 LF19 gives the correct covariance calculation. When \(c_H>0\), keeping a fixed nonunit width ratio prevents the moving comparison vectors from being Cauchy. Together with the vanishing comparison error, this excludes a fixed original-space strong limit for the actual outputs as well.

No altered filtration, extra coupling, or anticipative input is required.

### 4.2 Adapted multi-burst comparison

The physical schedule in S2 LF509–542 satisfies

\[
t_{j-1}+\delta=s_j.
\]

Consequently, every increment used by \(h_j\) has been observed by the original **input time** \(s_j\). Bounded Borel functions are sufficient; continuity of \(h_j\) is unnecessary.

The correct comparison keeps the amplitudes and increments width-dependent, as S1 LF23–29 specifies. Both the actual output and its moving comparison can be expressed using stochastic integrals over the disjoint applied-noise intervals. Their difference therefore has the stated Hilbert Itô-isometry error. Random dependence of later amplitudes on earlier increments does not invalidate this calculation: the coefficients are already measurable before their respective applied-noise intervals.

Boundedness of the amplitudes, finite \(N\), and continuity of \(F_s\) make that error tend to zero. The joint standard-normal increment law is the same for every admissible width, so the moving comparison’s joint law with the input norm is width-independent.

This proves the displayed expected-norm ratio limit without claiming convergence of discontinuous \(h_j\)-values to fixed original-space random variables.

## 5. Causal E1 extension, strict upper bound, and zero cases

### 5.1 Extension to the actual local solution

The pointwise cutoffs in S2 LF147–164 are progressive, bounded, and E2. Their pathwise time-\(L^2\) errors tend to zero and are bounded by the original path norm, so E1 convergence follows by dominated convergence.

Applying the imported E2 inequality to delayed cutoff differences produces the stated Cauchy estimate in \(L^1(\Omega;L^2_t)\).

Crucially, S2 LF177–200 does not merely define an abstract Banach-space extension. The original E1 input has finite time-\(L^2\) norm almost surely, hence an actual local Itô solution. The difference martingale’s terminal bracket tends to zero almost surely. Stopping at bracket level \(\delta\), applying Doob’s inequality, and then taking the two limits yields uniform convergence in probability of the actual cutoff solutions to that local solution. This identifies the Banach-space limit with the actual output.

The weighted norm is Lipschitz with constant \(c_H\), so the weighted inequality passes to the limit. Numerators and positive denominators of cutoff ratios converge, establishing equality of the E1 and E2 suprema.

No nonadapted full-path indicator enters this argument.

### 5.2 Strictness of the \(r c_H\) bound

The pointwise matrix inequality in S2 LF224–242 is valid. Equality for a nonzero direction at positive input time would force both equality at the top eigenvalue of \(G(H)\) and vanishing of the analytic impulse response on a nontrivial interval. Analyticity would then force it to vanish identically, contradicting the positive top-eigenvalue equality.

Integration gives a strict weighted-clock gap on every path with nonzero input norm; unused-tail energy also gives a gap. Since a nonzero admissible input has positive probability of nonzero path norm, taking expectations preserves strictness.

This excludes attainment of **the upper bound** \(r c_H\), not necessarily attainment of the actual gain. S2 LF252 correctly preserves that limitation.

### 5.3 Zero output and history

For \(\tau\ge T\), zero prehistory leaves no positive-length applied-noise interval.

For \(H>0\), vanishing \(G(H)\) is equivalent to vanishing of the continuous impulse kernel on an interval. Analyticity and Cayley–Hamilton give the stated finite matrix criterion. Conversely, the corrected burst expectation establishes positive gain when \(c_H>0\).

The uncharged-history divergence in S2 LF276–290 follows directly from the triangle inequality and scaling of the charged input denominator. It is appropriately separated from the zero-history theorem.

## 6. Deterministic Gaussian characterization and strict bounds

### 6.1 Exact deterministic supremum

After removing the unused tail, a normalized deterministic profile produces exactly the covariance \(Q_{\mu_v}\) in S2 LF370–379.

Conversely, a finite atomic measure can be approximated using finitely many disjoint, narrow deterministic bursts with the prescribed energy masses and directions. Repeated atom times can be separated by nearby times. The boundary times create no obstruction: one-sided intervals remain available, and \(F_H=0\). Continuity of \(F_s\) gives the required covariance approximation.

This argument needs covariance/expected-norm convergence, not the withdrawn fixed-space strong limit.

The compactness argument is also sufficient. The impulse-vector image of \(K\) is compact in \(\mathcal H\), hence uniformly approximable by a finite-dimensional subspace. The resulting Gaussian projection-tail estimate is uniform over all probability measures. Finite-dimensional covariance dependence is continuous, and the projection error bounds the expected-norm error uniformly. Therefore \(J\) is continuous on the weakly compact probability-measure space and attains its maximum.

Atomic approximation then identifies that compact maximum with the actual deterministic-input **supremum**, without claiming that an actual deterministic profile represents a maximizing measure.

### 6.2 Strict upper bound

Jensen and the trace bound give \(J(\mu)\le c_H\). Compact attainment is essential to promote this to \(D_H<c_H\): equality at a maximizing measure would require a nonzero Gaussian vector to have constant norm almost surely. A nonzero one-dimensional projection is unbounded, making that impossible.

The zero covariance case cannot supply equality when \(c_H>0\).

### 6.3 Strict lower bound

The source’s \(f=F_0a\) and \(g=F_sa\) are nonzero and noncollinear for \(0<s<H\). Analyticity ensures both the nonvanishing of \(g\) on its remaining interval and the nonvanishing of \(f\) on the initial interval where \(g\) is zero.

The displayed formula for \(j(\theta)\) is a valid **Gaussian norm-law representation** of the two-atom covariance mixture. It need not be interpreted as the norm of the original coefficient-by-coefficient stochastic coupling. In an orthonormal basis of the span of \(f,g\), the squared Gaussian norm has the quadratic-form law used in S2 LF418–434.

The right difference quotients increase as \(\theta\) decreases to zero and have the stated integrable lower bound. After adding that bound, monotone convergence applies. The transverse component produces the positive \(1/|X|\) divergence, whereas the negative part is integrable. Hence the right derivative is \(+\infty\), and sufficiently small positive mixtures improve strictly on \(\kappa c_H\).

Approximation by actual deterministic bursts completes

\[
\kappa c_H<D_H<c_H.
\]

No new selected parameter instance is needed for this reconstruction.

## 7. Long-lag conditioning and attainment boundary

When \(H\le\tau\), progressive measurability makes the entire active profile an \(\mathcal F_\tau\)-measurable random element of the separable time-\(L^2\) space. The entire future Brownian increment process after \(\tau\) is independent of \(\mathcal F_\tau\).

Conditioning therefore fixes the active profile and gives the stated centered Gaussian covariance. Its conditional expected norm is bounded by \(D_H\) times the active profile norm. For E1 inputs, cutoff convergence identifies this conditional construction with the actual local output and permits passage to the limit.

Taking expectations gives the upper bound for **all** admissible E1 random profiles. Deterministic profiles approximate \(D_H\), giving the reverse inequality. The common endpoint \(H=\tau\) supplies no positive-length opportunity to react to applied noise.

Thus

\[
L_\tau=D_H,\qquad T/2\le\tau<T,
\]

and the strict deterministic bounds yield the claimed long-lag chain.

For positive gain, equality by a random input would force equality in the conditional deterministic bound on its nonzero active profiles and no wasted tail energy. Such profiles would supply an actual deterministic maximizer. Conversely, an actual deterministic maximizing profile is itself admissible. This supports the stated optimizer-representation criterion.

It does **not** resolve whether such a profile exists. Neither compact measure attainment nor nonattainment of \(c_H\) settles attainment of \(D_H\).

## 8. Delay regularity, feasibility, and RMS distinction

The delay-comparison transformation in S2 LF594–610 preserves the effective input norm, remains progressive in the original filtration, and produces the identical delayed diffusion coefficient. This proves lag monotonicity; the zero-output regime is immediate separately.

For a fixed E1 input, zero-extended time translation is continuous pathwise in time-\(L^2\), with an integrable domination for its E1 norm. Applying the zero-lag inequality to delayed-input differences makes the actual output continuous in the delay.

For any nearly maximizing fixed input, this continuity gives the required lower bound on nearby gain values. Combined with monotonicity, it establishes right continuity. At zero lag, the **separate exact zero-lag import** then supplies the limit \(r c_T\). Since \(r>1\), the stated sufficiently-small-lag improvement over every deterministic profile follows. No numerical cutoff is asserted.

The strict-feasibility classification is a correct consequence of the definition of a supremum:

- above the gain, a uniform positive margin exists;
- below it, feasibility fails;
- at it, pointwise strict feasibility is equivalent to nonattainment.

The special upper-bound and long-lag conclusions use the appropriate established gaps and do not conflate pointwise strictness with a uniform margin.

Finally, the RMS statement follows from Itô isometry and the same narrow deterministic energy concentration. It is correctly kept distinct from the literal ratio of expected path norms.

## 9. Findings and historical disposition

**No new mathematical finding is raised against the operative corrected composite.**

The original S2 fixed-original-space \(L^2\) assertion remains false and withdrawn. This review does not clear it retrospectively, edit the original source, or overwrite either prior review:

- f549 retains its historical **0F/0M/1m**;
- f550 retains its historical **0F/1M/0m**;
- the parent’s conservative classification remains **one MAJOR mathematical proof-assertion defect for the same issue**.

The new **0F/0M/0m** count applies only to the fresh review of **S1 operating on the complete S2 body with the exact S3 imports**.

## 10. Final disposition

The corrected composite is supported as a **conditional, given-law written result** at its expressly stated scope. Its operative conclusions do not require the withdrawn fixed-space Gaussian limit, and their downstream uses retain the original input filtration and expected-norm criterion.

Still unestablished are the exact general short-lag adapted gain, evaluation and actual-profile attainment of \(D_H\), the unresolved actual critical endpoints, coefficient-level original-source equivalence, and controller synthesis. No novelty, independent-family, human, kernel, or executed-verification assurance is conferred, and no held episode or consumer is rehabilitated.