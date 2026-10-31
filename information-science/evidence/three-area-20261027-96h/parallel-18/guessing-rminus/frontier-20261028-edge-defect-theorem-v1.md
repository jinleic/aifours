# Any strict gain must route information through the unique non-triangle edge

**Status: WRITTEN with an independently checked exact Shannon identity; scientific review pending.** The original R-minus graph has 26 edges. Exactly one of them, `3--4`, lies in none of the ten triangles `123, 145, 167, 239, 2·7·10, 389, 4·5·10, 4·8·10, 569, 678`. Let `G'` be R-minus with that edge deleted (the union of the ten triangles), and write `N'(v)` for its neighbourhoods; `N'(v)=N(v)` except `N'(3)={1,2,8,9}` and `N'(4)={1,5,8,10}`.

**Theorem.** For every finite joint law of `X_1,...,X_10` (any alphabets), with `Delta=H(X_V)-(2/3)sum_v H(X_v)`,

\[
\Delta=\frac13\sum_{v=1}^{10}H(X_v\mid X_{N'(v)})-\sum_j a_j I_j,\qquad a_j>0,\tag{65}
\]

where the `I_j` are 108 elemental conditional mutual informations. Consequently every original R-minus FD law satisfies

\[
\boxed{\quad
\Delta\le\frac13\Bigl[I(X_3;X_4\mid X_1,X_2,X_8,X_9)+I(X_3;X_4\mid X_1,X_5,X_8,X_{10})\Bigr].\quad}\tag{66}
\]

Indeed, R-minus FDs kill the eight terms with `N'(v)=N(v)`; and since `H(X_3|X_{N(3)})=0`, `H(X_3|X_{1,2,8,9})=I(X_3;X_4|X_{1,2,8,9})`, and symmetrically at 4. In particular `G'` itself has Shannon guessing number at most `20/3`, attained by the triangle code, and any strategy on R-minus beating `20/3` must make the edge `3--4` carry conditional information in both directions' triangle contexts. This is an unconditional all-strategy structural inequality; it does not improve the numerical upper bound, because it is a Shannon consequence.

The exact identity `frontier-20261028-edge-defect-dual-v1.json` SHA-256 `09750933bddc4e47a25e94d1e11882f0742bdcc8cf0ab0f841836ec9ead3dc39` was proposed by an LP. The independent checker `frontier-20261028-edge-defect-dual-check.py` SHA-256 `76be1d9c754803b4b5939bb813940cfaf8cc3c62996fea0d8592e4120b4eb755`, receipt SHA-256 `6b9db9e874a6a525d8fa2dbd42735a05497b08ee4767ae629f2181c3883595ec`, rebuilds the edge set and confirms `3--4` is the unique non-triangle edge, rebuilds all ten `G'` FD rows with weight exactly `1/3`, checks every CMI sign and verifies all 1,023 coefficients with exact arithmetic, rejecting an altered target and a flipped CMI sign. The local component FDs in the syndrome-visibility theorems are exactly the extra information needed to control the two defect terms in (66) for structured supports. No formal proof, independent review, or novelty clearance is claimed.
