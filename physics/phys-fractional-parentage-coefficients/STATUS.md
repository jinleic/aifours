# Status and state of the art (as of 2026-10-14, America/Los_Angeles)

Book problem: 母配分系数递推关系的破解 ("Solve the recurrence relation of the fractional
parentage coefficients"), Bao Chengguang (鲍诚光), *10000 Selected Problems in Sciences:
Physics*, Science Press 2009, pp. 348–349 (PDF pp. 381–382); excerpt in
[source/problem.zh.txt](source/problem.zh.txt).

Reading key: **[read]** = the primary text (PDF/HTML) was opened and the cited statement was
located; **[abstract]** = only the abstract/metadata page was read; **[secondary]** = known only
from a summary or a citing paper. A failed literature search does not show that a result does not
exist.

## 1. What the book asks, made precise

N identical spin-f bosons in one spatial mode (or the spin factor of a symmetric state) carry the
symmetric representation [N] of U(2f+1). Total-spin eigenstates |N; Γ L M⟩ are labelled by
L (total spin) and extra labels Γ. The **one-body CFP** is the coefficient in

  |N; Γ L M⟩ = Σ_{Γ' L'} ⟨N Γ L {| N−1 Γ' L'⟩ [χ(particle N) ⊗ |N−1; Γ' L'⟩]_{L M},

and two-body CFPs are defined in the same way with a coupled pair. The book says (i) no general
analytic formula exists; CFPs come from a recursion in N that becomes unmanageable for 10–1000
particles; (ii) only the spin-1 boson case has a closed form; (iii) other cases are "very hard".
"Cracking the recursion" therefore means a closed form valid for **all N**, with no step-by-step
recursion.

For spin f ≥ 2 the natural labels are seniority v (the irrep (v) of O(2f+1)) and an extra
multiplicity label α for repeated L inside (v): U(2f+1) ⊃ O(2f+1) ⊃ SO(3). **The missing label α is
the core difficulty.** For f = 2 (d-bosons, spin-2 condensates) the first multiplicity occurs at
v = 6, L = 6.

## 2. Settled results (primary sources)

| Result | Scope | Source |
|---|---|---|
| CFPs defined | atomic shells | R. F. Bacher, S. Goudsmit, *Atomic energy relations. I*, Phys. Rev. **46**, 948 (1934), doi:[10.1103/PhysRev.46.948](https://doi.org/10.1103/PhysRev.46.948) [secondary: book ref. 3] |
| Closed-form spin-1 (j = 1) boson CFPs, removing 1, 2, 3 or 4 particles, any N | spin 1, symmetric | Z. Marić, M. Popović-Božić, J. Phys. A **13**, 2881 (1980), doi:[10.1088/0305-4470/13/9/015](https://doi.org/10.1088/0305-4470/13/9/015) [abstract: "explicit functional dependence … for arbitrary values of N … simple algebraic functions of J and N"]. **This predates the book's reference [5].** |
| Spin-1 one-body CFP a_S^N = [(1+(−1)^{N−S})(N−S)(S+1)/(2N(2S+1))]^{1/2}, b_S^N analogous | spin 1, {N} | C. G. Bao, Z. B. Li, Phys. Rev. A **72**, 043614 (2005), [arXiv:cond-mat/0505204](https://arxiv.org/abs/cond-mat/0505204) [read, p. 2] |
| One- and two-body CFPs for {N} and {N−1,1} | spin 1 | C. G. Bao, Front. Phys. China **1**, 92 (2006), doi:[10.1007/s11467-005-0001-9](https://doi.org/10.1007/s11467-005-0001-9) [abstract] |
| CFP recursion with seniority; isoscalar factors via generalized Wigner–Eckart | identical bosons, single l | H. Z. Sun, M. Zhang, Q. Z. Han, G. L. Long, J. Phys. A **22**, 4769 (1989), doi:[10.1088/0305-4470/22/22/008](https://doi.org/10.1088/0305-4470/22/22/008) [abstract] |
| Seniority for bosons via the SU(1,1) quasi-spin algebra | any l | P. Van Isacker, S. Heinze, Ann. Phys. **349**, 73 (2014), [arXiv:1406.4094](https://arxiv.org/abs/1406.4094) [read: "seniority can be introduced via the quasi-spin formalism … SU(1,1) … for bosons"]; I. Talmi, *Simple Models of Complex Nuclei* (Harwood, 1993) [secondary] |
| Arbitrary-spin condensates: U(2f+1) ⊃ O(2f+1) ⊃ O(3) energies | any f | P. Van Isacker, S. Heinze, J. Phys. A **40**, 14811 (2007), [arXiv:0710.5481](https://arxiv.org/abs/0710.5481) [secondary, via scout] |
| Spin-2 eigenstates from pair and trio operators | spin 2 | M. Ueda, M. Koashi, Phys. Rev. A **65**, 063602 (2002), [arXiv:cond-mat/0203052](https://arxiv.org/abs/cond-mat/0203052) [abstract] |
| Missing label n_Δ ("number of zero-coupled triplets"); non-orthogonal basis | SO(5) ⊃ SO(3) | E. Chacón, M. Moshinsky, R. T. Sharp, J. Math. Phys. **17**, 668 (1976), doi:[10.1063/1.522961](https://doi.org/10.1063/1.522961) [abstract] |
| **Analytic** elementary SO(5) ⊃ SO(3) Wigner coefficients ⟨(τ0)L₁;(10)2‖(τ+1 0)L⟩ for L = 2τ+2−k, **k ≤ 6** (k = 6 has multiplicity 2, given in one chosen basis containing the quartic f(τ) = 32τ⁴−288τ³+1024τ²−1692τ+1065) | spin 2, top families | F. Pan, L. Bao, Y.-Z. Zhang, J. P. Draayer, Eur. Phys. J. Plus **129**, 169 (2014), [arXiv:1309.2654](https://arxiv.org/abs/1309.2654) [read: Tables III–IV and Sec. V] |
| Exact-arithmetic Gram–Schmidt construction; tables of SO(5) ⊃ SO(3) CG coefficients up to v = 50; a reordered basis gives "a different, equally valid, set" | spin 2, all (v, L), numerical/exact tables | M. A. Caprio, D. J. Rowe, T. A. Welsh, Comput. Phys. Commun. **180**, 1150 (2009), [arXiv:0902.0020](https://arxiv.org/abs/0902.0020) [read] |
| SO(5) ⊃ SO(3) spherical harmonics and basic coupling coefficients (algorithm) | spin 2 | D. J. Rowe, P. S. Turner, J. Repka, J. Math. Phys. **45**, 2761 (2004), doi:[10.1063/1.1763004](https://doi.org/10.1063/1.1763004) [abstract] |
| Orthonormal O(5) × SU(1,1) basis | spin 2 | S. Szpikowski, A. Góźdź, Nucl. Phys. A **340**, 76 (1980), doi:[10.1016/0375-9474(80)90323-1](https://doi.org/10.1016/0375-9474(80)90323-1) [abstract] |
| Spin-2 condensates with U(5) ⊃ SO(5) ⊃ SO(3) labels, **no CFPs** (Fock-basis numerics) | spin 2 | Y. Z. He, Y. M. Liu, C. G. Bao, Phys. Rev. A **91**, 033620 (2015), [arXiv:1501.03356](https://arxiv.org/abs/1501.03356) [secondary, via scout] |

## 3. What is open (primary statements, secondary reports, search results — kept separate)

* Pan, Bao, Zhang, Draayer (2014), end of Sec. IV and Sec. V [read]: "it seems that the orthonormalized
  expansion coefficients c̄(τ,k) can always be expressed by polynomials of τ. But the expression
  becomes much more complicated with increasing of k, especially for non-multiplicity-free cases."
  For general k they use a numerical algorithm. Coefficients in multiplicity cases "may be
  numerically different when they are derived by using different methods": they are defined only
  up to an SO(Multi) rotation.
* Caprio, Rowe, Welsh (2009), Sec. 3.3 [read]: a conjectured closed form for the general SO(5)
  reduced matrix element ⟨Ψ_{v3}‖Ψ_{v2}‖Ψ_{v1}⟩ "has not been proved in full generality". The
  closed form exists only for ⟨Ψ_{v±1}‖Ψ_1‖Ψ_v⟩, citing their ref. [3].
* *Secondary report.* He, Liu, Li, Bao, Phys. Scr. **97**, 045407 (2022),
  [arXiv:2112.07885](https://arxiv.org/abs/2112.07885) [secondary, via scout]: integer-spin systems
  with a singlet-pairing force; "f ≥ 4 remains to be further clarified". CFPs appear only formally.
* *Search result, not a primary statement.* In the sources we examined, we found no closed forms for
  (a) the low-total-spin ("bottom") spin-2 sector at arbitrary seniority, (b) a general-f family
  beyond f = 1, or (c) a multiplicity basis with Bao–Li-type closed forms. This does not prove that
  no such source exists, so the corresponding items in RESULTS.md are **NOVELTY-UNCLEAR**.

## 4. Baseline to beat

* N-dependence: the standard quasi-spin seniority reduction. Talmi and Van Isacker–Heinze give it
  for single-l bosons; it is solved in principle, but we found no explicit general-f
  one-body formula printed in the sources opened.
* Spin 2, structure in v: Pan et al. (2014) give analytic coefficients for **k ≤ 6** (top families,
  L = 2v − k). Caprio et al. (2009) give an exact algorithm and tables (v ≤ 50).
* Multiplicity: no canonical basis. In the sources examined, the only closed form for a
  multiplicity family is Pan et al.'s k = 6 basis, which contains an irreducible quartic f(τ).

## 5. What "not too hard" means here

The bounded obligations were concrete:
1. Prove the all-N factorization of one-body CFPs for every f. This needs only commutator
   algebra (quasi-spin).
2. Derive closed forms for infinite multiplicity-free families, as functions of v. This is finite
   symbolic algebra once states are written in v-independent "deficit" coordinates.
3. Decide whether the first spin-2 multiplicity families admit rational directions with
   Bao–Li-type CFPs. This is decidable by residues for a fixed finite set of permitted linear
   factors. The unrestricted question depends on rational points of hyperelliptic curves.

The full problem (closed forms for every (v, α, L), every f, and fermions) is **not** in this class.
For spin 2 a uniform formula needs a resolution of the SO(5) ⊃ SO(3) missing label. RESULTS §D
shows that in five two-dimensional families no rational direction gives Bao–Li-type forms with
linear factors from an explicit finite set. Spin-3/2 fermions (spin part with mixed permutation
symmetry, Sp(4) ≅ SO(5)) were not attacked.

## Approved scoped target (2026-10-14 continuation)

The user explicitly approved precise subproblems: E2's 24 squared-CFP formulas and two
block weights previously unproved in this project, spin 2 and parent L ≤ 5, for all admissible
seniorities. **This target is now SOLVED mathematically (RESULTS §I, Theorem E2-W).**
The angular-momentum moment identity, normalization and eleven harmonic principal-parent
anchors close a finite acyclic derivation; no larger seniority tables were needed.
Independent Codex review accepted the universal theorem and all boundary cases.
FRONTIER: **DELIVERY-READY** for correctness, **NOVELTY-UNCLEAR** for scientific priority.
Universal phase signs and resolution within multiple daughter blocks are not claimed.

### E2-specific prior-art check for the scoped continuation

Checked publicly on 2026-10-14, before asserting scientific novelty:

| Primary source opened | Exact comparison to E2 |
|---|---|
| M. A. Caprio, D. J. Rowe, T. A. Welsh, *Construction of SO(5)⊃SO(3) spherical harmonics and Clebsch–Gordan coefficients*, CPC 180, 1150 (2009), [arXiv:0902.0020](https://arxiv.org/abs/0902.0020) | Existing exact computational construction of the relevant coefficients; not evidence that a later symbolic low-L specialization is new. |
| F. Pan, L. Bao, Y.-Z. Zhang, J. P. Draayer, *Construction of basis vectors for symmetric irreducible representations of O(5)⊃O(3)*, EPJ Plus 129, 169 (2014), [arXiv:1309.2654](https://arxiv.org/abs/1309.2654), abstract and previously inspected Tables III–IV | The explicitly listed analytic series hold for fixed deficit k≤6, L=2τ+2−k. E2 instead holds at fixed small L and unbounded v (so k grows); overlapping small instances are not a proof of these towers. |
| T. A. Welsh / D. J. Rowe, public [SO(5)⊃SO(3) state-label page](https://www.physics.utoronto.ca/site-archive/rowe/taw/acm/so5/so5vlabels.html) and [spherical-harmonic page](https://www.physics.utoronto.ca/site-archive/rowe/taw/acm/so5/so5sh.html), updated 2014 | Explicit branching multiplicity formula and finite harmonic tables (e.g. L≤20, v≤45). Confirms the low-L multiplicity-free supports used in the proof; no universal E2 formula table was identified on these pages. |
| P. Van Isacker, *Boson Models with Interactions of Arbitrary Order*, [arXiv:2606.04055v1](https://arxiv.org/html/2606.04055v1), 2026, §II Eqs. (3), (8), (11)–(14) | Primary contemporary statement of the Redmond/Gram–Schmidt recursion and the general bosonic seniority reduction. Eq. (11) explicitly supplies the two standard N-dependent factors of our earlier Theorem A. The low-spin closure uses this established machinery; neither the parentage recurrence nor the seniority factorization is a discovery here. The inspected §II presents a recursive construction, not the exact 26-entry E2 table. |

Searches included `"SO(5)" "coefficients" "L=0" "L=2" analytical`,
`"d bosons" "fractional parentage" analytic seniority coefficients L`, and searches for
the exact low-spin factors. They did not identify a primary publication listing all E2
families. This is a dated, scoped search result, **not** proof of openness or novelty.
Older IBM books and the full historical literature have not been exhaustively compared.
The defensible wording is **a certified derivation using established recoupling identities;
publication novelty not cleared**. No new/first/best-known priority claim is made.

Additional historical limitation: T. Kishimoto and T. Tamura, *Coefficients of fractional
parentage of many-boson systems*, Nuclear Physics A **163**, 100–112 (1971),
doi:[10.1016/0375-9474(71)90523-9](https://doi.org/10.1016/0375-9474(71)90523-9),
was checked through the [INSPIRE metadata/abstract](https://inspirehep.net/api/literature/1438239).
Its abstract describes a compact calculation for many quadrupole phonons. Full text was not
retrieved (the DOI read returned metadata and public searches did not locate the paper).
It is therefore a material outstanding prior-art comparison, not a source we can rule out.
In particular, E2 was an unproved local conjecture before this continuation; its status as
an unsolved question in the worldwide literature was not certified.

## Openness gate (final, 2026-10-14)

**Gate verdict: NO-SETTLING-SOURCE-AMONG-CHECKED.**
This is **not** a pass of the user's “not solved yet” selection requirement: important
primary full texts remain inaccessible, so E2's prior-open status is **NOT CERTIFIED**.
The mathematical proof remains valid as a Certification of formulas previously unproved
in this project; neither scientific novelty nor a first solution of a literature-open
problem is claimed. No source found explicitly declares this exact E2 family open.

The exact comparison is spin-2/d-boson one-body CFP squared magnitudes and the two
L'=6 block weights, parent total spin L≤5, **every admissible seniority v**.
Finite tables, fixed deficit 2v−L, N-dependence at fixed v, and a general numerical
algorithm are not automatically a prior settlement of this exact symbolic family.

Access labels below distinguish actual reading from abstracts and failed retrieval.
“No” in the last column means **no settlement of the all-v E2 statement demonstrated
by the material actually inspected**. For an inaccessible paper it is not a claim
that the paper lacks a settling result.

| Requested primary source | Access level and lawful routes observed | Exact relation to E2 | Settles exact all-v E2? |
|---|---|---|---|
| T. Kishimoto, T. Tamura, *Coefficients of fractional parentage of many-boson systems*, Nucl. Phys. A **163**, 100–112 (1971), [doi:10.1016/0375-9474(71)90523-9](https://doi.org/10.1016/0375-9474(71)90523-9) | **Abstract** via INSPIRE; full text **inaccessible**. OpenAlex: closed, no repository full text or OA location. Publisher and CORE: HTTP 403. IA Scholar: verification barrier. Exact-title public searches found no lawful full-text copy. | Directly relevant: abstract promises compact CFP construction for many quadrupole phonons. Without the actual formulas, this paper cannot be excluded as prior art. | **No demonstrated settlement; undetermined.** |
| A. Arima, F. Iachello, *Interacting boson model of collective states I. The vibrational limit*, Ann. Phys. **99**, 253–317 (1976), [doi:10.1016/0003-4916(76)90097-X](https://doi.org/10.1016/0003-4916(76)90097-X) | **Abstract** via [Groningen's republication record](https://research.rug.nl/en/publications/interacting-boson-model-of-collective-states-i-the-vibrational-li/); full text **inaccessible**. Original publisher HTTP 403. Both original and 2000 republication [doi:10.1006/aphy.2000.6007](https://doi.org/10.1006/aphy.2000.6007) have no OpenAlex OA location; Groningen and Yale author pages supplied no PDF. | Analytic U(5) energies and electromagnetic transitions may contain equivalent d-boson matrix elements. Abstract-level coverage does not resolve the exact low-L/all-v question. | **No demonstrated settlement; undetermined.** |
| F. Iachello, A. Arima, *The Interacting Boson Model* (CUP, 1987), [doi:10.1017/CBO9780511895517](https://doi.org/10.1017/CBO9780511895517) | **Read, partial authorized Google Books preview**, especially [p.45](https://books.google.com/books?id=PXv_SRqDG_IC&pg=PA45) and [p.46](https://books.google.com/books?id=PXv_SRqDG_IC&pg=PA46). Full publisher chapter PDF redirected to the access/abstract page. Preview pp.27–28 unavailable. | Eq. (2.101) is the reduced d† matrix element. Table 2.9 is explicitly for both missing labels nΔ=nΔ'=0 and near-stretched L values such as 2n_d, 2n_d−2, 2n_d−3. These formulas overlap the already-known top families and small E2 instances, but do **not** display the fixed-low-L towers with unbounded trio count. Other unviewed book pages are not ruled out. | **No for the inspected table; complete-book comparison incomplete.** |
| D. R. Bès, *The γ-dependent part of the wave functions representing γ-unstable surface vibrations*, Nucl. Phys. **10**, 373 (1959), [doi:10.1016/0029-5582(59)90226-3](https://doi.org/10.1016/0029-5582(59)90226-3) | **Inaccessible** beyond bibliographic metadata. Publisher HTTP 403; public Elsevier text endpoint HTTP 400; OpenAlex closed/no repository full text. | Low-L SO(5) harmonics could yield the same coefficients by integration, but no formula-level equivalence was inspected. | **No demonstrated settlement; undetermined.** |
| S. Szpikowski, A. Góźdź, *The orthonormal basis for symmetric irreducible representations of O(5)×SU(1,1) and its application to the interacting boson model*, Nucl. Phys. A **340**, 76–92 (1980), [doi:10.1016/0375-9474(80)90323-1](https://doi.org/10.1016/0375-9474(80)90323-1) | **Abstract** for original; original full text **inaccessible** (publisher HTTP 403, OpenAlex no OA copy). The full [2015 coauthor retrospective at UMCS](https://bc.umcs.pl/Content/24834/PDF/czas16364_2015_70_2.pdf) was read, but is not a replacement for the original. | Original abstract promises an orthonormal physical basis and operator examples; the retrospective confirms the basis construction but does not supply the 26 E2 formulas. | **No demonstrated settlement; original undetermined.** |
| D. J. Rowe, P. S. Turner, J. Repka, *Spherical harmonics and basic coupling coefficients for the group SO(5) in an SO(3) basis*, JMP **45**, 2761–2784 (2004), [doi:10.1063/1.1763004](https://doi.org/10.1063/1.1763004) | **Abstract**; full text **inaccessible**. AIP's Crossref-linked PDF HTTP 403; [author publication page](https://www.physics.utoronto.ca/site-archive/rowe/research.html) links back to AIP, not an author-hosted copy. OpenAlex no OA location; arXiv title/author search found the 2009 successor only; an indexed CiteSeer route failed. | Abstract describes an algorithm and Appendix coupling tables. The Appendix was not read and cannot be excluded as a source of a relevant closed family. Public author data files are finite tables, not evidence of all-v product formulas. | **No demonstrated settlement; Appendix undetermined.** |
| O. Castaños, E. Chacón, A. Frank, M. Moshinsky, *Group theory of the interacting Boson model of the nucleus*, JMP **20**, 35–44 (1979), [doi:10.1063/1.523959](https://doi.org/10.1063/1.523959) | **Abstract** through INSPIRE and [UNAM's record](https://produccion.siia.unam.mx/Publicaciones/ProdCientif/PublicacionFrw.aspx?id=363490&scopus=0); full text **inaccessible**. AIP PDF and CORE HTTP 403; OpenAlex no OA location. | Abstract concerns Casimir matrix elements and transformation brackets, using programmed reduced O(5) symbols. That is relevant machinery, not an inspected all-v E2 table. | **No demonstrated settlement; full text undetermined.** |
| B. F. Bayman, A. Lande, *Tables of identical-particle fractional parentage coefficients*, Nucl. Phys. **77**, 1–80 (1966), [doi:10.1016/0029-5582(66)90677-8](https://doi.org/10.1016/0029-5582(66)90677-8) | **Abstract** read at [University of Minnesota](https://experts.umn.edu/en/publications/tables-of-identical-particle-fractional-parentage-coefficients/); full text **inaccessible**. Publisher HTTP 403; OpenAlex no OA location. | Abstract explicitly limits the d-boson tables to n≤7. This overlaps initial E2 instances but is not, by itself, the all-v symbolic assertion. The introduction's derivations remain uninspected. | **No for finite tabulation alone; full text undetermined.** |
| I. Talmi, *Simple Models of Complex Nuclei* (Harwood, 1993) | **Read, limited preview index/snippets only** in the authorized [Routledge reprint preview](https://books.google.com/books?id=LLY4DwAAQBAJ). Index p.1068 points to d-boson CFPs on **pp.763–771**. Direct preview requests for pp.763 and766 were unavailable; p.764 explicitly excluded. | These are precisely the important missing pages. General seniority snippets elsewhere do not establish whether low-L reduced d† matrix elements are given at arbitrary v. | **No demonstrated settlement; relevant pages inaccessible.** |

**Decisive inspected comparison.** The 1987 book, p.45, says the reduced matrix elements
have been evaluated in closed form “for a number of states.” Page 46's Table 2.9 explicitly
restricts both nΔ labels to zero. This confirms analytic prior art for the near-stretched
sector; it does not clear the all-v fixed-low-L E2 target. Authorized preview captures are
[page 45](source/openness-gate/ibm-1987-page45.webp) and
[page 46](source/openness-gate/ibm-1987-page46.webp).

**Explicit missing set:** full Kishimoto–Tamura 1971; Arima–Iachello 1976 (including its
2000 republication); Bès 1959; Szpikowski–Góźdź 1980; Rowe–Turner–Repka 2004, especially
its Appendix; Castaños et al. 1979; Bayman–Lande 1966; unviewed sections of Iachello–Arima
1987; and Talmi 1993 pp.763–771. No claim of absence or of prior openness is made from
these access failures. An [access audit](source/openness-gate/access-audit.json) records
the attempted publisher, OA-index, author/institutional, arXiv, CORE, IA Scholar and
Google Books routes. No shadow-library, login, paywall bypass or preview-limit evasion
was used. No mathematics or heavy verification was rerun in this gate check.

**Selection consequence:** retain E2-W as a correct **Certification** of statements
previously unproved in this project. Do **not** advertise it as a formerly open scientific
problem now solved, and do **not** count it as satisfying a certified “not solved yet”
selection gate. The gate remains blocked on the missing primary comparisons, despite
the completed mathematical proof.
