# An all-syndrome inequality with no local-factor defects

**Status: WRITTEN with an exact checked coefficient identity; scientific review pending.** This bound applies to every original-neighbour R-minus FD law in the ten finite-group triangle-factor encoding, with **arbitrary** syndrome support size. Let `S=(sigma_1,...,sigma_10)` be the entire vector of ordered factor products, `D_N` the positive weighted automorphism average of `H(S|X_{N(v)})` in the pinned certificate, and `D_T` the corresponding weighted average of `H(S|X_T)` over its listed triangle rows. Then

\[
\boxed{\quad
381\Delta(X)+74\sum_v I(X_v;S)
\le111H(S)+492(D_N+D_T).\quad}\tag{40}
\]

No two-syndrome result is used, and the number of group values, groups and correlations are arbitrary. Because `S` is a function of the whole vector `X`, this is a concrete original-law inequality, not an assumed auxiliary coupling. The nonnegative terms `D_N,D_T` may be large and it does not by itself prove `Delta<=0` or improve the known numerical guessing-number upper bound.

## Proof

The exact all-functional-auxiliary inequality (39) in `frontier-20261028-functional-syndrome-defect-bound-v1.md` SHA-256 `d21ee79e797d278f76a0f65ab7d27514f28c4b7442ea1fe18df83e6b2372b58d` includes a third nonnegative term `D_L`, formed from `H(X_v|X_{L(v)},S)`. Here every factor product is known from the full vector `S`, and the other two components of each triangle are present in the local triangle neighbourhood `L(v)`; group inverse formulas determine the missing component even for nonabelian groups. Therefore `D_L=0` identically and (40) follows. This is the explicit component argument in `frontier-20261028-two-syndrome-local-factor-decoder-v1.md` SHA-256 `684a0486da79bf262c2b4f0bc037594c73582b06eb219f03d608c52ddcb82dba`, with the selector generalized from one bit to the full syndrome vector.

The underlying coefficient identity has 319 CMI terms and the exact independent checker receipt SHA-256 `8bd6527e81cd17c9a950d24a7e6f67e8ce29cb0d1f4af4ac7e34c570425f221d`; positive defect coefficient signs are checked in receipt SHA-256 `1588f967e6ce4027c814ac4f9d1f89063fa6e2db21e3ac629201971a0d36081e`. The earlier missing-local-FD erratum SHA-256 `8ff79f6d07b935025e0b2f3de27928f030d251787724b64e05ccd9f1f012a37f` is resolved here by the explicit actual-component decoder, not by inferring the missing edge away.

Conditioning on the full syndrome also gives the independent fixed-factor tensorization gate `3Delta+2 sum_v I(X_v;S)<=3H(S)`. Both gates hold simultaneously, but (40)'s neighbourhood/triangle defect terms prevent a general no-gap conclusion without additional information. Neither a new strict-gain law nor a general original guessing-number upper bound is claimed.
