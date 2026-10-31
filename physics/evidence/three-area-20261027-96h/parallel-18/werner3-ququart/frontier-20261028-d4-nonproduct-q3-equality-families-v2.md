# Source-independent q3 equality for arbitrary pairs of product projectors

**PhysicsResearch96h-2 / physics-1. WRITTEN all-variable proof; UNREVIEWED.** This is a self-contained successor to `frontier-20261028-d4-nonproduct-q3-equality-families-v1.md`, SHA256 `1211899d681e5841105911c49bd4b7d5be0296203d2bc2bd8dc78eaf9f79104c`. It removes the unnecessary global-orthogonality assumption and classifies equality in the entire arbitrary two-product-projector class. In particular it disproves the potential claim that product **operators** exhaust the original rank≤2 q3 equality set. It does not claim global q3≥0, a complete global equality classification, novelty, source-certificate correctness, parent/f62/f153 adoption, all-d/operational consequences, or formal/human/family verification. The already frozen f153 product-operator review is neither enlarged nor altered.

## 1. Exact arbitrary-pair statement

Let `H=(C⁴)^tensor3`. Choose arbitrary unit vectors `u_i,v_i∈C⁴`, without assuming any orthogonality, and write

`u=u1⊗u2⊗u3`, `v=v1⊗v2⊗v3`, `t_i=|<u_i,v_i>|²∈[0,1]`.

Set `P_u=|u><u|`, `P_v=|v><v|` and let arbitrary complex α,β define

`C=α P_u+β P_v`.

This C always has rank≤2. The original unnormalized-partial-trace functional obeys exactly

`q3(C) = (|α|²+|β|²)/8 + 2 Re(α conjugate(β)) Π_i(t_i−1/2)`
`      >= (|α|−|β|)²/8 >= 0`.                                        (1)

Assume αβ≠0. Equality `q3(C)=0` holds if and only if every `t_i∈{0,1}` and, with `k=#{i:t_i=0}`,

- k odd: `α=β`;
- k even: `α=−β`.

The k=0 case has u,v parallel globally and α=−β, hence C=0. If k≥1, u,v are globally orthogonal, C has exact rank2, and k=1,2,3 are the only possibilities. The k=1 branch is the known product-operator type. The k=2 and k=3 branches are **genuinely nonproduct operators**: at an orthogonal site with at least one other orthogonal site in the complement, the two summands have independent local operator factors on both sides of the cut, so the operator Schmidt rank is2.

In particular, the original rank2 q3 equality set contains, without a source/certificate premise, both all-variable nonproduct families:

- **Two orthogonal local pairs:** `C=α(P_u−P_v)`, with the remaining local pair parallel.
- **Three orthogonal local pairs:** `C=α(P_u+P_v)`.

Here α is any nonzero complex scalar, each orthogonal pair and parallel pair is arbitrary, and no particular numerical target state or q3 test value is selected. If one coefficient is zero and the other nonzero, (1) gives q3>0; if both vanish, C=0.

## 2. Direct proof from the original trace formula

For a product unit vector u, every reduced projection `Tr_S P_u` is again a rank1 product projection. Therefore every subset term has squared Hilbert–Schmidt norm1, giving

`q3(P_u) = 1−3/2+3/4−1/8 = 1/8`,

and similarly for v, regardless of whether u and v are orthogonal.

The Hermitian bilinear cross coefficient of original q3 is

`B(P_u,P_v) = Σ_(S⊂{1,2,3}) (−1/2)^|S| Tr[(Tr_S P_u)(Tr_S P_v)]`.

For every S,

`Tr[(Tr_S P_u)(Tr_S P_v)] = Π_(i∉S) t_i`.

Thus

`B(P_u,P_v)=Π_i(t_i−1/2)`.                                            (2)

The q3 quadratic form is Hermitian over complex C, so the equality in (1) follows, with exactly `2 Re(α conjugate(β))` multiplying (2).

Each `|t_i−1/2|≤1/2`; applying `|Re(α conjugate(β))|≤|α||β|` gives the lower bound in (1). If αβ≠0, equality q3=0 requires equality in both estimates and `|α|=|β|`: thus every `t_i=0 or1` and the relative phase satisfies `Re(α conjugate(β)) Π_i(t_i−1/2)=−|α||β|/8`. Since the product equals `(−1)^k/8`, this forces α=β for k odd, α=−β for k even. Conversely each displayed case gives q3=0.

For k≥1, at least one local pair is orthogonal, so u⊥v and the two nonzero weighted projectors have rank2. More generally, whenever u,v are nonparallel and αβ≠0, `C=M diag(α,β) M†` with the two-column map M=[u v] injective; M† is surjective, so C has rank2. For k=0 all local pairs are parallel, `P_u=P_v`, and α=−β makes C exactly zero.

For the k≥2 nonproduct assertion, fix an orthogonal local site i and group the remaining two sites into `H_rest`. The local projectors `|u_i><u_i|` and `|v_i><v_i|` are linearly independent; the complement projectors are also independent because another local pair is orthogonal. Therefore the nonzero sum or difference has operator Schmidt rank2 across `i|rest`, so cannot be a product of three local operators.

## 3. Scope and provenance

The proof uses only the original q3 trace formula and inner products of arbitrary product vectors. It is independent of the unreviewed fixed-d4 source certificate and of the conditional antisymmetry-bound packet, and does not use or reconstruct the elected HELD/ZERO/NONINPUT episode or any of its consumers/guidance. The public full-target Werner claim retires new-discovery status; no literature-exhaustiveness or novelty claim is made. Classification is complete only for the specified two-projector class, not all rank2 operators. Historical process/held findings and the frozen f153/f62 review boundaries remain unchanged.
