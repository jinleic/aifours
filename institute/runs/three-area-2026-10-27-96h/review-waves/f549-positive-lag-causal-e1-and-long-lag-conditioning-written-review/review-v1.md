# F549 — complete WRITTEN review

**Materialization:** Full review text returned for Main to save as this wave’s `review-v1.md`. No repository file was written, and no write restriction was bypassed.

**Finding count: 0 FATAL / 0 MAJOR / 1 MINOR.**

The substantive fixed-law results are supported at the stated import boundaries. One explicit common-probability-space \(L^2\)-convergence assertion is false and needs a local correction; the expected-norm lower bound and its downstream conclusions survive that correction.

## 1. Binding, read order, and evidence boundary

Reviewed frozen wave:

`f549-positive-lag-causal-e1-and-long-lag-conditioning-written-review`

Bindings, as supplied by the parent’s metadata records:

- Manifest: `81dd4623f71cd35e4721cc68a78bbb997a68ef85dbc406c07ff8b30893200e84`
- Freeze receipt: `716a57a8341de814e8fd3b3cbc95c3223d0e743add10ac3457da3774e4744ca2`
- Literal packet: `dfb1d613c848ffee8c91570c46835d1a57a22f50b23ddb87d5c5470dab365f0b`
- S1, complete author body: `89baa76a5e641fec4d3c4bf243ad430048c35a18642bae601087b18e39e9890a`
- S2, complete adopted import: `3fd8129086f29c1d44469ba976d5e9fa35e26be537c49f19dd098b44ef4ee3ba`

These are **parent-supplied hash/clock observations**, not independently executed child hashes or a child-native timestamp.

Before reading mathematical packet content, I completely read the manifest, freeze receipt, metadata supply, dispatch receipt, and all twelve status controls through their endings. I then sent the required **direct pre-body ACK to `agent://Main`**. Afterwards, I read packet LF1–728 in ordered raw windows of at most 20 LF, including S1’s final logical line 701 and S2’s final line 25, before deriving.

Entire held episodes and all their mathematical, selection, planning, verification, confidence, and reporting consumers remained NONINPUT. No excluded links, prior reviewer bodies, sibling outputs, new sources, or author code were followed.

**Execution: NOTRUN.** No scientific program, interpreter, solver, enumeration, numerical probe, test, build, formatter, external-model CLI, Git operation, installation, or live-infrastructure action was performed. No additional concrete mathematical instance was introduced.

The operative scope is the frozen f549 manifest: the actual positive-lag given law, causal E1 extension, strict weighted upper bound, deterministic Gaussian characterization, long-lag conditioning, and their expressly stated consumers. The separate f489/Tuscan frontier was not imported.

## 2. Exact imports

Two distinct S2 imports must remain separate:

1. **Weighted E2 inequality:** S2 LF7–9 supplies the zero-lag weighted inequality for progressive E2 inputs. Applying it to the actual delayed coefficient supports S1’s general positive-lag weighted inequality.
2. **Exact zero-lag gain:** S2 LF11 separately supplies the adopted zero-lag gain \(L_0=r c_T\). This is needed for S1’s small-delay limit and eventual advantage over deterministic profiles—not for the deterministic Gaussian optimization or the long-lag conditioning argument.

Neither the Bellman/generalized-Itô proof nor the original zero-lag lower family was reconstructed in this review. They are **named imports**, not newly verified results.

S1’s reference to an original S3 page observation is not an additional f549 mathematical input. The underlying source pages were not supplied here and were not followed.

## 3. Finding m1

**Title:** Replace the fixed L2 burst limit with a moving Gaussian comparison

**Body:** When \(c_H>0\), the burst outputs in §6.1 do not converge in \(L^2(\Omega;\mathcal H)\) to a fixed \(F_0aZ\) on the given Brownian probability space. The displayed error instead compares the output with \(F_0aZ_\delta\), where \(Z_\delta=(\beta_\delta-\beta_0)/\sqrt{\delta}\); these normalized increments are not an \(L^2\)-Cauchy family, since for \(0<\varepsilon\le\delta\), \(\mathbb E|Z_\delta-Z_\varepsilon|^2=2-2\sqrt{\varepsilon/\delta}\). Thus the asserted strong limit is false, although the intended lower bound remains valid: state that the moving-comparison error tends to zero and use the invariant standard-normal law of \(Z_\delta\) to obtain convergence of expected output norms, or state convergence in distribution instead. This correction preserves the positive-gain argument in §5 and the lower-bound consumers in §§6, 7, and 10.

- **Priority:** 2
- **Severity:** MINOR
- **Confidence:** 1.0
- **File path:** `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f494-stochastic-hinf-positive-lag-adapted-operator-frontier/review-v1.md`
- **Line start:** 329
- **Line end:** 333

This is a false proof assertion, not a refutation of the expected-norm lower bound. No downstream conclusion requires convergence to a fixed Gaussian on the original probability space.

## 4. Claim-by-claim reconstruction

### A. Actual law, information timing, and shifted upper-bound use — SUPPORTED

**Source:** S1 LF23–123.

For zero prehistory, variation of constants gives, for \(0\le u\le H\),

\[
z_{\tau+u}
=\int_0^u Ce^{P(u-s)}B w_s\,d\beta_s,
\qquad
\beta_s=W_{\tau+s}-W_\tau.
\]

The admissible input remains progressive with respect to the original \(\mathcal F_s\). It does not become an arbitrary input adapted to \(\mathcal F_{\tau+s}\).

The upper inequality can nevertheless be applied directly to the physical-time coefficient \(v_t=\mathbf1_{\{t\ge\tau\}}w_{t-\tau}\). It is progressive in the original physical-time filtration, and its weighted clock is exactly

\[
\int_\tau^T w_{t-\tau}^{\top}G(T-t)w_{t-\tau}\,dt
=\int_0^H w_s^{\top}G(H-s)w_s\,ds.
\]

This use does not import an anticipative lower witness. The timing distinction is correctly retained throughout the long-lag and adapted-burst consumers.

### B. Causal E1 extension and equality of E1/E2 suprema — SUPPORTED, conditional on the weighted E2 import

**Source:** S1 LF125–210; S2 LF7–19.

The cutoffs \(w^{(k)}=w\mathbf1_{\{|w|\le k\}}\) are progressive and E2. Their pathwise L2 differences tend to zero and are bounded by \(\|w\|_T\), so dominated convergence gives convergence in \(L^1(\Omega;L^2)\).

The imported inequality applied to cutoff differences makes the corresponding outputs Cauchy in that same Banach space. This alone would not identify the actual local solution; S1 supplies the necessary identification:

- E1 implies finite pathwise input energy almost surely.
- The actual local martingale representation therefore exists.
- The trace bracket of the difference from a cutoff solution tends to zero almost surely.
- Stopping at bracket level \(\delta\) and applying Doob’s L2 inequality yields uniform convergence in probability.
- Uniqueness of probability limits identifies the Banach-space limit with the actual output.

The weighted clock is Lipschitz:

\[
|Q_H(u)-Q_H(v)|\le c_H\|u-v\|_T.
\]

Consequently, the weighted inequality passes to E1. Numerator and denominator expectations of cutoff ratios converge to those of each nonzero E1 input. This proves equality of the E1 and E2 literal gain suprema.

The proof uses no nonprogressive full-path-norm indicator.

### C. Strict \(r c_H\) bound — SUPPORTED

**Source:** S1 LF212–252.

For \(s>0\), equality in

\[
G(H-s)\preceq G(H)\preceq c_H^2I
\]

along a nonzero vector \(a\) would force \(Ce^{Pv}Ba\) to vanish on \([H-s,H]\). Analyticity would make it vanish identically, contradicting the simultaneous equality \(a^\top G(H)a=c_H^2|a|^2>0\).

Thus, when \(c_H>0\),

\[
a^\top G(H-s)a<c_H^2|a|^2
\quad(s>0,\ a\ne0).
\]

Every path with nonzero active energy has a strictly positive integrated gap; unused-tail energy also gives a strict gap. For a nonzero E1 input, this occurs on a set of positive probability, so taking expectations preserves strictness.

The exact conclusion is that **no nonzero input attains the bound \(r c_H\)**. It does not establish nonattainment of \(L_\tau\), nor establish a uniform gap below \(r c_H\).

### D. Zero-output classification and uncharged history — SUPPORTED

**Source:** S1 LF254–292.

If \(\tau\ge T\), no positive-length applied-noise interval remains. The terminal singleton at \(\tau=T\) contributes nothing to the Itô integral.

For \(H>0\),

\[
G(H)=0
\iff Ce^{Pv}B\equiv0
\iff CP^kB=0,\quad 0\le k<n.
\]

The first equivalence follows from continuity and positivity of the integrated squared kernel, followed by analyticity. Taylor expansion and Cayley–Hamilton give the finite matrix criterion. If \(c_H>0\), the corrected expected-norm burst argument supplies positive gain.

The history conclusion has the necessary qualification: **nonzero history alone is not enough**. The infinite-gain argument assumes \(0<\mathbb E\|z^h\|_T<\infty\). Under that assumption, scaling an admissible positive-time input to zero leaves a positive history contribution in the numerator and makes the uncharged denominator vanish.

### E. Deterministic Gaussian variational characterization — SUPPORTED; the fixed-L2 limit wording is REFUTED by m1

**Source:** S1 LF294–395.

The impulse map \(s\mapsto F_s\) is operator-norm continuous. A support change contributes a term tending to zero with the interval length, and the remaining matrix-exponential kernel is uniformly continuous on its compact domain.

For a deterministic profile \(v\), the output is a centered Hilbert-valued Gaussian with covariance

\[
\int_0^H(F_sv_s)\otimes(F_sv_s)\,ds.
\]

After normalizing input energy, this is precisely \(Q_{\mu_v}\). Conversely, disjoint deterministic bursts approximate every finite atomic measure, including repeated atom times by nearby disjoint intervals. Atomic approximation and continuity then cover all probability measures on \(K\).

The asserted maximum exists. Compactness of the impulse-image set gives finite-dimensional projections whose Gaussian tail second moments are uniformly small. Finite-dimensional covariance entries vary continuously with the measure; therefore the expected norm is a uniform limit of continuous finite-dimensional functions. Weak compactness of \(\mathcal P(K)\) supplies a maximizer.

These steps prove that \(D_H\) equals the deterministic-input supremum. They do not assert that its maximizing measure is represented by an actual L2 profile.

### F. Strict deterministic bounds — SUPPORTED

**Source:** S1 LF397–441.

For the upper bound,

\[
J(\mu)^2\le \operatorname{tr}Q_\mu\le c_H^2.
\]

If the attained compact maximum equaled \(c_H>0\), Jensen equality would force a nonzero Gaussian vector to have constant norm. A nonzero Gaussian projection is unbounded, ruling this out. Hence \(D_H<c_H\).

For the strict lower bound, \(f=F_0a\) and \(g=F_sa\), with \(0<s<H\), are nonzero and noncollinear. Analyticity prevents \(f\) from vanishing throughout the initial interval on which \(g\) vanishes.

Writing \(f=c_He_1\) and \(g=\alpha e_1+\beta e_2\), \(\beta\ne0\), the stated Gaussian quadratic-form expression has the covariance eigenvalues of the two-atom mixture. Its right derivative at zero is \(+\infty\): the \(\beta^2Y^2/|X|\) contribution diverges positively, while the other terms have integrable negative part. Concavity makes the difference quotients monotone as the parameter decreases to zero; the supplied integrable lower bound justifies the expectation limit.

A sufficiently small positive mixture therefore improves strictly on the single-atom value. Atomic approximation by admissible deterministic bursts gives

\[
\sqrt{2/\pi}\,c_H<D_H<c_H.
\]

### G. Long-lag conditional Gaussian reduction — SUPPORTED

**Source:** S1 LF443–497.

When \(H\le\tau\), progressiveness makes the complete active input profile an \(\mathcal F_\tau\)-measurable random element of the separable space \(L^2([0,H];\mathbb R^m)\). E1 ensures that this profile has finite norm almost surely. Future Brownian increments are independent of \(\mathcal F_\tau\).

The conditional Gaussian assertion can be made precise without assuming additional regularity of the underlying probability space. First approximate bounded-cutoff profiles by \(\mathcal F_\tau\)-simple L2-valued profiles. Independence gives the conditional Gaussian characteristic functional for these simple profiles; Hilbert-space Itô isometry passes it to the cutoff profile. The E1 cutoff limit then identifies the actual local output as in Proposition 1.

The resulting conditional covariance is exactly

\[
\int_0^H(F_sw_s)\otimes(F_sw_s)\,ds,
\]

and the conditional expected norm is at most \(D_H\|w\|_{[0,H]}\). Taking expectations and allowing for unused-tail energy proves \(L_\tau\le D_H\). Deterministic profiles approaching \(D_H\) are admissible, proving equality.

The endpoint \(T=2\tau\) is included: the common endpoint does not supply a positive-length opportunity to react to applied noise.

Therefore,

\[
L_\tau=D_H,\qquad
\sqrt{2/\pi}\,c_H<L_\tau<c_H<r c_H
\]

in the nonzero long-lag case. The author’s stated scalar specialization follows, but no new scalar instance was introduced here.

### H. Genuine adapted lower bursts — SUPPORTED

**Source:** S1 LF499–588.

The timing identity \(t_{j-1}+\delta=s_j\) ensures that all arguments used to choose \(a_j\) are already observed at input time \(s_j\). The coefficient is then held constant during the input burst. No future applied increment enters its choice.

The input-energy identity follows from disjoint input supports. For convergence, retain the \(\delta\)-dependent normalized Brownian increments while comparing kernels with \(F_{(j-1)\tau}\). Hilbert-space Itô isometry, bounded amplitudes, and continuity of \(F_s\) make this comparison error tend to zero.

The resulting comparison numerator and denominator have distributions independent of \(\delta\), because the normalized increments have the same independent standard-normal joint law. This proves the displayed limiting expected-norm ratio. Unlike §6.1’s wording, this section asserts convergence of expected norms, not convergence to a fixed Gaussian realization.

The family supplies valid lower bounds and genuinely nonconstant causal responses when the stated timing condition allows them. It does not prove sharpness or quantify an improvement over deterministic inputs.

### I. Lag monotonicity, continuity, and endpoint consumers — SUPPORTED at the named zero-lag imports

**Source:** S1 LF590–634.

After removing unused-tail energy, delaying an input by \(\tau_2-\tau_1\) preserves its norm and gives exactly the same physical applied coefficient under lag \(\tau_1\). It remains progressive. Thus \(L_{\tau_1}\ge L_{\tau_2}\); zero-output cases are immediate.

Zero-extended translation is continuous in \(L^1(\Omega;L^2)\). The imported zero-lag E1 bound therefore gives continuity of the actual output for each fixed input as delay varies. The supremum of these continuous ratios is lower semicontinuous; together with monotonicity, this gives right continuity.

The upper bound proves \(L_\tau\to0\) as \(\tau\uparrow T\). The separately imported equality \(L_0=r c_T\), together with delayed versions of a fixed nearly sharp input, proves the limit as \(\tau\downarrow0\).

When \(c_T>0\), that limit exceeds \(c_T\), while \(c_{T-\tau}\to c_T\). Hence the eventual strict comparison with all deterministic profiles follows. No explicit cutoff was established or inferred.

### J. Feasibility, attainment, and RMS distinction — SUPPORTED, with the stated obligations still open

**Source:** S1 LF636–674.

The pointwise and uniform-margin classifications follow directly from the definition of a supremum. At \(\gamma=L_\tau\), pointwise strictness holds precisely when the supremum is not attained.

In the nonzero long-lag case, an attaining random input would have to satisfy both:

1. No unused-tail energy.
2. Equality in the conditional deterministic bound on its nonzero active-profile paths.

Such equality supplies an actual deterministic L2 maximizing profile. Conversely, such a deterministic profile is itself admissible and attains the gain. This establishes the representation criterion, **not its resolution**.

The RMS result is separate: Itô isometry gives squared gain at most \(c_H^2\), deterministic narrow bursts approach that value, and the strict clock gap excludes attainment when it is positive. None of this determines attainment of the literal expected-path-norm gain.

### K. Original-source equivalence, controller synthesis, and broader status — INCONCLUSIVE / NOT RECONSTRUCTED

**Source:** S1 LF676–701; S2 LF21–25.

The displayed mathematics concerns only the explicit given law, scalar Brownian driver, original-filtration inputs, and zero history.

The f549 packet does not supply the original S3 pages or a coefficient-level controlled-plant comparison. Accordingly, this review does not verify the documentary page observation, source equivalence, a controller construction, or closure of the printed synthesis problem.

The unpaid short-lag optimization, evaluation of \(D_H\), optimizer representation, and actual critical-endpoint/nonattainment questions remain unpaid. No novelty, current-openness, independent-family, human, or kernel/formal credit is assigned.

## 5. Consumer audit and disposition

The mathematical consumer paths were reconstructed as follows:

- **S2 weighted inequality → Proposition 1 → strict \(r c_H\) bound and delay-continuity estimates:** supported at the named import.
- **S2 exact zero-lag gain → small-delay limit → eventual adaptation advantage:** supported as a separate import, not established by long-lag conditioning.
- **§6.1 burst comparison → positivity and Gaussian lower-bound consumers:** expected-norm conclusions supported; fixed common-space L2 convergence requires m1’s correction.
- **Deterministic covariance characterization → compact maximum → strict deterministic bounds → long-lag equality → feasibility/attainment criterion:** supported, without claiming representability or actual nonattainment.
- **Physical timing identities → adapted-burst admissibility → lower-bound family:** supported; no shifted-filtration witness was silently treated as originally admissible.
- **Given-law conclusions → original controller-synthesis problem:** no such transfer is supported or accepted.

**Overall correctness:** incorrect

**Explanation:** The candidate contains one false common-space L2-convergence assertion that should be corrected before adoption as written. The expected-norm conclusions and the substantive causal E1, strict-bound, deterministic-variational, and long-lag results are supported at their explicit import boundaries; actual nonattainment and original controller-synthesis closure remain unproved.

**Confidence:** 0.98