# Nonconvex private staircase cores: sharp weak-to-TV erosion criterion

**AUTHOR CANDIDATE — WRITTEN with exact rational control; NOT independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 18:29:36 PDT 2026`.

## 1. Exact source-interface statement

Fix EVERY finite epsilon>0, b=e^(-epsilon), and the FULL CLOSED l1 unit diamond D. Let F_epsilon be all Borel probability laws satisfying the epsilon event inequality for EVERY Borel set and EVERY shift in D.

Let S be ANY compact planar set with nonempty interior satisfying

    S = closure(int S),          Lebesgue_area(boundary S)=0.             (1)

S may be disconnected, nonconvex, asymmetric and not contain 0. Define

    n_S(x)=min{k>=0:x in S+kD},       q_S(x)=Z^(-1)b^(n_S(x)),
    E={x:x+D subset S}.                                                  (2)

The candidate theorem is the exact equivalence

    |E|=0    iff    [for every mu_n in F_epsilon, mu_n=>q_S dx
                     implies TV(mu_n,q_S dx)->0].                        (3)

When |E|>0, a single explicit same-epsilon oscillatory construction violates the weak-to-TV implication. It does NOT require E itself to have an interior or a smooth bump. Every q_S and every constructed law is genuine full-event/FULL-CLOSED-D private with exact privacy epsilon.

This substantially extends the still-UNREVIEWED convex-core criterion `frontier-20261028-staircase-erosion-tv-criterion-v1.md`, SHA `2390d99df92b2a2254cc431a8c849613d0aea478dd00421a10e4ec25dce76758`, and the original-optimum saturation stability. It is a theorem about already-existing geometric shell frameworks, not a claim of original Euclidean optimality, source priority, or novelty. Its proof below is direct and does NOT import LAW642, v241, the f68 TV repair, MDA, PMLR or the earlier convex author candidate.

## 2. The law is actually private and its shell boundaries are null

Compact nonempty S implies n_S is finite everywhere; boundedness gives `n_S(x)>=||x||_1-M` for a finite M, so Z is finite and positive. If h in CLOSED D and x in S+kD, then x+h in S+(k+1)D; applying this to −h gives `|n_S(x+h)-n_S(x)|<=1`. Thus q_S is pointwise fully private and, on integration, satisfies EVERY Borel event inequality. Far in the positive quadrant the same compact-core argument `n_S(x)=ceil(x1+x2-max_S(s1+s2))` gives a positive-probability event that attains epsilon exactly.

For ANY closed S and k>0,

    S+kD={x:d(x):=dist_1(x,S)<=k},       boundary(S+kD) subset {d=k}.

Each positive level set `{d=k}` has planar measure zero. Indeed d is Lipschitz and hence differentiable a.e.; at a differentiability point outside S choose a nearest z in compact S and put u=(x-z)/d(x), so ||u||_1=1. For 0<t<d(x), nearest-point comparison and the 1-Lipschitz inequality give `d(x-tu)=d(x)-t`, hence grad(d)·u=1 and the gradient is nonzero. A differentiable function has zero gradient at a density-one point of any of its level sets (otherwise a cone of directions gives a positive fraction of nearby points off the level). Lebesgue density then forces the positive level set to be null. This proof does NOT assume S or S+kD convex.

Together with the separately assumed null boundary of S, the open sets

    U_0=int S,
    U_k=int(S+kD) minus (S+(k-1)D),     k>=1                              (4)

cover R^2 up to a null set. On U_k the actual q_S equals b^k/Z. The sets U_k need not be connected.

## 3. Null erosion: adjacent strict saturation without convexity

Assume |E|=0 and let mu_n in F_epsilon converge weakly to Q_S. As in the convex proof, integrating privacy over D yields all-point finite ball-limsup density representatives p_n of the SAME laws, bounded by 1/(2b) and satisfying `p_n(y)>=b p_n(x)` whenever ||x-y||_1<=1. Euclidean-ball boundaries are Q_S-null, so their masses converge under weak convergence.

For x in U_0 minus E, x+D is not contained in S. Closedness of S ensures some h in int D has x+h outside S; y=x+h lies in the open set S+int D, hence in U_1, and the l1 distance is <1.

For k>=1, consider a point x in U_k with `d(x)<k`; the ignored set d(x)=k is null by §2. Since S=closure(int S), approximate a nearest point of S by some z in int S with `||x-z||_1<k`. Set h=x-z and `y=z+(k-1)h/k`. Then y belongs to int(S+(k-1)D) and `||x-y||_1<1`. If k>=2 and y belonged to S+(k-2)D, adding h/k in int D would put x in S+(k-1)D, contradicting x in U_k. Hence y in U_(k-1); for k=1, y=z in U_0. Convexity of S is not needed: only convexity of D and the strict radius margin are used.

Small Euclidean balls U around x and B around y lie in these respective open plateaux and have every cross-pair at distance <1. For k>=1,

    p_n(x')-b p_n(y')>=0   on U×B,
    integral_(U×B)(p_n(x')-b p_n(y'))
       = |B|mu_n(U)-b|U|mu_n(B) ->0,

because q_S has exactly that saturated b ratio. A triangle inequality through the common B yields local L1 convergence to the constant target on U. The core-to-outer case has the same proof and factor 1/b. A compact exhaustion/finite-ball subcover plus the uniform density cap gives L1 convergence on each fixed bounded plateau; the null E and shell boundaries do not matter. Finally weak convergence on S+ND, whose boundary is target-null by §2, and N->infinity control the tails. Thus TV(mu_n,Q_S)->0.

## 4. Positive erosion: no interior of E is required

E is closed and bounded because it is the intersection of the closed sets S-h over h in compact D and is contained in S. Suppose |E|>0; E might still have empty interior. Define

    c_n=|E|^(-1) integral_E sin(2pi n x1)dx,
    f_n(x)=1_E(x)[sin(2pi n x1)-c_n],
    a=(1-b)/[4(1+b)],
    p_n(x)=q_S(x)[1+a f_n(x)].                                           (5)

On E subset S, q_S is the constant 1/Z, and the correction c_n makes `integral p_n=1`. Since |f_n|<=2 and `2a=(1-b)/[2(1+b)]<1`, the densities are strictly positive. On any two points of S their ratio is at most

    (1+2a)/(1-2a)=(3+b)/(1+3b)<1/b.

If a pair x,y at l1 distance<=1 crosses outside S, neither point is in E: membership of one in E would force its entire D-neighborhood, including the other, inside S. Thus both values are unperturbed q_S values and remain private; outside/outside pairs are also unperturbed. Hence every p_n satisfies the all-point, all-closed-D density bound and every event inequality.

E is bounded. Riemann–Lebesgue gives c_n->0 and weak convergence `p_n dx =>Q_S`. Periodic absolute-sine averaging and `|| |sin-c_n|-|sin| ||<=|c_n|` give

    TV(p_n dx,Q_S) -> a|E|/(pi Z)>0.                                     (6)

The far-quadrant exact-epsilon event of §2 is outside the bounded E and is unchanged, so each p_n has exact privacy epsilon. This establishes the converse of (3) even if E has no interior. No symmetry of S or E and no approximate normalization are assumed.

## 5. Concrete disconnected and shielded examples

**Nonconvex stable core:** take S to be the union of two disjoint Euclidean disks of radius 1/4 centered at (−2,0) and (2,0). It is compact, regular closed, has null boundary and is disconnected/nonconvex. E is empty: a translate of the connected D contained in S would lie in one connected disk component, but D has Euclidean diameter 2 while each disk has diameter 1/2. Hence the resulting fully private, exact-epsilon shell law has weak-to-TV continuity by (3).

**Explicit shielded failure:** take S=2D, b=1/2. Here E=D, |E|=2 and Z=22. In (5), symmetry gives c_n=0, and a=1/12, so

    p_n=q_(2D)[1+(1/12)1_D(x) sin(2pi n x1)].

The exact privacy bound is at most 7/5 inside the modified core versus the allowed factor 2; crossing pairs are unchanged, and an actual far-quadrant event attains factor 2. These densities converge weakly to Q_(2D) but have

    TV(p_n dx,Q_(2D)) ->1/(132pi)>0.

The bounded exact Fraction arithmetic actually printed

```text
b=1/2 indicator-erosion amplitude= 1/12 worst core factor ratio bound= 7/5
S=2D, Z= 22 erosion_area= 2 TV_limit_coefficient_of_1_over_pi= 1/132
```

The arithmetic is a selected control; the general iff uses the written distance-level, saturation and oscillatory arguments.

## 6. Limits and independent review

The hypothesis `S=closure(int S)` with null boundary is explicit and is NOT dropped for arbitrary fractal cores. Standard imports: Radon–Nikodym/Lebesgue differentiation and density, Rademacher, weak convergence/Portmanteau, Riemann–Lebesgue and periodic averaging. No general norm, higher-dimensional, or nonadditive-channel result is asserted. The original unique Euclidean optimizer's particular core is convex and hence satisfies (1), but identifying its empty erosion is a separate LAW642/v241/f68-repair caller, not an input to this standalone criterion.

Request complete disjoint review especially of positive distance-level nullity, nonconvex adjacent-level selection, oscillations on a possibly interior-empty erosion, and exact privacy at core boundary. This is AUTHOR-WRITTEN, not independent-model/human/formal/kernel or novelty acceptance; historical held results are not accepted premises.
