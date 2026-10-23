# Candidate universal obstruction: quadratic residue distance at least 96

Status: **written proof; independently reviewed by Claude Opus 5.5 (correct, five exposition fixes applied) and Codex `gpt-6.1-sol` (ACCEPT, no fixes; reviewed SHA-256 `dca8ce2e…c604`). Not formally verified or human peer reviewed.** This is a universal necessary condition on two odd-weight eight-variable halves, not a proof that balanced NL242 functions do not exist. Novelty is unestablished. The quadratic residue and canonical-sign tools are prior art (Wang–Lou–Wang, arXiv:2610.17871v1); the argument below is a proposed additional consequence, written during the authorized continuation. `SHARPER.md` strengthens the bound to112.

## Statement

Let `g,h:F_2^8 -> F_2` both have odd weight. Write their Walsh spectra as `G,H`, and suppose

```
|G(a)| + |H(a)| <= 28     for every a in F_2^8.
```

Define the Boolean quadratic residue functions

```
J_g(a) = (G(a)^2-4)/32 mod2,
J_h(a) = (H(a)^2-4)/32 mod2,
D = J_g + J_h    (sum over F_2).
```

Then the proposed necessary condition is

```
wt(D) >= 96.
```

The conclusion needs no Walsh-zero or balance assumption beyond the two halves being odd. For a balanced nine-variable target with nonzero support XOR `s`, each hyperplane whose normal has dot product one with `s` gives such an odd split. The condition is not sufficient for a completion.

For completeness, nonzero `s` is already necessary for a balanced peak-at-most28 target, by the elementary argument in Wang–Lou–Wang Proposition1; it is not a new claim here. If `s=0`, all Walsh values are divisible by8, hence bounded by24. The residue `q=W_f/8 mod2` is quadratic and `q(0)=0`. Thus the nonzero quadratic `1+q` has weight at least128, and Parseval would give `sum W_f^2 <= 128*16^2+384*24^2=253952<262144`, a contradiction. Section6 keeps `s!=0` explicit so its correspondence stands on its own.

## 1. Imported elementary tools and quadratic normal forms

For any odd-weight eight-variable Boolean function, every Walsh coefficient is two modulo four and nonzero. Its `J` above is quadratic. Canonically sign a magnitude `m` by `k(m)=m` for `m=2 mod8`, and `k(m)=-m` for `m=6 mod8`. The canonical spectrum `K` differs from the actual Walsh spectrum by an affine sign character. Therefore its character transform has only the values `+256,-256`; in particular `sum K=+256` or `-256`, and `sum K^2=65536`. Proofs are supplied in [the parent proof](../proof.md): these facts follow directly from odd support weight, character orthogonality and the support-moment expansion.

We also use the standard elementary normal form for a Boolean quadratic on `F_2^m`. Its polar alternating bilinear form has even rank `r`; choosing a symplectic basis gives `r/2` disjoint products, plus a linear form on the radical and a constant. If the radical-linear part is nonzero, the sign sum is zero by cancellation. Otherwise summing each two-variable product gives sign-sum magnitude `2^(m-r/2)`. Thus the possible nonzero sign biases are `+/-2^(m-r/2)`. An affine change of variables removes linear terms on the nondegenerate pairs.

Consequences used here:

- A nonzero quadratic on eight variables has weight at least64. Weight64 forces polar rank2 and, after an invertible affine coordinate change, the function is exactly `u*v` on two coordinates. There is no possible quadratic weight strictly between64 and96: rank2 gives64/192, rank4 gives96/160, higher ranks give112/144 or120/136, and a radical-linear part gives128.
- Quadratics on six variables with common polar rank `r>=4` have individual sign biases in `{0,+/-16}` (rank4) or `{+/-8}` (rank6). The sum of three such biases cannot be−64.

## 2. A complete pointwise inequality

Let `m=|G(a)|`, `n=|H(a)|`, `S(a)=k(m)+k(n)`, and let `D(a)=J_g(a)+J_h(a)` in `{0,1}`. Both magnitudes belong to `{2,6,10,14,18,22,26}`, with `m+n<=28`. On this finite domain,

```
m^2+n^2 + 4 S(a) <= 408 + 384 D(a).             (1)
```

This can be checked on every ordered pair. Its equality cases are exactly:

- `D=0, J_g=J_h=0`: `(m,n)=(2,18)` or `(18,2)`, giving `S=20`;
- `D=0, J_g=J_h=1`: `(6,22)` or `(22,6)`, giving `S=-28`;
- `D=1`: `(2,26)` or `(26,2)`, giving `S=28`.

Summing (1), using the two Parseval identities and `sum S >= -512`, gives

```
131072 - 2048 <= 104448 + 384 wt(D),
wt(D) >= 64.                                    (2)
```

Thus `D` is a nonzero quadratic. Only the equality case `wt(D)=64` remains to exclude before the standard weight spectrum implies96.

## 3. Consequences of a hypothetical weight64 difference

If `wt(D)=64`, every inequality used in (2) is an equality. In particular both canonical spectra have sum−256, `sum S=-512`, and every point is one of the equality pairs above. Let `A` count the points where `D=0` and `J_g=J_h=0`; the remaining `192-A` points with `D=0` have both residues1. Hence

```
-512 = 64*28 + A*20 - (192-A)*28,
A=64.
```

There are exactly128 points with `D=0,J_g=1`. The full pointwise sum is determined by the two quadratics:

```
S(a) = 20 - 48 J_g(a) + 8 D(a) + 48 J_g(a) D(a),  (3)
```

where the right side is ordinary integer arithmetic on Boolean values. Also

```
sum_a S(a)^2 = 64*20^2 + 192*28^2 = 176128.       (4)
```

## 4. The sum spectrum has a nontrivial translation symmetry

Use an invertible affine change of frequency coordinates to put `D(u,v,z)=u*v`, where `z in F_2^6`. An affine frequency change preserves both the energy of `S` and the bound that its character transform has magnitude at most512: its transform only permutes indices and multiplies by signs.

The three restrictions of `J_g` to `(u,v)=(0,0),(0,1),(1,0)` are quadratics on six variables with a common polar quadratic part; only their linear and constant terms differ. Their total number of ones is128, among192 points, so their three sign biases sum to

```
192 - 2*128 = -64.
```

By the six-variable bias consequence in Section1, their common polar rank cannot be4 or6; it is at most2.

Write, in these coordinates,

```
J_g(u,v,z) = Q(z) + L0(z) + u L1(z) + v L2(z)
             + c*u*v + b*u + a*v + d,
```

with `Q` a homogeneous quadratic of polar rank at most2 and `L0,L1,L2` linear forms. Let `R` be the radical of its polar bilinear form. Its dimension is at least4. The restriction of `Q` to `R` is linear, since its polar form vanishes there. Hence the three linear conditions

```
L1(tau)=0,   L2(tau)=0,   Q(tau)+L0(tau)=0
```

leave at least a one-dimensional solution space in `R`. Choose a nonzero `tau` in it. For every `u,v,z`, the change in `J_g` under `z -> z+tau` is

```
B_Q(z,tau)+Q(tau)+L0(tau)+u L1(tau)+v L2(tau)=0.
```

The function `D=u*v` is unchanged as well, so (3) makes `S` invariant under a nonzero translation. Its character transform vanishes on the128 frequencies taking value one on that translation, and is supported on at most128 frequencies. This argument includes every cross term and any linear term induced by a coordinate change; it does not mistakenly count a rank-two quadratic as depending on just two original coordinates.

## 5. Fourier-energy contradiction

Before any affine coordinate change, the character transform of `S=K_g+K_h` is the sum of two values each equal to+256 or−256, so its magnitude is at most512. The same magnitude bound holds after the affine frequency change above. Support at most128 and Parseval therefore imply

```
256 * sum_a S(a)^2 <= 128*512^2,
sum_a S(a)^2 <= 131072.
```

This contradicts (4), which gives176128. Therefore `wt(D)!=64`. Combining (2) with the possible weights of an eight-variable quadratic proves the proposed `wt(D)>=96`.

## 6. Intrinsic necessary condition on a balanced nine-variable spectrum

Let `f:F_2^9 -> F_2` be balanced with Walsh peak at most28 and nonzero
support XOR `s`. Then the proposed corollary is

```
#{a : a.s=0 and |W_f(a)| in {8,24}} >= 96.
```

Choose a hyperplane `V=ker(v)` with `v.s=1`, an isomorphism
`B:F_2^8 -> V`, and use `s` itself as the complementary-coset origin.
Write `g(y)=f(By)` and `h(y)=f(By+s)`. Both halves have odd weight:
the parity on `V` is `wt(f)+v.(XOR support(f))=1`. Moreover their
support XORs in eight-dimensional coordinates coincide, since

```
s = B(supportXOR(g)+supportXOR(h)) + (wt(h) mod2)*s.
```

Characters orthogonal to `s` restrict bijectively to characters on `V`;
for corresponding `a,b`, `W_f(a)=G(b)+H(b)`. Because
`wt(g)+wt(h)=256`, the canonical phases satisfy
`epsilon_h=-epsilon_g`. Their equal support XORs then give
`G+H=0 mod8` and `G-H=4 mod8`. Equivalently, balance gives the direct
congruence `W_f(a)=4(a.s) mod8`. Thus the following two integrality
statements use balance, not equal half-support XORs alone:

```
U=(G+H)/8 in Z,       V0=(G-H)/4 in 2Z+1.
```

Then `G/2=2U+V0` and `H/2=2U-V0`, so

```
J_g+J_h = (G^2+H^2-8)/32 mod2
          = U^2+(V0^2-1)/4 mod2 = U mod2.
```

The last term vanishes modulo two because the square of an odd integer
is one modulo eight. On `a.s=0`, the only possible magnitudes are
`0,8,16,24`; hence `U` is odd exactly at magnitudes8 or24. The half-pair
theorem proves the count bound96. This is still only a necessary
condition; it neither constructs a target nor rules out all targets.

## Verification and limits

`audit.py` checks the entire finite domain in (1), its equality cases, all integer constants, the canonical rank/bias possibilities used in the contradiction, and genuine odd-half examples showing the capacity hypothesis is essential. `majorant-negative-control.json` records that a deliberately weakened majorant is rejected at a genuine equality pair. Finite tests do not replace the universal proof, and they do not certify novelty. The common-rank restriction and translation step were explicitly audited in `independent-review.json` and the Codex review.
