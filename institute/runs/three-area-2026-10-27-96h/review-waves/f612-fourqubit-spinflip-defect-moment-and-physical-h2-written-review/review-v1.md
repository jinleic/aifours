# F612 — WRITTEN review of the F598 non-invariant four-qubit candidate

**Overall correctness: correct at the frozen, explicitly scoped inputs.**

**Explanation:** The mixed-state defect region \(d^2\le 3/13\), the pure-state region \(\eta\ge55/72\), and their all-physical-channel, all-sixteen-prefix conclusions follow from the written argument. The universal genuinely entangled family and its separation from the four named classes are also supported. This does not establish unrestricted four-qubit majorization.

**Confidence: 0.98.**

**Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

## 1. Review identity, read coverage, and method

Frozen wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f612-fourqubit-spinflip-defect-moment-and-physical-h2-written-review/`

Supplied pins:

- Manifest: `a0d4e0dab39c78555c99ab24e669a1071648cea3764c9ae805ca0f5fff7340a1`
- Freeze receipt: `7d686af30e14f8c02b74033a4b465bf466b92f103617eaee0b83544bdcc791fd`
- Literal packet: `6f13a3ca0b89a2dcf1533e7c985937c5a54c871b14e56214e198ca2548cc4c33`

These hashes, byte counts, LF counts, and the clock observation `2026-10-30T14:21:00-0700 PDT` are **parent-supplied live metadata**, not reviewer-native executions or a reviewer-native start time.

I completed the manifest, freeze receipt, parent metadata supply, and all thirteen status-only controls before sending the required pre-body acknowledgement directly to `agent://Main`. The controls included the entire-episode and consumer exclusions for f586 and the other listed held episodes.

Only after that acknowledgement did I read the mathematical packet. The reads were ordered raw windows of at most twenty LF: \(1\!-\!20,21\!-\!40,\ldots,801\!-\!820\), followed by the ending at \(821\!-\!835\). Coverage includes:

- S1 through logical line 765;
- S2 through line 31;
- S3 through line 37;
- the packet ending.

Derivation began after this complete read. No packet elision remained.

This was a **WRITTEN-only, same-harness reconstruction**. I used general variables and literal objects already present in the packet. I did not select an additional state, \(y\), parameter, Pauli instance, or diagnostic example; run scientific code, CAS, enumeration, or spectral computation; follow a linked scientific source; read a sibling review or held scientific payload; or use an external-model CLI.

This complete body is returned for Main materialization. No repository write or write bypass was attempted.

## 2. Exact input boundary

The reviewed candidate is packet S1:

`review-waves/f598-actual-noninvariant-four-qubit-common-projector-majorization-frontier/review-v1.md`

SHA-256:

`922575b7e823438269cd0dbd15bd0d6ed5f6233bad6fee6dccfb485e06571b88`

The adopted interface imported from packet S2 is confined to **actual spin-flip-invariant four-qubit densities**:

\[
0\le H_3(\sigma)\le2I,\qquad
\operatorname{Tr}H_3(\sigma)=8,\qquad
K_4(H_3(\sigma))\le6,
\]

together with

\[
H_2(\sigma)=I+H_3(\sigma).
\]

S2 is:

`dispositions/physics-2-all-mixed-spinflip-invariant-fourqubits-sharp-fourth-prefix-and-channel-parent-v1.md`

SHA-256:

`3c4b77b9ab49bf46e384f9106c1e8db3e0b94e6d8e70e6223cb286aa6c018f78`

Its universal invariant-sector theorem is the imported premise. I did not substitute its finite checks for that theorem or follow its linked proofs/checker.

Packet S3 is:

`dispositions/physics-2-coherent-vacuum-w4-all-physical-prefixes-and-h3-moment-certificate-parent-v1.md`

SHA-256:

`24751b4d1e2dd15a10f0f080500050ed40bad534cb0f086e639343a5a0dc3189`

The unrestricted pure-state moment identity recorded there is independently reconstructed below. Its literal vacuum/W4 support also suffices for the \(\eta=0\) class comparison. Its reported numerical spectral checks are not upgraded to exact spectral verification.

## 3. Per-claim disposition

| Candidate claim | S1 logical lines | Disposition |
|---|---:|---|
| Physical even/odd Pauli identities and pure moment formula | 171–274 | **SUPPORTED** |
| Mixed-state moment estimate \( \operatorname{Tr}H_3^2\le10(1+d^2)\) | 278–321 | **SUPPORTED** |
| Pure physical rank bound and the two moment certificates | 325–391 | **SUPPORTED** |
| Actual \(H_2\) majorization for \(d\le1/2\) | 397–479 | **SUPPORTED** |
| Universal \(H_1\), common-projector channel consumption, and all sixteen prefixes | 483–574 | **SUPPORTED** |
| Full physical negative-retention branch | 578–608 | **SUPPORTED** |
| Mixed theorem \(d^2\le3/13\), pure theorem \(\eta\ge55/72\), and finite-mixture consequence | 59–133 | **SUPPORTED** |
| Relation to the \(\Theta_4\)-real \(x+iy\) decomposition | 612–640 | **SUPPORTED** |
| Universal GME, non-invariant family outside the named hull | 644–717 | **SUPPORTED** |
| Stated remaining unrestricted frontier | 721–746 | **SUPPORTED as a limitation of this proof** |

The original author’s activity-history statements are author reports in the frozen body; this review does not independently certify that earlier actor’s execution or access history.

## 4. Actual-state identities and the mixed moment estimate

Write

\[
\widetilde\rho=Y^{\otimes4}\rho^TY^{\otimes4},\qquad
\sigma=\frac{\rho+\widetilde\rho}{2},\qquad
\Delta=\rho-\sigma.
\]

Both \(\rho\) and \(\widetilde\rho\) are physical densities. Hence \(\sigma\) is a physical density, \(\widetilde\sigma=\sigma\), and

\[
\Delta^\dagger=\Delta,\qquad
\operatorname{Tr}\Delta=0,\qquad
d=\|\Delta\|_1=\frac12\|\rho-\widetilde\rho\|_1\le1.
\]

There is no replacement of the actual invariant part by an independently chosen operator.

For the physical Pauli expansion, spin flip changes exactly the odd-weight signs. Consequently,

\[
\rho=\frac1{16}(I+R_1+R_2+R_3+R_4),
\]

\[
\sigma=\frac1{16}(I+R_2+R_4),\qquad
\Delta=\frac1{16}(R_1+R_3).
\]

Counting the actual subsets containing each Pauli support gives

\[
H_1=2I+\frac12R_1,
\]

\[
H_2=\frac14(6I+3R_1+R_2),
\]

\[
H_3=\frac18(4I+3R_1+2R_2+R_3).
\]

In particular,

\[
H_2(\rho)-H_2(\sigma)=\frac34R_1,
\qquad
H_3(\rho)-H_3(\sigma)=\frac18(3R_1+R_3).
\]

These identities all concern the same density and tensor positions.

### Pure moment identity

For a pure density, Pauli orthogonality gives

\[
\operatorname{Tr}\rho^2
=\frac{1+S_1+S_2+S_3+S_4}{16}=1,
\]

while

\[
\operatorname{Tr}(\rho\widetilde\rho)
=\frac{1-S_1+S_2-S_3+S_4}{16}
=\eta.
\]

Subtracting yields

\[
S_1+S_3=8(1-\eta).
\]

Equality of complementary marginal purities gives

\[
\frac{4+S_1}{2}
=
\frac{4+3S_1+2S_2+S_3}{8},
\]

and therefore

\[
2S_2+S_3=12+S_1.
\]

Thus

\[
S_3=8-8\eta-S_1,\qquad
S_2=2+4\eta+S_1.
\]

The physical \(H_3\) expansion gives

\[
\operatorname{Tr}H_3^2
=4+\frac14(9S_1+4S_2+S_3)
=8+3S_1+2\eta.
\]

This establishes the coefficient \(2\eta\) for unrestricted pure inputs by written identities, not by an \(\eta=0\) finite sample.

### Invariant mixed part

Because \(\Theta_4^2=I\), an invariant density has an orthonormal spectral decomposition into \(\Theta_4\)-fixed vectors: in a \(\Theta_4\)-real basis it is a real symmetric positive matrix.

Every invariant pure component has \(S_1=0\) and \(\eta=1\), hence moment \(10\). Linearity of \(H_3\) and convexity of its squared Hilbert–Schmidt norm therefore imply

\[
\operatorname{Tr}H_3(\sigma)^2\le10.
\]

### Defect control of the odd part

Every one-qubit marginal of \(\sigma\) is \(I/2\). Contractivity of the trace norm for Hermitian inputs under physical partial trace gives

\[
|\mathbf r_i|
=\|\rho_i-I/2\|_1
=\|\operatorname{Tr}_{i^c}\Delta\|_1
\le d.
\]

Consequently,

\[
S_1=\sum_i|\mathbf r_i|^2\le4d^2.
\]

The positive and negative parts of the traceless Hermitian \(\Delta\) each have trace \(d/2\). Therefore

\[
\operatorname{Tr}\Delta^2
\le2(d/2)^2=\frac{d^2}{2},
\]

and Pauli orthogonality gives

\[
S_1+S_3=16\operatorname{Tr}\Delta^2\le8d^2.
\]

Finally, the even and odd Pauli sectors are Hilbert–Schmidt orthogonal, so

\[
\begin{aligned}
\operatorname{Tr}H_3(\rho)^2
&=\operatorname{Tr}H_3(\sigma)^2+\frac14(9S_1+S_3)\\
&\le10+\frac14\bigl(8S_1+(S_1+S_3)\bigr)\\
&\le10+10d^2.
\end{aligned}
\]

The candidate’s mixed moment estimate is therefore supported for every actual four-qubit density.

## 5. Rank, moment thresholds, and \(H_3\) majorization

For every density,

\[
H_3\ge0,\qquad \operatorname{Tr}H_3=8,\qquad H_3\le4I.
\]

The physical Pauli identity is

\[
H_3=2\rho+\frac12\sum_{i=1}^4\sum_{P=X,Y,Z}P_i\rho P_i.
\]

For a pure density this is a sum of thirteen positive rank-one operators, so

\[
\operatorname{rank}H_3\le13.
\]

No linear independence of those thirteen vectors is needed.

For a positive matrix of trace \(8\) and rank at most \(r\), pad its spectrum to length \(r\). With \(s=K_k(A)\),

\[
\operatorname{Tr}A^2
\ge \frac{s^2}{k}+\frac{(8-s)^2}{r-k}.
\]

The right-hand side has derivative

\[
\frac{2(rs-8k)}{k(r-k)}.
\]

It is strictly increasing beyond each relevant target \(s=5,6,7\) for \(k=2,3,4\). Substitution gives exactly:

| Prefix | Target | \(r=16\) boundary moment | \(r=13\) boundary moment |
|---|---:|---:|---:|
| 2 | 5 | \(92/7\) | \(293/22\) |
| 3 | 6 | \(160/13\) | \(62/5\) |
| 4 | 7 | \(37/3\) | \(445/36\) |

The minima are \(160/13\) and \(445/36\), respectively. Since exceeding a target would force a strictly greater moment than its boundary value, equality at the sufficient moment threshold is allowed.

The first prefix follows from \(H_3\le4I\). Every prefix from five onward follows from positivity and trace \(8\). Thus these calculations establish all prefixes of

\[
L_3=(4,1^{\times4},0^{\times11}).
\]

For mixed inputs,

\[
d^2\le\frac3{13}
\quad\Longrightarrow\quad
\operatorname{Tr}H_3^2
\le10+\frac{30}{13}=\frac{160}{13}.
\]

For pure inputs,

\[
d^2\le\frac{17}{72}
\quad\Longrightarrow\quad
\operatorname{Tr}H_3^2
\le10+\frac{170}{72}=\frac{445}{36}.
\]

Both regions therefore give the required actual \(H_3\prec L_3\).

For two pure densities, the half trace distance is the square root of one minus their overlap squared. Applying this to \(\rho\) and \(\widetilde\rho\) yields

\[
d^2=1-\eta.
\]

Hence the pure region is exactly \(\eta\ge55/72\).

## 6. Actual \(H_2\) bound, including the sharp fourth-prefix import

The invariant interface gives

\[
K_k(H_2(\sigma))
=k+K_k(H_3(\sigma)).
\]

Its relevant bounds are therefore \(3,6,9,10\) for \(k=1,2,3,4\), and \(k+8\) for \(5\le k\le10\).

The remaining operator is precisely

\[
B=H_2(\rho)-H_2(\sigma)=\frac34R_1.
\]

After physical local rotations,

\[
B=\frac34\sum_i r_iZ_i,\qquad 0\le r_i\le d.
\]

For \(d>0\), independent sign probabilities with means \(r_i/d\) express \(B\) as a convex mixture of local bit-flipped conjugates of

\[
dB_0,\qquad B_0=\frac34\sum_i Z_i.
\]

This is a convexity argument for the signed Hermitian operator \(B\), not an assertion that \(B\) is positive.

The literal spectrum of \(B_0\) is

\[
(3,(3/2)^{\times4},0^{\times6},(-3/2)^{\times4},-3).
\]

Its needed prefix sums are \(3,9/2,6,15/2\), followed by \(9\) for \(5\le k\le10\).

For one arbitrary complex rank-\(k\) orthogonal projector \(Q\),

\[
\operatorname{Tr}(QH_2(\rho))
\le K_k(H_2(\sigma))+dK_k(B_0).
\]

Taking the supremum over that same physical projector class gives:

| \(k\) | Actual \(K_k(H_2(\rho))\) upper bound | Product-reference prefix |
|---|---:|---:|
| 1 | \(3+3d\) | 6 |
| 2 | \(6+\frac92d\) | 9 |
| 3 | \(9+6d\) | 12 |
| 4 | \(10+\frac{15}{2}d\) | 15 |
| \(5\le k\le10\) | \(k+8+9d\) | \(k+13\) |
| \(11\le k\le16\) | 24 | 24 |

The last row uses positivity and the actual trace \(\operatorname{Tr}H_2=24\), not a signed-tail estimate.

Every row holds when \(d\le1/2\), proving

\[
H_2(\rho)\prec
L_2=(6,3^{\times4},1^{\times6},0^{\times5}).
\]

Both theorem regions satisfy this defect restriction because

\[
\frac3{13}<\frac14,\qquad
\frac{17}{72}<\frac14.
\]

The imported sharp \(K_4(H_3(\sigma))\le6\) is used exactly where claimed. Replacing it by \(8\) would change the fourth-row invariant term from \(10\) to \(12\), which would not establish that row at \(d=1/2\). There is no unsupported extension of the invariant theorem to \(\rho\).

## 7. Common-projector consumption and all physical channel parameters

The universal one-body identity is

\[
H_1=2I+\frac12\sum_i r_iZ_i,\qquad 0\le r_i\le1
\]

after local rotations. The same sign-mixture argument gives

\[
H_1\prec L_1
=(4,3^{\times4},2^{\times6},1^{\times4},0).
\]

Also, \(\operatorname{Tr}(Q\rho)\le1\) for every nonzero-rank orthogonal projector.

For nonnegative retention,

\[
T_t^{\otimes4}(\rho)
=t^4\rho+t^3bH_3+t^2b^2H_2+tb^3H_1+b^4I.
\]

The subset sums already contain their multiplicities; no extra binomial factors belong outside them.

Fixing one arbitrary complex rank-\(k\) physical projector gives

\[
\operatorname{Tr}\!\left(QT_t^{\otimes4}(\rho)\right)
\le
t^4+t^3bK_k(L_3)+t^2b^2K_k(L_2)
+tb^3K_k(L_1)+kb^4.
\]

All weights are nonnegative. This inequality does not require the actual layers’ maximizing projectors to coincide.

For the literal product input, the \(j\)-body layer on a string of Hamming weight \(w\) has entry \(\binom{4-w}{j}\). All reference layers are therefore co-ordered. Their weighted entry is exactly

\[
\sum_{j=0}^4t^jb^{4-j}\binom{4-w}{j}
=b^w(t+b)^{4-w}
=b^wa^{4-w}.
\]

Consequently, the displayed upper bound is precisely \(K_k(D_t)\), not a relaxed larger reference. It applies to every \(k=1,\ldots,16\), with equality of total traces at \(k=16\).

The explicit rank-three and rank-four consumers also check:

\[
K_3(D_t)-\text{displayed upper bound}
=(3-6d)t^2b^2,
\]

\[
K_4(D_t)-\text{displayed upper bound}
=\left(5-\frac{15}{2}d\right)t^2b^2.
\]

They are strictly positive in both theorem regions when \(0<t<1\).

### Negative retention

The single-qubit identity

\[
YX^TY=\operatorname{Tr}(X)I-X
\]

implies

\[
\Phi_{1+t}^{\otimes4}(\rho)
=W\left(T_t^{\otimes4}(\rho)\right)^TW.
\]

This is full transpose. Since \(W^T=W\) for four factors, the consuming projector transforms as

\[
Q'=WQ^TW,
\]

and

\[
\operatorname{Tr}\!\left(
QW(T_t^{\otimes4}(\rho))^TW
\right)
=
\operatorname{Tr}\!\left(Q'T_t^{\otimes4}(\rho)\right).
\]

The transformed \(Q'\) remains a complex orthogonal projector of the same rank. Thus the already established common-projector inequalities apply on the full physical negative-retention interval \(p\in[1,4/3]\).

At \(t=0\), the output and reference are maximally mixed. At \(t=1\), the pure reference majorizes every density. The entire physical interval is covered.

For finite convex mixtures of the pure-region states, fixing \(Q\) first and using channel linearity proves the same bound with the unchanged reference. The pure rank bound is not incorrectly applied to the mixed density.

## 8. The \(x+iy\) formulation

After choosing the global phase to make the spin-flip overlap real and nonnegative, the decomposition into \(\Theta_4\)-fixed real and imaginary parts satisfies

\[
\psi=x+iy,\qquad
\langle x,y\rangle=0,\qquad
\|x\|^2+\|y\|^2=1,
\]

and

\[
\|x\|^2-\|y\|^2=\sqrt\eta.
\]

It follows that

\[
d^2=1-\eta=4\|x\|^2\|y\|^2.
\]

Thus the claimed pure stratum is correctly expressed by

\[
4\|x\|^2\|y\|^2\le17/72.
\]

No separate physical normal form for \(x\) and \(y\), or compatibility of independent signed SVDs, is assumed.

## 9. Universal GME family and named-hull separation

This claim is supported for **every** \(y\) and \(\theta\) satisfying the candidate’s quantified conditions.

The literal Dicke vector

\[
D=\frac1{\sqrt6}\sum_{|z|=2}|z\rangle
\]

is \(\Theta_4\)-fixed. The \(\Theta_4\)-fixed real space has dimension sixteen, so its real orthogonal complement to \(D\) has dimension fifteen; the specified unit \(y\) class is nonempty without choosing an instance.

For

\[
\psi_{\theta,y}=\cos\theta\,D+i\sin\theta\,y,
\]

orthogonality and normalization give

\[
\eta=\cos^2(2\theta)\in[55/72,1).
\]

Every such state is therefore within Theorem B and is non-spin-flip-invariant.

### Genuine entanglement

Across a singleton cut, the Dicke Schmidt coefficients are

\[
1/\sqrt2,\quad1/\sqrt2.
\]

Across a balanced cut, they are

\[
2/\sqrt6,\quad1/\sqrt6,\quad1/\sqrt6.
\]

Its second Schmidt singular value is consequently at least \(1/\sqrt6\) on every cut.

On the stated interval \(0<\theta<\pi/4\), the bound

\[
\sin^2(2\theta)\le17/72<1/4
\]

implies \(\theta<\pi/12\). Moreover,

\[
\|\psi_{\theta,y}-D\|
=2\sin(\theta/2)
\le\theta
<\frac{\pi}{12}
<\frac13
<\frac1{\sqrt6}.
\]

For every cut, matricization preserves the vector norm as Frobenius norm, and the perturbation’s operator norm is no larger. The singular-value perturbation inequality therefore keeps the second Schmidt singular value strictly positive on all seven bipartitions.

This proves genuine four-party entanglement uniformly in the entire stated \(y,\theta\) family.

### Separation from the four named classes

The absolute spin-flip overlap is invariant under physical local unitaries. In particular:

- every pure invariant state has \(\eta=1\);
- every physical Dicke-orbit state has \(\eta=1\);
- the literal coherent vacuum/W4 state has \(\eta=0\), because its weight-zero/one support is orthogonal to its spin-flipped weight-three/four support, and its physical local-unitary orbit retains that value;
- the new family has \(55/72\le\eta<1\);
- its GME property excludes pure biseparable states.

The convex-hull step is also valid, including mixed invariant or biseparable components. If a positive convex combination equals a rank-one density, positivity forces every nonzero component to be supported on that same ray and hence to equal that pure density. The new pure density belongs to none of the four classes, so such a convex representation is impossible.

The strict extension is therefore established **relative to those named classes**, without asserting literature-wide novelty or genuine entanglement of every mixed state in the defect region.

## 10. Final scope and assurance

The review supports:

\[
\boxed{d(\rho)^2\le3/13
\ \Longrightarrow\
\Phi_p^{\otimes4}(\rho)\prec D_{|1-p|}
\quad\text{for all physical }p}
\]

for arbitrary actual densities, and

\[
\boxed{\eta\ge55/72
\ \Longrightarrow\
\Phi_p^{\otimes4}(|\psi\rangle\langle\psi|)
\prec D_{|1-p|}
\quad\text{for all physical }p}
\]

for pure inputs, together with the stated finite-mixture consequence and universal GME family.

The unrestricted four-qubit theorem remains unproved by this argument. Failure of a sufficient moment or defect condition is not a physical counterexample.

**Scientific programs prepared or executed in this review: none. Numerical results produced: none. Independent finite corroboration by this reviewer: not performed.** The support supplied here is exact written mathematics at the frozen adopted interface, not numerical spectral assurance, independent-model-family review, human verification, formal-kernel verification, or a novelty audit. All held episodes and their consumers remain NONINPUT.