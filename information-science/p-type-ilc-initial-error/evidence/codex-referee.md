**Verdicts: A — correct with fixes; B — correct; C — correct with fixes.** I found no counterexample to B under its stated quantifiers. The main estimate in C is also sound; its signal regularity and domain assumptions need to be explicit.

**A — Correct with fixes.** In [§2](/Users/jinleic/jinleic-workspace/ai4s/p-type-ilc-initial-error/work/theorems.md:47), the factorial estimate establishes quasinilpotence, hence
\[
\sigma(I-GL)=\{1\},\qquad \|I-GL\|\ge1
\]
in every equivalent norm. The compatible closed subspace \(e(0)=0\) does not remove this obstruction. Spectra should be understood on the complexifications of the real spaces.

The load-bearing defect is the hypothesis **“bounded pointwise gain”** in the statement about both \(GL\) and \(LG\) on \(C([0,T])\). A discontinuous gain need not preserve continuity. For example, with \(G=J\), \(L(t)=\mathbf1_{\{t>t_0\}}\), and \(v=1\),
\[
(LGv)(t)=t\mathbf1_{\{t>t_0\}}\notin C([0,T]).
\]
A nonmeasurable bounded gain can even leave \(GL\) undefined.

Repair: require continuous \(L\) for the stated \(C\)-space theorem, or formulate the bounded measurable case on suitable \(L^\infty\) spaces. Constant P0 gains satisfy the continuous-gain requirement.

The nonlinear conclusion is valid for a \(C^1\) input-output map with fixed initial state: formulate the learning derivative on input space as \(I-LG\). Spectral radius one excludes a local Banach contraction; it supplies no divergence theorem.

**B — Correct.** The generating function in [§3](/Users/jinleic/jinleic-workspace/ai4s/p-type-ilc-initial-error/work/theorems.md:91) checks out independently. Write \(A=J^q\), \(V=I-\ell A\), and let \(\mathbf1\) denote the constant function. Then
\[
\begin{aligned}
H_q(z,\cdot)
&=\mathbf1-\ell zA(I-zV)^{-1}\mathbf1\\
&=(1-z)(I-zV)^{-1}\mathbf1\\
&=\left(I+\frac{\ell z}{1-z}J^q\right)^{-1}\mathbf1\\
&=\sum_{k\ge0}
 \left(-\frac{\ell z}{1-z}\right)^k
 \frac{t^{qk}}{(qk)!}.
\end{aligned}
\]
Thus the claimed \(E_q\) formula is correct. Volterra quasinilpotence justifies the inverse and analyticity throughout \(|z|<1\).

Every boundary case works:

- **\(\ell<0\):** along the real radius, the argument tends to \(+\infty\); even the first two nonnegative terms prove unboundedness.
- **\(\ell>0,q=1\):** the radial limit is zero, whereas \(z=iR/(1+iR)\) lies inside the disk and gives \(|H_1|=1\). Continuity at \(1\) fails.
- **\(\ell>0,q=2\):** the displayed cosine oscillates without a limit.
- **\(\ell>0,q\ge3\):** the root-of-unity formula is exact. The angles \(\pm\pi/q\) uniquely maximize the real exponent. One can take
  \[
  c_q=\cos(3\pi/q)<\cos(\pi/q).
  \]
  Along \(R_k=2\pi k/\sin(\pi/q)\), the dominant cosine equals one and the remainder is exponentially smaller. These are genuine radial approaches, with
  \[
  z_k=\frac{R_k^q}{R_k^q+\ell t_*^q}\uparrow1.
  \]
  There is no unresolved branch choice: \(R_k\) is positive real.

Consequently \(\sum_n|h_n(t_*)|=\infty\). The [uniform-boundedness step](/Users/jinleic/jinleic-workspace/ai4s/p-type-ilc-initial-error/work/theorems.md:130) is valid on the **real** Banach space \(\ell^\infty(\mathbb N_0)\), since
\[
\|F_i\|=\sum_{n=0}^{i}|h_n(t_*)|.
\]
It supplies one infinite bounded real sequence; scaling gives any prescribed \(\epsilon_0>0\). Every individual trial still has a smooth, finite-horizon solution.

The exact quantifier is
\[
\forall t_*>0\;\exists a\in\ell^\infty:
\quad \sup_i|y_i(t_*)|=\infty.
\]
The sequence may depend on \(t_*\). The proof does **not** establish one sequence working simultaneously at every positive time. The stated quantifier already disproves robustness.

For every fixed finite \(\lambda\),
\[
\|y_i\|_\lambda\ge e^{-\lambda t_*}|y_i(t_*)|,
\]
so the weighted-norm conclusion follows directly.

For **\(\ell=0\)**, this zero-reference experiment has bounded outputs. To disprove general nominal convergence, explicitly choose \(y_d(t)=t^q/q!\), \(u_d=1\), zero initial states, and \(u_0=0\). Actual outputs remain zero. A reference requiring nonzero input makes the edge-case argument precise.

**C — Correct with fixes.** The analytic calculations in [§4](/Users/jinleic/jinleic-workspace/ai4s/p-type-ilc-initial-error/work/theorems.md:144) are correct:

- The disturbance contribution is exactly \(J\eta_{i,1}+\cdots+J^q\eta_{i,q}\); the integration indices are correct.
- Injectivity of \(J^q\) preserves basis independence. Continuity then makes \(W\) positive definite.
- With \(e_i=\psi^\top a_i-d_i\), the recurrence has the stated **positive** disturbance sign:
  \[
  a_{i+1}=(1-\gamma)a_i+\gamma b_i.
  \]
- The continuous projection kernel gives the stated finite sup-norm operator norm \(\kappa\).

Indeed, putting \(\rho=1-\gamma\) gives the exact error identity
\[
e_i=\rho^i\psi^\top a_0+
\gamma\sum_{k=0}^{i-1}\rho^{i-1-k}Pd_k-d_i.
\]
Therefore the slightly sharper estimate is
\[
\|e_i\|_\infty
\le \rho^i\|\psi^\top a_0\|_\infty
+\bigl[1+\kappa(1-\rho^i)\bigr]\delta,
\]
which implies the displayed bound. Coefficients, virtual inputs, and chain states are uniformly bounded.

Two hypothesis repairs are needed:

1. **Specify signal regularity.** The update and disturbance integrals require measurable signals. State the result for continuous disturbances, or for measurable \(L^\infty\) disturbances with Carathéodory solutions and essential-sup norms. Literally arbitrary bounded functions need not be integrable.

2. **Make the domain assumption explicit for physical-input boundedness.** The [last sentence of the proof](/Users/jinleic/jinleic-workspace/ai4s/p-type-ilc-initial-error/work/theorems.md:210) requires \(a,b\) continuous on the entire common compact state-time set. Bounded states alone do not ensure compact containment in a local normal-form domain.

   A counterexample to that inference uses \(q=T=1\), domain \(x<1\),
   \[
   a(x)=\frac1{1-x},\quad b=1,\quad \phi=1,\quad
   y_d=0,\quad \gamma=1,\quad \theta_0=0,
   \]
   with zero disturbances and initial states
   \[
   \alpha_i=1-\frac1{i+2}.
   \]
   The update gives \(\theta_{i+1}=-3\alpha_i/2\). States
   \(x_i(t)=\alpha_i+\theta_i t\) remain uniformly bounded inside the domain, but
   \[
   u_i(0)=\theta_i-(i+2)\longrightarrow-\infty.
   \]
   Repair: assume globally defined coefficients with the stated lower bound on \(|b|\), or require uniform compact containment within the normal-form domain.

C also retains every substantive restriction stated in the draft: exact known cancellation, exact full-state measurements despite noise on the learning-output channel, a realizable finite-dimensional reference, and no internal dynamics. Its whole-trace filter and physical feedback lie outside P0.

**Strongest defensible overall claim:** every fixed nonzero real scalar P0 gain fails universal robustness even on the \(q\)-integrator chain, for every positive integer \(q\), under arbitrarily small bounded trial-varying initial shifts. Zero gain fails general nominal tracking. C proves an explicit robustness bound for a substantially more informed controller under restricted plant and reference assumptions.

I found no unsupported simulation-to-universality leap in this draft. Its finite witnesses alone would leave an infinite-sequence quantifier gap; uniform boundedness closes that gap analytically. Simulations cannot remove C’s controller-class, information, or realizability restrictions.