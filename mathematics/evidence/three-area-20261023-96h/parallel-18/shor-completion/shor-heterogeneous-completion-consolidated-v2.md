# Shor heterogeneous completion — consolidated all-run system and internal-pole obstruction

Observed before creation: **Sun Oct 25 05:21:43 PDT 2026** (`/bin/date`). MathShor, math-5. **WRITTEN ONLY.** No scientific interpreter, eval, enumeration, symbolic/numerical program, certificate replay or solver was used. Metadata clocks/hashes/source reads and written reasoning only. HOLD v2 and parent erratum v7 remain binding.

**Full Shor target: NOT_PROVED.** This is ONE consolidated primary continuation after the assigned v37-A review, not a new standalone subsystem note. It restates the operative raw-word data, exact all-run recursion and finite witness gate, then derives a triangular obstruction that eliminates unknown higher-arity bridge words before choosing their lengths: every internal pure-run pole must already cancel in the lower-arity data. It also identifies the exact finite-arity stabilization statement a full negative answer would need. No actual finite Shor completion or contradiction for all lower data has been obtained.

## 1. Literal target, immutable chain and current assurance

The target code is exactly

```text
C = b{1,a,a^7,a^13,a^14}
    union {a^3,a^8}b{1,a^2,a^4,a^6}
    union a^11 b{1,a,a^2}.
```

We seek a FINITE set M of nonempty raw words containing C, uniquely decodable on every finite codeword list, with every binary word a factor of some M-product. Word lengths, numbers of b's, pure-a order and cardinality remain unrestricted.

Pinned predecessors, all unchanged:

- `proof-RAW-GAP-PARSER-AND-FOUR-A-COMPATIBILITY-v1.md`, SHA-256 `adf92f65c11c0fe03e3941102bf4492979dcb68e493443553b3802c71a26c2bb`: exact GP/free-end parsing and finite invariant-subspace Q interface, at the parent boundary in `shor-raw-structure-parent-v1.md`.
- `shor-heterogeneous-completion-consolidated-v1.md`, SHA-256 `d249dd4129944f62beb73c78783bfee7a2e2feef155a1c941ffd3158cb4cb9a9`: full written source chain, all-run recursion, non-Shor control and written restricted pure-end support obstruction.
- `proof-HETEROGENEOUS-PURE-RUN-AND-ONE-GAP-ADDENDUM-1-WRITTEN-ROOTS.md`, SHA-256 `ae9567bb6363eafbcbaaaf78346cc6f03ce9117a157266354e7c8185adc515f0`: direct WRITTEN root-of-unity certificate, not dependent on the earlier evaluated remainders.
- `parent-HOLD-correction-disclosure-v1.json`, SHA-256 `85521395b7ad128b9b4d6340ae2d13496423f9491f23d26fa406d9150349214c`: every prior scientific eval call and the withdrawal of automatic-admission/verification implications. The parent originated the erroneous permission; no retrospective GO or executable credit is asserted.
- `raw-realization-protocol-v1.md`, SHA-256 `544f547ba826076f452d3f478bf4585ecfe9e2da0f2d643f03e79732e568e578`: elementary residual/Kraft proofs and the non-Shor complete UD control M0.

This v2 is an additive consolidated successor, not an edit or retroactive acceptance of v1. The new triangular/pole theorems are written candidates and have not received independent reconstruction, formal verification or novelty clearance. No reviewer verdict automatically transfers to these new bytes. Earlier unadmitted arithmetic outputs are not proof premises.

## 2. The exact raw gap criterion and pure-run elimination

Since b belongs to C, any UD M has no other pure-b word. For each a-containing word record its actual leading/trailing b-delays and its internal gap list between consecutive a's. A free-end parse partitions the a-positions into actual labelled words, matches their internal gaps, and permits a boundary u|v precisely when the actual gap is at least `beta_u+alpha_v`. The surplus is a UNIQUE number of intervening b codewords.

**GP:** a finite M with b and no other pure-b word is UD and factor-complete iff EVERY finite nonnegative gap list has exactly one free-end parse. Long b-padding gives existence from factor-completeness and converts two free-end parses into an actual raw ambiguity. Conversely a unique parse fixes all a-containing words and remaining b-counts, while outside b-padding embeds every core. This is the literal book quantifier, not prefix completeness or membership of every word in M*.

A finite complete code has a pure word a^n: otherwise every zero-gap parse has at most one start and one end or one isolated word, so its adjacent a-length is bounded. UD allows only one positive pure-a order. The other pure-core words are

```text
start:      b^e a^r,       e,r>=1;
end:        a^s b^d,       s,d>=1;
isolated:   b^e a^q b^d,   e,d,q>=1.
```

At zero gap both touching delays must be0. Thus all pure-run parses are an optional start, any number of a^n and an optional end, or a singleton isolated word.

Let the finite polynomials L,R include the empty ENDPOINT marker0, not an empty codeword, and let H record isolated a-lengths. Set

```text
Delta(z)=1-z^n,       S_n(z)=1+z+...+z^(n-1).
```

Unique parsing of every pure run is exactly

```text
L(z)R(z)+Delta(z)H(z)=S_n(z).                    (PR)
```

Its complete solution is the direct cyclic factorization `LR=S_n mod z^n-1`. Each residue k has one actual nonnegative sum `r_k+s_k=k+n h_k`. Then h_0=0 and

```text
H(z)=sum_(0<=k<n) sum_(0<=j<h_k) z^(k+jn).       (LIFT)
```

Conversely these lifted deficits give PR. Positive delays remain actual unknown labels; cyclic factorization alone is NOT a raw realization theorem.

## 3. Joint-delay matrix and actual bridge arity

Choose a finite delay index set0,...,D for a hypothetical finite M, with no universal bound on D. Split the pure polynomials by the actual delays:

```text
L_0=R_0=1;
L_e(z)=sum z^r for actual b^e a^r words,        e>0;
R_d(z)=sum z^s for actual a^s b^d words,        d>0;
H_ed(z)=sum z^q for actual b^e a^q b^d words, e,d>0,
```

with H_ed=0 if either index is0. The nonempty pure-run joint parse matrix is

```text
P_ed(z)=L_e(z)R_d(z)/Delta(z)+H_ed(z)-1_(e=d=0). (P)
```

Its row is the actual initial delay and its column the actual final delay. In particular `P_00=z^n/Delta(z)`. Every entry is a nonnegative formal count series, although this rational expression includes subtraction of the wholly empty parse. Let Z have its only1 in position(0,0), let 1 be the all-ones column, and define

```text
(T_g)_(d,e)=1_(d+e<=g),      g>=1,
A(z)=I+P(z)Z,               B(z)=I+ZP(z).        (AB)
```

A/B attach optional pure prefixes/suffixes at zero b-gap. Both touching delays there must be0.

For a positive-gap word `gamma=(g1,...,gk)`, define the polynomial matrix W_gamma(x0,...,xk) by actual words

```text
b^e a^i0 b^g1 a^i1 ... b^gk a^ik b^d,   i_j>=1,
```

contributing `x0^i0...xk^ik` in entry(e,d). Call k the bridge ARITY: the number of positive internal b-gaps, not raw length or number of individual a's. Distinct labelled words remain distinct. Finite M has finitely many nonzero W_gamma and a finite maximum bridge arity, but neither is bounded in advance.

These matrices are literal word data, not freely chosen Parikh counts or signed corrections. Zero/positive endpoint aggregation used below does not discard the actual positive delay magnitudes needed in later joint products.

## 4. Exact recursion for every positive-gap chain

Let D_gamma(x0,...,xk) count joint-endpoint free-end parses of all cores

```text
a^p0 b^g1 a^p1 ... b^gk a^pk,     p_i>=1.
```

For no positive gap,

```text
D_empty(x)=P(x).                                  (R0)
```

For1<=j<=k, a word crossing precisely the first j gaps has continuation

```text
E_k=B(x_k)                                       (R1)
```

when j=k. For j<k it has the disjoint continuation alternatives

```text
E_j=Z D_(g_(j+1),...,g_k)(x_j,...,x_k)
    +T_(g_(j+1)) D_(g_(j+2),...,g_k)(x_(j+1),...,x_k). (R2)
```

The first term has a NONEMPTY remaining suffix of shared run j and a zero-gap join; Z enforces both touching delays0. The second has NO a remaining in that run, so the next actual boundary is the positive gap g_(j+1). An empty gap-word suffix still means the final NONEMPTY pure run P, never an empty codeword.

The full all-run recursion is

```text
D_(g1,...,gk)
 =P(x0)T_g1 D_(g2,...,gk)(x1,...,xk)
  +A(x0) sum_(j=1)^k W_(g1,...,gj)(x0,...,xj) E_j. (R3)
```

Proof: either no word crosses the first gap, giving a full pure first-run parse and the T_g1 boundary, or a unique actual word crosses it. Such a word crosses a consecutive prefix of the gaps, determining j and an actual W-prefix label. Its optional first-run prefix is A. After it ends, the shared-run remainder is either nonempty or empty, exactly R2, with R1 at the last run. These cases are exhaustive, disjoint and recover every raw parse, including every b-surplus and endpoint label. Every D on the right has fewer positive gaps, so the definition is inductive.

For one gap the formula is

```text
D_g=P(x)T_gP(y)+A(x)W_g(x,y)B(y).                (G1)
```

For two gaps it gives the five cases: no crossing; first only; second only; two separate bridges; one bridge crossing both. The two separate bridges are glued through

```text
Z A(y)=Z+ZP(y)Z=Z/Delta(y).                     (JOIN)
```

Only a^n words can lie between their two zero-delay endpoints. ONE geometric factor is required, not two independent suffix/prefix factors that would count arbitrary cuts in the same pure chain. This recovers the earlier exact joint-two-gap theorem.

Induction in R3 shows that all entries of D_gamma have denominator dividing

```text
ProductDelta_gamma=product_(i=0)^k Delta(x_i).    (DEN)
```

No variable gets two independent pure-chain denominators at a shared run.

Let

```text
Target_gamma=product_(i=0)^k x_i/(1-x_i).
```

Then the FULL heterogeneous condition is

```text
1^T D_gamma 1=Target_gamma    for every positive-gap word gamma,
```

including the empty word. Each coefficient demands exactly one labelled parse of the actual run lengths. Every a-containing core has a unique adjacent-run decomposition, so these identities, plus the actual-word/b-only binding, are equivalent to GP and hence to UD/factor-completeness. They are full conditions, not their solution for Shor.

## 5. NEW triangular bridge residual theorem

Fix k>=1 and a positive-gap word gamma=(g1,...,gk). Separate the j=k term of R3. Define Lower_gamma as

```text
Lower_gamma
 =P(x0)T_g1 D_(g2,...,gk)(x1,...,xk)
  +A(x0) sum_(j=1)^(k-1)
        W_(g1,...,gj)(x0,...,xj) E_j.             (LOW)
```

Every W used here has arity strictly less than k. The same is true inside each suffix D: its gap-word length is at most k-1. Consequently Lower_gamma is determined COMPLETELY by pure data and actual bridges of smaller arity. It is independent of every unknown k-gap word and of all higher-arity words.

Define the scalar forced deficit and its integer polynomial numerator

```text
F_gamma=Target_gamma-1^T Lower_gamma 1,
N_gamma=ProductDelta_gamma * F_gamma.             (DEF)
```

The denominator bound DEN makes N_gamma an integer polynomial. The k-gap completion condition is EXACTLY

```text
F_gamma=1^T A(x0) W_gamma(x0,...,xk) B(xk) 1.     (TRI)
```

Thus the effective contribution needed from the entire k-gap bridge class is already uniquely prescribed by LOWER-ARITY actual data. This does not determine each raw endpoint label, but it is more than an arbitrary polynomial-correction problem.

The right side is a nonnegative formal count series. Therefore:

1. A NEGATIVE coefficient in F_gamma proves that the lower words already have multiple parses; no new word of any length/arity can repair UD.
2. A NONZERO F_gamma cannot be repaired with W_gamma=0; some actual k-gap bridge is needed. Higher-arity words cannot fit a core with only k positive gaps.
3. F_gamma must have the precise finite actual-word envelope TRI, not merely nonnegative coefficients. The actual positive delay labels chosen for W_gamma become joint lower data at the next stages.

These are universal conditional obstructions for fixed actual lower data. No Shor lower-data family has been universally eliminated by them here.

## 6. NEW internal-pole cancellation obstruction

The unknown W_gamma is a POLYNOMIAL in all run variables, since it represents finitely many actual words. A and B contribute denominators only in the FIRST and LAST run variables. Therefore TRI permits NO surviving pole in any INTERNAL variable x1,...,x_(k-1), regardless of how long newly proposed k-gap words are.

Set

```text
Abar(x)=Delta(x)A(x),    Bbar(z)=Delta(z)B(z).
```

Clearing TRI gives the exact identity

```text
N_gamma
 = [product_(i=1)^(k-1) Delta(x_i)]
       *1^T Abar(x0) W_gamma(x0,...,xk) Bbar(xk)1. (POLE)
```

### Theorem IP: eliminating arbitrary new bridge lengths

For ANY finite completion extending the specified actual pure/lower-arity data, the lower-data polynomial N_gamma MUST be divisible in the integer polynomial ring by

```text
product_(i=1)^(k-1) (1-x_i^n).                    (IP)
```

If that divisibility fails, NO choice of finitely many k-gap words, arbitrary lengths and arbitrary heterogeneous outer delays can repair the core subsystem. Nor can any still-higher-arity word help. The obstruction is already in the lower actual data.

Proof is POLE. It does not assume a guessed upper bound on the new word lengths. Distinct-variable Delta factors are primitive and pairwise coprime; their product condition is equivalently simultaneous individual divisibility. Over characteristic0, each is squarefree, so one may also state the condition as vanishing identically in the OTHER variables whenever an internal x_i is ANY n-th root of unity. Evaluating only x_i=1, only a scalar mass, or only all variables equal would not be the same condition.

No root evaluations or polynomial divisions were executed for this theorem. It is a written algebraic elimination argument.

### Exact endpoint envelope after pole cancellation

Suppose IP holds and write

```text
Q_gamma=N_gamma / product_(i=1)^(k-1) Delta(x_i).
```

Let L=sum_e L_e and R=sum_d R_d, with their empty endpoint markers. The row `1^T Abar(x0)` has component L(x0) at endpoint0 and Delta(x0) at every positive endpoint. The column `Bbar(xk)1` analogously has R(xk) at0 and Delta(xk) elsewhere. This follows directly by summing P's actual final/initial zero-delay profiles.

Grouping actual W words by zero/positive endpoint classes gives

```text
Q_gamma
 =L(x0)R(xk) W_00
  +L(x0)Delta(xk) W_0+
  +Delta(x0)R(xk) W_+0
  +Delta(x0)Delta(xk) W_++.                       (ENV)
```

Each W-class is a finite NONNEGATIVE integer polynomial bound to actual raw words. Positive delay MAGNITUDES disappear from this one free-end envelope but remain necessary joint labels for future Lower polynomials. They may not be discarded from the finite-code construction.

ENV is the remaining finite algebraic selection problem at this arity. It is not enough for Q_gamma to be an arbitrary signed decomposition or to have a correct scalar total. IP is necessary, not by itself sufficient for ENV or global completion.

### Forced internal run-length support

Because the first/last attachment factors involve no internal run variable, a nonzero internal-run coefficient of F_gamma must come from an actual W_gamma word with exactly that vector of internal run lengths. Conversely any such actual word contributes a nonnegative formal series there and cannot cancel against another word.

After IP, Q_gamma is a polynomial in the internal variables. Multiplication/division by the two endpoint Delta factors is invertible as a formal series and cannot change whether a fixed INTERNAL coefficient is identically zero. Thus its internal monomial support gives the exact internal run-length vectors that a k-gap bridge realization MUST use, and forbids all vectors outside it. In particular it bounds internal run lengths for these new words from lower data, without bounding their first/last a-runs or their positive b-delays.

This is a support constraint on actual k-gap words, not a new finite search admission or an implemented producer.

## 7. Control: pole cancellation can pass while bridge words are still needed

Use the non-Shor UD incomplete code

```text
K0={aa,b,abb,aaaba,baba}.
```

Its complete UD control M0 adds abbaba and abaaba, at the named raw-realization import. K0 has pure order2, L=1,R=1+z. Its one-gap matrices are `(W_1)_00=x^3y` and `(W_1)_10=xy`; all other one-gap W vanish. It parses every pure run and every one-positive-gap core, but fails a two-gap core. Its Kraft is31/32, not1.

The two extra M0 words both have three a-runs and zero outer delays:

```text
abbaba:   gamma=(2,1), W_gamma=xyz;
abaaba:   gamma=(1,1), W_gamma=xy^2z.
```

M0 and K0 have identical lower-arity data, so their Lower_gamma agrees at k=2. By the complete UD M0 import and TRI, the required deficits for K0 are exactly

```text
F_(2,1)=xyz(1+z)/[Delta(x)Delta(z)],
F_(1,1)=xy^2z(1+z)/[Delta(x)Delta(z)],
```

with Delta(w)=1-w². Thus the corresponding numerators have the factor Delta(y); IP PASSES. The quotient fixes middle run length1 in the first correction and2 in the second. Actual finite three-run words nevertheless remain necessary.

These are written consequences of the imported literal M0 and the exact recurrence, not an interpreter replay. They demonstrate why IP is not promoted to a completion theorem: passing a pole test does not supply an actual bridge envelope, compatibility at later arities or a full Shor witness.

## 8. Finite-arity stabilization: the exact negative target

Every actual finite code M has a maximum bridge arity r. For every gap word gamma longer than r, W_gamma=0, so TRI requires

```text
F_gamma=0, equivalently N_gamma=0.                (STAB)
```

This is eventual stabilization of the TRIANGULAR DEFICITS, not an automatic word-length growth claim.

Conversely, suppose finite actual raw data have bridge arity at most r, pure data satisfy PR, ENV/TRI holds for each gamma of length at most r with those actual words, and STAB holds for every longer gamma. R3 then gives the full ALL identity at every gap word; GP yields UD and factor-completeness. Thus this is an exact criterion, not a necessary-only residue relaxation.

A genuine all-order NEGATIVE proof could establish the following quantified obstruction:

```text
For EVERY finite actual pure/delay/bridge prefix extending C,
and EVERY proposed finite arity cutoff r,
either a required lower/core condition already fails,
or some gamma of length>r has nonzero N_gamma.
```

That would force bridge arity to escape every finite bound, ruling out every finite M. It would not rely on the invalid automatic iteration of the old critical-gap length argument. But this universal stabilization obstruction is NOT proved here. In particular no assumption that every completion contains the optional mixed seed is introduced.

This states the original unrestricted burden exactly: both the prefix data and the cutoff vary, and every coherent crossing escape must be covered. A demonstration at one fixed prefix or one finite depth would not suffice.

## 9. Finite all-list witness gate and current restricted results

For a given actual finite M, choose a bound on all internal a-gaps and all touching outer-delay sums, and replace larger gap values by one infinity symbol. Every equality/inequality decision is then unchanged. The existing GP automaton has actual word/a-position states, internal gap transitions and final-to-start threshold transitions. An exact finite rational invariant-subspace certificate Q can prove every accepting count1 for the resulting finite gap alphabet:

```text
nu=V z,
diag(A_c,1)V=V T_c for every gap symbol,
(I,-1)V=0,       nu=(F;1).
```

Its converse follows from the span of all orbit columns of nu. This is the already-supported witness language; no M,V or replay is produced here. The bridge/pole system is a written way to constrain the actual data BEFORE such a witness, not a substitute framework declared solved.

The restricted pure-END support theorem from the previous consolidation is retained unchanged: every actual completion contains `a^ell b^beta` with ell>=26,beta>=1. Its direct written certificate uses literal residual collisions to leave only two small endpoint masks, a signed-multiplier contradiction for `1+z^3+z^8+z^11`, and the explicit minimal-subsums/cyclotomic proof that adding z^19 still gives no root-of-unity factor. The mandatory written-roots addendum supplies the full proof; the old evaluated36-remainder output is not a premise. This is NOT a pure-a order bound or unrestricted noncompletion.

Homogeneous-tail and fixed-seed one-remaining-length no-go results retain their original restricted scopes. Neither is a premise that all finite completions have a flat remainder or contain that seed. The non-Shor controls do not constitute a proposed Shor seed addition.

## 10. Consolidated scientific disposition

The new contribution is a WRITTEN triangular elimination principle: actual k-gap bridge requirements are fixed in aggregate by smaller-arity words; all internal pure-run poles must cancel before any new k-gap words can help; the remaining internal run-length support is forced; a finite completion must stabilize these deficits beyond its maximum bridge arity.

No claim is made that the pole tests fail for every possible Shor lower data, that they are independent of every earlier algebraic condition in all subfamilies, or that they solve the remaining endpoint envelope. This is an exact obstruction INTERFACE and a consolidated next attack, not existence-changing progress by itself.

No finite actual Shor M with all-list UD/factor-completeness has been obtained. No universal nonstabilization invariant has been proved. Larger endpoint supports, endpoint-delay labels, nonnegative ENV choices and common-coordinate all-run coherence remain open. All-count identities at finite depths, passing IP, an excluded selected architecture or a scalar Kraft equality cannot be substituted for that missing proof.

This v2 is the ONE current consolidated primary continuation. All predecessor packets and parent/sibling records remain immutable. New independent written reconstruction, formal verification, executable certification and novelty clearance are not performed. Scientific HOLD remains binding with no new GO, and the frozen deadline is unchanged.
