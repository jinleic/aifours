# Theorem LS+-lin (assembly): LS+(p, kappa) when p - kappa = 2, or p - kappa >= 3 and p >= 10(p - kappa) - 13; exact list of
# exceptional cells, v1

Owner OlsonSTABSuccessor.  Written after /bin/date 2026-10-19T06:45:35-0700.  Status: CANDIDATE [W], UNREVIEWED assembly.  No new mathematics
beyond the cited files; it records exactly which cells the candidate chain covers and which it does not.  Sequence level only:
no INV*, ordered-Olson, novelty, Lean or human-review claim.

## Chain (exact files; status)
- Theorem LS+2 and Lemma CT: proof-LSplus-e2-v1.md 2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1 -- candidate in the delta review (Codex reported ACCEPT
  per parent IRC; Claude and parent verdict pending): CONDITIONAL.
- Lemma CTgen: lemma-CTgen-v1.md 462d52aa1c6708a1071e06e0d88d0558b7f58e00c14bd42565655a123f92e5ad -- same status: CONDITIONAL.
- Theorem LS+-RED (A), (B): proof-LSplus-red-v1.md 166fbac828e7e55a8f2139648930c82c5df1e8823bf9d8c4f84daf36086b4c27 -- candidate, unreviewed.
- Case a = -1: proof-LSplus-red-v1-addendum-1.md 6a79deb851f27d9e3d33c764559085894f5cbbeda40b957aef4030bb32341299 -- candidate, unreviewed.
- Case a = -1/2: proof-LSplus-red-v1-addendum-2.md f2984d80340f80569a1e9f91cde61db2edb8d3f35582b6334d8cae722f96d2b7 -- candidate, unreviewed.
- Parent-accepted: SLZ3 (review/olson-SLZ3-parent-verdict-v1.md 2b7b08a3ec861e953e35d2802d8deba2ae584edeed36f04350fc3a9c6fa1ae24); CF/RS/ROW package (review/olson-CFXT-
  ROW-LSII-parent-verdict-v1.md ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0).  Classical: index-one record (e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6, n = p), Cauchy-Davenport.

## Statement
Let p be prime, floor(2p/3) + 1 <= kappa <= p - 2 and e := p - kappa.  If e = 2 (p >= 7), or e >= 3 and p >= 10e - 13, then every odd
sequence Y over C_(2p) with no zero-sum of length in [2kappa + 2, 2p] and a zero-sum of length >= 2p + 2 has |Y| <= 3kappa + 1.
The bound is attained: E2(kappa) = h^(3kappa-p+2) (3h)^(p-1) and E3(kappa) = h^(3kappa-2p+2) (3h)^(2p-1) satisfy (ZP_kappa)
(proof-LSplus-e2-v1.md Sec. 4, CF instances valid for every kappa in the range) and contain the zero-sums h^(p+3) (3h)^(p-1) and
h^3 (3h)^(2p-1) of length 2p + 2 (exponents available as 3kappa >= 2p + 1).
## Proof
e = 2: Theorem LS+2.  e >= 3: if a counterexample exists, SLZ3 cuts it to length exactly 3kappa + 2 keeping a long zero-sum
(LS+-RED Sec. 0).  As p >= 10e - 13 >= 9e - 13, LS+-RED gives (A) a unique heavy generator g and (B) a in {-1, -1/2}.  a = -1 is
impossible by addendum 1 (p >= 10e - 13); a = -1/2 is impossible by addendum 2 (prime p >= 10e - 13).  []

## Exceptional cells (NOT covered by this statement or by BASE1+)
Exactly the pairs (p, kappa), p prime, with 3 <= e = p - kappa <= floor((p - 1)/3) (i.e. kappa >= floor(2p/3) + 1) and p < 10e - 13
(for primes: p <= 10e - 17, i.e. kappa <= (9p - 17)/10), except kappa = (2p + 1)/3 for p = 1 (mod 3) (BASE1+, proof-STAB-base-
p1mod3-v1.md 8a41189cb8d2c254394c4ac44963d7a64f7f6ace00a9ad829f7e0af96def0985, candidate).  For p <= 31:
  p = 11: kappa = 8;  p = 13: kappa = 10;  p = 17: kappa = 12, 13;  p = 19: kappa = 14, 15;  p = 23: kappa = 16, 17, 18, 19;
  p = 29: kappa = 20, ..., 24;  p = 31: kappa = 22, ..., 26.
(p = 5 has an empty range; p = 7 has only kappa = 5 = p - 2, covered.)  For large p the covered part of the range is
kappa >= (9p - 13)/10, i.e. roughly the top 30 percent of the interval (2p/3, p - 2].  Finite aid only (not a premise): the complete
DFS of probes v11/v12 found maximal length 3kappa + 1 at (p, kappa) = (11, 8).
## Relation to LS and STAB
LS+ implies LS (3kappa + 1 < p + 2kappa + 1); all covered cells already lie in LS-lin's range p >= 6e - 10 (proof-LS-lin-v1.md), so no
new LS cell.  STAB (classification at length 3kappa + 1) is NOT covered: at length 3kappa + 1 the analogue of (B) also allows
a = 1, -1/3 (E3 is the case a = -1/3 with g = 3h) and E2 lies in the two-heavy-value case, so the exclusions above do not transfer
verbatim.
Credit context [INFERENCE, run review/olson-new-cells-priority-scout-v3.json]: the e = 2 cell may be routine via EGZ plus classical
inverse theorems; the index-one/greedy inputs are Savchev-Chen 2007; no priority or novelty claim.
