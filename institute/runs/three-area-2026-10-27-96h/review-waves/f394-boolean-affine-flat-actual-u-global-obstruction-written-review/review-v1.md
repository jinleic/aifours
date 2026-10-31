# f394 WRITTEN review — actual-U affine-flat obstruction

**Scientific disposition:** SUPPORTED at the explicitly stated actual-object scope, with the complete second-fibre magnitude condition **(M) retained as a hypothesis**.  
**Mathematical findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Parent adoption:** Separate and not asserted by this return.

This is the complete review body for parent materialization. No working-tree file was written.

## 1. Binding, coverage, and execution boundary

Reviewed wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f394-boolean-affine-flat-actual-u-global-obstruction-written-review/`

Bindings supplied and observed by the **parent**, not independently hashed by this reviewer:

| Artifact | SHA-256 |
|---|---|
| Manifest | `d264dd53a7cfa5374f6e2cef635999d5206c0b9f75bcaa239531ed5915a64439` |
| Freeze receipt | `41ccd58bb841cc63cd1d4ea225d28c3b787f3c8070de3be92ea2768f5b33baf1` |
| Literal packet | `263b287e6c0b9d6da7e494ebc24cc17279787e5a0d9a2ffe7c2da7ff7afebc63` |
| S1: f384 complete candidate | `3c18f0df77421c82e9c75962381d50f9202df6c69ad53b8c57f071b8062e70e5` |
| S2: corrected actual-caller interface disposition | `b1834337754499fbfdc5f0c1165dff8a1f44bcc5ff0420c1264f4624082afede` |
| S3: adopted flat-fibre/cross-fibre disposition | `e09be9069bf8027bdb53e60a73c804f525b1c5c1953d517e417b5749b555ba09` |

The parent’s live metadata supply reports matching assigned hashes, bytes, and LF counts, with observation `2026-10-30T10:35:40-0700 PDT`. That is **parent-observed metadata**, not my native execution or research-start time.

### Read order

Before opening the mathematical packet, I read:

1. The complete manifest and freeze receipt.
2. The dispatch receipt.
3. All seven listed owner-direction/status/quarantine controls.
4. The parent’s live metadata supply.

I then sent a direct **PRE-BODY ACK** to Main, explicitly accepting the written-only boundary and disclosing the read-only materialization limitation.

After that ACK, I read the complete literal packet in ordered raw windows:

`1–20, 21–40, …, 661–680, 681–682`.

Every packet read contained at most 20 lines. The complete endings were read, including **S1 line 630**, **S2 line 19**, and **S3 line 31**, before mathematical derivation. The parent-reported S1 count is 629 LF characters; its manifested readable source range is 1–630.

S2 and S3 contain historical review/control summaries within the mandatory packet. Those summaries were read as part of the packet but were **not substituted for the reconstruction below**. No linked historical review body, control code, held payload, or current sibling outcome was opened.

### Execution

This was **WRITTEN ONLY**:

- No scientific code, interpreter, CAS, enumeration, solver, replay, or selected mathematical probe was run.
- No author code was read or used.
- No external-model CLI, public-source search, installation, deletion, commit, push, or publication occurred.
- No reviewer-native clock or hash execution is claimed.
- Historical quarantines and their consumers remain NONINPUT.

Runnable finite code is **not assigned to this WRITTEN slice**, and none is supplied or claimed executed.

## 2. Exact theorem reviewed

Let \(R^*\cong\mathbb F_2^6\), \(Q^*\cong\mathbb F_2^2\), and let

\[
u(c,w)\in\{0,\pm1\}.
\]

For distinct nonzero fibre labels \(1,2\in Q\), define

\[
U_s(c)=\sum_{w\in Q^*}u(c,w)\chi_s(w).
\]

Assume

\[
U_1(c)\in\{0,\pm3\},\qquad
S=\{c:U_1(c)\ne0\},\qquad |S|=16.
\]

The additional conditions are:

1. \(S\) is an affine four-flat.
2. For the **complete** 64-point transform of \(U_2\),

\[
|\widehat U_2(r)|=
\begin{cases}
4,&r\in A_2,\\
12,&r\notin A_2,
\end{cases}
\qquad |A_2|=4.
\tag{M}
\]

**Reviewed conclusion:** no such actual ternary \(u\) exists.

This is a theorem about actual four-point blocks, not merely necessary spectral shadows. It excludes the specified structural family even without imposing the remaining support, complementarity, or odd-half conditions. It does **not** exclude all non-affine actual callers or the entire \(m=116\) residual.

## 3. Actual-block restrictions — SUPPORTED

**Anchor:** S1 lines 75–101.

If \(U_1(c)=3\varepsilon\), multiply the four block entries by \(\varepsilon\chi_1\). Their sum is three. The support must have odd size and at least three entries; hence it has exactly three entries, and all three transformed nonzero entries equal \(+1\). There is exactly one hole \(w_0\), with

\[
u(c,w)=\varepsilon\chi_1(w)\quad(w\ne w_0).
\]

Because \(\chi_1\chi_2\) is a nontrivial character on four points,

\[
U_2(c)
=\varepsilon\sum_{w\ne w_0}\chi_{1+2}(w)
=-\varepsilon\chi_{1+2}(w_0)\in\{\pm1\}.
\]

Thus \(U_2=\pm1\) on all sixteen points of \(S\), without any affinity assumption on the hole map.

For \(c\notin S\), \(U_1(c)=0\). Modulo two, every signed character factor is one, so the block support is even. The same parity applies to \(U_2(c)\), while its absolute value is at most four. Therefore

\[
U_2(c)\in\{0,\pm2,\pm4\}\qquad(c\notin S).
\]

In particular, on these 48 blocks,

\[
U_2(c)\equiv0\pmod3
\quad\Longleftrightarrow\quad
U_2(c)=0.
\tag{A}
\]

This exact equivalence is what prevents a relaxed spectral construction from replacing actual realizability later.

## 4. Four-variable Boolean mod-three classification — SUPPORTED

**Anchor:** S1 lines 124–176.

Let \(f:H\to\{\pm1\}\), \(H=\mathbb F_2^4\), with unnormalized transform \(B\). Suppose

\[
E=\{y:3\nmid B(y)\},\qquad |E|\le4.
\]

Choose the nonzero residues \(b_y\in\{\pm1\}\). Since \(16\equiv1\pmod3\), Fourier inversion gives

\[
f(h)\equiv P(h):=\sum_{y\in E}b_y\chi_y(h)\pmod3.
\]

Consequently \(P\) must never vanish modulo three.

The complete support-cardinality analysis is:

- **Zero coefficients:** impossible, since the inverse would be identically zero modulo three.
- **One coefficient:** the unique \(\{\pm1\}\)-valued lift is the corresponding signed character. Its actual transform consists of one coefficient of magnitude 16.
- **Two coefficients:** the relative nontrivial character attains both signs, so the two terms cancel somewhere.
- **Three coefficients:** after removing a common signed character, the expression is \(1+\epsilon\chi_a+\eta\chi_b\). The distinct relative directions \(a,b\) are independent, so the last two signed terms can both equal \(+1\). The sum is then three, zero modulo three.
- **Four coefficients of affine dimension three:** the three relative characters attain every sign triple. They can give two positive and two negative summands, so the sum vanishes.
- **Four coefficients of affine dimension two:** write their support as
  \[
  y_0+\{0,a,b,a+b\}.
  \]
  If the product of coefficient signs is \(+1\), then, after extracting a signed character, the expression factors as
  \[
  (1+\epsilon\chi_a)(1+\eta\chi_b).
  \]
  It has zeros. If the product is \(-1\), the four evaluated summands always have product \(-1\), so their sum is always \(\pm2\).

There are no other affine dimensions for four distinct points.

In the surviving four-coefficient case, the actual Boolean lift is uniquely

\[
f(h)=-P(h)/2.
\]

This is an equality over the integers, not merely a residue assertion: \(P=2\) lifts to \(f=-1\), and \(P=-2\) lifts to \(f=1\). Taking the real transform gives

\[
B(y)=-8b_y\quad(y\in E),\qquad B(y)=0\quad(y\notin E).
\]

Thus the non-character alternative has affine two-flat support, magnitude eight at its four points, and sign product \(-1\).

The candidate’s classification is complete for **all** residue supports of size at most four. It does not assume in advance that an arbitrary Boolean function is a character.

## 5. Global obstruction over all 64 actual blocks — SUPPORTED

**Anchor:** S1 lines 180–410.

### 5.1 Affine gauge and exact normalization

An affine relabeling of the six-dimensional block coordinate permutes transform frequencies and multiplies transform coefficients by signs. It preserves all magnitudes, actual block values, and the number of exceptional frequencies. Hence we may write

\[
c=(h,d)\in H\times D,\qquad
H=\mathbb F_2^4,\quad D=\mathbb F_2^2,\qquad
S=H\times\{0\}.
\]

Set \(g(h,d)=U_2(h,d)\). Then

\[
g(h,0)\in\{\pm1\},\qquad
g(h,d)\in\{0,\pm2,\pm4\}\quad(d\ne0).
\]

Under (M),

\[
\widehat g(y,z)=4\kappa(y,z),
\]

where \(\kappa=\pm1\) at the four points of \(A_2\), and \(\kappa=\pm3\) everywhere else.

Define

\[
B_d(y)=\sum_hg(h,d)\chi_y(h).
\]

Inverting the four-point \(D\)-transform gives

\[
B_d(y)
=\frac14\sum_z\widehat g(y,z)\chi_z(d)
=\sum_z\kappa(y,z)\chi_z(d).
\tag{1}
\]

The factor four in (M) cancels the inverse factor \(1/4\); no normalization is missing.

### 5.2 Four exceptional frequency fibres and their orientation

For \(f(h)=g(h,0)\), write \(B=B_0=\widehat f\).

A \(y\)-fibre containing no exceptional point has \(3\mid B(y)\). Since there are only four exceptional points,

\[
|\{y:3\nmid B(y)\}|\le4.
\]

Also, (1) gives \(|B(y)|\le12\). The magnitude-16 character alternative of the classification is therefore impossible. Consequently, for an affine two-flat \(T\subset H^*\),

\[
B(y)=8\beta(y)\quad(y\in T),\qquad
B(y)=0\quad(y\notin T),\qquad
\prod_{y\in T}\beta(y)=-1.
\tag{2}
\]

Every \(y\in T\) must have an exceptional point above it. Four such fibres and four exceptional points force exactly one exceptional point in each:

\[
A_2=\{(y,\alpha(y)):y\in T\}.
\]

Within such a fibre, the sum of three numbers of magnitude three and one of magnitude one equals \(8\beta(y)\). This forces all three large values to be \(3\beta(y)\), and the small value to be \(-\beta(y)\). Hence

\[
\kappa(y,z)=\beta(y)\bigl(3-4\mathbf1_{z=\alpha(y)}\bigr).
\]

For every \(d\ne0\),

\[
B_d(y)=4\gamma_d(y),\qquad
\gamma_d(y)=-\beta(y)\chi_{\alpha(y)}(d).
\tag{3}
\]

Writing \(x=\sum_{y\in T}\alpha(y)\in D^*\), we obtain

\[
\prod_{y\in T}\gamma_d(y)
=-\chi_x(d).
\tag{4}
\]

These steps determine the exceptional-fibre orientation without restricting the original hole map.

### 5.3 Consuming-side routing of all twelve remaining fibres

For each \(y\notin T\),

\[
\kappa(y,z)=3\rho_y(z),\qquad \rho_y(z)\in\{\pm1\}.
\]

Equation (2) gives \(\sum_z\rho_y(z)=0\). A balanced sign function on four points has a two-point negative set, which is an affine line. Therefore it is a signed nontrivial character:

\[
\rho_y(z)=\eta_y\chi_z(d_y),
\qquad d_y\ne0.
\]

Character orthogonality in (1) now gives

\[
B_d(y)=
\begin{cases}
12\eta_y,&d=d_y,\\
0,&d\ne d_y.
\end{cases}
\tag{5}
\]

Thus each of the twelve remaining \(y\)-frequencies is routed to **exactly one** of the three nonzero \(d\)-cosets. If

\[
n_d=|\{y\notin T:d_y=d\}|,
\]

then

\[
\sum_{d\ne0}n_d=12.
\tag{6}
\]

There is no unmatched or discarded frequency branch: the four exceptional \(y\)-fibres account for sixteen full-transform coefficients, while the other twelve fibres account for forty-eight. Together they cover the four small and sixty large coefficients in (M).

### 5.4 Exact support sizes on all three external actual cosets

For fixed \(d\ne0\), invert the sixteen-point \(H\)-transform modulo three. Terms from (5) vanish; terms from (3) reduce to \(\gamma_d(y)\). Since \(16^{-1}=1\) modulo three,

\[
g(h,d)\equiv\sum_{y\in T}\gamma_d(y)\chi_y(h)\pmod3.
\tag{7}
\]

For four characters on an affine two-flat:

- Sign product \(-1\) gives \(\pm2\) at every \(h\).
- Sign product \(+1\) gives zero at twelve \(h\)-points and \(\pm4\) at four.

By the actual-value equivalence (A), residue support is exactly actual support. Therefore, with

\[
m_d=|\{h:g(h,d)\ne0\}|,
\]

equations (4) and (7) yield

\[
m_d=
\begin{cases}
16,&\chi_x(d)=+1,\\
4,&\chi_x(d)=-1.
\end{cases}
\tag{8}
\]

If \(x=0\), the three support sizes are \((16,16,16)\). If \(x\ne0\), a nontrivial character on \(D\) is positive at exactly one nonzero vector and negative at the other two, giving \((16,4,4)\).

This uses the actual restrictions at all **48 primal blocks outside \(S\)**, not just the sixteen signs on \(S\).

### 5.5 Integer Parseval contradiction

For each \(d\ne0\), (3), (5), and sixteen-point Parseval give

\[
\sum_hg(h,d)^2
=\frac{4\cdot4^2+n_d12^2}{16}
=4+9n_d.
\tag{9}
\]

All \(g(h,d)\) are even, so the left side is divisible by four. Thus

\[
n_d\equiv0\pmod4.
\]

Every nonzero actual value has square at least four, so

\[
4+9n_d\ge4m_d.
\]

It follows that

\[
m_d=16\Longrightarrow n_d\ge8,\qquad
m_d=4\Longrightarrow n_d\ge4.
\]

The two possibilities in (8) therefore require respectively

\[
\sum_{d\ne0}n_d\ge24
\quad\text{or}\quad
\sum_{d\ne0}n_d\ge16.
\]

Both contradict the exact routing total (6), which is twelve.

**Conclusion:** the core actual-U obstruction is proved. The factors \(4,8,12,16\), the exceptional orientation, the sign-product condition, and the full consuming-side partition are consistent.

## 6. Alternative full-block accounting — SUPPORTED with its additional hypothesis

**Anchor:** S1 lines 414–481.

This second argument additionally assumes

\[
X(A_2)=\sum_{r\in A_2}r\ne0.
\tag{10}
\]

It is not needed by the core proof.

For four distinct points in characteristic two, (10) is equivalent to affine dimension three. Let

\[
P(c)=\sum_{r\in A_2}\epsilon_r\chi_r(c),
\qquad \epsilon_r=\widehat U_2(r)/4.
\]

Full 64-point inversion under (M), reduced modulo three, gives

\[
U_2(c)\equiv P(c)\pmod3.
\]

After extracting one common signed character, the four-character sum has three independent relative characters. Their sign triples are uniformly distributed. Exactly three of the eight triples give total zero, so \(P\) has 24 zeros among the 64 points. Its other values are \(\pm2,\pm4\), nonzero modulo three.

The actual allowed \(U_2\)-values are \(0,\pm1,\pm2,\pm4\), whose only zero residue is zero. Hence

\[
|\operatorname{supp}U_2|=40.
\]

Global Parseval gives

\[
\sum_cU_2(c)^2
=\frac{4\cdot4^2+60\cdot12^2}{64}
=136.
\]

The sixteen points of \(S\) contribute sixteen, leaving 24 nonzero external values with energy 120. If \(F\) counts external values of magnitude four,

\[
120=4(24-F)+16F,
\]

so \(F=2\).

The link to the earlier coset analysis is exact:

\[
X(A_2)
=\left(\sum_{y\in T}y,\sum_{y\in T}\alpha(y)\right)
=(0,x),
\]

because the XOR of an affine two-flat is zero. Thus (10) forces \(x\ne0\), and there are two cosets with \(m_d=4\).

On either such coset, let \(F_d\) count magnitude-four values and write \(n_d=4\ell\). Equation (9) becomes

\[
4+36\ell=16+12F_d,
\qquad F_d=3\ell-1.
\]

The bounds \(0\le F_d\le4\) force \(F_d=2\). The two disjoint cosets would therefore require four magnitude-four blocks, contradicting the global count two.

Finally, \(|U_2|=4\) really does mean a full actual block: all four summands must attain the same extremal sign, so \(u(c,w)=\pm\chi_2(w)\) at all four positions.

This accounting is valid at its stated extra-XOR scope. It is another proof within the author candidate, not an independent external review.

## 7. Linear structures of the actual plateaued phase — SUPPORTED

**Anchor:** S1 lines 485–522.

Assume the actual phase relation

\[
\widehat\sigma=16a,\qquad \operatorname{supp}a=S,\qquad |S|=16.
\]

For a Boolean sign function \(\sigma\), translation by \(t\) multiplies its Fourier coefficient at \(c\) by \(\chi_t(c)\). Thus

\[
\sigma(r+t)=\varepsilon_t\sigma(r)\quad\text{for all }r
\]

is equivalent to

\[
\chi_t(c)=\varepsilon_t\quad\text{for all }c\in S.
\tag{11}
\]

If \(S\) is an affine four-flat, its direction annihilator has dimension two, giving two independent linear structures. Conversely, two independent structures impose two independent affine equations in (11), confining \(S\) to an affine four-flat. Since \(|S|=16\), it fills that flat.

Consequently, under (M), the core theorem implies

\[
\dim\operatorname{aff}(S)\ge5,
\]

equivalently, \(\sigma\) has at most one independent linear structure.

This is an exact equivalence for the **actual** Fourier support, not a conclusion about an arbitrary proposed shadow.

## 8. Parity-rank bridge — SUPPORTED as a separate conditional lemma

**Anchor:** S1 lines 526–588.

Let \(u:\mathbb F_2^8\to\{0,\pm1\}\) satisfy

\[
|\operatorname{supp}u|=116,\qquad
\widehat u\in4\mathbb Z,\qquad
|\widehat u|\le12.
\]

Put \(\kappa=\widehat u/4\) and \(q=\kappa\bmod2\).

### Degree bound

Expand

\[
\widehat u(r)=\sum_yu(y)\prod_i(1-2r_iy_i).
\]

After division by four:

- The constant coefficient is integral by \(\widehat u(0)\in4\mathbb Z\).
- The linear coefficients are integral because
  \[
  \widehat u(e_i)-\widehat u(0)=-2\sum_yu(y)y_i
  \]
  is divisible by four.
- Quadratic coefficients are integral.
- Every coefficient of degree at least three is even.

Therefore \(q\) has Boolean degree at most two.

### Rank-two weight and zero coset

If the quadratic polar form of \(q\) has rank two, its radical has dimension six. A nonzero linear restriction on the radical makes \(q\) balanced, of weight 128. Otherwise \(q\) descends to a nondegenerate two-variable quadratic on the quotient, with weight 64 or 192. Thus its possible weights are

\[
64,\ 128,\ 192.
\]

Parseval gives

\[
\sum_r\kappa(r)^2=16\cdot116=1856.
\]

At odd positions \(\kappa^2\le9\); at even positions \(\kappa^2\le4\). If \(w=\operatorname{wt}(q)\),

\[
1856\le9w+4(256-w)=1024+5w.
\]

Hence \(w\ge167\), forcing \(w=192\). The zero set is exactly one affine coset of the six-dimensional radical.

If \(u\) is balanced, \(\widehat u(0)=0\), so this zero coset contains the origin and is linear.

### Exact application gate

If the caller’s common quotient fibres are **identified with these parity cosets**, every nonzero fibre has odd \(\kappa\), hence

\[
k=2\kappa\in\{\pm2,\pm6\}.
\]

With exactly four \(|k_2|=2\) positions, this yields (M).

The algebraic bridge is proved. The identification of an unspecified historical “rank2” with this polar rank, and of the named caller fibres with these parity cosets, is **not independently established by that algebra**.

S3 line 13 states the nonzero-fibre magnitude pattern within its own adopted caller scope, while S3 also retains explicit historical-definition qualifications. I do not convert that source statement into a newly verified identification of every historical rank-two caller. The f394 core theorem therefore retains **(M) explicitly**, as required.

## 9. Claim-by-claim disposition

| Claim | Disposition | Exact boundary |
|---|---|---|
| Actual \(U_2=\pm1\) on \(S\), even \(0,\pm2,\pm4\) outside | **SUPPORTED** | Uses actual ternary blocks and distinct fibre characters |
| Boolean mod-three classification for residue support at most four | **SUPPORTED** | Includes every support cardinality, sign-product case, and actual lift |
| Affine gauge preserves the complete magnitude hypothesis | **SUPPORTED** | Affine coordinate relabeling only |
| Exactly one exceptional point above each \(y\in T\), with forced orientation | **SUPPORTED** | Uses all four exceptions and \(B=8\beta\) |
| Routing of all twelve regular fibres | **SUPPORTED** | Each has exactly one nonzero external-\(d\) transform coefficient |
| External support counts and integer Parseval contradiction | **SUPPORTED** | Uses actual even values on all 48 external blocks |
| Alternative full-block contradiction | **SUPPORTED** | Additionally requires \(X(A_2)\ne0\) |
| Affine-support/two-linear-structures equivalence | **SUPPORTED** | Requires the actual phase-support relation and \(|S|=16\) |
| Explicit parity-rank lemma | **SUPPORTED** | Rank means the specified quadratic polar rank |
| Historical rank/fibre identification for automatic (M) | **INCONCLUSIVE / NOT IMPORTED** | Remains a separate caller-identification gate |
| Author’s historical execution and read chronology | **NOT INDEPENDENTLY VERIFIED** | Source assertions are not execution evidence |
| Whole \(m=116\), general rank-two, or balanced NL242 closure | **NOT ESTABLISHED** | Not claimed by the reviewed theorem |

No mathematical claim in the stated conditional proof was refuted.

## 10. Final scope and verdict

The candidate supplies a complete written exclusion of actual ternary callers whose sixteen \(U_1=\pm3\) blocks form an affine four-flat **and** whose complete second-fibre spectrum satisfies (M). The proof accounts for every frequency fibre and all 64 actual blocks; it does not manufacture an actual caller from necessary shadow constraints.

The additional XOR-based block count and the phase linear-structure formulation are valid at their stated scopes. The parity-rank lemma is also valid, but its historical caller identification remains separate.

Not established here:

- Exclusion or construction of non-affine actual \(U\).
- A full \(U/V\) witness or complement solution.
- Exclusion of the entire \(m=116\) residual, other residuals, \(m=114\), rank two generally, or balanced NL242.
- Novelty, publication priority, human review, formal/kernel verification, or independent-model-family acceptance.

**overall_correctness:** correct  
**explanation:** The stated actual-object affine-flat obstruction is supported by a complete written reconstruction, including the Boolean classification, exceptional-fibre orientation, routing of every remaining fibre, and the all-block Parseval contradiction. This verdict retains (M) explicitly and does not close the historical rank/fibre identification or any whole-residual/global target.  
**confidence:** 0.98