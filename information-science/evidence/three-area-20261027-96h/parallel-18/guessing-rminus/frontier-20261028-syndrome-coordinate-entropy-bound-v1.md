# A marginal-entropy test for strictly positive gap

**Status: WRITTEN with exact compact-certificate import; scientific review pending.** For any original-neighbour R-minus FD law in the finite-group triangle-factor encoding, let `S=(S_1,...,S_10)` be the full syndrome vector. Denote `h=H(S)` and `h_t=H(S_t)`. Then

\[
\boxed{\quad
12\Delta\le12h-\frac23
\bigl(2h_1+2h_2+2h_3+h_4+2h_5+2h_6+h_7+2h_8+2h_9+2h_{10}\bigr).
\quad}\tag{50}
\]

All entropies use the same log base. Consequently a strict-gap law must have `h>0` and

\[
h>\frac1{18}\bigl(2h_1+2h_2+2h_3+h_4+2h_5+2h_6+h_7+2h_8+2h_9+2h_{10}\bigr).\tag{51}
\]

This is necessary, not sufficient; it covers arbitrary syndrome counts and group alphabets but does not prove a general numeric upper bound. Coefficients are specific to the chosen 60-CMI/automorphism certificate.

## Proof

For each original-neighbour tuple, all factor syndromes incident to its central vertex are deterministically recoverable by the graph FD and triangle products. In (42) of `frontier-20261028-compact-full-syndrome-inequality-v1-addendum-1.md` SHA-256 `2f7a18d11fde89e9c94bf57ee376967f0f8294b1b6660699d6be2c4cc25eeed6`, bound each neighbourhood defect `H(S|X_{N(v)})` by `H(S|S_t)=h-h_t` for any incident factor `t`; averaging equally over the three incident factors gives the sum of those three bounds divided by three. Each triangle defect is similarly bounded by `h-h_t` for its own factor.

Expanding the finite incidence list yields

\[
12\Delta\le12h-\frac13\left(4h_1+4h_2+4h_3+2h_4+4h_5+4h_6+2h_7+4h_8+4h_9+4h_{10}\right),
\]

which is (50). The integer incidence calculation is small and is independently checkable from the ten displayed triangles in `frontier-20261028-entropy-balance-equivalence-v1.md` SHA-256 `4013d40004f9e6576973517b5a36e634e294f6713f75ff44273d4266d920090e`. No independent scientific review, proof-assistant formalization, or novelty clearance is claimed.
