# Full-distribution collection-gap continuation

Date: 2026-10-14 (PT). Scope: the five previously unresolved strong-access collection rows on five participants, not the arbitrary-access book problem. Evidence label: exact finite certification; the standard-library replay passed all six obligations in20.86s. A focused other-vendor mathematical review found no fatal defect; its clarification requests are resolved in `evidence/continuation-20261014/review-resolution.json`. No priority claim or Lean/kernel certification.

## Contract fixed for this continuation

The original definition in `model.md` is unchanged. For every qualified set Q, including every qualified superset, every positive-probability black encoding B and white encoding W must satisfy `W_Q(B) >= W_Q(W)+1`. For every forbidden F the **whole ordered F-row matrix distribution** must be identical. We permit arbitrary positive rational probabilities (equivalently finite uniform multisets); the impossibility arguments below even allow arbitrary real probabilities on the finite matrix space.

The six bounded obligations are the five reciprocal-optimum lengths 5,6,5,6,6, and length7 for the final structure. Existing basis upper witnesses remain frozen. The continuation must not reseal their original acceptance package. The objective is an exact lower bound at each missing length, plus a full-distribution proof rather than a black-matrix relaxation. CPU is one process, numerical-library threads one; no sweep beyond these six obligations. Enumeration is bounded by the 12,620,256 sorted 7-column lists over 32 masks, with earlier exact filters. Exploratory assays are retained as such; the decisive verifier is run after the certificate and proof stabilize. This is not an AI-advantage benchmark.

| Minimal qualified masks (participant i is bit i-1) | Excluded lengths | Existing basis upper length |
|---|---|---:|
|3,5,6,9,10,28|5|6|
|3,5,9,22,26,28|6|7|
|3,5,10,12,22,25|5|6|
|3,5,10,22,25,28|6|7|
|7,11,13,19,21,25|6,7|8|

**Padding lemma, both models.** Append the same fixed column to every matrix of both colors. Forbidden ordered-matrix distributions remain equal, and every Q-weight receives the same deterministic increment, so every guaranteed gap is unchanged. Thus G is nondecreasing and existence at m implies existence at m+1. In particular excluding the upper-witness length minus1 excludes all smaller lengths; the reciprocal-alpha lower bound supplies an additional independent shortcut.

## 1. Exact column-permutation orbit reduction

Write each n-by-m binary matrix as an ordered list of m n-bit columns. Apply an independent uniform permutation of all m column positions to every encoding, for either secret. This preserves every stacking weight and preserves equality of each forbidden ordered-matrix distribution. Hence existence implies existence of a scheme invariant under column permutations.

An orbit is represented uniquely by its nondecreasing column list `c`. For a forbidden F define `sigma_F(c)=sort(t & F for t in c)`. Under a uniform global column permutation, the ordered projected matrix is uniform on all distinct orderings of this projected multiset: each ordering has the same number of preimages in the permutation group. Different projected multisets have disjoint supports. Therefore equality of **distributions of the complete sigma_F(c)**, not merely their expected counts, is equivalent to equality of the full ordered F-row matrix distributions. It suffices to check maximal forbidden sets, since any smaller row restriction is a deterministic projection.

For fixed integer thresholds `t_Q in {1,...,m}`, one could give each orbit of each color a nonnegative probability, impose total mass1 for each color and equality of every projected-multiset probability, and retain only white orbits with `W_Q<t_Q` and black orbits with `W_Q>=t_Q` for every qualified Q. This finite rational feasibility system is complete. We do not claim that this restatement resolves the book problem; the actual result below is the concrete infeasibility certification of its six missing cases.

## 2. Necessary support filters, valid for arbitrary collections

All five instances have all participants essential and all singletons forbidden. The following filters discard no positive-probability encoding of a gap-at-least1 scheme:

1. Every white matrix has an all-zero column. The full participant set is qualified; otherwise its white stacking weight m cannot be separated from a black weight at most m.
2. Every maximal forbidden restriction of either color has an all-zero column. This is immediate for white; security transfers the entire restriction support to black.
3. Every row of either color has at least one black subpixel. For an essential participant i there are forbidden F and qualified F union {i}. Security supplies for each black B a white matrix agreeing on F, and contrast forces a column of B that is zero on F and one on i. Singleton security transfers nonzero row weight to white.
4. Every black B satisfies `W_Q(B)-W_F(B)>=1` whenever F is forbidden and F subset Q is qualified. The white matching B on F has Q-weight at least `W_F(B)`, and contrast separates that white matrix from B. This is the classical unavoidable-pattern argument of Ateniese et al. (1996), Lemmas5.7--5.11; those primary proofs were read. For gap1 this amounts to requiring at least one column from `{T: T intersects Q, T disjoint F}`. Keeping only inclusion-minimal such column-type sets is logically equivalent, since hitting a smaller set hits each containing set.

These filters are only necessary. No surviving orbit or SAT answer is treated as a construction.

## 3. Extra restrictions at the maximum-contrast face

For the first five obligations, m equals the denominator q of the independently certified global contrast `alpha*=1/q`. A positive-gap scheme at m=q must have gap exactly1 and attain that optimum. The old rational LP certificate is used only after its dual inequalities are reconstructed and checked exactly.

Let x_T,y_T be expected column counts divided by m. Security implies all forbidden column moments agree. Let `f(S)=sum_{T disjoint S}(x_T-y_T)`. Then `f(Q)>=1/m`. The old LP minimizes -a, with constraints `-f(Q)+a<=0`, the two normalization equalities, and forbidden moments. Its stored multipliers u_Q<=0 and v give an exact lower bound `-alpha*`. For each column variable define its nonnegative dual slack as objective coefficient0 minus its dual left-hand coefficient. Equality of primal and dual objectives gives the sum of nonnegative complementarity products zero. Thus any type with positive dual slack has zero expected count and can occur in no positive-probability encoding. Also `f(Q)=alpha*` whenever u_Q<0.

For such a tight Q, the average black weight minus the average white weight is exactly1. The guaranteed inequality is true for **every** positive-probability black/white pair, so their average can equal1 only if every such pair has difference exactly1. Equivalently each color's tight-Q weight is individually constant, with constants differing by1. This is not an assumption that the whole collection has a basis matrix.

## 4. Safe full-projection support pruning

Let S0,S1 initially contain all nondecreasing column lists passing the relevant proved filters (and the optimal-face restrictions only when applicable). For each maximal forbidden F, join W in S0 to B in S1 if:

- `sigma_F(W)=sigma_F(B)`;
- `W_Q(B)>=W_Q(W)+1` for **every** qualified Q;
- at an optimum-face obligation, equality holds for every tight Q.

If a vertex has no neighbor for some F, delete it. Repeat simultaneously on both sides until stable or one side is empty. Actual positive-probability support is invariant under every round: security supplies a positive-probability opposite-color encoding with the same complete F projection, and global reconstruction supplies the pairwise inequalities. Thus emptiness is a valid infeasibility certificate. Nonemptiness is never sufficient.

In the m=7 case, white orbits are generated as `(0,) + tail` over all nondecreasing six-column tails. We may initially discard a white orbit whose complete projection for some maximal forbidden F is absent from the already completely enumerated black candidate set. This is simply a first safe support-pruning step, not an additional assumption.

## 5. Complete integer-threshold branching

The m=7 case is not at maximum contrast, so it uses **no optimum-face filter**. At a stable nonempty support pair, if for some Q the largest surviving white Q-weight is at least the smallest surviving black Q-weight, branch over **every** integer `t=1,...,m`. In branch t discard whites with weight>=t and blacks with weight<t, then apply support pruning again. Empty-color branches are immediately impossible. Every actual scheme survives at least one branch: use its true integer threshold `max_actual_white W_Q+1`, which is no larger than every actual black weight. Branching terminates because a conflicting Q has both colors present and each viable threshold branch strictly shrinks at least one finite support.

More sharply, once a threshold branch fixes Q, that Q is conflict-free in every descendant because only vertices are deleted. Therefore branching depth is at most the number of qualified sets. No nonempty terminal leaf may be ignored: the verifier applies the forbidden-indicator separator separately to every nonempty terminal leaf and additionally checks that this particular complete tree has exactly one.

If no qualified Q conflicts, the surviving supports have a common valid threshold for every Q. Only then is full projected-distribution feasibility the remaining obligation. In this continuation the sole nonempty terminal support has 17 white and13 black orbits, and all eleven qualified thresholds are7. Its exact separating functional is stored in `evidence/continuation-20261014/certificate.json`.

## 6. Integer full-distribution separating functional

A term `(F,h,c)` means `c * 1{sigma_F(M)=h}`. Let L(M) be the sum of the stored terms. Each F is forbidden, so full security forces `E_white L = E_black L`. The certificate checks by integer arithmetic that **each of the17 surviving white orbits has L>=1 and each of the13 black orbits has L<=0**. Consequently the expectations cannot agree. This is an explicit infeasibility proof for arbitrary probabilities, not reliance on a solver's UNSAT response. Z3 was used only to discover the integer separator; it is not in the decisive verifier's trust boundary.

## 7. Consequence and unresolved general question

The six exclusions, together with the old basis constructions and exact alpha bounds, give collection minimum expansions `(6,7,6,7,8)` in the README's order. The best contrast at those minima is respectively `(1/6,1/7,1/6,1/7,1/8)`, since the universal bound forces integer gap at most1 and the basis witness attains1. At global alpha* the expansion must be a multiple of its reduced denominator; the excluded first multiples and the old witnesses give minimum expansions `(10,12,10,12,12)`.

Therefore all four collection optima equal their basis counterparts for **every strong nonconstant access structure on at most five participants**, completing the previously missing five rows. This is a finite structural consequence, not equality of the entire trade-off functions at every m, and not an all-n collection-to-basis conversion theorem. The original general-access question remains unresolved here. Priority is unclear pending full primary comparison, especially Shyu--Chen2015.

**Real-probability extension.** The book's finite uniform multisets, and the explicit model here, have rational probabilities. If arbitrary real probabilities on finite supports are allowed instead, fix their positive support and the guaranteed thresholds. Security and normalization form rational linear equalities. Gaussian elimination gives a rational particular solution and a rational basis for their affine solution space; approximate the real coordinates in that basis by rationals closely enough to preserve strict positivity on the fixed finite support. This gives exactly the same support and reconstruction with rational probabilities and exact security. Clearing denominators then justifies the same concatenate-collections argument. Thus no irrational-probability loophole is needed for the global-contrast transfer.

## 8. General structural consequence: an indispensable participant

Let Gamma be any nonconstant strong access structure on n participants with the empty set forbidden. Its **cone** Gamma+ adds a new participant a and declares a set qualified exactly when it contains a and its old-participant part is qualified in Gamma. In particular the entire old participant set is forbidden in Gamma+. Write G_basis for the optimal integer gap at a fixed expansion, allowing gap0, and put G_basis(0)=0.

For every integer m>=0,

    G_basis,Gamma+(m) = G_basis,Gamma(floor(m/2)).

Also the globally maximum relative contrast, in either the basis or arbitrary-collection model, satisfies

    alpha*(Gamma+) = alpha*(Gamma)/2.

Proof. In a cone basis pair let d_(b,T) be the white-minus-black column multiplicity difference, with new row b in {0,1} and old black rows T. Security for the entire old participant set gives equality of every old projected column pattern, hence `d_(0,T)+d_(1,T)=0` for every T. Put delta_T=d_(0,T). The singleton {a} is forbidden, so sum_T delta_T=0. For any old subset S, the cone moment on {a} union S is exactly `sum_(T disjoint S) delta_T`. Thus delta is an admissible old difference vector with the same forbidden equalities and qualified gaps. Its minimum realization length is `L=sum max(delta_T,0)`. The minimum realization length of the cone difference vector `(delta,-delta)` is `sum |delta_T|=2L`; any common-column padding only increases actual length. Consequently a cone basis at m yields an old basis at L<=floor(m/2), and padding gives the upper inequality for G.

Here core length means `sum_(b,T) max(d_(b,T),0)`, which is at most actual expansion m because positive differences are bounded by the white multiplicities. For `(delta,-delta)` it is `sum_T |delta_T|=2L`. The padding lemma above supplies the monotonicity used in the upper inequality.

Conversely, given old basis column-count vectors x,y of length L, use cone white counts `(x,y)` in new-row blocks0,1, and cone black counts `(y,x)`. Old-only projections agree, and each projection containing a and an old forbidden set agrees separately in its new-row0/1 blocks. A qualified cone weight difference equals the old difference. This gives length2L and the same guaranteed gap; pad identically if m is odd. The stated G identity follows, including gap0.

The identity implies the basis contrast law: any cone ratio g/m is at most `(1/2) alpha*(Gamma)`, and doubling an attaining old scheme attains equality. The already proved concatenate-collections argument identifies the global alpha optimum in the collection and basis models separately for Gamma and Gamma+, so the same contrast law holds for arbitrary collections. This does **not** identify the fixed-length collection G functions: the extraction used the per-basis equality `d_(0,T)+d_(1,T)=0`, which arbitrary collections supply only in expectation. The last five-participant case is the cone of 2-out-of-4. Our full-distribution obstruction at7 is precisely what was needed beyond this general basis identity. The lemma is an independently derived structural observation, not a novelty-cleared theorem.

**Primary-source overlap.** Arumugam, Lakshmanan and Nagar, [“On (k,n)*-visual cryptography scheme”](https://doi.org/10.1007/s10623-012-9722-2), published online2012 and in *Designs, Codes and Cryptography*71 (2014),153–162, studies exactly the cone of a (k-1,n-1) threshold structure: the publisher abstract specifies every minimal qualified k-set containing participant1. Thus the fifth finite case is their (3,5)* family, not a newly introduced access structure. The primary abstract was read; the publisher PDF redirected to subscription preview, so its detailed numerical bounds, collection-versus-basis scope, and overlap with the general all-Gamma identity remain unverified. No priority is claimed for the cone theorem or fifth-row closure.
