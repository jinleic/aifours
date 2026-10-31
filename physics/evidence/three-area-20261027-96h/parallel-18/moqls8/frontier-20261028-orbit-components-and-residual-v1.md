# Classical solution components and a quantitative near-seed residual bound

**PhysicsMOQLS8-2 / physics-4. WRITTEN AUTHOR CANDIDATE with one EXACT rational diagnostic; awaiting independent review.** This is an additive strengthening of `frontier-20261028-uniform-classical-neighborhood-v1.md`, SHA256 **12d8a6e3e3c27ff0e5c776a196578a94ed1010f907986680ef74c0e7f42eb8aa**, not an edit of that packet. It does not settle the unrestricted order8 four-family question.

## 1. Definitions and previously established candidate used here

Fix n,m with `n≥2` and `2(m+1)>n`. Let X be the set of ALL labelled actual m-MOQLS(n) families, considered as tuples of PROJECTIVE rays at the n² cells of each member. A member-specific global output unitary acts simultaneously on its n² rays; per-cell phases are already quotiented out. The actual model retains each row/column ONB and each member-pair product ONB.

For projective rays define `d([v],[w])=sqrt(1−|<v,w>|²)` and use the maximum over all members/cells. This is a metric: it is the Frobenius distance of the two rank-one projections divided by sqrt2.

The previous candidate proves from first principles: for ANY actual classical reference C and ANY actual Q∈X,

    d_infinity(Q,C) ≤ η_n := 1/[8n(n+1)]  ==>  Q is obtained from C
    by member-specific output unitaries and per-cell phases.      (A)

Its proof uses a simple `(m+1)`-regular bipartite graph on occurrences of each pair of classical symbols, the >n/2 neighbor-intersection bound, and ACTUAL zero products. The source and proof are pinned above; no old held input is used.

## 2. Every classical orbit is an entire connected component

For any classical C, let O(C) be its orbit under `U(n)^m` on the output frames. **Claim:** O(C) is both open and closed in X and is path connected. Consequently it is exactly the connected component of X containing C.

**Closed.** `U(n)^m` is compact, and its orbit map to the finite product of projective spaces is continuous. Hence O(C) is compact and closed. No phase choices are required in projective space.

**Open.** For every C' in O(C), the same theorem (A), with C' as reference, says that all actual families at d_infinity≤η_n lie in O(C'). But O(C')=O(C). Thus each C' has a relative neighborhood in X contained in O(C). This uses a UNIFORM radius and fixes the labelled classical occurrence pattern; it does not assume the whole space X is a manifold.

**Path connected.** Every unitary has a spectral decomposition `V diag(exp(iθ_j)) V*`; the path `V diag(exp(itθ_j)) V*` joins I to it. Apply these paths independently in all m members. The orbit is the continuous path-connected image of `U(n)^m`.

Any connected subset of X containing C cannot meet the complement of the clopen orbit. Since the orbit itself is connected, it is the entire connected component. Therefore no continuous path of actual families can start at a classical family and finish at a nonclassical one, even if its intermediate states move far from the STARTING coordinates. This is a topological consequence, NOT an assumption that all actual families are path connected.

At n8,m4 each actual classical orbit is a connected component; a nonclassical component could still exist. No cardinality, novelty, uniqueness of a classical Latin pattern, or global classicality is inferred.

## 3. Distinct classical occurrence patterns are separated

For a classical member its occurrence partition declares two cells equivalent iff their rays agree. These equivalence relations, over all m members, are invariant under output unitaries and characterize the classical orbit: if two classical tuples have the same relations, map each member's ONB rays to the corresponding other ONB by a unitary.

For ANY TWO different classical orbits, some member has cells x,y with the same reference ray v in one tuple and two orthogonal rays u,w in the other (or with the roles reversed). Bessel's inequality gives

    |<v,u>|²+|<v,w>|²≤1.

If the maximum per-cell projective distance of the two labelled tuples were <1/sqrt2, both squared overlaps would exceed1/2, a contradiction. Thus their distance is at least1/sqrt2. This is an exact all-pairs statement, independent of the small η_n bound; it does not claim this bound is attained for a given pair of actual classical families.

The occurrence-pattern statement is discrete and intrinsic: different names for the same classical basis rays are not different orbits. Simultaneous grid relabellings are only reindexings if applied to BOTH families; no independent row/column permutation of members is silently allowed.

## 4. Approximate families: exact full-Gram residual controls distance from a fixed seed

This section applies to arbitrary **unit** vector arrays, not necessarily valid MOQLS. Fix an actual classical reference C as in §1 and align the first row of each candidate member EXACTLY with its reference first row. This alignment is an assumption here; a generic numerical candidate with a nonunitary first row cannot be silently aligned by a unitary. Rephase remaining cells so the reference coordinate is positive. Suppose the maximum norm δ of all off-reference-coordinate components is ≤1/(4n).

Define the full physical residuals

    r = max over all members and distinct same-row or same-column cells
        |<Q_a(x), Q_a(y)>|,
    s = max over all distinct members and all distinct cell pairs x,y
        |<Q_a(x),Q_a(y)> <Q_b(x),Q_b(y)>|,
    R = max(r,s).

For unit vectors, vanishing r and s is exactly the full row/column and pair-product Gram condition; the proper number of orthogonal unit vectors then gives each complete ONB. If m=1 there are no distinct-member pairs and s is defined to be0. No sampled subset is used in the definition.

For any edge of the reference symbol-pair graph in previous §3, the selected-member overlap is at most r on a row/column edge. On a companion-symbol edge, the companion overlap is at least `1−2δ²`, so the selected overlap is at most `s/(1−2δ²)`. Put

    e=max{r, s/(1−2δ²)}.

Exactly the coefficient expansion of previous §6, now with an edge residual, gives potential differences at most `e+δ²(1+2δ)`. Same-side graph distance≤2 from the first-row anchors yields

    δ ≤ 2 sqrt(n−1) [ e+δ²(1+2δ) ].                            (B)

Using `sqrt(n−1)≤n` and `δ≤1/(4n)` gives

    e ≥ δ/(2n)−δ²(1+2δ)
      ≥ δ[1/(4n)−1/(8n²)] ≥ 3δ/(16n).

Since `e≤R/(1−2δ²)` and `1−2δ²≥1/2`, the fully explicit bound is

    R ≥ 3δ/(32n).                                                 (C)

It holds also at δ=0, where it says only R≥0. Thus a near-seed numerical array with first-row anchor and FULL physical Gram residual R can have leakage at most `(32n/3)R`. For an exact actual family R=0 this recovers δ=0. The bounds are invariant under the earlier member-global unitary and per-cell phases, but the fixed-reference leakage δ is evaluated AFTER alignment.

**Limit:** a small finite-precision residual is not an exact witness, and (C) applies only inside the explicitly stated anchored neighborhood. It supplies neither a lower bound on residual far from C nor a solver-completeness/no-go certificate.

## 5. Executed exact rational diagnostic

New source: `frontier-20261028-nearby-residual-check-v1.py`, SHA256 **c75bda3fd2d4388e7bc1573a342ae1062209289fea71db75e8c9b6d2b123f2c6**.
Output receipt: `frontier-20261028-nearby-residual-receipt-v1.json`, SHA256 **7112dbffa0b24c64f1239b0752725852b871610bf75c25ef1fc65194289fc5ec**.

Executed once, bounded:

    python3 -B frontier-20261028-nearby-residual-check-v1.py \
      --input frontier-20261028-classical-boundary-receipt-v1.json \
      --output frontier-20261028-nearby-residual-receipt-v1.json

It hash-checks the previously generated classical GF(8) table receipt, constructs a deliberately INVALID near-classical real-vector perturbation at one non-first-row cell using exact rational unit-circle coefficients, and verifies ALL cells unit and all first-row anchors unchanged. It checks ALL 4,096 row/column and 24,576 pair-product Gram entries. Observed exact values:

- `δ=512/65537`, first-row anchors exact and cell-norm errors0.
- Max row, column and pair-product off-diagonal residuals are each `512/65537`.
- Proven lower bound (C) is `6/65537`; the observed residual satisfies it exactly by rational comparison.
- The stronger direct bound from (B) was also compared exactly and satisfied; the full rational is in the receipt.

This is deliberately NOT an MOQLS witness: it has nonzero physical Gram residual. It tests implementation and illustrates (C) for one specific input, not the universal theorem. No floating rounding, solver, exhaustive quantum search or third independent verifier was used.

## 6. Scientific status and next step

(A)–(C) are WRITTEN candidates, conditional on the full prior proof being correct; no parent/peer/formal/kernel/novelty acceptance is inferred. The exact program result is only an observed single-input arithmetic check. The original unrestricted four-family problem remains OPEN: nonclassical families, if any, must be outside every classical component but are not ruled out. A genuinely nonperturbative search or uniform bridge is still needed; do not equate lack of a classical-connected path with nonexistence.
