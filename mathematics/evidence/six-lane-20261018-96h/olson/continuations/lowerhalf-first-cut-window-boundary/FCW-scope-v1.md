# Frozen scope: first cut-window boundary p = 4kappa-1, lower-half terminal k=p+1, kappa_hat=kappa >= 3, v1

Owner OlsonUniformSmallKappa (math2 Olson slot, THROTTLED, no extra slots). Frozen after /bin/date 2026-10-20T01:19:12-0700 BEFORE
derivation for this target. Authority: RUN/control/written-olson-first-cut-window-boundary-transition-v1.json, whole-file
SHA256 ba6e8038fda856125303c26a85bfac78741ab04186efa98c18f3ebe9071b02d6 (at 2026-10-20T01:16:35-0700) and Main's IRC,
RUN=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h. Exactly ONE deliverable (one packet <=100 KB),
then park. Not a new target or runtime authority. All prior artifacts read-only. Writes ONLY in
DIR=/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-first-cut-window-boundary;
every file created exclusively (mode x), never edited or deleted; corrections are new versioned errata. Written mathematics
only; metadata limited to sha256, byte counts, LF line ranges and /bin/date. NO scientific scripts, assertions, enumeration,
solvers, tests, control/native launches, model CLIs, nested agents, /tmp, global configuration, commits/pushes, external
contact or paid API.

## Exact target
Every prime p = 4kappa-1 with integer kappa >= 3 (so p >= 11, p = 3 mod 4; kappa = (p+1)/4; e.g. (kappa,p) = (3,11), (5,19),
(6,23), (8,31), ...): no word w of length 4p-2 over D_(2p) with no identity 2p-subword in increasing original index order
has an admissible NF u with terminal k=p+1 and kappa_hat=kappa. FULL existential antecedent: SOME admissible NF; the
H=p-1-kappa extra reflection pairs lie anywhere in the odd blocks; every empty NF run separates different reflection values
(genuine empty-run rule); no o_F, nonempty-run, rotation-pair or reflection-rigidity hypothesis; no multiset-only statement
outside this antecedent. Deliver ONE written proof of exclusion for this exact boundary, OR the exact first failing lemma
or inequality with named, proved partial ranges (all completed steps kept, failed branches recorded). The case
(kappa,p) = (3,11) is explicitly covered or explicitly left open; it is never dropped. Labelled PARTIAL of ordered Olson in
every outcome.
Not in scope: kappa_hat = 0; p = 7; any other middle-range cell (p <= 4kappa-3, or kappa_hat > (p+1)/4 at other p); cells
already accepted (USK range 3 <= kappa <= floor((p-1)/4), kappa_hat <= 2, upper half); full ordered Olson. No claim of
"first", novelty, priority, "full Olson", human review or Lean.

## Accepted inputs (literal scopes)
- PL = .../olson/continuations/lowerhalf-terminal-cell/proof-LOWER-v1.md, SHA256
  251c8dca1c34be7b76432dc50d13368b11a7bf6da6bbb8bd31e4ee18e7cd476d, Secs. 2, 4-7, accepted relative to its inputs by the K1
  verdict (RUN/review/olson-LOWER-K1-parent-verdict-v1.md 93ea601c1255f52a8a186002e9e46986c99db1c81a1c4aba68eb6143ca926e83)
  with the LOWER parent erratum (RUN/review/olson-LOWER-parent-erratum-v1.md
  087ab3ae6e880633b26658ff68e8f787bdb59758a4a0662bc7744aeea5b96377: m(P) = half the number of sign transitions; theta only
  through an explicit full pair). PL's standing range p >= 11, 1 <= kappa <= (p-3)/2 contains p = 4kappa-1, kappa >= 3. Used:
  (SR) from the GRX if-direction, IF(a) and the gamma-normalisation, the explicit SS bijection, LT, and the U/A/C formulas,
  each with every needed density/label bound RE-DERIVED here at p = 4kappa-1 (no PL Lemma D, no Setting fact).
- Frame inputs as PL uses them: NF (ROT/proof-ROT-few-E-v4.md lines 28-43), GRX if-direction (ROT/notes-GRX-v1.md lines
  7-20), SC0 (R16/olson-index-one-primary-statement-parent-v1.md), ZSTRUCT and FB in (S') (R18/olson-FB-parent-verdict-v1.md
  with proof-FB-v1.md lines 11-19 and erratum 1; (S') extension R18/olson-balfull-rotzb-parent-verdict-v1.md line 33).
- USK verdict RUN/review/olson-USK-parent-verdict-v1.md SHA256
  6d3358ce3f1e9e95a366f2b32f10adbc73df607bc62723f561567dce1a53de18 with parent errata v1
  85718782c14dcb913706d5b7245ebfda1ef50ef1e9e7661d671a9ecbfcf4519e and v2
  4f3a2636594787337ebe8294dc086f8a3af9dccea89d5599e95e802e95590bfe: Theorem USK and its lemmas are accepted ONLY at
  3 <= kappa <= floor((p-1)/4); NOTHING of its full-window family, density, negative-letter bounds, lift framework or
  rigidity is transferred to p = 4kappa-1. Its methods may be re-used, and every statement used here is re-proved at
  p = 4kappa-1.
- K3 verdict RUN/review/olson-K3-parent-verdict-v1.md SHA256 9281cbc64bd2bc59edf7a8404481765d5d5d39c351ce5b2b28c35b6e6e03a9f6
  with parent erratum 8653cb3e183a6c8d21e95e971de95b598a5a29cb94e90bb69de6173623c332af: Theorem K3-11 (p = 11, kappa_hat = 3:
  no avoider admits a qualifying NF together with an admissible fixed frame in which (H11) holds) MAY be cited at exactly
  that literal scope, if used; K3 lemmas otherwise method/context only.
- B0S-CJ''' (R16/olson-cj-cjx-parent-verdict-v1.md lines 8-15, SHA256
  5cfd6a4fe15cab133e210cd6f6966e34fa633d1a8c432b79eb537c0016145f6d) only for the all-rotations-equal non-identity
  sub-case, if used; its literal antecedent is re-checked at p = 4kappa-1 before use.
- Untrusted context, NOT premises: P11R candidate proof-P11R-v1.md (SHA256
  6ee3df0985f02d01e6cde08c88944791b91dbc76e389e20f16e6b9accec87ac4; unreviewed partial/obstruction) and the parent's
  pre-freeze route sketch recorded in the transition JSON.

## Pre-freeze exposure (none is a premise)
Read before this freeze: the transition JSON (including the parent's untrusted sketch: at p = 4kappa-1 the m=kappa window is
[2,R] and the m=kappa+1 window is [0,R-2]; a two-signed-pattern/fullness route analogous to P11R might apply); the USK
verdict and parent errata v1/v2; my own USK packet (author; its Sec. 7 boundary remark notes that below p = 4kappa+1 the
m=kappa+1 window stops at 2p-2kappa-2 < R, that single-signed X^(P) need not be full, and that the numerics of USK Lemma
N(b),(c) use p >= 4kappa+1); proof-K3-v1.md (Lemma FULL at p=11: an m=4 pattern with two-signed X^(Q) is full, X^(Q) is
single-signed iff letters(Q) or letters(Q^c) equals A-; the p=11 residual (H11) failing; route remark (R3): at p=11 the m=3
window is [2,16], such a pattern is full iff X^(Q) has a nonempty integer zero-sum, and sorting the top THREE of each
alternating set would give B* <= p+3 < R if the framework were available); the K2 proof; the K3 verdict and erratum; the
P11R closing checkpoint summary only (checkpoint-003.md SHA256
ac6c176e9134c4796c36b16b46d1042451799d52134faf109060935d11f88aeb: residual not shown empty; B* in {16,18} sub-cases).
NOT read before freezing: proof-P11R-v1.md and its erratum; they may be read after this freeze as untrusted context only.
Remarks noted before freezing, unverified: at p = 4kappa-1, N = 4kappa, R = 6kappa-2, 2p = 8kappa-2, M = (p+1)/2 = 2kappa;
W_m = [max(0,2kappa+2-2m), min(R,2p-2m)] gives W_kappa = [2,R], W_(kappa+1) = [0,R-2], and no m has window [0,R].
Planned route: (1) windows; (2) frame, density and negative-letter bounds re-derived at p = 4kappa-1 (lift inequality);
(3) fullness criteria for m = kappa (nonempty integer zero-sum) and m = kappa+1 (representations within R-2 letters) in
terms of two-signed X^(P); (4) a lift framework on a family of full patterns avoiding single-signed ones: explicit full
pairs for theta, connectivity, additive constant, complement total; (5) rigidity by sorting the top kappa (or kappa+1)
runs of each alternating set, with the single-signed top sets treated separately; (6) final contradiction; (7) (3,11)
written out explicitly (or K3-11 at its literal scope plus the H11-failing branch); otherwise the exact first failing step.

## Deliverables
DIR/proof-FCW-v1.md (exclusion or exact first failing lemma with proved partial ranges, interface table),
DIR/review-package-FCW-v1.md, DIR/review-excerpts-FCW-v1.json ({path,sha256,start,end}, every hash re-checked),
DIR/checkpoints/checkpoint-NNN.md at most 1800 s apart (/bin/date immediately before each timestamp); packet <=100 KB;
exact pins to Main; then park.
