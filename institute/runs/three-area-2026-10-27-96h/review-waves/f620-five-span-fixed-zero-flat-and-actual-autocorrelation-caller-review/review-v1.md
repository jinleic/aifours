# F620 written review — fixed zero flat and actual autocorrelation caller

**Role:** WRITTEN; scientific execution **NOTRUN**.  
**Reviewed candidate:** f599, complete S1 logical LF1–379.  
**Result:** **SUPPORTED at the stated conditional scope.**  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**

This is the complete review body for parent materialization. No repository file was written. This review supplies same-harness written checking only; it does not adopt the candidate or supply independent-family, human, formal/kernel, novelty, or original-target acceptance.

## 1. Frozen bindings and reading chronology

The following bindings are **parent-supplied metadata**, not independently measured child hashes:

- Manifest SHA256: `9d649ab7d3530f90b7f14a0de7650ba885803402adcdbfb5a24efe9c07c0cbc7`.
- Freeze-receipt SHA256: `ba9e844916bfec76f9bfceda5360328da4b0aaca5af8603db5eff6c26614ce77`.
- Literal-packet SHA256: `e4e9d4eb6019668093408ba7ee74eb35784db0114b669a5d60c97bf3015f3561`.

Before reading mathematical packet content, I read:

1. The complete manifest.
2. The complete freeze receipt.
3. The complete parent-live-metadata supply.
4. The parent dispatch receipt.
5. Every listed `controls_before_body` file, through its ending, as **status-only controls**.

I then delivered a direct administrative **PREBODY ACK to `agent://Main`**. Only afterward did I read the complete packet, in contiguous ordered raw windows of at most 20 LF: LF1–20 through LF441–460, then LF461–470. Mathematical reconstruction began after that final window.

Complete scientific coverage:

- **S1:** f599 author candidate, logical LF1–379.
- **S2:** common actual four-fibre/XOR/balance/complement disposition, LF1–51.
- **S3:** normalized actual bent-graph/two-fibre disposition, LF1–38.

No linked scientific source, author code, sibling review, held mathematical payload, or held consumer was opened. Historical finite results appearing in S2 and S3 are imported only at those dispositions’ stated scopes; they were not rerun or independently certified here.

No new selected mathematical example, parameter instance, frequency probe, enumeration, scientific executable, CAS, solver, external model, build, test, or lint was used.

## 2. Claim dispositions

| Candidate claim | Source scope | Disposition |
|---|---|---|
| Walsh divisibility bounds the parity degree | S1 LF96–109 | **SUPPORTED**, reconstructed directly |
| Minimum-weight degree-\(d\) Boolean support is an affine flat in the equality case | S1 LF111–130 | **SUPPORTED**, including the equality argument |
| The \(U_0\) cap forces an eight-point affine spectral zero flat | S1 LF132–158 | **SUPPORTED** under the actual energy and divisibility assumptions |
| The actual odd support and the primal annihilator satisfy \(1_S+1_L=q\), \(\deg q\le2\) | S1 LF161–196 | **SUPPORTED**, including quotient integrality and parity degree |
| Every rank-four graph is excluded | S1 LF198–249 | **SUPPORTED**, uniformly over the stated common phases and physical choices |
| For rank two, \(L=\ker\ell\cap\ker p\cap\ker q\), independently of the factor basis | S1 LF251–263 | **SUPPORTED** |
| The specifically carried balance fixes \(Z=t+L^\perp\) | S1 LF265–269 | **SUPPORTED** |
| The full remaining \(U_0\) spectral-and-balance condition is equivalent to the displayed autocorrelation identity for every shift | S1 LF271–289 | **SUPPORTED** at the actual-caller scope |
| Weighted sums on cosets characterize vanishing on the prescribed spectral coset | S1 LF291–295 | **SUPPORTED**; not a replacement for the amplitude condition |
| The physical \(U_3\) relation and all block counts remain mandatory | S1 LF299–345 | **SUPPORTED** |
| The numerical products count normalized two-fibre parameters, not feasible original callers | S1 LF243–247, LF351–355; S3 LF30 | **SUPPORTED as scoped imported bookkeeping** |
| The surviving branch, complementary half, and full target remain unpaid | S1 LF349–367 | **SUPPORTED as the correct limitation** |

No claim below is interpreted as asserting feasibility from divisibility alone.

## 3. Independent reconstruction of the spectral-zero argument

### 3.1 Actual energy and the eight zeros

For the same physical \(x=U_0\), S2 LF21–25 supplies
\[
x=1_S-2\,1_P+2\,1_W-4\,1_N,
\qquad |S|=16,\quad |W|=10,
\]
with \(P\subseteq S\), \(N\subseteq W\), and the physical supports \(S,W\) disjoint. Therefore
\[
x\bmod2=1_S,\qquad \sum_c x(c)^2=56.
\]

Under criterion (C), every unnormalized six-variable Walsh coefficient is divisible by eight. Adding the required cap gives
\[
F_0(\xi)=\widehat x(\xi)\in\{0,\pm8\}.
\]
Unnormalized Parseval is
\[
\sum_\xi F_0(\xi)^2=64\sum_c x(c)^2.
\]
Consequently, there are exactly 56 nonzero coefficients and eight zeros.

This uses the actual \(U_0\) energy, not the energy of an independently selected spectrum.

### 3.2 Walsh divisibility and parity degree

For a general integer-valued function \(v\) on \(\mathbb F_2^n\), write
\[
\widehat v(\xi)=2^k b(\xi),\qquad b(\xi)\in\mathbb Z.
\]
Walsh inversion expands as
\[
v(c)=2^{k-n}\sum_\xi b(\xi)
       \prod_{i:\xi_i=1}(1-2c_i).
\]
The coefficient of a degree-\(s\) multilinear monomial is an integer multiple of \(2^{k-n+s}\). When \(s>n-k\), that coefficient is even. The multilinear coefficients of the integer-valued function are themselves integers by finite differences, so reducing modulo two removes every such term.

This establishes S1 Lemma 1 without an external theorem import.

### 3.3 Minimum-weight equality

For the Boolean decomposition
\[
P(c',s)=P_0(c')+sP_1(c'),
\]
the nonzero-\(P_1\) case gives
\[
\operatorname{wt}(P_0)+\operatorname{wt}(P_0+P_1)
\ge\operatorname{wt}(P_1)\ge2^{n-d}.
\]

At equality, \(P_0\) must vanish outside the support of \(P_1\). Induction makes that support an affine flat of codimension \(d-1\). In affine coordinates adapted to that flat,
\[
P_0=\prod_{i=1}^{d-1}(1+z_i)\,Q(t).
\]
The Boolean degree bound forces \(\deg Q\le1\): the term containing all \(z_i\) prevents a higher-degree term of \(Q\) from disappearing. On the flat, the support of \(P\) is therefore the affine graph
\[
s=1+Q(t).
\]
The \(P_1=0\) case doubles the inductive support, with the stated boundary cases handling the endpoints.

Thus the equality characterization needed here is established, not merely quoted.

### 3.4 Applying the lemmas to the actual dual array

Set
\[
z(\xi)=F_0(\xi)/8.
\]
Then \(z\in\{0,\pm1\}\), and the double-Walsh identity gives
\[
\widehat z=8x.
\]
Lemma 1 makes \(z\bmod2\) a degree-at-most-three Boolean function. Modulo two,
\[
1_Z=1+z.
\]
Its weight is eight. The minimum-weight equality result therefore gives
\[
Z=\zeta+K,\qquad \dim K=3.
\]
Writing
\[
L=K^\perp,
\]
one obtains the exact unnormalized transform
\[
\widehat{1_Z}(c)=8(-1)^{\zeta\cdot c}1_L(c).
\]

The resulting \(L\) is a primal three-space. It is not the physical two-dimensional \(Q\).

## 4. The quadratic parity identity

Let
\[
B_-=\{\xi:z(\xi)=-1\}.
\]
The exact integer identity
\[
z=1-1_Z-2\,1_{B_-}
\]
gives
\[
x(c)=8\delta_0(c)-(-1)^{\zeta\cdot c}1_L(c)
-\frac14\widehat{1_{B_-}}(c).
\]

Because the other terms are integer-valued, \(\widehat{1_{B_-}}\) is divisible by four at every point.

For the general multilinear character expansion
\[
\widehat{1_{B_-}}(c)=\sum_I(-2)^{|I|}m_Ic_I,
\]
divisibility of the function by four implies divisibility of all its multilinear coefficients by four, again by finite differences. In particular, the constant and degree-one coefficients have the integrality claimed in S1 LF185. After division by four, every degree-at-least-three coefficient is even.

Hence
\[
q(c)=\frac14\widehat{1_{B_-}}(c)\pmod2
\]
has degree at most two. Reducing the exact identity for \(x\) modulo two yields
\[
1_S+1_L=q.
\]

The sign character disappears modulo two, and \(8\delta_0\) contributes nothing. There is no omitted integrality assumption at this step.

## 5. Rank-four exclusion and the uniquely determined rank-two direction

### 5.1 The actual support has cubic form \(\ell\wedge B_f\)

In the supplied normalized coordinates,
\[
S=\{(2j+f(j,b),d_b)\},
\qquad
\ell=d_0+d_1+d_2.
\]
The four listed \(d_b\) are precisely the odd-parity \(d\)-values, and \(h_0=f(j,b)\) specifies the graph point. Thus
\[
1_S=\ell(1+h_0+f(j,b)).
\]

In the associated graded Boolean polynomial algebra, the degree-one generators square to zero. Its cubic leading form is consequently
\[
[1_S]_3=\ell\wedge B_f.
\]

For any independent defining equations \(\lambda_1,\lambda_2,\lambda_3\) of the linear three-space \(L\),
\[
1_L=\prod_{i=1}^3(1+\lambda_i),
\qquad
[1_L]_3=\lambda_1\wedge\lambda_2\wedge\lambda_3.
\]
The quadratic parity identity cancels these cubic forms:
\[
\ell\wedge B_f
=\lambda_1\wedge\lambda_2\wedge\lambda_3.
\]

### 5.2 Why this excludes rank four

For a nonzero decomposable three-form, the linear forms whose wedge with it vanishes are exactly the span of its three factors. Wedging the last identity with \(\ell\) therefore shows
\[
\ell\in\operatorname{span}(\lambda_1,\lambda_2,\lambda_3).
\]

Choose a factor basis of that span beginning with \(\ell\). After quotienting the linear-form space by \(\langle\ell\rangle\), the identity says that the image of \(B_f\) is a nonzero decomposable two-form.

The form \(B_f\) uses only the four independent \((j,b)\) coordinates. Removing the independent coordinate \(\ell\) does not change its alternating rank. A nonzero decomposable two-form has rank two, so a rank-four \(B_f\) cannot satisfy the identity.

This contradiction uses neither a particular \(f\), a phase \(r\), a choice of signs, nor a choice of carried balance frequency. It also occurs before any \(U_3\) or complementary-half completion. Those later constraints therefore cannot repair the rank-four branch.

### 5.3 Rank-two direction and factor-basis independence

For rank two, write
\[
B_f=p\wedge q
\]
with independent forms on \((j,b)\). The cubic form is then
\[
\ell\wedge p\wedge q.
\]
Its factor span is uniquely determined, so
\[
L^\perp=\operatorname{span}(\ell,p,q),
\qquad
L=\ker\ell\cap\ker p\cap\ker q.
\]

Changing the factor basis of the same nonzero decomposable \(B_f\) changes neither its factor span nor this kernel intersection.

The primal full-block direction \(e\) toggles \(h_0\) only. All three defining forms annihilate it, so \(e\in L\). This does not identify \(L\) with \(Q\), a dual normal, or the original shift \(T\).

## 6. Carried balance and exact autocorrelation equivalence

### 6.1 The prescribed coset is fixed by original balance

S2 LF35 explicitly requires tracking the original balance through
\[
u_N(c,w)=\eta\chi_t(c)u_O(Mc+b,w).
\]
At frequency \(t\), the character introduced by normalization cancels in the \(U_0\) Walsh sum, leaving the original DC sum up to the global sign. Thus original balance requires
\[
F_{0,N}(t)=0.
\]

Since the eight-zero set already has direction \(L^\perp\), its containing \(t\) forces
\[
Z=t+L^\perp.
\]
An arbitrary convenient normalized zero is not interchangeable with this tracked frequency.

### 6.2 Forward implication and normalization

For the actual \(x\), define
\[
A_x(v)=\sum_c x(c)x(c+v).
\]
Its unnormalized Walsh transform is
\[
\widehat{A_x}(\xi)=F_0(\xi)^2.
\]
Using
\[
F_0^2=64(1-1_{t+L^\perp}),
\]
and
\[
\widehat{1_{t+L^\perp}}(v)
=8(-1)^{t\cdot v}1_L(v),
\]
Walsh inversion gives
\[
A_x(v)=64\delta_0(v)-8(-1)^{t\cdot v}1_L(v)
\quad\text{for every }v\in R.
\]

The factors \(64\) and \(8\) are correct for the stated unnormalized transform.

### 6.3 Reverse implication

Conversely, transforming this all-shift autocorrelation identity gives
\[
F_0(\xi)^2
=64\bigl(1-1_{t+L^\perp}(\xi)\bigr).
\]
Therefore
\[
F_0(\xi)\in\{0,\pm8\},
\]
the zeros are exactly the prescribed eight-point coset, and \(F_0(t)=0\). At \(v=0\), the identity also gives the required energy \(56\).

Accordingly, within the fixed actual-caller setting—including the actual support data and imported divisibility requirement—the displayed identity is an exact replacement for the remaining \(U_0\) spectral-and-carried-balance obligation. It is not a theorem that arbitrary cap, energy, and balance assumptions without the divisibility context force this identity.

### 6.4 What the weighted coset sums do and do not prove

Put \(g(c)=(-1)^{t\cdot c}x(c)\), and sum it on each coset \(D\) of \(L\). Fourier transformation on \(R/L\) identifies these coset sums with the values
\[
F_0(t+\eta),\qquad \eta\in L^\perp.
\]
Thus
\[
\sum_{c\in D}(-1)^{t\cdot c}x(c)=0
\quad\text{for every }D
\]
is equivalent to vanishing on the prescribed spectral coset.

This alone does not control coefficients outside that coset and therefore is not sufficient for the amplitude cap. S1 retains the full autocorrelation identity as the required residual; it does not replace it by the weaker coset-sum condition.

## 7. Physical four-fibre consumer audit

The argument must return to the same physical inverse
\[
u(c,w)=\frac14\bigl[x(c)+3a(c)\chi_1(w)
+g(c)\chi_2(w)+y(c)\chi_3(w)\bigr].
\]

On an \(S\)-block, support three and \(|U_1|=3\) force the three nonzero signs to be \(a\chi_1(w)\). If \(w_*\) is missing, character orthogonality gives
\[
x=-a\chi_1(w_*),\quad
g=-a\chi_3(w_*),\quad
y=-a\chi_2(w_*).
\]
Since \(\chi_1\chi_3=\chi_2\),
\[
y=-agx.
\]
Thus \(y\) is not independently assignable after choosing \(x,a,g\).

The remaining supplied physical block types are consistent with the same inverse:

- Full blocks: \(x=y=0\).
- \(D0\): \((x,y)=(\pm2,0)\).
- \(D3\): \((x,y)=(0,\pm2)\).
- \(Z2\): \((x,y)=(\pm2,\pm2)\).
- \(Z4\): \((x,y)=(0,\pm4)\).
- \(Z0\): \((x,y)=(0,0)\).

With the imported counts, these give support \(116\), \(U_0\)-energy \(56\), and \(U_3\)-energy \(128\), as stated. In particular, the \(U_3\) zero count is the sum of the full, \(D0\), and \(Z0\) counts, namely 23.

Under the imported same-column residue relation, criterion (C) and \(J=1\) give
\[
F_3\equiv4\pmod8.
\]
Adding the cap \(|F_3|\le12\) restricts the coefficients to \(\{\pm4,\pm12\}\); Parseval with energy \(128\) gives exactly eight magnitude-four positions.

The candidate constructs no such globally capped physical \(y\). The new \(U_0\) residual is correctly passed to the existing physical inverse rather than treated as completing it.

## 8. Counts, residual, and acceptance boundary

The graph and phase counts are imported from S3’s normalized two-fibre classification. The rank-four obstruction therefore removes
\[
384\cdot384=147456
\]
labeled normalized parameter pairs.

The remaining
\[
512\cdot384=196608
\]
pairs are only potential necessary-interface parameters. They are not a count of feasible even halves, original callers, or equivalence classes.

The first unpaid consumer remains one common physical rank-two choice satisfying simultaneously:

1. The three common bent conditions.
2. The actual local block types, counts, and \(H=0\).
3. The full \(U_0\) autocorrelation identity with the specifically tracked \(t\).
4. Physical \(y=-agx\) on \(S\), the remaining physical block constraints, \(J=1\), and every \(F_3\) cap.
5. Any remaining named rank and original-\(T\) requirements at their exact imported scopes.

Even such an even half would still need a sign assignment on its **actual 140-point complement**, with odd negative parity and all 256 complementary Walsh caps. Only then could the conditional \(u\pm v\) inverse supply the original Boolean caller.

Nothing reviewed here closes the surviving rank-two five-span branch, either six-span branch, the other named classes, or the full NL242 target.

## 9. Final verdict

**overall_correctness:** correct

**explanation:** The rank-four exclusion follows from the reconstructed affine-zero-flat and cubic-form arguments, and the rank-two direction, carried-balance coset, and all-shift autocorrelation equivalence have the stated normalization. The candidate correctly leaves the common physical \(U_3\), complementary half, and original-target obligations unpaid.

**confidence:** 0.98

**Scientific execution:** NOTRUN.  
**Severity totals:** 0 FATAL / 0 MAJOR / 0 MINOR.  
**Adoption status:** unchanged; parent disposition and the other required gates remain necessary.