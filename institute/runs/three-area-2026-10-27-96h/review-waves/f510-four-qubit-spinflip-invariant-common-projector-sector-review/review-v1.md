# F510 WRITTEN review — four-qubit spin-flip-invariant common-projector sector

**Verdict: SUPPORTED at the frozen F510 scope.**  
**Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

For every actual four-qubit mixed density invariant under the full spin flip, the candidate proves the complete \(H_2\) layer majorization. It also proves the physical-channel product-reference bound for every prefix other than \(k=4\) throughout the physical parameter interval, and proves the fourth prefix on the stated closed noise region and at \(p=0\). No unrestricted four-qubit conclusion follows.

This is the complete review body for parent materialization as `review-v1.md`; no repository file was written.

## 1. Binding, read coverage, and process

The review is bound to the supplied frozen wave:

- Manifest SHA: `b002689dac86ffa721296ae3a021d10f557bd321ea61ede2578b15d8b435ce0f`.
- Freeze-receipt SHA: `d8262468984d7aff438b8b05da6efefba258fdf17d5293c59bffc5560384a2cb`.
- Literal-packet SHA, as supplied by the receipt: `49c2663584c02ddea0cde9d896817d6fd4825d43037206e8e88432c08f9934fb`.

These are **parent-supplied metadata**, not child-native hash observations.

Before mathematical packet access, I read the complete manifest, freeze receipt, parent live-metadata supply, dispatch receipt, and all eleven declared status-only controls. I then sent the administrative pre-body acknowledgment to `agent://Main`; the tool reported **“Delivered to Main.”** Only afterward did I read the literal packet.

The complete packet was read raw, in ordered windows \(1\!-\!20,21\!-\!40,\ldots,541\!-\!560,561\!-\!564\), each containing at most twenty lines. Coverage includes:

- **S1:** the complete F481 author body, logical lines 1–523, including its final unrestricted-target qualification. Its supplied whole-file SHA is `347e899d9e84bcd958f28348e10f7e0f45730a93d911eed2306299b39564d713`. The metadata reports 522 LF; the packet explicitly includes logical line 523.
- **S2:** the complete earlier three-qubit/biseparable disposition, lines 1–39, including its ending. Its supplied whole-file SHA is `cef7da09334dd4288d166782c9629daa3aeaef6af1db2ffd98ec012fe233fa93`.

Mathematical reconstruction began only after the complete packet read. No scientific executable, interpreter, CAS, solver, enumeration, replay, finite assay, build, test, linter, or formatter was run. No new selected state, projector, operator, parameter instance, or private diagnostic was introduced. No sibling body, linked new source, author code, or held scientific payload was opened.

The historical transport qualifications remain intact: F480 is transcript-only according to the supplied parent context; F481/F483 have the disclosed local-only pre-body ACK history, not established direct pre-body delivery. This review neither backdates delivery nor treats those transport facts alone as mathematical invalidation under owner addendum 2. F439/F444/F448 and every genuinely held episode and consumer remain **HELD/ZERO/NONINPUT**.

## 2. Exact reviewed statement and imports

Let
\[
\Phi_p(X)=(1-p)X+\frac p2\operatorname{Tr}(X)I_2,
\qquad 0\le p\le\frac43,
\]
and put
\[
t=|1-p|,\qquad b=\frac{1-t}{2},\qquad a=\frac{1+t}{2}.
\]
For an actual density \(\rho\) on four physical qubits, define
\[
H_j(\rho)=\sum_{|S|=j}\rho_S\otimes I_{S^c},
\qquad H_0=I_{16},\quad H_4=\rho,
\]
with the indicated factors on their actual physical subsystems.

The reviewed hypothesis is
\[
\widetilde\rho
=Y^{\otimes4}\rho^T Y^{\otimes4}
=\rho.
\]

The supported conclusions are:

1. For every such mixed density,
   \[
   H_2(\rho)\prec
   \operatorname{diag}(6,3^{\times4},1^{\times6},0^{\times5}).
   \]
2. For every complex orthogonal rank-\(k\) projector \(Q\), every physical \(p\), and every \(k\ne4\),
   \[
   \operatorname{Tr}\!\left[Q\Phi_p^{\otimes4}(\rho)\right]
   \le K_k\!\left(\operatorname{diag}(a,b)^{\otimes4}\right).
   \]
3. The same fourth-prefix inequality, and therefore full output majorization, holds when
   \[
   0\le t\le t_*=\frac{\sqrt{29}-2}{5},
   \quad\text{or}\quad t=1.
   \]
   Within the physical \(p\)-interval this is
   \[
   p\in\left[\frac{7-\sqrt{29}}5,\frac43\right]\cup\{0\}.
   \]

The reconstruction below is self-contained from the definitions and algebra in S1. It does **not** import S1’s earlier three-qubit candidate as a premise, Song–Chen as a four-qubit theorem, or the biseparable conclusion in S2 as a theorem about all spin-flip-invariant states. S2’s full-transpose interface agrees with the independently reconstructed transport below.

The Dicke-orbit theorem, its detailed spectra, and its comparison with earlier Class A/B and W hulls were read as required packet content but are **outside this F510 mathematical disposition**.

## 3. Physical expansion and all reference prefixes

**SUPPORTED — S1 lines 78–137.**

For the nonnegative branch
\[
T_t(X)=tX+b\operatorname{Tr}(X)I_2,
\]
expanding the four tensor factors gives exactly
\[
T_t^{\otimes4}(\rho)
=t^4\rho+t^3bH_3+t^2b^2H_2+tb^3H_1+b^4I_{16}.
\]
Each retained subset occurs once. There is no additional binomial coefficient outside \(H_j\).

Because every marginal has trace one,
\[
\operatorname{Tr}H_j=\binom4j2^{4-j}.
\]
Thus the nonconstant layer traces are \(1,8,24,32\), and the output trace is
\[
t^4+8t^3b+24t^2b^2+32tb^3+16b^4
=(t+2b)^4=1.
\]

For the author-explicit product reference \(|0000\rangle\), the \(j\)-layer value on a weight-\(w\) basis vector is \(\binom{4-w}{j}\). Consequently its decreasing layer spectra are
\[
L_4=(1,0^{\times15}),
\quad
L_3=(4,1^{\times4},0^{\times11}),
\]
\[
L_2=(6,3^{\times4},1^{\times6},0^{\times5}),
\quad
L_1=(4,3^{\times4},2^{\times6},1^{\times4},0).
\]
All are co-ordered by increasing Hamming weight. Their weighted sum is exactly
\[
D_t=\operatorname{diag}(a,b)^{\otimes4},
\]
whose weight-\(w\) entry is \(a^{4-w}b^w\).

Writing \(R_j(k)=K_k(L_j)\), one has \(R_4(k)=1\) for every \(1\le k\le16\), and
\[
K_k(D_t)
=t^4+t^3bR_3(k)+t^2b^2R_2(k)+tb^3R_1(k)+kb^4.
\]
This is the actual product-reference prefix, not a larger independently optimized relaxation.

All sixteen reference prefixes and the candidate’s coupled deficit table reconstruct as follows:
\[
m_k=\min(2k,8),\quad
A_k=R_3(k)-m_k,\quad
B_k=R_2(k)-k-m_k,\quad
C_k=R_1(k)-2k.
\]

| \(k\) | \(R_1(k)\) | \(R_2(k)\) | \(R_3(k)\) | \(m_k\) | \(A_k\) | \(B_k\) | \(C_k\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 6 | 4 | 2 | 2 | 3 | 2 |
| 2 | 7 | 9 | 5 | 4 | 1 | 3 | 3 |
| 3 | 10 | 12 | 6 | 6 | 0 | 3 | 4 |
| 4 | 13 | 15 | 7 | 8 | −1 | 3 | 5 |
| 5 | 16 | 18 | 8 | 8 | 0 | 5 | 6 |
| 6 | 18 | 19 | 8 | 8 | 0 | 5 | 6 |
| 7 | 20 | 20 | 8 | 8 | 0 | 5 | 6 |
| 8 | 22 | 21 | 8 | 8 | 0 | 5 | 6 |
| 9 | 24 | 22 | 8 | 8 | 0 | 5 | 6 |
| 10 | 26 | 23 | 8 | 8 | 0 | 5 | 6 |
| 11 | 28 | 24 | 8 | 8 | 0 | 5 | 6 |
| 12 | 29 | 24 | 8 | 8 | 0 | 4 | 5 |
| 13 | 30 | 24 | 8 | 8 | 0 | 3 | 4 |
| 14 | 31 | 24 | 8 | 8 | 0 | 2 | 3 |
| 15 | 32 | 24 | 8 | 8 | 0 | 1 | 2 |
| 16 | 32 | 24 | 8 | 8 | 0 | 0 | 0 |

There is no discrepancy with S1 lines 199–216.

## 4. Spin-flip identities and mixed-state marginal bounds

### 4.1 Compatible-layer identity

**SUPPORTED — S1 lines 141–163.**

The one-qubit identity
\[
\mathcal J(X)=YX^TY=\operatorname{Tr}(X)I_2-X
\]
gives, by tensor expansion on the actual density,
\[
\widetilde\rho=I-H_1+H_2-H_3+\rho.
\]

The map \(\mathcal J\) preserves trace, so taking a partial trace through the global spin flip gives the corresponding spin flip of the retained marginal. Global invariance therefore implies invariance of every marginal.

For each one-qubit marginal,
\[
\rho_i=\mathcal J(\rho_i)=I_2-\rho_i,
\]
and hence
\[
\rho_i=I_2/2,\qquad H_1=2I_{16}.
\]
Substituting \(\widetilde\rho=\rho\) into the four-qubit expansion yields
\[
\boxed{H_2=H_3+I_{16}.}
\]

This is an operator identity between layers of the **same density**. In particular, it remains an equality after application of every consuming projector.

### 4.2 Three-qubit antiunitary bound

**SUPPORTED — S1 lines 165–177.**

Every three-qubit marginal \(\sigma\) is invariant under
\[
\Theta_3=Y^{\otimes3}\mathcal K,
\qquad \Theta_3^2=-I.
\]
Thus \(\sigma\Theta_3=\Theta_3\sigma\).

If \(\sigma u=\lambda u\), then, because \(\lambda\) is real,
\[
\sigma\Theta_3u=\lambda\Theta_3u.
\]
Antiunitarity and \(\Theta_3^2=-I\) imply \(u\perp\Theta_3u\): applying
\(\langle\Theta x,\Theta y\rangle=\langle y,x\rangle\) with \(x=u\), \(y=\Theta u\) makes \(\langle\Theta u,u\rangle\) equal its own negative.

The largest eigenvalue consequently has multiplicity at least two. Positivity and \(\operatorname{Tr}\sigma=1\) give
\[
0\le\sigma\le I/2.
\]
There are four lifted three-body terms, so
\[
0\le H_3\le2I_{16},\qquad \operatorname{Tr}H_3=8.
\]

No pure-input restriction was used. For every complex rank-\(k\) orthogonal projector \(Q\),
\[
h_3:=\operatorname{Tr}(QH_3)\le2k,\qquad h_3\le8.
\]
Therefore
\[
h_3\le m_k,
\qquad
\operatorname{Tr}(QH_2)=k+h_3.
\]

### 4.3 Complete \(H_2\) layer majorization

**SUPPORTED — S1 lines 179–218.**

The reconstructed table has \(B_k\ge0\) for all sixteen prefixes. Hence
\[
\operatorname{Tr}(QH_2)
=k+h_3
\le k+m_k
\le R_2(k).
\]
Taking the maximum over all complex rank-\(k\) orthogonal projectors proves every Ky Fan inequality. At \(k=16\), both sides have trace \(24\). Thus the asserted \(H_2\) **majorization**, including its total-trace condition, follows for the complete invariant mixed-state sector.

## 5. The actual common-projector output bound

**SUPPORTED — S1 lines 220–241.**

Fix one actual density and one complex rank-\(k\) orthogonal projector \(Q\), and write \(q=\operatorname{Tr}(Q\rho)\le1\). Subtracting its physical output expectation from the exact reference prefix gives
\[
\begin{aligned}
G_k
&:=K_k(D_t)-\operatorname{Tr}[QT_t^{\otimes4}(\rho)]\\
&=t^4(1-q)
+t^3b(R_3(k)-h_3)\\
&\quad+t^2b^2(R_2(k)-k-h_3)
+tb^3(R_1(k)-2k).
\end{aligned}
\]
The same \(h_3\) occurs in both coupled layer terms. Since
\[
t^3b+t^2b^2\ge0,
\]
using \(h_3\le m_k\) and \(q\le1\) gives
\[
G_k\ge t^3bA_k+t^2b^2B_k+tb^3C_k.
\]

For every \(k\ne4\), all three displayed table entries are nonnegative. These fifteen prefixes therefore hold for all \(0\le t\le1\).

For \(k=4\), the lower bound is
\[
\begin{aligned}
-t^3b+3t^2b^2+5tb^3
&=tb(-t^2+3tb+5b^2)\\
&=\frac{tb}{4}(5-4t-5t^2).
\end{aligned}
\]
The quadratic has roots
\[
\frac{-2-\sqrt{29}}5,\qquad
\frac{-2+\sqrt{29}}5.
\]
Consequently this lower bound is nonnegative for
\[
0\le t\le\frac{\sqrt{29}-2}{5},
\]
and is also zero at \(t=1\), where \(b=0\).

The consuming interface is correct throughout: the proof never replaces the two-body and three-body layers by independently selected compatible-state maximizers, nor assumes their maxima occur on one projector.

For \(t_*<t<1\), the displayed **lower bound** on \(G_4\) is negative. This does not imply that \(G_4\) is negative for any physical density or projector. S1 correctly labels this as failure of the relaxation, not a state, layer, or channel counterexample.

## 6. Negative branch, physical interval, and boundaries

**SUPPORTED — S1 lines 426–454 and 226–241.**

The one-qubit identity
\[
T_{-t}=\mathcal J\circ T_t
\]
implies
\[
T_{-t}^{\otimes4}(\rho)
=W_4[T_t^{\otimes4}(\rho)]^TW_4,
\qquad W_4=Y^{\otimes4}.
\]
This is a **full transpose**, preserving spectrum, not a partial-transpose substitution.

Because \(W_4^T=W_4\), trace transposition gives
\[
\operatorname{Tr}[QT_{-t}^{\otimes4}(\rho)]
=\operatorname{Tr}[Q'T_t^{\otimes4}(\rho)],
\qquad Q'=W_4Q^TW_4.
\]
Transpose preserves idempotence and rank; unitary conjugation preserves those properties and Hermiticity. Thus \(Q'\) is an admissible complex orthogonal projector of the same rank. It is transported once and used consistently for the positive-branch bound.

For physical \(p>1\), \(t=p-1\le1/3<t_*\), so the whole negative physical branch lies inside the full-prefix region. Intersecting \(|1-p|\le t_*\) with \(0\le p\le4/3\), and adding the physical \(t=1\) endpoint, gives exactly
\[
\boxed{
p\in\left[\frac{7-\sqrt{29}}5,\frac43\right]\cup\{0\}.
}
\]

The boundary cases require no division by \(t\), \(b\), or a spectral gap:

- **\(t=0\), \(p=1\):** actual and reference outputs are \(I_{16}/16\); every projector prefix is equal.
- **\(t=t_*\):** the fourth-prefix lower bound is zero, so the endpoint is included. This establishes the weak inequality, not a claim of actual saturation.
- **\(t=1\), physical \(p=0\):** the output is \(\rho\), and the reference has pure spectrum. The bound is \(\operatorname{Tr}(Q\rho)\le1\). An arbitrary invariant mixed density is not being described as having pure spectrum.
- **\(k=16\):** trace equality holds for all parameters.
- For \(0<t<1\), \(B_k>0\) at every proper prefix. Thus every proper \(k\ne4\) has a strictly positive established gap; the fourth prefix has a strictly positive established gap for \(0<t<t_*\).

Local covariance is consistent with the statement’s physical-basis freedom. No independent-marginal replacement or extra tensorization premise is needed.

## 7. Per-claim disposition and exclusions

| Claim | Disposition | S1 logical lines |
|---|---|---|
| Actual subset expansion, multiplicities, and product-reference prefixes | **SUPPORTED** | 78–137 |
| Invariant one-body marginals, \(H_1=2I\), and \(H_2=H_3+I\) | **SUPPORTED** | 141–163 |
| Three-body marginal antiunitary pairing, \(H_3\le2I\), and trace 8 | **SUPPORTED** | 165–177 |
| All sixteen compatible \(H_2\) layer prefixes | **SUPPORTED** | 179–218 |
| Actual fixed-projector channel bound for all \(k\ne4\), all physical \(p\) | **SUPPORTED** | 220–226, 426–454 |
| Fourth-prefix closed region and physical-\(p\) translation | **SUPPORTED** | 226–241, 445 |
| Negative relaxed bound outside that region does not establish a physical counterexample | **SUPPORTED** | 241, 500–513 |
| Full Dicke-orbit theorem and prior-hull enlargement | **INCONCLUSIVE in this review; outside F510 audit scope** | 243–477 |
| Unrestricted four-qubit \(H_2\), unrestricted channel majorization, or general blocklength | **NOT PROVED by this reviewed argument** | 479–523 |

There are no refuted claims within the frozen F510 scope and no actionable mathematical defect to report there.

The supported result remains a **same-harness written reconstruction**. It is not independent-model-family, human, formal/kernel, finite-execution, novelty, or automatic-adoption assurance. Parent disposition is still required. The unrestricted original target remains open, and no held episode or consumer has been rehabilitated.

**overall_correctness:** correct  
**explanation:** The complete frozen F510 invariant-sector argument reconstructs without a mathematical defect: its compatible-layer identity, antiunitary bound, sixteen-prefix table, fixed-projector channel comparison, and full-transpose physical transport are valid. This verdict is limited to that frozen scope and does not accept the separate Dicke/hull claims or close the unrestricted four-qubit target.  
**confidence:** 0.98