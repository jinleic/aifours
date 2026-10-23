# RP-2NE short written review package v1

OlsonReflectionSuccessor.  Frozen after /bin/date observation 2026-10-19T08:43:30-0700.  CANDIDATE_UNVERIFIED; written only.
No solver, probe, scientific enumeration, test/build, model call or review launch by the worker.  Parent owns both reviews.
This packet is independent of running RPdelta snapshots; it reviews exactly ONE new candidate (no new addendum).

## 1. Exact frozen claim and full source

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-RPdelta-two-neutral-v1.md`,
SHA256 `e6471758f0e5aaba016286ccfb0e901ecb5fc670b980728407c9bbd468c8fa20`, lines1-164 (FULL file).
Theorem RP-2NE: prime p>=5, delta in {1,2}, length4p-2 over D_(2p), R=p+delta rotations all in one nonzero pair,
every maximal cyclic CONSTANT reflection block odd, and
   delta+1<=kappa<=floor((p-delta-3)/2)
imply an identity2p-subword in increasing original index order.  ANY B, no purity, no B<kappa or inherited assumption,
no restriction on reflection values.  The candidate itself imposes no explicit genuine-empty-run hypothesis: the proof
under avoidance obtains at least two more genuine empty runs than zero increments from P0 and kappa>=delta+1.

The companion `review-excerpts-RP2NE-v1.json` lists ordered inclusive raw line ranges and full-source hashes.  It supplies
full candidate + ONLY the needed W/Fact2.1/P0/CONNECT/LIGHT interfaces, definitions and governing acceptance records.
Accepted proofs and theorems outside those interfaces need not be re-audited.  CONNECT/LIGHT are imported only within their
literal generic quantifiers.  All R>p fixed-window, lift and zero-vertex sign arguments are NEW material in this candidate.
Do not assume RP-LIFT's R=p theorem at R>p, or any result in SEG-k, TRANSFER, region-B/B-prime, STAB or current RPdelta reviews.

The notes `conditional-RPdelta-smallkappa-v1.md` and `proof-RPdelta-two-neutral-v1-addendum-Zsign-v1.md` are deliberately NOT
in this packet.  No statement in them may strengthen the frozen candidate.  In particular this packet does NOT claim the
extra delta2,kappa2 cell, even if some later note discusses it.

## 2. Authority and exact imported interfaces

| ID | Path, whole-source SHA256 | Inclusive lines | Exact scope and use |
|---|---|---|---|
| VL | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-RP-LIFT-parent-verdict-v1.md`; `e90b8be22a7bc06b0c20e305274436ceb48784e5a1844005437058d04dff8652` | 1-31 | CORRECTNESS_ACCEPTED_SCOPED_PARTIAL; all seven bindings, especially cyclic order, proper patterns including empty runs, CONNECT decrement and interior-path independence |
| V5 | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-REFLHI-v5-parent-verdict-v1.md`; `13ee1ba86245fc549bd79c130a9fe15248ecc3fe9fc8428e875ca939c940a547` | 9-40 | Setting(S), binding readings, accepted W/Fact2.1/2.2 and I.14 baseline; no purity/B<kappa assumption on those interfaces |
| W/Facts | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5.md`; `4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c` | 38-48 | All-odd H0 window gamma_m(E)=min(p-m,E-kappa+m-1,floor(E/2)); floor endpoint criterion; avoider R>=p and proof's o_R>=k-2kappa |
| CONNECT | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-Rp-integer-lift-v1.md`; `34cb5e007095b6d3c9c9eb91b2385c9e52cd94f78cd5b82c73bac8a31961df69` | 82-85 | For any k-cycle and 1<=m,2m<k, F_m of proper nonempty subsets with exactly m cyclic intervals is connected by one-index toggles, including complements; every index toggled. Authority VL, with its binding3 |
| LIGHT | same `proof-Rp-integer-lift-v1.md`, same SHA | 142-144 | Nonnegative weights on an n-cycle, n>=2f,f>=1: independent f-set weight<=f/n times total; also disjoint paths. Authority VL, bindings5-7 when used inside signed-stretch arguments |
| P0-source | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/proof-K0star-r2.md`; `6681676e4f80018e792c7117ce9fc524a31aeb397c35880f57468ada9c0396e1` | 14-36,66-75 | Maximal decomposition, empty-gap genuineness, normalisations, R=2p-o_F+2kappa; P0 exact statement e_R<=e_F+2kappa (EMPTY runs count as even). In the all-odd setting this is o_R>=k-2kappa=M |
| P0-authority | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-reflection-K0star-RED-parent-verdict-v1.md`; `879aeee781a080d1b1cb4a4489f62e45e2fa332f7c2d9242f725cfae1d00c02a` | 1-8,36-39 | Accepts K0star-r2 mathematics/proof with specified corrections; P0 is the source73-75 proof step from accepted Theorem P, not an extension to another class |
| P0-current-use | V5 above, plus `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-REFLHI-v5-foundation-claude-v1.prompt.note.md`; `300bebdaafb9864b7d4bddecc04d514799934f40af1f2d60d5319e9b3db26224` | V5:27-30; foundation150-154 | Current accepted Fact2.2 proof (v5:47) explicitly imports P0 and derives o_R>=k-2kappa. Foundation E3 records the exact inequality checked; authority is parent V5 acceptance, NOT model agreement as a premise |

Precise P0 bridge, included to avoid an imprecise 'previously accepted' label: for N=4p-2 an avoider obeys
F+sum floor(r_i/2)<=3p-2 by the accepted Theorem P used in P0-source73-75.  With F+R=4p-2, sum floor(r_i/2)=(R-o_R)/2,
this rearranges to R+o_R>=2p.  With R=2p-k+2kappa and all blocks odd it gives o_R>=k-2kappa=M, exactly as in the
currently accepted Fact2.2 proof.  This is the only P0 consequence used.  No new RGR/zero-gap extension is made.

## 3. New proof chain to audit (not imported from RP-LIFT)

1. Candidate Sec.2 sets M=p-delta, k=M+2kappa, L=kappa+1, U=ceil(M/2).  Check that the written kappa upper floor gives
M>=5, L<=U and 2m<k for EVERY integer m in [L,U], including even M (delta odd) and odd M (delta even).
2. For these m BOTH gamma endpoints are floor-type for EVERY integer E in [0,R].  The even-lift construction in C_(2p)
encodes u_P's congruence and the selected-rotation parity: a pattern kills iff psi(P)=e(2u_P)-E has a representative in
[-R,0].  Thus an avoider gives representatives N(P) in [1,M-1].  Check BOTH directions, E=0,R, and 0<=E<=R for mixed runs.
3. CONNECT gives an edge adding each i.  Differences of N lie in [-(M-2),M-2] (fewer than2p integers), so every adding edge
in every layer has the same integer h_i representing alpha_i=e(theta_i)-d_i.  Re-prove the constant-on-F_m equation and
complement cancellation with the changed M bound; do not reuse RP-LIFT's nonzero-h conclusion.  Constants c_m can differ.
4. Zeros: h_i=0 iff alpha_i=0 iff d_i is even AND theta_i=d_i modp.  Since r_i=d_i mod2, a zero lies in a nonempty EVEN run;
empty runs are nonzero even increments because the ORIGINAL maximal constant blocks have distinct neighbours there.
Let z=#zeros, v=#positive-even runs, o=#odd runs, q=o+v, e=g_E=k-q.  P0 gives o>=M; R>=o+2v gives z<=v<=delta<=2.
R>=q+v then gives e-z>=2(kappa-delta)+(v-z)>=2.  This is where kappa>=delta+1 is ESSENTIAL.
5. SIGN-2Z is new.  Each zero may initially be assigned either sign, but the proof uses the stronger marked-count e>z,
not a special zero-sign rule.  CaseA S>=k+e-z>k; CaseB S>=2m0-z because at most z sign stretches have only zeros; same-parity
flips leave 2U boundaries and S U/m0> M-2 for z=1,2 (or >=M for z=0).  Check weights may be zero, the strict inequality,
and the preservation of nonadjacent-stretch assumptions from VL binding7.
6. CaseC: n>=k-4m0 and n-2f>=M-2-2kappa>=1; the LIGHT coefficient 1-2f/n is strictly positive.  With e_J marked and z_J zero
counts, the baseline w_i>=1+1_marked-1_zero gives the displayed signed bound
M-2+2m0-z+(1-2f/n)e>M-2.  Both z<=2 and m0>=1 matter.  Path independence implies original-cycle independence (VL binding5).
7. CaseD: when m0=0, LIGHT gives S(M-2)/k>M-2, relying on S>k.  No claim for e=z or for a length2p witness obtained by
padding a local identity4 is allowed.  Candidate Sec.5 expressly leaves delta2,kappa2 and delta>=3 outside its theorem.
8. ANY B is literal: E=A_P+B_(P^c) and d_i=a_i-b_i may include mixed even runs.  The run-count arguments use lengths and
parity only; no one-sign or purity shortcut may be inserted.  Identity selections stay in original increasing order,
using the accepted cyclic-conjugation convention VL binding1.

## 4. Exact numerical delta against accepted I.14

Put A(p,delta) equal to the two ACCEPTED integer bands
   [ceil((p+3delta+2)/4),floor((p-delta-4)/2)]_Z
   union [ceil((p+delta+1)/2),p-delta-3]_Z,
with an interval empty if lower>upper.  This is comparison only to I.14 UNIVERSAL NUMERICAL bands; some words may already
meet accepted structural SEG or B=0 criteria.  No matched-literature novelty or existence-of-avoider claim.

* delta=1: RP-2NE gives kappa in [2,(p-5)/2]_Z (p>=11); accepted SEG-num intersects as
  [ceil((p+5)/4),(p-5)/2]_Z, and accepted K2P+ begins at (p+3)/2.  Thus the exact newly added cells are
      2<=kappa<=min((p-5)/2,ceil((p+5)/4)-1),   k=p-1+2kappa.
* delta=2: RP-2NE gives kappa in [3,(p-5)/2]_Z (p>=11); accepted SEG-num intersects as
  [ceil((p+8)/4),(p-7)/2]_Z, and accepted K2P+ begins at (p+3)/2.  Thus the exact newly added set is
      [3,min((p-5)/2,ceil((p+8)/4)-1)]_Z union {(p-5)/2},   k=p-2+2kappa.
  The isolated top cell lies one above SEG-num's upper bound.  If it is also in the low interval, it is counted once.
Examples (arithmetic of hypotheses, not a finite search): p=11: delta1,kappa=2,3 and delta2,kappa=3; p=13:
delta1,kappa=2,3,4 and delta2,kappa=3,4.  All these lie outside BOTH I.14 bands.  To restrict to RES_< additionally retain
B<kappa and genuine empty/pure-run conditions; the theorem itself is broader and requires none of those extra hypotheses.

## 5. Requested review output and boundaries

Return verdicts on: changed fixed window/integer lift; zero/marked counts; SIGN-2Z (all four cases); RP-2NE and its exact
added-cell arithmetic.  Take accepted CONNECT/LIGHT and W/2.1/P0 only at the literal scopes in Sec.2, but check every changed
parameter inequality.  Explicitly distinguish a counterexample to an auxiliary SIGN assertion from an actual avoider.
No review or theorem beyond the frozen full candidate is requested.  Unrestricted REFL/INV*/Olson remain OPEN.
