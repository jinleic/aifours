# A Parseval screen for an odd-weight fixed half-table

This is a necessary-condition lemma and a restricted-class result.
It does not answer the global balanced nine-variable question. No
novelty is asserted.

Let V be an eight-dimensional input hyperplane and s any vector outside
it. Write a Boolean function as g(y) on V and h(y) on s+V, and use Walsh
spectra G,H in the same eight-dimensional coordinates. Its complete
nine-variable spectrum consists, up to harmless character signs and
index choices, of G(b)+H(b) and G(b)-H(b).

Fix g of odd weight. Suppose the full table has a Walsh zero and every
Walsh magnitude at most 28, so a linear output addition can make it a
balanced target. A function with a Walsh zero has even weight. Thus h
also has odd weight and all its eight-variable coefficients are 2 mod
4; in particular |H(b)|>=2. Since

    max(|G+H|,|G-H|) = |G|+|H|,

we have |G(b)|<=26 and |H(b)|<=28-|G(b)| at every b. Parseval on h gives

    65536 = sum H(b)^2
          <= sum (28-|G(b)|)^2
           = 256*784 - 56*sum|G(b)| + sum G(b)^2
           = 266240 - 56*||G||_1.

A Walsh zero means H(b0)=G(b0) or -G(b0). Put m=|G(b0)|. Then m<=14,
and at this index replace the capacity (28-m)^2 by the actual value
m^2. Its excess was 784-56m, so

    65536 <= 266240 - 56*||G||_1 - (784-56m),

which simplifies exactly to

    ||G||_1 <= 3570+m.

Therefore a necessary condition is

    max |G| <= 26,
    ||G||_1 <= 3570 + max{|G(b)|: |G(b)|<=14}.

The maximum over small coefficients exists: if every |G| exceeded 14,
all would be at least 18, contradicting sum G^2=65536. A failed screen
excludes every completion h and every linear output shift, not a sample
of the 2^256 possible completions. Passing the screen proves nothing
about existence of a completion.

## Explicit finite family screened

The data file lists full indexed balanced NL240 source tables and all
normals v for which the restriction to v.x=0 has odd weight. For each
source f, its support XOR is s. Odd restriction weight is equivalent to
v.s=1, because the full weight is even. Every nonzero s gives exactly
256 such normals.

For each listed (f,v), the class allows arbitrary changes at all 256
points v.x=1, fixes all points v.x=0 to f, and then allows any linear
output addition. A source f itself is a balanced NL240 attainer in each
of its classes. Thus a failed screen proves exact balanced maximum 240
in that class; passing classes remain unresolved.

The producer obtains the slice spectrum using
(W_f(a)+W_f(a+v))/2, one representative of every pair {a,a+v}.
The independent checker instead chooses an explicit basis of ker(v),
constructs all 256 slice values directly, and uses direct character
sums. It also directly checks the complete source tables and their
balanced nonlinearity. Every listed class is rechecked, without
sampling. Overlapping classes are not counted as distinct functions.

In this particular corpus all 31492 rejected cases have max|G|=30;
all 252 surviving cases have max|G|=26. The l1 condition adds no
exclusions in the corpus. Thus the class counts need only the simpler
odd-coefficient lower bound |H|>=2 and the displayed sum/difference
identity. The Parseval inequality remains a further necessary condition.
