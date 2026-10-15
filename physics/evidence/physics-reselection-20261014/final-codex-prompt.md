# Parent integration audit: five explicit-question physics refinements

Today is 2026-10-14. You are a read-only hostile referee for an AI-for-science research integration. You may read ONLY these files and paths under the current workspace root:

- `ai4s/PHYSICS_RESELECTION.md`
- `ai4s/phys-spiral-dense-forest/{README.md,STATUS.md,RESULTS.md}`
- `ai4s/phys-fermat-chabauty-classification/{README.md,STATUS.md,RESULTS.md}`
- `ai4s/phys-fermat-lattice-universality/{README.md,STATUS.md,RESULTS.md}`
- `ai4s/phys-spiral-delone-uniform-density/{README.md,STATUS.md,RESULTS.md}`
- `ai4s/phys-supersoliton-degree-obstruction/{README.md,STATUS.md,RESULTS.md}`
- `ai4s/phys-so5-reduced-matrix-conjecture/STATUS.md`

Do not read anything else. Do not write files, run code, delegate, browse, or contact anyone.

## Context

The user asked us to find unsolved, not-too-hard problems from the 2009 Chinese physics book *10000 Selected Problems in Sciences: Physics*, launch five workers, check current status and SOTA, create folders under `ai4s/`, and push toward full solutions. Initial chapter-level choices were too broad. Then the user approved precise subproblems. A first set of five proof targets was completed, but none passed historical-openness certification because no primary source explicitly called them open and some full texts were inaccessible. The user then selected: **“Re-select with explicit open statements.”**

The five replacement targets are later precise mathematical questions in related primary papers, tied to two book chapters: higher-dimensional bilinear constructions (pp. 350–351) and Fibonacci/cone arrangements (pp. 541–543). They are not literal full book chapters. A candidate based on Caprio–Rowe–Welsh's “unproved” SO(5) formula was rejected after pre-2009 equivalent literature was found; it is included only so you can check that it is not counted.

## Task

Audit whether the integration may honestly report the following:

1. Each counted target has a correctly quoted explicit primary open/conjectural statement.
2. Each counted target has a complete written proof or exact counterexample for the precisely stated problem, with evidence label Certification rather than Discovery/priority.
3. Classical prior art and overlap are honestly credited, particularly Bacher (2014) for local lattices, Shirandami/Adiceam–Solomon–Weiss for finite-grid forests, Hlawka/Guo discrepancy, and the 2026 single-tau supersymmetric classification.
4. No target overstates a solution of the broad 2009 book chapter, the physical cone-energy problem, worldwide first priority, Lean verification, a symmetry-integrability theorem, or optimal visibility.
5. The CRW SO(5) candidate is excluded.

Look specifically for these defects: wrong quotation or OCR normalization; definition substitution; the wrong topology or use of rotations rather than translations; finite evidence promoted to universal proof; missing tied-shell or finite-core argument; incorrect transfer from local lattices; failure to handle affine translates; misuse of an absolutely-winning set; an incorrect generic super-soliton quantifier; and incorrect handling of parameter projection versus the external theta.

Report only real defects, with severity (blocker/major/minor), file and line, evidence and the precise correction. If none remain, state that the integration may report five explicit-question Certification results with uncertified priority. Separate mathematical correctness from novelty/history.

Return concise Markdown with: `verdict` (ready/ready-with-fixes/not-ready), `counted_targets` (exact titles), `findings`, and `required_report_wording`.