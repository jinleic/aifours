# F429 — Written review of the parity-sector tensor extension and strict four-qubit enlargement

**Role:** WRITTEN  
**Result:** **0 FATAL / 0 MAJOR / 0 MINOR mathematical findings at the reconstructed scope.**  
**Assurance:** Same-harness written reconstruction only. This return is not parent adoption, independent-model-family review, human review, kernel verification, a finite-run result, or a novelty determination.

This is the complete review body for parent materialization. No repository review file was written.

## 1. Input binding, coverage, and methods

The assignment is bound to:

- Manifest SHA: `bd7566032a4740edc783e941fbf5c31680fd2474cf37605419a47f50f8f59d65`.
- Freeze-receipt SHA: `6ff32cd78403c75099e9ad0a0a8840b65fd73609603c4e9f3c57462d80cc9a66`.
- Literal-packet SHA: `b171be60d3e02ba76fc950a53739f9602ff5c86c8f37df5f6ad200625155e94d`.

These hashes, byte counts, LF counts, and the supplied clock `2026-10-30T11:02:48-0700 PDT` are **parent-observed metadata**, as recorded in `parent-live-metadata-supply-v1.json`; they are not child-native executions or start/completion observations.

Before opening the mathematical packet, I read the complete manifest, freeze receipt, all seven listed status-only controls in order, and the parent metadata supply. I then sent a direct administrative pre-body ACK to Main. After that ACK, I read the complete literal packet sequentially in raw windows of at most 20 LF, through its final line, including:

- **S1:** complete candidate, source lines 1–711.
- **S2:** complete prior Class A/B disposition, source lines 1–48.
- **S3:** complete separate symmetric-\(W_4\) disposition, source lines 1–42.

No elided mathematical passage was accepted as read. The dispatch receipt was also read as administrative context.

The review used written algebra and written arithmetic on the **already frozen example**. It did not use new selected mathematical instances, scientific programs, CAS, interpreters, solvers, enumeration, author code, sibling returns, held payloads, or excluded links.

- Native metadata commands: **NOT RUN**; parent-supplied observations are attributed accordingly.
- Scientific execution and finite physical-channel checks: **NOT RUN**, as required by the WRITTEN role.
- Builds, tests, lint, and formatters: **NOT RUN**.
- External-model CLI, paid/heavy runs, and public communication: **NOT PERFORMED**.

All genuinely held episodes and their method, selection, confidence, reporting, and proof consumers remained NONINPUT. The status records were not used as mathematical premises.

## 2. Exact scope and import boundaries

The new result reconstructed here concerns

\[
\Phi_p(X)=(1-p)X+\frac p2\operatorname{Tr}(X)I,
\qquad 0\le p\le\frac43,
\]

with

\[
t=|1-p|,\qquad a=\frac{1+t}{2},\qquad b=\frac{1-t}{2},
\qquad D_{n,t}=\operatorname{diag}(a,b)^{\otimes n}.
\]

The supported new scopes are:

1. Every complex three-qubit density commuting with \(Z^{\otimes3}\), and every physical-local-basis version of that condition.
2. All eight output-majorization prefixes, hence every complex orthogonal rank-\(k\) consuming projector, \(k=1,\ldots,8\).
3. Every four-qubit product of an arbitrary one-qubit spectator density and a three-qubit density in that parity sector, with arbitrary spectator placement and physical local bases.
4. Finite convex mixtures of those four-qubit products, allowing spectator placement and bases to vary between components.
5. All sixteen prefixes for that four-qubit class.
6. Strict enlargement when the new class is adjoined to the previously adopted Class A/B hull.

**Import used for item 6 only:** S2’s already scoped Class A/B all-prefix theorem. I did not reconstruct its underlying author proofs or rerun its reported finite checks. Its prior assurance remains its own, not a fresh result of this review.

The inherited reference to the “scoped S1 theorem” at candidate S1:565–571 denotes that prior Class A/B theorem by its description; in the present packet it is **S2**, not a self-import from the new candidate.

S3’s symmetric-\(W_4\) result is a **separate scoped disposition**. Its coefficient table and previously reported verifier results are not premises of the parity-sector proof.

## 3. Claim-by-claim disposition

| Claim | Disposition | Reconstructed scope |
|---|---|---|
| Complex-projector Ky Fan characterization | **SUPPORTED** | S1:99–108; arbitrary complex Hermitian orthogonal projectors |
| Direct-sum and finite-mixture majorization | **SUPPORTED** | S1:110–140; full-space projectors, not block-restricted ones |
| Actual complex pure-parity output blocks | **SUPPORTED** | S1:144–215; including conjugation in the complementary block |
| Coupled estimates and all eight prefixes | **SUPPORTED** | S1:219–406; every normalized complex coefficient vector, including zeros |
| Mixed parity states and local bases | **SUPPORTED** | S1:410–422 |
| Entire physical parameter range | **SUPPORTED** | S1:424–462; full transpose/spin flip and complex-projector transport |
| Tensor preservation | **SUPPORTED** | S1:468–483; positivity hypotheses are present and sufficient |
| Four-qubit finite hull with variable spectator/bases | **SUPPORTED** | S1:486–508; all sixteen prefixes, one arbitrary consuming projector |
| Complex spectator-\(W_3\) witness belongs to new class | **SUPPORTED** | S1:514–522 |
| Witness lies outside every Class A/B component and their hull | **SUPPORTED** | S1:524–571; all pairings and physical local bases |
| Frozen physical example and its projectors | **SUPPORTED** | S1:579–638; written exact arithmetic only |
| Separate parity-block product majorization | **REFUTED**, as the candidate states | S1:640–654; this is a rejected auxiliary premise, not a defect in the theorem |
| Closure by parity pinching | **REFUTED**, as the candidate states | S1:683–687; the majorization implication has the wrong direction |
| Unrestricted three-/four-qubit closure | **INCONCLUSIVE / NOT ESTABLISHED** | Explicitly outside the candidate’s proved scope |
| Novelty and validity of older stronger printed claims | **INCONCLUSIVE / NOT ADJUDICATED** | No priority claim or external proof-validity certification follows |

## 4. Reconstruction of the three-qubit premise

Although this wave particularly emphasizes tensor preservation and separation, I also reconstructed the load-bearing parity proof rather than treating its headline as an accepted premise.

### 4.1 Actual physical output and complex phases

For positive Bloch parameter,

\[
T_t(X)=tX+b\operatorname{Tr}(X)I.
\]

Use even strings \(e_i=(000,011,101,110)\) and complementary odd strings \(\bar e_i=e_i\oplus111\). For

\[
|\psi\rangle=\sum_i c_i|e_i\rangle,\qquad
R=cc^\dagger,\qquad D=\operatorname{diag}(|c_i|^2),
\]

define

\[
A=(1-t)D+tR,\qquad B=(1+t)D-tR.
\]

Distinct even strings differ in exactly two positions. Their off-diagonal matrix units therefore acquire \(t^2\), with common-bit retention factor \(a\) in the active parity block and flip factor \(b\) in the complementary block.

Writing \(u=a^3,d=a^2b,c_0=ab^2,\ell=b^3\), this gives exactly

\[
M_E=c_0I+atA,\qquad M_O=dI-bt\,\overline B.
\]

In particular, the complementary off-diagonal entry is

\[
bt^2\overline{c_i}c_j,
\]

not \(bt^2c_i\overline{c_j}\). Thus the displayed conjugation handles arbitrary complex phases correctly. It is not a partial transpose.

The diagonal entries and traces are

\[
(M_E)_{ii}=c_0+at|c_i|^2,\qquad
(M_O)_{ii}=d-bt|c_i|^2,
\]

\[
\operatorname{Tr}M_E=u+3c_0,\qquad
\operatorname{Tr}M_O=3d+\ell.
\]

These are actual channel outputs, not assumed spectral forms.

### 4.2 Bounds on \(A\) and \(B\)

\(A\) is positive with trace one. On \(c^\perp\), the quadratic form of \(B\) is nonnegative, so \(B\) has at most one negative eigenvalue.

The complex Gram identity in S1:246–255 is correct: its diagonal entries are \(1-|c_i|^2\), and its \(ij\) entry is \(c_i\overline{c_j}\). Hence

\[
I-2D+R\ge0,
\qquad
B=(1-t)D+t(2D-R)\le I.
\]

For \(t\le1/3\), \(R\le4D\) implies \(B\ge0\).

For \(t>1/3\), setting \(g=(3t-1)/4>0\), concavity gives

\[
\sum_i\frac{|c_i|^2}{g+(1+t)|c_i|^2}\le\frac1t.
\]

Weighted Cauchy–Schwarz therefore yields \(tR\le(1+t)D+gI\). Thus, with

\[
\gamma=\max(0,-\lambda_{\min}(B)),\qquad \delta=bt\gamma,
\]

one obtains

\[
\gamma\le\max\left(0,\frac{3t-1}{4}\right)\le\frac a2,
\qquad 2\delta\le abt.
\]

Zero populations cause no division problem: the rational denominators are used only in the branch \(g>0\).

For \(m=\max_i|c_i|^2\) and \(\alpha=\lambda_{\max}(A)\),

\[
\alpha\le t+(1-t)m.
\]

The candidate’s decomposition of \(c\) gives

\[
R-2D\le2(1-m)I,\qquad \gamma\le2t(1-m).
\]

Consequently,

\[
\delta\le2bt^2(1-m)
\le2abt(1-m)
\le at(1-\alpha).
\]

The direction of the final inequality is correct: the upper bound on \(\alpha\) gives the required **lower** bound on \(1-\alpha\).

### 4.3 Majorants, ordering, positivity, and all prefixes

The preceding estimates imply

\[
M_E\prec\operatorname{diag}(u-\delta,c_0+\delta,c_0,c_0)
\]

and

\[
M_O\prec\operatorname{diag}(d+\delta,d,d-\delta,\ell).
\]

For \(M_E\), the top-one bound follows from the coupled deficit. The top-two and top-three bounds follow by subtracting respectively two and one eigenvalues bounded below by \(c_0\) from its fixed trace.

For \(M_O\), at most one eigenvalue exceeds \(d\), its maximum is at most \(d+\delta\), and its minimum is at least

\[
d-bt=\ell.
\]

These facts supply all four prefixes.

The global ordering is justified, including the comparisons needed between the blocks:

\[
d-\delta\ge c_0+\delta,\qquad
u-\delta\ge d+\delta,
\]

because \(2\delta\le abt=d-c_0\) and \(abt\le a^2t=u-d\). Internal ordering and nonnegativity also follow:

- \(u-c_0=at\ge2\delta\).
- \(d-\ell=bt\ge\delta\), since \(\gamma\le a/2\le1\).
- \(c_0\ge\ell\ge0\).

Thus direct-sum majorization produces the genuinely ordered, nonnegative vector

\[
v=(u-\delta,d+\delta,d,d-\delta,c_0+\delta,c_0,c_0,\ell).
\]

Against

\[
r=(u,d,d,d,c_0,c_0,c_0,\ell),
\]

the eight reference-minus-majorant prefix differences are exactly

\[
(\delta,0,0,\delta,0,0,0,0).
\]

All are nonnegative. This proves every prefix simultaneously; it does not select different physical hypotheses or separately attained layer maxima for different projectors.

### 4.4 Mixed states, bases, and endpoints

A density commuting with \(Z^{\otimes3}\) has two arbitrary positive complex \(4\times4\) blocks. Their spectral decompositions express it as a finite convex mixture of pure parity eigenstates. Odd parity follows by physical local-unitary covariance, and Ky Fan convexity completes the mixed-state step.

Every traceless Hermitian one-qubit unitary is unitarily conjugate to \(Z\), so the stated local-basis formulation is covered without a real-coefficient restriction.

The endpoint handling is valid:

- At \(t=0\), the output is \(I_8/8\).
- At \(t=1\), the active block is the original pure density and the complementary block is zero.
- At \(t=1/3\), the nonnegative-\(B\) argument applies without using the \(g>0\) denominators.
- Zero coefficients, tied eigenvalues, and zero block traces do not require normalization by those quantities.

## 5. Physical negative branch and consuming-projector transport

The Pauli probabilities

\[
q_I=\frac{1+3s}{4},\qquad q_X=q_Y=q_Z=\frac{1-s}{4}
\]

give precisely the physical range \(-1/3\le s\le1\).

The single-qubit identity

\[
\mathcal J(X)=YX^TY=\operatorname{Tr}(X)I-X
\]

implies \(T_{-t}=\mathcal J\circ T_t\), and therefore

\[
T_{-t}^{\otimes n}(\rho)
=
W_n[T_t^{\otimes n}(\rho)]^TW_n,
\qquad W_n=Y^{\otimes n}.
\]

This is full transpose followed by unitary conjugation. It preserves positivity and spectrum. No partial-transpose positivity assumption is made.

The consuming-side transformation also works for arbitrary complex projectors:

\[
Q'=W_nQ^TW_n.
\]

This is Hermitian, idempotent, and rank \(k\), and the trace pairing is transported correctly. The signs from \(W_n^T=(-1)^nW_n\) occur twice and cancel.

The physical negative branch requires only \(t\le1/3\), already included above. The one-qubit pure-output reference is spectrally \((a,b)\) on both branches, even though its physical coordinate order reverses for \(p>1\).

**Disposition:** The proof covers all physical \(p\), including \(p=0,1,4/3\), and arbitrary complex consuming projectors.

## 6. Tensor preservation and the actual four-qubit finite hull

### 6.1 Tensor-preservation proof

For positive matrices \(X\prec X_0\) and \(Y\prec Y_0\), diagonalize \(X\) with eigenvalues \(x_i\ge0\). Then

\[
K_k(X\otimes Y)
=
\max_{\sum_i k_i=k}\sum_i x_iK_{k_i}(Y)
\le
\max_{\sum_i k_i=k}\sum_i x_iK_{k_i}(Y_0)
=
K_k(X\otimes Y_0).
\]

The first inequality is legitimate because every multiplier \(x_i\) is nonnegative. Diagonalizing the positive matrix \(Y_0\), interchanging tensor factors, and applying \(X\prec X_0\) gives the second replacement. Equality of total traces is preserved.

This proves

\[
X\otimes Y\prec X_0\otimes Y_0.
\]

It requires neither an input-independent postprocessing channel nor compatible diagonalizers across different inputs.

### 6.2 Arbitrary spectator and variable-component hull

For any one-qubit density of Bloch radius \(r_\sigma\in[0,1]\), the ordered output eigenvalues are

\[
\frac{1+tr_\sigma}{2},\qquad \frac{1-tr_\sigma}{2}.
\]

They are nonnegative, sum to one, and are majorized by \((a,b)\). Combining this with the parity theorem gives

\[
\Phi_p(\sigma)\otimes\Phi_p^{\otimes3}(\tau)\prec D_{4,t}.
\]

Identical physical channels on all qubits commute with qubit permutations, so arbitrary spectator placement is covered. Physical local covariance covers arbitrary permitted local bases.

For a finite mixture of components, each component is bounded by the **same** \(K_k(D_{4,t})\). At one fixed arbitrary complex projector \(Q\),

\[
\operatorname{Tr}\!\left[Q\Phi_p^{\otimes4}\!\left(\sum_jw_j\rho_j\right)\right]
=
\sum_jw_j\operatorname{Tr}[Q\Phi_p^{\otimes4}(\rho_j)]
\le K_k(D_{4,t}).
\]

The spectator, bases, and density operators may vary with \(j\). No common componentwise maximizing projector is required.

For \(k=3\), the reference prefix is indeed

\[
K_3(D_{4,t})=a^4+2a^3b.
\]

**Disposition:** Theorem B is supported for its entire stated finite hull, all physical parameters, all sixteen prefixes, and all complex consuming projectors.

## 7. Strict separation from the complete prior Class A/B hull

The frozen witness is

\[
|\Omega\rangle
=
|0\rangle\otimes
\frac{|100\rangle+i|010\rangle+|001\rangle}{\sqrt3}.
\]

Its three-qubit factor has odd parity, so it belongs to the newly proved class.

### 7.1 Exclusion from Class A

Across the first qubit of the three-qubit factor, its two-qubit Schmidt support is

\[
\operatorname{span}\{|00\rangle,\ i|10\rangle+|01\rangle\}.
\]

A general vector in this support has coefficient matrix

\[
\begin{pmatrix}u&v\\iv&0\end{pmatrix},
\]

with determinant \(-iv^2\). Over the complex numbers, this vanishes only for \(v=0\). Hence the support has just one product-vector direction.

A tensor-rank-two state with Schmidt rank two across this cut would provide two independent product vectors spanning that support. This is impossible. The displayed three-term expansion supplies the matching upper bound, so the three-qubit tensor rank is three.

Every Class A vector has tensor rank at most two, even though its actual definition is more restrictive than that necessary condition. If \(\Omega\) had such a two-term four-qubit product decomposition, contraction against the spectator \(\langle0|\) would give a two-term product decomposition of its three-qubit factor. Therefore \(\Omega\) is not Class A in any physical local bases.

### 7.2 Exclusion from Class B for every pairing

Every pairing includes one pair containing the pure spectator and one of the three \(W\) qubits. Each such \(W\)-qubit marginal has rank two. The pair’s reduced support is therefore

\[
S=|0\rangle\otimes\mathbb C^2.
\]

Its projector is \(P_S=|0\rangle\langle0|\otimes I\), whose marginal **retaining the spectator** is \(2|0\rangle\langle0|\).

For a physical local-basis repetition code

\[
E=\operatorname{span}\{|u_0v_0\rangle,|u_1v_1\rangle\},
\]

both one-qubit marginals of its projector equal \(I_2\), since both local pairs are orthonormal. Thus \(S\ne E\). Both spaces have dimension two, so \(S\) cannot even be contained in \(E\).

This argument handles either ordering of the spectator in its pair, every pairing, and arbitrary physical local bases. It does not discard the complex phase.

Consequently, \(\Omega\) is not any Class B state.

### 7.3 Full convex hull and exact strictness statement

If a finite positive convex mixture equals a rank-one density, every positive-weight component must have support in that same one-dimensional range. A normalized component is therefore that same pure density.

Since \(\Omega\) is neither Class A nor Class B, its density is outside the **entire** old hull \(\mathcal C_{\rm old}\). Hence

\[
\operatorname{conv}(\mathcal C_{\rm old}\cup\mathcal S)
\supsetneq \mathcal C_{\rm old}.
\]

Using only S2’s existing scoped theorem for the old hull and the newly reconstructed theorem for \(\mathcal S\), finite convexity gives all-prefix majorization on that enlarged hull.

The separately adopted symmetric-\(W_4\) family remains separate. This review does **not** establish or claim that \(W_4\) lies outside this newly enlarged hull, or that \(\Omega\) lies outside the hull obtained by adjoining the \(W_4\) orbit to the old classes. Neither comparison is needed for the proved strictness over Class A/B alone.

## 8. Frozen physical example: written arithmetic

Only the example already supplied in S1 was used:

\[
p=\frac14,\quad t=\frac34,\quad a=\frac78,\quad b=\frac18.
\]

For the frozen complex \(W_3\) factor, the active coefficient vector has three equal populations and one zero. The displayed matrices therefore have spectra

\[
\operatorname{spec}(A)=\left(\frac56,\frac1{12},\frac1{12},0\right),
\qquad
\operatorname{spec}(B)=\left(-\frac16,\frac7{12},\frac7{12},0\right).
\]

Using

\[
c_0=\frac7{512},\quad d=\frac{49}{512},
\quad at=\frac{21}{32},\quad bt=\frac3{32},
\]

gives the active-parity spectrum

\[
\frac1{512}(287,35,35,7)
\]

and complementary-parity spectrum

\[
\frac1{512}(57,49,21,21).
\]

Thus the ordered actual spectrum is exactly

\[
\frac1{512}(287,57,49,35,35,21,21,7).
\]

Against the reference

\[
\frac1{512}(343,49,49,49,7,7,7,1),
\]

the eight prefix differences are

\[
\frac1{512}(56,48,48,62,34,20,6,0).
\]

The frozen vectors \(\psi_W,\eta,000\) are orthonormal. The conjugated phase in

\[
|\eta\rangle=\frac{|011\rangle-i|101\rangle+|110\rangle}{\sqrt3}
\]

is correct for the complementary block. The resulting complex \(Q_3\) selects the eigenvalues \(287,57,49\), giving

\[
\operatorname{Tr}(Q_3T_t^{\otimes3}(\psi_W))=\frac{393}{512}.
\]

For the actual four-qubit spectator input and

\[
Q_4=|0\rangle\langle0|\otimes Q_3,
\]

the spectator contributes \(a=7/8\), giving

\[
\frac78\frac{393}{512}=\frac{2751}{4096}.
\]

The rank-three reference is

\[
a^4+2a^3b
=
\frac{2401+686}{4096}
=
\frac{3087}{4096},
\]

with slack \(336/4096=21/256\), as stated.

Finally, \(57/512>49/512\) verifies the candidate’s rejection of **separate corresponding parity-block majorization**. The full eight-prefix comparison remains valid. These are written checks, not executed finite corroboration.

## 9. Limits, literature, and remaining gates

### Discharged within this written review

- Actual complex physical-channel blocks.
- All load-bearing coupled inequalities and all eight prefixes.
- Positivity and ordering of the intermediate majorants.
- Mixed-state and local-basis extension.
- Full physical parameter range and consuming-projector transport.
- Positive tensor-majorization preservation.
- Actual four-qubit finite hull with variable spectators and bases.
- Strict separation from the full old Class A/B hull.
- The frozen complex-projector physical example.

### Still unpaid or outside scope

1. **Arbitrary three-qubit input:** cross-parity coherence \(C=\Pi_+\rho\Pi_-\) is not controlled by this proof. Parity pinching yields a more mixed output and cannot transfer this upper bound back to the unpinched output.
2. **General \(1|3\)-separable four-qubit input:** its three-qubit factors need not satisfy the proved parity condition.
3. **Unrestricted four-qubit \(k=3\) and all-prefix majorization:** not established.
4. **Finite physical-channel corroboration of this candidate:** not performed by this WRITTEN role. No execution or mutation-test PASS is claimed.
5. **Parent disposition:** not supplied by this return.
6. **Independent-family, human, or formal-kernel verification:** not performed.
7. **Novelty and older-proof validity:** unresolved.

In particular, S3 reports earlier formally stronger printed tensor-product majorization claims in Amosov’s cited preprints, while explicitly leaving proof validity and correspondence to inaccessible journal text uncertified. This review neither assumes those claims correct nor declares them false. It makes no first-result or novelty claim.

The frozen shifted-determinant example also correctly demonstrates that the quoted determinant-ordering premise alone does not imply exact prefix ordering: its determinant difference is \(h/5000+161/500000>0\), while its largest-eigenvalue comparison has the opposite required direction. External source coverage itself was not independently re-audited here.

## 10. Final verdict

**Findings:** None at the reconstructed scope — **0 FATAL / 0 MAJOR / 0 MINOR**.

**overall_correctness:** correct

**explanation:** The candidate’s complex parity-sector majorization, positive tensor-preservation argument, variable-spectator finite-hull extension, and strict separation from the prior Class A/B hull withstand written reconstruction. This verdict is scoped to those statements and does not certify unrestricted-target closure, finite execution, novelty, older literature’s proof validity, or parent adoption.

**confidence:** 0.97