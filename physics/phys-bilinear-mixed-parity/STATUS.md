# Status, prior art, and book bridge

Snapshot: **2026-10-14 PT**. This target was **previously unproved in this project**, not certified historically unsolved by a failed literature search. The result is presented as **Certification**, not Discovery. Related models and techniques were established long before this investigation. The final openness gate below is **PARTIAL-OVERLAP for each coefficient branch**; neither branch is cleared as a problem known to have been unsolved before this work.

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

## Openness gate (final, 2026-10-14)

### Gate question and access boundary

The gate concerns the **whole generic all-N F/G seed statement**, with constant normalized background, arbitrary type pattern, independent active amplitudes, and independent transverse wave numbers. It is stricter than asking whether the differential equation was already known or called integrable. The only supported historical wording is **“previously unproved in this project.”** No checked primary text explicitly states that this exact seed statement was open when our work began.

This pass used publisher-open material, arXiv, the author's University of Turku archive, INSPIRE, Crossref and OpenAlex. Peng/Hu/Gegenhasi retries were coordinated with the odd-cubic owner rather than duplicated. No login, shadow library, paid access, CAPTCHA bypass or paywall circumvention was used. The citation screen found 14 indexed citing works for Li–Lou (2008) and seven for Li–Jia–Lou (2007); these are **bounded metadata/title screens**, not proof that all relevant literature was found or read. URLs, counts and newly pinned PDFs are recorded in `source/openness-citation-screen.json`.

### Exact relation to Hietarinta's list and to Li–Lou model (ii)

**Cubic branch, c3 != 0.** The already-proved gauge in RESULTS.md §5 gives an exact equation-level dictionary. Write

```text
delta=c2/(3*c3), v=c1-c2^2/(3*c3),
q(r)=v*r+c3*r^3, Theta=delta*x-q(delta)*t,
Fhat=exp(Theta)*F, Ghat=G,
X=x-v*t, Y=c3*t, T=y.
```

In these coordinates the transformed pair, up to nonzero overall constants and harmless interchange of tau names, is

```text
B Fhat.Ghat=0,        D_T B Fhat.Ghat=0,
B=D_X^3+D_Y.
```

This is **precisely a=0**, not a nonzero-a member, of Hietarinta's displayed pair (37):

`B G.F=0`, `[D_T B+a D_X^2]G.F=0`.

The distinction cannot be removed by the stipulated **nonsingular Galilean/linear-coordinate, scaling and relative exponential-gauge maps**. Those maps induce invertible affine substitutions in the bilinear symbols. Our two symbols have the common factor P. For a≠0, `gcd(B,D_T B+a D_X^2)=gcd(B,a D_X^2)=1`, since `B=X^3+Y` does not divide `X^2`. Existence and degree of a common polynomial factor are preserved by those substitutions, nonzero rescalings, and invertible constant recombinations of the equations. This statement does not exclude a more general nonlocal Miura/Bäcklund correspondence.

Equation equivalence does **not** automatically identify the all-N seed families: our normalized vacuum `(1,1)` becomes `(exp(Theta),1)`, and the proof requires the background/charge construction, not just a variable rename.

**Quadratic branch, c3=0.** With `X=x-c1*t`, `Y=y`, `T=c2*t`, the pair becomes exactly

`(D_T+D_X^2)F.G=0`, `D_Y(D_T+D_X^2)F.G=0`.

This is Li–Lou (2008) Eq. (4), model (ii). The map preserves the constant tau background, seed amplitudes and independent transverse waves. It is not Hietarinta pair (37) at any a: at a=0 its common factor has degree three rather than two; at a≠0 it has no common factor. The other same-pair mKdV entries in the 1997 §4.2 list have a reducible lowest-degree quadratic symbol (`D_X^2` or `D_X D_T`), unlike the irreducible heat symbol `D_T+D_X^2`, or have a higher fixed degree. Thus they are not this pair under the same nonsingular affine-symbol maps. No singular degeneration is being promoted to an established equivalence.

### Per-source outcome

“Settles?” means **yes / partly / no on the evidence actually accessed**, for the exact all-N seed statement above, not merely its equation or an isolated soliton. “No” for an inaccessible source is not a claim that its unread contents lack a settling theorem.

| Source | Access actually achieved | Exact relation and level of result | Settles? |
|---|---|---|---|
| **J. Hietarinta, *Introduction to the Hirota bilinear method* (1997), [arXiv:solv-int/9708006](https://arxiv.org/abs/solv-int/9708006), §§3.3, 4.2–4.3** | **Read**, primary author text; pinned PDF already present | Lists pair (37), including a=0. §4.2 says the search combined “any set of three solitons” into a 3SS; §4.3 says many listed equations were known only to have 3SS and 4SS. The general NSS ansatz/definition in §3.3 is not an all-N proof for every listed pair. It does not give our shifted-background F/G dictionary. | **Partly:** exact cubic model overlap; no settling all-N theorem verified. |
| **J. Hietarinta, *A search for bilinear equations passing Hirota's three-soliton condition. II. mKdV-type bilinear equations*, JMP 28, 2094–2101 (1987), [DOI 10.1063/1.527421](https://doi.org/10.1063/1.527421)** | **Abstract/metadata; original full text inaccessible.** [INSPIRE record](https://inspirehep.net/literature/238832), [OpenAlex](https://api.openalex.org/works/https://doi.org/10.1063/1.527421), and [author archive](https://users.utu.fi/hietarin/home/hirotas-bilinear-method/) checked; no lawful open original PDF located | AIP-sourced abstract explicitly describes a three-soliton search. The 1997 author's summary supplies the pair used in the dictionary; the inaccessible original is not credited with a checked all-N result. | **Partly**, with a full-text limitation. |
| **Li Jin-Hua and Lou Sen-Yue, CPB 17, 747–753 (2008), [DOI 10.1088/1674-1056/17/3/002](https://doi.org/10.1088/1674-1056/17/3/002), Eqs. (4), (8), §4** | **Read**, full primary PDF | Eq. (4) is exactly the normalized quadratic system. The paper cites it as a known subcase; its main generalized-symmetry proof concerns the n=3 model (8). It does not display/prove arbitrary-pattern all-N F/G tau functions for Eq. (4). | **Partly:** exact known quadratic equation, not the specified all-N family. |
| **Li Jin-Hua, Jia Man and S. Y. Lou, *Kac–Moody–Virasoro symmetry algebra and symmetry reductions of the bilinear sinh-Gordon equation in (2+1)-dimensions*, JPA 40, 1585–1595 (2007), [DOI 10.1088/1751-8113/40/7/010](https://iopscience.iop.org/article/10.1088/1751-8113/40/7/010/pdf)** | **Abstract read; full text subscription-gated**, no OA location in the checked OpenAlex record | Li–Lou's precursor. Its abstract claims infinite symmetries, reductions, and a relation to the first negative KP member; no all-N F/G seed theorem is verified from the abstract. Absence from an abstract is not absence from the paper. | **Partly**; full-text scope remains undetermined. |
| **Peng, Zhang, Gegenhasi and Liu, PLA 372, 4197–4204 (2008), [DOI 10.1016/j.physleta.2008.01.090](https://doi.org/10.1016/j.physleta.2008.01.090)** | **Metadata/abstract-level account; full text inaccessible.** Coordinated retry checked publisher, public APIs, author/institutional profiles and lawful archive discovery | Reports Wronskian N-solitons for a Hietarinta mKdV-type case, making it a high-risk prior all-N overlap. The exact equation case, amplitudes and transformed-background/charge dictionary have not been inspected. The cubic gauge makes this source directly relevant, but does not establish that its family contains ours. | **Partly; not cleared in either direction.** |
| **Gegenhasi, X.-B. Hu and H.-Y. Wang, *A (2+1)-dimensional sinh-Gordon equation and its Pfaffian generalization*, PLA 360, 439–447 (2007), [DOI 10.1016/j.physleta.2006.07.031](https://doi.org/10.1016/j.physleta.2006.07.031)** | **Original full text inaccessible.** Coordinated owner found publisher/API metadata only and no OA location. Its equation and Wronskian/Pfaffian claims are independently described in the read 2023 primary paper below | That inherited pair has `P2=D_Y+D_X^2` and second symbol `D_T P2+2D_X`, not our `D_T P2`. A verified zero-remainder limit with all our independent F/G seeds is missing. | **Partly**, not a demonstrated settlement of the zero-remainder branch. |
| **S.-N. Wang, G.-F. Yu and Z.-N. Zhu, *General Soliton and (Semi-)Rational Solutions of a (2+1)-Dimensional Sinh-Gordon Equation*, JNMP 30, 1621–1640 (2023), [DOI 10.1007/s44198-023-00147-z](https://link.springer.com/article/10.1007/s44198-023-00147-z), Eq. (5), Theorem 1** | **Read**, publisher OA full text; pinned `source/wang-yu-zhu-2023.pdf` | Genuine arbitrary-N Gram determinants, but for `P2` and `D_T P2+2D_X`. Their pair has no common nonconstant factor, so no stipulated nonsingular affine/gauge map makes it our common-factor pair. Theorem 1 fixes the nonzero sinh-Gordon normalization; no checked singular-limit dictionary recovers the zero-remainder all-pattern statement. | **Partly:** strong adjacent all-N result, different pair. |
| **X.-B. Hu, S.-Y. Lou and X.-M. Qian, *Nonlocal symmetries for bilinear equations and their applications*, [arXiv:0812.0961](https://arxiv.org/abs/0812.0961) (2008; journal 2009), [DOI 10.1111/j.1467-9590.2009.00435.x](https://doi.org/10.1111/j.1467-9590.2009.00435.x)** | **Read relevant equations and conclusion**, public arXiv full text; pinned PDF | Derives positive/negative KP/BKP hierarchies and bilinear Bäcklund transformations. Its NKP formulation uses additional tau functions; its conclusion says further work is needed on tau-function structures. That is not an explicit open statement for our exact pair, nor a checked all-pattern formula for it. | **No** verified settlement; related hierarchy context only. |
| **A. Dimakis and F. Müller-Hoissen, *Multicomponent Burgers and KP Hierarchies, and Solutions from a Matrix Linear System*, SIGMA 5, 002 (2009), [arXiv:0811.0110](https://arxiv.org/abs/0811.0110), Prop. 2.1, Thm. 4.1** | **Read relevant primary sections**, public arXiv full text; pinned PDF | All-order heat/Cole–Hopf and matrix-KP constructions. Scalar heat exponentials cover our all-F or all-G vacuum sectors. No exact identification of both our coupled equations and arbitrary interacting F/G seed family is supplied by the checked statements. | **Partly:** known one-sided sectors and broader methods, not the whole target. |
| **J.-Y. Wang, Z.-F. Liang and X.-Y. Tang, *Infinitely many generalized symmetries and Painlevé analysis of a (2+1)-dimensional Burgers system*, Phys. Scr. 89, 025201 (2014), [DOI 10.1088/0031-8949/89/02/025201](https://doi.org/10.1088/0031-8949/89/02/025201)** | **Abstract via OpenAlex; full text inaccessible**, publisher CAPTCHA and no checked OA location | Relevant citing work on a coupled Burgers system. The abstract claims symmetries, a higher modified-KdV/potential-BLMP flow, and Painlevé analysis, not all-N tau functions. Its exact bilinear equation/family cannot be certified from that abstract. | **No verified settlement; full-text limitation retained.** |
| **A.-M. Wazwaz, *Burgers hierarchy: Multiple kink solutions and multiple singular kink solutions*, J. Franklin Inst. 347, 618–626 (2010), [DOI 10.1016/j.jfranklin.2010.01.003](https://doi.org/10.1016/j.jfranklin.2010.01.003)** | **Metadata checked; full text inaccessible**, publisher 403 and no checked OA copy | A relevant scalar/multiple-kink title, not evidence for the two-equation mixed-seed tau family. No equation dictionary was verified. | **No verified settlement.** |
| **Hietarinta, Ramani and Grammaticos, *Continuous vacua in bilinear soliton equations*, JPA 27, 3149–3158 (1994), [DOI 10.1088/0305-4470/27/9/027](https://doi.org/10.1088/0305-4470/27/9/027)** | **Author bibliography checked; full text inaccessible**, publisher CAPTCHA | Potentially relevant to shifted backgrounds; no theorem or seed dictionary was read, so it cannot be used either to settle or to clear novelty. | **No** verified settlement; unread contents remain undetermined. |
| **Alzaleq, Al-zaleq and Alkhushayni, *Traveling Waves for the Generalized Sinh-Gordon Equation with Variable Coefficients*, Mathematics 10, 822 (2022), [DOI 10.3390/math10050822](https://doi.org/10.3390/math10050822)** | **Setup read** from public INSPIRE PDF, retained as `source/inspire-57cf9b9a.pdf` | A nonmatching search hit: its equations concern a variable-coefficient (1+1)-dimensional sinh-Gordon problem, not our heat/cubic bilinear pair. | **No.** |

**Why heat exponentials alone do not settle the target.** With G=1, the quadratic pair reduces to the linear heat/transport equation for F, so a finite sum of F-type exponentials is an established all-N sector; likewise for F=1 and G-only seeds. But a generic mixed F/G pair requires the nonzero coefficients displayed in RESULTS.md §2, depending on both k and l. A scalar Cole–Hopf tau or a pair with one fixed tau does not establish those interactions. No new construction or calculation was performed in this gate.

### One final gate verdict per branch

| Branch | Gate verdict | Interpretation |
|---|---|---|
| **c3 != 0, c2 != 0** | **PARTIAL-OVERLAP** | The equation is exactly the known a=0 cubic member, not a≠0. Hietarinta's checked summary provides 3ST/classification evidence, not the target all-N proof. Peng's reported all-N work and continuous-vacuum literature remain serious uninspected overlaps. No verified dictionary establishes prior settlement of the entire shifted-background generic seed family; no primary statement establishes that it was unsolved. |
| **c3=0, c2 != 0** | **PARTIAL-OVERLAP** | The equation and constant background are exactly Li–Lou model (ii). All-order heat sectors and nearby determinant/Wronskian constructions predate this work. The strongest read arbitrary-N sinh-Gordon theorem has a nonzero `2D_X` remainder, and the relevant older/full coupled-Burgers sources remain partly inaccessible. Neither prior settlement nor prior openness of our full interacting F/G family is certified. |

**Inaccessible/high-risk items:** Hietarinta's 1987 original and 1994 continuous-vacuum paper; Peng et al. (2008); Gegenhasi–Hu–Wang (2007); Li–Jia–Lou (2007); Wang–Liang–Tang (2014); and Wazwaz (2010). Coordinated discovery also checked author/institutional pages, arXiv author/date queries, CORE and Internet Archive Scholar; no settling full-text dictionary was obtained. A rejected Unpaywall request was **not** treated as evidence of no OA copy.

**Consequence for the user's “not solved yet” requirement:** neither branch passes an affirmative historical-openness gate. The local theorem remains a correct written certification, but it must not be advertised as resolving a scientifically established open problem. No code, shared engine, proof theorem or heavy verification run was changed in this literature-only pass.

