## Verdict: ACCEPT-WITH-FIXES

The substantive hand proof checks out: I independently re-derived the two-cut kernel dimension, the LU tangent dimension, and the implicit-function argument without using computation receipts. One formal group-action error should be corrected; it does not change the orbit, dimension counts, or conclusions.

**Reviewed snapshot:** [PROOF.md:1–191](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/dualunitary-t7/review/PROOF.md), Git blob SHA-1 **33f139267ef066939baecfd40ae175583b4df604**, obtained from the full-index, read-only diff.

## Finding

### 1. [P2] Make the LU parametrization a genuine group action

**Location:** [PROOF.md:11](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/dualunitary-t7/review/PROOF.md#L11)  
**Confidence:** 1.0

With ordinary componentwise multiplication on \(G=U(3)^4\), the displayed formula is not a left action: composing \(\Phi_g\Phi_h\) produces right factors \(h_3g_3,h_4g_4\), whereas \(\Phi_{gh}\) has \(g_3h_3,g_4h_4\). This makes the action/equivariance justification invoked at lines 127–128 formally incorrect for noncommuting right factors. **Concrete fix:** define the acting group as \(U(3)^2\times U(3)_{\mathrm{op}}^2\), retaining every displayed transformation formula. It is a compact connected Lie group isomorphic to \(U(3)^4\), and all subsequent orbit and tangent arguments then apply unchanged.

No other actionable correctness defect found.

## Independent derivations and checks

### 1. Source conventions and the three cuts — correct

The pinned survey’s definitions at `2508.04777v3.layout.txt:239–241` agree with the proof.

Expanding indices gives both LU covariance formulas in §1.3, including the transposes—not adjoints—on the indicated factors. Those transposes remain unitary when the original factors are unitary.

For \(\psi_U(a,b,c,d)=U_{cd,ab}\), I obtain exactly
\[
M_{12}=U^T,\qquad M_{13}=S_9U^RS_9,\qquad
M_{14}=(U^\Gamma)^TS_9.
\]
In particular,
\[
[(U^\Gamma)^TS_9]_{ad,bc}
=U^\Gamma_{cb,ad}=U_{cd,ab}.
\]
**The corrected \(M_{14}\) formula is right.**

I checked the nine C7 entries against the pinned bounding-box extraction. They give \(P_9|ab\rangle=|2a+b,a+b\rangle\).

The source-representative bridges need no exhaustive-search receipt. Writing \(Q|x\rangle=|2x\rangle\), direct substitution gives:

- survey state (14), under the proof’s dictionary: \(P_{(14)}=P_9(Q\otimes I)\);
- [44], matrix (A14): \(P_{(A14)}=(I\otimes Q)P_9\);
- \(P_9S_9=(Q\otimes I)P_9\).

Thus the representative changes and the optional swap route are justified by elementary identities.

### 2. Perfectness, the involutions, and the free \(S_3\) action — correct

The generator columns represent the four distinct projective directions in \(\mathbf F_3^2\); every pair is independent. A nonzero codeword therefore cannot vanish in two coordinates, giving minimum distance three. The nine disjoint radius-one balls contain
\[
9(1+4\cdot2)=81
\]
points, proving the asserted unique representation \(y=c+te_q\).

Reassembling the two projected codewords gives
\[
\tau_S(c,q,t)=(c+t g_{q,\sigma_S(q)},q,-t).
\]
For distinct matchings,
\[
\tau_S\tau_{S'}(c,q,t)
=(c+t(g_{q,\sigma_{S'}(q)}-g_{q,\sigma_S(q)}),q,t).
\]
The translation vector is nonzero: equality of the two \(g\)'s would produce a nonzero codeword with two zero coordinates. Hence the rotations have order three and no off-code fixed points. Reflections flip nonzero \(t\), so also have no fixed points. This proves the six-element group and the **12 free six-point orbits**.

### 3. Real kernel dimension and conjugation parity — correct

The linearized Gram equation gives precisely the stated diagonal condition and off-code relation
\[
\delta\psi(\tau y)=-\overline{\delta\psi(y)}.
\]

Parity is well-defined: every odd word flips \(t\), so an odd word cannot represent the identity. On each free orbit, an arbitrary \(z\in\mathbf C\) therefore extends as \(z\) at even elements and \(-\bar z\) at odd elements. There is **no additional reality or imaginary-value restriction** on \(z\).

The code contributes nine imaginary parameters; the 12 off-code orbits contribute two real parameters each:
\[
\dim_{\mathbf R}\ker dF=9+12\cdot2=33.
\]
This argument applies to both designated pairs of cuts.

### 4. LU tangent rank \(24+9\) — correct

At an off-code point \(c+te_q\), only the \(q\)-th local generator contributes, with value \(h_q[c_q+t,c_q]\). The 12 complex anti-Hermitian off-diagonal parameters have disjoint, nonempty supports, so contribute 24 real dimensions.

The real diagonal-function claim also holds. An explicit real basis is
\[
1,\quad
\cos(2\pi\ell_q/3),\ \sin(2\pi\ell_q/3)
\quad(q=1,2,3,4).
\]
Their complex Fourier frequencies are the zero frequency and all eight distinct nonzero frequencies of \(\mathbf F_3^2\). Consequently they are nine real-linearly independent functions. This supplies the real-versus-complex step compressed into lines 114–115; it is not an unproved rank assumption.

The diagonal and off-diagonal images have disjoint supports, proving rank 33.

### 5. Implicit-function theorem, component, and uniform \(\epsilon\) — correct after the action fix

The hand-derived kernel gives derivative rank 129, so 129 independent real output components exist **without knowing any certified minor**.

Their zero set is locally a 33-manifold containing the dual-unitary locus. The embedded 33-dimensional LU orbit lies inside that manifold; its inclusion is a local diffeomorphism and hence has open image. Taking the subsequent neighborhood \(W_2\subset W_1\), which is always possible, yields the claimed local equality.

This is a valid subsystem/orbit-containment argument—not an unsupported inference from tangent equality alone. LU covariance transports the equality along the orbit. Compactness then gives positive distance from the orbit to the closed exterior of the resulting neighborhood. Being connected, relatively open, and closed makes the orbit a connected component. The same argument works for T-duality independently.

### 6. Qualitative entangling-power gap and T7 — correct

The eigenvalue inequality gives
\[
E(U)\le 1-\frac1{d^2},
\]
with equality exactly when \(U^R\) is unitary; the corresponding partial-transpose statement follows identically. With source normalization (11a), \(e_p=1\) is therefore equivalent to 2-unitarity.

The published uniqueness theorem explicitly covers **all** order-nine 2-unitaries, not only permutations or minimal-support representatives. Combining it with isolation makes the non-2-unitary complement in \(D\), respectively \(T\), compact. Continuity and attainment then establish a strict maximum below one.

The proof correctly distinguishes:

- **Literal T7:** yes, through distinct LU images approaching \(P_9\).
- **Non-2-unitary interpretation:** no, in dimension three.

No hypothesis about real matrices, permutation perturbations, or minimal support has been silently imposed.

## Assumptions and limits

- The proof uses ordinary finite-dimensional smooth-manifold/compact-Lie-orbit results.
- The global identification of the 2-unitary set imports **Rather–Ramadas–Kodiyalam–Lakshminarayan, Theorem 1**. I checked its statement, conventions, main reduction, and representative; I did not independently re-prove its complete appendix.
- The gap concerns non-2-unitaries **inside \(D\) or \(T\)**, not arbitrary non-2-unitary members of \(U(9)\).
- No explicit gap, explicit \(\epsilon\), higher-dimensional conclusion, novelty, or priority is established by this review.

**Read scope:** full proof; frozen contract; survey layout lines 1–40, 220–283, 367–433, 505–581, 1388–1412, 1770–1815; C7 bounding-box coordinates; uniqueness-paper layout lines 1–40, 174–275, 877–934; both PDFs’ extracted front matter; targeted citation searches. Required source passages were accessible locally. No external literature/status search or visual PDF rendering was performed.

**Not performed:** no earlier review notes read; no implementation receipts or source code used as lemma evidence; no scripts, rank computations, tests, builds, delegation, or writes.

**Overall correctness:** incorrect as literally written only in the declared group-action convention; the candidate theorem and corollary are otherwise supported by the hand argument.  
**Overall confidence:** 0.97.
