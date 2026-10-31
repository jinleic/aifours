# Bounded public-source overlap audit: symmetric W4 depolarizing majorization

**Status: PUBLIC-SOURCE AUDIT RETURN — UNREVIEWED UNTIL PARENT DISPOSITION.**

**Bottom line:** Song–Wang–Tomamichel–Fang, arXiv:2609.37240v1, does **not** establish the candidate’s exact four-use W4 majorization theorem. It conjectures unrestricted exact majorization, proves exact shifted-log-determinant ordering, and derives approximate majorization for sufficiently large blocklength. However, this audit also located **older, explicitly stronger tensor-product majorization claims in Amosov’s 2022 and 2024 papers**. At the level of their printed quantifiers, the 2022 claim encompasses the W4 statement throughout the physical qubit parameter interval. Its soundness and the relationship between the accessible manuscript and the subscription journal version are not certified here.

**Disposition recommended:** **STRONGER PRIOR CLAIM FOUND; ESTABLISHED-OVERLAP / PRIORITY INCONCLUSIVE.** Do not describe the W4 result as first, novel, or absent from prior literature. Equally, do not replace its independent proof gates with an unexamined citation to the older tensorization claims.

This is the complete materializable body for the assigned `author-candidate-v1.md`. No working-tree file was written under the read-only role.

## 1. Assignment, controls, and actual read frontier

### Frozen identity

All following hashes, lengths, and clocks are **parent-supplied metadata**, not independently computed child observations:

| Record | Parent-supplied SHA-256 | LF |
|---|---|---:|
| Manifest | `3d505ed081899405761fc5cdf6c11fe7b53a30feb5b1658b49c63342b977ff05` | 86 |
| Freeze receipt | `ec95bbd9091954df3e1133bd12eeaa27397839246127bf6adcef619f45b9bb3f` | 47 |
| Literal packet | `bdb1e59472814cc1db59092ea772f12682cd1a01fda6ba60595de9a0341f286b` | 151 |
| S1: parent W4 candidate | `8802cec012ddeac98128311040f5a14fb3067dc17eb8833d9f34deca15894b12` | 101 |
| S2: earlier Class A/B disposition | `8522551e1088a796288c73c9b1aad8fa40e197d74b6f7d41447392d07370d6c0` | 48 |

The complete manifest, receipt, and these seven status/permission controls were read before the scientific packet:

- `prospective-author-method-scope-restoration-20261030-v1.json`, LF 1–15.
- `contract-addendum-2-frontier-first-owner-direction-v1.json`, LF 1–14.
- `parent-L1-selected-diagnostic-release-quarantine-v1.json`, LF 1–23.
- `parent-privacy-auxiliary-parameter-diagnostic-quarantine-v1.json`, LF 1–11.
- `parent-core-gram-auxiliary-operator-diagnostic-quarantine-v1.json`, LF 1–9.
- `parent-ame-held-compression-claim-consumer-quarantine-v1.json`, LF 1–8.
- `parent-held-ph-registration-report-consumer-quarantine-v1.json`, LF 1–49.

The complete parent dispatch receipt and live-metadata supply were also read. Then the literal packet was read **in order, LF 1–151, including both source endings**, in raw windows of at most 20 lines. S1 LF 1–101 and S2 LF 1–48 were therefore actually displayed, not inferred from their receipts.

### Method separation

- This return performs public literature attribution and hypothesis comparison, **not** the disjoint written-proof or finite-check assignment.
- No linked parent scientific code, parent calculation output, sibling return, or held scientific payload was opened.
- Held L1/CORE/PH/AME material and its consumers remained NONINPUT; the quarantine documents were status-only inputs.
- No scientific program, calculator, CAS, author code, numerical experiment, or new selected-state probe was run.
- The symbolic parameter identification below compares a public theorem’s hypotheses with the specified channel; it is not a reconstruction of the candidate’s W4 spectrum or Bernstein certificate.
- No external-model CLI, installation, paid/heavy job, deletion, commit, push, publication, or infrastructure mutation occurred.
- No child-native clock or hash command was executed. No independently observed completion time or elapsed duration is asserted.

## 2. Exact object being compared

The frozen candidate concerns

\[
|W_4\rangle=\frac{|1000\rangle+|0100\rangle+|0010\rangle+|0001\rangle}{2},
\qquad
\Phi_p(X)=(1-p)X+\frac p2\operatorname{Tr}(X)I_2,
\]

for **every** \(0\le p\le4/3\). With \(t=|1-p|\), \(a=(1+t)/2\), \(b=(1-t)/2\), it claims

\[
\lambda\!\left(\Phi_p^{\otimes4}(|W_4\rangle\langle W_4|)\right)
\prec
\lambda\!\left(\operatorname{diag}(a,b)^{\otimes4}\right).
\]

Equivalently, every rank-\(k\) complex orthogonal projector satisfies the reference Ky Fan bound for \(k=1,\ldots,16\). The candidate additionally claims the local-unitary-orbit convex-hull extension and its union by convex mixing with the earlier Class A/B hull.

The comparison must retain all these distinctions:

- exact versus approximate prefix inequalities;
- four uses versus sufficiently large blocklength;
- every physical \(p\), including \(p>1\);
- output eigenvalue majorization versus entropy or Schatten-norm optimization;
- equal-amplitude W4 versus arbitrary unequal-amplitude W states;
- the candidate’s restricted state class versus unrestricted inputs.

The asserted separation of W4 from the earlier local Class A/B hull is **not adjudicated by this source audit**.

## 3. Required primary source: Song–Wang–Tomamichel–Fang

**Source:** Zhiwei Song, Xin Wang, Marco Tomamichel, Kun Fang, *Approximate majorization and high-order capacity of quantum depolarizing channels*, [arXiv:2609.37240v1](https://arxiv.org/html/2609.37240v1).

**Version/status actually observed:** The versioned article identifies v1, 29 September 2026. The unversioned HTML also resolved to v1. The [current abstract page](https://arxiv.org/abs/2609.37240), inspected as raw HTML, listed only the v1 submission in its submission history. Its inspected metadata did not establish a separate journal publication.

**Read scope:** §§1–3, §5, and Appendix A were inspected, including the complete relevant theorem statements, the §3 derivations, and Appendix A’s ending. The entire §4 capacity proof was not read. Retained reader rendering: `artifact://67005`, particularly LF 1–500 and 604–843.

### 3.1 Exact unrestricted majorization is a conjecture

In §1, Eq. (1) defines the same depolarizing convention and full physical interval

\[
0\le p\le p_{\max}(d)=\frac{d^2}{d^2-1}.
\]

Thus \(d=2\) gives the candidate’s \(p\in[0,4/3]\).

The authors introduce Eq. (2) with the words:

> “We conjecture that the output corresponding to a pure product input majorizes the output corresponding to any other input.”

That equation quantifies over arbitrary, possibly entangled inputs and arbitrary \(n\). Section 5 again identifies establishing Eq. (2) in general as an open direction.

**Comparison:** Eq. (2), if proved, would subsume the candidate, but the paper does not present it as a theorem. Its general conjectural status does not establish that every restricted W4 case is new or previously open.

Primary location: [§1, Eqs. (1)–(2)](https://arxiv.org/html/2609.37240v1#S1), and [§5](https://arxiv.org/html/2609.37240v1#S5).

### 3.2 The shifted-log-determinant theorem is exact, but different

Theorem 4, §3.1, Eq. (20), states that for every \(n\ge1\), every input state, every positive shift \(s\), and \(0<p\le p_{\max}(d)\),

\[
\ln\det\!\left(sI+\mathcal D_{p,d}^{\otimes n}(\rho)\right)
\ge
\ln\det\!\left(sI+\mathcal D_{p,d}^{\otimes n}(|0^n\rangle\langle0^n|)\right).
\]

This is an **exact all-\(n\) functional ordering**, including \(n=4\) and the physical negative-Bloch branch. It is not the collection of all Ky Fan prefix inequalities.

The paper itself calls the log-determinant ordering a necessary condition for its full-majorization conjecture. Remark 5 and Appendix A.1 distinguish its consequences from stronger spectral conclusions.

**Comparison:** The candidate’s all-prefix conclusion is not obtained merely by specializing Theorem 4 to W4.

Primary location: [§3.1, Theorem 4 and Remark 5](https://arxiv.org/html/2609.37240v1#S3.SS1).

### 3.3 Approximate majorization does not establish the fixed four-use theorem

Theorem 1 and Corollary 8 bound the defect by

\[
\delta_{\rm maj}\le
\frac{\kappa_{d,p}}{\sqrt n}\bigl(\log\log n+6\bigr)
\]

for fixed nondegenerate channel parameters and **all sufficiently large \(n\)**, uniformly over input states. Their stated channel range is \(0<p\le p_{\max}(d)\), \(p\ne1\).

Section 3.2 supplies the bridge:

- Proposition 6 bounds a nonzero possible defect using reference spectral anti-concentration.
- Theorem 7 applies to an i.i.d. reference with positive spectral-information variance.
- Corollary 8 specializes it to depolarizing outputs.

**Comparison:** Neither the eventual-blocklength quantifier nor a vanishing asymptotic upper bound establishes zero defect at \(n=4\). These statements also do not supply the candidate’s complete all-parameter, all-16-prefix certificate.

Primary location: [§3.2, Proposition 6, Theorem 7, Corollary 8](https://arxiv.org/html/2609.37240v1#S3.SS2).

### 3.4 The explicit log-determinant counterexample is not a channel counterexample

Appendix A explicitly says its counterexamples concern arbitrary states **not assumed to arise as channel outputs**.

Appendix A.1, Eqs. (75)–(77), gives

\[
X=\operatorname{diag}(42/100,29/100,29/100),\quad
Y=\operatorname{diag}(40/100,35/100,25/100),
\]

and records

\[
\det(sI+X)-\det(sI+Y)
=\frac{s}{5000}+\frac{161}{500000}>0.
\]

Nevertheless the largest eigenvalue of \(X\) exceeds that of \(Y\), and the paper records the reversed \(q=3\) norm comparison. Section 3.2 explicitly identifies the constant-sequence majorization defect from this example as \(1/50\).

This establishes the paper’s stated logical limitation: **shifted-log-determinant ordering alone does not imply exact majorization for arbitrary states**.

It does **not** refute depolarizing-output majorization, the W4 theorem, or any physical-input case.

Appendix A.2 separately constructs full-rank states obeying all of the indicated Schatten-norm bounds relative to the product reference while their defect tends to \(1/2\). Those states likewise are not asserted to be actual channel outputs. Its \(W_n\) notation does **not** denote physical W states.

Primary location: [Appendix A.1–A.2](https://arxiv.org/html/2609.37240v1#A1).

## 4. Stronger older prior claim: Amosov 2022

**Source:** G. G. Amosov, *On capacity of quantum channels generated by irreducible projective unitary representations of finite groups*, [arXiv:2103.08515v6](https://arxiv.org/html/2103.08515v6).

**Observed publication metadata:** The [publisher’s page](https://link.springer.com/article/10.1007/s11128-022-03431-x) identifies *Quantum Information Processing* **21**, article 81, published 3 February 2022. The publisher served a subscription preview, not the mathematical full text. The accessible manuscript’s v6 header is dated 3 February 2022; the unversioned arXiv HTML resolved to v6.

**Read scope:** §§5–6, including the tensorization statements and their proofs, §7 Example 1 on qubit channels, and §8/references. The relevant PDF pages were also inspected to confirm the tensorization statements were not merely an HTML conversion invention. Reader records: `artifact://67031`, LF 198–440, 458–495, 599–662; PDF `artifact://67034`, especially pages 6–12.

### 4.1 What is actually claimed

Section 5 defines coset marginals

\[
p_{[g]}=\sum_{t\in T}\pi_{gt},
\]

orders them, and imposes Eq. (16):

\[
j>k\ \Longrightarrow\ \pi_{g_jt}\le\pi_{g_ks}
\quad\text{for all }s,t\in T.
\]

Section 6 Proposition 2 asserts single-use output majorization by this marginal vector.

More importantly:

- Proposition 4 claims an ancillary identity-channel extension of an output majorization bound.
- Proposition 5 claims product-reference majorization for tensor products.
- The proof of the main theorem explicitly iterates Proposition 5 to arbitrary \(N\), writing output majorization by the sorted products of the marginal probabilities.

Thus this is **not merely an entropy theorem found by a loose keyword search**. An exact tensor-product eigenvalue-majorization claim appears in the proof body.

Section 7 Example 1 explicitly treats Pauli/qubit channels and gives the familiar reference probabilities through \(\lambda_{\max}=\max(|\lambda_x|,|\lambda_y|,|\lambda_z|)\).

### 4.2 Written hypothesis comparison with the specified channel

The public Pauli-channel formulas give depolarizing weights

\[
u=1-\frac{3p}{4},\qquad v=\frac p4,
\]

with weights \(u\) for \(I\) and \(v\) for each of \(X,Y,Z\). These are nonnegative on the entire physical interval. The formulas are also directly represented by the depolarizing Kraus operators in Ozaydin’s Eq. (7), discussed below.

Use the projective Pauli representation of \(G=\mathbb Z_2\times\mathbb Z_2\) and the subgroup corresponding to \(\{I,Z\}\). Its two cosets have weights

\[
\{I,Z\}:(u,v),\qquad \{X,Y\}:(v,v).
\]

The public hypothesis comparison is:

| Parameter interval | Descending coset order | Ordered marginal vector | Cross-coset condition |
|---|---|---|---|
| \(0\le p\le1\) | \(\{I,Z\}\), then \(\{X,Y\}\) | \((1-p/2,\ p/2)\) | Every later weight \(v\) is at most each earlier weight \(u,v\) |
| \(1\le p\le4/3\) | \(\{X,Y\}\), then \(\{I,Z\}\) | \((p/2,\ 1-p/2)\) | Every later weight \(u,v\) is at most each earlier weight \(v\) |

In both branches the ordered marginal vector is exactly \((a,b)\) from the assignment.

**[INFERENCE — source-hypothesis matching, not a certification of the cited proof.]** Taking the manuscript’s Proposition 5 and its stated iteration at face value therefore yields the same product reference for **arbitrary inputs and arbitrary numbers of uses**. It would encompass both three- and four-use majorization, including the W4 candidate and its convex-hull extension, for all physical \(p\).

**Priority consequence:** A “no earlier equivalent located” conclusion would be inaccurate for this audit. A substantially stronger **earlier printed claim** has been located and its channel hypotheses have been matched explicitly.

### 4.3 Why this is not an adoption of unrestricted majorization

This source audit does not certify the ancillary-extension and tensorization arguments. In particular, the proof of Proposition 4 contains a load-bearing assertion about the dimension and irreducibility of the span generated by \((I\otimes U_g)f\). Its use in Proposition 5 is a separate mathematical obligation, not something established by publication metadata.

The 2026 paper’s continued conjectural treatment of unrestricted depolarizing majorization creates an important literature tension. That tension is **not** resolved by assuming either that the older argument is valid or that the newer authors necessarily missed a valid theorem.

Accordingly:

- **Older, stronger claim:** verified present in the accessible primary manuscript.
- **Formal scope overlap:** explicitly identified above.
- **Soundness of the older tensorization proof:** not certified.
- **Equality of the subscription journal’s mathematical text to the inspected v6 body:** not verified.
- **Conclusion that unrestricted majorization is already established:** not issued.

## 5. Further primary-source checks

### 5.1 Amosov 2024: another explicit tensor-majorization claim, with textual qualifications

**Source:** [arXiv:2401.05104v1](https://arxiv.org/html/2401.05104v1), *On characteristics of mixed unitary channels being additive or multiplicative with respect to taking tensor products*, 10 January 2024.

**Read scope:** Complete HTML body and ending, with PDF cross-check of the relevant statements. Reader records: `artifact://67022`, LF 1–457; PDF `artifact://67030`, LF 1–305.

Section III defines channel majorization through projector sums. Proposition 1 asserts a composition rule. Section IV Theorem 2 and Eq. (17) explicitly claim

\[
\bigotimes_j\Phi_j
\prec P^{(1)}\star\cdots\star P^{(M)}.
\]

This is a genuine stronger-prior lead, not just a capacity-title match.

Two printed-text qualifications prevent silently treating it as a ready-made theorem import:

1. Its Eq. (8), written with \(p_{[U]}\le p_{[V]}\), does not state the same distinct-index restriction as the 2022 paper’s \(j>k\) condition. This audit does not silently amend it.
2. Theorems 1 and 2 print an **infimum** for arbitrary convex \(F\), while their proofs display upper-bound inequalities for the corresponding convex spectral functional.

These observations concern the text actually inspected. They are not a new counterexample or a complete proof-refutation. **Classification: stronger prior claim requiring mathematical adjudication; not independently established overlap.**

### 5.2 King: established norm/entropy prior, not the all-prefix theorem

**Source:** Christopher King, [*The capacity of the quantum depolarizing channel*, quant-ph/0204172v1](https://arxiv.org/html/quant-ph/0204172v1), 30 April 2002 manuscript; cited in the inspected literature as IEEE TIT **49**, 221–229 (2003).

**Read scope:** §1, especially §§1.2 and 1.6/Theorem 3, and §2.2/Lemmas 7–9. Reader `artifact://67018`, particularly LF 80–96, 307–375, 448–499.

Theorem 3 proves maximal-output Schatten-norm multiplicativity for a depolarizing channel tensored with an arbitrary auxiliary channel, and derives minimum-output-entropy additivity. Its parameter interval includes the full completely positive range in the \(\lambda=1-p\) convention.

**Classification:** substantial, broader-input prior for norm and entropy optimization. The inspected theorem and phase-damping bound do not state the candidate’s complete Ky Fan-prefix ordering. Do not rename the norm theorem “full majorization.”

### 5.3 Amosov 2020: grouped-weight majorization is not automatically the product-output reference

**Source:** [*On classical capacity of Weyl channels*, arXiv:2006.05855v3](https://arxiv.org/html/2006.05855v3), 31 October 2020.

**Read scope:** Complete body and ending, reader `artifact://67029`, LF 1–489.

Section 3 Proposition 2 gives a majorization bound obtained by sorting the channel’s mixing weights and summing them in groups. Section 4 then treats a specified deformation of q-c Weyl channels and states an entropy tensorization result.

**Classification:** relevant prior mechanism. The sorted/grouped global mixing-weight vector must not be silently identified with tensor powers of the single-use product-output spectrum. The exact tensorization statements in the 2022/2024 successors, rather than the 2020 title alone, are the significant overlap concern.

### 5.4 Siudzińska: explicit warning that the relevant capacity bound need not tensorize

**Source:** Katarzyna Siudzińska, [*Classical capacity of the generalized Pauli channels*, arXiv:1908.03917v1](https://arxiv.org/html/1908.03917), 11 August 2019 manuscript; the searched journal record is J. Phys. A **53**, 445301 (2020), [DOI 10.1088/1751-8121/abb276](https://iopscience.iop.org/article/10.1088/1751-8121/abb276).

**Read scope:** Pauli definitions, capacity-bound statements, and the classical-capacity section through its Pauli example and consequences; reader `artifact://67038`, LF 1–354. The publisher route returned a CAPTCHA; no bypass was attempted. The inspected manuscript is explicitly v1, not an asserted byte-equivalent copy of the journal article.

Example 1, Eqs. (37)–(40), records that the specified upper-bound construction is not weakly additive under tensoring.

**Classification:** a relevant caution against substituting single-use/grouped-weight bounds for the desired tensor product reference. It is **not** a counterexample to the W4 theorem or to depolarizing-output majorization.

### 5.5 Ozaydin: noisy W spectra predate the candidate, but the displayed calculation is W3/QFI

**Source:** Fatih Ozaydin, [*Quantum Fisher Information of W States in Decoherence Channels*, arXiv:1403.2376](https://ar5iv.labs.arxiv.org/html/1403.2376).

**Version/date caution:** The [arXiv record](https://arxiv.org/abs/1403.2376) dates the submission to 10 March 2014. The regenerated HTML title-page date is not used as the publication date.

**Read scope:** Complete returned article, including §I “Depolarizing channel” and its ending.

The article explicitly subjects each particle to the same local noise. Equation (7) gives the depolarizing Kraus operators in the same \(p\) convention. Section I prints the eight eigenvalues for a noisy **three-particle W state** and studies quantum Fisher information.

**Classification:** actual prior overlap in studying local-depolarized W-state spectra. It does not state all-prefix comparison with the pure-product output, does not display the candidate’s W4 spectrum, and does not certify the all-physical-\(p\) W4 theorem. Claims that noisy W-state spectral analysis itself is new would require qualification.

### 5.6 Zhang: majorization-preserving channels are a different property

**Source:** Lin Zhang, [*Majorization-preserving quantum channels*, arXiv:1209.5233v2](https://arxiv.org/html/1209.5233v2), 15 December 2012.

**Read scope:** Definitions, §3 Theorem 3.1, and the relevant §4 discussion; reader `artifact://67017`, LF 1–410.

The theorem classifies channels preserving an existing input majorization relation. Its depolarizing forms concern a channel on the specified whole Hilbert space.

**Classification:** not a tensor-product depolarizing-output theorem. It does not permit replacing four local qubit channels by one global 16-dimensional depolarizing map.

### 5.7 Song–Zong–Yang 2026: three-qubit entanglement ordering is not output majorization

**Source:** Wei Song, Xiao-Lan Zong, Ming Yang, [*Kempe-Invariant Ordering of Three-Qubit Pairwise Entanglement under Local Depolarization*, arXiv:2608.29707v3](https://arxiv.org/html/2608.29707), 20 September 2026 version.

**Read scope:** §§I–III and the §IV main theorem statement and relevant proof passage; reader `artifact://67024`, LF 1–349.

Theorem 1 orders **pairwise concurrence trajectories** for pure three-qubit states with fixed initial entanglement coordinates. Its local parameter is \(0\le\eta\le1\).

**Classification:** different functional, different state comparison, and a different parameter scope. It is not a stronger three-use output-majorization theorem.

## 6. Bounded search coverage and limitations

Eighteen bounded text-search queries were issued. They covered:

- depolarizing output majorization with W/four-qubit/few-use terminology;
- “majorization conjecture,” “majorizes,” and tensor/copy terminology;
- noisy W-state spectra;
- King and Amosov leads;
- the exact titles of the Weyl/group-channel antecedents;
- the generalized-Pauli capacity paper;
- identifier-based follow-up/correction searches for the stronger claims.

Search results were used only as leads. Mathematical attributions above rest on opened primary texts.

Several narrowly phrased searches returned unrelated dictionary, general-majorization, or legislative results. In particular, the identifier-based follow-up/correction searches were **not a reliable exhaustive citation search**. Their failure to return an erratum is not evidence that no erratum, criticism, or later clarification exists.

This audit did **not** exhaust:

- citation graphs or all forward citations;
- authors’ complete publication lists, theses, proceedings, or non-English literature;
- all W/Dicke-state decoherence papers;
- every possible parameter-restricted few-use result;
- the inaccessible full journal text behind the publisher preview;
- later text not represented by the inspected public versions.

No public preprint expressly presenting the candidate’s particular W4/Johnson-block/Bernstein-table proof was located in the inspected set. That is a **bounded observation, not a novelty conclusion**.

## 7. Conclusions by claim

| Claim | Public-source assessment |
|---|---|
| The 2026 required paper proves unrestricted exact majorization | **Incorrect attribution.** Its Eq. (2) is conjectural. |
| Its shifted-log-determinant theorem proves exact W4 majorization by specialization alone | **Not supported.** The functional ordering is different; the paper explicitly explains the logical limitation. |
| Its approximate theorem settles \(n=4\) with zero defect | **Not supported.** The result is asymptotic and approximate. |
| Its Appendix A counterexample disproves physical W4 majorization | **Not supported.** The counterexamples are not asserted to be channel outputs. |
| No earlier stronger exact majorization claim exists in the checked literature | **Contradicted by the inspected 2022/2024 manuscripts.** |
| Amosov 2022’s printed tensor claim formally encompasses this candidate | **Yes, at the hypothesis/quantifier level**, with the full-\(p\) identification in §4.2. |
| That older claim can now be adopted as a verified proof | **Not certified by this audit.** |
| The W4 candidate is false because of the literature tension | **No such conclusion.** |
| The candidate is novel or first | **Not established; priority remains inconclusive.** |
| This audit settles arbitrary-amplitude W states or the unrestricted original target | **No.** |

The frozen S1 already labels source/priority comparison unpaid and makes no novelty claim. Consequently, the additional older-prior evidence does not by itself identify a false novelty statement in S1. It does materially constrain any later significance or priority wording.

## 8. Proof, experiments, findings, and assurance ceiling

- **Candidate proof:** NOT REVIEWED by this role.
- **Independent finite physical checker:** NOT RUN and not read.
- **Candidate proof FATAL / MAJOR / MINOR counts:** NOT ASSESSED.
- **Public-source attribution defects in the frozen candidate’s existing caveat:** **0 FATAL / 0 MAJOR / 0 MINOR identified.** This is not a proof clearance.
- **Priority issue:** one substantive unresolved stronger-prior chain, identified and scoped above.
- **Scientific calculations/code/argv/results:** none; no experiment was performed.
- **Parent acceptance:** not granted.
- **Formal/kernel, human, independent-model-family, publication-priority, or exhaustive novelty assurance:** none.

### Precise remaining obligations

Before mathematical adoption, the separately assigned checks must establish the actual physical spectrum, all prefix certificates, degeneracies/endpoints, negative branch, local-unitary/convex extension, and state-class separation. This source return supplies none of that proof credit.

Before a novelty or “already established” claim, the older tensorization chain must receive explicit mathematical adjudication and, where relevant, comparison with the published text. The key publicly identified import boundaries are Amosov 2022 §6 Propositions 4–5 and their iteration, and Amosov 2024 §III Proposition 1 / §IV Eq. (17). This does not require holding otherwise valid, independently checked W4 mathematics hostage to a priority claim.

**Recommended report wording:**

> We have a parent-authored candidate exact all-prefix majorization certificate for the equal-amplitude four-qubit W state, with the stated local-unitary convex-hull extension, pending independent mathematical disposition. Song–Wang–Tomamichel–Fang’s general shifted-log-determinant and asymptotic approximate-majorization results do not themselves establish this fixed-use exact certificate. A bounded primary-source audit also found older, stronger tensor-majorization claims whose formal scope encompasses the candidate; their mathematical status has not been certified here. No novelty, first-proof, or unrestricted-target-closure claim is made.

**Overall correctness:** correct **only for the frozen candidate’s existing cautious public-source attribution**, not a verdict on its theorem.

**Explanation:** The required 2026 source supports the candidate’s distinction between exact log-determinant ordering, approximate majorization, and exact all-prefix majorization. The additional older tensorization claims prevent priority clearance but do not contradict a novelty claim in S1, because S1 makes none and expressly leaves that gate unpaid.

**Confidence:** 0.96 for the source-content distinctions and presence of the stronger printed claims; no numerical confidence is assigned to the unreviewed W4 proof or the soundness of those older tensorization arguments.