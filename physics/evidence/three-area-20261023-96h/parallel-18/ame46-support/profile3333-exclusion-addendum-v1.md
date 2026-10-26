# Candidate addendum v1 — the all-three officer obstruction does not need e=0

Observed before creation: `2026-10-23T15:42:32-0700`. PhysicsAME46, physics-6. New WRITTEN scope strengthening; no execution. The previously reviewed snapshots remain unchanged. This ADDENDUM has NOT been independently reconstructed or parent-accepted; InfoSPR7's0F/0M/0minor return applies only to its named earlier source pins and literal scopes.

## Exact strengthened statement

There is no AME(4,6), with arbitrary complex amplitudes in any product orthonormal basis, having officer-deficit profile

    {3,3,3,3}⁴,

**for any value of the excess e.** Consequently there is no AME(4,6) with h=12 and exactly four active values in each coordinate, for any e.

This strengthens `profile3333-exclusion-v1.md` (SHA256 `5e1907bd1b0f60f19e32ac4d19287f7dc4b466de5dfff72cc81890c71a3cec27`) and the first corollary of `active-slice-corollaries-v1.md` (`04b3ee1c19b7a6051cc91953ab3ce2933d846f9972e9417478363e9c16d1b68d`). It is not a claim that every other profile is excluded or that the support minimum exceeds48. The numerical48..60 range is unchanged.

## 1. Everything before the forced-line step is officer-only

For any AME state, irrespective of e:

- Each of all six pair-value lines has squared A-norm1, where A=6psi.
- An officer coefficient of modulus1 is alone on each such line through it, and distinct officers cannot agree in two coordinates.
- Every line is occupied. If it has no officer, it has at least TWO nonzero coefficients: a singleton would have modulus1 and be an officer.
- N uses only active local values. A deficit0 value has six officers covering every partner-coordinate line, so cannot support any additional coefficient.

These facts suffice for the global/local officer counts, the conclusion that every officer has exactly two active coordinates, the bijections F_ij, the four binary inactive pairs on T_ij, and the complete binary endpoint-function normal form in §§1–2 of the original profile proof. None of those steps uses a count of non-officer entries in a slice or an e=0 closed2×2 component.

Thus, for arbitrary e, the SAME derived active-pair maps remain valid after local value relabelings:

    F_12=F_13=F_14=id,
    F_23=[2,3,1,0], F_24=[1,2,3,0], F_34=[2,0,3,1].

All six necessary forbidden-pair inequalities(*) from the original proof continue to hold for every non-officer coefficient.

## 2. The two particular lines force their OWN exact-two property

The original proof invoked the general e=0 exact-two theorem for its two hole lines. That hypothesis is unnecessary at these lines because the derived forbidden-pair inequalities leave only two POSSIBLE positions on each of them.

On line12=(3,0), the only possible nonzero positions are

    X=(3,0,0,0), Y=(3,0,1,2).

The line has no officer and has at least two nonzeros by the universal norm facts above. Therefore both X,Y occur, and there are no others. This row has support EXACTLY{(0,0),(1,2)} even without assuming e=0.

On line34=(1,2), the only possible rows are(3,0),(0,3). It too is officer-free and requires at least two nonzeros, so

    Z=(0,3,1,2)

occurs. The point(0,3,0,0) is forbidden by F_13=id. Hence the row(0,3), whatever further entries it might have elsewhere, overlaps row(3,0) in exactly ONE nonzero column, namely(1,2). The inner product is the nonzero product A_Y conjugate(A_Z), contradicting actual unitarity.

No condition on the degrees of any other non-officer row, any closed block, the value of e, or the sizes of other support slices is needed. This proves the strengthened officer-profile exclusion. ∎

## 3. Four-active-values corollary, also for arbitrary e

At h=12 and v=(4,4,4,4), the officer moment equality and its local consequences in the active-slice manuscript hold for all e. They force every officer's active weight to be2 and every positive deficit to be3. The strengthened profile theorem therefore rules out this whole active-alphabet stratum without an e restriction.

This does NOT remove e=0 from the separate thin-axis theorem, whose proof genuinely uses exact-two slice/component structure. It does not extend the two narrowed residual profiles to exclusions. The new scope requires its own separate reconstruction; the earlier peer verdict is not transferred to this new hash.

The next verification target is narrowly identified: verify that the officer normal form is e-independent and replace the two uses of global exact-two by the universal at-least-two plus two-possible-positions argument. No new scientific program, numerical tensor, SAT search or old certificate replay is requested.
