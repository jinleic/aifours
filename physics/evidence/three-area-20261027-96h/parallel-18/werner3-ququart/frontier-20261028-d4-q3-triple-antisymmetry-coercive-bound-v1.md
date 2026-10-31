# A full-original-domain coercive bound from one physical source block

**PhysicsResearch96h-2 / physics-1. WRITTEN; conditional on the separately checked actual fixed-d4 source certificate and physical-PSD premises.** This is not a source-independent proof of q3≥0, an explicit numerical constant, a strictly positive bound on all nonzero inputs, a complete equality classification, or a parent/f62/human/family/formal/Lean/novelty/operational acceptance claim.

## Statement

Let `H=(C⁴)^tensor3`, `Q=C²` and let nonzero `C:H→H` have complex rank at most2 and be normalized by `||C||HS²=1/2`. Choose ANY normalized isometric physical lift a,b∈H⊗Q with `||a||=||b||=1`, `Tr_H|a><a|=I_Q/2` and `C_xy=Σ_j a_(x,j) conjugate(b_(y,j))`. Set `a_r=(I⊗<r|)a`, `b_r=(I⊗<r|)b`, and `A3=P_-^(1)⊗P_-^(2)⊗P_-^(3)` on H⊗H, with the two copies regrouped by site.

Assume the exact actual source identity `q3(C)=Σ_t Tr(Z_t B_t)` on these same-pair physical lifts, actual Gram PSD `B_t>=0`, all actual corrected `Z_t>=0`, and the actual corrected scalar `z270>0` of zero-based source block `pkg['types'][270]`, with the physical compression described below. These are the same explicit, separately reviewable source/certificate premises recorded in `frontier-20261028-d4-original-q3-global-certificate-equality-v1.md` and `frontier-20261028-d4-equality-triple-antisymmetry-v1.md`; neither their independent acceptance nor the f62 scope is assumed.

There is a constant `κ>0`, depending only on the d4 source block and group averages, such that for **all** such original C and **every** such lift,

`q3(C) >= κ ∫_(R∈U(2)) ||A3(a_(R†e0)⊗b_(R†e0))||² dR`.              (1)

Haar measures here and below are probability measures. In any fixed Q basis, writing

`w00=A3(a0⊗b0)`, `w01=A3(a0⊗b1+a1⊗b0)`, `w11=A3(a1⊗b1)`,

(1) is the finite explicit homogeneous bound

`q3(C) >= κ [(||w00||²+||w11||²)/3 + ||w01||²/6]`.                    (2)

The integral and bracket can vanish for nonzero inputs: no uniform strictly positive q3/||C||² gap follows. The bound implies the preceding all-r antisymmetry condition when q3(C)=0, and is strictly positive whenever the bracket is nonzero. It does not assert that bracket-zero inputs are equalities.

## Actual block and exact positive constant definition

The actual source-binding check `frontier-20261028-d4-equality-block270-source-check.py`, SHA256 `7b40a6423924848644149bfcd742f8ea44fad7ac825838b07b60568692464cc6`, independently checked the pinned source/data. Its result SHA256 `8a112e9e3e5acafefd0c27ddfc4e9a0c2754c33bfd85ae2a655749a1064c2316` binds zero-based index270, single row `a* a* a b`, source rank1, joint compression `[1]`, positive scalar multiplier z270, site tensors `e3⊗e3⊗(e1⊗e0−e0⊗e1)` at all three sites, and auxiliary tensor `e1⊗e1⊗e0⊗e0`. These are fixed certificate basis vectors, not chosen original target states. The source physical moments are the common local-unitary, finite site-permutation and simultaneous-conjugation average multiplied by `L=(2·4³)^4`; let θ>0 denote the weight of the identity site/conjugation term in that finite average.

For U=(U1,U2,U3)∈U(4)^3, define

`x(U)=U1†e3⊗U2†e3⊗U3†e3`,
`η(U)=⊗_(i=1)^3[(Ui†e1)⊗(Ui†e0)−(Ui†e0)⊗(Ui†e1)]`,

and `E=(wedge² C⁴)^tensor3`. Let

`m = min_(u∈H,w∈E, ||u||=||w||=1) ∫_(U∈U(4)^3) |<x(U),u>|^4 |<η(U),w>|² dU`.

The minimum exists and is **strictly positive** by the proof below. One valid constant in (1)–(2) is exactly

`κ = L θ z270 m / 4 > 0`.

No numerical value or computable lower approximation for m is claimed.

## Proof of the uniform bound

For nonzero u, `U↦<x(U),u>` is a nonzero real-analytic function: local product vectors span H. For nonzero w∈E, `U↦<η(U),w>` is also nonzero real-analytic: independent local orthonormal-frame wedges span E. The compact Lie group U(4)^3 is connected, so the nonzero sets of these two functions are dense and open. Their intersection is nonempty; by continuity and full Haar support, their squared-modulus product has strictly positive integral. This holds for EVERY nonzero u,w.

The integral is continuous in u,w. The product of unit spheres in the finite-dimensional H and E is compact, so its minimum m is positive. Homogeneity gives, for all u,w,

`∫ |<x(U),u>|^4 |<η(U),w>|² dU >= m ||u||^4 ||w||²`.         (3)

All source summands are nonnegative, and the actual scalar block is a scaled average of absolute squares. Keeping just block270 and just the identity finite symmetry term therefore yields

`q3(C) >= L θ z270 ∫_(R∈U(2))∫_(U∈U(4)^3) |<x(U),a_s>|^4 |<η(U),a_r⊗b_r>|² dU dR`,

where `r=R†e0` and `s=R†e1`. The exact contraction is the one in the preceding block270 theorem; the placement of conjugates changes no modulus. Since η(U) lies in E, its pairing with `a_r⊗b_r` equals its pairing with `w=A3(a_r⊗b_r)`. The isometric Q marginal gives `||a_s||²=1/2` for every R. Applying (3) pointwise in R proves (1) with κ as defined. The argument uses no selected state or q3 value.

Finally, r=R†e0 is uniformly distributed on the unit sphere of C². Its independent coordinate phases kill mixed monomial terms, and the exact sphere moments are `E|r0|⁴=E|r1|⁴=1/3` and `E|r0 r1|²=1/6`. Thus the integral in (1) equals the displayed bracket in (2). These are probability-Haar identities, not evaluations of a target state.

## Scope and provenance

The bracket is a proper restriction of physical lifts by the independent abstract linear-algebra argument `frontier-20261028-d4-equality-triple-antisymmetry-nonvacuity-v1.md`, SHA256 `bef6d3acf60eb94bbe5f5134f1521de566866c7f02bf5eaa6048bb9e67c5b080`; it is not proved sufficient for equality. This proof uses the pre-episode pinned source block/certificate, original physical lift, Haar invariance and elementary real-analytic compactness only. The elected prior episode and all its consumers remain HELD/ZERO/NONINPUT and are not used or reconstructed. Prior timing/process and source/runtime limitations, unreviewed status, parent/f62 boundaries, and public-prior-claim/novelty limitations remain unchanged.
