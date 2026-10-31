# Sharper explicit constants for the uniform high-noise k3 candidate

**CONDITIONAL AUTHOR-WRITTEN SUCCESSOR, INDEPENDENT REVIEW REQUIRED.** If the product-gauge, Hessian identities and \(15t/256\) second-order estimate in `frontier-20261028-59-uniform-high-noise-k3.md` (SHA256 `6f13422e52e6761a3d0d325df821ca78a721ea9c3ad1c8d321043bf93eeb2752`) hold, the sharper norm estimates below upgrade its explicit uniform interval from \(10^{-33}\) to \(10^{-24}\). The predecessor remains frozen. Neither this successor nor its finite checks establish the unrestricted-p or all-index conjecture, novelty, independent-family/human/formal acceptance, or a cure of historical findings.

## Conditional strengthened statement

For every actual four-qubit density \(\rho\), every actual complex rank-three orthogonal projector \(P\), and every physical p with
\[
 |1-p|\le10^{-24},
\]
we propose \(\operatorname{Tr}[P\Lambda_p(\rho)]\le R_3(p)\). The constant is conservative and not claimed optimal. The original general k3 problem outside this small interval remains open.

## Improved uniform block estimates

Use exactly the predecessor's notation: \(t=1-p\in[0,1/4]\), the locally optimal product gauge \(\psi=(|0\rangle+\epsilon v)/\sqrt{1+\epsilon^2}\), with \(v\) unit and supported on weights2–4, the rescaled Hermitian \(H_t=D+\epsilon V+\epsilon^2W+\epsilon^3R\), and the 0/1/rest reference spectral gaps at least \(g=3/2\).

The first-order matrix comes from \(|v\rangle\langle0|+|0\rangle\langle v|\). Its Pauli coefficients of weight0 **and weight1 vanish**: a single-site Pauli cannot connect the vacuum to a vector of weight at least2. Its trace norm is2, so the predecessor's Pauli expansion sharpens to
\[
\|V\|\le2(54t+108t^2+81t^3)
\le\frac{1377}{32}<44.\tag{2}
\]
We retain \(\|D\|\le6,\ \|W\|\le68,\ \|R\|\le136\). For the first divided-gap anti-Hermitian generator,
\[
\|S_1\|\le\|S_1\|_F\le\|V\|_F/g
\le4\|V\|/g<120,\tag{3}
\]
since a 16×16 matrix has Frobenius norm at most four times its operator norm. The second-order coefficient \(Q=W+[V,S_1]+\tfrac12[[D,S_1],S_1]\) obeys
\[
\|Q\|\le68+2(44)(120)+2(6)(120)^2
=183428<190000.\tag{4}
\]
The analogous divided-gap estimate yields \(\|S_2\|\le4\|Q\|/g<600000\).

For \(|\epsilon|\le10^{-4}\), both exponential commutator bounds satisfy \(e^{2|\epsilon|\|S_1\|}<2\) and \(e^{2\epsilon^2\|S_2\|}<2\). The first conjugation's cubic remainder coefficient is bounded by
\[
6(240)^3\frac{2}{6}+44(240)^2\frac{2}{2}+68(240)2+136
=30215176<31\cdot10^6.\tag{5}
\]
The first-order block diagonal is the pinching of V and has norm \(\le44\). With the second conjugation, the total cubic matrix-remainder coefficient is bounded by
\[
\begin{aligned}
&6(2\cdot600000)^2(10^{-4})
+2(44)(2\cdot600000)\\
&\quad+2(190000)(2\cdot600000)(10^{-4})+31\cdot10^6\\
&=1046200000<2\cdot10^9.\tag{6}
\end{aligned}
\]
The same three-block ordering and Weyl rank-three trace estimate as in the predecessor are valid on this larger temporary perturbation range: for \(|\epsilon|\le10^{-4}\), \(44|\epsilon|+68\epsilon^2+136|\epsilon|^3<0.0045\). The block-diagonal approximation differs from D by at most \(44|\epsilon|+190000\epsilon^2\le0.0063\). Both are far smaller than half the reference gap \(3/2\).

The predecessor's verified-in-writing Hessian bound makes the rescaled top3 second-order coefficient at most \(-15/16\). Choose the actual product-overlap gauge radius
\[
\epsilon_0=10^{-11};\qquad
3(2\cdot10^9)\epsilon_0=0.06<15/32.
\]
Then its local conclusion remains \(R_3-K_3(\Lambda_p\rho)\ge15t\epsilon^2/512\) for \(\epsilon\le\epsilon_0\). The constant \(2\cdot10^9\) bounds the **matrix** remainder; the factor3 above is the separate rank-three Weyl bound.

## Exact far-from-product bridge

The predecessor derives \(8-L\ge2(1-m)\), with \(m\) the maximum squared product overlap. If \(\epsilon>10^{-11}\), then \(1-m>10^{-22}/(1+10^{-22})\), hence \(8-L>10^{-22}\). Its common-projector first-order lower bound uses \(\sqrt{39(15-S)}-5<20\), so for \(t\le10^{-24}\), \(t(\sqrt{39(15-S)}-5)<2\cdot10^{-23}<10^{-22}<8-L\). Thus the far and local pure cases both hold at every such t. Product inputs have the reference spectrum; arbitrary mixed inputs follow by affinity with the **same** P. The deterministic four-site spin-flip mirror covers the physical negative-shrink side.

## Checks and boundaries

`frontier-20261028-60-sharper-constants-check.py`, SHA256 `302394fa0c49943d18b7d4bc39e217436e04871de81d410a410618fdcf1a28e1`, ran `python3 -B ...` from repo root, exit0; exact Fraction arithmetic checks the coefficients in (2)–(6), \(\epsilon_0\), and the far-case inequalities. `frontier-20261028-61-perturbation-block-audit.py`, SHA256 `cb1f90e74265ff58e9cd8bee27c896c578b20862f64e1b6eed56c5d4ad0aff3f`, independently exercised 60 numerical product-gauge block conjugations (10 complex v for each \(t=0,0.01,0.25\), \(\epsilon=10^{-4},10^{-5}\)). Its largest observed remainder-norm/\(\epsilon^3\) ratio was `13.938345377318406`; its smallest observed rescaled k3 gap/\(\epsilon^2\) was `7.649146382959771`. These finite floating checks test implementation/conventions only and do not prove a uniform theorem or authenticate extreme t numerically.

Native checker-pin clock **Wed Oct 28 18:34:01 PDT 2026**. The global 59 predecessor and this constants successor require a complete disjoint written review of the block expansions, Hessian algebra, norm budget, same-P quantifiers and actual source assumptions before any admission. No original all-p conclusion is drawn.
