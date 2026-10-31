# author-candidate-v1.md
## Coupled projected-phase code and uniform exclusions for the actual U/V caller

**Status:** AUTHOR / WRITTEN-PROOF CANDIDATE.  
**Actual model:** `anthropic/claude-fable-5-1`, same-harness general author.

### Result

For every **actual** U/V pair in the assigned rank-two/eight-zero/\(m=116\)/\((0,4,8)\)/\((G_3,H)=(1,0)\) residual, I derive:

1. An exact **common 16-sign code** coupling four projected V-phase fields to the actual flat U-fibre phase.
2. A four-fibre signed-correlation inequality stronger than the individual correlation bounds.
3. A uniform complement-fibre energy ceiling of **188**, improving the elementary ceiling 196.
4. Exclusion of entire phase-template neighborhoods:
   - any two V fibres require at least **16** total phase disagreements;
   - any three require at least **38**;
   - all four require at least **60**;
   - a specified linked family of four-fibre templates requires at least **78**.

These are quantified phase restrictions, not a restatement of coset occupancy, N1/N2, or the full autocorrelation equivalence. They apply regardless of how many surviving affine cosets the supports occupy.

**No actual U realizer, capped complement, balanced NL242 witness, or global no-go is claimed.**

---

## 1. Inputs, chronology, and verification status

The assigned bindings are:

- Manifest: `3755feeeb0da361d367e9ff3195f3864b09b4a47e775cabf34525e8140cc7c7e`
- Receipt: `2ba35cbefb9a2f18cc582bcc425c4a13da49309b90099ee175d4d5a21e2ef043`
- Literal packet: `ebf72b7aa01058fbd5886d8a579a67af11020d9c11d85c962840b60f07e0eaaa`

These are **parent-supplied bindings**, not hashes executed by this author.

Before derivation, I read the complete manifest and receipt, all six listed permission/status controls, and the ordered packet S1–S5 through its ending. Initial normal displays truncated long lines; I subsequently read raw packet ranges 1–40, 41–80, 81–118, and 119–156, plus the untruncated manifest research task.

The load-bearing scientific imports are:

- **S3:** the actual-object block normalization, the flat \(|k_1|=6\) fibre, and the sixteen \(U_1=\pm3\) blocks.
- **S4:** the original complementary U/V interface and the globally odd cap \(z\in\{\pm1,\pm3,\pm5,\pm7\}\).

S1 provides the preceding coset-exclusion frontier but is not used in the proofs below. S2’s full AC equivalence is not used as a substitute for the local arguments. S5 is used only for its explicitly bounded literature-status qualification. Historical proof bodies linked inside the dispositions were not separately opened. No held scientific payload or its consumers was used.

After the initial phase derivation, I read the parent metadata supply carrying the observation **2026-10-30T09:21:00-0700 PDT**. A later parent message supplied **2026-10-30T09:28:25-0700 PDT**. Neither is my native start, derivation, or completion timestamp. I sent Main a substantive mathematical checkpoint. No author-native date/hash execution or independently timestamped author cadence is claimed.

**Proof/experiment distinction:** no scientific executable, finite search, random experiment, or public-source search was run. All constants below follow from displayed exact arithmetic. There is no executed certificate or calculation-code output.

No repository/source file was changed. This is the complete body for Main materialization.

---

## 2. Actual-object notation

Let
\[
R=\mathbb F_2^6,\qquad Q=\mathbb F_2^2,
\]
with inherited labels \(1=2+3\). Write the actual eight-variable pair functions as
\[
u(c,w),\ v(c,w),\qquad c\in R^*,\ w\in Q^*.
\]

They are real ternary and satisfy
\[
u(c,w)^2+v(c,w)^2=1
\]
pointwise. All original balance, spectral, and residual conditions remain imposed.

Define the local four-point transforms
\[
U_s(c)=\sum_w u(c,w)\chi_s(w),\qquad
Z_s(c)=\sum_w v(c,w)\chi_s(w).
\]

A hat denotes the unnormalized 64-point Fourier transform between \(R\) and \(R^*\). The adopted normalization is
\[
\widehat U_s=2k_s,\qquad
\widehat Z_s=2z_s,
\]
where
\[
z_s(r)\in\{\pm1,\pm3,\pm5,\pm7\}.
\]

The assigned actual-object facts give
\[
k_1(r)=6\sigma(r),\qquad \sigma(r)\in\{\pm1\},
\]
and
\[
U_1(c)\in\{0,\pm3\},
\qquad
\#\{c:U_1(c)\ne0\}=16.
\]

Set
\[
S=\{c:U_1(c)\ne0\},\qquad a(c)=U_1(c)/3.
\]
Thus \(|S|=16\), \(a=\pm1\) on \(S\), and \(a=0\) elsewhere. Fourier involution gives
\[
\widehat a=4\sigma,\qquad \widehat\sigma=16a. \tag{1}
\]

### The sixteen triple-support blocks

For \(c\in S\), the equality \(|U_1(c)|=3\) means exactly three of the four ternary values \(u(c,w)\) are nonzero. A sum of four terms from \(\{0,\pm1\}\) equal to \(\pm3\) has exactly three nonzero terms, aligned in sign.

There is consequently a unique missing point \(w_0(c)\), and
\[
u(c,w)=a(c)\chi_1(w)\quad(w\ne w_0(c)),
\qquad
u(c,w_0(c))=0.
\]
For \(j\ne1\),
\[
U_j(c)=-a(c)\chi_{j+1}(w_0(c)). \tag{2}
\]

Actual complementarity supplies one sign \(b(c)\in\{\pm1\}\) such that
\[
v(c,w)=b(c)\mathbf1_{\{w=w_0(c)\}},
\qquad
Z_s(c)=b(c)\chi_s(w_0(c)). \tag{3}
\]

These formulas require an **actual** \(u\). Necessary support geometry or labelled magnitudes do not supply one.

---

## 3. Exact common 16-sign projected-phase code

For functions on \(R\), use
\[
(f*g)(t)=\sum_r f(r)g(r+t).
\]
Define
\[
C_s=\sigma*z_s.
\]

### Theorem 1 — common projected-phase code

Every actual complement satisfies
\[
\boxed{
C_s(t)=8\sum_{c\in S}
\theta(c)\chi_s(w_0(c))(-1)^{t\cdot c}
}
\tag{4}
\]
for one **common** sign field
\[
\theta(c)=a(c)b(c)\in\{\pm1\}.
\]

**Proof.** Since \(\widehat Z_s=2z_s\), Fourier involution gives
\[
\widehat z_s=32Z_s.
\]
Together with (1),
\[
\widehat C_s
=\widehat\sigma\,\widehat z_s
=512aZ_s.
\]
Inversion divides by 64, hence
\[
C_s=8\widehat{aZ_s}.
\]
Equation (3) gives \(aZ_s=\theta\chi_s(w_0)\) on \(S\), and this product vanishes off \(S\). This proves (4). ∎

### Exact local converse, not global sufficiency

Fix an actual \(u\). Suppose a real full-dual array \(z\) satisfies (4) for one \(\theta\). Comparing Fourier transforms gives, on \(S\),
\[
Z_s(c)=a(c)\theta(c)\chi_s(w_0(c)).
\]
Four-point inversion in \(Q\) then yields
\[
v(c,w)=a(c)\theta(c)\mathbf1_{\{w=w_0(c)\}}.
\]

Thus (4) is necessary and sufficient for the inverse \(v\) to sign precisely the required singleton complement on **these sixteen blocks**.

It is not sufficient for the other 48 blocks, the global odd cap, or any original-target witness.

For fixed actual \(u\), the **ambient code** in (4) contains exactly \(2^{16}\) quadruples: \(\theta\) is recovered from \(C_0\) by Fourier inversion. Actual globally admissible odd-capped complements realize only a subset, **possibly empty**. No admissible lift is asserted for every codeword.

### Immediate necessary conditions

For every \(s,t\),
\[
\boxed{C_s(t)\in16\mathbb Z,\qquad |C_s(t)|\le128,}
\tag{5}
\]
and
\[
\boxed{\sum_t C_s(t)^2=65536.} \tag{6}
\]

Indeed, the sum in (4) contains sixteen signs and is therefore even. Parseval applied to eight times the transform of a sixteen-support sign field proves (6).

### Exact cross-fibre identities

Put \(q_s=aZ_s\). On \(S\),
\[
q_s q_t=\chi_{s+t}(w_0)
=-aU_{s+t+1}\qquad(s\ne t),
\]
and both sides vanish outside \(S\). Since \(C_s=8\widehat q_s\),
\[
C_s*C_t=4096\widehat{q_s q_t}.
\]
Also,
\[
\sigma*k_j=8\widehat{aU_j}.
\]
Consequently,
\[
\boxed{
C_s*C_t=-512\,\sigma*k_{s+t+1}\quad(s\ne t),
}
\tag{7}
\]
while
\[
\boxed{
C_s*C_s=1024(\sigma*\sigma).
}
\tag{8}
\]

In particular,
\[
\begin{aligned}
C_0*C_1=C_2*C_3&=-512\,\sigma*k_0,\\
C_0*C_2=C_1*C_3&=-512\,\sigma*k_3,\\
C_0*C_3=C_1*C_2&=-512\,\sigma*k_2.
\end{aligned}
\]

These are derived restrictions, not additional independent gates once full actual complementarity is known.

---

## 4. A genuinely four-fibre phase inequality

### Theorem 2 — linked signed-correlation bound

Choose any
\[
t_0,t_1,t_2,t_3\in R,
\qquad t_0+t_1+t_2+t_3=0,
\]
and signs \(\epsilon_s\) satisfying
\[
\prod_s\epsilon_s=-1.
\]
Then
\[
\boxed{
\left|\sum_s\epsilon_s C_s(t_s)\right|\le256.
}
\tag{9}
\]

**Proof.** For each \(c\in S\), the four signs \(q_s(c)=a(c)Z_s(c)\) have product \(1\). Therefore the four signs
\[
\eta_s(c)=\epsilon_s q_s(c)(-1)^{t_s\cdot c}
\]
have product \(-1\). Their sum is \(+2\) or \(-2\). Sum over sixteen positions and multiply by eight. ∎

This is stronger than four separate bounds \(|C_s|\le128\). For example, the coordinate bounds alone permit the tuple
\[
(128,128,128,-128)
\]
at zero shifts, but \(\epsilon=(1,1,1,-1)\) makes its signed sum 512, violating (9). This tuple only illustrates the distinction; it is not asserted to be an actual or capped spectrum.

---

## 5. Uniform complement-fibre energy ceiling 188

Define
\[
E_s=\sum_c Z_s(c)^2.
\]
Parseval gives
\[
\sum_r z_s(r)^2=16E_s.
\]
The original odd cap implies
\[
E_s\le196. \tag{10}
\]

On \(S\), \(Z_s^2=1\). At every other \(c\), \(U_1(c)=0\) forces the support size of \(u(c,\cdot)\) to be even: \(U_1\) modulo two equals that support size modulo two. The complementary support size is also even, so \(Z_s(c)\) is even. Thus
\[
E_s\in4\mathbb Z. \tag{11}
\]

The two largest possibilities in (10)–(11) are impossible.

### Exclusion of \(E_s=196\)

Equality would force every \(|z_s(r)|=7\). Write \(z_s=7\rho\), with \(\rho=\pm1\). Then
\[
32Z_s=7\widehat\rho.
\]
Because \(Z_s\) is integral, this forces every \(Z_s\) to be divisible by seven, contradicting \(Z_s=\pm1\) on \(S\).

### Exclusion of \(E_s=192\)

Let \(n_j\) count the coefficients with \(|z_s|=j\). The deficit from \(64\cdot49\) is 64, giving
\[
6n_1+5n_3+3n_5=8.
\]
Its unique nonnegative solution is
\[
n_1=0,\qquad n_3=1,\qquad n_5=1.
\]
Hence, for distinct \(i,j\),
\[
z_s=7\rho-4\rho(i)\delta_i-2\rho(j)\delta_j.
\]
For any \(c\in S\),
\[
32Z_s(c)
=7\widehat\rho(c)
-4\rho(i)\chi_i(c)-2\rho(j)\chi_j(c).
\]
Modulo seven, the left side belongs to \(\{3,4\}\), because \(Z_s(c)=\pm1\). The right side belongs to \(\{1,2,5,6\}\). This is impossible.

We obtain the uniform ceiling
\[
\boxed{E_s\le188\quad\text{for every }s.} \tag{12}
\]

This improves a **fibre energy ceiling**, not the permitted pointwise cap \(|z|\le7\).

Finally, four-point Parseval and \(|\operatorname{supp}v|=140\) give
\[
\boxed{\sum_s E_s=4\cdot140=560.} \tag{13}
\]

---

## 6. Entire phase-template neighborhoods excluded

For any fibre \(s\), translation \(t\), and sign \(\epsilon\), define
\[
h_s(t,\epsilon)
=
\#\{r:\operatorname{sgn}z_s(r)\ne\epsilon\sigma(r+t)\}.
\]
Every sign is defined because the original \(z\) entries are odd and nonzero.

Let
\[
A_s=\sum_r|z_s(r)|,
\]
and let \(D_s\) be the sum of \(|z_s(r)|\) over those disagreements. Then
\[
\epsilon C_s(t)=A_s-2D_s,
\qquad D_s\le7h_s. \tag{14}
\]

For every allowed magnitude \(d\in\{1,3,5,7\}\),
\[
d^2\le8d-7.
\]
Summing and using \(\sum z_s^2=16E_s\) yields
\[
A_s\ge2E_s+56.
\]
Combining this with (5) and (14),
\[
\boxed{E_s\le36+7h_s(t,\epsilon).} \tag{15}
\]

### Theorem 3 — uniform two-, three-, and four-fibre exclusions

Let \(J\) be **any** set of \(m\) fibres, with independently chosen translations and flips for its members. By (12)–(13),
\[
\sum_{s\in J}E_s
\ge560-188(4-m)
=188m-192.
\]
Equation (15) therefore implies
\[
7\sum_{s\in J}h_s\ge152m-192.
\]

Thus:

| Selected fibres | Minimum total disagreements |
|---|---:|
| Any two | **16** |
| Any three | **38** |
| All four | **60** |

These statements are uniform over:

- every actual \(u\) in the assigned residual;
- every support placement;
- every allowed magnitude assignment;
- every independent choice of translations and global signs.

In particular:

- Two V fibres cannot both have phase exactly equal to translated/flipped copies of \(\sigma\).
- Every such two-fibre phase neighborhood of radius **15** is excluded.
- Every three-fibre neighborhood of radius **37** is excluded.
- Every four-fibre neighborhood of radius **59** is excluded.

Also, at least one fibre has \(E_s\ge140\), by (13). That fibre individually has at least
\[
\left\lceil\frac{140-36}{7}\right\rceil=15
\]
disagreements with **every** translated/flipped \(\sigma\).

### Stronger linked four-fibre exclusion

For the linked templates of Theorem 2,
\[
\sum_s A_s
\ge2\cdot560+4\cdot56
=1344.
\]
Using (9),
\[
\sum_s D_s
=
\frac{\sum_s A_s-\sum_s\epsilon_s C_s(t_s)}2
\ge\frac{1344-256}{2}
=544.
\]
Since each disagreement contributes at most seven,
\[
\boxed{\sum_s h_s(t_s,\epsilon_s)\ge
\left\lceil544/7\right\rceil=78.} \tag{16}
\]

Therefore the entire radius-**77** neighborhood of **every** four-fibre template with
\[
\sum_s t_s=0,\qquad \prod_s\epsilon_s=-1
\]
is excluded.

No bound is claimed optimal, and no actual caller is asserted to attain an endpoint.

---

## 7. Relation to the frozen target and exact remaining gaps

The new restriction is explicitly **U/V phase-coupled**:

- \(\sigma\) is the actual sign of the flat \(|k_1|=6\) U fibre.
- Each \(C_s=\sigma*z_s\) uses the actual odd-capped V spectrum.
- The common sixteen-sign code prevents the four projected fibres from being independently phased.
- The signed-correlation inequality and phase-distance bounds exclude quantified entire families, not merely selected examples.

The proof neither uses nor restates the two-coset obstruction. Its phase information is absent from the A2/A3 occupancy counts and unlabelled magnitude ledgers. Like every valid necessary consequence, these restrictions are automatic for a full actual solution; their load-bearing contribution is the explicit phase families now excluded.

**Still unpaid:**

- Existence of an actual U realizer in the assigned residual.
- An odd-capped V complement satisfying the other 48 blocks and all global equations.
- Exclusion of the residual beyond the phase families proved above.
- Other fibre patterns, \(m=114\), other class-count pairs, rank two generally, and the complete balanced nine-variable NL242 target.

No 512-character Walsh witness computation was performed or claimed. Any future exact witness still requires its complete Walsh transform, balance, and exact maximum coefficient.

No new literature or novelty claim is made. Frozen S5 establishes only that its checked published NL242 examples were imbalanced and did not supply a balanced NL242 witness. It does not establish global openness or priority.

**Acceptance boundary:** the displayed theorems remain author claims with complete written proofs, requiring disjoint mathematical checking and a separate parent disposition. They are not numerical, independent-family, human, or kernel acceptance.