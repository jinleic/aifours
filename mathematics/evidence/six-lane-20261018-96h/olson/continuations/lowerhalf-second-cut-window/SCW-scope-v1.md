# Frozen scope: second cut window p = 4kappa-3, lower-half terminal k=p+1, kappa_hat=kappa >= 4, v1

Owner OlsonSecondCutWindow (math2 Olson slot, THROTTLED, no extra slots). Frozen after /bin/date 2026-10-20T02:00:53-0700
BEFORE any written derivation for this target. Authority: RUN/control/written-olson-second-cut-window-transition-v1.json,
whole-file SHA256 baf55df8a92cbe40e0f469ac8a21a0d541f529abe053c94450afe5b3e959ab40 (at 2026-10-20T01:48:35-0700), and Main's
assignment; RUN=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h. Exactly ONE deliverable (one packet
<=100 KB), then park. Not a new target or runtime authority. All prior artifacts are read-only. Writes ONLY in
DIR=/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-second-cut-window;
every file is created exclusively (Python open(path,'x') used only to write already-drafted text; mkdir for DIR and
DIR/checkpoints), never edited, moved or deleted; corrections are new versioned errata. Written mathematics only; machine
steps limited to /bin/date, shasum -a 256, byte and LF-line counts, reading files and exclusive file creation. NO scientific
scripts, assertions, enumeration, solvers, tests, control/native launches, model CLIs, nested agents, /tmp, global
configuration, commits/pushes, external contact or paid API.

## Exact target (Theorem SCW candidate)
For every integer kappa >= 4 such that p = 4kappa-3 is prime (p = 1 mod 4, p >= 13; (kappa,p) = (4,13), (5,17), (8,29),
(10,37), (11,41), ...): no word w of length 4p-2 over D_(2p) with no identity 2p-subword in increasing original index order
has an admissible normal form (NF) with terminal k=p+1 and kappa_hat=kappa. FULL existential antecedent: SOME admissible
NF; the H=p-1-kappa extra reflection pairs lie anywhere in the odd blocks; every empty NF run separates different
reflection values (genuine empty-run rule); no o_F, nonempty-run, rotation-pair or reflection-rigidity hypothesis; no
multiset-only statement outside this antecedent. Deliver ONE written proof of exclusion for this exact family, OR the
exact first failing lemma or inequality with every proved partial range named (completed steps kept, failed branches
recorded). The cases (kappa,p) = (4,13) and (5,17) are written out explicitly. Labelled PARTIAL of ordered Olson in every
outcome. Optional, only after the primary target is settled: a statement for general deficiency delta := 4kappa-p-1 (the
target is delta = 2); any such text is either separately proved and scoped or explicitly marked as a non-claim remark.
Not in scope: kappa_hat = 0; p = 7; any other middle-range cell beyond the optional delta statement; cells already accepted
(USK range 3 <= kappa <= floor((p-1)/4), kappa_hat <= 3 at p >= 13, upper half); full ordered Olson. No claim of "first",
novelty, priority, "full Olson", human review or Lean.

## Accepted inputs (literal scopes; every hash re-checked before this freeze)
- PL = .../olson/continuations/lowerhalf-terminal-cell/proof-LOWER-v1.md, SHA256
  251c8dca1c34be7b76432dc50d13368b11a7bf6da6bbb8bd31e4ee18e7cd476d, Secs. 2, 4-6 (lines 40-50 and 61-106), accepted relative
  to its inputs by the K1 verdict (RUN/review/olson-LOWER-K1-parent-verdict-v1.md
  93ea601c1255f52a8a186002e9e46986c99db1c81a1c4aba68eb6143ca926e83) with the LOWER parent erratum
  (RUN/review/olson-LOWER-parent-erratum-v1.md 087ab3ae6e880633b26658ff68e8f787bdb59758a4a0662bc7744aeea5b96377: m(P) = half
  the number of sign transitions; theta only through explicit pairs). PL's standing range p >= 11, 1 <= kappa <= (p-3)/2
  contains p = 4kappa-3, kappa >= 4 (kappa = (p+3)/4 <= (p-3)/2 iff p >= 9). Used: (SR) from the GRX if-direction; IF(a)
  and the gamma-normalisation; the explicit SS bijection (instantiated through a density lemma RE-PROVED here); the LT
  argument (re-derived). PL Lemmas D, U, A, C, THETA are NOT imported (new proofs at p = 4kappa-3).
- Frame inputs as PL uses them (the 19 pinned ranges of the FCW manifest, used only at their own accepted scopes): NF
  (ROT/proof-ROT-few-E-v4.md lines 28-43, ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f), GRX if-direction
  (ROT/notes-GRX-v1.md lines 7-20, afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30), the (S1) definition
  (R16/olson-zx-s1c-parent-verdict-v1.md line 19, 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af), SC0
  (R16/olson-index-one-primary-statement-parent-v1.md lines 1-11, e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6;
  read through the standard step "append z = -sum(Y') to a zero-sum-free Y'", which is written out in full), ZSTRUCT and FB
  in (S') (R18/olson-FB-parent-verdict-v1.md 8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a; FBP/proof-FB-v1.md
  lines 9-24, 339dcadcd914a9f036ea71a5ec2b5d3f0678cc100e22aca9de2d75751373cc6b; erratum 1
  33de46d245ec89a31cce1a06ac44a11f2c81c91a713b0830c59f31686245e202; (S') extension R18/olson-balfull-rotzb-parent-verdict-v1.md
  lines 26-34, 56b988ee90805f850760c6969d9724f890fb637335248b9060189ef99b1e1bc0), applied at (k',kappa') = (p-1,kappa-1) only
  after its hypotheses are re-checked at p = 4kappa-3.
- USK verdict RUN/review/olson-USK-parent-verdict-v1.md 6d3358ce3f1e9e95a366f2b32f10adbc73df607bc62723f561567dce1a53de18
  with parent errata v1 85718782c14dcb913706d5b7245ebfda1ef50ef1e9e7661d671a9ecbfcf4519e and v2
  4f3a2636594787337ebe8294dc086f8a3af9dccea89d5599e95e802e95590bfe: context only. Theorem USK is accepted ONLY at
  3 <= kappa <= floor((p-1)/4); nothing of it is transferred to p = 4kappa-3.
- K3 verdict RUN/review/olson-K3-parent-verdict-v1.md 9281cbc64bd2bc59edf7a8404481765d5d5d39c351ce5b2b28c35b6e6e03a9f6 with
  erratum 8653cb3e183a6c8d21e95e971de95b598a5a29cb94e90bb69de6173623c332af: context only (kappa_hat = 3 is not this target).
- Not planned as premises: S1(a), the Setting fact, FB-E, Theorem P, B0S-CJ''', K3-11, PL Secs. 3, 7-9.

## Untrusted context (never a premise)
- FCW proof .../lowerhalf-first-cut-window-boundary/proof-FCW-v1.md, SHA256
  c23fd0378f68611070e3bf0fd74d66d1f7ad859bb01ccc1af4ce9a77cf4aaecf (first-family review only, NOT accepted): its methods may be
  re-derived at p = 4kappa-3; no FCW lemma is cited as a premise. Its manifest review-excerpts-FCW-v1.json
  (a3225345e84476d296357d64e6055dbfd95ad79e71521b8431969e733a53e143) is used only to locate accepted ranges, each re-hashed.
- The parent's prior exposure in the transition JSON (FCW Sec. 5 slack 4kappa-p; W_kappa = [2,2p-2kappa] and
  W_(kappa+1) = [0,2p-2kappa-2] lose delta at the top; "whether the losses fit is UNKNOWN"): disclosed route exposure only.

## Pre-freeze exposure (none is a premise)
Read before this freeze: the transition JSON; the USK verdict and errata v1/v2; the K3 verdict and erratum; the LOWER-K1
verdict and LOWER parent erratum; FCW-scope-v1.md, proof-FCW-v1.md, review-package-FCW-v1.md, review-excerpts-FCW-v1.json;
the parent records RUN/review/olson-FCW-parent-written-check-v1.md (0b6f88fd2d63402c1126fa1181e2bb83b8c063a2ab83440c60d354224a40731a)
and olson-FCW-first-family-parent-disposition-v1.json (first-family 0F/0M/0m; interface note that SC0 is read through the
"append z = -sum(Y')" step); PL lines 1-130; NF text lines 20-45; GRX notes lines 1-55; the SC0 record; the FB verdict;
proof-FB-v1.md lines 1-30; FB erratum 1; balfull-rotzb verdict lines 20-40; zx-s1c verdict lines 15-22.
Before this freeze I also made UNWRITTEN preliminary checks of the window arithmetic and of the route below; they are
recorded here as unverified remarks and are re-derived in the proof:
at p = 4kappa-3: N = p+1 = 4kappa-2 runs, R = p-1+2kappa = 6kappa-4, 2p = 8kappa-6, H = 3kappa-4, F = 10kappa-10;
W_m = [max(0,2kappa+2-2m), min(R,2p-2m)] gives W_(kappa-1) = [4,R], W_kappa = [2,R-2], W_(kappa+1) = [0,R-4];
the FCW choice P1 = {0,3,...,3kappa}, P2 = {1,4,...,3kappa+1} is not available at kappa = 4 (N = 14 cannot hold
2kappa+2 = 10 runs in kappa+1 = 5 separated intervals), so the additive-constant step needs another pair; the alternating
sets have 2kappa-1 runs each; m = kappa+1 patterns whose letter values have at most two letters of one sign may lose
values at one end of the window.
Planned route: (1) windows; (2) frame, labels, density and the lift inequality re-derived at p = 4kappa-3; (3) a
realisation lemma for m = kappa (window [2,R-2]) and m = kappa+1 (window [0,R-4]) by minimal representations, with the
near-single-signed patterns treated explicitly; (4) a common representative window for all patterns with m in
{kappa,kappa+1}, possibly wider than [Pi0, 2p-nu0], and additivity/complement/theta lemmas with explicit margins;
(5) connectivity, an additive-constant pair valid at kappa = 4, link to independent kappa-sets, complement total;
(6) sorting the top kappa runs of each alternating set, with single-signed and empty-run cases explicit; (7) final count;
(8) (4,13) and (5,17) written out; otherwise the exact first failing step with proved partial ranges.

## Deliverables
DIR/proof-SCW-v1.md (Sec. 0 statement; exclusion or exact first failing lemma with proved partial ranges; interface table
input/path/whole SHA256/lines/scope-use; explicit not-claimed list), DIR/review-excerpts-SCW-v1.json (JSON list of
{path,sha256,start,end}, absolute paths, inclusive LF ranges; includes this scope and the proof), DIR/review-package-SCW-v1.md
(claims, manifest hash, process disclosure), DIR/checkpoints/checkpoint-NNN.md at most 1800 s apart (target 1200 s;
/bin/date immediately before each timestamp); packet <= 100 KB; then park.
