# Theorem SEED-G* (relaxed seed bounds (QS*)) and Corollary X* (computer-assisted class level)

Version r2, written 2026-10-17T23:35:28-0700 in c6/ (task OlsonRunCount5, cycle 6): new immutable revision of r1 (c6/proof-SEEDGstar-r1.md,
sha256 8d4c844979d435b4...250806, kept unchanged) after the delegated parent delta check institute/runs/six-lane-2026-10-16/review/olson-repair-delta-v1/delta-check-v2.md
(r1: DELTA-ACCEPT-WITH-NOTES; Codex delta DELTA-ACCEPT-WITH-NOTES with MINOR-1..3; advisory, the parent decides).  Wording and
provenance only (its residual notes R1, R2, R3, R4, R7, R8); no statement, proof step, hypothesis, label or finite count changed:
(R1) Sec. 1's continuous-gap sentence now separates d>0, d=0, d<0 (the old 'far side (E-|d|+4)/2' was wrong at d=0, where both
gaps are (E+3)/2); (R2) the status line no longer calls the historical checker seedXstar2.py 'exact integer arithmetic';
(R3) the CPU/file-size limits are attributed to the hashed driver review_revision_runs.py (lines 9-11), not to its JSON;
(R4) the per-class receipt identifying the two passing OPEN0 classes as RA2 is cited; (R7) the stray ';' after (P2) is removed;
(R8) the MODE 2 range reads 11 <= p <= 23.  The r2 changes are not independently re-reviewed.

Version r1, written 2026-10-17T20:23:31-0700; immutable revision after Codex and Claude static reviews
(institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-star-{codex,claude}-review-v1.note.md: both ACCEPT-WITH-FIXES).
The r0 bytes (SHA 476e9a28...f5b22) remain unchanged.  Repairs: correct minimum-over-term-sums argument; complete exact LF closed
forms and integer relaxation; well-formed actual-empty alternative; remove redundant PIN; extend QQ to the conservative tested
weight-pair domain; precise historical finite scope, labels and evidence wording.  New seedXstar3.py uses doubled integers,
source hashes, per-class diagnostics and tightened-QS* MODE3.  Old receipt bytes are not retroactively assigned new hashes.
The r1 repairs themselves are not yet independently re-reviewed.  Original r0 provenance follows.

Version r0, written 2026-10-17T18:16:46-0700 in c6/ (task OlsonRunCount5, cycle 6; parent direction 2026-10-17 17:5x: prioritise a written (QS*)).
Status: Lemma LF, Lemma SCW-G*, Lemma QQ and Theorem SEED-G* are [W] written proofs (r0 reviewed with fixes; r1 repairs not yet re-reviewed).  Corollary X* is [W+F]: a written
implication whose hypotheses are verified class by class by the historical checker c6/seedXstar2.py, i.e. computer-assisted (it uses
float division by 2 and math.ceil: exact on its historical range 11<=p<=31, where every value is a small, exactly represented
half-integer, but not an arbitrary-p certificate; the repaired c6/seedXstar3.py uses doubled integers, Sec. 4).
Depends on c6/proof-SEEDG-r2.md (sha256 353b0e95...30b7): setting, notation (Delta0, lam, lamc, U, (QS), seeds), Lemmas P0, TS, NW, GS,
SL, the displayed term-sum bounds in the proof of Lemma SCW-G, Lemma C0+, Lemma CF; and, for Corollary X* only, on
c6/proof-SEEDG-cls-r1.md (Lemmas PR, CF', Corollary X; unreviewed).  Paths relative to mixdef-high/.  NOT a proof of NMH(p),
MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV* or ordered Olson.

## 1. The relaxed bounds

For an integer d with -min(B, E + 1) <= d <= E + 1 put mn := min(d, 0), mx := max(d, 0) and
  L_A(d) := min{ Delta0 + E + 2, Delta0 + E/2 + 1 - mn, (Delta0 + E)/2 + 2, Delta0 + E/2 - mn, Delta0 + E - d + 1,
                 (Delta0 + E - d - mn + 3)/2, (Delta0 + E + 3)/2 - d + mx/2, (R - d)/2 + 1 },
  L_B(d) := min{ Delta0 + E + 2, Delta0 + E/2 + mx, (Delta0 + E)/2 + 2, Delta0 + E/2 + mx + 1, Delta0 + E + d + 1,
                 (Delta0 + E + mx + d + 3)/2, (Delta0 + E + 3)/2 + d - mn/2, (R + d)/2 + 1 }.
These are exactly the lower bounds displayed in the proof of Lemma SCW-G (proof-SEEDG-r2.md Sec. 2, case s >= 3) for the nine (A^s)
term sums U_i + T_j, resp. the nine (B^s) term sums V_i + S_j (U1 + T3 and U3 + T1 share the bound (Delta0 + E)/2 + 2, as do V1 + S3,
V3 + S1).  Their derivation uses (2.1), (F1), (0.1'), 1<=m'<=m<=m'+1, m'>=1 and floor(a/2)>=(a-1)/2; it does not require (QS).
The run-weight domain (0.2') enters the later comparison with the targets and the simplification below.
**Lemma LF (exact closed forms).**  Throughout the stated run-weight domain,
  L_A(d)=(Delta0+E+3-max(d,-1))/2,  L_B(d)=(Delta0+E+3+min(d,1))/2=L_A(-d).
In particular d=u>=1 gives ((Delta0+E-u+3)/2,(Delta0+E)/2+2); d=0 gives both (Delta0+E+3)/2; d=-u<=-1 exchanges the positive pair.
Proof.  Put D=Delta0, u>=1, C=(D+E-u+3)/2 and T=(D+E)/2+2.  In the eight-expression order of the definitions, the DOUBLED
entrywise differences from C for L_A(u), and from T for L_B(u), are respectively
 [D+E+u+1, D+u-1, u+1, D+u-3, D+E-u-1, 0, 0, 2kappa-1],
 [D+E, D+2u-4, 0, D+2u-2, D+E+2u-2, 2u-1, 2u-1, 2kappa+u-2].
Every entry is nonnegative because D>=3,E>=0,u<=E+1,kappa>=2; a zero entry shows equality with the proposed minimum.  At d=0,
twice the L_A entry differences from (D+E+3)/2 are
 [D+E+1,D-1,1,D-3,D+E-1,0,0,2kappa-1];
L_B's vector exchanges entries 2 and4.  Negative d follows by exchanging the A/B collections and entries 2 and4, since their
multisets are reflected under d->-d.  This proves all signs including zero and both endpoints.  The discarded extra linear term
of r0's two-term minimum exceeds the attained term by (D+E-u-1)/2>0, so it never attains on the domain.  []

The continuous gaps from the original QS targets are: for d>0, (E+3)/2 on the lower (A) side and (E-d+4)/2 on the upper (B) side;
for d=0, (E+3)/2 on both sides; for d<0, (E-|d|+4)/2 on the lower side and (E+3)/2 on the upper side.  All are >=3/2, as |d|<=E+1.
More precisely the EXACT integer relaxation before canonical clipping or P2 is as follows.  Put h=E/2, epsilon=D mod2,
J(u)=h+2-floor((u-epsilon)/2).  Relative to the integer QS lower/upper endpoints, QS* permits the decrease/increase
  d>0: (h+2,J(d));  d=0: (h+2,h+2);  d<0: (J(-d),h+2).
These follow by substituting the closed forms into 1-ceil(L_A),ceil(L_B)-1 and the QS integer endpoints
ceil((d-D)/2)+1,floor((d+D)/2)-1.  Since |d|<=E+1, J(|d|)>=2; every side gains at least TWO integer units.  These window gains do
not establish that a word has seeds, and do not remove P2.  Implementation must use integer doubled expressions, not floating
rounding at unrestricted p.

## 2. Seeded certification with (QS*)

**Lemma SCW-G*.**  Let w be an NMH word with R <= 2p - 3 that avoids, x its canonical lifts, and let every run t have a seed [a_t, b_t]
(Definition in proof-SEEDG-r2.md Sec. 1) such that
  (QS*)  1 - a_t <= ceil(L_A(d_t))  and  b_t + 1 <= ceil(L_B(d_t));
  (P2)   for every two distinct runs s, t, with m_st := 1 if s, t are adjacent and 2 otherwise:
         a_s + a_t >= 1 - lamc(d_s + d_t, m_st)  and  b_s + b_t <= p + lam(d_s + d_t, m_st) - 1.
Then every proper pattern is certified (Lemma SL with these ranges), and X_[k]=p.  The old explicit (PIN) premise is automatic:
b_a<=U({a})=p-lambda({a}^c) and P0 give b_a-lambda({a})<=p-1 for EVERY run.  Existing checks of PIN are conservative, not required.
Proof.  Induct on s=|Q|>=2 as in Lemma SCW-G.  For s>=3 the (A^s) sum equals
 min_i U_i + min_j T_j = min_(i,j)(U_i+T_j) >= min_(i,j) B_ij = L_A(d),
where each individual term sum U_i+T_j is at least ITS displayed lower bound B_ij.  The sum is an integer, hence >=ceil(L_A(d))
>=1-a_t.  The (B^s) sum is handled by the identical minimum argument for L_B(d), giving >=b_t+1.  This does NOT claim that the sum
is at least each of the nine individual bounds.  For s=2 the two extension inequalities are exactly P2.
Pin with ANY run a: {a}^c is certified, and X_[k] lies in [a_a+lambda({a}^c),b_a+p-lambda({a})].  The lower end is at least
lambda({a})+lambda({a}^c)>=1.  The upper end is at most 2p-lambda({a})-lambda({a}^c)<=2p-1, using b_a<=U({a}) and P0.  Since
X_[k]=0 mod p, X_[k]=p.  []

**Lemma QQ (including the conservative arithmetic pair domain).**  QS implies QS*.  Suppose d1,d2 are any weights in
[-min(B,E+1),E+1], with e(d1)+e(d2)<=E (e(d)=|d|-1 for d!=0,e(0)=1), and their nonempty seed ranges satisfy QS and
lambda(d_i,1)<=a_i<=b_i<=U(d_i,1).  Then P2 holds at BOTH m=1 and2, even if these two formal weights cannot occur together in one
word.  In particular quality seeds on every actual run imply P2.
Proof.  The first assertion follows from L_A(d)>=(Delta0-d)/2,L_B(d)>=(Delta0+d)/2.  For the second repeat the two-run proof of
SCW-G with y=d1+d2.  The budget gives y<=E+2, and the formal range gives y>=-2min(B,E+1)>=-2B.  The original uses of y>=-B need
only y>=-2B-E-4, y>=-2kappa-E, y>-2B-2E-7, and d_i>=-B, respectively in its B-side, first A-side, canonical/seed fallback, and
heavy-singleton branch.  All four weaker inequalities hold here.  Thus the same seed/canonical case split gives both P2
inequalities for m=1,2.  The canonical lower endpoint remains essential in that fallback.  Automatic PIN was proved above.  []

**Theorem SEED-G*.**  Let w be an NMH word with R<=2p-3, p>=5 prime, satisfying (i) or (ii+) of C0+.  Suppose EITHER some actual
run t has configuration-derived GS(a) seeds with empty intersection, OR every run has a nonempty seed [a_t,b_t] satisfying QS* and
these seeds satisfy P2.  Then w has an identity 2p-subword.  This contains SEED-G by QQ.
Proof.  The actual-empty alternative excludes w immediately.  Otherwise, if w avoids, SCW-G* and SL give all proper-pattern lower
bounds, the canonical lifts give the singletons, and sum x=p; C0+ gives a contradiction.  No undefined endpoint is used before the
empty case is discharged.  []

## 3. Corollary X* [W+F] (class level, exact seeds)

In the notation of c6/proof-SEEDG-cls-r1.md Sec. 3 (allowed profiles pi, exact seeds sigma_pi(d) from the families S1, P1, SA, PA by
Lemma GS (a)), call a weight d of pi live if sigma_pi(d) is nonempty, and let e(d) be the excess of a run of weight d.
**Corollary X*.**  Suppose that for every allowed profile pi of a parameter class either one of the weights a*, -b* (if b* >= 1),
0 (if n_pr >= 1) has sigma_pi empty, or: every live weight satisfies (QS*); every two live weights d1, d2 (equal or not) with
e(d1) + e(d2) <= E satisfy a1 + a2 >= 1 - lamc(d1 + d2, m) and b1 + b2 <= p + lam(d1 + d2, m) - 1 for m = 1 and m = 2
([a_i,b_i]:=sigma_pi(d_i)).  If moreover C+'s class sufficient condition holds, no word of the class avoids.  PIN is automatic
because each sigma_pi is canonically contained; it is not a hypothesis of X*.
Proof.  As for Corollary X (c6/proof-SEEDG-cls-r1.md): for a word w with profile pi and a run t of weight d, sigma_pi(d) contains a seed of t
(Lemmas PR, CF, CF', GS (a)); a run whose weight has empty sigma_pi excludes w; otherwise every run has a seed inside sigma_pi(d_t),
so QS* holds and P2 holds for every two distinct runs (their excesses add up to at most E and their block count is 1 or2).
Theorem SEED-G* applies (C+'s class condition gives (i) or (ii+) for every word).  []
Coverage [F] (c6/seedXstar2.py MODE 0, out/seedXstar2_mode0.txt; every item-(iii) class, primes 11..31; OPENE classes of the c6 map):
    p | OPENE | SA/PA |  X   |  X*  | X*,noC+ | fail || OPEN0 | X*
   11 |    24 |    15 |    7 |    2 |     0 |   0 ||   0 |   0
   13 |    47 |    27 |   14 |    5 |     1 |   0 ||   0 |   0
   17 |   137 |    84 |   39 |    5 |     9 |   0 ||   0 |   0
   19 |   210 |   125 |   61 |    7 |    17 |   0 ||   0 |   0
   23 |   438 |   257 |  114 |   21 |    46 |   0 ||   1 |   0
   29 |  1001 |   572 |  232 |   64 |   133 |   0 ||   4 |   1
   31 |  1257 |   713 |  289 |   83 |   171 |   1 ||   7 |   1
(SA/PA = written regions of proof-SEEDG-r2.md; X = additionally by Corollary X; X* = additionally by Corollary X*; X*,noC+ = the
seed/certification hypotheses of X* hold but C+'s class SUFFICIENT condition fails.  OPEN0's X* column counts ALL passing classes,
not additional exclusions.)  Historical totals for 11<=p<=31: of 3,114 OPENE classes, 1,793 (SA/PA, written) + 756 (X, [W+F]) +
187 (X*, [W+F]) are excluded; for 377 more the seed part holds but C+'s class condition fails; 1 class (p = 31) fails the
seed part.  OPEN0 has no additional exclusion: its two passing entries are the RA classes of base r2 Sec.6, one at p=29 and one
at p=31; the aggregated receipt alone does not identify their RA subtype.  The new per-class receipt out/revision_star3mode0.txt
(LF 4413, 7247; repaired checker, whose per-label counts reproduce the historical ones) lists them as (p;k,kappa,B)=(29;55,26,2) and
(31;59,28,2): B=2, kB=p-5, i.e. RA2 (proof-SEEDG-r2.md Sec. 5).
[F, historical 11<=p<=31] Among the 378 OPENE classes remaining in this test, 377 pass the class seed/certification tests but fail
C+'s CLASS SUFFICIENT condition; one further class fails the seed test.  This is not a proof that C+'s per-word (i)/(ii+) fail in
all words of those 377 classes, nor that counting is the only general obstacle.  Later construction/finisher files are separate.
Controls: MODE1 (QS in place of QS*, historical 11<=p<=23) reproduces seedX2.py MODE0's PER-LABEL COUNTS (out/seedXstar2_mode1.txt).
QQ supplies the class-wise nesting for the tested conservative pair domain; the old receipts themselves only aggregate counts; MODE 2 (every exact seed widened by one, 11 <= p <= 23) changes only IS/IE classes (p = 19: 1, p = 23: 9 more
failures) and no OPENE class -- (QS*) has slack there, so MODE 2 is not a sensitivity control for OPENE.
The superseded seedXstar.py tested PIN at some live weight; the automatic-PIN lemma explains why this did not change the real-mode counts.  No unsoundness of that vacuous real-mode test is claimed.

## 4. Review-repair implementation and provenance

seedXstar3.py replaces floating division by eight doubled INTEGER expressions and exact ceil(n/2)=(n+1)//2.  The compact LF form
provides a second exact formula for its unit controls; the review's legal p=2^61-1 case is tested on the REPAIRED implementation
only.  The old floating implementation is exact on the historical finite receipt range, but is not an arbitrary-p certificate.
Real modes0/1/3 omit PIN; the widened mutation MODE2 retains a pin diagnostic because its expanded ranges need not be seeds.
MODE3 tightens QS* by one on each side.  Per-class detail records identify the first failed profile, weight or P2 pair and block
count.  Headers hash every exec'ed source (including map6/c4 label dependencies); this does NOT retroactively establish hashes
for old receipts.  The old map-label partition relied on dependencies absent from the review bundle, whereas the X/X* endpoint
criteria did not.  New receipts and their exact outcomes are recorded in the appended repair receipt section.

## 5. New immutable repair receipts (all finite instantiations, not universal numerical coverage)

The run driver is review_revision_runs.py (sha256 997131d6d7a1f4b5...ef78f7 in out/freeze.txt); its source sets the native limits
(lines 9-11: RLIMIT_CPU (1800,1860) s, RLIMIT_FSIZE 128 MiB).  out/review_revision_runs.json records date-based starts/ends and
four completed exit-0 jobs, one scientific child at a time; it has no limit fields.  Its observed peak child RSS is 23,035,904 bytes.  Headers in
out/revision_X3p23.txt and out/revision_star3mode0/mode1/mode3.txt bind the exact revised scripts and every exec'ed map/c4 source.
These are new runs; old receipts are untouched.

* X3 MODE0, 11<=p<=23 and star3 MODE0, 11<=p<=31 reproduce the historical PER-LABEL counts exactly.  Separately, the new per-class
  records compare star3 MODE1 against X3 MODE0 on all 2,154 class IDs at 11<=p<=23: no mismatch.  Thus this NEW evidence really is
  class-wise; the old aggregated receipts were not described that way.
* The real MODE0 report has 70 classes whose FIRST failing stage is QS*.  It does not say their unexecuted later P2 tests would
  pass.  The single OPENE failure at p=31 is (k,kappa,B)=(51,24,23), profile (n1,n_al,a*,b*,pairs)=(26,28,8,1,false), weight8:
  actual computed seed range [8,8], required QS* range [-2,7].  This is a sufficient-criterion failure, not an avoider or group
  counterexample.
* Requested one-unit tightening (MODE3,11<=p<=31) gives 151 first-stage QS* failures: 46 IS and 34 IE formerly passing classes plus
  one OPENE seed-pass/no-C+ class are lost.  No accepted OPENE exclusion changes.  The separately declared two-unit control
  (star3_tight2.py,11<=p<=23) likewise changes no accepted OPENE exclusion (16 IE and34 IS passes are lost).  We do NOT call those
  sensitive OPENE-exclusion controls.  A declared FOUR-unit endpoint ablation (star3_tightN.py SHIFT4,11<=p<=23) loses630 accepted
  OPENE classes; other labels also change as recorded in out/review_repair_summary.json.  These mutations are negative tests,
  not valid alternative theorem modes or measurements of mathematical necessity.
* Nonvacuous P2 control: out/star3_p2_negative_fixture.json supplies deliberately UNCERTIFIED boxes at the legal arithmetic class
  (11;15,6,1).  They satisfy QS*/canonical containment but not P2.  The real class_report rejects at pair(-1,-1),m=2, sum range
  [-10,2] against required[-9,5].  An in-memory mutant bypassing ONLY the P2 comparison accepts.  This detects a vacuous P2 gate;
  no claim is made that the injected boxes come from GS, a feasible full lifted system or an avoider.  Source/fixture hashes and
  both outcomes are in out/star3_p2_controls.txt.
* Exact-bound regression: out/star3_exact_controls.txt checks528,214 small-domain weights against the exact compact LF expression,
  the review's legal p=2^61-1 input with exact ceilings2^59+101 and2^59+102, and15 further huge-integer bounds.  Only the repaired
  integer implementation is run.  No known-broken old checker was rerun to confirm the reported defect.

All comparisons, detailed control deltas, review-note hashes and driver metadata are bound in out/review_repair_summary.json.
These producer checks do not claim new independent verification beyond the named static reviews.

