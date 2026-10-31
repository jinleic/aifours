# author-candidate-v1.md — Bounded public-source audit of arbitrary three-qubit depolarizing majorization

**Status: PUBLIC SOURCEAUDIT RETURN — parent disposition required. No mathematical adoption or novelty clearance is issued.**

## 1. Principal result

**An exact prior theorem for the candidate’s two-body marginal-sum conclusion was located.** In **Song–Chen, *A counterexample to the strong spin alignment conjecture*, arXiv:2603.25410v1**, Section III, Proposition 3, Equation (15), the authors state and prove a **weighted** majorization theorem for the compatible two-body marginals of an arbitrary three-qubit state. Its equal-weight specialization is precisely

\[
H_2(\rho)\prec \operatorname{diag}(3,1,1,1,0,0,0,0).
\]

This is not a parity-restricted, real-input, pure-input-only, entropy, norm, or approximate result. The source statement permits arbitrary three-qubit density operators and arbitrary nonnegative weights. The complete relevant HTML argument and the five-page primary PDF were read; the PDF also supplied Equation (35), which was blank in the HTML rendering.

Consequently:

- **The \(H_2\) theorem itself cannot be credited as a newly discovered statement.**
- The candidate’s **paired-projection derivation** remains a separately reviewable proposed proof method. This audit neither verifies it nor establishes its novelty.
- The arbitrary-three-use channel theorem now has a **specific prior-theorem/corollary comparison obligation**, not merely an unresolved keyword search.
- Song–Wang–Tomamichel–Fang, arXiv:2609.37240v1, still does **not** itself prove the candidate’s exact three-use all-prefix theorem.
- The older, stronger Amosov tensor-majorization claims remain relevant prior claims, but their already identified proof-step obstructions are **not** counterexamples to their theorem statements.

**Recommended source classification:**  
**DIRECT PRIOR \(H_2\) THEOREM FOUND; THREE-USE THEOREM/METHOD PRIORITY NOT CLEARED; OLDER STRONGER TENSOR CLAIMS STILL QUALIFIED.**

## 2. Frozen identity, coverage, and methods

### 2.1 Assignment identity

Wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f467-three-qubit-exact-majorization-bounded-public-source-audit/`

The following are **parent-supplied observations**, not independently computed child hashes or child-native timestamps:

| Record | Parent-supplied SHA-256 | Bytes | LF |
|---|---|---:|---:|
| Manifest | `ab9a0296dc9a056bbb0e10f52240bf0f3cb676b3b481a1ee1b3825a40246f2cf` | 7,788 | 130 |
| Freeze receipt | `d7cbae94a0868d3b3ea87df6a51bc22b7f25d01cab3a046b40484afdce4ece6b` | 2,922 | 73 |
| Literal packet | `d08625ed1edf5499b8a50466db0fdb7112d8db98fc4c2aa164e70b9101c0be33` | 70,023 | 1,225 |

The supplied observation clock was **2026-10-30T11:57:24-0700 PDT**, attributed exclusively to the parent. No independently observed child start, completion time, or elapsed duration is asserted.

### 2.2 Actual local read chronology

Before opening the scientific packet, I read the complete manifest, freeze receipt, parent-live metadata supply, and all ten status/permission controls, including their endings:

- prospective author-method restoration, LF 1–15;
- owner frontier-first addendum, LF 1–14;
- L1 quarantine, LF 1–23;
- privacy quarantine, LF 1–11;
- CORE-GRAM quarantine, LF 1–9;
- AME held-consumer quarantine, LF 1–8;
- PH held-registration/report quarantine, LF 1–49;
- F439 quarantine, LF 1–23;
- F444 quarantine, LF 1–16;
- F448 quarantine, LF 1–20.

A direct pre-body acknowledgement was sent to Main. I then read **literal-packet-v1.md LF 1–1225 sequentially in raw windows of at most 20 lines**, including every source ending:

| Frozen input | Actually displayed logical source lines | Assigned status |
|---|---:|---|
| S1: F463 candidate | 1–783 | Unreviewed candidate; target definition, not accepted proof |
| S2: ancillary orbit-span obstruction disposition | 1–13 | Scoped adopted proof-step obstruction |
| S3: weakened tensorization implication disposition | 1–21 | Scoped countermodel, not a full two-channel counterexample |
| S4: earlier bounded W4 source audit | 1–406 | Background source/status record |

The logical-line counts for S1 and S4 exceed their supplied LF-byte counts by one; both final logical lines were actually displayed. Coverage is not inferred solely from a receipt.

The dispatch receipt was read after the packet. Public-source research followed the complete packet reading.

### 2.3 Method and assurance boundaries

- **No scientific executable, calculator, CAS, numerical experiment, candidate proof replay, or author program was run.**
- Code, argv, experiment inputs, and execution results: **none**.
- Parameter identifications below are literature-hypothesis comparisons, not independent reconstructions of the candidate.
- No off-manifest sibling scientific return was opened. Frozen S4 was read because it was an expressly assigned input.
- Held mathematical episodes and their consumers remained **NONINPUT**. Quarantine controls were used only for status and permissions.
- No external-model CLI, paid/heavy job, installation, deletion, credential change, Git mutation, build, test, linter, or formatter was used.
- No repository file was written. This is the complete body for Main’s materialization; no write bypass was attempted.
- This return supplies source attribution and scope comparison—not human, independent-model-family, finite-check, or formal/kernel assurance.

## 3. Exact objects being compared

The candidate uses

\[
\Phi_p(X)=(1-p)X+\frac p2\operatorname{Tr}(X)I_2,
\qquad 0\le p\le\frac43,
\]

and

\[
t=|1-p|,\qquad a=\frac{1+t}{2},\qquad b=\frac{1-t}{2}.
\]

Its principal channel claim is

\[
\lambda\!\left(\Phi_p^{\otimes3}(\rho)\right)
\prec
\lambda\!\left(\operatorname{diag}(a,b)^{\otimes3}\right)
\]

for **every complex three-qubit density operator**, equivalently all eight Ky Fan prefixes and every consuming complex orthogonal projector.

Its load-bearing marginal statement is

\[
H_2(\rho)=
\rho_{AB}\otimes I_C+
\rho_{AC}\otimes I_B+
I_A\otimes\rho_{BC}
\prec
L_2,
\]

where

\[
L_2=\operatorname{diag}(3,1,1,1,0,0,0,0).
\]

The proposed proof method uses three-qubit spin flip, an invariant rank-two projection for pure inputs, a normalized complementary-pair spectral decomposition, and compressed projection spectra.

The claimed four-qubit consequence concerns the convex hull of states separable across the four \(1|3\) cuts. **It is not the unrestricted four-qubit theorem.**

These distinctions are retained throughout this audit.

## 4. Direct prior theorem: Song–Chen’s compatible-marginal result

### 4.1 Source and version

Zhiwei Song and Lin Chen, **[A counterexample to the strong spin alignment conjecture](https://arxiv.org/html/2603.25410v1)**, arXiv:2603.25410v1.

The [current abstract-page submission history](https://arxiv.org/abs/2603.25410) inspected as raw HTML lists only v1, submitted **26 March 2026**. The [versioned PDF](https://arxiv.org/pdf/2603.25410v1) carries an internal date of 27 March 2026. The regenerated HTML title-page date was not used as its submission or publication date. No journal publication for this paper was established in this audit.

**Read coverage:** complete returned HTML, including Section III and references/ending; complete five-page versioned PDF; current abstract-page metadata and submission history.

### 4.2 Exact statement overlap

Section III, **Proposition 3, Equation (15)** states, for nonnegative \(u,v,w\) with \(u+v+w=1\), and for a three-qubit state \(\rho_{ABC}\),

\[
\begin{aligned}
&u\,\rho_{AB}\otimes I_C
+v\,\rho_{AC}\otimes I_B
+w\,I_A\otimes\rho_{BC}\\
&\quad\prec
u\,|00\rangle\langle00|_{AB}\otimes I_C
+v\,|00\rangle\langle00|_{AC}\otimes I_B
+w\,I_A\otimes|00\rangle\langle00|_{BC}.
\end{aligned}
\]

The notation \(u,v,w\) here avoids confusing the source’s weights with the candidate’s channel eigenvalues \(a,b\).

**[INFERENCE — exact source specialization, not candidate proof replay.]** Setting the three source weights equal and scaling both sides gives exactly the candidate’s \(H_2\prec L_2\) statement. The source also explicitly identifies the unweighted reference spectrum as

\[
(3,1,1,1,0,0,0,0)
\]

and concludes \(X_3\prec T_3\) in **Equation (34)**.

The hypotheses match as follows:

| Feature | Source Proposition 3 | Candidate \(H_2\) conclusion |
|---|---|---|
| Local systems | Three qubits | Three qubits |
| Global state | Arbitrary density operator | Arbitrary density operator |
| Complex inputs | No reality restriction | No reality restriction |
| Parity | No parity restriction | No parity restriction |
| Marginals | From the same global state | From the same global state |
| Inequality | Exact spectral majorization | Exact spectral majorization |
| Prefix coverage | All prefixes | All prefixes |
| Coefficients | Arbitrary nonnegative weights | Equal-weight sum |

This is **direct theorem-statement overlap in a stronger weighted form**, not merely a suggestive title or a norm/entropy analogue.

### 4.3 What the source’s proof actually contains

For the unweighted sum, Section III uses:

- convex reduction to pure global states;
- local diagonalization of the one-qubit marginals;
- the three-qubit polygon inequalities;
- the spin-flip identity in Equations (29)–(31);
- a decomposition \(X_3=D+P\);
- lower-tail/Weyl estimates giving the first three Ky Fan bounds;
- positivity and total trace for the remaining prefixes.

The weighted extension decomposes the weighted sum into one-, two-, and three-summand pieces. Its two-summand import is Alhejji–Knill’s Corollary IV.10; the final Ky Fan combination is Equation (35).

**Rendering limitation resolved:** Equation (35) was empty in the HTML output. Its complete chain is present in the primary PDF on page 4 and was read there. I did not infer the missing displayed equation from surrounding prose.

The source’s method is **not the candidate’s displayed paired-projection compression argument**. Thus prior theorem overlap does not, by itself, establish proof-method identity.

**Assurance ceiling:** the source’s full relevant proof was read for attribution and hypothesis comparison. No independent mathematical soundness disposition of that proof is issued here.

### 4.4 The counterexample in that paper is not a physical counterexample here

Section II chooses three two-body pure states independently and reports a violation of the unrestricted strong spin-alignment conjecture. The paper expressly distinguishes these from marginals compatible with a single three-qubit global state.

Therefore its counterexample does **not** refute:

- Proposition 3;
- the candidate’s compatible-marginal \(H_2\) statement;
- arbitrary-three-qubit depolarizing-output majorization.

The reported approximate eigenvalues and entropy values are **source-reported numerics**, not computations performed by this audit.

### 4.5 Consequence for novelty assessment

The exact \(H_2\) statement must be credited to **Song–Chen, Proposition 3**. At that lemma level, the candidate can be assessed as a proposed alternative proof, not a new theorem statement.

**[INFERENCE — corollary comparison obligation.]** Because the candidate’s channel argument combines this precise \(H_2\) bound with a one-body majorant and the ordinary depolarizing marginal expansion, a theorem-level priority assessment must explicitly examine the resulting prior-theorem corollary. It cannot infer novelty from the absence of a separately titled “three-use depolarizing majorization” theorem.

This is not an independent certification of that corollary or of the candidate’s negative-parameter transport.

## 5. Required source: Song–Wang–Tomamichel–Fang

### 5.1 Version and actual coverage

Zhiwei Song, Xin Wang, Marco Tomamichel, Kun Fang, **[Approximate majorization and high-order capacity of quantum depolarizing channels](https://arxiv.org/html/2609.37240v1)**, arXiv:2609.37240v1, **29 September 2026**.

The current abstract page, inspected as raw HTML, lists only v1 in its submission history. No separate journal publication was established.

**Read coverage:** the complete 843-line reader rendering, Sections 1–5, references, Appendix A.1–A.2, and ending. Relevant long reference/discussion lines were additionally displayed raw. Reader record: `artifact://67184`.

### 5.2 Exact majorization is conjectural in this source

Section 1, Equation (2), proposes the unrestricted relation for arbitrary dimension, arbitrary blocklength, and arbitrary possibly entangled inputs. It introduces it with:

> “We conjecture that the output corresponding to a pure product input majorizes the output corresponding to any other input.”

Section 5 again identifies establishing that relation **in general** as an open direction.

**Small-\(n\) qualification:** I did not find a theorem in this paper separately proving exact arbitrary-input \(n=3,d=2\) majorization. Equally, its statement that the **general** conjecture remains open must not be rewritten as a claim that every small-\(n\) specialization is open or novel.

### 5.3 Exact log-determinant ordering is not exact all-prefix ordering

Section 3.1, **Theorem 4, Equation (20)** proves shifted-log-determinant ordering for all blocklengths and all states, with \(0<p\le p_{\max}(d)\).

The source itself identifies this as a **necessary condition** for its majorization conjecture. Remark 5 and Appendix A distinguish its implications from full spectral ordering.

Thus specializing Theorem 4 to three qubits does not, by that specialization alone, supply all eight exact prefix bounds.

### 5.4 Approximate majorization does not settle fixed \(n=3\)

Theorem 1, Theorem 7, and Corollary 8 give a defect bound of order

\[
\frac{\log\log n+6}{\sqrt n}
\]

for fixed nondegenerate channel parameters and all sufficiently large blocklengths.

This is neither a zero-defect theorem at \(n=3\) nor a substitute for a fixed-use all-parameter exact certificate.

### 5.5 Appendix counterexamples have the stated nonphysical boundary

Appendix A explicitly says its counterexamples concern arbitrary states **not assumed to arise as channel outputs**.

They show that certain functional inequalities do not logically imply the desired majorization for freely chosen spectra. They do not constitute actual depolarizing-channel counterexamples.

### 5.6 References and the newly found \(H_2\) result

The inspected bibliography includes King’s depolarizing norm/capacity work and the analytic/probabilistic references supporting this paper’s method. The returned text did not contain a reference to the Song–Chen compatible-marginal result, Alhejji’s spin-alignment results, or Amosov’s tensor-majorization chain.

That is a statement about **this inspected bibliography**, not proof that those subjects have no connection or that one set of authors overlooked a valid theorem.

## 6. Relevant established small-system and norm precedents

### 6.1 Alhejji–Knill: spin alignment and the channel-marginal connection

**[Towards a resolution of the spin alignment problem](https://arxiv.org/html/2307.06894v3)**, arXiv:2307.06894v3, **5 March 2024**.

Relevant inspected passages include:

- Section III, Equation (III.6): the tensor-product depolarizing channel expressed using **compatible marginals** and maximally mixed factors;
- Remark IV.3: the strong spin-alignment conjecture holds for \(n=d=2\);
- Theorem IV.7: integer-order Schatten-norm results;
- Section IV.D, Theorem IV.9 and Corollary IV.10: the relevant two-summand/projector results.

**Boundary:** the channel connection in Equation (III.6) is written for nonnegative local depolarizing coefficients. The unrestricted strong spin-alignment problem permits independently chosen subset states and is stronger than the compatible-output problem. Its later counterexample cannot simply be transported to physical channel outputs.

This source already makes the compatible-marginal/channel relationship explicit; that conceptual connection should not be presented as new.

### 6.2 Alhejji: exact two-letter spin alignment

**[Refining Ky Fan’s majorization relation with linear programming](https://arxiv.org/html/2410.18254v3)**, arXiv:2410.18254v3, **16 June 2025**.

Theorem 1.3 gives the separable Fan relation for a sum of two tensor products of positive operators. Section 4.3, **Proposition 4.4, Equation (4.24)** proves the exact two-letter strong spin-alignment relation.

The [publisher’s open-access article](https://link.springer.com/article/10.1007/s00023-025-01592-w) was also read at Theorem 1.3 and Proposition 4.4, including the latter’s proof. Publisher metadata gives online publication **16 June 2025**, with **Annales Henri Poincaré 27, 909–932 (2026)**.

This establishes a genuine exact two-letter precedent. It is not an arbitrary-three-letter theorem.

No source-wide byte or proof identity between the manuscript and journal article is asserted; the identified statements were inspected in both.

### 6.3 A newer extension still has a two-summand boundary

Alhejji and Kelson-Packer, **[A majorization relation for a sum of two tensor products of positive semidefinite operators](https://arxiv.org/html/2607.07913v1)**, arXiv:2607.07913v1, **8 July 2026**.

The complete returned article and references were read.

Theorem 1.1 extends the separable Fan relation to **two summands with arbitrarily many tensor factors**. Section 4 gives a counterexample to the unrestricted extension to three summands and three factors.

It does not supply the candidate’s compatible \(H_2\) theorem by merely changing “two” to “three.” Its counterexample is not an actual depolarizing-output counterexample. The article’s reference [13] independently confirms the Song–Chen paper as a public antecedent; it does not independently validate Proposition 3.

### 6.4 King’s full-range result concerns norms and entropy

Christopher King, **[The capacity of the quantum depolarizing channel](https://arxiv.org/html/quant-ph/0204172v1)**, quant-ph/0204172v1, **30 April 2002**; cited in the inspected literature as IEEE TIT **49**, 221–229 (2003).

Sections 1.2 and 1.6, especially Theorem 3, were read. The source includes the full completely positive parameter interval and proves maximal-output Schatten-norm multiplicativity with an arbitrary auxiliary channel, with minimum-output-entropy additivity as a consequence.

This is substantial prior work, but it is **not the full family of Ky Fan-prefix inequalities**. Neither “all Schatten norms” nor “arbitrary auxiliary channel” should be relabelled as the candidate’s exact majorization theorem.

## 7. Spin flip, universal inversion, and paired projections

### 7.1 Universal inversion is established machinery

Rungta, Bužek, Caves, Hillery, Milburn, **[Universal state inversion and concurrence in arbitrary dimensions](https://arxiv.org/html/quant-ph/0102040v2)**, quant-ph/0102040v2, **10 June 2001**.

The introduction, Section II.1, and the relevant portion of Section II.2 were read, including the spin-flip representation and

\[
\mathcal S_D(A)=\nu_D[\operatorname{Tr}(A)I-A].
\]

The source distinguishes positive inversion from completely positive physical dynamics.

It is an antecedent for the inversion machinery, not an inspected proof of the candidate’s \(H_2\) majorant.

### 7.2 The alternating marginal identity and odd-party property predate the candidate

Eltschka, Huber, Gühne, Siewert, **[Exponentially many entanglement and correlation constraints for multipartite quantum states](https://arxiv.org/html/1807.09165v1)**, arXiv:1807.09165v1, **24 July 2018**.

The inspected portions include:

- Equation (3): the three-party alternating marginal identity;
- Equations (5)–(8): multipartite inversion;
- Equation (19): the vanishing pure-state invariant for an odd number of minus signs;
- the “Compatibility of marginals” discussion and Equation (26).

These explicitly precede the candidate’s use of the alternating marginal sum and establish relevant historical machinery. The inspected passages do not themselves state \(H_2\prec L_2\).

References there to earlier compatibility work were not silently treated as separately inspected primary proofs.

### 7.3 Quaternionic projection theory is related, not an identified identical lemma

Terry Loring, **[Principal angles and approximation for quaternionic projections](https://arxiv.org/html/1306.1923v1)**, arXiv:1306.1923v1, **8 June 2013**.

Section 1, Theorem 1.1, Corollary 1.3, and the surrounding discussion were read. They treat projection geometry respecting antiunitary symmetry, including paired principal vectors for invariant subspaces.

The hypothesis distinction matters: Corollary 1.3 concerns **two antiunitary-invariant subspaces**, whereas the candidate’s construction combines an invariant projection with a projection sent to its **complement**. I did not locate the candidate’s exact normalized paired-projection \(H_2\) argument as a theorem in the inspected Loring text.

**Permitted conclusion:** relevant classical projection/antiunitary machinery exists.  
**Not permitted:** “Loring already proves this exact lemma,” or conversely, “the paired-projection method is novel.”

## 8. Older stronger tensor-majorization claims remain qualified

### 8.1 Amosov 2022 manuscript

G. G. Amosov, **[On capacity of quantum channels generated by irreducible projective unitary representations of finite groups](https://arxiv.org/html/2103.08515v6)**, arXiv:2103.08515v6, **3 February 2022**.

Sections 5–6, including Propositions 2, 4, 5 and the explicit iteration, and Section 7’s qubit example were read. The full load-bearing ancillary orbit-span assertion was additionally read raw.

The accessible manuscript genuinely prints an **exact arbitrary-use tensor-product majorization claim**. At the hypothesis/quantifier level, the frozen S4 comparison encompasses the present three-qubit target throughout the physical interval: the Pauli weights are

\[
u=1-\frac{3p}{4},\qquad v=\frac p4,
\]

and the appropriate descending coset marginals give the ordered one-qubit output vector \((a,b)\) on both parameter branches.

This is not merely a capacity-title match.

However, frozen S2 records an adopted obstruction to Proposition 4’s orbit-span dimension/irreducibility step. Frozen S3 records insufficiency of the weaker combination used in the displayed Proposition 5 argument, while expressly excluding its countermodel as a full admissible two-channel counterexample.

These scopes remain unchanged:

- defective proof step: **yes, at the adopted scope**;
- theorem statement disproved: **no**;
- general Proposition 4/5 repaired or accepted here: **no**;
- unrestricted four-qubit/all-\(n\) target closed: **no**.

The [publisher page](https://link.springer.com/article/10.1007/s11128-022-03431-x) confirms **Quantum Information Processing 21, article 81**, published **3 February 2022**, but serves a subscription preview rather than the mathematical full text. **No identity with uninspected journal mathematics is asserted.**

### 8.2 Amosov 2024 manuscript

**[On characteristics of mixed unitary channels being additive or multiplicative with respect to taking tensor products](https://arxiv.org/html/2401.05104v1)**, arXiv:2401.05104v1, **10 January 2024**.

The complete returned body and ending were read.

Section III, Proposition 1, and Section IV, Theorem 2/Equation (17), print another exact tensor-majorization chain. The previously recorded textual qualifications remain visible:

- Equation (8) uses a non-strict comparison without the same distinct-index condition as the 2022 formulation.
- Theorems 1 and 2 print an infimum for convex functionals while the displayed proofs derive upper-bound inequalities.

No silent amendment, complete proof-refutation, or theorem adoption is made.

The newer direct \(H_2\) theorem is an additional source comparison; it does not retrospectively resolve either older chain.

## 9. Consolidated comparison

| Candidate-related claim | Strongest relevant observation from this audit | Status |
|---|---|---|
| Exact compatible \(H_2\) majorant for arbitrary complex mixed three-qubit states | Song–Chen Proposition 3, with stronger nonnegative weighted scope | **Direct prior theorem statement found; proof present and read** |
| Candidate’s specific paired-projection derivation | Related spin-flip, inversion and quaternionic projection machinery inspected; identical derivation not located | **Method priority unestablished; proof gate unpaid** |
| Exact arbitrary-input three-use depolarizing majorization | Direct \(H_2\) prior creates a concrete corollary-comparison obligation; older Amosov claims formally subsume it | **No first-result or novelty clearance** |
| Song–Wang–Tomamichel–Fang proves the exact \(n=3\) result | It proves log-determinant ordering and asymptotic approximate majorization | **Unsupported attribution** |
| General exact majorization remains a conjecture in that paper | Explicit in Equation (2) and Section 5 | **Verified source statement, not proof that every small case is open** |
| King’s norm/entropy theorem is full majorization | Different conclusion | **Do not conflate** |
| Free-subset spin-alignment counterexample refutes the physical target | Compatibility/actual-output hypotheses are absent | **No such implication** |
| Older proof obstruction refutes the older theorem | Adopted records expressly distinguish these | **No such implication** |
| Four-qubit \(1|3\) hull closes unrestricted four-qubit majorization | Genuinely four-party-entangled inputs remain outside that class | **No** |

**Significance calibration:** no major contribution or new-theorem priority is established by this audit. At the \(H_2\) level there is direct prior overlap. A separately validated paired-projection proof could still be useful, but its originality and value require an explicit method comparison rather than inference from a search miss.

## 10. Four-qubit consequence and the biseparable boundary

The candidate claims the convex hull over the four single-qubit-versus-three-qubit separable cuts.

**[INFERENCE — conditional scope bookkeeping only.]** If the arbitrary-three-qubit theorem is independently validated, and the necessary two-qubit theorem is separately admitted with matching physical-parameter and complex-input scope, combining the \(1|3\) and \(2|2\) cut classes under a common majorant could cover **all four-qubit biseparable states**, including mixtures across different cuts.

That conditional bookkeeping does not establish:

- the candidate’s proof;
- a new accepted union theorem;
- coverage of genuinely four-party-entangled states;
- unrestricted four-qubit majorization or its unrestricted \(k=3\) target.

No family, human, kernel, priority, or full-original-target credit follows.

## 11. Search coverage and access limits

Ordinary public searches covered:

- depolarizing majorization with three-qubit/three-use terminology;
- compatible marginal-sum majorization;
- spin flip and universal state inversion;
- quaternionic projections and Kramers-pair terminology;
- the exact titles and identifiers of the spin-alignment and older tensor claims;
- bounded follow-up/correction queries.

No unpublished candidate proof text was pasted into search queries. Search output was used as a lead; mathematical attributions above rest on opened primary texts.

Several narrowly phrased queries returned unrelated general-majorization results. Identifier/correction searches were **not a reliable exhaustive citation graph**. Their failure to locate a correction is not evidence that no correction exists.

### Primary-source coverage register

| Source | Version actually inspected | Coverage and limits |
|---|---|---|
| Song–Wang–Tomamichel–Fang | 2609.37240v1 | Complete reader body, §§1–5, references, Appendix A, ending; current raw abstract history lists v1 |
| Song–Chen | 2603.25410v1 | Complete HTML and five-page PDF; Proposition 3 and proof, including PDF Equation (35); current raw history lists v1 |
| Alhejji–Knill | 2307.06894v3 | Introduction/definitions, channel expansion, relevant small-system and two-summand passages; not a complete-paper proof audit |
| Alhejji | 2410.18254v3 | Theorem 1.3, §4.3 Proposition 4.4/proof, relevant §5 limits |
| Alhejji journal article | DOI 10.1007/s00023-025-01592-w | Open-access metadata, Theorem 1.3, Proposition 4.4/proof; no source-wide identity assertion |
| Alhejji–Kelson-Packer | 2607.07913v1 | Complete returned article and references |
| King | quant-ph/0204172v1 | Channel definitions/range and §1 theorem statements, especially Theorem 3; full proof not audited |
| Rungta et al. | quant-ph/0102040v2 | Introduction, §II.1, relevant §II.2 inversion formulas; partial paper |
| Loring | 1306.1923v1 | §1 projection/antiunitary results and surrounding material; partial paper |
| Eltschka et al. | 1807.09165v1 | Inversion identities, odd-party property statement, compatibility discussion; appendices not fully read |
| Amosov | 2103.08515v6 | §§5–6 claims/proofs/iteration and qubit example; journal full text unavailable |
| Amosov | 2401.05104v1 | Complete returned manuscript body and ending |
| Amosov publisher record | DOI 10.1007/s11128-022-03431-x | Metadata, abstract and subscription preview; mathematical full text not accessed |

Except for the current histories explicitly inspected above, pinned historical versions are not presented as exhaustive latest-version certificates. Authors’ complete publication lists, all theses/non-English literature, exhaustive forward citations, and every equivalent formulation were not screened.

## 12. Recommended qualified wording

> We have an unaccepted candidate proof of exact output majorization for arbitrary complex three-qubit inputs throughout the physical qubit depolarizing interval, together with its stated four-qubit \(1|3\)-separable convex-hull consequence. Its proposed paired-projection argument still requires disjoint mathematical review.
>
> A bounded primary-source audit located an exact antecedent for the central two-body marginal-sum conclusion: Song and Chen, arXiv:2603.25410v1, Proposition 3, prove a stronger nonnegative weighted compatible-marginal majorization statement. The \(H_2\) theorem itself is therefore not new. Whether the present channel theorem should be described as a corollary of that antecedent, and whether the paired-projection derivation adds an original proof method, remain explicit comparison obligations.
>
> Song–Wang–Tomamichel–Fang’s shifted-log-determinant and asymptotic approximate-majorization theorems do not themselves supply exact fixed-three-use all-prefix majorization. Their general conjectural formulation is not evidence of novelty for every small-system specialization.
>
> Older Amosov manuscripts print stronger tensor-majorization claims whose formal scope encompasses the target. Identified obstructions concern their displayed proof steps, not theorem-statement counterexamples; no equivalence with uninspected subscription-journal mathematics is asserted. No first-proof, novelty, unrestricted four-qubit closure, or independent-family/human/kernel verification claim is made.

## 13. Findings, verdict scope, and unpaid obligations

**Candidate mathematical proof findings:** **NOT ASSESSED** by this role. No FATAL/MAJOR/MINOR proof clearance is issued.

**Patch-anchored source-attribution findings:** none identified against the candidate’s existing cautious Section 11 wording. It makes no first-result claim and expressly leaves priority unpaid. The newly found Proposition 3 is a substantive addition required for future attribution and significance assessment, not evidence that an existing novelty claim is false.

The remaining obligations are precisely:

1. Disjointly reconstruct the candidate’s paired-projection argument and its all-prefix use; this source audit supplies no proof credit.
2. Compare the full three-use channel conclusion with Song–Chen Proposition 3 plus the known channel-marginal framework, rather than treating the \(H_2\) theorem as new.
3. Assess proof-method originality separately from theorem-statement overlap.
4. Preserve the older ancillary/tensorization qualifications; neither adopt nor refute their full statements from proof-step objections alone.
5. Keep every four-qubit report within its actually admitted state class and parameter scope.

**Overall correctness: correct — restricted to the frozen candidate’s existing cautious public-source attribution, not its mathematical theorems.**

**Explanation:** The required 2026 source supports the distinction between exact log-determinant ordering, approximate majorization, and exact all-prefix majorization. The newly located compatible-marginal Proposition 3 establishes direct prior \(H_2\) statement overlap and prevents novelty clearance, while leaving the candidate’s proof and any parent adoption entirely unadjudicated.

**Confidence: 0.98** for the identified source statements, hypothesis match, and attribution boundaries. No numerical confidence is assigned to the unreviewed candidate proof, exhaustive priority, or the soundness of the qualified older tensorization chains.