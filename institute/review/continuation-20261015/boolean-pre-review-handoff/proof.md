# Spectral residue and canonical-sign completion obstructions

This is a restricted-class result for `info-p0403`, not a proof of the book problem, and not a novelty claim. All arithmetic below is integral. The computations have not been Lean-verified.

**Attribution.** Affine sign normalization of an odd Walsh spectrum and its quadratic low bit are prior art: Wang–Lou–Wang, [arXiv:2610.17871v1](https://arxiv.org/abs/2610.17871), proof of Theorem 1, equations (31)–(32). Their normalized quadratic `q=(K-2)/8 mod2` equals our `J_H`, since `K=2+8t` implies `(K^2-4)/32=t mod2`. Their Lemma 4 uses the paired-half capacity identity and Parseval. This self-contained proof applies those known tools to the explicit finite corpus; no unrestricted theorem of that preprint is assumed and no new general mechanism or priority is claimed.

## 1. Exact fixed-half question

For each of the 252 records that **passed** the epoch-2 necessary-condition screen, let `v` be its nonzero nine-bit normal. Fix `g(y)=f(x(y))` on `v.x=0`, where `x(y)` is the basis map stored in the certificate. The 256 values on the other coset are arbitrary; write them as `h(y)=f(x(y)+s)`, with `v.s=1`. Both spectra use the same eight-bit character coordinates:

`G(a)=sum_y (-1)^(g(y)+a.y)`, and likewise `H(a)`.

The nine-variable Walsh coefficients occur in pairs `G(a)+H(a)` and `G(a)-H(a)`, up to signs. Thus every magnitude is at most 28 exactly when

`|G(a)|+|H(a)| <= 28` for every `a`.

The full table has a Walsh zero exactly when `H(a)=+G(a)` or `-G(a)` somewhere. Adding the corresponding linear output function then balances the table and permutes its Walsh spectrum. In particular, a table with no Walsh zero cannot be balanced by a linear output shift.

Each fixed half has odd weight. Any completion with a Walsh zero has even total weight, so its other half also has odd weight. Consequently every `H(a)` is two modulo four and is nonzero. The initial slice screen was not an enumeration of completions: all 252 listed classes were unresolved by it. The old proof-capped and time-capped runs remain UNKNOWN and are not used here.

## 2. The quadratic square-residue lemma

Let `h:F_2^8 -> F_2` have odd support size `w`. For `S=support(h)` set `I(a)=sum_{x in S} (a.x mod2)`, an ordinary integer. Direct expansion gives

`H(a)/2 = 128*1_(a=0) - w + 2 I(a)`.

The first term vanishes modulo eight. If `t` is odd, `(t^2-1)/8` is an integer and its parity depends only on `t mod8`. Hence

`J_h(a) := (H(a)^2-4)/32 mod2`

`= (w^2-1)/8 + binom(I(a),2) + ((1-w)/2) I(a) mod2`.

Every `l_x(a)=a.x` is a linear Boolean form. Since

`binom(I(a),2)=sum_{unordered distinct x,y in S} l_x(a) l_y(a)`,

`J_h` has Boolean degree at most two. Negative Walsh values cause no exception because the definition uses squares. Among possible magnitudes at most 26,

* `J=0`: `2,14,18`;
* `J=1`: `6,10,22,26`.

For a direct support-moment audit, let `c_i=sum_{x in S} x_i` and `M_ij=sum_{x in S} x_i x_j`. The constant coefficient of `J_h` is `(w^2-1)/8 mod2`; its linear coefficient at `i` is `binom(c_i,2)+((1-w)/2)c_i mod2`; its `ij` coefficient is `c_i c_j + M_ij mod2`. The independent checker constructs these coefficients without fitting a polynomial to a spectrum.

Where `|G(a)|=26`, the capacity `28-|G(a)|=2` forces `J_h(a)=0`. Quadratic functions on eight variables form a 37-dimensional vector space with monomials `1,a_i,a_i a_j`. Evaluation on those forced-zero indices is a binary linear system. The exact ranks in this corpus are 31 through 36, so only 2 through 64 possible quadratics remain per class. Both implementations compute and exhaust the entire nullspace, using different pivot conventions and different monomial orderings.

For each such quadratic `J`, define

`D_a={m in {2,6,10,14,18,22,26}: m<=28-|G(a)|, (m^2-4)/32 mod2=J(a)}`.

If a domain is empty, reject the quadratic. Otherwise let `m0(a)=max D_a` and `S0=sum_a m0(a)^2`. Parseval requires `sum_a H(a)^2=65536`. A zero at index `a` additionally requires `|G(a)| in D_a` and fixes that square to `G(a)^2`. Therefore a necessary condition is

`max_(a:|G(a)| in D_a) (S0-m0(a)^2+G(a)^2) >= 65536`.

Rejecting every quadratic with this inequality excludes the class completely, not just sampled functions. This first new stage rejects 152 of the 252 classes.

## 3. Autocorrelation residue with an energy budget

For an odd-weight `h` and nonzero `d`, partition the domain into the 128 pairs `{x,x+d}`. The number `u_d` of unequal pairs is odd, because the parity of `w` equals the parity of that count. The autocorrelation is

`AC_h(d)=sum_x (-1)^(h(x)+h(x+d))=256-4u_d=4 mod8`.

Walsh orthogonality gives

`sum_a (-1)^(a.d) H(a)^2 = 256 AC_h(d) = 1024 mod2048`.

Write `delta_a=m0(a)^2-H(a)^2 >=0`. Its total is `Delta=S0-65536`. Every character sum of `delta` has absolute value at most `Delta`. Thus, if any nonzero character sum of the maximal squares is farther than `Delta` from every integer congruent to 1024 modulo 2048, the quadratic cannot be completed. Rejecting all quadratics this way rejects a further 71 classes.

This is stronger than checking only Parseval. The checker also computes every autocorrelation directly on deterministic odd tables to audit the identity and its odd-weight congruence.

## 4. Canonical signs remove the missing affine phase

For odd `h`, let `s=XOR_(x in S) x` and `epsilon=(-1)^((w+1)/2)`. Reduction modulo four gives

`H(a)/2 = -w+2 I(a) = epsilon*(-1)^(a.s) mod4`.

For a nonzero magnitude `m=2 mod4`, define its canonical signed value

`k(m)=m` if `m=2 mod8`, and `k(m)=-m` if `m=6 mod8`.

Every `k(m)` is two modulo eight. Its sign is uniquely fixed by that residue. Consequently the canonical spectrum `K(a)=k(|H(a)|)` satisfies

`K(a)=epsilon*(-1)^(a.s) H(a)`,

and exact Walsh inversion gives

`sum_a (-1)^(a.x) K(a) = epsilon*256*(-1)^h(x+s)`.

Thus its inverse character sums are all `+256` or `-256`. Conversely, any integer vector with that inverse property is the Walsh spectrum of a Boolean sign table, and multiplication by a sign character and by a global sign translates/complements that table. No 512-way sign-phase search is necessary.

Let `K0(a)=k(m0(a))`. Within a fixed `J` class the permitted canonical values are

* `J=0`: `2,-14,18`;
* `J=1`: `-6,10,-22,26`.

For every `m` in the corresponding domain,

`4|k(m0)-k(m)| <= m0^2-m^2`.

This is checked for every finite allowed pair. It also follows by factoring the difference of squares: if the canonical signs agree the magnitude sum is at least four, while if they disagree their distinct magnitudes differ by at least four. Therefore

`sum_a |K0(a)-K(a)| <= (S0-65536)/4`.

Every inverse character coordinate changes by at most that L1 distance. If any inverse character sum of `K0` is farther than `(S0-65536)/4` from both `+256` and `-256`, no completion exists. This rejects a further 28 classes and leaves exactly one class at this stage: source 96, normal 511.

## 5. Final finite-domain formulation

For the one remaining class, only the quadratic coefficient mask `7887107311` survives (producer's stated monomial order). Its maximal square sum is `69120`, leaving exact energy deficit `3584=64*56`. At each spectral index choose `m(a)` from its stored finite magnitude domain, form `K(a)=k(m(a))`, and require

`sum_a (-1)^(a.x) K(a) in {-256,+256}` for all 256 input indices.

Equivalently write `K=K0-16e`. Every local choice gives an integer pair

`e(a)=(K0(a)-k(m(a)))/16`, `d(a)=(m0(a)^2-m(a)^2)/64`.

The exact problem is

* each `(e(a),d(a))` belongs to its explicit local list;
* `sum_a d(a)=56`;
* `sum_a (-1)^(a.x)e(a)=inverse(K0)(x)/16 +/-16` for every `x`.

A SAT model of these equations must still be reconstructed as a complete truth table and independently checked. A solver-only UNSAT status is not a negative certificate. Requiring equality of `m(a)` and `|G(a)|` somewhere adds the Walsh-zero condition; omitting it searches a larger class, so a correctly certified exclusion of the larger class would suffice. Every finite domain is included; some have four values, not three.

### 5.1 A complete parity-coset certificate, not a solver verdict

The exact equations imply

`FWHT(e)(x) = r(x) mod32`, where `r(x)=inverse(K0)(x)/16-16`.

For a subset `T` of the eight coordinate positions, let `Delta_T` be the integer mixed difference on the Boolean cube at its origin:

`Delta_T r = sum_(U subset T) (-1)^(|T|-|U|) r(1_U)`.

Expanding the character as `(-1)^(a.x)=product_(i:x_i=1)(1-2a_i)` gives the exact identity

`Delta_T FWHT(e) = (-2)^|T| sum_(a:T subset support(a)) e(a)`.

For `|T|<=4`, the congruence modulo 32 therefore implies

`sum_(a:T subset support(a)) e(a) mod2 = (Delta_T r/(-2)^|T|) mod2`.

The quotient is integral in this instance and is explicitly checked. These are 163 affine binary equations, one for each subset of size zero through four. At the 90 spectral indices with maximum magnitude two the only local choice is `e=d=0`; the other 166 parity variables remain. Independent binary elimination gives rank 147 and dimension 19. The certificate supplies a particular solution and 19 independent homogeneous basis vectors, while the checker derives a different basis from scratch.

The local magnitude domains give the following **minimum deficit when `e` is odd**, with zero a lower bound when it is even:

| Maximal magnitude | Count | Minimum odd-parity `d` |
|---|---:|---:|
| 2 | 90 | impossible (`e=0`) |
| 10 | 6 | 1 |
| 14 | 30 | 3 |
| 18 | 40 | 5 |
| 22 | 60 | 7 |
| 26 | 30 | 3 |

For example, a maximal magnitude 22 has canonical value -22 and local choices `(e,d)=(0,0),(-2,6),(-1,7)`. A maximal magnitude 26 has `(e,d)=(0,0),(3,3),(1,9),(2,10)`. No local choice is omitted.

Both implementations enumerate all `2^19=524288` parity words in the affine solution space and sum these unavoidable local deficit costs. The minimum is **140**, attained by six parity words. But the exact Parseval deficit budget is only **56**. Thus every possible parity pattern already costs too much before its even corrections or any higher congruences are considered:

`sum_a d(a) >= 140 > 56`.

This is a complete contradiction for the final class. It does not use the zero condition, and so excludes the larger problem of an odd complementary half satisfying all 28-bound inequalities. The stored cost histogram, particular solution, kernel, local domains, and all mixed-difference equations are sufficient compact replay evidence. The checker imports neither the producer nor a solver, uses direct character sums, explicit corner sums instead of a Moebius transform, opposite pivot conventions, and a different enumeration order. A planted balanced bound-32 completion in this same half validates the finite-domain-to-parity correspondence without satisfying the false target exclusion.

## 6. Coverage and equivalence

All 252 source-normal pairs are explicitly mapped to the new certificates in their pinned original order. The computations screen all of them; no unproved equivalence is used to skip a class. There are 154 literal `|G|` arrays in the stated eight-bit coordinates. Equality of these arrays gives the same magnitude-completion question, with the identity spectral-coordinate map. It also preserves the zero-existence question, since that requires only equality of magnitudes at an index and the freely chosen complement of `h` can match its sign there. The mapping to all 252 classes is retained. This is not an exhaustive EA-equivalence classification and does not assert that different groups are inequivalent.

All 252 formerly screened-but-unresolved classes are therefore excluded, with exact balanced maximum 240 attained by their pinned original sources. Together with the accepted epoch-2 screen's 31492 other exclusions, this closes all 31744 **listed** source-normal classes. No distinct-function count is asserted. The unrestricted balanced maximum remains in `{240,242}` until an explicit balanced witness or a global proof is supplied.
