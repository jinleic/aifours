# ROT-SING+ parent commentary erratum v1

Recorded at 2026-10-19T11:27:45-0700. Read after immutable [proof-ROT-SINGPLUS-v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/terminal-pplus1-singletons/proof-ROT-SINGPLUS-v1.md) `68865d55311128167ead7e3e966e92545520eb5224e4b44458ab469af67a8d9d`. Disposes the single MINOR finding of Codex review [olson-ROT-SINGPLUS-codex-v1](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ROT-SINGPLUS-codex-v1.prompt.stdout.txt) `c205c24f3f2d49ff99d1299c9fa9c8f48abbc39b6d81420b784346ac260c1f84` (main and strengthened multiset ACCEPT-WITH-FIXES, 0 FATAL/0 MAJOR/1 MINOR). The change is confined to the explanatory remark in section 7; no statement, lemma, case split or proof step changes. The Old span occurs exactly once.

## Remark, section 7 (proof lines 133-136)

Old:
````text
- Preserved failed branch (exact). The k = p argument (one arc, omit p letters, all b-letters free) gives only p-1 free nonzero
  weights here because an arc omits p-1 letters; when all 2p-1 letters a lie on the filler side (type H1, every arc), the free letters
  are the p-2 letters of B and Sigma misses one residue. This is the predicted "fails by one" step; Lemma ER (empty runs, including the
  FOUR-change pattern) and the run count in Sec. 6 replace it.
````

New:
````text
- Preserved failed branch (exact). For an empty negative run, K = p-1 and N_z = B~ has p-2 nonzero occurrences. RS(b) gives at
  least p-1 subsum residues; avoidance forces exactly one missing residue. This is the predicted "fails by one" step; Lemma ER (empty
  runs, including the FOUR-change pattern) and the run count in Sec. 6 resolve this case. (The earlier wording conflated the omission
  budget K, the number of free nonzero weights and the number of subsum residues; p-1 free nonzero weights would already give full
  coverage by OM', and placing every a-letter in Pi_+ does not by itself make the free weights equal B~.)
````
