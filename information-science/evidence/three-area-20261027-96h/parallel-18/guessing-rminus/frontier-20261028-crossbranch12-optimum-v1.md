# The source LP remains tight after coupling branches 1 and 2

**Status: WRITTEN with independent exact primal checks and the matching published dual.** This is an additive strengthening of `frontier-20261028-full-source-lp-optimum-v1.md` (SHA-256 `08af469a09689dcdf40b07bbb086c851349141f582b92714b92d5a7eef63fcdd`). The larger LP defined below also has exact optimum `1847/276`, including the stated original-variable all-order `F_n` family. It remains an outer relaxation: no entropic realization or unrestricted guessing-number improvement is claimed.

## Larger LP and valid coupling

Use the graph, caps, original FDs, automorphism symmetries and copy protocols of the preceding packet. Let `X=(a,b,c,d,e,f,g,h,i,j)`, `U=b'0` be the auxiliary of source branch 1, and `V=(d'1,e'1,g'2)` be the three auxiliaries of source branch 2. Replace the publisher's separate 11- and 13-variable elemental systems by **all** elemental Shannon inequalities on the combined 14-variable set `(X,U,V)`. Also impose

\[
I(U;V'\mid X)=0\quad\text{for every nonempty subtuple }V'\subseteq V.
\]

These are valid for a joint entropic extension: first retain the original law of `X`, then sample the complete conditional branch-1 and branch-2 auxiliary kernels independently given `X`. This leaves each branch's original/copy marginal unchanged and makes `U` independent of the whole of `V` given `X`. It is sufficient in fact to impose independence of the whole `V`; the seven subtuple equations make the exact check explicit.

Source branch 3 `(X,f'3,g'3,h'4)` remains a separate full 13-variable Shannon/copy system with the **same** original `X` profile. No Shannon inequalities mixing branch 3 auxiliaries with `U` or `V` are included. The augmented LP has `23,551` distinct nonempty coordinates, namely `2^14-1 + 2^13-1 - (2^10-1)`.

## Matching exact primal and upper bound

The common original profile is again the 1,023-original-coordinate projection of `frontier-20261028-separator-bound-primal.json`, SHA-256 `aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651`; all singleton values are 1 and the objective is `1847/276`.

* Coupled 14-variable rational primal: `frontier-20261028-crossbranch12-exact-candidate.json`, SHA-256 `1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739`.
* Separate branch-3 rational primal on the same original profile: `frontier-20261028-affine-exact-branch-3.json`, SHA-256 `fd53af75dfa47e9eb03af60fb9704d89719ba8720ddf6aeb192533bcb44c4cd0`.

Separate exact verifiers check all **372,750** 14-variable elemental Shannon inequalities, **899** branch-1/2 copy equalities, **7** cross-branch independence equalities, all original caps/FDs/symmetries, and all **1,052** applicable publisher rows. For branch 3 they independently check all **159,757** elemental Shannon inequalities, **1,282** copy equalities and all **1,372** applicable publisher rows. The combined verifier merges only the shared original profile, checks all **1,920** publisher rows exactly tight and revalidates the publisher's exact signed dual. Thus the augmented LP has a primal attaining the published dual upper bound `1847/276`.

The exact all-order base receipt from the preceding packet still applies: all `13,729,980` disjoint original-variable `A,B,C,D,Z` substitutions of `F_n` hold for every positive integer `n`. Adding this infinite family as well does not change the augmented LP optimum. It does not cover overlapping substitutions, new copy protocols or source-branch-3 cross constraints.

**Old partial-point boundary:** only the 1,023 original coordinates of the older 4,397-coordinate file are fixed. Among old auxiliary coordinates also present in the coupled candidate, **247 of 1,372** differ; in branch 3, **460 of 2,002** differ. The result is not a completion of the older partial auxiliary assignment and does not undo prior nonextension findings about it or other saved points.

## Evidence

* Coupled producer `frontier-20261028-crossbranch12-exact.py` SHA-256 `544f598dae4ddd529f2635c74be4caa2827a1feaaea617f4712a8b6e8633a7d8`; it used IPM only for a proposal, followed by exact affine reconstruction. Its exact candidate is independently checked; float status is not the proof.
* Independent 14-variable checker `frontier-20261028-crossbranch12-independent-check.py` SHA-256 `1249cc1692dcc8d76b62094d3c5ef66f274dda899632f9090195d543a962b2a5`; receipt SHA-256 `371ed6d0da680cdbacf36704f61f7d1888b800a5489470c9c36512811df9a86e`. It rebuilds graph, all elemental and copy forms, the seven cross equations and source rows, and rejects six intended mutations.
* Branch-3 independent checker `frontier-20261028-branch23-exact-independent-check.py` SHA-256 `dbed7ff9de6cd8c3693b0086509540eb06df3cc60c21f7e5549cbc4cfa4be78e`; receipt SHA-256 `24632017c2defe3aea5debb8f4a1b8541bbe38a87804ce3e1d708bed31373ea2`.
* Combined source/primal checker `frontier-20261028-crossbranch12-combined-check.py` SHA-256 `990e01192011cfaa09ca154df26fca9d65cfba8cad4da995f960fc20de4da6d7`; receipt SHA-256 `c264898b6eed1c5e3500f75088a4ae2b2e4ccb8985bb6d8938483e6fa0a37502`. It binds both branch receipts, all 1,920 source rows, the published dual and the all-order base receipt; three mutations including a cross-only coordinate are rejected.

No proof-assistant check, cross-model review or novelty clearance was performed. The exact primal has balance gap `7/276` as an LP point, not as a known probability law. New copy structures, mixed constraints involving branch 3 and actual strict-gain laws remain open.
