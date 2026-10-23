# What can be audited without network or unstaged sources

The supplied `selection-inputs/literature/achlioptas-peres.reader.md` reports
10.23 and 21.33 in both its introduction and Table 10. Its references identify
Dubois–Boufkhad (1997), *A general upper bound for the satisfiability threshold
of random r-SAT formulae*, and Kirousis–Kranakis–Krizanc–Stamatiou (1998),
*Approximating the unsatisfiability threshold of random formulas*.
The frozen contract records the latter's equation

    (1-2^-k)^a [2-exp(-ka/(2^k-1))] = 1.                       (1)

Neither original primary text nor Achlioptas–Menchaca-Mendez (2012) nor
Lelarge–Oulamara (2018) was staged in this directory. The supplied reader's
introduction writes 2^k n^k possible clauses and hence is not, literally,
an unambiguous statement of the distinct-variable model. We do not silently
resolve that discrepancy as a citation fact. Instead we derive (1) for the
requested model below. The written proof in PROOF.md supplies all
model transfers. There is no current literature search and no novelty claim.

## Independent derivation of the classical criterion

Fix n>=k, M clauses in the contract's distinct-variable model, and a Boolean
assignment sigma. Conditional on each clause being satisfied by sigma,
the clauses remain independent. A clause is supported by variable v if
sigma satisfies exactly one of its literals and that literal is at v.
The probability of this category, conditional on satisfaction, is

    p = (k/(n 2^k))/(1-2^-k) = k/[n(2^k-1)].                 (2)

Support categories for different variables are disjoint. Suppose sigma has
z coordinates with value zero. If sigma is a satisfying assignment of maximum
Hamming weight, every such coordinate has at least one supporting clause:
otherwise changing that zero to one preserves satisfaction. Thus every
satisfiable formula has at least one such one-flip maximal assignment.

For fixed sigma, its conditional support counts have the multinomial
distribution from M independent trials. Poissonize the number of those
trials to N~Poisson(M). Then the support counts at all variables are
independent Poisson(Mp). The conditional probability that all z required
categories are nonempty is at most

    (1-exp(-Mp))^z / P(N=M).                                (3)

This is the elementary inequality P(A|N=M)<=P(A)/P(N=M), without any
negative-association assumption. Since each fixed assignment satisfies all
clauses with probability (1-2^-k)^M, summing (3) over all assignments gives

    E[number of one-flip maximal satisfying assignments]
      <= (1-2^-k)^M [2-exp(-kM/(n(2^k-1)))]^n / P(N=M).     (4)

For positive integer M, the standard elementary Stirling bound
M! <= exp(1/(12M)) sqrt(2 pi M) (M/e)^M gives
P(Poisson(M)=M) >= exp(-1/(12M))/sqrt(2 pi M). The inverse factor in (4)
is therefore only O(sqrt(M)). Equivalently, its nth root tends to 1 for
M=floor(alpha n). If

    g_k(alpha) = alpha log(1-2^-k)
                 + log(2-exp(-k alpha/(2^k-1))) < 0,         (5)

(4) decays exponentially and Markov's inequality proves UNSAT with high
probability. This derives the criterion on exactly the requested model.

The equation g_k(a)=0 has precisely one positive root. Indeed g_k(0)=0,
g'_k(0)=log(1-2^-k)+k/(2^k-1)>0 for k>=2, g''_k(a)<0 for a>=0,
and g_k(a) tends to minus infinity. The sign at zero follows, for
x=2^-k, from -log(1-x)<=x/(1-x)<kx/(1-x).

`python3 code/baseline.py` brackets that root with exact exponential and
logarithm series enclosures. This recovers the meaning of the tabulated
two-decimal bounds, without treating them as exact optimal constants.
It does not establish that no later work improved them.
