# Olson reflection: RP-2NE (delta=1,2)

Recorded at 2026-10-19T09:02:07-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** Written theorem relative to the accepted W/Fact2.1/P0 and generic CONNECT/LIGHT interfaces. No finite calculation, Lean, novelty or full-target claim.

## Exact theorem
Let p>=5 be prime and delta in {1,2}. A word of length4p-2 over D_(2p) with exactly R=p+delta rotations, all in one nonzero pair {rho_x,rho_-x}, has an increasing-original-index identity subword of exactly2p letters if every maximal cyclic CONSTANT reflection block is odd and
    delta+1 <= kappa=p-1-sum floor(l_i/2) <= floor((p-delta-3)/2).
Any B; no purity, B<kappa, inherited or reflection-value assumption. The nonempty ranges start at p11: delta1,2<=kappa<=(p-5)/2; delta2,3<=kappa<=(p-5)/2.

[Proof](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-RPdelta-two-neutral-v1.md) `e6471758f0e5aaba016286ccfb0e901ecb5fc670b980728407c9bbd468c8fa20`; [frozen review](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-RP2NE-review-freeze-v1.json) `093d39e8d657ec5805490e78d4d5680494658d6a01a331d5bbe3b706c8b485fc`.

## Binding readings (all5 Claude MINORs)
1. e(x) means the UNIQUE even class modulo2p congruent to x modulo p, equivalently (p+1)*x modulo2p. Not an arbitrary additive isomorphism.
2. Use RP-LIFT bindings1,3,4,6. The new interval[1,M-1], E in[0,R] and fixed-window calculation replace its R=p-only binding2; generic stretch facts for bindings5,7 are re-proved in SIGN-2Z casesC/B. Never assert E<=p here.
3. Cite P0 directly: [K0star-r2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/proof-K0star-r2.md) lines73–75, accepted at verdict879aeee7 and carried into v5. Fact2.2's proof uses the same P0 step, but its statement alone does not give o_R>=2p-R.
4. SIGN-2Z: let z<=2 be the NUMBER of zero increments; there EXISTS a sign vector with2m cyclic changes, L<=m<=U, satisfying the strict signed-sum bound. The marked set has e>z; weakening it to e>=z is not accepted.
5. Same-parity stretches in caseB are nonadjacent: their indices differ evenly modulo2m0, neighbours differ by+-1 and m0>=U+1>=4. Exactly2f boundaries disappear.

## Parent check and reviews
Parent read the complete164-line proof and directly checked P0's original inequality F+sum floor(r_i/2)<=3p-2. The ensuing o_R>=M=p-delta, z<=v<=delta, and g_E-z>=2(kappa-delta)+(v-z)>=2 use no rotation purity. The fixed CRT window and edge-lift uniqueness retain modulus2p; no enlarged RP-LIFT theorem is assumed. SIGN-2Z caseC has n-2f>=M-2-2kappa>=1, so its strict coefficient remains positive. CaseB uses S>=2m0-z and m0>U; caseD needs S>k from e>z. Parent also read exact range differences and the excluded (delta,kappa)=(2,2) case. These are written proof checks, not runtime tests.

- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-RP2NE-codex-v1.prompt.stdout.txt) `75f0fa0232f83281ba0cb6d3b6e6ab2384cec7e44468d48933930f0b47b03bcf`: observed gpt-6.1-sol/max, ACCEPT0F/0M/0m.
- [Claude](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-RP2NE-claude-v1.prompt.note.md) `f1a8237c7be4774d65dfa801c09467c7e7f5a65ea61de5f1b8fd62ebdc0344ea`: observed claude-opus-5-5/max, ACCEPT-WITH-FIXES0F/0M/5m. All fixes above are wording/citations and change no range.

## Exact additional coverage versus I.14 numerical bands
- delta1 adds [2,min((p-5)/2,ceil((p+5)/4)-1)].
- delta2 adds [3,min((p-5)/2,ceil((p+8)/4)-1)] union {(p-5)/2}, counting overlaps once.
- p11 new cells: delta1,kappa2/3; delta2,kappa3. p13: delta1,kappa2/3/4; delta2,kappa3/4.
This comparison is only against accepted I.14 universal numerical bands, not every structural criterion or any pending RPdelta/SEG-k/B package and not published SOTA.

Not covered: kappa<=delta (including delta2,kappa2), kappa>=(p-3)/2, delta>=3, or the empty small-prime ranges. The auxiliary sign estimate's equality cases are not actual avoiding words. REFL(p), REFL-HI(p), RES-HI(p), INV*(p) and ordered Olson remain OPEN. The referee's optional delta1 upper-endpoint suggestion is outside this theorem and requires its own proof/review.
