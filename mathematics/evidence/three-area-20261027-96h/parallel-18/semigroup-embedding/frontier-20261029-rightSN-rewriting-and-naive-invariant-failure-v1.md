# A deletion rewriting system for RIGHTSN words, and why the naive evaluation invariant fails

**Status: NEW AUTHOR exact finite controls + written observations; UNREVIEWED / UNADOPTED.** Tooling and a documented dead end for item4 (`frontier-20261029-Q1-reduction-state-v1.md`, SHA `231a862f484d1d304d7094319e98f715fa5f5442522d227a7a87ac0df9a66157`). No theorem about Q1.

## 1. Rewriting system

Write c(B) for the content (set of letters) of a word B. Consider

- (I) `A x x B → A x B`;
- (D) `A x B → A B` whenever A is nonempty, `x∈c(B)` and the last letter of A lies in c(B).

Written soundness. Both rules are valid in every RIGHTSN band: (I) is idempotency, and (D) holds because the candidate normal form `nf(w)=(first letter, last-new-letter-from-right, nf(suffix after it))` is unchanged — the deleted occurrence is not a last occurrence and is not the successor of a last occurrence (its predecessor occurs again), and the first letter is unchanged. This soundness relies on the normal form being an invariant of RIGHTSN equality. That invariance is checked here only for words on three letters, where nf matches F3/ρ exactly (`frontier-20261029-SN-kimura-decomposition-checker-v1.py`).

Exact control. `frontier-20261029-rightSN-rewriting-checker-v1.py`, SHA `7045d3fe596d1fb2d314453cef414540b2ded5c91b480533594d08b47f43ef0a`, ran with python3.14 before ThuOct29 06:34:55 PDT2026. On all 3279 words of length ≤7 over three letters, every (I)/(D) step preserves nf, and greedy reduction reaches the canonical representative `rep(nf(w))` of each of the 51 classes. So on that range (I)+(D) is a terminating rewriting system with unique normal forms. Compare: LRB uses `A x → A` for x∈c(A); RRB uses `x B → B` for x∈c(B). RIGHTSN keeps the first letter and the successors of last occurrences.

## 2. The naive invariant fails

A natural attempt at item4 is to evaluate canonical words over labelled letters (u,s) — u being the entering weight — whenever adjacent labels are consistent, and to show that consistency and value survive every RIGHTSN step. The label-consistent RIGHTSN instance lemma (`frontier-20261029-rightSN-instance-lemma-and-canonical-certificates-v1.md`, SHA `d50d288dce5098d6e01eecf0c1585cd6512c6a59a1bec9557de2d8bbcf9dd2ec`) handles whole instances of `exeyexe=eyexe`. But the elementary deletion (D) on labelled letters does NOT preserve consistency. For S45 with its actor, the checker built 20000 random consistent words and found that (D) broke consistency in 10911 of 31533 applicable instances. Idempotency insertion `x→xx` also breaks consistency whenever x evaluates to a non-idempotent.

So any proof of item4 by an evaluation invariant must use a more flexible encoding. In Szendrei's group-actor proof the letters are G-translates of idempotents and products are partially defined by the existence of connecting elements (`frontier-20261029-primary-one-sided-globalization-reconstruction-v1.md`, SHA `0603d2562665884cfab1ec4885852f0d634c056b70ff4b28d7f7a92e8d8f6dfb`). A CS-actor analogue of that partial groupoid, together with this RIGHTSN deletion system, is the natural next attempt; it is not done here.
