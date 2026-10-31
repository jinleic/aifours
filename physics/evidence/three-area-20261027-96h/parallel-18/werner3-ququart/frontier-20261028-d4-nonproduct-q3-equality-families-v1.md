# Source-independent nonproduct equality families for the original q3

**PhysicsResearch96h-2 / physics-1. WRITTEN all-variable proof; UNREVIEWED.** This source-independent result disproves the potential assertion that the previously identified product-operator equality family exhausts the original complex rank≤2 equality set. It does not claim global q3≥0, a complete equality classification, novelty, source-certificate correctness, parent/f62/f153 adoption, all-d/operational consequences, or formal/human/family verification. The already frozen f153 product-family review is not enlarged or altered.

## 1. Exact statement, including all complex weights

Let `H=(C⁴)^tensor3`. For each physical site i, choose arbitrary unit vectors `u_i,v_i∈C⁴` and write

`u=u1⊗u2⊗u3`, `v=v1⊗v2⊗v3`, `t_i=|<u_i,v_i>|²∈[0,1]`.

Assume u and v are globally orthogonal, equivalently `t_1 t_2 t_3=0`. Let `P_u=|u><u|`, `P_v=|v><v|` and let arbitrary complex α,β define

`C=α P_u+β P_v`.

C has rank2 when αβ≠0. Its original unnormalized-trace functional obeys exactly

`q3(C) = (|α|²+|β|²)/8 + 2 Re(α conjugate(β)) Π_i(t_i−1/2)`
`      >= (|α|−|β|)²/8 >= 0`.                                        (1)

For nonzero α,β, equality in (1) occurs if and only if every `t_i∈{0,1}` and, with `k=#{i:t_i=0}`,

- k=1 or k=3: `α=β`;
- k=2: `α=−β`.

Here `t_i=0` means the local vectors are orthogonal, and `t_i=1` means they are parallel up to phase. The k=1 branch is the already known product-operator type. The k=2 and k=3 branches are **genuinely nonproduct operators**: at any site where u_i and v_i are orthogonal and the complementary sites include another orthogonal pair, the two summands have independent local operator factors on both sides of the cut, giving operator Schmidt rank2 across that cut.

Thus the original rank2 q3 equality set contains, without any conditional source premise, BOTH of these all-variable families:

- **Two orthogonal local pairs:** `C=α(P_u−P_v)`, where the remaining local pair is parallel.
- **Three orthogonal local pairs:** `C=α(P_u+P_v)`.

α is any nonzero complex scalar and the local vectors may vary through all corresponding orthonormal/parallel frames. No selected numerical target state or q3 numerical test is used; these are universal symbolic families. The case α=β=0 is C=0; if precisely one coefficient vanishes, q3>0.

## 2. Direct proof from the original trace formula

For any product unit vector u, every reduced projection `Tr_S P_u` is again a rank1 product projection. Therefore every subset term has squared Hilbert–Schmidt norm1, so

`q3(P_u) = 1−3/2+3/4−1/8 = 1/8`,

and likewise `q3(P_v)=1/8`.

The Hermitian bilinear cross coefficient of the original q3 is

`B(P_u,P_v) = Σ_(S⊂{1,2,3}) (−1/2)^|S| Tr[(Tr_S P_u)(Tr_S P_v)]`.

For every S, the reduced product projectors give

`Tr[(Tr_S P_u)(Tr_S P_v)] = Π_(i∉S) t_i`.

Consequently, by the elementary product expansion,

`B(P_u,P_v)=Π_i(t_i−1/2)`.                                            (2)

The q3 quadratic form is Hermitian over complex C, so inserting C=αP_u+βP_v gives the equality in (1), with exactly `2 Re(α conjugate(β))` multiplying (2).

Each `|t_i−1/2|≤1/2`, hence the absolute value of (2) is at most1/8. Using `|Re(α conjugate(β))|≤|α||β|` yields the lower bound in (1). If αβ≠0, equality requires equality in every estimate: `|α|=|β|`, every `t_i=0 or1`, and the relative phase must make `Re(α conjugate(β)) Π_i(t_i−1/2) = −|α||β|/8`. Since global orthogonality requires k≥1, the signs are `Π_i(t_i−1/2)=(−1)^k/8`, giving the three stated cases. Conversely, substitution gives q3=0 in each case. This is an exact characterization **only within the stated two-orthogonal-product-projector class**; no general equality classification is inferred.

For the nonproduct assertion when k≥2, fix one orthogonal site i and put the rest in `H_rest`. The two local projectors `|u_i><u_i|` and `|v_i><v_i|` are linearly independent, and so are the corresponding complement projectors because at least one other local pair is orthogonal. Therefore a nontrivial sum or difference of their simple tensors cannot have operator Schmidt rank1 across `i|rest`; C cannot be a product of three local operators.

## 3. Provenance and nonclaims

The proof uses only the original q3 trace formula and all-variable inner products of arbitrary local product vectors. It is independent of the unreviewed fixed-d4 source certificate and of the consolidated conditional antisymmetry-bound packet; it does not use or reconstruct the elected HELD/ZERO/NONINPUT episode or any of its consumers/guidance. The prior public full-target Werner claim retires any new-discovery assertion; no literature-exhaustiveness or novelty claim is made. Historical process/held findings and the frozen f153/f62 review boundaries remain unchanged.
