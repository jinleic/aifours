# Reflection half of INV*(p) for rigid rotations ("reflection" slice of the math-2 continuation)

Owner: OlsonReflectionRigidity (sub-agent of Main).  Directory reflection/ (with tmp/, code/, out/) created by os.mkdir
(exclusive) at 2026-10-18T01:55 PDT inside the shared parent created by OlsonRotationRigidity at 01:44:19.  This README
was written at host clock 2026-10-18T02:24:43-0700, BEFORE any experiment of this slice, and is FROZEN: it is never edited;
later notes go to new exclusively-created files (checkpoint-NN.md, versioned proofs).
Contract: institute/runs/six-lane-2026-10-16/screening/math-2-invstar-continuation-contract-v1.json,
sha256 9a362a94108dc6ad3bd55581ecdacc2b8ed1b0dcd486c2f5b3a47af914850512 (re-hashed 01:47 PDT, matches).
All older olson/ files are read-only inputs.  TMPDIR for every tool: reflection/tmp/.

## 1. Exact target (frozen)

Conventions of olson/proof-dihedral-partial.md Sec. 0: D_(2p) = {(v,e)}, (v,e)(v',e') = (v + e v', e e'),
rho_x = (x,+1), sigma_y = (y,-1).  An avoider is a word with no INCREASING index set of size 2p whose ORDERED product is
(0,+1); existence is invariant under cyclic rotation.  Identity subwords are never treated as reorderable subsequences.

REFL(p) [= INV*b-rig(p) of c2/invstar/README.md Sec. 1 = the "reflection" slice of the contract]:  for a prime p >= 5,
every avoider w of length 4p-2 over D_(2p) whose rotation letters all lie in one set {rho_x, rho_-x}, x != 0, has every
maximal CYCLIC reflection run constant.

Deliverable: a written proof of REFL(p) for every prime p >= 5 with every assumption named, or an explicit word violating
it verified by two independent raw ordered-product DPs (no window formula), or a precisely scoped conditional theorem
plus an exact obstruction.  Scope (never blurred):
* REFL(p) is HALF of INV*(p); it says nothing about rotation values (rotation slice).  REFL(p) alone does not prove INV*(p)
  or ordered Olson.
* A counterexample to REFL(p) (length 4p-2) is NOT a counterexample to ordered Olson (length 4p-1).
* No finite census is a universal premise; search misses and timeouts are UNKNOWN.

## 2. Inputs (cited; anything about words with empty rotation runs is RE-DERIVED here before use)

* Lemma GR, Lemma WAS (olson/proof-GR.md 33621e9e..., olson/repr-WAS.md 87d7cade...; Claude-reviewed).
* GR0, WAS0, H0, MP0, NF (c2/invstar/proof-GR0-r1.md 205ee0c7...; UNREVIEWED): not imported; the needed parts are
  re-derived in this directory.  Sharpness family (c2/invstar/proof-sharpness.md 20bcdde7...): sigma_(v-2) rho_1^(2p-3)
  sigma_v^(2p-1) avoids at length 4p-3; its three natural one-letter extensions are solvable (already checked there).
* Tools valid for every word of length N <= 4p-1 (hypotheses re-checked for N = 4p-2): EGZ; Theorem P (proof-theoremP.md,
  Codex-reviewed); Davenport-alpha (F >= 2, sizes < 4p); p disjoint same-letter reflection pairs; Lemma AR.
* RGR-only results, usable ONLY on a genuine RGR word produced by a proved avoidance-preserving reduction, each with its
  exact status: Theorem K0 (proof-PAR-K0.md, Codex ACCEPT); Theorems M, P (parent-accepted); Lemma M0 (parent-accepted);
  Lemma OR (Codex ACCEPT-WITH-FIXES); Corollary B0 / Sec. 11 of proof-RUNS.md, Corollary B' (MIX_DEF without inherited
  hypotheses), KB, KBH, RGR-LONG: conditional on the RUNS assembly R/olson-runs-assembly-proof-v4.md (06579ba5...), whose
  imports U2-U10 await parent acceptance.  Every use is labelled with this status.
* NOT imported: any RGR window lemma (K0, BC, OR, TL, KW, C0-B, A1, KB, ...) for words with EMPTY rotation runs unless its
  proof is redone here; at an empty run lambda({t}) can be 0 or -1 and the RGR proofs use lambda >= 0.

## 3. Prior routes that failed or are finished (not repeated)

* c2/invstar GR0/NF searches: p = 5 all k (finite proof of REFL(5)); p = 7 NF k <= 9 none; k = 10..19 open.  NOT rerun,
  NOT extended by brute force.
* Single-window / block-chain certificates that ignore genuineness (theta_t != 0) cannot prove REFL: the fused word
  (theta_t = 0) is an avoider in the relevant cases, e.g. a single empty run next to one even block gives a K0-type
  partition sum of exactly p, not p + 1 (derived 02:0x PDT before this README; to be written in the notes).
* "Fill the empty run with a rotation" (FILL) is NOT a general lemma: at p = 5, N = 17 the avoider sigma_y^2 rho_1^9
  sigma_(y+3)^6 (listed in c2/invstar/out/gwas_p5_N17.txt) has an (even,even) empty run, and filling it gives an RGR word
  with R + H = 14 > 3p - 2, solvable by Davenport-alpha (to be confirmed by raw DP in E0).

## 4. Plan: new representation and proof obligations first

New representation: G-words (rotations rho_1, rho_-1 after normalisation; cyclic alternation of maximal constant blocks
and possibly EMPTY rotation runs) together with exact segment-SPECTRUM moves.  Obligations, each to be written with proof:
L1 SPEC: replacing a contiguous segment X by Y with |Y| = |X| and Spec(Y) subset of Spec(X) (Spec = set of (size, ordered
   product) of subwords) preserves avoidance.
L2 FUS: sigma_u^l sigma_v^l' with l' even is dominated by sigma_u^(l+l').  L3 SL: Spec(sigma_u^a sigma_v^b) depends only on
   floor(a/2)+floor(b/2), a mod 2, b mod 2 (a, b >= 1): sliding pairs across an empty run is exact in both directions.
L4 TR: moving one pair rho_1 rho_-1 from one rotation run to another (possibly empty) run leaves every GR0 window unchanged.
L5 H0: Lemma H re-derived for representations with empty runs.  L6 P0: Theorem P gives e_R <= e_F + 2 kappa (empty runs are
   even rotation runs).  L7 BC': Lemma BC with the genuineness boost (lambda(Q) = 0 and u_Q != 0 => use 1).
L8 OR0/PM0: odd-segment reduction and merging for G-words, re-derived from H0.
T1 (target theorem, all p): K0*: no G-avoider of length 4p-2 with kappa = 0 has a genuine empty run.
T2 (reduction): every hypothetical G-avoider with a genuine empty run reduces, by L1-L8 and the labelled RGR imports, to an
   explicitly described residual class (expected: all blocks odd with (odd,odd) empty runs and kappa >= 1, plus the
   penultimate FUS words over type-(II) RGR avoiders); then attack the residual by new lemmas.
Every failed route is recorded concretely in a notes/checkpoint file.

## 5. Experiments (only to test a stated lemma; each with controls)

E0 raw DP (fresh, in code/, states (size, sign, value)), spot-checked against unchanged olson/code/was_verify.py dp_has.
   Positive controls (must AVOID): sharpness family at 4p-3 (p = 5, 7, 11, 13); rho_1^(2p-1) sigma_0^(2p-1) at 4p-2.
   Negative controls (must be SOLVABLE, explicit index set multiplied directly): the three sharpness extensions; the
   FILL example of Sec. 3.
E1 brute-force spectra of all two-block segments (lengths <= 12; p = 5, 7, 11) for L2, L3; window identity for L4 on random
   G-words (GR0 formula AND raw DP before/after the move); mutation: a one-letter (not pair) slide must change Spec.
E2 replay of the T1 certificate (the exact partition and BC' inequalities of the written proof) on random and exhaustive
   small kappa = 0 G-words with genuine empty runs, p = 7..31, plus raw DP at p = 5, 7, 11 confirming solvability;
   mutation: dropping the boost must make some certificate fail.
E3 FILL test restricted to the residual class (all blocks odd, one (odd,odd) empty run) at N = 4p-3, input read-only from
   c2/invstar/out/gwas_p5_N17.txt (81389b5c...) and freshly generated p = 7 words; positive control = sharpness family.
E4 only if T2 yields a NEW finite normal form: an exact census at p = 7 in that normal form, with p = 5 agreement control
   (must find 0 at N = 18), 4p-3 positive control, and a window-shrinking mutation whose spurious hits raw DP rejects.
   Any candidate counterexample: explicit word, two DPs, hash-pinned JSON, parent notified immediately.

## 6. Resource caps (contract v1)

<= 1 busy process for this slice; <= 2 GiB RSS; <= 100 MB new data in this directory; native chunks <= 10800 s with
checkpoints <= 30 min; native stop by 2026-10-18T18:20:00-07:00.  Before EACH native launch: fresh statvfs free >= 12.2e9 B
plus projected retained growth (gate failure: report once, wait, no polling); continuous floor 12.0e9 B.  CPU limits via
ulimit -t inside bash; no native children under eval deadlines; no SIGKILL, Popen.kill or subprocess.run(timeout).  No model
CLIs, installs, paid APIs, network, Git, /tmp, global config, cron/launchd, deletion, old-engine edits.  python3 -B and
PYTHONDONTWRITEBYTECODE=1 (no __pycache__).  Free space just before this README: 15,009,992,704 B (02:20:14 PDT).
