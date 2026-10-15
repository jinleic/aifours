# Eligibility, current status, and comparable prior art

Date: **2026-10-14 (America/Los_Angeles)**. Scope: the SO(5)-reduced harmonic multiplication matrix element in CRW (2009), Eq. (29), not arbitrary tensor operators or every fractional-parentage coefficient.

**Final selection verdict: ALREADY-SOLVED in equivalent pre-2009 class-one coupling literature. Frontier state: HEADROOM-ABSENT for a new scientific-resolution claim.** The complete convention-matched proof is preserved as Certification, but this candidate must not be counted among newly solved open problems. The decisive backward-prior-art identity is `RESULTS.md` §4A.

## 1. Why this particular statement was selected

Bao Chengguang's book entry, “母配分系数递推关系的破解,” in *10000个科学难题·物理学卷* (Science Press, 2009), pp. 348–349 / PDF pp. 381–382, asks for analytic solutions of CFP recurrences beyond spin-1 bosons. The supplied excerpt is copied unchanged as `source/problem.zh.txt`. Spin-2 bosons and d-boson models use SO(5) representation theory; analytic reduced elements and SO(5)→SO(3) coupling coefficients are part of that machinery.

The parent explicitly approved reselection to a **published, explicitly conjectural precise target**. The selected formula is not presented as equivalent to the whole book question. Its connection is a reduction-theory subproblem: the common SO(5)-reduced factor of harmonic multiplication, after the SO(3) and missing-label dependencies have been separated. Solving it does not determine all isoscalar factors or all CFPs.

### Primary-source open statement

**M. A. Caprio, D. J. Rowe, T. A. Welsh, “Construction of SO(5) ⊃ SO(3) spherical harmonics and Clebsch–Gordan coefficients,” Computer Physics Communications 180 (2009), 1150–1163.** DOI [10.1016/j.cpc.2008.12.039](https://doi.org/10.1016/j.cpc.2008.12.039); [arXiv:0902.0020v1](https://arxiv.org/abs/0902.0020v1).

Location: **§2.5, Eq. (29), PDF p. 7; explicit qualification on PDF p. 8**. The exact short quote is:

> “However, we stress that is has not been proved in full generality.”

The grammatical “is” is in the source. The expression is introduced immediately above as conjectured and numerically inspected. Both page images are preserved (`source/crw2009-page-07.png`, `source/crw2009-page-08.png`), and the equation/quote were checked visually against the PDF. Section 3.3 is implementation, not the conjecture location.

### Later primary restatement

**T. A. Welsh, D. J. Rowe, “A computer code for calculations in the algebraic collective model of the atomic nucleus,” Computer Physics Communications 200 (2016), 220–253.** DOI [10.1016/j.cpc.2015.10.017](https://doi.org/10.1016/j.cpc.2015.10.017); [arXiv:1408.3824v3](https://arxiv.org/abs/1408.3824v3), version dated 2016-01-05.

Location: **§IV, Eq. (45), PDF p. 7**. The authors call it “the empirical expression” and say it

> “was obtained by recognising the pattern of results obtained numerically.”

This is direct evidence of the formula's empirical presentation in that version, **not** proof that nobody else had proved it by 2016 or by 2026.

The relevant section of **D. J. Rowe and J. L. Wood, *Fundamentals of Nuclear Models: Foundational Models* (World Scientific, 2010)** was subsequently reached through the public [Google Books preview, p.199](https://books.google.com/books?id=Du07DQAAQBAJ&pg=PA199). Section 4.5.4, Eq. (4.175), labels the identical formula “Empirical formula”; footnote 49 describes inference from numerical patterns and finite verification, not a general proof. Pages 197–199 are preserved as `source/rowe-wood2010-page*.png`. Claim 4.4 on pp.198–199 proves only the quadrupole case. This clears a specific source-access hole, not the backward-prior-art problem below.

## 2. Precise baseline and missing obligation

The initially screened physics baseline was an all-seniority factorial formula, extensive finite checks, and established scalar/quadrupole cases. **That baseline was incomplete:** the independent referee identified an equivalent already-derived class-one SO(n) formula predating 2009. The final deliverable is therefore a convention-matched reproduction/certification, not an improvement over the strongest prior mathematical baseline.

The bounded certification obligation is to identify the CRW normalization sum (28) with a basis-independent triple-harmonic trace, evaluate its invariant integral for arbitrary integer seniorities, and preserve the paper's measure mass and chosen positive phase. It does **not** require diagonalizing every SO(5)→SO(3) multiplicity space. This explains tractability, but does not establish novelty or openness.

The supplied universal proof is in `RESULTS.md`, Theorem 1. It uses the addition theorem and classical Rogers linearization, then accounts for all normalization factors. Finite computations are independent controls, not the proof of the all-integer claim.

## 3. Strongest directly comparable prior art

| Primary source | What is already established | Relation to this deliverable |
|---|---|---|
| CRW (2009), above, §§2.2–2.5, Eqs. (26)–(29) | Orthogonal harmonic construction, exact arithmetic algorithm, normalized CG extraction; empirical all-seniority reduced-element expression; quadrupole cases | The convention-matched derivation here certifies their expression; it is not claimed as a new mathematical result. |
| Welsh–Rowe (2016), above, Eqs. (43)–(46) | Constant harmonic, multiplication integral, empirical formula, algebraically established quadrupole reduced elements | Independent convention and boundary checks; still empirical wording for the general formula. |
| M. A. Caprio, D. J. Rowe, T. A. Welsh, “Racah's method for general subalgebra chains: Coupling coefficients of SO(5) in canonical and physical bases,” J. Math. Phys. 51 (2010), 093518, DOI [10.1063/1.3445529](https://doi.org/10.1063/1.3445529), [arXiv:1006.2875](https://arxiv.org/abs/1006.2875) | General coupling-coefficient methods, including generic SO(5) representations | A computational/representation-theory result is not automatically an explicit proof of this particular multiplication reduced-element formula. Parent-supplied full-text screen found no such proof there. |
| S. Ališauskas, “Integrals involving triplets of Jacobi and Gegenbauer polynomials and some 3j-symbols of SO(n), SU(n) and Sp(4),” chapter 9, *Studies of Mathematical Physics Research*, ed. Ch. V. Benton, Nova (2004), pp. 203–241; [arXiv:math-ph/0509035v1](https://arxiv.org/abs/math-ph/0509035v1) (posted 2005) | **PDF Eq. (26a), p.11, already gives the all-class-one SO(n) zero-index 3j symbol.** Eq. (23a) fixes its normalized integral; Eq. (21) gives the zonal function. The source attributes (26a) to G. Junker, J. Phys. A 26, 1649 (1993), not independently inspected here. | **Decisive equivalent prior solution:** at n=5, \(R_{\rm CRW}^2=d_{v_1}d_{v_2}G_5^2/V\), exactly. The original equation image and complete factorial dictionary are preserved; see RESULTS §4A. PDF (13b) separately supplies the classical integral, attributed to Vilenkin. |
| G. E. Andrews, R. Askey, R. Roy, *Special Functions*, Cambridge University Press (1999), Theorem 6.8.2; authoritative transcription [DLMF 18.18.22](https://dlmf.nist.gov/18.18.E22) | Rogers's Gegenbauer product linearization; positivity for positive Gegenbauer parameter | The universal summation theorem used in the proof. Its exact TeX is saved as `source/dlmf-18.18.E22.tex`. |

**Prior-art interpretation:** the mathematical content is known in equivalent form before 2009, not merely derivable using an old technique. The positive phase and area convention supply the dictionary, not a new invariant. **ALREADY-SOLVED / HEADROOM-ABSENT** is the conservative selection verdict. Earliest historical priority and whether someone explicitly wrote the CRW-normalization dictionary remain unclaimed.

## 4. Forward-citation screen and its limits

The following **forward** screen is bounded and found no explicit CRW-convention proof in the checked later material. It cannot find pre-2009 sources by construction. The backward source in §3 does contain an equivalent solved formula, so the forward-search miss does not support current openness.

### Databases and provenance

- **OpenAlex, checked directly on 2026-10-14:** work [W1663297195](https://openalex.org/W1663297195) reports 27 citing records. The complete title/DOI/date inventory is `source/openalex-citing-20261014.json`; [query](https://api.openalex.org/works?filter=cites:W1663297195&per-page=100&select=id,title,doi,publication_year,publication_date). These are **records, not 27 audited proofs**. There are duplicate DOI records and an apparently irrelevant title, “Geomagnetic orbit determination: EKF or UKF?” (W3184110961), whose full text was not checked. The latest returned date is 2026-04-08.
- **Parent's literature scout `ScoutSO5Conjecture`, report read on 2026-10-14:** 27 OpenAlex records, 23 INSPIRE records, approximately 26 distinct works. Its citation-screen excerpt is preserved as `review/scout-handoff-excerpt.txt`. The INSPIRE count, approximate union, and scout-designated reading depths below are **externally reported and not independently reconstructed**; most corresponding full texts are not preserved in this package.
- **Semantic Scholar:** scout reported fetch rejection; not checked.
- Exact-term web searches for the arXiv id/proof and SO(5) reduced-element/conjecture language returned no additional settling source. Some returned unrelated Welsh conjectures; those were rejected as irrelevant. Search result summaries were not treated as mathematical evidence.

### Depth table

| Work / link | Actual depth | Finding and limitation |
|---|---|---|
| [CRW 2009, arXiv:0902.0020](https://arxiv.org/abs/0902.0020) | Worker: relevant full-text sections and original page images | Exact formula, normalization, positive phase, explicit unproved statement confirmed. |
| [Welsh–Rowe 2016, arXiv:1408.3824v3](https://arxiv.org/abs/1408.3824v3) | Worker: relevant full-text sections; scout: full text | Eq. (45) repeats formula with empirical/pattern-recognition wording; no general proof identified in the screen. |
| [Caprio et al. 2010, arXiv:1006.2875](https://arxiv.org/abs/1006.2875) | Scout: full text | Generic coupling algorithm, no identified derivation of CRW (29). |
| [D. J. Rowe, “The fundamental role of symmetry in nuclear models,” 2013, arXiv:1304.6115](https://arxiv.org/abs/1304.6115), DOI [10.1063/1.4810815](https://doi.org/10.1063/1.4810815) | Scout: full text; worker: bibliographic/abstract verification | Scout reports restatement with “We also obtain [5]” but no proof. No inference that every cited book passage was checked. |
| [Pan et al., arXiv:1309.2654](https://arxiv.org/abs/1309.2654), “Construction of basis vectors for symmetric irreducible representations of O(5) ⊃ O(3),” Eur. Phys. J. Plus 129 (2014), 169, DOI [10.1140/epjp/i2014-14169-0](https://doi.org/10.1140/epjp/i2014-14169-0) | Scout: full text | Tensor (1,0) results, not an identified all-tensor-seniority proof. |
| [D. J. Rowe, “Applications of the Capelli identities in physics and representation theory,” J. Phys. A 48 (2015), 055203, arXiv:1501.02390](https://arxiv.org/abs/1501.02390), DOI [10.1088/1751-8113/48/5/055203](https://doi.org/10.1088/1751-8113/48/5/055203) | Scout: full text; worker: abstract/metadata | No settling proof identified by scout; abstract is not a proof audit. |
| [arXiv:1105.4297](https://arxiv.org/abs/1105.4297) and the 2014 *Acta Physica Polonica B* ACM review | Scout: full text | No settling proof identified. The review was not independently reacquired by this worker. |
| [A. C. N. Martins, M. W. Suffak, H. de Guise, “SU(3) Clebsch–Gordan coefficients and some of their symmetries,” J. Phys. A (2019), arXiv:1909.09055](https://arxiv.org/abs/1909.09055), DOI [10.1088/1751-8121/ab4b70](https://doi.org/10.1088/1751-8121/ab4b70) | Scout: full text; worker: abstract/metadata | SU(3) coupling subject; no CRW proof identified. |
| Caprio, “Coupling coefficients for SO(5) with applications to nuclear physics,” J. Phys.: Conf. Ser. 237 (2010), 012009, DOI [10.1088/1742-6596/237/1/012009](https://doi.org/10.1088/1742-6596/237/1/012009); Deveikis et al., CASC 2020 | Scout: **abstract only** | IOP full text was captcha-blocked; neither abstract excludes a proof in the full text. |
| Remaining nuclear applications in the OpenAlex inventory, including the 2025 overview and 2026 “Triaxiality in Mo and Ru nuclei” | **Titles only** here; scout reports about 16 title-only applications | Not an exclusion certificate. A relevant appendix or citation can be missed. |
| Rowe–Wood book (2010), §4.5.4 pp.197–199, [public preview](https://books.google.com/books?id=Du07DQAAQBAJ&pg=PA199) | **Worker: relevant original page images**, reached after the frozen review started | General Eq. (4.175) is labeled empirical; only quadrupole Claim 4.4 is proved in that passage. This supersedes the scout's “not reachable” status for this section, not for the whole book. |
| Rowe–Welsh–Caprio, “Bohr model as an algebraic collective model,” Phys. Rev. C 79 (2009), 054304, DOI [10.1103/PhysRevC.79.054304](https://doi.org/10.1103/PhysRevC.79.054304); a possible Welsh thesis | **Full text not reached** | OpenAlex reports no open-access copy; APS abstract/accepted routes returned 403 and a normal browser reached a Cloudflare challenge. No challenge/paywall was bypassed. No conclusion about that paper's proof contents. |
| P. S. Turner, *The Algebraic Collective Nuclear Model and SO(5)*, Toronto PhD thesis (2005), §§2.2.6–2.2.7, pp.30–31, [text mirror](https://paperzz.com/doc/8284479/the-algebraic-collective-nuclear-model-and-so-5--by-peter...) | Worker: relevant text sections through a third-party transcription, **not an independently authenticated PDF** | Normalized harmonic multiplication, CG orthogonality, and quadrupole formulas; no all-tensor closed formula in the checked passage. This is a distinct Turner thesis, not a Welsh thesis. |

## 5. Present verdict and most valuable next action

**Selection verdict: ALREADY-SOLVED in equivalent literature. Frontier state: HEADROOM-ABSENT for new-open-problem counting.** The full all-integer CRW-convention formula is proved in `RESULTS.md`, with independent exact representations and two completed referee reports; this remains Certification / Reproduction.

The parent was notified and accepted rejection of this candidate. Do not weaken the target or change a parameter to manufacture novelty. The most valuable next action for the user's five-problem selection is a genuinely different explicitly open target, screened both backward and forward before discovery claims. The broad CFP/missing-label problem remains outside what this folder settles.
