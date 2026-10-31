# RQLS10 v18 — the ENTIRE Witting40-ray model cannot fill the surviving4-dimensional sector

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 06:52:27 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact complex/finite-field/character/graph arguments only. No interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO, no private decimal/approximate scout or discarded-probe backconversion. No machine/kernel/formal/human/configured-family/novelty acceptance.

Original unrestricted maximal1-RQLS(10) remains UNKNOWN. The new v15/v16 intrinsic sector theorem leaves{10},{4,6},{5,5}. This paper attacks a natural actual40-ray candidate for the4-sector, rather than transferring a3-dimensional argument to C^4. It excludes its ENTIRE phase/permutation/unitary-equivalence orbit as a sector model, not arbitrary4-dimensional sectors or the whole original problem.

## 1. Literal rays and theorem

Put omega=exp(2*pi*i/3). Besides the four coordinate rays e0,e1,e2,e3 in C^4, take the following four9-ray families, with all labels in F3 and normsqrt3 before normalization:

    V0(a,b)=(0,1,-omega^a,omega^b),
    V1(c,d)=(1,0,-omega^c,-omega^d),
    V2(e,f)=(1,-omega^e,0,omega^f),
    V3(g,h)=(1,omega^g,omega^h,0).                  (RAYS)

These are40 DISTINCT rays: different zero positions distinguish the four families, fixed leading coordinate phases distinguish all9 within each, and none is a coordinate ray.

**Theorem.** No assignment of these40 rays, each exactly once, to the cells of a rank4 common sector of a maximal1-RQLS10 can satisfy BOTH its row and column ONB requirements. Therefore the6-dimensional complement and designated-transversal completion cannot rescue this whole model. The statement is invariant under a common unitary, arbitrary ray phases and any ray/cell permutation.

The proof supplies ALL bases, the exact quadric incidence, every spread classification step and the all-spread intersection argument. It does not import a computer catalogue, an unproved identification of Witting with a generalized quadrangle, or a finite search over partitions.

## 2. The COMPLETE list of possible bases, parametrically

A useful elementary reduction is F4={0,1,Omega,Omega^2}, with Omega^2+Omega+1=0. Reducing signed powers of omega to F4 (where minus=plus) maps RAYS bijectively onto the projective NONISOTROPIC rays of the standard Hermitian4-space overF4. They are precisely the rays with odd support size1 or3: the Hermitian norm is the support parity. There are4 coordinate and4*3^3/3=36 weight3 rays.

This map preserves orthogonality in BOTH directions. Within one family the complex product is a sum of THREE cube roots, zero iff they are all different; the F4 sum has the same criterion. Between different families there are TWO terms of OPPOSITE fixed signs, zero iff their cube-root phases agree; in F4 the two equal terms also cancel. With coordinate rays orthogonality is exactly the zero-coordinate condition. No arithmetic approximation or unlisted pair test is used.

Any two orthogonal nonisotropic F4 rays span a nondegenerate2-space. Their complement is another nondegenerate2-dimensional Hermitian space and has exactlyTWO nonisotropic projective rays; in orthonormal coordinates they are the two coordinate rays (support2 vectors are isotropic). Those two are orthogonal. Thus every orthogonal ray pair has a UNIQUE completion to a4-ray basis in this configuration.

Consequently a basis containing two coordinate rays is the full coordinate basis B0. A basis containing one coordinate ray ei and no other axis consists of the three rays of Vi whose two phase labels sum to a fixed value; there are3 such bases for each i, giving12 in total. If an axis-free basis contained two rays of the SAME family Vi, their unique completion would contain ei, contradiction. Every axis-free basis therefore contains exactlyONE ray of EACH family.

Their six orthogonality equations give ALL such bases in the following exact form:

    B(a,b,c)={V0(a,b),
               V1(c,c-a+b),
               V2(c-a,c-a+b),
               V3(c-a,c)},             a,b,c in F3. (BASES)

For example V0/V1 gives d=c-a+b; V0/V2 gives f=e+b; V1/V2 gives f=d and e=c-a; V0/V3 gives h=g+a; V1/V3 gives h=c and g=c-a. The remaining relation agrees. This proves necessity AND sufficiency. All27 triples(a,b,c) give distinct bases; along with B0 and the12 axis bases, these are exactly40 possible ONBs. No additional basis is silently excluded.

## 3. A literal basis-point/ray-line quadric bridge

Use projective coordinates(P,Q;a,b,c) overF3 and the nonsingular parabolic quadric

    P*Q=F(a,b,c),
    F(a,b,c)=a^2-ab-ac-bc.                          (QUADRIC)

Map the27 bases B(a,b,c) to(1,F(a,b,c);a,b,c), and B0 to infinity=(0,1;0,0,0). Its other P=0 points have F(a,b,c)=0 with(a,b,c)!=0. The four isotropic directions of F are EXACTLY

    k0=(0,0,1), k1=(1,1,0),
    k2=(1,0,1), k3=(0,1,0).

Indeed at a=0 one has bc=0; at a!=0 normalize a=1 and F=0 is(b+1)(c+1)=2, with precisely the two indicated remaining directions. Each direction gives3 projective points(0,t;ki). These are exactly the12 axis bases under this map:

- ei=e0: Vi=V0 phase sum a+b=-t, direction k0;
- e1: V1 phase sum c+d=-t, direction k1;
- e2: V2 phase sum e+f=t, direction k2;
- e3: V3 phase sum g+h=t, direction k3.

Holding the labels of a fixed V0(a,b) in BASES lets c vary. Its three affine points form an affine line of direction k0; the fourth projective point is(0,-a-b;k0), exactly its axis-basis point. Similarly the directions for V1,V2,V3 are k1,k2,k3, and direct differentiation of F along them gives respectively-(c+d),e+f,g+h. Hence EACH of the36 nonaxis rays is mapped to its literal4-point quadric line. An axis ei is incident with B0 and its3 axis bases; those four points are the line spanned by infinity and(0,0;ki).

Thus the40 rays are40 quadric lines, and the40 bases are ALL40 quadric points, with EXACTLY the original incidence. To see there are no other quadric lines, infinity has exactly4 such lines (the four isotropic directions). The explicit quadric point transitivity below gives4 lines through every point; counting gives40*4/4=40. This supplies the whole incidence identification, not only matching parameters.

## 4. Explicit quadric point transitivity — no geometry-classification import

Let B_F(x,u)=F(x+u)-F(x)-F(u). For fixed u in F3^3, the linear projective map

    P'=P,
    x'=x+u*P,
    Q'=Q+B_F(x,u)+F(u)*P

preserves P*Q=F(x), and has inverse obtained by-u. The swap(P,Q) also preserves it. The ternary F is nondegenerate, as is seen from the invertible coordinates

    x=a-b+c, y=c, z=a+c,
    F=x*z-y^2.                                     (COORD)

Every affine point P!=0 can therefore be moved to(1,0;0) by a translation and then to infinity by the swap. A point with P=0,x!=0 can first have Q made nonzero, because nondegeneracy makes u->B_F(x,u) ontoF3; after a swap it is affine. The remaining P=0,x=0 point is infinity itself. Thus the orthogonal/projective incidence group is transitive on all40 points, by explicit formulas.

This transitivity applies both to arbitrary ovoids and to hyperplane sections; no assumption that every combinatorial automorphism is projectively linear is needed.

## 5. Classify EVERY ovoid through infinity by a27-point character identity

A10-basis spread is a set of ten bases partitioning all40 rays. Under Section3 it is an ovoid of QUADRIC: ten pairwise noncollinear points. Conversely ten pairwise noncollinear quadric points meet each of its40 lines exactly once (each point is incident with4 lines), so give a spread.

An ovoid containing infinity cannot contain any other P=0 point, because those12 points are collinear with infinity. Its remaining9 points are affine, and two such points are collinear iff their ternary coordinate difference has F=0. In COORD, this is the graph on F3^3 with adjacency

    v~w iff v!=w and Q3(v-w)=0,
    Q3(x,y,z)=x*z-y^2.

It has degree8 (four isotropic projective directions, two nonzero vectors each). This is a finite-field GRAPH REPRESENTATION, not an executed27-vertex search.

Put xi=(xi1,xi2,xi3), eta=exp(2*pi*i/3), G=eta-eta^2 with G^2=-3. Completing the y-square and eliminating one of x,z in the character sum yields, for t!=0,

    sum_v eta^(t*Q3(v)+xi dot v)
       =-3*G*Legendre(t)*eta^(-Q3(xi)/t).

Here4=1 in F3, so the dual quadratic has the same displayed form. Applying the identity1_(Q3=0)=(1/3)sum_t eta^(t Q3) and subtracting the origin gives the adjacency character eigenvalues:

    8,                 xi=0;
   -1,                 xi!=0,Q3(xi)=0;
   -4,                 Q3(xi)=1;
    2,                 Q3(xi)=2.                  (SPECTRUM)

For example at Q3(xi)=1 the needed difference is eta^-1-eta^-2=-G, giving-1+G^2=-4. At2 it is G, giving-1-G^2=2. This derives the full spectrum without an arithmetic program.

Let C be the9 affine ovoid points and f its0/1 indicator. Write f=(1/3)1+g, so |g|^2=6. Independence gives f^T A f=0. The constant contribution is24 and the smallest eigenvalue is-4, so equality forces g ENTIRELY in the-4 eigenspace.

The six frequencies with Q3(xi)=1 are the plus/minus multiples of exactlyTHREE independent directions

    (1,0,1), (1,1,2), (1,2,2).

Completeness follows directly by separating xi2=0 from xi2!=0 in xi1*xi3=1+xi2^2: there are2+4=6 vectors. Their determinant is2 in F3, so the three linear forms ell1,ell2,ell3 are independent. Thus f has the form

    f(v)=1/3+h1(ell1(v))+h2(ell2(v))+h3(ell3(v)),

where each h is a real zero-mean function onF3.

**Boolean additive lemma.** Such a0/1 function on three independent coordinates depends on AT MOSTONE coordinate. If h1 takes two different values, their difference must be+/-1, because f changes by the same nonzero amount at ALL settings of the other coordinates. Those two f values are then FORCED to be0 and1 everywhere, so h2+h3 is constant for every choice; varying each separately makes both constant. The same argument applies whichever h is nonconstant. Since f has mean1/3, preciselyONE of the three values of its one relevant coordinate is accepted.

Hence C is EXACTLY one affine plane

    ell_i(v)=s,       i in{1,2,3}, s in F3.          (NINE)

Conversely each such plane has no isotropic nonzero difference, as is also implied by its equality-case character construction; directly its kernel restricts Q3 to an anisotropic binary form. Thus there are exactlyNINE ovoids through infinity. No positive-dimensional/generic or finite-subset assumption was made.

## 6. ALL36 spreads are hyperplane sections and ANY TWO intersect

Each ovoid in NINE, together with infinity, is the hyperplane section

    ell_i(x)-s*P=0

of QUADRIC. Its P=0 points consist only of infinity, because Q3 has no nonzero zero in ker(ell_i). It is therefore an elliptic10-point hyperplane section and an ovoid.

By Section4 every quadric point lies in exactly9 ovoids. Counting(point,ovoid) incidences gives

    number of ALL ovoids=40*9/10=36.

The same transitivity applies to hyperplane sections that are ovoids. Through infinity there are exactlythe9 just classified; hence the number of ovoid hyperplane sections is also36. Different such hyperplanes give different10-point sections: otherwise their common projective plane would contain10 quadric points, impossible because a NONZERO ternary quadratic overF3 has at most7 projective zeros. A plane cannot be wholly in this nonsingular5-dimensional quadric, since a3-dimensional totally singular vector subspace would be contained in its2-dimensional orthogonal complement.

For transparency, the ternary zero count needs no classification catalogue: diagonalize in odd characteristic. Rank1 gives4 projective zeros; rank2 gives7 (split) or1 (anisotropic); rank3 gives4, from the two possible sign patterns of diagonal coefficients+/-1. Thus7 is a uniform bound. The36 ovoid sections exhaust the36 ovoids, so EVERY spread is a hyperplane section.

Now take ANY TWO spread hyperplanes. Their intersection is a projective plane. The restricted ternary quadratic ALWAYS has a nonzero zero overF3: if degenerate it has a nontrivial radical; if nondegenerate, diagonalize with coefficients+/-1. Opposite signs cancel using two coordinates1,1; if all signs agree then1+1+1=0 in F3. Therefore their plane meets QUADRIC.

Thus ANY TWO ovoids meet in at leastONE point. Dually, ANY TWO spreads of the40-ray configuration share at leastONE ENTIRE four-ray basis. This is a whole-spread theorem, not a numerical packing failure or one chosen pair of resolutions.

## 7. Application to the ORIGINAL row/column partial array

A rank4 common sector in a maximal1-RQLS10 has exactly40 distinct rays and ten row ONBs of size4 partitioning them, by the unrestricted context trace identity in v15. If those rays are RAYS, the row bases form one spread S. Its ten column ONBs form a second spread T.

They CANNOT share a basis: that same set of four distinct rays would have to occur in one original row AND one original column. Since each ray occurs in exactlyONE cell, the two four-cell sets would coincide, whereas an original row and column intersect in onlyONE cell. Contradiction.

But Section6 says every pair of spreads shares a basis. Hence no row/column partial array exists with this whole model, before any issue of designated transversals or the6-dimensional complement is considered. This proves the theorem for every unitary/phase/ray-permutation equivalent model.

The dimension4 unique-completion property used in Section2 is a property of this EXACT40-ray finite Hermitian configuration, not of arbitrary complex rays inC4. No rank4 common-sector no-go is inferred without that model hypothesis. The proper4/6 branch remains open for other configurations; proper5/5 and irreducible10 remain open as well.

## 8. Source context and assurance

The model was suggested by the exact Witting/Penrose coordinate sets in [Vlasov2503.18431v1](https://arxiv.org/html/2503.18431v1) and [Waegell–Aravind1701.06512v2](https://arxiv.org/html/1701.06512v2), which were read as static text/image context. [De Winter–Thas2010](https://msp.org/iig/2010/11-1/iig-v11-n1-p02-p.pdf) supplied general spread/ovoid background. Their source algorithms, computer equivalences, counts or classifications are NOT operative proof imports here: every basis, incidence bridge, spectrum, equality case, transitivity and counting argument actually needed is displayed above. The elementary nondegenerate Hermitian-complement and quadratic diagonalization facts remain ordinary finite-dimensional linear algebra, not a formal kernel proof.

No actual100-ray maximal1-RQLS10, full original no-go, complete rank4-sector classification, I1 certificate TYPE, novelty/SOTA or executable finite certificate is supplied. This is a new conditional candidate closure of a natural surviving-sector construction mechanism, with its actual model hypothesis explicit. Fresh full source/dependency review is needed. All frozenbytes/old findings, v9 and v14 mathematical withdrawals and ZERO-credit quarantines remain permanent. Same original18/exclusive root/HOLD/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 and30min substantive actual-clock cadence. Primary continues the genuinely arbitrary surviving branches, not a terminal park for pending gates.
