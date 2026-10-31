# F613 — Complete WRITTEN reconstruction

**Overall correctness: correct.**  
**Findings: 0 FATAL / 0 MAJOR / 0 MINOR at the reconstructed scope.**  
**Confidence: 0.97.**

The mixed-state defect theorem, larger pure-state theorem, fixed-projector finite-mixture extension, and universal genuinely entangled family outside the four named classes are supported by the written reconstruction below. These conclusions remain dependent on the exact frozen invariant-sector theorem; they do not establish unrestricted four-qubit majorization.

## 1. Read coverage, provenance, and methods

Before opening the mathematical packet, I completed the manifest, freeze receipt, parent-supplied live-metadata record, and all thirteen status-only controls, including their endings. I then sent the administrative pre-body ACK directly through `agent://Main`; the tool reported delivery.

After that delivery, I read the complete literal packet in consecutive raw windows of at most twenty lines, covering packet lines **1–877**, including the final `S4|42` ending. Source coverage was:

- **S1:** lines 1–765, the complete f598 candidate.
- **S2:** lines 1–31, the adopted mixed invariant-sector disposition.
- **S3:** lines 1–37, the coherent-vacuum–W4 disposition.
- **S4:** lines 1–42, the earlier invariant-sector/Dicke disposition.

Derivation began only after that complete read.

The supplied manifest pin, `5691b319788c3142611640460ebbe5f7a5d27e0a6d9b7e6de2c02d645d9df21b`, and receipt pin, `d4e0378a58ec23d1cf64db8aadd4b33e2baf4225b611b58329c4e87fdc52c2c0`, agree with the **parent-supplied metadata**. The packet pin is parent-reported as `c119a83b6c84c2e8030dd7e041ddfe7d2a812fbd70d90ede09fb7aab9f2e014e`. I did not independently execute hashing or a native clock command. The supplied `2026-10-30T14:21:00-0700 PDT` observation belongs to the parent, not to my native start.

This review used written general-variable reasoning only. I did not introduce a selected \(y\), parameter value, state, Pauli instance, or diagnostic probe; execute scientific code; follow scientific links; inspect author code or sibling reviews; or use any held episode or its consumers. The status controls were used only as exclusions. No repository file was written; this is the complete body for parent materialization.

## 2. Exact imports and acceptance boundary

The load-bearing pre-existing theorem is **S2 lines 3 and 17–23**: for every *actual mixed spin-flip-invariant four-qubit density* \(\sigma\),

\[
K_4(H_3(\sigma))\le 6.
\]

Its quantifier is the entire physical invariant mixed sector, not merely the Dicke orbit or selected pure normal forms. I use that adopted result at its stated scope; I do not claim a new reconstruction of its underlying physical normal-form/frame proof from the abbreviated disposition.

The accompanying invariant identities and operator bound are stated in **S4 lines 9–13** and S2 line 23:

\[
H_1(\sigma)=2I,\qquad H_2(\sigma)=I+H_3(\sigma),\qquad
0\le H_3(\sigma)\le2I,\qquad \operatorname{Tr}H_3(\sigma)=8.
\]

The literal Dicke vector is supplied by **S4 line 24**. The coherent-vacuum–W4 class being compared is defined in **S3 lines 5–7**. The unrestricted pure moment identity stated in S3 line 29 is independently reconstructed below rather than inferred from that disposition’s finite samples.

No linked review or checker is an additional input. In particular, their reported exact and numerical checks are not executions or spectral certificates produced by this WRITTEN review.

## 3. Defect normalization and actual Pauli identities — SUPPORTED

**Candidate anchors: S1 lines 66–78, 173–219, 614–640.**

Spin flip is a positive, trace-preserving involution on these density matrices. Consequently,

\[
\sigma=\frac{\rho+\widetilde\rho}{2}
\]

is an actual invariant density, while

\[
\Delta=\rho-\sigma=\frac{\rho-\widetilde\rho}{2}
\]

is Hermitian and traceless. Thus \(d=\|\Delta\|_1\in[0,1]\).

For a pure input, write \(\widetilde\rho=|\Theta_4\psi\rangle\langle\Theta_4\psi|\). The nonzero eigenvalues of \(\rho-\widetilde\rho\), when distinct from zero, are

\[
\pm\sqrt{1-\eta}.
\]

Dividing that operator by two and summing its absolute eigenvalues gives

\[
\boxed{d=\sqrt{1-\eta},\qquad d^2=1-\eta.}
\]

There is no extra factor of two.

For the actual Pauli expansion,

\[
\rho=\frac1{16}(I+R_1+R_2+R_3+R_4),
\]

spin flip changes precisely the odd-weight signs. Therefore

\[
\sigma=\frac1{16}(I+R_2+R_4),\qquad
\Delta=\frac1{16}(R_1+R_3).
\]

A weight-\(w\) Pauli contribution appears in
\(\binom{4-w}{j-w}\) of the lifted \(j\)-body marginals, with coefficient \(2^{-j}\). This gives, on the same physical tensor positions,

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

These are compatible identities for one density, not independently chosen marginal data.

For the phase-normalized decomposition \(\psi=x+iy\) with both vectors fixed by \(\Theta_4\), their inner product is real. Making the spin-flip overlap real and nonnegative forces

\[
\langle x,y\rangle=0,\qquad
\|x\|^2+\|y\|^2=1,\qquad
\|x\|^2-\|y\|^2=\sqrt\eta.
\]

Hence \(d^2=4\|x\|^2\|y\|^2\). No simultaneous independent signed-SVD reduction of \(x\) and \(y\) is used.

## 4. Pure and mixed moment bounds — SUPPORTED

**Candidate anchors: S1 lines 225–274 and 280–318.**

For a pure density, Pauli orthogonality gives

\[
1=\frac{1+S_1+S_2+S_3+S_4}{16},
\]

\[
\eta=\frac{1-S_1+S_2-S_3+S_4}{16}.
\]

Subtracting yields

\[
S_1+S_3=8(1-\eta).
\]

Equality of each singleton purity with its complementary triple purity gives

\[
\frac{4+S_1}{2}
=
\frac{4+3S_1+2S_2+S_3}{8},
\]

and thus

\[
2S_2+S_3=12+S_1.
\]

Solving these two relations,

\[
S_3=8-8\eta-S_1,\qquad S_2=2+4\eta+S_1.
\]

The physical \(H_3\) expansion consequently gives

\[
\operatorname{Tr}H_3^2
=
4+\frac14(9S_1+4S_2+S_3)
=
\boxed{8+3S_1+2\eta}.
\]

This reconstructs the coefficient \(2\eta\) without relying on an \(\eta=0\) family.

Because \(\Theta_4^2=+I\), an invariant density is real symmetric in a basis fixed by that conjugation and has a decomposition into invariant pure densities. Each such pure density has \(S_1=0\), \(\eta=1\), and moment \(10\). Linearity of \(H_3\) and convexity of squared Hilbert–Schmidt norm therefore prove

\[
\operatorname{Tr}H_3(\sigma)^2\le10.
\]

For arbitrary mixed \(\rho\), its invariant midpoint has singleton marginals \(I/2\). Trace-norm contraction gives

\[
|\mathbf r_i|
=\|\rho_i-I/2\|_1\le d,
\qquad S_1\le4d^2.
\]

The positive and negative parts of traceless \(\Delta\) each have trace \(d/2\), so

\[
\operatorname{Tr}\Delta^2\le\frac{d^2}{2},
\qquad
S_1+S_3=16\operatorname{Tr}\Delta^2\le8d^2.
\]

Even and odd Pauli sectors are Hilbert–Schmidt orthogonal. Accordingly,

\[
\begin{aligned}
\operatorname{Tr}H_3(\rho)^2
&=\operatorname{Tr}H_3(\sigma)^2
  +\frac14(9S_1+S_3)\\
&\le10+\frac14\bigl(8S_1+(S_1+S_3)\bigr)\\
&\le\boxed{10(1+d^2)}.
\end{aligned}
\]

All normalization factors in this passage are consistent.

## 5. Physical rank and moment-to-prefix conversion — SUPPORTED

**Candidate anchors: S1 lines 327–391.**

Positivity of the actual marginals gives \(H_3\ge0\), trace \(8\), and \(H_3\le4I\).

The single-site Pauli twirl gives the physical identity

\[
H_3=2\rho+\frac12\sum_{i=1}^4\sum_{P=X,Y,Z}P_i\rho P_i.
\]

For a pure input this is a sum of thirteen positive rank-one terms, proving \(\operatorname{rank}H_3\le13\).

For a positive matrix of trace \(8\), use a fixed padded spectral length \(r=16\), or \(r=13\) in the pure case. With \(s=K_k(A)\), Cauchy–Schwarz gives

\[
\operatorname{Tr}A^2\ge
f_{r,k}(s):=\frac{s^2}{k}+\frac{(8-s)^2}{r-k}.
\]

**Rank-deficient cases are included.** Here \(r\) is the chosen padded upper bound, not the actual rank. If the actual rank is below \(k\), zeros remain among the leading \(k\) entries and the trailing sum is zero; the same inequality still applies. There is no division by “actual rank minus \(k\).”

Moreover,

\[
f'_{r,k}(s)=\frac{2(rs-8k)}{k(r-k)},
\]

which is positive beyond each relevant target \(s=k+3\). The boundary moments reconstruct as follows:

| \(k\) | Target \(s\) | \(r=16\) | \(r=13\) |
|---|---:|---:|---:|
| 2 | 5 | \(92/7\) | \(293/22\) |
| 3 | 6 | \(160/13\) | \(62/5\) |
| 4 | 7 | \(37/3\) | \(445/36\) |

The respective column minima are \(160/13\) and \(445/36\). A prefix strictly exceeding its target would therefore force a moment strictly above the applicable threshold. Equality at a threshold remains permitted.

The first prefix follows from \(H_3\le4I\); prefixes \(k\ge5\) follow from positivity and trace \(8\). Thus the certificates establish

\[
H_3\prec(4,1^{\times4},0^{\times11}).
\]

Finally,

\[
10(1+3/13)=160/13,
\qquad
10(1+17/72)=445/36.
\]

This proves the required \(H_3\) majorization for both proposed regions. It does not, by itself, prove the channel theorem.

## 6. Compatible \(H_2\) and universal \(H_1\) bounds — SUPPORTED

**Candidate anchors: S1 lines 399–502.**

The imported invariant interface gives

\[
K_k(H_2(\sigma))\le
3,\ 6,\ 9,\ 10
\]

for \(k=1,2,3,4\), respectively, and \(K_k(H_2(\sigma))\le k+8\) for \(5\le k\le10\).

The remaining actual operator is

\[
B=\frac34R_1.
\]

Local rotations diagonalize its four Bloch contributions, with lengths \(0\le r_i\le d\). For \(d>0\), choosing independent local signs with means \(r_i/d\) expresses \(B\) as a convex combination of local bit-flipped conjugates of

\[
dB_0,\qquad B_0=\frac34\sum_iZ_i.
\]

The \(d=0\) case is immediate and requires no division.

The spectrum of \(B_0\) is

\[
(3,(3/2)^{\times4},0^{\times6},(-3/2)^{\times4},-3),
\]

so its relevant prefixes are \(3,9/2,6,15/2\), followed by \(9\) for \(5\le k\le10\). For each fixed complex rank-\(k\) projector \(Q\),

\[
\operatorname{Tr}(QH_2(\rho))
\le K_k(H_2(\sigma))+dK_k(B_0).
\]

The resulting bounds are

\[
3+3d,\quad6+\tfrac92d,\quad9+6d,\quad
10+\tfrac{15}{2}d,
\]

and \(k+8+9d\) for \(5\le k\le10\). Each is at most the corresponding prefix of

\[
L_2=(6,3^{\times4},1^{\times6},0^{\times5})
\]

when \(d\le1/2\). For \(k\ge11\), positivity and trace \(24\) give the remaining prefixes.

Both theorem regions satisfy \(d<1/2\). The sharp imported fourth-prefix bound is used correctly: replacing it by \(K_4(H_3(\sigma))\le8\) would not establish the displayed \(H_2\) fourth-prefix conclusion at \(d=1/2\).

The same sign-mixture argument with singleton Bloch lengths at most one proves universally

\[
H_1\prec L_1=(4,3^{\times4},2^{\times6},1^{\times4},0).
\]

No alignment of the actual layer maximizers is assumed.

## 7. Full physical channel and common-projector consumers — SUPPORTED

**Candidate anchors: S1 lines 508–608 and 131.**

The physical subset expansion is

\[
T_t^{\otimes4}(\rho)
=t^4\rho+t^3bH_3+t^2b^2H_2+tb^3H_1+b^4I.
\]

There are no missing or additional binomial factors.

Fixing one arbitrary physical complex rank-\(k\) orthogonal projector throughout gives

\[
\operatorname{Tr}(QT_t^{\otimes4}(\rho))
\le
t^4+t^3bK_k(L_3)+t^2b^2K_k(L_2)
+tb^3K_k(L_1)+kb^4.
\]

For the product input, all reference layers are co-ordered by Hamming weight. Their entry at weight \(w\) sums to

\[
\sum_{j=0}^{4-w}\binom{4-w}{j}t^jb^{4-j}
=b^w(t+b)^{4-w}=b^wa^{4-w}.
\]

Hence the displayed bound is **exactly** \(K_k(D_t)\), not a relaxed larger reference.

The explicit consumers also reconstruct:

\[
\operatorname{Tr}(QT_t^{\otimes4}(\rho))
\le K_3(D_t)-(3-6d)t^2b^2
\]

for rank three, and

\[
\operatorname{Tr}(QT_t^{\otimes4}(\rho))
\le K_4(D_t)-\left(5-\frac{15}{2}d\right)t^2b^2
\]

for rank four. Their stated strict gaps hold when \(0<t<1\) in either region. The \(t=0\) and \(t=1\) endpoint arguments are valid.

For negative retention,

\[
YX^TY=\operatorname{Tr}(X)I-X
\]

implies

\[
\Phi_{1+t}^{\otimes4}(\rho)
=W\bigl(T_t^{\otimes4}(\rho)\bigr)^TW.
\]

This is the full transpose. Since \(W^T=W\), the consuming projector transports to

\[
Q'=WQ^TW,
\]

which preserves rank, positivity, and orthogonality, and satisfies the required expectation identity for arbitrary complex \(Q\). This explicitly handles the consuming-side boundary; no real-projector or partial-transpose substitution occurs.

Therefore **all sixteen prefixes hold for every physical \(p\in[0,4/3]\)**.

For finite mixtures of Theorem B states, output linearity is applied to one fixed \(Q\) before taking its supremum. This does not require the mixture to retain the pure-state rank bound or satisfy a nonlinear pure-state overlap condition.

## 8. Universal GME family and named-hull separation — SUPPORTED

**Candidate anchors: S1 lines 648–717.**

For every allowed fixed-real unit \(y\perp D\),

\[
\psi_{\theta,y}=\cos\theta D+i\sin\theta y
\]

is normalized. Antiunitarity gives

\[
\Theta_4\psi_{\theta,y}
=\cos\theta D-i\sin\theta y,
\]

and consequently

\[
\eta=\cos^2(2\theta),\qquad d^2=\sin^2(2\theta).
\]

The stated parameter restriction puts every such state in Theorem B and makes its density non-invariant. Existence of admissible \(y\) follows from the real fixed space of the conjugation; no particular \(y\) needs to be chosen.

For the supplied Dicke vector, the singleton Schmidt coefficients are \(1/\sqrt2,1/\sqrt2\). Across each balanced cut they are \(2/\sqrt6,1/\sqrt6,1/\sqrt6\). Thus the second coefficient is at least \(1/\sqrt6\) on all seven cuts.

Because \(2\theta\in(0,\pi/2)\),

\[
\sin^2(2\theta)\le17/72<1/4
\quad\Longrightarrow\quad \theta<\pi/12.
\]

Uniformly in every allowed \(y\),

\[
\|\psi_{\theta,y}-D\|
=2\sin(\theta/2)
\le\theta<\pi/12<1/3<1/\sqrt6.
\]

Across any cut, coefficient-matrix operator-norm perturbation is bounded by this vector norm. Singular-value perturbation therefore preserves a strictly positive second Schmidt coefficient on every cut. Every state in the entire quantified family is genuinely four-party entangled.

For separation, the magnitude of spin-flip overlap is invariant under physical local unitaries: the one-qubit alternating-form identity contributes only a determinant phase. Accordingly:

- Pure invariant states and the Dicke local-unitary orbit have \(\eta=1\).
- Coherent-vacuum–W4 states have \(\eta=0\), since their weight-zero/one support is orthogonal to its flipped weight-three/four support; local unitaries preserve this value.
- The proposed family has \(55/72\le\eta<1\).
- Its genuine entanglement excludes pure biseparable states.

Finally, if a positive convex combination equals a rank-one density, every positively weighted density in that combination must be supported on that same ray. Thus mixed invariant or mixed biseparable components cannot evade the pure-state exclusions. This proves exclusion from the convex hull of all four named classes.

The conclusion is a universal strict addition relative to that named hull—not a claim that every mixed defect-bounded state is genuinely entangled, and not a literature-wide novelty result.

## 9. Final claim dispositions and limits

| Claim | Disposition |
|---|---|
| Every mixed actual four-qubit density with \(d^2\le3/13\) satisfies all sixteen output-majorization prefixes at every physical \(p\) | **SUPPORTED**, using the exact imported invariant-sector theorem |
| Every pure input with \(\eta\ge55/72\) satisfies the same conclusion | **SUPPORTED** |
| Finite convex mixtures of those pure inputs | **SUPPORTED** by fixed-projector linearity |
| Universal allowed \((\theta,y)\) family is non-invariant and GME on all seven cuts | **SUPPORTED** |
| That family lies outside the four named classes’ convex hull | **SUPPORTED** |
| Thresholds are necessary or optimal | **NOT ESTABLISHED; not claimed** |
| Unrestricted four-qubit majorization | **NOT PROVED; correctly left open** |
| Underlying invariant normal-form/frame proof beyond the imported disposition | **NOT independently reconstructed here** |
| Standalone biseparable channel theorem | **NOT reconstructed here and not needed for the new proofs or hull exclusion** |
| Fresh finite corroboration, numerical spectral assurance, independent-model-family, human, formal-kernel, or novelty verification | **NOT PERFORMED by this review** |

**Verdict explanation:** No mathematical defect was found in the complete candidate at its frozen scope. The actual-state coupling, pure trace-norm normalization, rank-deficient moment argument, compatible \(H_2\) bound, common complex-projector channel consumption, full-transpose transport, and universal hull-separation argument all reconstruct without enlarging the claims.