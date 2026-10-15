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

The user explicitly approved precise open subproblems. This continuation fixes E2's
24 unproved squared-CFP formulas and two block weights, spin 2 and parent L ≤ 5, for all
admissible seniorities. The baseline is the previously tabulated exact finite evidence plus
the established seniority/recoupling machinery; novelty requires a separate prior-art check.
The missing ingredient is a finite acyclic derivation of the low-spin one-body weights,
not larger seniority tables. Normalization and the angular-momentum moment identity may
close the principal-parent recursion without solving general missing-label blocks.

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
