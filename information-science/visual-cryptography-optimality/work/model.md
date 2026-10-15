# Exact model and certification derivation

Date: 2026-10-14 (PT). Evidence label: Certification; two independent Codex reviews completed, with scope/precision corrections recorded in evidence/referee-resolution.md. Novelty is not claimed.

## Scope

The book asks to minimize pixel expansion, maximize contrast, maximize contrast at minimum expansion, and minimize expansion at maximum contrast for general black-and-white visual cryptography. Its cited primary source is Ateniese, Blundo, De Santis, Stinson (1996), Definitions 2.1 and 2.2. These are different models.

We enumerate every nonconstant **strong** monotone access structure on n participants: a nonempty antichain A of nonempty minimal qualified sets; Q is its upward closure; F is the complement in 2^[n]. Dummy participants and singleton-qualified sets are included. All qualified sets, not only A, must reconstruct by stacking all their shares. Weak structures with unclassified sets, XOR reconstruction, reversing, meaningful cover shares, random grids, and expected-only contrast are not the enumeration's model.

For a binary n-by-m matrix M, W_Q(M) counts columns with at least one black entry in rows Q. A deterministic VCS still randomly selects an encoding matrix; “deterministic” means an almost-sure separation, not an absence of encoding randomness. In the collection model, there are nonempty finite multisets C0,C1 with a common expansion m, uniform sampling, identical distributions of the entire F-row restriction for every F in F, and an integer gap

    g = min_{Q in Q} [min_{M in C1} W_Q(M) - max_{M in C0} W_Q(M)] >= 1.

We optimize alpha=g/m. Ateniese et al. call alpha the “relative difference” and g the “contrast”; later papers commonly call alpha “contrast.” Maximizing unnormalized g without bounding m is unbounded by repetition, so the book's maximum-contrast objective is interpreted as alpha. No Michelson or background-normalized alternative is substituted.

The basis-matrix subclass chooses all column permutations of fixed B0,B1. In this class the two F-row column multisets must coincide; each qualified weight is fixed. The four finite-expansion optima below are initially certified only in this subclass. They must not be silently promoted to the collection model.

## Column-count LP and ILPs

Index a column by T subset [n], its set of black rows. Let x_T,y_T be the numbers of copies in B0,B1. Both sums are m. For S subset [n] define

    f(S) = sum_{T intersect S = empty} (x_T-y_T).

Then f(empty)=0 and W_Q(B1)-W_Q(B0)=f(Q). Security is exactly f(F)=0 for all F in F. To see sufficiency, the difference of counts of any prescribed pattern on F (zero rows Z and one rows U, Z disjoint U, Z union U=F) equals

    sum_{V subset U} (-1)^|V| f(Z union V),

which vanishes because F is downward closed. Necessity follows by inspecting the all-zero projected pattern. Thus only column multiplicities matter for a fixed basis pair.

The integer programs have x,y nonnegative integers:

1. Minimum m: minimize sum x subject to sum x=sum y, f(F)=0, f(Q)>=1.
2. Maximum g at that m: maximize integer g subject to the same equalities, sums=m, and f(Q)>=g.
3. Maximum alpha: allow rational x,y, set both sums=1, maximize a with a>=0 and f(Q)>=a. This is a bounded rational LP (the code already imposed nonnegativity on every variable).
4. Minimum m at alpha*=p/q reduced: minimize sum x subject to equal sums, f(F)=0, q f(Q)>=p sum x, and sum x>=1.

The rational LP optimum is attained. Its feasible region is compact: both count vectors lie in simplices and 0<=a<=1. Positive feasibility follows by setting f(F)=0, f(Q)=1, applying the integer inverse below, and normalizing the positive/negative count vectors. Clearing denominators gives integer basis matrices attaining the same alpha, so its value is the exact maximum over all finite basis schemes, not merely a supremum. Every LP primal and dual is checked using Fraction arithmetic; floating-point discovery is not itself a certificate.

## Maximum relative contrast is unchanged by allowing collections

Take any finite collection scheme, and replicate matrices so both collections have the same size r. Concatenate all r matrices in C0, and separately all r matrices in C1. Equality of forbidden projected-matrix distributions implies equality of aggregated projected-column counts, hence these concatenations form a basis pair. For every qualified Q, the black concatenation weight minus the white one is at least r*g. Its expansion is r*m, so its relative contrast is at least g/m. Conversely every basis pair defines a collection scheme. Therefore the global maximum relative contrast is identical in the two models. This argument does **not** preserve minimum expansion, or expansion at the contrast optimum.

Consequently, every collection scheme satisfies m >= ceil(1/alpha*), and its integer gap at expansion m is at most floor(alpha* m). When an integer basis witness matches either bound, that particular optimum transfers to collections. If alpha*=p/q, any finite scheme attaining it has q dividing m; equality of the realized worst-case integer gap g/m supplies this divisibility.

## Independent integer formulation

Let d_T=x_T-y_T. The complement-zeta transform above has the exact inverse

    d_T = sum_{S superset ([n] minus T)} (-1)^{|S|-|[n] minus T|} f(S).

All f(S) are integers, f(F)=0, and f(Q)>=g. Since f(empty)=0, sum d=0, so the minimum length realizing d is

    m(d) = sum_T max(d_T,0) = (1/2) sum_T |d_T|.

Conversely x=max(d,0), y=max(-d,0) realize d. Common columns can be added to reach any larger common expansion without changing f. A second exact integer solver uses only integer f(Q), the inversion formula, and a sum-of-positive-parts length bound. It never imports the generator's constraint matrix. It checks infeasibility below each claimed m, above each claimed fixed-m gap, and below each claimed expansion attaining alpha*. Rational LP bounds and denominator divisibility may discharge such obligations without a solver.

For any m(d)<=M, every f(S) is a sum over a subset of the signed d_T, so -M<=f(S)<=M. Thus the integer search is finite without an arbitrary numerical cutoff. The code uses the exact piecewise-linear expression sum If(d_T>0,d_T,0); equivalently one may introduce z_T>=d_T, z_T>=0, sum z_T<=M. For the optimum-alpha obstruction, the actual expansion m is an integer with 1<=m<the claimed optimum length, m(d)<=m, and q f(Q)>=p*m. It is **not** legitimate to use the shorter core length on the right and then report the padded length as retaining the same contrast. All three required infeasibility obligations are either discharged by a proved rational/integer bound or retained as exact SMT queries.

## General trade-off consequences

For a fixed access structure, define separate functions G_basis(m) and G_collection(m), each the largest integer gap at expansion m in its specified class, setting it to zero if no positive-gap scheme exists (identical matrices always give zero). They are not asserted equal at each m. For either function G, padding proves G(m+1)>=G(m). Basis concatenation proves superadditivity. For collections, use **Cartesian-product multisets** C_i={A||B : A in C_i^(1), B in C_i^(2)}, with product multiplicities and the same access structure in both components. Forbidden distributions factor, and the guaranteed gaps add, giving G(m1+m2)>=G(m1)+G(m2). Arbitrarily pairing matrices, or combining different access structures without extra proof, is not this argument. The common global LP bound gives G(m)<=floor(alpha* m). If an optimum-alpha basis witness has expansion L and gap h, repetition and padding give, for either function,

    h floor(m/L) <= G(m) <= floor(h m/L).

In particular G(kL)=kh, and G(m)/m tends to alpha*. These elementary statements do not claim a closed formula at the remaining residue classes, nor novelty. The tables test whether minimum expansion also attains alpha*; one contrary structure refutes that universal assertion, but is not automatically a counterexample to any published conjecture.

## Universal collection lower bound used after the basis sweep

For every individual black encoding matrix M, every qualified Q and every forbidden F subset Q,

    W_Q(M) - W_F(M) >= g.

Proof: security guarantees that some white encoding N has exactly the same full F-row restriction as M (both collections have positive probability at this restriction). Hence W_F(N)=W_F(M). Worst-case contrast gives W_Q(M)>=W_Q(N)+g, and stacking monotonicity gives W_Q(N)>=W_F(N). This is a necessary condition on **each black matrix**, not a basis-matrix assumption.

Writing b_T for its column multiplicities yields b_T>=0 integer, sum b_T=m, and sum_{T intersects Q, T disjoint F} b_T>=g. Infeasibility at length <=m0-1 excludes all collection schemes of that length. Feasibility is only a witness to this relaxation, never an actual VCS. The argument is the unavoidable-pattern principle of Ateniese et al.; no novelty is claimed.

`collection_bounds.py` checks the nine instances for which the global LP bound alone does not certify minimum expansion. Four become UNSAT in this necessary model: the (2,4) structure and three five-participant structures containing that obstruction. The other five remain unresolved as collections. These outcomes are in `evidence/collection-bounds.json`; all query files are retained.

Once a collection minimum lower bound L is known and alpha*=p/q is reduced, expansion at maximum contrast is at least q*ceil(L/q). **Equality is concluded only if an independently checked witness has exactly that expansion and contrast alpha*.** The reporter explicitly compares this lower bound with the witness's actual length, rather than merely observing some optimum-alpha witness. This proves the four-objective transfer for every n<=4 structure and 203 of the 208 n5 structures. The other five are reported as intervals, not basis optima promoted to collection optima. Divisibility is asserted only at the global contrast optimum, not for arbitrary padded schemes.

## Scope and prior-art checks after computation

The 248 basis rows (n=1..5 counts 1,3,8,28,208) have 248 checked rational LP primal/dual pairs, 744 direct integer witnesses, 726 elementary exact LP/integrality/divisibility objective bounds and 18 UNSAT obligations from the independently derived Mobius formulation. All fixed-minimum-expansion gaps are one in this finite table; that is **not** a theorem for arbitrary n. There are 24 finite trade-off rows (one at n4, 23 at n5).

The global maximum-contrast collection-to-basis argument already appears for thresholds in Blundo–De Santis–Stinson (1999), Section6, and in Blundo et al. (2003), Lemma3.5. Our use for general access structures has the same elementary proof. Neither this observation nor an LP/ILP reformulation nor a finite enumeration resolves the original all-structures scientific question. In particular, Blundo et al. (1999), Theorem4.7 gives a concrete design-existence obstacle: when n=3 mod4, a (2,n) scheme at optimal contrast has expansion n iff a real Hadamard matrix of order n+1 exists.

The quantitative original goal remains unclosed for arbitrary strong access structures and, a fortiori, for all admissible weak structures. We do not impose a polynomial-time requirement absent from the book. Nor do we replace the requested structural optimization/trade-off result by mere decidability or by an optimization restatement.
