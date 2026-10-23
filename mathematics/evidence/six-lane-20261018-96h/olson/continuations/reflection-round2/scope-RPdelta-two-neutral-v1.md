# Written continuation: at most two neutral-even increments

Frozen after /bin/date observation 2026-10-19T08:36:32-0700.  Owner OlsonReflectionSuccessor.  Continues the authorised
R=p+delta small-kappa analogue; not another target slot.  No computation, models, tests/builds or launches.

Accepted RP-LIFT verdict read in full and SHA checked:
RUN/review/olson-RP-LIFT-parent-verdict-v1.md,
e90b8be22a7bc06b0c20e305274436ceb48784e5a1844005437058d04dff8652, with all seven binding readings.
It accepts the original R=p theorem only.  Its CONNECT and LIGHT lemmas are used within their literal general
combinatorial quantifiers; the changed R>p fixed window, integer lift, and zero-increment sign argument are NEW proof
obligations, not an automatic consequence of that theorem.  Accepted W/Fact2.1/Fact2.2/P0 remain at verdict13ee1ba8 scopes.

Exact bounded target: delta in {1,2}, kappa>=delta+1 and 2kappa<=p-delta-3, word length4p-2, R=p+delta rotations in one
nonzero pair, every maximal cyclic constant reflection block odd, any B.  Prove solvability without the 'no neutral even
run' assumption of conditional-RPdelta-smallkappa-v1.md (88aada7e...b227).

Plan: a zero alpha_i=e(theta_i)-d_i in C_2p is confined to a nonempty even run.  P0 forces at most delta such runs, hence
at most two zero integer increments.  Pair count gives g_E-z>=2(kappa-delta)>0, where z counts zero increments.  Extend the
SIGN lemma with z<=2 and a larger set of nonzero even increments (g_E>z); write every inequality including Case3's strictly
positive LIGHT coefficient.  The old conditional note remains unchanged and is not an import.

Success: a complete new candidate excluding all parameter cells in this exact target, especially delta=1 at
2<=kappa<=(p-5)/2 (including p11,kappa2), or a precise failure of the proposed zero-increment SIGN lemma.  No claim outside
the target, no promotion of RPdelta review-package candidates, no novelty/Lean/full-REFL assertion.
