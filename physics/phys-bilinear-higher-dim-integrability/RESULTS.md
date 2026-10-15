# Results

Verdict: **SOLVED** for the approved C6 all-N odd-cubic Pfaffian formula (Theorem 9.1;
Certification, not a novelty claim). The unrestricted book conjecture remains **PARTIAL**,
and its single-function generic-Hirota-property reading has a **COUNTEREXAMPLE**.
A failed three-soliton test does not by itself exclude a Lax pair. FRONTIER state:
DELIVERY-READY for the scoped written proof; NOVELTY-UNCLEAR for prior-art positioning.

**Final openness gate (2026-10-14): PARTIAL-OVERLAP.** C9 was previously unproved
in this project. No inspected primary source establishes that this precise formula
was previously open in the literature, and high-risk full texts remain inaccessible.
Theorem 9.1 is a Certification, not a certified solution of a previously open problem.
The user's “not solved yet” selection criterion is unconfirmed; STATUS.md's final gate
table and `results/openness-gate-20261014.json` record the evidence boundary.

All load-bearing computations are exact (rational numbers or sympy rational-function fields). Floating point
is used only in the exploratory scan C8, which is labelled Empirical evidence.

## 0. Precise formulations

**Hirota operators.** For a polynomial `B(D_x, D_y, D_t)` and wave vectors `κ = (k, l, w)`,
`B(D) e^{κ·z}·e^{κ'·z} = B(κ − κ') e^{(κ+κ')·z}`, `z = (x, y, t)`. Hence for
`F = Σ_S F_S e^{η_S}`, `G = Σ_S G_S e^{η_S}` (`S ⊆ {1..N}`, `η_S = Σ_{i∈S} η_i`, `η_i = κ_i·z + const`) the
coefficient of `e^{Σ n_i η_i}`, `n ∈ {0,1,2}^N`, in `B(D)F·G` is `C_B(n) = Σ_{μ+ν=n} F_μ G_ν B(κ_μ − κ_ν)`.

**Systems.** `P` is a polynomial in `(D_x, D_t)` with `P(0) = 0`.

    (1)  P F·G = 0,  D_x P F·G = 0          (2)  P F·G = 0,  D_y P F·G = 0

A linear `Q = αD_x + β` (α ≠ 0) gives the same system as `Q = D_x`, because the second equation equals
`α D_x P F·G + β P F·G` and the first equation removes the β-term; likewise for `R`. So "Q and R of the
same linear form" means Q = D_x, R = D_y.

**The class 𝒫.** `P = D_t + p(D_x)`, `p` a polynomial with `p(0) = 0` and `deg p ≥ 2`. It contains Li & Lou's
family (7) (`p = k^n`) and their models (ii) n = 2 and (iii) n = 3. It does not contain their model (i),
`P = D_x D_t`.

**One-soliton seeds.** `F = 1 + a e^{η}`, `G = 1 + b e^{η}` solves (1) or (2) iff
`P(κ)a + P(−κ)b = 0` and `M(κ)[P(κ)a − P(−κ)b] = 0`, where `M(κ) = k` for (1) and `M(κ) = l` for (2).
For `M(κ) ≠ 0` this means `P(κ)a = 0 = P(−κ)b`. For `P ∈ 𝒫` a seed is therefore of

- F type: `a ≠ 0, b = 0, w = −p(k)`;
- G type: `a = 0, b ≠ 0, w = p(−k)`;
- two-amplitude type (a, b free): only if `p(k) + p(−k) = 0`, i.e. for all k iff p is odd.

Seeds with `M(κ) = 0` are excluded as non-generic. For (2) they are the y-independent modes (`l = 0`, w free,
`a/b = −P(−κ)/P(κ)`): on y-independent functions the second equation of (2) vanishes identically, so (2)
collapses to the single underdetermined equation `P F·G = 0` (linear in F for any given G), and the recursion
has zero determinants. These modes say nothing about (2) as a genuinely (2+1)-dimensional system.

**Generic N-soliton test (two-function systems).** Fix N seeds of given types with generic parameters
(`k_i`, for (2) also `l_i`, amplitudes). For every `S` with `|S| ≥ 2`, the two equations `C_{B_1}(1_S) =
C_{B_2}(1_S) = 0` (`B_1 = P`, `B_2 = MP`) are linear in `(F_S, G_S)` with determinant
`−2 M(κ_S) P(κ_S) P(−κ_S)`; when it is nonzero they fix `F_S, G_S` uniquely. The system *passes the test for
a type pattern* if then every coefficient `C_{B_j}(n)`, `n ∈ {0,1,2}^N`, vanishes identically as a rational
function of the free parameters. It *passes the generic N-soliton test* if it passes for every type pattern
(for odd p: two free amplitudes per soliton, which contains all F/G patterns as specialisations). The
**three-soliton test (3ST)** is N = 3. Failing means: for generic parameters there is no solution of the
form above with these seeds.

**Single-function test.** For even `B`, Hirota's ansatz `f = Σ_S Π_{i<j∈S} A_ij e^{η_S}`,
`A_ij = −B(κ_i − κ_j)/B(κ_i + κ_j)`, `B(κ_i) = 0`; `B(D)f·f = 0` passes the 3ST if all coefficients vanish
identically.

**Readings of the conjecture.**

- **(R-sys)**, the literal reading: if (1) passes the generic N-soliton test for every N, so does (2).
  **(R-sys-3)**: the same statement with N = 3 only.
- **(R-eq)**, the single-function reading: for odd P and odd Q, if `Q(D_x)P f·f = 0` is integrable then
  `Q(D_y)P f·f = 0` is integrable. Because `P f·f ≡ 0` for odd P, these are exactly the F = G reductions of
  (1) and (2). Here "integrable" for the premise is taken in any of the usual strong senses (Lax pair and
  N-soliton solutions for all N); the conclusion is refuted by failure of the 3ST.

**What these readings do not cover.** Integrability that is invisible to exponential solitons (for
`P = D_x D_t` the seed conditions force `kw = 0`, so this test is degenerate); integrability defined by Lax
pairs or symmetries alone; supersymmetric and q-deformed operators S. The discrete case is touched in C7.

## 1. Claims

| ID | Claim | Evidence label | Novelty status | Verification command (from `code/`) |
|---|---|---|---|---|
| C1 | Diagonal reduction: (2) passes the generic N-soliton test ⇒ (1) passes it (any P, any N). | Certification (proof, §2) | Elementary; not found stated | proof only |
| C2 | For odd P, the two-function test of (1) or (2) at `a_i = b_i` is Hirota's single-function test of `MP f·f = 0`; single-function 3ST failure implies two-function 3ST failure. | Certification (proof, §2) | Elementary | proof only |
| C3 | For `P ∈ 𝒫` with `deg p ≤ 3`, (1) and (2) pass the generic 3ST (two amplitudes for odd p; all 8 F/G patterns otherwise). | Certification (86 exact symbolic identities) | Odd cubic pair appears as Eq. (37) in Hietarinta's primary 1997 account; Peng2008 abstract reports related N-solitons, but its exact family is uninspected. NOVELTY-UNCLEAR | `python two_function_3ss.py` (Part A) |
| C4 | For `P ∈ 𝒫` with `deg p ≥ 4`, (1) and (2) both fail the generic 3ST (the F F G pattern fails). Hence in 𝒫: (1) passes ⇔ (2) passes ⇔ `deg p ≤ 3`; Li–Lou's (7) passes only for n = 2, 3. | Certification (proof §2 + exact computation) | Consistent with the mKdV-type list in Hietarinta's primary 1997 account; original search-space attribution and priority remain unverified | `python two_function_3ss.py` (Parts B–D) |
| C5 | (R-eq) is false in the Hirota sense: `D_x(D_t + D_x^5) f·f = 0` (Sawada–Kotera) is integrable, `D_y(D_t + D_x^5) f·f = 0` fails the 3ST; with lower terms `c1 D_x + c3 D_x^3` the D_x-equation still passes the 3ST and the D_y-equation fails for every `c5 ≠ 0`. | Certification (exact symbolic residual, rational witness, independent direct substitution); the c1 = c3 = 0 obstruction reproduces Wang et al. 2024, Eq. (16) | Counterexample framing NOVELTY-UNCLEAR; core computation is a Reproduction | `python single_function_3ss.py`; `python direct_substitution_check.py` |
| C6 | Beyond three solitons in the passing class: N = 4, 5 at exact sample points; conjectured Pfaffian closed form matching the recursion for N ≤ 7 at sample points; symbolic N = 4 status in §2. | Empirical evidence (exact arithmetic, finitely many points); symbolic N = 4 see §2 | Closed form: not found in sources read | `python n_soliton_checks.py` |
| C7 | A discrete extra dimension, `R(S) = sinh(D_n)`, passes the 3ST for `deg p ≤ 3` and fails it for every `deg p ≥ 4`. | Certification (N = 3 symbolic identities; failure by a continuum-limit proof from C4, plus exact failing points) | NOVELTY-UNCLEAR | `python discrete_variant.py` |
| C8 | Outside 𝒫 (P with `D_t^2`, `D_x^j D_t` terms; Q ∈ {D_x, D_x^3, D_x + D_x^3}, R = Q(D_y)) no type pattern was found where (1) passes and (2) fails. | Empirical evidence (60-digit floats, 3 random points per pattern) | — | `python exploratory_scan.py` |
| C9 | The C6 amplitude-polynomial Pfaffian formula solves both coupled equations for every finite N, `P=Dt+c1Dx+c3Dx^3`, `c3≠0`, arbitrary independent amplitudes including zeros, and nonzero pair-sum denominators. | Certification (dimension-independent proof, §6; exact replay controls) | NOVELTY-UNCLEAR: Hietarinta equation identified; Peng full-family comparison unavailable | `python code/all_n_pfaffian.py` (from target root) |

## 2. Statements and proofs

### C1. Diagonal reduction

*Claim.* If `(F, G)(x, y, t) = (F̃, G̃)(x + y, t)` solves (2), then `(F̃, G̃)(x, t)` solves (1). Consequently,
if (2) passes the generic N-soliton test for a type pattern, so does (1).

*Proof.* For functions of `s = x + y` and t, `∂_y = ∂_x = ∂_s`, so `D_y P(D_x, D_t)F·G = D_x P(D_x, D_t)F·G`,
both evaluated at `s`; the first equations coincide. For the test: the seed conditions do not involve M
(for `M(κ) ≠ 0`), so seeds of (2) with `l_i = k_i` are seeds of (1), and the recursion and residuals of (2) at
`l_i = k_i` are literally those of (1) (the multiplier `λ_μ − λ_ν` becomes `k_μ − k_ν`). The residuals of (2)
are zero rational functions; the specialisation `l = k` keeps the determinants `−2 k_S P(κ_S)P(−κ_S)`
nonzero polynomials, so the residuals of (1) vanish identically. ∎

### C2. The F = G sector

*Claim.* Let P be odd and `M ∈ {D_x, D_y}`. With seeds `a_i = b_i`, the recursion gives `F_S = G_S` for all S,
and these coefficients are those of the single-function recursion for `MP f·f = 0`. For N = 3 the
single-function recursion passes iff Hirota's product ansatz passes.

*Proof.* Induction on |S|. If `F_T = G_T` for `|T| < |S|`, the first equation at `n = 1_S` reads
`P(κ_S)(F_S − G_S) + Σ_{T≠∅,S} F_T F_{S∖T} P(κ_T − κ_{S∖T}) = 0`; the sum vanishes because the terms `T` and
`S∖T` cancel (P odd), so `F_S = G_S` (as `P(κ_S) ≠ 0`). The second equation is then the single-function
equation for `B = MP`. For N = 3 the single-function residual at `n = (2,1,1)` equals
`2[f_1 f_123 B(κ_2+κ_3) + f_12 f_13 B(κ_2−κ_3)]`, which vanishes iff `f_123 = A_12A_13A_23 f_1f_2f_3`
(given `f_1 B(κ_2+κ_3) ≠ 0`), i.e. iff the product ansatz satisfies the `(1,1,1)` equation, which is
Hirota's condition; for the product ansatz all coefficients with an entry 2 vanish automatically. ∎

So if `MP f·f = 0` fails the 3ST, the two-function system fails the 3ST (at `a_i = b_i`, hence generically).

### C3. `deg p ≤ 3` passes (both systems)

`two_function_3ss.py`, Part A, runs the two-function recursion in the field
`ℚ(k_i, l_i, a_i, b_i, c_1, c_2, c_3)` and finds every residual coefficient identically zero for

- `p = c1 k + c3 k^3` with two free amplitudes per soliton, for (1) and for (2);
- `p = c1 k + c2 k^2 + c3 k^3` and `p = c1 k + c2 k^2`, each of the 8 F/G patterns, for (1) and (2);
- the specialisations `k^3`, `k^3 − 2k` (two-amplitude) and `k^2`, `k^3 + k^2`, `3k^2 + k` (all patterns).

Printed: `Part A: 86 symbolic three-soliton identities, nonzero residual sets: none`.

Specialisation to any particular p with `deg p ∈ {2, 3}` is legitimate: the only denominators are the
determinants `−2M(κ_S)P(κ_S)P(−κ_S)`, and for `deg p = d ≥ 2` each `P(±κ_S)`, `|S| ≥ 2`, is a nonzero
polynomial in the `k_i`: its top-degree part `c_d[(Σ_{i∈S} ε_i k_i)^d − Σ_{i∈S} ε_i σ_i k_i^d]` (`σ_i = ±1`
from the seed type) contains, for `i ≠ j ∈ S`, the monomial `k_i^{d−1} k_j` with coefficient `±d c_d ≠ 0`.

### C4. `deg p ≥ 4` fails (both systems); classification in 𝒫

**Lemma 4.1 (F F G pattern).** Let P be any polynomial with `P(0) = 0` and `M ∈ {D_x, D_y}`, with values
`m_i = M(κ_i)` (`k_i` or `l_i`). Take solitons 1, 2 of F type (`P(κ_1) = P(κ_2) = 0`, `b_1 = b_2 = 0`) and
soliton 3 of G type (`P(−κ_3) = 0`, `a_3 = 0`). Assume `m_S ≠ 0` and `P(±κ_S) ≠ 0` for
`S ∈ {12, 13, 23, 123}`. Then the coefficient of `e^{2η_1+η_2+η_3}` in `P(D)F·G` equals

    a_1^2 a_2 b_3 m_3 Φ / ( m_123 P(−κ_123) P(−κ_13) ),
    Φ = P(κ_2−κ_3) P(κ_1−κ_2−κ_3) P(−κ_1−κ_3) + P(κ_1−κ_3) P(κ_2−κ_1−κ_3) P(−κ_2−κ_3).

In particular, if `a_1 a_2 b_3 m_3 ≠ 0` and `Φ ≠ 0`, the system fails the 3ST, and the criterion `Φ ≠ 0` does
not depend on M. (Without `m_3 ≠ 0` the coefficient vanishes: for `p = k^4`, `k = (1, 2, −4)` and system (2),
`l = (1, 3, 0)` gives zero residuals although `Φ = −672768`, while `l = (1, 3, 7)` gives five nonzero ones;
a seed with `l_3 = 0` is in any case excluded by the seed definition in §0.)

*Proof.* Level 12: the lower terms `F_1G_2`, `F_2G_1` vanish, so `F_12 = G_12 = 0`. Level 13 (only `F_1G_3`
contributes): `F_13P(κ_13) + G_13P(−κ_13) = −a_1b_3P(κ_1−κ_3)` and
`m_13[F_13P(κ_13) − G_13P(−κ_13)] = −a_1b_3 (m_1−m_3) P(κ_1−κ_3)`; subtracting and using
`m_13 − (m_1 − m_3) = 2m_3` gives `G_13 P(−κ_13) = −a_1b_3 P(κ_1−κ_3) m_3/m_13`. Likewise
`G_23P(−κ_23) = −a_2b_3P(κ_2−κ_3)m_3/m_23`.
Level 123: only `T = 1` (`a_1G_23`) and `T = 2` (`a_2G_13`) contribute besides `F_123, G_123`. With
`X = a_1G_23P(κ_1−κ_2−κ_3)`, `Y = a_2G_13P(κ_2−κ_1−κ_3)` the two equations give
`G_123P(−κ_123) = −[X m_23 + Y m_13]/m_123`, i.e.
`G_123 = a_1a_2b_3 m_3 Φ / (m_123 P(−κ_123)P(−κ_13)P(−κ_23))`. At `n = (2,1,1)` the pairs are
`(123, 1)` (contains `G_1 = 0`), `(12, 13)`, `(13, 12)` (contain `F_12 = G_12 = 0`) and `(1, 123)`, so the
coefficient is `a_1G_123P(−κ_23)`. ∎

`two_function_3ss.py`, Part B, re-derives this identity with every value `P(Σ ε_iκ_i)` an independent symbol
(only the dispersion relations imposed) and arbitrary `m_i`: printed `closed form ... True`.

**Lemma 4.2 (monomials).** Let `p = k^d` and `(k_1, k_2, k_3) = (1, 2, −4)` with types F, F, G, so
`w = (−1, −2^d, 4^d)`. Then

    Φ_d = (6^d − 4^d − 2^d)(3^d + 2^d − 4^d − 1)(3^d + 1 − 4^d) + (5^d − 4^d − 1)(5^d − 4^d − 2^d + 1)(2^{d+1} − 4^d),

`Φ_2 = Φ_3 = 0` and `Φ_d < 0` for every `d ≥ 4` (`Φ_4 = −672768`). The hypotheses of Lemma 4.1 hold for all
`d ≥ 2`, for (1) (`k_12, k_13, k_23, k_123 = 3, −3, −2, −1`) and for (2) with `l = (1, 3, 7)`.

*Proof.* `4 ≤ d ≤ 60`: exact integer evaluation (Part C). `d ≥ 30`: the first product is positive and
`< 6^d·4^d·4^d = 96^d` (its last two factors are negative with absolute values `< 4^d`). In the second product,
for `d ≥ 4` the first two factors are `≥ 5^d − 2·4^d > 0` and the last is `≤ −4^d/2`, so it is
`≤ −100^d (1 − 2·0.8^d)^2 / 2`. Hence `Φ_d < 0` whenever `(1 − 2·0.8^d)^2 ≥ 2·0.96^d`; this holds at d = 30
(checked exactly) and the left side increases and the right side decreases with d. Nondegeneracy:
`P(κ_12) = 3^d − 2^d − 1 > 0`; `P(−κ_12) = 1 + 2^d + (−3)^d ≠ 0`; `P(κ_13) = 4^d − 1 + (−3)^d > 0`;
`P(−κ_13) = 1 + 3^d − 4^d < 0`; `P(κ_23) = 4^d − 2^d + (−2)^d > 0`; `P(−κ_23) = 2^{d+1} − 4^d < 0`;
`P(κ_123) = 4^d − 2^d − 1 + (−1)^d > 0`; `P(−κ_123) = 2 + 2^d − 4^d < 0` (all for `d ≥ 2`, `d ≥ 3` where
needed); Part C rechecks them for `d ≤ 60`. ∎

Part C also recomputes the full recursion for `d = 4, …, 9` for (1) and for (2) and confirms that the engine's
`(2,1,1)` residual equals the closed form and is nonzero.

**Lemma 4.3 (lower-order terms).** Let `deg p = d ≥ 4` with leading coefficient `c_d`. At the configuration
`s·(1, 2, −4)` (and `l = (1, 3, 7)` for (2)), each `P(±κ_S)` and each factor of Φ is a polynomial in s of
degree ≤ d whose `s^d` coefficient is `c_d` times the corresponding monomial value of Lemma 4.2. Hence
`Φ(s)` has `s^{3d}` coefficient `c_d^3 Φ_d ≠ 0`, every hypothesis of Lemma 4.1 holds for all but finitely many
s, and the 3ST fails. (Part D shows nonzero residuals for `k^5+k^2`, `k^4+k^3`, `k^6−3k^2+k`, `2k^5−k^3+k`,
`k^7+k^5+k^3` at s = 1, 2, 5, 20.) ∎

**Theorem 4.4 (classification in 𝒫).** For `P = D_t + p(D_x)`, `p(0) = 0`, `deg p ≥ 2`, the following are
equivalent: (a) (1) passes the generic 3ST; (b) (2) passes it; (c) `deg p ≤ 3`.

*Proof.* (c)⇒(b): C3. (b)⇒(a): C1. (a)⇒(c): if `deg p ≥ 4`, Lemmas 4.1–4.3 with `M = D_x` give an
F F G configuration with nonzero residual; F- and G-type seeds exist for every p, and for odd p they are
specialisations of the two-amplitude seeds. ∎ (Lemmas 4.1–4.3 with `M = D_y` show directly that (2) fails.)

**Corollaries.**

- *Li–Lou question (7).* `(D_t + D_x^n)F·G = 0, D_y(D_t + D_x^n)F·G = 0` passes the generic 3ST iff
  n ∈ {2, 3} (n = 1 is linear and degenerate). For n ≥ 4 this system and its (1+1)-dimensional counterpart
  fail the generic test: the F F G pattern has no solution of the stated form. Some multi-soliton families
  survive for every p — e.g. `F = 1 + Σ_i a_i e^{η_i}`, `G = 1` (all F type, a linear superposition) — and
  families with constrained parameters or other ansätze are not excluded. So for n ≥ 4 the model is not
  integrable in the sense of the generic Hirota multi-soliton property; the result says nothing about Lax or
  symmetry integrability. This answers, in that sense and negatively, the question left open in Li & Lou
  (2008), Section 4.
- *(R-sys-3) holds in 𝒫* with `R(S) = Q(D_y) = D_y`: the hypothesis and the conclusion hold for exactly the
  same P. The all-N statement (R-sys) in 𝒫 reduces to the open obligation in C6.

### C5. The single-function reading (R-eq) is false

Let `P_c = D_t + c1 D_x + c3 D_x^3 + c5 D_x^5` with `(c3, c5) ≠ (0, 0)` (for `c3 = c5 = 0` the equation is a
linear transport law, every phase ratio is `0/0` and the test is undefined).

1. `D_x P_c f·f = 0` passes the 3ST identically in `(k_i, c1, c3, c5)` (`single_function_3ss.py` (a):
   `nonzero three-soliton coefficients = 0`). For `c1 = c3 = 0` this is the Sawada–Kotera equation, whose
   N-soliton solutions for all N are classical (Sawada & Kotera 1974); this supplies the premise of (R-eq).
2. For `D_y P_c f·f = 0` the only nonzero three-soliton coefficient is the `e^{η_1+η_2+η_3}` one, equal to

       −200 c5^2 k1 k2 k3 (k1−k2)(k1−k3)(k2−k3) (6 c3 + 5 c5 (k1^2+k2^2+k3^2)) Λ
       ─────────────────────────────────────────────────────────────────────────────
       (l1+l2)(l1+l3)(l2+l3) Π_{i<j} (3 c3 + 5 c5 (k_i^2 + k_i k_j + k_j^2))

       Λ = (3c3 k1 + 5c5 k1^3) l2 l3 (l2^2 − l3^2) − (3c3 k2 + 5c5 k2^3) l1 l3 (l1^2 − l3^2)
           + (3c3 k3 + 5c5 k3^3) l1 l2 (l1^2 − l2^2).

   For `c5 = 0` (and `c3 ≠ 0`) it vanishes identically; for `c5 ≠ 0` it is a nonzero rational function for
   every `c1, c3` (Λ contains `5c5 k1^3 l2^3 l3`, which no `c3` term can cancel). For `c1 = c3 = 0`,
   `Λ = 5c5 ×` the left-hand side of Wang et al.'s constraint (16): the residual vanishes on the zero set of Λ,
   which for `c1 = c3 = 0` is their constraint (Reproduction); the factor `6c3 + 5c5Σk_i^2` is a second branch
   (complex k when `c3 = 0`).
3. Witness: `k = (1, 2, 3)`, `l = (1, 3, 7)`, `c = (0, 0, 1)`: coefficient `3600/247 ≠ 0` (engine), and the same
   value `3600/247` from `direct_substitution_check.py`, which builds f with the phase factors printed in
   Wang et al. (2024) and evaluates `D_y(D_t + D_x^5) f·f` by sympy differentiation from the definition of the
   Hirota derivative, without the coefficient formula of `hirota_ns.py`. Control: the Sawada–Kotera f at
   `k = (1, 2, 3)` gives no nonzero coefficient in both implementations.

By C2 the full two-function systems with `P = D_t + D_x^5` also fail the 3ST. So this is a counterexample to
(R-eq) — with "integrable" in the conclusion read as the Hirota multi-soliton property; a failed 3ST does not
exclude a Lax pair or constrained soliton families such as Wang et al.'s — but **not** to (R-sys): by C4 the
two-function system (1) with `P = D_t + D_x^5` already fails the 3ST (only its F = G sector passes; at
fixed rational points, of the eight sectors `b_i = ±a_i` only `b_i = a_i` passes for (1) and none for (2),
scratch check). The supersymmetric analogue — `S P τ·τ = 0` with `P = aX^5 + bX^3 + cX + T` admits
unconstrained three-super-soliton solutions only for `a = 0` — is reported by Delisle & Jaouadi
(arXiv:2609.14372); we did not verify it.

### C6. Initial finite-N evidence (odd-cubic obligation closed by C9)

The following records the initial conjecture, finite checks and unsuccessful expansions.
It is retained for provenance; C9 below supersedes the odd-cubic all-N limitation.

- Exact random points: `n_soliton_checks.py` evaluates the two-function recursion for N = 4 and N = 5 at three
  fixed-seed rational points each, for `P = D_t + D_x^3`, `D_t + 2D_x^3 − 3D_x` (two amplitudes),
  `D_t + D_x^2`, `D_t + D_x^3 + D_x^2 − D_x` (random F/G patterns), systems (1) and (2): all residuals zero
  (16 cases × 3 points = 48 evaluations). Controls (6 cases × 3 points): ANNV `D_y(D_t + D_x^3)` and
  Sawada–Kotera pass at N = 4, 5; the
  `D_y(D_t + D_x^5)` equation has 9 (N = 4) and 51 (N = 5) nonzero coefficients. This is Empirical evidence
  (exact arithmetic, finitely many points).
- Symbolic N = 4 for (2), `P = D_t + D_x^3`, two amplitudes: neither the recursion in
  `ℚ(k_i, l_i, a_i, b_i)` (stopped at 3500 s) nor the closed-form identity `n_soliton_checks.py --symbolic 4`
  in `ℚ(k_i, l_i, x_i)` (stopped at 2400 s) finished; no symbolic claim is made beyond N = 3 (the closed form
  passes symbolically at N = 3: `--symbolic 3` prints 0 nonzero coefficients).
- Conjectured closed form (odd cubic `p = c1k + c3k^3`, two amplitudes). With `x_i = a_i/b_i`,
  `b_S = Π_{i∈S} b_i`, `R_S(k) = Π_{i<j∈S} (k_i − k_j)/(k_i + k_j)` and the antisymmetric matrices

      M_ij = (x_i l_i − x_j l_j)/(l_i + l_j),  M_i0 = x_i;     N_ij = (x_j l_i − x_i l_j)/(l_i + l_j),  N_i0 = 1,

  the solution of (2) is `F_S = R_S(k) b_S Pf(M_{S'})`, `G_S = R_S(k) b_S Pf(N_{S'})`, where `S' = S` for
  `|S|` even and `S' = S ∪ {0}` (0 last) for `|S|` odd; for (1) put `l_i = k_i`. Examples:
  `F_12 = R_12(k)(a_1b_2l_1 − a_2b_1l_2)/(l_1+l_2)`, `F_1 = a_1`, `G_1 = b_1`. In the F = G sector
  (`x_i = 1`) Schur's Pfaffian identity gives `Pf(M_{S'}) = R_S(l)`, the known ANNV/KdV phase factors.
  `n_soliton_checks.py` confirms, at two fixed-seed rational points for each N = 3, …, 7 and each of the
  systems (1), (2) (`p = 2k^3 − 5k`), that this formula equals the recursive solution coefficient by
  coefficient and that all residual coefficients vanish. Empirical evidence for N ≥ 4 (symbolic only at N = 3).
- The all-N formula was previously unproved in this project. C9 now proves it for
  every N and arbitrary independent amplitudes, including zeros. The old timeouts above
  were not used as evidence for this conclusion. Peng et al.'s full-family comparison remains
  unverified because the full text was not reached. The mixed-parity case (`c2≠0`) is outside
  this resumed assignment; no claim about its subsequent status is made here.

### C7. Discrete extra dimension

For `(2d)`: `P F·G = 0`, `sinh(D_n) P F·G = 0` (on `e^{νn}` the multiplier is `sinh(ν_A − ν_C)`, rational in
`z_i = e^{ν_i}`), `discrete_variant.py` finds the three-soliton residuals identically zero in
`ℚ(k_i, z_i, amplitudes, c_j)` for `p = c1k + c3k^3` (two amplitudes) and `p = c1k + c2k^2 + c3k^3` (all 8
patterns), and nonzero residuals for `p = k^4`, `k^5`, `k^5 + k^2` at `k = (1, 2, −4)`, `z = (2, 3, 5)`.

*Proposition 7.1.* For every `p` with `deg p ≥ 4`, (2d) fails the 3ST. *Proof.* Take the configuration of
Lemmas 4.2–4.3 for (2) (`k = s(1, 2, −4)`, `l = (1, 3, 7)`, F F G seeds, s generic) and put `z_i = e^{ε l_i}`.
Divide the second equation of (2d) by ε: its multiplier `sinh(ε(λ_A − λ_C))/ε` is analytic in ε and tends to
`λ_A − λ_C`, the multiplier of (2). The recursion determinants tend to the nonzero determinants of (2), so
`F_S(ε), G_S(ε)` and the residuals are continuous at ε = 0 and tend to those of (2), whose `(2,1,1)`
coefficient is nonzero by Lemmas 4.1–4.3. Hence for all small ε ≠ 0 the residual of (2d) is nonzero at
`z_i = e^{εl_i}`, so it is not identically zero as a rational function of z. ∎

So within 𝒫, at the 3ST level, `R(S) = sinh(D_n)` passes exactly when `R(S) = D_y` does. (Exploratory remark:
for `P = D_t + D_x^3` the multiplier `φ(μ) − φ(ν)` works for additive φ (D_y) and multiplicative φ (shift),
but fails for their sum and for random φ; scratch script, not part of the claims.)

### C8. Exploratory scan outside 𝒫 (Empirical evidence)

`exploratory_scan.py` tested 15 polynomials P (12 outside 𝒫, with `D_t^2`, `D_x^j D_t` terms, even, odd and
mixed parity; `D_t + D_x^2`, `D_t + D_x^3`, `D_t + D_x^5` as controls) against
Q ∈ {D_x, D_x^3, D_x + D_x^3} with R = Q(D_y), three random points per type pattern, 60-digit arithmetic.
Printed: `patterns where (1) passes but (2) does not: none`. Passing pairs: only `D_t + D_x^3` and
`D_t + D_x^2` with Q = D_x (and trivially linear F-only/G-only patterns). With `Q = D_x^3, R = D_y^3` the
passing example `P = D_t + D_x^3` fails in both systems: the cubic multiplier destroys it, but since (1)
fails too this is not a counterexample to the conditional `R = Q` rule. The scan is finite and floating
point; it supports, but does not prove, that (R-sys-3) has no counterexample among these shapes.

## 3. Novelty and wording audit

- "Counterexample" (C5) refers to the single-function reading only; the literal reading is not refuted.
- C5's core computation (the n = 5 obstruction for c1 = c3 = 0) is a Reproduction of Wang et al. (2024);
  the extension to `c1, c3`, the second factor, the independent re-derivation and the connection to the
  Li–Lou conjecture are not found in the sources read (NOVELTY-UNCLEAR).
- C3/C4 against prior art: Hietarinta's primary 1997 account already lists the odd
  cubic pair as Eq. (37) with a=0. Its exact attribution among the cited 1987/1990 sources is unverified; the
  abstract of Peng et al. (2008) reports Wronskian N-soliton solutions and proposes a bilinear Bäcklund
  transformation and a Lax representation for "a particular case" of Hietarinta's system, which we infer
  (not verified) to be that pair. C4's statement for all degrees, for mixed parity and under the
  independent-amplitude test, and the F F G obstruction lemma, were not found in the sources read
  (NOVELTY-UNCLEAR; Hietarinta 1987 II and Peng et al. 2008 were not read in full).
- "Proved" is used only for C1, C2, Lemmas 4.1–4.3, Theorem 4.4 and Proposition 7.1 (three-soliton level).
  "Integrable" in C3/C4/C7 always means "passes the stated soliton test", never Lax or symmetry integrability.

## 4. Open and next steps

1. The original top obligation, proving the C6 all-N odd-cubic formula, is closed by C9.
   The remaining most valuable local action is a full-text comparison with Peng et al.'s
   Wronskian family, establishing an exact parameter map or a demonstrated scope difference
   before claiming originality. Mixed parity is outside this resumed assignment.
2. Extend the classification beyond 𝒫 (P nonlinear in `D_t`, `s(D_x)D_t + p(D_x)`), where C8 found no
   counterexample.
3. Supersymmetric and q-deformed S; the model `P = D_x D_t` needs a non-soliton criterion.

## 5. Review disposition

External review: Codex (`gpt-6.1-sol`, effort max, read-only sandbox, live web search), prompt
`review/codex-prompt.md`, output `review/codex-review.md` (2026-10-14). The reviewer reproduced Parts A–D,
the discrete checks, the N = 4, 5 checks and the `3600/247` witness, re-derived C5's factorization and
judged C1–C3 correct and C4, C5, C7, C8 "correct with fixes". Dispositions (each point re-checked here):

| # | Finding (severity) | Disposition |
|---|---|---|
| 1 | Failure of the universal test overstated as absence of multisoliton solutions; pure F-type superpositions with G = 1 solve both systems for every p (major) | Accepted. Verified the counterexample family directly from the equations (G = 1 makes both equations linear in F). C4 corollary, verdict and README now say "fails the generic test (F F G pattern)", name the surviving families, and qualify the C5 verdict as the Hirota sense. |
| 2 | The "extra condition" in README exceeds the proved result (major) | Accepted. README now states it at the three-soliton level only. |
| 3 | Literature: Hietarinta 1987 II treats same-pair systems via a rotation and lists the cubic pair as (37); Peng et al. 2008 give Wronskian N-solitons, a Bäcklund transformation and a Lax pair (major) | Accepted after checking: Hietarinta's 1997 summary (arXiv solv-int/9708006, §4.2) read and quoted; Peng et al. only via the OSTI abstract (full text inaccessible). STATUS.md §2, §4, §5 and the novelty columns of C3/C4 rewritten; the earlier statement that Hietarinta's classes "have a different second equation" was wrong and is removed. |
| 4 | Lemma 4.1 needs `a_1 a_2 b_3 m_3 ≠ 0` (minor) | Accepted. Reproduced the reviewer's example (`p = k^4`, `l = (1,3,0)`: zero residuals; `l = (1,3,7)`: five nonzero); hypothesis added. |
| 5 | Discrete classification wording outruns the proof (minor) | Accepted; added Proposition 7.1 (continuum-limit proof) so the claim now holds for every `deg p ≥ 4`. |
| 6 | Cubic-Q example does not refute the conditional R = Q rule (minor) | Accepted; C8 wording corrected. |
| 7 | C5's linear limit `c3 = c5 = 0` is undefined (minor) | Accepted; `(c3, c5) ≠ (0, 0)` now assumed explicitly. |
| 8 | C6 count is 48, not 24 × 3 (nit) | Accepted; corrected and controls listed separately. |

Second-round check (Codex, same model, read-only, no web; prompt `review/codex-prompt-2.md`, output
`review/codex-review-2.md`): Proposition 7.1 "ok"; Pfaffian closed form and its check "ok" (reviewer reran
`(N, seed, mult) = (4, 4000, Dy), (5, 5001, Dx), (7, 7001, Dy)`, all `(True, 0)`); one remaining minor
overclaim — Peng et al. described as having "proved" Lax integrability and their results attributed
unconditionally to the cubic model — accepted and fixed in RESULTS.md §3 and STATUS.md §4–§5 (abstract-only
evidence, conditional identification).

## 6. Approved scoped target: the all-N odd-cubic family

The user approved choosing precise open subproblems. The resumed target is C6 alone:
prove the displayed Pfaffian formula for every finite N, arbitrary independent amplitudes
`a_i,b_i`, and generic `k_i,l_i`, for `P=D_t+c1 D_x+c3 D_x^3`, `c3≠0`.
First compare it with the full Peng et al. paper and Hietarinta's primary account; this target
is not certified scientifically open by a missing search result. A prior theorem with a verified
parameter dictionary will be imported as Reproduction/Certification. The missing mathematical
ingredient is an all-N identity or induction, not another finite-N expansion. The general book
conjecture, mixed parity, and other operators are outside this resumed scope. Historical finite
checks and timed-out expansions above are retained.

### C9. All-N Pfaffian construction (Certification; novelty unverified)

The following is a written algebraic proof, not an inference from finite N. It uses
Pfaffian identities valid in every even dimension. It is independent of an all-N theorem
from Peng et al.; full-text access to that paper remains a prior-art limitation recorded
in STATUS.md. No priority claim is made.

**Theorem 9.1.** Fix a finite `N≥0`, constants `c1,c3` with `c3≠0`, and parameters over
the real or complex numbers with
`k_i+k_j≠0`, `l_i+l_j≠0` for every distinct pair `i,j`. Let `a_i,b_i` be arbitrary
independent constants (zero is allowed), and put

    eta_i = k_i x + l_i y − (c1 k_i + c3 k_i^3)t,
    R_S(k) = product_{i<j in S} (k_i−k_j)/(k_i+k_j).

Constant phase shifts can be absorbed into both `a_i,b_i`. Define two antisymmetric
matrices on the physical indices by their upper entries

    B0_ij = (l_i a_i b_j − l_j a_j b_i)/(l_i+l_j),
    C0_ij = (l_i b_i a_j − l_j b_j a_i)/(l_i+l_j).

For an odd subset `S`, append a dummy index `*` **last**, with
`B0_i*=a_i`, `C0_i*=b_i`. For an even subset use no dummy index. Write the resulting
ordered set as `S*`, and set `Pf(empty)=1`. Then

    F = sum_{S subset [N]} R_S(k) Pf(B0_{S*}) exp(sum_{i in S} eta_i),
    G = sum_{S subset [N]} R_S(k) Pf(C0_{S*}) exp(sum_{i in S} eta_i)

satisfy

    P(D_x,D_t)F·G = 0,       D_y P(D_x,D_t)F·G = 0,
    P = D_t + c1 D_x + c3 D_x^3.

This is exactly C6's formula when all `b_i≠0`: multiplying row and column i by `b_i`
in the Pfaffian shows `Pf(B0_{S*})=(product b_i)Pf(M_{S*})` and likewise for C0/N.
Unlike the ratio notation `x_i=a_i/b_i`, this expression has **no amplitude
denominator** and is defined without taking limits when any `b_i=0`.

The only parameter denominators in the displayed solution are the pair sums
`k_i+k_j` and `l_i+l_j`. The proof does not divide by F, G, a determinant, a seed
amplitude, an individual `k_i` or `l_i`, or a multi-index dispersion value.
It therefore remains valid when the recursive ansatz's determinant happens to
vanish, provided the displayed pair sums do not vanish. Distinctness and nonzero
individual wave numbers are needed only to describe generic nondegenerate
solitons, not for the algebraic identity. Tau-function zeros are allowed; no
claim about globally regular logarithmic physical fields is included.

#### 9.1 Pfaffian conventions and elementary identities

For an even-dimensional antisymmetric matrix H and ordered column vectors
`v1,...,v(2m)`, define

    [v1,...,v(2m)]_H =
        Pf( [ H       V ]
            [ −V^T    0 ] ),           V=(v1 ... v(2m)),
    []_H = Pf(H).

The bottom-right block here is zero. Also write `u∧v = uv^T−vu^T`.
The sign convention is important: in dimension two
`[u,v]_H = −u1 v2 + u2 v1`, independent of H.

The identities used below are:

    Pf(H+u∧v) = Pf(H) − [u,v]_H,                         (9.1)
    [V]_{H+u∧v} = [V]_H − [u,v,V]_H,                   (9.2)
    Pf(H)[u,v,w,z]_H =
        [u,v]_H[w,z]_H − [u,w]_H[v,z]_H
        + [u,z]_H[v,w]_H.                              (9.3)

Here (9.2) includes the empty V and any even number of border vectors.
For (9.1)–(9.2), expand the Pfaffian in its entries: terms with two copies of
the decomposable two-form `u∧v` vanish by alternation, leaving exactly its
linear contribution with the indicated minus sign. Alternatively expand the
bordered matrix along its final two rows.
For (9.3), on the dense set of invertible H the block Pfaffian identity gives

    [V]_H = Pf(H) Pf(V^T H^(-1) V).

The Pfaffian of the resulting 4-by-4 antisymmetric matrix is its three-term
pairing expansion, proving (9.3) there. Both sides of (9.3) are polynomials
in the entries of H and the vectors, so the identity also holds at singular H.
This supplies a dimension-independent proof, not an invertibility assumption.

Differentiating (9.1) gives the rule

    if H_z = u∧v, then
    d_z [V]_H = −[u,v,V]_H
                + sum of [V]_H with one vector differentiated.      (9.4)

Linearity handles sums of rank-two derivatives.

#### 9.2 Universal cubic bilinear lemma

Let `H=H(X,s)` be any even antisymmetric matrix, and let vectors `r_j`, `j≥0`,
satisfy

    (r_j)_X = r_(j+1),       (r_j)_s = r_(j+3),
    H_X = r1∧r0,
    H_s = r3∧r0 − 2 r2∧r1.                             (9.5)

Let v be independent of X and s; it may depend on y. Put
`tau=Pf(H)` and `psi=[r0,v]_H`. Then

    (D_X^3 − D_s) tau·psi = 0.                         (9.6)

*Proof.* Abbreviate `[r_i,r_j]_H` by `[ij]`, and likewise for longer brackets.
By (9.4), repeated vectors vanish and

    tau_X=[01],       tau_XX=[02],
    tau_XXX=[03]+[12], tau_s=[03]−2[12],
    psi_X=[1v],       psi_XX=[2v],
    psi_XXX=[3v]+[012v], psi_s=[3v]−2[012v].

Thus the left side of (9.6) equals

    3( [12][0v] − [02][1v] + [01][2v] − tau[012v] ),

which is zero by (9.3). This proves the lemma for every matrix size and
without any division. ∎

#### 9.3 Converting the subset formula to block Pfaffians

Work first in variables `X=x−c1 t`, `s=−c3 t` and y. Put

    f_i=exp(k_i X + k_i^3 s),     h_i=exp(l_i y),
    alpha_i=a_i h_i,            beta_i=b_i h_i,
    A_ij=((k_i−k_j)/(k_i+k_j)) f_i f_j,
    B_ij=(l_i alpha_i beta_j − l_j alpha_j beta_i)/(l_i+l_j),
    C_ij=(l_i beta_i alpha_j − l_j beta_j alpha_i)/(l_i+l_j).

All these N-by-N matrices have zero diagonal. Let

    K = [ A       I ]
        [ −I     −B ],
    q_j = (k_i^j f_i in the first block; 0 in the second),
    alpha = (0 in the first block; alpha_i in the second),
    beta  = (0 in the first block; beta_i in the second),
    sigma = (−1)^(N(N−1)/2).

The reuse of alpha, beta as 2N-vectors will always mean their zero-extended
versions in matrix expressions.

The elementary block minor sum is

    sigma Pf( [ A    I ] ) = sum_{S even} Pf(A_S) Pf(B_S).            (9.7)
              [ −I  −B ]

To prove it, expand in perfect matchings. Each cross-block pair must be the
matched pair i from the identity matrix; therefore the indices used internally
in the A- and B-blocks must be the same even subset S. If `|S|=2m`, grouping
these internal pairs has sign `sigma (−1)^m`; the factor `Pf(−B_S)=
(−1)^m Pf(B_S)` cancels that last sign. The remaining terms are precisely
the two internal Pfaffians. This proves (9.7) for arbitrary A,B.

For odd subsets, append one index `*` to each block, setting
`A_i*=f_i`, `B_i*=alpha_i`, and extending the cross identity matrix by
`I_**=1`. In the full order `(x1,...,xN,x*,y1,...,yN,y*)`, move x* past
the N original y-indices. This permutation contributes `(−1)^N`, exactly
the ratio of the two normalization signs. The final two border columns
are q0 and −alpha and their mutual entry is 1. Expansion in that mutual
entry gives

    F = sigma ( Pf(K) − [q0,alpha]_K ).                 (9.8)

Indeed, (9.7) in dimension N+1 produces the even physical subsets and the
odd physical subsets with `*`; Schur's identity

    Pf( ((k_i−k_j)/(k_i+k_j))_{i,j in S} ) =
        product_{i<j in S}(k_i−k_j)/(k_i+k_j)

gives the required `R_S(k)`. For odd S use the appended value `k_*=0`,
whose entries against a physical index are 1, and factor out the f_i.
Schur's identity follows, for example, by induction in the last parameter:
the two sides have identical simple poles/residues at `k_m=−k_j`;
their difference is bounded at infinity and vanishes at `k_m=k_j`.
The generic-parameter proof extends as a rational identity wherever its
pair denominators exist. Factoring the h_i from the B-Pfaffian gives
exactly the B0-coefficients in Theorem 9.1.

For G, replace B by C and the boundary alpha by beta. Since

    C = B − (alpha_i beta_j − beta_i alpha_j)_{ij},

the corresponding block matrix is `K_C=K+alpha∧beta`. From (9.1)–(9.2),
and the repeated beta in the correction to its border, one obtains

    G = sigma ( Pf(K) − [alpha,beta]_K − [q0,beta]_K ).  (9.9)

Equations (9.8)–(9.9) establish the dictionary from the old coefficient
formula to the finite-dimensional matrices used in the proof.

#### 9.4 Two uses of the lemma prove both coupled equations

Set

    L=K+q0∧alpha,       r0=q0+alpha,       r_j=q_j (j≥1).

Then (9.1)–(9.2) give, with all brackets below based at L,

    F = sigma Pf(L),
    G = F + sigma [r0,alpha−beta]_L.                   (9.10)

For the second equality, the rank-two correction in the bordered expression
vanishes because `r0=q0+alpha`; expanding its two border vectors gives
`[q0,alpha]_K−[q0,beta]_K−[alpha,beta]_K`, which added to F
is (9.9).

Direct differentiation, using the split between the x/s-dependent f_i
and the y-dependent alpha_i,beta_i, gives

    K_X = q1∧q0,
    K_s = q3∧q0 − 2q2∧q1,
    K_y = −alpha_y∧beta.                              (9.11)

The cubic coefficient in the second identity follows from
`(k_i^3+k_j^3)(k_i−k_j)/(k_i+k_j)
=k_i^3−k_j^3−2k_i^2k_j+2k_ik_j^2`.
For the y identity, `(B_ij)_y=l_i alpha_i beta_j−l_j alpha_j beta_i`;
the minus sign is the minus sign of the bottom-right block of K.
Consequently L and the r_j satisfy (9.5).

In (9.10), `alpha−beta` is independent of X,s. Apply the cubic lemma and
use oddness of `D_X^3−D_s` on `F·F` to conclude

    (D_X^3−D_s)F·G=0.                                 (9.12)

Differentiate (9.9) in y using (9.4) and (9.11). The matrix-derivative
terms in the borders repeat beta, so they vanish:

    d_y Pf(K) = [alpha_y,beta]_K,
    d_y [alpha,beta]_K =
        [alpha_y,beta]_K + [alpha,beta_y]_K,
    d_y [q0,beta]_K = [q0,beta_y]_K.

Therefore

    G_y = −sigma [r0,beta_y]_K
        = −sigma [r0,beta_y]_L,                       (9.13)

where again the rank-two correction contains q0,alpha,r0 and vanishes.
Since beta_y is also independent of X,s, a second application of (9.6)
gives `(D_X^3−D_s)F·G_y=0`.

Finally

    P(D_x,D_t)=c3(D_X^3−D_s).

Thus `P F·G=0` and `P F·G_y=0`. The ordinary y-derivative of the first
identity is `P F_y·G + P F·G_y=0`; hence both terms vanish separately.
Their difference is precisely `D_y P F·G=0`. This proves Theorem 9.1
for all finite N. ∎

#### 9.5 Scope, continuation and reductions

- **Zero amplitudes.** B0 and C0 are polynomial in all `a_i,b_i`.
  Multiplication by the product of pair-sum denominators makes each bilinear
  equation a polynomial identity in the amplitudes. Thus the original
  ratio-form C6 formula extends uniquely to every zero-amplitude case,
  and the B0/C0 version implements that continuation directly. F-only/G-only
  soliton patterns are covered, without an assumption that all b_i are nonzero.
- **Generic recursive solution.** On the open set where the earlier recursive
  determinants `−2 l_S P(kappa_S)P(−kappa_S)` are nonzero for `|S|≥2`,
  the square-free ansatz is unique. Theorem 9.1 has the prescribed constants
  `F_empty=G_empty=1`, `F_i=a_i`, `G_i=b_i`, so it is that recursive solution
  for every N. The identities themselves do not need this open-set restriction.
- **The original (1+1)-dimensional system.** Taking `l_i=k_i` makes F,G
  depend on x,y only through x+y. Hence `D_y=D_x` on this solution and C1
  yields `P F·G=D_x P F·G=0`. This proves the all-N implication in the
  approved odd-cubic class; it is not a proof for arbitrary P,Q,S.
- **Equal amplitudes.** For `a_i=b_i`, Schur's identity reduces both amplitude
  Pfaffians to `(product a_i)R_S(l)`. This reproduces the ANNV/BLMP
  tau coefficients `R_S(k)R_S(l)` and, with `l_i=k_i`, the usual squared
  KdV phase factors. This reduction is a check, not the all-N proof.
- **Evidence status.** The all-N quantifier is supported by the written
  dimension-independent proof above. Finite exact checks are supplemental
  controls. This is Certification; originality and an exact parameter
  dictionary to Peng et al.'s unavailable full text remain unverified.

#### 9.6 Replay and review evidence

From this target directory:

    /Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python -B code/all_n_pfaffian.py

Observed output:

    universal cubic expression + 3*Pluecker = 0 (no matrix dimension selected)
    matrix identity controls: 10 passed (including singular matrices)
    finite controls: 28 passed; N=0..6, zero amplitudes, zero individual wave numbers, diagonal reduction
    both Hirota residuals: all exact coefficients zero; block F,G,G_y agree

The replay writes `results/all_n_pfaffian.json`. It imports neither the shared
`code/hirota_ns.py` engine nor the old C6 implementation. Its coefficient Pfaffians
use signed perfect-matchings; its block-matrix values use independent skew
elimination. Direct ordered-pair enumeration reconstructs both Hirota residuals.
The symbolic part differentiates abstract Pfaffian brackets and verifies that the
cubic expression is exactly minus three times (9.3), without selecting a matrix size.
The mathematical identity (9.3) itself and the all-N quantifier are proved above;
there is no Lean/kernel certification claim.

An independent Codex review is pinned to
`review/all-n-snapshot/RESULTS.md`, SHA-256
`e41f63bc84f0eb8ec0cafce162823b7b63ed1a310fabd9cd5a17f4568319a021`.
The reviewer prompt is `review/codex-all-n-prompt.md`, output
`review/codex-all-n-review.md`; runtime identity in
`review/codex-all-n-process.log` is `gpt-6.1-sol`, effort `max`, read-only sandbox.
The process exited 0. Its verdict is **correct**, with **no required fixes and no
remaining unproved mathematical step within the approved scope**.

Review dispositions:

| Check | Independent finding | Disposition |
|---|---|---|
| Rank-two/Pfaffian derivative signs | Re-derived using exterior algebra; correct in every even dimension | Accepted; no change |
| Four-border Pluecker identity | Re-derived by determinant-one congruence, continued polynomially to singular H | Accepted; no change |
| Block minor sum and odd dummy | Normalization signs and coefficient dictionary match C6 | Accepted; no change |
| Both Hirota equations | Independent G_y derivation confirms the ordinary/Hirota derivative distinction and time-coordinate sign | Accepted; no change |
| Degenerate cases | N=0,1,2 checked explicitly; zero b_i, singular K/L and individual zero wave numbers introduce no gap | Accepted; no change |
| Verdict and prior art | SOLVED for the approved formula, PARTIAL for the unrestricted book problem; originality remains separate | Accepted; no change |

The reviewer also performed independent in-memory N=2 symbolic checks of the block
dictionary, G_y and both residuals. A separate worker independently rederived the
same cubic derivative and G_y identities before using the theorem for a different
assignment. These cross-checks supplement the written all-N proof; no finite
experiment, model review, or stopped expansion is substituted for that proof.

### Final openness disposition (2026-10-14)

No new mathematical work or numerical rerun was performed for this gate.
The reviewer's correctness verdict remains intact, but does not establish priority.
The source table in STATUS.md records:

- verified equation/three-soliton overlap with Hietarinta's primary 1997 account;
- the unresolved full-family comparison with Peng2008, despite additional legitimate
  archive, author-page, institutional and API routes;
- the Hu–Gegenhasi sinh-Gordon/Pfaffian risk and the inspected 2023 follow-up theorem,
  whose base pair is quadratic with a nonzero `2Dx` remainder;
- unresolved access to the original modified-discrete-BKP Pfaffian construction and
  to Hietarinta1987 II.

There is no basis to relabel the full C9 family **ALREADY-SOLVED/Reproduction** without
a verified prior theorem and dictionary, and equally no basis to call it a newly
solved open problem. Retain **Certification / NOVELTY-UNCLEAR**, gate **PARTIAL-OVERLAP**.
Li–Lou's explicit question about other n beyond 2 and 3 must not be repurposed as an
openness statement about the cubic n=3 C9 family.
