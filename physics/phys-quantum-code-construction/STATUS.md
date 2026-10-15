# Status and state of the art

Snapshot: **2026-10-14, America/Los_Angeles**. This is a focused public-source review, not an exhaustive priority search. Primary sources support every substantive status statement below. A table gap is reported as a **table gap**, not proof that no recent paper has resolved it. Preprint claims and locally replayed certificates are distinct.

## 1. The four questions in the book

| Book question | What is settled / representative frontier results | What remains open |
|---|---|---|
| Better finite binary codes | Stabilizer/CSS constructions, graph/CWS codes, LP and shadow bounds are established. Panteleev–Kalachev [P1] settled the existence of asymptotically good qLDPC families: both rate and relative distance stay positive. This major post-2009 theorem does not determine individual small-code parameters. The 2025 SDP hierarchy [P2] is complete at all levels, not necessarily tractable at the level needed. The 2026 rational-certificate paper [P3] strengthens 18 finite-code upper bounds for lengths 6–19 and removes floating-point uncertainty from those certificates. | Exact finite maxima and many achievable trade-offs remain undetermined. A complete hierarchy does not mean its first practical relaxation settles every entry. |
| Good decoding algorithms | Dinur–Hsieh–Lin–Vidick [P4] construct good qLDPC codes with linear-time decoders. Sparse Blossom [P5] reports, at 0.1% circuit-level depolarizing noise, processing both bases of distance-17 surface-code syndrome data in under one microsecond per round on a single core. A September 2026 preprint [P6] claims explicit capacity-approaching qLDPC **list** decoding in near-linear time. | There is no single noise-model-independent “best decoder.” Finite-length latency, circuit noise, measurement errors, degeneracy, accuracy, hardware connectivity, and unique versus list decoding must be matched. We did not benchmark or reproduce these decoders. [P6] is a preprint result, not a claim that arbitrary physical errors can be uniquely corrected near the Singleton radius. |
| Nonbinary quantum codes | Ketkar et al. [P7] establish the finite-field stabilizer framework and multiple code families. Hermitian self-orthogonal generalized Reed–Solomon and related constructions continue to extend q-ary quantum MDS parameter families; He et al. [P8] give a 2025 example for specified lengths. Grassl maintains separate physical-q tables [T]. | The existence spectrum is not classified, even at small q. The ternary entries below retain distance gaps. Particular MDS families do not settle every q or length. |
| Nonadditive codes | Cross et al. [P9] develop CWS codes; Yu–Chen–Oh [P10] give two infinite one-error-correcting families with code-space dimension 50% above the optimal stabilizer dimension at their parameters. Chuang et al. [P11] prove that every dimension-three CWS code extends to a dimension-four stabilizer code, excluding the seven-qubit CWS instance. General-code rational SDP bounds [P3] apply beyond stabilizers. | The unrestricted `((7,3,3))_2` question remains explicitly unresolved in [P12] and retains a 2–3 gap in the 2026 primary table [P3]. The same table leaves `((11,5,4))_2` and several other existence questions unresolved. |

**Stronger prior art found during the final check:** Rigby–Olivier–Jarvis [P14, §III.C] report an exhaustive search over LC-inequivalent graph states for n=11,d=4: 3,060 graph classes yield K=4 and none yields a larger code. Thus the eleven-qubit target is already excluded throughout **CWS**, including non-vertex-transitive frames. Our 32-frame result is only a restricted reproduction of that stronger published exclusion. This source also reports CWS exclusions for K=25,26 at n=7,d=2 (§III.A) and K=13 at n=9,d=3 (§III.B). These statements do not close the unrestricted general-code gaps.

**Notation:** `[[n,k,d]]_q` has dimension `K=q^k`; `((n,K,d))_q` gives the dimension itself. Grassl's URL parameter is the **squared** physical alphabet: `q=4` means physical qubits, `q=9` qutrits, and `q=16` four-level systems. Search summaries which call a `q=16` entry “binary” are incorrect.

The supplied book excerpt is retained unedited. We use the projector/Knill–Laflamme definition rather than propagate extraction defects in its displayed formulas. The familiar pure-code qubit Hamming counting bound contains `3^j binomial(n,j)`; its ordinary packing derivation must not silently be imposed on arbitrary degenerate codes.

## 2. Concrete instances considered

### Primary general-code table, not stabilizer-only bounds

The following are entries of [P3, Table 1]. Here `K_max(n,d)` maximizes dimension over **all** qubit subspace codes of distance at least d.

| n, d | Primary-source interval | First unresolved existence question | Decision |
|---|---:|---|---|
| 7, 3 | 2–3 | `((7,3,3))_2` | Initial target; known CWS obstruction and numerical history make “not too hard” unjustified. Exact barriers reproduced, not an open-problem solution. |
| 7, 2 | 24–26 | `((7,25,2))_2` | Screened; [P14, §III.A] already excludes K=25,26 within CWS. No local computation claimed. |
| 9, 3 | 12–13 | `((9,13,3))_2` | Screened; [P14, §III.B] already excludes K=13 within CWS. No local computation claimed. |
| 11, 4 | 4–7 | `((11,5,4))_2` | A 32-frame exact assay was performed, but final primary-source checking found that [P14, §III.C] already excludes every CWS frame. Restricted reproduction only; global interval unchanged. |

The 2026 source explicitly presents lower/upper gaps, rather than a statement inferred solely from an unsuccessful search. The earlier VarQEC primary paper [P12] explicitly describes numerical evidence against the seven-qubit code, not a proof. Current NumQI implementation documentation also calls it open, but this secondary/program-documentation source is not the basis of the status claim: <https://numqi.github.io/numqi/application/qecc/qecc733/>.

### Live stabilizer-table entries

Fetched individually on the snapshot date. These are candidate **table gaps only**; not all are approved open research targets.

| Physical alphabet | Entry | Live distance interval | Primary live URL / caution |
|---|---|---:|---|
| 2 | `[[17,3,d]]_2` | 5–6 | <https://www.codetables.de/QECC/QECC.php?q=4&n=17&k=3> |
| 2 | `[[18,3,d]]_2` | 5–6 | <https://www.codetables.de/QECC/QECC.php?q=4&n=18&k=3> |
| 3 | `[[11,2,d]]_3` | 4–5 | <https://www.codetables.de/QECC/QECC.php?q=9&n=11&k=2> |
| 3 | `[[11,3,d]]_3` | 4–5 | <https://www.codetables.de/QECC/QECC.php?q=9&n=11&k=3>; d=5 would meet Singleton. |
| 2 | `[[14,3,d]]_2` | 4–5 | <https://www.codetables.de/QECC/QECC.php?q=4&n=14&k=3>; **not selected as confidently open**, because of the subsequent primary preprint below. |

The live pages carry a June 2024 page date, and several lower-bound constructions are dated 2005 or 2008. Fetching them live does not make their coverage complete to October 2026.

**Important rejected candidate:** Mansehej Singh, *The Optimal Distance of Fourteen-Qubit Stabilizer Codes Encoding Three Qubits*, Zenodo preprint v1.0, 10 August 2026, DOI [10.5281/zenodo.21874338](https://doi.org/10.5281/zenodo.21874338), claims nonexistence of `[[14,3,5]]_2`, including degenerate codes, and a Lean formalization. Its primary metadata was accessible at <https://zenodo.org/api/records/21874337> (redirected to record 21874338); the HTML landing pages returned HTTP 403. This project did **not** replay or audit that formalization. It records a primary unreviewed-preprint claim, neither a locally certified resolution nor an unqualified open problem. An earlier August 5 note by Daniel Kirtchakov only proves automorphism restrictions and explicitly leaves existence open: <https://github.com/05oz/certify/blob/main/qec1435-paper/note.md>. These different scopes and dates must not be conflated.

## 3. Target selection and difficulty verdict

No unrestricted instance screened here has earned the user's **“not too hard”** designation. Small n only makes representation and checking manageable; it does not bound the missing mathematical step. The real missing step for `((7,3,3))_2` is exclusion or construction of arbitrary rank-three projectors, outside CWS and outside large stabilizer-parent subcodes. For `((11,5,4))_2`, the published CWS classification excludes both symmetric and asymmetric graph frames; a constructive resolution requires genuinely non-CWS projectors.

The eleven-qubit assay was intended to attack the book's finite-code construction question, but the initially missed 2019 classification means the chosen construction class was already closed. This is a baseline-screening failure, not open-problem progress. The defensible deliverable is a **negative tractability screening decision plus exact restricted reproductions**, not a claimed successful choice of an easy open physics problem. No further CWS search at these parameters is justified.

## 4. Primary references

- **[P1]** Pavel Panteleev and Gleb Kalachev, *Asymptotically Good Quantum and Locally Testable Classical LDPC Codes*, STOC 2022; [arXiv:2111.03654](https://arxiv.org/abs/2111.03654).
- **[P2]** Gerard Anglès Munné, Andrew Nemec, and Felix Huber, *SDP bounds on quantum codes*, arXiv preprint, v2 (2025); [arXiv:2408.10323](https://arxiv.org/abs/2408.10323). The practical exclusions named in this work receive exact certificates in [P3].
- **[P3]** Gerard Anglès Munné and Felix Huber, *SDP bounds on quantum codes: rational certificates*, arXiv preprint (2026); [arXiv:2603.19901](https://arxiv.org/abs/2603.19901), especially Eq. (11) and Table 1. **Nemec is not an author of this follow-up.** Pinned PDF: `source/rational-sdp-2603.19901.pdf`.
- **[P4]** Irit Dinur, Min-Hsiu Hsieh, Ting-Chun Lin, and Thomas Vidick, *Good Quantum LDPC Codes with Linear Time Decoders*, arXiv preprint (2022); [arXiv:2206.07750](https://arxiv.org/abs/2206.07750).
- **[P5]** Oscar Higgott and Craig Gidney, *Sparse Blossom: correcting a million errors per core second with minimum-weight matching*, **Quantum 9**, 1600 (2025); DOI [10.22331/q-2025-01-20-1600](https://quantum-journal.org/papers/q-2025-01-20-1600/); arXiv:2303.15933.
- **[P6]** William Gay, Fernando Granha Jeronimo, and Abhi Shukul, *Explicit Capacity-Achieving Quantum LDPC Codes List Decodable in Near-linear Time*, arXiv preprint, 30 September 2026; [arXiv:2609.40313](https://arxiv.org/abs/2609.40313). Abstract-level status summary here; no independent proof audit.
- **[P7]** Avanti Ketkar, Andreas Klappenecker, Santosh Kumar, and Pradeep Kiran Sarvepalli, *Nonbinary stabilizer codes over finite fields*, **IEEE Transactions on Information Theory 52**, 4892–4914 (2006); DOI [10.1109/TIT.2006.883612](https://doi.org/10.1109/TIT.2006.883612); [arXiv:quant-ph/0508070](https://arxiv.org/abs/quant-ph/0508070).
- **[P8]** Xianmang He, Jingli Wang, Chunfang Huang, and Yindong Chen, *Exploring new lengths for q-ary quantum MDS codes with larger distance*, **PLOS ONE 20(6)**, e0325027 (2025); DOI [10.1371/journal.pone.0325027](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0325027). This is a representative recent construction, not a universal optimality theorem.
- **[P9]** Andrew Cross, Graeme Smith, John A. Smolin, and Bei Zeng, *Codeword Stabilized Quantum Codes*, **IEEE Transactions on Information Theory 55** (2009); [arXiv:0708.1021](https://arxiv.org/abs/0708.1021).
- **[P10]** Sixia Yu, Qing Chen, and C. H. Oh, *Two infinite families of nonadditive quantum error-correcting codes*, arXiv preprint (2009); [arXiv:0901.1935](https://arxiv.org/abs/0901.1935).
- **[P11]** Isaac L. Chuang, Andrew W. Cross, Graeme Smith, John A. Smolin, and Bei Zeng, *Codeword stabilized quantum codes: algorithm and structure*, **Journal of Mathematical Physics 50**, 042109 (2009); DOI [10.1063/1.3086833](https://doi.org/10.1063/1.3086833); [arXiv:0803.3232](https://arxiv.org/abs/0803.3232). Pinned PDF: `source/cws-structure-0803.3232.pdf`.
- **[P12]** Chenfeng Cao, Chao Zhang, Zipeng Wu, Markus Grassl, and Bei Zeng, *Quantum variational learning for quantum error-correcting codes*, arXiv preprint (2022); [arXiv:2204.03560](https://arxiv.org/abs/2204.03560).
- **[P13]** Man-Duen Choi, David W. Kribs, and Karol Życzkowski, *Higher-Rank Numerical Ranges and Compression Problems*, **Linear Algebra and its Applications 418**, 828–839 (2006); [arXiv:math/0511278](https://arxiv.org/abs/math/0511278). Standard Hermitian-compression theory underlying the parent-subcode argument below; no priority claim for that argument.
- **[P14]** Alex Rigby, JC Olivier, and Peter Jarvis, *Heuristic construction of codeword stabilized codes*, **Physical Review A 100**, 062303 (2019); [arXiv:1907.04537v2](https://arxiv.org/html/1907.04537v2), especially §§III.A–III.C. Despite the title, the n=11,d=4 result is an exhaustive maximum-clique result, not their heuristic n=12,d=4 search. Pinned PDF: `source/cws-exhaustive-1907.04537.pdf`. We independently replayed only the 32-frame subfamily, not the entire published LC-class enumeration.
- **[T]** Markus Grassl, *Bounds on the minimum distance of linear codes and quantum codes*, online database, individual entries above; [quantum table interface](https://www.codetables.de/QECC/index.html). Selected raw pages are hash-pinned in `source/manifest.json`.
