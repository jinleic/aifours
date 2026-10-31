# Intrinsic original-operator form of the d4 lower bound

**PhysicsResearch96h-2 / physics-1. WRITTEN.** The source-independent trace identity and nonnegativity below are elementary operator facts. The resulting q3 inequality is conditional on the actual pinned fixed-d4 source-certificate/physical-PSD premises in `frontier-20261028-d4-q3-explicit-rational-coercive-bound-v1.md`, SHA256 `5fdd6a6040bb57569aad8ba95c05bb49b6bc16849a81e0cfb2167962f4c0f619`. It is not a source-independent proof of q3≥0, an equality classification, or parent/f62/human/family/formal/novelty/physical-operational acceptance.

## 1. No auxiliary basis or lift in the final expression

Let H=(C⁴)^tensor3 and let `A3=P_-^(1)⊗P_-^(2)⊗P_-^(3)` on H⊗H, with the usual regrouping by site. Let C:H→H be any nonzero complex rank≤2 operator normalized by `||C||HS²=1/2`. Let P be any rank2 orthogonal projection with `PC=C`; for rank2 C, P is the uniquely determined range projection. Define the real scalar

`Δ(P,C) = Tr[ A3 (P⊗C†C − C⊗C†) ]`.                               (1)

Then, independently of any source certificate,

`Δ(P,C) >= 0`.                                                        (2)

Moreover, subject to the separately pinned certificate/physical-Gram premises, the full-original-domain bound is

`q3(C) >= [41960431118628029 / 14774058577588912128000] · Δ(P,C)`     (3)

for every such C and P. Thus for exact rank2, the right side is an **intrinsic expression in the original C and its range projection**, not in chosen auxiliary coordinates. For rank1, every rank2 range extension P is allowed. Neither Δ>0 nor q3>0 is asserted universally; Δ=0 is not asserted sufficient for q3 equality. The normalization is harmless because every nonzero original C can be scaled to the displayed norm and q3 is homogeneous.

## 2. Exact lift-free identity

Choose any isometry `A:Q=C²→H` with `AA†=P`. The corresponding normalized physical lift is

`a=vec(A)/sqrt2`, `b=sqrt2 vec(C†A)`.

It has unit norms, a Q marginal I/2, and reconstructs C, because `PC=C` and `||C||HS²=1/2`. For a unit `r∈Q`, write `t=conjugate(r)`, `a_r=(I⊗<r|)a`, `b_r=(I⊗<r|)b`. Then

`a_r⊗b_r = (A⊗C†A)(t⊗t)`.

The exact Haar second moment on the unit sphere of C² is

`∫ |t⊗t><t⊗t| dμ(t) = (I+F_Q)/6`.

Let `F=F_H` swap the two complete H copies. Since `PC=C` and `(A⊗A)F_Q=F(A⊗A)`, this gives the operator identity

`∫ |a_r⊗b_r><a_r⊗b_r| dμ(r)`
` = [P⊗C†C + (C⊗C†)F]/6`.                                        (4)

The range of A3 is globally antisymmetric: `F A3 = −A3` because there are three local antisymmetric factors. Tracing (4) against A3 and cyclically moving F therefore yields

`∫ ||A3(a_r⊗b_r)||² dμ(r) = Δ(P,C)/6`.                              (5)

The left side is nonnegative, proving (2), and is exactly the bracket in the preceding rational bound. Multiplying (5) by the explicit preceding coefficient yields (3). Since the right side of (5) uses only P,C, the integral is independent of the choice of isometry A and Q basis. For rank2 P is canonical; for rank1 P may vary but each identity and bound remains valid.

## 3. Source-independent general operator fact

The nonnegativity does not require rank≤2, local dimension4, or the source certificate. Let H be any finite-dimensional Hilbert space, P any orthogonal projection with `PC=C`, F the global swap, and K≥0 any operator on H⊗H with `F K=−K`. Choose an isometry A onto ran P, of any finite positive rank. Then

`P⊗C†C + (C⊗C†)F = (A⊗C†A)(I+F_Q)(A⊗C†A)† >= 0`.          (6)

Indeed `I+F_Q` is positive semidefinite. Taking the trace against K and moving F through K proves

`Tr[ K (P⊗C†C − C⊗C†) ] >= 0`.                                    (7)

For K=A3 this is (2); `Tr[K(C⊗C†)]` is real because conjugation interchanges the two factors and K commutes with F. The rank0 projection case has C=0 and is immediate. This is a source-independent comparison inequality, **not** the original q3 nonnegativity theorem.

For direct original-coordinate evaluation, any operators X,Y on H obey

`Tr[A3(X⊗Y)] = (1/8) Σ_(S⊂{1,2,3}) (−1)^|S| Tr[(Tr_(S^c)X)(Tr_(S^c)Y)]`,

by expanding the three local swap projectors. Thus Δ can also be expressed using only unnormalized partial traces of P,C†C,C,C†; no Gram tuple, tensor-lift coordinate, or source bundle is needed to state (2) itself.

## 4. Scope and provenance

The exact source coefficient in (3) depends on the source equality/PSD identity and the pinned exact frame/multiplier witnesses in the preceding bound; no independent status is silently promoted. The source-independent statement is only (2), (4)–(7), not q3 positivity. The properness of the lift obstruction does not give a converse equality classification. Public prior-claim/novelty, source/runtime, historical process and frozen review boundaries remain as before. This derivation uses the original C, standard Haar/swap algebra and the prior prospective source-bound proof; no elected HELD/ZERO/NONINPUT episode or its guidance is used.
