# Two additional three-syndrome color-equivariant classes

**Status: WRITTEN with exact rational certificates; conditional on the repaired two-syndrome theorem and pending independent scientific review.** Under the q=8 binary triangle-factor original-neighbour FD model, suppose the full syndrome has at most three states and every factor parity is a nonconstant function of those states. After independent fixed parity translations and relabeling the states, assume the three one-hot factor-color classes are one of

\[
\begin{array}{c|c|c}
\{1,5,8\}&\{2,6,9\}&\{3,4,7,10\}\\
\{1,8,9\}&\{2,5,6\}&\{3,4,7,10\}.
\end{array}\tag{57}
\]

Then every such finite FD law satisfies `Delta<=0`; every uniform FD support has at most `2^20` words. These are two further restricted three-syndrome cases, not a no-go for all syndrome triples or a numerical unrestricted guessing bound.

## Proof and dependency

In each row every vertex meets at least two color classes, so its original neighbourhood determines the full three-state syndrome. Each triangle determines its own one-hot indicator; conditional on the full syndrome, local factor parity equations decode every vertex block from its triangle neighbours. The full syndrome and indicator data-processing/one-hot inequalities are exactly the same as in `frontier-20261028-three-syndrome-threecolor-theorem-v1.md` SHA-256 `e97cc19491b09288dbabf3cb37c4a9fb879f74218bad2f14d39043fa8ec17f9e`, and the required local-neighbourhood erratum SHA-256 `8ff79f6d07b935025e0b2f3de27928f030d251787724b64e05ccd9f1f012a37f` is addressed by the explicit component decoders.

Both exact identities use an indicator conditional-gap gate. It follows only if `Delta<=0` is established separately on every conditional fiber: the indicator-one fiber contains one syndrome value, the indicator-zero fiber at most two. We therefore **explicitly import** the still-unreviewed repaired two-syndrome theorem `frontier-20261028-two-syndrome-repaired-theorem-v1.md` SHA-256 `9feb6cd50a2b376b971c2091369b5c5ad7d50e18446ce4cd3293bfc718b776b1`. These two conclusions remain conditional until that input and the current identities receive independent scientific review.

The first partition uses certificate `frontier-20261028-three-syndrome-color5-equivariant-dual-v1.json` SHA-256 `abfeb0c54d0e093cece96ef82a65bd15f14b6a1c78118b9cf18391c3cbb63ddf` (440 rows); the second uses `frontier-20261028-three-syndrome-color6-equivariant-dual-v1.json` SHA-256 `b115cfe7400e6e11b8787554c4f2a2cf3d005c68ec1c5ce9fdc978bae6be61bf` (461 rows). Both identities average over four graph automorphisms **together with the induced permutation of the three state-indicator labels**; no equality of probabilities between states is assumed, since an inequality is valid before and after any permitted relabeling.

`frontier-20261028-three-syndrome-color56-equivariant-dual-check.py` SHA-256 `c3d1d47ec36cdeab3eecd92e885cce1be0a6841feb0df05ab0b4f172c8910703`, receipt SHA-256 `585949fd97c834aa7c15cb0d399a6a1f8e0b3c72fa4b4455b7b604c15e7657c8`, reconstructs both identities on all 5,119 original/auxiliary-branch entropy coordinates using exact rationals, verifies graph/factor automorphisms, color action and group closure, local decoding and neighbourhood color premises, row signs and two negative controls. The one-hot inequalities and conditional-gate import are written mathematics, not formalized or independently adopted.
