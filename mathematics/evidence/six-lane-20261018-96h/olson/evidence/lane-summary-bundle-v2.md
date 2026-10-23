# math-2 Olson lane (96-hour continuation): summary bundle v2

Owner ContinueOlson.  Written after /bin/date 2026-10-19T01:17:50-0700.  Supersedes bundle v1 (1d9b2e36...83cd).  Navigation and status
only; immutable texts, receipts, reviews and parent verdicts are the authority.  Lane: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson.

## 1. Results and candidates

| item | status | text of record | reviews / verdict |
|---|---|---|---|
| Lemma S1-sharp: (ZP_kappa) => (S1_kappa), p >= 5, 0 <= kappa <= floor(2p/3); sharp | CORRECTNESS-ACCEPTED SCOPED PARTIAL | evidence/proof-S1-sharp-v1.md 992ab63f...0cb0c + erratum 1 bf504cdf...f9507 | Codex AWF 0/0/3; Claude AWF; parent verdict run review/olson-s1sharp-parent-verdict-v1.md bd4a0a60...4f41 |
| Corollary: INV* and ordered Olson for 3o_F <= 2p + 1 (any F), p >= 5 | same | same | same |
| Lemma BAL1, Lemma ROOM, Theorem ROT-ZB, Corollary OLSON-ZB (o_F <= p-1, 2F >= 2p + 3o_F - 5, p >= 7) | REVIEWED: Codex ACCEPT x4 (no findings); Claude ACCEPT x3 + Corollary AWF 0/0/6; erratum frozen; parent verdict pending | evidence/proof-ROT-ZB-v2.md 65dbedbf...f5f1 + erratum 1 evidence/proof-ROT-ZB-v2-erratum-1.md a181edbb...c0de | run review/olson-rotzb-codex-v1.prompt.stdout.txt 960a6033...f7f2; run review/olson-rotzb-claude-v1.prompt.note.md 6c1b7108...72f2 |
| Lemma BAL-forall (L >= 2t + 1 => every longest Z balanced w.r.t. every index-<1 g), Theorem ROT-ZB+ (2 <= k <= p-1, 2kappa^ + k <= 2p - 1), Corollary OLSON-ZB+ (o_F <= p-1, F >= 2o_F - 1, p >= 7) | CANDIDATE, unreviewed (parent reading) | evidence/proof-BALfull-v2.md dffbfea8...a3e1 + pre-review erratum 1 evidence/proof-BALfull-v2-erratum-1.md e0f826a2...1fcf; scope evidence/BALfull-scope-v1.md f2b82c5e...2f315 | - |

## 2. Notes (not claims)
- evidence/notes-ROT-T-conditional-v2.md 57381452...70f4: rotation rigidity conditional on the longest zero-sum length t
  ((i) R - 2t >= p + 1, (ii) R - 2t >= 2t + 1, (iii) 2t <= 2p - k, (iv) 2t <= 2p - 2k + 2kappa^ - 1).  Remaining rotation
  obstruction = long longest zero-sums (t near kappa^), incl. k = p with t = kappa^ (S(p)).  Supersedes
  evidence/notes-kp-under-zb-v1.md 6cadd03d...8ddc.
- In the high cells (2kappa^ + k >= 2p, k <= p - 1) balance alone does not suffice: at t = kappa^ ROOM needs L >= 2t and
  SHgen (H) needs n+ <= 2p - 1 - k (or (2p - 1 - k)/2 without ROOM), while balance gives n+ >= t >= (2p - k)/2.

## 3. Finite aids (never premises)
- probes v1-v5: see bundle v1 Sec. 3.
- probes v6/v7/v8 (BAL-forall falsification, degenerate-example extraction, sharpness search):
  evidence/probe-v6/RECEIPT-v6-v8-v1.md a011b83c...562d.  0 counterexamples (exhaustive p = 7, R = 10..17; random p = 11..19);
  the L < 2t unbalanced items are degenerate (2t > 2p); no unbalanced longest Z found inside t < p, p + 1 <= L <= 2t.

## 4. Residual map
- After ROT-ZB (if parent-accepted): rotation half {k = p, kappa^ >= 2} OR {(2p+1)/3 < k <= p - 1, kappa^ >= 2,
  4kappa^ >= 2p - k + 2}.
- After BAL-full (if accepted): {k = p, kappa^ >= 2} OR {(2p+2)/3 <= k <= p - 1, 2kappa^ + k >= 2p}; uniformly, for
  o_F <= p - 1 only 3o_F >= 2p + 2 with F <= 2o_F - 2.
- Reflection half o_F > p untouched; non-dihedral groups untouched; dihedral success would not settle the all-groups
  ordered Olson statement.

## 5. Withdrawn
- ROT-ZB v2 Sec. 6 cell counts (p = 31: 28/202, p = 61: 129/803, p = 101: 386/2255) and their quotations in checkpoint 005 and
  the parent notice: depended on unrecorded kernel planning functions (T3/T4/T5); withdrawn by ROT-ZB erratum 1 (m2).

## 6. Limits
Written mathematics relative to explicit imports (index-one/Savchev-Chen statements via the parent import record; 2007
proofs not read).  No Lean, no human review, no literature search; a search miss would never be novelty evidence.  All
lane files exclusive-created; no deletions; probes v2-v8 through the stdin-gated launcher with pre-compute PID records.
