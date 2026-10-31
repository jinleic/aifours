# Equal-probability test for three-state indicator entropy constants

**Status: WRITTEN exact counterexample to one possible sharpening; not a claim of optimality.** Let `S` be uniform on three states and `S_i=1{S=i}`. Then

\[
H(S)=\log_2 3,\qquad
\sum_i H(S_i)=3\log_2 3-2.
\]

Thus a uniform bound `sum_i H(S_i)>=c H(S)` must satisfy

\[
c\le3-\frac{2}{\log_2 3}<\frac74.
\]

The strict last inequality is elementary: `3-2/log_2 3<7/4` iff `3^5<2^8`, and `243<256`. Hence the attractive conjectural coefficient `7/4` fails even at the equal three-state law. This does not show that the valid `5/3` coefficient in `frontier-20261028-three-state-exclusion-entropy-v1.md` SHA-256 `9c5ee203ba255776702e93e90b958663e98a43ebfb3b522b97898381116785e7` is sharp, nor does it resolve the guessing problem. Conditional variants are defeated by taking the conditioning variable constant.
