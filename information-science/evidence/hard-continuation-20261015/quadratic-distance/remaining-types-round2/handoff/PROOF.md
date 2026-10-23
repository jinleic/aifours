# Remaining types, round 2: (2,192), (4,160) and (6,144)

**Status.** No residue type is excluded in this round. Round 2 proves new necessary conditions and sub-case results, and it supplies exhaustive finite certificates. It refutes all three round-1 (2,192) witnesses and states a precise stopping point for each of the three types. Everything is conditional on the same reviewed inputs as `../zero-geometry/PROOF.md` and round 1 (`inputs/round1-PROOF.txt`):

- the canonical-sign, residue and Pfaffian tools;
- the zero moments: even count, XOR zero, second moment `C(B)`;
- `hat p ∈ {0, ±64}`, the next-bit lemma, and the slack identity;
- the round-1 lemmas. Lemmas 3.1 and 3.2 there are the coset energy identity and the coset form.

This proof was written by a model and checked by exact finite computations. It is not Lean-verified, not peer reviewed, and has not had an independent proof review. Novelty is unestablished: Wang–Lou–Wang ([arXiv:2610.17871](https://arxiv.org/abs/2610.17871)) and Lou–Xu–Wang ([arXiv:2610.17897](https://arxiv.org/abs/2610.17897)) introduced the residue and paired-half tools. The six-variable cubic classification in §2.2 reproduces a classical result (Hou's GL(6,2) classes of cubic forms) by direct computation. The book question remains open.

Notation follows round 1. `K ⊆ rad B ∩ D^{-1}(0)` has dimension `τ`. For a coset `u+K` and a character `κ` of `K`, `hat p_u(κ) = Σ_{k∈K} p(u+k)(−1)^{κ·k}`. On a `D=1` coset, `p = (−1)^E(−3+4·1_L)`. Hence `hat p_u = −3W_{E_u} + 4Λ_u`, where `Λ_u(κ) = Σ_{k∈L_u}(−1)^{E_u(k)+κ·k}`. Here `ℓ_u = |L_u|` and `c = Σ ℓ_u`.

## 1. General lemmas (all types)

**Lemma 1.1 (slice ternary structure).** For every `κ` there is `ε^κ ∈ {0,±1}^{F_2^{8−τ}}` such that, for all `u`, `hat p_u(κ) = 2^{τ−2}(Hε^κ)(u)`, where `H` is the `(8−τ)`-dimensional Sylvester transform. Consequently:

1. (uncertainty) `Σ_u hat p_u(κ)² = 2^{τ+4}|supp ε^κ|`, and `Σ_u hat p_u(κ)² ≥ 64·max_u |hat p_u(κ)|`;
2. (uniform parity) every `hat p_u(κ)/2^{τ−2}` is congruent to `|supp ε^κ|` mod 2;
3. (affine second bit) `hat p_u(κ)/2^{τ−2} ≡ |supp ε^κ| − 2α_κ(u) (mod 4)` for an affine function `α_κ` of `u`.

*Proof.* For `x = (x_u, κ)`, `hat p(x) = Σ_u (−1)^{x_u·u} hat p_u(κ) ∈ {0,±64}`. Inverting the `(8−τ)`-dimensional transform gives `hat p_u(κ) = 2^{τ−8}Σ_{x_u}(−1)^{x_u·u} hat p(x) = 2^{τ−2}(Hε^κ)(u)` with `ε^κ = hat p(·,κ)/64`. Parseval gives the energy. Every entry of `Hε` is a sum of `|supp ε|` terms `±1`, so its absolute value is at most `|supp ε|`, with the stated parity. Writing it as `|supp ε| − 2N(u)`, where `N(u)` counts the `−1` terms, gives `N(u) ≡ Σ_{x∈supp ε}[ε_x=−1] + u·Σ_{x∈supp ε}x (mod 2)`, which is affine in `u`. ∎

**Lemma 1.2 (the Λ residue is affine).** On a `D=1` coset, `Λ_u(κ) ≡ ℓ_u − 2(ε_u + κ·σ_u) (mod 4)`. Here `σ_u` is the XOR of the `K`-coordinates of `L_u` and `ε_u = Σ_{k∈L_u}E_u(k) mod 2`. In type (2,192) (`τ = 6`, `hat p_c(κ) ∈ 16Z`), therefore

`W_{E_c}(κ) ≡ 12ℓ_c + 8(ε_c + κ·σ_c) (mod 16)`.

The same holds on the S side with `a_c` and `X_c`, because the round-1 S form has the same integrality: `−3W_{X_c} + 4Λ^S_c ≡ 0 mod 16`.

*Proof.* `Λ = ℓ − 2N(κ)`, where `N(κ) = #{k∈L: E(k)+κ·k = 1}` has parity `ε + κ·σ`. Integrality `16 | −3W + 4Λ`, together with `3^{−1} ≡ 11 (mod 16)`, gives the congruence for `W`. ∎

**Lemma 1.3 (first moments).** For every Boolean function `f` on `F_2^m`, `Σ_κ W_f(κ) = 2^m(−1)^{f(0)}`. For every signed set, `Σ_κ Λ(κ) = 2^m·λ(0) ∈ {0, ±2^m}`. (This is Fourier inversion at the origin.)

## 2. Type (2,192)

Here `U = K = D^{-1}(0)` is six-dimensional and the three `D=1` sets are its other cosets. Because the polar rank is 2, `E` and `X` are cubic: `E = A + a0B1 + a1B2 + a0a1C`, where `A = 1 + 1_Z` on `U`, `deg B_i ≤ 2` and `deg C ≤ 1`.

**2.1 Coupling.** The four coset functions share the cubic part of `A`, and `Σ_{c∈F_2^2} E_c = 4A + 2B1 + 2B2 + C ≡ C` is affine. Hence their quadratic parts sum to zero modulo `RM(1,6)`. The affine parts of the three `D=1` coset functions are independent free parameters. The same holds for `X_c`, whose four cosets share the cubic part of `J1|_U`.

**Lemma 2.2 (six-variable cubics).** Let `f` have degree at most 3 on `F_2^6`, and let `P6` count the unordered pairs of complementary cubic monomials in its ANF. Then:

- `W_f(κ) ≡ 4·P6 (mod 8)` for every `κ`;
- if `P6` is even, `κ ↦ W_f(κ)/8 mod 2` is affine;
- if `P6` is odd, `κ ↦ (W_f(κ)/4 − P6)/2 mod 2` is affine.

*Proof.* Expanding `(−1)^g = Π_{m∈M(g)}(1−2m)` gives `W_g(0) = Σ_{T⊆M(g)}(−2)^{|T|}2^{6−|∪T|}`. Modulo 16, the only surviving terms come from pairs with `|∪T| = 5` (contributing 8) or `|∪T| = 6` (contributing 4), and from triples with `|∪T| = 6` (contributing 8). Apply this to `g = f + κ·x`. Linear monomials cannot appear in such a pair. A triple with union 6 contains at most one linear monomial. So `W_f(κ) ≡ 4P6 + 8(P5 + T6(κ)) (mod 16)`, where `T6` is affine in `κ`. ∎

Lemma 2.2 shows that Lemma 1.2's affine residue is automatic for genuine cubics. Lemma 1.2 then pins the XOR of `L_c` to the linear part of that residue.

**2.2 Exhaustive tables (certificate `results/rank2-cubic-classes.json`).** Label propagation along three generators of GL(6,2) on all `2^20` cubic forms finds exactly six orbits, of sizes `1, 1395, 54684, 468720, 357120, 166656`. For each orbit representative, all `2^15` quadratic completions were enumerated, and the complete table of |W| histograms is recorded. Affine terms only permute and negate Walsh values, so this covers every cubic up to that action. Lemma 2.2 was checked on every completion.

For `z = 8`, the reviewed moments make `Z` a linear 3-flat. In coordinates where `Z = {x0=x1=x2=0}`, the shared cubic part is `x0x1x2`. Its `2^15` completions fall into exactly six Walsh classes:

| class | abs-W histogram | completions |
|---|---|---:|
| flat | `0^56 16^7 48^1` | 8 |
| 32 | `0^54 16^8 32^2` | 392 |
| semi-bent | `0^48 16^16` | 2352 |
| bent | `8^64` | 1344 |
| 24 | `0^32 8^28 24^4` | 3584 |
| 16 | `0^24 8^32 16^8` | 25088 |

**Lemma 2.3 (exact per-coset realizability, `z = 8`; certificate `results/rank2-coset-realizability.json`).** Each class is a single orbit of the affine stabilizer of `x0x1x2`. Under that group and under affine terms, `(h, Λ)` changes only by a κ-permutation and a joint per-κ sign. Hence the sign-normalized `(h, Λ)` histogram is a class invariant. Exhausting every ℓ-subset `L_c` for one representative per class gives the complete set of realizable histograms:

- `ℓ_c = 0`: only the semi-bent class is possible.
- `ℓ_c = 2`: only class 16 (16 subsets, one histogram).
- `ℓ_c = 4`: semi-bent (5296 subsets, 4 histograms), bent (5376, 1), class 24 (2408, 1) and class 16 (5088, 8). The flat class and class 32 are impossible.

**Proposition 2.4 (round-1 witnesses refuted; certificate `results/rank2-witness-check.json`).** All three round-1 joint count witnesses (`z = 8`) are inconsistent with genuine cubic coset functions. Every one of them violates the first moments (Lemma 1.3), the affine residue count `#{W ≡ 8 mod 16} ∈ {0,32,64}` (Lemmas 1.2/2.2), and the class table on several cosets. All of their `ℓ = 4` R-cosets have histograms that Lemma 2.3 shows cannot be realized.

**Proposition 2.5 (new stopping point; `results/rank2-probe2-z8.json`).** This experiment is exploratory: the solver's unsat or unknown verdicts would carry no claim. Adding Lemmas 1.2, 1.3, 2.2, the class table and a shared S-side cubic class to the round-1 relaxation at `z = 8` is still satisfiable (z3, 38 s). The audit verifies the explicit witness independently. It has `ℓ = (4,4,4)` and `a = (8,0,4,4)`, and all three R-cosets are in class 16. Their `(h,Λ)` histograms **are** realizable (Lemma 2.3).

**Precise obstruction (2,192), z = 8.** Per-coset spectral information is now exhausted for the R side with `ℓ ≤ 4`. What the histograms cannot express is the **cross-coset alignment**: which κ carries which `(h_c, Λ_c)` in each of the four cosets. That alignment is subject to the per-κ fiber patterns, the quadratic-part coupling of §2.1, and the D0-coset form `h_00 = 8δ − 1_{Z^⊥} − hat G/4` (`G = {p = −2} ⊆ U∖Z`). The S side was not enumerated exactly: `X_c` may lie in any of the four `P6`-even cubic classes, and the witness has `a_0 = 8`, whose `C(64,8)` subsets are too many to exhaust directly. The next proof-producing step would be an aligned search over the explicit orbit representatives, using the per-coset valid-subset lists as domains.

## 3. Type (4,160)

`D = q4(u)` with `u = a0..a3`, `K = span(e4..e7)`, `τ = 4`. There are 10 `D=1` cosets and 6 `D=0` cosets, and the quartic part of `E` is `u0u1u2u3`. In units `Y_κ(u) = hat p_u(κ)/4 = (Hε^κ)(u)`, the bound of Lemma 3.1 becomes `Σ_u Y_κ(u)² ≤ 256`, and Lemma 1.1 gives `Σ_u Y_κ(u)² ≥ 16·max_u|Y_κ(u)|`. Recall `z + 2c ≡ 0 (mod 8)` and `2(a+c) + z ≤ 56`.

**Lemma 3.1 (coset-affine criterion).** If every slice `Z_u` (`u ∈ D0`) has an affine indicator on `K` (∅, `K`, or an affine hyperplane), then `E` is affine on every coset. *Proof.* Write `E = u0u1u2u3 + Σ_{S⊆{4..7}} c_S(u)k^S` with `deg c_S ≤ 3−|S|`. On `D0`, `E_u = 1+1_{Z_u}` is affine in `k`, so `c_S` vanishes on `D0` for `|S| ≥ 2`. For `|S| = 3`, `c_S` is constant, hence zero. For `|S| = 2`, `c_S` is affine, and `D0 = {0,4,8,13,14,15}` spans `F_2^4` affinely, so `c_S ≡ 0`. ∎

**Lemma 3.2 (exact affine-coset values).** If `E_u` is affine with character `χ_u` and `s = (−1)^{E_u(0)}`, then `Λ_u(χ_u) = sℓ_u` and `Y_{χ_u}(u) = −s(12 − ℓ_u)` exactly. The remaining energy `Σ_{κ≠χ_u}Y_κ(u)² = ℓ_u(16 − ℓ_u)`. Also `Y_κ(u) ≡ ℓ_u (mod 2)` for **every** `κ`. With Lemma 1.1(2), it follows that **all coset-affine `D=1` cosets have `ℓ_u` of one common parity, and every `|supp ε^κ|` has that parity.**

**Proposition 3.3 (z = 8 classification; `results/rank4-160-structure.json`).** There are 715 linear 3-flats inside `D^{-1}(0)`, and all pass the E-extension criterion. Their projection to `u` is totally singular for the minus-type `q4`, so it has dimension ≤ 1:

- 8a, 15 sets: `Z` is a hyperplane of `K`. Lemma 3.1 makes `E` coset-affine.
- 8b, 700 sets: `π(Z) = {0,d}`. The quadratic-in-`k` coefficients are affine in `u` and determined on `D0`. They force `E_u` to be non-affine on exactly 6 of the 10 `D=1` cosets.

**Theorem 3.4 (pairwise distinct characters cost energy).** Suppose `E` is affine on all ten `D=1` cosets and their characters `χ_u` are pairwise distinct. Then `c ≥ 12 + z/2`, so `c ≥ 16`.

*Proof.* In slice `χ_u`, Lemma 1.1 gives `Σ_v Y_{χ_u}(v)² ≥ 16(12−ℓ_u)`, while coset `u` contributes `(12−ℓ_u)²`. The remaining `(12−ℓ_u)(4+ℓ_u)` must come from two sources. One is other `D=1` cosets at a foreign character; their total over all κ is `Σ_v ℓ_v(16−ℓ_v)` (Lemma 3.2). The other is the `D0` cosets, whose total is `Σ_{D0}p² = 4(96−z)`. The slices are distinct, so summing gives `Σ_u[(12−ℓ_u)(4+ℓ_u) − ℓ_u(16−ℓ_u)] = 480 − 8c ≤ 384 − 4z`. ∎

**Corollary 3.5.** In case 8a, `c ≠ 0`, so `c ≥ 4`. *Proof.* If `c = 0`, two `ℓ=0` cosets cannot share a slice, since `2·144 > 256`. The characters would then be distinct, and Theorem 3.4 would give `c ≥ 16`. ∎ Parity uniformity also rules out a slice holding two cosets with `ℓ = 1`: then `242 ≤ 16|supp ε| ≤ 256` and `|supp ε|` would be odd, which is impossible.

**Lone-slice lemma (exact).** Suppose a slice contains one coset with `Y = ±12` and the other nine `D=1` values are 0. Then that slice needs at least 48 energy on `D0`, by Lemma 1.1. For each of the ten `u1`, exhaustive enumeration finds eight ternary solutions, and the minimum energy outside `u1` is exactly 48.

**Precise obstruction (4,160).** Two aggregate slice witnesses in case 8a (`z = 8`) satisfy every slice constraint proved here: total energy, the 256 cap, the uncertainty floor, uniform parity, the energy balance between `D0` and the spreads, the congruence and the slack. One has `c = 4` and uses collisions. The other has `c = 16` with **pairwise distinct characters**, exactly at the bound of Theorem 3.4. Collisions are therefore not forced by these lemmas. Injective characters cost `c ≥ 12 + z/2`, which is still compatible with `c ≤ 24` when `z ≤ 24`. Excluding (4,160) needs the full spatial condition `hat p ∈ {0,±64}`, which is the original problem, or the S side. Case 8b (and every `z ≥ 12` with non-affine slices) has non-affine cosets, and Theorem 3.4 does not apply there.

## 4. Type (6,144)

`u = a0..a5`, `k = (a6,a7)`, `K = span(e6,e7)`, `τ = 2`. There are 36 `D=1` and 28 `D=0` cosets. `z + 2c ≡ 4 (mod 8)` and `2(a+c) + z ≤ 100`.

**Lemma 4.1 (E structure).** `E = e_0(u) + e_6(u)k6 + e_7(u)k7 + e_67(u)k6k7`, with `deg e_67 ≤ 1` and `deg e_6, e_7 ≤ 2`, because the Pfaffian quartics use only `u`. On `D0`, `e_67(u) ≡ |Z_u| (mod 2)`. *(The `k6k7` coefficient of `1+1_{Z_u}` is `|Z_u| mod 2`.)*

**Proposition 4.2 (dichotomy; `results/rank6-144-zero-sets.json`).**

- If `e_67 ≢ 0`, then `D0 ∩ {e_67 = 1}` has 12, 16 (non-constant `e_67`) or 28 points, each with an odd slice, so `z ≥ 12`.
- If `e_67 ≡ 0`, then `E` is coset-affine with characters `χ_u = (e_6,e_7)(u)`. On `D0`, `χ_u ≠ 0` exactly on `T2 = {u: |Z_u| = 2}`. `RM(2,6)|_{D0}` has dimension 21, kernel `{0,q6}`, and minimum weight 4 (its full weight enumerator is recorded). So a non-K-invariant `Z` has `|T2| ≥ 4` and `z ≥ 8`.

**Theorem 4.3 (z = 8 classification).** At `z = 8`, `Z` is either K-invariant (two `K`-cosets) or one of exactly **540** sets. Each of the 540 has the form `T2 ×` lines: `T2` is a totally singular plane through 0, all four lines have one direction, and the offsets satisfy the `(6,7)` moment parity. All 540 pass the reviewed moments and the E-extension criterion. For each of them, `E` has exactly two characters on `D=1`, with fibers of sizes **12 and 24**.

**Precise obstruction (6,144).** Even with `c = 0`, the larger fiber contributes `24·144 = 3456 < 4096` to its slice. Lemma 1.1's floor `64·12` is also met. So the single-character projection mechanism (round-1 Theorem 4.1) cannot exclude non-K-invariant zero sets, even at the minimal `z = 8`.

**Theorem 4.4 (sharper K-invariant bound).** If `Z` is K-invariant, then `c ≥ 14`, and `c ≥ 16` when `z ≡ 4 (mod 8)`. *Proof.* There is one character, and Lemma 3.2's analogue gives `|hat p_u(χ)| = 12 − 4ℓ_u` exactly, so `Σ_{u∈D1}(12−4ℓ_u)² ≤ 4096`. Exact integer minimization over the 36 cosets (recorded in the certificate) gives `c ≥ 14`. The congruence `z + 2c ≡ 4 (mod 8)` with `z = 4m` gives `c ≡ 0 (mod 4)` when `m` is odd. ∎ This improves round 1's `c ≥ 12`, but it is not an exclusion: `c ≤ 48` remains possible.

## 5. Status

| Type | New here | Where the levers stop |
|---|---|---|
| (2,192) | Lemmas 1.1–1.3, 2.2; exhaustive cubic tables; exact per-coset `(h,Λ)` lists (`ℓ ≤ 4`, `z = 8`); all round-1 witnesses refuted | strengthened `z = 8` witness passes every per-coset test; cross-coset κ-alignment is unconstrained by histograms |
| (4,160) | Lemma 3.1; z = 8 split (15 + 700); Theorem 3.4 (`c ≥ 12 + z/2` for distinct characters); `c ≥ 4` in 8a; parity uniformity | explicit slice witnesses at `c = 4` (collisions) and `c = 16` (distinct characters); case 8b has non-affine cosets |
| (6,144) | Lemma 4.1; dichotomy; z = 8 classification (540 sets, fibers 12/24); K-invariant `c ≥ 14` (16) | the projection lever cannot see non-K-invariant `Z` |

None of these results excludes a type. The (4,128) exclusion and the round-1 results are unchanged.
