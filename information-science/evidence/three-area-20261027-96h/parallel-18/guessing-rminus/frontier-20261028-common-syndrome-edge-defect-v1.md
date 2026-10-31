# Common-syndrome gap is bounded by the missing edge information

**Status: WRITTEN with an exact rational certificate; scientific review pending.** This is the corrected unconditional consequence of the common-syndrome dual. It is not a two-syndrome no-go.

Let `X` be any finite original-neighbour FD law, and let `S` be any common value of all ten ordered triangle-factor syndromes, with the property that each triangle's syndrome determines `S` and that, conditional on `S`, any two components of each triangle determine the third. This includes a common binary XOR syndrome and arbitrary finite common group-valued factor syndromes. Then

\[
\boxed{\quad
\Delta(X)\le\frac{127}{984}\left[
H(X_3\mid X_{1,2,8,9},S)+
H(X_4\mid X_{1,5,8,10},S)\right].\quad}\tag{35}
\]

The two terms measure exactly the information about `X_3` and `X_4` that might be supplied by the original edge `3--4` beyond their triangle neighbours and `S`. In particular, if both vanish, the original dual proves `Delta<=0`. No claim is made that these terms vanish for an arbitrary original FD law.

## Proof from the pinned dual

The required pre-source erratum `frontier-20261028-two-syndrome-local-neighborhood-erratum-v1.md` SHA-256 `8ff79f6d07b935025e0b2f3de27928f030d251787724b64e05ccd9f1f012a37f` explains the missing edge premise. Under the common-syndrome hypotheses, every factor syndrome recovers `S`; original FDs therefore make `S` a function of every neighbourhood. Each triangle determines `S`, and the tensorized conditional triangle inequality makes the certificate's gate `G_S<=0`. All original graph-FD rows vanish, and all local-triangle FD rows vanish except possibly those at vertices 3 and 4, where the original graph has the extra edge.

In `frontier-20261028-two-syndrome-all-factor-dual-v1.json` SHA-256 `a8f6822f2c3e3a8e0b0fd639a9b0095a8ea6f38c7833f0ef2fb6551fa9bba087`, the representative local row at vertex 3 has coefficient `127/492`; its orbit under the four checked factor-preserving automorphisms is `{3,4}` with multiplicity two each. Its averaged contribution is therefore exactly `127/984` times the sum in (35). The local representative at vertex 6 has orbit `{6,7}`, and those local neighbourhoods equal their original graph neighbourhoods; the representatives 1 and 2 likewise have no defect. Every remaining elemental Shannon term has a negative coefficient. The independent exact dual checker receipt SHA-256 `8bd6527e81cd17c9a950d24a7e6f67e8ce29cb0d1f4af4ac7e34c570425f221d` establishes the full coefficient identity and orbit group. No actual distributional realization, new unrestricted numerical bound, proof-assistant formalization, or novelty clearance follows.
