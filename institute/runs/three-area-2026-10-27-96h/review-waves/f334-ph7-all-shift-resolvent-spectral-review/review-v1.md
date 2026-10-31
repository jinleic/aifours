# F334 — Written reconstruction of the PH7 all-shift cubic resolvent condition

**Disposition:** SUPPORTED at the stated conditional necessary-condition scope.  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Overall correctness:** correct.  
**Confidence:** 0.99.

The all-positive-shift inequality and the displayed hidden-spectrum consequences follow from an actual representation, using the inherited conditional seven-state irreducibility theorem at its exact scope. No seven-state existence or exclusion, parameter endpoint, sufficient realization criterion, global verifier GO, or original-target closure follows.

## 1. Inputs, read order, and transport

The reviewed run root is:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`

The frozen source labels in this review are:

- **S1:** `review-waves/f318-ph7-irreducible-topology-universal-development/review-v1.md`, complete logical LF1–334; SHA-256 `5d087a324a15a4774ddf0ce8c887f981102e0a7407276624a0d2c52af0224047`.
- **S2:** `written-releases/math-1-ph-order-definitions-v1.md`, LF1–17; SHA-256 `a4db7478cf384fabdddccede032efe2cd1f33d12ad3e771788e58d5596682e85`.
- **S3:** `dispositions/math-1-ph7-global-irreducibility-eight-edges-parent-v1.md`, LF1–31; SHA-256 `42ae3d996ffb7f46cc5ad72a0d18f3eae665290f8d7901e994ac7776a6b4d281`.

Before opening mathematical source content, I read the complete manifest, complete freeze receipt, and all seven declared status-only controls, including their endings, in raw windows of at most 20 LF. Live metadata hashes matched all pins, including:

- Manifest: `42c51779b6fc485c64465729e152c87ba83c5410cc301768ddbb6a86eaee1933`.
- Receipt: `ce45e3dd50484410e5fae1e59cf7c800eb34194aa15fa7d3ad1ebe915ca0a712`.

After the fresh clock **2026-10-30T07:59:29-0700 PDT**, the administrative PRE-BODY ACK was delivered to `agent://Main`. Only afterward did I read the complete ordered literal packet, sequentially in raw windows LF1–20, LF21–40, continuing in 20-line windows through LF361–380, then LF381–384. This included S1’s final logical line and all source endings. No displayed elision remained.

The packet’s live SHA-256 matched `b9b184b52de6d0423cfab0e9c34b0a52c9fbde7152fd4703d9127c150a81903e`; all three live source hashes also matched. Source bodies were read through that packet; direct source access afterward was metadata hashing only.

An own-wave `reviewer-process-v1.md` write was attempted and refused because the available write tool does not support working-tree paths. The refusal was disclosed directly to Main. No filesystem bypass was attempted. **This complete return is supplied for parent materialization of the review and process record.** The transport refusal does not change the mathematical verdict.

## 2. Exact actual-representation premise and inherited structural input

**SUPPORTED — S2 LF5–10; S1 LF31–50.**

For arbitrary
\[
a>c>0,\qquad b>0,\qquad d=a-c,\qquad z=b^2/d^2>1/2,
\]
the exact transform is
\[
H(s)=\frac{c(a^2+b^2)^2}
{(s+c)((s+a)^2+b^2)^2}.
\]

The premise is an actual representation using at most seven states:
\[
T\ \text{real Hurwitz Metzler},\quad T\mathbf1\le0,\quad
\alpha\ge0,\quad\alpha\mathbf1=1,
\]
with the **tied exit vector**
\[
r=-T\mathbf1
\]
and exact equality
\[
\alpha(sI-T)^{-1}r=H(s).
\]

This is not a free-input/free-output positive realization, and it does not merely prescribe visible eigenvalues.

**SUPPORTED as an exact named import — S3 LF11; S1 LF50.**

S3 states that **every actual representation of this transform using at most seven states**, for \(z>1/2\), has exactly seven states, all reachable from the input, a strongly connected generator graph, and at least eight positive off-diagonal entries. Its quantifier matches the present premise directly.

I use that inherited conditional theorem at precisely this scope. I do not count the historical executions described in S3 LF27–29 as evidence produced by this review, nor claim a fresh independent re-proof of the earlier lower-state barrier from its linked manuscripts. Those manuscripts, reviewer bodies, and code were not opened. The new resolvent argument needs the resulting dimension seven and irreducibility; it does not need edge sharpness.

## 3. Positive Perron visibility and characteristic factorization

**SUPPORTED — S1 LF103–128.**

Because \(T\mathbf1\le0\), its tied exit vector satisfies \(r\ge0\). Moreover \(r\ne0\): otherwise \(T\mathbf1=0\), contradicting Hurwitz stability.

By irreducible Metzler Perron theory, the spectral bound \(s(T)\) is a real algebraically simple eigenvalue with positive right and left eigenvectors \(v,w_T\). The residue contributed to the scalar transfer at that eigenvalue is
\[
\frac{(\alpha v)(w_T^{\mathsf T}r)}
{w_T^{\mathsf T}v}>0.
\]
Here \(\alpha v>0\) follows from \(\alpha\ge0\), \(\alpha\mathbf1=1\), and \(v>0\); the second numerator factor is positive because \(w_T>0\) and \(r\ge0\) is nonzero.

Thus the Perron eigenvalue cannot be canceled in the actual transfer.

The exact rational function \(H\) has only one real pole, namely \(-c\). Its residue there is
\[
\frac{c(a^2+b^2)^2}{(d^2+b^2)^2}>0.
\]
Consequently \(s(T)=-c\). This also gives the author’s density-asymptotic conclusion: the positive Perron term has decay \(e^{-ct}\), while the other visible terms are polynomial multiples of \(e^{-at}\).

Define the derived normalized matrix
\[
G=\frac{T+cI}{d}.
\]
It is irreducible Metzler, with algebraically simple Perron eigenvalue zero and every other eigenvalue strictly in the open left half-plane.

The constant nonzero numerator of \(H\) means its denominator is reduced. Its two nonreal poles \(-a\pm ib\), each of order two, therefore force the corresponding characteristic roots of \(T\) with algebraic multiplicity at least two. After normalization, the characteristic polynomial contains
\[
x\bigl((x+1)^2+z\bigr)^2.
\]

Since the dimension is exactly seven, the remaining factor is monic quadratic and real:
\[
p(x)=\det(xI-G)
=x\bigl((x+1)^2+z\bigr)^2(x^2+\sigma x+\pi).
\]

The remaining two roots are either negative real roots or a conjugate pair with negative real part. Writing them as \(-u,-v\), these alternatives give
\[
\sigma=u+v>0,\qquad \pi=uv>0.
\]
For a conjugate pair, \(\pi=|u|^2>0\); real hidden roots are not being assumed.

Repeated hidden roots, coincidence with the prescribed nonreal roots, and nontrivial Jordan blocks cause no difficulty. A further zero root is excluded by Perron simplicity.

## 4. Every positive-shift resolvent and the trace formulas

**SUPPORTED — S1 LF63–85 and LF130–155.**

For every real \(x>0\),
\[
N=(xI-G)^{-1}
=\int_0^\infty e^{-xt}e^{tG}\,dt.
\]
The integral converges because \(s(G)=0\). Irreducible Metzler semigroup positivity gives \(e^{tG}>0\) entrywise for every \(t>0\), so
\[
N_{ij}>0
\]
for every pair of indices and every \(x>0\).

No replacement realization or selected shift has entered this argument.

Put
\[
w=x+1,\qquad A=w^2+z,\qquad B=x^2+\sigma x+\pi.
\]
All denominators below are positive on \(x>0\).

Jacobi’s logarithmic determinant identity gives
\[
L=\frac{p'(x)}{p(x)}
=\operatorname{tr}N
=\frac1x+\frac{4w}{A}+\frac{2x+\sigma}{B}.
\]
Since \(N'=-N^2\),
\[
V=-L'=\operatorname{tr}N^2
=\frac1{x^2}
+\frac{4(w^2-z)}{A^2}
+\frac{(2x+\sigma)^2-2B}{B^2},
\]
and
\[
W=-\frac12V'=\frac12L''
=\operatorname{tr}N^3
=\frac1{x^3}
+\frac{4w(w^2-3z)}{A^3}
+\frac{(2x+\sigma)((2x+\sigma)^2-3B)}{B^3}.
\]

These are the author’s formulas, including the factors arising from the two copies of each prescribed nonreal root.

The trace identities do not require diagonalizability: rational functions of Jordan blocks have the relevant scalar function on each diagonal entry, so their traces count eigenvalues with algebraic multiplicity.

## 5. Centered traces and reciprocal-edge AM–GM

**SUPPORTED — S1 LF159–196.**

Let
\[
X=N-\frac L7I.
\]
Direct expansion gives
\[
\operatorname{tr}X=0,
\]
\[
\operatorname{tr}X^2
=V-\frac{L^2}{7}=Q,
\]
and
\[
\operatorname{tr}X^3
=W-\frac{3LV}{7}+\frac{2L^3}{49}=R.
\]
In particular, the coefficient \(2/49\) in the centered cubic is correct.

Define the derived real symmetric matrix \(S\) by
\[
S_{ii}=X_{ii},\qquad
S_{ij}=\sqrt{N_{ij}N_{ji}}\quad(i\ne j).
\]
It has strictly positive off-diagonal entries. Moreover
\[
\operatorname{tr}S=0,\qquad
\operatorname{tr}S^2=\operatorname{tr}X^2=Q.
\]
Indeed,
\[
Q=\sum_i X_{ii}^2+
2\sum_{i<j}N_{ij}N_{ji}>0.
\]

For the cubic comparison, the diagonal terms and the terms involving only two distinct indices agree between \(X\) and \(S\). For each unordered triple \(i,j,k\), write
\[
U=N_{ij}N_{jk}N_{ki},\qquad
D=N_{ik}N_{kj}N_{ji}.
\]
Its contribution to the difference of cubic traces is exactly
\[
3(U+D-2\sqrt{UD})
=3(\sqrt U-\sqrt D)^2\ge0.
\]
Summing over all unordered triples yields
\[
R=\operatorname{tr}X^3\ge\operatorname{tr}S^3.
\]

The coefficient three and the reciprocal-edge product under the square root are correct. This comparison uses every triple and assumes neither a selected directed cycle nor any additional topology.

## 6. Exact seven-dimensional spectral bound and strictness

**SUPPORTED — S1 LF200–229.**

For real \(\mu_1,\ldots,\mu_7\) with
\[
\sum_i\mu_i=0,\qquad \sum_i\mu_i^2=Q>0,
\]
the constraint set is compact. Its two constraint gradients are independent: dependence would make every \(\mu_i\) equal, incompatible with zero sum and \(Q>0\).

At a constrained extremum of \(\sum_i\mu_i^3\), Lagrange multipliers give one common quadratic equation for every \(\mu_i\). There are therefore at most two distinct values. There cannot be only one; the two values have opposite signs.

If the negative value has multiplicity \(k\) and the positive value multiplicity \(7-k\), the constraints give
\[
\sum_i\mu_i^3
=Q^{3/2}\frac{2k-7}{\sqrt{7k(7-k)}}.
\]
The coefficient is strictly increasing for \(0<k<7\): its derivative is
\[
\frac{49}{2\sqrt7\,[k(7-k)]^{3/2}}>0.
\]
Its minimum over \(k=1,\ldots,6\) is consequently
\[
-\frac5{\sqrt{42}},
\]
attained only when one eigenvalue is negative and the other six are equal and positive. Thus
\[
\sum_i\mu_i^3\ge-\frac5{\sqrt{42}}Q^{3/2}.
\]

Apply this to the real eigenvalues of the symmetric matrix \(S\). Equality is impossible here: \(S\) is irreducible Metzler, so its largest eigenvalue is algebraically simple, whereas the lower-bound equality spectrum has its largest eigenvalue with multiplicity six. Therefore
\[
\operatorname{tr}S^3>
-\frac5{\sqrt{42}}Q^{3/2}.
\]

Combining this with the preceding AM–GM comparison proves the exact necessary condition
\[
\boxed{
Q(x)>0,\qquad
R(x)+\frac5{\sqrt{42}}Q(x)^{3/2}>0
\quad\text{for every }x>0.
}
\]

The strictness argument is valid even when the triangle AM–GM comparisons are equalities. It comes from Perron simplicity of the resolvent-derived symmetrization, not from an assumed strict triangle gap.

## 7. Large-\(x\) hidden-spectrum constraints

**SUPPORTED — S1 LF235–266.**

The large-\(x\) resolvent expansion gives
\[
N=\frac Ix+\frac G{x^2}+O(x^{-3}),
\]
and hence
\[
X=\frac1{x^2}
\left(G-\frac{\operatorname{tr}G}{7}I\right)
+O(x^{-3}).
\]
Therefore
\[
\lim_{x\to\infty}x^4Q(x)
=\operatorname{tr}G^2-\frac{(\operatorname{tr}G)^2}{7}
\ge0.
\]
Only a non-strict inequality follows at the limit. The author correctly does not pass finite-\(x\) strictness to that limit.

The characteristic factorization gives
\[
\operatorname{tr}G=-4-\sigma
\]
and
\[
\operatorname{tr}G^2
=4(1-z)+\sigma^2-2\pi.
\]
Substitution yields
\[
\operatorname{tr}G^2-\frac{(\operatorname{tr}G)^2}{7}
=
\frac27\left(3\sigma^2-4\sigma+6-14z-7\pi\right).
\]
Thus the stated necessary constraint is exactly
\[
\boxed{7\pi+14z\le3\sigma^2-4\sigma+6.}
\]

Since \(\pi>0\),
\[
3\sigma^2-4\sigma+6-14z>0.
\]
Its two roots are
\[
\frac{2\pm\sqrt{42z-14}}3.
\]
For \(z>1/2\), the lower root is negative. Together with \(\sigma>0\), the strict quadratic inequality therefore implies
\[
\boxed{\sigma>\frac{2+\sqrt{42z-14}}3.}
\]

Both consequences apply to real or conjugate hidden roots. Neither is a restriction to a selected hidden-spectrum type.

## 8. Per-claim dispositions

| Claim | Verdict | Exact scope or evidence |
|---|---|---|
| Original transform, initial-distribution conditions, and tied exit vector | **SUPPORTED** | S2 LF5–10; reconstructed in §2 |
| Exactly seven states and irreducibility under the actual \(\le7\)-state premise | **SUPPORTED as a named inherited import** | S3 LF11; not a fresh gate on earlier lower-state proofs |
| Positive Perron visibility and \(s(T)=-c\) | **SUPPORTED** | S1 LF103–115; reconstructed in §3 |
| Normalized factorization with real \(\sigma,\pi>0\), allowing complex hidden roots and Jordan structure | **SUPPORTED** | S1 LF117–128; reconstructed in §3 |
| Entrywise-positive resolvent for every \(x>0\) | **SUPPORTED** | S1 LF130–147; reconstructed in §4 |
| Logarithmic derivatives and \(L,V,W\) trace formulas | **SUPPORTED** | S1 LF63–85, LF149–155; reconstructed in §4 |
| Centered second/third traces and reciprocal-edge AM–GM comparison | **SUPPORTED** | S1 LF159–196; reconstructed in §5 |
| Constant \(5/\sqrt{42}\) and strictness from Perron simplicity | **SUPPORTED** | S1 LF200–229; reconstructed in §6 |
| All-\(x>0\) strict necessary condition | **SUPPORTED** | S1 LF88–95, LF227; reconstructed in §§4–6 |
| Displayed large-\(x\) \(\sigma,\pi,z\) constraints | **SUPPORTED** | S1 LF235–266; reconstructed in §7 |
| Seven-state existence, exclusion, improved endpoint, or exact minimum-order function | **INCONCLUSIVE / NOT ESTABLISHED** | Explicitly unpaid in S1 LF286–310; not claimed as proved |
| Sufficient PH-realization criterion or executable global-verifier GO | **NOT SUPPLIED** | Outside the proved necessary-condition scope |

No mathematical claim within the candidate’s stated proved scope was refuted. No actionable defect was found.

## 9. Named imports and acceptance boundary

The reconstruction uses:

1. The **conditional structural theorem** of S3 LF11.
2. The rational-transfer fact that visible poles must occur in the matrix spectrum with sufficient multiplicity.
3. **Irreducible Metzler Perron theory**, including a simple real spectral bound and positive left/right Perron vectors.
4. **Strict positivity of irreducible Metzler semigroups** and the Laplace resolvent formula.
5. **Jacobi’s determinant derivative identity**, resolvent differentiation, and trace identities valid with Jordan blocks.
6. **AM–GM**, the real symmetric spectral theorem, compactness, and the ordinary Lagrange-multiplier argument.
7. The large-\(x\) **resolvent expansion**.

The proof starts from an actual tied-exit representation, but its final scalar relaxation no longer enforces all realization data. Passing the inequalities does not construct a Metzler generator, the required visible Jordan structure, or an initial distribution with the exact tied-exit numerator. The author correctly preserves that distinction in S1 LF270–302.

In particular, **f203 GLOBAL NO GO remains unchanged**. This review supplies neither global leaf coverage nor repaired global certificate semantics, and it is not an execution authorization.

## 10. Reviewer process and final verdict

Fresh substantive checkpoints were observed at:

- **2026-10-30T07:59:29-0700 PDT:** pre-body administrative ACK.
- **2026-10-30T08:01:28-0700 PDT:** complete packet reading and substantive written reconstruction.
- **2026-10-30T08:03:09-0700 PDT:** completed review checkpoint.

No selected mathematical instance, chosen PH generator, numerical \(z\) or resolvent shift, scientific executable, interpreter calculation, CAS, solver, enumeration, replay, external-model call, test, build, lint, or formatter was used. All mathematical statements above concern arbitrary variables under the stated actual-representation hypothesis. Historical execution reports were not replayed or promoted to new evidence.

**Overall correctness: correct.** The exact all-shift necessary inequality, its strictness, and the displayed large-\(x\) consequences are supported, conditional on the precisely imported structural theorem. This is a same-harness written review only, with no human, independent-family, formal/kernel, novelty, seven-state existence/exclusion, endpoint, or original-target acceptance.