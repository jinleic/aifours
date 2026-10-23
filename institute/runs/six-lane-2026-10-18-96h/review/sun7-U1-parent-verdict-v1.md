# Sun k7: one marked vertex (any markers 2/3/5 on it) excluded

Recorded at 2026-10-19T03:12:58-0700.

**CORRECTNESS-ACCEPTED (scoped partial, written mathematics), with the mandatory overlay.** Theorem K7-U1: there is no
class-K7 configuration with exactly one marked vertex z, where m_z = 2^E 3^A 5^B with all exponents unbounded
(including E, A >= 1 together), in any group (finite-core lift via R0). ROW-1*, CROSS* and LIGHT* are accepted at the
U1 scope. **K7 remains OPEN**; full Sun(7) is not claimed.

## Evidence
- [Candidate](../../../../mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-U1-v1.md) `d4e6cdc9e11320bee2456e589459c2b0e961bec466e1b7c05e7ff4003e751965`
  (successor worker Sun7K62Successor; written, single author).
- [Mandatory erratum](../../../../mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-U1-erratum-v1.md) `a795c5b7cafca0dbfdc4c250f92262b2f8f0179ee441cb89d02ae65be3b999d5`:
  E-1 title/frontier (|M| = 1 mandatory), E-2 explicit k3 = 3 remainder weights (x = 1: (1,1) total 8; x = 2: (1/2,1/2)
  total 6; x = 4: (1/2,1/2) total 7), E-3 LT labels, E-4 description of Z2's x = 5 removal, E-5 pinned scopes,
  E-6 valuations and symmetry. No statement change.
- [Codex](sun7-U1-codex-v1.prompt.stdout.txt) `d93325bfdd7c58b4fcf54c5defbc7eb3f474cc791b05ca8240e0282daff8e1ec` (receipt identity gpt-6.1-sol, read-only, max): ACCEPT, 0 FATAL /
  0 MAJOR / 1 MINOR (E-2).
- [Claude](sun7-U1-claude-v1.prompt.note.md) `264a1577b0d17ebfd72e841be3cbccf296111ea82f6ca191e7e768c5a5986089` (receipt init model claude-opus-5-5): ACCEPT-WITH-FIXES,
  0 FATAL / 1 MAJOR (frontier sentence and title only) / 7 MINOR; all disposed by the erratum.
- Parent: full read and independent re-derivation before the reviews (no gap); erratum read in full against both
  reports; E-2 weights checked against the strict LFC bound (< 6) and the allowed-set feasibility stated there.

## Exact remaining K7 frontier after this verdict
With accepted K7-M0 (M empty), K7-M1, K7-Z2 (2-marker, no 3-marker), K7-35 (no 2-marker, 3 and 5 on distinct
vertices) and now K7-U1 (|M| = 1), K7 remains open exactly for |M| >= 2 with both a 2-marker and a 3-marker present:
(a) 2- and 3-markers on different vertices (5-marker absent, on one of them, or on a third vertex); or
(b) 2- and 3-markers together on z with the 5-marker on y != z.

## Limits
Written mathematics only; model reviews only; no Lean, human review, novelty or significance claim beyond the
[bounded Sun priority note](sun7-priority-parent-note-v1.md). Exploratory probes are not premises.
