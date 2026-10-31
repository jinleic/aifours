# Explicit rational full-domain q3 bound from the actual d4 source block

**PhysicsResearch96h-2 / physics-1. WRITTEN plus exact rational local-frame computation; conditional on the pinned actual d4 source certificate and physical PSD/equality premises.** This strengthens `frontier-20261028-d4-q3-triple-antisymmetry-coercive-bound-v1.md`, SHA256 `fa6a603d774db75be797a1dbff343ac0f09342c3c3f774014392daa2e0dbaa5e`, by replacing its positive compactness-defined constant with an explicit positive rational constant. It is not a source-independent q3 proof, a universal strict gap, a complete equality classification, a selected-target-state calculation, or parent/f62/human/family/formal/Lean/novelty/operational acceptance.

## 1. Bound on the entire original rank≤2 domain

Let H=(C⁴)^tensor3, Q=C², and let any nonzero complex rank≤2 operator C on H be rescaled to `||C||HS²=1/2`. Let a,b∈H⊗Q be ANY normalized isometric physical lift with `||a||=||b||=1`, `Tr_H|a><a|=I_Q/2`, and `C_xy=Σ_j a_(x,j) conjugate(b_(y,j))`. Let `a_j=(I⊗<e_j|)a`, `b_j=(I⊗<e_j|)b`. On two H copies, regrouped by site, set `A3=P_-^(1)⊗P_-^(2)⊗P_-^(3)` and

`w00=A3(a0⊗b0)`, `w01=A3(a0⊗b1+a1⊗b0)`, `w11=A3(a1⊗b1)`.

Assume the separately pinned source identity, physical Gram PSD/equalities, and corrected multiplier PSD as in the preceding bound. Then for every C and every such lift,

`q3(C) >= [41960431118628029 / 2462343096264818688000] · [ (||w00||²+||w11||²)/3 + ||w01||²/6 ]`.    (1)

The rational constant is strictly positive; the bracket can vanish for nonzero C, so (1) is not a universal strict q3 gap. The bracket being zero is necessary for q3 equality under the source premises but is NOT asserted sufficient. No equality parameterization or product exhaustion is claimed.

## 2. Exact single-site Haar frame

Take V=C⁴, `S=Sym²(V)⊗wedge²(V)`, and

`v=e3⊗e3⊗(e1⊗e0−e0⊗e1) ∈ S`,
`T=∫_(U∈U(4)) U^tensor4 |v><v| (U†)^tensor4 dU`.

Haar measure is normalized. The source compression uses exactly v at all three physical sites; these are fixed compression-basis vectors, not chosen target operators. The exact local identity is

`675 T² − 60 T + I_S = 0`, `Tr_S T=2`.                              (2)

T is self-adjoint, so its only eigenvalues are `1/45` and `1/15`. The dimension of S is 60; (2) and the trace give multiplicities45 and15 respectively. Hence on the ambient V^tensor4,

`T >= (1/45) P_S`.                                                   (3)

Here `P_S=P_+^(first two replicas)⊗P_-^(last two replicas)`. The precise exact calculation of (2) is in `frontier-20261028-d4-local-haar-frame-rational-check-v1.py`, SHA256 `138961ee025273a0b11ea8c66867524a04ed537879e2b088fe75106633b87351`; result `frontier-20261028-d4-local-haar-frame-rational-check-results-v1.json`, SHA256 `ed3a75e270ace86ef9dbdde8af137405ef7cba9b90dff5727704889a3e999b74`, PASS. It uses Python integers/Fraction, not floats. A changed local wedge sign and an incorrect polynomial sign are both detected.

The calculation invokes the named standard four-copy Schur–Weyl/permutation-commutant theorem for U(4): twirling is the Hilbert–Schmidt projection onto the span of the 24 permutation operators P_p. Its 24×24 Gram matrix is `G_pq=4^cycles(p^(-1)q)`. The program independently checks each Gram entry against all 256 basis-word traces, solves `G c=b` exactly for `b_p=<v,P_p v>`, and builds the twirl `Σ_p c_p P_p`. In the explicit 60-vector orthogonal tensor basis of S, with metric diagonal D (entries2 or4), it verifies all 3600 exact entries of `675 H D^(-1) H−60 H+D=0`, where `H_ij=<basis_i,T basis_j>`, along with H symmetry and the trace. The calculation is a finite exact arithmetic witness conditional on the named commutant theorem, not a formal proof assistant check or an independent review of the whole source certificate.

## 3. From the local frame to a uniform explicit constant

For `u∈H`, `w∈E=(wedge² C⁴)^tensor3`, define as in the preceding bound

`I(u,w)=∫_(U∈U(4)^3) |<x(U),u>|⁴ |<η(U),w>|² dU`,

where `x(U)=⊗_i Ui†e3` and `η(U)=⊗_i[(Ui†e1)⊗(Ui†e0)−(Ui†e0)⊗(Ui†e1)]`. Regroup the four replicas `u⊗u⊗w` site by site. Independence of the three Haar integrations and (3) give

`I(u,w) >= (1/45³) || P_+^(1)⊗P_+^(2)⊗P_+^(3) (u⊗u) ||² · ||w||²`.   (4)

For the pure (not necessarily normalized) vector u, let `ρ_S=Tr_(S^c)|u><u|`. Expanding the three symmetric projectors and using the swap trick,

`|| P_+^(1)⊗P_+^(2)⊗P_+^(3) (u⊗u) ||² = (1/8) Σ_(S⊂{1,2,3}) Tr(ρ_S²)`.

The empty and full subset each contribute `||u||⁴`. Each of the three one-site reductions has trace `||u||²` and purity at least `||u||⁴/4` by Cauchy–Schwarz; its complementary two-site reduction has the same nonzero spectrum by the Schmidt decomposition. Therefore

`|| P_+^(1)⊗P_+^(2)⊗P_+^(3) (u⊗u) ||² >= (7/16)||u||⁴`.

Together with (4), this proves the all-variable frame bound

`I(u,w) >= [7/1458000] ||u||⁴ ||w||²`.                               (5)

No target state or value is selected; the argument applies to all complex u,w.

## 4. The exact rational source coefficient

Use the physical source moment formed with the **uniform** average over the six site permutations and the two simultaneous-conjugation choices, in addition to normalized local Haar twirling. Its identity finite branch has weight `1/12`. The source moment scale is `L=(2·4³)^4=128⁴`. The independently rebound actual corrected scalar of zero-based source block `pkg['types'][270]` is

`z270 = 5994347302661147 / 9444732965739290427392 > 0`.

For the actual scalar block, keeping only that nonnegative term and the identity finite branch gives the integrated source inequality in the preceding note. For every auxiliary unitary R, the lift satisfies `||a_(R†e1)||⁴=1/4`. Substitute (5), then use the exact U(2) sphere moments `E|r0|⁴=E|r1|⁴=1/3`, `E|r0r1|²=1/6` to obtain (1), with

`κ = 128⁴ · (1/12) · z270 · [7/(16·45³)] · (1/4)`
`  = 41960431118628029 / 2462343096264818688000`.

The separate source-scalar/hash and exact Fraction arithmetic check `frontier-20261028-d4-coercive-constant-source-check-v1.py`, SHA256 `f152b9a972d8107a92f99f1f5abade854c4b5bc070f77e2582f9327770dab93d`, result SHA256 `065d87613a108cf585e14d59ebba323a903094af61991c7a67a37080cd489bc0`, PASS, detected deliberately incorrect finite-twirl and lift-normalization factors. It does not itself prove the source identity, the Haar theorem, or the written inequality.

## 5. Boundaries and provenance

The source identity/PSD and whole physical-lift bridge remain necessary separately reviewed premises, not assumed independent family/human/formal acceptance. The properness of the bracket is recorded in `frontier-20261028-d4-equality-triple-antisymmetry-nonvacuity-v1.md`, SHA256 `bef6d3acf60eb94bbe5f5134f1521de566866c7f02bf5eaa6048bb9e67c5b080`; that does not prove sufficiency or an independence count. The prior public full-target claim retires novelty and is not automatically correctness-accepted. No all-d or physical operational claim follows.

This proof uses the pre-episode pinned source certificate/block, original physical lift, standard four-copy commutant theorem, Haar/swap identities and the exact rational witnesses above. No content or guidance from the elected earlier HELD/ZERO/NONINPUT episode is used or reconstructed; historic timing/process and frozen f62/parent-review boundaries are unchanged.
