# The final equivariant-bicover three-syndrome color class

**Status: WRITTEN with exact 198-row rational certificate; conditional on the repaired two-syndrome theorem; independent scientific review pending.** In the q=8 binary triangle-factor original-neighbour FD model, assume the full syndrome takes at most three states and each factor parity is a nonconstant function of them. After fixed parity translations and state relabeling, suppose the three one-hot factor-color classes are

\[
\boxed{\quad\{1,2,10\},\quad\{3,6,8\},\quad\{4,5,7,9\}.\quad}\tag{58}
\]

Then every such joint FD law has `Delta<=0`, and every uniform FD support has at most `2^20` words. This is the seventh and last partition in the restricted equivariant-bicover census `frontier-20261028-three-syndrome-equivariant-census-v1.md` SHA-256 `8125a855eef1e59d2f52831a51ba1d9162be27cf70a2ad7c67087476103b971a`; it is not a no-go for all three-syndrome laws or a new unrestricted bound.

## Certificate and prerequisites

The graph-FD, local-component decoder, one-hot entropy, and state/indicator visibility premises are the same as in `frontier-20261028-three-syndrome-equivariant56-theorem-v1.md` SHA-256 `12de70c68bf009c53c9518d18416a5ddf4bb5ebf538886a989d1617e735817c3`. In particular each vertex sees at least two factor colors, so the original-neighbour tuple determines the full syndrome; each triangle exposes its own one-hot indicator; and the full syndrome determines each local triangle component. The required earlier local-FD erratum SHA-256 `8ff79f6d07b935025e0b2f3de27928f030d251787724b64e05ccd9f1f012a37f` is respected by using actual component equations, not by assuming graph FDs imply the stronger local FDs.

The identity uses one indicator conditional-gap gate. This gate is valid if the repaired two-syndrome theorem `frontier-20261028-two-syndrome-repaired-theorem-v1.md` SHA-256 `9feb6cd50a2b376b971c2091369b5c5ad7d50e18446ce4cd3293bfc718b776b1` is valid, because conditioning on one indicator leaves at most two syndrome values. Thus this theorem is explicitly **conditional** on that written candidate and its independent review.

The exact identity `frontier-20261028-three-syndrome-color4-equivariant-dual-v1.json` SHA-256 `7b7af573da508f314674a9eb3bbd21af65717946a2537f22877223d4a8744e62` uses 121 elemental CMIs, 26 indicator-refined CMIs, 21 data-processing rows, 5 pair-subadditivity rows, 3 one-hot inequalities, the single indicator gate and 21 exact FD/visibility rows. It is averaged over the four graph automorphisms **together with their induced state-label permutations**. The independent checker `frontier-20261028-three-syndrome-color4-equivariant-dual-check.py` SHA-256 `b1f8bc2c54df10e67af3a5044436f18856a0f185dbc83be8faf29ed5df9979bd`, receipt SHA-256 `3d0efa8a33b620a1a90bdd32f58f8e856b9455664d45c9a19418b0c4a9c9846d`, validates all 5,119 entropy coefficients, action closure, color/graph incidence, row signs and changed-target/changed-sign controls exactly. The numerical LP was only a proposer and is not part of the proof.

Scientific review, formal proof and novelty clearance are not claimed. With the six prior exact candidates and the finite seven-partition census, this completes only the stated equivariant-bicover family, conditional on the above import; all non-equivariant, constant-factor and non-bicover three-syndrome cases remain open.
