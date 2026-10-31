# A continuum of genuinely entangled Pauli-frame equality states

**Author-written exact family and actual-projector coupling, not a global k3 proof.** Let
\[
F(\rho)=\sum_{i=1}^4\sum_{a=x,y,z}\sigma_i^a\rho\sigma_i^a,
\qquad E_i(X)=\tfrac12 I_i\otimes\operatorname{Tr}_iX.
\]
The global conjectural inequality \(\|F(\rho)\|_{(3)}\le8\) remains **unproved**. Regardless of whether that global inequality holds, the family below has the exact value8 at genuine entangled inputs. It therefore falsifies any proposed assertion that the value8 is attained only by product inputs. No novelty, independent-family, human or formal acceptance is claimed.

## All-parameter family

For real \(a,b,c>0\) satisfying \(ab=4c^2\), put \(N=a^2+b^2+4c^2\) and
\[
|\psi_{a,b,c}\rangle=\frac1{\sqrt N}\Bigl(a|0000\rangle+b|1111\rangle
+c(|0101\rangle+|0110\rangle+|1001\rangle+|1010\rangle)\Bigr),
\quad \rho=|\psi\rangle\langle\psi|.
\]
Every one-versus-three Schmidt rank is2. Across the 12|34 cut the coefficient matrix has rank3; across 13|24 and 14|23 it has rank4, because its nontrivial 2×2 corner has determinant \(ab-c^2=3c^2\ne0\). Thus every member is genuinely four-partite entangled.

Its exact frame spectrum consists of the following values with multiplicity, with coinciding values merged when needed:
\[
\frac{4(a^2+b^2)}N\ (1),\quad
\frac{2(a+b)^2}N\ (2),\quad
\frac{2a^2}N\ (2),\quad\frac{2b^2}N\ (2),\quad
\frac{8c^2}N\ (2),\quad0\ (7).\tag{1}
\]
The first three listed eigenvalues dominate all the remaining ones, and
\[
 \|F(\rho)\|_{(3)}
 =\frac{4(a^2+b^2)+4(a+b)^2}{N}=8,\tag{2}
\]
because \(N=a^2+b^2+ab\). In particular, balanced \(a=b=2c\) gives \(\lambda_1=\lambda_2=\lambda_3=8/3>2\). Both proposed individual-eigenvalue shortcuts \(\lambda_2(F)\le2\) and \(\lambda_3(F)\le2\) fail on this actual state, even though its top-three frame sum equals8.

An actual rank-three top projector \(P_F\) is the sum of the normalized projectors onto the following mutually orthogonal vectors:
\[
\begin{aligned}
w_e&=a|0000\rangle-b|1111\rangle,\\
w_1&=a(|0001\rangle+|0010\rangle)+2c(|0111\rangle+|1011\rangle),\\
w_2&=a(|0100\rangle+|1000\rangle)+2c(|1101\rangle+|1110\rangle).
\end{aligned}
\]
Their squared norms are \(a^2+b^2,2a(a+b),2a(a+b)\). Each is an eigenvector in the corresponding top eigenspace, and \(\operatorname{Tr}[P_FF(\rho)]=8\). The frame top eigenspace has dimension exactly3 and is strictly above the rest, so \(P_F\) is the unique rank-three frame maximizer.

## Same-projector coupling and a continuum of LU types

For the SAME actual \(\rho,P_F\),
\[
 x:=\operatorname{Tr}(P_F\rho)
 =\frac{(a^2-b^2)^2}{N(a^2+b^2)}<1,\qquad
 \sum_i\operatorname{Tr}[P_F E_i(\rho)]=x+2<3.\tag{3}
\]
The inequality is strict because
\(N(a^2+b^2)-(a^2-b^2)^2=ab(a^2+b^2+4ab)>0\).
The identity in (3) is \(\sum_iE_i(\rho)=\rho+F(\rho)/4\).

For this family, every actual \(P\) obeys \(\operatorname{Tr}(P\rho)\le1\) and \(\operatorname{Tr}[PF]\le8\), by its explicitly computed spectrum. If their sum attained3, both would be equalities. Frame equality would force \(P=P_F\), but \(P_F\rho\) has overlap strictly less than1. Thus the actual one-erasure objective is **strictly below3 for every \(P\)** in this family; compactness gives a positive state-dependent gap. This conclusion is restricted to the displayed family. It is a concrete obstruction to treating the two separately optimized maxima as jointly attained, not a nonphysical counterexample to original majorization.

Each local Bloch radius is \(|a^2-b^2|/N\). With \(c=1\), \(b=4/a\), and \(a/b=t\ge1\), this equals \((t^2-1)/(t^2+t+1)\), whose derivative is \((t^2+4t+1)/(t^2+t+1)^2>0\). Hence the family contains continuously many mutually local-unitary-inequivalent inputs, even allowing party permutations; no priority claim is made.

## Frame calculation

In even/odd computational parity, the even block of \(NF(\rho)\) has the nonzero blocks
\[
4\begin{pmatrix}a^2&-ab\\-ab&b^2\end{pmatrix},\qquad
4c^2\begin{pmatrix}1&-1\\-1&1\end{pmatrix}^{\oplus2},
\]
and two further zero directions. The odd block is two copies of
\[
\begin{pmatrix}
2a^2+4c^2&4c^2&2c(a+b)&2c(a+b)\\
4c^2&2a^2+4c^2&2c(a+b)&2c(a+b)\\
2c(a+b)&2c(a+b)&2b^2+4c^2&4c^2\\
2c(a+b)&2c(a+b)&4c^2&2b^2+4c^2
\end{pmatrix}.
\]
Its two antisymmetric directions have eigenvalues \(2a^2\) and \(2b^2\). On symmetric directions \((x,x,y,y)\), the remaining block is
\[
\begin{pmatrix}2a^2+8c^2&4c(a+b)\\4c(a+b)&2b^2+8c^2\end{pmatrix}
=2(a+b)\begin{pmatrix}a&2c\\2c&b\end{pmatrix}.
\]
Because \(ab=4c^2\), its eigenvalues are \(2(a+b)^2\) and0. Combining the even and two odd blocks proves (1), including multiplicities. Positivity of \(a,b\) gives the asserted strict separation of the top three from all other eigenvalues.

## Balanced original-channel example and executed checks

For \(a=b=2,c=1\), all local marginals are \(I/2\), \(x=0\), and the frame spectrum is \((8/3)^{(3)},(2/3)^{(6)},0^{(7)}\). Here \(T_1(\rho)=\sum_iE_i(\rho)=\rho+F(\rho)/4\) has exact spectrum \(1^{(1)},(2/3)^{(3)},(1/6)^{(6)},0^{(6)}\), so its actual top-three value is \(7/3\), while the frame-maximizing \(P_F\) gives2. The separate bounds \(1+8/4=3\) are not jointly attained.

At each original physical \(p=2/3,4/3\), direct exact Kraus construction gives full output spectrum
\[
 (1/9)^{(1)},\quad(20/243)^{(3)},\quad(14/243)^{(6)},\quad(4/81)^{(6)}.
\]
The actual original top3 is \(67/243\), product reference \(32/81=96/243\), gap \(29/243\). A separate actual rank-three \(P_{\rm chan}\) attains that original top3, while \(P_F\) gives \(20/81\). Neither is an original counterexample.

Exact checker `frontier-20261028-36-oneuniform-frame-saturation.py`, SHA256 `201ee12a2b1e6ee7c1eda20706f1d8b58cfcfb7395818851bd92bf4e0615d837`, ran under `python3 -B` from the repo root, exit0: exact seven Schmidt-cut ranks, all local marginals, actual projectors, all frame/T1/original spectral multiplicities by rational Gaussian rank, same-pair traces, and full original Kraus/sequential matrix agreement at both p. Family checker `frontier-20261028-37-frame-equality-family-check.py`, SHA256 `949849c3b0e4a8bd028dbd6c5be0dd81f5cdffde9a2f348550ae23de662e4b27`, also ran under `python3 -B`, exit0: 23 distinct positive rational \(a\) values with \(b=4/a,c=1\), all exact spectra and actual projectors, including both balanced and unbalanced cases. These finite checks support but do not replace the written all-parameter calculation. Native metadata observation **Wed Oct 28 17:56:00 PDT 2026**.

The missing all-state frame inequality, all-variable t1/t2 layer bounds and full original k3 claim remain open. This family and its inequality do not assert any current literature priority.
