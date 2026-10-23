# MOQLS(8) P1-B3: simultaneous-pair genuine-GB reduction

Recorded at 2026-10-19T13:13:57-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL — conditional written reduction only.** Candidate [B3 pair proof](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/review/B3-PAIR-GENUINE-GB-CANDIDATE-v1.md) `66f1e55719e1f755c480d0e9064071616089394291f2827f1b5b40fb1e0ae734`, read with [parent erratum](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-pair-genuine-parent-erratum-v1.md) `98025ddebb6a2091ba584368ab44c1eb599534b0ec9e53b4dce72ff450771a59`. It proves neither UNSAT input, no n=8 theorem and no counterexample.

## Exact accepted implication

For every genuine five-set of pairwise-orthogonal QLS(8) satisfying the stated standard row 0, SB2 with the weight-three Q1 witness, and the exact P1-B3 template:

1. At least two column-0 support matrices among X2,...,X5 are permutation matrices in the SAME configuration.
2. One common genuine isotopy and square relabelling from {id,a,b,c,ab} preserves the template and sends a selected pair to squares {2,3} or {2,4}. ROWLEX is a consequence of the fixed template, not a separate required hypothesis.
3. Reapplying accepted GB necessity to that moved genuine configuration produces a SINGLE canonical assignment satisfying H_23=GB_B3 AND M2 AND M3 or H_24=GB_B3 AND M2 AND M4.
4. Therefore **UNSAT(H_23) AND UNSAT(H_24)** implies there is no genuine configuration with those hypotheses. **Both UNSAT premises are unproved.**

The base GB_B3 identity is the pinned P1-B3 entry of GBBINDING: SHA256 `f8fd0a51d8ff30069c105b52c20fdc02ad3f22a15a500e95014e5aac4954d487`, 350551015 bytes, 3803745 variables and 17025620 clauses. Each M_s is the 126 own-name primary at-most-one binaries in candidate section 1. H_23/H_24 are conceptual conjunctions only: no new DIMACS bytes, binding or certificate exists.

## Import and verification boundary

[G] GB necessity/genuine normal-form parent verdict `f529224e82ce6126d1a1fbc5776330d4b9ac6970faadb681acb3a8b56358ce0c`, read with [D,E], is accepted only at its original scope. The U/T16 connection to arbitrary genuine non-classical five-sets remains conditional; WMAN/template and shared NF imports are not independently established by GB's independent CNF construction. No arbitrary-Boolean-model symmetry or auxiliary-extension theorem is proved here.

- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-pair-genuine-codex-v1.prompt.stdout.txt) `c0c7e7b04140d86ee1996889a8d4406475eaa205970a8614c0709290f40a30c6`: ACCEPT, 0 FATAL/0 MAJOR/0 MINOR.
- [Claude](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-pair-genuine-claude-v1.prompt.note.md) `735d06162df96bd68a4bae94e2fad0e561987acf37965d364ffa5a14a06f092a`: ACCEPT-WITH-FIXES, 0 FATAL/0 MAJOR/6 MINOR, disposed by the mandatory erratum.
- Parent hand checks: a 7x7 non-permutation support satisfying nonempty rows and no singleton row intersections needs >=9 ones; 16+3*9+7=50>49; all six literal pair maps; sigma(T_i)=T_rho(i), including ab; tau(s)=sigma(s+2)-2; the same assignment satisfies both selected tails. The original freeze `516784fc` records the ten snapshot/input pin checks.

## Unchanged

GB remains **15/18**, with its three recorded UNKNOWNs. This does not replace B3.M2, refute arbitrary models of GB_B3 or GB_B3 AND M2, discharge A10/A11, reuse GA certificates as GB proof, or change B1/B2/B5. No further native work is admitted. No novelty, priority, Lean or human-referee claim.
