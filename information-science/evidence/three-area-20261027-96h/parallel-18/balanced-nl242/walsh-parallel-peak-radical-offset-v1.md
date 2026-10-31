# info-6: non-affine parallel peak cubes obey one common offset constraint

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Actual `/bin/date` observed before this write: **2026-10-27T15:55:32-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** This is an all-direction conditional compatibility theorem; it is not a selected cube, witness, unrestricted no-go, rank/type exclusion, numerical nonlinearity improvement, formal/kernel or novelty claim. No scientific program or selected-state/direction probe was used.

## Claim

For any original balanced peak≤28 object and any 3-dimensional frequency direction H admitting a fully peak cube with non-affine signs, the restriction of the one common mod-4 bilinear form 𝔅 to H has a unique nonzero vector r that pairs to zero with all H. The actual parity pattern of the eight source cosets of H^⊥ is the indicator of the affine hyperplane

    {y∈V/H^⊥ : y(r)=c},

where c is the common sign derivative along r of any fully peak cube with direction H. Consequently, if a₀+H and a₀+d+H are **any** two such parallel peak cubes, then

    𝔅(r,d)=0.                                                    (1)

If the functional d↦𝔅(r,d) is nonzero on T^⊥, there can be at most 16 parallel peak cubes with direction H; otherwise the separate Parseval bound of 20 still applies. No such H, r, d or object is selected or asserted to exist.

## Proof

All peak frequencies lie in the odd half {a:a·T=1}, so H⊆T^⊥. The v1 mod-4 identity gives a Boolean quadratic phase Q on that whole odd half. A peak sign on E=a₀+H is −(-1)^{Q(a)}. Non-affine signs mean the restriction of 𝔅 to H is nonzero. The elementary 3-dimensional alternating-form argument in `walsh-peak-cube-shift-coupling-v1.md` gives its unique nonzero common-kernel vector r. Thus Q(a+r)+Q(a)=c is constant on each individual peak cube, and its sign function ε satisfies ε(h+r)=(-1)^c ε(h) for all h∈H.

Let y range over the dual quotient V/H^⊥. The transform of ε vanishes unless y(r)=c, because translating h by r multiplies its transform by both (-1)^c and (-1)^{y(r)}. In the non-affine case the local-restriction theorem says its support has four points, so it is exactly that affine hyperplane. The source-coset parity theorem identifies p_H with the support indicator, proving the first assertion.

The parity pattern p_H comes from the one actual f and is independent of the peak-cube base. Therefore any other parallel peak cube has the same c. The global quadratic second-difference identity gives

    [Q(a₀+d+r)+Q(a₀+d)]−[Q(a₀+r)+Q(a₀)] = 𝔅(r,d)  in F₂,

proving (1). Both cube bases are in the odd T-half, so d∈T^⊥. Since r is a radical vector on H, 𝔅(r,·) vanishes on H and descends to K/H with K=T^⊥. If it is nonzero there, only half of that 5-dimensional quotient can occur as offsets, giving at most 16 parallel cubes. If it is zero on K, the previously proved source-cell Parseval bound remains 20. ∎

## Exact scope and dependencies

This is a necessary cross-cube condition for all directions and every actual object; it does not claim any non-affine cube, offset, truth table or witness exists, nor does it rule out the remaining cases. Inputs are the S1 supplied definitions, the v1 full mod-4 identity, and unreviewed `walsh-peak-cube-shift-coupling-v1.md` SHA-256 `c0b51e5c3684c487641b27a482173f416909d5ddbccb2037434cb7288f572e16`, 25 LF, `walsh-peak-cube-source-coset-parity-v1.md` SHA-256 `6d09a7a4ee8487a50b91d0536169d21b7212a0a7b61da4da3b7740c3b4abb841`, 27 LF, and `walsh-parallel-peak-cubes-v1.md` SHA-256 `f221400aaca91783e780c6975127a8d31540820c0bee650f32470523e0e47512`, 25 LF. All new implications remain unreviewed despite Main's earlier written support for the v1 caller and ≥92 peak result with its MINOR overlay.

No old Gate-I/candidate/HELD body, stopped half-split/canonical method or stopped global truth-degree/ANF source is used or reconstructed. The original unrestricted witness-or-no-go, every rank/weight alternative and `(24,24,2)` remain open. Book-source equivalence, independent full-scope review, human, formal/kernel, executable and novelty gates remain unperformed. Prior exposure, metadata-poll MINOR, S1 STOP/HOLD/ZERO, N4 UNKNOWN and aux214 STOP persist.
