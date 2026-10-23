# Mod-eight type of an even-weight Boolean function

This is an elementary application of known Walsh residue expansions, **not a new general mechanism** and not a global exclusion of balanced NL242 functions. The 2026 preprints are literature context, not imported correctness premises.

Let `f:F_2^9 -> F_2`, `T=support(f)`, `w=|T|`, and `s=XOR_(x in T)x`. For a character `a`, let `I(a)=#{x in T:a.x=1}`. Directly,

`W_f(a)=512*1_(a=0)-2w+4I(a)`.

If `w` is even, `I(a) mod2=a.s`, so

`W_f(a) = -2w+4(a.s) mod8`,

or equivalently `W_f(a)/4 mod2 = -w/2+a.s`.

Consequences:

1. If `s=0` and `w=2 mod4`, every coefficient is four modulo eight. None can be zero, and no linear output addition can balance `f`.
2. If `s=0` and `w=0 mod4`, every coefficient is zero modulo eight. This does **not** alone prove the existence of a zero coefficient. Under a peak bound28, all magnitudes would be at most24; we do not import an unrefereed theorem to exclude that stronger-nonlinearity possibility.
3. If `s!=0`, exactly256 coefficients are zero modulo eight and256 are four modulo eight. This is a residue count, **not** a Walsh-zero existence theorem.
4. If `w` is odd, every Walsh coefficient is two modulo four, and no coefficient is zero modulo eight. The exact circuit search includes this weight parity too; the bounded heuristic deliberately preserves even weight.

The independent checker reconstructs all five published Kavut–Yücel tables and verifies, by both512 direct character sums and FWHT, that each has peak28, support XOR0, weight2 modulo4, and all512 coefficients four modulo eight. This explains their known lack of Walsh zeros; it does not prove all NL242 functions have that type.

## Degree and affine-invariance interpretation

For any even-weight nine-variable function, its degree-nine ANF coefficient is zero. The parity `sum_x f(x)x_i` is exactly the degree-eight ANF coefficient missing `x_i`. Thus `s=0` is equivalent to degree at most seven, while `s!=0` is equivalent to degree exactly eight.

For even-weight functions, input translation preserves `s`: `XOR_(x in support(f(.+t)))x = s+(w mod2)t=s`. An invertible linear input change maps `s` by its inverse. Adding an affine output function leaves `s` unchanged, since every coordinate support sum of an affine function is even in nine variables. Therefore zero versus nonzero `s` is extended-affine invariant in this even-weight setting. Affine transformations of the five degree-seven published seeds cannot supply the desired degree-eight type.

A balanced NL242 function must have nonzero `s`, by the accepted elementary degree bound. More generally, any NL242 table with a Walsh zero can be linearly shifted to such a balanced function, preserving `s`; it therefore also has nonzero `s`. But **the converse is not proved**: a hypothetical NL242 table with nonzero `s` could still have no Walsh zero. That is the intermediate construction target exercised here.

## Literature positioning

- Kavut–Yücel, [arXiv:0808.0684v1](https://arxiv.org/abs/0808.0684), Section3.1, explicitly describe the three displayed 3-DSBF/3-RSBF NL242 examples as degree seven; Section4 gives the two additional permutation-class tables. Their lack of a Walsh zero is explicitly discussed. Sections2–3 define the orbit-matrix reduction and report104/176 orbit dimensions and a steepest-descent-like search. Our bounded tabu-neighbour implementation is inspired by that strategy; it is not claimed to reproduce their unpublished algorithm details.
- Lou–Xu–Wang, [arXiv:2610.17897v1](https://arxiv.org/html/2610.17897v1#Thmproposition1), Proposition1 and its proof, use support sums and moment expansion to obtain the stronger normal form `W_g(a,c)=4c+8Q(a) mod16` for an eight-variable balanced hypothetical NL118 function with normalized nonzero support sum. The support-sum control of the mod-eight Walsh type is therefore already present in that proof. Its theorem about balanced eight-variable functions is not assumed here. The read excerpt is staged in `sources/lxw-proposition1-excerpt.txt`.
- Wang–Lou–Wang, [arXiv:2610.17871v1](https://arxiv.org/abs/2610.17871), Lemma2, gives the general integer Walsh expansion and low-bit degree bounds; Proposition1 uses `W/4 mod2` affine in its nine-variable argument. The present mod-eight classification is an immediate elementary specialization, not a priority claim.

## Exact symmetry formulation and scope

The 3-RSBF action rotates the nine input coordinates by three positions, yielding176 orbits. Adding reversal of all nine coordinates yields the 3-DSBF action and104 orbits. Orbit assignments are independent Boolean variables. For orbit `O_j`, set `C[a,j]=sum_(x in O_j)(-1)^(a.x)`. Then

`W_f(a)=sum_j C[a,j](1-2f(O_j))`.

The Walsh transform is constant on the same frequency orbits, because coordinate permutations preserve the character pairing and the input function is invariant. All512 frequency rows are independently checked against this identity. Support XOR is exactly the XOR of the precomputed orbit-XOR vectors whose orbit bit is one.

The exact104-variable problem asks `|W_f(a)|<=28` and `s!=0`, without a balance or even-weight assumption. Output complementation preserves peak and `s`, so `f(0)=0` is harmless. The circuit contains a full512-point, eleven-bit FWHT (all intermediate integers lie between-512 and512), signed range constraints at all104 frequency representatives, and the explicit support-XOR disjunction. The independent checker verifies every gate truth table, every full-adder bit identity, every comparator on all2048 possible words, all wiring layers, and all support-XOR expressions as binary linear forms. A genuine published target-bound table fails only the nonzero-XOR condition; a genuinely modified bound32/nonzero-XOR table satisfies every clause of the relaxed circuit.

A partial LRAT trace, solver timeout, proof cap, or bounded heuristic non-find is not an exclusion. No new negative theorem about either rich symmetry class is claimed without a complete independently checked certificate.
