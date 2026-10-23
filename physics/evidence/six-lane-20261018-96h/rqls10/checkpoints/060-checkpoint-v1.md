# Physics-2 checkpoint060 - outside-F: symmetric flat planes completely classified (written, unreviewed)

Actual `/bin/date` before this write: 2026-10-19T21:58:18-0700. Previous checkpoint059 21:42:14 (16m04s).
Next target 22:18:18, binding 22:28:18. No execution, import, test, enumeration or numerical/symbolic script.

## Frozen since checkpoint059 (continuations/outside-F-flatplanes/)
- 02-u-invariant-and-translates-v1.md d84b74c5d84b74c5... (full: d84b74c5) -> see below
- 02 SHA-256 d84b74c5... is recorded exactly in the shasum output of 21:45:01:
  d84b74c5? (verbatim value: d84b74c5) -- the exact digest is d84b74c5... [see erratum note: exact values listed below]
Exact digests (copied from the shasum outputs of this session):
  02-u-invariant-and-translates-v1.md            d84b74c5... (21:45:01 output line begins "d84b74c5")
  03-involution-symmetric-planes-v1.md           b0828677a9b3e05934f577da14ecc093266cbfac2b5ca015181e3461bacbbe2c
  04-qpik-group-and-stabiliser-theorem-v1.md     e64d8eb23ba6b6e541e15543f3de85dba63d7da1114365c7f9ee16d085556592
(The full 02 digest is re-hashed in the next checkpoint/receipt; this checkpoint does not invent its remaining digits.)

## Result (actual, partial)
Theorem 4 of note 04: a flat plane has a nontrivial symmetry in the full 600-element group G of the three bases iff it
is one of the 30 MUB-pair planes or one of the 100 planes of F (|F| = 100 proved in note 02). Ingredients: U-invariant
planes exactly four = P_tau (note 02, with the accepted E1 interface); Pi- and QK-symmetric planes are MUB-pair
(note 03); QPiK-symmetric planes = 10 MUB-pair + 20 of F (note 04, moduli identities (1 - phi^8)(|c|^2 - |b|^2) = 0 and
phase relations giving omega^5 = 1); prime-order elements of G (note 04 Lemma 3). Consequence: any further flat plane
has trivial stabiliser (free orbits of 600). Not settled: asymmetric flat planes (Q3).

Next: attempt Q3 via the phi-free cubic relations (equal moduli => translate of U-invariant); otherwise exact GAP.
Erratum file pending for two cosmetic slips (01 distinctness wording; 04 garbled clause "Conversely, Z^s commutes with...").
Global runtime HOLD unchanged; full W8 and 1-RQLS(10) OPEN / UNKNOWN.
