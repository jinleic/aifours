# author-candidate-v1.md

## A complete actual-U obstruction for affine flat-fibre support

**Status:** AUTHOR / COMPLETE WRITTEN-PROOF CANDIDATE at the explicitly stated family scope. No parent adoption, independent review, executable verification, or novelty clearance is claimed.

### Result

I prove that the following two properties cannot coexist in an actual ternary \(u\):

1. The sixteen blocks supporting \(U_1=\pm3\) form an affine four-dimensional subspace of \(\mathbb F_2^6\).
2. The complete second-fibre transform has magnitude \(4\) at four frequencies and magnitude \(12\) at every other frequency:
   \[
   |\widehat U_2(r)|=
   \begin{cases}
   4,&r\in A_2,\quad |A_2|=4,\\
   12,&r\notin A_2.
   \end{cases}
   \tag{M}
   \]

In the normalization of the frozen packet, (M) is exactly
\[
|k_2|=2\text{ on }A_2,\qquad |k_2|=6\text{ elsewhere}.
\]

The obstruction treats **all 64 actual blocks**, including all 48 blocks outside the flat-fibre support. It allows every hole map, every actual sign assignment, every placement of \(A_2\), and every potential \(V\). It is not a restriction on the sixteen projected complement signs.

The conclusion is a **complete exclusion of this structural actual-caller family**, not a complete exclusion of the entire \(m=116\) residual.

There is one important source boundary: the supplied packet explicitly gives \(|A_2|=4\), but does not spell out the complete magnitude table of \(k_2\) away from \(A_2\). Accordingly, I keep (M) explicit rather than silently deriving it from an unspecified historical meaning of “rank2.” Section 7 supplies a self-contained parity-rank bridge that establishes (M) when rank two means the stated quadratic parity rank.

---

## 1. Inputs, chronology, and execution status

The assignment bindings supplied by the parent are:

- Manifest: `2f35fba31f92611581d6251f1218b0d11eb64c0318a70d594eee9f40c86351ef`.
- Freeze receipt: `540c7c87895b757fcc9ebbb943f9732a2d6b88c741176f6c5d1ae270b710da3e`.
- Literal packet, as recorded in that receipt: `b7842a2796146c999a390ed4f9226dd8efd9120d6be4c47946bd0298d40c530c`.

These are **supplied bindings**, not author-executed hashes.

The read chronology was:

1. Required memory summary.
2. Research-round and written-math protocol skills.
3. Complete manifest and freeze receipt.
4. All seven listed permission/status/quarantine controls, before the scientific packet.
5. Complete ordered literal packet, raw ranges 1–200, 201–400, and 401–596, including the ending of S5.
6. Written mathematical development.
7. Novelty-audit skill; no literature search or priority claim followed.
8. Targeted rereads of the already permitted S5 caller disposition, S4 support disposition, and S2 actual-object normalization.

No linked historical scientific body outside the frozen inputs was opened. No held scientific payload or its consumers was used. No sibling current outcome was consulted.

**No scientific executable, finite enumeration, external-model CLI, public-source search, or repository write was performed.** All results below are written algebra. There is consequently no executed code, observed stdout, or machine certificate to report.

The manifest records a parent/native observation of `2026-10-30T10:18:22-0700 PDT` before its creation. That is not this author’s observed research start or completion time. No independent author-native clock observation or timestamped cadence certificate is claimed.

This is the complete body for parent materialization.

---

## 2. Actual-object definitions and exact excluded family

Use the packet’s common coordinates:
\[
R=\mathbb F_2^6,\qquad Q=\mathbb F_2^2.
\]

Let
\[
u(c,w)\in\{0,\pm1\},\qquad c\in R^*,\ w\in Q^*,
\]
be an **actual** ternary function. Define
\[
U_s(c)=\sum_{w\in Q^*}u(c,w)\chi_s(w).
\]

The adopted flat-fibre facts are
\[
U_1(c)\in\{0,\pm3\},\qquad
S=\{c:U_1(c)\ne0\},\qquad |S|=16.
\tag{1}
\]

For \(c\in S\), the packet’s actual block argument gives
\[
U_2(c)\in\{\pm1\}.
\tag{2}
\]

For \(c\notin S\), \(U_1(c)=0\). Reduction modulo two shows that the support size of \(u(c,\cdot)\) is even. Therefore
\[
U_2(c)\in\{0,\pm2,\pm4\}.
\tag{3}
\]

These are statements about actual four-point blocks, not prescribed inverse values of a relaxed spectral array.

### Definition of the excluded actual family

Let \(\mathcal C\) consist of actual callers in the assigned residual that additionally satisfy:

- **Affine-support condition:** \(S\) is an affine four-flat in \(R^*\).
- **Complete second-fibre condition:** (M) holds at all 64 frequencies.

Every original balance, support, parity, cap, rank, zero-count, and complementarity condition remains imposed in the definition of \(\mathcal C\). The proof will use only a necessary subset of those conditions.

### Theorem

\[
\boxed{\mathcal C=\varnothing.}
\]

In fact, the theorem is stronger than this application: no actual ternary \(u\) satisfying (1)–(3), affine \(S\), and (M) exists, regardless of its total support size or whether a complement has been proposed.

---

## 3. A small exact Fourier classification

### Lemma 1 — Boolean four-variable functions with at most four nonzero ternary Fourier residues

Let \(f:\mathbb F_2^4\to\{\pm1\}\), and write its unnormalized transform as \(B=\widehat f\). Suppose
\[
\#\{y:3\nmid B(y)\}\le4.
\tag{4}
\]

Then precisely one of the following holds:

1. \(f\) is an affine character, with one transform coefficient of magnitude \(16\); or
2. \(B\) is supported on an affine two-flat \(T\), has magnitude \(8\) at its four points, and the product of its four signs is \(-1\).

#### Proof

Work modulo three. Fourier inversion on 16 points has factor \(16^{-1}=1\) in \(\mathbb F_3\). Thus
\[
f(h)\equiv\sum_{y\in T}b_y\chi_y(h)\pmod3,
\]
where \(T=\{y:3\nmid B(y)\}\) and \(b_y\in\{\pm1\}\).

The right side must be nonzero for every \(h\), because \(f(h)=\pm1\).

- **No coefficients:** impossible by invertibility.
- **One coefficient:** the inverse is a signed character. Its actual transform has one coefficient \(\pm16\).
- **Two coefficients:** the two signed characters cancel somewhere.
- **Three coefficients:** after removing a common character and sign, the expression is
  \[
  1+\epsilon\chi_a+\eta\chi_b
  \]
  with independent \(a,b\). Some \(h\) makes all three summands \(+1\), producing zero modulo three.
- **Four coefficients with affine span of dimension three:** their three relative characters attain every sign triple. Some \(h\) makes two of the four summands positive and two negative, producing zero.
- **Four coefficients on an affine two-flat:** after removing a common character, the expression has coefficient signs \(b_0,b_1,b_2,b_3\) on
  \[
  \{0,a,b,a+b\}.
  \]
  If their product is \(+1\), its real values include zero. If their product is \(-1\), its real values are always \(\pm2\).

Only the last case survives. Let
\[
P(h)=\sum_{y\in T}b_y\chi_y(h)\in\{\pm2\}.
\]
The unique value \(f(h)\in\{\pm1\}\) congruent to \(P(h)\) modulo three is
\[
f(h)=-P(h)/2.
\]
Consequently
\[
B(y)=-8b_y\quad(y\in T),\qquad B(y)=0\quad(y\notin T).
\]
The product of the four signs of \(B\) is \(\prod b_y=-1\). ∎

This lemma is proved here; no classification table or executable enumeration is imported.

---

## 4. Complete obstruction, including the other 48 blocks

Assume for contradiction that an actual \(u\) satisfies the theorem’s hypotheses.

Translate and choose linear coordinates in \(R^*\) so that
\[
c=(h,d)\in H\times D,\qquad
H=\mathbb F_2^4,\quad D=\mathbb F_2^2,
\]
and
\[
S=H\times\{0\}.
\]

These changes preserve the block-value restrictions and all transform magnitudes.

For brevity put
\[
g(h,d)=U_2(h,d).
\]
By actual block realizability,
\[
g(h,0)\in\{\pm1\},\qquad
g(h,d)\in\{0,\pm2,\pm4\}\quad(d\ne0).
\tag{5}
\]

Index the full transform by \((y,z)\in H^*\times D^*\). Under (M), write
\[
\widehat g(y,z)=4\kappa(y,z),
\]
where
\[
\kappa(y,z)\in\{\pm1\}\text{ on }A_2,\qquad
\kappa(y,z)\in\{\pm3\}\text{ off }A_2.
\tag{6}
\]

Define the four partial transforms
\[
B_d(y)=\sum_{h\in H}g(h,d)(-1)^{y\cdot h}.
\]

Inverting in the two-dimensional \(D\)-coordinate gives the exact normalization
\[
B_d(y)
=\frac14\sum_z\widehat g(y,z)(-1)^{z\cdot d}
=\sum_z\kappa(y,z)(-1)^{z\cdot d}.
\tag{7}
\]

### 4.1 The affine support forces a four-point partial spectrum

Set
\[
f(h)=g(h,0)\in\{\pm1\},\qquad B=B_0=\widehat f.
\]

If the frequency fibre \(\{(y,z):z\in D^*\}\) contains no point of \(A_2\), then all four \(\kappa(y,z)\) are divisible by three. Equation (7) therefore implies \(3\mid B(y)\).

There are only four points of \(A_2\), so
\[
\#\{y:3\nmid B(y)\}\le4.
\]

Also, directly from (7),
\[
|B(y)|\le12.
\]
This rules out the affine-character alternative of Lemma 1. Hence there is an affine two-flat \(T\subset H^*\) such that
\[
B(y)=
\begin{cases}
8\beta(y),&y\in T,\\
0,&y\notin T,
\end{cases}
\qquad
\prod_{y\in T}\beta(y)=-1.
\tag{8}
\]

Every \(y\in T\) must have a point of \(A_2\) above it. Since \(|T|=|A_2|=4\), there is exactly one above each, and none elsewhere. Write it as
\[
(y,\alpha(y)),\qquad y\in T.
\tag{9}
\]

### 4.2 The four exceptional frequency fibres are completely determined

At \(y\in T\), the four values of \(\kappa\) comprise three values of magnitude three and one of magnitude one. Their sum is \(8\beta(y)\).

The only possibility is three copies of \(3\beta(y)\) and one copy of \(-\beta(y)\). Thus
\[
\kappa(y,z)
=\beta(y)\bigl(3-4\mathbf1_{\{z=\alpha(y)\}}\bigr).
\]

For every nonzero \(d\in D\), equation (7) becomes
\[
B_d(y)=-4\beta(y)(-1)^{\alpha(y)\cdot d},
\qquad y\in T.
\tag{10}
\]

Put
\[
x=\sum_{y\in T}\alpha(y)\in D^*,
\qquad
\gamma_d(y)=-\beta(y)(-1)^{\alpha(y)\cdot d}.
\]
Then
\[
\prod_{y\in T}\gamma_d(y)
=-(-1)^{x\cdot d}.
\tag{11}
\]

No assumption about the hole map \(w_0\) has been made.

### 4.3 The remaining twelve frequency fibres route into the three other actual cosets

For \(y\notin T\), there is no point of \(A_2\), so
\[
\kappa(y,z)=3\rho_y(z),\qquad \rho_y(z)\in\{\pm1\}.
\]
Equation (8) says
\[
\sum_z\rho_y(z)=0.
\]

Every balanced sign function on four points is a signed nontrivial character. Hence there are a unique nonzero \(d_y\in D\) and a sign \(\eta_y\) such that
\[
\rho_y(z)=\eta_y(-1)^{z\cdot d_y}.
\]

Consequently,
\[
B_d(y)=
\begin{cases}
12\eta_y,&d=d_y,\\
0,&d\ne d_y.
\end{cases}
\tag{12}
\]

Let
\[
n_d=\#\{y\notin T:d_y=d\}.
\]
All twelve remaining \(y\)-frequencies are accounted for exactly once:
\[
\boxed{\sum_{d\ne0}n_d=12.}
\tag{13}
\]

This is an explicit consuming-side partition, not an assumption that the remaining blocks can be filled independently.

### 4.4 Ternary inversion determines the support sizes of all three other actual cosets

For \(d\ne0\), reduce the 16-point inverse transform modulo three. The coefficients in (12) disappear, whereas (10) reduces to \(\gamma_d(y)\). Since \(16=1\pmod3\),
\[
g(h,d)\equiv
\sum_{y\in T}\gamma_d(y)(-1)^{y\cdot h}\pmod3.
\tag{14}
\]

For four characters on an affine two-flat:

- coefficient-sign product \(-1\) gives values \(\pm2\) at all sixteen points;
- coefficient-sign product \(+1\) gives zero at twelve points and values \(\pm4\) at four points.

By (5), \(g(h,d)\) is zero **if and only if** its residue modulo three is zero. Therefore, writing
\[
m_d=\#\{h:g(h,d)\ne0\},
\]
equations (11)–(14) prove
\[
m_d=
\begin{cases}
16,&(-1)^{x\cdot d}=+1,\\
4,&(-1)^{x\cdot d}=-1.
\end{cases}
\tag{15}
\]

Thus the three other actual cosets have support sizes:

- \((16,16,16)\) if \(x=0\);
- \((16,4,4)\), in some order, if \(x\ne0\).

All 48 blocks outside \(S\) are included.

### 4.5 Integer Parseval makes both cases impossible

On a fixed nonzero coset, equations (10) and (12) give
\[
\sum_h g(h,d)^2
=\frac1{16}\left(4\cdot4^2+n_d12^2\right)
=4+9n_d.
\tag{16}
\]

Because all \(g(h,d)\) are even, the left side is divisible by four. Therefore
\[
n_d\equiv0\pmod4.
\tag{17}
\]

Every nonzero value in that coset has square at least four, so
\[
4+9n_d\ge4m_d.
\tag{18}
\]

If \(m_d=16\), equations (17)–(18) force \(n_d\ge8\).  
If \(m_d=4\), they force \(n_d\ge4\).

Consequently:

- If \(x=0\),
  \[
  \sum_{d\ne0}n_d\ge8+8+8=24.
  \]
- If \(x\ne0\),
  \[
  \sum_{d\ne0}n_d\ge8+4+4=16.
  \]

Both contradict the exact total \(12\) in (13).

This proves the theorem. ∎

---

## 5. An additional actual-block accounting check

The frozen actual caller supplies
\[
X(A_2)\ne0.
\]
For four points over \(\mathbb F_2\), this means their affine span has dimension three.

This permits another accounting of the contradiction at the level of **full four-point \(u\)-blocks**.

Let
\[
P(c)=\sum_{r\in A_2}\epsilon_r\chi_r(c),
\qquad
\epsilon_r=\widehat U_2(r)/4\in\{\pm1\}.
\]
Full Fourier inversion modulo three gives
\[
U_2(c)\equiv P(c)\pmod3.
\tag{19}
\]

Four characters with affinely independent relative directions have sum zero at exactly \(24\) of the \(64\) points. Their other values are \(\pm2,\pm4\), never divisible by three.

The actual allowed values of \(U_2\), namely
\[
0,\ \pm1,\ \pm2,\ \pm4,
\]
are divisible by three only at zero. Thus (19) implies
\[
|\operatorname{supp}U_2|=40.
\]

Full Parseval under (M) gives
\[
\sum_c U_2(c)^2
=\frac{4\cdot4^2+60\cdot12^2}{64}
=136.
\]

The sixteen points of \(S\) contribute \(16\). Hence outside \(S\), there are \(24\) nonzero \(U_2\)-values contributing \(120\). If \(F_2\) counts those of magnitude four, then
\[
120=4(24-F_2)+16F_2,
\]
so
\[
\boxed{F_2=2.}
\tag{20}
\]

A value \(U_2=\pm4\) means the actual \(u\)-block has all four entries nonzero, aligned with \(\pm\chi_2\).

Under affine \(S\), the proof above yields two other cosets with \(m_d=4\). For either such coset, let \(F_d\) count its magnitude-four values. Equations (16)–(17) give
\[
4+9n_d=16+12F_d,\qquad n_d=4\ell,
\]
and therefore
\[
F_d=3\ell-1.
\]
Since \(0\le F_d\le4\), necessarily
\[
F_d=2.
\]

Those two cosets alone require four full \(\chi_2\)-blocks, contradicting the exact global count two in (20).

This is a second written accounting of the obstruction, not a disjoint external review.

---

## 6. Exact structural meaning for the actual plateaued phase

The packet supplies
\[
\widehat\sigma=16a,\qquad
\operatorname{supp}a=S,\qquad |S|=16.
\]

A linear structure of the Boolean sign function \(\sigma\) is a vector \(t\) such that
\[
\sigma(r+t)=\varepsilon_t\sigma(r)
\quad\text{for every }r,
\qquad \varepsilon_t\in\{\pm1\}.
\]

Fourier transformation shows that this is equivalent to
\[
\chi_t(c)=\varepsilon_t
\quad\text{for every }c\in S.
\tag{21}
\]

It follows that:

- If \(S\) is an affine four-flat, its direction annihilator gives two independent linear structures.
- If \(\sigma\) has two independent linear structures, (21) confines \(S\) to an affine subspace of dimension at most four. Its cardinality sixteen forces equality.

Therefore, under (M),
\[
\boxed{\text{the actual }\sigma\text{ cannot have two independent linear structures}.}
\]

Equivalently,
\[
\boxed{\dim\operatorname{aff}(S)\ge5.}
\]

This closes a natural structural class of actual flat-fibre phases. It does **not** assume an affine hole map, and it is not a near-template distance restriction on the complement.

---

## 7. Explicit parity-rank bridge to the usual magnitude pattern

The following lemma identifies the exact additional interpretation needed to make (M) automatic. It is proved here rather than imported from an unstated convention.

### Lemma 2 — parity rank two at support size 116

Let \(u:\mathbb F_2^8\to\{0,\pm1\}\) satisfy
\[
|\operatorname{supp}u|=116,\qquad
\widehat u\in4\mathbb Z,\qquad
|\widehat u|\le12.
\]
Put
\[
\kappa=\widehat u/4.
\]

Then \(q=\kappa\bmod2\) is a Boolean polynomial of degree at most two. If its quadratic polar form has rank two, \(q\) has weight \(192\), and its zero set is one affine six-flat.

#### Proof

Expand the character product:
\[
\widehat u(r)
=\sum_yu(y)\prod_{i=1}^{8}(1-2r_i y_i).
\]

Dividing by four and reducing modulo two kills all terms of degree at least three. The constant term is integral because \(\widehat u(0)\in4\mathbb Z\). The linear terms are integral because divisibility of both \(\widehat u(0)\) and \(\widehat u(e_i)\) by four forces \(\sum_yu(y)y_i\) to be even. Thus \(q\) has degree at most two.

A rank-two quadratic Boolean polynomial on eight variables has weight \(64\), \(128\), or \(192\): a nonzero linear part on its six-dimensional radical makes it balanced; otherwise it is a nondegenerate two-variable quadratic, extended over the radical.

Let \(w=\operatorname{wt}(q)\). Since \(\kappa\in\{0,\pm1,\pm2,\pm3\}\), its square is at most nine at odd positions and at most four at even positions. Parseval gives
\[
\sum_r\kappa(r)^2
=\frac{256\cdot116}{16}
=1856,
\]
hence
\[
1856\le9w+4(256-w)=1024+5w.
\]
Therefore \(w\ge167\), leaving only \(w=192\).

A rank-two quadratic of weight \(192\) is zero on exactly one of its four radical cosets, an affine six-flat. ∎

If the caller is balanced, \(\widehat u(0)=0\), so this zero coset contains zero and is linear.

In quotient coordinates where fibre \(0\) is this zero coset, the other three fibres have \(\kappa\) odd. Thus, on fibre \(2\),
\[
k_2=2\kappa_2\in\{\pm2,\pm6\}.
\]
Together with the supplied \(|A_2|=4\), this proves (M).

### Source boundary

The bridge is fully proved under its explicit definition of parity rank. However, S1–S5 do not explicitly define the historical word “rank2” as this polar rank or explicitly identify the common \(R,Q\) fibres with these parity cosets.

Accordingly:

- **Unconditional author result at the supplied documentary scope:** the exact actual family \(\mathcal C\) is empty.
- **Additional application, if that identification is established from the original caller definitions:** every actual member of the named residual has non-affine \(S\), equivalently at most one independent linear structure of \(\sigma\).

The latter identification is an exact remaining import gate, not a presumed fact.

---

## 8. Coverage and relation to the original target

| Original obligation | Treatment |
|---|---|
| Actual ternary \(u\) | Essential: supplies the pointwise block-value restrictions. |
| Sixteen \(U_1=\pm3\) blocks | Used exactly; not manufactured from a projection code. |
| Other 48 blocks | All included in the three nonzero \(D\)-cosets and their exact Fourier/Parseval equations. |
| Arbitrary holes and signs | Fully covered; no affinity or independence assumption on \(w_0\). |
| Complete even-fibre spectrum | (M) is imposed at all 64 frequencies, not selected positions. |
| Actual 116/140 support counts | Retained in the caller family. The core obstruction is stronger and does not need them; support 116 is used in Lemma 2. |
| Eight-zero and remaining fibre pattern | Retained, not claimed to follow from the proof. Not needed for the core contradiction. |
| Balance | Retained. Not needed by the core theorem; identifies the parity zero coset as linear in the bridge. |
| Full real complementarity | Retained. No complement can rescue an impossible actual \(U\). |
| Odd global Walsh cap and \(V\)-parity | Retained; unnecessary for this U-side exclusion. |
| All 512 Boolean coefficients | No witness is claimed, so no coefficient list is fabricated. |
| Complete residual exclusion | **Not proved.** The non-affine-support residual remains. |

The theorem does not claim to fill the 48 blocks or construct \(U\) from necessary shadows. It proves that, for the specified family, **no filling by actual blocks exists**.

This is separate from the prior two-coset exclusion: that theorem concerns concentration of \(A_3\) in cosets generated by \(A_2\). The present theorem concerns the affine geometry of the **primal flat-fibre support \(S\)** and uses the actual values on every block. It neither assumes nor restricts the number of \(A_3\)-cosets.

---

## 9. Exact remaining gates

The following are unpaid:

1. **Original-caller interpretation:** establish from the complete original definitions whether the named rank-two/common-fibre structure is precisely the parity-rank structure of Lemma 2. Without that import, keep (M) explicit.
2. **Non-affine actual \(U\):** construction or exclusion when \(\dim\operatorname{aff}(S)=5\) or \(6\).
3. **Global complement:** for any surviving actual \(U\), solve or exclude the full real complementarity system with all global odd caps, balance, and parity.
4. **Whole original target:** other residuals, \(m=114\), other class-count pairs, rank two generally, and the full balanced nine-variable NL242 question.
5. **Verification:** a disjoint mathematical review and separate parent disposition. The two written accountings above are not independent-family, human, or formal-kernel verification.
6. **Novelty:** no public primary-source comparison was performed. The claimed contribution is a proved structural family obstruction relative to the supplied frontier, not a claim of first discovery or publishability.

### Final scientific disposition

**A complete actual-family exclusion has been obtained:** affine flat-fibre support is impossible under the exact four-small-coefficient \(4/12\) second-fibre pattern. The contradiction is global over all 64 blocks and can also be expressed as incompatible counts of actual full four-point \(u\)-blocks.

**No actual \(U/V\) witness and no complete \(m=116\) residual exclusion is claimed.**