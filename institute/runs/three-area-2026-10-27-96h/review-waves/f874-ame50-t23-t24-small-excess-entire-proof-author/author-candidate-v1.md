# N=50: actual t=23 and t=24 low-excess exclusions

**Status: prospective author candidate, not a parent disposition or accepted review.** This is a self-contained written reconstruction for exactly the two branches below. It uses one actual unitary flattening and allows arbitrary complex entries; it does not assume a global bound on t, a no-OLS result, any finite enumeration, or a phase ansatz.

## Statement and quantifiers

Let |ψ⟩ be any normalized complex AME(4,6) state, and choose any fixed local orthonormal product basis. Write its coefficients as ψ_abcd and let N be the number of their nonzero values. Define t to be the number of coefficients for which |6ψ_abcd|=1. Then neither **(N,t)=(50,23)** nor **(N,t)=(50,24)** occurs.

All references to rows, columns, components and degrees in the proof are to the actual complex matrix of this same tensor, not merely to a graph satisfying an independently posited combinatorial condition. The three balanced flattenings are not assumed jointly realizable on abstract data; only the AB|CD flattening is needed.

## 1. Actual residual unitary and component bookkeeping

Let M be the 36×36 AB|CD coefficient matrix and U=6M. The AME condition gives MM* = I_36/36, hence UU*=I_36; because U is square, U is unitary on both sides. Flattening reindexes the coefficients, so U has exactly N nonzeros and exactly t entries of modulus one. Each entry of U has modulus at most one.

If |U_rc|=1, the norm-one row and norm-one column containing it have no other nonzero entry. Two different modulus-one entries therefore have distinct rows and distinct columns, and each is an isolated 1×1 unitary block. Delete precisely those t rows and t columns. No other nonzero is deleted: the remaining matrix V is a square unitary of order

    n = 36−t,
    E = N−t,
    e = E−2n = N+t−72,

where E is its actual number of nonzeros. Every row and column of V has degree at least two. Indeed, a zero line contradicts unitarity; a degree-one line has its sole entry of modulus one, which would already have been deleted. This also excludes a hidden saturated 1×1 component in V.

Form the bipartite nonzero-support graph of V. After independent row and column permutations, the components are disjoint blocks. If a component has p rows and q columns, its block B satisfies BB*=I_p and B*B=I_q, since the other components supply no nonzeros on those rows or columns. Its rank is both p and q, so p=q=:m. In particular no non-square component may be used to evade the parity argument. Let its number of nonzeros be E_c and its excess be e_c=E_c−2m. Since every line has degree at least two,

    e_c = Σ_rows (degree−2) = Σ_columns (degree−2) ≥ 0,
    Σ_c e_c = e,        Σ_c m_c = n.                         (1)

The sums and degrees are integers. A component of order one is impossible. At order two, minimum degree two forces the full 2×2 support, and its excess is zero.

## 2. Complex-unitary twin/isolation bound

We now derive the load-bearing local bound, including the isolation step; no graph-only replacement is being assumed. Consider a connected component of order m>2, and let k be its number of degree-two rows.

* If a row r has support {a,b}, then the column supports of a and b coincide. For any other row s, orthogonality to r is

      U_ra conjugate(U_sa) + U_rb conjugate(U_sb) = 0.

  Because U_ra and U_rb are both nonzero, U_sa is zero if and only if U_sb is zero. This conclusion uses arbitrary complex numbers and is not a sign or equal-modulus assumption.
* Their common support has size at least two by the residual minimum-degree condition. If it had size exactly two, the two unit-norm orthogonal columns a,b would be an orthonormal basis of the coordinate plane on those two rows. Every other column is orthogonal to both, hence is zero on both rows. The component would be an isolated full 2×2 unitary block, contradicting m>2. Thus each of a,b has degree at least three.
* Two degree-two rows cannot have supports intersecting in exactly one column: their inner product would be one nonzero complex term. If their supports are identical, their restrictions are two orthonormal vectors in C², so every other row has zero entries on those two columns. The two rows themselves have no entries outside the pair. They again form an isolated full 2×2 component, contrary to m>2. Consequently the column pairs associated with the k degree-two rows are pairwise disjoint.

Each such pair thus contributes at least 2 to the column excess. On the other hand every row not counted by k has degree at least three and contributes at least 1 to the row excess. Using (1),

    e_c ≥ 2k,       e_c ≥ m−k,
    m−e_c ≤ k ≤ floor(e_c/2),
    m ≤ e_c + floor(e_c/2).                                  (2)

These inequalities are necessary for the genuine complex unitary block, not asserted sufficient for unitary realization.

In particular, a connected zero-excess component is a full 2×2 block. Besides the order-two case above, an order m>2 component with e_c=0 would violate (2). Equivalently, its degree-two rows would have twin columns of degree two, isolating a 2×2 block. This handles the zero-excess boundary explicitly; it is not an arbitrary even cycle or a component of unchecked size. Also no component has excess one: at m=2 the excess is zero, while for m>2, (2) with e_c=1 requires m≤1. There is no m=1 residual component.

## 3. Exact t=23 branch

Suppose N=50 and t=23. Equation (1) applies to the order-13 residual unitary with E=27 nonzeros and total excess

    e = 27−2·13 = 1.

Every component excess is a nonnegative integer, and no component has excess one. Thus their sum cannot be one. This contradiction excludes the entire actual t=23 branch, regardless of the number of zero-excess 2×2 components or the phases of their entries. In particular, all-zero component excess would sum to zero, not one; there is no omitted zero-excess exception.

## 4. Exact t=24 branch and the odd remainder

Suppose N=50 and t=24. The residual unitary has order 12, E=26 nonzeros and total excess

    e = 26−2·12 = 2.

By nonnegativity and the absence of excess-one components, exactly one component has positive excess, and that excess is two. All other components have excess zero. For the positive component, m>2 and (2) gives m≤2+floor(2/2)=3. Hence m=3 and E_c=2m+2=8: its support is exactly a 3×3 matrix with one missing entry. In fact (2) forces k=1, consistent with the unique degree-two row; its unique degree-two column follows by transposition. No other m or split of the excess is possible.

The other components must all be full 2×2 blocks. They would have to cover 12−3=9 rows and 9 columns, an odd number. This is impossible. Therefore the entire actual t=24 branch is excluded.

The 3×3-minus-one mask itself is **not** being declared unrealizable. For example, this genuine unitary block has exactly that mask and no modulus-one entry:

       [ 0       1/√2    1/√2 ]
       [ 1/√2    1/2    −1/2  ].
       [ 1/√2   −1/2     1/2  ]

Its three row norms are one and their pairwise inner products are zero. The example is only a local illustration, not an AME tensor or a witness for any N=50 branch. The contradiction is the unavoidable odd nine-row remainder, not an illicit claim that the positive-excess block cannot exist. The zero-excess 2×2 blocks themselves may have arbitrary complex phases and nonzero moduli compatible with unitarity.

## 5. Imports, limits, and process declaration

The proof derives all load-bearing component claims above from the actual unitarity of the chosen flattening and elementary linear algebra. **No unavailable mathematical source body is used as a conditional import.** S1's broader proposed union, S2's other t branches and finite-search reporting, and S3's t=28 analysis are not premises of this proof. Their linked bodies, including the earlier named author/source/GO files, were not opened; their reported statuses are not independently checked here. In particular, no t≤28, no-OLS, minimum-support bound, support-50 witness, other t exclusion, global AME theorem, novelty/priority, publication, human, independent-family, or formal/kernel acceptance is asserted. Parent disposition and independent checks are separate.

Before any mathematical body read or reasoning, I read the frozen manifest, freeze receipt, final pre-dispatch binding, parent live metadata supply, actual-dispatch receipt, and **all 22** status-only controls listed in the manifest, and wrote `prebody-ack-v1.md` and sent the direct acknowledgment to Main. The controls were used only for permissions and exclusions, not as mathematical inputs. The parent metadata reports matching bindings; I did not independently hash the files.

After that acknowledgment I read the sole literal packet part completely and in order as raw windows **1–20, 21–40, 41–60, and 61–78**, including the ending. Each display was under 30,000 bytes because the entire part is 19,451 bytes according to the frozen parent metadata; no clipping or recovery was observed or needed. The packet contains the complete literal bodies S1 lines 1–12, S2 lines 1–33, and S3 lines 1–19. The supplied source pins are, respectively, `5aca1a1ed6d733dad4f17e2c24955829cc177056de57b751b86aaa8ccf7c88dd`, `9dcffb913663a29d438d53354e44aaacff0ba7cd0c5b37d4b803ea98936af336`, and `44a750bb54cf2736b7e170910e7172578587f9338f204b9ce4d450afbaf09619`; the parent-supplied packet pin is `d9eb81b19addd9dbc744c238a390888a90c83b437a6ff7f18a46b9c1840b092f`. These are supplied administrative identifiers, not independently recomputed hashes or correctness certificates.

I did not open held episodes or any of their proof/method/planning/selection/verification/reporting/confidence/downstream consumers, linked unlisted files, sibling mathematical work, or old code. I performed no network use, external-model call, child subprocess, scientific code execution, test, solver, compilation, scientific eval, or prepared-code run. No verifier code was prepared, so no prepared-code hash applies. No known process deviation or clipping occurred; this is not a certificate about unobservable prior cognition.
