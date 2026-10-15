# Status and state of the art (as of 2026-10-14)

Book problem: 关于得到高维可积模型的一个新猜想 (On a new conjecture to find higher-dimensional integrable
models), 楼森岳 (Lou Senyue) and 李金花 (Li Jinhua), Ningbo University, in 《10000个科学难题·物理学卷》
(Science Press, 2009), book pp. 350–351 (PDF pp. 383–384). Source text: `source/problem.zh.txt`; page images:
`source/loulipage-383.png`, `source/loulipage-384.png`.

## 1. What the book states

If the (1+1)-dimensional bilinear system

    (1)  P(D_x, D_t) F·G = 0,   Q(D_x) P(D_x, D_t) F·G = 0

is integrable, then

    (2)  P(D_x, D_t) F·G = 0,   R(S) P(D_x, D_t) F·G = 0

"may be" (可能是) integrable. P and Q are polynomials, R is an undetermined polynomial ("in many cases R has
the same functional form as Q"), and S may be the Hirota operator of an extra dimension, a supersymmetric,
discrete or q-deformed Hirota operator. The book says that Ref. [6] (Li & Lou 2008) gives seven simple
successful examples, all with R and Q of the same linear form and R(S) = D_y or R(S) = A (a supersymmetric
bilinear operator). It asks: how to prove the conjecture, how to determine R(S), and, if it fails, which extra
conditions make it hold.

Typography. The page image (`source/loulipage-384.png`) prints the second equation of (2) as
`R(S)P(D_x, D_c)F,G = 0`. Both primary statements of the same ansatz write `P(D_t, D_x)` in both equations
(Li & Lou 2008, Eqs. (62)–(63); Wang, Lou & Qian 2010, Eqs. (4)–(5)), so `D_c` is a typo for `D_t`, and
`F,G` denotes the bilinear pair F·G.

Precision. The book's statement is a heuristic: it does not define "integrable" and does not say whether
integrability of (1) is meant for general (F, G) or only on special reductions such as F = G. The precise
readings used here are fixed in `RESULTS.md` §0.

## 2. Primary sources on the conjecture

| Source | What it contains | Access |
|---|---|---|
| Li Jin-Hua, Lou Sen-Yue, "Kac–Moody–Virasoro symmetry algebra of a (2+1)-dimensional bilinear system", *Chin. Phys. B* **17**(3), 747–753 (2008), doi:[10.1088/1674-1056/17/3/002](https://doi.org/10.1088/1674-1056/17/3/002) | Book's Ref. [6]. Three explicit models: (i) `D_y D_x D_t F·G = 0, D_x D_t F·G = 0` (bilinear form of the isotropic integrable sine-Gordon / Loewner–Konopelchenko–Rogers system); (ii) `(D_t + D_x^2)F·G = 0, D_y(D_t + D_x^2)F·G = 0` (a subcase of the bilinear non-isotropic sine/sinh-Gordon system); (iii) `(D_t + D_x^3)F·G = 0, D_y(D_t + D_x^3)F·G = 0`, shown to have infinitely many generalized symmetries (formal series symmetry approach) and a Kac–Moody–Virasoro point-symmetry algebra. Asks (their Eq. (7)) whether `(D_t + D_x^n)F·G = 0, D_y(D_t + D_x^n)F·G = 0` is integrable for other n, and states the ansatz (62)–(63). | Full text read: CPB site PDF (`https://cpb.iphy.ac.cn/en/article/pdf/preview/10.1088/1674-1056/17/3/002.pdf`, sha256 `9186c7bf…a739d`) |
| Wang You-Fa, Lou Sen-Yue, Qian Xian-Min, "A new (2+1)-dimensional supersymmetric Boussinesq equation and its Lie symmetry study", *Chin. Phys. B* **19**(5), 050202 (2010), doi:[10.1088/1674-1056/19/5/050202](https://doi.org/10.1088/1674-1056/19/5/050202) | Restates the conjecture ("Conjecture: If (4) is integrable, then (5) may be integrable … in many cases R(x) = Q(x)"), lists the three Li–Lou models "and some others in Refs. [17]–[19] and [20]" (supersymmetric bilinear forms of Liu, Hu, Zhang, Wang, Wu, Yang 2005–2008). Proposes `(D_t + D_x^2)F·G = 0, S_y(D_t + D_x^2)F·G = 0` (super-Hirota S_y) and calls it "a further positive example of the conjecture", adding that "the conjecture should be checked further". | Full text read (CPB site PDF) |
| Wang Jianyong, Yang Yunqing, Tang Xiaoyan, Chen Yong, "A novel (2+1)-dimensional Sawada–Kotera type system: multisoliton solution and variable separation solution", *Nonlinear Dyn.* (2024), doi:[10.1007/s11071-024-09511-0](https://doi.org/10.1007/s11071-024-09511-0); preprint Research Square rs-3801786 (CC BY 4.0) | Studies `D_y(D_x^5 + D_t) f·f = 0`, obtained from the Sawada–Kotera bilinear form `D_x(D_x^5 + D_t) f·f = 0` "only by changing one of the Hirota operators D_x → D_y". Finds three- and four-soliton solutions only under extra constraints on the wave numbers (their Eq. (16) for N = 3) and conjectures N-soliton solutions under such constraints. Does not discuss the Li–Lou conjecture. | Preprint full text read (sha256 `b99addf5…d966c`); journal version not read |
| Delisle L., Jaouadi A., "A Classification of Hirota-Integrable Supersymmetric Bilinear KdV-Type Equations", arXiv:[2609.14372](https://arxiv.org/abs/2609.14372) (2026-09-13) | Supersymmetric analogue: `S P(D_x, D_t) τ·τ = 0`, P odd. Within `P = aX^5 + bX^3 + cX + T` only `a = 0` admits unconstrained three-super-soliton solutions; the N = 1 SUSY Sawada–Kotera–Ramani equation is only "weakly" Hirota integrable (needs Carstea's fermionic constraint). | Preprint full text read; not peer reviewed as far as we know |
| J. Hietarinta, "A search for bilinear equations passing Hirota's three-soliton condition. II. mKdV-type bilinear equations", *J. Math. Phys.* **28**, 2094 (1987), doi:[10.1063/1.527421](https://doi.org/10.1063/1.527421); summarised by the author in "Introduction to the Hirota bilinear method", arXiv:[solv-int/9708006](https://arxiv.org/abs/solv-int/9708006), §4.2 | mKdV-type pairs `B(D)G·F = 0, A(D)(F·F + G·G) = 0` (B odd, A even); the rotation `F = f + g, G = i(f − g)` turns them into `B g·f = 0, A g·f = 0`, i.e. **both equations on the same pair**, the shape of (1)/(2). A computer search for pairs where any three solitons of the two kinds (A-type: `F = 1 + e^η, G = 0`; B-type: `F = 1, G = e^η`) combine gave five equations; one is (37) `(D_x^3 + D_y)G·F = 0, (D_x^3 D_t + aD_x^2 + D_t D_y)G·F = 0`, which for a = 0 is `B = D_y + D_x^3`, `A = D_t B`: Li & Lou's model (iii) with t and y interchanged (exactly the form of their Eqs. (10)–(11)). The other four are not of the form `A = R·B` with R linear. | 1987 paper **not** read (paywalled); content taken from the author's 1997 summary (sha256 `6b415a0b…62553`), which does not state the search space |
| Peng Lingzhi, Zhang Mengxia, Gegenhasi, Liu Q. P., "On integrability of a (2+1)-dimensional MKdV-type equation", *Phys. Lett. A* **372**, 4197–4204 (2008), doi:[10.1016/j.physleta.2008.01.090](https://doi.org/10.1016/j.physleta.2008.01.090) | Abstract (OSTI record 21171282): "A (2+1)-dimensional equation of MKdV type proposed by Hietarinta is considered. It is shown that this equation has N-soliton solution represented in terms of Wronski determinants. Also, a bilinear Bäcklund transformation and a Lax representation are proposed." The publisher's snippet says it treats "a particular case" of Hietarinta's system; that this case is (37) with a = 0, i.e. model (iii), is our inference (the external reviewer reports the same identification). | Abstract only; full text not accessed |

Other works citing Li & Lou 2008 (OpenAlex, 14 citing records on 2026-10-14; titles/abstracts only, full
text **not** read): Wang, Yu & Lou, *Commun. Theor. Phys.* **53**, (2010), doi:10.1088/0253-6102/53/6/01
("Symmetries and algebras of a (2+1)-dimensional MKdV-type system": infinitely many generalized symmetries,
w∞-type algebra); Tang, Li, Liang & Wang, *Phys. Lett. A* (2014), doi:10.1016/j.physleta.2014.03.040
(variable-separation solutions of "a coupled system of the modified KdV and potential BLMP equations");
Wang, Tang & Liang, *Chin. Phys. B* **27**, 040203 (2018), doi:10.1088/1674-1056/27/4/040203 (N = 1
supersymmetric (2+1)-dimensional systems from the Hirota formalism in superspace). The remaining citing
records concern unrelated equations.

A different program with a similar goal — Lou, Hao & Jia, "Deformation conjecture" (arXiv:2211.06844;
*JHEP* 03 (2023) 018) — deforms (1+1)-dimensional integrable systems using conservation laws; it does not
address the bilinear ansatz above.

Background used: R. Hirota, *The Direct Method in Soliton Theory* (CUP 2004); J. Hietarinta, "A search for
bilinear equations passing Hirota's three-soliton condition. I. KdV-type bilinear equations", *J. Math. Phys.*
**28**, 1732 (1987) (the three-soliton test as an integrability criterion); K. Sawada, T. Kotera, *Prog.
Theor. Phys.* **51**, 1355 (1974) (N-soliton solutions of the Sawada–Kotera equation, bilinear form
`D_x(D_t + D_x^5) f·f = 0`). Hietarinta's papers III–IV (sine-Gordon-type and complex bilinear equations)
were not read.

## 3. Which seven examples?

The cited Ref. [6] (Li & Lou 2008) contains three explicit (2+1)-dimensional examples, (i)–(iii) above, each
paired with its (1+1)-dimensional counterpart Q = D_x. It contains no supersymmetric example. The seven
examples with "R(S) = D_y or R(S) = A" therefore cannot be listed exactly from the cited paper. Wang, Lou &
Qian (2010) attribute further examples to the supersymmetric bilinear literature (their Refs. [17]–[20]); from
that paper the supersymmetric Boussinesq pair `(D_t + D_x^2)F·G = 0, S_x(D_t + D_x^2)F·G = 0` and its
`S_y` extension are explicit. Identifying the remaining examples with the supersymmetric KdV/mKdV/two-boson
bilinear forms of Liu, Hu and co-workers is an inference, not checked against those papers.

## 4. Settled vs open (2026-10-14)

Settled in the literature:

- Positive examples: the three Li–Lou models and the Wang–Lou–Qian supersymmetric model are shown
  "integrable" in the sense of infinitely many (generalized or Lie point) symmetries. Neither of these two
  papers constructs general N-soliton solutions of the two-function systems.
- The n = 3 model (iii) is, up to renaming t ↔ y, Hietarinta's mKdV-type pair (37) with a = 0, found in 1987
  to pass his three-soliton test (for his A- and B-type solitons); the abstract of Peng, Zhang, Gegenhasi &
  Liu (2008) reports Wronskian N-soliton solutions and proposes a bilinear Bäcklund transformation and a Lax
  representation for "a particular case" of Hietarinta's system (that this case is a = 0 is inferred, see §2). If so,
  model (iii) is integrable in the Lax sense, independently of Li & Lou's symmetry argument. Neither Li & Lou
  2008 nor Wang, Lou & Qian 2010 cite these works.
- The single-function (F = G) version of the n = 5 case, `D_y(D_t + D_x^5) f·f = 0`, has three- and
  four-soliton solutions only under wave-number constraints (Wang et al. 2024, by explicit computation). The
  generic three-soliton failure is implied by their need for constraint (16) but not stated as a theorem,
  and the paper does not connect it to the Li–Lou conjecture.

Explicitly open in the primary sources:

- Li & Lou 2008, Section 4: "Because of complicity of calculation, we have not yet found other integrable
  systems from Eq. (7)" — i.e. whether `(D_t + D_x^n)F·G = 0, D_y(D_t + D_x^n)F·G = 0` is integrable for any
  n other than 2, 3 — and "Even if the ansatz is not correct, we believe that we can still obtain many new
  integrable models from the ansatz!"
- Wang, Lou & Qian 2010: "the conjecture should be checked further".

No proof, general counterexample or class-level characterization of the conjecture itself was found
(searches of the web, OpenAlex citations of Li & Lou 2008, arXiv). The closest class-level result is
Hietarinta's 1987 mKdV-type search: according to his 1997 summary, among the five pairs found only (37) has
the shape `A = R·B` with R linear (search space and soliton families as in that paper, not read in the
original). An unsuccessful search does not establish that nothing else exists.

## 5. Baseline to beat

- Strongest positive evidence: three continuous-variable examples (`P = D_x D_t`, `D_t + D_x^2`,
  `D_t + D_x^3`, each with Q = D_x and R = D_y) and one supersymmetric example, verified by symmetry analysis;
  for `D_t + D_x^3` additionally a three-soliton test (Hietarinta 1987) and, per the abstract of Peng et al.
  (2008), Wronskian N-soliton solutions and a proposed Lax representation for "a particular case" of
  Hietarinta's system, inferred (not verified) to be this one.
- Strongest negative evidence: the Wang et al. (2024) constrained-soliton computation for the F = G reduction
  of n = 5, not framed as evidence against the conjecture.
- At intake, no general proof of the conjecture itself or general rule for R(S) was
  identified in the sources read. C9 below now independently certifies the odd-cubic
  subcase; no claim of historical priority follows.

## 6. Approved scoped target and primary-source comparison

The user explicitly approved selecting precise open subproblems. This continuation
addresses only the arbitrary-independent-amplitude C6 Pfaffian formula for
`P=D_t+c1 D_x+c3 D_x^3`, `c3≠0`, for **all finite N**. Its decision value is
closing an explicit all-N proof obligation, not declaring the already-known cubic
equation new. The new written proof is RESULTS.md C9; its evidence label is
**Certification**, with **NOVELTY-UNCLEAR**. No claim that this formula was
scientifically open has been established.

Primary comparison:

1. Hietarinta's own 1997 account, §4.2, Eq. (37), was re-read. The exact
   dictionary to the approved class is
   `(x_H,y_H,t_H)=(x−c1 t,c3 t,y)`, `a_H=0`. Consequently
   `P=c3(D_xH^3+D_yH)` and `D_yP=c3 D_tH(D_xH^3+D_yH)`.
   This identifies the equation, not our full independent-amplitude family.
   His §4.2 states two seed types and a three-soliton search. The original
   1987 paper II has not been accessed in full. A pinned extracted copy of
   the primary 1997 account is `source/hietarinta-9708006.txt`
   (SHA-256 `982ef2dbcb3b6e4fca19c13e39c8e7f754ccd3d3591431e6809e345dceb39572`).
2. Peng et al. 2008 remains **abstract-only**. Fresh attempts at the publisher
   HTML/abstract/PDF routes returned HTTP 403; real Chromium stayed at an
   access challenge. The public Elsevier XML API returned metadata only.
   OpenAlex and Semantic Scholar report a closed article with no public
   full-text link; arXiv/title/coauthor/archive searches found no reachable
   copy. No credentials, paid access, or external contact were used.
   The concrete attempted URLs and outcomes are in
   `results/all_n_prior_art_access.json`.
3. Therefore no parameter dictionary to Peng's Wronskian family can be
   verified, and neither novelty nor a claim that Peng's theorem fails to cover
   this family is warranted. The all-N result here is proved independently
   from finite-dimensional Pfaffian identities, not imported from an unread
   theorem. Reading Peng's full text remains a bibliographic prerequisite for
   originality or exact family-equivalence claims, not a premise of C9.

The old finite checks and timeouts are retained as historical evidence.
The new path `code/all_n_pfaffian.py` reduces the cubic differential expression
to a four-border Pluecker identity without choosing N. Its supplemental exact
controls cover singular Pfaffian matrices, zero seed amplitudes, zero individual
wave numbers, both Hirota equations, and the diagonal reduction. None of those
finite controls is presented as the all-N proof.

Independent review of C9 completed with no mathematical findings requiring fixes:
`review/codex-all-n-review.md` (gpt-6.1-sol, max, read-only) concludes the all-N theorem
is correct with no remaining mathematical proof obligation in the approved scope.
This closes the **mathematical** target, not the Peng-family/novelty comparison.
Current scoped verdict: **SOLVED**, FRONTIER **DELIVERY-READY / NOVELTY-UNCLEAR**.
