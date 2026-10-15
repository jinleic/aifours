**Verdict: MINOR-REVISION**

I found no substantive mathematical defect in RESULTS.md §§1–5. On correctness alone, the universal proof meets the acceptance bar. The revisions below concern prior art (which affects novelty, not correctness), overstated descriptions of the finite controls, and one citation gap plus some ordering of the exposition.

Review scope: I worked read-only on the snapshot set and did not execute any code. I read CRW Eqs. (20) and (25)–(29) and the "not proved" sentence from the page images, because the text extraction of (29) is garbled. I did not open the other referees' outputs under `review/`.

---

## A. Independent recomputation (audit items 1–7)

**Statement.** In the page-7 image of Eq. (29), set σ = 2s. Then (σ/2+1)! = (s+1)!, (σ/2−vᵢ)! = jᵢ!, (σ−2vᵢ+1)! = (2jᵢ+1)!, σ+4 = 2s+4 and (σ+3)! = (2s+3)!. RESULTS (2) is an exact transcription.

**(1) Trace normalization.**
- CRW (20) writes a matrix element as (L₁M₁L₂M₂|L₃M₃)·r/√(2L₃+1), where r is the SO(3)-reduced element. CRW (26) writes r = √(2L₃+1)·F·R, with F the isoscalar factor.
- Combining them gives T = F·(SO(3) CG)·R; the √(2L₃+1) factors cancel.
- For fixed (α₃L₃M₃), Σ_{M₁M₂}|T|² = r²/(2L₃+1). Summing over α₁L₁α₂L₂ then gives exactly the right side of (28), i.e. R². Summing over the d_{v₃} output states gives (3).
- The Edmonds 3j convention gives the same sums, because Σ(3j)² = 1/(2j′+1).

I also checked the bridge directly in CRW's own per-(α₃,L₃) form, without using the trace:
- Take (1,1,2) with L₃ = M₃ = 4. Only L₁ = L₂ = 2 contributes, and [Y₁×Y₁]⁽⁴⁾₄ = Y₁,₂², with Y₁ = √15·Q/(4π) from Welsh–Rowe Eq. (41).
- R² = (15/16π²)²·V·E|Q₂|⁴ = (225/256π⁴)(16π²/3)(2/35) = 15/(56π²). So π²R² = 15/56, matching (2) and the receipt key "1,1,2". This triple is also a saturated-triangle case.
- The L₃ = 2 states agree: the total v = 2 content is 75/16π² − 15/16π² = 15/4π², which equals 14 × 15/(56π²).

The quadrupole case gives a second check that does not depend on V. The kernel of Q is x·y, and tC_v = [(v+1)C_{v+1} + (v+2)C_{v−1}]/(2v+3). These give ⟨v+1|||Q|||v⟩² = d_v·E[P_v·P_{v+1}·t] = (v+1)/(2v+5), which is Welsh–Rowe Eq. (46).

**(2) Outer multiplicity and missing labels.**
- The contraction argument is correct. The pairing numbers are forced to be n₁₂ = j₃, n₁₃ = j₂, n₂₃ = j₁.
- Any ε term needs 5 slots drawn from only 3 symmetric groups, so it vanishes.
- Cross-check: [2]⊗[2] = [4]+[3,1]+[2,2]+[2]+[1,1]+[0] has dimensions 55+81+35+14+10+1 = 196, so [2] occurs once.
- The internal SO(3) labels are summed in the trace. Independence of (28) from α₃ follows from the Wigner–Eckart theorem plus multiplicity one.

**(3) Measure.**
- V = 8π²·∫₀^{π/3} sin3γ dγ = 16π²/3, while |S⁴| = 2π^{5/2}/Γ(5/2) = 8π²/3. The ratio is 2.
- From Table I, Ψ₀₀₀ = √3/(4π), and |Ψ₀₀₀|²·V = 1.
- Table I's N₁,₂ = 32π²/15 equals ‖√2·Q₂‖² in this measure.
- Using the ordinary area instead would double R², as the proof states.

**(4) Addition theorem and latitude density.**
- K_v(x,x)·V = d_v, so K_v = (d_v/V)·P_v, with k_v = (3)_v/v! = (v+1)(v+2)/2.
- On S⁴ the density of t = x·y is proportional to (1−t²); normalizing with ∫(1−t²)dt = 4/3 gives (3/4)(1−t²).
- This gives |R|² = (d₁d₂/V)·E[P₁P₂P₃]. Using d_v/k_v = (2v+3)/3, the prefactor is 1/(6V) = 1/(32π²), which is Eq. (6).

**(5) Rogers specialization and factorials.**
- The DLMF TeX matches (7). Ališauskas's own citation ("Theorem 6.8.2 of [27]", where [27] is Andrews–Askey–Roy) corroborates the AAR attribution.
- With m = b+c, n = a+c, ℓ = c: m+n−ℓ = s, m+n−2ℓ = p = a+b, m−ℓ = b, n−ℓ = a. ℓ = c is the only index that produces output degree p.
- (p+3/2)·p!/(3)_p · h_p = 2, which gives (9).
- (s+3/2)(2s+1)! = (2s+3)!/(4(s+1)), which gives (10).
- The ratio (11)/(2)² = (1/8 ÷ 1/16)·(s+2)/(2s+4) = 1.
- Every step holds for all (a,b,c) in ℤ≥0³. The q = 0 cases are fine, and no denominator vanishes.
- Spot check: I(1,1,2) = 144/35 from (10), and also from C₁C₁ = (6/5)C₂ + 9/5 directly.
- Ališauskas (13b) at l′ = 0, n = 5 reduces to (10) exactly.

**(6) Boundary and forbidden cases.**
- From (2) I recomputed π²R(v;0,v)² = 3/16, π²R(0;v,v)² = 3d_v/16, both quadrupole formulas, and π²R(2;2,2)² = 7/8.
- Odd sum: the integrand is odd, so the integral is 0.
- Even sum with a triangle violation: v₃ is not among the degrees v₁+v₂−2ℓ, so orthogonality gives 0.
- Saturated triangles correspond to the top Rogers term (c = 0).

**(7) Phase.** CRW's "to within an arbitrary phase, which is chosen to be unity" means R is the positive square root of (28). Expression (2) is strictly positive for admissible triples, so taking the positive root is correct.

**Receipt consistency (hand checks).**
- 616 admissible triples in the 0–12 cube: correct.
- 58,840 overlaps = h₃(1,5,14,30) = (50³ + 3·50·1122 + 2·29870)/6: correct.
- The values for keys 1,1,2 / 1,2,3 / 2,3,1 / 2,3,3 / 3,3,2 match my hand evaluations of (2).

`★ Insight ─────────────────────────────────────`
- Σ|T|² is the squared Frobenius norm of the intertwiner, and it does not change under unitary changes of basis in each slot. That is why CRW's missing labels, the Gram–Schmidt ordering and the CG sign choices all drop out. Only |R| survives, and the "positive phase" is pure convention.
- The scalar and quadrupole cases check two different conventions independently. The scalar case pins the mass V. The quadrupole case has kernel x·y with no V, so it pins the unitary CG normalization.
`─────────────────────────────────────────────────`

---

## B. Findings

**Correctness defects: none.**

**1. [Novelty, significant; does not affect correctness] Direct prior art for the formula itself is missing.**
- Locations: STATUS.md:46 and :49; RESULTS.md:154 and :209 ("the normalization bridge … is the deliverable"); README.md:44.
- Ališauskas 2005, Eq. (26a) (alisauskas2005.txt:795–815), gives the class-one SO(n) 3j-symbol (l₁ l₂ l₃; 0 0 0)ₙ in closed form. The paper says it was derived in [5], which is Junker, J. Phys. A 26 (1993) 1649.
- By (23a) and (33a) at M = 0, its square equals E[P₁P₂P₃]. At n = 5 I computed (26a)² = 24·(J+1)!(J+2)!/(2J+3)!·Π(2j+1)!/(j!)²/Π(lᵢ+1)(lᵢ+2), which is exactly (3/4)∫P₁P₂P₃(1−t²)dt.
- Therefore CRW (29) is equivalent to **π²R² = (3/16)·d_{v₁}·d_{v₂}·(v₁ v₂ v₃; 0 0 0)₅²**. Check: (2,2,2) gives (3j)² = 1/42, so π²R² = 7/8.
- The text extraction of (26a) is garbled. I fixed the reading by checking that at n = 3 it reduces to the standard SO(3) symbol (l₁l₂l₃; 000)². The authors should confirm it against the PDF.
- **Correction:**
  - Add this to the STATUS prior-art table and to RESULTS §4 and §7.
  - Describe the contribution as the explicit identification with CRW's normalization (28), measure and phase. The SO(5)-reduced element does not depend on the subgroup chain, so the canonical-chain results already contain it.
  - Consider replacing NOVELTY-UNCLEAR with something like "known in equivalent form before 2009; explicit CRW-convention proof not found in the bounded screen".

**2. [Evidence overstatement, minor] The negative controls are mostly tautological.**
- Locations: verify.py:102–108, README.md:27 ("5/5 negative controls detected"), RESULTS.md:192.
- `2·x ≠ x` and `14·x ≠ x` are applied after the fact to values already asserted equal at line 100, so they cannot fail.
- The two "nonzero forbidden" controls compare the arbitrary constant 1/16 with a computed 0.
- Only the Legendre control re-runs a mutated calculation, and only for the single triple (1,1,0): 5/48 versus 15/16.
- **Correction:** relabel these as arithmetic illustrations, or implement real mutations across all triples (V = 8π²/3 in the Cartesian oracle, Legendre kernels in the univariate oracle) and record how many triples disagree.

**3. [Evidence scope, minor] No finite check tests the §2 bridge or the mass V.**
- verify.py:56 hard-codes Eq. (6), including the 1/32. cartesian_oracle.py:115 hard-codes 3/(16·d_{v₃}).
- So the univariate oracle tests only §§4–5 (v ≤ 12), and the Cartesian oracle tests §§3–5 (v ≤ 3). Neither can detect an error in the step RESULTS:209 calls the deliverable.
- The symbolic check (verify.py:64–68) receives (3/2)_q and (3)_s already rewritten as factorials. It therefore verifies the algebra from (9) to (10) to (2)², not the specialization from (7).
- **Correction:** state this in §6, §8 and the README. Optionally add a CRW-convention oracle that evaluates (28) at fixed (α₃,L₃) from Table I, like the hand-worked (1,1,2), L₃ = 4 case in Section A.

**4. [Rigor/citation, minor] The multiplicity-one argument rests on an unnamed theorem (RESULTS.md:68).**
- **Correction:**
  - Name the first fundamental theorem of invariant theory for SO(5) (every invariant is built from δ-contractions and single-ε terms).
  - Note that dim Hom(V₁⊗V₂, V₃) = dim (V₁⊗V₂⊗V₃)^G because these representations are real.
  - Or cite the standard O(n) rule [p]⊗[q] = ⊕_{k,l}[p+q−2k−l, l].
  - Optionally note that the same pairing count also proves the selection rule.

**5. [Exposition, minor] §2 states things in the wrong order (RESULTS.md:53–61).**
- The text says "Choose any orthonormal bases" and then uses the factorization T = R·(isoscalar factor × SO(3) CG). That factorization holds only in CRW's SO(5)⊃SO(3) basis.
- **Correction:**
  - Derive (3) in CRW's basis first, then invoke invariance under U₁⊗U₂⊗Ū₃ to extend it to any orthonormal bases.
  - Add one line noting that CRW's (28) uses a plain square, not a modulus squared. The two agree because the SO(3)-reduced elements are real (the F_K are real, and ∫D*DD is real).

**6. [Optional]** The SO(5)-invariance of sin3γ dγ dΩ is load-bearing: both the Wigner–Eckart step and Eq. (5) need it. It is currently only cited from CRW (RESULTS.md:24). Add the standard Bohr Jacobian (d⁵q ∝ β⁴|sin3γ| dβ dγ dΩ) and state that its pushforward to S⁴ is 2 × the area measure.

**7. [Optional wording]**
- RESULTS.md:76: invariance makes K_v a function of t; it is a polynomial in t because its restriction to a great circle is.
- RESULTS.md:89: "first-coordinate distribution" should be "distribution of x·y".
- README.md:44: the proof is also conditional on the invariant-theory result (or the tensor-product rule) and on measure invariance, not only on Rogers's theorem.

**8. [Trivial]** The OpenAlex inventory includes an evident false-positive record, W3184110961 ("Geomagnetic orbit determination: EKF or UKF?"). STATUS.md:57 could note it.

`★ Insight ─────────────────────────────────────`
- A forward-citation screen of CRW cannot, by construction, find work published before CRW. The real priority risk here runs backward, to Vilenkin, Gavrilik, Kildyushov–Kuznetsov, Junker 1993 and Ališauskas 2002/2005.
- Because the doubly reduced element does not depend on the subgroup chain, canonical-basis SO(n) results already encode CRW's physical-basis number. Only the normalization dictionary R² = d₁d₂(3j)²/V was missing.
`─────────────────────────────────────────────────`

---

## C. Limits of this review

- **The finite checks are not the universal proof.** The all-integer statement rests only on the written argument in §§1–5, which I find correct. The 2,197 univariate triples and 64 Cartesian triples are controls, and per Finding 3 neither one tests the convention bridge.
- **This bounded source set cannot certify worldwide priority.** Finding 1 shows the formula's content predates CRW. Junker 1993 is not in the folder, so I could not verify it directly.
- I did not execute `verify.py` or recompute any hashes. The receipt and source hashes are consistent with the snapshot, and every receipt value I checked by hand matches.
