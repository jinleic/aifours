# Heterogeneous completion: exact pure-run solution, one-gap equations and a finite support obstruction

Observed before creation: **Sun Oct 25 04:04:36 PDT 2026** (`/bin/date`). MathShor, math-5.

**Original-target verdict: NOT_PROVED.** This packet does not supply a finite complete extension of Shor's code and does not exclude every finite extension. It replaces the retired common-tail-length ansatz by an exact algebraic elimination of the unrestricted pure-run subsystem, followed by exact one-positive-gap equations. It also proves an all-order obstruction to a precisely stated heterogeneous architecture. The obstruction is not unrestricted noncompletion.

**Verification label:** WRITTEN, with the finite polynomial/collision calculations explicitly listed in Section 8 WRITTEN-checked-in-kernel. Here “kernel” means this owner's ordinary persistent Python eval kernel, NOT Lean, a proof-assistant kernel, independent implementation, cross-vendor review or novelty clearance. Integer/Fraction arithmetic only; no native scientific program, solver, background scientific job, model CLI or nested agent.

## 1. Literal target, imports and achieved statements

The literal sixteen words remain

```text
C = b{1,a,a^7,a^13,a^14}
    union {a^3,a^8}b{1,a^2,a^4,a^6}
    union a^11 b{1,a,a^2}.
```

Throughout, a completion means a FINITE set M of nonempty raw words containing C, uniquely decodable on all finite lists, with every binary word a factor of some M-product. No restriction on added lengths, number of b's, pure-a order, symmetry or number of words is imposed unless a theorem explicitly says so.

Named local imports, with freshly observed SHA-256:

- `proof-RAW-GAP-PARSER-AND-FOUR-A-COMPATIBILITY-v1.md`, `adf92f65c11c0fe03e3941102bf4492979dcb68e493443553b3802c71a26c2bb`: Section 1, the exact free-end gap-parser theorem GP. Its parent boundary is `shor-raw-structure-parent-v1.md`. Only the stated GP interface is consumed here, not a general realization converse.
- `raw-realization-protocol-v1.md`, `544f547ba826076f452d3f478bf4585ecfe9e2da0f2d643f03e79732e568e578`: Section 2, the non-Shor complete UD control M0, and the elementary residual/Kraft proofs. Its control is not evidence for a Shor completion.
- `mathematics/shor-code-finite-completion/evidence/raw-instance.json`, `6eb38f63bfee602369a09b22be26a0c598111f33b8202d44349786903f63ecf4`: the sixteen literal exponent pairs.

The new results are:

1. An exact solution of ALL adjacent-pure-a-run parsing conditions in terms of a cyclic direct factorization and uniquely determined finite lifted deficits. Arbitrary positive b-delays are retained.
2. A finite bivariate polynomial identity for ALL two-run cores with a fixed positive b-gap, valid for every run length, not a finite sample. This gives exact heterogeneous constraints beyond the scalar Bernoulli identity.
3. An explicit control proving that satisfying every pure-run and every one-positive-gap equation still does NOT imply complete extension.
4. Every actual completion must contain a pure-end word `a^ell b^beta`, with `ell>=26` and `beta>=1`. Equivalently, there is no finite completion whose pure-end a-exponents are all at most 25, even if ALL other tail lengths and b-counts are unrestricted. The proof is an exact finite algebraic certificate, uniform in every possible pure-a order.

Statement 4 is a structural escape requirement, not a new pure-a order bound or an existence answer. No significance/novelty claim is attached to this finite support exclusion; the existence-changing obligation remains the one in Section 9.

## 2. Pure-run data with genuinely heterogeneous delays

A pure-core word means a raw word whose a's form one adjacent run. Apart from the codeword b, classify such words as follows:

```text
pure:      a^n;
start:     b^alpha_r a^r,             alpha_r>=1, r>=1;
end:       a^s b^beta_s,              beta_s>=1, s>=1;
isolated:  b^rho_q a^q b^tau_q,       rho_q,tau_q>=1, q>=1.
```

A finite complete M has a pure word: otherwise any zero-gap parse can contain at most one start word and one end word, or one isolated word, so its number of adjacent a's is bounded. GP requires zero-gap parses of every length. UD permits only ONE pure word, since two different positive powers of a commute and give an ambiguity.

GP also allows at most one start of a given a-length r, at most one end of a given a-length s, and at most one isolated word of a given a-length q. Two words of the same type and length would give distinct singleton free-end parses. Different types can likewise not coexist at a length already parsed by the others.

Define finite polynomials with nonnegative integer coefficients:

```text
L(z) = 1 + sum_start z^r,       R(z) = 1 + sum_end z^s,
H(z) = sum_isolated z^q,        Delta(z)=1-z^n,
S_n(z)=1+z+...+z^(n-1).
```

The constant 1 in L and R is an empty endpoint, not an empty codeword. In particular H has zero constant term. Delays are attached to the actual labelled words and are not discarded in later positive-gap conditions.

At zero internal b-gap, a proper boundary requires both the preceding trailing delay and the following leading delay to be zero. Consequently every nonempty pure-run parse is exactly one of:

- an optional start, followed by any number of `a^n`, followed by an optional end;
- a single isolated word.

There is no other order: a positive leading delay prevents a start from occurring after another word at gap zero; a positive trailing delay prevents an end from occurring before another word; an isolated word cannot be joined on either side.

Including the empty a-run once, the exact count series is therefore

```text
L(z) R(z)/(1-z^n) + H(z).
```

It follows that the pure-run conditions are equivalent to the POLYNOMIAL identity

```text
L(z)R(z) + (1-z^n)H(z) = S_n(z).                 (PR)
```

This is necessary and sufficient for unique free-end parsing of every pure a-run by these actual pure-core words. It does NOT assert unique parsing when a positive internal b-gap is present.

## 3. Algebraic solution of PR, including the lifted deficits

Reducing PR modulo `z^n-1` gives

```text
L(z)R(z) = S_n(z)  modulo z^n-1.                 (CF)
```

All coefficients in L and R are nonnegative. Thus every residue k modulo n has exactly ONE representation `r+s mod n`, with r an actual exponent from L and s an actual exponent from R. Neither set can repeat a residue. In particular

```text
|supp L| * |supp R| = n.
```

For each `0<=k<n`, let the unique ACTUAL nonnegative sum be

```text
r_k+s_k = k+n h_k,       h_k>=0.
```

The two empty endpoints give the unique residue-zero sum 0, so `h_0=0`. Equation PR now has the unique solution

```text
H(z) = sum_(k=0)^(n-1) sum_(j=0)^(h_k-1) z^(k+jn). (LIFT)
```

Proof: subtract the unique monomial `z^(k+n h_k)` from `z^k` and divide by `1-z^n`; the finite geometric sum is exactly the displayed inner sum. Different k give disjoint exponent classes. Therefore every coefficient of H is 0 or 1 and its constant term is zero.

Conversely, any finite nonnegative endpoint sets containing 0 that directly factor the cyclic residues yield precisely this H, and then PR holds. Give each nonzero L exponent an arbitrary positive leading b-delay, each nonzero R exponent an arbitrary positive trailing b-delay, and each exponent of H arbitrary positive delays at both ends. The resulting pure-core words uniquely parse every pure a-run. Positive-gap compatibility is a separate obligation.

Thus the pure-run subsystem has been solved algebraically, rather than truncated at an a-count cutoff. Lifted exponents need not lie below n; no short-representative cancellation or residue-to-raw-code converse has been assumed. No Szabo/Redei theorem is used in this derivation.

## 4. Exact one-positive-gap heterogeneous completion equation

Keep actual positive b-delays, and suppose the pure-run data satisfy PR. Split their profiles by delay:

```text
R_d(z) = sum_(end beta_s=d) z^s,        d>=1,
L_e(z) = sum_(start alpha_r=e) z^r,     e>=1,
H^end_d(z) = sum_(isolated tau_q=d) z^q,
H^start_e(z) = sum_(isolated rho_q=e) z^q.
```

Let `F_d(z)` count nonempty pure-run parses by final trailing delay d, and `G_e(z)` by initial leading delay e. The classification above gives exactly

```text
F_0(z)=L(z)/Delta(z)-1,
F_d(z)=L(z)R_d(z)/Delta(z)+H^end_d(z),       d>=1;
G_0(z)=R(z)/Delta(z)-1,
G_e(z)=R(z)L_e(z)/Delta(z)+H^start_e(z),     e>=1.
```

All are actual nonnegative formal count series. Their sums over the delay index are `z/(1-z)`. Define their finite numerators

```text
U_0=L-Delta,      U_d=L R_d+Delta H^end_d  (d>=1),
V_0=R-Delta,      V_e=R L_e+Delta H^start_e (e>=1).
```

Fix ANY positive integer g. Consider every core `a^p b^g a^q`, with p,q positive. A parse with no word crossing the displayed gap is counted by

```text
N_g(z,w) = sum_(d+e<=g) F_d(z)G_e(w).       (NB)
```

The inequality is exact; the remaining `g-d-e` copies of b are uniquely determined. If a word crosses the gap, it is uniquely of form

```text
b^alpha a^i b^g a^j b^beta,       i,j>=1, alpha,beta>=0.
```

There can be at most one crossing word. All other a-containing words of this parse have pure core. Classify the ACTUAL crossing words by whether alpha and beta are zero or positive, and let their four finite bivariate count polynomials be

```text
B_00(z,w), B_0+(z,w), B_+0(z,w), B_++(z,w),
```

where each word contributes `z^i w^j` to its class. This classification retains distinct raw labels. It does not identify two words merely because their internal core agrees.

If alpha=0, the possible prefix before the crossing word is empty or any pure-run parse with trailing delay zero, hence has generating series `L(z)/Delta(z)`. If alpha>0, that prefix must be empty. The right-side analogue is `R(w)/Delta(w)` when beta=0, and only the empty suffix when beta>0.

Consequently all one-positive-gap conditions for this g are equivalent to the FINITE polynomial identity

```text
D_g(z,w)
 := z S_n(z) w S_n(w)
       - sum_(d+e<=g) U_d(z)V_e(w)

  = L(z)R(w) B_00(z,w)
      + L(z)Delta(w) B_0+(z,w)
      + Delta(z)R(w) B_+0(z,w)
      + Delta(z)Delta(w) B_++(z,w).             (HG_g)
```

Proof: the target count series is `z/(1-z) * w/(1-w)`. Subtract NB, add the four mutually exhaustive crossing-word contributions, and multiply by `Delta(z)Delta(w)`. Both Delta factors have constant term 1, so this multiplication is invertible in formal power series and loses no condition. The converse follows by coefficient comparison for every p,q. This is an equivalence for this subsystem, not merely a necessary moment identity.

Only finitely many g can have a nonzero crossing-word polynomial in any fixed finite M. If g is at least every sum of a pure-run final delay and initial delay, NB already equals the target, and no crossing word may occur. However, the equations for different g and for cores with TWO OR MORE positive gaps still have to be compatible. The four B-polynomials are actual-word data, not freely chosen signed corrections.

## 5. Exact control: every PR and HG_g can hold while completeness fails

Use the non-Shor code

```text
K0={aa,b,abb,aaaba,baba}.
```

It is a subset of the complete UD control

```text
M0={aa,b,abb,aaaba,baba,abbaba,abaaba}
```

proved in the named raw-realization protocol. Hence K0 is UD, but its exact Kraft sum is `31/32`, so it is not complete. M0 has Kraft 1.

For K0 the pure data are

```text
n=2, L(z)=1, R(z)=1+z, H=0,
```

and its only positive pure-end delay is 2. PR holds exactly.

At g=1 the only crossing words are

```text
aaaba = a^3 b a:       B_00=z^3 w,
baba  = b a b a:       B_+0=z w.
```

The numerator of the no-crossing count is `z^2(w+w^2)`. Thus the HG_1 defect is `z w(1+w)`, and the supplied bridges give exactly

```text
(1+w) z^3 w + (1-z^2)(1+w) z w = z w(1+w).
```

For every g>=2 all pure-run boundaries are permitted, no single-gap crossing word exists, and the defect is zero. Therefore K0 uniquely parses EVERY pure-run core and EVERY core with exactly one positive b-gap.

Nevertheless the three-a core `a b^2 a b a` has no free-end parse by K0. The only one-a word is `abb`, with final delay 2; the only crossing candidate with two separated a's is `baba`, with internal gap 1 and initial delay 1. If it covers the last two a's, its join to the first `abb` requires gap at least `2+1=3`, but that gap is 2. It cannot cover the first two because their gap is 2. Singleton parsing fails at the last gap 1. The words `aa` and `aaaba` require adjacent a's and cannot fit. These cases exhaust the codewords.

This exact all-length positive/negative control is why PR plus every HG_g is NOT presented as a solution to the original problem. A two-positive-gap coherence obligation is real and cannot be removed by solving each bivariate identity separately.

## 6. Raw C identities exclude nearly every small pure-end exponent

Let

```text
I={0,3,8,11},
S={1,2,4,6,7,12,13,14}.
```

For every s in S there are literal words `p_s` and `p_s a^s` in C. Explicit choices are:

| s | p_s | p_s a^s |
|---|---|---|
| 1 | b | ba |
| 2 | a^3b | a^3ba^2 |
| 4 | a^3b | a^3ba^4 |
| 6 | a^3b | a^3ba^6 |
| 7 | b | ba^7 |
| 12 | ba | ba^13 |
| 13 | b | ba^13 |
| 14 | b | ba^14 |

For any `i in I`, the base word `v_i=a^i b` is in C. Suppose a completion also contained `w=a^(i+s) b^beta`, beta>=1. Then the two distinct literal codeword lists

```text
(p_s a^s)(v_i)(b)^(beta-1) = (p_s)(w)           (COL)
```

have the same raw concatenation. The first codewords differ and all exponents are nonnegative. Thus this w is impossible in ANY UD extension, independently of completeness.

The exact sumset `I+S` is

```text
{1,2,4,5,6,7,9,10,12,13,14,15,16,17,18,20,21,22,23,24,25}.
```

Consequently the only possible pure-end exponents at most 25 are

```text
0,3,8,11,19.
```

Here 0 belongs only to the empty endpoint marker in R: a positive pure-b codeword other than b is forbidden by UD, and b itself has no a's. GP rules out another pure-end word with a-length 3,8 or 11 and a different trailing delay, since C already supplies the singleton parse. Therefore, if ALL pure-end exponents were at most 25, the actual endpoint polynomial R would be exactly one of

```text
R4(z)=1+z^3+z^8+z^11,
R5(z)=1+z^3+z^8+z^11+z^19.
```

There is no assumption on other codewords or on their lengths in this dichotomy.

## 7. Exact finite, all-order obstruction to both endpoint masks

### 7.1 Four-term case: one explicit signed multiplier

The integer polynomial identity

```text
R4(z)(1-z^3+z^6)=1+z^8+z^9+z^17               (DUAL)
```

is exact. If L and R4 directly factored the cyclic group modulo ANY n, let `u_j` be the 0/1 indicator of L's residue support. Multiplication of CF by the displayed multiplier preserves `S_n`, since its value at 1 is 1. Hence

```text
u_j+u_(j-8)+u_(j-9)+u_(j-17)=1,       all j modulo n.
```

C contains `ba^13` and `ba^14`, so `u_13=u_14=1`. At j=22 the left side includes BOTH of these entries and the two nonnegative entries `u_22,u_5`; it is at least 2, contradicting 1. The argument remains valid if some indices coincide modulo n: repeated contributions do not become negative. No bound on n was used.

### 7.2 Five-term case: no root of unity

The polynomial R5 has no root of unity. Here is a complete finite certificate with an explicit completeness bound.

If a primitive m-th root were a zero, its minimal polynomial `Phi_m` would divide the degree-19 integer polynomial R5, so `phi(m)<=19`. For `m=product p^a`,

```text
phi(m)^2/m = product p^(a-2)(p-1)^2 >= 1/2.
```

Indeed the only possible factor less than 1 is 1/2 from p=2,a=1; every odd-prime factor is at least 4/3. Therefore `m<=2*19^2=722`.

The complete candidate list is

```text
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
21,22,24,26,27,28,30,32,34,36,38,40,42,48,54,60.
```

For each candidate, exact monic polynomial division leaves a nonzero remainder. The table records ONE nonzero coefficient of each remainder; the companion JSON contains every full divisor, quotient and remainder, not just this summary.

| m | phi(m) | remainder exponent | coefficient |
|---|---:|---:|---:|
| 1 | 1 | 0 | 5 |
| 2 | 1 | 0 | -1 |
| 3 | 2 | 1 | -1 |
| 4 | 2 | 0 | 2 |
| 5 | 4 | 2 | -1 |
| 6 | 2 | 1 | 1 |
| 7 | 6 | 0 | 1 |
| 8 | 4 | 0 | 2 |
| 9 | 6 | 0 | 1 |
| 10 | 4 | 0 | 2 |
| 11 | 10 | 0 | 2 |
| 12 | 4 | 0 | 1 |
| 13 | 12 | 0 | 1 |
| 14 | 6 | 0 | 1 |
| 15 | 8 | 4 | 2 |
| 16 | 8 | 3 | 1 |
| 17 | 16 | 0 | 1 |
| 18 | 6 | 0 | 1 |
| 19 | 18 | 0 | 2 |
| 20 | 8 | 2 | 1 |
| 21 | 12 | 0 | 2 |
| 22 | 10 | 3 | 1 |
| 24 | 8 | 4 | 1 |
| 26 | 12 | 0 | 1 |
| 27 | 18 | 0 | 1 |
| 28 | 12 | 0 | 1 |
| 30 | 8 | 1 | -2 |
| 32 | 16 | 0 | 1 |
| 34 | 16 | 0 | 1 |
| 36 | 12 | 0 | 1 |
| 38 | 18 | 3 | 1 |
| 40 | 16 | 0 | 1 |
| 42 | 12 | 1 | -1 |
| 48 | 16 | 0 | 1 |
| 54 | 18 | 0 | 1 |
| 60 | 16 | 0 | 1 |

This uses only the elementary minimal-polynomial property of cyclotomic polynomials and their product formula, explicitly named classical algebra imports. There is no numerical root finding or assumption that a search miss at an arbitrary order suffices.

Now for ANY positive n, R5 is relatively prime to `z^n-1`. The cyclic equation `L R5=S_n` therefore has a unique solution over the rational quotient ring. Since `R5 S_n=5 S_n`, that solution is `L=(1/5)S_n`. Its coefficients are not 0/1 and its constant coefficient is not 1. This contradicts the actual endpoint polynomial L. Hence R5 cannot occur.

### 7.3 Structural consequence and its non-claim

Both possibilities from Section 6 are impossible. Every finite UD factor-complete M containing C therefore has an ACTUAL word

```text
a^ell b^beta in M,       ell>=26, beta>=1.        (ESCAPE)
```

This excludes all finite heterogeneous extensions with the pure-end support capped at 25. It also rules out any completion architecture keeping the seed proof's first-b rows `{0,3,8,11}`, even if arbitrary long words with arbitrarily many internal b's are admitted in those rows.

ESCAPE does NOT prohibit larger pure-end exponents and does NOT make the critical-gap theorem iterate. It supplies neither a new pure-a order threshold nor a new general noncompletion theorem. A finite architecture with new pure-end rows beyond this support remains mathematically possible as far as this argument reaches.

## 8. Exactly what the eval arithmetic checked

Companion evidence:

`heterogeneous-pure-run-and-gap-certificate-v1.json`

SHA-256: `0a12885d622e7ba14b642e656bb5b088d3614fb6981cd86b39481e3774203c49`.

Only the following finite calculations receive WRITTEN-checked-in-kernel credit:

1. The literal 16-word set, the eight residual witnesses and all 21 raw COL identities at beta=1. The written b-padding argument, not a beta cutoff, extends them to every beta>=1.
2. The exact forbidden sumset, allowed exponents through 25, and integer polynomial identity DUAL.
3. All cyclotomic polynomials through m=722 by exact recursive monic division of `z^m-1`; the degree filter yielding the 36 candidates; all 36 quotient/remainder identities; nonzero remainders. The finite bound itself is the written arithmetic argument above.
4. The two bivariate polynomial equalities for the non-Shor K0 control and its Fraction Kraft `31/32`, plus M0's Kraft 1.

The elementary polynomial routines, expressed here in reproducible form, were:

```python
def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p

def divmonic(a,b):
    a=trim(a); b=trim(b)
    assert b[-1]==1
    q=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and a!=[0]:
        d=len(a)-len(b); c=a[-1]; q[d]=c
        for j,bj in enumerate(b):
            a[d+j]-=c*bj
        a=trim(a)
    return trim(q),a

Phi={}
for m in range(1,723):
    p=[-1]+[0]*(m-1)+[1]
    for d in range(1,m):
        if m%d==0:
            p,rem=divmonic(p,Phi[d])
            assert rem==[0]
    Phi[m]=p
P=[int(e in {0,3,8,11,19}) for e in range(20)]
candidates=[m for m,p in Phi.items() if len(p)-1<=19]
for m in candidates:
    q,r=divmonic(P,Phi[m])
    assert r!=[0]
    # The saved certificate also reconstructs q*Phi[m]+r==P exactly.
```

The symbolic PR/HG derivations, cyclic-ring argument and all-order scope are WRITTEN proofs, not machine-checked quantified theorems. An attempted sympy import failed because sympy was absent; no installation occurred. A compact mod-2 irreducibility shortcut was tried, failed its exact criterion and was discarded. An exploratory six-term endpoint mask was not used to claim another cutoff or exclusion. These explorations are disclosed in the JSON and receive no additional theorem credit.

No external executable, solver, native scientific interpreter, compile/test/lint run, proof assistant, independent-model review, git mutation, deletion, publication or scientific launch GO occurred. Finite integer enumeration within the allowed eval kernel DID occur as specified above; this is not a blanket no-computation statement.

## 9. Exact remaining gap and parkable continuation

The full heterogeneous task remains NOT_PROVED. The single required positive input is still an ACTUAL finite raw M containing all sixteen C words, together with all-list UD and factor completeness, for example the accepted GP/Q or residual/Kraft certificate. The negative alternative must exclude every finite raw M, including endpoint supports beyond ESCAPE and all coherent multi-gap choices.

The new algebraic normal form leaves these exact unresolved choices:

1. Choose finite endpoint sets L,R extending the literal start/end exponents and satisfying their cyclic direct factorization, with the forced isolated pure words LIFT. The proof above eliminates only the stated small pure-end supports, not all choices.
2. Choose actual raw delays and crossing words that satisfy every HG_g simultaneously.
3. Most importantly, prove uniqueness AND existence for gap lists containing arbitrarily many positive gaps. Section 5 gives an explicit UD control where steps 1-2 succeed but step 3 fails. No step is licensed to infer this last condition from bivariate identities, Kraft mass alone or a residue realization.

No finite M, universal multi-gap invariant or all-order elimination of the surviving larger endpoint supports has been obtained. The obstruction is mathematical, not a request to launch computation or build a verifier. The fixed-seed one-remaining-length no-go keeps its exact previous scope; this packet neither edits it nor converts it into unrestricted noncompletion. All predecessor packets, parent records and sibling roots remain unchanged.
