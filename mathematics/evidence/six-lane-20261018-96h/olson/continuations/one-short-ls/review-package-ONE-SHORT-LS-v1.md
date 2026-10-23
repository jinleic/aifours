# Review package: Theorem ONE-SHORT-LS (ZP_kappa => S1_kappa at the exact length p+2kappa), v1

Owner OlsonAssemblyLS. Frozen after /bin/date 2026-10-19T10:40:17-0700. CANDIDATE_UNVERIFIED written proof, CONDITIONAL on the
statement-level external Lev 2022 Theorem 2 (used once, in case (I)), exactly as G-LS. No computation, model launch, novelty,
priority, Lean or human-review claim. The parent owns reviews and verdicts.

## 1. Review exactly this candidate
WHOLE proof: proof-ONE-SHORT-LS-v2.md, sha256 c544aad2ab0cadc4c76870dc97382b6a749bbdda85f96596bdb128efe9b19ffc, lines 1-276
(26,173 bytes). v1 (f42aac1cbf91ab844734b593a28a39510e3e0fc8d831d7e2782acbdbebe7e050) is a preserved, never-sent draft; v2 differs
only in two citation line ranges (ROW 56-59; LS+2 template 28-63) and one wording repair in Sec. 3 (the bound r+2h is stated under
rho(W) <= h). Do not review v1.
Frozen scope, written BEFORE derivation: ONE-SHORT-LS-scope-v1.md, sha256
2b9cfbcdf66cf43b173aa2f9a43542c906b50e04cbae690a860e3c321dd5b872 (10:17:32).
Statement (copied from the proof): Let p >= 7 be prime and kappa an integer with floor(2p/3)+1 <= kappa <= p-2. Every sequence Y of
odd elements of C_(2p) with |Y| = p+2kappa EXACTLY that satisfies (ZP_kappa) satisfies (S1_kappa).
Excluded: kappa = p-1 (false: g^(2p-1)(3g)^(p-1)); kappa <= floor(2p/3) (S1-sharp); |Y| >= p+2kappa+1 (G-LS); |Y| < p+2kappa;
any word-level statement. The G-LS threshold is NOT lowered by assertion: every step at the new length is re-derived.

## 2. Coverage and trust accounting (not an extra claim)
| Item | Status |
| --- | --- |
| Imports | CF(a), CT, ROW, AP' (parent-accepted, original scopes); Lev 2022 Thm 2 (external, statement level, CONDITIONAL). |
| Not imported | RED, DGM-p, LS-II', SLZ3, S1-sharp, G-LS (template only), any pending narrower candidate. |
| New lemmas | IP (involution pairs), DOM (dominant generator at length p+2kappa via CT, n = p-2), AP'' (progression in an arc of 2N+2). |
| Cells also covered without Lev by accepted LS+ | kappa = p-2 (LS+2); e >= 3 with p >= 10e-13 (LS+ chain); BASE1+ (p = 1 mod 3, kappa = (2p+1)/3). LS+ (|Y| <= 3kappa+1) implies the theorem because 3kappa+1 < p+2kappa. |
| New (Lev-conditional) coverage | 3 <= e, p < 10e-13, outside BASE1+, e.g. (11,8), (13,10), (17,12-13), (19,14-15), (23,16-19). |
| Computation | none; no transitive computer-assisted input in the cited interfaces. |

## 3. Governing source manifest
Use ONLY review-excerpts-ONE-SHORT-LS-v1.json, sha256 b1b3d3a8ad47b7b7eee397cb9531964edd60d7e33a9a419e6761d624fed2adc5
(5,262 bytes): JSON list of {path, sha256 of the WHOLE file, start, end}, inclusive ranges, absolute paths; 22 ranges from 17
files, 68,520 selected bytes, including the whole proof v2, the whole scope, the full G-LS template body (lines 62-196) and LS-II
v2 / addendum Step 5' (for the constant comparison). Package + manifest + selected text stay below 100 KB. Old CANDIDATE headers in
imported files are superseded ONLY by the cited parent verdict lines plus mandatory errata; model reviews alone are not acceptance
authorities. Proof Sec. 10 gives every interface's source lines, sha256, verdict item, original domain and discharge.

## 4. Argument map with endpoints for hostile review
A. Lemma IP / Corollary IP' (proof Sec. 1): deleting |T|-2p involutions from a long zero-sum leaves a zero-sum of length exactly 2p.
   IP' needs at most d-1 terms equal to neither g nor iota.
B. Lemma DOM (Sec. 2): CT with n = p-2 (|Y|-n = 2kappa+2); heavy = multiplicity >= p-1; at most two heavy values. Two heavy:
   not both >= p (x0^p x1^p); the multiplicity-(p-1) value is x1; j0 >= 1 gives a length-(2kappa+2) zero-sum; j0 = 0 forces
   alpha = 0 because p does not divide 2kappa+2 (THIS is the step that fails at kappa = p-1); then only iota-power zero-sums.
   One heavy: M >= 2kappa+2, not iota, M <= 2p-1; d <= 2e-2, r <= p-2.
C. Sec. 3: (1) from CF(a) using |W|+2rho <= r+2h <= 2p UNDER rho <= h; ROW at K = p-2e (check r >= d and r+2e-2 <= 2p);
   dichotomy (I) d <= h; (II) one value v1 >= p-2e+1, s <= e-1 and s <= d-1.
D. Case (II) (Sec. 4): AP' with n = h on an arc of 2h+1 residues (3h+2 = 3e-1 < p): mu1 in {1,-1,1/2,-1/2}. 1 and 1/2 forbidden
   (check m = min(h, floor(v1/2)) and 4m > d); -1/2 is iota (IP'); -1: v1 <= p-e, three phi-bullets with d <= 2e-2, rule (R),
   TINY/NEGATIVE with c' <= 2e-3, Step 5 prefix bound, Step 6 (a)-(c) with drop c'+1 <= 2e-2 landing at >= 2kappa+4.
E. Case (I) core (Sec. 5): Z0 maximal mod-p zero-sum with k <= d-1; delta' in [1, h]; n = p-2e+delta'; (2); t; strict few-sums
   inequality |A| <= p-e+t < 2n with margin p-3e+2delta'-t >= 2; Lev hypotheses (zero-sum-free in C_p, empty sum counted);
   interval realizability of every s in [0, S].
F. Pinning (Sec. 6): l <= 2e-1-delta'. delta' >= 2: AP' on 2N+1, exclusions b = 1 (t <= S), 2 (2t <= delta' <= S), -2
   (p-2h <= n <= S). delta' = 1: NEW Lemma AP'' (check (i)-(iii) and the no-wrap lift with p >= 3N+5); b = 1, 2, and for N = 1
   b = +-3, excluded; b = -2 survives iff S = n and then U' is all involutions (6.2, IP'). e = 2: b in {-1, -2}.
G. b = -1 (Secs. 6.3-8): S <= p-e; R in [1, e-delta'+1]; localization (h <= zeta <= S+h impossible); (8) P_(j0) <= d-2 <= h-2;
   (10) s >= p-3e+2delta'+1 >= 4; witness from ANY long T with j <= (p-2e)/2 (no SLZ3); lifts -j, p-j; tau = -j; final
   contradiction with (1) at Z*.
H. Endpoints to test: e = 2 (d = 1; compare LS+2), e = 3 (N = 1 in AP''), delta' in {1, 2}, d in {1, h}, k = 0 (Z0 empty),
   R = 1, S = n, S = p-e, j = 1 and j = floor((p-2e)/2), p = 7 (kappa = 5, e = 2), p = 11 (kappa = 8, e = 3, Lev-conditional),
   p = 13 (kappa = 10, e = 3). Compare each changed constant with the G-LS template via proof Sec. 9.

## 5. Requested verdict boundary
Judge validity of Theorem ONE-SHORT-LS at EXACT |Y| = p+2kappa for prime p >= 7 and floor(2p/3)+1 <= kappa <= p-2, relative to the
accepted interfaces at their original scopes and the declared Lev statement. Report any interface used outside its domain
separately from any new algebraic/occurrence-level gap, and check the three new lemmas (IP, DOM, AP'') in full. Not requested and
not claimed: LS+ or STAB at new cells, lengths below p+2kappa, kappa = p-1, any word-level or ordered-Olson conclusion (an o_F = p
consequence would stay conditional on the pending ASSEMBLY-LS and a separate word-level review), novelty or priority, Lean or
human review.
