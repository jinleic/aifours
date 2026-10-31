# f436 WRITTEN correction review — complete return

**Disposition: additive correction supported at its stated scope.**  
**New correction findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

These counts apply only to the supplied correction. They do **not** replace f419’s historical **0 FATAL / 1 MAJOR / 0 MINOR**, certify f418’s earlier clean-review claim, or accept the whole f400 manuscript.

## 1. Frozen scope and actual methods

The object reviewed is:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-1-cutoff2-penalty-monotonicity-correction-author-v1.md`

The following bindings are **parent-attributed metadata**, not independently executed child hashes:

| Artifact | SHA256 |
|---|---|
| Manifest | `80c5b0b0bcea96bb90e8c43179a67c49234f11eeec2eeeff940a40aa8c33d54a` |
| Freeze receipt | `ac9a4abff0b62c2a848684612f8e5573fe8869c64fe6bf8dff5a243646c15b62` |
| Literal packet | `69c0c74e8708b88a81935660315041b27cd53097c6bdc0ac2a8912b7fcd9e046` |

The supplied observation `2026-10-30T11:15:12-0700 PDT` belongs to the **parent**. It is not my native start, completion time, or execution evidence.

I read the complete manifest, freeze receipt, dispatch receipt, parent metadata supply, and all seven status-only controls through their endings. I then sent the direct administrative **pre-body ACK before reading mathematical packet content**. After that ACK, I read the complete packet in consecutive raw windows of at most 20 LF: packet LF 1–1160, followed by 1161–1175. Derivation began after the complete read. A focused reread followed.

Source references below use **this f436 packet’s labels**:

- **S1 LF 1–21:** additive author correction; SHA `0ea327b3ef67c844660c9e0a57e2b69ae4dc1eea3268f7fcc632f497a62877cd`.
- **S2 LF 1–698:** complete f400 manuscript; SHA `6d907d4f950cb5ab4a1a17ad051ea061a48d7916d24547e4ff14997a46162654`.
- **S3 LF 1–454:** complete f419 review; SHA `0118598ec9ac426b28284882a0461b81eda8932b995bb44a42676a2206ddfb38`.

This is an explicitly **nonblind, targeted correction review**: S3 was an expressly frozen input. It is not a blind reconstruction unaware of the earlier finding.

No selected mathematical instance, scientific executable, CAS, interpreter, solver, enumeration, replay, external scientific source, model CLI, build, lint, or formatter was used. A read-only `git diff` restricted to the correction path returned no output; that observation neither establishes the file’s Git history nor replaces the frozen snapshot binding.

All held episodes and their consumers—including the privacy auxiliary episode, CORE-GRAM episode, AME compression episode, and PHv8/cp116—were **NONINPUT**. No excluded scientific links, unsupplied reviewer returns, author code, or current sibling results were opened. This reports actual access and methods, not cognitive isolation.

No repository file was written under this role. This is the complete body for parent materialization.

## 2. Exact mathematical scope and imports

Fix

\[
0<b<1,\qquad
m=\frac{b}{1-b}>0,\qquad
v=m(1+m),\qquad
T_2=m^2+v,
\]

and

\[
a\ge0,\qquad u=a+\frac12,\qquad
\lambda\in\mathbb R\ \text{finite}.
\]

The claim quantifies over **all \(d\ge u\)**, not merely actual optimizing scalar pairs.

The definitions used are:

1. The displayed integrands and derivatives, **S2 LF 119–163**:
   \[
   \psi_0(x,y;\lambda)
   =\frac{x^3}{3}+(y^2-\lambda)x-\frac{4y^3}{3}+\lambda y,
   \]
   \[
   g_y(z):=\psi_1(z,y;\lambda)
   =\psi_0(z,y;\lambda)+m(z^2+y^2)+T_2z,
   \]
   \[
   g_y'(z)=(z+m)^2+v+y^2-\lambda.
   \]

2. The independent clips and corrected joint pointwise profiles, **S2 LF 423–438**, together with the corner clip in **S2 LF 359–370**.

3. The exact definitions of \(h_{\rm ind}\), \(P\), and their decomposition, **S2 LF 440–476**.

The proof below reconstructs the pointwise constrained minimization needed to identify \(P\). Identification with the canonical profile value \(h\) retains the manuscript’s existing corrected-profile reduction as an explicit import. **No actual-optimizer existence, positivity, pruning, \(V<Q_*\), stationarity, or active-core theorem is needed for the monotonicity of the displayed \(P\).**

## 3. Root convention and conditional excess

### 3.1 Where \(g_y\) is nondecreasing

Put

\[
s=\lambda-v-y^2,\qquad
r=\max\{0,\sqrt{\max(s,0)}-m\}.
\]

Then

\[
g_y'(z)=(z+m)^2-s,\qquad
g_y''(z)=2(z+m)>0\quad(z\ge0).
\]

There are two exhaustive cases:

- If \(s\le m^2\), then \(r=0\), and
  \[
  g_y'(z)\ge m^2-s\ge0\qquad(z\ge0).
  \]
  This includes negative radicands and cases with no nonnegative stationary root.

- If \(s>m^2\), then \(r=\sqrt{s}-m>0\). The derivative vanishes at \(r\) and is nonnegative for \(z\ge r\).

Thus, under the complete displayed root convention,

\[
g_y\text{ is nondecreasing on }[r,\infty).
\]

There is **no** claim that it is nondecreasing below a positive root.

### 3.2 Moving independent tail box

Fix \(y\in[0,u]\). For \(d\ge u\), define

\[
U_d=2d-y,\qquad
q_d=\operatorname{clip}(r,[d,U_d])
    =\min\{U_d,\max(d,r)\}.
\]

The box is nonempty because \(d\ge u\ge y\). Both endpoints increase with \(d\), so \(q_d\) is nondecreasing.

That observation **alone does not prove** that \(g_y(q_d)\) increases: an upper-face clip may lie below the root, on the decreasing side of \(g_y\). The correction correctly supplies the additional threshold argument.

### 3.3 Conditional-excess lemma

For a **fixed** threshold \(t\) admissible at the compared parameters, meaning \(t\le U_d\), let

\[
E_d(t)=g_y(\max(q_d,t))-g_y(q_d).
\]

Conditional minimization over the tail box with the added constraint \(z\ge t\) gives

\[
\operatorname*{argmin}_{z\in[\max(d,t),U_d]}g_y(z)
=\max(q_d,t).
\]

Consequently \(E_d(t)\ge0\).

Take any \(d_-\le d_+\), both at least \(u\), with \(t\le U_{d_-}\). Admissibility at \(d_+\) follows automatically.

- If \(q_{d_-}\ge t\), monotonicity of \(q_d\) gives \(q_{d_+}\ge t\). Both excesses are zero.

- Suppose \(q_{d_-}<t\). Since \(t\le U_{d_-}\),
  \[
  q_{d_-}<U_{d_-}.
  \]
  The clip therefore cannot be an upper-face clip. Hence
  \[
  q_{d_-}=\max(d_-,r)\ge r.
  \]

  If \(q_{d_+}<t\), then
  \[
  r\le q_{d_-}\le q_{d_+}<t,
  \]
  so
  \[
  E_{d_+}(t)
  =g_y(t)-g_y(q_{d_+})
  \le g_y(t)-g_y(q_{d_-})
  =E_{d_-}(t).
  \]

  If instead \(q_{d_+}\ge t\), then \(E_{d_+}(t)=0\le E_{d_-}(t)\).

Therefore

\[
\boxed{E_d(t)\text{ is nonnegative and nonincreasing in }d.}
\]

This establishes **S1 LF 11** and independently reconstructs the central argument in **S3 LF 238–258**.

The proof covers all moving-bound crossings. In particular:

- An upper-face selection \(q_d=U_d\) forces \(q_d\ge t\), so its excess is zero—even when \(q_d<r\).
- Once the moving lower bound passes \(t\), the excess is zero.
- Root, lower-face, and upper-face ties obey the same inequalities.
- A singleton tail box has zero excess for every admissible threshold.
- The zero-root convention requires no separate unproved monotonicity assumption.

The lemma concerns fixed thresholds while \(d\) varies. It does not assert monotonicity for an arbitrary independently moving threshold \(t(d)\).

## 4. Shared-core minimization over an unchanged box

Fix a shared-core height \(y\in[0,a]\), and write

\[
A=2a-y,\qquad
p_0=\operatorname{clip}(r_0(y),[a,A]).
\]

The first-core box and its independent minimizer do not depend on \(d\). Moreover,

\[
U_d=2d-y\ge2u-y=2a+1-y=A+1.
\]

Thus every threshold \(x+1\), \(x\in[a,A]\), is admissible for every \(d\ge u\).

For fixed \(x\), conditional tail minimization gives \(z=\max(q_d,x+1)\). Subtracting the independent minima therefore yields the exact pointwise core penalty

\[
\boxed{
\kappa_d(y)=
\min_{x\in[a,A]}
\left\{
(1-b)\bigl[\psi_0(x,y)-\psi_0(p_0,y)\bigr]
+bE_d(x+1)
\right\}.}
\]

The first summand is independent of \(d\). The second is nonincreasing by §3. Thus every fixed-\(x\) expression is nonincreasing.

The domain of minimization is unchanged. More explicitly, if \(x_-\) is a minimizer at \(d_-\), then

\[
\kappa_{d_+}(y)
\le F_{d_+}(x_-)
\le F_{d_-}(x_-)
=\kappa_{d_-}(y),
\]

where \(F_d\) denotes the expression inside braces. Hence

\[
\boxed{\kappa_d(y)\ge0
\quad\text{and}\quad
\kappa_d(y)\text{ is nonincreasing in }d.}
\]

This verifies **S1 LF 13–17**. Crucially, the proof does not minimize over the changing *active-line* interval; it minimizes over the complete, unchanged first-core box.

### Agreement with the corrected joint rule

The fixed-box formula is the penalty of the joint minimizer used in **S2 LF 429–438**:

- If \(q_d\ge p_0+1\), the independent pair is feasible and has zero penalty.
- Otherwise, a joint minimum cannot have a slack coupling constraint: a slack minimum would satisfy the separate box optimality conditions and equal the infeasible independent pair. Thus \(z=x+1\).

On the active line, the feasible interval is

\[
x\in[\max(a,d-1),A].
\]

It is nonempty because

\[
d-1\le q_d-1<p_0\le A.
\]

For

\[
W_y(x)=(1-b)\psi_0(x,y)+b\psi_1(x+1,y),
\]

the relations \(b(1+m)=m\) and \(T_2=m+2m^2\) give

\[
W_y'(x)
=(1-b)d_0(x,y)+bd_1(x+1,y)
=d_1(x,y)=g_y'(x).
\]

Thus its minimizer is exactly

\[
x_d=\operatorname{clip}
\bigl(r,[\max(a,d-1),A]\bigr),
\qquad z_d=x_d+1.
\]

This reconstructs the source rule and establishes that the fixed-box minimum is the same pointwise core penalty appearing in \(P\).

## 5. Normal terms, corner penalty, and exact integral weights

### 5.1 Normal terms are retained

For \(s,t\ge0\), direct written expansion gives

\[
\psi_1(t,y)-\psi_1(s,y)
=d_1(s,y)(t-s)
 +(t-s)^2\left(\frac{t+2s}{3}+m\right)
=\mathcal B_y(t,s),
\]

and

\[
\psi_0(t,y)-\psi_0(s,y)
=d_0(s,y)(t-s)
 +(t-s)^2\frac{t+2s}{3}
=\mathcal B_y^0(t,s).
\]

If \(s\) minimizes the relevant integrand on an interval containing \(t\), its normal term satisfies

\[
d_j(s,y)(t-s)\ge0.
\]

This includes lower and upper faces: at an upper face both the derivative and allowable displacement can be nonpositive. At a singleton the displacement is zero. No normal term is discarded merely because the minimizing coordinate is clipped rather than stationary.

For the core, \(p_0,x_d\in[a,A]\) and \(q_d,z_d\in[d,U_d]\). Therefore

\[
\kappa_d(y)
=(1-b)\mathcal B_y^0(x_d,p_0)
+b\mathcal B_y(z_d,q_d).
\]

This is exactly the core integrand in **S2 LF 461–465**.

### 5.2 Corner block

For \(y\in[a,u]\), take the fixed threshold

\[
t_y=2u-y.
\]

It satisfies \(t_y\le U_d\) for every \(d\ge u\). The corner minimizer is

\[
\phi_d
=\operatorname{clip}
\bigl(r,[\max(d,t_y),U_d]\bigr)
=\max(q_d,t_y).
\]

Hence

\[
\mathcal B_y(\phi_d,q_d)
=g_y(\phi_d)-g_y(q_d)
=E_d(t_y).
\]

It is nonnegative and nonincreasing in \(d\). This also covers the crossing at which the moving floor \(d\) overtakes \(t_y\).

### 5.3 Full penalty and absence of a missing far-tail term

Combining the two blocks gives precisely

\[
\boxed{
P(a,d;\lambda)
=8\int_0^a\kappa_d(y)\,dy
 +8b\int_a^u E_d(2u-y)\,dy.}
\]

The weights are:

- \(8(1-b)\) for the first-core excess;
- \(8b\) for the tail-core excess;
- \(8b\) for the corner excess.

They agree with **S2 LF 460–471** and **S1 LF 15–17**.

On the far-tail interval \([u,d]\), there is no additional coupling constraint, so the corrected minimizer and the independent minimizer are both \(q_d\). That contribution cancels in \(h-h_{\rm ind}\) at the **same** \(d\). The deterministic term \(bC(d;\lambda)\) likewise cancels at the same \(d\).

Thus

\[
h(a,d;\lambda)=h_{\rm ind}(a,d;\lambda)+P(a,d;\lambda)
\]

contains no omitted far-tail coupling penalty. This does **not** cancel the far-tail or deterministic contributions when comparing two *different* values of \(d\).

## 6. Universal monotonicity and boundary cases

The integration intervals \([0,a]\) and \([a,u]\) are fixed while \(d\) varies. Both pointwise integrands are nonnegative and nonincreasing. All displayed quantities are finite on these finite intervals for fixed finite parameters. Consequently,

\[
\boxed{
0\le P(a,d_+;\lambda)\le P(a,d_-;\lambda)
\qquad(u\le d_-\le d_+).}
\]

In particular,

\[
\boxed{
P(a,c;\lambda)-P(a,u;\lambda)\le0
\qquad(c\ge u).}
\]

No actual-optimizer hypothesis has entered this argument.

The requested degeneracies are included:

- **\(a=0\):** the first-core integral has zero length. The corner integral remains and satisfies the same proof.
- **First-core singleton boxes:** the fixed-box minimum is simply evaluation at the singleton.
- **\(d=u\):** admissibility holds with equality where appropriate; the proof does not require a nonempty far-tail interval.
- **Zero root or negative radicand:** covered by the derivative analysis in §3.1.
- **Upper-face selections below the root:** their admissible conditional excess is zero; no incorrect below-root monotonicity is used.
- **Moving lower and upper faces and threshold ties:** covered by the ordered-parameter case split, without differentiating the clips.

## 7. Disposition of the old error and limits of the correction

### f400 LF 498

The sentence in **S2 LF 498** stating that the two penalties’ difference “need not have a fixed sign” is **REFUTED**. For the manuscript’s specified ordering \(c\ge u\), that difference is always nonpositive.

The additive replacement is mathematically supported. The original frozen sentence and f419’s MAJOR finding remain historical records; neither is retrospectively made correct.

### Repeated f418 assertion

The same unsigned-penalty proposition attributed to f418 in **S1 LF 3 and 21** is also **REFUTED as a mathematical proposition**. It requires the same additive qualification.

The f418 body itself was not a frozen input to this gate and was not opened. Accordingly, this return does not claim independent verification of its exact sentence location or acceptance of the rest of f418. Its earlier reported zero-finding review cannot certify this repeated false assertion.

### What the correction does not establish

The full endpoint identity remains

\[
\begin{aligned}
h(a,c;\lambda)-h(a,u;\lambda)
={}&b[C(c;\lambda)-C(u;\lambda)]\\
&+8b\int_u^c\psi_1(q_c,y;\lambda)\,dy\\
&+8b\int_0^u
 [\psi_1(q_c,y;\lambda)-\psi_1(q_u,y;\lambda)]\,dy\\
&+P(a,c;\lambda)-P(a,u;\lambda).
\end{aligned}
\]

Only its final summand has received the universal nonpositive sign proved here. No sign estimate for the remaining sum follows from that fact.

This gate therefore establishes neither:

- a sign for the full endpoint difference or actual-edge derivative;
- global edge dominance or identification of the minimizing scalar branch;
- scalar-pair or law uniqueness;
- existence or parameter range of an actual cutoff-two regime;
- a global value formula or original-target completion.

The competitor, strict \(V<Q_*\), active-core binding, all-block calibration, endpoint identities, and actual-edge derivative are **not withdrawn by this localized correction**. Their separate prior scopes and gate states are unchanged; they are not newly accepted wholesale by f436.

## 8. Claimwise outcome and remaining acceptance boundary

| Claim | Outcome |
|---|---|
| S1 LF 7: \(P\ge0\), nonincreasing for all \(d\ge u\) at fixed \(a,b,\lambda\) | **SUPPORTED** |
| S1 LF 11: conditional-excess proof, including upper-face and zero-root cases | **SUPPORTED** |
| S1 LF 13–17: minimum over the unchanged core box preserves monotonicity | **SUPPORTED** |
| Exact normal terms, core/corner weights, and identification with the defined \(P\) | **SUPPORTED** |
| S1 LF 17: no additional far-tail coupling penalty | **SUPPORTED** |
| S2 LF 498: endpoint penalty difference need not have a fixed sign | **REFUTED — historical MAJOR remains recorded** |
| Corresponding f418 unsigned proposition identified by S1 | **REFUTED; no whole-f418 review claimed** |
| Nonpositive penalty difference determines the full endpoint sum or scalar optimizer | **INCONCLUSIVE / NOT PROVED** |
| Other f400 theorems and actual-optimizer claims | **Outside this correction gate; prior scopes unchanged** |

The process assertions in **S1 LF 21** about the parent’s earlier complete reads and methods remain **parent-attributed statements**, not independently certified execution history from this reviewer.

This return supplies a same-harness written reconstruction of the exact correction. It does not perform or assess the separately required finite algebra gate, grant parent adoption, or provide independent-family, human, formal/kernel, source-equivalence, priority, novelty, or clean-provenance assurance.

**Overall correctness:** correct, for the supplied additive correction only.

**Explanation:** The corrected universal nonpositive sign follows from a complete conditional-excess argument and minimization over an unchanged first-core box, including clipping faces, ties, zero roots, and degenerate intervals. It resolves the mathematical wording error prospectively without erasing the historical MAJOR or proving the remaining scalar-optimization claims.

**Confidence:** 0.98.