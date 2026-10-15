# Results — closed forms and obstructions for spinor-boson CFPs (2026-10-14)

Evidence labels follow `docs/knowledge-system/FRONTIER_METHOD.md`. **Certification** means a
checkable proof. Proofs marked *computer-assisted* consist of exact rational-function algebra in
sympy, with every step reproducible by the stated command. **Reproduction** means a known result
re-derived independently. **Empirical evidence** means exact checks on finitely many cases.
Novelty is reported separately (see STATUS.md). `$PY` =
`/Users/jinleic/jinleic-workspace/scratch/ai4s-venvs/phys-fractional-parentage-coefficients/bin/python`;
commands are run from this folder with `cd code` (output paths are relative to `code/`).

## 0. Conventions

* Spin f, D = 2f+1, bosons a_m (m = −f..f), Condon–Shortley phases. Pair operator
  P† = Σ_m (−1)^m a†_m a†_{−m}; [P, P†] = 4N̂ + 2D. The seniority-v states are the harmonic
  (Pψ = 0) states. |N v α L M⟩ = (P†)^n h_{vαLM}/‖·‖ with N = v + 2n and h harmonic of degree v.
  All harmonic bases are taken **real** (rational polynomial coefficients, as in the code). The
  signed formulas below assume this; for complex phases, replace r by its conjugate and squares
  by |·|².
* One-body CFP: |N; vαL M⟩ = Σ c(NvαL; N−1 v'α'L') [χ(N) ⊗ |N−1; v'α'L'⟩]_{LM}, with the particle
  coupled first, ⟨f m; L' M'|L M⟩. In second quantization,
  c = ⟨N vαL L| a†_μ |N−1 v'α'L' L'⟩ / (√N ⟨f μ; L' L'|L L⟩), μ = L − L'. The reduced CFP is
  r(vαL; v−1 α'L') := c at N = v, so Σ_{α'L'} r² = 1.
* Spin 2: α is the Chacón–Moshinsky–Sharp label e = n_Δ (number of SO(3)-scalar trios), with
  λ = v − 3e. Basis states are harmonic projections of covariant monomials f^a H^b T^c j^e of the
  binary quartic. Here f = a†_2, H is the spin-2 pair, T the spin-3 trio and j the scalar trio,
  with a = L − λ, c = (2λ − L) mod 2 and b = (2λ − L − 3c)/2. In a multiplicity block they are
  Gram–Schmidt orthonormalized, either "asc" (e = 0 first; compare Caprio–Rowe–Welsh, who
  orthonormalize their monomials in order of increasing t — we did not check that their monomials
  coincide with ours) or
  "desc" (most trios first). Squared CFPs between multiplicity-free states do not depend on these
  conventions.

## Claims at a glance

| ID | Claim | Label | Novelty | Verify |
|---|---|---|---|---|
| A | All-N seniority factorization of one-body CFPs, any spin f ≥ 1, N ≥ 1, explicit formulas and sign rule (real bases) | Certification (proof §A) + exact checks f ≤ 4 | standard quasi-spin consequence; general-f formula not found printed (no priority claimed) | `$PY check_seniority_factorization.py 30` |
| A1 | Spin-1 Bao–Li formula = case f = 1 of A | Reproduction | known (Marić & Popović-Božić 1980; Bao & Li 2005) | same |
| B | Near-stretched states of **any** spin f ≥ 2 (L = fv − 2, fv − 3): the five reduced CFPs (v → v−1 branch, hence all N for that branch) | Certification (computer-assisted symbolic proof; hand derivation of one case) | f = 2 case known (Pan et al. 2014); general f NOVELTY-UNCLEAR | `$PY top_family_symbolic.py general 3`; `$PY check_general_f.py` |
| B' | First multiplicity family of **any** spin f ≥ 3 (L = fv − 4, two states): all ten reduced CFPs (v → v−1) of Bao–Li type in the pair-first basis | Certification (computer-assisted symbolic proof) + 150 exact numeric checks | NOVELTY-UNCLEAR | `$PY check_general_f.py`; `$PY general_f_k4.py` |
| C | Spin 2, top families L = 2v − k, k ≤ 8 (multiplicity 2 for k = 6, 8): every **squared** reduced CFP, with its sign, as an explicit rational function of v on v ≥ max(k, k'+1), in two specified Gram–Schmidt bases | Certification (computer-assisted) + Reproduction of Pan et al. Table III (14/14) and Table IV (8/8 multiplicity-free rows) | k ≤ 6 known; k = 7, 8 and the trio-first k = 6 basis NOVELTY-UNCLEAR | `$PY top_family_symbolic.py 2 8 ../results/spin2_r_table_v22.json asc` (and `… v18_desc.json desc`); `$PY compare_pan2014.py` |
| D | **Bounded obstruction:** in the spin-2 multiplicity-2 families k ∈ {6, 8, 9, 10, 11}, no rational direction x ∈ Q(v)⊗V_k has a nonzero CFP into a multiplicity-free daughter of Bao–Li type with linear factors from the explicit finite set T (all 4v − n, \|n\| ≤ 10⁶, and small-height roots). For k = 6 the trio-first basis attains one irreducible quadratic factor | Certification (exact algebra + finite search; scope in §D) | NOVELTY-UNCLEAR (not found) | `$PY multiplicity_obstruction.py 6`; `$PY brauer_residues.py k 30` |
| E1 | Weight of a scalar parent, any f: Σ_α \|c(v α L=f; v−1, L'=0)\|² = (2v+D−2)(v+D−3)/(Dv(2v+D−4)) | Certification (proof §E) + exact checks | NOVELTY-UNCLEAR | `$PY check_general_f.py` |
| E2 | Spin 2, low-spin sector L ≤ 5, **arbitrary** seniority: 26 product formulas, 24 of them unproved, plus two block weights | Empirical evidence (742 exact CFP checks and 58 block checks, v ≤ 88); **conjecture** | NOVELTY-UNCLEAR | `$PY verify_bottom_conjectures.py ../results/spin2_r_table_v88_L5.json` |
| F | Engine validation: first-quantized recomputation, null-space multiplicities, operator algebra | Exact validation on the stated cases (not a proof of the implementation) | — | `$PY selftest.py`; `$PY verify_first_quantized.py` |
| G | Two-body CFPs from one-body ones by the chain (recoupling) formula, with signs | Reproduction of a standard formula; exact first-quantized check | standard (no novelty) | `$PY verify_two_body.py` |

---

## A. Theorem A — the N-recursion is solved for every spin f

**Theorem A.** Let f ≥ 1, D = 2f+1, N ≥ 1, N = v + 2n, and let |N vαL⟩, |N−1 v'α'L'⟩ be built as in
§0 from real orthonormal harmonic states. Then c = 0 unless v' = v ± 1. A branch whose daughter
seniority does not exist (v−1 < 0, or v+1 > N−1) is absent. Otherwise

  c(N vαL; N−1, v−1, α'L') = √[ v(N+v+D−2) / (N(2v+D−2)) ] · r(vαL; v−1 α'L'),

  c(N vαL; N−1, v+1, α'L') = (−1)^{L+L'} √[ (N−v)(v+D−2) / (N(2v+D−2)) ]
          · √[ dim_v (2L'+1) / (dim_{v+1}(2L+1)) ] · r(v+1 α'L'; vαL),

where dim_v = (2v+D−2)(v+D−3)!/(v!(D−2)!) is the dimension of the O(D) irrep (v).

*Proof.* (i) P(P†)^n h = 4n(v + D/2 + n − 1)(P†)^{n−1}h for harmonic h of degree v (induction
on n with [P,P†] = 4N̂+2D). Hence ‖(P†)^n h‖² = c_{n,v}‖h‖², c_{n,v} = Π_{k=1}^{n} 4k(v+D/2+k−1).
States with different v are orthogonal (eigenvectors of P†P with distinct eigenvalues).
(ii) Write Φ = [a† ⊗ h']_{LM} for harmonic h' of degree v−1. Then PΦ = 2[ã ⊗ h']_{LM} with
ã_m = (−1)^m a_{−m}, using [P, a†_m] = 2(−1)^m a_{−m}. This vector is harmonic, so
Φ = h_v + P†g with g = [ã⊗h']/(2v+D−4) and h_v harmonic of degree v.
(iii) v' = v−1: [a† ⊗ (P†)^n h'] = (P†)^n Φ, because a† commutes with P†. Only (P†)^n h_v overlaps
the parent, so c = N^{−1/2} √(c_{n,v}/c_{n,v−1}) ⟨h|Φ⟩. Telescoping gives
c_{n,v}/c_{n,v−1} = (N+v+D−2)/(2v+D−2), and ⟨h|Φ⟩ = √v·r.
(iv) v' = v+1: the daughter is (P†)^{n−1}h''/√c_{n−1,v+1} with h'' harmonic of degree v+1. By (ii),
[a† ⊗ h''] = h_{v+2} + P†[ã ⊗ h'']/(2v+D), and only the second term overlaps (P†)^n h. Hence
c = N^{−1/2} c_{n,v}/√(c_{n,v} c_{n−1,v+1}) · ⟨h|[ã⊗h'']_L⟩/(2v+D), with
c_{n,v}/c_{n−1,v+1} = 2n(2v+D). The CG identity
⟨f −m; L L|L' L−m⟩ = (−1)^{m+L'−L} √((2L'+1)/(2L+1)) ⟨f m; L' L−m|L L⟩ gives
⟨h|[ã⊗h'']_L⟩ = (−1)^{L'−L} √((2L'+1)/(2L+1)) √(v+1) r(v+1 α'L'; vαL). Collecting factors gives
c² = (N−v)(v+1)(2L'+1) r²/(N(2v+D)(2L+1)). This equals the stated form because
dim_v/dim_{v+1} = (v+1)(2v+D−2)/((2v+D)(v+D−2)). ∎

All N-dependence is therefore closed-form. The whole problem reduces to the N-independent
O(2f+1) ⊃ SO(3) isoscalar factors r at N = v.

**Corollary A1 (f = 1, Bao–Li).** For f = 1 the irrep (v) of O(3) is spin L = v. There is one
daughter, r = 1, and the dimension ratio is 1. Theorem A gives a_S² = (N−S)(S+1)/(N(2S+1)) and
b_S² = (N+S+1)S/(N(2S+1)). In our pair-operator phase the S+1 branch has sign (−1)^{L+L'} = −1.
With the Clebsch–Gordan singlet pair Σ(−1)^{f−m}a†_m a†_{−m}, as used by Bao & Li, both are positive.

*Verification (ran):* `cd code && $PY check_seniority_factorization.py 30` printed
`spin-1 Bao-Li closed form: 465 CFPs equal exactly (N <= 30)` and, for f = 1, 2, 3, 4 with
N ≤ 16, 12, 9, 7: `Theorem A verified exactly for all 81 / 358 / 594 / 566 seniority states …
136 / 4492 / 21513 / 26349 CFPs, completeness sum = 1; sign rule (-1)^(L+L') holds for 15 / 519 /
3124 / 3653 v+1 couplings`.

## B. Theorem B — near-stretched states of any spin f ≥ 2

Write a highest-weight state of degree v and S_z = fv − k in "deficit" coordinates
z_f^{v−|d|} Π_j z_{f−j}^{d_j}, with Σ_j j d_j = k. Here z_m creates the unnormalized orbital u^{f+m}v^{f−m},
so its Fock weight is w_{f−j} = 1/binom(2f, j). In these coordinates
S₊ z_{f−j} = j z_{f−j+1} does not depend on v or f. For k < 2f the pair operator P lowers the
deficit by 2f, so every such state is harmonic with seniority v. The highest-weight space has
dimension p(k) − p(k−1) (partition numbers): 1 for k = 2 and k = 3. The states are
ψ₂ = z_f^{v−1}z_{f−2} − z_f^{v−2}z_{f−1}² and
ψ₃ = z_f^{v−1}z_{f−3} − 3z_f^{v−2}z_{f−1}z_{f−2} + 2z_f^{v−3}z_{f−1}³.

**Theorem B.** For every integer spin f ≥ 2, with parent spin L = fv − k and daughter spin
L' = f(v−1) − k', the following hold for v ≥ 2, 3, 3, 3, 4 (rows in order):

| k → k' | r² | sign |
|---|---|---|
| 2 → 0 | 2(fv−1) / (v(2fv−2f−1)) = 2(L+1)/(v(2L'−1)) | + |
| 2 → 2 | (v−2)(2fv−1) / (v(2fv−2f−1)) = (v−2)(2L+3)/(v(2L'+3)) | + |
| 3 → 0 | f(v−2)(2fv−3) / (v(fv−f−1)(2fv−2f−1)) = f(v−2)(2L+3)/(v(L'−1)(2L'−1)) | − |
| 3 → 2 | 6(f−1)(fv−1) / (v(fv−f−2)(2fv−2f−1)) = 6(f−1)(L+2)/(vL'(2L'+3)) | + |
| 3 → 3 | (v−3)(fv−2)(fv−1) / (v(fv−f−2)(fv−f−1)) = (v−3)(L+1)(L+2)/(v(L'+1)(L'+2)) | + |

Signs use the phase "coefficient of the largest single deficit positive". With Theorem A these
give the **v → v−1 branch** of the one-body CFPs of these states for all N, in Bao–Li form. The
**v → v+1 branch** at N > v is not covered. It needs the reverse coefficients r(v+1 α'L'; vαL),
whose parent families have deficit up to k + 2f, and these can contain irreducible non-linear
factors. Example (spin 2, Codex review): k = 2 parent, N = v+2, trio-first daughter of seniority
v+1 and deficit 6: c² = 294(4v−1)/((v+2)(2v+3)(2v+5)(18v²+127v−81)), v ≥ 5. For spin 2 the
reverse coefficients of the top families k ≤ 4 lie inside Claim C (deficits ≤ 8), so all branches
are explicit there, but not all are of Bao–Li type.

*Proof (computer-assisted).* The states ψ₂ and ψ₃ follow from S₊ψ = 0 (shown above). Every CFP is
a finite sum over at most three monomials with Fock weights (v−|d|)! Π d_j! w_{f−j}^{d_j}. The CG
coefficient of the stretched state is ⟨f μ; L' L'|L L⟩² = Π_{i<j}(2L'−i)/(2L+2+i) with
j = f − μ = k − k'. All ratios of factorials have fixed integer offsets, so each r² is an exact
rational function of (v, f). `top_family_symbolic.py general 3` performs this algebra.

*Hand check of 2 → 0.* X = ⟨ψ₂, z_{f−2}z_f^{v−1}⟩ = (v−1)! w_{f−2}, ‖ψ₂‖² = (v−2)!(2fv−1)/(2f²(2f−1)),
‖z_f^{v−1}‖² = (v−1)!, w_{f−2} = 1/(f(2f−1)) and CG² = (2fv−2f)(2fv−2f−1)/((2fv−2)(2fv−1)).
Then r² = X²/(w_{f−2}‖ψ₂‖²‖φ‖² v CG²) = 2(fv−1)/(v(2fv−2f−1)), as stated.

*Verification (ran):* `$PY top_family_symbolic.py general 3` printed the table above.
`$PY check_general_f.py` printed `Theorem B formulas agree exactly (with signs) with the
polynomial engine: 200 checks, f = 2..6, v <= 10`. That engine is a separate implementation: full
monomial spaces with a null-space computation.
*Scope:* k = 2, 3. The case k = 4 is the first multiplicity family for f ≥ 3; it is treated in
Theorem B' below.

### Theorem B' — the first multiplicity family of every spin f ≥ 3 has Bao–Li-type closed forms

For f ≥ 3 the states with L = fv − 4 form a two-dimensional space, and both have seniority v
(P lowers the deficit by 2f > 4). Let Q4 and H2 be the degree-2 highest-weight pairs of spin
2f − 4 and 2f − 2. The **pair-first basis** is the Gram–Schmidt basis of
φ_A = z_f^{v−2}Q4, followed by φ_B = z_f^{v−4}H2². Set g(v) = f(2f−1)v + 3(4f²−10f+5) and
g⁻ = g(v−1). Daughters k' = 4 use the same rule at v − 1. For every integer f ≥ 3 and v ≥ 5:

| parent → daughter | r² | sign |
|---|---|---|
| 1 → k'=0 | (2f−1)(fv−3)(fv−2)(2fv−5)(2fv−3) / (v(fv−f−1)(2fv−2f−3)(2fv−2f−1) g) | + |
| 1 → k'=2 | 12f(f−1)(2f−3)(v−2)(fv−3)(2fv−5) / (v(fv−f−2)(2fv−2f−5)(2fv−2f−1) g) | + |
| 1 → k'=3 | 2f²(2f−3)(2f−1)(v−3)(v−2)(fv−3) / (v(fv−f−3)(fv−f−2)(fv−f−1) g) | + |
| 1 → k'=4, 1 | (v−2) g / (v g⁻) | + |
| 1 → k'=4, 2 | 12f⁴(f−1)(2f−3)(2f−1)(v−4)(v−3)(v−2) / (v(fv−f−3)(2fv−2f−5)(2fv−2f−3) g⁻ g) | − |
| 2 → k'=0 | 12f²(f−1)(2f−3)(v−3)(v−2)(fv−2) / (v(fv−f−1)(2fv−2f−3)(2fv−2f−1) g) | − |
| 2 → k'=2 | 4f(2f−1)(v−3)(2fv−3)(fv+2f−5)² / (v(fv−f−2)(2fv−2f−5)(2fv−2f−1) g) | + |
| 2 → k'=3 | 24(f−1)³(2fv−5)(2fv−3) / (v(fv−f−3)(fv−f−2)(fv−f−1) g) | − |
| 2 → k'=4, 1 | 0 | |
| 2 → k'=4, 2 | (v−4)(fv−3)(2fv−5)(2fv−3) g⁻ / (v(fv−f−3)(2fv−2f−5)(2fv−2f−3) g) | + |

Every factor is linear in v, so for each fixed f all ten CFPs are of Bao–Li type, and the two rows
sum to 1 exactly. Together with Theorem A this gives the v → v−1 branch for all N. The v → v+1
branch needs reverse coefficients, as explained after Theorem B. This **contrasts with spin 2**
(Theorem D): there the first multiplicity family (k = 6) admits no Bao–Li-type rational direction
with linear factors in T. The pair state Q4 here has spin 2f−4 > 0 and is harmonic; for f = 2 it
would be the SO(5)-invariant pair, and the spin-2 multiplicity enters instead through the scalar
trio j.
*Proof (computer-assisted):* the same exact symbolic algebra in (v, f) as for Theorem B
(`top_family_symbolic.run_general_k4`; completeness checked symbolically). All overlaps X have
factors that are manifestly positive for v ≥ 5, f ≥ 3, so the signs hold on the whole range.
*Ran:* `$PY check_general_f.py` printed `Theorem B' (k = 4, pair-first basis) agrees exactly (with
signs; completeness = 1): 150 CFPs, f = 3, 4, 5, v = 5..9`, against the independent polynomial
engine. For f = 3, 4, 5 the script `general_f_k4.py` confirms the square-class picture:
q(φ_A) is linear in v, Δ is a product of linear factors, and the residue search finds solutions.
*Novelty:* NOVELTY-UNCLEAR. We found no general-f CFP closed forms in the literature checked.

## C. Spin 2: top families L = 2v − k, k ≤ 8, as rational functions of v

The deficit method of §B is extended with the harmonic projection
H(φ) = Σ_i β_i (P†)^i P^i φ, β_i = (−1)^i/(2^i i! Π_{l≤i}(D+2v−2−2l)). P acts on the implicit z₂
power through a factor v − |d|. The covariant monomial H^b T^c j^e is fixed in deficit coordinates,
and f^a only fixes the degree. The basis vectors are checked symbolically: S₊ψ = 0 and Pψ = 0
identically in v. Integer roots of the norms, of the CG factors and of the overlaps are checked so
that no excluded v lies in the stated range. **What is certified:** r² (a rational function of v)
and the sign of r, for v ≥ max(k, k'+1), in the two specified Gram–Schmidt bases ("asc", "desc").
These bases are conventions, not intrinsically canonical. r itself is in general algebraic, a
square root. Below this range the multiplicities can drop; for example, at v = 3 the k = 6 family
consists of the single scalar state. Small v are covered by the exact tables, not by the formulas.

* **k ≤ 5 (multiplicity-free).** All 14 transitions are products of linear factors, for example
  r²(k=4→4) = (v−4)(2v−3)(2v−1)(4v−5)(4v−3)/(v(2v−5)(2v+1)(4v−9)(4v−7)). The full list is in
  [results/spin2_top_families_k8_asc.txt](results/spin2_top_families_k8_asc.txt). **Reproduction:**
  with τ = v − 1, all 14 nonzero squared entries of Table III of Pan, Bao, Zhang, Draayer (2014)
  are reproduced exactly; signs differ by phase convention.
* **k = 6 (multiplicity 2).** In the asc basis the formulas contain the irreducible quartic
  128v⁴−1376v³+5608v²−10042v+6465 = 2304(2v+1)·q(φ₀). The basis-independent total parentage
  weight into the k' = 2 daughter is Q_{dd} = 3·F(v)/(v(v−2)(2v−5)(2v+1)(4v−11)(4v−9)) with
  F(v) = 32v⁴−288v³+1024v²−1692v+1065. F(τ+1) is exactly Pan et al.'s f(τ+1). Their Table IV
  basis is the **principal-parent basis of the k' = 2 daughter** (χ = 2) and its orthogonal
  complement (χ = 1). All 8 multiplicity-free rows of their Table IV are **reproduced exactly**
  from basis-independent data (`$PY compare_pan2014.py`: `Table III: 14/14 squared entries
  reproduced exactly; Table IV (multiplicity-free rows): 8/8 reproduced`). In the
  **trio-first (desc) basis** every k = 6 CFP into a multiplicity-free daughter
  has the form (rational)²·(product of linear factors)/q₂(v), with the **irreducible quadratic**
  q₂(v) = 18v²+91v−190. For example
  r²(k=6, e=1 → k'=2) = 147(4v−7)(4v−5)/(v(2v+1)(4v−11)q₂(v)) and
  r²(k=6, e=0 → k'=5) = 300(v−2)(4v−9)(4v−7)(4v−5)/(v(v−3)(2v−7)(2v−5)(4v−11)q₂(v)).
  CFPs into the two-dimensional daughter block contain q₂(v) and q₂(v−1) = 18v²+55v−263.
  The full list is in [results/spin2_top_families_k8_desc.txt](results/spin2_top_families_k8_desc.txt).
* **k = 7 (multiplicity-free), k = 8 (multiplicity 2).** The formulas are in the same files. In the
  trio-first basis the k = 8 forms contain the irreducible cubic 36v³+620v²−2517v+2023 and its shift.

*Verification (ran):* `$PY top_family_symbolic.py 2 8 ../results/spin2_r_table_v22.json asc`
printed `cross-check vs exact numeric table: 769 (v, family) values agree exactly`.
`$PY spin2_tables.py 18 - desc` followed by
`$PY top_family_symbolic.py 2 8 ../results/spin2_r_table_v18_desc.json desc` printed
`585 (v, family) values agree exactly`. The tables come from the independent polynomial engine.

## D. Theorem D — a bounded no-go for Bao–Li-type CFPs in spin-2 multiplicity families

Setting: let V_k be the two-dimensional Q(v)-space of seniority-v, spin-(2v−k) highest-weight
states for spin 2, with k ∈ {6, 8, 9, 10, 11} and v > k. It is spanned by the rational polynomials
φ₀, φ₁, the projected covariants with e = 0, 1. All objects below are those computed by the code.
With the unnormalized rational daughter y_d of a multiplicity-free daughter d (deficit k') and
μ = (2v−k) − (2(v−1)−k'), define

  q(x) = ⟨x, x⟩_F/(v−k)!,  b_d(x) = ⟨x, z_μ y_d⟩_F/(v−k)!,  n_d = ⟨y_d, y_d⟩_F/(v−1−k')!,
  C_d = [(v−k)!/(v−1−k')!] / (w_μ n_d v CG²).

These are rational functions of v for rational x. The physical state of a rational **direction**
x is x/‖x‖, and its CFP satisfies c(x/‖x‖; d)² = b_d(x)² C_d / q(x). The normalization ‖x‖ is in
general a square root; this is allowed. The script factors C_d exactly; **every C_d is a product of
linear factors with roots in ¼Z**.

Call c² **Bao–Li type over T** (T ⊂ Q) if c² = R(v)²·κ·Π_{t∈T}(v−t)^{n_t} with R ∈ Q(v), κ ∈ Q*
and n_t ∈ Z. Take T = {n/4 : |n| ≤ 10⁶} ∪ {p/q : |p/q| ≤ 30, 1 ≤ q ≤ 30}. In the spin-2 formulas
of §C and of Pan et al., every linear factor of odd multiplicity has its root in ¼Z ⊂ T. This is
**not** claimed for general-f formulas, whose roots depend on f.

**Theorem D.** Let k ∈ {6, 8, 9, 10, 11}. For every nonzero rational direction x ∈ V_k and every
multiplicity-free daughter d with b_d(x) ≠ 0, c(x/‖x‖; d)² is **not** Bao–Li type over T.
Equivalently, q represents no element of L_T = Q*·⟨v−t : t ∈ T⟩ modulo squares. Consequently,
for every orthogonal
pair of rational directions (x₁, x₂), some nonzero CFP of x₁/‖x₁‖ or x₂/‖x₂‖ into a
multiplicity-free daughter is not of Bao–Li type over T. For k = 6 the trio-first basis of §C
**attains one irreducible quadratic factor**: each of its CFPs into the multiplicity-free daughters
has square class (linear factors)·q₂(v), with q₂ = 18v²+91v−190 irreducible (discriminant 21961
is not a square). Within the class of rational directions whose norms have odd linear support in T,
this is minimal: some non-linear factor is unavoidable, and non-linear means degree ≥ 2.
Unrestricted minimality is not claimed.

*Proof.* Since C_d ∈ L_T·K*² and b_d(x)² is a square, c² is Bao–Li type over T iff q(x) ∈ L_T·K*².
Hence such an x exists iff q represents an element of L_T. Diagonalizing,
q ≅ ⟨q₁₁, Δ/q₁₁⟩ ≅ ⟨q₁₁, q₁₁Δ⟩ with q₁₁ = q(φ₁) and Δ = det G. Then q represents c iff
⟨1, Δ, −cq₁₁⟩ is isotropic, iff the quaternion algebra (cq₁₁, −Δ) splits over K = Q(v). A
necessary condition is that every residue (tame symbol) vanishes.
(1) *Non-linear places.* Δ has only linear factors. For each irreducible non-linear π dividing q₁₁
to odd order, the residue is −Δ mod π. It is a square in Q[v]/(π) in every case. For quadratic π
this is decided by an explicit square root in Q(√disc π); for cubic π, by a resultant
factorization g(t)g(−t) with g irreducible of prime degree. So these places impose no condition.
(2) *Rational places.* Tame symbols {x, y} = (−1)^{ab} u^b w^{−a} are bimultiplicative. So the
residues of (c₀Π_{s∈S}(v−s)q₁₁, −Δ) at the set R_k of rational places are explicit classes in
Q*/Q*², computed in exact rational arithmetic. R_k consists of all rational roots of q₁₁ and Δ (any
multiplicity), ∞, and the extra places of (3). A constant c₀ contributes c₀ at places where Δ has
odd valuation and nothing elsewhere. Exhausting all subsets S ⊆ R_k (2⁹ to 2¹⁵ cases) finds no S
and c₀ for which all residues vanish.
(3) *Other places.* If c has odd valuation at t ∈ T outside R_k, the residue there is −Δ(t), which
must then be a nonzero rational square. An exact integer search over T finds no such t for
k ≤ 10. For k = 11 it finds t = 2, which was added to (2); there is still no solution.
Hence q represents no c ∈ L_T. ∎

*Checks.* The inputs q₁₁ and Δ are bound to the symbolic derivation (assertion). The
scale-invariant ratio q₀₁²/(q₀₀q₁₁) agrees with the independent numeric engine for 10 values of v
per k. Weil reciprocity is asserted for the base algebra **and for every generator (v−s)**.
`sqclass` rejects any inexact (floating) input. A positive control, replacing q₁₁ by a
linear-type 3(v−r₁)(v−r₂), is found. The pairing matrix (b_d) has rank 2 for k = 6, 8, 9 and
rank 1 for k = 10, 11, where only one multiplicity-free daughter (k' = 7) exists.
**True-positive test of the same machinery:** for spin f = 3, 4, 5 and L = fv − 4 a linear-type
value is genuinely represented (Theorem B'), and `general_f_k4.py` finds residue-free solutions
(2, 2 and 4).
**Corrections during review.** (i) The first version of `tame` computed (−1)^{ab} with a negative
Python exponent, which gives a float. For generators with a valuation −1 this produced wrong
square classes, found by Codex. The fix uses integer parity, rejects floats, and adds
per-generator reciprocity assertions. All runs were repeated; the conclusion (0 solutions for
every k, true positives for f = 3, 4, 5) is unchanged, and Codex's independent exact
recomputation agrees. (ii) A factorization-based square test over imaginary quadratic fields
wrongly returned "not a square". It was replaced by the exact criterion above.
*Ran:* `$PY multiplicity_obstruction.py 6` (and 8, 9, 10, 11), output in
[results/k6_square_class.txt](results/k6_square_class.txt) etc. The loop
`for k in 6 8 9 10 11; do $PY brauer_residues.py $k 30; done` printed
`subsets S … with all residues trivial for some c0: 0 []` for all five k; see
[results/brauer_residues_k6_to_k11.txt](results/brauer_residues_k6_to_k11.txt).

*Scope and limits.* (a) Only rational **directions** are covered, normalized afterwards. A change
of direction with algebraic, non-rational coefficients (e.g. involving √g(v)) is not excluded.
(b) Linear factors outside T are excluded only if the hyperelliptic curve w² = −Δ_k(s) (genus ≥ 4)
has no further rational points. We did not prove this; the search bounds are stated above.
(c) Only these five two-dimensional families are covered. Nothing is claimed for higher
multiplicities or other (v, L).
(d) This rules out one product ansatz, **not** closed forms in general. In any specified rational
basis the CFPs are explicit (§C): square roots of rational functions of v that contain an
irreducible polynomial. That is a legitimate analytic representation, only not of Bao–Li type.

## E. Low total spin, arbitrary seniority (the regime of antiferromagnetic/cyclic spin-2 condensates)

**Theorem E1 (any f).** Let φ be any normalized seniority-(v−1) state with total spin 0. Then
Σ_α |c(v α L=f; φ)|² = (2v+D−2)(v+D−3) / (D v (2v+D−4)); the sum runs over any orthonormal
basis of the (v, L=f) block. For f = 2 and v ≡ 1 (mod 3) the parent (v, L=2) is unique, so this
is the CFP itself: r² = (v+2)(2v+3)/(5v(2v+1)).

*Proof.* Let Φ = a†_f φ = [a†⊗φ]_{f f}. Rotational invariance of φ gives ⟨n_m⟩ = (v−1)/D for every
m, so ‖Φ‖² = 1 + (v−1)/D. Also PΦ = 2(−1)^f a_{−f}φ is harmonic of degree v−2, so the non-harmonic
part of Φ has norm² ‖PΦ‖²/(4(v−2)+2D) = 2(v−1)/(D(2v+D−4)). The harmonic part of Φ is a spin-f,
seniority-v vector, so Σ_α |⟨vα f f|Φ⟩|² = ‖h_v‖². Dividing by v gives the claim. ∎
*Ran:* `$PY check_general_f.py` printed `Theorem E1 (scalar-parent weight) agrees exactly: 19
daughters, f = 1..4, v <= 9`.

**Conjecture E2 (spin 2, L ≤ 5, all seniorities).** In the notation (L, λ) → (L', λ') with
v ≡ λ (mod 3), the following hold, together with 0 → 2: r² = 1. Daughters with λ' = λ+2 lose a
boson from a trio and always carry the factor v − λ = 3e.

| (L,λ)→(L',λ') | r² | (L,λ)→(L',λ') | r² |
|---|---|---|---|
| (2,1)→(0,0) | (v+2)(2v+3)/(5v(2v+1)) [**proved, E1**] | (4,3)→(2,2) | (v+3)(2v+5)/(6v(2v+1)) |
| (2,1)→(3,3) | (v−1)(2v+3)/(2v(2v+1)) | (4,3)→(4,2) | 2(2v−1)(2v+5)/(11v(2v+1)) |
| (2,1)→(4,3) | 3(v−1)(2v−1)/(10v(2v+1)) | (4,3)→(5,5) | (v−3)(2v+5)/(6v(2v+1)) |
| (2,2)→(2,1) | 2(2v+3)/(7v) | (4,3)→(6,5) | 10(v−3)(2v−1)/(33v(2v+1)) |
| (2,2)→(4,4) | 3(v−2)/(7v) | (4,4)→(3,3) | 2(2v+3)(2v+5)/(15v(2v+1)) [sign −] |
| (3,3)→(2,2) | 5(v+3)/(14v) | (4,4)→(4,3) | 2(2v−1)(2v+5)/(11v(2v+1)) |
| (3,3)→(4,2) | 6(2v−1)/(35v) [sign −] | (5,4)→(3,3) | 21(v+5)(2v+3)/(110v(2v+1)) |
| (3,3)→(5,5) | 3(v−3)/(10v) | (5,4)→(4,3) | 3(v+5)(2v−1)/(22v(2v+1)) |
| (4,2)→(2,1) | 5(v+4)(2v+3)/(21v(2v+1)) | (5,4)→(7,6) | 15(v−4)(2v−1)/(77v(2v+1)) |
| (4,2)→(4,4) | 64(v−2)(v+4)/(385v(2v+1)) [sign −] | (5,5)→(4,4) | 21(v+4)/(55v) |
| (4,2)→(5,4) | 7(v−2)(2v+3)/(15v(2v+1)) | (5,5)→(5,4) | 6(2v+3)/(65v) |
| (4,2)→(6,4) | 7(v−2)(2v−3)/(33v(2v+1)) | (5,5)→(6,4) | 4(2v−3)/(77v) [sign −] |
| | | (5,5)→(7,7) | 30(v−5)/(91v) |

For the two-dimensional daughter blocks (L' = 6, λ' ∈ {3, 6}, at v−1 ≡ 0 mod 3) only the
basis-independent block weights are listed. They are **not** of product type:
(4,4)→6: (122v²−427v−180)/(165v(2v+1)); (5,4)→6: 4(92v²−92v−285)/(385v(2v+1)).

*Evidence (Empirical, exact).* `$PY verify_bottom_conjectures.py ../results/spin2_r_table_v88_L5.json`
printed `product-formula checks: 742 over 26/26 formulas; block-weight checks: 58; formulas with
disagreements: 0`. The script also asserts full coverage and at least 10 checks per formula. Each
product formula is checked at every available v in its residue class, from the smallest
admissible v up to v ≤ 88 (27–30 values per formula). Two of the 26 product formulas are already
established: (2,1)→(0,0) is Theorem E1, and (0,0)→(2,2) = 1 is trivial because there is a single
daughter. **24 product formulas and 2 block weights remain conjectural.** The (5,4) block weight
follows from completeness and the other (5,4) formulas, so its checks are not independent. The
L' = 6 daughter block is one-dimensional at v = 4 and two-dimensional from v = 7.
The formulas were found by exact rational interpolation from part of the data and checked against
all of it. This is **not** a proof for all v. A proof would need either the one-body densities of
the daughters (the Redmond-type recursion does not close at bounded L; see §G) or explicit SO(5)
spherical harmonics in Bohr coordinates.

## F. Validation of the exact engine (exact validation on the stated cases, not a proof of the implementation)

* `$PY selftest.py`: `selftest OK: 462 exact checks passed`. These cover [P,P†] = 4N̂+2D,
  S₊ commuting with P and P†, adjointness, idempotence and orthogonality of the harmonic projector,
  [S₊,S₋] = 2S_z, and the stretched CG formula against sympy.
* `$PY verify_first_quantized.py`: `first-quantized check OK: 74 CFPs (f=1 N<=5, f=2 N<=4, f=3 N<=3)
  agree with the engine, including signs`. This is an independent definition-level computation with
  explicit symmetric tensors and sympy CG coefficients.
* Multiplicity labels agree with the null-space dimension for every (v, L), v ≤ 14
  (`spin2_tables.py`).
* Sign constancy: for every spin-2 family formula, the largest real root of the overlap X lies
  below the start of the validity range. For the (v, f) formulas of Theorems B and B', every
  factor of X is certified sign-constant on the stated domain (`certified_sign`). So the stated
  signs hold on the whole range.

## F'. Two-body CFPs (Claim G)

With the pair φ_s(N−1, N) coupled first and C2 defined by
|N; ΓL⟩ = Σ C2(ΓL; s, Γ''L'') [φ_s ⊗ |N−2; Γ''L''⟩]_L, the standard chain formula

  C2(ΓL; s, Γ''L'') = Σ_{Γ'L'} c(ΓL; Γ'L') c(Γ'L'; Γ''L'') (−1)^{L+L''} √((2s+1)(2L'+1)) {f f s; L'' L L'}

holds for even s, and C2 = 0 for odd s. Combined with Theorem A and the one-body closed forms, it
gives the two-body CFPs needed for interaction matrix elements as a finite sum. There are at most
2f+1 intermediate spins (five for spin 2), plus a sum over multiplicity labels. The formula does
not supply one-body closed forms that are missing. *Ran:* `$PY verify_two_body.py` printed `two-body chain
formula verified exactly: 84 two-body CFPs (f=1 N<=5, f=2 N<=4), including signs and the vanishing
of odd-s pairs`. The left side is computed independently from explicit symmetric tensors.

## G. What remains open, and the exact blockers

1. **General (v, α, L) for spin 2.** Closed forms exist family by family. §C is an algorithm that
   is exact for every fixed k, with degrees growing in k, in specified bases. There is no uniform
   formula. Theorem D shows that in the five two-dimensional families k ∈ {6, 8, 9, 10, 11}, no
   rational direction gives Bao–Li-type CFPs with linear factors in T. Higher multiplicities are
   untested. *Open objective:* uniform formulas in a specified basis. These may carry
   irreducible factors, or use a non-rational direction or a different representation of the
   missing label. This is NEEDS-NEW-REPRESENTATION for the Bao–Li ansatz.
2. **Proof of Conjecture E2.** The block-weight recursion
   W(v, L; L') = (1/v)[m' + Σ_{L''} (density terms of the daughters)] couples L to L+2 at each step
   down in v, so induction at bounded L does not close. *Missing lemma:* closed forms for the one-body
   densities ⟨(a†ã)^{(k)}⟩, k = 2, 3, 4, of the low-L states. This is a bounded PROOF-OBLIGATION.
3. **General f beyond k = 3, and spin-3/2 fermions.** Fermions were not attacked. Two-body CFPs
   are covered by Claim G wherever one-body closed forms exist.
4. **Unconditional form of Theorem D.** This needs the rational points of the curves
   w² = −Δ_k(s), or a different invariant.

## H. Independent review and dispositions

See [review/codex-review.md](review/codex-review.md) (prompt: [review/codex-prompt.md](review/codex-prompt.md))
and the focused second review [review/codex-review-2.md](review/codex-review-2.md)
([prompt](review/codex-prompt-2.md)). Both used gpt-6.1-sol at max effort, read-only. Verdicts
before fixes: A, B, C, E1, E2 and STATUS "accept with fixes"; D "reject as written" (first
review), then "accept with fixes" (second review, finite-T theorem); README table "reject as
written". I checked each point myself. Dispositions:

| # | Finding | Disposition |
|---|---|---|
| R1.1 / R2.1 | **Critical:** `(-1)**(a*b)` with a·b < 0 gave a float, so wrong residue classes (k = 6, v + 1/2 at −1/2: class 30, not 11799795063484930) | **Fixed.** Integer parity sign; `sqclass` rejects floats; per-generator reciprocity asserted; regression test for this exact case. All runs repeated: still 0 solutions for k = 6, 8, 9, 10, 11 (matches both reviewers' exact reruns) and true positives for f = 3, 4, 5 |
| R1.2 / R2.3 | B and B' do not give every all-N CFP (v→v+1 branch needs reverse coefficients with deficit up to k+2f). Counterexample: 294(4v−1)/((v+2)(2v+3)(2v+5)(18v²+127v−81)) | **Accepted.** Claims restricted to the reduced CFPs and the v→v−1 branch. Counterexample re-derived by hand from A and C and quoted in §B |
| R1.3 | §D normalization (b_d, n_d, C_d) did not match the code | **Fixed.** §D now defines unnormalized rational y_d and factorial-scaled quantities exactly as in the code |
| R1.4 / R2.2 | Unrestricted quadratic-optimality and blanket no-go unsupported (linear factors outside T) | **Accepted.** Optimality restricted to directions with linear support in T. No-go stated over L_T only. README, STATUS and §G re-scoped |
| R1.5 | §G and STATUS overstated multiplicity obstruction and "decidable" | **Fixed** (five families, rational directions, finite T; decidable for fixed finite support) |
| R1.6 | rational orthonormal basis vs rational directions | **Fixed** (directions normalized afterwards; algebraic changes of direction not covered) |
| R1.7 | real-basis assumption; E1 needs \|c\|² | **Fixed** (§0, Theorem A hypotheses, E1) |
| R1.8 | domains (A: f ≥ 1, N ≥ 1; B row starts; C: v ≥ max(k,k'+1); r² not r; bases are conventions) | **Fixed** |
| R1.9 | T-membership false for general-f roots | **Fixed** (restricted to spin-2 formulas) |
| R1.10 / R2.6 | E2 accounting (742 + 58; 27–30 values; 2 of 26 already proved) | **Fixed**; the script now prints these counts |
| R1.11 | checkers could exit 0 on disagreement; F overlabelled | **Fixed** (assertions on zero disagreements, full coverage and 8/8 Pan rows; F relabelled "exact validation") |
| R1.12 | STATUS mixed primary, secondary and search statements; "every published" overclaim | **Fixed** (separated; narrowed to the sources examined) |
| R1.13 | two-body "at most five" spins is the spin-2 bound | **Fixed** (2f+1 in general) |
| R2.4 | B' phase convention of the second state unclear | **Fixed** (Q4, H2, t = (f−1)(2f−3)/g stated; residual keeps its inherited sign) |
| R2.5 | B' symbolic completeness and sign certification only numeric or asymptotic | **Fixed** (symbolic row-sum assertions; `certified_sign` proves sign constancy on v ≥ 5, f ≥ 3; also for Theorem B) |

Not fixed: none of the accepted findings is left open. The scope limits that the reviewers
emphasized (rational directions, finite T, the open rational-point question, the unproved E2)
are stated as limitations, not resolved.

## I. Approved scoped continuation: universal E2 weights

The user approved choosing precise open subproblems. The fixed target is the 24 unproved
individual squared-CFP formulas and two block weights in §E, for all admissible v, rather
than every spin-2 CFP. New work must be a universal derivation, independently reviewed and
replayed exactly. Existing v ≤ 88 tables are controls only; no expansion of that range is
part of this continuation.

### I.1 Statement and evidence boundary

**Theorem E2-W (squared coefficients and block weights).** Every squared-CFP product formula
in §E and both displayed L'=6 block-weight formulas hold for every admissible seniority
v=λ+3e, e≥0, whenever the parent and the indicated daughter exist. There are 26 individual
formulas (two previously proved) and two block formulas. An absent daughter has weight zero.
Thus the 24 previously unproved squared formulas and both block weights are settled by
the derivation below. This is a written proof with finite, replayable rational algebra,
not inference from the v≤88 table.

**Phase boundary:** this theorem proves |r|², not the convention-specific signs printed
beside four formulas in §E. Those signs retain their previous exact finite evidence.
The two block weights do not determine the individual coefficients into a multiple
daughter block. Neither limitation changes the squared-weight target approved for this
continuation; no all-spin, all-state or all-N ascending-seniority claim is made.

Evidence label: **Certification** (written proof and exact identities in Q(v)).
Novelty status: **NOVELTY-UNCLEAR**. The ingredients are standard parentage/recoupling
identities. A closed finite dependency chain is exhibited here; no priority is asserted.

### I.2 Supports and the two moment identities

Let W_{v,L}(J)=Σ_α |r(v,L;v−1,α,J)|². All parent blocks used here have multiplicity one.
The SO(5)→SO(3) branching rule is λ=v,v−3,..., with
λ≤L≤2λ and L≠2λ−1 (λ=0 gives L=0). This yields exactly:

| parent (L,λ) | admissible v | possible daughter spins J, including zeros at the lower boundary |
|---|---|---|
| (0,0) | 3,6,... | 2 |
| (2,1) | 1,4,7,... | 0,3,4 |
| (2,2) | 2,5,8,... | 2,4 |
| (3,3) | 3,6,9,... | 2,4,5 |
| (4,4) | 4,7,10,... | 3,4,6 |
| (4,2) | 2,5,8,... | 2,4,5,6 |
| (4,3) | 3,6,9,... | 2,4,5,6 |
| (5,4) | 4,7,10,... | 3,4,6,7 |
| (5,5) | 5,8,11,... | 4,5,6,7 |

For L≤5 the only λ of each residue is the one displayed, so these parent blocks are
one-dimensional for every listed v. The daughter L=6 block at v−1≡0 mod3 has λ'=3,6
(only λ'=3 at v=4); all other daughter blocks listed here are one-dimensional.
For example L=7 admits λ'=5,6,7, exactly one for each residue. These assertions follow
by listing λ∈[ceil(L/2),L], not by extrapolating multiplicity counts.

For a normalized symmetric state of v spin-2 particles,

  Σ_J W_{v,L}(J)=1,                                    (I.1)
  Σ_J J(J+1) W_{v,L}(J)=6+(v−2)L(L+1)/v.               (I.2)

Proof of (I.2): write total spin J_tot=Σ_i s_i, s_i²=6. Permutation symmetry implies
⟨J_tot·s_i⟩=L(L+1)/v. The remaining particles have spin J_tot−s_i, hence their squared-spin
expectation is L(L+1)+6−2L(L+1)/v. The CFP expansion diagonalizes this observable.
Both identities also apply to daughter block sums, without choosing a missing-label basis.

Given all but two weights, (I.1)–(I.2) determine the last two uniquely: the determinant is
J_b(J_b+1)−J_a(J_a+1)≠0. This second moment identity is the ingredient missing from the
earlier attempted recursion in §G. The earlier assertion that bounded-L closure was
unavailable is superseded for this scoped target.

### I.3 Harmonic principal-parent identity

Fix a normalized harmonic daughter |d,J,M'> of degree v−1. Define
Φ_{LM}=Σ_m ⟨2m,J(M−m)|LM⟩ a†_m |d,J,M−m⟩.
Its creation norm is

  ||Φ||²=1+(v−1) Σ_K A_{LJK} W_d(K),                  (I.3)

where W_d(K)=W_{v−1,J}(K), and

  A_{LJK}=Σ_{m,n=-2}²
    ⟨2m,J(L−m)|LL⟩ ⟨2n,J(L−n)|LL⟩
    ⟨2n,K(L−m−n)|J(L−m)⟩
    ⟨2m,K(L−m−n)|J(L−n)⟩
  =(2J+1){K 2 J; L 2 J}.                             (I.4)

Invalid magnetic projections contribute zero. To prove (I.3), commute a_m past a†_n
in ||Φ||². The commutator gives one by CG normalization. In the remaining expectation,
insert a complete (v−2)-particle basis between a†_n and a_m. The annihilation amplitudes
are √(v−1) times the daughter's CFP and CG coefficient. Since [P,a_m]=0, the states left
by annihilation are harmonic; no lower seniorities enter. Sum over the multiplicity
index to obtain W_d(K). The four-CG contraction is (I.4).

Now PΦ=2[ã×d]_{LM}, where ã_m=(−1)^m a_{−m}. This vector is harmonic of degree v−2.
Therefore the non-harmonic part of Φ is
P†PΦ/[2(2v+1)], since PP†=2(2v+1) on such harmonic vectors. Orthogonality of different
seniorities gives

  ||HΦ||²=||Φ||²−2||[ã×d]_{LM}||²/(2v+1).            (I.5)

The CG adjoint identity (or Wigner–Eckart conjugation) gives

  ||[ã×d]_{LM}||²
     =(v−1)(2J+1)/(2L+1) W_d(L).                     (I.6)

Because the degree-v harmonic spin-L block is unique,
||HΦ||²=v |r(v,L;v−1,d,J)|². Combining (I.3)–(I.6) proves

  W_{v,L}(J) =
    [1+(v−1)Σ_K A_{LJK}W_{v−1,J}(K)
       −2(v−1)(2J+1)W_{v−1,J}(L)/((2v+1)(2L+1))]/v. (I.7)

We use (I.7) only when this daughter block J is unique. Its own daughters can have
multiplicity: (I.7) requires only their block weights, which are basis-independent.
With multiple parent states, (I.5) instead gives their summed weight; that case is
not substituted for an individual coefficient here.

### I.4 The finite acyclic closure (no induction with an unbounded spin window)

Start with W_{v,0}(2)=1 for v=3,6,... . Each following row denotes an identity valid for
all seniorities in its residue class. An anchor (J,λ_d) uses the already-established
row W_{v−1,J}, not an independent assumption about a higher-L state.

| parent row | anchor daughters in (I.7) | remaining two J fixed by (I.1)–(I.2) |
|---|---|---|
| (2,1) | (0,0) | 3,4 |
| (2,2) | none | 2,4 |
| (3,3) | (2,2) | 4,5 |
| (4,4) | (3,3) | 4,6 |
| (4,2) | (2,1), (4,4) | 5,6 |
| (4,3) | (2,2), (4,2) | 5,6 |
| (5,4) | (3,3), (4,3) | 6,7 |
| (5,5) | (4,4), (5,4) | 6,7 |

Every dependency points to an earlier row. Thus this is a finite construction of
rational functions, not a recurrence that must be iterated up to v. The eleven anchor
values are exactly the corresponding entries of the §E table. All remaining entries
are uniquely forced by two linear equations.

Example: for (L,λ)=(2,2) there are only J=2,4. Solving the two moments directly gives
W(2)=2(2v+3)/(7v), W(4)=3(v−2)/(7v). For (3,3), (I.7) with daughter (2,2) uses
A_{3,2,2}=4/7 and A_{3,2,4}=1/14; W_d(3)=0. Substitution yields
W_{v,3}(2)=5(v+3)/(14v). The moments then give W(4)=6(2v−1)/(35v) and
W(5)=3(v−3)/(10v). The same exact operations produce every subsequent row.

Boundary care: the (2,1) row uses the scalar anchor for v≥4; at v=1 the only daughter
is the vacuum, so W(0)=1 and the displayed expressions give W(3)=W(4)=0. The (4,2)
row uses two anchors for v≥5; at v=2 there is only one spin-2 daughter, so W(2)=1 and
the other displayed weights vanish. All other anchors exist at their row's smallest v.
Any additional channel absent at a minimal seniority has zero weight, as is explicit
in the numerator factors (v−λ). The scalar-parent case begins at v=3, never at the
vacuum. There are no poles on the positive admissible domains.

This proves all 26 squared product formulas and both block weights. The two L=6
block formulas follow from the same two-moment solve; no basis for that block or
closed form of its individual CFPs is needed. ∎

### I.5 Reproduction and independent-review contract

`$PY code/low_spin_proof.py` computes eleven anchors with exact four-CG contractions,
solves the two moment equations at each row and then (only after deriving the answers)
compares them with the previously registered formulas. It prints:
`UNIVERSAL IDENTITIES: 26/26 product formulas + 2/2 block weights derived exactly in Q(v).`
The full dependency ledger is `results/low_spin_universal_derivation.json`.
The derivation has no access to finite-v tables and uses no interpolation.

The independent implementation `code/verify_low_spin_proof.py` uses a factorial Racah
sum for (I.4), without any CG/Wigner routine. It checks the registered rational formulas
against all eleven anchor identities, both moments, physical minimal-v cases and the
existing v≤88 evidence. Negative controls omit the harmonic correction, corrupt the
normalization, or perturb two weights while preserving their sum; each must be detected.
The finite controls validate encoding and boundaries, not the universal quantifier.
The universal claim rests on (I.1)–(I.7), branching, and the finite acyclic construction.
