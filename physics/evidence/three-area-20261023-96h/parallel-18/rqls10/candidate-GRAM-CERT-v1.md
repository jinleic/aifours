# GRAM-CERT v1 — unrestricted exact certificate protocol for maximal 1-RQLS(10)

Before-creation clock actually observed: **2026-10-23T14:06:42-07:00**. Author PhysicsRQLS10. Frozen target: `selection-v1.md`; dependencies: `baseline-dependency-freeze-v1.json`.

**Status: CANDIDATE / PARTIAL, written research.** This gives an exact equivalence and a complete *type* of certificate in either direction. It supplies **neither an order-10 witness nor an infeasibility identity**. It is not a claimed discovery, executable checker, completed computational search, formal proof or solution of the open target. No scientific program was executed.

## 1. Exact Gram formulation, without an ansatz

Let `P=[10]×[10]` be the 100 cells, ordered row-major. For any Latin square B define `E_B` to be the set of unordered distinct cell pairs sharing a row, column, or B-symbol. The three relations are disjoint on distinct pairs: a pair sharing a row or column cannot also share a B-symbol, by Latinity. Hence `|E_B|=30*binom(10,2)=1350` and there are 3600 remaining unordered pairs.

### Theorem G (all B, all complex vectors)

A maximal-cardinality 1-RQLS(10) exists if and only if there are a Latin B and a 100×100 matrix G satisfying:

1. `G=G*` and `G_pp=1` for every p;
2. `G_pq=0` for `{p,q}∈E_B`;
3. `G²=10G`;
4. `D_pq:=1-|G_pq|²>0` for all `p≠q` (only the 3600 pairs outside E_B need be checked).

No separate positive-semidefinite or rank constraint is omitted: they follow from 1 and 3.

**Proof, forward.** Put the 100 unit vectors in the columns of a 10×100 matrix V. Each of the ten rows of the square is an ONB, so `VV*=10I_10`. Thus `G=V*V` is Hermitian, has diagonal 1 and the required zero entries, and `G²=V*(VV*)V=10G`. For unit vectors, equality in Cauchy–Schwarz says `|G_pq|=1` exactly when their rays agree. Maximal cardinality is therefore condition 4.

**Proof, backward.** Since G is Hermitian, its eigenvalues are real. Equation 3 forces each eigenvalue to be 0 or 10. Its trace is 100 by condition 1, so exactly ten eigenvalues are 10. Therefore G is positive semidefinite of rank ten, and admits a factorization `G=V*V` with V of size 10×100. Diagonal 1 gives unit columns. On every row, column or B-class, condition 2 gives ten mutually orthogonal unit vectors in a ten-dimensional space, hence an ONB. Condition 4 excludes every repeated ray. These are exactly the original predicates. QED.

### Explicit extraction from G: no square roots or larger field required

Let `R={(0,0),...,(0,9)}` be the first row. Its principal submatrix is `G_RR=I_10`. In the R/complement order write

    G = [ I    X  ]
        [ X*   Y  ].

Block elimination by invertible triangular matrices gives `rank(G)=10+rank(Y-X*X)`. Thus Theorem G implies `Y=X*X`. Consequently the ten coordinates

    q_p(k) := G_((0,k),p),  k=0,...,9,

give `V=[I X]` with `V*V=G` **exactly**, and `q_(0,j)=e_j`. This is a proved first-row normalization, not a flat-coordinate hypothesis. If all real and imaginary parts of G lie in a number field K contained in R, the extracted vectors lie in K(i) with no extra square-root extension.

Conversely, starting with an arbitrary witness, the common unitary taking its first row to the standard basis produces precisely these coordinates. Neither B nor the off-first-row amplitudes are restricted.

## 2. A single rational polynomial system covering every B

This section avoids the missing coverage step that would arise from certifying only a chosen Latin square. It is an explicit finite defining schema, not a generated or executed system.

Real variables:

- `b_(i,j,s)` for i,j,s in [10];
- `a_pq,c_pq` for p<q, with `G_pp=1`, `G_pq=a_pq+i c_pq`, `G_qp=a_pq-i c_pq`;
- `z_pq` for p<q.

Let the following real polynomials be the list F. Any complex equality below means its real and imaginary parts, obtained by the displayed substitution; all coefficients are integers.

**L — exact Latin encoding**

    b_(i,j,s)^2-b_(i,j,s)=0,
    sum_s b_(i,j,s)-1=0,                 for every i,j,
    sum_j b_(i,j,s)-1=0,                 for every i,s,
    sum_i b_(i,j,s)-1=0,                 for every j,s.

Over R, the first equations make every b exactly 0 or 1. The remaining equations make exactly one symbol per cell and exactly one copy per row and column. Thus they encode precisely all Latin squares. No isotopy classification or coverage enumeration is imported.

**O — the exact required orthogonalities**

    G_pq=0                              if p,q share a row or column,
    b_(p,s) b_(q,s) G_pq=0              for every p<q and every s.

Here `b_(p,s)=b_(i,j,s)` for p=(i,j). At a real solution of L the second group enforces zero inner product exactly when the two cells carry the same symbol; its other instances impose nothing. Extra orthogonalities are allowed.

**T — tight-frame/rank equation**

    sum_r G_pr G_rq - 10 G_pq = 0        for all p,q.

Because Hermiticity and diagonal 1 are built into G, T forces positive semidefiniteness and rank ten by the spectral proof above. A complex symmetric matrix without conjugation is not a substitute.

**S — saturation by exact ray noncoincidence**

    z_pq (1-a_pq^2-c_pq^2)-1=0          for every p<q.

At a real solution of T, `1-a²-c²≥0` by the positive-semidefinite 2×2 principal minor (or Cauchy–Schwarz in the proved Gram factor). S makes this quantity nonzero, therefore strictly positive. Conversely, if it is strictly positive, the real value `z_pq=1/(1-a²-c²)` satisfies S. No sign assumption on z is needed. On E_B one has D=1 and z=1 automatically.

### Corollary GS (literal unrestricted equivalence)

The real zero set of the entire rational system F=L∪O∪T∪S is nonempty **if and only if** the owner’s unrestricted order-10 target has a witness.

**Proof.** The forward implication reads B from L and applies Theorem G; O supplies exactly its required edge zeros and S supplies its strict ray conditions. The reverse implication takes the target Gram matrix, the b indicator table and the reciprocals just displayed. QED.

S is essential. Removing it reopens the repeated-ray classical solutions whenever B has a classical mate. Dropping T would retain nonphysical positive-semidefinite moment relaxations; the companion `candidate-PROJECTOR-INVARIANT-v1.md` explicitly diagnoses that gap.

## 3. Positive certificate protocol is complete beyond cyclotomic fields

### Theorem A (algebraic witness suffices, conditionally on a witness existing)

If any complex order-10 witness exists, there is one whose real and imaginary coordinates are real algebraic numbers. They lie in one finite real number field K, and a Gram certificate over K(i) suffices.

**Proof.** Existence of a real zero of F is an existential first-order sentence with rational coefficients. The real algebraic numbers `R_alg=R∩Qbar` form a real closed field (Netzer Example 1.4.8). Both R and R_alg induce the unique ordering on Q. Tarski–Seidenberg transfer (Netzer Theorem 1.5.18, Example 1.5.19) transfers existence to R_alg. F has finitely many variables, so the algebraic coordinates generate a finite extension K/Q contained in R. The explicit first-row extraction above produces the desired vectors in K(i). QED.

This theorem does **not** assert that every actual witness has algebraic coordinates, a bounded algebraic degree, or cyclotomic coordinates. The old `Q(zeta_N)` format remains a useful sufficient special case, not an exhaustive search universe.

A positive exact certificate must contain:

1. `n=10`; B as a literal 10×10 integer table, not a generator assertion alone;
2. one primitive real algebraic element θ for K, its defining irreducible polynomial in Z[t], and a rational isolating interval identifying the intended real root;
3. every real and imaginary part of G as a rational polynomial in θ, with explicit nonzero rational denominators, in a fixed row-major serialization;
4. exact equation checks for Hermiticity, diagonal 1, every edge zero and `G²=10G`; exact positive signs for every nonedge D, using the isolated embedding;
5. the extracted vector array `q_p(k)=G_((0,k),p)` or its deterministic extraction rule, checked again directly against all 30 bases and all 4950 ray pairs.

The primitive-element theorem is the standard characteristic-zero algebra import. Root isolation/sign testing can use exact Sturm procedures; decimal evaluation or a tiny residual does not establish any equality or strict sign. Every serialized entry must be accounted for; malformed, duplicate, missing or extra cells are rejected. A checker must be independently authored from the original definition, not merely rerun producer algebra.

A simple *field-arithmetic* positive control for a future general algebraic parser is available in writing. Let θ be the unique root in (1,2) of `t³-t-1`. The rational function matrix

    U = 1/(1+θ²) * [ 1-θ²   -2θ  ]
                    [  2θ    1-θ²]

is exactly real orthogonal, since `(1-θ²)²+4θ²=(1+θ²)²` and the cross term cancels. The polynomial is irreducible over Q by the rational-root test. This control exercises algebraic coordinates beyond simply hard-coding roots of unity; it is **not** a QLS(10) witness or a claim that the target needs this field. This control has not been executed.

## 4. Negative certificate protocol is also complete in principle

### Theorem N (rational real-Nullstellensatz alternative)

Exactly one of the following can occur:

- F has a real algebraic solution (a positive target certificate as above exists); or
- there are finitely many rational polynomials h_j and A_ν for which the following **formal polynomial identity** holds:

    -1 = sum_j h_j(x)^2 + sum_ν A_ν(x) F_ν(x).                 (N)

No degree, coefficient-height or runtime bound is claimed.

**Soundness.** Evaluating (N) at any real common zero of F would give `-1=sum h_j²≥0`, impossible. Since F encodes all B simultaneously, a valid identity for this F excludes the unrestricted target, not just a selected resolution.

**Completeness and rationality.** Suppose F has no real zero. Let `A=Q[x]/(F)`. If -1 were not a sum of squares in A, the sum-of-squares cone would be a proper preordering. The abstract ordering-extension theorem (Netzer Proposition 3.2.1, or the abstract real Nullstellensatz, Theorem 3.2.4, applied to the quotient) supplies a real prime/order quotient and then an ordered field containing Q in which the coordinate classes solve F. Pass to its real closure. Transfer to R, using the unique ordering on Q, contradicts the supposed absence of a real solution. Thus `-1=sum h_j²` in A. Lifting the finitely many h_j to Q[x] gives (N), with rational ideal multipliers by the definition of the finitely generated ideal. This proves rational certificates, rather than silently assuming one can round a real-coefficient SOS certificate. QED.

A submitted negative certificate must identify the exact F schema/version, list every monomial and rational coefficient of h_j and A_ν, and verify (N) coefficient-by-coefficient after exact expansion. A solver's infeasibility flag, finite degree-search failure, numerical PSD Gram matrix or samples at finitely many parameter values is not such a certificate. If a sparse or symmetry quotient is used by a producer, a direct expansion back to the full original F must still establish the identity, with its coverage bridge independently reconstructed.

This is a genuine exact-certificate *protocol*, not a promise that an affordable generic SOS search will find a certificate. No such search is proposed or justified here.

## 5. Verification boundary and required controls

Before any checker execution, parent admission must bind actual source/input hashes, controls, resources and settlement; the current written protocol itself grants no GO.

Planned—not exercised—controls:

- Positive physical anchor: Zhang–Cao Example 2.4 at n=8, using the actual designated transversals and exact 64-ray data.
- Cardinality negative: the old classical control must pass all line predicates but fail saturation/nonparallelism, rather than being accepted as maximal.
- ONB negative: the published phase mutation must fail a named exact line equation; unit-norm perturbation must fail a norm/diagonal predicate.
- Latin negative: duplicate/missing B symbol must fail Latinity before a claimed transversal interpretation is accepted.
- Algebraic-format negatives: nonisolating or root-free interval, invalid denominator, extra or omitted entries must fail their intended parser/field checks.
- Negative-certificate module: `F={x²+1}` has exact refutation `-1=x²-(x²+1)`; changing its constant to -1 gives real solutions and the same alleged identity must fail exact coefficient comparison.
- A negative certificate scoped to one B is explicitly rejected as an unrestricted proof unless a separate exhaustive all-B coverage certificate is supplied. The single all-B F avoids that coverage dependency.

No present checker PASS, formal/kernel verdict, independent reconstruction, human review or priority verdict is claimed. Known projection/algebraic-variety reformulations are acknowledged below. This protocol earns no solved-target count.

## 6. Imports and prior-art limits

- Zhang–Cao [2608.29201v2](https://arxiv.org/html/2608.29201v2), Definition 1.1, Lemma 2.2 and §5: exact target and current named order-10 exception. The target still remains open here.
- Huang–Li [2606.27758v1](https://arxiv.org/html/2606.27758v1): exact cardinality means rays, not differently phased copies.
- Ion Nechita, [author exposition, 23 August 2016](https://ion.nechita.net/2016/08/23/bipartite-unitary-operators-and-quantum-latin-squares/): QLS are already explicitly described as a real algebraic variety. That general observation is prior art, not a contribution claimed here.
- Nechita–Pillet, [SudoQ, QIC 21 (2021), pp.781–799](https://www.rintonpress.com/xxqic21/qic-21-910/0781-0799.pdf), §2 Definitions 1–3 and Lemmas 1–2: general constraint lists of rank-one projections with identity sums. Again prior art.
- Tim Netzer, [Real Algebra and Geometry](https://www.uibk.ac.at/media/filer_public/28/02/280225fd-dde6-4e9c-bff6-baad33ff4a05/ragen.pdf), Example 1.4.8, Theorem 1.5.18/Example 1.5.19, Proposition 3.2.1 and Theorem 3.2.4. These exact bodies were read. Theorems A/N import these classical results; they are not new real algebraic geometry.
- Michałek–Sturmfels, [Invitation to Nonlinear Algebra](https://math.berkeley.edu/~bernd/gsm211.pdf), Theorem 6.12, independently confirms the real-coefficient weak real Nullstellensatz; its statement alone is not used to justify rational rounding.

The substantive deliverable is the scope-complete order-10 interface, its proofs, and the explicit real/ray/all-B safeguards, not scientific priority of Gram or SOS methods. A bounded literature search cannot clear novelty of even this application.
