# review-v1 — f130-depolarizing-global-k10-k5-k6

**Kind.** `INDEPENDENT_SAME_HARNESS_SCIENTIFIC_REVIEW` (same harness as the author; this is **not** a human review, **not** an independent-model-family review, **not** a formal/kernel verification and **not** a novelty assessment).

**Manifest.** `manifest-v1.json`, SHA-256 `d8e0db347bf2e1e00b137e6b348b2b4e3b3556d96be97da433014635bc3047a1`, 2588 bytes, verified at `2026-10-29T03:27:22Z` (= 2026-10-28T20:27:22-0700 PDT) before reading. No pre-source overlays are declared in the manifest. The manifest's `authority` file was not read (it is not an input); only the three declared inputs were read, completely and in declared order, after full SHA-256/bytes/LF verification at `2026-10-29T03:27:28Z`:

| # | role | file | SHA-256 | bytes | LF |
|---|---|---|---|---|---|
| 1 | Rank-6 global k10 candidate | `…/depolarizing-majorization4/frontier-20261028-98-rank6-global-k10.md` | `05c04b8b093835c2a0fe63e849e2552c012ef1d33a7b35e78a9738ebce0799f2` | 7605 | 131 |
| 2 | Author rank-6 exact checker (read only) | `…/frontier-20261028-97-rank6-tail-check.py` | `16e3f2b3ec6572d2d1ff3c8caea863affec342db7e0bf3753b0f44e43555175f` | 3835 | 90 |
| 3 | Ranks 10/11 global k5,k6 candidate | `…/frontier-20261028-100-rank10-11-global-k5-k6.md` | `108322fa2469cb6a374b9b8cca633e78e8810169f6cdb7b7183cef26cdb188db` | 7140 | 108 |

All three matched the manifest. Files cited by the packets but outside the manifest (`…-94-global-tail-biseparable.md`, `…-95-pair-tail-scout.py`, `…-96-spinflip-tail-scout.py`, `…-99-balanced-rank-tail-check.py`) were **hashed only, not read**; the SHA-256 values quoted in the packets for 95, 96 and 99 match on disk (94 quotes none). Input 2 was read but **not executed or imported**; it itself imports author modules `…-66-noise-endpoint-check.py` and `…-26-dicke-pauli-counterexample.py`, which are outside the manifest and were not read.

No web search, external model, author contact, Git, deletion, publication or infrastructure change was performed. Artifacts were written only in this review directory with the `reviewer-` prefix (plus this `review-v1.md`); see §7 for hashes and one disclosed byproduct.

---

## 1. The exact original problem addressed

Let $\Phi_p(\rho)=(1-p)\rho+p\,\tfrac{I}{2}$ be the qubit depolarizing map; it is completely positive exactly for $0\le p\le 4/3$ (the packets' "physical" interval). Write $t=1-p$, $b=p/2$, $a=t+b=1-p/2$, so $\Phi_p(|0\rangle\langle0|)=\mathrm{diag}(a,b)$ and $a+b=1$. The **product reference** is $\Phi_p^{\otimes4}(|0000\rangle\langle0000|)$, whose spectrum is $a^{4-w}b^{w}$ with multiplicity $\binom4w$, $w=0,\dots,4$ (any pure product input gives the same spectrum by local covariance).

For an index $k\in\{1,\dots,16\}$, the **prefix (Ky Fan) comparison** $\mathcal P_k$ is

$$\forall\rho\ \text{(four-qubit density)},\ \forall p\in[0,4/3]:\qquad K_k\big(\Phi_p^{\otimes4}(\rho)\big)\ \le\ K_k\big(\Phi_p^{\otimes4}(|0000\rangle\langle0000|)\big),$$

where $K_k(X)=\max\{\operatorname{Tr}[PX]:P \text{ a complex rank-}k\text{ orthogonal projector}\}$ is the sum of the $k$ largest eigenvalues. Full output majorization is the conjunction of all $\mathcal P_k$. Because both sides have unit trace, $\mathcal P_k$ is equivalent to the **tail** comparison with $r=16-k$:

$$\min_{Q\ \text{rank-}r}\operatorname{Tr}[Q\,\Phi_p^{\otimes4}(\rho)]\ \ge\ \text{(sum of the } r \text{ smallest reference eigenvalues)}.$$

For $0\le p\le1$ one has $a\ge b\ge0$, so the ascending reference order is $b^4\le ab^3\le a^2b^2\le a^3b\le a^4$ (ties at $p=1$) and, for $5\le r\le 11$,

$$\text{ref}_r(p)=b^4+4ab^3+(r-5)a^2b^2 = r\,b^4+(2r-6)\,t\,b^3+(r-5)\,t^2b^2 .$$

Packet 98 claims $\mathcal P_{10}$ (rank $r=6$: $\text{ref}_6=b^4+4ab^3+a^2b^2$). Packet 100 claims $\mathcal P_6$ and $\mathcal P_5$ (ranks $10$ and $11$), and its rank-5 case re-yields $\mathcal P_{11}$. Both packets state they do **not** address $\mathcal P_3$, $\mathcal P_7$–$\mathcal P_9$, full majorization or novelty. This review likewise makes **no** statement about $k=3$, $k=7,8,9$, or global majorization.

---

## 2. Independent reconstruction (every load-bearing premise stated)

All objects live on $(\mathbb C^2)^{\otimes4}$, dimension $D=16$. Notation (mine; it agrees with the packets'):

* unnormalised erasure $E_i(X)=I_i\otimes\operatorname{Tr}_iX$; for $S\subseteq[4]$, $E_S=\prod_{i\in S}E_i$ (commuting);
* $H_1(X)=\sum_i E_{[4]\setminus i}(X)=\sum_i I_{\bar i}\otimes X_i$, $H_2(X)=\sum_{i<j}I_{\overline{ij}}\otimes X_{ij}$, $H_3(X)=\sum_iE_i(X)$;
* spin flip $\widetilde X=Y^{\otimes4}X^{T}Y^{\otimes4}$ (plain transpose);
* $F(X)=\sum_{i}\sum_{a\in\{X,Y,Z\}}\sigma^a_iX\sigma^a_i$ (non-identity Paulis; this is the reading under which packet 98's "$F=4T_1-4\rho$" is correct);
* $Z_{\rm tot}=\sum_iZ_i$, $N=\sum_i(I-Z_i)/2$ (Hamming weight), $E_0=|0000\rangle\langle0000|$, $E=|1111\rangle\langle1111|$, $\Pi_1$ = weight-one projector (rank 4).

Standard facts used without proof: Ky Fan's variational principle (sum of $r$ largest/smallest eigenvalues = max/min of $\operatorname{Tr}[QX]$ over rank-$r$ projectors; hence the bottom-$r$ sum is concave in $X$); a $2\times2$ Hermitian matrix with non-negative diagonal and determinant is PSD; the Schur-complement characterisation of PSD used by my exact LDL check; transpose and unitary conjugation preserve projectors.

### 2.1 Erasure expansion and the retained terms (packet 98 eq. (10))

Single site: $\Phi_p=t\,\mathrm{id}+b\,E_i$. Hence
$$\Phi_p^{\otimes4}(\rho)=\sum_{S\subseteq[4]}t^{4-|S|}b^{|S|}E_S(\rho)=b^4I+t b^3H_1(\rho)+t^2b^2H_2(\rho)+t^3b\,H_3(\rho)+t^4\rho .$$
For $0\le p\le1$, $t,b\ge0$ and every $E_S(\rho)\ge0$, so the dropped remainder $t^3bH_3(\rho)+t^4\rho$ is PSD and (10) holds. **For $p>1$ (10) is false** (my negative control N4: at $p=4/3$, $\rho=E_0$, the remainder has entry $-7/81$ at $|0000\rangle$); the packets correctly use (10) only on $[0,1]$ and reach $(1,4/3]$ through the mirror (§2.5).

### 2.2 The dual lemma: $H_1(Q)+\widetilde Q\ge(2r-5)I$ for rank $r\in\{5,6,10,11\}$ (rank 6: $\ge7I$)

Let $Q$ be a complex rank-$r$ orthogonal projector.

**(a) Local marginal rotations and covariance.** $Q_i=\operatorname{Tr}_{\bar i}Q=\tfrac r2I+\tfrac12\vec m_i\!\cdot\!\vec\sigma$ with $m_i:=|\vec m_i|\ge0$. Choose $U_i\in U(2)$ with $U_i(\vec m_i\!\cdot\!\vec\sigma)U_i^\dagger=m_iZ$ and $U=\bigotimes_iU_i$. Then $H_1(UQU^\dagger)=UH_1(Q)U^\dagger$ (marginals transform covariantly) and $\widetilde{UQU^\dagger}=U\widetilde QU^\dagger$: writing $U_i=e^{i\phi_i}V_i$ with $V_i\in SU(2)$, $Y\overline{U_i}Y=e^{-i\phi_i}V_i$, so $Y^{\otimes4}\overline U\,Q^T\,U^TY^{\otimes4}=(e^{-2i\sum\phi}U)\widetilde Q(e^{-2i\sum\phi}U)^\dagger=U\widetilde QU^\dagger$. Hence it suffices to prove the lemma when every $Q_i=\tfrac r2I+\tfrac{m_i}2Z$, $m_i\ge0$; then
$$H_1(Q)=2rI+\tfrac12\sum_im_iZ_i,\qquad H_1(Q)-(2r-5)I=5I+\tfrac12\sum_im_iZ_i .$$
(Verified exactly, including a non-$SU(2)$ factor, in control C4.)

**(b) $S:=\sum_im_i\le12$.** $m_i=\operatorname{Tr}[Q_iZ]=\operatorname{Tr}[QZ_i]$, so $S=\operatorname{Tr}[QZ_{\rm tot}]\le$ (sum of the $r$ largest eigenvalues of $Z_{\rm tot}$). Spectrum of $Z_{\rm tot}$: $4^{(1)},2^{(4)},0^{(6)},(-2)^{(4)},(-4)^{(1)}$; the top-$r$ sum is $12$ for every $5\le r\le11$ (control C1 table).

**(c) $\sum_{j\ne i}m_j\le10$, hence $m_i\ge S-10$ for every $i$.** $\sum_{j\ne i}m_j=\operatorname{Tr}[Q\sum_{j\ne i}Z_j]$; the three-site sum (fourth factor carried along) has spectrum $3^{(2)},1^{(6)},(-1)^{(6)},(-3)^{(2)}$ and top-$r$ sums $9,10,10,9$ at $r=5,6,10,11$ (at $r=7,8,9$ they are $11,12,11$, which is exactly why the proof is confined to $\{5,6,10,11\}$; packet 100 says so).

**(d) Case $S\le10$.** $5I+\tfrac12\sum m_iZ_i\ge(5-S/2)I\ge0$ and $\widetilde Q\ge0$; done.

**(e) Case $S>10$: $c=(S-10)/2\in(0,1]$.** In the rotated computational basis $5I+\frac12\sum_im_iZ_i$ is diagonal with entry $-c+\sum_{i:x_i=0}m_i$ at $|x\rangle$: at $x=1111$ it equals $-c$; at every other $x$ some $x_i=0$, so the entry is $\ge-c+\min_im_i\ge-c+(S-10)=c$. Therefore
$$H_1(Q)-(2r-5)I\ \ge\ c\,(I-2E).$$

**(f) Occupancy bound $q:=\langle1111|\widetilde Q|1111\rangle=\langle0000|Q|0000\rangle\ge(S-8)/4=(1+c)/2$.** $Y^{\otimes4}|1111\rangle=(-i)^4|0000\rangle=|0000\rangle$ gives the first equality. Diagonal inequality $N\ge2I-2E_0-\Pi_1$ (entries $0,1,\ge2$ vs $0,1,2$). With $0\le Q\le I$: $\operatorname{Tr}[Q\Pi_1]\le4$ and $\operatorname{Tr}[QN]\ge2r-2q-4$. Since $Z_{\rm tot}=4I-2N$, $S=4r-2\operatorname{Tr}[QN]\le8+4q$. (Rank-independent.)

**(g) Exact $2\times2$ projector lemma.** For an orthogonal projection $R$, unit $e$, $0\le c\le1$, $q=\langle e|R|e\rangle$: if $q\ge(1+c)/2$ then $M:=R+c(I-2|e\rangle\langle e|)\ge0$. For $0<q<1$: $u=Re/\sqrt q$, $v=(I-R)e/\sqrt{1-q}$ are orthonormal and $W=\mathrm{span}(u,v)$ is invariant under $R$ and $|e\rangle\langle e|$, hence under $M$; on $W^\perp$, $M=R+cI\ge0$; on $W$, in basis $(u,v)$, $M=\begin{pmatrix}1+c-2cq&-2c\sqrt{q(1-q)}\\-2c\sqrt{q(1-q)}&c(2q-1)\end{pmatrix}$ with determinant $c(2q-1-c)$ (polynomial identity confirmed on a $4\times4$ rational grid, control C2). Under the hypothesis: $1+c-2cq\ge1-c\ge0$, $c(2q-1)\ge c^2\ge0$, $c(2q-1-c)\ge0$. For $q=1$: $R\ge|e\rangle\langle e|$ so $M=(R-|e\rangle\langle e|)+(1-c)|e\rangle\langle e|+c(I-|e\rangle\langle e|)\ge0$. $q=0$ violates the hypothesis. The hypothesis is sharp (control N2: $c=2q-1+10^{-3}$ gives a negative pivot).

**(h) Conclusion.** With $R=\widetilde Q$ (a projector), $e=|1111\rangle$, and (f)–(g): $\widetilde Q+c(I-2E)\ge0$; adding (e) gives $H_1(Q)+\widetilde Q-(2r-5)I\ge0$. $\blacksquare$

Where rank enters: (b) needs $S\le12$ (so $c\le1$); (c) needs the three-site cut $\le10$; nothing else is rank-specific. The lemma as reconstructed holds for **every** complex projector of rank $5,6,10,11$. It is tight: $Q=\mathrm{span}\{0000,\text{wt-1}\times4,0011\}$ (rank 6) has $S=12,c=1,q=1$ and a zero eigenvalue (control C5; the false threshold $7+10^{-3}$ fails, N1).

### 2.3 The identity $H_2-H_1+I=\rho+\widetilde\rho+\tfrac12F(\rho)$ (packet 98 eq. (8)) and $\operatorname{Tr}[QH_2(\rho)]\ge r-5$

One qubit: $Y\rho^TY=\operatorname{Tr}(\rho)I-\rho=E(\rho)-\rho$ (Bloch components flip sign). Tensoring, $\widetilde X=\sum_S(-1)^{|S|}E_S(X)=X-H_3+H_2-H_1+\operatorname{Tr}(X)I$. The Pauli twirl gives $E_i(X)=\tfrac12\sum_{a=0}^3\sigma_i^aX\sigma_i^a$, so $H_3(X)=2X+\tfrac12F(X)$. Substituting: $H_2(X)-H_1(X)+\operatorname{Tr}(X)I=X+\widetilde X+\tfrac12F(X)$, an exact linear identity for every operator (control C8 on random Gaussian-integer inputs; N3 shows the coefficient $\tfrac12$ is forced). For a density all three right-hand terms are PSD, so $H_2-H_1+I\ge\rho+\widetilde\rho\ge\widetilde\rho$.

$H_1$, $H_2$ and the spin flip are self-adjoint for $\langle A,B\rangle=\operatorname{Tr}[AB]$ (control C9). Therefore, for the same $Q$ and any density $\rho$,
$$\operatorname{Tr}[QH_2(\rho)]=\operatorname{Tr}\!\big[\rho\,(H_1(Q)+\widetilde Q)\big]-r+\operatorname{Tr}[Q\rho]+\tfrac12\operatorname{Tr}[QF(\rho)]\ \ge\ (2r-5)-r=r-5 ,$$
using the dual lemma and $\operatorname{Tr}\rho=1$, and dropping two non-negative terms (the "retained erasure terms" $\rho$ and $F(\rho)/2$ are only dropped here, never sign-abused). Rank 6: $\operatorname{Tr}[QH_2(\rho)]\ge1$.

### 2.4 $\operatorname{Tr}[QH_1(\rho)]\ge2r-6$ (rank 6: $\ge6$)

Write each $\rho_i=\lambda_iP_i+(1-\lambda_i)P_i^\perp$. Then $H_1(\rho)=\sum_{\epsilon\in\{0,1\}^4}\big(\prod_i w_i^{\epsilon_i}\big)\sum_jI\otimes P_j^{\epsilon_j}$ (product weights), a convex combination of local-unitary conjugates of $\sum_i|0\rangle\langle0|_i$, whose spectrum is $0^{(1)},1^{(4)},2^{(6)},3^{(4)},4^{(1)}$; bottom-$r$ sums are $4,6,14,16=2r-6$ at $r=5,6,10,11$ (control C1). By concavity of the bottom-$r$ sum and unitary invariance, $\min_Q\operatorname{Tr}[QH_1(\rho)]\ge2r-6$ for every density. (Packet 98 attributes the phrasing to packet 94; the argument is self-contained as above and I rely only on my reconstruction, not on packet 94.)

### 2.5 Assembly: bottom-$r$ spectrum, endpoints, $p>1$ mirror

For $0\le p\le1$ and any rank-$r$ $Q$ ($r\in\{5,6,10,11\}$), by §2.1, §2.3, §2.4 and $t,b\ge0$:
$$\operatorname{Tr}[Q\Phi_p^{\otimes4}(\rho)]\ \ge\ r\,b^4+(2r-6)\,t\,b^3+(r-5)\,t^2b^2=b^4+4ab^3+(r-5)a^2b^2=\text{ref}_r(p).$$
(Rank 6: $6b^4+6tb^3+t^2b^2=b^4+4ab^3+a^2b^2$, exactly the sum of the six smallest reference eigenvalues.) Minimising over $Q$ and subtracting from the unit trace gives $\mathcal P_{16-r}$ on $[0,1]$. Endpoints: $p=0$ is $K_k(\rho)\le1$; $p=1$ is $t=0$, both sides $r/16$; ties are harmless since $\text{ref}_r$ is the ascending partial sum. The bound is attained by $\rho=E_0$ with its own bottom-$r$ eigenprojector (control C13), so no slack is available and the argument is tight.

**Mirror.** $\Theta(\rho):=Y\rho^TY$ satisfies $\Theta\circ\Phi_p=\Phi_{2-p}$ on one qubit ($\Theta(t\rho+bE\rho)=t(E\rho-\rho)+bE\rho=aE\rho-t\rho$), hence $\Theta^{\otimes4}\circ\Phi_p^{\otimes4}=\Phi_{2-p}^{\otimes4}$. $\Theta^{\otimes4}$ is transpose followed by unitary conjugation, so $\operatorname{spec}\Phi_p^{\otimes4}(\rho)=\operatorname{spec}\Phi_{2-p}^{\otimes4}(\rho)$ for every $\rho$; the reference multiset is the same at $p$ and $2-p$ ($a\leftrightarrow b$). For $p\in[1,4/3]$, $2-p\in[2/3,1]$, so $\mathcal P_k$ at $p$ follows from $\mathcal P_k$ at $2-p$; equivalently $\operatorname{Tr}[Q\Phi_p(\rho)]=\operatorname{Tr}[\widetilde Q\Phi_{2-p}(\rho)]$ with $Q\mapsto\widetilde Q$ a bijection of rank-$r$ projectors (control C11, exact at $p=4/3,5/4$).

### 2.6 Generalisation to ranks 5/6/10/11 (k11/k10/k6/k5)

Everything above is uniform in $r$ except (b)–(c) of the lemma and the two coefficient bounds $2r-6$, $r-5$. Packet 100's constants are correct: lemma threshold $2r-5$ (so $H_1(Q)-(2r-5)I=5I+\frac12\sum m_iZ_i$ for every $r$), $H_2$ coefficient $r-5$, $H_1$ coefficient $2r-6$, reference $b^4+4ab^3+(r-5)a^2b^2$ with multiplicities $1,4,r-5$ (for $r=5$ the $H_2$ bound is vacuous and $\mathcal P_{11}$ needs only §2.4). Rank $10\Rightarrow\mathcal P_6$, rank $11\Rightarrow\mathcal P_5$, rank $6\Rightarrow\mathcal P_{10}$, rank $5\Rightarrow\mathcal P_{11}$.

---

## 3. Controls actually run (independently written; author code never executed or imported)

All in this directory; receipts (UTC clocks, SHA-256) are inside each `.result.json` and in `reviewer-receipts-v1.txt`.

**A. `reviewer-exact-controls-v1.py`** — exact Gaussian-rational arithmetic (`fractions.Fraction`), my own erasure/partial-trace, $H_{1,2,3}$, spin flip (explicit $Y^{\otimes4}$), $F$, sequential channel, erasure expansion, projector builder, and an exact LDL$^*$ PSD test with zero-pivot handling. Run `2026-10-29T03:41:56Z`–`03:41:57Z`, exit 0, **23 positive controls PASS, 4 negative controls FAIL as predicted**:

* C0 conventions; C1 spectral tables (all of §2.2(b)(c), §2.4, $N\ge2I-2E_0-\Pi_1$); C1b three-site cut $11,12,11$ at ranks $7,8,9$; C2 determinant identity.
* C3 dual lemma on **my own** projectors with $S>10$: $v_0=(12|0000\rangle+5i|1111\rangle)/13$ plus weight-one/weight-two basis vectors at ranks $5,6,10,11$; exact $S=1828/169>10$, $c=69/169$, $q=144/169\ge(1+c)/2=119/169$; rank-6 $m=(626,626,288,288)/169$; every step (a)–(h) checked exactly; dual operator PSD with 16 positive pivots.
* C4 the same four projectors after a Gaussian-rational $U(2)^{\otimes4}$ rotation (one factor with $\det=-1$): all four marginals non-diagonal (e.g. site-0 marginal $\begin{pmatrix}10484/4225&-7512i/4225\\7512i/4225&14866/4225\end{pmatrix}$), Bloch lengths preserved, dual operator PSD, and exact covariance $A(UQU^\dagger)=UA(Q)U^\dagger$.
* C5 tight projector ($S=12,c=1,q=1$): PSD with one zero pivot; **N1** threshold $7+10^{-3}$ fails.
* C6 the packet-98 projector rebuilt from its text: $S=7108/625$, $c=429/625$, $q=576/625$, 16 positive pivots (matches the packet's quoted figures).
* C7/**N2** $2\times2$ lemma on $16\times16$: PSD at $c=(S-10)/2$ and at the boundary $c=2q-1$; fails at $c=2q-1+10^{-3}$.
* C8/C8b/**N3** identity (8), alternating-erasure spin flip, one-qubit spin flip; wrong coefficient fails. C9 self-adjointness.
* C10/**N4** channel = expansion; remainder $=t^3bH_3+t^4\rho$; PSD at $p=2/5,2/3$; **fails** at $p=4/3$ (entry $-7/81$).
* C11 mirror, exact at $p=4/3,5/4$. C12 full chain at $p=2/5$ on a rank-3 rational mixed state and a reviewer pure state, ranks $5,6,10,11$, rotated and unrotated $Q$: exact five-term decomposition, $\operatorname{Tr}QH_1\ge2r-6$, $\operatorname{Tr}QH_2$ identity and $\ge r-5$, $\operatorname{Tr}[Q\Phi]\ge\text{ref}_r$ ($17/625,33/625,97/625,113/625$). C13 equality case attained exactly.

**B. `reviewer-adversarial-search-v1.py` / `-v2.py`** — numpy, seed 20261028, single-thread BLAS; self-checks (partial-trace vs twirl erasure, identity (8), self-adjointness, mirror) pass. Projected-gradient descent on the Stiefel manifold for $\lambda_{\min}(H_1(Q)+\widetilde Q)-(2r-5)$ from Haar and structured starts, and on pure $\psi$ for $\mathrm{bottom}_r(\Phi_p^{\otimes4}(\psi))-\text{ref}_r(p)$ (pure states suffice by concavity). v1 (03:43:36Z–03:44:15Z, 210 starts/rank) reported $q$ in the computational rather than rotated frame in its *descriptive* minimiser statistics only; v2 (03:45:10Z–03:46:16Z, 520 starts per claimed rank, 260 per informational rank) fixes that diagnostic. Results (v2): minimum dual margins $-1.3\times10^{-14},-1.3\times10^{-14},-2.3\times10^{-14},-3.2\times10^{-14}$ at ranks $5,6,10,11$, every minimiser at $S=12,c=1,q_{\rm rot}=1$ with $q-(S-8)/4$ at roundoff — i.e. the search converges onto the proven tight boundary and finds **no violation**; negative control (false threshold $7.05$ at rank 6) **does** report a violation; output-comparison minima over $p\in\{0.05,0.2,0.4,0.6,0.8,0.95,1,1.1,1.25,4/3\}$ and $r\in\{5,6,10,11\}$ all within $[-3.3\times10^{-16},\,4.2\times10^{-10}]$ (tight, no violation); random-pair margins for $\operatorname{Tr}QH_1-(2r-6)$ and $\operatorname{Tr}QH_2-(r-5)$ are $\ge4.9$ and $\ge6.4$ (uninformative but consistent). Informational only: at ranks $7,8,9$ the same search also found no violation ($\approx-2\times10^{-14}$); the packets neither claim nor prove those ranks and nothing is concluded here.

**C. `reviewer-exact-reproduction-v1.py`** — with my exact library, the packet-98 §4 quoted figures for its named projector and state reproduce exactly: $\operatorname{Tr}Q(H_1+\widetilde\rho)=79606/5625$, $\operatorname{Tr}QH_2=67243/5625$, $\operatorname{Tr}[Q\Phi_{2/3}]=\operatorname{Tr}[\widetilde Q\Phi_{4/3}]=68864/151875>13/81$, remainder at $p=2/3$ equal to $(3\rho+F/2)/81$, sequential = Pauli-expansion channel (run 03:47:57Z, exit 0).

Floating-point results are evidence about the searched instances only; the exact controls are proofs about the specific rational instances only. Neither is a universal proof; the universal claims rest on the written argument of §2.

---

## 4. Findings

**FATAL: none. MAJOR: none.** I found no gap, sign error, missing case or unstated premise in the written arguments of packets 98 and 100 after independent reconstruction of every step.

**MINOR (presentation / reproducibility; none affects the proofs):**

1. *Packet 100 §4, reproducibility.* The rank-10/11 example projectors are described as including "respectively five and six weight-two basis vectors" without naming them, so the quoted state-dependent traces $(41054/1875,\,99743/5625)$, $(44804/1875,\,105368/5625)$, $106364/151875$, $113864/151875$ cannot be reproduced from the packet text alone; they would require reading checker 99, which is outside this manifest and was not read. (The frame-independent figures $S=7108/625$, $c=429/625$, $q=576/625$ *are* determined by the text — $S$ does not depend on which weight-two vectors are used — and agree with my computation of the rank-6 analogue.) Not load-bearing for the universal claim.
2. *Packet 98 eq. (6).* "the rank of Q" is listed among the ingredients of $\operatorname{Tr}(QN)\ge12-2q-4$; the resulting occupancy bound $S\le8+4q$ is rank-independent (the $2\cdot6$ cancels against $4\cdot6$). Harmless.
3. *Packet 98 §1 covariance sentence.* Covariance of the spin flip under local unitaries is asserted without the $U(2)$-vs-$SU(2)$ phase remark; it is true (§2.2(a)) and verified exactly with a $\det=-1$ factor (C4). Harmless.
4. *Packet 98 §2 / packet 100 (7).* "$\ge\widetilde\rho$" is correct and could be stated as $\ge\rho+\widetilde\rho$; the dropped $\operatorname{Tr}[Q\rho]+\tfrac12\operatorname{Tr}[QF(\rho)]\ge0$ is handled correctly as a dropped non-negative term. Harmless.
5. *Packet 98 §3, scope statement.* "Together with the separately written tail comparison 94, this candidate gives original global $k=10,\dots,15$ plus trace" leans on packet 94, which is outside this manifest and not reviewed; this review covers $k=10$ (packet 98) and $k=5,6$ and, via the rank-5 case, $k=11$ (packet 100) only.
6. *Author checker 97 (read only).* Its `h1`/`h2` rescale normalised erasures by $8$ and $4$, consistent with the packets' definitions, and it depends on author modules 66/26 (not in the manifest). It was not executed; its quoted numbers were instead reproduced with reviewer code (control C). Its finite checks are, as the packet itself says, not a universal proof.

No counterexample was found to any claimed statement; none is asserted.

---

## 5. Verdicts (separate)

**V1 — Dual lemma $H_1(Q)+\widetilde Q\ge(2r-5)I$, $r\in\{5,6,10,11\}$ (rank 6: $\ge7I$).** Reconstructed in full (§2.2). **Correct for every complex orthogonal projector of those ranks**; no FATAL/MAJOR/MINOR mathematical defect. Exact dependencies: Ky Fan; local-unitary covariance of $H_1$ and spin flip; spectra of $Z_{\rm tot}$ (top-$r$ sum $12$) and of the three-site sums (top-$r$ sum $\le10$ at these ranks only); $\operatorname{Tr}[Q\Pi_1]\le4$ and $N\ge2I-2E_0-\Pi_1$; the $2\times2$ projector lemma with $0<c\le1$. The bound is tight (zero eigenvalue at $S=12$). Instances tested exactly (C3–C6) and adversarially (B) are consistent and add no scope beyond the written proof. The proof does not extend to ranks $7,8,9$ (three-site cut $11,12,11$); nothing is claimed there.

**V2 — Original global $k=10$ (packet 98).** **Correct for every four-qubit density, every complex rank-10 projector and every $p\in[0,4/3]$**, given V1 at rank 6, the exact identity (8), the $H_1$ bottom-6 bound ($\ge6$), the retained-erasure Loewner bound on $[0,1]$, Ky Fan, and the $p\mapsto2-p$ spin-flip mirror on $[1,4/3]$. No FATAL/MAJOR; MINOR notes 2–6 above are presentational. Reproduces $\text{ref}_6=b^4+4ab^3+a^2b^2$ exactly and tightly.

**V3 — Original global $k=5$ and $k=6$ (packet 100; rank 11 and rank 10), and $k=11$ (rank 5).** **Correct for every density, every projector of the required rank and every $p\in[0,4/3]$**, by the same chain with constants $(2r-5,\,2r-6,\,r-5)$ and reference $b^4+4ab^3+(r-5)a^2b^2$; verified rank by rank (§2.6; C1, C3, C4, C12, C13; B). No FATAL/MAJOR; MINOR note 1 (unnamed weight-two vectors) is a documentation gap in the finite example only.

**What is proved for all densities versus only for tested instances.** The universal statements in V1–V3 are established by the written arguments as independently reconstructed in §2 (proof-level claims, same-harness). The exact controls prove only the specific rational instances they touch, and the floating-point search is evidence only; neither extends the scope of §2, and neither was needed to close any gap in it.

**Not claimed.** Nothing about $k=3$, $k=7,8,9$, $k=2,4$, full output majorization, packet 94's $k=12$–$15$, novelty, or any human / independent-family / formal-kernel acceptance. Same-harness review only.

**Overall:** V1 PASS, V2 PASS, V3 PASS at the written-argument level; no INCONCLUSIVE items.

---

## 6. Residual risks

* Same-harness review: a shared blind spot between author and reviewer is possible in principle; the exact controls (including the $S>10$, non-diagonal, rotated and tight cases, and the four negative controls) were designed to catch sign, frame and threshold errors rather than to re-run the author's checks.
* Standard linear-algebra facts (Ky Fan, Schur complement/Sylvester, transpose preserving projectors) are used without re-derivation.
* The "physical" interval $[0,4/3]$ is the complete-positivity range of $\Phi_p$ as defined; if a different channel parametrisation were intended, the mirror map and the reference spectrum would need re-checking (not indicated by the packets).

---

## 7. Artifacts and disclosures

Written in this directory (hashes listed in `reviewer-receipts-v1.txt`, computed after this file was finalised):

* `review-v1.md` (this file)
* `reviewer-exact-controls-v1.py`, `reviewer-exact-controls-v1.result.json`
* `reviewer-adversarial-search-v1.py`, `reviewer-adversarial-search-v1.result.json`
* `reviewer-adversarial-search-v2.py`, `reviewer-adversarial-search-v2.result.json`
* `reviewer-exact-reproduction-v1.py`, `reviewer-exact-reproduction-v1.result.json`
* `reviewer-receipts-v1.txt`

Disclosure: a `__pycache__/` directory containing a byte-compiled copy of `reviewer-exact-controls-v1.py` was created by my one-time `python3 -m py_compile` syntax check before the first run; the harness blocked `rm`, so it remains in the directory. It contains no evidence and all runs used `python3 -B`. Scripts were staged through the session scratch area (`local://`) and copied in; the copies in this directory are the ones that ran, and their hashes are in the receipts.
