# F869 author candidate: the original weighted gcd-15 and gcd-16 fibre contradictions

**Status.** Prospective GENERAL AUTHOR written candidate, not a parent disposition or independent review. The two exclusions below are proved directly from the stated actual-object hypotheses, with the finite set arithmetic displayed. No unweighted quotient tiling, exhaustive computer search, or execution is assumed. The scope is exactly the original two-point-direct-factor subclass; there is no claim of existence or unrestricted nonexistence of an anchored tiling.

## 1. Quantifiers, actual fibres, and the weighted equation

Let `n>14`, let actual sets `P,Q` directly tile `Z_n`, meaning every residue has exactly one ordered representation `p+q`, and suppose

\[
\{0,3,8,11\}\subseteq P,\qquad S=\{0,1,7,13,14\}\subseteq Q.
\]

Assume additionally that the **original** head has an actual direct factorization `P={u,u+d}⊕C_0`, with `d≠0 mod n`, and write `g=gcd(d,n)` using the original cyclic modulus. The claim is that **neither `g=15` nor `g=16` is possible**, for every such `n,P,Q,u,d,C_0`.

Absorb `u` into `C_0`. If `0` is not in the resulting second factor, then `-d` is in it; replace `d` by `-d` and translate that factor by `d`. Thus, without changing `P,Q` or `g`,

\[
P=\{0,d\}\oplus C,\qquad 0\in C.
\]

Because `P⊕Q=Z_n`, the original set `T=C⊕Q` is direct and `{0,d}⊕T=Z_n`. Consequently `1_T(x)+1_T(x-d)=1`. Around any `d`-cycle this alternates, so `n/g` is even, `2g|n`, and `d/g` is odd. Hence `gcd(2d,n)=2g` and `d≡g (mod 2g)`. The set `T` is invariant under `2d`, whose generated subgroup is precisely the set of multiples of `2g`. Thus `T` consists of complete fibres modulo `m=2g` and its image `V⊂Z_m` contains exactly one of each antipodal pair `{r,r+g}`.

Let `L=n/m`, and let `c_i` and `q_j` count the **original** members of `C` and `Q`, respectively, in residues `i,j mod m`. Directness counts the actual pairs in the complete fibres, so for every `s∈Z_m`,

\[
\tag{1}\sum_{i\in Z_m}c_iq_{s-i}=L\,1_V(s),\qquad L>0.
\]

All these multiplicities are nonnegative integers. Moreover `c_0>0` and `q_0,q_1,q_7,q_{13},q_{14}>0`, since the corresponding actual original elements are present. Positivity in (1) implies `S⊂V`, and `c_i>0` implies `i+S⊂V`. Conversely, every actual original head anchor `a` has its `C` representative at residue `a` or `a-g` modulo `m`; this is a necessary choice attached to the one physical factorization, not a free choice in a replacement tiling.

For a forced set `D` of `C` residues containing `0`, define the *complete necessary support supersets*

\[
\tag{2} A(V)=\bigcap_{s\in S}(V-s),\qquad B(V,D)=\bigcap_{a\in D}(V-a).
\]

Then `supp c⊂A(V)` and `supp q⊂B(V,D)`: the first follows from the five positive original `q_s`, and the second from the positive original `c_a` for `a∈D`. The intersections enumerate **all** potentially occupied residues under these necessary tests. They need not be jointly realizable, and are never treated as a quotient tiling.

## 2. Forced selectors and all support supersets for `g=15`

Work modulo `30`. The original head anchor `3` has possible `C` residues `3,18`. If `c_3>0`, then `3+13=16∈V`, opposite the already occupied `1`; hence `c_{18}>0`. Anchor `8` has candidates `8,23`; `8+7=15` is opposite `0`, so `c_{23}>0`. Anchor `11` has candidates `11,26`; if `c_{26}>0`, then `26+7=3∈V`, opposite `18∈V`, so `c_{11}>0`. Together with `c_0>0`, put `D={0,11,18,23}`.

The four actual forced translates, before taking their union, are

\[
\begin{array}{c|l}
a&a+S\pmod{30}\\\hline
0&\{0,1,7,13,14\}\\
11&\{11,12,18,24,25\}\\
18&\{1,2,18,19,25\}\\
23&\{0,6,7,23,24\}.
\end{array}
\]

Their union is `F={0,1,2,6,7,11,12,13,14,18,19,23,24,25}`. Its fourteen residues have distinct images modulo `15`, and the only unrepresented antipodal pair is `{5,20}`. Since `V` is a selector, **all** possibilities are exactly `V_5=F∪{5}` and `V_20=F∪{20}`.

The following intersection stages explicitly establish the complete support supersets. In the first table, start with `V_h` and successively impose `i+1,i+7,i+13,i+14∈V_h`; membership of `i` itself has already been imposed.

| Selector | after `+1` | after `+7` | after `+13` | after `+14`: `A(V_h)` |
|---|---|---|---|---|
| `h=5` | `{0,1,5,6,11,12,13,18,23,24}` | `{0,5,6,11,12,18,23,24}` | `{0,5,6,11,12,18,23,24}` | `{0,5,11,18,23}` |
| `h=20` | `{0,1,6,11,12,13,18,19,23,24}` | `{0,6,11,12,13,18,23,24}` | `{0,6,11,12,18,23,24}` | `{0,6,11,18,23}` |

For `B(V_h,D)`, start with `V_h` and successively impose `j+11,j+18,j+23∈V_h`:

| Selector | after `+11` | after `+18` | after `+23`: `B(V_h,D)` |
|---|---|---|---|
| `h=5` | `{0,1,2,7,12,13,14,19,24,25}` | `{0,1,7,12,13,14,19,24,25}` | `{0,1,7,12,13,14,19,25}` |
| `h=20` | `{0,1,2,7,12,13,14,19,20,25}` | `{0,1,2,7,12,13,14,19,25}` | `{0,1,2,7,13,14,19,25}` |

For a row `s`, let `I_s={(i,j)∈A(V_h)×B(V_h,D): i+j=s mod 30}`. The following are the **complete** incidences for the four rows used; a potentially allowed residue that is actually absent simply has zero original multiplicity.

| `h` | `I_11` | `I_14` | `I_0` | `I_25` |
|---|---|---|---|---|
| `5` | `{(11,0)}` | `{(0,14)}` | `{(0,0),(5,25),(11,19),(18,12),(23,7)}` | `{(0,25),(11,14),(18,7)}` |
| `20` | `{(11,0)}` | `{(0,14)}` | `{(0,0),(11,19),(23,7)}` | `{(0,25),(6,19),(11,14),(18,7),(23,2)}` |

All four row residues lie in either selector, so (1) and these exact incidence sets give, in **each** case,

\[
\tag{3}L=c_{11}q_0=c_0q_{14},\qquad
L\ge c_0q_0+c_{23}q_7,\qquad
L\ge c_{11}q_{14}+c_{18}q_7.
\]

The table retains every other term as a nonnegative product. As `c_{18},c_{23},q_7,q_0,q_{14}>0`, the first inequality together with the first equality gives `c_{11}>c_0`, while the second together with the second equality gives `c_0>c_{11}`. This strict positive two-cycle excludes both antipodal choices and hence `g=15`.

## 3. Forced selectors and all support supersets for `g=16`

Work modulo `32`. For original anchor `3`, the choices are `3,19`. If `c_3>0`, then `3+13=16∈V`, opposite `0`; therefore `c_{19}>0`. For anchors `8` and `11` the respective choices are `{8,24}` and `{11,27}`. Choosing both unshifted would put `8+1=9` and `11+14=25` in `V`, an antipodal pair. Choosing both shifted would put `24+1=25` and `27+14=9 mod 32` in `V`. Thus the only possible cases are

* **A:** `D_A={0,8,19,27}`, all four actual `c`-multiplicities positive;
* **B:** `D_B={0,11,19,24}`, all four actual `c`-multiplicities positive.

The forced translates are displayed without omitting overlaps:

| Case | `a` | `a+S mod 32` |
|---|---:|---|
| A, B | `0` | `{0,1,7,13,14}` |
| A, B | `19` | `{0,1,19,20,26}` |
| A | `8` | `{8,9,15,21,22}` |
| A | `27` | `{2,8,9,27,28}` |
| B | `11` | `{11,12,18,24,25}` |
| B | `24` | `{5,6,24,25,31}` |

Their unions are respectively

\[
\begin{aligned}
V_A&=\{0,1,2,7,8,9,13,14,15,19,20,21,22,26,27,28\},\\
V_B&=\{0,1,5,6,7,11,12,13,14,18,19,20,24,25,26,31\}.
\end{aligned}
\]

Each union has sixteen elements with distinct images modulo `16`, so in the respective case it is the **entire** selector; there is no further antipodal choice. The following stages establish the complete `C` support supersets (successively requiring `i+1,i+7,i+13,i+14∈V`):

| Case | after `+1` | after `+7` | after `+13` | after `+14`: `A(V)` |
|---|---|---|---|---|
| A | `{0,1,7,8,13,14,19,20,21,26,27}` | `{0,1,7,8,13,14,19,20,21,26,27}` | `{0,1,7,8,13,14,19,20,21,26,27}` | `{0,1,7,8,13,14,19,20,26,27}` |
| B | `{0,5,6,11,12,13,18,19,24,25,31}` | `{0,5,6,11,12,13,18,19,24,25,31}` | `{0,5,6,11,12,13,18,19,24,25,31}` | `{0,5,6,11,12,18,19,24,25,31}` |

For the `Q` supersets, start from `V_A` and test `+8,+19,+27` in case A, and start from `V_B` and test `+11,+19,+24` in case B:

| Case | first extra shift | second extra shift | third extra shift: `B(V,D)` |
|---|---|---|---|
| A | `{0,1,7,13,14,19,20,26}` | `{0,1,7,13,14,20,26}` | `{0,1,7,13,14,20,26}` |
| B | `{0,1,7,13,14,20,26}` | `{0,1,7,13,14,20,26}` | `{0,1,7,13,14,20,26}` |

Again let `I_s={(i,j)∈A(V)×B(V,D): i+j=s mod 32}`. These are **all** incidences on the rows used, not just selected terms:

| Case | row `s` | complete `I_s` |
|---|---:|---|
| A | `19` | `{(19,0)}` |
| A | `22` | `{(8,14)}` |
| A | `8` | `{(1,7),(7,1),(8,0),(14,26),(20,20),(26,14),(27,13)}` |
| A | `1` | `{(0,1),(1,0),(7,26),(13,20),(19,14),(20,13),(26,7)}` |
| B | `11` | `{(11,0)}` |
| B | `14` | `{(0,14)}` |
| B | `0` | `{(0,0),(6,26),(12,20),(18,14),(19,13),(25,7),(31,1)}` |
| B | `25` | `{(5,20),(11,14),(12,13),(18,7),(24,1),(25,0),(31,26)}` |

All listed row residues are in their case's selector. In case A, (1) therefore gives the exact singletons and nonnegative-remainder bounds

\[
\tag{4}L=c_{19}q_0=c_8q_{14},\qquad
L\ge c_8q_0+c_{27}q_{13},\qquad
L\ge c_{19}q_{14}+c_0q_1.
\]

The original forced multiplicities in the remainders are strictly positive, so these equations imply both `c_{19}>c_8` and `c_8>c_{19}`. In case B, the complete incidences likewise give

\[
\tag{5}L=c_{11}q_0=c_0q_{14},\qquad
L\ge c_0q_0+c_{19}q_{13},\qquad
L\ge c_{11}q_{14}+c_{24}q_1.
\]

Here the forced remainders are also strictly positive, yielding both `c_{11}>c_0` and `c_0>c_{11}`. Thus both necessary cases fail, excluding `g=16`.

In (3)–(5), the full incidence tables specify the exact equalities at the nonsingleton rows as well: sum `c_iq_j` over the displayed row. Every optional product remains nonnegative, whether or not its residue is actually occupied; no omitted term is cancelled or assumed zero. In particular the proof uses the original positive counts, not unit weights or a supposed quotient direct factorization.

## 4. Boundary and conditional imports

The argument covers all `n>14`, all actual original anchored tilings and every actual two-point direct factor whose original gcd is exactly `15` or `16`; it also covers either orientation of that same factor through the normalization in §1. It does not prove that any such tiling or factor exists, that all heads have such a factor, or that any other gcd is possible or impossible. It does not settle the unrestricted anchored tiling, original printed-problem correspondence, finite maximal completion, literature novelty or priority. The present gcd-15/16 exclusion uses no missing mathematical body as an import.

If one additionally wants to combine this result with the smaller-gcd or prime-gcd claims, those are separate, **conditional** imports at their respective scopes: S2's stated actual original-factor gcd-at-least-15 disposition (its underlying fourteen-case support/checker bodies are not in this packet) and S1's Theorem A excluding prime original gcd. Neither is needed in §§1–3. Similarly the separately named coprime-cardinality graph route and the RSS/pure-letter bridge have missing underlying bodies and are not used or promoted here. No family/human review, formal/kernel acceptance, global theorem, or publication-priority claim is made.

## 5. Read, process, and execution declaration

* Before any packet body read or task mathematics, I read the complete f869 manifest, freeze receipt, final pre-dispatch binding, parent-live-metadata supply, actual-dispatch receipt, and every one of the 22 manifest-listed status-only controls. Initial formatted administrative displays elided fields or a long line; complete raw rereads recovered the five administrative files before acknowledgement. I also read the mandatory memory summary and written-math protocol as administrative guidance. I then wrote `prebody-ack-v1.md` in this wave and sent a direct prebody ACK to Main, both before the packet read. The controls were used only for status and permissions, not as mathematical inputs. No prior exposure to these task bodies is known in this session; no private-cognition certificate is claimed.
* After that ACK, I read the sole literal packet part completely and serially in raw windows `1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–180, 181–200, 201–220, 221–240, 241–260, 261–280, 281–300, 301–320, 321–340, 341–360, 361–374`, including the ending. Each display was at most 20 LF and below 30,000 bytes; none showed packet clipping or required packet clipping recovery. The windows cover all rendered S1 `1–278`, S2 `1–51`, and S3 `1–31`. The parent-supplied packet pin is `e4903ba0b42848ed92da00d02dfa00a3be19177f88cf158941def095850d35c5` (35,551 bytes, 374 LF); source pins are S1 `91f2b1a4d4326feeff89cf6ec6541c1437989a08ea84d60e359a8ba546e16e14`, S2 `45e8f43ab00178a600fd733276bc540164260cf97127c73106a1dc541c8838ad`, S3 `d8dfa1b1323f81c3c1be627fbf08794144d52b73de3efbcdded64ac6c3ad6d26`. These are supplied metadata, not independently recomputed hashes or a separate source-identity certification. No packet link was followed.
* All genuine held episodes and all proof/method/selection/planning/verification/reporting/confidence/downstream consumers remained NONINPUT. No network, external model, scientific eval, child subprocess, test, build, compilation, solver, executable code preparation, or code execution was used. There is therefore no prepared-code hash or execution result. The finite support and incidence tables are handwritten, unreviewed author mathematics; parent disposition and a separate disjoint check remain necessary. Apart from the disclosed and recovered initial administrative display elisions, no process deviation is known.
