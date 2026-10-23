# Focused primary screen for Theorem A / Proposition C — v1 (2026-10-19T00:25:35-0700, ContinueCFR21; read-only)

Scope question: is the mod-3 constant-character statement (no sum-zero mod-3 character of support <= 5 is constant on
the columns of a (Z_n,k;1)-DM with k >= 4, 3 | n, 9 ∤ n; hence mod-3 affine rank >= 5 for k = 7) or its count
congruences already in the primary literature?

## Read scopes (exact)
1. Evans, "A class of orthogonal latin square graphs", Australas. J. Combin. 57 (2013) 189-216,
   https://ajc.maths.uq.edu.au/pdf/57/ajc_v57_p189.pdf — full text pp. 189-200 read (markit extraction): Lemmas 1-5,
   Theorems 1-4 with proofs, Conjecture 1 and the strong-complete-mapping remark. Theorem 4 (verbatim): "If p is the
   smallest prime divisor of |G| and the Sylow p-subgroup of G is cyclic, then any (p − 2)–clique of P(G) is a
   maximal set of orthomorphisms of G", where P(G) = power maps x -> x^r. For G = Z_n, p = 3 this says the linear
   triple {0, x, rx} cannot be extended; proof via a homomorphism onto the cyclic Sylow 3-subgroup and Evans (1991).
2. Evans, "The existence of strong complete mappings", Electron. J. Combin. 19 (2012) #P34 (+2018 corrigendum),
   https://www.combinatorics.org/ojs/index.php/eljc/article/download/v19i1p34/2093 — full text read: Theorem 3
   (Evans 1990) and Corollary 4: a group of odd order with nontrivial cyclic Sylow 3-subgroup has no strong complete
   mapping (equivalently, for Z_n: the triple {0, x, -x} is not extendable to a 4-row DM); "Horton's proof, Evans'
   proof of Theorem 3, and Hedayat's 1977 proof that the order of a Knut Vik design cannot be divisible by 3, are
   essentially the same" (proofs themselves not read).
3. Lampio, Östergård, Szöllősi, "Orderly generation of Butson Hadamard matrices", arXiv:1707.02287v1 — HTML fetched
   to sources/arxiv-1707.02287v1.html (sha d7ecbcafc209693343e8d8b9b0c5620f036033e308d6ee547e70fd5bb59ed1ca) and
   searched for lemma statements (Lemmas 3.1-3.6: vanishing sums of roots of unity, orderly generation); no
   constant-character/rank lemma found. Not read in full.
4. Web searches (titles/snippets only): J-characteristics / aliasing of three-level orthogonal arrays; ternary
   difference matrices or generalized Hadamard matrices with index not divisible by 3; strong complete mappings.
NOT accessed: Hedayat 1977 (JCTA 22), Horton 1990 (Discrete Math 79), Evans 1990 (Congr. Numer. 70), Evans 2018 book,
Hedayat-Sloane-Stufken "Orthogonal Arrays" ch. 6 (difference schemes), de Launey's GH papers, Tang-Deng 1999,
Xu-Wu 2001, Pistone-Rogantin 2008, Cheng-Ye 2004 (J-characteristics / indicator functions).

## Findings
* The LINEAR special case of L3 (rows 0, x, rx; in particular 0, x, -x = strong complete mappings) is classical and
  holds for every n with a nontrivial cyclic Sylow 3-subgroup, including 9 | n (Hedayat 1977, Horton 1990, Evans 1990,
  Evans 2013 Thm 4). L3/Theorem A instead cover ARBITRARY rows whose mod-3 images satisfy a sum-zero relation of
  support 3, 4 or 5, but need 9 ∤ n. Overlap; neither contains the other (verified against the Evans texts read).
* No statement of the support-4/5 exclusions, of the k = 7 rank bound, or of Proposition C was found in the sources
  read. Because Theorem A depends only on the mod-3 projection (a (Z_3,k;n/3) difference matrix = difference
  scheme), the unread difference-scheme / generalized-Hadamard / J-characteristic literature is the main priority
  risk. Note: the OA obtained by developing the mod-3 image has 3n runs (63 for n = 21, divisible by 9), so general
  OA run-size results do not directly give Theorem A; the relevant object is the difference scheme with n columns.
* Verdict: PRIORITY UNCLEAR. No novelty claim; describe Theorem A as "a necessary condition proved in this lane;
  the linear special case is classical".
