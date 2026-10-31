# Uniform-overlap resolvable QLS: real and two-phase no-go mechanisms

**NEW WRITTEN AUTHOR CANDIDATE, unreviewed; exact finite checks and an explicit complex fragment.** Native `/bin/date` before writing: **Wed Oct 28 17:34:48 PDT 2026**. All theorems below concern a **hypothetical physical lift of the uniform overlap matrix** M_*; M_* itself is only a formal scalar relaxation. The uniform equality branch is NOT known to be WLOG for the original QLS10 target. No result below excludes nonuniform arrays or proves the unrestricted order-10 no-go.

## 1. Exact hypotheses and principal results

For n>=4, let an actual 1-resolvable QLS(n) consist of n² SAME labelled unit vectors in C^n, with row, column and transversal ONBs, such that the squared overlaps are1 on the diagonal,0 for distinct cells sharing any of those three blocks, and `1/(n-2)` for all remaining pairs. The incidence L ranges over ALL Latin resolutions. These conditions are the physical uniform-pattern M_* branch, not just the formal matrix.

**A. Universal row-support/conference condition.** Use ANY one row ONB as the coordinate basis. Every vector in that row is a standard basis ray. Every other cell has EXACTLY TWO zeros, at the two reference-row basis cells in its column and transversal, and all its other n−2 coordinates have squared modulus `1/(n-2)`. Each unordered pair of coordinate zeros appears in EXACTLY TWO of the n(n−1) remaining cells. Each column or transversal block intersecting the reference row yields a complex conference matrix of order n−1 (zero diagonal, unit-modulus offdiagonal, Gram `(n−2)I`) after removing its reference basis vector and multiplying the remaining entries by sqrt(n−2).

**B. All-even-order real no-go within this branch.** For EVERY EVEN n>=4, no such uniform-pattern array can be represented by real vectors in any common orthonormal basis, even allowing arbitrary per-cell phases before making the vectors real. In particular no real uniform physical lift exists at n=10, for ANY L.

**C. Order10 two-phase Paley-alphabet no-go.** At n=10, fix ANY reference row basis and let `omega` be a unit complex number with `Re(omega²)=-3/4`. Even after arbitrary per-cell phases and a common coordinate-diagonal unitary, it is IMPOSSIBLE that every nonzero coordinate of every nonreference vector belongs to the two-phase alphabet `{omega,conjugate(omega)}` times `1/sqrt(8)`. This excludes an entire natural attempt to glue order-9 GF(9) complex conference blocks across all three partitions; it does not exclude more general phase sets.

**D. Arbitrary-basis support constraint.** In any physical M_* lift and for EVERY unit vector e, at least `ceil(n²(n-2)/(2n-3))` of the n² rays have nonzero overlap with e. For n=10 this is48, so EVERY hyperplane contains at most52 of the rays. In every coordinate basis the total number of nonzero entries among the100 vectors is at least480; therefore at least14 vectors have support size at least5. The reference-row basis has the stronger exact total730 and pattern from A. None of these conditions asserts an actual uniform lift exists.

## 2. SAME-array support and zero-pair proof

Fix an arbitrary reference row R0 and choose its n labelled vectors as e_0,...,e_(n−1), indexed by their columns. Let x be ANY cell outside R0, in column i and transversal T. Its column meets R0 in e_i. Its transversal meets R0 in a second basis vector e_j. These two reference cells are distinct: if j=i, the transversal would contain two cells in column i, contradicting its definition. Thus the x-vector is orthogonal to e_i and e_j.

For every other reference-row cell e_k with k!=i,j, x shares neither row, column nor transversal with it, so the physical uniform hypothesis gives `|<e_k,psi_x>|²=1/(n−2)>0`. This establishes EXACTLY those two zeros and n−2 flat nonzero coordinates, with no assumed extra zeros.

Conversely, fix i!=j. There is exactly one cell outside R0 in column i and the transversal through e_j, since a transversal meets every column once and e_j is in column j. Its zeros are {i,j}. Similarly there is exactly one cell outside R0 in column j and the transversal through e_i. They are distinct because their columns differ. Every outside cell with zero pair {i,j} must be one of these two oriented cases. Hence each unordered pair occurs EXACTLY twice, for ALL L. The resulting total support in the reference-row basis is

`n + n(n−1)(n−2)`;

for n=10 this is `10+90*8=730`.

For a column block through e_i, its remaining n−1 vectors lie in e_i^perp. Their other zero coordinates are all distinct because their transversal labels are distinct down the column. Index them by those zero coordinates. On the remaining n−1 coordinates, multiplying by sqrt(n−2) gives a square matrix with zero diagonal and unit-modulus offdiagonal. Its columns are orthogonal with squared norm n−2, hence it is a complex conference matrix of order n−1. The same statement holds for a transversal block through e_i, using its other zero coordinates indexed by columns. This is a NECESSARY condition on each local block, not an assertion the many blocks can be chosen independently and glued.

## 3. Proof of the even-order real obstruction

Suppose n is even and a uniform lift can be made real in one common basis after cell phases. Its reference row is then a real ONB, and a real orthogonal change of coordinates sends it to the standard basis without losing realness. Choose ANY column and two distinct cells x,y outside R0 in that column; n>=4 ensures they exist. Their second zero positions are distinct because their transversal labels in the column are distinct.

Their supports therefore intersect in exactly `n−3` coordinates. Every nonzero coordinate of either vector is real of modulus `1/sqrt(n−2)`, so their inner product is a sum of exactly n−3 terms, each `+1/(n−2)` or `−1/(n−2)`. Since n is even, n−3 is ODD and this sum cannot be zero. But x,y belong to the SAME column ONB and must be orthogonal. Contradiction.

Equivalently a real conference matrix of odd order n−1 would have two distinct columns with an odd number n−3 of ±1 products, which cannot sum to zero. No assumption about an individual input phase is lost: all phase choices were allowed before declaring the array real in a common basis.

## 4. At least fourteen seven-overlap nonsharing partners at order10

Fix an arbitrary nonreference x with zero coordinates {i,j}, where x is in column i and in the transversal T_j through reference-row e_j. In the OTHER transversal T_i, there is exactly one cell in each column k. Excluding columns i and j leaves8 cells y, each with zero set {i,k} where k!=i,j. None shares a column or transversal with x. At most one is in x's row, because T_i meets a row once. Therefore at least7 have NO shared row/column/transversal with x and their two zero sets intersect exactly in {i}.

Similarly, use column j and exclude the cells in transversals T_i and T_j. Eight remaining cells have zero sets {j,k}, k!=i,j; none shares column or transversal with x, and at most one shares its row. This yields at least7 further nonsharing cells. The two sets are disjoint because a zero pair sharing exactly i cannot also share exactly j. Hence every nonreference x has at least **14** such nonsharing partners y. Their support intersection has `10-|{i,j,k}|=7` coordinates. The physical uniform condition requires their squared inner product to be exactly1/8.

This counting uses one actual Latin resolution, but L was arbitrary. An independent finite incidence checker `frontier-20261028-uniform-zero-incidence-v1.py`, SHA **f38f41f844d4e64e72e143a4f372c127be8d8824c8f9fa3aa0bdfa93a6cc8864**, checked all ten reference rows for both Weisner Fig.1 and Parker 1959: every unordered zero pair appears twice and the one-common-zero/nonsharing partner counts were14 or16 for all900 nonreference cells per table. That finite check is not the all-L proof, which is the preceding paragraph.

## 5. Exact two-phase obstruction, with arbitrary gauges

Let the common allowed nonzero phases be omega and its conjugate, with `|omega|=1` and `Re(omega²)=-3/4`. Multiplying an entire vector by a cell-dependent unit phase and multiplying each coordinate by a common unit phase do not change inner-product magnitudes, so include both freedoms in the hypothesis. Put `zeta=omega²=(-3±i sqrt(7))/4`.

For the nonsharing pair x,y from §4, the seven common support coordinates contribute seven numbers in `{1,zeta,conjugate(zeta)}` to the inner product, up to one common unit phase. Let their counts be a,b,c with a+b+c=7 and set

`S=a+b zeta+c conjugate(zeta)`.

Directly,

`16|S|² = [4a-3(b+c)]²+7(b-c)² = 49(a-3)²+7(b-c)²`.

The right side is divisible by7. A physical uniform lift would require `|S/8|²=1/8`, hence `|S|²=8` and `16|S|²=128`, which is NOT divisible by7. Contradiction. This argument covers ALL binary phase assignments, any cell phases, any common coordinate phases and every L; it is not based on a numerical sign search or a chosen pair.

The scope is the two-phase alphabet with this particular omega and the uniform M_* branch. General complex conference matrices/phases are NOT ruled out. In particular it would be wrong to infer nonexistence of a 9×9 complex conference matrix from the real parity obstruction.

## 6. Independently checked COMPLEX 9×9 conference and 19-ray fragment

Et-Taoui, [arXiv:1409.4282v1](https://arxiv.org/abs/1409.4282v1), §2, gives an odd-order complex conference construction using the quadratic character of GF(q). Independently specialize and check it for q=9 as follows. Represent GF(9)=F3[t]/(t²+1), compute its four nonzero squares exactly, and set for distinct x,y

`C_xy=(1 + chi(x-y)*i sqrt(7))/sqrt(8)`, `C_xx=0`.

Here chi is +1 on nonzero squares and −1 otherwise. This has precisely the two omega/conjugate phases with `omega=(1+i sqrt(7))/sqrt(8)`. The exact code `frontier-20261028-gf9-conference-v1.py`, SHA **663bfd831e9fe9c6a02bfc0af20800def7e7a3c15d667ada005eddfb5eabf530**, represents `U=C/sqrt(8)` by integer pairs `(a,b)/8` meaning `(a+b i sqrt(7))/8`; it verifies all81 entries of `UU*=I` exactly. It exports the conference block plus two actual ONBs as `frontier-20261028-gf9-conference-result-v1.json`, SHA **b099da227dd3d3c0e81bb5afb8172bba7660d1c7e2c73c65317fc88fa2e8dec7**.

The first ONB is e_0,...,e_9; the second is e_0 plus the9 conference columns embedded in e_0^perp. A separately written verifier `frontier-20261028-conference-fragment-check-v1.py`, SHA **92bffea124021c04424c729d8190dbfc1d56040a6a4ecf3b21836c6af513ca7c**, uses integer arithmetic in Q(i sqrt7), checks both original ONBs, every cross-reference zero/1/8 squared overlap, and all171 pairwise projective nonparallel comparisons among the19 distinct rays. Actual output:

```text
exact field check: Q(i sqrt 7) using integer-pair arithmetic
two ONBs: all 200 ordered inner products exact; one shared basis ray
cross basis: two zero coordinates and eight squared overlaps 1/8 each
all 171 distinct-ray pairs nonparallel: PASS; actual rays 19
scope: 2 ONB blocks only; NOT a 100-ray resolvable QLS
```

The independent verifier's FIRST run failed because its expected unnormalized cross-product square was mistakenly8 rather than `8^4/8=512`. The scaling was corrected before the successful run above; the failed assertion was not reported as a pass. The producer and its exact array were unchanged. This fragment proves individual complex conference feasibility but deliberately does NOT fill the remaining rows/columns/transversals. Theorem C says repeating its global two-phase alphabet cannot produce the full uniform array.

## 7. Arbitrary hyperplane and basis support bound

Let P_x=psi_x psi_x*, and let M_xy=tr(P_x P_y) be the ACTUAL physical projector Gram matrix. The given uniform pattern has the full incidence spectrum

`M=n P_1 + [n/(n−2)] P_U`,

with P_1 the all-one line and P_U orthogonal to both that line and the three centered block spaces. In particular its eigenvalues are n, n/(n−2), 0. This follows from `M=(nI-B^T B+J)/(n−2)` and the three block classes' pairwise single intersections, as in the valid scoped scalar computation; no physical lift is inferred merely from that formal M.

Let H be the REAL Hilbert space of Hermitian n×n matrices, with trace inner product, and define `(T X)_x=tr(P_x X)`. Then `TT*=M`. Because each of the n row ONBs sums to I, `sum_x P_x=nI`, so `T(I/n)=1/n * 1` and T maps traceless matrices into 1^perp. For traceless X, the nonzero eigenvalues of `T*T` are those of M on 1^perp, at most n/(n−2). Therefore

`sum_x [tr(P_x X)]² <= [n/(n−2)] tr(X²)`.

For ANY unit e put E=ee*, X=E−I/n. Then `tr X=0`, `tr X²=1−1/n`, and the identity and traceless contributions to TE are orthogonal. Consequently

`sum_x |<e,psi_x>|^4 <= 1+(n−1)/(n−2) = (2n−3)/(n−2)`.

Also `sum_x |<e,psi_x>|²=n`. If m(e) denotes the number of NONZERO such overlaps, Cauchy gives

`n² <= m(e) * sum_x |<e,psi_x>|^4`,

so `m(e)>=ceil[n²(n−2)/(2n−3)]`. At n=10 this is48, since `47*17<800<=48*17`. Thus at most52 rays lie in e^perp. For ANY orthonormal basis e_1,...,e_10, sum over its coordinates to obtain at least480 nonzero vector entries. If q vectors have support>=5, total support is at most `4(100-q)+10q=400+6q`, so q>=14. This is a conditional original-vector bound, not a lower bound on rank of the unlifted M alone.

Independent `frontier-20261028-uniform-incidence-check-v1.py`, SHA **142d47bdcdb5ed79674c475ee89a4e90aeb2c052b453656536778d19d45d08ee**, checked on an exact published OLS incidence that `B=8M_*` obeys the integer identity `B²=10B+56J` in ALL10000 entries and `B1=80*1`, with eigenvalues10,5/4,0 for M_* of multiplicities1,72,27. That is an exact check of a FORMAL scalar matrix, not proof of a physical lift. The all-L proof comes from the incidence projectors and actual Hilbert–Schmidt map above.

## 8. Exact open boundary

These theorems materially constrain the uniform M_* branch: no real physical lift for even n; at n10 no fixed two-phase GF9-style global glue; exact zero/support incidence and hyperplane occupancy. The explicit complex conference fragment shows that a single local block is possible, so the unresolved step is the simultaneous phase compatibility across the SAME remaining row, column and transversal ONBs with ALL100 distinct rays. No proof covers arbitrary complex phases, all nonuniform overlaps, another original state topology, or every 1-resolvable QLS10. No actual full uniform or nonuniform witness/no-go is delivered.

Every exact program result is bounded to its stated inputs. Novelty, independent review and original 100-ray target remain open; no external model, secrets, deletion, publication or infrastructure action. The earlier local-process records remain historical, not newly validated premises.

**END — uniform-branch real/two-phase obstructions and exact complex fragment, not unrestricted QLS10 closure.**
