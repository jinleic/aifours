# Addendum 4 — an all-integer iterated-copy inequality family

InfoGuessingRminus-2, original info-5. Actual native clock immediately before writing: **Tue Oct 27 15:16:39 PDT 2026**. AUTHOR-WRITTEN UNREVIEWED, under the existing definition-first S1 release.

Only finite probability, entropy chain identities and nonnegative conditional mutual information are used. This is a complete proof from those elementary facts, not an imported research theorem. No source expansion, closed fragment, held method, selected law, evaluated parameter, scientific execution or nested agent is involved. Prior exposure and the source-scope MINOR remain disclosed. No novelty or original guessing-number improvement is claimed.

## 1. Universal statement

For ANY four jointly distributed finite random variables A,B,C,D, set

`a=I(A;B|C)`,
`d=I(A;C|B)+I(B;C|A)`,
`Delta=I(A;B)-I(A;B|D)-I(C;D)`.

For EVERY integer n>=1,

`n Delta <= (n+1)a + [n(n+1)/2] d`.   (F_n)

Equivalently,

`n[I(A;B|C)+I(A;B|D)+I(C;D)-I(A;B)]`
` +I(A;B|C)+[n(n+1)/2][I(A;C|B)+I(B;C|A)] >= 0`.

No conditional-independence or alphabet restriction is placed on the original four variables. All degeneracies, deterministic variables and overlaps/identifications of variable blocks are allowed.

The proof below gives an exact decomposition into nonnegative CMIs for every n, rather than checking finitely many n or fitting coefficients from instances. The inequality is a classical finite-copy type of statement; identification with literature is not audited here.

## 2. One actual extension for the ENTIRE fixed-n proof

Fix an arbitrary positive integer n. Attach R_1,...,R_(n+1), each on C's finite alphabet, by the joint law

`p(a,b,c,d) product_(j=1)^(n+1) p(R_j=r_j | A=a,B=b)`,

where every new kernel is the original conditional law of C given A,B. On zero-probability conditioning pairs any kernel is harmless. The original A,B,C,D marginal is unchanged.

Conditional on A,B, the variables C,R_1,...,R_(n+1) are independent and identically distributed. The block of all R's is also independent of C,D given A,B. In particular every R_j has (A,B,R_j) distributed as (A,B,C).

Write S_j=(R_1,...,R_j), with S_0 empty, and h=H(C|A,B). For j=0,...,n define

`a_j=I(A;B|S_j)`,
`B_j=H(R_(j+1)|S_j)-h`,
`d_j=H(R_(j+1)|A,S_j)+H(R_(j+1)|B,S_j)-2h`.

Then a_1=a, and

`d_0=H(C|A)+H(C|B)-2H(C|A,B)=d`.

The conditional kernel implies H(R_(j+1)|A,B,S_j)=h. Therefore

`B_j=I(R_(j+1);A,B|S_j) >= 0`,
`d_j=I(R_(j+1);B|A,S_j)+I(R_(j+1);A|B,S_j) >= 0`.

No new graph-law independence is inferred: the independence belongs only to the explicitly attached auxiliary variables.

## 3. Two exact identities retaining the same coupling

### 3.1 Recurrence and bounded increments

The entropy chain rule gives

`a_(j+1)=a_j-B_j+d_j`.   (Rec)

Indeed the difference a_j-a_(j+1) is

`H(R_(j+1)|S_j)-H(R_(j+1)|A,S_j)`
` -H(R_(j+1)|B,S_j)+H(R_(j+1)|A,B,S_j)`
` = B_j-d_j`.

Marginal matching for each R_(j+1) also gives the EXACT nonnegative difference

`d-d_j=I(R_(j+1);S_j|A)+I(R_(j+1);S_j|B) >= 0`.   (Inc)

Thus d_j<=d, but not by an unproved monotonicity of conditional mutual information. The displayed difference proves precisely what is needed.

### 3.2 Exchangeability across the original C and the copies

For k=1,...,n, the conditional iid construction implies

`H(S_k,C)=H(S_(k+1))`,
`H(C)=H(R_1)`.

This equality concerns only C and the R's, not D. Also H(S_k|A,B,C)=kh. Consequently

`I(S_k;A,B|C)`
` =H(S_(k+1))-H(R_1)-kh`
` =sum_(j=1)^k [H(R_(j+1)|S_j)-h]`
` =sum_(j=1)^k B_j`.   (Ex)

No interchange of independently optimized extensions occurs; all terms above belong to the one fixed-n extension.

## 4. Exact nonnegative remainders for each prefix

Define

`E_k=a_k+I(S_k;A,B|C)-Delta`.

The conditional-kernel identities I(S_k;D|A,B)=0 and I(S_k;D|A,B,C)=0 give

`E_k = I(A;B|S_k,D)+I(S_k;D|A)+I(S_k;D|B)`
`      +I(C;D|S_k)+I(S_k;A,B|C,D) >= 0`.   (E)

Here are the two chain identities establishing it:

`I(A;B|S_k)+I(A;B|D)+I(S_k;D)-I(A;B)`
` +I(S_k;D|A,B)`
` =I(A;B|S_k,D)+I(S_k;D|A)+I(S_k;D|B)`;

`I(C;D)+I(S_k;A,B|C)-I(S_k;D)`
` =I(C;D|S_k)+I(S_k;A,B|C,D)-I(S_k;D|A,B,C)`.

The two subtracted/added conditional terms vanish in the actual extension. Adding the identities gives (E), with every term at the original same-law coupling.

Combining (Rec) and (Ex), the same E_k can alternatively be written

`E_k=a_1+sum_(j=1)^(k-1) d_j+B_k-Delta`.   (Tel)

## 5. Complete positive decomposition of the family

Sum (Tel) over k=1,...,n. Summing (Rec) over j=1,...,n gives

`a_(n+1)=a_1-sum_(j=1)^n B_j+sum_(j=1)^n d_j`.

The exact resulting identity is

`(n+1)a+[n(n+1)/2]d-n Delta`
` =sum_(k=1)^n E_k + a_(n+1)`
`   +sum_(j=1)^n (n-j+1)(d-d_j)`.   (Cert)

For clarity, the coefficient of d_j before the last sum is (n-j+1): it appears in E_(j+1),...,E_n and then once in a_(n+1). The last sum replaces these increments by their common upper bound d, and the sum of the integer weights is n(n+1)/2. This is finite symbolic summation for arbitrary n, not an executed enumeration or a check at selected values.

All terms on the right are nonnegative CMIs or positive integer multiples of their explicitly displayed sums: E_k by (E), a_(n+1) by CMI nonnegativity and d-d_j by (Inc). Hence (Cert) proves (F_n) for EVERY n.

## 6. Useful all-variable consequences, not parameter tests

### 6.1 Conditional zero-defect limit

If d=0, (F_n) gives Delta<=a+a/n for every positive integer n. Taking the ordinary scalar limit yields

`I(A;B)<=I(A;B|C)+I(A;B|D)+I(C;D)`.

This is a conditional consequence under the stated d=0 hypothesis, not unrestricted Ingleton and not a claim that the original graph forces that hypothesis.

### 6.2 A nonlinear uniform estimate from the entire family

For all finite original four-laws,

`Delta <= a+sqrt(2ad)+d`.   (Smooth)

If d=0 use §6.1. If d>0 and a=0, the family at its first member gives Delta<=d. If a,d>0 put t=sqrt(2a/d).

- If t>=1, take the integer n=ceil(t). Since n>=t and n+1<=t+2, (F_n)/n gives
  `Delta<=a+a/t+(t+2)d/2 = a+sqrt(2ad)+d`.
- If 0<t<1, use the first member Delta<=2a+d and a<d/2, which implies a<=sqrt(2ad).

This is an all-variable symbolic choice of an integer as a function of the theorem's parameters. No value of a,d,t or n is chosen or evaluated. It does not estimate an original-graph endpoint without an actual graph-specific coupling argument.

## 7. Exact original-law caller and unchanged gap

Apply the theorem to ANY four finite-valued functions/blocks A,B,C,D of an original ten-variable R-minus FD law. Attach the finite copies while retaining the entire original X marginal, not merely A,B,C,D. All original FDs then hold unchanged on X. The auxiliary-copy entropy equalities can be used only as displayed; replacing an original game variable by a copy is not justified.

The family can supply valid inequalities in an original ALL-ten-variable upper certificate. It is not itself that coefficient certificate, an actual strict-gain law, a bound below the inherited endpoint or a finite-word witness. No selected four blocks or finite-law table were used to validate it. All candidate graph substitutions must still pay every original FD and the homogeneous H(joint)/max H(vertex) normalization proved in v1.

The v1 type-class/decoder caller, this exact all-n inequality family and any eventual graph-specific coefficient identity require their own full-scope union assessment. No old review/adoption is transferred. A literature/SOTA audit and a claim of a genuinely stronger original bound remain unperformed.

Same original slot/new root; source line closed; STOP outside S1 and all HELD/ZERO/finding histories, scientific HOLDv2, N4 outcome/exit UNKNOWN and aux214 STOP persist. No program, selected arithmetic, source fetch or new GO. Research deadline 2026-10-31T21:23:27.000Z.
