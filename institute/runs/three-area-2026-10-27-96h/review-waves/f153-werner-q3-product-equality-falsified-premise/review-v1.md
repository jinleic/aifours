# f153 review v1 — original q3 on rank≤2 product operators: factorization, equality class, no universal strict gap

**Review id:** `f153-werner-q3-product-equality-falsified-premise` · **kind:** INDEPENDENT_SAME_HARNESS_SCIENTIFIC_REVIEW · **reviewer:** same-harness subagent (not human, not independent model family, not formal/kernel, not novelty verification).
**Authority:** `contract-addendum-2-frontier-first-owner-direction-v1.json` (as cited by the manifest).
**Manifest:** `manifest-v1.json`, SHA256 `c190e82606f6302bd55343c7678a6334e537d71325ab26cf6ba6a9e2a8fe4f4f` (recomputed, matched).
**Native clock observed before composing this file:** `2026-10-28T21:51:58-0700 PDT` (from `/bin/date`; the file write occurs after this reading).

## 0. Verdict (exact scope)

**No FATAL. No MAJOR. Three MINOR notes (non-blocking). Within the frozen scope the candidate's statements are correct as independently reconstructed and exactly controlled.**

Exact scope reviewed (manifest `scope`): for every nonzero product `C = X1⊗X2⊗X3` of rank ≤ 2 in the original d=4 domain, the original unnormalized `q3` equals `∏_i (‖X_i‖² − |Tr X_i|²/2)`, is ≥ 0, and vanishes iff exactly one factor is a nonzero scalar multiple of a rank-2 orthogonal projection while the other two have rank 1; hence nonzero (normalizable) equality operators exist in the original domain and **no** universal constant δ>0 with `q3(C) ≥ δ‖C‖²` on the whole rank ≤ 2 domain can exist.

Everything outside that scope is a **non-claim** of this review (see §7).

## 1. Input verification (performed before any interpretation)

Observed clock at verification: `2026-10-28T21:45:05-0700 PDT`. All three inputs recomputed with `shasum -a 256`, `wc -c`, `wc -l`; every SHA-256, byte count and LF count matched the manifest exactly.

| # | input (read order) | role | SHA-256 | bytes | LF |
|---|---|---|---|---|---|
| 1 | `…/werner3-ququart/frontier-20261028-d4-consolidated-proof-dossier-v3.md` | definitions/context only; **not adopted** | `5fd7eae54aecf154113461982fb429704dfe0cf53bbc786281c54356e280b223` | 12290 | 89 |
| 2 | `…/werner3-ququart/frontier-20261028-d4-original-q3-product-equality-v1.md` | main candidate | `b4d5f2673d9a2d605681f627e3ad2da943c68b010313c377d6d6fd4b6bd5fb1a` | 4454 | 42 |
| 3 | `…/werner3-ququart/frontier-20261028-d4-q3-product-formal-check-results.json` | author check result; **read/hash only, not evidence** | `5a532f1c4787032b975e52c6e335cbbe48ea7b0eeeed4fa21f4a8b92e0035758` | 394 | 9 |

All three were read completely (`:raw` full ranges) in the declared order. No author code was imported, read for method, or executed. No web search, external model, author contact, Git, deletion or publication occurred. The author JSON's `"verdict": "PASS"` played no role in the verdict below.

## 2. Definition extracted from the dossier (the only thing taken from input 1)

Dossier v3 §1 defines, for `H=(C⁴)^⊗3` and **every complex** `C:H→H` with rank ≤ 2 (explicitly including 0, rank 1, singular, nonnormal, non-Hermitian), the **unnormalized-trace** functional

```
q3(C) = ‖C‖²_HS − (1/2) Σ_i ‖Tr_i C‖²_HS + (1/4) Σ_{i<j} ‖Tr_ij C‖²_HS − (1/8) |Tr C|² .
```

`Tr_S` is the unnormalized partial trace over the sites in `S`; all norms are Hilbert–Schmidt. The dossier's theorems (certificate, positivity, identity audits, etc.) are **not** used as premises anywhere below; this review would read identically if every dossier theorem were false.

## 3. Independent reconstruction of every load-bearing step

Notation: `n_i = ‖X_i‖²`, `t_i = |Tr X_i|²`, `g(X) = ‖X‖² − |Tr X|²/2`.

**3.1 Partial trace of a product.** The unnormalized partial trace is the linear map fixed on product operators by `Tr_S(⊗_i A_i) = ∏_{i∈S} Tr(A_i) · ⊗_{i∉S} A_i`. Hence `Tr_i C = Tr(X_i)·⊗_{j≠i}X_j`, `Tr_ij C = Tr(X_i)Tr(X_j)·X_k`, `Tr C = ∏Tr(X_i)`. Candidate §1 formula: **correct.**

**3.2 HS multiplicativity.** `‖A⊗B‖² = Tr(A†A⊗B†B) = ‖A‖²‖B‖²`. So `‖Tr_S C‖² = ∏_{i∈S} t_i · ∏_{i∉S} n_i` for each of the 8 subsets `S`.

**3.3 Eight-term bookkeeping.** Substituting 3.2 into the definition gives
`n1n2n3 − ½(t1n2n3+n1t2n3+n1n2t3) + ¼(t1t2n3+t1n2t3+n1t2t3) − ⅛ t1t2t3`, which is literally the expansion of `∏_i (n_i − t_i/2)`. The identity holds for **arbitrary complex** 4×4 `X_i`: no rank, Hermiticity, normality or product-vector hypothesis is used (candidate §1 says so; confirmed, and exercised with non-normal rank-2 and rank-4 factors in control B10/B11). Candidate eq. (1): **correct.**

**3.4 Rank pattern.** `rank(⊗X_i) = ∏rank(X_i)`. If `C≠0` each `X_i≠0`, so each rank ≥ 1; `∏r_i ≤ 2` with 2 prime leaves exactly `(1,1,1)` or one factor of rank 2 and the others rank 1 (control C1 enumerates `{1..4}³`). Candidate §2 first paragraph: **correct.**

**3.5 Inequality (2).** For nonzero `X` of rank `r` with SVD `X = Σ_{j≤r} s_j |u_j⟩⟨v_j|`, `s_j>0`, orthonormal `{u_j}`, `{v_j}`: `Tr X = Σ_j s_j ⟨v_j|u_j⟩`, so `|Tr X| ≤ Σ_j s_j |⟨v_j|u_j⟩| ≤ Σ_j s_j = ‖X‖₁ ≤ √r (Σ s_j²)^{1/2} = √r ‖X‖_HS` (Cauchy–Schwarz against the all-ones vector of length `r`). Thus `g(X) ≥ (1 − r/2)‖X‖²`: for `r=1`, `g ≥ ‖X‖²/2 > 0`; for `r=2`, `g ≥ 0`. **Correct.**

**3.6 Nonnegativity on the product subdomain.** By 3.3–3.5 every factor `g(X_i) ≥ 0`, so `q3(C) ≥ 0` for every product of rank ≤ 2; for pattern `(1,1,1)`, `q3(C) ≥ ‖C‖²/8 > 0`. (The rank hypothesis is load-bearing: `g(diag(1,1,1,0)) = −3/2`, control B9 gives `q3 = −3/8 < 0` for a rank-3 product, which is outside the domain.) **Correct.**

**3.7 Rank-2 equality class.** Let `rank X = 2` and `g(X)=0`, i.e. `|Tr X|² = 2(s1²+s2²)`. Then every inequality in 3.5 is an equality: (a) `s1+s2 = √2·√(s1²+s2²)` forces `s1 = s2 =: s`; (b) `|⟨v_j|u_j⟩| = 1` for both `j` forces `u_j = e^{iθ_j} v_j`; (c) `|s e^{iθ1} + s e^{iθ2}| = 2s` forces `θ1 = θ2 =: θ`. Hence `X = s e^{iθ}(|v1⟩⟨v1| + |v2⟩⟨v2|) = λP`, `λ≠0`, `P` the orthogonal (Hermitian idempotent) projection onto `span{v1,v2}`, rank 2. No uniqueness of the SVD is needed (the argument applies to any chosen SVD). Conversely for `X=λP`: `‖X‖² = 2|λ|²`, `|Tr X|² = 4|λ|²`, `g = 0`. Candidate §2 "iff": **correct** (both directions).

**3.8 Combined classification.** `q3(C) = ∏g(X_i)` with all factors ≥ 0 vanishes iff some `g(X_i)=0`, which by 3.5/3.7 happens iff that `X_i` has rank 2 and equals `λP`; by 3.4 the other two then have rank 1. Candidate §2 bold statement: **correct.**

**3.9 Existence, homogeneity, no universal δ.** `P12 = diag(1,1,0,0)` and `E00` exist on `C⁴`; `C₀ = P12⊗E00⊗E00` has rank 2, `‖C₀‖² = 2`, `q3(C₀) = 0` (control B1/B13, exact). `q3(λC) = |λ|²q3(C)` because each of the eight terms is quadratic in `C`, so `C₀/√2` is a normalized equality operator in the original domain. Any δ>0 with `q3(C) ≥ δ‖C‖²` for all rank ≤ 2 `C` would give `0 ≥ 2δ`, contradiction. Even the weaker "q3(C) > 0 for all nonzero rank ≤ 2 `C`" fails. Candidate §3 first paragraph: **correct.**

**3.10 Conditional infimum remark.** Candidate §3 states that the normalized global infimum equals 0 *only if* full nonnegativity on the whole (nonproduct) domain is accepted. Logically correct as a conditional; this review verifies neither full nonnegativity nor the infimum value (non-claim).

## 4. Independently authored exact control (actually run)

Artifacts (reviewer-owned, this directory):

| artifact | SHA-256 | bytes | LF |
|---|---|---|---|
| `reviewer-q3-product-control-v1.py` | `9b25c3182c491c9770cb666d172625748795e977952f01c11f66f3d52ca06e83` | 14842 | 258 |
| `reviewer-q3-product-control-run-v1.txt` (stdout via `tee`) | `27d53d1c1c3bcd9a9cf1e377202d4742f0550fac022efefd53b2594509b5b3e7` | 3172 | 19 |

Run receipt: Python 3.14.3 on Darwin 27.0.0 arm64; clock before run `2026-10-28T21:51:31-0700 PDT`, after run `2026-10-28T21:51:32-0700 PDT`; exit status 0; **18/18 checks PASS**; wall ≈ 1.1 s. Pure standard library (`fractions`, `itertools`, `json`), exact Gaussian-rational arithmetic (`Fraction` pairs); no NumPy, no floating point, no author code.

Design (written from the §2 definition only):
- **Check A (formal, 6 variables).** Hand-rolled polynomial dictionaries over `Q`: `q3_formal(n,t)` built term-by-term from the definition via 3.1–3.2 equals `∏(n_i − t_i/2)` with exactly 8 monomials and coefficient multiset `{1, −½×3, ¼×3, −⅛}`. **Negative controls:** flipping the single-trace sign (A2) or using pair coefficient ½ instead of ¼ (A3) each produce 3 differing monomials → detected.
- **Check B (concrete, 64×64).** `q3_direct` evaluates the definition literally on the explicit Kronecker matrix with partial traces computed entry-by-entry over the traced indices (never via the product structure), then is compared **exactly** to `∏g(X_i)`; exact rank over `Q(i)` certifies domain membership.

| case | factors (site 1 ⊗ 2 ⊗ 3) | q3 (direct = product) | ‖C‖² | rank | expectation |
|---|---|---|---|---|---|
| B1 | `P12 ⊗ E00 ⊗ E00` | `0` | 2 | 2 | equality ✓ |
| B2 | `(1+2i)·U P12 U† ⊗ |e0⟩⟨e1| ⊗ |u⟩⟨v|` (U rational unitary ⅕[[3,4i],[4i,3]] on coords 1,2; non-diagonal projection; non-normal rank-1 factors) | `0` | 660 | 2 | equality ✓ |
| B3 | projection factor moved to site 3 | `0` | 45100/147 | 2 | equality ✓ |
| B4 | projection factor on site 2 | `0` | 2050/441 | 2 | equality ✓ |
| B5 | **oblique** idempotent `E00+E01+E22` (rank 2, Tr 2, not Hermitian) ⊗ rank-1 ⊗ rank-1 | `131/2 > 0` | 198 | 2 | non-equality; reason: orthogonality broken ✓ |
| B6 | `diag(1,½,0,0)` ⊗ rank-1 ⊗ rank-1 | `131/32 > 0` | 165/2 | 2 | non-equality; reason: `s1≠s2` ✓ |
| B7 | `diag(1,i,0,0)` ⊗ rank-1 ⊗ rank-1 | `1/2 > 0` | 2 | 2 | non-equality; reason: phase mismatch ✓ |
| B8 | three rank-1 factors | `26855/1764 > 0` | 4510/147 | 1 | strictly positive ✓ (B14: `≥ ‖C‖²/8` ✓) |
| B9 | `diag(1,1,1,0)` ⊗ `E00` ⊗ `E00` | `−3/8 < 0` | 3 | 3 | outside domain; rank hypothesis load-bearing ✓ |
| B10 | generic non-normal complex rank-2 ⊗ rank-1 ⊗ rank-1 | `21615/4 > 0` | 6666 | 2 | factorization exact ✓ |
| B11 | generic rank-4 ⊗ rank-2 ⊗ rank-1 | `−21615/4` | 326634 | 8 | outside domain; identity still exact ✓ |
| B12 | corrupted evaluator (pair coefficient ½) on an equality-class product | direct `1345` ≠ product `0` | — | — | corruption detected ✓ |
| B13 | `q3(C₀)/‖C₀‖²` for B1 | `0` exactly | 2 | — | normalized ratio 0 ✓ |
- **Check C.** Enumeration of `(r1,r2,r3) ∈ {1..4}³` with product ≤ 2 yields exactly `(1,1,1),(1,1,2),(1,2,1),(2,1,1)`.

Hand spot-checks of control values (independent of the script): `g(P12)=2−4/2=0`; `g((1+2i)P_u)=10−20/2=0`; `g(|u⟩⟨v|)` for `u=(1,2,i,0)`, `v=(1,−1,0,3i)`: `66−|−1|²/2=131/2`; `g(E00+E01+E22)=3−4/2=1`; `g(diag(1,½,0,0))=5/4−9/8=1/8`; `g(diag(1,i,0,0))=2−|1+i|²/2=1`; `g(diag(1,1,1,0))=3−9/2=−3/2`. All agree with the run output.

## 5. Findings

- **F1 (none / correct).** Factorization `q3(X1⊗X2⊗X3)=∏g(X_i)` — reconstructed (3.1–3.3), formally checked (A1) and concretely checked on 11 explicit operators (B1–B11) in exact arithmetic.
- **F2 (none / correct).** Nonnegativity on rank ≤ 2 products and strict positivity for all-rank-1 — reconstructed (3.4–3.6), controlled (B5–B9).
- **F3 (none / correct).** Rank-2 equality class = nonzero scalar × rank-2 orthogonal projection — reconstructed with both directions and the three forced equalities (3.7); positive cases B1–B4 (including a non-diagonal projection with complex scalar), intended-reason negatives B5–B7 each breaking exactly one hypothesis.
- **F4 (none / correct).** Existence of normalized equality operators in the original domain and impossibility of a universal δ>0 — reconstructed (3.9), controlled (B1, B13).
- **MINOR-1 (exposition).** Candidate §2 compresses three distinct forced equalities (`s1=s2`; `|⟨v_j|u_j⟩|=1`; common phase) into one sentence ("equality in the triangle/inner-product inequalities … thus `u_j=e^{iθ}v_j` … same phase"). The conclusion is right; a reader must supply the triangle-equality step (c) in 3.7. No change to the result.
- **MINOR-2 (out-of-scope attribution, unverified).** The candidate's header sentence that "the earlier public Tomar v4 source already states a sharpness/equality clause for dimensions at least 2" was **not** verified here (no source path given in the manifest; web search prohibited). It is not load-bearing for any mathematical statement in scope and the candidate already disclaims priority; this review makes no statement about Tomar's content.
- **MINOR-3 (evidence boundary of the author artifact).** Input 3 (author JSON) by its own `scope` field covers only the formal 8-monomial expansion, i.e. it does not by itself check the partial-trace lemma 3.1, HS multiplicativity 3.2, the SVD argument, or any concrete operator. The candidate text does not overclaim it, and the present review does not rely on it; recorded so that downstream consumers do not cite that JSON as a check of §§2–3 of the candidate.

No step of the candidate within scope was found incorrect, circular, or dependent on the dossier's unadopted theorems or on any held/quarantined output. The candidate's §4 provenance boundary states that only the q3 definition, tensor identities and SVD are used; the mathematics indeed needs nothing else (same-harness, not a provenance audit).

## 6. Load-bearing dependencies of this verdict

1. The quoted dossier §1 text is the "original unnormalized q3" (taken as the frozen definition; the verdict is relative to that text — under a *normalized*-partial-trace convention the eight coefficients would change and nothing here transfers).
2. Standard facts: partial trace on product operators (3.1), HS multiplicativity (3.2), rank multiplicativity of Kronecker products (3.4), SVD existence and Cauchy–Schwarz (3.5).
3. Trust base of the control: Python 3.14.3 `fractions.Fraction` exactness, the reviewer's own 258-line script (hashed above), `shasum`/`wc`/`/bin/date` on this macOS host. The control is bounded (finite explicit operators) and supports, but does not replace, the written proof in §3; the universal statements rest on §3.
4. Same-harness only: no human, independent-model-family, formal/kernel or novelty verification is provided or implied.

## 7. Explicit non-claims

- **No nonproduct positivity:** nothing here says `q3(C) ≥ 0` for nonproduct rank ≤ 2 `C`; the dossier's certificate/positivity program is not adopted, reviewed, or contradicted.
- **No global classification:** the equality class is characterized **only among product operators**; the set of all rank ≤ 2 `C` with `q3(C)=0` is not characterized.
- **No infimum value:** that the normalized infimum over the whole domain equals 0 is **not** asserted (it would need full nonnegativity).
- **No novelty/priority, no all-d, no operational/distillability, no f62/parent adoption, no human/model-family/formal acceptance.**
- The phrase "falsified premise" is verified only in the mathematical sense that the universal statement `∃δ>0 ∀C: q3(C) ≥ δ‖C‖²` is false on the original domain; who, if anyone, held that premise is not assessed.

## 8. Review-directory artifacts written by this reviewer

- `review-v1.md` (this file)
- `reviewer-q3-product-control-v1.py` — SHA256 `9b25c3182c491c9770cb666d172625748795e977952f01c11f66f3d52ca06e83`
- `reviewer-q3-product-control-run-v1.txt` — SHA256 `27d53d1c1c3bcd9a9cf1e377202d4742f0550fac022efefd53b2594509b5b3e7`

No other file inside or outside this directory was created, modified or deleted.
