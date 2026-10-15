# Quantum error-correcting code construction

Feng Keqin's **Quantum Error-Correcting Codes** chapter in *10000 Selected Problems in Sciences: Physics* (Science Press, 2009), pp. 601–604, asks for better finite quantum codes, useful decoding algorithms, nonbinary constructions, and nonadditive codes. These are research programs, not one finite conjecture. We investigated two precise unresolved qubit instances: `((7,3,3))_2` and `((11,5,4))_2`, where the middle number is the dimension of the protected subspace, not a number of logical qubits. A source-backed status survey and exact construction/exclusion checks are preserved here; neither unrestricted instance is solved.

## Verdict and selection outcome — 2026-10-14 PT

**OPEN-BLOCKED** for the unrestricted existence questions. **PARTIAL** for the restricted mathematical certificates, whose exclusion results are **ALREADY-SOLVED** in stronger prior literature. FRONTIER states: **HEADROOM-ABSENT** in the CWS construction class for the attacked targets; **NEEDS-NEW-REPRESENTATION** for further construction work. No Discovery or parameter improvement is claimed.

**The “still-open but not-too-hard” selection criterion was not established.** The seven-qubit CWS obstruction was already proved in 2009. A stronger 2019 exhaustive-CWS result, found during the final prior-art check, also excludes the eleven-qubit target throughout CWS, not merely our tested circulant family. The assay is therefore a restricted reproduction, not research headway on an open class. Known-code reproduction and these family-specific certifications do **not** count as solving the user's requested open target. Small matrices and fast replay do not make the remaining mathematical obligation easy.

### Precise statements addressed

1. Does a rank-three projector P on `(C^2)^⊗7` obey `PEP=c_E P` for every Pauli E of weight at most two? The 2026 primary general-code table leaves `2 <= K_max(7,3) <= 3`.
2. Does a rank-five projector on `(C^2)^⊗11` detect every Pauli of weight at most three? The same table leaves `4 <= K_max(11,4) <= 7`.
3. Restricted reproduction: at `(n,d)=(11,4)`, the maximum dimension of a CWS code with a **vertex-transitive graph-state frame** is exactly **four**. All 32 circulant graph frames were exhausted; 20 attain four and none attains five. Our replay does not cover other graph frames; Rigby–Olivier–Jarvis (2019), arXiv:1907.04537 §III.C, already report the stronger all-CWS exclusion. General quantum codes remain outside that result.
4. Supporting certifications: the seven-qubit enhanced LP admits an exact rational K=3 witness but excludes K=4; any subcode larger than half a stabilizer parent cannot improve its distance; the known CWS K=3 exclusion and known Steane anchor were independently checked.

## Reproduction

From this folder, this single shell command replays all **local computational results**. It does not replay the full published CWS classification:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/verify.py && /Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/verify_circulant.py
```

It needs Python, NetworkX and NumPy, but no internet, LP/SDP solver, GPU, or model call. It checks rational identities, two independent distance representations for each explicit code, all 1,044 seven-vertex graph representatives, all 32 eleven-vertex circulant frames, and four negative controls across the two programs. The complete analytic arguments, trust boundaries, observed output and review dispositions are in [RESULTS.md](RESULTS.md). The analytic dimension lemma is not machine-formalized by the command.

Optional regeneration of the proposals/search records:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/build_lp_certificates.py && /Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/search_circulant.py
```

The first generator uses SciPy/HiGHS to propose tiny LP certificates, accepting only exact rational results. The second is an exhaustive integer bitset search, independently checked by a different clique implementation.

## Frozen protocol and explicit adaptation

Before computation the seven-qubit target, primary baseline, exact verification requirements, degeneracy handling, fixed negative controls, and lack of random search were fixed. The redundant graph atlas was never the sole premise of a universal proof. After recognizing that the CWS barrier was already known, the target-selection amendment **preceded** the eleven-qubit computation: enumerate every undirected circulant graph on 11 vertices, allow arbitrary word sets, seek K=5, and retain K=4 as a control. A complete miss was explicitly to produce a **negative screening decision**, not to be reinterpreted as global nonexistence. All runs used one process and small arrays; no model-based optimization, hardware run or decoder benchmark was performed.

**Post-assay literature correction:** the initial screening missed the stronger 2019 CWS classification. That miss is retained as a process limitation, not erased by rebranding the assay. The prior suggestion to search non-vertex-transitive CWS frames is withdrawn; a hypothetical `((11,5,4))_2` must be genuinely non-CWS according to that published exhaustive result. See STATUS.md [P14] and RESULTS.md §6.

## File map

- [STATUS.md](STATUS.md): all four book subproblems, primary citations, live-table gaps and preprint-status caveats.
- [RESULTS.md](RESULTS.md): claims, complete arguments, evidence labels, novelty boundary and independent-review dispositions.
- `source/problem.zh.txt`: supplied source excerpt, copied without edits.
- `source/manifest.json`: hash-pinned selected primary PDFs and live table pages.
- `code/build_lp_certificates.py`, `code/search_circulant.py`: deterministic proposal/search programs.
- `code/verify.py`, `code/verify_circulant.py`: independent exact replay programs.
- `results/lp-*.json`: rational LP witnesses; `results/steane-7-1-3.json`: explicit known code.
- `results/circulant-11-5-4.json`: every graph frame and its admissible words; `results/circulant-11-4-4-anchor.json`: explicit control code.
- `results/verification.json`, `results/circulant-verification.json`: observed exact replay records.
- `review/`: hostile Codex prompt, output and invocation record.

The most valuable next action is to derive a bounded constraint on **genuinely non-CWS rank-five projectors** that is absent from the current weight-enumerator relaxation, before allocating a larger search. No such missing lemma has been closed here. Neither further CWS search nor an unstructured restart campaign is justified by the present evidence.
