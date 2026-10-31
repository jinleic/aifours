# Strict gain reduces to cubic alphabets and non-identifying syndromes

**Status: WRITTEN, conditional on the checked compact dual; scientific review pending.** The original strict-gain problem is equivalent to the existence of some integer `m>=2` and an original-neighbour FD support

\[
W\subset((\mathbb Z/m\mathbb Z)^3)^{10},\qquad |W|>m^{20}.\tag{44}
\]

This equivalence uses the standard triangle-factor grouping of each vertex's three components. Moreover, any such strict support, under **every** choice of bijection of each vertex's `m^3` labels with those three group components, must have a syndrome projection collision on at least one of the five factors `123,145,167,389,4·8·10`: two distinct full syndrome vectors induce the same syndrome on that factor.

## Proof

A support satisfying (44) directly provides a fixed-alphabet strategy with `q=m^3` and gain above `20/3`. Conversely, if an alphabet `q` and FD support `W_0` have `|W_0|>q^(20/3)`, take `n` independent Cartesian products and embed the `q^n` symbols at each vertex into `m^3` symbols with `m=ceil(q^(n/3))`. The graph FDs extend by arbitrary outputs outside observed neighbour tuples. The ratio `|W_0|^n/m^20` exceeds one for all sufficiently large `n`, since it is at least `(|W_0|/q^(20/3))^n/(1+q^(-n/3))^20`.

For the additional necessary condition, choose any such vertex relabelings and apply `frontier-20261028-five-factor-syndrome-criterion-v1.md` SHA-256 `ee2694c7c02b2d2bab934723d86d13fda7ede452d59ebf71a81faaa4368e1e49` to the uniform law on the support. If all five syndrome coordinates individually distinguish all full syndrome vectors, that theorem gives `H(X_V)<=(2/3)sum H(X_v)<=20 log m`, contradicting `|W|>m^20`. Therefore at least one of the five coordinates has a collision. This conclusion remains valid for any nonabelian choice of group of order `m` in each factor.

This corrected caller requires no assertion that two syndromes are impossible: that stronger conclusion depends on separate review of `frontier-20261028-two-syndrome-repaired-theorem-v1.md` SHA-256 `9feb6cd50a2b376b971c2091369b5c5ad7d50e18446ce4cd3293bfc718b776b1`. It incorporates the required earlier source erratum and is not a witness, a no-go, formal verification, independent scientific adoption, or novelty clearance.
