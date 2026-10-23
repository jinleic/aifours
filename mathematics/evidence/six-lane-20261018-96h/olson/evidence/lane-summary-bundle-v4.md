# math-2 Olson lane (96-hour continuation): summary bundle v4

Owner ContinueOlson.  Written after /bin/date 2026-10-19T02:57:25-0700.  Supersedes bundle v3 (2bddecc5...cd4c) by adding Sec. 2b.  Navigation
only; immutable texts, receipts, reviews and parent verdicts are the authority.  Lane: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson.

## 1. Accepted (parent verdicts; written scoped partials) -- unchanged from v3
S1-sharp (run review/olson-s1sharp-parent-verdict-v1.md); ROT-ZB and BAL-full (run review/olson-balfull-rotzb-parent-verdict-v1.md);
FB (run review/olson-FB-parent-verdict-v1.md 8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a): uniform INV*/ordered Olson for o_F <= p - 1 and
F - o_F >= 2(p - 1 - floor(2p/3)), p >= 7; terminal ROT-FB (a) 2 <= k <= p - 1 with (S1) at kappa^, (b) k = p with no zero-sum
of length 2kappa^.

## 2. Candidates (unreviewed)
- evidence/proof-KPS-cond-v3.md cfaf3cc5...ed01 (conditional on S(p)): FB-p, ARC0, ROT-KP+.
- evidence/proof-SLZ-EXT-v2.md 24953003...51: SLZ, EXT, PROP, RED; conditional: LS => INV*/ordered Olson for all o_F <= p - 1.

## 2b. Notes since v3 (not claims)
- evidence/notes-LS-base-v1.md dcb03fb3...b9 + erratum 1 evidence/notes-LS-base-v1-erratum-1.md c24a43d5...d561: induction on
  kappa, Lemma BB (boundary branch), residue of the LS base case; under S(p) the residue is branch (i) alone (every Y - z
  of a length-(p + 2kappa + 1) counterexample fails (S1)).
- evidence/notes-Sp-IDX1-v1.md 7af84f0d...1e53: S(p) <=> IDX1-odd(p+1); probe v13: S(p) holds for p <= 17 (complete; aid).
- evidence/notes-Sp-involution-reduction-v1.md 233b1cb1...843f: parent's involution reduction checked; all-unit
  reformulation of S(p).
- Checkpoints 010 (32ec1b06...e097), 011 (f95442d2...7e03).

## 3. Residual map (rotation half, terminal k <= p)
- k <= p - 1: kappa^ >= floor(2p/3) + 1 with (S1) failing (LS would close it; LS reduces to length p + 2kappa + 1, branch (i)
  plus, without S(p), branch (iii)).
- k = p: zero-sum of length exactly 2kappa^ (closed by KPS-cond under S(p)), or (S1) failing.
- Terminal k >= p + 1 and the reflection half o_F > p: open.

## 4. Limits
Written mathematics; no Lean, no human review, no literature search by the lane; a search miss is never novelty evidence.
