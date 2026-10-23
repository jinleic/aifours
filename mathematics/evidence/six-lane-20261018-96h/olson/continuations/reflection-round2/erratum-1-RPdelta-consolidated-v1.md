# RPdelta consolidated erratum 1: all five Codex MINOR findings

OlsonReflectionSuccessor.  Frozen after /bin/date observation 2026-10-19T08:53:31-0700.  Written correction only; no
computation, model call or review launch.  All original source files and the first RPdelta snapshots remain unchanged.
Source of findings: RUN/review/olson-RPdelta-codex-v1.prompt.stdout.txt,
e11c4dcb4d57f9e665e892c40955c695c0b48ab605853171d21d47fe75b1759d: 0 FATAL / 0 MAJOR / 5 MINOR, conditional
ACCEPT-WITH-FIXES for all four candidate groups.  The first Claude RPdelta attempt returned NO_VERDICT (rc1, provider
session-capacity), not mathematical rejection or acceptance.  Parent controls any rescope/review after retry eligibility;
no second-family acceptance is claimed here.  RUN/ = institute/runs/six-lane-2026-10-18-96h/.

## 0. Governing sources and precedence

Read this ONE overlay with the following exact files (no changes to theorem ranges):
K = proof-REFLHI-arcs-v5-addendum-SEGk-v2.md,
b6d526829c9065eeefe75e8cbf7c12c31c88950f9de8788729a55144810a70d5;
K-e = its erratum-1, 7030b7583a47f777a52f5d352795c4e1a1a200c879625ce6fce52b3ecc82a8e3;
T = proof-REFLHI-transfer-v2.md, dc1974c8e8c8229002dd02e6bb4ef1e97cd123f7d411479bcd7d8cc9b58729fa;
B = proof-REFLHI-regionB-v2.md, 35948d69955ab44faa6464741a2190c97d528218334101b8fc02674422640af3;
B-e1 = its erratum-1, 94a018c5dbf63112157c6f6c6564887a24e934a1ce68eb7102c14b4c1f0543e3;
B-e2 = its erratum-2, f6fc960f3dc49ac1464ae24f792937fa772e268c23f0a7b77574de4eaee46d56;
BP = proof-REFLHI-regionB-v2-addendum-Bprime-v1.md,
4a5b00570d72b8b812129944cf980dd10752d97ed127130517d3429b1317dcc5;
BP-e = its erratum-1, fa4c249e1dff1ee8a887aa0c29dafc547cf730bde0fffa7d71e84202ce626943.
All are in this reflection-round2 directory.  This erratum takes precedence over overlapping wording in those texts and
in review-package-RPdelta-v1.md; otherwise their earlier errata stay in force.  Accepted imports are governed by parent
verdict13ee1ba86245fc549bd79c130a9fe15248ecc3fe9fc8428e875ca939c940a547, with all bindings and full-scope Theorem SEG.
RP-LIFT and RP-2NE are independent; neither is used or given a verdict by this packet.

## E1. MINOR 1: historical 'remaining' descriptions are not exhaustive

K38-41 and T69-72 list only selected types of remaining parameters; they are NOT an exhaustive ledger.  Replace any
exhaustive reading by the following exact set-complement description, for delta>=1 (comparison to the stated numerical
tests, not a realizability claim):
   J(p,delta)=[max(2,ceil((delta+1)/2)),p-1]_Z,
   A(p,delta)=[ceil((p+3delta+2)/4),floor((p-delta-4)/2)]_Z
              union [ceil((p+delta+1)/2),p-delta-3]_Z.
An integer interval is empty if lower>upper.  J records kappa>=2, H>=0 and k=p-delta+2kappa>=p+1; actual residual-word
conditions remain necessary.  E(p,delta) consists of the single point (p+3delta+1)/4 exactly when
   delta>=2 even, p+3delta=3 mod4, p>=5delta+11,
and is empty otherwise (the SEG-k parity endpoint, K's contribution outside A).  Put
   M_BP(p,eps)=min(floor((p-12+4eps)/3),floor((2p-32+2eps)/3)),
   N(p,delta)={(p-1)/2-eps : eps in {0,1}, 1<=delta<=M_BP(p,eps)}.
Then the remaining numerical values under I.14+SEG-k+B/B-prime are exactly
   J(p,delta) minus [A(p,delta) union E(p,delta) union N(p,delta)].
Within this complement accepted raw structural SEG, B=0 CJ/EDGE and B.4 may exclude/restrict particular words; they are
not additional universal parameter bands without a further argument.  TRANSFER adds no independent terminal band.
This supersedes any suggestion in K/T or their package that only the three historical example regions remain.
The Codex example p=3 mod4, p>=19, delta=1, kappa=(p+1)/4, k=(3p-1)/2, B=1 illustrates an omitted parameter cell; it is
NOT an asserted avoider or a counterexample to any theorem.

## E2. MINOR 2: empty-box qualifier in T54-55

Replace T54-55's parenthetical by: an empty box already gives TRANSFER's conclusion, because a violating word would
produce a terminal cell in it.  WHEN THE BOX IS NONEMPTY, no cell has R>=p iff D0+2B0<p.  Thus only in that nonempty-box
case does failure of this trivial exclusion require B0>=(p-1)/2 and kappa0>=(p+1)/2 under T1's D0<=1 hypothesis.
In particular g0=0 is an empty box regardless of R0; no equivalence involving R0 is asserted for that case.  The proofs
of INV, TRANSFER and T1-T3 are unchanged and already handle empty boxes by contradiction.

## E3. MINOR 3: selected unsaturated segment, not every segment (B-e2:11-13)

Replace the intermediate invariant by the following.  A segment about to be incremented is UNSATURATED: its current
certified gain min(p-1,2t,b'-1) equals 2t (the final rate-1 unit of a saturated segment is never followed by another unit).
Since the certified total is still below Pi_need, for THIS SELECTED segment
   2t<=current certified total<Pi_need.
After its increment, 2(t+1)<=Pi_need+1<=(p+1)/2<=p-1.  Thus clipping at p-1 cannot interfere with any useful unit before
the target is reached.  A different segment already saturated by its final rate-1 unit need not have its gain equal to
2t, and no bound on its unneeded uncapped 2t is asserted.  W2/W1 remain capacities; rate-1 units are used after rate-2 units
are exhausted, respecting each segment's prerequisites.  No allocation bound or theorem range changes.

## E4. MINOR 4: sufficient estimates, not equivalences or necessities

(a) B31: read 'N_O<=q iff 3x<=p+3delta-7+4eps' as 'N_O<=q IS ENSURED BY 3x<=p+3delta-7+4eps', since only an upper bound
on N_O was substituted.  Its displayed sufficient delta bound is unchanged.
(b) BP17-23: 'm_lo>=1 needs ...', 'N_O<=q needs ...' and the corresponding potential/width requirements mean
'IS ENSURED BY ...' or 'IT SUFFICES THAT ...', not necessary conditions.  The proof verifies those sufficient conditions
at every parameter in Theorem B-prime's range and never invokes B.2 outside its own range without checking them anew.
(c) B81-83 and any analogous packet wording: raw accepted SEG's H1 is
   m_hi-m_lo>=Pi_need+1,
not the stronger sufficient lower-bound test H-floor(d/2)>=Pi_need+1.  When the maximum in m_lo is inactive, the exact
width is H-[floor((R+d)/4)-ceil((R-d)/4)], which may be larger than H-floor(d/2).  No claim that raw structural SEG misses
EVERY word of region B is made.  The statement that all positive-delta B/B-prime cells lie outside both I.14 UNIVERSAL
NUMERICAL bands remains correct; no disjointness from every accepted structural SEG instance is inferred.

## E5. MINOR 5: B.4 survives outside B-prime at its own range

BP37-39's phrase 'There only v2 Lemma B.1 is claimed' is replaced by: Lemma B.1 always remains available; additionally,
Corollary B.4 remains available wherever its own range 1<=delta<=(p-12)/3 holds, even outside B-prime.  In that range any
remaining avoider must satisfy |AB|<=N_O and 2x<7delta-2p+29-2eps.  This is necessary word structure, not a universal
exclusion of every cell satisfying that inequality.  Example (p,eps,delta)=(17,0,1) lies outside B-prime but B.4 still gives
|AB|<=N_O and x=0.  No remaining B.4 restriction is withdrawn merely because its cell lies outside B-prime.

## Boundary

All four theorem groups remain CANDIDATE until a parent verdict based on both families.  No theorem range is narrowed or
strengthened by these five wording/coverage repairs.  The first second-family attempt produced no mathematical verdict;
there is no paid fallback or worker launch.  Full REFL/INV*/ordered Olson and priority remain open.
