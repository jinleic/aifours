# Joint-boundary gluing: the exact two-positive-gap obstruction

Observed before creation: **Sun Oct 25 04:31:58 PDT 2026** (`/bin/date`). MathShor, math-5. **WRITTEN only.** No scientific interpreter, enumeration, symbolic/numerical program, certificate replay or solver was used. Metadata clocks/hashes and written reasoning only; scientific HOLD v2 and parent erratum v7 remain binding.

This follows completion of the one assigned v30-C written NL242 review. It returns to the primary Shor gap using a materially different representation: JOINT leading/trailing-delay matrices, rather than independent one-gap marginals or another pure-end support cutoff. It supplies an exact coupled obstruction for every three-run core. It does NOT produce a finite complete extension or an unrestricted noncompletion proof.

## 1. Imports and the information lost by the one-gap marginal

Keep the exact literal sixteen-word C and the finite raw gap-parser theorem GP. Relevant immutable inputs are:

- `proof-RAW-GAP-PARSER-AND-FOUR-A-COMPATIBILITY-v1.md`, SHA-256 `adf92f65c11c0fe03e3941102bf4492979dcb68e493443553b3802c71a26c2bb`, Section1 (GP).
- `proof-HETEROGENEOUS-PURE-RUN-AND-ONE-GAP-v1.md`, SHA-256 `38328e19b46a88f524b7af2b51654b9d6bf8e7dcf62cba1bdfdd5ce2350cba7f`, its WRITTEN pure-run classification and one-gap identities only, with the mandatory admission disclosure and written-roots addendum.
- `raw-realization-protocol-v1.md`, SHA-256 `544f547ba826076f452d3f478bf4585ecfe9e2da0f2d643f03e79732e568e578`, Section2, solely for the non-Shor complete UD control M0.

The earlier HG_g equation aggregates pure-run parses into a final-delay profile F_d or an initial-delay profile G_e. For TWO positive gaps, the middle run has to meet a condition at BOTH ends. The two marginals do not tell whether a chosen initial delay and a chosen final delay occur in the SAME pure-run parse. In addition, two bridge words touching the middle run require a canonical zero-gap join; independently attaching suffixes/prefixes would count the same middle pure-word chain several times.

The joint matrix and the zero-gap resolvent below retain exactly these missing data. They are actual raw labelled-parse counts, not independent probability couplings or a relaxation of codeword overlap.

## 2. Joint pure-run matrix

Consider any finite hypothetical raw M containing b, with the previously classified pure-run data. A genuine completion is one such M. Let n be its unique pure-a order, and let all outside b-delays lie in a finite index set `0,...,D`. The index set may be enlarged by unused zero rows; no universal bound on D is assumed.

Split the pure-core polynomials by their actual delays:

```text
L_0(z)=1, R_0(z)=1;
L_e(z)=sum z^r over actual b^e a^r words,       e>0;
R_d(z)=sum z^s over actual a^s b^d words,       d>0;
H_ed(z)=sum z^q over actual b^e a^q b^d words, e,d>0.
```

Set H_ed=0 if either index is0. Here the isolated word has one adjacent a-run; the pure word a^n is treated by the geometric series, not by H. Let `Delta(z)=1-z^n`.

Define the matrix P(z), with row e=actual initial leading delay and column d=actual final trailing delay, by

```text
P_ed(z)=L_e(z) R_d(z)/Delta(z)+H_ed(z)
        -1_(e=0,d=0).                               (J0)
```

This counts NONEMPTY pure-run free-end parses jointly by BOTH endpoint delays. The proof is the same raw zero-gap classification: optional start, any number of a^n, optional end, or one isolated word. Subtracting1 removes only the wholly empty parse. In particular

```text
P_00(z)=z^n/(1-z^n).
```

Every matrix entry is a nonnegative formal series when read as a count. Denote by Z the rank-one coordinate projector with its only1 in position(0,0), and let 1 be the all-ones column vector. The earlier marginals are exactly

```text
F_d(z)=sum_e P_ed(z),
G_e(z)=sum_d P_ed(z).
```

Thus no new freedom in the marginals is introduced.

For a positive b-gap g, define the 0/1 boundary matrix

```text
(T_g)_(d,e)=1 if d+e<=g, else0.                    (J1)
```

This is precisely the actual b-surplus test; a legal boundary has a UNIQUE number `g-d-e` of intervening b codewords. The code cannot have another pure-b word, because b itself already gives its factorization.

## 3. Actual bridge matrices and zero-gap attachments

For each positive g, let `W_g(x,y)` be the polynomial matrix whose (e,d) entry sums `x^i y^j` over ACTUAL raw words

```text
b^e a^i b^g a^j b^d,        i,j>=1.
```

For positive g,h, let `W_(g,h)(x,y,z)` similarly count actual words

```text
b^e a^i b^g a^j b^h a^k b^d,   i,j,k>=1.
```

Different raw words are retained as different labels, even if a chosen aggregation agrees. These matrices are not arbitrary signed correction terms.

The optional pure-run prefix/suffix attachment matrices are

```text
A(z)=I+P(z)Z,       B(z)=I+ZP(z).                  (J2)
```

For example, a nonempty prefix ending at zero gap can meet a bridge only if the prefix's final delay AND the bridge's initial delay are0. This is exactly the term PZ; I means no prefix. The right attachment is the dual ZP.

Consequently the joint profile of parses crossing ONE positive gap g in a single bridge word is

```text
C_g(x,y)=A(x) W_g(x,y) B(y).                      (J3)
```

This is not the complete two-run profile: the no-bridge term is `P(x)T_gP(y)`. Summing their external endpoints recovers the earlier HG_g condition.

Two distinct bridges crossing successive positive gaps can have pure words between them only at ZERO b-gap inside the middle adjacent a-run. Both bridge endpoints there must be0. Any intervening nonempty pure-run parse must also have both endpoints0, so consists only of a^n words. The exact canonical join is therefore

```text
J(z)=Z+ZP(z)Z=Z/(1-z^n).                          (J4)
```

This is ONE geometric factor, not its square. Separately attaching a pure suffix to the first bridge and a pure prefix to the second would choose an arbitrary cut in that same chain and overcount it. J4 is the gluing correction absent from a product of independent one-gap completion equations.

## 4. Exact three-run parse matrix: five disjoint cases

For every fixed g,h>=1 consider ALL cores

```text
a^p b^g a^q b^h a^r,       p,q,r>=1.
```

Their full joint endpoint count matrix is EXACTLY

```text
D_(g,h)(x,y,z)
 = P(x)T_gP(y)T_hP(z)
   + C_g(x,y)T_hP(z)
   + P(x)T_gC_h(y,z)
   + A(x)W_g(x,y) [Z/Delta(y)] W_h(y,z)B(z)
   + A(x)W_(g,h)(x,y,z)B(z).                     (J5)
```

Proof by disjoint exhaustive raw parse classification:

1. **No bridge at either gap.** Every run has a nonempty pure-run parse; the two positive boundaries use T_g,T_h. This is the first term.
2. **A bridge at the first gap only.** Its optional pure prefixes/suffixes are C_g; its final delay meets the final run's initial delay through T_h. This is the second term.
3. **A bridge at the second gap only.** The symmetric third term.
4. **Two distinct bridge words, one at each gap.** They occupy ordered, nonoverlapping parts of the middle a-run. Their zero-gap join is J4, and only the first and third runs have external pure attachments. This is the fourth term. Positive middle a-lengths on both bridges automatically prevent them from covering an impossible empty middle run.
5. **One word bridges both gaps.** It contains all of the middle run, with optional pure prefix/suffix only at the first/third runs. This is the last term.

At most one word can cross a fixed gap in an ordered word factorization. Thus there is no sixth case or overlap among cases. A word with at least four a-runs has at least three positive internal b-gaps and cannot fit any of these three-run cores. The formula consequently remains exact even if the hypothetical M contains arbitrary longer/more-complicated words.

The free-end criterion for ALL three-run cores at these gaps is the formal-series identity

```text
1^T D_(g,h)(x,y,z) 1
   = x/(1-x) * y/(1-y) * z/(1-z).                (J6)
```

Its coefficient at every positive p,q,r is precisely one labelled free-end parse. Thus J6 is NECESSARY AND SUFFICIENT for this entire three-run subsystem, not a finite run-length sample.

All entries of J5 have denominator dividing `Delta(x)Delta(y)Delta(z)`. Therefore J6 is an exact FINITE trivariate polynomial identity after multiplication by that product. No interpreter, test cutoff or solver is required to state or prove the equivalence.

## 5. The coupled residual and a conditional actual-word obstruction

Let Lower_(g,h) be the first FOUR terms of J5. Their joint parse counts already follow from the pure words and actual one-gap bridge words. Define

```text
Def_(g,h)= x/(1-x)*y/(1-y)*z/(1-z)
             -1^T Lower_(g,h) 1.                 (J7)
```

A completion must realize the EXACT equation

```text
Def_(g,h)=1^T A(x) W_(g,h)(x,y,z) B(z) 1.         (J8)
```

Two consequences hold for arbitrary finite heterogeneous data:

- If any coefficient of Def is NEGATIVE, the lower actual words already have two different parses. Adding a three-run or longer word cannot repair this UD failure.
- If Def is nonzero, the data cannot be completed while W_(g,h)=0. Some ACTUAL three-run word with exactly those two positive gaps is required. Words with more internal positive gaps cannot supply the missing core. The allowed correction is J8, with real nonnegative labelled-word data and its prescribed pure attachments, not an arbitrary polynomial filling.

Clearing denominators gives a useful exact form. Put `Abar(x)=Delta(x)A(x)` and `Bbar(z)=Delta(z)B(z)`, both polynomial matrices. Then

```text
Delta(x)Delta(y)Delta(z) Def_(g,h)
 = Delta(y) * 1^T Abar(x) W_(g,h)(x,y,z) Bbar(z) 1. (J9)
```

This couples BOTH boundary gaps through the SAME middle-run pure order and joint delay data. It is strictly more informative than independently imposing HG_g and HG_h. It is still not the universal all-gap-list certificate: after three-run coherence, four or more runs remain.

## 6. Written non-Shor control showing the correction is indispensable

Use the immutable earlier control

```text
K0={aa,b,abb,aaaba,baba},
M0=K0 union {abbaba,abaaba}.
```

K0 is UD but incomplete; M0's UD/completeness proof is the named prior import. The earlier written calculation showed K0 parses EVERY pure run and EVERY one-positive-gap core, so this is not a marginal-failure example.

For K0, n=2. Its nonzero pure endpoint polynomials are `L_0=1`, `R_0=1`, `R_2=z`. Hence

```text
P_00=z^2/(1-z^2),
P_02=z/(1-z^2),
```

with all other P entries0. Its sole positive-gap bridge matrix is W_1, with the two entries

```text
(W_1)_00(x,y)=x^3 y       from aaaba,
(W_1)_10(x,y)=x y         from baba.
```

There is no W_2 and no three-run word in K0.

At gaps(g,h)=(2,1), consider the coefficient xyz, namely the core `a b^2 a b a`. Singleton pure parses would use abb at each of the three runs, and fail the last gap1 because its final delay is2. A bridge at the first gap is impossible, since W_2=0. The only length-compatible bridge at the second gap is baba, but its initial delay1 following the first abb would require first gap at least2+1=3, not2. Thus every term of Lower has coefficient0, while the target has1.

The actual missing correction is the three-run word `abbaba=a b^2 a b a`, an entry xyz in `(W_(2,1))_00`. It is one of the two actual extra words of M0. With no pure attachment it supplies exactly the missing coefficient. This is a written direct raw-word check, not an interpreter calculation.

Likewise, the other extra M0 word `abaaba=a b a^2 b a` is a three-run bridge with gaps(1,1). It addresses a different coupled core that K0's independent one-gap conditions do not control. No claim that these two particular additions generalize to Shor's code is made.

The example illustrates a genuine two-gap obstruction, not a merely formal renaming of the old marginal equation. It also shows why filling a deficit with a longer word is a new actual-word obligation whose compatibility must still be proved globally.

## 7. Exact status and unchanged full obligation

This packet gives an exact joint-boundary representation and a finite polynomial obstruction for every specified two-positive-gap pair, uniform over all three positive run lengths and arbitrary heterogeneous outer delays. It is WRITTEN mathematics at the GP/pure-run imports, not executable verification, formal proof, independent review or novelty clearance.

For Shor's C there is still no chosen global finite endpoint/bridge data and no contradiction for every such choice. J5–J9 identify the first coupled obstruction beyond the previously solved one-gap marginal, but they do not solve it universally and do not turn the fixed-seed critical-gap growth into an infinite descent.

The single original acceptance criterion therefore remains unmet: an ACTUAL finite raw M with all-list UD plus factor completeness, or an all-order impossibility reaching every finite heterogeneous completion. No pure-end threshold, support enumeration, word addition, ansatz flattening or claim of a solved replacement subsystem is substituted for that criterion. The next mathematical barrier is the coherent actual-word solution of these joint conditions and their arbitrary-run analogues, with the full raw GP/Q criterion still the acceptance interface.
