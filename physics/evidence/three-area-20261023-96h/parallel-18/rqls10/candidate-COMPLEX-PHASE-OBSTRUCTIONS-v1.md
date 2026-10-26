# COMPLEX-PHASE v1 — two concrete complex construction routes are obstructed

Clock actually observed before creation: **2026-10-23T14:22:52-07:00**. PhysicsRQLS10, physics-5. Continuation scope: `complex-lift-scope-v1.md`, after Main's instruction to attack an actual complex lift rather than enlarge encoding/verification machinery.

**CANDIDATE WRITTEN PARTIAL.** These are actual analytic negative results for specified **complex** construction routes. They are not the earlier real-only no-lift and not a failure of numerical search. They do not cover arbitrary phases or all 1-RQLS(10). No scientific program, solver, enumeration, exact executable calculation, formal kernel or outside-model review was used.

## 1. Where a uniform-overlap complex construction has to start

Assume the equality-point route H0: the squared overlap is zero on required row/column/B-class pairs and 1/8 on every line-disjoint pair. This is an explicit ansatz, **not a normalization of the unrestricted target**.

Normalize the first row by one common unitary to `q_(0,j)=e_j`, and label the B-symbols so `B(0,j)=j`. For i>0, each vector q_(i,j) has zero coordinates j and B(i,j); these are different by Latinity. All other eight coordinates have modulus 1/sqrt8, because each remaining first-row cell shares no required line with it.

Fix i>0 and put the ten row vectors q_(i,j) as columns of U_i. The row ONB makes U_i unitary. Therefore

    W_i=sqrt8 U_i

is a **unit weighing matrix UW(10,8)**: its entries have modulus zero or one, every row/column has eight nonzeros, and `W_i W_i*=8I`. This condition is necessary for an H0 lift; it involves actual vector orthogonality, not just the feasible projector-Gram relaxation.

There is also an honest local positive baseline. Take any first-row line and a column line, which share one vector e_j. Removing it leaves two bases of its nine-dimensional orthogonal complement. Their transition matrix has one zero per row/column and eight entries of modulus1/sqrt8; after row/column permutation it is a normalized complex conference matrix of order9. **Such complex matrices exist.** Et-Taoui [1409.4282v1](https://arxiv.org/html/1409.4282v1), §2 Theorem2/Corollary3, gives entries `w^chi(x-y)` with

    w=(1+i sqrt7)/sqrt8,       Re(w²)=-3/4,
    C9 C9*=8I9.

The actual theorem and its explicit order9 example were read. Odd real conference nonexistence cannot be used against this complex baseline.

The issue is gluing such local transitions into the required ten-dimensional W_i and then the full array.

## 2. A nonreal two-phase UW(10,8) cannot exist

### Theorem W2

Let W be 10×10, with `WW*=8I`, and suppose that after arbitrary unitary row/column scalings and permutations every nonzero entry of W belongs to a fixed pair `{u,v}` of unimodular complex numbers. Then `v/u=-1`; in that gauge W is a real weighing matrix up to one common phase. In particular there is **no such W with v/u nonreal**.

This theorem permits arbitrary choices of the two phases; it does not discretize them as roots of unity.

**Proof.** The allowed monomial operations preserve the weighing condition. Divide by u, and write the two entries as 1 and z, |z|=1. If z=1, inner products between rows have at least six positive terms and cannot vanish. If z is real and distinct from1, then z=-1 and the stated conclusion already holds. It remains to rule out nonreal z.

Let Z_r be the two zero columns in row r. Column norms are eight too, because a square matrix with `WW*=8I` also has `W*W=8I`. Thus every column belongs to exactly two of the Z_r. For two different rows r,s, the number of common nonzero coordinates is

    m=10-|Z_r union Z_s|=6+|Z_r intersection Z_s|,

so m is 6,7 or8. Their inner product has the form

    n0+n+ z+n- conjugate(z)=0,

where n0 counts equal letters in the common support. Nonreality of z forces n+=n-=h>0. With c=Re z,

    n0+2hc=0,       m=n0+2h=2h(1-c).                    (W)

**A disjoint zero pair exists.** A fixed Z_r has two columns, each belonging to just one other row's zero set, so at most two other rows intersect Z_r. Among the other nine rows there is a disjoint one. Hence m=6 occurs and the corresponding positive integer h6 is at most3.

**No singly intersecting zero pair can exist.** If m=7 also occurred, (W) would give `6h7=7h6`. Coprimality forces h6 to be a positive multiple of6, contradicting h6≤3. Therefore any two zero sets are either disjoint or identical.

It follows that the ten zero sets consist of five disjoint two-element sets, each occurring in exactly two rows: any one occurrence uses one of each column's two allowed zeros, and the second occurrence must be the identical set because a single intersection is forbidden. Thus m=8 occurs within each pair of rows, while m=6 occurs between pairs.

Equation (W) now gives `6h8=8h6`, equivalently `3h8=4h6`. The bounds h6≤3,h8≤4 imply h6=3,h8=4, and then c=0 and n0=0 for every row pair from different zero-set blocks. Hence in **every shared nonzero column**, two rows from different blocks must use different letters.

Choose one row from each of three different blocks. Their zero sets are disjoint and occupy six columns, so they have four common nonzero columns. In any one of those columns three letters drawn from {1,z} cannot be pairwise different. This contradicts the previous paragraph for one of the three row pairs. Nonreal z is impossible. QED.

### Direct complex-lift consequence

An H0 construction cannot use a parallel-row transition W_i that is monomially equivalent to a two-valued **nonreal** phase matrix. In particular the tempting extension/gluing that retains only the Et-Taoui alphabet `{w,w^-1}` in one common row/column gauge is impossible, since `w²=(-3+i sqrt7)/4` is nonreal.

This is a genuine complex obstruction. It does **not** exclude using the conference matrix locally with independent compatibility phases, a three-or-more-value alphabet, or different phase alphabets in different columns. Nor does separately rephasing different W_i to real matrices make the full array globally real. Those loopholes are mathematical missing cases, not presumed harmless gauges.

## 3. An exact non-Butson Paley-core QLS construction, and why its full equivalence class has no resolution

The same complex-conference route suggests bordering its finite-field core to obtain Hadamard-product squares without the old quaternary alphabet. This section actually constructs the underlying ordinary QLS family and then rules out every orthonormal transversal in it.

Let F=GF(9), Omega={infinity} union F, and let chi be its quadratic character, with chi(0)=0. Put

    Q_ab=chi(a-b),  a,b in F.

Then Q is real symmetric, `Q1=0`, and `Q²=9I-J`.

**Elementary proof of the last identity.** The diagonal is eight. For a≠b, rescaling and translating reduces the entry to `sum_t chi(t(t-1))`. Count pairs (t,y) with `y²=t(t-1)`: the invertible change `A=2t-1-2y`, `B=2t-1+2y` identifies them with `AB=1`, of which there are eight. The same number equals `9+sum_t chi(t(t-1))`, so the character sum is -1. Symmetry uses chi(-1)=1, and zero row sums use equally many nonzero squares and nonsquares. QED.

Define

    z=(-1+i sqrt15)/4,              z+z^-1=-1/2,
    K=(5I-J+i sqrt15 Q)/4,
    H=[1   1^T]
      [1    K ].

Thus H's first row and first column are all1, its finite diagonal entries are1, and its finite off-diagonal entries are `z^chi(a-b)`.

### Lemma H (exact ordinary QLS baseline)

H is a complex Hadamard matrix: every entry is unimodular and `HH*=10I`.

**Proof.** The entry description and |z|=1 show unimodularity. `K1=-1`. Since Q commutes with J and `QJ=0`,

    KK* = ((5I-J)^2+15Q²)/16
        = (25I-10J+9J+135I-15J)/16
        = 10I-J.

Bordering therefore gives exactly `HH*=10I`. QED.

This is not a claimed new Hadamard matrix. A public Hadamard-catalogue search located the same parameter; direct catalogue retrieval failed certificate verification and the returned GitHub mirror path was404, so no equivalence to a specifically named catalogue representative is imported. The displayed matrix is proved directly. The complex-conference finite-field core is prior art. Also z is not a root of unity: otherwise the rational number `z+z^-1=-1/2` would be an algebraic integer and hence an integer, contradiction.

For any coordinate permutation pi of Omega, form

    q_ij(t)=H_i(t) H_j(pi(t))/sqrt10.                     (P)

Every row and every column of this array is an exact ONB: multiplication by a fixed unimodular row is a diagonal unitary, and H's rows are orthogonal. The family permits arbitrary row/column phases and row/column permutations of either Hadamard factor as well. Such phases become independent cell phases and one common diagonal unitary of (P), so they do not affect existence of an orthonormal transversal.

### Theorem P15 (complex non-Butson product no-go)

For **every** coordinate permutation pi and **every** cell transversal `{(i,sigma(i)):i∈Omega}` with sigma a permutation, the ten vectors (P) are not an ONB. Consequently **no Latin resolution B at all** turns (P) into a1-RQLS(10), of any cardinality. The conclusion covers the whole Hadamard monomial-equivalence class of each factor.

**Proof, step1: a vanishing-sum congruence for z.** The primitive irreducible polynomial of z is

    M(T)=2T²+T+2.

If `sum_(t=1)^10 z^d_t=0`, d_t integers, multiply by a large enough power of T to obtain an integer polynomial F(T) vanishing at z. By Gauss's lemma the primitive M divides F in Z[T]. Since `M(-1)=3`,

    sum_t (-1)^d_t = 0 mod3.

If w of the ten exponents are odd, this says `10-2w=0 mod3`, equivalently

    w in {2,5,8}.                                        (V)

Hence orthogonal power-of-z coordinate vectors must have exponent-parity patterns at Hamming distance2,5 or8. This is an exact complex-field consequence, not an assumption that phases are real.

**Step2: express every transversal's parity patterns without fixing pi or sigma.** Work over F2, let e_a be the coordinate singleton at a∈Omega, let 1 denote the all-ones binary vector, and let epsilon_i=0 for i=infinity and1 otherwise. The exponent-parity vector of row i of H is exactly

    tau_i=e_infinity+e_i+epsilon_i 1.

For the second factor after coordinate permutation, its row j parity is

    tau'_j=e_v+e_(pi^-1(j))+epsilon_j 1,
    v=pi^-1(infinity).

Therefore the vector in transversal cell (i,sigma(i)) has parity

    x_i=e_infinity+e_v+e_i+e_(rho(i))
             +(epsilon_i+epsilon_(sigma(i)))1,
    rho=pi^-1 composed with sigma.

Translate all x_i by the same binary vector `e_infinity+e_v`, and complement individual x_i when their final coefficient of1 is1. The resulting patterns are

    y_i=e_i+e_(rho(i)).                                  (Y)

A common translation preserves Hamming distance, and complementing one of a pair replaces a distance w by10-w. The allowed set {2,5,8} in (V) is closed under that replacement. Thus if the class were orthogonal, all distinct y_i,y_j would still have distances in {2,5,8}.

**Step3: a permutation-edge counting contradiction.** Each y_i has weight zero or2, so each pairwise distance is even and at most4. Consequently every one of the45 pairs would have distance exactly2, making their total Hamming distance90.

Let m be the number of nonfixed points of rho. A fixed coordinate a occurs in zero of the y_i. A nonfixed coordinate a occurs in exactly two, namely y_a and y_(rho^-1(a)). Summing pairwise Hamming distances by coordinates therefore gives

    total = m*2*(10-2)=16m.

The equality `16m=90` is impossible for an integer m. Thus the ten class vectors cannot all be mutually orthogonal. This applies to arbitrary pi and sigma. No transversal, and therefore no full resolution, exists. QED.

### Exact relationship to the previous baseline

The old R9 result concerns `H=I+iC10` with quaternary entries and a mod4 phase-parity argument. P15 instead concerns the displayed non-root-of-unity z/H, and uses its minimal polynomial evaluated at-1 modulo3. No R9 conclusion is imported as a premise. R10 fixes one factor to the quaternary Paley class and takes the other in an i-free field; neither factor is fixed to that old class in P15. Thus this is not simply calling the old floating Paley miss UNSAT. It is another **scoped** exact obstruction, not an unrestricted QLS10 theorem or priority claim.

## 4. Consequence and remaining single obligation

The attempted complex route now has actual limits:

- Local complex conference9 bases are feasible by prior art, so odd-real parity cannot end the analysis.
- Direct two-valued nonreal gluing cannot even produce the necessary UW(10,8) transition, by W2.
- The non-Butson Paley-core bordering family produces exact ordinary QLS(10), but its entire coordinate/monomial product family has **not one orthonormal transversal**, by P15.

Neither result fixes flat coordinates for the unrestricted problem. W2 is applied only under the explicitly stated H0/two-phase route; P15 only to the fully written Hadamard-product family. No 100-ray witness, H0-wide no-go, arbitrary-Hadamard no-go or unrestricted impossibility is claimed.

The next same-problem obligation is the actual independent-phase gluing of the complex conference9 cores: does the freedom to put separate diagonal compatibility phases on their coordinate directions overcome W2 while satisfying the row bases and third-direction bases? Alternatively a materially different non-product construction is needed. Repeating either excluded two-valued or same-H product construction is no longer justified. No numerical search or scientific executable is requested or authorized by this file.

## 5. Source and verification boundary

Primary texts actually read:

- Et-Taoui [arXiv:1409.4282v1](https://arxiv.org/html/1409.4282v1), §2 Theorem2/Corollary3 and the order9 example: local complex conference baseline. Its general construction is not a new result of this round.
- Best–Kharaghani–Ramp [arXiv:1307.8161](https://arxiv.org/pdf/1307.8161), definitions of unit weighing/unbiased matrices and general bounds. Their real perfect-square weight lemma is explicitly real-only and was not misapplied to complex phases.
- The exact old R9/R10 files in `physics/evidence/six-lane-20261016/rqls10-maximal/restricted-results-addendum-{4,6}.md`: compared at their actual scope.
- Zhang–Cao [2608.29201v2](https://arxiv.org/html/2608.29201v2): the unchanged original row/column/resolution/ray target.

W2 and P15 are complete author-written candidate arguments requiring a separate actual reconstruction and parent check at pinned bytes. No claim of novelty, kernel verification, human review or completed scientific execution. The existing eighteen-slot target remains UNKNOWN.
