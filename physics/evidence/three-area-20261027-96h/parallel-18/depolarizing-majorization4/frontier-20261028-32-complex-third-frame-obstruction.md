# Exact physical counterexample to the third-frame-eigenvalue shortcut

**Result:** the candidate auxiliary inequality \(\lambda_3(F(\rho))\le2\) is false for an explicitly given physical complex four-qubit pure state, where \(F(\rho)=\sum_{i,a=x,y,z}\sigma_i^a\rho\sigma_i^a\). In fact this witness has \(\lambda_3(F)>9/4\). It is not an original-channel counterexample and does **not** refute the still-unproved candidate \(\|F(\rho)\|_{(3)}\le8\). No novelty, independent-family or formal verification claim is made.

## Actual state and rational projector

Use computational-basis indices 0–15 and define \(|\psi\rangle=v/\sqrt{10}\), where the only nonzero entries of the Gaussian-integer vector \(v\) are
\[
\begin{array}{c|rrrrrrrrrr}
\text{index}&2&3&5&8&9&10&12&13&14&15\\\hline
v&-i&-i&-i&-i&i&-1&-1&1&i&i
\end{array}
\]
Then \(\rho=vv^\dagger/10\) has trace1, is Hermitian and idempotent, and is an actual rank-one density. Define the Gaussian-integer 16×3 matrix \(W\) by rows in that same basis:
\[
\begin{array}{c|rrr}
0&0&-2&-1\\
1&3&-1&2\\
2&0&2i&5i\\
3&-2i&-i&3i\\
4&2i&i&2i\\
5&0&-3i&-2i\\
6&2&2&1\\
7&3&3&1\\
8&-3i&4i&-3i\\
9&0&-i&3i\\
10&-2&5&1\\
11&-4&0&0\\
12&1&3&-4\\
13&-5&1&4\\
14&-3i&-3i&-i\\
15&i&2i&0
\end{array}
\]
Exact arithmetic for \(G=W^\dagger(F(\rho)-\tfrac94I)W\) gives the three leading principal minors
\[
\frac{33}{20},\qquad\frac{1069}{80},\qquad\frac{1048061}{4000},
\]
all strictly positive. By Sylvester's criterion \(G\) is positive definite; in particular \(W\) has full column rank. Hence
\[
P=W(W^\dagger W)^{-1}W^\dagger
\]
is an explicitly specified actual complex rank-three orthogonal projector, and every nonzero vector in its range has frame Rayleigh quotient strictly greater than \(9/4\). The min–max principle yields \(\lambda_3(F)>9/4>2\). The exact checker additionally constructs \(P\), verifies \(P=P^\dagger=P^2\), \(\operatorname{Tr}P=3\), and obtains
\[
 \operatorname{Tr}[PF(\rho)]=\frac{5491759}{779445}.
\]
This is an exact auxiliary-premise violation by one physical state and one actual projector, not a chosen nonphysical block.

## Original channel and spectra: not a violation

For both physical parameters \(p=2/3\) and \(p=4/3\), the checker independently builds the original fourfold Pauli Kraus mixture and sequential partial-trace channel and verifies exact entrywise equality for this same \(\rho\). It checks the channel output is positive definite by 16 positive exact rational Hermitian-LDL pivots. It also checks 16 positive exact pivots for
\[
\frac18 I-\Lambda_p(\rho),
\]
so every original output eigenvalue is strictly below \(1/8\), and its top-three sum is strictly below \(3/8\). The actual product reference top3 is \(32/81\), yielding a certified margin
\[
 \frac{32}{81}-\|\Lambda_p(\rho)\|_{(3)}
 >\frac{32}{81}-\frac38=\frac{13}{648}>0.
\]
The same specified \(P\) has exact original-output trace \(3606097/14030010\) at \(p=2/3\) and \(5890409/28060020\) at \(p=4/3\). For additional **numerical** eigenvalue observation only, the original output's top three were approximately `(0.12314462579855834, 0.08704769547553534, 0.08342670128332873)` at \(p=2/3\); their sum was `0.2936190225574224`. The \(p=4/3\) values agreed to roundoff. The exact LDL bound, not those decimal eigenvalues, supplies the certified comparison.

## Actual executed checks

- `frontier-20261028-29-pauli-third-scout.py`, SHA256 `4cdec808c99da0fd034e6a42fe456c7b19d694315ee51d4a55ff3204f01637a1`: bounded seed2026102829, 120 numerical starts, ≤100 steps; observed a candidate third frame eigenvalue `2.6504810555834557`, residual `1.7395912193470069e-15`. That approximate state is not the exact witness above.
- `frontier-20261028-30-sparse-frame-scout.py`, SHA256 `9acc039d8d62a6dfa21efda91df24e0a7d6ea93a4d555e45afbccb0430d9c2c8`: bounded seed2026102830, **12000** actual sparse-state samples; the best was at sample8471 with numerical third frame eigenvalue `2.28519667856061`. It found no three-coordinate computational-basis projector in its checked candidate pass; the rational non-coordinate \(W\) above was then constructed. Its initial console output mislabeled the best index as samples observed; the source was corrected before the final reported run.
- `frontier-20261028-31-complex-frame-counterexample.py`, SHA256 `f88a31f4e283fe2a1d79f643521f0a534f17a9d3583f4073053f0bace7255a07`: ran `env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B ...` from the repo root, exit0. Exact Fraction-based Gaussian rational arithmetic proves the input/projector, displayed Gram minors, actual frame trace, both complete original Kraus/sequential matrix equalities and all LDL signs. NumPy was used only for the expressly labelled decimal eigenvalue observations. The checker imports the previously pinned `frontier-20261028-26-dicke-pauli-counterexample.py` and its exact helper chain.
- Native clock after these pins **Wed Oct 28 17:46:18 PDT 2026**.

The two independent-looking shortcuts \(\lambda_2(F)\le2\) and \(\lambda_3(F)\le2\) are now both ruled out by separate exact physical witnesses. Neither falsification decides the actual rank-three frame-sum bound or the global original k3 conjecture.
