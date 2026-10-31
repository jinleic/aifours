# Conditional local-triangle decoding for a two-syndrome mixed block

**Status: WRITTEN; scientific review pending.** This is the key missing input in the attempted unrestricted two-syndrome proof, and supplies a possible repair **without** assuming the original extra edge `3--4` is absent.

Fix any set `J` of the ten triangle factors and two syndrome vectors whose XOR difference is `1_J`. Condition on the full tuple of every factor outside `J`, obtaining selected-factor vertex blocks `Y_v`. Translate the selected factor parities so that each equals the same selector bit `S`. Then for every vertex `v`, regardless of `J`,

\[
H(Y_v\mid Y_{L_J(v)},S)=0,\qquad
L_J(v)=\bigcup_{t\in J:v\in T_t}\left(T_t\setminus\{v\}\right).\tag{36}
\]

Indeed, for each selected triangle containing `v`, its bit at `v` is the XOR of the other two triangle bits and `S`. All those other factor components appear explicitly in `Y_{L_J(v)}`. This is an actual componentwise decoding identity, not a graph-FD consequence, and it holds with arbitrary support probabilities and correlations. `L_J(v)` is contained in the original neighbourhood, but can be strictly smaller.

## Interaction with the gap-preserving lift

If `J` covers every vertex, the previously written lift in `frontier-20261028-two-syndrome-global-entropy-bound-v1.md` SHA-256 `4fcbf234c2710ee91c8a5e0a9b0b79414bb97438be7986468094d8e2230b2bf9` appends independent uniform triangle-bit factors with common parity `S`, preserves `Delta` on each fiber, and yields an augmented law where the analogous full-factor `H(X_v|X_{L(v)},S)=0` holds by the same explicit decoder (36). The lift's recovery of `S` from original neighbourhoods follows from the selected original FD plus `J` covering, as in that packet.

Thus the all-factor rational dual's formerly missing local-triangle FD rows do vanish **for these actual triangle-component laws**, though not for arbitrary original-neighbour FD laws with an abstract auxiliary. This addresses the specific extra-edge objection in required pre-source erratum `frontier-20261028-two-syndrome-local-neighborhood-erratum-v1.md` SHA-256 `8ff79f6d07b935025e0b2f3de27928f030d251787724b64e05ccd9f1f012a37f`. A complete repaired theorem must explicitly incorporate this observation, re-check every hypothesis and independently review the lifting, conditional tensorization and all source corrections; this note does not by itself adopt or reassert the withdrawn theorem. The unrestricted auxiliary-defect inequality remains valid without (36), where its local defects need not vanish.
