# Explicit seed and small-neighborhood scope

The seed names in current claims mean exactly the three hex truth tables
in `code/seeds.py`. Decode left to right, most significant bit first in
each nibble, to obtain f(0),...,f(511); input coordinate i is bit i of the
integer index. Their correspondence to the three Section 3.1 tables is
checked against the delivered staged manuscript. This is provenance of
the supplied text, not a fresh online bibliographic certification.

Their full directly computed Walsh spectra and autocorrelations are in
`results/seed-invariants.json`. The absolute indicators are 40,32,56.
For h(x)=g(Ax+b)+ell(x)+c with invertible A,
AC_h(t)=(-1)^ell(t) AC_g(At). Thus the absolute indicator is invariant,
and these three explicit seeds are pairwise not extended-affine
equivalent. A shared absolute Walsh histogram alone would not establish
equivalence.

Adding a linear output a.x permutes Walsh coefficients, and balances h
exactly when W_h(a)=0. All local claims therefore allow every linear
output shift by looking for a zero anywhere in the entire spectrum.
Constants also cause no issue: complementation negates all coefficients.
Each seed has even weight and no Walsh zero. Odd numbers of flips give
odd weight, which no affine output addition can turn into weight 256.

For flip set S, write c_x(a)=(-1)^(g(x)+a.x). Exactly

    W_(g+1_S)(a) = W_g(a) - 2 sum_(x in S) c_x(a).

All seed magnitudes belong to {4,12,20,28}. With two flips, the bound 28
fails exactly when some initially magnitude-28 coefficient has both
selected signs opposing its old sign. A new zero requires an initially
magnitude-4 coefficient whose selected signs both align with its sign.
The independent checker computes all 512 coefficients for every pair.

With four flips, only an initially magnitude-28 coefficient can exceed
28; it does so exactly when at least three selected signs oppose its
old sign. Therefore every triple of a legal four-set must have empty
common opposing mask. Conversely that condition suffices. Both programs
exhaust all C(512,3)=22238720 triples and reconstruct every possible
four-set; the independent checker then computes fresh direct sums on all
45 surviving sets. None has a zero. Its distance-two count is computed
from all pair spectra, rather than hard-coded.

Original forced balancing distances are |W_g(0)|/2 = 6,6,14. The minimum
over all linear shifts is min_a |W_g(a)|/2 = 2 for every seed. Thus small
original-origin balls alone could be vacuous, whereas the claimed
all-linear-shifts balls are non-vacuous. These finite exclusions say
nothing about arbitrary degree-eight functions outside their scope.
