# math-2 Olson lane (96-hour continuation): summary bundle v1

Owner ContinueOlson.  Written after /bin/date 2026-10-19T00:49:58-0700.  Navigation and status only; immutable texts, receipts and
parent verdicts are the authority.  Lane: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson.

## 1. Results

| item | status | text of record | review / verdict |
|---|---|---|---|
| Lemma S1-sharp: (ZP_kappa) => (S1_kappa) for every prime p >= 5 and every 0 <= kappa <= floor(2p/3); sharp (F1 for every p; F2 for p = 1 mod 3) | CORRECTNESS-ACCEPTED SCOPED PARTIAL | evidence/proof-S1-sharp-v1.md 992ab63f40aa08626560ccf121b0004a08588fdb24805ff4eb30d25a2150cb0c + erratum 1 evidence/proof-S1-sharp-v1-erratum-1.md bf504cdf8b8cfd3e96a26609d00162d365415b3481ca3a7dcbd7112af82f9507 | Codex gpt-6.1-sol AWF 0/0/3; Claude claude-opus-5-5 AWF 0/0/9 + 0/0/5; parent verdict run review/olson-s1sharp-parent-verdict-v1.md bd4a0a60cdea0765517ca33a9a2ddefb664b24fad7b20e709835bbdec1e94f41 (+ parent wording overlay) |
| Corollary: INV* (length 4p-2) and ordered Olson for D_2p (length 4p-1) for every word with 3 o_F <= 2p+1, every prime p >= 5; S1(g)'s residual terminal pairs (incl. (21,20) at p = 31) discharged; new coverage only p >= 31 | same | same | same |
| Lemma BAL1, Lemma ROOM, Theorem ROT-ZB (terminal 2 <= k <= p-1, 2kappa^ + k <= 2p-1, (B)), Corollary: INV* and ordered Olson for o_F <= p-1 and 2F >= 2p + 3o_F - 5, every prime p >= 7 | CANDIDATE, unreviewed | evidence/proof-ROT-ZB-v2.md 65dbedbf8f679b583a0186c84d64ede9c0564fc15ca8b13404c4766019f4f5f1 (v1 9d2da0a0...a72b2a never sent) | reviews to be arranged by parent |

## 2. Notes (not claims)
- evidence/notes-kp-under-zb-v1.md 6cadd03d62751106c27acd42d61e85c4ad6141131e34f9aeba50ac11c3a18ddc: at terminal k = p the
  ROT-ZB tools close the subcase t < kappa^ for kappa^ <= min((p+7)/4, p/2); the exact remaining Q1a obstruction is
  t = kappa^ (zero-sum-free complement of length exactly p; S(p) open).
- Balance beyond (B) (needed to extend ROT-ZB to all 2kappa^ + k <= 2p-1): unproved; derived necessary conditions for an
  unbalanced longest zero-sum are recorded in checkpoints 004/005.

## 3. Finite aids (never premises)
- probe v1 (restricted representation; circular w.r.t. S1-sharp Steps 3-8): evidence/probe-v1/RECEIPT-run1-v1.md
  4351a750cd2f60fa4cd186962649d83cb67e2199c6ef9425fe8a929ee3393f8f.  Process deviation: PID only from a later ps census.
- probes v2/v3 (support <= 3 exact, independent of Steps 3-9): RECEIPT db784ec3...70a5 and c4f89301...c9bc.
- probe v5 (balance, support <= 3, p = 13, 17, 19 partly): RECEIPT 932f3a67d541465b247038d18cf341a19739696e7dfbcc1b50f91a30700abf9b.
- probe v4 (balance) frozen b3a8a7dc...a6d3, never run (superseded by v5).  launcher v1 54b934aa...7f81742 frozen, never used.

## 4. Residual map after S1-sharp (+ ROT-ZB if accepted)
Rotation half: terminal k = p with kappa^ >= 2 (Q1a); 2p/3 < k <= p-1 with (B) failing or 2kappa^ + k > 2p-1, and T4
failing.  Reflection half: o_F > p.  Non-dihedral groups untouched.  Dihedral success would not settle the all-groups
ordered Olson statement.

## 5. Limits
Written mathematics relative to explicit imports (Savchev-Chen/Yuan index-one theorem: author statement via the parent
import record; 2007 proofs not read; S1+, ROT-ZR lemmas, GRX/normal form/DAV/K1/K01/KETA/SHgen/SHgen-E/restricted
REFL/ledger/RGR-LONG at their accepted scopes).  No Lean, no human review, no literature search for the new lemmas; a
search miss would never be used as novelty evidence; correctness, priority and significance are separate.
Process: all lane files exclusive-created; no deletions; no tool timeouts on probes (self-budgets only); probes v2-v5 via
the stdin-gated launcher with pre-compute ownership records.
