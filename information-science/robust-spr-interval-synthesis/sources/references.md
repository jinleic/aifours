# References

Verification legend: **[read]** primary text fetched and the cited statement checked in it;
**[meta]** bibliographic record confirmed via Crossref (title, authors, venue, pages) but the full
text was not read here; **[UNVERIFIED]** cited from a secondary source only. Local copies of fetched
files are in `/Users/jinleic/jinleic-workspace/scratch/ai4s-robust-spr-interval-synthesis/` with
SHA-256 listed (not synced; re-download with the URLs below).

## Book

- 郁文生, 王龙. 区间系统的鲁棒严格正实综合 (Robust Strictly Positive Real Synthesis for Interval
  Systems). In: 《10000个科学难题·信息科学卷》, Science Press, 2011, pp. 680–682 (PDF pp. 701–703).
  Page images: `book/pdfpage-0701.png`–`pdfpage-0703.png`. **[read]**

## Status-deciding sources (2026)

1. T. Xu, G. Dou, X. Ji, L. Wang, W. Yu. *Robust Strictly Positive Real Synthesis for Sixth-Order
   Interval Polynomial Families.* arXiv:2609.26541v2 [eess.SY], 22–23 Sep 2026.
   https://arxiv.org/abs/2609.26541 (v2 PDF sha256 1e44801454177b0b405ef82a6cc64a1b3a602223438d8d561db8047942c0056a).
   Theorem 2.1: every robustly Hurwitz MONIC sextic box has one real numerator of exact degree 6 with
   Re(beta(iw)/p(iw)) > 0 for all members and all real w; degenerate intervals allowed; Lean 4.30.0 /
   mathlib v4.30.0 formalization; acknowledges GPT-6 Astra assistance. Not peer reviewed. **[read]**
2. Lean development for (1): https://github.com/dgjszy/sextic-spr-proof, commit
   2b94aa79e472288d6044eae4382ac4abad535bb9 (2026-09-22), public theorem `SPR.N6.Direct.robustSPR`
   (`Lean/Main.lean`), statement `SPR.N6.RobustSPRStatement` (`Lean/SPR/N6/Definitions/Frequency.lean`).
   793 Lean files, 34.1 MB. **[read: statements and audit sources; not built]**
3. W. Yu, T. Xu, G. Dou, X. Ji, L. Wang. *Robust Strictly Positive Real Synthesis for Fifth-Order
   Interval Polynomial Families.* Manuscript PDF released 2026-10-06 as GitHub release
   `paper-2026-10-06` of https://github.com/dgjszy/quintic-spr-proof
   (https://github.com/dgjszy/quintic-spr-proof/releases/download/paper-2026-10-06/QuinticSPR-English.pdf,
   sha256 2e458cc3904523e5ecad08b9672d05a3688e04e4ec2629136251c8d30cc4c85f). Theorem 2.1: the
   same statement for monic quintic boxes; non-constructive proof (critical family, finite moment
   certificate with <= 6 support points, interpolation rigidity, 26-row enumeration, root-ratio
   exclusions). Cited as ref. [10] of (1). Not peer reviewed; no arXiv version found (not proof of
   absence). **[read]**
4. Lean development for (3): https://github.com/dgjszy/quintic-spr-proof, commit
   866e2b53774e8f614b6b01a393301da47ac887b2 (tag `paper-2026-10-06`), public theorem
   `SPR.N5.Direct.robustSPR`, statement `SPR.N5.Direct.RobustSPRStatement`
   (`Lean/SPR/N5/Definitions/Frequency.lean`). 65 Lean files. **[read: statements and audit sources; not built]**

## Earlier results cited by the book and by (1), (3)

5. L. Wang, W. Yu. *Robust SPR synthesis for low-order polynomial segments and interval polynomials.*
   Proc. 2001 American Control Conference, vol. 5, pp. 3612–3617, doi:10.1109/ACC.2001.946195;
   preprint arXiv:math/0202242. Defines the interval family as monic
   K = {s^n + sum a_i s^{n-i}, a_i in [a_i^-, a_i^+]}, proves n <= 4 (Theorem 4), states that for n <= 3
   the result is due to [Hollot–Huang–Xu 1989; Huang–Hollot–Xu 1990; Anderson et al. 1990; ...], gives
   a third-order triangle (polytope) whose members admit no common numerator of degree n-1 (Example 4).
   **[read, arXiv version]**
6. W. Yu, L. Wang. *Anderson's claim on fourth-order SPR synthesis is true.* IEEE Trans. Circuits
   Syst. I 48(4):506–509, 2001, doi:10.1109/81.917990. (Book ref. [10].) **[meta]**
7. B. D. O. Anderson, S. Dasgupta, P. Khargonekar, F. J. Kraus, M. Mansour. *Robust strict positive
   realness: characterization and construction.* IEEE Trans. Circuits Syst. 37(7):869–876, 1990,
   doi:10.1109/31.55062. (Book ref. [9].) **[meta]**
8. A. Betser, E. Zeheb. *Design of robust strictly positive real transfer functions.* IEEE Trans.
   Circuits Syst. I 40(9):573–580, 1993, doi:10.1109/81.244906. Their example (a synthesizable
   fourth-order family violating the LP condition of (7)) is reproduced as Example 1 of (5). **[meta]**
9. C. V. Hollot, L. Huang, Z. L. Xu. *Designing strictly positive real transfer function families: a
   necessary and sufficient condition for low degree and structured families.* Proc. MTNS 1989,
   Birkhäuser, pp. 215–227. (Book ref. [7].) **[UNVERIFIED]**
10. V. V. Patel, K. B. Datta. *Classification of units in H-infinity and an alternative proof of
    Kharitonov's theorem.* IEEE Trans. Circuits Syst. I 44:454–458, 1997. (Book ref. [8].) **[UNVERIFIED]**
11. S. Dasgupta, A. S. Bhagwat. *Conditions for designing strictly positive real transfer functions for
    adaptive output error identification.* IEEE Trans. Circuits Syst. 34(7):731–736, 1987,
    doi:10.1109/TCS.1987.1086198 (four-vertex reduction, as cited in (5) Lemma 4). **[meta]**
12. W. Yu, L. Wang, J. Ackermann. *Robust strictly positive real synthesis for polynomial families of
    arbitrary order.* Science in China Ser. F 47(4):475–489, 2004, doi:10.1360/03yf0053; related
    preprints L. Wang, arXiv:math/0210452 and arXiv:math/0211012 (abstracts: for any two n-th order
    polynomials, Hurwitz stability of their convex combination is necessary and sufficient for a
    common SPR numerator). **[meta; arXiv abstracts read]**
13. W. Yu, L. Wang. *Robust strictly positive real synthesis for convex combination of the sixth-order
    polynomials.* Proc. 2003 ACC, vol. 5, pp. 3840–3845, doi:10.1109/acc.2003.1240434; preprint
    arXiv:math/0211009 (abstract read). **[meta]**
14. W. Yu, L. Wang. *Design of robust strictly positive real transfer functions.* In F.-Y. Wang,
    D. Liu (eds.), Networked Control Systems, Springer, 2008, pp. 293–341,
    doi:10.1007/978-1-84800-215-9_11. **[meta]**
15. L. Wang, W. Yu. *Complete characterization of strictly positive real regions and robust strictly
    positive real synthesis method.* Science in China Ser. E 43:97–112, 2000. (Book ref. [6].) **[UNVERIFIED]**
16. V. L. Kharitonov. *Asymptotic stability of an equilibrium position of a family of systems of linear
    differential equations.* Differentsial'nye Uravneniya 14(11):2086–2088, 1978. **[UNVERIFIED]**

## Searches that found nothing (not evidence of absence)

- 2026-10-14 web searches for robust SPR synthesis of interval polynomials of order >= 7, arbitrary
  order, or counterexamples returned only (1), (5), (12), (13). The sextic repository states it was
  extracted from a non-public project `nth-order-spr-proof` (commit 52dd82d); no public higher-order
  result was found.

## Continuation source comparison (2026-10-14, Pacific)

- Re-read the primary quintic PDF linked in item 3, Sections 3.1–3.3, 4.1–4.3 and 5.1–5.3
  (PDF pp. 5–13): the first-failure construction, six-point bound, quadratic coprimality argument,
  interpolation identities, infinity alternative, and shared-component contact exclusions.
  Section 1 explicitly says that its support/degree argument is specific to the quintic problem
  and asserts no higher-order interval result. The continuation's I–J supply an all-order written
  argument using positive-real boundary geometry, not a replay of that source's Lean theorem.
- Re-read the primary [sextic v2 PDF](https://arxiv.org/pdf/2609.26541v2), Sections 4–6
  (PDF pp. 6–9): double contacts are separated from the nonnegativity proof; Section 5 explicitly
  warns that their existence alone does not imply nonnegativity. The exact degree-seven control
  in `../work/theory.md` illustrates a stronger failed shortcut (even a Hurwitz contact vector
  can fail), but is not presented as a newly discovered general warning.
- The proof of I uses elementary harmonic minimum principles and the local geometry of a
  positive-real rational function. K uses a sign-definite Laplace/Vandermonde expansion.
  L uses continuous, unwrapped phase. These are self-contained arguments here; a search of the
  entire positive-real/interpolation literature has not been performed. Their correctness and
  **novelty status are separate**: priority remains unclear, and none resolves the uniform
  n>=7 interval-synthesis question.
- The continuation's M is a general interior-transfer argument, not the sextic formula:
  positive-real rigidity excludes nonzero imaginary zeros, and adding
  epsilon*(1+s^n) supplies positivity near both endpoint frequencies while a compact middle
  interval retains its strict margin. The sextic paper's Section 6 instead establishes strictness
  for its specifically constructed numerator using the odd-part bounds. M's broader
  hypothesis/conclusion is proved here; its priority in the older positive-real literature has
  not been established.
