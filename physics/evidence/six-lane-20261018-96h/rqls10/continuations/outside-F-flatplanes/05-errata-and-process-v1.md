# Errata and process disclosures for the outside-F package (v1)

Recorded after actual `/bin/date`: 2026-10-19T21:59:14-0700. ContinueRQLS10b. Frozen files are not edited; these
items are read alongside them. No item changes a theorem statement or its validity.

## Errata
E-1 (01-weyl-sparse-system-v1.md, Theorem 5, converse, distinctness of the 30 MUB-pair planes). The reason given
("vectors of different B_k are not orthogonal") is replaced by: a MUB-pair plane of B_k has diagonal (1,1,0,0,0) in B_k
and constant diagonal 2/5 in B_k' for k' != k (B_k is unbiased to B_k'); so planes from different k differ, and planes
from the same k differ because different pairs of basis vectors span different planes.
E-2 (04-qpik-group-and-stabiliser-theorem-v1.md, end of the proof of Theorem 1). Delete the garbled clause
"Conversely, Z^s commutes with... more precisely:"; the sentence that follows it is the intended converse argument.
E-3 (checkpoints/060-checkpoint-v1.md, a progress record, not a premise). Its digest block is garbled and contains a
transcription error. Exact digests (shasum output at 2026-10-19T21:58:59-0700):
  02-u-invariant-and-translates-v1.md         d84b74c53ef0ab379dd7772916217b6d096fef1ac7a1b221a97fe50218968af0
  03-involution-symmetric-planes-v1.md        b0828677b9a3e05934f577da14ecc093266cbfac2b5ca015181e3461bacbbe2c
(checkpoint060 wrote "...a9b3..." for the 03 digest; the correct digits are "...b9a3...").

## Process disclosures
P-1. Scope/knowledge exposure frozen first (00, 3e161b96...31e5) before any derivation; Q1-Q3 and outcomes unchanged.
P-2. Metadata-only `ls` was used at 2026-10-19T21:25:39-0700 to check directory/checkpoint absence; the frozen CLI list
names /bin/date, shasum, chmod, wc. Disclosed as a metadata-only deviation; no computation, script, import or test ran.
P-3. Parent IRC during the slice (21:4x): E1 accepted at literal scope (ad790caa...e872); note 02 cites only that accepted
interface. Parent IRC (after 21:58): owner workload throttle RUN/control/owner-workload-throttle-one-third-v1.json
(3ba3ca96e2a869d5fee8fa76186184e5d380cc296fec5713da9d97c35776f9de): finish this deliverable at its frozen scope, no
extra packets/variants/optional work, then park. Accordingly Q3 (asymmetric planes) is delivered as an exact remaining
obligation, not pursued further.
P-4. All files written to fresh paths, frozen 0444; no same-path rewrite. No unreviewed candidate (internal-F E2/E3,
F-closure) is a premise. Single author, unreviewed; parent owns review and verdict. Runtime HOLD unchanged.
