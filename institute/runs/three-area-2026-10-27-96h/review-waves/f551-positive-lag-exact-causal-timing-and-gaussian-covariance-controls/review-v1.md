# author-candidate-v1.md — F551 exact causal timing and Gaussian covariance interfaces

**Status:** WRITTEN, SOURCE-EXPLICIT INTERFACE RECONSTRUCTION. Scientific execution **NOT RUN**. Complete body returned for Main materialization; no repository file was written.

**Scoped result:** The delayed-input timing, scalar impulse Gram kernel, two-atom covariance/distribution identity, and deterministic rectangular-burst interfaces below reconstruct correctly. There is one locally repairable false fixed-space \(L^2\)-convergence statement in F494 §6.1. Correcting it preserves the expected-norm limit and the resulting lower bound.

This is not verification of the imported Bellman/generalized-Itô inequality, evaluation of the general adapted gain, controller synthesis, original-source equivalence, novelty, or a formal/kernel/human/independent-family check. F489 and Tuscan closure are outside this assignment and were not read.

## 1. Binding, chronology, and execution boundary

The assigned wave is:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f551-positive-lag-exact-causal-timing-and-gaussian-covariance-controls/`

Bindings supplied by the frozen controls:

| Artifact | SHA256 |
|---|---|
| Manifest | `4a960db53037c8ca22b8d3a187d387411d81649ae2ff5b829e0f3dc98d26c134` |
| Freeze receipt | `dab39509eb940ee62e4fbbbfd6a2d7f5a046dbcddea6290b8b6afa4014f62945` |
| Literal packet | `43ef099719a5290e3bb90844d6f458b31e369d86e74228c59bcd1b95d4d3eb22` |
| F494 author source S1 | `89baa76a5e641fec4d3c4bf243ad430048c35a18642bae601087b18e39e9890a` |

These are **parent-observed metadata**, not hashes or clocks independently executed by this child.

Chronology:

1. Read the manifest through LF103, freeze receipt through its ending, parent live metadata supply through its ending, dispatch receipt, and all twelve manifest-listed permission/status controls.
2. Sent a direct pre-body ACK to `agent://Main`.
3. Read all 703 physical packet lines, in order, using exact raw windows of at most twenty LF: 1–20 through 681–700, then 701–703.
4. Only after the complete packet ending was read did the mathematical reconstruction begin.
5. Subsequently reread packet windows 321–340, 501–520, and 401–420 to anchor the coupling, timing, and Gaussian identities.

The source uses labels S1|1 through S1|701. Its reported LF count is 700; the complete packet includes the final labeled source line. No tail was omitted.

All held episodes and their consumers remain NONINPUT. No external source, sibling scientific output, author code, held payload, Git operation, build, test, solver, scientific interpreter, or external-model CLI was used.

The FINITE manifest permits modest calculations, but this assignment’s higher-priority read-only role prohibits scientific execution. Consequently, the exact-arithmetic program in §9 is **prospective source and argv only, NOT RUN**, with no filesystem-write or execution bypass.

## 2. Exact physical timing

The law is exactly

\[
dx_t=Px_t\,dt+B w_{t-\tau}\,dW_t,\qquad x_0=0,\qquad z_t=Cx_t,
\]

with \(\tau>0\), zero input prehistory, and \(w_s\) progressive relative to the **physical input-time filtration** \(\mathcal F_s\).

Write \(H=T-\tau>0\). For \(u\in[0,H]\),

\[
z_{\tau+u}=\int_0^u F_s w_s\,d\beta_s,
\qquad
\beta_s=W_{\tau+s}-W_\tau,
\]

where, as a Hilbert-space output vector,

\[
(F_sa)(u)=\mathbf1_{\{u\ge s\}}Ce^{P(u-s)}Ba.
\]

The shifted Brownian filtration is \(\mathcal G_s=\mathcal F_{\tau+s}\). Admissibility remains \(w_s\in\mathcal F_s\), not merely \(w_s\in\mathcal G_s\).

### 2.1 The F494 burst schedule is causal

Suppose

\[
N\tau<T,\qquad
0<\delta<\frac{T-N\tau}{N}.
\]

Define

\[
s_j=(j-1)(\tau+\delta),\qquad
t_j=s_j+\tau.
\]

The physical input and applied-noise intervals are respectively

\[
I_j=[s_j,s_j+\delta],\qquad
A_j=[t_j,t_j+\delta].
\]

Their relevant endpoints satisfy

\[
t_N+\delta=N(\tau+\delta)<T,
\]

and

\[
s_N+\delta=(N-1)\tau+N\delta<H.
\]

Thus every input burst is active and every applied burst finishes before \(T\).

For adjacent bursts,

\[
s_{j+1}-(s_j+\delta)=\tau>0,
\]

\[
t_{j+1}-(t_j+\delta)=\tau>0,
\]

and, critically,

\[
t_j+\delta=s_{j+1}.
\]

Therefore the input intervals are mutually disjoint, the applied-noise intervals are mutually disjoint, and every preceding applied increment has been observed before the next amplitude is selected.

Specifically, with

\[
Z_j^{(\delta)}
=\frac{W_{t_j+\delta}-W_{t_j}}{\sqrt\delta},
\qquad
a_j^{(\delta)}
=h_j(Z_1^{(\delta)},\ldots,Z_{j-1}^{(\delta)}),
\]

each \(a_j^{(\delta)}\) is \(\mathcal F_{s_j}\)-measurable. Holding it constant on \(I_j\) gives a progressive input. Endpoint conventions do not affect the time integrals.

The path input norm is exactly

\[
\|w^{(\delta)}\|_T^2
=\sum_{j=1}^N |a_j^{(\delta)}|^2.
\]

**Important distinction:** the stated upper bound on \(\delta\) does not imply \(\delta\le\tau\). A burst’s own input interval and applied interval overlap when \(\delta>\tau\). This does not invalidate the construction because its amplitude is already fixed at \(s_j\). If one wants *all* input and applied intervals to have disjoint interiors, the additional restriction

\[
0<\delta<\min\!\left(\tau,\frac{T-N\tau}{N}\right)
\]

suffices and leaves the \(\delta\downarrow0\) family available. No such stronger restriction is needed for the source’s causality claim.

### 2.2 Long lag prevents active feedback from applied noise

If

\[
H=T-\tau\le\tau,
\]

all active input times lie in \([0,H]\subseteq[0,\tau]\). The complete active profile is therefore \(\mathcal F_\tau\)-measurable as an \(L^2[0,H]\)-valued random variable. Brownian increments after \(\tau\) are independent of \(\mathcal F_\tau\).

Consequently, conditional on \(\mathcal F_\tau\), the active input is fixed and the shifted output is a centered Gaussian with covariance

\[
\int_0^H(F_sw_s)\otimes(F_sw_s)\,ds.
\]

This verifies the physical conditioning interface used in F494 §7. At \(H=\tau\), observing the single endpoint does not create a positive-duration active-input interval that can react to subsequent applied noise.

Equivalently, a schedule with \(N\ge2\) requires \(2\tau<T\); it cannot exist in the long-lag regime \(T\le2\tau\).

This does not independently re-prove every compactness step defining \(D_H\), but it finds no anticipative substitution in the source’s conditional reduction.

## 3. Scalar impulse Gram interface

For the manifest-named scalar law

\[
P=0,\qquad B=C=1,
\]

the output Hilbert space is \(\mathcal H=L^2[0,H]\), and

\[
F_s(u)=\mathbf1_{\{u\ge s\}}.
\]

For \(s,t\in[0,H]\),

\[
\boxed{\langle F_s,F_t\rangle=H-\max(s,t).}
\]

Indeed, the product of the two indicators is one precisely on \([\max(s,t),H]\).

Hence

\[
\|F_s\|^2=H-s,
\qquad
\boxed{\|F_s-F_t\|^2=|s-t|.}
\]

These are exact integral identities, not quadrature approximations.

For \(q\in(0,H)\), let \(f=F_0\) and \(g=F_q\). They are nonzero and noncollinear: \(g\) vanishes on \([0,q)\), whereas \(f\) does not. Their Gram determinant is

\[
\det
\begin{pmatrix}
H&H-q\\
H-q&H-q
\end{pmatrix}
=q(H-q)>0.
\]

## 4. Two-atom covariance and the §6.3 distribution identity

Take atom masses \(1-\theta,\theta\), with \(0<\theta<1\), at \(0,q\). Set \(d=H-q\). In an orthonormal basis with \(f=\sqrt H\,e_1\), write

\[
g=\alpha e_1+\beta e_2,
\qquad
\alpha=\frac d{\sqrt H},
\qquad
\beta^2=\frac{qd}{H}>0.
\]

The covariance operator

\[
Q=(1-\theta)f\otimes f+\theta g\otimes g
\]

has matrix

\[
\begin{pmatrix}
(1-\theta)H+\theta\alpha^2&\theta\alpha\beta\\
\theta\alpha\beta&\theta\beta^2
\end{pmatrix}.
\]

Therefore

\[
\boxed{\operatorname{tr}Q=H-\theta q},
\qquad
\boxed{\det Q=\theta(1-\theta)q(H-q)>0}.
\]

Its two nonzero eigenvalues are

\[
\lambda_\pm
=\frac{\operatorname{tr}Q
\pm\sqrt{(\operatorname{tr}Q)^2-4\det Q}}2,
\]

and both are positive.

### 4.1 Why the expression in F494 §6.3 is correct in distribution

The direct Gaussian realization is

\[
Y=\sqrt{1-\theta}\,fX+\sqrt\theta\,gY_0,
\]

where \(X,Y_0\) are independent standard normals. Its squared norm contains a cross term.

Define

\[
L=
\begin{pmatrix}
\sqrt{1-\theta}\sqrt H&\sqrt\theta\,\alpha\\
0&\sqrt\theta\,\beta
\end{pmatrix}.
\]

The direct squared norm is the quadratic form with matrix \(L^\top L\). The expression used in the source,

\[
(1-\theta)H X^2+\theta(\alpha X+\beta Y_0)^2,
\]

is the quadratic form with matrix \(LL^\top\).

The matrices \(L^\top L\) and \(LL^\top\) have the same eigenvalues. Orthogonal invariance of a standard Gaussian vector consequently gives

\[
\boxed{
\|Y\|
\ \stackrel{\mathrm{law}}=
\sqrt{(1-\theta)H X^2+\theta(\alpha X+\beta Y_0)^2}.
}
\]

This is a **distributional identity**, not a pathwise identity under the displayed shared \(X,Y_0\). Thus the expression in §6.3 is not a missing-cross-term defect.

The same argument applies to the source’s general two-dimensional decomposition \(f=c_He_1\), \(g=\alpha e_1+\beta e_2\).

### 4.2 The scalar strict-lower mechanism reconstructs

Let

\[
j(\theta)
=\mathbb E\sqrt{(1-\theta)H X^2+\theta(\alpha X+\beta Y_0)^2}.
\]

For \(X\ne0\), the right derivative of the integrand at zero is

\[
\frac{(\alpha X+\beta Y_0)^2-HX^2}
     {2\sqrt H\,|X|}.
\]

The term involving \(\beta^2Y_0^2/|X|\) has infinite positive expectation. The mixed term and the terms proportional to \(|X|\) are integrable. The difference quotients increase as \(\theta\downarrow0\), by concavity in \(\theta\), and are bounded below by \(-\sqrt H\,|X|\).

Adding this integrable lower bound justifies monotone convergence and yields

\[
j'(0+)=+\infty.
\]

Hence, for sufficiently small positive \(\theta\),

\[
j(\theta)>j(0)=\sqrt{2/\pi}\sqrt H.
\]

This reconstructs the scalar two-atom strict-improvement mechanism. It is not a numerical evaluation of the maximizing measure or of \(D_H\).

## 5. Actual deterministic rectangular bursts

Atoms are limits, not actual \(L^2\) inputs. Their finite-width replacements must retain the integrated covariance.

Let \(I_i=[q_i,q_i+\ell_i]\subseteq[0,H]\) have disjoint interiors, with \(\ell_i>0\), and let \(p_i\ge0\), \(\sum_i p_i=1\). Define

\[
v(s)=\sum_i\sqrt{\frac{p_i}{\ell_i}}\,
\mathbf1_{I_i}(s).
\]

This is deterministic and has input norm one. Its shifted output is

\[
Y(u)=\int_0^u v(s)\,d\beta_s.
\]

### 5.1 Exact integrated covariance

For \(u,v\in[0,H]\),

\[
\boxed{
\mathbb E[Y(u)Y(v)]
=
\sum_i\frac{p_i}{\ell_i}
\min\!\left(\ell_i,\,[\min(u,v)-q_i]_+\right).
}
\]

Equivalently,

\[
Q_{\rm rect}
=\sum_i\frac{p_i}{\ell_i}
\int_{q_i}^{q_i+\ell_i}F_s\otimes F_s\,ds.
\]

Its trace is exactly

\[
\boxed{
R:=\operatorname{tr}Q_{\rm rect}
=\sum_i p_i\left(H-q_i-\frac{\ell_i}{2}\right)>0.
}
\]

A nonzero finite-width rectangle does not have the rank-one covariance of its limiting atom.

For an additional exact covariance invariant, put \(d_i=H-q_i\). The diagonal contribution to \(\operatorname{tr}(Q_{\rm rect}^2)\), divided by \(p_i^2\), is

\[
d_i^2-\frac43d_i\ell_i+\frac12\ell_i^2.
\]

If \(I_i\) precedes \(I_j\), the corresponding off-diagonal integral, divided by \(p_ip_j\), is

\[
d_j^2-d_j\ell_j+\frac13\ell_j^2.
\]

Thus

\[
\boxed{
\operatorname{tr}(Q_{\rm rect}^2)
=
\sum_i p_i^2
\left(d_i^2-\frac43d_i\ell_i+\frac12\ell_i^2\right)
+
2\sum_{i<j}p_ip_j
\left(d_j^2-d_j\ell_j+\frac13\ell_j^2\right).
}
\]

No numerical integration enters these formulas.

### 5.2 Positive expected-path-norm bounds

Let \(\kappa=\sqrt{2/\pi}\). For a centered Hilbert-space Gaussian with trace \(R\), spectral decomposition and Cauchy–Schwarz give

\[
\mathbb E\|Y\|\ge\kappa\sqrt R.
\]

Indeed, with covariance eigenvalues \(\lambda_k\) and \(p_k=\lambda_k/R\),

\[
\sqrt{\sum_k p_k Z_k^2}\ge\sum_k p_k|Z_k|,
\]

and taking expectations proves the inequality.

For an actual nonzero rectangular burst, the covariance has rank at least two. One direct certificate is

\[
R^2-\operatorname{tr}(Q_{\rm rect}^2)>0.
\]

Its integral representation contains, for \(s<t\) inside any positive-energy interval, the strictly positive factor

\[
(H-s)(H-t)-(H-t)^2=(H-t)(t-s).
\]

Thus the lower inequality is strict. Jensen’s upper inequality is also strict because a nonzero Gaussian vector cannot have constant norm. Consequently,

\[
\boxed{
0<\kappa\sqrt R
<
\mathbb E\|Y\|_{\mathcal H}
<
\sqrt R.
}
\]

These are bounds for the literal expected path norm. The upper endpoint \(\sqrt R\) is the RMS output, not its expected norm.

An explicitly evaluable projection bound is also available. For the unit vector \(\phi=F_0/\sqrt H\),

\[
V:=\operatorname{Var}\langle Y,\phi\rangle
=
\frac1H\sum_i p_i
\left(d_i^2-d_i\ell_i+\frac{\ell_i^2}{3}\right)>0,
\]

so

\[
\mathbb E\|Y\|\ge\kappa\sqrt V.
\]

### 5.3 Exact comparison with moving atomic Gaussians

Define

\[
Z_i^{(\ell_i)}
=
\frac{\beta_{q_i+\ell_i}-\beta_{q_i}}{\sqrt{\ell_i}},
\qquad
A_{\boldsymbol\ell}
=\sum_i\sqrt{p_i}\,F_{q_i}Z_i^{(\ell_i)}.
\]

The \(Z_i^{(\ell_i)}\) are independent standard normals for disjoint intervals. Hilbert-space Itô isometry and \(\|F_s-F_{q_i}\|^2=s-q_i\) give

\[
\boxed{
\mathbb E\|Y-A_{\boldsymbol\ell}\|^2
=\sum_i\frac{p_i\ell_i}{2}.
}
\]

Therefore

\[
\left|\mathbb E\|Y\|-\mathbb E\|A_{\boldsymbol\ell}\|\right|
\le
\sqrt{\sum_i\frac{p_i\ell_i}{2}}.
\]

The distribution of \(A_{\boldsymbol\ell}\) is the desired fixed atomic Gaussian law, even though its realization changes with the widths. This proves the expected-norm approximation needed to transfer the strict two-atom improvement to actual deterministic \(L^2\) inputs. It does not compute \(D_H\).

## 6. Finding: replace fixed-normal \(L^2\) convergence with a moving comparison

**Priority:** P2  
**Mathematical classification:** MINOR, locally repairable; no fatal or major defect established in the scoped gain interfaces  
**Confidence:** 1.00  
**File path:** `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f494-stochastic-hinf-positive-lag-adapted-operator-frontier/review-v1.md`  
**Line start:** 329  
**Line end:** 333

**Body:** For the nonzero burst considered in §6.1, the displayed integral is the squared error relative to \(F_0a\,Z_\delta\), where \(Z_\delta=(W_{\tau+\delta}-W_\tau)/\sqrt\delta\), not relative to one fixed random variable \(F_0a\,Z\). The standardized nested Brownian increments are not \(L^2\)-Cauchy, so the asserted fixed-space \(L^2(\Omega;\mathcal H)\) convergence is false. Replace it with convergence in law plus convergence of expected norms, justified by the moving comparison; this repairs the statement without changing the lower bound \(L_\tau\ge\sqrt{2/\pi}\,c_H\).

### 6.1 Exact obstruction to a fixed-space limit

For \(0<\delta,\eta\),

\[
\boxed{
\mathbb E[Z_\delta Z_\eta]
=\frac{\min(\delta,\eta)}{\sqrt{\delta\eta}}
=\sqrt{\frac{\min(\delta,\eta)}{\max(\delta,\eta)}}.
}
\]

For any fixed \(0<\rho<1\), set \(\eta=\rho\delta\). Then

\[
\boxed{
\mathbb E|Z_\delta-Z_{\rho\delta}|^2
=2(1-\sqrt\rho)>0.
}
\]

This does not tend to zero with \(\delta\). For \(f=F_0a\ne0\),

\[
\mathbb E\|fZ_\delta-fZ_{\rho\delta}\|^2
=2\|f\|^2(1-\sqrt\rho)>0.
\]

Thus no fixed \(L^2\) limit exists for these moving comparison vectors.

The actual burst output \(Y_\delta\) satisfies

\[
\mathbb E\|Y_\delta-fZ_\delta\|^2
=
\frac1\delta\int_0^\delta
\|(F_s-F_0)a\|^2\,ds
\longrightarrow0.
\]

If \(Y_\delta\) had a fixed \(L^2\) limit, the moving comparison vectors would be \(L^2\)-Cauchy as well, contradicting the preceding identity.

### 6.2 Correct replacement and downstream consumer

Because every \(Z_\delta\) has the standard normal law,

\[
Y_\delta\Rightarrow fZ,
\]

and

\[
\left|\mathbb E\|Y_\delta\|-\kappa\|f\|\right|
\le
\left(\mathbb E\|Y_\delta-fZ_\delta\|^2\right)^{1/2}
\longrightarrow0.
\]

For the scalar law, the error is exactly

\[
\boxed{\mathbb E\|Y_\delta-F_0Z_\delta\|^2=\delta/2.}
\]

The direct consumer is the lower bound at S1 LF336–339. That consumer needs convergence of expected norms, not fixed-space \(L^2\) convergence. It therefore survives the correction. The later positivity and lower-bound uses likewise do not become counterexamples to the gain formula because of this wording defect.

## 7. Adapted lower-family consumer: distributional limit is enough

F494 §8 states an expected-norm limit for the causal amplitudes \(a_j^{(\delta)}=h_j(Z_{<j}^{(\delta)})\). It can be justified without identifying all widths with one fixed collection of Gaussian variables.

Put

\[
q_j=(j-1)\tau,
\qquad
\widetilde Y_\delta
=\sum_{j=1}^N F_{q_j}
h_j(Z_{<j}^{(\delta)})Z_j^{(\delta)}.
\]

At every \(\delta\), the vector \((Z_1^{(\delta)},\ldots,Z_N^{(\delta)})\) has the same independent-standard-normal law. Hence \(\widetilde Y_\delta\) has the claimed limiting law for every \(\delta\).

The actual shifted output is

\[
Y_\delta
=
\sum_j\delta^{-1/2}
\int_{s_j}^{s_j+\delta}
F_s a_j^{(\delta)}\,d\beta_s.
\]

The difference from \(\widetilde Y_\delta\) is an admissible stochastic integral. Applied-noise intervals are disjoint, and the coefficient for each interval is measurable before that interval begins. Therefore Itô isometry applies to the complete difference integral; dependence of later amplitudes on earlier increments does not introduce cross terms.

If \(|h_j|\le M_j\), continuity of \(F_s\) gives

\[
\mathbb E\|Y_\delta-\widetilde Y_\delta\|^2
\le
\sum_j M_j^2
\sup_{s\in[s_j,s_j+\delta]}
\|F_s-F_{q_j}\|_{\rm op}^2
\longrightarrow0.
\]

For the scalar law this is more explicit:

\[
\boxed{
\mathbb E\|Y_\delta-\widetilde Y_\delta\|^2
=
\delta\sum_{j=1}^N
\left(j-\frac12\right)
\mathbb E|h_j(Z_{<j})|^2.
}
\]

The denominator

\[
\mathbb E\sqrt{\sum_j|h_j(Z_{<j}^{(\delta)})|^2}
\]

is independent of \(\delta\). Consequently, when it is positive, the expected-norm ratio converges to the Gaussian expression used in the source’s lower bound.

This verifies the lower-family consumer at its stated scope. It does not establish sharpness, an optimal policy, or a fixed-space \(L^2\) limit under reused Gaussian symbols.

## 8. Required mutant controls

| Mutant | Exact diagnosis |
|---|---|
| Treating \(\mathcal G_s=\mathcal F_{\tau+s}\) as the input filtration | Adds \(\tau\) units of preview. The shifted output formula does not authorize coefficients depending on all of \(\mathcal G_s\). |
| Starting the second input at \(\delta\) while using the first applied increment | The increment ends at \(\tau+\delta>\delta\). For \(0<\delta<\tau\), it is entirely future at the proposed selection time. The source’s bounded nonconstant \(h_2\) is therefore not an admissible \(\mathcal F_\delta\)-measurable amplitude under this mutation. |
| Confusing \(s_j\) with \(t_j\) | \(s_j\) is the input selection time; \(t_j=s_j+\tau\) is the application time. The valid observation identity is \(t_j+\delta=s_{j+1}\). |
| Inferring own input/applied disjointness from the source’s \(\delta\) bound | Not implied when \(\delta>\tau\); also not required for causality. Add \(\delta<\tau\) only if that stronger geometry is desired. |
| Dropping zero prehistory | Removes the guarantee of zero output before \(\tau\) and changes the zero-gain case \(\tau\ge T\). The source already explains that an uncharged history with positive finite expected output norm makes the ratio unbounded as charged input tends to zero. |
| Replacing expected path norm by RMS | The rectangular calculation gives \(\mathbb E\|Y\|<\sqrt{\mathbb E\|Y\|^2}=\sqrt R\). These criteria are not interchangeable. |
| Turning Jensen into equality | A nonzero Gaussian norm is not almost surely constant. In the two-atom case, \(\det Q>0\) additionally certifies two positive covariance directions. |
| Equating the two §6.3 quadratic forms pathwise | They have the same distribution through the spectra of \(L^\top L\) and \(LL^\top\); their shared-normal realizations need not be identical. |
| Reusing \(Z\) as a fixed-space limit across nested widths | Nested standardized increments have covariance \(\sqrt{\min/\max}\) and fail the \(L^2\)-Cauchy criterion. A moving comparison repairs the expected-norm argument. |
| Treating finite-width rectangles as exact atoms | Their covariance is the integrated kernel in §5, not a finite-rank atomic covariance. The approximation error is explicit and vanishes only with widths. |

## 9. Complete prospective exact-arithmetic source and argv — NOT RUN

**Purpose:** bounded rational calculations of timing endpoints, scalar Gram/covariance invariants, actual rectangular covariance moments, and nested-width covariance distances. No sampling, Gaussian-integral evaluation, quadrature, Bellman/Itô proof, or universal gain certification.

**Execution status:** NOT RUN. The following fixtures are declared prospective inputs only; no numerical outputs from them are claimed.

The program uses only the Python standard library, no files, network, subprocesses, installation, or background work. It emits a finite stdout report. Its loop bound is \(N\le8\), and rational input numerator/denominator bit lengths are limited. The intended calculation is modest and subject to the manifest’s 55-second bound; no observed runtime is claimed.

### Exact argv

For each invocation:

- argv[0]: `python3`
- argv[1]: `-I`
- argv[2]: `-S`
- argv[3]: `-c`
- argv[4]: the complete source below, obtained by removing each `Lnnn|` prefix and joining the remaining lines with LF, retaining indentation verbatim.
- argv[5] onward, first invocation: `3`, `1`, `1/8`, `1/2`, `1/2`, `1/2`, `2`.
- argv[5] onward, second invocation: `3`, `2`, `1/8`, `1/2`, `1/2`, `1/2`, `1`.

The seven scientific arguments, in order, are \(T,\tau,\delta,q,\theta,r,N\), with nested width \(\eta=r^2\delta\). These two invocations separately expose the short-lag and long-lag timing interfaces. They are not proposed Gaussian gain measurements.

### Complete source

L001|import sys  
L002|import time  
L003|from fractions import Fraction as F  
L004|  
L005|started = time.monotonic()  
L006|  
L007|def need(condition, message):  
L008|    if not condition:  
L009|        raise ValueError(message)  
L010|  
L011|def emit(name, value):  
L012|    print(str(name) + " = " + str(value))  
L013|  
L014|need(len(sys.argv) == 8, "Expected T tau delta q theta r N")  
L015|values = tuple(F(x) for x in sys.argv[1:7])  
L016|need(all(max(abs(x.numerator).bit_length(),  
L017|             x.denominator.bit_length()) <= 32  
L018|         for x in values), "Input fraction exceeds finite bound")  
L019|T, tau, delta, q, theta, r = values  
L020|N = int(sys.argv[7])  
L021|need(1 <= N <= 8, "N outside this finite calculator's scope")  
L022|need(T > 0 and tau > 0 and delta > 0, "Positive times required")  
L023|need(0 < theta < 1 and 0 < r < 1, "Interior weights required")  
L024|H = max(F(0), T - tau)  
L025|emit("execution scope", "Exact finite interfaces; no gain evaluation")  
L026|emit("zero prehistory", "Assumed, not inferred from a scalar input")  
L027|emit("H", H)  
L028|if H == 0:  
L029|    emit("zero-history output", "Zero on the stated horizon")  
L030|    sys.exit(0)  
L031|need(N * (tau + delta) < T, "Burst schedule exceeds horizon")  
L032|need(delta <= q and q + delta <= H, "Rectangles must be disjoint and active")  
L033|need(0 < q < H, "Two-atom time must be interior")  
L034|emit("long-lag interface H <= tau", H <= tau)  
L035|emit("N tau < T", N * tau < T)  
L036|previous_applied_end = None  
L037|for j in range(1, N + 1):  
L038|    s = (j - 1) * (tau + delta)  
L039|    t = s + tau  
L040|    need(s + delta < H and t + delta < T, "Inactive burst")  
L041|    if previous_applied_end is not None:  
L042|        need(previous_applied_end == s, "Observation is not available at selection")  
L043|    emit("burst " + str(j), (s, s + delta, t, t + delta))  
L044|    previous_applied_end = t + delta  
L045|emit("adjacent input gap", tau)  
L046|emit("adjacent applied gap", tau)  
L047|emit("own input/applied overlap length", max(F(0), delta - tau))  
L048|emit("mutant input-two-at-delta observation deficit", tau)  
L049|d = H - q  
L050|alpha2 = d * d / H  
L051|beta2 = q * d / H  
L052|atom_trace = H - theta * q  
L053|atom_det = theta * (1 - theta) * q * d  
L054|c00 = (1 - theta) * H + theta * alpha2  
L055|c11 = theta * beta2  
L056|c01_squared = theta * theta * alpha2 * beta2  
L057|need(c00 + c11 == atom_trace, "Covariance trace mismatch")  
L058|need(c00 * c11 - c01_squared == atom_det > 0, "Covariance determinant mismatch")  
L059|g00 = (1 - theta) * H  
L060|g11 = theta * d  
L061|g01_squared = theta * (1 - theta) * d * d  
L062|need(g00 + g11 == atom_trace, "Gram trace mismatch")  
L063|need(g00 * g11 - g01_squared == atom_det, "Gram determinant mismatch")  
L064|emit("unweighted impulse Gram determinant", q * d)  
L065|emit("two-atom covariance trace", atom_trace)  
L066|emit("two-atom covariance determinant", atom_det)  
L067|rectangles = ((F(0), delta, 1 - theta), (q, delta, theta))  
L068|R = F(0)  
L069|HS = F(0)  
L070|V = F(0)  
L071|comparison_error2 = F(0)  
L072|for a, length, mass in rectangles:  
L073|    distance = H - a  
L074|    second = distance * distance - distance * length + length * length / 3  
L075|    diagonal = distance * distance - F(4, 3) * distance * length + length * length / 2  
L076|    R += mass * (distance - length / 2)  
L077|    HS += mass * mass * diagonal  
L078|    V += mass * second / H  
L079|    comparison_error2 += mass * length / 2  
L080|HS += 2 * (1 - theta) * theta * (d * d - d * delta + delta * delta / 3)  
L081|need(R > 0 and 0 < V <= R, "Positive expected-norm bound unavailable")  
L082|need(0 < HS < R * R, "Rectangular rank certificate failed")  
L083|emit("rectangular covariance trace R", R)  
L084|emit("rectangular covariance trace Q squared", HS)  
L085|emit("rectangular projection variance V", V)  
L086|emit("rectangular moving-atom squared error", comparison_error2)  
L087|emit("expected-norm bounds", "sqrt(2/pi)*sqrt(R) < E norm < sqrt(R)")  
L088|eta = r * r * delta  
L089|normalized_increment_covariance = r  
L090|normalized_increment_distance2 = 2 * (1 - r)  
L091|output_inner_product = r * (H - eta / 2)  
L092|output_distance2 = (H - delta / 2) + (H - eta / 2) - 2 * output_inner_product  
L093|need(0 < eta < delta < H, "Nested widths outside active interval")  
L094|need(normalized_increment_distance2 > 0 and output_distance2 > 0, "Nested-distance identity failed")  
L095|emit("nested width eta", eta)  
L096|emit("nested standardized-increment covariance", normalized_increment_covariance)  
L097|emit("nested standardized-increment squared distance", normalized_increment_distance2)  
L098|emit("actual scalar burst-output squared distance", output_distance2)  
L099|emit("single-burst moving-comparison squared error", delta / 2)  
L100|emit("fixed-normal convergence", "Not established; nested distances preclude it as widths shrink")  
L101|emit("uncomputed quantities", "Gaussian expected norm, D_H, adapted gain, optimizer, attainment")  
L102|if time.monotonic() - started > 55:  
L103|    raise RuntimeError("Calculation exceeded prospective 55-second bound")  

No output from this source is evidence in the present return. The identities proved in §§2–7 are written mathematics, not fabricated program results.

## 10. Claim-by-claim disposition and exact unpaid scope

| Claim/interface | Disposition |
|---|---|
| \(N\tau<T\), horizon constraints, selection/application endpoints | Reconstructed for all stated \(N,\tau,\delta,T\). |
| Previous applied increments available at the next input selection | Reconstructed using \(t_j+\delta=s_{j+1}\). |
| Mutual disjointness within the input family and within the applied family | Reconstructed. Own input/applied disjointness needs the optional stronger \(\delta<\tau\). |
| No active feedback from applied increments when \(H\le\tau\) | Reconstructed, including \(H=\tau\). |
| Scalar Gram kernel \(H-\max(s,t)\), noncollinearity, two-atom positive determinant | Reconstructed exactly. |
| §6.3 Gaussian expression | Correct in distribution; not asserted pathwise. |
| Actual rectangular covariance, trace, squared-covariance trace, positive expected-norm bounds | Reconstructed exactly; no quadrature or gain value. |
| Fixed-space \(L^2\) burst limit in §6.1 | Incorrect as stated; one local MINOR finding, corrected by a moving comparison. |
| Expected-norm single-burst lower limit | Preserved by the corrected argument. |
| Adapted lower-family expected-norm limit | Reconstructed with moving Gaussian vectors and actual physical filtration. |
| Finite arithmetic executions | NOT RUN because of the role restriction. |
| Bellman/generalized-Itô import, global \(D_H\) optimization, general short-lag gain, attainment, controller synthesis, source equivalence, novelty | Not verified or resolved by this assignment. |

**FATAL:** none established in the assigned interfaces.  
**MAJOR:** none established in the assigned interfaces.  
**MINOR:** one false fixed-space coupling/convergence statement, with a complete repair above.

No scientific result is inferred from a held episode, from an unexecuted program, or from a numerical success rate.

## Verdict fields

**overall_correctness:** incorrect

**explanation:** F494 §6.1 incorrectly asserts fixed-space \(L^2\) convergence of shrinking Brownian bursts to one fixed Gaussian vector; nested standardized increments are not \(L^2\)-Cauchy. The moving-comparison repair preserves the expected-norm lower bound, and the other specifically assigned timing, scalar Gram, two-atom distribution, and rectangular-covariance interfaces reconstruct at the scopes stated above.

**confidence:** 0.99