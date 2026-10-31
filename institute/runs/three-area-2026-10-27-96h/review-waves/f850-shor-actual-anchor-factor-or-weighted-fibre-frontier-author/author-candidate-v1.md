# F850 author candidate: prime-gcd exclusion, two further weighted exclusions, and an original-gcd spectrum obstruction

**Status.** Prospective GENERAL AUTHOR written candidate, not a parent disposition or an independent review. All theorems below concern one actual ordered direct tiling and an actual direct factor of its original head. They do not establish that such a factor exists, that the anchored tiling exists or does not exist, or that any remaining gcd is feasible. No scientific execution was performed.

## 1. Quantifiers and the original weighted reduction

Let `n > 14`, let `P,Q ⊂ Z_n`, and suppose every element of `Z_n` has exactly one ordered representation as `p+q` with `p∈P, q∈Q`. Assume

\[
A_0=\{0,3,8,11\}\subseteq P,\qquad
S=\{0,1,7,13,14\}\subseteq Q.
\]

Suppose in addition, not as a consequence of the anchors, that the **original** head has the direct factorization

\[
P=\{u,u+d\}\oplus C_0,\qquad d\not\equiv0\pmod n,
\qquad g=\gcd(d,n).
\]

Absorb `u` into `C_0`. Since `0∈P`, reversing `d` and translating the resulting `C` if necessary gives

\[
P=\{0,d\}\oplus C,\quad 0\in C,
\]

without changing `P`, `Q`, or the original cyclic gcd `g`. Every `a∈A_0` has a unique representation `a=c_a+e_a d`, where `c_a∈C` and `e_a∈{0,1}`. Its actual other factor-pair element is `a+ε_a d∈P`, with `ε_a=1−2e_a`. These signs are attached to the one physical factorization; they are not arbitrary independent CRT choices.

Put `T=C⊕Q`. This is an actual set with unique representations, and

\[
1_T(x)+1_T(x-d)=1\quad(x\in\mathbb Z_n).
\]

Alternation on the `d`-cycles gives `n/g` even; hence `2g|n`, `d/g` is odd, and `gcd(2d,n)=2g`. Also `T` is invariant under `2d`, so it consists of complete fibres modulo `2g`. There is a selector `V⊂Z_{2g}` with exactly one of `s,s+g` in `V` for each `s mod g`, and

\[
T=\{x\in\mathbb Z_n:x\bmod 2g\in V\}.
\]

Set `L=n/(2g)`. For original multiplicities

\[
c_i=|\{c\in C:c\equiv i\pmod{2g}\}|,\qquad
q_j=|\{q\in Q:q\equiv j\pmod{2g}\}|,
\]

directness gives the exact weighted identity, for every `s mod 2g`,

\[
\tag{1}\sum_i c_iq_{s-i}=L\,1_V(s).
\]

Here `c_0>0`, the residues of `S` lie in `V`, each occupied `c`-residue translates all of `S` into `V`, and each original head anchor `a` requires a positive `c`-residue at `a` or `a−g` modulo `2g`. Equation (1), not an unweighted projected tiling, is used throughout.

## 2. General theorem: no prime original gcd, and the weighted prime-fibre condition

**Theorem A.** Under the hypotheses of §1, the original integer `g=gcd(d,n)` is not prime. More generally, for every prime `p|g`, at least one of the following two original-element multiplicity profiles is exactly constant on `Z_p`:

\[
r\longmapsto |\{c\in C:c\equiv r\pmod p\}|,\qquad
r\longmapsto |\{q\in Q:q\equiv r\pmod p\}|.
\]

The choice of factor allowed to be constant may depend on `p`; this is not an assertion that either support is a quotient tile.

**Proof.** Projecting (1) to `Z_g` retains multiplicities. Define `α_r=c_r+c_{r+g}` and `β_r=q_r+q_{r+g}`. Since `V` contains exactly one residue from each antipodal pair,

\[
\tag{2}(\alpha*\beta)(r)=L\quad(r\in\mathbb Z_g).
\]

Projecting further to any prime `p|g` gives convolution of the two stated original-element profiles equal to the constant `Lg/p`. Let their integer polynomials of degree at most `p−1` be `F,G`. Evaluating at a primitive `p`th root `ζ` gives `F(ζ)G(ζ)=0`. The polynomial `Φ_p=1+X+⋯+X^{p−1}` is irreducible over `Q`: after `X↦X+1`, Eisenstein applies at `p`. Thus `Φ_p` divides `F` or `G`; because its degree is `p−1`, the corresponding coefficients are all equal. The common value is positive because `C,Q` are nonempty. This proves the stated condition, including `p=2`.

Now take `g=p` prime. If `α` is constant, every residue modulo `g` has a `C` element. Since `q_0>0`, the support of `c` lies in `V`; it contains at most one member of each antipodal pair, hence its support is exactly `V`. Since `q_1>0`, also `V+1⊂V`, hence `V+1=V`, impossible for a half-sized subset of `Z_{2g}`.

If instead `β` is constant, its support modulo `2g` is exactly `V`, using `c_0>0`. Choose an original head anchor `a` coprime to `g`: use `a=3` unless `g=3`, when `a=8`. Its actual `C` representative has residue `c≡a` or `a+g mod 2g`, so `gcd(c,g)=1` and `gcd(c,2g)` is `1` or `2`. As `V+c⊂V`, equality holds. In the first case this invariance makes `V` all of `Z_{2g}`; in the second it makes `V` a union of parity classes, but the original tail anchors `0,1` put both parity classes in `V`, again forcing the whole group. Both contradict the selector size `g`. ∎

This is an unbounded exclusion, including every prime `g≥17`; it does not require any assumed pairing of a projected head or any cardinality allocation.

## 3. Two additional actual weighted exclusions: `g=15` and `g=16`

**Theorem B.** The same hypotheses exclude `g=15` and `g=16`. The finite support lists below are necessary supersets of the supports of the original integer multiplicities, not constructions of tilings. Every inequality retains all omitted terms as nonnegative.

### 3.1. `g=15`

Work modulo `30`. Since `0∈C`, the five residues in `S` lie in `V`. The anchor `3` forces `c_18>0`: choosing `c_3>0` would put `3+13=16` opposite the already occupied residue `1`. The anchor `8` similarly forces `c_23>0`, since choosing `c_8>0` would put `8+7=15` opposite `0`. Finally the anchor `11` forces `c_11>0`: choosing `c_26>0` would put `26+7=3 mod 30` opposite the occupied `18`.

The four forced translates of `S` occupy exactly

\[
F=\{0,1,2,6,7,11,12,13,14,18,19,23,24,25\}.
\]

These use fourteen distinct antipodal pairs; the remaining pair is `{5,20}`. Thus `V=F∪{h}` for one `h∈{5,20}`. Checking `i+S⊂V` for a possible `c_i>0`, and checking `j+{0,11,18,23}⊂V` for a possible `q_j>0`, gives

\[
\begin{array}{c|l|l}
h&\operatorname{supp}c\ \text{is contained in}&\operatorname{supp}q\ \text{is contained in}\\\hline
5&\{0,5,11,18,23\}&\{0,1,7,12,13,14,19,25\}\\
20&\{0,6,11,18,23\}&\{0,1,2,7,13,14,19,25\}.
\end{array}
\]

The lists deliberately allow optional residues simultaneously even when further compatibility would forbid them. In **both** rows, the complete coefficient equations at residues `11` and `14` are

\[
\tag{3}L=c_{11}q_0,\qquad L=c_0q_{14}.
\]

At the other two displayed rows, the original positive forced terms give

\[
\tag{4}L\ge c_0q_0+c_{23}q_7,\qquad
L\ge c_{11}q_{14}+c_{18}q_7.
\]

All `c_0,c_11,c_18,c_23,q_0,q_7,q_14` are positive. Equations (3)–(4) yield both `c_11>c_0` and `c_0>c_11`, a contradiction.

### 3.2. `g=16`

Work modulo `32`. The anchor `3` forces `c_19>0`, because `3+13=16` is antipodal to `0∈V`. The possible residues for the anchors `8,11` are respectively `{8,24}` and `{11,27}`. If both are in the unshifted choices, or both in the shifted choices, the residues `8+1=9` and `11+14=25` (shifted together if applicable) are antipodal. There are therefore precisely two necessary cases. Each forced union below has all sixteen antipodal pairs represented, so it is the entire `V`.

**Case A: `c_8,c_27>0`.** The forced selector and support supersets are

\[
\begin{aligned}
V={}&\{0,1,2,7,8,9,13,14,15,19,20,21,22,26,27,28\},\\
\operatorname{supp}c\subseteq{}&\{0,1,7,8,13,14,19,20,26,27\},\\
\operatorname{supp}q\subseteq{}&\{0,1,7,13,14,20,26\}.
\end{aligned}
\]

The support lists follow by testing `i+S⊂V` and `j+{0,8,19,27}⊂V`. Consequently the complete coefficients at `19,22` are

\[
L=c_{19}q_0,\qquad L=c_8q_{14},
\]

while coefficients at `8,1` give

\[
L\ge c_8q_0+c_{27}q_{13},\qquad
L\ge c_{19}q_{14}+c_0q_1.
\]

The original forced factors are positive, so these imply both `c_19>c_8` and `c_8>c_19`.

**Case B: `c_24,c_11>0`.** Here

\[
\begin{aligned}
V={}&\{0,1,5,6,7,11,12,13,14,18,19,20,24,25,26,31\},\\
\operatorname{supp}c\subseteq{}&\{0,5,6,11,12,18,19,24,25,31\},\\
\operatorname{supp}q\subseteq{}&\{0,1,7,13,14,20,26\}.
\end{aligned}
\]

The same support tests, now with forced `C` residues `{0,11,19,24}`, give the lists. The complete coefficient equations at `11,14` and the positive terms at `0,25` give

\[
L=c_{11}q_0=c_0q_{14},\quad
L\ge c_0q_0+c_{19}q_{13},\quad
L\ge c_{11}q_{14}+c_{24}q_1.
\]

Thus `c_11>c_0` and `c_0>c_11`. This closes both orientations and proves Theorem B. ∎

## 4. Original cyclic gcd spectrum: another unbounded obstruction

Let

\[
D_Q=\{1,6,7,12,13,14\},\qquad
\mathcal D(n)=\{\gcd(n,s):s\in D_Q\}.
\]

These six positive integers are precisely the positive differences of the literal tail anchors. All gcds here are of original cyclic residues with the original `n`; they are **not** gcds computed in a projected group.

**Theorem C.** For the actual tiling of §1, any two distinct actual head elements `x,y` satisfy

\[
\tag{5}\gcd(n,x-y)\notin\mathcal D(n).
\]

Consequently, for each actual anchor `a` and its actual partner sign `ε_a`, and every `b∈A_0`,

\[
\tag{6}\gcd\bigl(n,a+\varepsilon_a d-b\bigr)\notin\mathcal D(n)
\]

whenever the two compared head elements are distinct. If they coincide, the gcd is `n`, which is not in `𝒟(n)` because `n>14`, so (6) still holds. In particular the actual factor is impossible whenever **both**

\[
\tag{7}\gcd(n,8+d)\in\mathcal D(n),\qquad
\gcd(n,8-d)\in\mathcal D(n).
\]

This is a general test for all candidate differences `d`, including composite `g≥18`. The condition on both signs makes no assumption about which physical orientation belongs to the anchor `8`; the sharper (6) uses its actual sign.

**Proof.** First, if `A⊕B=Z_n` and `k>0` is coprime to `|A|`, then `kA⊕B=Z_n`, with dilation injective on `A`. For a prime `ℓ∤|A|`, in the integral group ring modulo `ℓ`,

\[
A(X^\ell)B(X)=A(X)^\ell B(X)
=|A|^{\ell-1}\,J=J,
\quad J=\sum_{x\in Z_n}X^x.
\]

The integral coefficients on the left are nonnegative, all congruent to `1 mod ℓ`, and sum to `n`; every one is therefore exactly `1`. This also proves injectivity. Iterate over the prime factors of `k`. In particular every unit `u mod n` is admissible for `P`, since `|P|` divides `n`.

If two residues `t,s` have the same gcd with `n`, there is a unit `u mod n` with `ut≡s mod n`. For each prime power `p^e||n`, their truncated `p`-valuations agree; when both vanish modulo `p^e`, take `u≡1`, and otherwise divide out the common power of `p` and choose a unit sending the remaining unit part of `t` to that of `s`. Lift to `p^e` and combine by CRT.

If (5) failed, take an actual tail pair `r,r+s∈Q` with `s∈D_Q` and a unit `u` sending `x−y` to `s`. Then in the actual dilated direct tiling `uP⊕Q`, the two distinct ordered pairs `(ux,r)` and `(uy,r+s)` have the same sum, contradiction. The original factor gives the actual partners in (6), and (7) applies this to `a=8,b=0`. ∎

### 4.1. Explicit infinite composite-gcd exclusions

Write `rad_odd(n)` for the product of the distinct odd primes dividing `n`. The following are consequences of (7), not assumed properties of a quotient.

1. If `g` is odd and `rad_odd(n)|g`, no such actual factor exists. Indeed `d` is odd and every odd prime dividing `n` divides `d`; hence both `8±d` are coprime to `n`, and `1∈𝒟(n)`.
2. If `v_2(g)=1`, `rad_odd(n)|g`, and `7∤n`, no such actual factor exists. Since `2g|n`, both `8±d` have exact two-adic valuation `1` and have no common odd prime with `n`; their original gcd with `n` is `2=gcd(n,14)∈𝒟(n)`.
3. Let `r∈{7,13}`. If `g` is odd, `r|n`, `r∤g`, `v_r(n)=1`, and every other odd prime dividing `n` divides `g`, no such actual factor exists. Each `gcd(n,8±d)` is `1` or `r`, and both belong to `𝒟(n)` because `0,r∈Q`.

For a concrete unbounded family with no prime-gcd premise, let

\[
n=2^s3^a5^b11^c,\quad s\ge4,\quad a,b,c\ge1,
\]

and let the **original** candidate gcd be

\[
g=2^e3^i5^j11^k,\quad e\in\{0,1\},\quad
1\le i\le a,\quad1\le j\le b,\quad1\le k\le c.
\]

Then `2g|n` and the stated gcd is arithmetically possible for a residue `d`, but items 1–2 rule out an actual anchored head factor with that gcd. This includes arbitrarily large odd and even **composite** gcds. It does not assert an actual tiling for any of these parameters. The necessary allocation `|P|=8, |Q|=n/8` is numerically compatible with `330|Q|` in this family; the exclusion is not merely a failure of that cardinality divisibility check.

For context, the cardinality necessities used in that last sentence also follow directly from the same proved dilation lemma: if `|P|` were odd, `2·3+1=2·0+7` would collide in `2P⊕Q`; if `|Q|` were odd, `8+8·0=0+8·1` would collide in `P⊕8Q`; and the anchor differences `3,5,11` against the tail difference `1` force `3,5,11` to divide `|Q|`. Thus `2||P|` in the divisibility sense and `330|Q|`. Moreover, when `g≥15`, the four head anchors lie in four distinct residue classes modulo `g`, so their original `C` representatives are distinct and `|C|≥4`, `|P|≥8`. If `|P|=8`, these representatives are all of `C` and `P` is the union of the four actual anchor-pairs; this conclusion still **assumes** the original direct factor and does not manufacture one.

## 5. CRT compatibility and exact remaining boundary

Everything above is in the original cyclic group. If, additionally, `n=HR` with `gcd(H,R)=1` and the **actual** head is known to be a graph

\[
P=\{(a,f(a)):a\in\mathcal A\}\subseteq\mathbb Z_H\times\mathbb Z_R,
\]

write the actual difference as `(δ_H,δ_R)`. Then an original direct factor by this difference exists **if and only if** there is a set `B⊂𝒜` such that

\[
\mathcal A=B\mathbin{\dot\cup}(B+\delta_H),\qquad
f(b+\delta_H)-f(b)=\delta_R\quad\text{for every }b\in B.
\]

The forward direction projects the original `C`, using graph injectivity; the reverse direction takes `C={(b,f(b)):b∈B}`. In particular `δ_H=0` cannot give a nonzero factor difference of a graph. A projected pairing lacking one constant original `δ_R` does not lift. The coupled actual-tail equations remain

\[
\sum_{a\in\mathcal A}1_{Q_{r-f(a)}}(h-a)=1
\quad\text{for every }(h,r)\in\mathbb Z_H\times\mathbb Z_R;
\]

separate complement statements for the `Q_r` alone do not establish these equations. CRT also requires the **same** sign in both coordinates and gives

\[
g=\gcd(H,\delta_H)\gcd(R,\delta_R),\qquad
\gcd(n,8\pm d)=\gcd(H,8\pm\delta_H)\gcd(R,8\pm\delta_R).
\]

Thus neither a favourable `H`-shadow gcd nor an anchor rectangle supplies a qualifying original factor. The source packet mentions a separately named coprime-cardinality dilation route to the graph property; its underlying proof body is not in this packet. That route is a **conditional import**, not used to prove Theorems A–C. The displayed graph criterion itself is proved under the explicitly stated graph hypothesis.

Theorem A excludes every prime gcd; Theorem B excludes `15,16`; Theorem C supplies the exact original-gcd/sign tests and infinite composite-gcd families above. If the packet's prior `g≤14` exclusion is additionally imported **at its stated scope**, then every remaining factor has composite `g≥18`. The packet's full fourteen-case support/checker bodies are not present here, so this last combined lower bound is conditional on that named S1 import, not freshly reconstructed or independently checked here. For the rest—composite `g≥18` not satisfying a proved spectrum obstruction, heads with no two-point direct factor, and all unclosed allocations—the first unpaid step is still an actual-factor construction compatible with the graph increments and coupled fibres, or an independent obstruction. No such existence or global nonexistence is claimed. The source-packet RSS/pure-letter bridge, original printed-problem correspondence, literature novelty, priority, family/human review, formal/kernel acceptance, and publication remain outside this result.

## 6. Read, process, and execution declarations

* Before reading or reasoning from mathematical bodies, I read the complete F850 manifest, freeze receipt, final binding, parent-live-metadata supply, actual-dispatch receipt, and all 22 manifest-listed controls for status and permissions only. The first formatted administrative displays elided entries/one long line; complete raw rereads recovered them before acknowledgement. The new `prebody-ack-v1.md` was written and a direct prebody acknowledgement was delivered to Main before the packet was opened.
* I read the sole literal packet part serially, raw, in windows `1–20`, `21–40`, `41–60`, `61–80`, `81–92`, including its ending. Its supplied metadata is 15,593 bytes and 92 LF, so every window was below 30,000 bytes and at most 20 lines. The displayed windows were complete, with no packet clipping to recover. These windows include the complete rendered S1 lines `1–51` and S2 lines `1–31`. No linked mathematical source body was opened. Parent-supplied SHA256 pins, not independently recomputed here: part `bdb768b20091366b437a041453148e3cbaea81aacac31a4cda66005addc14e86`; S1 `45e8f43ab00178a600fd733276bc540164260cf97127c73106a1dc541c8838ad`; S2 `d8dfa1b1323f81c3c1be627fbf08794144d52b73de3efbcdded64ac6c3ad6d26`.
* Status-only controls were not mathematical premises. All genuinely held episodes and all their proof/method/planning/selection/verification/reporting/confidence/downstream consumers remained NONINPUT. No claim of clean private cognition is made.
* No network, external model, code execution, scientific eval, child subprocess, test, compilation, solver, code preparation, or hash computation was performed; therefore there is no prepared-code hash or execution evidence. The written calculations and support lists are unreviewed author work. No process deviation beyond the recovered administrative display elisions is known.
