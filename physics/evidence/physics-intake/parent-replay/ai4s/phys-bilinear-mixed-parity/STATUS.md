# Status, prior art, and book bridge

Snapshot: **2026-10-14 PT**. This target was **unsolved in this project when assigned**, not certified globally novel by a failed literature search. The result is presented as **Certification**, not Discovery. Related models and techniques were established long before this investigation.

## 1. Bridge to the book

Lou Senyue and Li Jinhua, *On a new conjecture to find higher-dimensional integrable models*, in *10000 Selected Problems in Sciences: Physics* (Science Press, 2009), book pp. **350–351**, PDF pp. 383–384. The unedited supplied excerpt is `source/problem.zh.txt`, copied from the sibling chapter project.

The book asks whether integrability of a bilinear pair

`P(D_x,D_t)F.G=0`, `Q(D_x)P(D_x,D_t)F.G=0`

can imply integrability of its extension with another Hirota operator S, often replacing Q(D_x) by Q(D_y). It asks for proofs, a rule for R(S), and additional conditions if the general conjecture fails. The word integrability is not defined by one exhaustive criterion in the chapter.

Here the user-approved precise subproblem is **generic finite exponential N-solitons for every N**, with `Q(D_x)=D_x`, `R(S)=D_y`, and

`P=D_t+c1 D_x+c2 D_x^2+c3 D_x^3`, `c2 != 0`.

This is a parity branch of the same chapter as the sibling odd-cubic project, not a fifth unrelated book problem. All generic seeds in this branch are one-sided: F-only with `w=-p(k)` or G-only with `w=p(-k)`. The theorem permits arbitrary type patterns and independent active amplitudes. It includes the quadratic branch `c3=0`, unrestricted transverse parameters, and the D_x reduction. It does not prove the full book conjecture or identify Hirota's N-soliton criterion with every other meaning of integrability.

## 2. Primary comparison before the all-N claim

### Li–Lou (2008): known quadratic and odd-cubic models

**Li Jin-Hua and Lou Sen-Yue**, *Kac–Moody–Virasoro symmetry algebra of a (2+1)-dimensional bilinear system*, **Chinese Physics B 17(3)**, 747–753 (2008), DOI [10.1088/1674-1056/17/3/002](https://doi.org/10.1088/1674-1056/17/3/002). [Primary PDF](https://cpb.iphy.ac.cn/en/article/pdf/preview/10.1088/1674-1056/17/3/002.pdf), pinned as `source/li-lou-2008.pdf`.

The full paper was read. Eq. (4) explicitly gives the quadratic pair `(D_t+D_x^2)F.G=0`, `D_y(D_t+D_x^2)F.G=0`; Eq. (8) gives the odd-cubic pair. The paper proves generalized-symmetry results for the latter, not the parameterized mixed-parity all-N formula in this folder. Its §4 leaves additional powers n in Eq. (7) unclassified. That historical open statement must not be relabeled as an explicit primary claim that our exact mixed-coefficient seed problem remained open in 2026.

### Hietarinta (1987, author summary 1997): earlier same-pair cubic system

**Jarmo Hietarinta**, *A search for bilinear equations passing Hirota's three-soliton condition. II. mKdV-type bilinear equations*, **Journal of Mathematical Physics 28**, 2094 (1987), DOI [10.1063/1.527421](https://doi.org/10.1063/1.527421).

The accessible primary author summary was read: **J. Hietarinta**, *Introduction to the Hirota bilinear method* (1997), [arXiv:solv-int/9708006](https://arxiv.org/abs/solv-int/9708006), §4.2; pinned as `source/hietarinta-1997.pdf`. It explains the rotation to two equations on the same bilinear pair and lists

`(D_x^3+D_y)G.F=0`, `(D_x^3 D_t+a D_x^2+D_t D_y)G.F=0`.

At a=0 and with y,t renamed, this is the same odd-cubic pair used as the auxiliary family in our proof. The summary discusses the three-soliton search and its two soliton kinds; it is not a checked source for our all-N mixed-parity amplitude dictionary. The original 1987 article was not independently obtained in full.

### Peng et al. (2008): important unresolved prior-art comparison

**Ling-Zhi Peng, Meng-Xia Zhang, Gegenhasi, and Q. P. Liu**, *On integrability of a (2+1)-dimensional MKdV-type equation*, **Physics Letters A 372(23)**, 4197–4204 (2008), DOI [10.1016/j.physleta.2008.01.090](https://doi.org/10.1016/j.physleta.2008.01.090).

The DOI/Crossref metadata were read and pinned (`source/peng-2008-crossref.json`). The sibling's earlier status record quotes an abstract reporting Wronskian N-solitons and a bilinear Bäcklund transformation/Lax representation for a Hietarinta case. This pass did **not** verify that quoted abstract against accessible full text. The publisher [article](https://www.sciencedirect.com/science/article/pii/S0375960108004611) and [abstract page](https://www.sciencedirect.com/science/article/abs/pii/S0375960108004611) returned HTTP 403; the public Elsevier article and abstract APIs returned only sparse metadata, not the paper. A subsequent direct archive fetch was rate-limited (429), and the cited OSTI route returned 404. No credentials, paid access or access-control bypass were used.

Consequently, no claim is made that Peng et al. lack this family, that our Pfaffian representation improves their Wronskian representation, or that their exact case/parameter scope has been established here. **The all-N proof below is self-contained and does not import an unavailable theorem. Novelty remains unverified.**

## 3. Comparable project baseline and actual advance

The sibling `phys-bilinear-higher-dim-integrability/RESULTS.md` C3/C6 had established all eight mixed-parity three-soliton patterns and exact finite N=4,5 controls, but no closed mixed formula or all-N argument. Those facts were only the local starting baseline, not evidence of scientific priority.

This folder supplies a closed Pfaffian-subset formula rational in `lambda=3*c3/(2*c2)`, with a complete all-N proof. The key mixed-branch obligations are:

1. complete the cube while retaining the nonconstant background;
2. introduce one auxiliary F-type spectral point with zero transverse parameter;
3. extract a valid **unique charge coefficient of the bilinear identity**, rather than project tau functions arbitrarily;
4. normalize each F/G physical seed correctly;
5. cancel the total lambda exponent for every permitted subset cardinality, producing a formula regular at `lambda=0` and proving the quadratic branch.

The elementary odd-cubic matrix lemma is shared standard Pfaffian algebra, developed concurrently with the sibling and rederived in this folder. We do not rely on an unproved sibling conclusion: RESULTS.md gives the derivative, minor-sum and bilinear identities in full. The sibling subsequently obtained an independent Codex audit of its own all-N lemma; that audit does not replace the independent review of our charge/gauge/limit steps.

## 4. What is settled versus still unverified

- **Known model-level background:** the quadratic and odd-cubic models are in older primary literature. For `c3 != 0`, the mixed operator is explicitly gauge-equivalent to the odd-cubic operator. We do **not** claim a new integrable model.
- **Precisely addressed here:** the generic F/G all-N tau construction with constant normalized mixed background, including `c3=0`, unrestricted transverse waves, and all type patterns. RESULTS.md supplies a written algebraic proof, with exact finite independent controls kept separate.
- **Not established:** scientific novelty, a complete dictionary to Peng et al.'s full paper, a formal Lean/kernel certificate, general polynomial P, arbitrary R(S), or globally nonsingular physical solutions.

If future access reveals the exact same all-N seed family in primary prior art, its novelty verdict should become **ALREADY-SOLVED (literature)** while the written derivation and replay package remain a useful reproduction. An unsuccessful search is not a priority claim.
