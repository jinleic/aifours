DISPOSITION: ACCEPT-WITH-FIXES

**FATAL**

none.

**MAJOR**

**MAJOR-1 — Class-list coverage still has an unverified provenance dependency.** The completeness claim at `review/GRAM-ENCODING.r1.md:65` requires the listed multiplicities to be actual autoparatopy-group orders computed by the reviewed normaliser. The manifest explicitly says the producing binary’s build provenance was not recorded (`manifest.json:681`), and its input seeds are unpinned (`manifest.json:688`). The pinned `MATCH` line exists (`explore/ls_classes.stderr:149`), and the printed reduced counts do sum correctly by hand, but neither establishes that those multiplicities came from this source.

Correction: independently validate every reconstructed square, its canonical key and multiplicity, or provide a reproducible source-bound enumeration with validated seeds. Supply the precise published source for the reduced-square total assumed at `code/ls_classes.c:6`. I found no evidence that the list is actually incomplete; this is an evidence gap, not a demonstrated unsound reduction.

**MAJOR-2 — The promised frozen-control rerun and code-hash certification record are absent.** `review/AMENDMENT-1.r1.md:42` promises both. The driver records the CNF hash, solver information and checker status (`code/gram_certify.py:76`), but no encoder, driver, imported-helper or control-code hashes. It neither invokes the controls nor records their outcomes. Its instance identifiers also depend on an externally supplied, unhashed class file (`code/gram_certify.py:82`).

Correction: implement that step or provide a pinned wrapper that does it. Bind the certification record to the class-list digest, class key, encoder, driver, imported `square_from_key` implementation and frozen control results. Check coverage of all 147 K2 keys and both K3 encodings.

**MAJOR-3 — The certification driver does not implement the bounded production protocol or robust FIFO lifecycle.** The three-hour limit is required at `review/AMENDMENT-1.r1.md:30` and remains required by `README.md:96`. Neither solver command has a limit (`code/gram_certify.py:46`, `code/gram_certify.py:56`), and both `communicate()` calls are unbounded (`code/gram_certify.py:71`).

There are also failure paths without bounded recovery: a solver that exits before opening the FIFO can leave the checker waiting; an early checker exit can strand the writer; and waiting for the solver before draining the checker’s output permits pipe backpressure. Solver output is discarded, so the driver also does not implement the promised SAT-model retention at `review/AMENDMENT-1.r1.md:33`.

Correction: enforce the resource bound, drain both outputs concurrently, handle premature exits and EOF, terminate and reap both processes with bounded waits, and retain any SAT assignment. These are operational gaps; they do not invalidate an actually valid proof of the intended CNF.

**MAJOR-4 — The controls leave the symmetry path entirely untested.** Encoder A’s calls never enable `sym` (`code/gram_controls.py:53`, `code/gram_controls.py:57`, `code/gram_controls.py:59`, `code/gram_controls.py:69`). Encoder B likewise never passes `--sym` (`code/gram_controlsB.py:47`, `code/gram_controlsB.py:57`, `code/gram_controlsB.py:61`, `code/gram_controlsB.py:64`). Heavy and multiple-square G5 are exercised separately, without a combined control.

Correction: add matched component controls before production under `README.md:91`. In particular, the existing genuine Ψ(f) can test heavy plus sym with one square: its three prescribed edges are nonzero. Add a control that removes one prescribed edge and distinguishes sym enabled from disabled, and a genuine classical assignment accepted without heavy but rejected with heavy. Add encoder A’s missing classical K2-shaped control. A positive genuine K2/K3 example at order 7 cannot reasonably be required—it would resolve the research question—but these feasible component controls are still missing.

**MINOR**

**MINOR-1 — Encoder A cites the expressly unaccepted K1 §8.** `code/gram_enc.py:15` names `review/K1-THEOREM.r1.md` section 8 as part of G4’s justification. Correction: cite Theorem K1 at `review/K1-THEOREM.r1.md:114` and the independent minimal-counterexample argument at `review/GRAM-ENCODING.r1.md:45`. The latter argument works without §8, so this is a dependency-reference error rather than a fatal reliance.

**MINOR-2 — Complete the Gram conventions.** The definition at `review/GRAM-ENCODING.r1.md:25` introduces G only for distinct points, but `review/GRAM-ENCODING.r1.md:37` uses G(s,s). Correction: explicitly state conjugate-linearity in the first argument, G(p,p)=1, G(q,p)=conj(G(p,q)), and symmetry of the off-diagonal Boolean support. No production encoder call uses the diagonal as a false Boolean literal.

**MINOR-3 — Frozen-document status and references are inconsistent.** The frozen document still says “lane draft” (`review/GRAM-ENCODING.r1.md:3`), and its opening sentence resumes after the inserted block (`review/GRAM-ENCODING.r1.md:21`). The amendment and code point to an unversioned filename (`review/AMENDMENT-1.r1.md:11`, `code/gram_enc.py:6`, `code/gram_encB.py:4`). Correction: repair these in an explicitly reviewed delta, preserving the current frozen bytes.

**MINOR-4 — Encoder B has weaker control-input validation and an unreachable malformed branch.** B silently ignores marked collinear pairs (`code/gram_encB.py:213`), whereas A rejects them (`code/gram_enc.py:146`). Also, a one-item G2 list with collinear p,q would emit `None` as a literal at `code/gram_encB.py:151`. Correction: reject collinear marked pairs and handle that branch as the unit clause ¬s1. The malformed branch is unreachable in the valid production nets, as shown below.

**MINOR-5 — Two contextual hash abbreviations are wrong against the manifest’s recorded digests.** `review/K1-THEOREM.r1.md:64` should end `…e113`, not `…3c7e` (`manifest.json:637`). `README.md:7` should end `…a3ff2`, not `…ff3a2` (`manifest.json:648`). Correction: repair the abbreviations. Their unpinned target files were not independently rehashed in this audit.

**MINOR-6 — The manifest’s LF-split count convention is off by one.** `manifest.json:10` says a file ending in LF has `lines_split_LF = lf_count`. Under the requested `text.split('\n')` convention, the terminal empty element remains: 49 LF characters give 50 elements, contrary to `manifest.json:22`. Correction: use `lf_count + 1`. This does not move any nonempty line cited here.

The mathematical implication survives these findings: **with verified class coverage, valid UNSAT proofs of the specified instances would exclude K2 using K1, and then exclude K3 using K1 plus K2.** Model completeness is unnecessary. The present pin does not yet discharge the evidence and production-control gaps above.

**(1) G1, G2 and G3**

These conditions are necessary for arbitrary complex unit-vector assignments carrying ONBs on the designated lines; they are not an ansatz.

The line inventory is correct: rows and columns, plus L-symbol lines in K2 (`review/GRAM-ENCODING.r1.md:28`, `review/GRAM-ENCODING.r1.md:29`). The extra lines follow from C1, whose proof at `review/K1-THEOREM.r1.md:11` is valid.

With the convention stated in MINOR-2,
\[
\psi_p=\sum_{r\in\ell}G(r,p)\psi_r,\qquad
G(p,q)=\sum_{r\in\ell}\overline{G(r,p)}G(r,q).
\]
Thus zero common support coordinates force zero inner product; exactly one gives a single nonzero complex product and forces nonzero inner product. This verifies `review/GRAM-ENCODING.r1.md:33`–35.

If p,q lie on another ONB line k, their inner product is zero, so exactly one common coordinate is impossible. When ℓ meets k, the meeting coordinate is zero for both off-line points. When ℓ is parallel to k, the same expansion applies without a meeting coordinate. Neither case needs a further hypothesis. Removing coordinates structurally forced zero by a third ONB line is legitimate; removing other coordinates would not be.

For G3, write the two ordered ONBs as unitary column matrices A and B. Their transition matrix is A*B. If the lines meet at s, the common vector gives a 1 entry and zeros elsewhere in its row and column, leaving a unitary 6×6 block. Parallel lines give a full unitary 7×7 matrix. Every row has a nonzero entry. A row with one nonzero entry has modulus one there, exhausting the corresponding column norm and forcing every other entry in that column to zero. Reversing the ordered line pair gives the column-to-row statement. This verifies `review/GRAM-ENCODING.r1.md:36`–40.

Unit vectors have nonempty support in every ONB; points on their own frame line have weight one through G(p,p)=1.

**(2) G5 and the classical square**

For distinct cells, tensor inner products factor exactly:
\[
\langle\psi_{a,p}\otimes\psi_{b,p},
        \psi_{a,q}\otimes\psi_{b,q}\rangle
=G_a(p,q)G_b(p,q).
\]
There are 49 unit tensor vectors in dimension 49. Pairwise orthogonality therefore is equivalent to being an ONB, proving both directions claimed at `review/GRAM-ENCODING.r1.md:42`.

For a classical L in the standard basis, different symbols already give zero tensor inner product; equal symbols require the quantum entries to be orthogonal. Seven unit vectors on each symbol line then form an ONB. Thus G1 on those lines is exactly C1 (`review/GRAM-ENCODING.r1.md:44`).

Putting L into the standard basis uses entry phases and a unitary on L alone, both permitted by `sources/2607.12933v2.layout.txt:111`–113. It leaves the other squares’ entries and Gram supports unchanged.

**(3) G4 heavy**

The full printed proof of Lemma 10 supports the arbitrary-basis use. It rotates all entries with one selected two-coordinate support and preserves every previously zero inner product (`sources/2607.12933v2.layout.txt:185`–192). An orthogonal vector of weight at most two must have either the same two-coordinate support or disjoint support: a one-coordinate intersection cannot cancel. The proof uses neither standard form nor row 0. The raw extraction agrees (`sources/2607.12933v2.raw.txt:349`–356).

Each operation preserves norms and all row/column orthogonalities, hence the QLS axioms. It preserves orthogonality with **both** other squares simultaneously: for every tensor pair, whichever factor originally supplied a zero still supplies one. Repetition strictly decreases the number of weight-two entries and ends with a classical QLS. This is stronger than preserving orthogonality to one preselected partner.

For an arbitrary ONB B, first apply a unitary taking B to the standard basis. A unitary on one whole square preserves all its Gram inner products and therefore every tensor orthogonality. Classicality also survives the inverse unitary. The argument at `review/GRAM-ENCODING.r1.md:48`–50 is consequently valid.

The minimisation must be over **all non-classical triples of MOQLS(7)**, minimising the number m of individually non-classical squares. If this family is nonempty, a minimiser exists because m belongs to {1,2,3}; no compactness argument is needed. C0 is valid because separate square unitaries are permitted (`README.md:24`): m=0 means a classical set. K1 excludes m=1. Replacing one light non-classical square decreases m by exactly one while leaving m−1≥1, contradicting minimality.

The logical order at `review/GRAM-ENCODING.r1.md:54`–55 is correct:

- Given K1, every K2 triple is minimal and both quantum squares are heavy.
- Only after K2 is excluded does the same argument apply to every K3 triple.
- While K2 remains open, a heavy K3 exclusion alone does not exclude arbitrary K3 triples; it excludes heavy K3 triples, including any globally m-minimal K3 counterexample.

For an own-line frame, coefficient support is exactly the set of nonzero Gram overlaps. Points on the frame have weight one, so a heavy witness lies off it. Both K2 quantum squares are individually non-classical by the definition of K2, and imposing heavy on all 21 of their lines is justified. No part of K1 §8 is needed.

**(4) K2 main-class normalisation and enumeration**

The genuine-configuration transport works, including global tensor orthogonality.

Represent L by its triples \((i,j,L(i,j))\). A permutation of the three coordinates, followed by independent coordinate-label permutations, gives another Latin square L′ and a bijection f between its 49 cells and the original cells. Transport both quantum assignments by that **same** bijection.

Every new row, column and symbol line is an old net line. Thus both transported assignments satisfy the QLS axioms and C1. Their 49 tensor vectors are simply globally reindexed, so the tensor ONB condition is preserved—not merely its restrictions to lines. Their projective-ray sets are unchanged, preserving non-classicality. G1–G3, G5 and own-line heavy transport with incidence. This supplies the configuration-level justification abbreviated at `review/GRAM-ENCODING.r1.md:58`.

The normaliser considers all six conjugations (`code/ls_classes.c:19`). After choosing class order and origin, ordering the other six cells of the new first row fixes column and symbol labels; the first column then forces row labels (`code/ls_classes.c:46`, `code/ls_classes.c:48`). These are precisely the paratopies producing reduced squares:
\[
6\cdot49\cdot6!=211680.
\]
The autoparatopy group acts freely on these fully labelled normalisations. Each reduced output therefore occurs with multiplicity \(|\operatorname{Par}(L)|\). The minimum reduced key is a complete main-class invariant, and its multiplicity gives the group order. This establishes the source algorithm’s counting principle.

Cycle switches preserve Latin squares (`code/ls_classes.c:112`–115), but BFS connectivity alone is not a completeness proof. Moreover, the run used 32 seed classes (`explore/ls_classes.stderr:1`); Z₇ alone is atomic under the switches described at `code/ls_classes.c:91`. Completeness follows conditionally from distinct verified canonical classes and the orbit sum exhausting the assumed total—not merely from reaching BFS closure.

By hand, the printed reduced counts total **16,942,080**, agreeing with the actual pinned log at `explore/ls_classes.stderr:149`. The remaining assumptions are those identified in MAJOR-1: the published reduced-square count, correct source-to-binary provenance and correct computed multiplicities. The 147-class McKay–Meynert–Myrvold claim is cited at `review/GRAM-ENCODING.r1.md:66`; its source is not pinned or re-derived.

The requested spot checks pass:

- `evidence/ls7_main_classes.txt:1` decodes to \(L(i,j)=i+j\bmod7\). Its autotopism group has order \(7^2\cdot6=294\); all six conjugations preserve its main class, giving autoparatopy order 1764. By hand, \(120\cdot1764=211680\).
- `evidence/ls7_main_classes.txt:2` decodes to the following reduced Latin square; every displayed row and column contains 0–6 once:
  ```text
  0 1 2 3 4 5 6
  1 2 0 4 5 6 3
  2 3 4 5 6 0 1
  3 4 1 6 0 2 5
  4 5 6 2 1 3 0
  5 6 3 0 2 1 4
  6 0 5 1 3 4 2
  ```
  By hand, \(17640\cdot12=211680\).

The decoder in `code/k2_classes.py:22` reconstructs exactly the omitted first row/column and the 36 internal entries. It matches `code/ls_classes.c:62`. The certification driver uses this decoder directly for both K2 encoders (`code/gram_certify.py:41`, `code/gram_certify.py:50`).

**(5) K3 symmetry**

The symmetry reduction is valid after heavy has been justified for K3.

Choose any square as square 1. Heavy already holds in every row frame, so choose a row; transposition is unnecessary. Simultaneously permute rows to place the frame at row 0 and an off-frame heavy point at row 1. Simultaneously permute columns to place that point at column 0 and three distinct neighbours at columns 1,2,3. None can occupy the heavy point’s column because column orthogonality forces that overlap to zero.

These permutations preserve global tensor ONBs and permute every other heavy condition. Hence the units do not lose a configuration up to the permitted normalisation (`review/GRAM-ENCODING.r1.md:69`–71).

Both encoders list rows before columns and use coordinates (row,column) (`code/gram_enc.py:55`, `code/gram_encB.py:102`). Their units are exactly the three stated edges (`code/gram_enc.py:124`, `code/gram_encB.py:192`). The replacement heavy clause is implied by those units. K3 correctly uses only the 14 row/column lines; no classical symbol class exists there.

**(6) Encoders, driver and controls**

Both encoders use one variable per unordered non-collinear pair (`code/gram_enc.py:67`–73, `code/gram_encB.py:115`–123). This implements support symmetry and structural G1 zeros.

For encoder A:

- The three H clauses give full equivalence with the conjunction (`code/gram_enc.py:83`–85).
- `code/gram_enc.py:96` enforces “g true implies at least one common neighbour.” `code/gram_enc.py:99` enforces “exactly one implies g true,” or forbids exactly one when g is structurally zero.
- G3 uses ordered line pairs, requires a neighbour, and enforces the unique-neighbour implication (`code/gram_enc.py:100`, `code/gram_enc.py:106`, `code/gram_enc.py:114`).
- G5 is exactly pairwise edge exclusion (`code/gram_enc.py:118`).
- The subset encoding is correct: requiring every \((n-t+1)\)-subset to contain a true literal is equivalent to at least t truths (`code/gram_enc.py:50`). Guards only imply the threshold, while their disjunction selects a witness (`code/gram_enc.py:136`–137). Every genuinely heavy assignment extends to suitable guards.

For encoder B:

- `counter2` gives full equivalences. Its updates are \(n_1\leftrightarrow(a_1\lor x)\) and \(n_2\leftrightarrow(a_2\lor(a_1\land x))\), with the correct initial case (`code/gram_encB.py:50`, `code/gram_encB.py:53`, `code/gram_encB.py:55`).
- The zero-item G2 branch correctly forces g false when present (`code/gram_encB.py:146`–149). The one-item non-collinear branch is correct (`code/gram_encB.py:154`–155). The one-item collinear branch has the malformed literal noted in MINOR-4.
- That malformed branch cannot occur in production. An off-line point has five structurally possible neighbours on a 3-net line, or six on a 2-net line. Two such sets intersect in at least three or five points respectively. Thus production G2 item lists never have length zero or one.
- G3’s required c1 and c2-controlled exclusion implement the same ordered-line conditions as A (`code/gram_encB.py:172`, `code/gram_encB.py:183`). G5 is the same edge exclusion (`code/gram_encB.py:187`).
- `counter_ge3` has the advertised direction: a true counter state implies enough true inputs (`code/gram_encB.py:73`–88). Conversely, assigning states their actual prefix thresholds extends every qualifying input. Requiring at least one returned literal therefore gives an equisatisfiable existential heavy witness (`code/gram_encB.py:202`).

These encodings implement the stated Boolean conditions; they do not implement full Gram positivity, rank, phases or general unitary-pattern realisability. Those omissions weaken the relaxation and cannot make an UNSAT exclusion unsound.

No structural empty clause arises in the valid production nets. Transition neighbourhoods have five possible entries in a 3-net and six in a 2-net, including intersecting-line cases after removing the common point. Heavy witnesses likewise have five or six candidate entries. A’s insufficient-length branch is not reached (`code/gram_enc.py:47`), and neither transition-empty branch is reached (`code/gram_enc.py:106`, `code/gram_encB.py:168`). If an empty clause did arise, it would mean immediate CNF contradiction; its DIMACS representation is valid, and a checker can establish UNSAT without substantive proof steps. The driver’s FIFO lifecycle could nevertheless hang around such an early termination.

For the intended identifiers, CNF construction matches section C exactly: K2 uses two squares, decoded L and heavy; K3 uses three squares, no L, heavy and sym (`code/gram_certify.py:41`, `code/gram_certify.py:43`, `code/gram_certify.py:51`, `code/gram_certify.py:53`).

The exact checker-status test avoids the `NOT VERIFIED` substring trap (`code/gram_certify.py:73`–74). A genuinely valid checker verification proves CNF UNSAT independently of `solver_rc == 20`; requiring that return code is useful consistency checking, not a mathematical prerequisite. FIFO streaming is not itself unsound when the checker consumes the intended stream against the unchanged CNF. Its termination and recovery remain deficient as described in MAJOR-3.

The control data are mathematically appropriate. By hand:
\[
M_0=\{2,6\},\quad m_0=2,\quad m=4,\quad
f=(0,6,5,1,3,4,2).
\]
Also \(f(x)-4x=(0,2,4,3,1,5,6)\), a permutation. The shifted f is non-additive—for example \(f(1)+f(2)=4\ne f(3)=1\). Thus Definition 11, Lemmas 12–14 and the Theorem 6 shift apply (`sources/2607.12933v2.layout.txt:239`, `sources/2607.12933v2.layout.txt:265`, `sources/2607.12933v2.layout.txt:302`, `sources/2607.12933v2.layout.txt:330`). The unshifted function matches Example 15 (`sources/2607.12933v2.layout.txt:352`).

For seven seventh roots, a vanishing sum with multiplicities \(c_0,\ldots,c_6\) gives a polynomial divisible by \(1+X+\cdots+X^6\). Its coefficients sum to seven, forcing every multiplicity to equal one. Consequently the permutation test computes exact Gram support (`review/GRAM-ENCODING.r1.md:74`, `code/gram_controls.py:39`).

Here the zero directions are precisely rows, columns and the Φ(4) symbol lines. Every off-line point has five nonzero overlaps with each such frame, explaining both heavy and the printed 735 unordered nonzero pairs by hand: \(49\cdot30/2=735\).

The JSON files contain the reported control outcomes (`explore/gram/gram_controls_v1.json:17`, `explore/gram/gram_controlsB_v1.json:3`). They are not independently checked solver runs in this audit. Their coverage is limited as stated in MAJOR-4. The source’s order-4 control is unmatched by these hard-coded order-7 encoders, so its absence alone is not a violation of the matched-control rule.

**(7) Hashes and consistency**

I rehashed all 18 listed payload files. Every digest matches its manifest entry, including both full hashes specified in the request. Every printed hash in the amendment and Gram document agrees with the corresponding manifest digest. The two contextual abbreviation mismatches are exactly those recorded in `manifest.json:631`; unpinned targets could only be compared textually against the manifest’s recorded digest.

“Observed MATCH” is backed by the pinned log (`explore/ls_classes.stderr:149`), subject to the provenance qualification above. The following are **not established by the pin**:

- The single-frame UNKNOWN results and timings at `review/AMENDMENT-1.r1.md:7`.
- Stage-1/stage-2 exploration claims and the 23.5-second bound at `review/AMENDMENT-1.r1.md:46` and `review/GRAM-ENCODING.r1.md:87`–88.
- The reported running/progress states at `review/AMENDMENT-1.r1.md:48`–49.
- The external McKay–Meynert–Myrvold count at `review/GRAM-ENCODING.r1.md:66`.

Those remain reports or explicit trust assumptions, not accepted computational evidence. The amendment legitimately changes the representation and verification plan, but it amends only §§0.4–0.5 (`review/AMENDMENT-1.r1.md:3`); it does not remove the resource limits in README §§0.6–0.7. The code therefore needs the bounded-run correction above. The frozen-document, dependency-reference and convention inconsistencies are identified in the MINOR findings.

**Scope:** I read the pinned protocol, amendment, soundness document, both encoders, certification driver, controls and their outputs, enumeration source/list/log, exploration screens, manifest, relevant source passages in both extractions, and K1 context. I checked the reductions, clause implications, auxiliary extensions, control formulas, two class representatives and aggregate arithmetic by hand, and checked payload hashes with SHA-256. I ran no interpreter, claimant code, compiler, solver or proof checker; made no writes; used no network or delegation; and read no outside files. I could not verify the enumeration binary’s provenance, independently recompute all canonical keys and stabilisers, verify external counting literature, or validate any solver/proof/runtime result. K1 remains an input dependency pending its separate review; K2, K3 and the resulting M(7)=2 claim remain open pending the identified fixes and accepted production evidence.