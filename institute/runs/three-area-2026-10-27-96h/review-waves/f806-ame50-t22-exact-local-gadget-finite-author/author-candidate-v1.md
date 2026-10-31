# N=50, t=22: exact local-gadget and phase-interface finite author candidate

**Status: NONBLIND GENERAL AUTHOR; NEW SOURCE UNRUN; no finite result or parent adoption.** The adjacent complete source `finite-t22-local-gadget-v1.py` is offered for a future bounded check, not as evidence that its assertions have passed. It has not been run, tested, compiled, linted, formatted, or executed through an interpreter. Parent must first whole-read the actual final source and only then decide whether to issue a separate GO. The source's printed summary describes what a successful future run would have checked; no such output was observed here. Its expected values and negative controls remain subject to that read and run.

This is a local interface check, not a construction of P, a 28-word E, a 50-support state, or a proof of a support bound. It does not settle the same-tensor t=22 branch, phases of an arbitrary support, any other t, existence of a P completion, or a global minimum. No novelty, priority, human, independent-family, formal/kernel, or parent-adoption claim is made.

## Exact finite scope and mathematical rationale

### 1. One 12-word partial tensor, all three physical cuts

The source specifies the actual words and signs twice, once literally and once from the rule in S1. For `i` in Z/3 let `L_i=(i,i,i)`, `R_i=(i,i-1,i+1)`, append `d=0,1`, and give every word integer sign `+1` except `(R_i,1)`, which has sign `-1`. The intended actual coefficient is the integer sign divided by `sqrt(2)`. The source compares the literal four-tuples and signs with the formula, checks all 12 words are distinct, the `(3,3,3,2)` local alphabet profile and occurrence counts, and connectedness under agreement in at least two of the same four physical parties.

The intended reason there are three blocks in each cut is that each pair among A,B,C identifies one of the six distinct L/R triples, while fixing one of A,B,C identifies one L and one R. Consequently in each physical flattening AB|CD, AC|BD, AD|BC the active six rows and six columns decompose into three full 2-by-2 supports. The signed matrices are Hadamard blocks after appropriate row/column order. The source forms each 36-by-36 physical flattening from the *same* signed dictionary, verifies exact integer row and column Grams including zero inactive rows/columns, checks both norms and off-diagonal orthogonality, constructs the actual squares, and checks `a*d+b*c=0` on each. Integer active Gram `2I` corresponds to identity after division of the integer matrix by `sqrt(2)`; no floating point or symbolic square root is evaluated. A partial block-unitary with 30 zero rows and columns in every full flattening is not a unitary 36-by-36 tensor and does not imply any completion.

Named intended-reason mutants are a single phase flip (same support/norms, expected row and column orthogonality failures in each cut), two coordinated flips (AD|BC expected to remain good while AB|CD and AC|BD fail), one coefficient changed from integer 1 to 2 (norm and orthogonality failures), and one word removed from an in-memory copy (singleton pair lines, block failure, and norm failures). In particular, the two-flip control is designed to catch paying only the still-good cut. These are source assertions, not observed mutation results.

### 2. Eight even binary words and the integer-kernel interface

The source enumerates the eight even-parity words in `{0,1}^4`, extracts two actual four-word squares per physical cut, and finds the explicitly specified square rows, with `w` denoting the basis vector indexed by word `w`:

- `r1` in AB|CD: `0000 + 1111 - 0011 - 1100`;
- `r2` in AC|BD: `0011 + 1100 - 0110 - 1001`;
- `r3` in AD|BC: `0000 + 1111 - 0110 - 1001`.

The written cancellation `r1+r2-r3=0` has coefficient sum `1`, so it is the specific odd-sum **integer** dependency that contradicts the three simultaneous phase equations `r_j theta=1/2 mod 1`. This is an eight-word local obstruction under the stated square interface, not a proposed 28-word E and not a proof that an arbitrary support contains it. The source also checks all eight sign choices for independently reversing row orientations.

The `(1,1,1)` coefficient mutant is deliberately subtler: its sum is odd and its weighted row sum is zero mod 2, but its exact integer weighted row sum is `2*r3`, not zero. It must be rejected for failure of the integer-kernel condition rather than treated as an obstruction merely modulo 2. Conversely `(2,2,-2)` is an exact integer dependency but has even coefficient sum and must not be treated as the required odd dependency. These are intended exact checks; no result from this source has been observed.

### 3. Necessary E-alphabet and P-incidence arithmetic

For the actual common-tensor pair-line interface assumed in S1, write `q_i` for E-alphabet sizes, `d_i(x)` for an E partner degree, and `n_k` for the number of P words having exactly `k` coordinates in their corresponding E alphabets. The necessary premises are `3 <= q_i <= 6`, `q_i*q_j >= 14`, `d_i(x) >= 2`, and `sum_x d_i(x)=14`. Counting P incidences and P cells gives

`sum n_k=22`, `S1=sum k*n_k=6*sum q_i-56`, and `S2=sum binom(k,2)*n_k=sum_{i<j}q_i*q_j-84`.

Thus `66-2*S1+S2=3*n_0+n_1+n_4 >= 0`. The source enumerates sorted profiles satisfying the stated pair-capacity bounds, checks the six stated negative-defect exclusions and the 13 remaining **necessary** profiles, and separately checks existence of nonnegative moment count vectors consistent with the elementary `k >= number_of_full_six_symbol_parties` condition. Count-vector existence is only an arithmetic relaxation; it is not a realization of pair cells or words.

The source also requires the stated unique moment vectors for `3566`, `3666`, and `4456`, and enumerates their stated degree multisets by integer combinations. For `4456`, the additional bound on a six-symbol-party degree follows conditionally from its resulting `n_2+n_3=22`: for any fixed symbol of that party, the two missing symbols of each four-symbol party and the one missing symbol of the five-symbol party give five P pair-incidences. Each P word contributes at most two such incidences, so `2*(6-d) >= 5`, forcing `d <= 3` in addition to the lower bound. This derivation depends on the common P pair-injectivity and pair saturation assumptions; the source checks only its finite arithmetic consequences, not the physical completion.

Intended-reason controls require rejection of a count vector only on its second moment; another satisfies both moments but violates the lower bound on `k` from the two full parties; another satisfies the degree sum and lower bound but exceeds the partner alphabet; a `4456` degree vector passes the unrefined cap 4 but violates the incidence-improved cap 3; and `4444` has negative defect. The source additionally requires that every retained profile have at least one arithmetic count vector; this is a conservative additional source guard, not a claim of a realized support. No asserted count, surviving profile, or mutant outcome has been obtained by execution in this duty.

## Check bounds, semantics, and remaining gaps

The new source is self-contained standard-library Python with no file inputs, file output, network, solver, floating point, or third-party dependency. It uses fixed objects only: 12 words in three 36-by-36 matrices; the eight binary even words and eight row-orientation choices; and sorted four-party profiles with sizes in `3..6`. Its moment search uses three nonnegative bounded counts and derives the other two from total count and first moment; no search over physical P or E subsets is performed. On a future success it emits one JSON line to stdout; any violated `require` raises instead of reporting success. Source validity, expected behavior, and runtime have **not** been independently established here.

The remaining actual problem is the common physical incidence of all 22 P words and 28 E words in six projections, the seven actual squares in each of three cuts, and their simultaneous complex phases. In particular, neither this 12-word gadget nor the 13 arithmetic profiles constructs a common 50-word tensor; the checker has no P-completion procedure or global search, and does not establish the general integer-kernel converse. Any source defect or failed intended-reason mutant discovered by the parent must be preserved and reported as such, not retroactively described as a successful run.

## Source, controls, and process coverage

Main directly confirmed the actual finalized dispatch before this duty opened its receipt or any scientific packet body. I read the complete actual dispatch receipt; then the complete 213-LF manifest, the 212-LF prepared metadata, the 199-LF freeze receipt and the 181-LF final pre-dispatch binding (metadata was read before freeze/binding), and all 22 listed status/permission controls through their endings. I sent Main a direct PREBODY ACK identifying **22 controls** and the one ordered **250-LF** part before opening the body. Thereafter I read that part serially RAW in windows `1-20, 21-40, 41-60, 61-80, 81-100, 101-120, 121-140, 141-160, 161-180, 181-200, 201-220, 221-240, 241-250`, including complete long lines and the ending, before mathematics or comparison. No packet-display truncation or body-sequence deviation is known. The globally required memory summary and coding-discipline skill were read before the direct dispatch notice; no scientific packet body or scientific source was read then.

The single packet contains the complete bodies below; hashes are the **manifest/freeze-reported** pins, not independently measured in this duty:

1. S1, f786 `author-candidate-v1.md`, 143 LF, SHA-256 `14c09bbaf27bbf57d77cfd4bba0225c693834a531371ec1c9eb0bc241e01549c` — local gadget, phase obstruction, and profile arithmetic being checked.
2. S2, `physics-6-conditional-minimum-support-50-to-60-same-tensor-union-parent-v1.md`, 29 LF, SHA-256 `ccbadbf970b31c199b08f8adeeca03e489f345052d204b31a6192af69aa1e6f0` — historical conditional context only, not a new global claim.
3. S3, `physics-6-actual-ame49-t28-entire-same-complex-tensor-exclusion-parent-v1.md`, 29 LF, SHA-256 `ceadc652cbdcfc957d9ca64ab97cd6e0e8c7faa0826356dc03de8d60f093957a` — separate N=49 branch context only.
4. S4, `physics-6-actual-ame49-t23-through-t27-exclusion-and-t28-frontier-parent-v1.md`, 31 LF, SHA-256 `69f2bff74957951086b6481b2c553e6ab2d2c59f6ea2fd7d369c4c4acefaf8b0` — separate N=49 branch context only.

The dispatch reports packet-part SHA-256 `d3c36d2bf9c1ed8e3eaff5e9f1df74cc81e83b6c7d52779b23ba47ea50f90a86`; it reports manifest SHA-256 `c1cab9307bf78b782e95a88861d8cf231012ff0381f7d7469031246ceba43bb1` and metadata SHA-256 `8e115bf71702ac6a0ed28ae55ed46b933ba4ebea96fccbcc967447259332d505`. The metadata reports freeze-receipt SHA-256 `75364433cfa57f1e169716f7e56a9c0876fdffa348bb877223273ef08ea525a7` and final-binding SHA-256 `b0e011df9c3bc9f9eca4af6985a1d0e832f832fc5da44d4ad93279cc4b618dbe`. These are administrative statements read from those records, not independent hashing, source-identity authentication, or cognition/separation certification. Original linked scientific files and old code were not opened.

For precise control coverage, let `R=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h` and `W=R/review-waves`. All 22 complete controls are exactly those pinned in the manifest, in that order:

1. `R/prospective-author-method-scope-restoration-20261030-v1.json`;
2. `R/contract-addendum-2-frontier-first-owner-direction-v1.json`;
3. `R/parent-L1-selected-diagnostic-release-quarantine-v1.json`;
4. `R/parent-privacy-auxiliary-parameter-diagnostic-quarantine-v1.json`;
5. `R/parent-core-gram-auxiliary-operator-diagnostic-quarantine-v1.json`;
6. `R/parent-ame-held-compression-claim-consumer-quarantine-v1.json`;
7. `R/parent-held-ph-registration-report-consumer-quarantine-v1.json`;
8. `W/f439-depolarizing-ancillary-all-dimensional-repair-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json`;
9. `W/f444-spr-full-seven-coefficient-enlargement-and-all-ray-review/parent-selected-diagnostic-process-major-quarantine-v1.json`;
10. `W/f448-kac-actual-second-arm-exterior-module-and-character-review/parent-selected-diagnostic-process-major-quarantine-v1.json`;
11. `W/f508-coherent-vacuum-w4-h2-channel-and-strictness-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json`;
12. `W/f513-boolean-five-span-physical-four-fibre-xor-obstruction-review/parent-selected-diagnostic-process-major-quarantine-v1.json`;
13. `W/f586-semigroup-finite-pure-source-free-band-regularity-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json`;
14. `W/f602-olson-deficit-six-protected-triples-independent-actual-word-check/parent-selected-diagnostic-process-major-quarantine-v1.json`;
15. `W/f596-actual-ame48-t24-entire-4555-same-tensor-frontier/parent-selected-instance-process-major-quarantine-v1.json`;
16. `W/f653-sun8-psl2-small-exception-actual-cosets-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json`;
17. `W/f654-sun8-primepower-source-and-actual-normalcut-consumer-review/parent-selected-diagnostic-process-major-quarantine-v1.json`;
18. `W/f659-fresh-original-input-sun8-source-and-normalcut-consumer-review/parent-selected-diagnostic-process-major-quarantine-v1.json`;
19. `W/f660-fresh-original-input-sun8-exceptional-actual-coset-review/parent-selected-diagnostic-process-major-quarantine-v1.json`;
20. `W/f662-report-v23-werner-core-falsification-documentary-audit/parent-selected-diagnostic-process-major-quarantine-v1.json`;
21. `R/parent-remaining-d0-occupancy-E-row-omission-process-major-v1.json`;
22. `R/parent-prerun-f746-matching-and-f749-occupancy-design-corrections-v1.json`.

Controls were used only for status and permissions. All genuinely held episodes and all proof/method/selection/planning/verification/reporting/confidence/downstream consumers remain NONINPUT. No held payload, sibling return, unlisted source, source-follow, prior code, scientific executable, interpreter, solver, test, build, external CLI, network, Git, installation, or filesystem deletion was used. This record and the new source are the only scientific writes by this worker. No execution or validation is claimed; parent whole-read plus separately authorized execution and independent mathematical review remain necessary before any finite assertion is adopted.
