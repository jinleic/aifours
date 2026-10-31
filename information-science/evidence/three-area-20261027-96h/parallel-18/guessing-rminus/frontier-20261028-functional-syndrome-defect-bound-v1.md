# All-variable functional-syndrome inequality with local defects

**Status: WRITTEN; exact coefficient identity independently checked; scientific review pending.** Let `X=(X_1,...,X_10)` be any original-neighbour R-minus FD law and let `S` be **any** auxiliary random variable satisfying `H(S|X_V)=0`. No common syndrome, alphabet, factor or support-size assumptions are needed. Let `d_N`, `d_T`, and `d_L` denote the positive weighted graph-orbit averages of `H(S|X_{N(v)})`, `H(S|X_T)` for the ten designated triangles, and `H(X_v|X_{L(v)},S)` respectively, with the exact term weights in `frontier-20261028-two-syndrome-all-factor-dual-v1.json` SHA-256 `a8f6822f2c3e3a8e0b0fd639a9b0095a8ea6f38c7833f0ef2fb6551fa9bba087`. Then

\[
\boxed{\quad
381\Delta(X)+74\sum_{v=1}^{10}I(X_v;S)
\le111H(S)+492(d_N+d_T+d_L).\quad}\tag{39}
\]

This is an unconditional all-variable FD inequality for **every** functional auxiliary, not an improved numerical guessing-number upper bound. The weighted defects may be positive; neither their vanishing nor any two-syndrome theorem is assumed.

## Proof

The unrestricted auxiliary bound `frontier-20261028-auxiliary-syndrome-defect-bound-v1.md` SHA-256 `a09f5a9b6c7341e3a6cc3097f3b20903ad05838b784ab28f6dfed536641d25f5` states

\[
\Delta\le\frac{37}{492}G_S+d_N+d_T+d_L,
\quad G_S=3H(X_V)+17H(S)-2\sum_vH(X_v,S).
\]

Using `H(X_v,S)=H(X_v)+H(S)-I(X_v;S)` and the definition of `Delta` gives `G_S=3Delta-3H(S)+2 sum_v I(X_v;S)`. Rearrange the previous inequality and multiply by 492 to obtain (39). The exact coefficient/sign checker receipt for that parent inequality is SHA-256 `1588f967e6ce4027c814ac4f9d1f89063fa6e2db21e3ac629201971a0d36081e`; its specialization to common two-syndrome factors must be read with required erratum `frontier-20261028-two-syndrome-local-neighborhood-erratum-v1.md` SHA-256 `8ff79f6d07b935025e0b2f3de27928f030d251787724b64e05ccd9f1f012a37f` and the corrected explicit local decoder in the repaired theorem. Formula (39) itself retains all local defects, so does not rely on their vanishing.

An actual strict-gap witness therefore must satisfy the corresponding strict inequality with `Delta>0`, for every choice of functional auxiliary `S`. Taking `S` to be a full factor-syndrome vector makes `d_L=0`, since knowing all factor syndromes and the other two triangle components determines every component of `X_v`; the remaining terms quantify how far each neighbourhood/triangle is from determining the whole syndrome. This specialization accommodates arbitrary numbers of syndrome values and arbitrary (even nonabelian) finite group factors. It remains a constraint, not a global solution or independent review.
