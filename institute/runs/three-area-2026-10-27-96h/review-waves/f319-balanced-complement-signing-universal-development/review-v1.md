# UNREVIEWED AUTHOR CANDIDATE — Full complement-autocorrelation compatibility

**Publication qualification.** The write to the wave’s reviewer-prefixed pre-body ACK file was refused by the tool; no filesystem bypass was attempted. The ACK and substantive checkpoints are retained in `local://f319-reviewer-prebody-ack-v1.md`, `local://f319-reviewer-checkpoint-v1.md`, and `local://f319-reviewer-checkpoint-v2.md`. The complete intended `review-v1.md` text follows for parent materialization.

## 1. Scope, read coverage, and correction dependencies

The administrative PRE-BODY ACK was recorded after the actual clock observation **2026-10-30T14:42:55Z**, before mathematical packet access. Before that ACK, I read the entire manifest, freeze receipt through its ending, and all six status-only controls. Observed metadata hashes matched:

- Manifest: `a88702fc31819c89d4db1063b010a577ea9e4c335c56279eecf94dc2e9874bc1`
- Freeze receipt: `b6317ba34a16db2ad46e36b9445c8d37c123211ec5661879671c7fb8989499f2`
- Literal packet: `e91e1de62945b36caa7f327ef95e2518d64b4a2610f3be75fdf917c34af73d1c`

After the ACK, I read all **61 LF** of the ordered literal packet raw, in windows **1–20, 21–40, 41–60, 61–61**, including its ending. No truncation appeared. No excluded link, held packet, or prior returned review body was opened.

This result applies to **every actual real Boolean candidate** in the adopted rank-two, eight-zero, \(m=116\), \((G_3,H)=(1,0)\), \((U)/(V)\) scope. It does not assume that any such candidate exists.

The exact scoped imports are:

1. **S4 LF 19–35:** the real complementary ternary split, the identification of \(K\) with the full dual of \(V\), the two Fourier normalizations, and both caps.
2. **S1 LF 7–12, controlling the older wording:** global odd-half congruences do not require the unread odd-half import; \((N1),(N2)\) are already redundant; the D1 sign-product correction remains mandatory.
3. **S2 LF 7–8:** the adopted support-XOR theorem has its stated perfect-array scope, and neither redundant coupling condition supplies a new restriction here.
4. **S3 LF 3–7:** the cross-fibre conditions remain necessary conditions on an actual original candidate, **not** a sufficient construction of a real \(u\).

In particular, “cap decoupling” is not interpreted as permission to choose two arbitrary Fourier arrays independently. Their inverse transforms must still be real complementary ternary functions. The theorem below exposes that compatibility in full Fourier coordinates. No D1 rule or unread import is used in its proof.

## 2. Notation

Write \(G=V\), so \(|G|=N=256\), and let \(K=G^*\). For every \(r\in K\), let \(\chi_r\) denote its real character.

For an actual \(u\)-side realizer, define
\[
k(r)=\frac{\widehat u(r)}2.
\]
Thus \(u:G\to\{0,\pm1\}\), \(|\operatorname{supp}u|=116\), and all the adopted \(U\)-side requirements remain imposed.

Set
\[
e(y)=1-u(y)^2,\qquad \Omega=\operatorname{supp}e,
\]
so \(e=1_\Omega\) and \(|\Omega|=140\).

For any **real** proposed normalized complement spectrum \(z:K\to\mathbb R\), define its real inverse transform by
\[
v_z(y)=\frac{2}{N}\sum_{r\in K}z(r)\chi_r(y).
\]
Consequently \(\widehat{v_z}=2z\). For an actual capped complement, the corrected congruences give
\[
z(r)\in\{\pm1,\pm3,\pm5,\pm7\}
\qquad\text{for every }r\in K.
\]

Convolution below is on the entire dual group:
\[
(a*b)(\xi)=\sum_{r\in K}a(r)b(r+\xi),
\qquad Q_a=a*a.
\]
Because the group has exponent two, \(Q_a\) is also the full translation autocorrelation of the real array \(a\).

## 3. Main result: the full phase-sensitive compatibility relation

### Theorem

Every admissible actual Boolean candidate satisfies
\[
\boxed{\quad
Q_k(\xi)+Q_z(\xi)=2^{14}\delta_0(\xi)
\qquad\text{for every }\xi\in K.
\quad} \tag{AC}
\]

More strongly, at any fixed actual real ternary \(u\), **(AC) is necessary and sufficient** for the real inverse \(v_z\) to sign exactly \(\Omega\):
\[
v_z(y)^2=e(y)\qquad\text{for every }y\in G.
\]

This is a fixed-\(u\) real-lifting equivalence—not an existence theorem for \(u\), \(z\), or the original Boolean target.

The same complement autocorrelation also satisfies the all-shift quartic identity
\[
\boxed{\quad
Q_z*Q_z=2^{14}Q_z.
\quad} \tag{QI}
\]
Thus the full autocorrelation of \(z\), not merely its scalar second moment, is a scaled convolution idempotent.

### Proof of (AC), including sufficiency

With the stated normalization, Fourier multiplication gives
\[
\widehat{ab}(\xi)
=\frac1N(\widehat a*\widehat b)(\xi).
\]
Indeed, expanding the convolution and summing the characters over the full dual group eliminates precisely the terms with unequal primal arguments.

Therefore
\[
\widehat{u^2}=\frac4NQ_k,\qquad
\widehat{v_z^2}=\frac4NQ_z.
\]
For an actual complementary pair,
\[
u^2+v_z^2=1.
\]
Taking its full Fourier transform yields
\[
\frac4N(Q_k+Q_z)=N\delta_0,
\]
which is (AC), since \(N^2/4=2^{14}\).

Conversely, suppose \(u\) is an actual real ternary \(u\)-side object and the real array \(z\) satisfies (AC). Fourier inversion gives
\[
u^2+v_z^2=1
\]
pointwise. Since \(u^2\) is an indicator, this says exactly
\[
v_z^2=1-u^2=e.
\]
Reality then implies that \(v_z\) is ternary and signs precisely \(\Omega\). No sign assignment has been supplied or tested in this argument.

For a quantitative form of the same equivalence, define the complete residual
\[
E_{k,z}(\xi)=Q_k(\xi)+Q_z(\xi)-2^{14}\delta_0(\xi).
\]
The preceding calculation gives
\[
E_{k,z}=\frac N4\,\widehat{\,u^2+v_z^2-1\,}.
\]
Hence Parseval yields the exact nonnegative defect identity
\[
\boxed{\quad
\sum_{\xi\in K}E_{k,z}(\xi)^2
=
2^{20}\sum_{y\in G}
\bigl(u(y)^2+v_z(y)^2-1\bigr)^2.
\quad} \tag{RD}
\]
Thus vanishing of the **entire** Fourier residual is exactly real complement realizability.

### Proof of the quartic identity

For an actual complement, \(v_z^2=e\), so
\[
Q_z=\frac N4\widehat e.
\]
Because \(e\) is an indicator, \(e^2=e\). Applying the Fourier product identity once more,
\[
Q_z*Q_z
=\left(\frac N4\right)^2
(\widehat e*\widehat e)
=\left(\frac N4\right)^2N\widehat e
=\frac{N^2}{4}Q_z
=2^{14}Q_z.
\]
This proves (QI) simultaneously at every dual shift.

The mixed identity
\[
k*z=0
\]
also follows, since the established real complement condition implies \(uv_z=0\). It is therefore **not** advertised as another independent gate.

## 4. Ordinary-autocorrelation shadow: an integer compatibility condition

The same theorem has a necessary consequence depending on the **labelled squared spectrum**, rather than its scalar magnitude counts.

For every primal shift \(t\in G\), define
\[
M(t)=\sum_{y\in G}e(y)e(y+t).
\]
Using \(\sum_yu(y)^2=116\),
\[
M(t)=24+\sum_{y\in G}u(y)^2u(y+t)^2. \tag{1}
\]
The ordinary autocorrelation of the proposed complement is
\[
C_z(t)=\sum_yv_z(y)v_z(y+t)
=\frac1{64}\sum_{r\in K}z(r)^2\chi_r(t). \tag{2}
\]

For every actual candidate, put
\[
D(t)=\frac{M(t)-C_z(t)}4.
\]
Then the following holds **for all shifts**, with no selected-shift diagnostic:
\[
\boxed{\quad
D(t)\in\mathbb Z_{\ge0},
\qquad
2D(t)\le M(t).
\quad} \tag{IC}
\]

Equivalently, every actual candidate obeys
\[
\frac1{64}\sum_rz(r)^2\chi_r(t)
\equiv
24+\sum_yu(y)^2u(y+t)^2
\pmod4,
\]
together with
\[
\left|\frac1{64}\sum_rz(r)^2\chi_r(t)\right|
\le
24+\sum_yu(y)^2u(y+t)^2.
\]

### Proof

For an arbitrary actual complement, define its positive and negative indicators universally by
\[
P=\frac{e+v_z}{2},\qquad
N_-=\frac{e-v_z}{2}.
\]
They are disjoint \(\{0,1\}\)-valued functions; no particular signing is chosen.

Expanding \(M-C_z\) gives
\[
M(t)-C_z(t)
=
2\sum_y\bigl(P(y)N_-(y+t)+N_-(y)P(y+t)\bigr).
\]
Translation by \(t\), together with \(t+t=0\), identifies the two sums. Thus
\[
D(t)=\sum_yP(y)N_-(y+t).
\]
This proves nonnegative integrality. The two oppositely signed contributions occupy \(2D(t)\) of the \(M(t)\) occupied ordered pairs, proving \(2D(t)\le M(t)\).

This proof includes all shifts uniformly; it requires no exceptional diagnostic case.

Consequently, a proposed squared-spectrum placement must satisfy an entire integer autocorrelation system tied to the **actual \(u\)-determined support**. Passing (IC) is only necessary: it is not asserted to replace the phase-sensitive equation (AC).

## 5. Why this is not the existing second-moment ledger

The diagonal part of (AC) recovers the adopted energy normalization. **That part is not claimed as new progress.** The additional content is the full collection of off-diagonal signed correlations, plus their prescribed coupling to \(Q_k\).

To see precisely what magnitude-only bookkeeping omits, take arbitrary positive magnitudes \(a(r)\) and formal signs \(\varepsilon_r\), writing \(z(r)=a(r)\varepsilon_r\). For every nonzero shift \(\xi\),
\[
Q_z(\xi)
=
2\sum_{\{r,r+\xi\}}
a(r)a(r+\xi)\varepsilon_r\varepsilon_{r+\xi},
\]
where the sum is over the translation pairs.

This has distinct, nonzero pair-monomial coefficients in the free sign algebra. It is not a constant expression determined by the magnitude counts. In contrast, the scalar ledger is unchanged by these formal phase signs.

This is an all-variable algebraic statement: **no sign assignment or character has been instantiated, enumerated, or tested**. It shows why scalar spectral bookkeeping cannot certify the required fixed-support complement compatibility. It does not exclude any actual Boolean candidate.

Likewise, (IC) retains the positions of \(z(r)^2\) through every character sum. Merely knowing the numbers of coefficients of each magnitude does not supply those labelled autocorrelations.

The relations do **not** claim a new improvement of the cap \(14\). They expose the real Boolean compatibility that remains when one attempts to use capped spectral relaxations.

## 6. Actual objects, relaxation boundary, and unpaid step

For an **actual** \(U/V\) candidate:

- \(u\) is a real ternary realization of the full adopted \(U\)-side system.
- Its \(e=1-u^2\), hence every \(M(t)\), is fixed.
- The actual complement spectrum satisfies (AC), (QI), and (IC).

For an **arbitrary spectral relaxation**:

- Integral \(k\), odd capped \(z\), scalar energies, and magnitude counts do not by themselves establish complementary ternary inverse transforms.
- The conditions on \(X_2,X_3,\Pi_2,\Pi_3\) and shifted cross-fibre data are retained at their adopted necessary scope; they are not substituted for a real \(u\)-realizer.
- At fixed actual \(u\), imposing the full (AC) does establish complement reality. Imposing only selected moments or the shadow (IC) has not been shown sufficient.

The exact remaining task is therefore:

> Produce, or rule out, an actual real \(U\)-side realizer \(u\) and an odd capped array \(z(r)\in\{\pm1,\pm3,\pm5,\pm7\}\) satisfying the complete coupled autocorrelation equation (AC).

No such realizer, signing, or exclusion is supplied here. The original balanced NL242 target remains open. This result neither reopens the quarantined selected-assignment gate nor derives a universal impossibility from failure of a route.

## 7. Claim status and assurance

| Claim | Status |
|---|---|
| Full coupled autocorrelation equation (AC) | **SUPPORTED by the written author derivation; UNREVIEWED** |
| Fixed-\(u\) real-lifting equivalence and residual identity (RD) | **SUPPORTED by the written author derivation; UNREVIEWED** |
| Quartic autocorrelation idempotence (QI) | **SUPPORTED by the written author derivation; UNREVIEWED** |
| All-shift integer autocorrelation condition (IC) | **SUPPORTED by the written author derivation; UNREVIEWED** |
| Existence or exclusion at the actual residual | **INCONCLUSIVE / NOT PROVED** |
| Original-target completion | **NOT PROVED** |

No new FATAL/MAJOR/MINOR finding about the frozen sources is asserted; their explicitly supplied corrections remain binding.

This is **one consolidated Boolean-complement compatibility result**, with exact Fourier and necessary ordinary-autocorrelation forms. It is not independent review, acceptance, a novelty certification, or original-target completion. No scientific code, CAS, solver, enumeration, replay, selected mathematical diagnostic, external-model CLI, live service change, or new execution budget was used.