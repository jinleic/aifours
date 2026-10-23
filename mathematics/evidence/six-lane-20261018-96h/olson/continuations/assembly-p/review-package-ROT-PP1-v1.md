# Review package: terminal k = p+1 -- Proposition VAC, Lemmas P/U, Theorem ROT-PP1-TOP, and obstruction note, v1

Owner OlsonAssemblyP. Frozen after /bin/date 2026-10-19T12:17:20-0700. CANDIDATE_UNVERIFIED. Separate from the ASSEMBLY-P
packet. Written word-level proofs relative to the accepted NF, GRX and CT and the classical Cauchy-Davenport theorem; no Lev,
(S1), index-one, S(p), REFL, SHgen or pending candidate is a premise. No computation, model launch, novelty, priority, Lean or
human-review claim. The parent owns reviews and verdicts.

## 1. Review exactly these texts
- WHOLE proof: proof-ROT-PP1-v2.md, sha256 99143ea503a01a6376bed91a2a7ca8b91591617351f35ce4864117bf2949f1ca, lines 1-211
  (20,095 bytes). v1 (efbd4afbb5e3a40d64b6d5d659d5e71dc9c09fdc6d8f874036e36551c92389f6) is a preserved never-sent draft
  differing by four wording repairs (header lines 3-7); do not review v1.
- WHOLE obstruction note: obstruction-ROT-PP1-v2.md, sha256 4839cbd37d178038747a07e6c603ba344718d1c4c74508cfc7229aae417528dc,
  lines 1-106 (9,712 bytes); v1 (c5885a0b50913632d3b2e3653dda9ee14d19fc3779887cb0088168a62b83a84c) differs by one line
  citation and one added case; do not review v1.
- Frozen BEFORE derivation: ROT-PP1-scope-v1.md 698521494bcfbd951f417e182698102e3ba1f49559adc15d6a23d709d93686e0 (11:57:04)
  and ROT-PP1-scope-v1-addendum-1.md d29e2180eac74d78b0c1346819f586835824c8605df53742cabcc1fcf2741b7c (12:06:22).
Statements (proof Sec. 0; p >= 7 prime, w an avoider of length 4p-2, w^ an admissible normal form with terminal k):
- Proposition VAC: k >= p+1 implies kappa^ >= 1.
- Lemma P: k = p+1, (p-1)/2 <= kappa^ <= p-2: every non-constant sign pattern has a signed rotation value of multiplicity
  >= 2kappa^+1. Lemma U: these values lie in one class {a, -a} with a != 0; at most p-2 letters lie outside it.
- Theorem ROT-PP1-TOP: SOME admissible normal form with k = p+1 and kappa^ = p-2 => rotation multiset rho_c^A rho_(-c)^(3p-5-A),
  2p-3 <= A <= 2p-1, c != 0.
- Obstruction note: the sequence statement "(ZP_kappa) => (S1_kappa) at length p+2kappa-1" holds for kappa <= floor(2p/3) and
  in the accepted LS+-band/BASE1+ cells with e >= 3, FAILS at kappa = p-2 (E2, E3) and kappa = p-1 (g^(2p-1)(3g)^(p-2)), and is
  undecided on U(p); exact failure points of the available routes for 1 <= kappa^ <= p-3 and the smallest missing lemmas.

## 2. Governing source manifest
Use ONLY review-excerpts-ROT-PP1-v1.json, sha256 ae4fc4662dcaf62062e603cce0dbaa404609e6107f23a2a9acd827fdf65a9677
(6,486 bytes): a JSON list of {path, sha256 of the WHOLE file, start, end}, inclusive ranges, absolute paths; 28 ranges from 19
files, 49,694 selected bytes (both texts and both scope files whole). Every entry was re-verified at creation. Package +
manifest + selected text < 100,000 bytes. Accepting authority = cited parent verdict lines; excerpts of SHgen, SHgen-E, FB
and KPS-SLZ are included only because the obstruction note quotes their hypotheses (they are not premises of the proofs).

## 3. Argument map with endpoints for hostile review
A. (SR) (proof Sec. 1): with all blocks odd, delta = k-2m and C_max = 2H^+2m; n = 2p-C ranges over even numbers in
   [max(0, 2kappa^+2-2m), min(2p-2m, R)]. T(z_P) = sum_(i in P) tau_i; tau_i != 0 for empty runs (NF, ROT-few-E-v4 line 38).
B. VAC (Sec. 3): pigeonhole on p+1 block values, arc between equal values, n = 0 admissible when kappa^ = 0.
C. Lemma M (Sec. 4): capped-multiplicity pairing; check the capped total >= 2q and the i <-> i+q pairing.
D. Lemma P: n := max(p-1, 2kappa^+2-2m) is admissible for EVERY m >= 1 (m <= (p+1)/2); p-1 disjoint distinct pairs with
   F' of size n-(p-1); Cauchy-Davenport on {0, d_i} gives all residues. Check R >= 2p-2 iff kappa^ >= (p-1)/2.
E. Lemma U: uniqueness (2(2kappa^+1) > R), one class for all patterns, a = 0 excluded via the equal-value arc and 2kappa^
   zero letters.
F. Theorem (Sec. 5): Step 2 (A' <= p-2, A <= 2p-1 from (ZP_(p-2))); Step 3 (CT at n = p-3: b in {p-4, ..., p-1}); Step 4 window
   (W) with lambda = p-2-b, Lambda = 2p-3-A', gap p-1+delta; Step 5 heavy run via first passage of partial sums; Step 6 (needs
   delta >= 1): b >= p-1+2delta contradiction; Step 7 (b = p-1: A' >= p); Step 8 (>= 2 empty runs: nonempty runs <= 1+b+lambda);
   Step 9 (subset-sum set Sigma(B), |M| <= p-1-b, filler bound n-|J| <= A; cases b = p-2, p-3, p-4; the scaled equations
   x = 1 / x = -1/2 and p >= 7).
G. Endpoints to test: p = 7 (k = 8, kappa^ = 5, R = 16, n in {10, 12} for arcs); b = p-1 (A = 2p-4); A = 2p-1 (b = p-4);
   delta = 1; adjacent vs non-adjacent empty runs; tau_i = -2a; the E2/E3 multisets of the remark in Sec. 6.
H. Obstruction note: check every "holds" claim is a length comparison with the cited accepted statement, the explicit
   verifications for E2, E3 and g^(2p-1)(3g)^(p-2), and that Secs. 3-4 assert only where routes stop (no falsity or existence
   claim).

## 4. Requested verdict boundary
Judge Proposition VAC, Lemmas M/P/U and Theorem ROT-PP1-TOP for prime p >= 7 relative to the cited accepted interfaces at their
original scopes; judge the sequence facts of the obstruction note (Sec. 2) and whether Secs. 3-4 are accurately bounded. Report
interface-domain issues separately from logical gaps. Not requested and not claimed: rigidity for 1 <= kappa^ <= p-3 or
kappa^ = p-1 at k = p+1; reflection rigidity; INV*; any o_F assembly; ordered Olson for D_(2p) or all groups; p = 5; novelty
or priority; Lean or human review.
