# Sign-digit duality for balanced nine-variable NL242: lemmas and stopping point

**Status: Sections 1–4 received a focused Claude Opus 5.5 model review, ACCEPT-WITH-FIXES;
the scope/wording fixes are incorporated below. Sections 5–8 remain UNREVIEWED. No Lean or human
peer review. No residue type is excluded and nothing here settles balanced NL242.** The general
identities pass exact checks on 40 genuine balanced controls, with required mutation rejections
(`evidence/digit-lemmas-check.json`; `code/digit_lemmas_check.py`). The parent also independently
checked 4,088 affine hyperplanes using direct character sums. See [review scope and provenance](review/README.md).
Section 6 imports Wang–Lou–Wang Theorem 3 (arXiv:2610.17871v1, unrefereed) as an explicit premise.
Novelty is unestablished: the method is the WLW residue/Walsh-l1 technique with Lucas digits and Cauchy–Binet.

## 0. Notation

`f: F_2^9 -> F_2` is balanced, with `X = supp f`, `|X| = 256`, `F = (-1)^f` and
`W(a) = sum_x F(x)(-1)^{a.x}`. Put `s = XOR of X` and `beta = sum_{x in X} x x^T (mod 2)`. The latter is a
symmetric form on frequency space with `beta(a,a) = a.s`. Write `N_a = #{x in X : a.x = 1}` and `T = W/4`.
Then `W(a) = 512 delta_{a,0} - 512 + 4 N_a`, so `T` is congruent to `N_a` modulo 16 for every `a`.
Let `d_k` be binary digit `k` of the **least nonnegative residue** of `T` modulo 16, and
`B = beta + s s^T` (zero diagonal). A *target* is a balanced `f` with `max|W| <= 28`.
Any statement using coordinates `s=e_9`, the eight-dimensional `s^perp`, or its odd coset
assumes **`s != 0` explicitly**. Those normalized statements alone do not handle `s=0`.

## 1. Lucas digits and their top-degree parts (all balanced f)

**Lemma 1.** For k = 0..3:

- `d_k(a) = sum_{S subset X, |S| = 2^k} prod_{x in S} (a.x)` over `F_2`;
- `deg d_k <= 2^k`;
- for `|I| = 2^k`, the coefficient of `a^I` is `det(beta_I)` (mod 2).

In particular:

- `d0 = a.s`;
- `d1` is quadratic with polar matrix `B`;
- the quartic part of `d2` is `sum_{|I|=4} Pf(B_I) a^I`.

More generally, the restriction of `d3` to any affine hyperplane `{a.h = c}` (`h != 0`) has weight parity
`det(beta restricted to h^perp)`.

*Proof.* Lucas gives digit `k` of `N` as `C(N, 2^k) mod 2`, which counts the `2^k`-subsets of
`{x : a.x = 1}`. A product of `r` linear forms has degree `<= r`. A monomial of full degree `r` arises only
from bijective variable choices, so its coefficient is a permanent, which equals the determinant mod 2.

Cauchy–Binet gives `sum_{|S|=r} det(V_S)^2 = det(V V^T)`, with `V` the `I x X` incidence matrix, and
`det^2 = det` mod 2. For `r = 2`: `det(beta_{ij}) = s_i s_j + beta_ij`.

For `r = 4`, write `beta_I = B_I + s_I s_I^T`. Then `det(beta_I) = det(B_I) + s^T adj(B_I) s = Pf(B_I)`,
because `adj` of an even-size alternating matrix is alternating. On an affine hyperplane,
weight parity is the top eight-variable coefficient. Only the eight linear parts of the substituted
forms contribute to that coefficient, so Cauchy–Binet gives `det(L^T beta L)` for any basis `L`
of `h^perp`. The affine offset cannot change it; replacing `L` by `L P` multiplies its determinant
by `det(P)^2=1`, so it is basis-independent. ∎

## 2. Translation normalization

**Lemma 2.** Translating the input by `c` keeps `s` and `|W|`, and replaces `B` by `B + c s^T + s c^T`.

Assume `s != 0`. In coordinates with `s = e_9`, choosing `c_i = B_{i,9}` (i <= 8) zeroes
the last row and column of the **translated** `B`. Its rank is the rank of
`D = d1|_{s^perp}`, the residue quadratic of the reviewed `SHARPER.md`.
The restriction `B|_{s^perp}` is translation-invariant because
`a^T(c s^T+s c^T)b=0` for `a,b in s^perp`. *Proof:* expand `sum (x+c)(x+c)^T`
and use `|X| = 256`. ∎

## 3. Sign-digit identity (targets)

**Lemma 3.** For a target, `T` lies in `[-7, 7]` and residue 8 never occurs. Hence `d3 = [W < 0]`,
`T = d0 + 2 d1 + 4 d2 - 8 d3`, and

`W_{d3} = 32 F + 64 delta_0 + 64 delta_s + W_{d1}/4 + W_{d2}/2`.

For general balanced `f`, the last identity holds with the extra term `-4 H(e)`, where
`e = (T - d0 - 2d1 - 4d2 + 8d3)/16`; this general form is what is checked.
*Proof:* invert `512 F = H(4T)` with `H(d) = (512 delta - W_d)/2`. ∎

## 4. Sign-parity theorem (target-only sign interpretation)

**Theorem 4.** For a target and every `h != 0`, `c`:

`#{a : a.h = c, W(a) < 0} = det(beta|_{h^perp}) (mod 2)`.

If `s != 0`, take `h = s`; then `beta|_{s^perp}` is the polar matrix of `D`. Hence

`#{a.s = 1 : W(a) < 0} = #{a.s = 0 : W(a) < 0} = [polar rank of D = 8] (mod 2)`.

*Proof:* Lemma 1 (k=3) with Lemma 3. ∎

**Corollary 5 (kappa).** Assume a target with **`s != 0`**. Work in coordinates `s = e_9` with
`v(y) = (F(y,0) - F(y,1))/2`, so `W(a,1) = 2 H v(a)`. Put `q = T(.,1)`,
`Dq = d1(.,1)`, `Jq = d2(.,1)`, `sigma = d3(.,1)` and `kappa = [rank D = 8]`. Then:

- `4 W_sigma = 128 v + W_{Dq} + 2 W_{Jq}` (8-variable transforms);
- for **every** `z in F_2^8`, `W_{Jq}(z) = 4 kappa (mod 8)`.

*Proof:* `H q = 128 v`. The quadratic `Dq` has the same polar form as `D`. If its rank is `2h`,
then its Walsh values lie in `{0,+2^(8-h),-2^(8-h)}`, with `h<=4`; thus **16 divides every
`W_{Dq}(z)`**, including zero values. Also `W_sigma(z) = 256 - 2 wt(sigma) (mod 4)`.
Theorem 4 gives `wt(sigma)=kappa (mod 2)`. Reducing the first identity modulo 16 proves the congruence. ∎

The congruence alone also holds for **every balanced** `f` with `s != 0`, without the cap:
use the general digit identity with carry, whose additional term is a multiple of 16 before this
reduction, and the general digit-parity statement of Lemma 1. Only the exact identity without carry
and the interpretation `sigma=[W<0]` require the target cap. This distinction explains why the
general balanced controls satisfy the congruence; it is not by itself a target obstruction.

## 5. Odd-coset duality bound (all seven types)

**Proposition 6.** For any `g: F_2^8 -> F_2`, `sum_y v(y) W_g(y) = 2 sum_a (-1)^{g(a)} q(a)`.

For `g = Jq`, `(-1)^{Jq} q` equals `+|q|` when `|q| <= 3` and `-|q|` when `|q| >= 5`. Hence

`L_O/2 := 14 n28 + 10 n20 - 6 n12 - 2 n4 = -sum_y v W_{Jq} <= sum_{y in supp v} |W_{Jq}(y)|`,

where `n_k` counts `|W| = k` on the odd coset and `|supp v| = m' = sum_odd W^2 / 1024`. The lattice data:

- An 8-variable degree<=4 function has `W mod 16` affine in the frequency, after the constant mod-8 class.
- If rank D <= 6: `W_{Jq}` lies in `8Z`, and `W_{Jq}/8 mod 2` is affine.
- If rank D = 8: `W_{Jq}(y) = (-1)^{l(y)} w(y)` with `l` affine and `w` in `c0 + 16Z`, and
  `|sum_y v(y)(-1)^{l(y)}| = |H v(lambda)| <= 14`.

`m'` is fixed by the even-coset histogram: `16 m' = 3072 - 5d + 4z + 8c`. Exact maximization of the
right-hand side over these lattices (`code/oside_ilp.py` helper `M_bound`, and the twisted rank-8 version)
forces `a = n4 + n12` to be at least about 5–15 for every remaining type at small `(z, c)`. The table is
recorded in `evidence/oside-bounds.json`. These bounds come from a single implementation and need an
independent re-derivation before being cited.

## 6. Type (2,192): cubic duality (imports WLW Theorem 3)

**Proposition 7.** After Lemma 2, `d2` is cubic (`Pf4` of a rank-2 form vanishes), and so is
`g' = d2 + (1 + d0)(1 + d1)`. WLW Theorem 3 gives `||W_g||_1 <= 10240` for cubic `g`.

Duality gives `-sum_a (-1)^{g(a)} W(a) = -sum_x F(x) W_g(x) <= ||W_g||_1`. Combined with the exact
histogram identity

`L = 21248/3 + (52/3) d - (64/3) c + (16/3) z - (80/3) n12 - 16 n4 + 16 Delta`

(checked exactly by rational arithmetic; `Delta = n_{W=+16} - n_{W=-16}` on `{D = 0}`), this yields for
`(2,192)`:

`4c + 5 n12 + 3 n4 >= 32 + z + 3|Delta|`.

## 7. Rank-8 rigidity

**Proposition 8.** For types `(8,120)` and `(8,136)`, take the 9-variable quadratic
`Phi(y, x9) = Dtilde(y) + x9 + c'`, where `Dtilde` is the bent dual of `Dq` and `c'` is chosen suitably.
Then `|W_Phi| = 32` on the odd coset and `0` on the even coset, and

`d(f, Phi) = 256 - |Gamma|/32 = 48 + 1.25 d - 2(a + c) - z`,

using the reviewed slack identity `Gamma = 40d - 6656 - 64(a+c) - 32z`. Equivalently, `v = -(-1)^{Dtilde}`
on `supp v` except at `48.25 - 0.375z - 0.75c - a` points (for d=120).

## 8. Where this stops (decisive obstruction)

Aggregate per-point integer models were solved by CP-SAT; these are exploratory, not certificates. Over
point types `(v, W_{Dq}, W_{Jq})`, with the twisted rank-8 sign and the bent-dual weight, they include every
identity of Sections 4–7 and all lattice classes. They are feasible for all seven types
(`evidence/oside-ilp-kappa0.jsonl`, `evidence/oside-ilp-rank8.jsonl`). The new conditions force many small
odd-coset values, while nothing proved caps them strongly enough: the prior cap is `a + c + z/2 <= 28..50`,
and rank 8 has no cap. Feasible relaxations are not Boolean functions.

A Gaussian-sphere count heuristic gives about `2^-63` expected `s != 0` cap-28 functions. The same
heuristic gives about `2^96` for the `s = 0` class, where Kavut–Yücel tables exist. This suggests, but
**does not prove**, nonexistence.

Remaining bounded routes are specialist partial at best:

- (a) The near-rigid regime of `(2,192)`: when `L > 10048`, WLW's proof forces `16 | W_{d2}` and
  `F = -sgn W_{d2}` up to about 10 points. That leaves a finite residue-involution check over the
  Brier–Langevin cubic classes.
- (b) Rank 8 via `f = Phi + 1_M`.

No route to full resolution was identified.
