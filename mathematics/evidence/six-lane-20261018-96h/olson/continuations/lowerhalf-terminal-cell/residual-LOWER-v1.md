# LOWER residual note: exact remaining lower-half regime after proof-LOWER-v1, and failed routes, v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T22:08:56-0700. Companion of proof-LOWER-v1.md (SHA256 251c8dca1c34be7b76432dc50d13368b11a7bf6da6bbb8bd31e4ee18e7cd476d).
CANDIDATE_UNVERIFIED. This note records where the routes stop; it does not claim that any remaining cell is false or that an
avoider exists; "missing claims" are route targets, not lemmas shown necessary. No counterexample is supplied. Full NF/word
antecedent throughout; no multiset-only statement.

## 1. What is proved (pointers into proof-LOWER-v1.md)
- Theorem R (Sec. 1): k=p+1 admissible kappa_hat range 0..p-1; the accepted coverage found by searching the R16/R18 parent
  verdicts excludes no whole lower-half cell; accepted B0S-CJ''' excludes exactly the all-rotations-equal sub-case.
- Theorem S (Secs. 3-7): run structure sum floor(r_i/2)<=2kappa-1; integer form at a T=0 arc (all letters odd multiples of
  one gamma, ZSTRUCT/FB data); interval-filling signed sums; light side; the lift framework (Lemmas U, A, C, THETA) for FULL
  patterns.
- Theorem K1 (Sec. 8): the whole cell kappa_hat=1 is excluded for every prime p>=11 (sub-case of equal rotations by CJ''').
- Lemma CR (Sec. 9): CONDITIONAL on (H-ALT) and kappa<=(p-3)/4: rotation rigidity with tight lift data.

## 2. Exact remaining regime (target minus proved parts)
Every prime p>=11 and every integer 2<=kappa_hat<=(p-3)/2 (for p=11: kappa_hat in {2,3,4}), under the full antecedent, with
rotations NOT all equal. Every putative avoider there satisfies, after the normalisation of Sec. 4 at a light T=0 arc P0:
 (i) sum_i floor(r_i/2)<=2kappa-1 (<=2kappa even-length runs); (ii) letters c_l odd, Pi0+nu0=B*=W+2n+>=R, n+ + n- = 2t<=2kappa-2,
 n-<=n+, W+n+<=2p-1, |c_l|<=p-2, at least (p+4)/2 coefficients equal to 1 at P0; (iii) for every pattern P the signed sums of
 X^(P) are all integers of [-nu(P),Pi(P)]; (iv) o(P0)<=kappa; (v) for every FULL pattern P: B*<=2p-2 and H(P) has its
 representative U(P) in [Pi0+1,2p-1-nu0] with parity sigma(P); additivity (Lemma A, when 2Pi0+3+nu0>2p), complements
 (Lemma C) and run increments theta_i (Lemma THETA) hold; patterns with kappa+1<=m<=(p+1)/2-kappa are full; (vi) if (H-ALT)
 holds and kappa<=(p-3)/4, all rotations lie in one pair {rho_g,rho_-g} and in each alternating set all but kappa runs have
 theta_i=-1, the top kappa+1 summing to -1-nu0.

## 3. Smallest missing claims of this route (not claimed necessary)
(MC-L1) Rigidity for 2<=kappa: prove (H-ALT) (fullness of alternating subsets with more than (p+1)/2-kappa runs, i.e. every
        even v realisable with at most 2p-2|J| letters), or replace it by another family whose fullness is provable and
        whose complement identity sum_all theta = Pi0-nu0-2p is available; and remove kappa<=(p-3)/4 (two disjoint
        (kappa+1)-subsets of an alternating set) for larger kappa.
(MC-L2) The rotation-pair case with the tight data of Lemma CR (B>=1 after the all-equal sub-case of CJ''') must be
        contradicted with partial-window patterns (m<=kappa, e.g. arcs), whose holes near 0 (size about 2kappa) are exactly
        what Theorem K1 avoids at kappa=1 (where singletons and arcs are full).

## 4. Failed routes (retained, with the failing inequality)
(F1) Upper-half pairing (Lemma P/U): p-1 unequal pairs need 2(p-1)<=R=p-1+2kappa, false for kappa<=(p-3)/2; a common dominant
     class needs 2(2kappa+1)>R, also false. Only "some signed value has multiplicity >=2kappa+1" survives (RS(a) at n=2kappa).
(F2) Omission window MW at m=1: counted lengths are even K in [w0,min(p-1,phi)], so q is about (p-1-w0)/2 and w0+q<p.
(F3) Theorem P (Chevalley-Warning) needs F+sum floor(r_i/2)>=3p-1; here this sum is 3p-1-2kappa+sum floor(r_i/2)<=3p-2,
     short by 2kappa-sum floor(r_i/2)>=1 variables; it yields (i) only.
(F4) Davenport-alpha items: H+R=2p-2+kappa<3p-1 (plus at most 2kappa empty brackets).
(F5) Zero-sum reformulation: identity iff some zero-sum S of the 2p+2kappa elements (1,x_l), (r_i mod 2, -h_i) of C_(2p) has
     n(S)+2m(S) in [2kappa+2,2p]; Davenport (2p) supplies zero-sums but n is not additive under unions.
(F6) Block values alone: y_i=i (mod p) has no zero alternating sum at all, so rotations are essential.
(F7) Fixed-base additivity on isolated families (P0 u Q): every full piece contributes only <=-1-nu0; for kappa>=2 single runs
     are not full (holes about 2kappa near the bottom), and averaging gives only about -(1+nu0)/(kappa+1) per run.
(F8) Pigeonhole guarantees only one pair of equal block values (one T=0 arc pair).
