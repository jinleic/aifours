# Principal idempotent bands and inverse-pair transport, without global orthodoxy

MathSemigroup, math-4. Actual precreation clock: **Sun Oct 25 04:36:41 PDT 2026** (`/bin/date`).

**Status: WRITTEN, PARTIAL, NOVELTY_UNCLEAR.** This supplies an explicit local transport representation, not the required global semidirect-product embedding. There is no scientific execution or arithmetic/symbolic interpreter. No separate reconstruction, formal/kernel verification, parent acceptance, human/cross-vendor review or novelty clearance is claimed.

## 1. A one-sided characterization of local r-orthodoxy

Let S be an arbitrary regular semigroup. Global orthodoxy is NOT assumed. For an idempotent e define

    B_e = {x in E(S): ex=x} = E(S) intersect eS,
    D_e = {x in E(S): xe=x} = E(S) intersect Se.

**Proposition.** S is locally r-orthodox if and only if every B_e is a regular band. Equivalently, every D_e is a regular band. Thus in a locally r-orthodox regular semigroup the idempotents in EVERY principal right or left ideal form a globally regular band, even though E(S) as a whole need not be a subsemigroup.

**Proof.** Suppose S is locally r-orthodox. Take x,y in B_e. The elements xe,ye are idempotents of the actual local monoid eSe:

    (xe)^2=xexe=xe,
    e(xe)=xe=(xe)e,

and similarly for ye. Local orthodoxy gives that

    (xe)(ye)=xye

is idempotent. Right multiply `(xye)^2=xye` by y. Using `ex=x`, `ey=y`, and `y^2=y`, the result is

    (xy)^2=xy.

Also `e(xy)=xy`, so xy belongs to B_e. Thus B_e is an actual band.

The map

    rho_e:B_e -> E(eSe),       x |-> xe

is multiplicative, because `(xe)(ye)=xye`. The target is a regular band. For x,y,z in B_e,

    rho_e(xyxzx)=rho_e(xyzx).

Both words end in x; `xex=x` follows from `ex=x`. Hence right multiplication by x recovers the words from their rho images, giving

    xyxzx=xyzx.

So B_e is regular. The D_e assertion is dual.

Conversely, if B_e is a regular band, then E(eSe) is a subband of B_e, hence regular. Also eSe is regular: if `a in eSe` and `a' in V_S(a)`, then `ea'e` is a mutual inverse in eSe. This gives exactly the original local r-orthodoxy. QED.

For arbitrary a in S choose `a' in V(a)`. Then `aS=aa'S` and `Sa=Sa'a`, so the idempotent assertion extends from eS,Se to every principal one-sided ideal. This does NOT say that the one-sided ideal aS itself is regular; only its idempotents form a regular band.

## 2. Explicit left/right regular coordinate bands

Green R is a congruence on a regular band, as is Green L. This is the same named classical regular-band structure import used in `n3-transport-closure-addendum-v1.md`; no such congruence is asserted on all E(S).

Consequently the quotient bands

    L_e = B_e / R,
    R_e = D_e / L

are well defined. L_e is a left regular band: in ANY band `xy R xyx`, since

    (xy)(xyx)=xyx,
    (xyx)(xy)=xy.

Thus the quotient by R satisfies `xyx=xy`. Dually R_e satisfies `xyx=yx`, so is a right regular band. These claims concern the intrinsic principal bands; the displayed idempotent multiplication criteria also show that the same R/L comparisons hold in S.

For idempotents e,f put

    B_(e,f) = {x in E(S): ex=x=xf}.

It is a subband of B_e and D_f, and the explicit map

    x |-> ([x]_R in L_e, [x]_L in R_f)             (C)

is an INJECTIVE band homomorphism. Indeed both coordinate maps are homomorphisms. Equality of both coordinates gives R- and L-related idempotents x,y, so `xy=y` from R and `xy=x` from L; hence x=y. This is genuine local separation, not an assertion of global faithfulness for the canonical band presentation.

## 3. The groupoid of regular inverse pairs

Use the following explicit groupoid Gamma(S):

- objects are E(S);
- an arrow `(s,s')` has source `s's` and target `ss'`, where `s' in V(s)`;
- inverse is `(s',s)`;
- identity at e is `(e,e)`;
- if `s's=tt'`, compose `(s,s')` after `(t,t')` as

    (s,s') o (t,t') = (st,t's').

This really is an inverse pair with the required endpoints. Setting `e=s's=tt'`,

    st(t's')st = s e e t = st,
    (t's')st(t's') = t' e e s' = t's',
    (t's')st=t't,
    st(t's')=ss'.

Associativity is source associativity, and the identity/inverse laws follow from the inverse equations. No global orthodoxy or choice of one inverse for every element is required.

## 4. Actual transport maps and exact functoriality

For an arrow `(s,s'):e -> f` of Gamma(S), define

    theta_s(x)=sxs'.

For x in B_e, this is an idempotent in B_f:

    (sxs')^2=s x (s's) x s'=s x e x s'=sxs',
    f(sxs')=sxs'.

For x,y in B_e it is multiplicative:

    theta_s(x)theta_s(y)
      =s x e y s'
      =s x y s'
      =theta_s(xy).

Thus it induces a band homomorphism `L_e -> L_f`. The reverse arrow induces its inverse: for x in B_e,

    theta_(s') theta_s(x)=e x e=xe,

and `xe R x` because `x(xe)=xe`, `(xe)x=x`. Therefore the induced map on L_e is the identity after the round trip. The other round trip is identical. These are actual isomorphisms of left regular bands.

The SAME formula on D_e induces an isomorphism `R_e -> R_f`. Now the multiplication calculation uses `xe=x`, and the reverse composite is `ex`, which is L-related to x. This is the dual proof, not an assertion that the right-ideal band and left-ideal band are the same.

For composable inverse pairs,

    theta_s(theta_t(x))=st x t's'=theta_(st)(x).

Hence these two families are genuine functors

    Gamma(S) -> isomorphisms of left regular bands,
    Gamma(S) -> isomorphisms of right regular bands.

Everything here is an explicit formula with verified domains, products and inverses. This is not a pair of unspecified faithful-functor premises.

## 5. A pure completely simple quotient is faithful on these groupoid hom-sets

Suppose additionally that an actual homomorphism `q:S -> C` is idempotent pure, where C is completely simple. It induces the obvious functor `Gamma(S) -> Gamma(C)`.

That functor is faithful on each hom-set. Indeed, let `(s,s'),(t,t')` both have source e and target f, and suppose `q(s)=q(t)`. Then `t's` belongs to eSe and

    q(t's)=q(t')q(t)=q(e)

is idempotent. Purity gives that `t's` is idempotent. It is also a unit of eSe, with inverse `s't`:

    (t's)(s't)=t'(ss')t=t'ft=e,
    (s't)(t's)=s'(tt')s=s'fs=e.

An idempotent unit equals e, so `t's=e`. Therefore

    s=fs=tt's=te=t.

The inverses agree as well: `s'=s'f=s'(st')=(s's)t'=et'=t'`.

No claim is made here that such a pure quotient exists for every arbitrary infinite book-class S. Faithfulness on groupoid hom-sets is also NOT the full semigroup embedding: Gamma(S) composes only when the idempotent endpoints match.

## 6. The precise global step still absent

The representation (C) separates every actual bi-local idempotent band. The two transport functors preserve the one-sided regular-band coordinates under every composable inverse-pair arrow. A supplied pure Rees quotient has no collapse on parallel arrows of Gamma(S).

What remains absent is a multiplication-compatible gluing across NONCOMPOSABLE inverse-pair arrows. For arbitrary s,t, their chosen middle idempotents need not agree, while the semigroup product st still exists. An ordinary groupoid-action globalization therefore does not automatically validate the canonical mixed multiplication relations; assuming it would reproduce the original construction gap.

Equivalently, the local coordinate bands and all transports above have not been glued into ONE locally regular band with the specified Rees/group action in a way preserving all idempotent fibres. There is no displayed globally injective S-map from this packet, and no contradiction to embeddability. The N3 countermodel route is separately closed by the complete written addendum, not revived here.

These exact local maps are a new representation for the remaining global gluing problem. They are complete WRITTEN results at the regular-band R/L-congruence import, not an unfinished implementation or a claimed solution of the original book question.
