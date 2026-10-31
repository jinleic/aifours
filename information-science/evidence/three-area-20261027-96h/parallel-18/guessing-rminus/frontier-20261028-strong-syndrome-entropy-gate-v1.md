# An unproved stronger two-syndrome information gate

**Status: OPEN conjecture; no proof or counterexample.** Under the finite-group triangle-factor hypotheses and at-most-two-syndrome condition of `frontier-20261028-two-syndrome-repaired-theorem-v1.md` SHA-256 `9feb6cd50a2b376b971c2091369b5c5ad7d50e18446ce4cd3293bfc718b776b1`, let `S` denote the full syndrome vector and `X_v` the original vertex triples. The tempting candidate inequality is

\[
3\Delta+2\sum_v I(X_v;S)\ \stackrel{?}{\le}\ 2H(S).\tag{45}
\]

If valid, it would strengthen the direct fixed-factor conditional-tensorization gate `3Delta+2 sum I(X_v;S)<=3H(S)` for this class. It is not established here and does **not** by itself bound arbitrary syndrome support or the unrestricted guessing number.

## Why the direct route fails

Fix a syndrome value `s` with positive probability and a factor index `t`. Let `Y_t` be its three group components and `Z` the tuple of all other factors. Condition first on `(S=s,Z=z)`. The original graph FDs then restrict the three active components to graph FDs on that one triangle: all other components are fixed and may be supplied as constants to the original decoders. Since a syndrome value is also fixed, the component law has arbitrary fixed-product support. The pinned proper-subgraph Shannon inequality implies `H(Y_t|S=s,Z=z)<=2/3 sum_{v in T_t}H(X_v^t|S=s,Z=z)`, so the individual triangle-factor entropy deficit

\[
D_t(s,z)=2\sum_{v\in T_t}H(X_v^t\mid S=s,Z=z)-3H(Y_t\mid S=s,Z=z)
\]

is nonnegative. However, this alone merely reproduces the coefficient `3H(S)`. To prove (45) one would need additional information that the original law obeys `sum_v I(X_v;S)>=3H(S)/2`, or an equivalent bound on the conditional factor deficits. The previously constructed rare-syndrome example `frontier-20261028-rare-syndrome-mi-counterexample-v1.md` SHA-256 `5caa8b5bf3f33536439cfbd60984b062e4a55268d8d002cb69a48a3a5dcad405` **disproves** that mutual-information premise for general original graph laws, including a law with at most two syndromes.

Therefore (45) is **not established**, and no implication of this paragraph is an adopted theorem. The true two-syndrome conclusion `Delta<=0` and the ordinary coefficient-3 gate, both separately proved subject to review, remain unaffected. Any stronger coefficient-2 inequality requires a direct proof or an explicit counterexample, not merely the repaired theorem.
