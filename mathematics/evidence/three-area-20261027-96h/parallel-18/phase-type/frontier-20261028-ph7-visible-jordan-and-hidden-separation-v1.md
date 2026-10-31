# PH7: hidden poles cannot coincide with the visible poles, and both visible Jordan blocks are defective

**WRITTEN CANDIDATE, not independently reviewed; no 8/9 existence/exclusion.** MathResearch96h-2. This is an additive all-topology deduction from the exact global-irreducibility candidate `frontier-20261028-ph7-global-irreducibility-v1.md` SHA256 `729926c5fa9779ec4b1ca27156f80c4ca80c49c973ca4c7cbf352da614a94b49`. It is not a new PH6 result and no novelty is claimed.

## Claim

For an actual PH representation of H with at most seven states and `z=b^2/(a-c)^2>1/2`, normalize `G=(T+cI)/(a-c)` and let `lambda=-1+i sqrt(z)`. Then:

1. The matrix has exactly seven states and is irreducible; its spectral bound0 is simple.
2. There is a real monic quadratic Q with `det(yI-G)=y[(y+1)^2+z]^2 Q(y)` and Q is Hurwitz. It has no root at0, lambda or its conjugate.
3. Each visible complex eigenvalue has algebraic multiplicity EXACTLY2, geometric multiplicity EXACTLY1, and a unique Jordan block of length2.
4. For the SAME PH input/output vectors, the visible right eigenvector is observed by the input and the visible left eigenvector by the exit. Their bilinear pairing is zero, as required by the defective Jordan block. These are complex, nonzero coupling assertions, not sign assertions.

The target does not force Q to have real roots or distinct roots. None of the above decides whether such an irreducible PH7 generator exists at8/9.

## 1. Excluding hidden coincidences by a strict all-variable trace inequality

The named global-irreducibility theorem yields a reachable irreducible seven-state G with Perron root0, and0 is algebraically simple. The actual target transfer has coprime degree-five denominator, so its visible pole factors divide the characteristic polynomial. The two remaining degrees define Q. Strict Perron spectral dominance gives Re(all Q roots)<0 and hence Q(0)!=0.

Because Q has real coefficients, if Q(lambda)=0 then necessarily

    Q(y)=(y-lambda)(y-conjugate(lambda))=(y+1)^2+z.

In that case G has spectrum `0` and `-1 +/- i sqrt(z)` each with algebraic multiplicity THREE. Therefore

    tr G = -6,       tr G^2 = 6(1-z).

For every real seven-by-seven Metzler matrix, `tr G^2 >= (tr G)^2/7`: the off-diagonal pair contributions `G_ij G_ji` are nonnegative and the diagonal squares obey Cauchy. It follows that

    6(1-z) >= 36/7, hence z<=1/7.

This contradicts z>1/2. Thus Q(lambda)!=0 and Q(conjugate(lambda))!=0. This argument excludes the entire coincidence scenario, including semisimple/defective decompositions and arbitrary diagonal entries, without dividing by an assumed hidden-root difference.

## 2. Exact Jordan structure and actual couplings

The visible complex factors in the characteristic polynomial therefore occur exactly twice. A scalar transfer with a double pole at lambda requires the matrix resolvent to have a double pole there, so at least one Jordan block has length >=2. Algebraic multiplicity2 forces precisely one length2 block, geometric multiplicity1; the conjugate block follows over the reals.

For the same actual PH pair, let `beta=alpha`, `gamma=omega/(a-c)`, and set `y=(s+c)/(a-c)`. The transfer is `k/D_z(y)` for positive k, where `D_z=y[(y+1)^2+z]^2`. From the actual resolvent determinant identity, identically as polynomials,

    beta adj(yI-G) gamma = k Q(y).

At lambda this scalar is nonzero by §1. Since the pencil has rank6 and adjugate rank1, the adjugate is `K0 v w^T` for some nonzero complex K0 and right/left eigenvectors v,w. Thus `(beta v)(w^T gamma)!=0`; both factors are separately nonzero. A generalized vector g satisfies `(G-lambda I)g=v`, while `w^T(G-lambda I)=0`, so `w^T v=0`. No transpose conjugation is intended in these purely algebraic formulas.

The target's second-order pole, not merely algebraic root multiplicity, is essential in the Jordan conclusion. An algebraic multiplicity-two eigenvalue can otherwise be semisimple and give only a simple resolvent pole; that case is excluded here.

## 3. Boundaries

Ordinary imports: the separately frozen irreducibility proof; characteristic/divisibility and adjugate identities; real conjugate-root pairing; Cauchy; Jordan resolvent facts. The trace inequality was derived here exactly, with no numerical or machine check required. This is prospective written reasoning, not a kernel/formal/cross-model verification or review. The prior v121 framework deliberately allowed potential coincidences in its general coefficient formulas; the narrower z>1/2 argument here does not retroactively rewrite that source or assert its broader formulas wrong.

The conclusion rules out neither an irreducible PH7 witness nor an irreducible spectrum with a defective pair. No upper endpoint, graph exclusion beyond the named dependency, novelty, actual 8/9 answer, or stronger-family adoption is claimed. Historic holds and findings remain unchanged and are not used as premises.

END — exact hidden-root separation and observable length-two Jordan chains are necessary for PH7 above1/2.
