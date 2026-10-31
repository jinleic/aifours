# Addendum 1 — the one-copy separator is redundant in the full source LP

This additive correction applies to `frontier-20261028-one-copy-separating-inequality-v1.md`, SHA256 `1d5cb24c9dfb38248bdc8d32ead3818288f77b8cc8494501ee03963ce7d92d27`. Its universal inequality, exact partial-core separation and fixed-base nonextension claims are unchanged. Its final suggestion to test L and graph-symmetry images as a way to improve the **same full publisher LP** is withdrawn: those rows are already implied there.

The 48-row exact certificate has 33 elemental conditional mutual information inequalities in the source’s **full first eleven-variable copy branch** and 15 of that very branch’s copy equalities. The full source LP imposes all those CMI rows and copy equalities, so their verified nonnegative combination gives `L>=0` automatically. For the graph-symmetric base slice, every graph-automorphism image has the same value as L and is also redundant. Adding L or its images cannot lower the full source LP optimum.

This does not undo the exact value `L(h*)=-1/276`, the separation of the weaker partial-coordinate/F_n relaxation, or the proof that that particular original-variable profile has no valid first-copy Shannon extension. It does not show that the full source LP is entropically tight or that other copy structures, extra valid inequalities or different base profiles cannot improve the original bound.

Main reports a disjoint f59 review of the complete certificate with verdict 0 FATAL / 0 MAJOR / 1 MINOR (this redundancy qualification). The proof of redundancy above follows directly from the independently checked row types; the review’s own body has not been re-opened here. No new bound, novelty, formal/human or cross-model acceptance is claimed.

**END OF ADDENDUM 1.**
