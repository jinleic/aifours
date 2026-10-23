# FQW scope v1 (frozen before any derivation)

Owner: OlsonThirdCutWindow (same throttled math2 slot, after the parked P7L delivery).
Freeze time: 2026-10-20T06:26:24-0700 (`/bin/date`, taken immediately after mkdir of this directory and checkpoints/,
immediately before exclusive creation of this file).
Authority: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-olson-fourth-cut-window-transition-v1.json
(sha256 21fac2252ccfd0127c898b09aab83a63cd252d0283c0d391cafd3dae8f61327b, LF lines 1-55, read in full), plus the Main IRC
assignment of 2026-10-20 (same content; deliverables in Sec. 5).

## 1. Target (Theorem FQW candidate)

Deficiency delta := 4kappa-p-1 = 6: for every integer kappa >= 5 such that p = 4kappa-7 is prime ((kappa,p) = (5,13),
(6,17), (9,29), ...), no word of length 4p-2 over D_(2p) without an identity 2p-subword (subword = terms in increasing
original index order) has an admissible normal form with terminal k = p+1 and kappa_hat = kappa.
Antecedent: the full existential one: SOME admissible NF, extra reflection pairs anywhere in the odd blocks, the genuine
empty-run rule; no o_F, nonempty-run, rotation-pair or rigidity hypothesis.
Deliverable: EITHER a complete written proof, OR the exact first failing lemma with every proved partial range named.
The cell (5,13) (the last open terminal lower-half cell at p = 13) must be explicitly covered or explicitly left open
with its exact obstruction. No other cell; no full-Olson scope expansion.

## 2. Allowed imports (accepted; each only at its literal accepted scope, re-hash-checked before use)

Hashes checked with `shasum -a 256` at 2026-10-20T06:26 before this freeze.
- NF: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-few-E-v4.md
  ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f, lines 28-43.
- GRX (if-direction): .../rotation/notes-GRX-v1.md afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30, lines 7-20.
- SC0: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-index-one-primary-statement-parent-v1.md
  e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6, lines 1-11, read through the minimal-zero-sum step Y'z.
- ZSTRUCT / Lemma FB in (S'): /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FB-parent-verdict-v1.md
  8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a (1-16);
  /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-FB-v1.md
  339dcadcd914a9f036ea71a5ec2b5d3f0678cc100e22aca9de2d75751373cc6b (9-24); erratum .../evidence/proof-FB-v1-erratum-1.md
  33de46d245ec89a31cce1a06ac44a11f2c81c91a713b0830c59f31686245e202 (1-7); (S') extension
  /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-balfull-rotzb-parent-verdict-v1.md
  56b988ee90805f850760c6969d9724f890fb637335248b9060189ef99b1e1bc0 (26-34).
- (S1) definition only: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-zx-s1c-parent-verdict-v1.md
  2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af, line 19.
- PL /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-terminal-cell/proof-LOWER-v1.md
  251c8dca1c34be7b76432dc50d13368b11a7bf6da6bbb8bd31e4ee18e7cd476d, lines 40-129, accepted via
  /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-LOWER-K1-parent-verdict-v1.md
  93ea601c1255f52a8a186002e9e46986c99db1c81a1c4aba68eb6143ca926e83 (p >= 11 prime, 1 <= kappa <= (p-3)/2; its standing
  range is to be checked against every (kappa,p) of the target after the freeze), read with
  /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-LOWER-parent-erratum-v1.md
  087ab3ae6e880633b26658ff68e8f787bdb59758a4a0662bc7744aeea5b96377 (m(P) = half the sign transitions; theta only through
  explicit pairs). Only PL Secs. 2, 4-6 ((SR), IF(a), normalisation, SS bijection, LT) may be used; anything else is
  re-derived.
- FCW parent erratum (derivation patterns m3, m4): /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FCW-parent-erratum-v1.md
  e56bf0f337d7d670be99075829217431cf605437320dd3414cde75c3d1ae2413.
- Elementary facts (pigeonhole, parity, residues mod p and mod 2) proved inline.

## 3. Context only and untrusted inputs

- Accepted context (never premises below their own scope): FCW verdict b28837c9c8a9549b99a6c2205e8bbe40d65ab1aad265595c511395d4c1738f71
  (p = 4kappa-1, kappa >= 3), SCW verdict d51b5d8e6c6a7c38047434b3740d477bccd2ab7e0e53ce68ea34aa83486bdfe0 (p = 4kappa-3,
  kappa >= 4), USK verdict 6d3358ce3f1e9e95a366f2b32f10adbc73df607bc62723f561567dce1a53de18 (3 <= kappa <= floor((p-1)/4)),
  K0T verdict 4a2a2ffd8d8624c33c0f7cc1265cf679c18ac3a9c63565bc093b2e8afc8bf8ba (kappa_hat = 0). No FCW/SCW/USK lemma is
  used outside its own accepted p.
- UNTRUSTED (methods only, re-derived, never premises): my own TCW proof
  .../lowerhalf-third-cut-window/proof-TCW-v1.md 62c747911239c32998d2ec2b3bd9ec538eee5e523f68b92233aa06e890f85713 and its
  parent errata .../review/olson-TCW-parent-erratum-v1.md eb673b3200d4d0f8f7e36f61fbf3225e5c3542e0b14de05a604ca50c640ee8c9,
  .../review/olson-TCW-parent-erratum-v2.md a8204c0e533828fc86816ea6de648a2d52ff3409898f0c557bd8fe5a79f8e88d (texts NOT
  read before this freeze); my own P7L proof .../p7-lower-terminal/proof-P7L-v1.md
  7e8bee08dacb10a9b4dd373dc9e57e526a21bd4bc77e91a41091b8e88cacb7e8; the FCW and SCW proof texts.

## 4. Pre-freeze exposure (complete list)

1. My previous TCW assignment (same session): I read FCW (verdict, erratum, whole proof), SCW (whole proof), PL 26-133, NF,
   GRX, SC0, FB inputs and the LOWER/K1/K0T/USK verdicts, and I derived and wrote TCW (delta = 4, p = 4kappa-5): exception
   lists for shortened windows, (lambda,mu) representative-window tables, duality J -> complement for the m = kappa-1
   window, the coupling q(P u i)+q'(P) >= |A^c|, the all-m=kappa additive triple, swap inequalities, empty-run evenness and
   the two-sided "no empty alternating set" lemma.
2. My previous P7L assignment: I derived and wrote P7L (p = 7, kappa_hat in {1,2}), including a general representative
   lemma with (lo,hi) windows and a lift family containing m = kappa-1 = 1 sets (singletons) when their window is
   [2,R]; I read the R7 and SCW verdict texts there.
3. The Main IRC assignment and this transition in full, including the parent's UNTRUSTED notes: "at delta=6 windows
   Win_kappa=[2,R-6], Win_(kappa+1)=[0,R-8], Win_(kappa-1)=[4,R-4]; minimal representations missing <=6 letters; u1
   margin must exceed 6 (check u1>=|b|+6 or adapt); N=4kappa-6, alternating sets 2kappa-3 runs (odd N? N=p+1=4kappa-6 is
   even). The final count slack against R is again small; the TCW swap/empty-alternating-set machinery may need
   extension. Whether the label margins suffice at kappa=5 (p=13) is UNKNOWN."
4. shasum/wc/ls metadata of the files above. No text of the TCW parent errata was read.
5. The harness memory summary (process-level only).
6. No derivation, written or unwritten, concerning delta = 6 or p = 4kappa-7 (including any check of the parent notes)
   was made before this freeze.

## 5. Process rules adopted

- Writes only inside /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-fourth-cut-window
  (created with checkpoints/ immediately before this file). Every file is created exclusively (Python open(path,'x'));
  nothing is edited, overwritten, moved or deleted; corrections go into new errata files.
- Machine steps limited to `/bin/date` (before every timestamp), `shasum -a 256`, byte and LF-line counts, reading files,
  mkdir of this directory, exclusive creation of already-drafted text. No assert statements, scripts, enumeration,
  scientific computation, solvers, tests, Lean, control/native runs, model CLIs, nested agents, network, /tmp, deletion,
  commit or push.
- Checkpoints in checkpoints/ at most 1800 s apart (target 1200 s) and before/after each substantial derivation sub-case;
  derivation turns are kept short so that no output is lost.
- No "first", "novel" or priority claims. English only.
- Deliverables: this file; checkpoints/cp-*.md; proof-FQW-v1.md (Sec. 0 statement, interface table with path, whole
  SHA256, lines, scope; explicit not-claimed list); review-excerpts-FQW-v1.json ({path, sha256, start, end}, including this
  scope and the proof); review-package-FQW-v1.md; numbered packet <= 100 KB; then park.
