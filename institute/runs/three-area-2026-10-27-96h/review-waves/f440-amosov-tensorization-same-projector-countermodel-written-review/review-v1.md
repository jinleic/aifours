# F440 WRITTEN review — depolarizing ancillary repair and same-projector countermodel

**Disposition recommendation:** The author candidate is **SUPPORTED at its explicitly limited mathematical scope**. It supplies a valid direct proof of depolarizing ancillary majorization and a valid exact countermodel to the isolated weight/twirl/Ky Fan implication. The countermodel is **not admissible under Proposition 5’s pure-output hypothesis**. Neither full Proposition 5 nor unrestricted tensor-product depolarizing majorization is proved or refuted.

**Findings against the reviewed author candidate:** **0 FATAL / 0 MAJOR / 0 MINOR.**

This is a complete written reconstruction, **not automatic acceptance**. Parent disposition remains mandatory.

## 1. Identity, read coverage, and method

The following identities are **parent-supplied metadata**, not independently measured child hashes:

- Manifest: `f32a3ad6921544a8af06ab48f7eb4d52a9f37e5d3ee1a595ad4cb16afc6d590a`.
- Freeze receipt: `d900b541e4db875a9e81c39262d4b470372ffa5916f5efa11423a51136899935`.
- Literal packet: `a504beafc4ef9b188bd7eb2a6d33b596e4a65861c58ab2234fd43752d359643a`.
- S1, author candidate: `84fb421b024feb5a296de66212323357703672c96487a66b0ad67c963fba45ad`.
- S2, primary reader excerpt: `e5ea40f15d472862bc9219e76fcbfc472382a0de758643c0828fec3033168b00`.
- S3, bounded public-source audit: `2936dbecf01ab76d81afd4bd6a931d559b2ecbbe9a26fdd2013c7737c903c87e`.

Before the mathematical packet, I read the complete manifest, freeze receipt, dispatch receipt, parent metadata supply, and all seven named status-only controls. I then issued the administrative pre-body ACK.

After that ACK, I read the literal packet **in order, raw, LF 1–1140, in windows of exactly 20 lines**, including all endings:

- S1 displayed source lines **1–595**;
- S2 displayed source lines **1–137**;
- S3 displayed source lines **1–406**.

The parent’s LF counts of 594 for S1 and 405 for S3 are newline counts; they do not omit their final displayed source lines.

The mathematical reconstruction below began after completion of those reads. It is **nonblind**: the manifest and author text disclosed the intended construction and conclusions.

No external source was followed. No sibling return, author code, held scientific payload, or held consumer was opened. PH/v8/cp116, AME/t28, CORE, privacy, and other genuinely quarantined material remained NONINPUT. The quarantine records were used only for status and exclusion.

**Scientific execution, code, argv, and finite-test results:** **NOT RUN; none claimed.** No new selected instance or probe was introduced. No filesystem artifact was written under this read-only role; this text is the complete materializable review body.

## 2. Exact import boundaries

I use the inputs as follows:

1. **S1** supplies the candidate theorem, its exact frozen construction, and its expressly limited conclusions.
2. **S2** supplies the actual reader-rendered text of Propositions 4–5, Eqs. (23)–(25), the final “combined” inference, and the stated iteration. It is not original HTML or subscription-journal text.
3. **S3** supplies only the bounded literature-status account and its qualifications. I do not import its mathematical results as premises or claim an independent live recheck of its external citations.

The ordering condition called Eq. (16) is transcribed in S1 LF 43–49 and S3 LF 189–194. Its earlier primary-text location is outside S2’s supplied excerpt. The concrete cross-coset inequality in the candidate can nevertheless be checked directly from the frozen weights.

No equivalence between the accessible manuscript and the subscription journal article is established here.

## 3. Ancillary orbit obstruction: the proof step is false, not thereby the inequality

**Relevant locations:** S1 LF 63–129; S2 LF 50–51.

For the frozen Bell vector
\[
f=\frac{|00\rangle+|11\rangle}{\sqrt2},
\]
the actions of \(I,Z,X,XZ\) on the second factor give the four displayed Bell vectors. Each has norm one. The two supported on \(\{|00\rangle,|11\rangle\}\) are orthogonal to each other, the two supported on \(\{|01\rangle,|10\rangle\}\) are orthogonal to each other, and the two support sectors are orthogonal.

Consequently,
\[
\dim\operatorname{span}\{(I\otimes U)f:U=I,Z,X,XZ\}=4,
\]
not \(2\). The action on that space is the direct sum of two copies of the two-dimensional Pauli representation, not an irreducible two-dimensional restriction.

The general statement in S1 also follows. If the \(U_g\) span \(M_d\), and
\[
f=\sum_{i=1}^r s_i e_i\otimes h_i,\qquad s_i>0,
\]
then linear combinations of the orbit give all \((I\otimes A)f\) with \(A\in M_d\). Since the \(h_i\) are linearly independent, the vectors \(Ah_i\) can be prescribed independently. Thus
\[
L=\operatorname{span}\{e_1,\ldots,e_r\}\otimes\mathbb C^d,
\qquad \dim L=rd.
\]
Under that spanning hypothesis, the asserted dimension \(d\) and irreducibility hold at Schmidt rank one, not at arbitrary Schmidt rank.

This directly refutes the assertion in S2 LF 51.

It does **not** refute ancillary majorization. For the frozen depolarizing parameter \(p=1/2\), the Bell orbit is orthonormal, so the ancillary-output spectrum is
\[
(5/8,1/8,1/8,1/8).
\]
Its prefixes are \(5/8,3/4,7/8,1\), bounded by the prefixes \(3/4,1,1,1\) of
\[
(3/4,1/4,0,0).
\]
The selected source example therefore disproves the dimension step while satisfying the spectral inequality.

**Claimwise result:** The orbit assertion is **REFUTED**. The inference that its failure alone refutes Proposition 4’s inequality is **REFUTED**.

## 4. Complete reconstruction of the depolarizing ancillary proof

**Relevant locations:** S1 LF 131–281.

Let
\[
\mathcal D_{p,d}(X)=(1-p)X+\frac pd\operatorname{Tr}(X)I_d,
\quad d\ge2,\quad
0\le p\le\frac{d^2}{d^2-1}.
\]
Put
\[
t=1-p,\qquad b=\frac pd,\qquad \alpha=t+b.
\]
For any density operator \(\rho_{AB}\),
\[
R=(\operatorname{id}_A\otimes\mathcal D_{p,d})(\rho_{AB})
=t\rho_{AB}+b\rho_A\otimes I_d.
\]

### 4.1 Positivity, trace, and reference probabilities

The normalized Choi operator is
\[
t|\Omega_d\rangle\langle\Omega_d|+\frac{p}{d^2}I,
\]
with eigenvalues
\[
1-p+\frac{p}{d^2},
\qquad
\frac{p}{d^2}\quad(d^2-1\text{ times}).
\]
The stated interval makes them nonnegative. Thus the map is completely positive, and \(R\ge0\). Moreover,
\[
\operatorname{Tr}R=t+db=1.
\]

The proposed reference has entries \(\alpha,b,\ldots,b\), summing to one. Its entries are nonnegative: \(b\ge0\), and \(\alpha\) decreases with \(p\) to
\[
1-\frac{d^2}{d^2-1}\frac{d-1}{d}
=\frac1{d+1}>0.
\]

For a density operator,
\[
0\le\rho_A\le I_A,
\qquad
0\le\rho_A\otimes I_d\le I_{AB}.
\]

### 4.2 Nonnegative \(t\)

For any orthogonal rank-\(k\) projector \(P\),
\[
\operatorname{Tr}(P\rho_{AB})\le1,
\qquad
\operatorname{Tr}\bigl(P(\rho_A\otimes I_d)\bigr)\le k.
\]
When \(t\ge0\),
\[
\operatorname{Tr}(PR)\le t+bk.
\]
Here \(\alpha=t+b\ge b\), so for \(1\le k<d\) the sorted reference prefix is exactly
\[
\alpha+(k-1)b=t+kb.
\]

### 4.3 Negative \(t\)

When \(t<0\), the operator inequality \(t\rho_{AB}\le0\) gives
\[
R\le b\rho_A\otimes I_d\le bI_{AB}.
\]
Therefore
\[
\operatorname{Tr}(PR)\le bk.
\]
Now \(\alpha<b\), so the sorted reference is
\[
(\underbrace{b,\ldots,b}_{d-1},\alpha).
\]
For \(1\le k<d\), its prefix is exactly \(kb\). The change in reference order on this branch is essential and is handled correctly in S1.

### 4.4 Remaining ranks and majorization

For every \(k\ge d\) within the output dimension,
\[
\operatorname{Tr}(PR)\le\operatorname{Tr}R=1.
\]
The zero-padded reference prefix is also one. Rank zero is trivial, and equality holds at the full trace.

Maximization over all orthogonal rank-\(k\) projectors yields every Ky Fan prefix inequality. Hence
\[
\lambda(R)\prec q_{p,d}\oplus0.
\]

This argument applies **directly to mixed \(\rho_{AB}\)**; it does not silently rely on a pure-input reduction.

### 4.5 Endpoints, sharpness, and infinite ancillas

- At \(p=0\), the reference is \((1,0,\ldots,0)\).
- At \(p=1\), \(t=0\) and the reference is uniform on \(d\) entries.
- At \(p=d^2/(d^2-1)\), the sorted reference is
  \[
  \left(
  \underbrace{\frac d{d^2-1},\ldots,\frac d{d^2-1}}_{d-1},
  \frac1{d+1}
  \right).
  \]
  No division by \(t\), continuity argument, or omitted endpoint case is needed.
- A product pure input produces the reference spectrum, so all prefix constants are sharp.

For a trace-class density operator on an infinite-dimensional ancilla, the same operator inequalities and finite-rank projector bounds remain valid. The output is positive trace class of trace one, so its decreasing nonzero eigenvalues admit the usual zero-padded majorization interpretation.

**Claimwise result:** The depolarizing ancillary theorem, including the mixed-input and stated endpoint extensions, is **SUPPORTED**. This is not an adjudication of general group-channel Proposition 4.

## 5. Exact reconstruction of the common-orbit/common-projector countermodel

**Relevant locations:** S1 LF 283–446.

Write \(u=|00\rangle\) and
\[
v=\frac{\sqrt3|01\rangle+|10\rangle}{2}.
\]
These are orthonormal. Consequently,
\[
R=\frac23|u\rangle\langle u|+\frac13|v\rangle\langle v|,
\qquad
Q=|u\rangle\langle u|+|v\rangle\langle v|
\]
are respectively a density operator and an orthogonal rank-two projector.

In the stated basis,
\[
R=\frac1{12}
\begin{pmatrix}
8&0&0&0\\
0&3&\sqrt3&0\\
0&\sqrt3&1&0\\
0&0&0&0
\end{pmatrix}.
\]
Its spectrum is
\[
(2/3,1/3,0,0)\prec(3/4,1/4,0,0).
\]
The only nontrivial prefix check is \(2/3\le3/4\); all prefixes from rank two onward equal one.

Partial traces give
\[
\sigma=\operatorname{Tr}_H R
=\operatorname{diag}(3/4,1/4),
\]
and
\[
\operatorname{Tr}_K R
=\operatorname{diag}(11/12,1/12).
\]
Thus the marginal constraint is satisfied with equality, not merely by a loose bound.

### 5.1 Genuine Pauli weights and ordering

The specified channel is
\[
\Phi=\frac58\operatorname{Ad}_I+
\frac18\operatorname{Ad}_Z+
\frac18\operatorname{Ad}_X+
\frac18\operatorname{Ad}_{XZ}
=\mathcal D_{1/2,2}.
\]
For \(T=\{I,Z\}\), the coset weights are
\[
(5/8,1/8),\qquad(1/8,1/8),
\]
with ordered sums
\[
p=(3/4,1/4).
\]
Every weight in the second coset is at most every weight in the first coset. This is the required cross-coset ordering, including its equality cases.

### 5.2 Exact twirl and all row bounds

For any two-by-two block operator on the first factor, summing conjugation by \(I,Z\) removes its off-diagonal blocks, and summing conjugation by \(X,XZ\) does the same while interchanging the diagonal blocks. Therefore, for this actual \(R\),
\[
\sum_{U\in\{I,Z,X,XZ\}}
(U\otimes I)R(U^\dagger\otimes I)
=2I_H\otimes\sigma.
\]
This is the operator twirl corresponding to Eq. (23), not a separately assigned table constraint.

For every unit vector \(h\),
\[
\sum_U\langle h|R_U|h\rangle
=2\langle h|I_H\otimes\sigma|h\rangle
\le2\lambda_{\max}(\sigma)=\frac32<2.
\]
Thus Eq. (24) holds for every unit vector, with the stronger bound from the actual marginal.

### 5.3 All-projector Eq. (25)

Every \(R_U=(U\otimes I)R(U^\dagger\otimes I)\) has spectrum
\[
(2/3,1/3,0,0).
\]
For every rank-one projector its expectation is at most \(2/3\le3/4\). For every projector of rank at least two, its expectation is at most one, which equals the corresponding padded-\(q\) prefix.

Hence Eq. (25) holds **simultaneously for every projector, every permissible rank, and every one of the four conjugations**.

### 5.4 Entire same-projector table

The matrix elements for the frozen, common consuming vectors are:

| Consuming vector | \(I\) | \(Z\) | \(X\) | \(XZ\) |
|---|---:|---:|---:|---:|
| \(u=|00\rangle\) | \(2/3\) | \(2/3\) | \(1/12\) | \(1/12\) |
| \(v\) | \(1/3\) | \(1/12\) | \(1/6\) | \(1/6\) |
| Sum over \(Q\) | \(1\) | \(3/4\) | \(1/4\) | \(1/4\) |

The entries follow from the actual vectors:

- \(Zu=u\) and \(\langle v|Zv\rangle=(3-1)/4=1/2\), giving the \(Z\)-column entry \(1/12\) in the second row.
- \(Xu=|10\rangle\), while \(Xv=(\sqrt3|11\rangle+|00\rangle)/2\). Their squared overlaps with \(v\) and \(u\) are respectively \(1/4\), giving \(1/6\) and \(1/12\).
- \(XZ\) changes the relevant sign but leaves those squared overlaps unchanged.

This reconstructs all eight entries. They are not independently optimized weights or entries obtained from different consuming projectors.

### 5.5 Violation of the product-reference conclusion

For
\[
Y=(\Phi\otimes\operatorname{id})(R),
\]
the same \(Q\) gives
\[
\operatorname{Tr}(QY)
=\frac58+\frac18\left(\frac34+\frac14+\frac14\right)
=\frac{25}{32}.
\]
But
\[
(p\otimes q)^\downarrow
=\left(\frac9{16},\frac3{16},\frac3{16},\frac1{16}\right),
\qquad
K_2(p\otimes q)=\frac34=\frac{24}{32}.
\]
Thus
\[
K_2(Y)\ge\operatorname{Tr}(QY)
=\frac{25}{32}>\frac{24}{32}.
\]
No assertion that \(Q\) is a spectral projector of \(Y\) is necessary.

### 5.6 Output matrix and exact eigenvalues

Using the twirl,
\[
Y=\frac12R+\frac14I_H\otimes\sigma
=\frac1{48}
\begin{pmatrix}
25&0&0&0\\
0&9&2\sqrt3&0\\
0&2\sqrt3&11&0\\
0&0&0&3
\end{pmatrix}.
\]
The central unscaled block has trace \(20\) and determinant
\[
9\cdot11-(2\sqrt3)^2=87,
\]
so its eigenvalues are \(10\pm\sqrt{13}\). Since \(3<\sqrt{13}<4\), the complete decreasing spectrum is
\[
\frac{25}{48},\quad
\frac{10+\sqrt{13}}{48},\quad
\frac{10-\sqrt{13}}{48},\quad
\frac3{48}.
\]
In particular,
\[
K_2(Y)=\frac{35+\sqrt{13}}{48}
>\frac{36}{48}=\frac34.
\]

**Claimwise result:** The countermodel to the **standalone implication from ordering, twirl, row bounds, and all conjugated-state Ky Fan bounds** is **SUPPORTED**. It also satisfies the stated global and actual-marginal spectral constraints.

## 6. Necessary conditional-output admissibility excludes this \(R\)

**Relevant locations:** S1 LF 448–501.

Suppose, contrary to the exclusion claim, that
\[
R=(\operatorname{id}\otimes\Omega)(|f\rangle\langle f|)
\]
for a trace-preserving quantum channel satisfying the proposition’s pure-output bound by \(q=(3/4,1/4)\).

For any ancilla vector \(a\), set
\[
f_a=(\langle a|\otimes I)f,\qquad
C_a=(\langle a|\otimes I)R(|a\rangle\otimes I).
\]
Linearity and the fact that \(\Omega\) acts on the other factor give
\[
C_a=\Omega(|f_a\rangle\langle f_a|).
\]
Trace preservation then implies
\[
w_a:=\operatorname{Tr}C_a=\|f_a\|^2.
\]
If \(w_a>0\), normalize \(f_a\) and apply the pure-output hypothesis:
\[
\lambda(C_a)
=w_a\,\lambda\!\left(
\Omega\!\left(\frac{|f_a\rangle\langle f_a|}{w_a}\right)
\right)
\prec w_aq.
\]
If \(w_a=0\), then \(f_a=0\) and \(C_a=0\), so the corresponding zero constraint also holds.

For the frozen construction, contraction with the first-system vector \(|1\rangle\) gives
\[
C_1=\frac1{12}|0\rangle\langle0|,
\qquad w_1=\frac1{12}.
\]
The necessary comparison is therefore
\[
(1/12,0)\prec
\left(\frac1{16},\frac1{48}\right),
\]
which already fails at the first prefix:
\[
\frac1{12}>\frac1{16}.
\]

This excludes **every** realization by a channel with the stated pure-output bound, not merely a particular proposed realization. The weight \(w_1\) is fixed by \(R\), so changing the purifying input cannot evade this obstruction.

The argument uses only the actual intermediate-state form, trace preservation, and the pure-output hypothesis. It does not depend on accepting general Proposition 4.

**Claimwise result:** The construction’s inadmissibility is **SUPPORTED**. The claim that this construction refutes full Proposition 5 is **REFUTED**.

The conditional-output constraints are necessary. Their sufficiency is neither proved nor needed here.

## 7. The excluded Kraus realization is correct and remains excluded

**Relevant locations:** S1 LF 503–524.

For the displayed operators,
\[
A_0^\dagger A_0
=\operatorname{diag}(3/11,1),\qquad
A_1^\dagger A_1
=\operatorname{diag}(8/11,0),
\]
so their sum is \(I\). They define a CPTP channel.

For the specified \(f_{\rm bad}\),
\[
(I\otimes A_0)f_{\rm bad}
=\frac1{\sqrt3}v,
\qquad
(I\otimes A_1)f_{\rm bad}
=\sqrt{\frac23}|00\rangle.
\]
Summing their output projectors gives exactly \(R\).

However,
\[
\Omega_{\rm bad}(|1\rangle\langle1|)=|0\rangle\langle0|,
\]
which violates the maximum-eigenvalue bound \(3/4\). Also,
\[
\Omega_{\rm bad}(I)
=A_0A_0^\dagger+A_1A_1^\dagger
=\operatorname{diag}(19/11,3/11)\ne I.
\]
The channel is nonunital and therefore cannot be mixed unitary.

Thus the realization confirms only that \(R\) is physically producible by an **excluded** channel. It does not restore Proposition 5 admissibility.

**Claimwise result:** The stated excluded CPTP realization and both reasons for exclusion are **SUPPORTED**.

## 8. What the primary proof text does and does not establish

The supplied primary reader text contains two distinct issues correctly separated by S1:

1. **False ancillary proof step:** S2 LF 50–51 asserts dimension \(n\) and irreducibility for the orbit-generated space. The frozen Bell orbit refutes that assertion.
2. **Insufficient isolated tensorization inference:** S2 LF 111 says the final product-reference bound is obtained by combining Eqs. (24), (16), and (25). The frozen countermodel satisfies their corresponding operator constraints, including the exact twirl and a genuine common consuming projector, but violates that conclusion.

These are supported objections to the inspected proof route. They are **not defects in S1**, which identifies them and retains the correct limitations.

In particular, the second objection must not be rewritten as:

> All hypotheses of Proposition 5 hold, but its conclusion fails.

That statement would be false for this construction. The actual \(\Omega\)-admissibility hypothesis provides additional structure and excludes \(R\). Accordingly, the countermodel proves insufficiency of the listed consequences, not falsity of the theorem under all its original assumptions.

The source’s stated iteration is present in S2 LF 118–126. It does not repair either issue. Conversely, the failure of the inspected proof chain does not establish that no other proof, stronger implicit argument, or valid theorem is possible.

## 9. Remaining tensorization obligation

**Relevant locations:** S1 LF 526–568.

The displayed residual identity follows from the channel formula:
\[
(\mathcal D_{p,2}\otimes\operatorname{id})(R_m)
=(1-p)R_m+\frac p2I_2\otimes\sigma_m,
\qquad
\sigma_m=\operatorname{Tr}_{H_1}R_m.
\]
To obtain the claimed unrestricted induction, one still needs the all-input, all-rank, same-projector inequality
\[
\operatorname{Tr}\!\left[
Q\left((1-p)R_m+\frac p2I_2\otimes\sigma_m\right)
\right]
\le K_k(q_{p,2}^{\otimes(m+1)})
\]
on the **actual admissible family** \(R_m\).

For a single depolarizing second channel, expanding the pure input in first-system blocks gives
\[
(R_\Omega)_{ij}
=(1-r)|f_i\rangle\langle f_j|
+\frac r\ell\langle f_j|f_i\rangle I_\ell.
\]
This follows by applying the channel to each block \(|f_i\rangle\langle f_j|\), whose trace is \(\langle f_j|f_i\rangle\). These blocks are coupled by the same underlying \(f\); arbitrary globally bounded operators cannot replace them.

S1 does not claim to solve that remaining admissibility-sensitive inequality. Its one-leg theorem is not silently promoted into an unrestricted tensorization theorem.

## 10. Claimwise disposition and findings

| Claim | WRITTEN disposition |
|---|---|
| The ancillary orbit always has dimension \(d\) | **REFUTED** by the frozen Bell orbit. |
| The false dimension step alone refutes Proposition 4’s spectral conclusion | **REFUTED**; the displayed example satisfies that conclusion. |
| Depolarizing ancillary majorization for every \(d\), arbitrary finite ancilla, mixed inputs, and the full CP interval | **SUPPORTED** by the reconstructed direct proof. |
| The stated trace-class infinite-ancilla extension | **SUPPORTED** by the same finite-rank projector argument. |
| Ordering plus exact twirl, row bounds, and all conjugated-state Ky Fan bounds imply the product-reference conclusion | **REFUTED as a standalone implication** by the frozen exact construction. |
| The countermodel uses one genuine orbit and the same consuming projector | **SUPPORTED**; all table entries are reconstructed. |
| The countermodel satisfies global and actual-marginal majorization | **SUPPORTED**. |
| The countermodel is an admissible intermediate state for the stated \(q\)-bounded \(\Omega\) | **REFUTED** by the conditional-output constraint. |
| The excluded Kraus realization is CPTP and produces \(R\) | **SUPPORTED**, while failing the required output bound and mixed-unitary condition. |
| Full general Proposition 4 | **INCONCLUSIVE / not adjudicated** beyond the identified false proof step. |
| Full Proposition 5 | **INCONCLUSIVE**; neither proved nor refuted. |
| Unrestricted all-\(n\) or general four-qubit depolarizing majorization | **INCONCLUSIVE**; not closed by this return. |
| Earlier Class A/B mathematics | **UNCHANGED**; no new proof credit or re-review asserted. |
| Worldwide status, novelty, or priority | **INCONCLUSIVE**. |
| Subscription-journal equivalence | **INCONCLUSIVE / not checked**. |

**Candidate findings:** **0 FATAL / 0 MAJOR / 0 MINOR.** No corrective finding against S1 is identified at its stated scope.

S3’s account of the newer paper remains a **bounded documentary import**, not a fresh external verification by this reviewer. It supports retaining the candidate’s caution, but cannot establish worldwide open status, clear priority, or decide the older theorem’s truth.

## 11. Parent adoption boundary and assurance ceiling

The parent may consider adopting, after its own disposition:

1. The exact depolarizing ancillary theorem at the proved quantifiers.
2. The exact common-orbit/common-projector countermodel to the weakened implication.
3. The conditional-output obstruction excluding that countermodel from Proposition 5.
4. The limited conclusion that the inspected source proof chain is not established by its displayed steps as written.

The parent must **not** adopt from this review:

- a two-channel counterexample satisfying Proposition 5’s hypotheses;
- falsity of general Proposition 4 or Proposition 5;
- unrestricted four-qubit or all-\(n\) target closure;
- sufficiency of the conditional-output constraints;
- novelty, priority, exhaustive literature clearance, or journal-text equivalence.

This is **same-harness, nonblind written reconstruction**. It is not independent-model-family, human, formal/kernel, numerical-replay, or publication-priority assurance. No execution evidence exists, and no child-native completion clock or independently measured hash is asserted.

**Overall correctness:** **correct** for the reviewed author candidate’s expressly limited claims.

**Explanation:** The direct ancillary proof covers both signs of \(1-p\), all required ranks, mixed inputs, and endpoints. The exact countermodel invalidates only the isolated displayed tensorization implication; its necessary conditional-output violation correctly prevents any claimed refutation of the full theorem.

**Confidence:** **0.99** in the reconstructed identities and scoped logical conclusions. Parent disposition remains required.