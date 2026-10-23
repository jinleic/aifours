# LKTS(57): independently verified finite existence certificate

## Mathematical result

**An LKTS(57) exists.** The explicit certificate lists 55 pairwise block-disjoint Steiner triple systems on `X={0,...,56}`, each resolved into 28 parallel classes of 19 triples. Each class partitions X; every pair of points occurs exactly once in each system; the union is exactly all 29,260 three-element subsets of X.

This resolves the fixed-order target in the frozen six-lane contract. It does **not** resolve the book's existence question for every admissible order. Priority remains under investigation; there has been no human peer review or publication.

## Evidence

| Gate | Observed result | Artifact |
|---|---|---|
| Raw witness identity | SHA-256 `09a9d8ca0602ed28541e170ada7f096871311c29fd4515b6fea3e25f72b05f09` | `lkts57-parent-inputs-v1/lkts57_g513.txt` |
| Parent independent verifier | Direct point partitions, pair uniqueness, inter-system disjointness and explicit complete triple-set equality all pass | `check_lkts_independent.py`, `lkts57-parent-verification-v1.json` |
| Prior dossier verifier, executed by parent | PASS for the same pinned input; checker SHA-256 `7cebb330ea7fe26efabd3c3a7ad7a61af12704a900e2ebf8c9d24daf3c11ed2d` | `mathematics/kirkman-large-sets-57-87/work/check_lkts.py`; original tool output in the conversation |
| Independent Codex execution | `gpt-6.1-sol`, maximum effort: **RESULT: VALID** using its own in-memory verifier before reading the parent checker; all 30,856 noncomment lines accounted; all mathematical conditions checked | `lkts57-codex-verification.md` |
| Positive controls | Previously verified LKTS(9), cyclic LKTS(15), Denniston LKTS(15) all pass the parent checker | `lkts57-parent-controls-v1.json` |
| Negative controls | Eight targeted mathematical/format corruptions rejected for the intended `CertificateError`; Codex separately rejected 22 malformed/misplaced input variants | `lkts57-parent-controls-v1.json`, `lkts57-codex-verification.md` |
| Construction action | Parent reconstructs the group of order 513, point transitivity, constituent orbits `19+9+9+9+9` and triple-orbit sizes `19` once, `171` six times, `513` fifty-five times; all generator images of all constituent block sets verified | `check_lkts57_action.py`, `lkts57-action-parent-check.json` |

The bound evidence and review dispositions are in [`lkts57-independent-verification-receipt.json`](lkts57-independent-verification-receipt.json). All verification above is finite computation, not a Lean-kernel existence proof.

## Construction scope

The point generators are `tau(x,i)=(x+1,i)`, `nu(x,i)=(4x,i+1)` and `rho(x,i)=(x,i+1)` on `Z_19 x Z_3`, with label `19i+x`. They act on the **underlying STS block sets**. They do not all preserve the chosen resolution on every constituent: that stronger assertion is neither needed for an LKTS nor supported by the certificate. Resolutions are supplied separately for all constituents.

The raw witness's validity does not depend on the search solver, an automorphism lemma, an alleged forced orbit structure, or solver UNSAT/UNKNOWN reports. Written construction lemmas and compact seed regeneration are additional explanation/provenance gates, being checked separately.

## Primary-source comparison

The parent opened the latest [arXiv record](https://arxiv.org/abs/2607.21521) and [Wang v1, Section 4](https://arxiv.org/html/2607.21521v1#S4). Its only listed version is dated 23 July 2026. It defines LKTS with the same resolvability and disjointness conditions, and identifies 57 and 87 as the two possible exceptions below 200. Thus this witness answers a target explicitly identified there. That source does not establish absence of a later construction.

**FRONTIER: NOVELTY-UNCLEAR.** The dedicated priority search is in progress. Safe wording now: “An explicit independently checked LKTS(57) certificate; no priority claim yet.” No claim that the universal conjecture is solved, that a method is new, or that a model review is human peer review.

## Remaining gates

- Freeze and independently regenerate the compact seed construction, retaining the exact witness bytes.
- Resolve the primary-source priority screen and any construction-lemma referee findings.
- Complete a separate pure-kernel existence attempt if feasible; do not relabel finite checks as Lean verification before it passes.
- Continue the mathematics slot at LKTS(87) after preserving the 57 package; record any transition explicitly.
