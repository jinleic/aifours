# Independent derivation: a quadratic residue of an odd-weight Walsh spectrum

This is a parent proof audit of a candidate necessary-condition mechanism reported by the Boolean continuation. It is not a global nonexistence proof or a novelty verdict. The class-exclusion count requires a separate checked completeness argument.

**Priority correction.** The source audit located the same normalized quadratic
in Wang–Lou–Wang, [arXiv:2610.17871v1](https://arxiv.org/pdf/2610.17871v1),
proof of Theorem 1: canonical `K=2+8t` gives `(K^2-4)/32=t mod2`.
Their Lemma 2 supplies the residue-degree argument and their Lemma 4 already
uses the paired-half capacity identity. The independently derived formulas
below reproduce those tools; only their checked application to the explicit
fixed-half corpus is a candidate contribution. No new general mechanism is claimed.

Let `m >= 4`, let `S` be the support of an odd-weight Boolean function `h` on `F_2^m`, and write `w=|S|`. For a character index `a`, put `l_x(a)=a dot x` in `{0,1}` and `I(a)=sum_{x in S} l_x(a)`. Its Walsh transform satisfies

```
H(a)/2 = 2^(m-1) * 1_{a=0} - w + 2 I(a).
```

Consequently `H(a)/2` is odd and congruent to `-w+2I(a)` modulo eight. For odd integers, changing the argument by eight changes `(t^2-1)/8` by an even integer. Therefore

```
J_h(a) := (H(a)^2-4)/32 mod 2
        = (w^2-1)/8 + (I(a)^2-w I(a))/2 mod 2
        = (w^2-1)/8 + binom(I(a),2) + ((1-w)/2) I(a) mod 2.
```

Here all displayed quotients are integers. Since each `l_x(a)` is a Boolean value,

```
binom(I(a),2) = sum_{unordered distinct x,y in S} l_x(a) l_y(a).
```

Modulo two, each `l_x` is a linear form. Thus `J_h` is a Boolean polynomial of degree at most two. This argument also covers `a=0`, and negative Walsh coefficients cause no sign exception because only squares occur. Equivalently, `J_h(a)=1` exactly when `|H(a)| mod 16` is six or ten.

## Explicit coefficient formula for an independent check

Let `c_i` count support points with coordinate `i` equal to one, set `s_i=c_i mod 2`, and let `M_ij` count support points whose coordinates `i,j` both equal one. In the square-free Boolean polynomial, the constant, linear, and cross coefficients are

```
constant = (w^2-1)/8 mod 2,
linear_i = binom(c_i,2) + ((1-w)/2) c_i mod 2,
cross_ij = s_i s_j + M_ij mod 2   (i<j).
```

The cross formula follows by expanding the product of the two coordinate sums and removing equal-support-point terms. It is a direct support-moment derivation, independent of a producer's fitted quadratic or Walsh implementation.

For a fixed odd-weight half-table with spectrum `G`, a target completion must obey `|G(a)|+|H(a)| <= 28`. Wherever `|G(a)|=26`, its odd-weight complementary half has `|H(a)|<=2`, hence `J_h(a)=0`. The permissible quadratics are the nullspace of these linear evaluation constraints in the 37-dimensional quadratic-function space for eight variables. Restricting spectral capacities by each possible quadratic and applying Parseval and a necessary Walsh-zero condition is a valid rejection strategy if every possible quadratic and zero position is covered. Passing it does not construct a Boolean completion.

The accompanying `boolean_residue_audit.py` checks the coefficient identity using direct character sums on deterministic odd-weight tables, not the research producer's transform or fit. It also checks a corrupted spectrum with one coefficient changed by eight is rejected. Finite controls support the implementation audit; the proof above supplies the universal argument. No priority or Lean-kernel claim is made.

## Independent derivation: canonical signed spectrum

For the same odd-weight function, `H(a)/2 = -w + 2 I(a) (mod 4)`. Write
`s=XOR(S)` and `epsilon=(-1)^((w+1)/2)`. Since `I(a) mod 2 = a dot s`,

```
H(a)/2 = epsilon * (-1)^(a dot s) (mod 4).
```

Define `K(a)` to be `|H(a)|` when that magnitude is two modulo eight, and
`-|H(a)|` when it is six modulo eight. All coefficients are nonzero and
`K(a)=2 (mod 8)`. The residue above determines the sign exactly:

```
K(a) = epsilon * (-1)^(a dot s) * H(a).
sum_a (-1)^(a dot x) K(a) = epsilon * 2^m * (-1)^h(x+s).
```

The second identity is Walsh inversion. Thus the inverse transform of `K`
has only the values `+2^m` and `-2^m`, without needing to guess its missing
affine sign phase. Conversely, any proposed integer vector with inverse
transform in those two values is the Walsh spectrum of a Boolean sign
table; modulation and complementation recover any permitted affine phase.

For eight variables and capacity `c(a)=28-|G(a)|`, consider every nonnegative
magnitude at most `c(a)` that is two modulo four and has the specified bit
`J(a)=(magnitude^2-4)/32 mod 2`. Let `m0(a)` be the largest permitted
magnitude and `K0(a)` its canonical sign. An empty domain rejects that
quadratic candidate. Since `|G(a)|>=2`, the largest possible capacity is 26.
For `J=0`, the possible canonical values are `2,-14,18`; for `J=1`, they are
`-6,10,-22,26`, restricted by the local capacity.

For any permitted value `K(a)` with magnitude `m(a)`,

```
|K0(a)-K(a)| <= (m0(a)^2-m(a)^2)/4.
```

This is a finite inequality on the two explicitly displayed sets of signed
values. It can also be seen by separating equal-sign and opposite-sign
pairs: a nontrivial same-bit pair has magnitude sum at least four, and an
opposite-sign pair has magnitude difference at least four. For a Boolean
completion, Parseval gives `sum_a m(a)^2=65536`. Therefore

```
sum_a |K0(a)-K(a)| <= (sum_a m0(a)^2-65536)/4 =: L.
```

Every character-transform coordinate changes by at most that same `L`.
If any coordinate of the transform of `K0` is farther than `L` from both
`+256` and `-256`, no Boolean completion exists for that quadratic.
Negative slack also rejects immediately. This is a necessary-condition
screen, not a sufficiency theorem or a universal exclusion of NL242.

A full nine-variable table has a Walsh zero exactly when some coefficient
of `H` equals `+G` or `-G`. Since complementation of the free half is
permitted, existence within the class can equivalently require equality
of magnitudes at some index, followed by the appropriate phase and linear
output shift. Positive claims must still reconstruct and directly check
the resulting full balanced table.
