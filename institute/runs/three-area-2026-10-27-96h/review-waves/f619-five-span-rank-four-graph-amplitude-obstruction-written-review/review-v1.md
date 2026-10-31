# f619 — Full written review

**Role:** WRITTEN. Scientific execution **NOTRUN** in child.  
**Candidate:** f599, “Actual five-span amplitude obstruction: the rank-four graph branch is impossible.”  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Disposition:** The rank-four obstruction and the stated rank-two \(U_0\) residual are supported at their frozen, conditional actual-five-span scope. This review is not parent adoption or original-target closure.

## 1. Source coverage and process

Before mathematical packet reading, I read the manifest, freeze receipt, dispatch receipt, parent metadata supply, and all fifteen listed status-only controls through their endings. I then delivered the required direct pre-body ACK to `agent://Main`.

I subsequently read **all 470 packet lines**, sequentially in raw windows of at most twenty lines, including the endings of all three sources:

- **S1:** f599 candidate, logical LF1–379; SHA256 `2f9e8a3d9a923b012e05b5f835db096f02493cdcd08ca6e80b0b26d2aca4d284`.
- **S2:** common four-fibre/XOR/complement disposition, LF1–51; SHA256 `fc7169410a6540a6d63ea033720a90207fd49e89e4cc048d9eb208639eb65e5c`.
- **S3:** normalized graph/phase classification disposition, LF1–38; SHA256 `443d0a1a94384e237076cb7974b49845e6fa52edf3ca83f161259e79a369de1e`.

The reconstruction below followed that complete read.

The parent’s supplied bindings identify:

- Manifest SHA256: `bb8bf4f73964e412c276f45388014cc37fd20e93752c24ffaf9d2ad59dfdc3f5`.
- Receipt SHA256: `dff7de03d3ef22efe623e30ee8b30c5393d4f2124cccd1010c3296ca8014ecbd`.
- Packet SHA256: `e4e9d4eb6019668093408ba7ee74eb35784db0114b669a5d60c97bf3015f3561`.

These are **parent-observed metadata**, not independently measured child hashes.

No scientific executable, selected diagnostic, additional concrete instance, linked scientific source, sibling review, author code, external model, build, test, or repository mutation was used. The complete f586/f602/f596 episodes and all other held material and consumers remain NONINPUT. No cognition-isolation certificate is asserted. This full body is returned for parent materialization.

## 2. Exact imports

The new obstruction uses the following supplied scopes:

1. **S2 LF9–27:** the same physical \(u\), its actual block counts, the representation
   \[
   x=1_S-2\,1_P+2\,1_W-4\,1_N,
   \]
   and criterion (C), whose consequence is divisibility of every \(U_0\) Walsh coefficient by eight.

2. **S2 LF31–35:** the common-fibre residue relation, unpaid amplitude caps, and specifically carried original balance frequency.

3. **S3 LF7–30:** the actual five-span normalization, graph representation, common bent conditions, quadratic graph classification, polar ranks, and labeled census.

4. **S2 LF39–41:** the actual-complement and conditional full-caller requirements.

The review reconstructs the candidate’s new mathematical implications. It does **not** independently reproduce the imported finite enumerations, inspect their linked code, or certify collateral atom claims beyond their stated import scopes.

## 3. Physical parity, energy, and spectral cardinality

**Status: SUPPORTED — S1 LF39–92.**

On \(S\), the displayed representation makes \(x=\pm1\). On \(W\), it makes \(x=\pm2\), and elsewhere \(x=0\). Since \(S\cap W=\varnothing\),
\[
x\bmod2=1_S,\qquad
\sum_c x(c)^2=16+4\cdot10=56.
\]

Divisibility by eight together with \(|\widehat x|\le8\) gives
\[
\widehat x(\xi)\in\{0,\pm8\}.
\]
With the unnormalized transform on a group of order \(64\), Parseval gives
\[
\sum_\xi \widehat x(\xi)^2=64\cdot56.
\]
Consequently there are exactly \(56\) nonzero coefficients and eight zeros.

The graph-indicator expression is also correct. In the supplied coordinates, the four \(d_b\) are precisely the points with \(\ell=1\), and graph membership there is \(h_0=f(j,b)\). Hence, over \(\mathbb F_2\),
\[
1_S=\ell(1+h_0+f(j,b)).
\]
The change from \((h,d)\) to \((\ell,h_0,j,b)\) is linear and invertible.

## 4. Walsh-divisibility/parity-degree lemma

**Status: SUPPORTED — S1 LF98–109.**

Write \(\widehat v=2^k b\) with integer \(b\). Inversion gives the exact multilinear representation
\[
v(c)=2^{k-n}\sum_\xi b(\xi)
       \prod_{i:\xi_i=1}(1-2c_i).
\]
Its coefficient at \(c_I\) is
\[
(-1)^{|I|}2^{k-n+|I|}
\sum_{\xi:\,I\subseteq\operatorname{supp}\xi}b(\xi).
\]
For \(|I|>n-k\), this is even.

The required integrality of the remaining coefficients is justified independently: every integer-valued function on the Boolean cube has integer multilinear coefficients, given by finite differences. Reduction modulo two therefore removes all terms above degree \(n-k\).

The application \(n=6,k=3\) is valid. No converse to this lemma is assumed.

## 5. Minimum-weight lemma, including equality

**Status: SUPPORTED — S1 LF113–130.**

The induction establishes both the lower bound and the affine-flat equality classification.

For the boundary cases, a nonzero degree-zero function is constant one, while weight one in the degree-\(n\) case has singleton support. These give the stated affine-flat conclusions.

For the interior induction, write
\[
P(c',s)=P_0(c')+sP_1(c'),\qquad \deg P_1\le d-1.
\]

- If \(P_1=0\), weight doubles. Equality reduces to equality for \(P_0\); its support is the corresponding affine flat times the free \(s\)-coordinate.

- If \(P_1\ne0\), then
  \[
  \operatorname{wt}(P)
  =\operatorname{wt}(P_0)+\operatorname{wt}(P_0+P_1)
  \ge\operatorname{wt}(P_1)\ge2^{n-d}.
  \]
  At points where \(P_1=1\), the two terms contribute exactly one. At points where \(P_1=0\), they contribute twice \(P_0\). Equality therefore forces \(P_0\) to vanish outside \(\operatorname{supp}P_1\), and forces \(P_1\) itself to attain minimum weight.

By induction, \(\operatorname{supp}P_1\) is an affine flat of codimension \(d-1\) in the \(c'\)-space. After an affine coordinate change it is \(z_1=\cdots=z_{d-1}=0\), and
\[
P_0=\prod_{i=1}^{d-1}(1+z_i)\,Q(t).
\]
Affine substitutions do not increase Boolean degree. Because the \(z\)-variables and \(t\)-variables are disjoint, a nonzero \(Q\) makes this product have degree \(d-1+\deg Q\). Thus \(\deg Q\le1\).

On the flat, \(P=Q(t)+s\), so its support is \(s=1+Q(t)\), an affine \((n-d)\)-flat. The zero-\(P_0\) possibility is included.

## 6. The affine spectral zero flat and quadratic parity identity

**Status: SUPPORTED — S1 LF134–196.**

Set \(z=\widehat x/8\). Under the cap and divisibility hypotheses, \(z\) is integer ternary and
\[
\widehat z=8x.
\]
The parity-degree lemma makes \(z\bmod2\) have degree at most three. Since \(1_Z=1+z\) modulo two and \(|Z|=8\), the minimum-weight equality theorem gives
\[
Z=\zeta+K,\qquad \dim K=3.
\]
For \(L=K^\perp\),
\[
\widehat{1_Z}(c)=8(-1)^{\zeta\cdot c}1_L(c).
\]

Now let \(B_-=\{\xi:z(\xi)=-1\}\). Transforming
\[
z=1-1_Z-2\,1_{B_-}
\]
gives
\[
x=8\delta_0-(-1)^{\zeta\cdot c}1_L
   -\frac14\widehat{1_{B_-}}.
\]
Thus \(\widehat{1_{B_-}}\) is pointwise divisible by four.

For the quotient’s parity degree, the exact polynomial is
\[
\widehat{1_{B_-}}(c)=\sum_I(-2)^{|I|}m_Ic_I.
\]
Pointwise divisibility by four implies divisibility by four of its integer finite-difference coefficients. In particular,
\[
4\mid m_\varnothing,\qquad 2\mid m_{\{i\}}.
\]
After division by four, all coefficients are integral, and every coefficient of degree at least three is even. Therefore
\[
q_B:=\frac14\widehat{1_{B_-}}\pmod2
\]
has degree at most two. Reducing the transformed identity modulo two yields
\[
1_S+1_L=q_B,\qquad \deg q_B\le2.
\]

This argument genuinely uses the amplitude cap through the ternary dual and its eight zeros. It does not incorrectly derive the identity from divisibility alone.

## 7. Exterior-form obstruction and rank preservation

**Status: SUPPORTED — S1 LF200–249.**

The characteristic-two convention is correct. For the degree filtration on Boolean polynomials, the associated graded algebra has square-zero degree-one generators and identifies with exterior algebra over \(\mathbb F_2\). The class of the quadratic part of \(f\) is the alternating polar two-form \(B_f\). Hence
\[
[1_S]_3=\ell\wedge B_f.
\]

A linear three-space \(L\) has three independent normal equations \(\lambda_i=0\), so
\[
1_L=\prod_{i=1}^3(1+\lambda_i),\qquad
[1_L]_3=\lambda_1\wedge\lambda_2\wedge\lambda_3.
\]
Cancellation of cubic terms gives
\[
\ell\wedge B_f
=\lambda_1\wedge\lambda_2\wedge\lambda_3\ne0.
\]

Wedging with \(\ell\) shows that \(\ell\) lies in the span of the three normal forms. Choosing a basis of that span beginning with \(\ell\), then passing to the quotient by \(\langle\ell\rangle\), makes the image of \(B_f\) a nonzero decomposable two-form. Such a two-form has alternating rank exactly two.

The quotient step does **not** lose the graph’s polar rank. The four-dimensional form space generated by \((j,b)\) is disjoint from \(\langle\ell\rangle\), so its image in the quotient is injective. The same alternating form is merely embedded with an additional unused coordinate; its rank is unchanged.

It follows that the amplitude hypotheses force
\[
\operatorname{rank}B_f=2.
\]
This excludes the entire rank-four graph branch.

The conclusion is uniform: the proof depends on the graph’s odd support and the fixed physical energy, not on a selected phase, sign pattern, placement, balance frequency, or \(U_3\) choice. Consequently no additional \(U_3\) or complementary-half requirement can repair the contradiction.

The count \(384\cdot384=147456\) is correct **conditional on the imported labeled census**. It is neither a newly executed enumeration nor an original-caller count.

## 8. Rank-two direction, balance coset, and autocorrelation consumer

**Status: SUPPORTED — S1 LF253–297.**

For \(B_f=p\wedge q\), the nonzero three-form
\[
\ell\wedge p\wedge q
\]
determines its factor span. Therefore the normal space of \(L\) is exactly \(\operatorname{span}(\ell,p,q)\), and
\[
L=\ker\ell\cap\ker p\cap\ker q.
\]
This has dimension three. The physical direction \(e\), which toggles \(h_0\), is annihilated by all three forms and belongs to \(L\).

The specifically carried balance frequency \(t\) satisfies \(\widehat x(t)=0\). Since \(Z=\zeta+L^\perp\), this determines the whole zero coset:
\[
Z=t+L^\perp.
\]
No arbitrary normalized zero is substituted.

For
\[
A_x(v)=\sum_c x(c)x(c+v),
\]
the unnormalized transform obeys
\[
\widehat{A_x}(\xi)=\widehat x(\xi)^2.
\]
Thus the forward implication gives
\[
A_x(v)=64\delta_0(v)-8(-1)^{t\cdot v}1_L(v).
\]
Conversely, transforming this identity gives
\[
\widehat x(\xi)^2
=64\bigl(1-1_{t+L^\perp}(\xi)\bigr).
\]
Hence the coefficients are exactly zero on the prescribed coset and \(\pm8\) elsewhere. This recovers divisibility, the cap, the exact eight zeros, and carried balance.

Equation (16) has the appropriate weaker scope. Setting \(Y(c)=(-1)^{t\cdot c}x(c)\), vanishing of \(\widehat x\) on \(t+L^\perp\) is equivalent, by Fourier inversion on \(R/L\), to
\[
\sum_{c\in D}Y(c)=0
\]
for every coset \(D\) of \(L\). These sums alone do not establish the amplitudes outside that coset. The candidate retains equation (15), rather than substituting equation (16) for the full residual.

## 9. Common physical inverse and remaining consumers

**Status: SUPPORTED — S1 LF301–345.**

The candidate correctly retains
\[
u(c,w)=\frac14\left[x+3a\chi_1+g\chi_2+y\chi_3\right]
\]
on one common physical \(u\).

On an \(S\)-block, support three and \(U_1=3a\) force every nonzero entry to have sign \(a\chi_1(w)\). Removing the missing position \(w_*\) gives
\[
x=-a\chi_1(w_*),\quad
g=-a\chi_3(w_*),\quad
y=-a\chi_2(w_*).
\]
Since \(\chi_1\chi_3=\chi_2\),
\[
x=\pm1,\qquad y=-agx.
\]
Thus \(y\) is not independently adjustable there.

The remaining displayed block forms agree with the imported physical inverse. Their counts give
\[
|\operatorname{supp}u|
=16\cdot3+2\cdot4+22\cdot2+6\cdot2+4=116,
\]
and
\[
\sum x^2=16+4\cdot4+6\cdot4=56,
\]
\[
\sum y^2=16+18\cdot4+6\cdot4+16=128.
\]

For the common physical \(u\), \(J=1\) and the imported residue relation give \(F_3\equiv4\pmod8\). Combining this with \(|F_3|\le12\) leaves magnitudes four and twelve. If \(n_4\) is the number of magnitude-four positions, Parseval gives
\[
16n_4+144(64-n_4)=64\cdot128,
\]
so \(n_4=8\).

This is a necessary consequence, not a supplied \(y\). The auxiliary \(L\) is never substituted for physical \(Q\), the primal direction \(e\), a dual normal, or original \(T\).

## 10. Acceptance boundary and residual

**Status: SUPPORTED — S1 LF349–379.**

The review supports:

- Uniform exclusion of every rank-four normalized graph under the frozen actual counts, \(U_0\) divisibility, and \(U_0\) amplitude cap.
- The uniquely determined rank-two zero direction.
- The balance-determined zero coset.
- The exact autocorrelation equivalence for the rank-two \(U_0\) spectral condition and carried balance.
- Preservation of the common physical inverse and unpaid consumers.

The imported \(512\cdot384=196608\) rank-two labeled pairs remain necessary-interface parameters, not feasible callers. No simultaneous physical \(x,y\), capped \(F_3\), or actual complementary sign assignment is constructed. The complementary odd-half caps, original rank/\(T\) requirements, other five-/six-span classes, and full NL242 target remain unresolved.

This is same-harness written checking only. It supplies no independent-family, human, formal/kernel, novelty, or original-book-equivalence acceptance.

**Overall correctness:** correct.

**Explanation:** The load-bearing parity-degree, minimum-weight equality, affine-zero-flat, quadratic-parity, and exterior-rank implications reconstruct successfully. The rank-two residual and physical consumers preserve the supplied normalization and carried balance without promoting the obstruction to a whole-five-span or original-target conclusion.

**Confidence:** 0.98.