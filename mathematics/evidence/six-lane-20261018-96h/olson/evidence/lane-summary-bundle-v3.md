# math-2 Olson lane (96-hour continuation): summary bundle v3

Owner ContinueOlson.  Written after /bin/date 2026-10-19T02:43:55-0700.  Supersedes bundle v2 (5ada5d13...c71b).  Navigation only; immutable
texts, receipts, reviews and parent verdicts are the authority.  Lane: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson.

## 1. Accepted (parent verdicts; written scoped partials)
| result | text of record | verdict |
|---|---|---|
| S1-sharp: (ZP_k) => (S1_k) for k <= floor(2p/3); corollary INV*/ordered Olson for 3o_F <= 2p+1 | evidence/proof-S1-sharp-v1.md + erratum 1 | run review/olson-s1sharp-parent-verdict-v1.md bd4a0a60...4f41 |
| ROT-ZB (BAL1, ROOM) | evidence/proof-ROT-ZB-v2.md + erratum 1 | run review/olson-balfull-rotzb-parent-verdict-v1.md 56b988ee...1bc0 |
| BAL-full (BAL-forall, ROT-ZB+): o_F <= p-1 and F >= 2o_F - 1 | evidence/proof-BALfull-v2.md + pre-review erratum 1 | same verdict |
| FB (full balance with room), ROT-FB (a) terminal 2<=k<=p-1 with (S1); (b) k=p with no zero-sum of length 2kappa^; uniform: o_F <= p-1, F - o_F >= 2(p-1-floor(2p/3)) | evidence/proof-FB-v1.md 339dcadc...cc6b + erratum 1 33de46d2...e202 | run review/olson-FB-parent-verdict-v1.md 8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a |
Dispositions: evidence/disposition-BALfull-ROTZB-v1.md 55138906...16c4.

## 2. Candidates (unreviewed)
- evidence/proof-KPS-cond-v3.md cfaf3cc5...ed01: CONDITIONAL on S(p): Lemma FB-p (L = p), Lemma ARC0 (rho_c/rho_0 families),
  Theorem ROT-KP+ (k = p cells reduce to S(p)).
- evidence/proof-SLZ-EXT-v2.md 2495300317299fda49c0fb7d4b22daa81dfcecf1aef8c161361b9c04861bd751: Lemma SLZ, Lemma EXT,
  Corollaries PROP and RED (LS reduces to its threshold length p + 2kappa + 1); conditional: LS for all kappa <= p-2 =>
  INV* and ordered Olson for all o_F <= p-1.  LS itself is the parent's conjecture, NOT proved.

## 3. Scopes, notes, aids
- Scopes: evidence/BALfull-scope-v1.md, evidence/TMAX-scope-v1.md 858d9a3e...568f (answered by FB: no obstruction),
  evidence/LS-scope-v1.md 80ae8041...dfa.
- Notes: evidence/notes-ROT-T-conditional-v2.md (superseded in substance by FB), evidence/notes-kp-under-zb-v1.md.
- Receipts: probe-v6/RECEIPT-v6-v8-v1.md a011b83c...562d; probe-v10/RECEIPT-v9-v10-v1.md a5d3da6a...a134;
  probe-v11/RECEIPT-v11-v1.md b7e4c9ee...4d97; v12 recorded in proof-SLZ-EXT-v2.md Sec. 6.

## 4. Residual map (rotation half, terminal k <= p), after FB
- kappa^ >= floor(2p/3) + 1 with (S1) failing at kappa^ (would follow from LS; LS reduces to length exactly p + 2kappa + 1;
  at p = 11, kappa = 9 failures of (S1) exist up to length p + 2kappa - 1, so LS is within 2 of sharp there).
- k = p with a zero-sum of length exactly 2kappa^ (S(p) via KPS-cond), and k = p with (S1) failing.
- Terminal k >= p + 1 and the reflection half o_F > p: open.  Non-dihedral groups: untouched.

## 5. Limits
Written mathematics; no Lean, no human review, no literature search; a search miss is never novelty evidence.
