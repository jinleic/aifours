# math-2 Olson lane (96-hour continuation): summary bundle v5

Owner ContinueOlson.  Written after /bin/date 2026-10-19T03:24:44-0700.  Supersedes bundle v4 (47f1e373...9a1b).  Navigation only; immutable
texts, receipts, reviews and parent verdicts are the authority.  Lane: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson.

## 1. Accepted (parent verdicts; written scoped partials)
- S1-sharp (+ erratum 1): run review/olson-s1sharp-parent-verdict-v1.md; overlap disposition
  evidence/disposition-S1sharp-ZengYuan-v1.md 439b80debaafb015721730c940de8d4cbf45d5d59db042507b6910d3bd176315.
- ROT-ZB, BAL-full: run review/olson-balfull-rotzb-parent-verdict-v1.md; disposition evidence/disposition-BALfull-ROTZB-v1.md.
- FB (+ erratum 1): run review/olson-FB-parent-verdict-v1.md 8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a: uniform INV*/ordered Olson for o_F <= p - 1,
  F - o_F >= 2(p - 1 - floor(2p/3)), p >= 7; ROT-FB (a), (b).

## 2. Candidates for parent review (packet requested)
- evidence/proof-KPS-v4.md 68c4e7a7ff898219bfebee028052415cdb785b4b460b87e5cd4e7a6370510170 (relative to Import S(p)): FB-p, ARC0, ROT-KP+; Corollary for o_F <= p,
  kappa(w) <= floor(2p/3).  Supersedes proof-KPS-cond-v3.md.
- evidence/import-Sp-XiaYuan-v1.md d4d515cd4ff7b848d703f9337a3e9b6f12f85bd99319173207014519961381d7 (classical import note).
- evidence/proof-SLZ-EXT-v2.md 2495300317299fda49c0fb7d4b22daa81dfcecf1aef8c161361b9c04861bd751: SLZ, EXT, PROP, RED.

## 3. Notes (not claims)
- evidence/notes-LS-base-v1.md + erratum 1; evidence/notes-LS-propagation-v1.md be14d640f97f47e119f31d2e9b4bc5d7ef8c4f33129346e953435c6334c0de5d (EXT', EXT-p, PROP+, PAIR, LS+).
- evidence/notes-Sp-IDX1-v1.md, evidence/notes-Sp-involution-reduction-v1.md.
- Checkpoints 001-012 (latest checkpoints/012-Sp-import-LSplus-v1.md e5679ad2c1ce895efd6376528e74316b28107c2dfd0230d4de73b9c649ee6477).

## 4. Residual map (rotation half)
- Terminal 2 <= k <= p - 1: kappa^ >= floor(2p/3) + 1 with (S1) failing at kappa^ (closed by LS, or by LS+).
- Terminal k = p: (S1) failing at kappa^ (closed by LS+ for kappa^ <= p - 2); kappa^ = p - 1.
- Terminal k >= p + 1 and the reflection half o_F > p: open.  Non-dihedral groups untouched.

## 5. Limits
Written mathematics; no Lean, no human review; literature only through the parent's bounded audit (primary Xia-Yuan and
Zeng-Yuan texts unread); a search miss is never novelty evidence.
