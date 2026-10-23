# UMR scope v1 (frozen before any derivation and before reading the parent route note)

Owner: OlsonThirdCutWindow (same throttled math2 slot, after the parked FQW delivery).
Freeze time: 2026-10-20T07:29:56-0700 (`/bin/date`, taken immediately after mkdir of this directory and checkpoints/,
immediately before exclusive creation of this file).
Authority: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-olson-uniform-middle-transition-v1.json
(sha256 459233f3ac03cac347540d9c173d54810d9f464aab20e2a909c19d9df4447e59, LF lines 1-49, read in full), plus the Main IRC
assignment of 2026-10-20 (same content; deliverables in Sec. 5).

## 1. Target (Theorem UMR candidate)

For every prime p >= 17 and every integer kappa with floor((p+7)/4) < kappa <= (p-3)/2, no word of length 4p-2 over
D_(2p) without an identity 2p-subword (subword = terms in increasing original index order) has an admissible normal form
with terminal k = p+1 and kappa_hat = kappa.
Antecedent: the full existential one: SOME admissible NF, extra reflection pairs anywhere in the odd blocks, the genuine
empty-run rule; no o_F, nonempty-run, rotation-pair or rigidity hypothesis.
Deliverable: EITHER a proof of the ENTIRE range, OR every fully proved partial range/lemma together with the EXACT FIRST
FAILING UNIFORM LEMMA. The cells (kappa,p) = (7,17), (7,19), (8,19) must each be explicitly proved or explicitly
obstructed. No silent reduction to one fixed deficiency. No other k, no full ordered Olson.

## 2. Allowed imports (accepted; each only at its literal accepted scope; hashes re-checked at 2026-10-20T07:29)

- NF: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-few-E-v4.md
  ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f, lines 28-43.
- GRX (if-direction): .../rotation/notes-GRX-v1.md afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30, lines 7-20.
- SC0: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-index-one-primary-statement-parent-v1.md
  e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6, lines 1-11, read through the minimal-zero-sum step Y'z.
- ZSTRUCT / Lemma FB in (S'): /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FB-parent-verdict-v1.md
  8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a (1-16);
  /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-FB-v1.md
  339dcadcd914a9f036ea71a5ec2b5d3f0678cc100e22aca9de2d75751373cc6b (9-24); .../evidence/proof-FB-v1-erratum-1.md
  33de46d245ec89a31cce1a06ac44a11f2c81c91a713b0830c59f31686245e202 (1-7); (S') extension
  /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-balfull-rotzb-parent-verdict-v1.md
  56b988ee90805f850760c6969d9724f890fb637335248b9060189ef99b1e1bc0 (26-34).
- (S1) definition only: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-zx-s1c-parent-verdict-v1.md
  2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af, line 19.
- LOWER parent erratum (m(P) = half the sign transitions; theta only through explicit pairs):
  /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-LOWER-parent-erratum-v1.md
  087ab3ae6e880633b26658ff68e8f787bdb59758a4a0662bc7744aeea5b96377.
- FCW parent erratum (derivation patterns m3, m4 only):
  /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FCW-parent-erratum-v1.md
  e56bf0f337d7d670be99075829217431cf605437320dd3414cde75c3d1ae2413.
- Elementary facts (pigeonhole, parity, residues mod p and mod 2, elementary inequalities) proved inline.
Every other step ((SR), frame, normalisation, light side, density, signed sums, realisation, representatives, lift
framework, final count) is re-derived in the proof from these interfaces.

## 3. Context only and untrusted inputs

- Accepted context, exact scopes only, never premises outside them: USK verdict
  6d3358ce3f1e9e95a366f2b32f10adbc73df607bc62723f561567dce1a53de18 (3 <= kappa <= floor((p-1)/4)); FCW verdict
  b28837c9c8a9549b99a6c2205e8bbe40d65ab1aad265595c511395d4c1738f71 (p = 4kappa-1); SCW verdict
  d51b5d8e6c6a7c38047434b3740d477bccd2ab7e0e53ce68ea34aa83486bdfe0 (p = 4kappa-3); TCW verdict
  /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-TCW-parent-verdict-v1.md
  17f6d80d664c4e3b60bb7be5aba560502f5597350b025b3d058d7d989fef0c29 (p = 4kappa-5); P7L verdict
  /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-P7L-parent-verdict-v1.md
  57664b53b35aa0de0729d7ec7b2c2ff4d9b7e738155612c5ffcb43ec169a8569 (p = 7); K0T and LOWER-K1 verdicts
  (4a2a2ffd8d8624c33c0f7cc1265cf679c18ac3a9c63565bc093b2e8afc8bf8ba, 93ea601c1255f52a8a186002e9e46986c99db1c81a1c4aba68eb6143ca926e83).
  The TCW and P7L verdict TEXTS were not read before this freeze.
- UNTRUSTED (methods only, never premises): my FQW proof
  .../lowerhalf-fourth-cut-window/proof-FQW-v1.md 9b4561780b37874c47a188fc788ae34fc223f1252f7e4bf9a1be9a6dffd09dc5
  (not accepted); my TCW and P7L proofs (62c747911239c32998d2ec2b3bd9ec538eee5e523f68b92233aa06e890f85713,
  7e8bee08dacb10a9b4dd373dc9e57e526a21bd4bc77e91a41091b8e88cacb7e8) outside their verdict scopes; FCW/SCW proof texts; the
  parent route note /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-untrusted-route-note-v1.md
  738567ca9367edf739444af614bc923a40773d28926d42411b52bdb3cbbb142a, to be read only AFTER this freeze.

## 4. Pre-freeze exposure (complete list)

1. My TCW (delta = 4), P7L (p = 7, kappa_hat in {1,2}) and FQW (delta = 6) derivations in this session, and everything read
   for them (FCW, SCW proofs and inputs; NF, GRX, SC0, FB inputs; LOWER/K1/K0T/USK/R7/SCW verdicts; TCW parent errata
   v1-v2). Known methods: frame and label counts, shortened-window exception lists, (lambda,mu) tables, couplings for
   theta pair-independence, additive triples at m in {kappa-1,kappa}, complements, sorting the top kappa or kappa-1 runs
   of alternating sets, empty-run evenness, two-sided "no empty alternating set" lemmas.
2. The parent's disclosed untrusted notes in the TCW and FQW transitions (windows at delta = 4, 6; slack; u1 margins).
3. The Main IRC assignment and this transition in full. The transition and IRC message name the parent route note's
   topics only ("proposed uniform unit reservoir, two-sided realisation offsets, central m-levels and coupled
   additivity"); its text was NOT read.
4. Unwritten arithmetic made while reading the target statement, before this freeze (disclosed in full): (i) the range at
   p = 17 is kappa = 7 and at p = 19 is kappa in {7,8}, matching the named cells; (ii) delta := 4kappa-p-1 is 10, 8, 12 at
   (7,17), (7,19), (8,19), delta = -(p+1) (mod 4), and kappa = 6 at p = 17 resp. 19 are the FQW resp. TCW cells; (iii) at
   the top end kappa = (p-3)/2 one has delta = p-7 and R = p-1+2kappa = 2p-4. No other derivation, written or unwritten.
5. shasum/wc/ls metadata of the files above; the harness memory summary (process-level only).

## 5. Process rules adopted

- Writes only inside /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-uniform-middle-range
  (created with checkpoints/ immediately before this file). Every file is created exclusively (Python open(path,'x'));
  nothing is edited, overwritten, moved or deleted; corrections go into new errata files.
- Machine steps limited to `/bin/date` (before every timestamp), `shasum -a 256`, byte and LF-line counts, reading files,
  mkdir of this directory, exclusive creation of already-drafted text. No assert statements, scripts, enumeration,
  scientific computation, solvers, tests, Lean, control/native runs, model CLIs, nested agents, network, /tmp, deletion,
  commit or push.
- Checkpoints in checkpoints/ at most 1800 s apart (target 1200 s) and before/after each substantial derivation sub-case;
  derivation turns kept short so that no output is lost.
- No "first", "novel" or priority claims. English only. No full ordered Olson, other k, Lean, human or runtime claim.
- Deliverables: this file; checkpoints/cp-*.md; proof-UMR-v1.md (full proof OR fully proved partials + exact first failing
  lemma; literal interface table; not-claimed list); review-excerpts-UMR-v1.json ({path, sha256, start, end}, including
  this scope and the proof); review-package-UMR-v1.md; whole numbered packet <= 100 KB; then park.
