# UNREVIEWED author candidate: full-physical-range k3 bound for a low-polarization entangled sector

## 1. Result and exact scope

Consider the original four-qubit channel
\[
\Phi_p(X)=(1-p)X+\frac p2\operatorname{Tr}(X)I,
\qquad
\Lambda_p=\Phi_p^{\otimes4}.
\]
Its physical range is \(0\le p\le4/3\). Write
\[
t=|1-p|,\qquad a=\frac{1+t}{2},\qquad b=\frac{1-t}{2},
\]
and
\[
R_3(t)=a^4+2a^3b,\qquad
16R_3(t)=3+8t+6t^2-t^4.
\]
This is exactly the sum of the three largest output eigenvalues for a pure product input.

For a normalized, arbitrarily complex pure state \(\rho=|\psi\rangle\langle\psi|\), order its one-qubit Bloch radii as
\[
r_1\ge r_2\ge r_3\ge r_4\ge0
\]
and define
\[
s=\sum_{i=1}^4r_i^2,\qquad
L=3r_1+3r_2+r_3+r_4.
\]
Let
\[
W=Y^{\otimes4},\qquad
\widetilde\rho=W\rho^TW,
\qquad
\tau=\operatorname{Tr}(\rho\widetilde\rho)
=\left|\langle\psi|W\overline\psi\rangle\right|^2.
\]
Finally put
\[
c=\sqrt{39(s+2+4\tau)},\qquad
\kappa(\psi)=14-L+4\tau-c.
\]

### Structural author theorem

For every such pure state, every physical \(p\), and every **complex orthogonal rank-three projector** \(Q\),
\[
\boxed{
\operatorname{Tr}\!\left(Q\Lambda_p(\rho)\right)
\le K_3\!\left(\Lambda_p(\rho)\right)
\le R_3(t)-\frac{\kappa(\psi)}{16}t(1-t^2).
}
\]

Consequently, \(\kappa(\psi)\ge0\) is a sufficient certificate for the actual k3 target throughout the physical parameter range.

### Uniform entangled-sector corollary

If
\[
\boxed{\sum_i r_i^2\le\frac14,}
\]
then \(\kappa(\psi)>1/8\), and therefore
\[
\boxed{
K_3\!\left(\Lambda_p(\rho)\right)
\le R_3(t)-\frac{t(1-t^2)}{128}
\qquad(0\le p\le4/3).
}
\]

The same bound holds for every convex mixture of pure states **individually** satisfying \(s\le1/4\).

This includes every pure state with maximally mixed one-qubit marginals, and the convex hull of those pure states. It is a full-physical-range result on a specified entangled sector—not a claim that the existing all-density \(1/142\) interval has been enlarged. Small Bloch radii of a mixed state alone are not asserted to establish membership in this convex hull. Other Ky Fan indices and full majorization are not claimed.

---

## 2. Elementary variational facts

For Hermitian \(H\),
\[
K_3(H)=\max_{\substack{Q=Q^\dagger=Q^2\\\operatorname{rank}Q=3}}
\operatorname{Tr}(QH).
\]
To see this, diagonalize \(H\): the diagonal entries of a rank-three orthogonal projector lie in \([0,1]\) and sum to three, so the maximum selects the three largest eigenvalues.

It follows directly that \(K_3\) is subadditive, positively homogeneous and convex. These statements concern all complex projectors; no real-state restriction is used.

## 3. Pure-state Pauli identities

Expand
\[
\rho=\frac1{16}(I+C_1+C_2+C_3+C_4),
\]
where \(C_w\) contains all Pauli-string terms of weight \(w\). Let \(A_w\) be the sum of their squared coefficients. Hermiticity makes these coefficients real even when the state has complex amplitudes. Pauli orthogonality gives
\[
\operatorname{Tr}(C_wC_v)=
\begin{cases}
16A_w,&w=v,\\
0,&w\ne v.
\end{cases}
\]
In particular \(A_1=s\), and purity gives
\[
1+s+A_2+A_3+A_4=16. \tag{1}
\]

For a subsystem \(J\), its purity is \(2^{-|J|}\) times the sum of squared coefficients supported in \(J\). A pure state’s marginal and complementary marginal have identical nonzero eigenvalues. Summing the four one-qubit versus complementary three-qubit purities therefore yields
\[
2+\frac s2=\frac{4+3s+2A_2+A_3}{8}.
\]
Hence
\[
A_3=12+s-2A_2,\qquad A_4=3-2s+A_2. \tag{2}
\]

Spin flip changes every weight-\(w\) Pauli term by \((-1)^w\). Thus
\[
\tau=\frac{1-s+A_2-A_3+A_4}{16}
=\frac{A_2-s-2}{4},
\]
or
\[
\boxed{A_2=s+2+4\tau.} \tag{3}
\]
Also \(0\le\tau\le1\), because it is the squared overlap of two normalized vectors.

These identities hold for arbitrary complex phases. The complementary-marginal step is an explicitly derived purity identity, **not** an erasure-channel Ky Fan bound. No one-erasure/L1 assertion is invoked.

## 4. Bounds on the first two correlation layers

The summands of \(C_1\) act on different qubits, so its eigenvalues are signed sums of the \(r_i\). Its three largest eigenvalues sum to
\[
K_3(C_1)=3r_1+3r_2+r_3+r_4=L,
\]
including zero-radius and degeneracy cases. Consequently,
\[
L\le\sqrt{(9+9+1+1)\sum_i r_i^2}
=\sqrt{20s}. \tag{4}
\]

For every complex rank-three projector \(Q\), tracelessness of \(C_2\) and Hilbert–Schmidt Cauchy–Schwarz give
\[
\begin{aligned}
\operatorname{Tr}(QC_2)
&=\operatorname{Tr}\left[\left(Q-\frac3{16}I\right)C_2\right]\\
&\le
\sqrt{\operatorname{Tr}\left(Q-\frac3{16}I\right)^2}
\sqrt{\operatorname{Tr}(C_2^2)}\\
&=\sqrt{\frac{39}{16}}\sqrt{16A_2}
=\sqrt{39A_2}=c.
\end{aligned}
\]
Therefore
\[
K_3(C_2)\le c. \tag{5}
\]

## 5. Exact decomposition retaining the negative rank-one term

First take \(p=1-t\), with \(0\le t\le1\). Define
\[
\alpha=\frac{t^3(1+t)}2,\qquad
\beta=\frac{t^3(1-t)}2,
\qquad
B=\alpha\rho-\beta\widetilde\rho.
\]
Comparison of the five Pauli weights gives the exact identity
\[
\boxed{
\Lambda_{1-t}(\rho)
=
B+\frac{1-t^4}{16}I
+\frac{t-t^3}{16}C_1
+\frac{t^2-t^4}{16}C_2.
} \tag{6}
\]
There is no perturbative remainder.

Set
\[
d=\sqrt{1-(1-t^2)\tau}.
\]
The two potentially nonzero eigenvalues of \(B\) are
\[
\lambda_\pm=\frac{t^4\pm t^3d}{2}. \tag{7}
\]
Indeed, on the span of \(\psi\) and \(W\overline\psi\), its trace is \(\alpha-\beta=t^4\), and its determinant is
\(-\alpha\beta(1-\tau)\), which gives (7). The formula extends to coincident vectors by continuity or direct substitution.

Because \(d\ge t\), one has \(\lambda_-\le0\le\lambda_+\). Its remaining fourteen eigenvalues vanish, so
\[
K_3(B)=\lambda_+.
\]
This also covers \(t=0,1\), \(\tau=1\), and rank drops.

Subadditivity applied to (6), with its nonnegative remaining coefficients, now gives
\[
16K_3(\Lambda_{1-t}(\rho))
\le
3+Lt+ct^2+(8d-L)t^3+(5-c)t^4. \tag{8}
\]
Subtracting this from the exact product target,
\[
\begin{aligned}
16\bigl[R_3(t)-K_3(\Lambda_{1-t}(\rho))\bigr]
\ge{}&
t(1-t^2)\bigl[8-L-(c-6)t\bigr]\\
&+8t^3(1-d).
\end{aligned} \tag{9}
\]

For \(0\le x\le1\), \(\sqrt{1-x}\le1-x/2\). Therefore (9) is at least
\[
t(1-t^2)f(t),
\qquad
f(t)=8-L-(c-6)t+4\tau t^2. \tag{10}
\]

Moreover,
\[
\begin{aligned}
c^2-(6+8\tau)^2
&=39s+42+60\tau-64\tau^2\\
&\ge38>0.
\end{aligned}
\]
The quadratic \(42+60\tau-64\tau^2\) is concave and has endpoint values \(42\) and \(38\) on \([0,1]\). Thus \(c-6>8\tau\), and
\[
f'(t)=-(c-6)+8\tau t<0
\qquad(0\le t\le1).
\]
It follows that
\[
f(t)\ge f(1)=14-L+4\tau-c=\kappa(\psi).
\]
This proves the structural inequality for \(p=1-t\), without restricting the input sector.

## 6. A uniform certificate for \(s\le1/4\)

Suppose \(s\le1/4\). By (4),
\[
L\le\sqrt5<\frac94,
\qquad
c^2\le\frac{351}{4}+156\tau.
\]
For \(0\le\tau\le1\),
\[
\begin{aligned}
\left(\frac{93}{8}+4\tau\right)^2
-\left(\frac{351}{4}+156\tau\right)
&=\frac{3033}{64}-63\tau+16\tau^2\\
&\ge\frac{25}{64}>0.
\end{aligned}
\]
The quadratic decreases on \([0,1]\), since its derivative is \(-63+32\tau<0\), and its value at \(\tau=1\) is \(25/64\). Therefore
\[
c<\frac{93}{8}+4\tau.
\]
Consequently,
\[
\boxed{
\kappa(\psi)
=14-L+4\tau-c
>14-\frac94-\frac{93}{8}
=\frac18.
}
\]
Together with (9)–(10), this proves the uniform sector corollary.

For a mixture \(\rho=\sum_j w_j\rho_j\), where each pure \(\rho_j\) satisfies \(s_j\le1/4\), apply the pure inequality at the **same arbitrary \(Q\)** and sum. Maximization over \(Q\) proves the mixed-sector statement.

For the particularly important \(s=0\) sub-sector, there is also a stronger explicit certificate:
\[
\kappa=14+4\tau-\sqrt{78+156\tau}
\ge18-\sqrt{234}>0.
\]
The expression decreases on \([0,1]\), so its minimum is at \(\tau=1\).

## 7. Physicality and the negative Bloch-parameter branch

Writing \(q=1-p\), the single-qubit channel is the Pauli mixture with probabilities
\[
\frac{1+3q}{4}\quad\text{for }I,
\qquad
\frac{1-q}{4}\quad\text{for each of }X,Y,Z.
\]
These are nonnegative precisely for \(-1/3\le q\le1\), equivalently \(0\le p\le4/3\). Thus all outputs claimed here are physical.

Let \(S(A)=WA^TW\). Its action on weight-\(w\) Pauli strings is multiplication by \((-1)^w\), giving
\[
\Lambda_{1+t}(\rho)=S\!\left(\Lambda_{1-t}(\rho)\right). \tag{11}
\]
Transposition followed by unitary conjugation preserves the spectrum. Hence the same \(K_3\) bound holds on the physical negative-\(q\) branch \(0\le t\le1/3\). Equation (11) is derived here, not imported from the withdrawn reflection sentence.

The consuming projector is explicit: for complex \(Q\),
\[
Q'=WQ^TW
\]
is again an orthogonal rank-three projector, and, because \(W^T=W\),
\[
\operatorname{Tr}(QS(A))=\operatorname{Tr}(Q'A).
\]
Thus reflection correctly transports the actual rank-three observable; there is no real-\(Q\) assumption.

At \(t=0\), both sides of the target equal \(3/16\). At \(t=1\), a pure input has \(K_3=1=R_3(1)\). For \(0<t<1\), the uniform sector has a strictly positive certified gap. No nonphysical parameter range is claimed.

## 8. Explicit entangled content

An arbitrary-phase family inside the sector is
\[
|\psi_{u,\phi}\rangle
=
\sqrt u\,|0000\rangle
+e^{i\phi}\sqrt{1-u}\,|1111\rangle,
\qquad
\frac38\le u\le\frac58,
\quad \phi\in\mathbb R.
\]
Its local radii satisfy
\[
s=4(2u-1)^2\le\frac14.
\]
Across every nontrivial bipartition its two nonzero Schmidt coefficients are \(\sqrt u\) and \(\sqrt{1-u}\); hence every member is entangled across every such bipartition.

This is a written membership example, not the proof. The theorem covers **all** complex pure states satisfying the radius condition, not merely GHZ states, real amplitudes, or a finite set of selected cases.

## 9. Remaining global obligation

The scalar certificate is not necessary. For \(|0000\rangle\),
\[
s=4,\quad L=8,\quad\tau=0,\quad
\kappa=6-\sqrt{234}<0,
\]
although the actual k3 target is attained exactly. A negative \(\kappa\) is therefore failure of this sufficient certificate, not a counterexample.

The loss is identifiable: (8) separately maximizes \(B,C_1,C_2\), discarding their alignment at the same \(Q\). A precise sufficient next obligation can be written using the nonnegative slacks
\[
\Delta_B=\lambda_+-\operatorname{Tr}(QB),\quad
\Delta_1=L-\operatorname{Tr}(QC_1),\quad
\Delta_2=c-\operatorname{Tr}(QC_2).
\]
The preceding derivation gives
\[
\begin{aligned}
16\bigl[R_3-K_3\bigr]
\quad\text{at a maximizing }Q
\ge{}&
t(1-t^2)f(t)
+16\Delta_B\\
&+(t-t^3)\Delta_1+(t^2-t^4)\Delta_2.
\end{aligned}
\]
Thus a sufficient remaining inequality in the uncovered region is
\[
\boxed{
16\Delta_B+(t-t^3)\Delta_1+(t^2-t^4)\Delta_2
\ge t(1-t^2)\max\{0,-f(t)\}.
}
\]
This joint-slack inequality is **unproved here**. Unlike independent norm optimization, it requires the actual common projector. For the pure product example, \(\Delta_B=\Delta_1=0\) and \(\Delta_2=c-6\), exactly supplying the deficit in (10).

The unrestricted k3 theorem remains **OPEN**. The proposed next step is a joint correlation-layer comparison in the highly polarized region, without importing the quarantined one-erasure/L1 route.

## 10. Methods, chronology, pins and limitations

- **Role and assurance:** GENERAL AUTHOR development; all results above remain **UNREVIEWED** pending separate disjoint review and parent disposition. No independent-family, human, formal, novelty, or acceptance claim is made.
- **Native observations made in this run:** start clock `2026-10-30T15:39:24Z`; substantive derivation clocks `2026-10-30T15:45:56Z` and `2026-10-30T15:47:06Z`. These are actual tool observations, not reconstructed cognition times. Scope/start are recorded in this return rather than claimed as a prior live announcement.
- **Read-order exception:** an initial packet preview was requested alongside the manifest/receipt before all six controls had been read. All controls, complete S1 and pins were subsequently read before mathematical derivation. The complete packet was reread after controls. This disclosure does not retroactively assert that controls preceded the first preview.
- **Inputs:** complete manifest, receipt, six named controls, and all seventeen S1 lines—including endings and previously truncated long lines—were read. No held payload or linked scientific consumer was followed. S1 supplied target/status context; its adopted theorem is not a premise above.
- **Scientific methods:** written algebra and the two disclosed fresh written examples only. No scientific program, numerical experiment, solver, public-source search, external-model CLI, or package installation was used. Accordingly there are no scientific code/inputs/numerical outputs to preserve. All load-bearing identities are proved above rather than imported from an uncited theorem.
- **Own metadata checks:** SHA-256 and LF/byte counts matched the manifest entries. A metadata-only byte comparison returned `packet_source_equal: True packet_source_lines: 17 source_lines: 17`. It read bytes with line endings retained, removed the `S1|line|` prefixes from packet lines 3–19, and compared them to the seventeen original S1 byte lines.
- **Parent-supplied corroboration:** the complete `parent-live-metadata-supply-v1.json` was read after the candidate-write refusal. Its observation at `2026-10-30T08:47:07-0700 PDT` is **parent-supplied**, not this agent’s start or execution.

Verified principal pins:

| Artifact | SHA-256 | Bytes / LF |
|---|---|---:|
| Manifest | `397924389c738117ec83756558482ff3afc01d6a175c91a3d0e92b6ec734a96d` | 4870 / 67 |
| Receipt | `2503b5a2e7279fcaad2aa39e0abb5c39dac9130dc4e35ee17225dd6df4791c69` | 1366 / 34 |
| Packet | `33d37978be00a4b9fdd8785808bbc8e2cc1cc3c84571965cb6f9647fa7ec9192` | 5002 / 19 |
| S1 | `bb16e861cedad17fc2a9eb9520dba4cb7bdbd69ad3cd510df2e7bd59060f8b54` | 4873 / 17 |

All six control hashes and sizes also matched their manifest pins. No source snapshot was changed.

**Disposition requested:** separately check the Pauli identity (3), signed rank-two spectrum (7), common-projector variational bound (8), uniform \(1/8\) certificate, and physical reflection (11). Until that gate returns, this is an **UNREVIEWED full-range restricted-sector author theorem**, not a global solution.