# Screen v2 (parent lead, 2026-10-17 16:04:22 PDT): primary nonexistence / upper-bound theorems for (Z_p^e, k; 1) DMs

Question: does any primary theorem exclude a cyclic (Z_27, 6; 1) difference matrix (= CFR(5,27))?
Conventions: van Greevenbroek-Jedwab write "(G, m, lambda) difference matrix" = m rows x lambda|G| columns; Pan et al.
write "(G, k, 1)-DM is a k x |G| matrix". Both count ROWS, so CFR(r,n) <=> (Z_n, r+1, 1) (facts-v1 E2): CFR(5,27) is
a (Z_27, 6, 1)-DM; CFR(3,9) a (Z_9, 4, 1)-DM; CFR(5,25) a (Z_25, 6, 1)-DM.

## Sources read (pinned bytes in ../sources/web, text extractions in sources/)
1. K. van Greevenbroek, J. Jedwab, "A new structure for difference matrices over abelian p-groups", arXiv:1806.04279v3
   (29 Nov 2018), survey Sections 2-3 and 7. PDF sha256 0efe81f0…8f91, text sources/arxiv-1806.04279v3.txt (a07f89ef…a8c).
   Nonexistence/upper-bound results stated there (verbatim):
   * "Theorem 2.1 (Jungnickel [Jun79, Theorem 2.2]). Let G be a group, and suppose there exists a (G, m, λ)
     difference matrix. Then m ≤ λ|G|."  -> m <= 27: no obstruction for m = 6.
   * "Theorem 2.2 (Hall and Paige [HP55, Theorem 5], Drake [Dra79, Theorem 1.10]). Let G be a group containing a
     nontrivial cyclic Sylow 2-subgroup, and let λ be odd. Then there does not exist a (G, 3, λ) difference matrix."
     -> not applicable (|G| = 27 odd).
   * "Theorem 3.19 (Ge [Ge05, Theorem 3.12]). Let v ≥ 5 be an odd integer for which gcd(v, 27) ≠ 9. Then there exists
     a (Z_v, 4, 1) difference matrix." and "it is known [PC16, Lemma 2.2] that there does not exist a (Z9, 4, 1)
     difference matrix."  (pdftotext renders the "≠" as "6=")
   * Question 7.2: "For which primes p and abelian p-groups G is the largest integer m for which a (G, m, 1)
     difference matrix exists not a power of p?" -- i.e. no general max-row theorem for abelian p-groups was known.
   * Constructions only (Buratti Thm 3.12: a (G, p^floor(n/e), 1)-DM for |G| = p^n, exponent p^e; for Z_27 this gives
     3 rows) -- lower bounds, not upper bounds.
2. R. Pan, R.J.R. Abel, Y.A. Bunjamin, T. Feng, T.J. Tsang Ung, X. Wang, "Difference matrices with five rows over
   finite abelian groups", Des. Codes Cryptogr. (2022), doi:10.1007/s10623-021-00981-6; Springer abstract page pinned
   (springer-s10623-021-00981-6.html, sha256 624164be…a7). Verbatim abstract: "It is proved that if G is a finite
   abelian group and the Sylow 2-subgroup of G is trivial or noncyclic, then a (G, 5, 1)-DM exists, except for
   G ∈ {Z_3, Z_2⊕Z_2, Z_4⊕Z_2, Z_9} and possibly for some groups whose Sylow 2-subgroup lies in {Z_2⊕Z_2, Z_4⊕Z_2,
   Z_32⊕Z_2, Z_16⊕Z_4}, and some cyclic groups of order 9p with p prime."  -> a (Z_27, 5, 1)-DM exists (Z_27 is
   not excepted and 27 is not 9p), i.e. CFR(4,27); nothing about 6 rows. Body not read (Springer full text closed).
3. P.H.J. Lampio, doctoral thesis "Classification of difference matrices and complex Hadamard matrices" (Aalto 2015),
   PDF sha256 122c1944…b114: exhaustive classification only "where the number of columns c < 20 and G is an abelian
   group of order g with 3 ≤ g ≤ 7" (Table 6.1 covers Z_2..Z_7, Z_2xZ_2). Nothing on Z_27.
4. OpenAlex works citing Pan et al. 2022 (12, pinned openalex-cites-pan2022.json): none treats six rows or cyclic
   3-groups (two are about PAIRS of orthogonal orthomorphisms of cyclic/nilpotent groups).

## Controls of conventions (all computed in this lane)
* Z_9: no CFR(3,9) = no (Z_9,4,1): our CNF UNSAT with verified DRAT (controls/encoder-v1, D1) and 0 orthogonal pairs
  among the 225 normalized orthomorphisms (../code/z9_pairs_check.py) -- agrees with [PC16, Lemma 2.2].
* Z_25: Kirtchakov's CFR(5,25) = (Z_25, 6, 1) passes both checkers -> no theorem "max rows for Z_{p^2} is p".
* Z_27: our odd CFR(4,27) witnesses = (Z_27, 5, 1) pass both checkers -> agrees with Pan et al. 2022.
* Z_33: Sage DM_33_6_1 = (Z_33, 6, 1) -> no "smallest prime factor" upper bound.

## Conclusion
No primary theorem found that excludes a cyclic (Z_27, 6, 1)-DM. The only odd-order cyclic nonexistence results in the
read sources are the trivial m <= |G| and (Z_9, 4, 1) [PC16]. Access holes: Handbook VI.17 (Colbourn, Table 17.42),
Hedayat-Sloane-Stufken Table 6.67, Evans' books (1992, 2018), Ge 2005 body, Pan-Chang 2016 body, Pan et al. 2022 body,
Evans 2007 (J. Combin. Des. 15:195-209). Our own restrictions (facts-v3 E7/E8: no linear rows when 3 | n; Gram
constraint) are lane-derived proofs of sub-model nonexistence, not literature, and not a nonexistence of CFR(5,27).
