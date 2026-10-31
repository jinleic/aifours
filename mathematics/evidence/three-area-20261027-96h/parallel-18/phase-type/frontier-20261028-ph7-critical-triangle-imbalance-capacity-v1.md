# Critical PH7: total triangle imbalance must exceed the top-three symmetric eigenvalue product

**NEW ALL-TOPOLOGY WRITTEN APPLICATION of the exact universal six-rate lemma; independent review, parent adoption and novelty clearance pending.** MathResearch96h-2. This strengthens `frontier-20261028-ph7-critical-two-triangle-vertex-sets-v1.md` SHA256 `b08ddcaca076342c98089bef3592475c1698b8ee7762b0617111e4eaf7ce6793`. No 8/9 PH7 existence/exclusion or minimum8 claim follows.

## Theorem

Let G be any irreducible seven-state Metzler matrix of spectral bound0 whose characteristic polynomial contains `D(y)=y[(y+1)^2+8/9]^2`. Let the symmetric geometric-mean matrix be

    S_ii=G_ii,     S_ij=sqrt(G_ij G_ji),

and let `0<=lambda1<=...<=lambda7` be the eigenvalues of `-S`. For every unordered triple C={i,j,k}, denote the two oriented directed triangle products by A_C,B_C, with missing edges assigned0. Then necessarily

    sum_(unordered C) (sqrt(A_C)-sqrt(B_C))²
          > lambda5 lambda6 lambda7 > 0.             (CAPACITY)

The inequality allows arbitrary numbers of triangles, 2/4/long cycles, edge counts and hidden-root types. The sum is unchanged by positive diagonal similarity, and both sides scale cubically under positive time rescaling. Thus the statement is intrinsic to any actual PH7 realization after the standard critical shift/scale.

## Proof

The separately written symmetrization proof shows `-S` is positive semidefinite and each proper principal block is positive definite. In particular the top-three product is strictly positive by interlacing with any 3-by3 principal block.

Put `w_C=(sqrt(A_C)-sqrt(B_C))²`, `W=sum_C w_C`, and `m4=lambda1+...+lambda4`. Comparing determinant permutation terms exactly as in the two-triple theorem gives

    [y^4]det(yI-G)=[y^4]det(yI-S)-W,
    [y^3]det(yI-G)
       <= [y^3]det(yI-S)-sum_C w_C L_C,

where `L_C` is the sum of the four diagonal escape rates outside C. All 2-cycle and disjoint 2+2 terms agree; triangle orientation differences are precisely w_C; every 4-cycle orientation difference is nonnegative by AM–GM. Ky Fan's rank-four trace inequality gives `L_C>=m4` for EVERY triple, not only for a selected triangle. Therefore, using the actual target quotient Q and its positive constant q,

    E4=e3(lambda)-W-4e2(lambda)+(74/9)e1(lambda)-28/3=0,
    E3=e4(lambda)-W m4-(70/9)e2(lambda)
          +(212/9)e1(lambda)-1007/27 >=0.

Suppose contrariwise `W<=lambda5 lambda6 lambda7`. Choose the three top eigenrates as the positive triangle slots of the universal six-rate lemma; their positivity follows from proper-principal interlacing. Choose any three of the four nonnegative bottom eigenrates as its outside slots and the last as its nonnegative seventh rate. Then `theta=W/(lambda5lambda6lambda7)` belongs to[0,1]. The exact Q/H lemma pinned in the two-triple source gives, from E4=0 and q>0, the strict contradiction E3<0. Hence(CAPACITY). □

## Corollary and nonclaims

For a SINGLE unordered triple C, the row-fraction/determinant inequality in the two-triple source proves `w_C<=det((-S)_C)<=lambda5lambda6lambda7`. Thus(CAPACITY) directly implies at least two different imbalanced triangle triples. The displayed inequality is strictly stronger: it quantifies their REQUIRED cumulative imbalance relative to the symmetric spectrum, not just their count.

It is NOT a universal matrix inequality: two nearly disjoint directed triangles can make the left side larger than the top-three product. It is a necessary condition for the particular repeated-pole spectrum at8/9. The proof depends on the exact six-rate mixed-domain/two-way copositive Bernstein certificate, Perron/Cauchy symmetrization, full triangle/4-cycle coefficient bookkeeping and Ky Fan; each requires the requested independent audit. It does not rule out matrices satisfying(CAPACITY), yield an explicit 8/9 witness, prove PH order8, establish novelty, or cure historic process findings.

END — any critical PH7 realization must carry total triangle irreversibility strictly above the top-three symmetric eigenvalue product.
