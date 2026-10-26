# Shor heterogeneous completion — consolidated written all-run bridge grammar

Observed before creation: **Sun Oct 25 04:55:09 PDT 2026** (`/bin/date`). MathShor, math-5. **WRITTEN ONLY.** Scientific HOLD v2 and parent evidence erratum v7 are binding. No scientific arithmetic interpreter, eval, enumeration, symbolic/numerical program, certificate replay or solver was used for this consolidation. Metadata clocks/hashes and written reasoning only.

**Original existence verdict: NOT_PROVED.** No finite complete extension or unrestricted noncompletion proof is supplied. This is ONE consolidated manuscript after the pure-run, written-roots and joint-two-gap packets, not a fourth isolated subsystem increment. Its new attack is the exact all-run recursion in Section6: it keeps actual bridge words and joint endpoint delays, canonically separates empty and nonempty shared-run continuations, and recovers every earlier subsystem as a specialization. It does not assert that satisfying finitely many subsystems settles the code.

## 1. Literal question, immutable provenance and assurance

Keep the sixteen literal words

```text
C = b{1,a,a^7,a^13,a^14}
    union {a^3,a^8}b{1,a^2,a^4,a^6}
    union a^11 b{1,a,a^2}.
```

The target is a FINITE set M of nonempty raw binary words containing C, with unique decodability for every finite codeword list, and every binary word a factor of some M-product. All added lengths, numbers of b's, pure-a orders and cardinalities remain unrestricted.

Principal source chain, all immutable:

- `proof-RAW-GAP-PARSER-AND-FOUR-A-COMPATIBILITY-v1.md`, SHA-256 `adf92f65c11c0fe03e3941102bf4492979dcb68e493443553b3802c71a26c2bb`: GP and its finite Q interface. Its accepted parent boundary remains `shor-raw-structure-parent-v1.md`.
- `proof-HETEROGENEOUS-PURE-RUN-AND-ONE-GAP-v1.md`, SHA-256 `38328e19b46a88f524b7af2b51654b9d6bf8e7dcf62cba1bdfdd5ce2350cba7f`: prior written pure-run and one-gap representation, subject to the mandatory correction below.
- `proof-HETEROGENEOUS-PURE-RUN-AND-ONE-GAP-ADDENDUM-1-WRITTEN-ROOTS.md`, SHA-256 `ae9567bb6363eafbcbaaaf78346cc6f03ce9117a157266354e7c8185adc515f0`: the direct written root-of-unity proof, replacing reliance on earlier arithmetic observations.
- `parent-HOLD-correction-disclosure-v1.json`, SHA-256 `85521395b7ad128b9b4d6340ae2d13496423f9491f23d26fa406d9150349214c`: all eight earlier scientific eval calls and withdrawal of automatic-admission/verification implications. Parent's erroneous exception is not attributed to owners. No retrospective GO or executable credit is inferred.
- `proof-HETEROGENEOUS-JOINT-BOUNDARY-TWO-GAP-v1.md`, SHA-256 `6532a032aed9e19eef70927c98f07c470d29b2e6d241eef34c7ac16adfde511f`: the five-case coupled three-run identity, consolidated below and generalized to every number of runs.
- `raw-realization-protocol-v1.md`, SHA-256 `544f547ba826076f452d3f478bf4585ecfe9e2da0f2d643f03e79732e568e578`: elementary residual/Kraft proofs and the non-Shor control M0.

The scientific arithmetic JSON is preserved elsewhere as unadmitted observed output. It is NOT a proof premise here. Every algebraic step used below is written. New consolidated bytes and the all-run recursion have NOT received independent review, formal verification or novelty clearance. Prior supplied-proof reviews do not automatically accept this successor.

## 2. Exact raw parsing interface and the pure-run solution

Because b is a codeword, any actual UD M has no other pure-b word. For each a-containing raw word write

```text
b^alpha a b^g1 a ... b^g_(q-1) a b^beta.
```

A free-end parse partitions a-positions into actual labelled words, matches every internal gap, and permits a boundary u|v exactly when its actual b-gap is at least `beta_u+alpha_v`. The surplus uniquely counts intervening b codewords. Outer padding is free, not a new codeword.

**GP:** finite M containing b and no other pure-b word is UD and factor-complete iff every finite nonnegative gap list has exactly one labelled free-end parse. Existence follows by embedding the core with b-margins longer than the largest word; any two parses can be padded to the same raw product, contradicting UD. Conversely a unique parse fixes every a-containing word and every remaining b-count; adding outside b's embeds each core. This is the exact factor-completeness quantifier.

A finite complete M must contain a pure word a^n: without one, an adjacent a-run can contain at most one positive-leading-delay start and one positive-trailing-delay end, or one isolated word, so its parsed length would be bounded. UD permits only one positive pure-a order, since two powers commute and give an ambiguity.

The remaining pure-core words are

```text
start:     b^e a^r,          e,r>=1;
end:       a^s b^d,          s,d>=1;
isolated:  b^e a^q b^d,      e,d,q>=1.
```

For fixed a-length, two different such singleton words cannot coexist, because their free-end parses would differ. At zero b-gap a boundary requires both touching delays0. Thus every pure-run parse consists of an optional start, any number of a^n, and an optional end, or a single isolated word.

With L,R including an empty ENDPOINT marker0 (never an empty codeword), and H counting isolated lengths, define

```text
L(z)=1+sum_start z^r,    R(z)=1+sum_end z^s,
Delta(z)=1-z^n,          S_n(z)=1+...+z^(n-1).
```

Unique parsing of every pure a-run is exactly

```text
L(z)R(z)+Delta(z)H(z)=S_n(z).                     (PR)
```

It has a complete algebraic solution. Modulo z^n-1, L and R directly factor the cyclic residues. For each residue k, its unique ACTUAL sum is `r_k+s_k=k+n h_k`, h_k>=0. The residue0 pair is the two empty endpoints, so h_0=0. The unique isolated-word polynomial is

```text
H(z)=sum_(0<=k<n) sum_(0<=j<h_k) z^(k+jn).        (LIFT)
```

Conversely any finite nonnegative endpoint sets containing0 with that direct cyclic factorization produce this H and satisfy PR. Each actual nonzero endpoint/isolated exponent may be given positive raw b-delays, but their positive-gap compatibility is still unproved. No cyclic-factorization-to-raw-code converse is assumed.

## 3. Joint endpoint matrix and actual bridge data

Choose a finite delay index set0,...,D containing all outer b-delays of the hypothetical finite M; no universal bound on D is imposed. Split the pure polynomials by ACTUAL delays:

```text
L_0=R_0=1;
L_e=sum z^r for b^e a^r words,             e>0;
R_d=sum z^s for a^s b^d words,             d>0;
H_ed=sum z^q for b^e a^q b^d words,        e,d>0,
```

and H_ed=0 when either index is0. Define P(z), with row=initial leading delay and column=final trailing delay, by

```text
P_ed(z)=L_e(z)R_d(z)/Delta(z)+H_ed(z)-1_(e=d=0). (P)
```

This counts NONEMPTY pure-run parses jointly at both ends. In particular `P_00=z^n/(1-z^n)`. The final and initial marginals are its column and row sums, respectively, but must not be treated as independent couplings.

Let Z be the matrix with its only1 at(0,0), let 1 be the all-ones column, and let

```text
(T_g)_(d,e)=1_(d+e<=g),       g>=1,
A(z)=I+P(z)Z,                B(z)=I+ZP(z).        (AB)
```

T_g counts the unique legal positive-gap boundary. A and B attach an optional pure prefix/suffix at ZERO gap: a nonempty attachment requires both touching delays0.

For every positive-gap word `gamma=(g1,...,gj)`, define the polynomial matrix W_gamma(x0,...,xj) by assigning each ACTUAL raw word

```text
b^e a^i0 b^g1 a^i1 ... b^gj a^ij b^d,   all i_l>=1,
```

the monomial `x0^i0 ... xj^ij` in entry(e,d). Different raw labelled words remain distinct. A finite M has only finitely many nonzero W_gamma. These are not freely chosen signed array corrections: a proposed positive answer must bind them to actual literal words and their delays.

## 4. One positive gap and the joint two-gap identity

For one gap g, all joint parses are exactly

```text
D_g(x,y)=P(x)T_gP(y)+A(x)W_g(x,y)B(y).           (G1)
```

The first term crosses no word over the gap; the second has the unique crossing word and optional pure attachments. Taking all-ones external endpoints gives the earlier HG_g scalar identity. It is equivalent to unique parsing for every pair of positive run lengths at this g, not global completeness.

For two gaps g,h define `C_g=A(x)W_g(x,y)B(y)`. Then every three-run core has exactly the five disjoint cases

```text
D_(g,h)(x,y,z)
 = P(x)T_gP(y)T_hP(z)
   + C_g(x,y)T_hP(z)
   + P(x)T_gC_h(y,z)
   + A(x)W_g(x,y) [Z/Delta(y)] W_h(y,z)B(z)
   + A(x)W_(g,h)(x,y,z)B(z).                    (G2)
```

These are respectively: no crossing; first only; second only; two distinct crossing words; one word crossing both. At most one actual word can cross a fixed positive gap, so the cases exhaust and do not overlap.

The middle zero-gap join of TWO distinct bridge words is

```text
Z+ZP(y)Z=Z/(1-y^n).                            (JOIN)
```

Both touching delays must be0, and intermediate both-zero-endpoint pure words can only be a^n. There is ONE geometric factor, not independent suffix and prefix factors: choosing an arbitrary cut in that same a^n chain would overcount a raw parse.

A word with four or more a-runs cannot fit any of these three-run cores. Therefore a negative coefficient in the target-minus-first-four-terms defect is already an irreparable UD ambiguity; a nonzero defect requires actual W_(g,h) words with the prescribed pure attachments. Longer/more-complicated words cannot repair a three-run core. This is an exact conditional obstruction for arbitrary heterogeneous data, not a proof that all Shor data fail.

## 5. Why independent one-gap solutions cannot settle the target

The non-Shor control

```text
K0={aa,b,abb,aaaba,baba}
```

is a subset of the complete UD set

```text
M0={aa,b,abb,aaaba,baba,abbaba,abaaba}.
```

The named raw-realization protocol proves M0 by substituting a complete prefix code into an abstract suffix code; its exact Kraft sum is1. K0 is UD but has Kraft31/32, hence is incomplete.

For K0 the only nonzero pure matrix entries are

```text
P_00=z^2/(1-z^2),    P_02=z/(1-z^2),
```

and the only one-gap bridge entries are

```text
(W_1)_00=x^3 y,      (W_1)_10=x y.
```

The earlier written one-gap identity shows all pure runs and every one-positive-gap core are uniquely parsed: at g=1 the cleared defect `xy(1+y)` equals

```text
(1+y)x^3y+(1-x^2)(1+y)xy,
```

and for g>=2 all pure boundaries are legal and no bridge is needed.

Yet `a b^2 a b a` is missing as a free-end core. Singleton abb parses fail at the final gap1; there is no gap2 bridge; a baba bridge at the second gap requires preceding gap at least2+1=3 rather than2. The actual M0 word abbaba supplies this three-run correction. Its other extra word abaaba is a distinct bridge with gaps(1,1). This is a written raw-word control, not a replay or a Shor seed proposal.

## 6. New consolidated attack: exact recursion for EVERY positive-gap chain

The pairwise formula can be closed without losing shared-run endpoint data. This gives one all-run grammar rather than another isolated next-gap note.

For a positive-gap word `gamma=(g1,...,gk)`, let

```text
D_gamma(x0,...,xk)
```

be the JOINT endpoint matrix counting all labelled free-end parses of cores

```text
a^p0 b^g1 a^p1 ... b^gk a^pk,       all p_i>=1.
```

For the empty gap word define

```text
D_empty(x)=P(x).                                  (R0)
```

For each1<=j<=k define the continuation after a word that crosses the FIRST j gaps. If j=k, its optional suffix is

```text
E_k=B(x_k).                                      (R1)
```

If j<k, the exact continuation is

```text
E_j
 = Z D_(g_(j+1),...,g_k)(x_j,...,x_k)
   + T_(g_(j+1))
       D_(g_(j+2),...,g_k)(x_(j+1),...,x_k).       (R2)
```

The first term means a NONEMPTY remaining suffix of the shared run j. Its boundary to the previous bridge is gap0, forcing both delays0 via Z. The second term means NO a remains in shared run j: the next actual boundary is the positive gap g_(j+1), so T performs its exact delay/surplus test. These alternatives are disjoint. In the second term an empty suffix of the gap WORD still means the nonempty final a-run P, by R0; it never means an empty codeword.

The full recursion is

```text
D_(g1,...,gk)(x0,...,xk)
 = P(x0) T_g1 D_(g2,...,gk)(x1,...,xk)
   + A(x0) sum_(j=1)^k
        W_(g1,...,gj)(x0,...,xj) E_j.             (R3)
```

Every D on the right has fewer positive gaps, so this defines the matrix coefficient series inductively from actual finite raw data.

### Proof of R3, with every empty/nonempty case retained

If no actual word crosses the first gap, all a's of the first run have a nonempty pure-run parse P(x0). Its final delay meets the first suffix word through T_g1. The remaining core is exactly the first term of R3.

Otherwise the first gap has a UNIQUE crossing word. Suppose it crosses precisely the first j positive gaps. It is an actual word in W_(g1,...,gj), preceded by an optional pure prefix of run0; A(x0) gives exactly that prefix and its required zero-gap join. A crossing word cannot skip a middle positive gap, because its raw letters form one interval.

If it reaches the last run, only an optional pure suffix is left: R1. Otherwise it ends inside run j. There is either a positive number of unassigned adjacent a's in that run, giving the zero-gap continuation in the first term of R2, or none, giving the next positive-gap boundary in its second term. A raw parse determines which case occurred and determines j, its actual crossing word, prefix and continuation uniquely. Conversely every matrix product listed gives exactly a legal raw parse. Thus no path, raw label, b-surplus or continuation is discarded or multiply counted.

This proves R3 for every finite positive-gap chain in WRITING. There is no run-length cutoff and no assumption that added words have a common length or at most two/three a-runs.

### Exact agreement with the two-gap gluing correction

At k=1, R3 gives G1. At k=2, expand R2 for j=1. The two terms after the first bridge are

```text
Z[P(y)T_hP(z)+A(y)W_h(y,z)B(z)] +T_hP(z).
```

Collecting the no-second-bridge pieces gives `B(y)T_hP(z)`. The two-bridge piece contains

```text
Z A(y)=Z+ZP(y)Z=Z/Delta(y),
```

exactly JOIN. The j=2 term is the single two-gap bridge, while the first R3 term supplies the no-first-bridge alternatives. This recovers ALL five G2 cases and shows precisely why the all-run continuation cannot be replaced by a product of one-gap marginals.

### Full heterogeneous completion condition and its limit

For every k and every positive-gap word gamma, require

```text
1^T D_gamma(x0,...,xk)1
    = product_(i=0)^k x_i/(1-x_i).                (ALL)
```

For k=0 this is PR. For k=1 it is HG; for k=2 it is the joint condition. For arbitrary k, each coefficient says exactly one parse of the actual run lengths. Every a-containing binary core has a unique decomposition into adjacent a-runs separated by positive b-gaps. Thus, by GP, ALL for every gamma is NECESSARY AND SUFFICIENT for a finite candidate M to be UD and factor-complete, once b/no-other-pure-b and the actual-word binding above are enforced.

Induction on R3 shows that every D_gamma has denominator dividing

```text
product_i (1-x_i^n).
```

No variable acquires two independent pure-chain denominators at a shared run; R2/ JOIN canonically make the split. Hence each particular ALL identity is a finite integer polynomial identity after clearing those denominators.

This is an exact all-order CONDITION, not its solution. A finite M gives finitely many W_gamma, but ALL still quantifies over arbitrarily long gap words; checking any finite collection of k would not establish it. The problem is not made easier by silently declaring the recursion itself a completion.

## 7. A finite witness gate remains available, not yet instantiated

For any actual finite candidate M, take a bound B_* at least every internal a-gap and every sum of touching outer delays. Replace each gap larger than B_* by one symbol infinity. Every internal equality and boundary comparison is then unchanged. In the run grammar, W_gamma containing infinity vanishes and T_infinity permits every outer-delay pair. The gap alphabet is finite, but word length remains unbounded.

The existing raw GP automaton has states(w,j) for the j-th a of a labelled word, its internal transitions matching actual gaps and its final-to-start boundary transitions satisfying the delay inequality. Initial/final indicators I,F count exactly the free-end parses. A genuine finite witness can provide rational V,z,T_c with

```text
nu=V z,
diag(A_c,1)V=V T_c for every gap symbol c,
(I,-1)V=0,
nu=(F;1).                                       (Q)
```

These identities prove every accepting count is1 by induction on gap words. Conversely the rational span of all orbit columns of nu supplies such data whenever all counts are1. This is the already accepted finite invariant-subspace witness interface, not a newly built program or a confirming replay.

The all-run recursion is a written elimination of zero-gap repetitions exposing the ACTUAL bridge compatibility that such a witness must satisfy. No finite M, V or universal obstruction has been supplied. No source/input-pinned scientific GO exists.

## 8. Restricted pure-end support obstruction, with a purely written certificate

This structural result is included to keep the complete current boundary in ONE manuscript. It is not another order search or a negative answer to the original target.

Let I={0,3,8,11} be the literal end exponents (including the empty endpoint marker) and let S={1,2,4,6,7,12,13,14}. For each s in S there are literal C words p_s and p_s a^s; choose b for s1,7,13,14, a^3b for s2,4,6, and ba for s12. For i in I, a^i b is in C. A proposed end word `w=a^(i+s)b^beta` gives the two distinct lists

```text
(p_s a^s)(a^i b)(b)^(beta-1)=(p_s)(w), beta>=1.
```

Thus i+s is forbidden. Through25 these exclude exactly

```text
1,2,4,5,6,7,9,10,12,13,14,15,16,17,18,20,21,22,23,24,25.
```

Each exclusion has the displayed actual-word witness, not a residue-only collision. Therefore if all end exponents were at most25, R would be one of

```text
R4=1+z^3+z^8+z^11,
R5=1+z^3+z^8+z^11+z^19.
```

The exact identity `R4(1-z^3+z^6)=1+z^8+z^9+z^17` rules out R4: multiplying the cyclic tiling relation preserves S_n, but its coefficient at22 includes BOTH forced L residues13 and14, so is at least2 instead of1, for every n.

Here is a self-contained written root certificate for R5, independent of the earlier unadmitted36-remainder computation. Suppose a primitive m-th root zeta zeros R5.

If the five indexed terms form a minimal zero subsum, m has no square prime factor: for p²|m, grouping exponents modulo p in the degree-p basis over Q(zeta^p) makes each group vanish; minimality forces all exponents into one group, impossible since0,3,8 occur. Nor can a prime p>=7 divide the now-squarefree m: grouping by a primitive p-th root over Q(zeta_(m/p)) gives a relation with fewer than p nonempty groups. Its minimal polynomial is1+...+x^(p-1), so the empty group forces all group coefficients zero; minimality again contradicts the relatively prime exponent differences. These are the elementary cyclotomic degree-ratio/minimal-polynomial imports. Hence m divides30.

The eight candidate orders are excluded in WRITING by the following nonzero reductions:

```text
m1:   5;
m2:  -1;
m3:  -zeta;
m5:   zeta^2(zeta-1);
m6:   zeta;
m10:  2+zeta^2-zeta^3, degree3 below phi(10)=4;
m15:  zeta^7-zeta^6-zeta^5+2zeta^4, degree7 below phi(15)=8;
m30:  eta^7+eta^6-eta^5-2eta^3+2eta, eta=-zeta primitive15.
```

The last two use `Phi_15=z^8-z^7+z^5-z^4+z^3-z+1` and `zeta^10=-zeta^5-1`; the last is the same reduction with eta=-zeta. Nonzero polynomials below the relevant minimal degree cannot vanish.

If the five-term relation is not minimal, it must split into an opposite pair and a zero-sum triple: a one-term zero sum is impossible, and a four-term zero sum would leave one. Three unit roots sum zero only as a rotated cube-root triangle. For nine of the ten exponent triples from{0,3,8,11,19}, the gcd of the two differences from the smallest exponent is1, forcing m=3, which permits no opposite pair. The sole exception is{3,11,19}, whose step8 would make zeta^8 a primitive cube root, while its complementary pair{0,8} demands zeta^8=-1. Contradiction.

Thus R5 has no root of unity. It is invertible modulo z^n-1 for every n, so the cyclic equation L R5=S_n would have the unique rational solution L=S_n/5, impossible for the actual0/1 endpoint polynomial with constant coefficient1.

Both small masks are excluded. Every finite completion must contain an actual word

```text
a^ell b^beta,       ell>=26, beta>=1.             (ESCAPE)
```

This is an obstruction to the stated bounded pure-END support architecture, allowing arbitrary heterogeneous other words. It is not a new pure-a order bound, not all-order noncompletion, and not a license to iterate an old seed-growth theorem after changing its base.

## 9. Exact remaining obligation and consolidated disposition

The all-run grammar closes the REPRESENTATION gap between isolated HG equations and arbitrary positive-gap chains. It does not close the EXISTENCE gap. A positive answer must still supply actual finite raw words and satisfy every ALL/Q condition; a negative answer must eliminate every possible finite endpoint/delay/bridge choice, including larger pure-end supports and every surviving crossing escape.

The following remain explicitly unproved:

- a finite literal M containing all sixteen C words with the required universal all-list/factor certificate;
- a coherent finite nonnegative actual-word realization of R3/ALL at every positive-gap word;
- an invariant forcing a contradiction for every such finite realization;
- unrestricted Shor noncompletion, novelty, formal verification or independent acceptance of this consolidated manuscript.

Earlier homogeneous-tail and fixed-seed one-remaining-length no-go results keep their exact scopes. Not every possible completion contains the optional seed, and no automatic infinite-growth iteration follows. The non-Shor controls and the restricted support obstruction are method boundaries, not substitute solutions.

This manuscript is the ONE current consolidated written attack: pure-run algebra, joint delay data, canonical shared-run continuation, all-run grammar and exact finite witness interface. Predecessors and parent/sibling records remain unchanged. Any further scientific computation still requires a separate exact source/input-pinned named GO; no interpreter is authorized by this written consolidation.
