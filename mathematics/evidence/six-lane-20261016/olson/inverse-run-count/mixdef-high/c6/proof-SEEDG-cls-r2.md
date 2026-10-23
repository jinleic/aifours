# Corollary X: class-level exclusions by Theorem SEED-G with exact seeds (computer-assisted), and the run-length profile lemma

Version r2, written 2026-10-17T23:35:28-0700 in c6/ (task OlsonRunCount5, cycle 6): new immutable revision of r1 (c6/proof-SEEDG-cls-r1.md,
sha256 30c442668d5154c0...8eff61, kept unchanged) after the delegated parent delta check institute/runs/six-lane-2026-10-16/review/olson-repair-delta-v1/delta-check-v2.md
(r1: DELTA-ACCEPT-WITH-NOTES; Codex delta DELTA-ACCEPT-WITH-NOTES; advisory, the parent decides).  Wording and provenance only (its
residual notes R3, R4, R6, R8); no statement, proof step, hypothesis, label or finite count changed: (R3) the CPU/file-size limits
are attributed to the hashed driver review_revision_runs.py, not to its JSON; (R4) the per-class receipt identifying the passing
OPEN0 classes as RA2 is cited, with the inference to Corollary X marked [I]; (R6) the base-r2 citation has its missing space and
its review status; (R8) the control ranges read 11<=p<=31 and 11<=p<=23.  The r2 changes are not independently re-reviewed.

Version r1, written 2026-10-17T20:23:31-0700, after both static star/cls reviews (ACCEPT-WITH-FIXES).  r0 (SHA5a5038e4...02ba) stays unchanged.
Repairs: base r2 citations; wrap/properness/count wording; EXACT arithmetic allowed-profile filters matching profiles(); dated
computer-assisted scope and conservative control wording.  Necessary-condition profiles may be unrealizable (extra obligations
are conservative).  New seedX3.py adds provenance hashes without changing the endpoint/profile arithmetic.  Repairs not re-reviewed.
Original r0 provenance: written 2026-10-17T17:45:10-0700 in c6/ (task OlsonRunCount5, cycle 6).
Status: Lemmas PR and CF' are [W] written proofs (r0 reviewed with fixes; r1 not re-reviewed); Corollary X is [W+F]: a written implication whose hypothesis is
verified class by class by exact integer arithmetic (c6/seedX2.py), i.e. computer-assisted, like the class-level use of Theorem
IND*.  Depends on c6/proof-SEEDG-r2.md (sha256 353b0e95...30b7; r1 reviewed ACCEPT-WITH-FIXES,
the r1->r2 delta rated DELTA-ACCEPT-WITH-NOTES by the parent's SeedGReviewDesk): Theorem SEED-G, Lemmas GS, CF, the notation
(Delta0, (QS), lam, lamc, U).  Paths relative to mixdef-high/.  NOT a proof of NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV*
or ordered Olson.

## 1. Run-length profiles

**Lemma PR.**  Let w be an NMH word with R <= 2p - 3 (parameters k, kappa, B, E = R - k).  Let n_al, n_an, n_pr be its numbers of
aligned runs, anti runs and (1,1)-pairs, e_al := sum_aligned (a_t - 1), e_an := sum_anti (b_t - 1), n1 the number of aligned runs of
length 1, a* the largest aligned length and b* the largest anti length (b* := 0 if n_an = 0).  Then E = e_al + e_an + n_pr,
n_al = k - B + e_an, e_an >= (b* - 1)^+, and
   n1 >= k - B - E + 2(b* - 1)^+ + n_pr + a* - 2  if a* >= 2,      n1 = n_al  if a* = 1.
Every run weight of w lies in {1, ..., a*} u {-b*, ..., -1} u ({0} if n_pr >= 1), and w contains runs of weight a*, -b* (if b* >= 1)
and 0 (if n_pr >= 1).
Proof.  E = sum_t (r_t - 1) splits as stated (a pair has two letters).  B = sum_anti b_t + n_pr = n_an + e_an + n_pr and
k = n_al + n_an + n_pr give n_al = k - B + e_an.  If a* >= 2, the j := n_al - n1 aligned runs of length >= 2 carry e_al >= (a* - 1) +
(j - 1) excess letters, so n1 = n_al - j >= n_al - e_al + a* - 2 = (k - B + e_an) - (E - e_an - n_pr) + a* - 2; finally e_an >= (b* - 1)^+.  []

## 2. Single-letter configurations

**Lemma CF'.**  In the setting of Lemma CF of c6/proof-SEEDG-r2.md (t a run; t and its two neighbours deleted, a path of k - 3 runs
remains), with n1 the number of aligned runs of length 1:
 (S1) if 1 <= m <= ceil((n1 - 3)/2), there are m pairwise non-adjacent aligned runs of length 1, none adjacent to t; type (y, m) = (m, m);
 (P1) if 1 <= m <= ceil((2 n1 - k - 4)/3), there are m pairwise non-adjacent blocks of two adjacent aligned runs of length 1, none
      adjacent to t; type (2m, m).
In both cases Q has m blocks and Q+t has m+1 blocks.  Both are proper: t and its neighbours are omitted from Q, and t's neighbours
remain outside Q+t.  Thus the actual block count also gives 2m+2<=k.
Proof.  The path contains >= n1 - 3 aligned runs of length 1 and at most (k - 3) - (n1 - 3) = k - n1 other runs, so these runs lie in at
most k - n1 + 1 maximal intervals of consecutive length-1 aligned runs, of lengths L_i with sum L_i >= n1 - 3.  Every other run of an
interval gives ceil(L_i/2)>=L_i/2 pairwise non-adjacent runs, at least sum ceil(L_i/2)>=(n1-3)/2 in total; the blocks {l, l + 1}, {l + 3, l + 4}, ... give floor((L_i + 1)/3) >=
(L_i - 1)/3 blocks, in total >= (n1 - 3 - (k - n1 + 1))/3 = (2 n1 - k - 4)/3.  Members of different intervals are separated by a run of
the path; its ends t+2,t-2 have cyclic distance min(4,k-4)>=2 because k>=2kappa+3>=7, and no member is adjacent to t.  []

## 3. Corollary X

For an item-(iii) parameter class, call pi=(a*,b*,n_pr) ARITHMETICALLY ALLOWED iff all these necessary conditions hold:
 - 1<=a*<=E+1, 0<=b*<=min(B,E+1), 0<=n_pr<=min(B,E);
 - b*=0 implies n_pr=B; b*>=1 implies n_pr+b*<=B;
 - if a*>=2: (a*-1)+(b*-1)^++n_pr<=E, and set e_an=(b*-1)^+;
 - if a*=1: set e_an=E-n_pr, require e_an=0 when b*<=1, require e_an>=b*-1, and require n_pr+e_an+1<=B when b*>=1.
The triple of every ACTUAL word passes these filters (PR).  Some passing triples can still be unrealizable; their inclusion only
adds conservative obligations.  Put n_al(pi)=k-B+e_an.  If a*>=2 put n1(pi)=k-B-E+2e_an+n_pr+a*-2; if a*=1 put n1(pi)=n_al(pi).
These use the least anti excess consistent with the filters for a*>=2 and the forced anti excess for a*=1, giving valid lower
bounds for every actual word of that triple.
For a weight d of pi let e_d be the excess of a run of
weight d (d - 1, -d - 1 or 1 for aligned, anti, pair) and define the exact seed
   sigma_pi(d) := [lambda({t}), U({t})]  intersected with  the hulls  [min_y s_lo, max_y s_hi]  over the families
   S1 (y = m, m <= ceil((n1(pi) - 3)/2)), P1 (y = 2m, m <= ceil((2 n1(pi) - k - 4)/3)), SA (m <= y <= m + E - e_d,
   m <= ceil((n_al(pi) - 3)/2)), PA (2m <= y <= 2m + E - e_d, m <= ceil((n_al(pi) - B - 4)/3)) and all admissible m (2m + 2 <= k),
where s_lo = lam(y + d, m + 1) - U(y, m), s_hi = U(y + d, m + 1) - lam(y, m), and a family/m term is used only if the no-wrap condition
of Lemma GS (a) holds for every y of its range.
**Corollary X** [W+F].  Suppose that for every allowed pi (i) every weight d of pi has sigma_pi(d) empty or satisfying (QS), or (ii) one of
the weights a*, -b* (if b* >= 1), 0 (if n_pr >= 1) has sigma_pi empty; and that C+'s class condition (E <= 4, or 2kB <= p and
E <= 2(k - kB - 2B) - 1) holds.  Then no word of the class avoids.
Proof.  Let w be a word of the class, pi its triple (allowed by Lemma PR) and t a run of w of weight d.  w has at least n1(pi) aligned
runs of length 1 and at least n_al(pi) aligned runs (Lemma PR; n1 and n_al grow with e_an), so every family/m term used in
sigma_pi(d) is realised at t (Lemma CF of c6/proof-SEEDG-r2.md and Lemma CF'), with D_Q in the stated range; by Lemma GS (a) each term
is a seed for t and so is the intersection, which therefore contains a seed for t inside sigma_pi(d) (more available configurations
only shrink it).  If w avoids, x_t lies in this set; so an empty sigma_pi(d) for a weight occurring in w is a contradiction (in case
(ii) such a weight occurs), and in case (i) every run of w has a quality seed or w is already excluded; Theorem SEED-G (with C+'s class
condition, which implies (i) or (ii+) of its Lemma C0+ for every word of the class) gives the claim.  []

## 4. Coverage [F] (c6/seedX2.py MODE 0, out/seedX2_mode0.txt; every item-(iii) class, primes 11..31)

Columns: OPENE classes of the c6 map; already excluded by the written Corollaries SA/PA of proof-SEEDG-r2.md; ADDITIONALLY excluded by
Corollary X [W+F]; X holds but C+'s class condition fails; neither | OPEN0 classes, excluded (RA2/RA3 or X), not excluded.
    p | OPENE | SA/PA |   X   | X,noC+ | rest  || OPEN0 | excl | rest
   11 |    24 |    15 |     7 |    0 |     2 ||   0 |   0 |   0
   13 |    47 |    27 |    14 |    1 |     5 ||   0 |   0 |   0
   17 |   137 |    84 |    39 |    9 |     5 ||   0 |   0 |   0
   19 |   210 |   125 |    61 |   13 |    11 ||   0 |   0 |   0
   23 |   438 |   257 |   114 |   26 |    41 ||   1 |   0 |   1
   29 |  1001 |   572 |   232 |   71 |   126 ||   4 |   1 |   3
   31 |  1257 |   713 |   289 |   87 |   168 ||   7 |   1 |   6
Totals 11<=p<=31: OPENE 3,114 classes: 1,793 by SA/PA (written), 756 more by Corollary X [W+F], 207 with X but
not C+'s class sufficient condition, 358 neither.  Corollary X adds nothing to OPEN0 in this historical 11<=p<=31 range: the
aggregated receipt records the RA class of base r2 Sec.6 at p=29 and31, without identifying its RA subtype from counts alone.  The new
per-class X* receipt out/revision_star3mode0.txt (LF 4413, 7247) lists the only passing OPEN0 classes at p=29, 31 as (29;55,26,2)
and (31;59,28,2): B=2, kB=p-5, i.e. RA2 (proof-SEEDG-r2.md Sec. 5).  [I] A class passing X also passes X* (QQ nesting,
proof-SEEDGstar-r1.md Sec. 2) and each of these primes has exactly one passing OPEN0 class in both tables, so the X-passing classes
are these RA2 classes; no per-class X receipt exists at p=29, 31.  The same run also re-excludes many IE/IS classes (previously IND* [W+F]); every class excluded by the written
regions passes Corollary X as well (consistency).
Controls (out/seedX2_mode1.txt, out/seedX2_mode2.txt), 11<=p<=23: MODE 1 ((QS) tightened by one on both sides): of the 2,154 classes
only 190 pass (+6 without C+'s condition), against 1,887 (+93) in MODE 0; among the OPENE classes 3 (+6) against 743 (+49), and every
OPENE class of the written regions fails under this stricter endpoint test.  No universal endpoint-attainment claim is inferred
from that aggregate control.  MODE 2 (families SA, PA removed): 1,358
classes pass (OPENE: 355) against 1,887 (743) in MODE 0.
Superseded (never cited): c6/seedX.py and out/seedX_mode0..2.txt -- its profile test accepted an empty seed of ANY weight of the
profile, also of weights that a word need not contain; seedX2.py accepts empty seeds only for a*, -b*, 0 (case (ii)).

## 5. Review-repair provenance

The frozen seedX2.py profile/seed arithmetic is unchanged in seedX3.py; it now cites base r2, describes E=0 processing explicitly,
and prints all exec-source hashes in new receipt headers.  The old receipt metadata did not pin those dependencies; no retrospective
hash claim is made.  Newly run controls and per-class records are listed below after execution.  The historical data remain [W+F]
instantiations at primes11..31, not universal numerical coverage.

## 6. New repair receipt

seedX3.py MODE0 at11<=p<=23 (out/revision_X3p23.txt) now prints every exec-source hash and every class ID.  Its per-label counts
are identical to the historical seedX2.py receipt.  Compared with the new star3 MODE1 per-class records, all2,154 class verdicts
agree (out/review_repair_summary.json).  The old p=29/31 evidence remains the old [W+F] receipt; its source hashes are not
retroactively inferred from these new runs.  No profile/seed arithmetic changed in X3.  Native CPU/file-size limits are set by the
hashed driver review_revision_runs.py (lines 9-11); its JSON out/review_revision_runs.json records the date-based run metadata but
has no limit fields.  The other review-repair controls are documented in proof-SEEDGstar-r1.md.

