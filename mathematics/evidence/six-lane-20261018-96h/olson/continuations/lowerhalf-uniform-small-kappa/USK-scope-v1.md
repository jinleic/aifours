# Frozen scope: lower-half terminal k=p+1, uniform cells 3 <= kappa_hat <= floor((p-1)/4), v1

Owner OlsonUniformSmallKappa (math2 Olson slot, THROTTLED, no extra slots). Frozen after /bin/date 2026-10-20T00:25:01-0700 BEFORE derivation
for this target. Authority: RUN/control/written-olson-uniform-small-kappa-transition-v1.json, whole-file SHA256
3ea785068797a0e0939d9c9130cee764a2774219717d8f7901cd7147919cb4ca (at 2026-10-20T00:21:43-0700),
RUN=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h. Exactly ONE deliverable (one packet <=100 KB), then
park. Not a new target or runtime authority. All prior artifacts read-only. Writes ONLY in
DIR=/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-uniform-small-kappa;
every file created exclusively (mode x), never edited or deleted; corrections are new versioned errata. Written mathematics
only; metadata limited to sha256, byte counts, line ranges and /bin/date. NO scientific scripts, assertions, enumeration,
solvers, tests, model CLIs, nested agents, /tmp, global configuration, commits/pushes, external contact or paid API.

## Exact target
For every prime p and every integer kappa with 3 <= kappa <= floor((p-1)/4) (so p >= 13; equivalently 4kappa+1 <= p), no
word w of length 4p-2 over D_(2p) with no identity 2p-subword in increasing original index order has an admissible NF u
with terminal k=p+1 and kappa_hat=kappa. FULL existential antecedent: SOME admissible NF; the H=p-1-kappa extra reflection
pairs lie anywhere in the odd blocks; every empty NF run separates different reflection values (genuine empty-run rule);
no o_F, nonempty-run, rotation-pair or reflection-rigidity hypothesis; no multiset-only statement outside this antecedent.
Deliver ONE written proof of this uniform theorem, OR the exact first failing lemma/inequality with its exact (kappa,p)
range (all completed steps kept, failed branches recorded). The endpoint p=4kappa+1 and the smallest case kappa=3, p=13
are treated explicitly. Labelled PARTIAL of ordered Olson in every outcome.
Not in scope: the p=11 kappa_hat=3 residual; kappa_hat > (p-1)/4; kappa_hat <= 2 (K1/K2, separately accepted); full
ordered Olson. No claim of "first", novelty, priority, "full Olson", human review or Lean.

## Accepted inputs (literal scopes)
- PL = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-terminal-cell/proof-LOWER-v1.md,
  SHA256 251c8dca1c34be7b76432dc50d13368b11a7bf6da6bbb8bd31e4ee18e7cd476d, Secs. 1-7 only: Theorem S frame for prime p>=11,
  1<=kappa<=(p-3)/2 (contains the target range since (p-1)/4 <= (p-3)/2 for p>=5): (SR) windows, Lemmas IF, D, SS, LT,
  U, A, C, THETA, relative to PL's inputs NF, GRX (if direction), Theorem P (Sec. 3), S1(a), SC0, ZSTRUCT/FB/FB-E with the
  (S') extension and Setting fact, each used only as PL uses it. PL Secs. 8-9 (K1, conditional CR) are not premises.
- LOWER parent erratum RUN/review/olson-LOWER-parent-erratum-v1.md, SHA256
  087ab3ae6e880633b26658ff68e8f787bdb59758a4a0662bc7744aeea5b96377: m(P) = half the number of sign transitions
  (m(empty) = m(all runs) = 0); theta_i is defined only through an explicit full pair; CR is conditional only.
- K1 parent verdict RUN/review/olson-LOWER-K1-parent-verdict-v1.md, SHA256
  93ea601c1255f52a8a186002e9e46986c99db1c81a1c4aba68eb6143ca926e83 (acceptance of Theorem S relative to its inputs).
- B0S-CJ''' (/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-cj-cjx-parent-verdict-v1.md
  lines 8-15, SHA256 5cfd6a4fe15cab133e210cd6f6966e34fa633d1a8c432b79eb537c0016145f6d), only for the all-rotations-equal
  non-identity sub-case, at its literal antecedent (checked at k=p+1, lower half, in PL Sec. 1).
- Context only, NOT premises: accepted K2 verdict RUN/review/olson-K2-parent-verdict-v1.md (SHA256
  5ca98c9a81b2e1607cf5f562bc276ad29ed81feb774857f1428e657293db04c7) and its proof proof-K2-v1.md (SHA256
  04dc8c68cbe80044c040ea9d6a85acb12960094b0a06f7ce90106af6a8193272); untrusted K3 candidate proof-K3-v1.md (SHA256
  35ea47b03ad4a2c57c5b1430dfd642d524a935ae0c152ad220d5bb388da4ab30) and P11R candidate proof-P11R-v1.md (SHA256
  6ee3df0985f02d01e6cde08c88944791b91dbc76e389e20f16e6b9accec87ac4). Every needed step is re-derived here.

## Pre-freeze exposure (none is a premise)
Read before freezing: the transition JSON; PL in full; the LOWER parent erratum; the K1 and K2 parent verdicts;
K3-scope-v1.md (SHA256 5b04e5ac805c225f25820d52447752ebc6a8d6278dde9e459a24ca38c7c12676, incl. its unverified kappa=3
window remarks); P11R checkpoint-003.md (SHA256 ac6c176e9134c4796c36b16b46d1042451799d52134faf109060935d11f88aeb; summary
only); the K3 excerpts manifest (format only). NOT read before freezing: proof-K2-v1.md, proof-K3-v1.md, proof-P11R-v1.md;
they may be read after this freeze as context only, and any reuse is re-derived and disclosed in the proof.
Remarks noted before freezing, unverified: (i) the m=kappa+1 (SR) window is [0, min(R,2p-2kappa-2)], equal to [0,R] iff
p >= 4kappa+1 (R = p+2kappa-1); for m >= kappa+1 the window is [0,R] iff m <= (p+1)/2-kappa, so at p=4kappa+1 ONLY
m=kappa+1 qualifies; (ii) a pattern whose window is [0,R] is full by Lemma SS (parity), suggesting the family
F = (m(P)=kappa+1); (iii) rigidity as in PL Lemma CR but using only (kappa+1)-subsets of the alternating sets plus a
complement total from Lemma C on a pair in F, avoiding (H-ALT); (iv) if B* >= R then 2Pi0+3+nu0 > 2p iff
nu0 <= 4kappa + 2(B*-R).
Planned route: (1) windows; (2) negative-letter lemma at the empty pattern (window [2kappa+2,R]) bounding |A-|+nu0 and
giving 2Pi0+3+nu0>2p; (3) lift framework on F: explicit full pairs for theta, toggle connectivity, two explicit disjoint
members with union in F (Lemma A), complement total (Lemma C), valid for every N=p+1 >= 4kappa+2; (4) rigidity: B*=R and
tight theta data; (5) final cases over nu0 with explicit (SR) selections, valid sizes and nonempty-run arguments, CJ''' for
all-equal; the endpoint p=4kappa+1 and (kappa,p)=(3,13) explicit; (6) otherwise the exact first failing step.

## Deliverables
DIR/proof-USK-v1.md (uniform theorem or exact obstruction, with interface table), DIR/review-package-USK-v1.md,
DIR/review-excerpts-USK-v1.json ({path,sha256,start,end}, every hash re-checked), DIR/checkpoints/checkpoint-NNN.md at most
1800 s apart (/bin/date immediately before each timestamp); packet <=100 KB; exact pins to Main; then park.
