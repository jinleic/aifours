# TCW scope v1 (frozen before any derivation)

Owner: OlsonThirdCutWindow (written-mathematics slot, Olson lane, throttled math2 slot).
Freeze time: 2026-10-20T03:27:24-0700 (`/bin/date`, taken immediately before exclusive creation of this file).
Authority: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-olson-third-cut-window-transition-v1.json
(sha256 201201cd69cc7148e22ccea814d5f61f6e46e540ddd64546fe5a5fd2436c25cf, LF lines 1-44, read in full).

## 1. Target (Theorem TCW candidate)

For every integer kappa >= 4 such that p = 4kappa - 5 is prime
((kappa,p) = (4,11), (6,19), (7,23), (9,31), ...), no word of length 4p-2 over
the dihedral group D_(2p) that has no identity subword of length 2p (subword =
terms taken in increasing original index order, product in that order) has an
admissible normal form with terminal k = p+1 and kappa_hat = kappa.

Antecedent is the full existential one: SOME admissible normal form (NF in the
sense of the accepted NF definitions at their pinned ranges), extra reflection
pairs allowed anywhere in the odd blocks, the genuine empty-run rule. No o_F,
nonempty-run, rotation-pair or rigidity hypothesis is added.

Deliverable: EITHER a complete written proof of the target, OR the exact first
failing lemma with every proved partial range named. The cell (kappa,p) = (4,11)
must be explicitly covered or explicitly left open with its exact obstruction;
it is never dropped silently. No other cell and no full-Olson scope expansion.

## 2. Allowed imports (accepted; cited only at their exact accepted scope)

Every import is cited as path + whole-file sha256 + inclusive LF line range and
is re-hash-checked before use. Hashes below were checked by `shasum -a 256`
before this freeze.

- FCW parent verdict: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FCW-parent-verdict-v1.md
  b28837c9c8a9549b99a6c2205e8bbe40d65ab1aad265595c511395d4c1738f71
- FCW parent erratum: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FCW-parent-erratum-v1.md
  e56bf0f337d7d670be99075829217431cf605437320dd3414cde75c3d1ae2413
- FCW proof (accepted only for p = 4kappa-1; its lemmas are not reused at
  p = 4kappa-5 without re-derivation): /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-first-cut-window-boundary/proof-FCW-v1.md
  c23fd0378f68611070e3bf0fd74d66d1f7ad859bb01ccc1af4ce9a77cf4aaecf
- FCW excerpt manifest (source of the pinned ranges below): /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-first-cut-window-boundary/review-excerpts-FCW-v1.json
  a3225345e84476d296357d64e6055dbfd95ad79e71521b8431969e733a53e143
- USK verdict and errata: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-USK-parent-verdict-v1.md
  6d3358ce3f1e9e95a366f2b32f10adbc73df607bc62723f561567dce1a53de18;
  olson-USK-parent-erratum-v1.md 85718782c14dcb913706d5b7245ebfda1ef50ef1e9e7661d671a9ecbfcf4519e;
  olson-USK-parent-erratum-v2.md 4f3a2636594787337ebe8294dc086f8a3af9dccea89d5599e95e802e95590bfe (same directory)
- K0T verdict: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-K0T-parent-verdict-v1.md
  4a2a2ffd8d8624c33c0f7cc1265cf679c18ac3a9c63565bc093b2e8afc8bf8ba
- LOWER-K1 verdict: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-LOWER-K1-parent-verdict-v1.md
  93ea601c1255f52a8a186002e9e46986c99db1c81a1c4aba68eb6143ca926e83
- LOWER parent erratum (m(P) = half the sign transitions; theta only through
  explicit pairs): /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-LOWER-parent-erratum-v1.md
  087ab3ae6e880633b26658ff68e8f787bdb59758a4a0662bc7744aeea5b96377
- Pinned accepted-input ranges listed in the FCW manifest, each at its own
  accepted scope (NF, GRX, (SR) via PL Sec. 2, SC0 read through the
  minimal-zero-sum step Y'z, ZSTRUCT/FB in (S')):
  - proof-LOWER-v1.md (lowerhalf-terminal-cell) 251c8dca1c34be7b76432dc50d13368b11a7bf6da6bbb8bd31e4ee18e7cd476d lines 40-129
  - proof-ROT-few-E-v4.md 'ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f' lines 28-43
  - notes-GRX-v1.md afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 lines 7-20
  - olson-zx-s1c-parent-verdict-v1.md 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af line 19
  - olson-index-one-primary-statement-parent-v1.md e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6 lines 1-11
  - olson-FB-parent-verdict-v1.md 8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a lines 1-16
  - proof-FB-v1.md 339dcadcd914a9f036ea71a5ec2b5d3f0678cc100e22aca9de2d75751373cc6b lines 9-24
  - proof-FB-v1-erratum-1.md 33de46d245ec89a31cce1a06ac44a11f2c81c91a713b0830c59f31686245e202 lines 1-7
  - olson-balfull-rotzb-parent-verdict-v1.md 56b988ee90805f850760c6969d9724f890fb637335248b9060189ef99b1e1bc0 lines 26-34
  - olson-K3-parent-verdict-v1.md 9281cbc64bd2bc59edf7a8404481765d5d5d39c351ce5b2b28c35b6e6e03a9f6 lines 1-13
  - olson-K3-parent-erratum-v1.md 8653cb3e183a6c8d21e95e971de95b598a5a29cb94e90bb69de6173623c332af lines 1-9
  (full absolute paths as in the FCW manifest lines 5-20).
- Elementary textbook facts proved inline when used (Cauchy-Davenport over
  Z_p, pigeonhole, parity of sign changes) are re-proved or stated with their
  standard hypotheses checked by hand.

## 3. Untrusted context (methods only, never a premise)

- SCW proof (p = 4kappa-3; one review family only; NOT accepted):
  /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-second-cut-window/proof-SCW-v1.md
  6a1965aecf599e00b512ca1df36127d21e5bac21bea7ac0da5804092245f3650.
  Any method taken from it is re-derived in full at p = 4kappa-5.

## 4. Pre-freeze exposure (complete list)

1. Assignment message from Main (target, inputs, change list, acceptance), and
   the transition file above in full. Both repeat this disclosed, unproved
   parent observation: at deficiency delta = 4 the m = kappa window is
   [2, R-4] and the m = kappa+1 window is [0, R-6]; the final sorting count
   B* <= 2p - 2kappa - 1 + (exceptions) has slack 4kappa - p = 5 against R; at
   (4,11) N = 12 and the SCW additive-constant pair does not fit
   (3kappa <= N-1 fails), so another pair or argument is needed; whether the
   minority-sign exceptions fit the slack is UNKNOWN. I treat this only as
   untrusted exposure; nothing in it is used as a premise.
2. Directory listings (names, sizes, mtimes only) of
   .../olson/continuations/, .../lowerhalf-first-cut-window-boundary/,
   .../lowerhalf-second-cut-window/ and the olson-* files of
   .../six-lane-2026-10-18-96h/review/.
3. The FCW excerpt manifest review-excerpts-FCW-v1.json, lines 1-21 (paths,
   hashes and line ranges only; it contains no mathematics).
4. `shasum -a 256` and `wc -c -l` outputs for the files named above.
5. Agent memory summary supplied by the harness: process-level mentions of the
   Olson lane (review names, file names, acceptance status of unrelated
   results); no mathematical content bearing on TCW.
6. No mathematical text of NF, FCW, SCW, K0T, USK, LOWER or any other source
   was read before this freeze, and no derivation, written or unwritten
   (including preliminary arithmetic on windows, counts or slacks), was done
   before this freeze.

## 5. Process rules adopted

- Writes only inside
  /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-third-cut-window
  (created by mkdir at 2026-10-20T03:27:24-0700 together with checkpoints/).
  Every file is created exclusively (Python open(path,'x')); no file is edited,
  overwritten, moved or deleted; corrections go into new files.
- Machine steps limited to `/bin/date`, `shasum -a 256`, byte and LF-line
  counts, reading files, mkdir of this directory, exclusive creation of
  already-drafted text. No assert statements, scripts or computation over
  scientific data, enumeration, brute force, solvers, tests, Lean, model CLIs,
  nested agents, network, commit or push. All mathematics by hand in Markdown.
- Checkpoints in checkpoints/ at most 1800 s apart (target 1200 s).
- No "first", "novel" or priority claims. English only.
- Planned outputs: this file; checkpoints/cp-*.md; proof-TCW-v1.md (Sec. 0
  statement, interface table, 'not claimed' list); review-excerpts-TCW-v1.json;
  review-package-TCW-v1.md; closing checkpoint; then park.
