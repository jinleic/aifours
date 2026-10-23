# Olson: terminal k=p+1, kappa-hat=p-1 is impossible

Recorded at 2026-10-19T13:29:48-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL**, written mathematics relative to accepted NF, GRX, CT at its explicit full scope and RS(b), with classical Cauchy-Davenport (also through CT/RS(a)). No Lev, S(p), index-one, REFL or pending candidate is a premise.

## Exact accepted statements

1. **PP1-EXCL:** for primep>=7, no length-(4p-2) avoider over D_(2p) has SOME admissible normal form with terminal k=p+1 and kappa-hat=p-1. An avoider means no increasing-original-index identity2p-subword. No o_F or run hypothesis is imposed on the original word.
2. **PP1-EXCL-prime:** no such avoider word u has a cyclic representation with p+1 singleton reflection blocks, possibly empty rotation runs, and every empty run separating different reflection values. This word-level statement implies item1 by NF.
3. **EXCL-PM:** item2 under the additional hypothesis that all rotation values lie in one nonzero pair {c,-c}; its only imported criterion is GRX. This is an independently proved conditional alternative, not a pending premise of item2.
4. Lemmas W, CL, OM/OM', SR and ER at their printed local hypotheses, read with the [parent erratum](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-PP1-EXCL-parent-erratum-v1.md) `722f27ac7e5eea5e1ea334796f0c438e19c7a7ef2f35a9fcd8f989a68e249da1`.

## Frozen evidence and reviews

- [Proof](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/terminal-pplus1-exclusion/proof-PP1-EXCL-v1.md) `6fea2fd20ba4d13fb1cf972927da379556b1f33ea18a8ea661740705c80944d0`; [scope](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/terminal-pplus1-exclusion/PP1-EXCL-scope-v1.md) `d386f94414f0bdcbd44694d9676b836da511daa5c923200ff9375db977e32fba`; [review freeze](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-PP1-EXCL-review-freeze-v1.json) `a20e53091e4d41443abd7b9ead070fabee29e580d78218c9f5af97044cf47c79`. The parent verified six worker-file pins and all17 source ranges; the route's mental pre-freeze sketch is disclosed, so no blind preregistration claim.
- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-PP1-EXCL-codex-v1.prompt.stdout.txt) `073ec9547be474ca2bc43e72d404474d9ae6e3b6cb7ef1cbb63c54aa448d1bf3`: gpt-6.1-sol/max/read-only, all three theorems and supporting steps ACCEPT, 0 FATAL/0 MAJOR/0 MINOR.
- [Claude](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-PP1-EXCL-claude-v1.prompt.note.md) `ac7455cf3a0904f3bed67b0c5c4c7a73100c20f945bd409d4552768b90aa25d7`: claude-opus-5-5/max/no tools, all three theorems and mathematical steps ACCEPT, 0 FATAL/0 MAJOR/5 MINOR plus optional o6. Mandatory five findings disposed by the parent erratum; no main-proof repair.

## Parent checks

NF gives H-hat=0, F=p+1 and R=3p-3. GRX gives delta=p+1-Phi, C_max=Phi, so C=Phi exactly. The two-change signed window has p consecutive feasible q values when each sign has >=p-1 occurrences. CT at kappa=p-1,n=p-3 has |Y|-n=2p; its truncated bound leaves H1/H2a/H2c. The omission argument uses distinct free occurrences and plus-side fillers; SR counts N+alpha_i-beta_i nonzero deviations. H2a/H2c exhaust too many non-a letters across >=p runs. H1 with a=0 uses an equal-block-value arc; H1 with a!=0 forces two empty runs. ER's adjacent and nonadjacent patterns respectively force a forbidden zero tau or missing residue r0=0. These were independently re-derived in writing before review (freeze records details); no finite computation or Lean replay.

## Relationship to ROT-SING+

The precise antecedent of ROT-SING+ (p>=7, length4p-2 avoider, SOME admissible NF k=p+1,kappa-hat=p-1) is now impossible. Its conclusion is consequently vacuous **only under that antecedent**. This does not accept the ROT-SING+ proof and does not exclude its multiset in other normal-form cells. Its unlaunched second-family review may be disposed as superseded by this stronger dual-reviewed statement.

## Open

Other terminal cells, o_F>p reflection/word assembly, unrestricted INV* and full ordered Olson remain open. KP2 and upper-half targets have separate pending proofs. No p=5, existence, novelty/priority, Lean or human-referee claim.
