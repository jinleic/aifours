# author-candidate-v1.md

## Actual five-span amplitude obstruction: the rank-four graph branch is impossible

**Status: AUTHOR proof candidate; not independently reviewed or parent-adopted.**

**Result.** In the frozen named actual m116 five-span caller, the required \(U_0\) divisibility, energy and amplitude cap exclude **every graph \(f\) whose quadratic polar form has rank four**, uniformly over all common phases \(r\), all allowed physical block placements and signs, and every carried balance frequency. No \(U_3\) choice or complementary \(V\) can repair this obstruction.

For the remaining rank-two graph branch, the same argument determines the direction of the eight \(U_0\) spectral zeros. Once the original balance frequency is carried correctly, it determines the **entire zero set**, yielding an exact autocorrelation formulation of the remaining \(U_0\) amplitude-and-balance condition.

This is an exclusion of one complete meaningful branch, not a construction of a feasible even half, a whole-five-span exclusion, or an NL242 conclusion.

Returned in full for Main materialization under the read-only role; no repository file was written.

## 1. Frozen scope and evidence

Assignment: `f599-actual-five-span-all-four-fibre-amplitude-feasibility-frontier`.

Parent-supplied pins:

- Manifest: `c1182bcc19c2b928764c2b1a4369d68c2efd0ffd0c2440f44e9580ebf79dffbf`.
- Freeze receipt: `03195296504bf291caea273dfb49249c612a012f4e721430774b0e93daede5c5`.
- Literal packet: `22214f0c3d91fb9a20add2b0e17247d6030c5b620dac4fb2c644729f17387a3f`.

The complete packet supplies:

- **S1, LF1–51:** actual common four-fibre counts, \(U_0\) divisibility criterion, energies, unpaid amplitude caps and carried balance.
- **S2, LF1–38:** actual normalized graph, common bent-phase conditions and rank-two/rank-four graph census.
- **S3, LF1–37:** named actual m116 caller and five-/six-span separation.

These are the scientific input scopes used below. Their underlying linked sources were not followed, and their earlier finite executions were not repeated or independently certified here.

The proof is written and general. It uses no newly selected example, finite probe, search, scientific execution, or external source.

## 2. Actual objects and target condition

Keep the frozen common physical coordinates
\[
R=\mathbb F_2^6,\qquad Q=\mathbb F_2^2.
\]
Let \(u(c,w)\) be the **same physical ternary half-function** throughout, and put
\[
x(c)=U_0(c),\qquad U_1(c)=3a(c),\qquad U_2(c)=g(c),\qquad y(c)=U_3(c).
\]
Use the unnormalized Walsh transform
\[
\widehat x(\xi)=\sum_{c\in R}x(c)(-1)^{\xi\cdot c}.
\]

The adopted actual counts give
\[
x=1_S-2\,1_P+2\,1_W-4\,1_N,
\qquad |S|=16,\quad |W|=10,
\]
with \(P\subseteq S\), \(N\subseteq W\), and \(S\cap W=\varnothing\). Consequently,
\[
x(c)\bmod2=1_S(c),\qquad
\sum_c x(c)^2=16+4\cdot10=56. \tag{1}
\]

The required criterion (C) makes every \(\widehat x(\xi)\) divisible by eight. If the still-unpaid cap
\[
|\widehat x(\xi)|\le8\quad\text{for every }\xi \tag{2}
\]
also holds, then
\[
\widehat x(\xi)\in\{0,\pm8\}.
\]
Parseval and (1) imply exactly 56 nonzero coefficients and eight zeros. Define their actual zero set
\[
Z=\{\xi:\widehat x(\xi)=0\},\qquad |Z|=8. \tag{3}
\]

The normalized support from S2 is
\[
S=\{(2j+f(j,b),d_b):j,b\in\mathbb F_2^2\},
\qquad d_b\in(1,2,4,7).
\]
Write the bits of \(d\) as \(d_0,d_1,d_2\), and set
\[
\ell(c)=d_0+d_1+d_2,\qquad b=(d_1,d_2).
\]
Together with the low bit \(h_0\) of \(h\), these give linear coordinates
\[
(\ell,h_0,j,b)
\]
on \(R\). The support indicator therefore has the exact Boolean-polynomial expression
\[
1_S=\ell\bigl(1+h_0+f(j,b)\bigr). \tag{4}
\]

The frozen classification says that \(f\) is quadratic and its polar rank is either two or four. No graph or common phase is fixed in the following argument.

## 3. Two elementary lemmas

### Lemma 1: Walsh divisibility bounds parity degree

If \(v:\mathbb F_2^n\to\mathbb Z\) has every Walsh coefficient divisible by \(2^k\), then \(v\bmod2\) has Boolean algebraic degree at most \(n-k\).

**Proof.** Write \(\widehat v=2^k b\), with integer \(b\). Walsh inversion gives
\[
v(c)=2^{k-n}\sum_\xi b(\xi)
       \prod_{i:\xi_i=1}(1-2c_i).
\]
The coefficient of a monomial \(c_I\) of degree \(|I|\) is an integer multiple of
\[
2^{k-n+|I|}.
\]
For \(|I|>n-k\), this coefficient is even. All coefficients of the multilinear polynomial for the integer-valued function \(v\) are integers, by the usual finite-difference formula. Reduction modulo two thus removes every term of degree greater than \(n-k\). ∎

### Lemma 2: minimum-weight Boolean polynomials

A nonzero Boolean polynomial of degree at most \(d\) on \(\mathbb F_2^n\) has weight at least \(2^{n-d}\). If equality holds, its support is an affine \((n-d)\)-flat.

**Proof.** Induct on the number of variables, writing
\[
P(c',s)=P_0(c')+sP_1(c'),\qquad \deg P_1\le d-1.
\]
If \(P_1=0\), the weight doubles and induction applies.

Otherwise,
\[
\operatorname{wt}(P_0)+\operatorname{wt}(P_0+P_1)
\ge \operatorname{wt}(P_1)\ge2^{n-d}.
\]
Equality forces \(P_1\) to have minimum weight and \(P_0\) to vanish outside its support. By induction, that support is an affine flat of codimension \(d-1\) in the \(c'\)-space. In affine coordinates where it is \(z_1=\cdots=z_{d-1}=0\),
\[
P_0=\prod_{i=1}^{d-1}(1+z_i)\,Q(t).
\]
The degree bound forces \(\deg Q\le1\). On this flat, the support of \(P\) is the graph \(s=1+Q(t)\), an affine \((n-d)\)-flat. The constant and degree-\(n\) boundary cases give the induction bases. ∎

## 4. The amplitude cap forces an affine zero flat

Define the actual dual ternary array
\[
z(\xi)=\widehat x(\xi)/8\in\{0,\pm1\}.
\]
Since the Walsh transform squares to \(64I\),
\[
\widehat z(c)=8x(c).
\]
Lemma 1, with \(n=6,k=3\), shows that \(z\bmod2\) has degree at most three. As functions modulo two,
\[
1_Z=1+z.
\]
Thus \(1_Z\) has degree at most three and weight eight. Lemma 2 forces
\[
Z=\zeta+K, \tag{5}
\]
where \(K\) is a three-dimensional linear subspace of \(R^*\).

Let
\[
L=K^\perp\subseteq R,\qquad \dim L=3.
\]
The zero-flat transform is
\[
\widehat{1_Z}(c)=8(-1)^{\zeta\cdot c}1_L(c). \tag{6}
\]

There is a further restriction linking this actual zero flat to the physical odd support \(S\). Let
\[
B_-=\{\xi:z(\xi)=-1\}.
\]
The exact identity
\[
z=1-1_Z-2\,1_{B_-}
\]
and (6) give
\[
x(c)=8\delta_0(c)-(-1)^{\zeta\cdot c}1_L(c)
      -\frac14\widehat{1_{B_-}}(c). \tag{7}
\]
In particular, every coefficient of \(\widehat{1_{B_-}}\) is divisible by four.

To determine the parity degree of its quotient, put
\[
m_I=\#\{\xi\in B_-:\xi_i=1\text{ for every }i\in I\}.
\]
Then
\[
\widehat{1_{B_-}}(c)
=\sum_I(-2)^{|I|}m_Ic_I.
\]
Divisibility by four at all \(c\) implies \(4\mid m_\varnothing\) and \(2\mid m_{\{i\}}\). After division by four, every term of degree at least three has even coefficient. Hence
\[
q(c):=\frac14\widehat{1_{B_-}}(c)\pmod2
\]
is quadratic.

Reducing (7) modulo two and using (1) proves the central identity
\[
\boxed{1_S+1_L=q,\qquad \deg q\le2.} \tag{8}
\]

This is a consequence of the **amplitude cap**, not merely the previously adopted divisibility criterion.

## 5. Uniform exclusion of every rank-four graph

Let \(B_f\) denote the quadratic polar two-form of \(f\), on the four linear coordinates \((j,b)\).

For clarity, compare highest-degree Boolean terms in the associated graded polynomial ring. Its degree-one generators square to zero, so this is exterior algebra over \(\mathbb F_2\). Equation (4) gives the cubic leading form
\[
[1_S]_3=\ell\wedge B_f. \tag{9}
\]

Choose three independent linear equations \(\lambda_1,\lambda_2,\lambda_3\) defining the linear three-space \(L\). Then
\[
1_L=\prod_{i=1}^3(1+\lambda_i),
\qquad
[1_L]_3=\lambda_1\wedge\lambda_2\wedge\lambda_3. \tag{10}
\]
Equation (8) cancels all cubic terms, so
\[
\ell\wedge B_f
=\lambda_1\wedge\lambda_2\wedge\lambda_3. \tag{11}
\]

The right side is nonzero and decomposable. Wedging (11) with \(\ell\) shows
\[
\ell\in\operatorname{span}(\lambda_1,\lambda_2,\lambda_3).
\]
Choose a basis of this span beginning with \(\ell\). In the quotient of the linear-form space by \(\langle\ell\rangle\), equation (11) then says that \(B_f\) is a nonzero decomposable two-form.

A nonzero decomposable two-form \(p\wedge q\) has polar rank two: its associated alternating matrix has image in the span of \(p,q\), and independence makes that rank exactly two. But quotienting by \(\ell\) does not change the rank of \(B_f\), which uses only the four independent \((j,b)\) coordinates.

Therefore
\[
\boxed{\operatorname{rank}B_f=2.} \tag{12}
\]

This contradicts the entire rank-four graph branch.

### Exact exclusion scope

For **every** normalized graph \(f\) of polar rank four and **every** common phase \(r\), there is no common physical \(u\) having the frozen actual counts and satisfying both:

1. the required divisibility of all 64 \(U_0\) Walsh coefficients by eight; and
2. the required cap \(|F_0|\le8\).

The contradiction precedes the \(F_3\) cap, \(J=1\), carried balance and complementary \(v\). These additional requirements cannot rescue an excluded choice.

Using the adopted S2 census, this eliminates all **384 rank-four labeled graphs** and their \(384\) common phases each:
\[
384\cdot384=147456
\]
normalized two-fibre parameter pairs. This is not an original-caller census, an equivalence-class count, or a new finite execution.

The proof fixes no graph, phase, sign pattern, zero position or convenient gauge.

## 6. Exact amplitude-and-balance condition in the surviving rank-two branch

For rank two, write
\[
B_f=p\wedge q
\]
with independent linear forms \(p,q\) on \((j,b)\). Equation (11) determines the normal space of \(L\):
\[
\boxed{L=\ker\ell\cap\ker p\cap\ker q.} \tag{13}
\]
Indeed, a nonzero decomposable three-form determines the span of its three factors. Thus \(L\) is fixed by the graph’s cubic support term; it is not a newly adjustable parameter.

In particular, \(L\subseteq\ker\ell\), and the primal full-block direction \(e\), which toggles \(h_0\), belongs to \(L\).

Let \(t\in R^*\) be the **specifically carried original balance frequency** from S1. Required original balance means \(F_0(t)=0\). Equations (5) and (13) therefore force
\[
\boxed{Z=t+L^\perp.} \tag{14}
\]
There is no freedom to replace this by an arbitrary normalized zero.

Define the actual autocorrelation
\[
A_x(v)=\sum_{c\in R}x(c)x(c+v).
\]
The remaining \(F_0\) spectral condition and carried balance are equivalent to
\[
\boxed{
A_x(v)=64\delta_0(v)-8(-1)^{t\cdot v}1_L(v)
\quad\text{for every }v\in R.
} \tag{15}
\]

**Forward direction.** Since \(F_0^2=64(1-1_Z)\), inverse Walsh transformation and (14) give (15).

**Reverse direction.** Walsh transformation of (15) gives
\[
F_0(\xi)^2=64\bigl(1-1_{t+L^\perp}(\xi)\bigr).
\]
Hence \(F_0\in\{0,\pm8\}\), its eight zeros are exactly the required coset, and \(F_0(t)=0\).

Equivalently, the zero-flat condition alone requires, on every actual coset \(D\) of \(L\),
\[
\sum_{c\in D}(-1)^{t\cdot c}x(c)=0. \tag{16}
\]
This follows by Walsh inversion on \(R/L\); it does not replace the physical two-dimensional \(Q\).

Thus the surviving \(U_0\) problem is no longer merely divisibility: it requires the prescribed autocorrelations (15), with the zero direction fixed by \(f\) and the zero coset fixed by the original balance.

## 7. Physical four-fibre interface remains mandatory

Neither the exclusion nor the residual formulation permits choosing \(F_3\) independently. The actual inverse remains
\[
u(c,w)=\frac14\left[
x(c)+3a(c)\chi_1(w)+g(c)\chi_2(w)+y(c)\chi_3(w)
\right].
\]

On an \(S\)-block, \(|U_1|=3\) forces all three nonzero entries to have signs \(a\chi_1(w)\). If \(w_*\) is the missing position, then
\[
x=-a\chi_1(w_*),\qquad
g=-a\chi_3(w_*),\qquad
y=-a\chi_2(w_*).
\]
Consequently,
\[
\boxed{x\in\{\pm1\},\qquad y=-agx\quad\text{on }S.} \tag{17}
\]

The remaining blocks retain their frozen physical forms:

- two full blocks: \(x=y=0\);
- four \(D0\) blocks: \((x,y)=(\pm2,0)\);
- eighteen \(D3\) blocks: \((x,y)=(0,\pm2)\);
- six \(Z2\) blocks: \((x,y)=(\pm2,\pm2)\);
- one \(Z4\) block: \((x,y)=(0,\pm4)\);
- seventeen \(Z0\) blocks: \((x,y)=(0,0)\).

These give, on the same inverse,
\[
|\operatorname{supp}u|
=16\cdot3+2\cdot4+22\cdot2+6\cdot2+4=116,
\]
and
\[
\sum x^2=56,\qquad \sum y^2=128.
\]

For a remaining rank-two candidate, all of the following are still required:

1. The common conditions \(f+q\), \(r\), and \(r+f\) are bent, at the adopted normalization.
2. The actual block choices satisfy (17), the displayed counts and local \(H=0\).
3. Their actual \(x\) satisfies (15), with the tracked \(t\).
4. Their actual \(y\) has \(J=1\) and all 64 caps \(|F_3|\le12\).

Under item 4, S1’s residue and energy argument forces \(F_3\in\{\pm4,\pm12\}\), with exactly eight magnitude-four positions. This candidate supplies no such \(y\).

The auxiliary three-space \(L\) is not substituted for physical \(Q\), the primal full-block direction \(e\), a dual normal, or the original shift \(T\).

## 8. Precise residual and assurance boundary

The **512 rank-two graphs** and their common phases remain open as potential necessary-interface parameters:
\[
512\cdot384=196608
\]
labeled pairs before the remaining amplitude and physical constraints. This is not a feasibility assertion.

No complete even-half \(u\) is constructed here. In particular, simultaneous satisfaction of (15), physical \(y\), \(J=1\), the \(F_3\) cap and all named rank/\(T\) requirements remains unproved.

Even a successful even half would still require signs on its **actual 140-point complement**, with:

- an odd number of negative signs;
- all 256 odd-half Walsh coefficients bounded by 14;
- the same tracked physical coordinates and original \(T\).

Only after those obligations are met can the actual \(u\pm v\) inverse supply the 512 Boolean signs, original balance and full Walsh bound 28.

Nothing here excludes the surviving rank-two five-span branch, either six-span branch, other m116/m114 classes, or the full NL242 target.

## 9. Read chronology and execution disclosure

Before scientific packet reading or derivation, I read the manifest, freeze receipt, all thirteen listed controls, parent dispatch receipt and parent metadata supply through their endings, then delivered a direct pre-body ACK to `agent://Main`.

I next read the complete 128-LF literal packet in ordered raw windows of at most 20 LF through its ending. The derivation above followed that complete read.

No scientific executable, search, new selected diagnostic, linked scientific source, external model, installation or repository mutation was used. There is no experiment result or unrun search program underlying the conclusion. Parent-supplied hashes and clocks are not represented as independently measured child metadata.

All historical held episodes and their proof, method, selection, planning, reporting, verification and confidence consumers—including the entire f586 episode—remain NONINPUT. No cognition-isolation certificate is asserted.

**Acceptance boundary:** a self-contained written obstruction for the entire rank-four normalized actual five-span graph branch, together with an exact rank-two \(U_0\) amplitude-and-carried-balance residual. Independent checking and parent disposition remain required; no human, independent-family, formal/kernel, novelty or original-target acceptance is claimed.