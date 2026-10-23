# An exact restriction on a possible balanced 242 witness

This is a self-contained restriction, not a resolution of the frozen
existence question. No novelty is asserted. No claimed 2026 covering-radius
upper bound is used.

**Proposition.** Every balanced Boolean function on nine variables with
algebraic degree at most seven has nonlinearity at most 240. The bound is
attained by

    f(x) = x_0 + x_1 x_2 + x_3 x_4 + x_5 x_6 + x_7 x_8  (over F_2).

Consequently any balanced nine-variable function with nonlinearity at
least 242 must have algebraic degree exactly eight, and the bitwise XOR
of all input indices in its support must be nonzero.

## Proof of the upper bound

Let T be the support of f, w=|T|=256, m_i=sum_{x in T} x_i, and
m_ij=sum_{x in T} x_i x_j. All sums in the next identities are ordinary
integers. For a in F_2^9, expansion of the parity character gives

    W_f(a) = 512 [a=0] - 2w
             + 4 sum_i m_i a_i - 8 sum_{i<j} m_ij a_i a_j
             + terms divisible by 16.

Suppose first that every m_i is even. Since w=256 is divisible by four,
all W_f(a) are divisible by eight. Reduction modulo two after division
by eight shows that the function

    q(a) = W_f(a)/8 mod 2
         = -w/4 + sum_i (m_i/2) a_i - sum_{i<j} m_ij a_i a_j mod 2

has degree at most two. The term 64[a=0] vanishes modulo two. Balance
implies q(0)=0, so q is not the constant one polynomial.

A nonzero squarefree polynomial of degree at most d in m variables has
weight at least 2^(m-d). For completeness, write it as p_0(x)+t p_1(x)
and induct on m. If p_1 is nonzero, each input with p_1(x)=1 contributes
exactly one one in the pair t=0,1, giving at least
2^((m-1)-(d-1)) ones. If p_1=0 the weight is twice the weight of p_0;
the constant case starts the induction. Applying this to 1+q gives at
least 128 inputs with q(a)=0.

If max |W_f| were at most 28, divisibility by eight would make it at
most 24. At q(a)=0 it would be at most 16, since those coefficients are
divisible by 16. Thus

    sum_a W_f(a)^2 <= 128*16^2 + 384*24^2
                      = 253952 < 262144 = 512^2,

contradicting character orthogonality (Parseval). Hence max |W_f|>=32
and nonlinearity <=256-32/2=240 whenever all m_i are even.

For a polynomial f of degree at most seven, the product f(x) x_i has
degree at most eight after squarefree reduction. Every monomial of
degree less than nine sums to zero over F_2^9, modulo two. Thus every
m_i=sum_x f(x)x_i is even, proving the proposition's upper bound.

More precisely, the coefficient of the full degree-nine monomial is
sum_x f(x)=0 mod 2 for any balanced f, so its degree is at most eight.
The parity m_i is then the coefficient of the degree-eight monomial
missing x_i: the coefficient of the full monomial in f(x)x_i receives
contributions only from that monomial and the full degree-nine monomial.
Therefore, among balanced functions, all m_i even is equivalent to
degree at most seven. Their parities are also the coordinates of
XOR_{x in T} x. Any balanced function with nonlinearity >=242 must
therefore have nonzero support XOR and degree eight.

## Attainment

The displayed quadratic is balanced because toggling x_0 toggles its
value. Its Walsh transform factors into the transform of x_0 and four
transforms of uv. The first factor is 0 or 2; each of the four remaining
factors is +2 or -2. Its spectrum is consequently 256 zeros and 256
coefficients of magnitude 32. Its nonlinearity is 240 and degree is two.
An explicit indexed table and complete spectrum are recorded in
results/baseline240.json. The FWHT producer and separate direct-sum
checker verify this witness; the proof above, not the witness check,
establishes the upper bound for the whole restricted class.

## Elementary global bound, without the 2026 covering-radius claim

For every balanced nine-variable f, the same integer expansion gives

    W_f(a)/4 mod 2 = sum_i (m_i mod 2) a_i.

The right side is linear. If it is zero, the preceding argument already
forces max|W_f|>=32. If it is nonzero, it is one at exactly 256 indices.
Suppose max|W_f|<=24. At these 256 indices the coefficient is 4 mod 8
and has magnitude at most 20; at the other 256 it is 0 mod 8 and has
magnitude at most 24. Then Parseval would give

    sum_a W_f(a)^2 <= 256*(20^2+24^2)
                      = 249856 < 262144,

again impossible. Every Walsh coefficient of a balanced function is
divisible by four, so max|W_f|>=28 and its nonlinearity is at most 242.
Together with the displayed balanced quadratic attainer, this proves
the elementary interval [240,242] for the global balanced maximum.
It does not determine which endpoint is attained. This bound is
independent of the unrestricted covering-radius preprint and carries
no novelty claim.
