# A vertex needs only its incident syndrome functional for local component decoding

## Required first inputs

Read `frontier-20261028-full-source-lp-optimum-v1-erratum-1.md` first (SHA-256 `c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9`). The actual binary factor encoding is the one in `frontier-20261028-triangle-code-global-obstruction-v1.md` (SHA-256 `bdf79fd631e8e58a734a4ef4c93f899e319f45712a219a876f527b52f1d61bb4`). The selected-factor fiber and fixed-factor tensorization are those of `frontier-20261028-syndrome-cover-entropy-gate-v1.md` (SHA-256 `d6df004e025f067a14a6cc69e9aef8d9fc78a20a2fc49c4e431328120e32014b`).

**Status: WRITTEN elementary decoder identity.** No held review, two-syndrome entropy theorem, or functional-fiber Delta gate is an input. This is a new explicitly checked premise for actual component laws; it is not a consequence of graph FDs with an abstract auxiliary.

## Setting

The ten selected triangle factors are colored by the three nonzero affine-plane linear functionals A,B,A+B, or omitted when their syndromes are fixed. Condition first on the complete tuples of all omitted factors. Let Y_v be the tuple of remaining selected component bits at vertex v, and let S=(A,B) be affine coordinates of the syndrome plane. A selected factor t has parity c_t + l_(color(t))(S), with c_t a known constant.

For a vertex v let J(v) be its incident selected factors and let L_J(v) be the union of the other vertices in those factors.

## Lemma and proof

If the nonempty set of functional colors at v is the singleton {c}, then

H(Y_v | Y_(L_J(v)), l_c(S)) = 0.

Indeed, fix the conditioning variables. For EACH selected triangle through v, its other two component bits are coordinate projections of the available vertex tuples Y_(L_J(v)). Its parity is known from l_c(S) and the fixed offset c_t. Therefore its missing bit at v is uniquely the XOR of those two bits and that known parity. Doing this for every member of J(v) recovers every component of Y_v. This is a deterministic reconstruction for every support point, so it holds for arbitrary probabilities and correlations.

If two or three distinct nonzero functionals occur, the full S suffices as in the old mixed-local row; this lemma does NOT replace it by an arbitrary single functional. If no selected factor is incident, the selected tuple is constant, but that separate noncover case is not needed in the residual covering census.

## Why this changes the previous relaxation

The old functional LP included only H(Y_v | Y_(L_J(v)),S)=0, even at vertices with one incident color. It included visibility of that functional from neighbor/triangle tuples, but not this finer local decoder. Those old rows alone permit the exact twenty counterprofiles. All twenty violate at least one of the new local equalities in exact arithmetic.

The new row is H(Y_(L_J(v))+Y_v,l_c)-H(Y_(L_J(v)),l_c)=0. A checker must recompute J(v) from the actual coloring and require its color set to be EXACTLY {c}. It must not assume that the full vertex tuple is one triangle component, omit the real edge 3-4, or infer a smaller local neighborhood from the original graph FD alone.

A future Delta exclusion requires a separate exact signed coefficient identity with this premise and independent semantic checking. Mathematical review, formalization, novelty clearance and scientific adoption remain unperformed.
