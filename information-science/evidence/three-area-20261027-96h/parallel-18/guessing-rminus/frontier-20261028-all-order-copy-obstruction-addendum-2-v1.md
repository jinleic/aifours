# Addendum 2 — the stronger partial point cannot extend

This addendum corrects the uncertainty recorded in `frontier-20261028-all-order-copy-obstruction-addendum-1-v1.md`, SHA256 `13f21942f6f2ddc8af3f0750b03d366b2c5f950364132e91d8bda461ab667679`. Its exact partial-core feasibility and all-disjoint-block `F_n` checks are unchanged; its sentence that existence of a full Shannon extension was “unestablished” is superseded for **this particular frozen assignment**.

## A one-line exact contradiction

The stronger partial point is `frontier-20261028-source-closure-primal-frozen.json`, SHA256 `97e38946440c30bd2d16e349c2c8e22d69ac133e1831e7f2d6ff913bfd2f2bec`. In the publisher’s second copy branch, define

```
K = {a,b,c,d,e,g,h},       d'1 = the fresh copy of d.
```

Both of the following coordinates are actually present in the frozen point and are exact:

```
h(K)             = 871/138,
h(K union {d'1}) = 0.
```

Every entropic vector, and every full Shannon-polymatroid vector, has `h(K union {d'1}) >= h(K)`. Here the required conditional entropy is `h(d'1|K)=-871/138<0`. **Therefore no choice of the 280954 previously missing row coordinates can extend this particular assignment to a feasible full-source Shannon point.** The conclusion is exact and does not depend on the numerical LP’s status.

This is not a contradiction in the predecessor’s partial relaxation: that partial relaxation included all source-branch *elemental rows individually evaluable from its coordinates*, not every non-elemental Shannon consequence between known coordinates. Monotonicity is a consequence of the full branch’s elemental Shannon constraints, but the derivation can involve missing intermediate coordinates. This distinction is essential.

## Independent two-CMI form

Let `U=h(K union {d'1,f})`, which is **not** one of the frozen 4397 coordinates. Two ordinary source-branch CMIs would force

```
I(f;d'1 | K) >= 0        => U <= 35/92,
I(f;e'1 | K,d'1) >= 0    => U >= 2057/276.
```

The bounds conflict by exactly `2057/276-35/92=488/69>0`. The separately written `frontier-20261028-extension-two-cmi-check.py`, SHA256 `69146fa42adcbfae4be0007e1d867d846bc4d5ed896e5974159595aaca13d3e9`, directly checks each known rational coordinate and the two algebraic bounds; its receipt SHA256 is `f971bf8a989dfd0d6bc2161dfbeeff8a2e4f35873f38c80b24e46800865a6ec5`.

An exhaustive exact scan of every immediate nested pair of **known** branch coordinates found 0 violations among 6554 checked in branch 1, 5 among 9758 in branch 2, and 18 among 14782 in branch 3. Checker `frontier-20261028-extension-known-monotonicity.py` SHA256 `e73c1c10192d8359258612c4424938db1d5468d4a8b9d4601e09fa220339be0b`; receipt SHA256 `25df4da7b321db7e9bd2eb8fd4237d253b51c330db552bf3184728257371a346`. The known-coordinate checking was observed at **Wed Oct 28 17:41:16 PDT 2026**.

The bounded numerical extension screen also returned `Infeasible` for each of the three fixed-coordinate branch models, but its LP statuses are **not used** for the exact nonextension proof above. Its `frontier-20261028-partial-point-extension-result.json` has SHA256 `6fbbf47fda0c3b96b3d9e51052aa37861de64b6e01c61295d407c88fd8878755`; no exact infeasibility certificate is claimed for branch 1.

## Scope

This rules out a full-source extension of **the chosen 4397-coordinate assignment**, including its particular auxiliary values. It does not rule out the same ten-original-variable entropy profile with different auxiliary coordinates, a different full-LP primal, a genuine Boolean/guessing strategy, or an improved universal upper bound. It does not establish novelty, formal/human/cross-model review or original-target resolution. The next materially justified search strengthens the partial LP by actual nested-entropy inequalities rather than repeating the unextendible assignment.

**END OF ADDENDUM 2.**
