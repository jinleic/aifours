# Olson reflection: RP-LIFT

Recorded at 2026-10-19T08:34:29-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** Accepted written theorem relative to Lemma W and Facts 2.1–2.2 in the [v5 parent verdict](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-REFLHI-v5-parent-verdict-v1.md) `13ee1ba86245fc549bd79c130a9fe15248ecc3fe9fc8428e875ca939c940a547`. No Lean, scientific computation, unrestricted Olson result or priority claim.

## Exact theorem
For prime p>=5, let w have length 4p-2 over D_(2p), with exactly p rotation letters, all in one nonzero pair {rho_x,rho_-x}. Every maximal cyclic constant reflection block must have odd length. Put H=sum floor(l_i/2) over those blocks and kappa=p-1-H. If 1<=kappa<=(p-3)/2, w contains exactly 2p letters in increasing original index order whose ordered product is the identity. There is no purity, B<kappa or reflection-value hypothesis.

Source: [proof-Rp-integer-lift-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-Rp-integer-lift-v1.md) `34cb5e007095b6d3c9c9eb91b2385c9e52cd94f78cd5b82c73bac8a31961df69`.

## Binding readings
These implement all reviewer MINORs, without changing the statement or proof structure:
1. Avoidance means no increasing-index identity subword of exactly 2p letters, as defined in the [reflection source README](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/README.md) lines13–15. Cyclically shifting an identity product preserves identity by conjugation, so cyclic selection gives the same increasing-index conclusion. Normalisation belongs to setting (S).
2. In FWIN, 0<=E(P)=A_P+B_(P^c)<=A+B=p. Its representative in [0,2p) lies in [1,p-1].
3. In CONNECT, decreasing x_i keeps the preceding gap >=1 and x_i>=z_i; it does not preserve the gap's value.
4. Imports are at the [foundation review](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-REFLHI-v5-foundation-claude-v1.prompt.note.md) §C scope (with I.10/I.11 for the unrelated claims there). A pattern is any proper nonempty subset of all k runs, including empty runs. The later bindings S1/m1–m7 do not change W/2.1/2.2.
5. In SIGN case3, adjacent indices of J in the k-cycle belong to one stretch interior, because endpoints are excluded and m0>=1. Independence in the path interiors therefore implies independence on the original cycle.
6. Read the marked set E as Z and the flipped set F as Phi, to distinguish them from E(P), reflection count F and pattern families F_m.
7. In SIGN case2, m0>=U0+1>=4, so same-parity stretches are nonadjacent. Exactly 2f boundaries disappear because each boundary touches at most one flipped stretch.

## Verification boundary
- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-RP-LIFT-codex-v1.prompt.stdout.txt) `9277d7387897007ef03bd7b7fb3d89317c274f2079766b865fa2e73447e01eeb`: observed gpt-6.1-sol, max; ACCEPT-WITH-FIXES, 0 FATAL/0 MAJOR/1 MINOR.
- [Claude](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-RP-LIFT-claude-v1.prompt.note.md) `abb1d1a8da8efe4a1d410151ad41d0c1f5296e227c3a59251aeee3677baa0367`: observed claude-opus-5-5, max; ACCEPT-WITH-FIXES, 0 FATAL/0 MAJOR/7 MINOR. Both reviewed the complete written proof without tools.
- Parent read the complete candidate and checked: the even-lift parity equivalence at E=0,p; coordinate-minimum connectivity including the wrap constraint; uniqueness of h_i in an interval shorter than 2p; complement cancellation; nonnegative LIGHT coefficients and exact sign-change counts in all SIGN cases. The original increasing-order avoidance definition was read directly. No finite samples are proof premises.
- W/2.1/2.2 remain imported accepted statements; this review did not re-prove their entire historical dependency chain.

## Exact progress and remaining targets
For every p>=11 this theorem covers the previously unresolved written band R=p, 2<=kappa<ceil((p+1)/4), any B. Together with accepted I.14 it covers every residual all-odd R=p cell 2<=kappa<=p-1, without borrowing FP-1's diversity condition. This is a coverage increase relative to the lane, not a published-SOTA claim.

The theorem does not cover (5,2), (5,3), (7,3); those remain outside this universal written coverage (FP-1 retains only its conditional exclusions). It says nothing new about R>p. REFL(p), REFL-HI(p), RES-HI(p), INV*(p) and ordered Olson remain OPEN. The independent priority/applicability screen is pending; no novelty or major-result designation follows from this correctness verdict.
