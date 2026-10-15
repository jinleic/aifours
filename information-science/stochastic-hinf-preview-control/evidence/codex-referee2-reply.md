**(a) Objections 1–8**

All line references below are to [work/theory.md](/Users/jinleic/jinleic-workspace/ai4s/stochastic-hinf-preview-control/work/theory.md).

| # | Resolved? | Exact lines and remaining gap |
|---|---|---|
| 1 | **Yes** | L50–57, L231–237: uniform positivity and bounded data remove the singular-transition counterexample. |
| 2 | **Yes** | L71, L130–132, L203–207, L231–237: identities no longer assume positivity; differential equations hold a.e. A minor presentation fix would invoke Picard on an open neighborhood with uniformly positive \(\widehat R\), then establish positivity. |
| 3 | **Yes** | L195–199: the BDG/\(H^1\) estimate correctly supplies a uniformly integrable martingale. |
| 4 | **Yes** | L39–41, L176–188: uncounted incoming disturbances are explicitly zero. |
| 5 | **Yes** | L22–33: the norm replacement and its scope are now explicit. |
| 6 | **Yes** | L265–267, L436–439: the linear \(F_0\) comparison preserves the additive decomposition and gives a horizon-independent bound. |
| 7 | **Partly** | L409–425: the block argument works for \(h>0\), including adapted block inputs. At \(h=0\), every block has zero length and the argument proves nothing. |
| 8 | **Yes** | L401–407, L432–444, L457–463: positivity, support-restricted monotonicity, history-window convergence, and subsequential transversality are supplied. These arguments are sound, subject to the Lemma 9 qualifications below. |

**(b) Theorem 1 verdict**

**The equivalence, feedback, and squares identity are correct under revised F6.** No remaining substantive mathematical error found.

Two minor wording points: make the open-neighborhood Picard argument explicit at L231–237; and interpret “not attained” at L123–124 as *no strict feasibility at \(\gamma_{\rm opt}\)*. It does not establish that no controller minimizes the actual induced gain.

**(c) Theorem 2 and Lemma 9 verdict**

**The main N&S argument now works, modulo legitimate standard facts. The full stated scope still needs two minor corrections:**

1. **The \(h=0\) bounded-inverse proof is missing**: L410–420 uses blocks of length \(h\).
2. **The renewal forcing is misstated for random initial histories**: L382–386 requires an expectation of the conditional-mean outer product.

The other steps check out: steps 0–2 and 4, the \(F_0\) comparison, monotonicity, the \(\Pi'\) limit, convergence on compacts, and uniqueness. In particular, the terminal pairings in L458–462 vanish along a common subsequence because the relevant products are integrable.

The **nonzero initial window does not invalidate the subspace claim or \(\Psi\)**. Write \(y=(x;p)\), and
\[
g_0=\int_0^h[P,-I]e^{-H_0r}[C;0]v_0(r)\,dr.
\]
For deterministic initial data, the first-window mean is
\[
\bar y(s)=e^{H_0s}[x_0;Px_0+g_0]
+\int_0^s e^{H_0(s-r)}[Cv_0(r);0]\,dr.
\]
Consequently,
\[
\bar y(h)=E[I;P]\left(x_0+
\int_0^h(e^{-H_0r})_{11}Cv_0(r)\,dr\right)\in\mathcal S.
\]
Thus its subsequent \(H_\gamma\) evolution stays in \(\mathcal S\), as claimed at L372–377. The innovation propagator in L340–341 and L382 is correct.

The renewal equation at L385 **holds for deterministic nonzero \(v_0\)** when \(m\) denotes this full, forced mean. Substituting \(\Psi(s)x_0\) would be wrong. For random initial histories, the forcing must instead be
\[
f(s)=\Gamma_\sigma\,\mathbb E[m_0(s)m_0(s)^\top]\Gamma_\sigma^\top,
\qquad m_0(s)=\mathbb E[y(s)\mid\mathcal F_0].
\]

The renewal and Krein–Rutman facts are true in the forms needed here: the kernel decays exponentially under T1, and the positive map acts on a finite-dimensional PSD cone. Excitation in the converse is automatic:
\[
\left\langle\Lambda,\int f_{\rm basis}(s)\,ds\right\rangle
=\langle\Lambda,\mathcal T_P(I)\rangle
=\rho\,\operatorname{tr}\Lambda>0.
\]
The SFDE facts apply with the finite-interval \(L^2\) estimate at L411–412 supplying boundary-input admissibility. No additional irreducibility or controllability hypothesis is needed.

**(d) Numerical-evidence verdict**

**Consistent as approximation evidence; overstated as certification.**

- One sampled **discrete** controller violates its design bound: \(0.8262320114>0.8238474064\), ratio \(1.002894\). This contradicts a blanket numerical success claim, but does not contradict the continuous theorem. See [numerics.json L353–356](/Users/jinleic/jinleic-workspace/ai4s/stochastic-hinf-preview-control/evidence/numerics.json:353).
- The reported \(h=0\) “infinite-horizon bracket” \([1.72166557,1.72167435]\) excludes the same file’s scalar threshold \(1.7215205057\). Indeed, minimizing
  \[
  \gamma^2=\frac{P^2(1+0.16P)}{1.08P^2-2.41P-1}
  \]
  gives \(1.7215205056\). The bracket measures convergence within \(T_{\max}=400\), not theorem solvability: [run_evidence.py L169–175](/Users/jinleic/jinleic-workspace/ai4s/stochastic-hinf-preview-control/work/run_evidence.py:169), [shp.py L340–346](/Users/jinleic/jinleic-workspace/ai4s/stochastic-hinf-preview-control/work/shp.py:340).
- [Identities L172–205](/Users/jinleic/jinleic-workspace/ai4s/stochastic-hinf-preview-control/evidence/identities.json:172) show refinement toward the saddle identity; coarse discrepancies are about \(7.5\) and \(3.5\) Monte Carlo standard errors, so discretization bias matters. [T40 results](/Users/jinleic/jinleic-workspace/ai4s/stochastic-hinf-preview-control/evidence/long_horizon_T40.json:19) show mesh convergence. The [deterministic table](/Users/jinleic/jinleic-workspace/ai4s/stochastic-hinf-preview-control/evidence/deterministic_limit.json:4) does not certify exact thresholds or an \(h\to\infty\) limit. None of these experiments directly checks Lemma 9 with nonzero initial history.

**(e) New objections and fixes**

| Severity | Objection | Fix |
|---|---|---|
| Minor | Zero-length blocks omit \(h=0\). | Use a fixed positive block length for that case. |
| Minor | Random-history renewal forcing loses initial variance. | Use the conditional-mean second moment above; extend deterministic estimates by conditioning. |
| Major, evidential | Finite-budget convergence brackets are presented as threshold brackets. | Report mesh/time-budget uncertainty and distinguish numerical convergence failure from nonexistence. |