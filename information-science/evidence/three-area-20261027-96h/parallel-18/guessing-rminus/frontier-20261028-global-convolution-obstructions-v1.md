# Two further explicit global amalgams fail Shannon

**Status: WRITTEN-checked-in-kernel, two fixed representations only.** Both constructions start from the same rational original vector and the two pinned 14-variable star profiles in `frontier-20261028-global-parallel-sum-obstruction-v1.md` (SHA-256 `b3325969993e8a6275660af021eb6806a997aa8bdb78d1013f2582fa004e1718`); they preserve both star marginals exactly. Put `B=(X,U)`, with `U=b'0`, and `V,W` as in that packet.

1. The common-superset convolution
   \[
   h(S)=\min_{S\cap B\subseteq T\subseteq B}\left[h_{BUV}(T\cup(S\cap V))+h_{BUW}(T\cup(S\cap W))-h_B(T)\right]
   \]
   has `I((U,V);W|X)=0`, but violates **44,275** of the 4,456,465 elemental 17-variable Shannon rows. In particular `I(i;j | a,c,d,e,f,d'1,e'1,g'2,h'4)=-26317/215625`. Exact checker `frontier-20261028-global-min-convolution-check.py` SHA-256 `49fbb2694c3847bc15d6061cdc046ecafe800a52843cca0f6cc9e3f24b352137`, receipt SHA-256 `3d02955d44c2a7ab5b3aab86addb53cc8f6f98ac6f2760f7c75f4f8227cc1232`.

2. The common-partition convolution
   \[
   h(S)=\min_{T\subseteq S\cap B}\left[h_{BUV}(T\cup(S\cap V))+h_{BUW}(((S\cap B)\setminus T)\cup(S\cap W))\right]
   \]
   violates **427,891** elemental rows and has `I((U,V);W|X)=-11899103/6900000`. Its worst recorded elemental slack is `-217/276`. Exact checker `frontier-20261028-global-partition-convolution-check.py` SHA-256 `71e3124bc04ae1cc54067c86cc63be9aa622657e6839a32e74756c1ce23f1e4c`, receipt SHA-256 `39c790bf211cdcb2b1422f461acc8f2d3cdf2732e01eba2327fae78232a902a5`. Python emitted a `SyntaxWarning` for the backslash in the human-readable construction string; its displayed text and exact integer computations were nevertheless produced as recorded.

These are two explicit failed formulas, not evidence against every global Shannon extension or any original FD law. No scientific review, formalization, or novelty claim is made.
