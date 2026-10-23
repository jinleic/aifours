# P7L scope v1 (frozen before any derivation)

Owner: OlsonThirdCutWindow (reassigned after the parked TCW delivery; same throttled math2 slot).
Freeze time: 2026-10-20T05:53:51-0700 (`/bin/date`, taken immediately before mkdir of this directory and exclusive
creation of this file).
Authority: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-olson-p7-lower-transition-v1.json
(sha256 618eff97592b75aab0a382ed57c25a072c5cb076ee3af07084855d35eda3578f, LF lines 1-42, read in full), plus the Main IRC
assignment of 2026-10-20 (same content; deliverables listed in Sec. 5).

## 1. Target

Exactly p = 7, terminal k = 8 = p+1, kappa_hat in {1, 2}. Two cells, treated SEPARATELY:
- Cell (1,7): no word of length 26 = 4p-2 over D_14 without an identity 14-subword (subword = terms in increasing
  original index order, product in that order) has an admissible normal form with terminal k = 8 and kappa_hat = 1.
- Cell (2,7): the same with kappa_hat = 2.
Antecedent: the full existential one: SOME admissible normal form (NF at its accepted definition), extra reflection
pairs anywhere in the odd blocks, the genuine empty-run rule; no o_F, nonempty-run, rotation-pair or rigidity hypothesis.
Deliverable for EACH cell: either a complete written proof of the exclusion, or the exact first failing lemma with every
proved partial range named. Each cell is explicitly covered or explicitly left open; none is dropped. Out of scope: every
other kappa_hat (kappa_hat = 3 is the R7 verdict's cell, kappa_hat = 0 the K0T verdict's), every other p, nonterminal k,
whole p = 7, full ordered Olson.

## 2. Allowed imports (accepted; each only at its literal accepted scope, re-hash-checked before use)

Hashes below were checked with `shasum -a 256` at 2026-10-20T05:53 before this freeze.
- NF: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-few-E-v4.md
  ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f, lines 28-43 (its applicability at p = 7 to be checked
  against its accepted scope after the freeze and recorded).
- GRX (if-direction): .../rotation/notes-GRX-v1.md afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30, lines 7-20.
- SC0 (classical index-one import, author statement): /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-index-one-primary-statement-parent-v1.md
  e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6, lines 1-11, read through the minimal-zero-sum step Y'z.
- ZSTRUCT / Lemma FB in (S'): /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FB-parent-verdict-v1.md
  8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a; /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-FB-v1.md
  339dcadcd914a9f036ea71a5ec2b5d3f0678cc100e22aca9de2d75751373cc6b (lines 9-24); erratum .../evidence/proof-FB-v1-erratum-1.md
  33de46d245ec89a31cce1a06ac44a11f2c81c91a713b0830c59f31686245e202; (S') extension /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-balfull-rotzb-parent-verdict-v1.md
  56b988ee90805f850760c6969d9724f890fb637335248b9060189ef99b1e1bc0 (lines 26-34).
- (S1) definition only: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-zx-s1c-parent-verdict-v1.md
  2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af, line 19.
- LOWER parent erratum (m(P) = half the sign transitions; theta only through explicit pairs):
  /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-LOWER-parent-erratum-v1.md
  087ab3ae6e880633b26658ff68e8f787bdb59758a4a0662bc7744aeea5b96377.
- FCW parent erratum item m4 (the direct NF+GRX derivation of (SR)), as a written derivation pattern re-done at p = 7:
  /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FCW-parent-erratum-v1.md
  e56bf0f337d7d670be99075829217431cf605437320dd3414cde75c3d1ae2413.
- Theorem P only at its literal accepted statement, IF needed and only after its source and scope are located and
  recorded after the freeze (the K0T verdict records reliance on it at p = 5, 7).
- Elementary facts (pigeonhole, parity, residues mod p and mod 2) proved inline.
PL (proof-LOWER-v1.md 251c8dca1c34be7b76432dc50d13368b11a7bf6da6bbb8bd31e4ee18e7cd476d) is accepted only for p >= 11, so at
p = 7 its Secs. 2, 4-6 are NOT imported; every step (SR), IF(a), normalisation, SS bijection, LT is re-derived at p = 7.

## 3. Context only (never premises below their scope)

- K0T verdict 4a2a2ffd8d8624c33c0f7cc1265cf679c18ac3a9c63565bc093b2e8afc8bf8ba; R7 verdict
  /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-R7-parent-verdict-v1.md
  b83058b2ed220d663da2e6906954572a5b3fbfe32d97f1c36317a2e87cf796f1 (kappa_hat = 3 only); FCW verdict
  b28837c9c8a9549b99a6c2205e8bbe40d65ab1aad265595c511395d4c1738f71 (kappa >= 3, p = 4kappa-1 only); SCW verdict
  d51b5d8e6c6a7c38047434b3740d477bccd2ab7e0e53ce68ea34aa83486bdfe0 (p = 4kappa-3 only); USK verdict
  6d3358ce3f1e9e95a366f2b32f10adbc73df607bc62723f561567dce1a53de18; LOWER-K1 verdict
  93ea601c1255f52a8a186002e9e46986c99db1c81a1c4aba68eb6143ca926e83 (p >= 11 only). No FCW/SCW/USK/K1/K2/R7 lemma is
  imported below its scope; methods may be re-derived at p = 7.
- UNTRUSTED, never a premise: my own TCW proof proof-TCW-v1.md 62c747911239c32998d2ec2b3bd9ec538eee5e523f68b92233aa06e890f85713
  (unaccepted; second review family pending), the FCW and SCW proof texts (accepted only at their own p-families).

## 4. Pre-freeze exposure (complete list)

1. My entire previous TCW assignment (same session): I read the FCW verdict and erratum, the FCW proof (whole), the SCW
   proof (whole), PL lines 26-133, NF 27-46, GRX 6-23, SC0 record 1-24, proof-FB 1-33, FB erratum 1-54, FB verdict 1-41,
   balfull verdict 23-37, zx-s1c verdict 16-24, the LOWER erratum, LOWER-K1, K0T and USK verdicts; and I derived and wrote
   proof-TCW-v1.md (p = 4kappa-5, kappa >= 4). I therefore know the general frame/window/lift/sorting method and the TCW
   devices (exception lists for shortened windows, (lambda,mu) representative-window tables, swap inequalities, the
   two-sided empty-alternating-set lemma). None of this was applied to p = 7 before this freeze.
2. The Main IRC assignment and the transition file in full, including the parent's disclosed UNTRUSTED route exposure:
   "at kappa1 the m2 window is full (N8,R8,t0), and tight alternating-set sorting may force unit labels; need handle
   possible theta0 by empty-run/parity/letter-count before a final SR selection. At kappa2 (N8,R10) FCW-style m2/m3 lifts
   seem plausible; its old all-m3 additive pair does not fit N8, but a re-derived all-m2 triple P1={0,3},P2={1,4},union
   might force f0=0 after proving f constant also on m2." Treated only as untrusted exposure.
3. One brief unwritten arithmetic observation made while reading the transition, before this freeze: 7 = 4*2-1, so the
   cell (2,7) is the kappa = 2 member of the FCW family p = 4kappa-1, below FCW's accepted range kappa >= 3; and PL's
   standing range p >= 11 excludes p = 7. No other derivation, written or unwritten, concerning p = 7 was done.
4. shasum/wc/ls metadata of the files listed above; the SCW and R7 verdict TEXTS were NOT read before this freeze.
5. The harness memory summary (process-level, no p = 7 mathematics).

## 5. Process rules adopted

- Writes only inside /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/p7-lower-terminal
  (created with checkpoints/ by mkdir immediately before this file). Every file is created exclusively (Python
  open(path,'x')); nothing is edited, overwritten, moved or deleted; corrections go into new errata files.
- Machine steps limited to `/bin/date` (before every timestamp), `shasum -a 256`, byte and LF-line counts, reading files,
  mkdir of this directory, exclusive creation of already-drafted text. No assert statements, scripts, enumeration,
  scientific computation, solvers, tests, Lean, model CLIs, nested agents, network, /tmp, deletion, commit or push.
- Checkpoints in checkpoints/ at most 1800 s apart (target 1200 s), AND before and after each substantial derivation
  sub-case; derivation turns are kept short so that no output is lost.
- No "first", "novel" or priority claims. English only.
- Deliverables: this file; checkpoints/cp-*.md; proof-P7L-v1.md (complete statements or exact obstruction per cell,
  literal interface table, not-claimed list); review-excerpts-P7L-v1.json ({path, sha256, start, end}, including this
  scope and the proof); review-package-P7L-v1.md; whole numbered packet <= 100 KB; then park.
