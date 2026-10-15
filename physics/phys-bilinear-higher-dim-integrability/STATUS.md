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
| J. Hietarinta, "Introduction to the Hirota bilinear method", arXiv:[solv-int/9708006](https://arxiv.org/abs/solv-int/9708006), §4.2; related original paper II, *J. Math. Phys.* **28**, 2094–2101 (1987), doi:[10.1063/1.527421](https://doi.org/10.1063/1.527421) | The primary 1997 account explicitly rotates the odd-B formulation to two equations on the same pair, gives two seed types, and lists `(Dx^3+Dy)G·F=0`, `(Dt(Dx^3+Dy)+aDx^2)G·F=0` as Eq. (37). At a=0 this is the cubic equation studied here. Its cited sources include papers II/III (1987) and a 1990 chapter; attributing Eq. (37) specifically to paper II is not verified. | 1997 account read; 1987 II publisher abstract inspected through INSPIRE, original PDF inaccessible. The 1987 II abstract describes odd P1 with quadratic P2, not an inspected all-N C9 theorem. |
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
- The n = 3 model (iii) is, up to renaming t ↔ y, Hietarinta's mKdV-type pair (37) with a = 0 in the
  primary 1997 account, which lists it among three-soliton-compatible pairs; the abstract of Peng, Zhang, Gegenhasi &
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
Hietarinta's mKdV-type search as summarized in his primary 1997 account: among the five listed pairs,
only (37) has the shape `A=R·B` with R linear at a=0. The exact original search space and paper-level
attribution have not been checked in full. An unsuccessful search does not establish absence.

## 5. Baseline to beat

- Strongest positive evidence: three continuous-variable examples (`P = D_x D_t`, `D_t + D_x^2`,
  `D_t + D_x^3`, each with Q = D_x and R = D_y) and one supersymmetric example, verified by symmetry analysis;
  for `D_t + D_x^3` additionally the three-soliton result in Hietarinta's primary 1997 summary and, per Peng et al.'s abstract,
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

## Openness gate (final, 2026-10-14)

**Gate verdict: PARTIAL-OVERLAP.**

C9 was **previously unproved in this project**. We have not established that it was
previously open in the literature. Its equation and substantial soliton structure are
prior art; the exact arbitrary-independent-amplitude all-N family has not been matched
to, or excluded from, the inaccessible high-risk sources. Thus C9 remains a mathematically
proved **Certification**, but it is **not an accepted selection of a confirmed
currently-unsolved problem**. The reviewed proof and this failed openness certification
are distinct conclusions. Do not count it as a newly solved open physics problem.

In the following table, “settles?” means “settles the full C9 family on the material
actually inspected,” not whether the equation has ever been called integrable.
“No—uninspected” does not mean the original source lacks the result.

| Prior source | Access reached | Exact relation to C9 | Settles? |
|---|---|---|---|
| [Hietarinta, primary 1997 account](https://arxiv.org/abs/solv-int/9708006), §4.2, Eq. (37) | Read, pinned in `source/hietarinta-9708006.txt` | At `a_H=0`, `(x_H,y_H,t_H)=(x−c1t,c3t,y)` gives exactly C9's pair. The source describes two seed types and three-soliton compatibility, not an inspected all-N arbitrary-amplitude Pfaffian coefficient theorem. | **Partly**: equation and lower-N structure |
| [Hietarinta 1987 II](https://doi.org/10.1063/1.527421), JMP 28, 2094–2101; [publisher abstract via INSPIRE](https://inspirehep.net/api/literature/238832) | Abstract read; original inaccessible | The abstract searches odd P1 with quadratic P2. The 1997 summary's Eq. (37) has quartic second polynomial and cites 1987 II/III plus a 1990 chapter. Exact attribution to II alone is not verified. No inspected C9 all-N theorem. | **No—uninspected** full text |
| [Peng, Zhang, Gegenhasi & Liu 2008](https://doi.org/10.1016/j.physleta.2008.01.090), PLA 372, 4197–4204; [OSTI abstract](https://www.osti.gov/etdeweb/biblio/21171282) | Abstract and institutional bibliography read; full text inaccessible | Abstract reports Wronskian N-solitons and a proposed Lax representation for a Hietarinta mKdV-type equation. No verified seed/amplitude dictionary shows whether that theorem contains the entire C9 family. | **Partly** at claimed equation/soliton level; full family unresolved |
| [Gegenhasi, Hu & Wang 2007](https://doi.org/10.1016/j.physleta.2006.07.031), PLA 360, 439–447, “A (2+1)-dimensional sinh-Gordon equation and its Pfaffian generalization” | Metadata; original inaccessible; equation attribution checked in the primary 2023 follow-up below | The attributed base pair is `P2=Dy+Dx²`, `P2F·G=0`, `[DtP2+2Dx]F·G=0`, not C9's cubic zero-remainder pair. The original Pfaffian generalization's full range remains uninspected. | **No** direct matching theorem inspected; original scope unresolved |
| [Wang, Yu & Zhu 2023](https://doi.org/10.1007/s44198-023-00147-z), JNMP 30, 1621–1640, Eq. (5), Theorem 1 | Publisher OA text read (introduction, equation and theorem) | An all-N Gram determinant theorem for the preceding quadratic pair with nonzero `2Dx` remainder. It explicitly attributes its bilinear form and earlier Pfaffian generalization to Gegenhasi–Hu–Wang. No C9 parameter dictionary or limiting reduction is established here. | **No**: inspected theorem has different pair |
| [Gegenhasi & Tam 2006](https://doi.org/10.1016/j.chaos.2005.08.084), “A pfaffian solution to the modified discrete BKP equation”; [HKBU institutional record](https://scholars.hkbu.edu.hk/en/publications/a-pfaffian-solution-to-the-modified-discrete-bkp-equation/) | Institutional abstract read; no manuscript link | General Pfaffian-method overlap; the record concerns modified discrete BKP. Without its full formula and a continuum/coefficient dictionary, it neither certifies C9 as prior art nor can safely be dismissed as unrelated. | **No—uninspected** full text |
| [Hu & Tam 2001](https://doi.org/10.2991/jnmp.2001.8.s.26), “Some Recent Results on Integrable Bilinear Equations” | Publisher abstract/reference page read | Describes coupled differential-difference lattices and an extended Lotka–Volterra system. The inspected abstract does not state the C9 family. | **No** settling theorem inspected |
| Li–Lou 2008, full text already read, §4 question (7) | Read | Asks about **other n beyond 2 and 3**. Its quoted “not yet found other integrable systems” does not assert that the cubic n=3 all-N formula was open. The book's broader conjecture is also not an explicit openness assertion for C9. | **No** explicit primary-open statement for C9 |

### Fresh legitimate access attempts

- **Unpaywall:** the requested
  [API URL](https://api.unpaywall.org/v2/10.1016/j.physleta.2008.01.090?email=research@example.com)
  returned HTTP 422, “Please use your own email address in API calls.” No user email or
  invented substitute identity was supplied.
- **CORE:** [exact-title search](https://core.ac.uk/search?q=%22On%20integrability%22%20%22MKdV%22)
  returned 403; normal Chromium remained at its access challenge.
- **Internet Archive Scholar:** normal browser verification succeeded. Searches for the
  exact Peng DOI, `title:"On integrability of a" AND title:MKdV`, and the exact
  Gegenhasi–Hu–Wang title each returned **0 hits**. Broad text matches were unrelated.
  This is a search result, not proof that no archived copy exists.
- **Google Scholar/all-versions discovery:** the exact-title search returned HTTP 403,
  so no version cluster was reachable.
- **Author/institutional routes:** [Q.P. Liu's CUMTB page](https://lxy.cumtb.edu.cn/info/1067/1238.htm)
  lists Peng2008 as entry 65, but the inspected HTML has no manuscript/PDF link.
  [Gegenhasi's IMU profile](https://math.imu.edu.cn/info/1035/2038.htm), including its raw
  page content, has no individual paper links. [Hu's ICMSEC profile](https://icmsec.cc.ac.cn/en/article/5/18.html?zc=36)
  and its linked homepage did not expose the target manuscripts.
- **Hietarinta original:** [author bilinear-method archive](https://users.utu.fi/hietarin/home/hirotas-bilinear-method/)
  links paper II only through DOI. The Crossref-linked
  [AIP PDF](https://pubs.aip.org/aip/jmp/article-pdf/28/9/2094/8157151/2094_1_online.pdf)
  returned 403; INSPIRE has the report number `TURKU-FTL-R115` but no document attachment.
  The author-hosted 2008 Bangalore lecture is accessible and again describes the
  seed types/search; it does not supply an inspected C9 all-N formula.
- **Alternative arXiv author searches:** `au:Gegenhasi` returned `nlin/0604066`
  (discrete Davey–Stewartson) and `2006.03943` (nonlocal discrete derivative NLS).
  `au:Liu_Q_P` restricted to 2007–2008 returned `0809.0947` (N=2 supersymmetric KdV)
  and `0802.4011` (supersymmetric Sawada–Kotera), not Peng2008.
- **Hu/Gegenhasi corpus:** Crossref and OpenAlex author searches over 2000–2011 located
  sinh-Gordon Pfaffian, modified discrete KP/BKP, Toda and three-wave papers.
  No separate inspected all-N continuous cubic family theorem was obtained. This
  metadata search does not rule out a broader hierarchy theorem containing C9.

No shadow-library access, login, paywall circumvention, paid access or external contact
was used. The machine-readable gate record is `results/openness-gate-20261014.json`.
The next decisive prerequisite is the full Peng2008 and relevant Hu-school formula,
followed by an explicit amplitude/phase dictionary—not another numerical replay.
