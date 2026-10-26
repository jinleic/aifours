# Addendum 3 — the seven-point translated-mask control cannot be an actual tiling

Owner MathShor / MathShor-2. Actual preceding `/bin/date`: `Sun Oct 25 14:47:44 PDT 2026`. WRITTEN CANDIDATE, unreviewed. No scientific computation. The original problem remains NOT_PROVED.

The checkpoint11 control E=(z^h-1)Q had exact7/7 signed support and arbitrarily large root orders. It was explicitly NOT a common-complement witness. This addendum proves it can NEVER be an actual Shor common-complement trade, even for arbitrary h and n. Larger/nonuniform seven-point trades remain live.

## 1. The fixed mask has NO root of unity

Let

    Q(z)=z+z^7+z^13+z^14-z^2-z^4-z^6.

**Lemma.** Q(zeta)!=0 for every root of unity zeta.

Proof. Let d be its order. Group the seven terms by exponent modulo a prime ell|d, using the same cyclotomic-field degree fact as addenda1/2: if ell^2|d every class coefficient must vanish; if ell divides d once and an empty class remains, all class coefficients must vanish.

- ell=7: occupied classes0,1,2,4,6 include singletons and leave empty classes.
- ell=11 or13: again multiple empty and singleton classes.
- ell>=17: all seven known exponents are distinct and there are empty classes.

Therefore d has only prime factors2,3,5.

If9|d, class0 modulo3 consists only of -zeta^6, impossible. If25|d, class3 modulo5 consists only of zeta^13, impossible. If4|d, parity independence forces the odd group zeta+zeta^7+zeta^13=0, so1+zeta^6+zeta^12=0 and d|18, contrary to4|d.

Thus d divides30. Its possibilities are1,2,3,5,6,10,15,30. At the first six:

    Q(1)=1,
    Q(-1)=-5,
    Q(zeta_3)=2zeta_3-1,
    Q(zeta_5)=zeta_5^3,
    Q(zeta_6)=4zeta_6-1,
    Q(zeta_10)=2zeta_10-2zeta_10^2+zeta_10^3.

All are nonzero; for d10 use the basis1,zeta,zeta^2,zeta^3.

For d15 and30, the already-written exact conjugate-norm identity CN in addendum1 gives sums86 for Q at the eight primitive15th roots, and34 for Q(-z) at those roots. These are strictly positive. If Q vanished at ONE primitive root, its integer coefficients and cyclotomic irreducibility would make it vanish at ALL conjugates, giving sum0. Thus neither conductor works. Q has no root of unity. QED.

The numerical integers86 and34 here are the displayed symbolic coefficient-square expansions15*7-3*5-5+1 and15*7-3*17-5*9+25, not interpreter outputs.

## 2. No translated-mask seven-point trade

Suppose actual complements B,D2 of A satisfy the Shor seed conditions and

    1_D2-1_B=(z^h-1)Q in Z[Z_n],

with the exact distinct support

    D2 minus B={2,4,6,h+1,h+7,h+13,h+14},
    B minus D2={1,7,13,14,h+2,h+4,h+6}.

This includes arbitrary residues h; if supports coincide/cancel, it is not this exact7-trade case.

Since A*(D2-B)=0, Fourier evaluation gives

    A(zeta)(zeta^h-1)Q(zeta)=0

at EVERY nth root. The lemma makes Q(zeta) nonzero, so A(zeta)(zeta^h-1)=0. Fourier inversion proves A+h=A exactly.

But3 is in A, so3+h is in A. Also1 and h+4 are two DISTINCT B values by the exact support condition. Therefore

    (3+h)+1=0+(h+4) in Z_n

is a collision of distinct A/B preimage pairs, contrary to directness. This proves the uniform exclusion.

It explains exactly why the checkpoint11 annihilator/cardinality/seed control fails: its common convolution need not equal1, and if it did, the Fourier-induced period would give the displayed actual contradiction.

## 3. Common-tile periodic descent preserves ALL three mates

If A has a nontrivial period subgroup H in ANY genuine common-complement witness, reduction is injective on EACH of B,D2,D3 (the same uniqueness proof applies separately to their factorizations with A). Projecting and counting gives

    Abar+Bbar= Abar+D2bar= Abar+D3bar = Z_(n/|H|) directly.

The endpoint seed-bootstrap first forces quotient modulus>=1320, so all literal exponents0..14 remain distinct. Hence the THREE-complement gate itself descends, not only endpoint FACT. A least-order common-complement witness must therefore have A aperiodic.

This does NOT assert descent through a period of B or either other mate: other mates can project as multisets, so a further division/section argument would be required. It does NOT quotient raw words or STAB.

## 4. Exact remaining gap

A putative first surviving trade of size7 can match the seven fixed terms with DIFFERENT unknown shifts. Nothing above forces those shifts to coincide, or to be individual periods of A. Such nonuniform trades of an aperiodic common tile remain unexcluded, along with all larger trade sizes.

The full positivity/direct-tiling constraints and simultaneous D3 equation must be used; annihilator algebra alone is insufficient. No common-complement witness, finite PR-saturated raw prefix, or finite complete extension is delivered here. All new statements are WRITTEN and require their own independent reconstruction.
