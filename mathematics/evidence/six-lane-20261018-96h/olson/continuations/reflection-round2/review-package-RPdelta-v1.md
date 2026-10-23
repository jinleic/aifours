# RPdelta written review package v1: SEG-k, TRANSFER, region (B), B-prime

Owner OlsonReflectionSuccessor.  Frozen after /bin/date observation 2026-10-19T08:26:44-0700.  CANDIDATE review package;
written mathematics only.  No computation, finite search, model call or review launch by the worker.  Earlier sources remain
unchanged.  Parent requested this as the next slice after freezing RP-LIFT for dual review.

## 0. Governing scope and reading order

This packet reviews ONLY the eight frozen candidate source/erratum files in Sec. 1 and their deductions.  The accepted
baseline is the parent verdict
`/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-REFLHI-v5-parent-verdict-v1.md`,
SHA256 `13ee1ba86245fc549bd79c130a9fe15248ecc3fe9fc8428e875ca939c940a547` (V5 below).  V5 lines 56-59 expressly exclude these
separate files from its acceptance.  Their statements remain CANDIDATE_UNVERIFIED.

V5, not stale candidate headers, governs every v5 import: all errata 1-5 and bindings S1/m1-m7 apply.  Erratum 5 Part II is
accepted and erratum 4's narrowing is superseded; Theorem SEG holds under its printed hypotheses for every R.  None of the
new applications needs its R>2p branch.  Accepted interfaces may be taken as premises at the scopes stated in Sec. 2; this
is not a request to repeat the already completed foundation review.

`review-excerpts-RPdelta-v1.json` (same directory) is an ordered array of `{path, sha256, start, end}`.  Hashes bind WHOLE
source files; lines are one-based and inclusive, read raw (no contextual lines, no ellipses).  Repeated entries select disjoint
ranges.  Supply this package once plus all selected excerpts; the manifest does not include the package or itself.
The packet is required to remain below 120000 UTF-8 bytes; byte/hash checks are packaging metadata only, not scientific
computation.  The exact measured count accompanies delivery to the parent.

RP-LIFT is in a different frozen review and is NOT an import, comparison baseline, or proof premise here.  No integer-lift
claim, STAB statement, unrestricted rotation rigidity, INV*, ordered Olson, novelty or formal verification is assumed.

Ambient notation for the numerical exclusions: p>=5 prime, w length 4p-2 over D_(2p), rotations in one nonzero pair,
normalised to {rho_1,rho_-1} and A>=B.  Unless discussing TRANSFER's INITIAL word, every maximal cyclic CONSTANT reflection
block is odd.  k counts those blocks, H=sum floor(l_i/2), kappa=p-1-H, R=A+B=2p-k+2kappa.  Empty rotation runs must be
genuine.  An avoider has no increasing-index identity 2p-subword.  No purity or B<kappa restriction is imposed on SEG-k,
Theorems B/B-prime, or their elementary lemmas; RES_< consequences retain their additional pure-run, empty-run and B<kappa
conditions.  The initial word of TRANSFER may have EVEN blocks; its terminal word is all-odd.

## 1. Frozen candidate texts and exact statements

All paths in this table are absolute; each file is supplied in full by the excerpt manifest.  Nothing from a superseded
v1 or a stale unreviewed inventory is an additional theorem.

| ID | Path | Whole-file SHA256 | Lines |
|---|---|---|---|
| K | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5-addendum-SEGk-v2.md` | `b6d526829c9065eeefe75e8cbf7c12c31c88950f9de8788729a55144810a70d5` | 1-41 |
| K-e | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5-addendum-SEGk-v2-erratum-1.md` | `7030b7583a47f777a52f5d352795c4e1a1a200c879625ce6fce52b3ecc82a8e3` | 1-21 |
| T | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-transfer-v2.md` | `dc1974c8e8c8229002dd02e6bb4ef1e97cd123f7d411479bcd7d8cc9b58729fa` | 1-72 |
| B | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-regionB-v2.md` | `35948d69955ab44faa6464741a2190c97d528218334101b8fc02674422640af3` | 1-98 |
| B-e1 | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-regionB-v2-erratum-1.md` | `94a018c5dbf63112157c6f6c6564887a24e934a1ce68eb7102c14b4c1f0543e3` | 1-7 |
| B-e2 | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-regionB-v2-erratum-2.md` | `f6fc960f3dc49ac1464ae24f792937fa772e268c23f0a7b77574de4eaee46d56` | 1-16 |
| BP | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-regionB-v2-addendum-Bprime-v1.md` | `4a5b00570d72b8b812129944cf980dd10752d97ed127130517d3429b1317dcc5` | 1-39 |
| BP-e | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-regionB-v2-addendum-Bprime-v1-erratum-1.md` | `fa4c249e1dff1ee8a887aa0c29dafc547cf730bde0fffa7d71e84202ce626943` | 1-5 |

### K: Corollary SEG-k (K9-27 read through K-e)

Under the all-odd ambient hypotheses, if
   k >= 4 kappa + 5   AND   k >= p + floor(R/2) + 1,
then w has an identity 2p-subword.  Any B, any run purity, any reflection values.  R=0 is handled separately by AR.
The candidate proves the three hypotheses of accepted Theorem SEG using q (number of nonempty runs),
q>=k-2kappa, q<=R, and d<=R-q+1.  K-e replaces the erroneous direction of the max(1,.) width argument by a two-case proof;
no old erroneous max-branch inference is an import.  The (Pairs) fact handles kappa<0 before the contradiction proof.

### T: Lemma INV, box transfer, T1-T3 (T15-65)

Initial w0 has length 4p-2, rotations in one pair, A0>=B0, D0=A0-B0 and g0=kappa0-B0.  Its maximal constant blocks may be
even or odd.  If reflection rigidity fails, accepted RED produces a terminal avoider in RES_< with kappa_T>=2.
INV claims D is constant and B,kappa,g=kappa-B never increase along the actual maximal-decomposition P1-P4 process.  Thus
   1<=g_T<=g0,  0<=B_T<=B0,  R_T=D0+2B_T>=p,
   k_T=2p-D0+2g_T,  kappa_T=g_T+B_T>=2.
For a box cell (g,b) with 1<=g<=g0, 0<=b<=B0, g+b>=2 define k=2p-D0+2g, kappa=g+b, R=D0+2b,
Delta=p+kappa-1-R.  TRANSFER claims REFL for w0 if every cell satisfies at least one of:
(a) k<=p; (b) k>=2p+1 and k>=3kappa+3; (c) both SEG-k inequalities;
(d) p>=11, R=p, kappa>=(p+1)/4; (e) R<p;
(f) b=0, R>=4kappa-4 and [Delta<=1 OR p>=kappa+5Delta-5].
Sources: (a) SMALLK; (b),(d),(e) accepted V5; (c) K (candidate within this packet); (f) accepted CJ/EDGE at their B=0 scope.
If clause (f) has R>=2p, the 2p equal rotations already solve the word; otherwise the accepted CJ/EDGE range R<=2p-1 is
satisfied.  This makes explicit the trivial cut implicit in T(f); no enlarged CJ theorem is used.
T1: |A0-B0|<=1 and o_F(w0)>=3kappa0+3 imply REFL for the initial avoider w0.
T2: o_F(w0)>=4kappa0+5 and A0+floor((A0-B0)/2)<=p+1 imply REFL for w0 (depends on K).
T3: under o_F(w0)>=3kappa0+3, only box cells with D0-p<2g<=D0 need checking; the others are covered by (a)/(b).
o_F always counts odd maximal cyclic CONSTANT blocks, not reflection runs.  No caller may assume these corollaries when
constructing RED or its RGR imports; the dependency is RED -> INV -> TRANSFER, not a cycle.

### B: counting lemmas, mixed gain accounting, Theorem B and B.4

Let eps in {0,1}, kappa=(p-1)/2-eps, R=p+delta, delta>=1, k=2p-1-2eps-delta.  For an avoider define q nonempty runs,
x=R-q, g_E=k-q, d=max|a_j-b_j| over nonempty runs; C/AB/L classify maximal reflection runs with 1/2/at-least-3 BLOCKS.
Lemma B.1 (B17-22): p-delta<=q<=p+delta, 0<=x<=2delta, g_E=p-1-2eps-2delta+x, d<=x+1, and
|L|<=(g_E-|AB|)/2.  Lemma B.2 (B23-32) supplies the exact bounds on m_lo,m_hi,N_O for delta<=(p-12)/3; review them as printed.
B36-54 constructs the base AB-first, then C, then L.  A selected L-run supplies a pair-arc on its first two blocks; the
remaining blocks form a segment.  The new counting uses rate-2 segment units first, then rate-1 units.  B-e2 governs:
W2 and W1 are capacities and every certified segment gain is min(p-1,2t,b'-1), with the cap harmless until the target
Pi_need=p-ceil(R/2)<=(p-1)/2 is reached.  Lemma B.3 is the ensuing balanced-window kill.
Theorem B (B58-77, B-e1): any all-odd ambient word with
   1<=delta<=(2p-29+2eps)/7
is solvable (any B, no run purity).  Nonempty for eps=0 at p>=19; eps=1 at p>=17.
B.4 (B87-93): a remaining avoider with 1<=delta<=(p-12)/3 must satisfy
   |AB|<=N_O   AND   2x<7delta-2p+29-2eps.
This is necessary word structure, not universal exclusion of its remaining parameter cells.

### BP: Theorem B-prime (BP9-31 read with BP-e and B-e2)

Same all-odd ambient and eps,kappa,R parameters as Theorem B.  If
   1<=delta<=min((p-12+4eps)/3, (2p-32+2eps)/3),
then w is solvable, any B.  BP keeps floor(d/2)<=floor((x+1)/2) rather than replacing it uniformly by delta, and rechecks
B.2's actual required bounds when eps=1 permits a slightly larger delta.  It uses B's construction and capped-gain
accounting, not accepted Theorem SEG.  BP-e fixes only the comparison example at p=19 (B gave delta<=1 for each eps).

## 2. Accepted imports: exact records, ranges, and uses

The manifest supplies these accepted INTERFACES, not a re-review of every upstream proof.  Their classical and RGR
trust limits stay as recorded.  All whole-file SHA256s were checked before packaging.

| ID | Exact path | SHA256 | Inclusive ranges | Scope / use |
|---|---|---|---|---|
| V5 | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-REFLHI-v5-parent-verdict-v1.md` | `13ee1ba86245fc549bd79c130a9fe15248ecc3fe9fc8428e875ca939c940a547` | 1-61 | Authority for v5 interfaces and all binding readings; accepted I.14 baseline at31-40; candidates excluded from verdict at56 |
| A5 | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5.md` | `4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c` | 38-108,121-143 | Setting, W, P0-derived Fact2.2, floor condition; ARC+, Lemma SEG, labels/BAL; K2P+ and Theorem SEG. All are accepted by V5:27-30, not new hypotheses of this packet |
| A5-e2 | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5-erratum-2.md` | `b4451461bc6495e1b66588ddb762eb19ddd0428e8aad0c6b8fadc298476b8820` | 1-21 | Singleton/pair restriction; read with A5-e5 I.7 and V5 S1/m1 (SEG/MID toggle unique base arcs directly, not the priority e5 recipe) |
| A5-e5 | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5-erratum-5.md` | `40832206bf581a685266c4f885ecf2d3008e6e362b6a791acc11fa2527d325f4` | 35-92,120-144 | I.1-I.9 repaired foundations, m_b>=1, capped gains, arc choices and BAL; I.12 gain loop, I.13 max-branch proof. V5 overrides obsolete 'not accepted' labels and is the authority |
| V-RED | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-reflection-K0star-RED-parent-verdict-v1.md` | `879aeee781a080d1b1cb4a4489f62e45e2fa332f7c2d9242f725cfae1d00c02a` | 1-8,36-39 | K0*/RED acceptance and mandatory P4 bookkeeping correction; imported RGR I1-I4 only at the RED-produced RGR exits |
| K0 | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/proof-K0star-r2.md` | `6681676e4f80018e792c7117ce9fc524a31aeb397c35880f57468ada9c0396e1` | 14-36,66-75,84-97,104-114 | Definitions/maximality, normalisations, (0.1), AR/Pairs/P0, FUS double-fusion H change, TR and PM0. Used in K's degeneracies and T's process invariants; authority V-RED |
| RED | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/proof-RED-r2.md` | `c4e7697f0f691980e19ef3332a1e2c6b0dbdc76ba268e87c32eb563f4d3fd3d7` | 132-164 | Exact RES_< definition, moves, exits and all-odd terminal kappa>=2. T uses the accepted proof, not only the theorem statement; read L147 through V-RED39 and MON104-111 below |
| MON | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/proof-REFL-fewodd-r5.md` | `4615dcb957966ee4c18166c269e1c9c8a1bc4ee6f9bc48539155079b297a5363` | 79-112 | Maximal-decomposition move bookkeeping: P4 inserts into a block OF THE SAME VALUE; extra kappa drop only when fused neighbours are both odd. Supports T18-27; no unrestricted monotonicity beyond these moves |
| V-FEW | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-refl-fewodd-parent-verdict-v1.md` | `16436c07e2dc1b6b773989b2ff5d05900ea92f8e6c1d681b0c5979673688f1ca` | 1-16 | Authority for MON and few-odd scope; verdict binds r4, r5 supplies its explicit errata-only bookkeeping (also imported through accepted V5) |
| V-SMALL | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-reflection-smallk-parent-verdict-v1.md` | `b71fcaf461a98bf9f034871208a298a471dcbb2006aa26c9153d523e140413b8` | 1-15 | No avoider of RES_< with k<=p; T(a) only, not arbitrary mixed words outside the residual definition |
| V-CJ | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-cj-cjx-parent-verdict-v1.md` | `5cfd6a4fe15cab133e210cd6f6966e34fa633d1a8c432b79eb537c0016145f6d` | 1-17,27-34 | Exact B=0 setting and Cor2 (Delta<=1 or p>=kappa+5Delta-5), with mandatory overlay; T(f) only |
| V-EDGE | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-edge-parent-verdict-v1.md` | `d2b67d96ee697da6536c443354a2ea9f6a7bb32851ecd07fff9050c2fd40b58b` | 1-18,45-55 | Extends CJ''' to R>=4kappa-4 without 2kappa<=p-1; retains all other Cor2 hypotheses/overlay. T(f) only; R>=2p handled by equal-rotation selection, not an enlarged EDGE statement |

Per new proof the non-elementary bridge is therefore:
K -> accepted Theorem SEG + P0/Pairs/AR;
T -> accepted RED proof/move bookkeeping + SMALLK + accepted V5 numerical exclusions + K(candidate) + accepted CJ/EDGE;
B/BP -> accepted W/floor condition/ARC+/Lemma SEG/labels/BAL, with a NEW rate-2/rate-1 allocation and inequalities.
Classical Cauchy-Davenport enters only inside those accepted lemmas (no fresh external theorem).  The RGR theorems imported
by RED are not extended to genuine empty runs.  Nothing uses the unreviewed documentation successors K0star-r3/RED-r3.

## 3. EXACT delta beyond accepted I.14 (not a novelty claim)

For a fixed p and R=p+delta with delta>=1, restrict to the RES-HI cells under discussion (kappa>=2, k=p-delta+2kappa>=p+1,
B<kappa and the actual residual word hypotheses).  Let an integer interval with lower endpoint above its upper endpoint
mean the empty set.  The accepted I.14 numerical set is
   A(p,delta) = [ceil((p+3delta+2)/4), floor((p-delta-4)/2)]_Z
                union [ceil((p+delta+1)/2), p-delta-3]_Z.                                                 (D0)
Words that satisfy the accepted RAW structural Theorem SEG can already be excluded outside A; the delta below is to I.14's
UNIVERSAL NUMERICAL bands, not a disjointness claim against every accepted structural instance or B=0 CJ/EDGE import.

### 3.1 SEG-k: one precise parity endpoint, not an entire new band

Substitute k=p-delta+2kappa in K's two inequalities.  They are exactly
   ceil((delta+floor((p+delta)/2)+1)/2) <= kappa <= floor((p-delta-5)/2).                                    (D1)
For delta odd, D1's lower endpoint equals the accepted SEG-num lower endpoint and its upper endpoint is no larger: no
new I.14 cell.  For delta even, its upper endpoint equals floor((p-delta-4)/2) and the lower is
ceil((p+3delta+1)/4), which is one smaller than the accepted lower endpoint ONLY if p+3delta=3 (mod 4).  Thus the exact
new R>p cells are
   delta>=2 even,  p+3delta=3 (mod4),  p>=5delta+11,  kappa=(p+3delta+1)/4,  k=p-delta+2kappa.                  (D2)
They are below the accepted K2P+ lower bound as well.  Example (arithmetic, not a search): p=29,delta=2,kappa=9,k=45;
accepted SEG-num begins at kappa=10 and accepted K2P+ begins at16.  For delta=0, D1 adds no universal cell beyond I.14's R=p
table (including the small primes).
Derivation of p>=5delta+11: in this parity case the candidate point is an integer and lies below the D1 upper endpoint iff
p+3delta+1<=2p-2delta-10.  D2 is an exact restatement to be checked, not a stronger hypothesis silently replacing K.

### 3.2 Theorem B and B-prime: two near-middle rows outside BOTH accepted bands

For each eps in {0,1} set
   kappa_eps=(p-1)/2-eps,
   M_B(p,eps)=floor((2p-29+2eps)/7),
   M_BP(p,eps)=min(floor((p-12+4eps)/3), floor((2p-32+2eps)/3)).
B adds all cells (p,kappa_eps,delta) with 1<=delta<=M_B; BP adds all with 1<=delta<=M_BP.  For every such cell,
   kappa_eps > (p-delta-4)/2   and   kappa_eps < (p+delta+1)/2,
so it lies in neither interval of A(p,delta).  Thus every positive-delta cell claimed by B/BP is new to I.14's numerical
bands.  BP contains B whenever B is nonempty; BP's additional cells beyond B itself are precisely
   M_B < delta <= M_BP,  delta>=1,  kappa=kappa_eps.                                                       (D3)
B4 is a structural restriction, not another universal band; when its interval is already covered by BP it is vacuous there.
Examples from the formulas only: p=19 BP adds delta=1,2 on both rows; p=31 BP adds delta=1..6 on eps=0 and1..7 on eps=1.
No existence of avoiders, realizability census or literature-wide newness is asserted by these examples.

### 3.3 TRANSFER: initial-word reflection corollaries, not another terminal exclusion band

TRANSFER adds no independent R=p+delta terminal cells beyond its component clauses.  In terminal coordinates
   delta_b=D0+2b-p, kappa=g+b, k=2p-D0+2g,
clauses (b),(d),(e) use the accepted V5 exclusions; clause (c) contributes exactly the candidate K cells (D1), whose
numerically new subset is D2; clause (a) is accepted SMALLK, and clause (f) is a previously accepted B=0 exclusion, not a
new result of this packet.  The NEW claim is a transfer of these exclusions through an entire box of possible RED
terminals to INITIAL words with arbitrary block parity.  Its explicit initial families T1/T2 are exactly those in Sec. 1;
new potential applicability beyond the old few-odd result is their o_F(w0)>p part.  They are not proofs that avoiders exist
with those parameters, and no exact count of newly covered initial words is claimed.
T1 uses only accepted K2P+ plus the NEW process invariant/box proof.  T2 additionally depends on accepting K in this packet.

## 4. Reviewer focus and mandatory precision checks

Return separate dispositions for K; INV/TRANSFER/T1-T3; B1-B3/Theorem B/B4; and BP.  Accepted interfaces in Sec. 2 may be
assumed, but every new use must meet their literal hypotheses.  Check:
1. K: both branches of max(1,.) in K-e; positivity of Pi_need (R<=2p-2 here), the (Pairs) degeneracy kappa<0, and exact parity
   endpoints D1/D2.  Historical Range/Remaining prose in the source is not an exhaustive current ledger; D0-D3 govern this
   package's comparison.
2. T: bookkeeping on the ACTUAL maximal decomposition: P1 raises H only for odd-odd double fusion, P2 keeps H, P3 keeps
   A/B/H, P4 lowers A/B by1 and raises H by1 plus a possible odd-odd neighbour fusion.  No splitting by inserting the
   reflection pair into a block of a DIFFERENT value.  Check B/g monotonicity, terminal R>=p, empty boxes, and every clause's
   hypotheses.  SMALLK is residual-only; CJ/EDGE is B=0-only with the trivial equal-rotation cut for R>=2p.
3. B/BP: O_0 puts AB first, C second and L last.  Base arcs in L are TWO-block arcs, not the singleton bases of accepted
   Theorem SEG.  The parity move deletes/adds that base arc directly (the accepted priority e5 realisation recipe is not
   claimed to implement this particular construction).  Keep lambda=|L intersect O_0| separate from |L intersect O|.
4. Rate accounting: a base pair-arc is one arc; an optional pair is TWO singleton arcs and raises m by1.  A selected L-run
   leaves blocks3..|M_i| as its segment; the unused gap after block2 has no gain.  W2/W1 are CAPACITIES, not uncapped actual
   cardinalities.  Gain is min(p-1,2t,b'-1).  Rate-1 units in a segment require its earlier rate-2 units, which are exhausted
   before the allocation reaches the rate-1 stage.  Total certified gain needs to reach Pi_need only, not all capacities.
5. Nonnegative-budget clarification for the new proofs: G_need=max(0,Pi_need-G_b).  Whenever the base already has
   G_b>=Pi_need, take every t_j=0; no upper bound by a negative expression is used.  In the budget lines B67-76/BP24-30
   involving Pi_need-a-lambda+2 or G_need-W2/2, the nontrivial estimates are used only on the branch G_need>0; otherwise
   m_b<=m_hi is enough.  This is an explicit proof-reading clarification, not an extra assumption or narrowed statement.
6. Establish d>=1 in the B/BP ranges before using B2(vii): P0 gives at least p-delta>0 odd nonempty runs (an odd-length
   rotation run has odd d_i), so the allowance of mixed rotation runs does not permit d=0 there.  Check m_lo>=1 without a
   hidden max branch, N_O<=q, every use of x<=2delta, and all ceil/floor endpoints for eps=0/1.
7. B-e1 fixes the sign in p>=6eps-3; BP-e fixes the p=19 comparison.  B-prime's eps=1 range can exceed the stated range of
   Lemma B.2, so BP16-23 must supply the REAL requirements afresh, not silently invoke that lemma beyond its hypotheses.
8. B4: a failing sufficient budget proves only its necessary inequality for a remaining avoider under its stated delta
   range; do not count it as universal exclusion of that inequality's cells.  Check equality cases at the strict boundary.
9. Neither the pending RP-LIFT candidate nor any result deduced from it may be used to reduce the review workload or to
   certify the frozen candidates here.  Parent V5 expressly leaves this packet's sources unaccepted.

## 5. Boundaries

Only source/hash/excerpt-byte metadata is inspected for packaging.  No finite calculation of words, theorem cases,
certificate checker, solver, test, or model run is performed.  Parent owns reviews and verdicts.  REFL(p), REFL-HI(p),
RES-HI(p), INV*(p), ordered Olson, priority and novelty are not claimed by this package.
