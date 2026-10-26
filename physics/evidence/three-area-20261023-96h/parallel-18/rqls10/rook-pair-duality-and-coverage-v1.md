# Rook-pair duality and coverage v1 — all-negative pairs close too

PhysicsRQLS10. Written exact argument; no creation-clock estimate or scientific executable. Read with `rook-positive-pairs-closure-v1.md`, the rank8 theorem and conference-gluing scope. All conclusions remain author-written CANDIDATE pending independent reconstruction/parent check.

## 1. Explicit normalization clarification for the positive-pair paper

When describing the four second-grid pairs as covering every point except0, choose a representative p fixing0. This is without loss for a literal second core Q': if p(0) is another grid point, compose the old grid labels with an additive translation sending that point to0. Translations preserve Q and C, so Q' itself is unchanged. No physical phase or relative orientation is fixed by this choice. This supplies the implicit normalization used in that paper's geometric classification and384-table count.

## 2. An actual solution-preserving complement duality

Fix the first core C on GF(9), rho(t)=-t and arbitrary second core Q'. Let g be multiplication by a nonsquare, for example1+alpha. It fixes0, commutes with rho, and

    g Q g^T=-Q,

because chi(g)=-1. Here g denotes the corresponding permutation action; either inverse convention gives the same sign conclusion.

Complex-conjugate every basis vector and phase, then apply the same coordinate and basis relabeling g. The first core C is restored: conjugation sends C(Q) to C(-Q), and g sends -Q back to Q. The second character core becomes

    Q''=-g Q' g^T.                                        (D)

The zero matching rho is preserved because g commutes with it. Arbitrary diagonal compatibility phases are merely conjugated/permuted and remain arbitrary unit phases. Thus a physical local phase gluing exists for Q' iff one exists for Q''. This is an exact existence-preserving map, not an assumption that conjugation is an allowed isotopy equivalence.

If k of the four inversion pairs satisfy Q'_(r,-r)=+1, exactly4-k satisfy this for Q''. Therefore the complete k=4 no-go in the positive-pair paper also excludes **every k=0 second core**, with all independent complex phases retained.

No new phase-field, global vector symmetry or candidate enumeration is needed. It also suffices to treat the k=3 class before its dual k=1 class. The k=2 class is self-dual and remains genuinely separate.

## 3. Exact discrete signature counts, not scientific-instance counts

After p(0)=0, the raw orientations of the four inversion pairs are perfect matchings of the eight other grid points. Let N_k count matchings with exactly k rook edges. There are105 total matchings. The positive-pair classification gives N_4=8; complement duality gives N_0=8 and N_3=N_1=a. Write N_2=b.

Then

    2a+b=105-16=89.

The rook graph induced on the eight nonzero points has14 edges: four vertices have degree3 and four have degree4. Its pairs of disjoint edges number

    binom(14,2)-4 binom(3,2)-4 binom(4,2)
      =91-12-24=55.

A fixed disjoint edge pair extends to a perfect matching in exactly3 ways on the remaining four points. Hence

    sum_k binom(k,2) N_k=3*55=165,
    6*8+3a+b=165,
    3a+b=117.

Subtracting gives a=28,b=33. Thus

    (N_0,N_1,N_2,N_3,N_4)=(8,28,33,28,8).

As a consistency anchor, the first moment is210, equal to14 times15, since each rook edge extends to15 matchings on the other six points.

Assigning four pair labels and orientations multiplies by384, and the literal second-grid point stabilizer has order8, so each raw-matching class contributes48 distinct character tables. The5040 second cores split by k as

    (384,1344,1584,1344,384).

These are literal discrete input tables of ONE fixed-first-core/oriented-rho route, not separate quantum existence problems, discoveries or18-slot targets. The positive/negative signature closure now covers the two extreme classes in writing; the remaining classes are not called phase-feasible or low-rank merely because this argument does not close them.

The prepared source/request are unchanged and unexecuted. No skipped input, counter rewrite, GO, control pass or runtime/verification promotion is implied by this coverage calculation. Other first orientations, other conference classes, nonuniform arrays and unrestricted maximal1-RQLS(10) remain uncovered.
