# ROT-PP1 parent ancillary wording erratum v1

Recorded at 2026-10-19T12:19:08-0700. Read after immutable proof `99143ea503a01a6376bed91a2a7ca8b91591617351f35ce4864117bf2949f1ca` and obstruction `4839cbd37d178038747a07e6c603ba344718d1c4c74508cfc7229aae417528dc`. Parent source-read found the ancillary failed-route F1 statement conflates an occurrence bound with an upper bound on subset-sum residues; the corrected text asserts only absence of a guaranteed full-cover lower bound. No theorem, case split or mathematical proof step changes. Old span occurs once in the obstruction note.

Old:
````text
- (F1) Full coverage from one pattern (the OM'-type step of the k = p and kappa^ = p-1 singleton arguments): by Lemma P every
  non-constant pattern has at most p-2 letters off its dominant signed value, so the omission sums of one pattern cover at
  most p-1 residues. Replaced by the window (W), the heavy run and comparisons between the all-plus, empty-run and empty-pair
  patterns.
````

New:
````text
- (F1) Full coverage from one pattern (the OM'-type step of the k = p and kappa^ = p-1 singleton arguments): Lemma P permits
  at most p-2 letters off the dominant signed value. This does not GUARANTEE full residue coverage from the Cauchy-Davenport
  lower bound alone; it is not an upper bound of p-1 on the actual subset-sum set. The proof instead uses window (W), a heavy
  run and comparisons between the all-plus, empty-run and empty-pair patterns.
````

All proof navigation references to obstruction-ROT-PP1-v1.md now mean the delivered obstruction-ROT-PP1-v2.md, read with this overlay. Earlier drafts remain immutable and are not inputs.
