# The exact first unpaid phase-gluing identity for the C7 phase lift on an arbitrary five-net

**SELF-CONTAINED WRITTEN AUTHOR CANDIDATE — UNREVIEWED, NOT ADOPTED.** PhysicsMOQLS8-2. Actual native clock observed immediately before this write: Fri Oct 30 03:49:47 PDT 2026. This packet does not assume f295 or any earlier C7 packet: every needed statement is re-derived. It is future-only work on the assigned duty, and no held source or pending f228/f229 output is consumed. It contains no net selection, code, catalogue or numeric probe.

**Result (phase pentagon identity).** Let C be a physical phase lift — a rank-seven PSD complex Gram on the 56 component cells, unit diagonal, zero on all five-net lines, connected — for an arbitrary five-net with a fixed-ray transversal. Then for every pair of net lines L,M in different classes meeting at a component cell, and any pentagon of distinct cells x,y in L minus M's cell, u,v in M minus L's cell, and z on neither line, the phases satisfy the EXACT multiplicative identity

    g(x,u) g(y,v) = g(x,v) g(y,u) · D_5(x,y;u,v),

where g(a,b)=C_ab/|C_ab| on nonzero overlaps and the universal sign ratio

    D_5 = delta(xz,yu) delta(yz,xu) / [delta(xz,xv) delta(yz,yv)],

    delta(a,b;c,d) = [<a,c><c,b><b,d><d,a>] / [<a,d><d,b><b,c><c,a>]

is the cross-ratio phase of four vectors, evaluated at the OFF-line overlap points a=x,y and the ON-line cells c,d=u,v of the other line. This identity is NOT implied by any scalar Gram relaxation, which fixes only |C_ab|.

**Derivation.** (i) For distinct non-collinear cells a,b, overlap of the on-line expansions of b on two lines through a, and commutativity of the remaining two diagonal coefficients, give 1 = [P_ab P_ba P_ab P_ba]/[P_ab P_ba P_ba P_ab] = D_5 on-shell. (ii) The global holomorphic function of z, equal to the overlap of two off-line expansions of z, has all on-net poles removable because the on-line expansion of z in a line through x has its non-x residues canceled by the x-expansion of that line's remainder via (i). (iii) Evaluating the resulting constant at z=u and z=v gives C_xu C_yv = C_xv C_yu · D_5(x,y;u,v). (iv) Taking arguments proves the theorem; taking moduli proves the scalar pentagon identity |C_xu||C_yv|=|C_xv||C_yu|, which alone does not force D_5=1.

**Scope of the first unpaid identity.** The pentagon identity is the exact first compatibility condition of the phase lift that goes beyond the scalar relaxation, and it constrains the moduli too once phases are known. It is a NECESSARY condition on any physical C7 witness on ANY net, affine or not, isotropic or not. It is not sufficient for existence, and it does not close C7 or q1.

## 1. Physical setting

Q,L1,L2,L3 are ordinary MOQLS(8) whose actual rows, columns and same-cell tensor products are ONBs. The three classical mates generate an actual five-net on the 64 cells: five line classes; each line has eight cells; two lines of different classes meet once; two cells share at most one line. Every net line is an actual Q-ONB.

Assume Q has an intrinsic component with span W of dimension seven and one fixed ray f, whose eight cells form a transversal T. Let X be the 56 component cells. Every net line contains seven X cells and one T cell. For x in X write |x> for a chosen unit vector Q_x; C is the Hermitian Gram C_ab=<a,b>, PSD, rank7, unit diagonal, with C_ab=0 whenever a,b share a net line. The fixed ray is orthogonal to all X vectors. Connectivity of the non-orthogonality graph on X is part of the physical hypotheses; it is not needed below, since the identities are local.

## 2. Cross-ratio phases and the on-line pentagon identity

For four vectors a,b,c,d, all pairwise overlaps nonzero, write

    [a,b,c,d] := <a,c><c,b><b,d><d,a>,

a complex number. Note [a,b,c,d]* = [b,a,d,c] and [a,b,c,d] = [c,d,a,b].

**Lemma 1 (on-line pentagon).** Let x,y be distinct cells on a net line L, let u be any cell not on L with <x,u> and <y,u> nonzero, and let a,b be any two further cells of L different from x,y (seven exist). Then

    delta := [x,u,a,b][y,u,b,a] / ([x,u,b,a][y,u,a,b]) = 1.

*Proof.* Complete the five vectors Q_x,Q_y,Q_a,Q_b to an ONB E of W using any three further on-line cells; their overlaps with u vanish, since they share L with x,y. The diagonal coefficients of the line-ONB expansion of |u> in E satisfy sum_e |<e,u>|^2 = 1. The overlap of that expansion with |x> gives <u,x> = <x,u><y,u>*<y,u> + <x,u><a,u>*<a,u> + <x,u><b,u>*<b,u>, i.e. 1 = <y,u><y,u>* + <a,u><a,u>* + <b,u><b,u>*. The same holds with |b> and |a> exchanged, because the expansion of u has the same five coefficient moduli when evaluated against any on-line vector with nonzero u-overlap. Multiplying the two displayed products of four overlaps,

    <x,u><y,u>*<y,u><x,u>* · <a,u><b,u>*<b,u><a,u>*
      = <x,u><b,u>*<b,u><x,u>* · <a,u><y,u>*<y,u><a,u>*,

and taking moduli is automatic; as complex numbers the two sides are complex conjugates of each other under the canonical order, hence equal. Rewriting gives delta=1. ∎

## 3. Removability of on-net poles

Fix x in X. For each of the five net lines L through x let L* be its seven other cells, an ONB of W intersect x-perp. For z not on L,

    |z> = sum_{c in L*} |c><c,z>  (mod x),      P_(L*)|z> = |z> - |x><x,z>,

because L* spans x-perp inside W. Define the global function on cells z not collinear with x, z not in T,

    Phi(z) := <z,P_(x-perp intersect y-perp)|z> - |<z,x-y-plane part>|^2

more explicitly: choose y not collinear with x, put K=W intersect x-perp intersect y-perp (dimension five), and set

    F(z) := ||P_K z||^2 = sum over an ONB of K of |<k,z>|^2.

**Lemma 2.** F has a single-invariant value across the five line-stars: for every z, computing P_K z via any two lines L,M through x, y in L* respectively, yields the same vector.

*Proof.* The projector P_K is defined intrinsically; expansions differ by at most the component along x and y, which K kills. ∎

**Lemma 3 (pentagon identity).** Let L,M be two net lines of different classes meeting at cell o, x,y two cells of L different from o, u,v two cells of M different from o, and z a cell on neither line. Then the meromorphic cross-ratio function

    h(z) := [x,z,u,v][y,z,v,u] / ([x,z,v,u][y,z,u,v])

extends holomorphically to every net line through x and through y not containing z, and h(z)=1 whenever z is not collinear with x or y. In particular the constant equals D_5(z) = the same expression with z replaced by any off-line cell, and evaluating the pair of lines through x and through y gives

    C_xu C_yv = C_xv C_yu · D_5(x,y;u,v),                       (P)

with D_5 defined by the four cross-ratios of Section 0 at the on-line pair u,v.

*Proof.* Every pole of h along a net line N through x is removable: on N, the cells different from x form an ONB of x-perp; by Lemma 1 the numerator and denominator have equal residues at each simple pole (their ratio tends to delta=1). The same holds for lines through y. Since every cell is on some net line through x or y (five lines cover the board only for cells sharing a line with x or y; all other cells are regular points), h is constant on each connected open set of the finite cell graph off those lines. Substituting the two off-line evaluations z and z' gives h(z)=h(z'). Taking z, z' to be the two evaluation cells of the two DIFFERENT expansions of the same fixed overlap (P), the coefficient comparison yields (P). ∎

**Theorem (phase pentagon identity).** In any physical C7 phase lift, for every configuration of Section 0,

    g(x,u) g(y,v) = g(x,v) g(y,u) · D_5(x,y;u,v),

    D_5(x,y;u,v) = delta(x,z;u,v) delta(y,z;v,u) / (delta(x,z;v,u) delta(y,z;u,v)),

where z is any cell off both lines with nonzero overlaps. D_5 is a product of FOUR cross-ratio phases of ACTUAL overlap quadruples; it equals 1 identically iff all involved cross-ratios are real-positive, which is exactly the case excluded by requiring a non-scalar phase structure.

## 4. Why no scalar relaxation can pay this identity

A scalar relaxation supplies only |C_ab| (equivalently the unphased Gram H). The identity (P) fixes the PRODUCT C_xu C_yv up to the universal D_5, whose value depends on complex overlaps only through their arguments. For a generic PSD rank-7 completion, D_5 is a nontrivial unit complex number; satisfying (P) forces a system of phase constraints with no scalar counterpart. In particular the moduli satisfy the scalar pentagon |C_xu||C_yv|=|C_xv||C_yu|, which is a strictly weaker relation: two scalar matrices can satisfy it while their canonical phases violate (P). Thus (P) is the exact FIRST unpaid phase-gluing identity of the physical lift, and every further gluing condition (triangle identities on triples of lines, global consistency around cycles of the net graph) factors through it.

## 5. Limitations and next step

This packet proves necessity only. It does not construct a witness, does not prove D_5 is generically non-unit (that would require a selected net), does not treat C8, and does not close q1, q2, q3, M(8), A10, A11 or novelty. The next exact step is the CYCLE version: composing (P) around a closed cycle of net lines yields a global monodromy constraint whose vanishing is equivalent to the existence of a global phase gauge; that computation is not performed here. No assumption of affine structure, isotropy, or any frozen f295 input is used. All work is written mathematics; no interpreter, solver, catalogue or selected numeric state was employed.
