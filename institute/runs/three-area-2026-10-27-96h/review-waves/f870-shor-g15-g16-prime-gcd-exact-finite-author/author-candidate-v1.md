# F870 author candidate: exact selectors and weighted incidences at original gcd 15 and 16

**Status.** Prospective GENERAL AUTHOR candidate, with a NEW, complete, **UNRUN** standard-library exact verifier. The written argument below is author work, not an independent review or parent disposition. Its exhaustive implementation, its reason-specific mutants and the bounded controls have not been run. In particular there are no observed selector counts, passing controls, timing result, or verifier certificate from this source. The source is prepared for a complete parent source read and a **separate** one-shot GO, not authorized by this document. No independent-family, human, formal/kernel, original-book-source, novelty, priority or publication acceptance is claimed.

## 1. Actual-object quantifiers and projection

Let `n>14`, and let actual sets `P,Q ⊆ Z_n` satisfy `P⊕Q=Z_n`, with one ordered representation of every residue. Assume the actual original anchors

`A={0,3,8,11} ⊆ P`, `S={0,1,7,13,14} ⊆ Q`,

and, as an additional hypothesis, an actual direct head factorization `P={u,u+d}⊕C_0`, where `d` is nonzero modulo `n`. Put `g=gcd(d,n)`. The conclusion of this candidate is **only** that these hypotheses cannot hold when `g=15` or `g=16`. It does not assert that the factorization exists, that every possible head has a two-point direct factor, or that any anchored target tiling exists or fails to exist without this factor hypothesis.

Absorb `u` into `C_0`. Since `0∈P`, orient the factor as `P={0,d}⊕C` with `0∈C`: if the zero representation uses `d`, replace `(d,C)` by `(-d,C+d)`. The sign reversal preserves the original `P,Q` and `g`. Put `T=C⊕Q`. Actual directness gives

`1_T(x)+1_T(x-d)=1` for every `x∈Z_n`.

Alternating around each `d`-cycle forces `n/g` even, hence `2g|n`; and `T` is invariant under `2d`. Since `gcd(2d,n)=2g`, the occupied residues are complete fibres modulo `m=2g`. Thus `T` is the inverse image of a selector `V⊂Z_m` containing exactly one element from each pair `{r,r+g}` for `0≤r<g`. Set `L=n/m>0`. For the **original-element** projected multiplicities

`c_i=#{c∈C:c≡i (mod m)}`, `q_j=#{q∈Q:q≡j (mod m)}`,

all of which are nonnegative integers, directness and full fibres give, for every `s∈Z_m`, the exact identity

`Σ_i c_i q_(s-i) = L·1_V(s)`.                                      (1)

No quotient set-tiling or unit multiplicity is assumed. Since `c_0>0`, `S⊆V`; each positive `c_i` forces `i+S⊆V`. Each actual head anchor `a∈{3,8,11}` has a positive `C` residue at `a` or `a+g`, because `d≡g (mod 2g)`. These residues are tied to the actual original factor, not chosen independently in different CRT shadows.

For any forced positive set `I⊆Z_m` containing `0`, define the **necessary supersets**

`C*(V)=⋂_{s∈S}(V-s)`, `Q*(V,I)=⋂_{i∈I}(V-i)`.                 (2)

Then `supp(c)⊆C*` and `supp(q)⊆Q*`, with `I⊆supp(c)` and `S⊆supp(q)`. These are coordinatewise supersets, not a claim that all their elements can occur together. In particular, if `i+j∉V`, (1) forces `c_i q_j=0`. For each `s`, the exact list of all incidence pairs permitted by these supersets is

`E_s={(i,j): i∈C*, j∈Q*, i+j≡s (mod m)}`.                       (3)

The right side is an exact finite set even when some of its optional pairs cannot jointly occur in an actual tiling. It is the entire coefficient support; for an occupied row, every omitted term in a lower bound is nonnegative.

## 2. Complete selector reduction by written set identities

### `g=15`

Work modulo `30`. Choosing residue `3` for anchor `3` would put `3+13=16` opposite `1∈V`; hence `18∈supp(c)`. Choosing `8` for anchor `8` would put `8+7=15` opposite `0`; hence `23∈supp(c)`. Once `18` is forced, choosing `26` for anchor `11` would put `26+7=3` opposite `18`; hence `11∈supp(c)`. Therefore the forced positive `C` set is `I={0,11,18,23}`. The union of its four translates of `S` is exactly

`F={0,1,2,6,7,11,12,13,14,18,19,23,24,25}`.

It occupies 14 different antipodal pairs; the remaining pair is `{5,20}`. Consequently there are exactly two possible selectors, `F∪{5}` and `F∪{20}`, and no other anchor orientation is possible. Applying (2) gives the first two rows of the table below.

### `g=16`

Work modulo `32`. A `C` residue `3` would put `3+13=16` opposite `0`, so anchor `3` forces `19`. The `8` and `11` choices are respectively `{8,24}` and `{11,27}`. If both choices are unshifted, or both shifted by `16`, the two forced translated tail residues `8+1` and `11+14` are antipodal. Hence only `(8,27)` and `(24,11)` remain. In each case the union of the four forced translates has exactly 16 elements, one in each antipodal pair, and therefore already equals the entire `V`. Applying (2) gives the last two rows:

| Case | Entire selector `V` | Forced positive `I` | Exact `C*(V)` | Exact `Q*(V,I)` |
|---|---|---|---|---|
| 15, `h=5` | `{0,1,2,5,6,7,11,12,13,14,18,19,23,24,25}` | `{0,11,18,23}` | `{0,5,11,18,23}` | `{0,1,7,12,13,14,19,25}` |
| 15, `h=20` | `{0,1,2,6,7,11,12,13,14,18,19,20,23,24,25}` | `{0,11,18,23}` | `{0,6,11,18,23}` | `{0,1,2,7,13,14,19,25}` |
| 16 A | `{0,1,2,7,8,9,13,14,15,19,20,21,22,26,27,28}` | `{0,8,19,27}` | `{0,1,7,8,13,14,19,20,26,27}` | `{0,1,7,13,14,20,26}` |
| 16 B | `{0,1,5,6,7,11,12,13,14,18,19,20,24,25,26,31}` | `{0,11,19,24}` | `{0,5,6,11,12,18,19,24,25,31}` | `{0,1,7,13,14,20,26}` |

Each entry is the literal intersection in (2). This calculation is a written author derivation; the independent finite implementation is prepared but unexecuted. Equation (3), the entire displayed supersets, and the modulus provide an exact specification of **all** coefficient incident pairs for every residue, including unoccupied rows.

## 3. Exact coefficient incidences and positive two-cycles

For clarity, the following list records *all* pairs in the two singleton rows and in the two strict-inequality rows in each case, not merely the forced pairs. The order `(i,j)` means the coefficient term `c_i q_j`; sums are modulo the case's `2g`.

| Case | Singleton row `s`: `E_s` | Singleton row `s`: `E_s` | Strict row `s`: `E_s` | Strict row `s`: `E_s` |
|---|---|---|---|---|
| 15, `h=5` | `11: {(11,0)}` | `14: {(0,14)}` | `0: {(0,0),(5,25),(11,19),(18,12),(23,7)}` | `25: {(0,25),(11,14),(18,7)}` |
| 15, `h=20` | `11: {(11,0)}` | `14: {(0,14)}` | `0: {(0,0),(11,19),(23,7)}` | `25: {(0,25),(6,19),(11,14),(18,7),(23,2)}` |
| 16 A | `19: {(19,0)}` | `22: {(8,14)}` | `8: {(1,7),(7,1),(8,0),(14,26),(20,20),(26,14),(27,13)}` | `1: {(0,1),(1,0),(7,26),(13,20),(19,14),(20,13),(26,7)}` |
| 16 B | `11: {(11,0)}` | `14: {(0,14)}` | `0: {(0,0),(6,26),(12,20),(18,14),(19,13),(25,7),(31,1)}` | `25: {(5,20),(11,14),(12,13),(18,7),(24,1),(25,0),(31,26)}` |

All listed rows are in their corresponding `V`, so their coefficient is `L`. For both `g=15` selectors, (1) and the listed incidences give the exact equations and positive-remainder inequalities

`L=c_11 q_0=c_0 q_14`,

`L≥c_0 q_0+c_23 q_7`, `L≥c_11 q_14+c_18 q_7`.

Here `c_0,c_11,c_18,c_23,q_0,q_7,q_14` are strictly positive original multiplicities. The first inequality yields `c_11>c_0` after division by `q_0`; the second yields `c_0>c_11` after division by `q_14`. Both cannot hold.

For `g=16` A,

`L=c_19 q_0=c_8 q_14`,

`L≥c_8 q_0+c_27 q_13`, `L≥c_19 q_14+c_0 q_1`.

The forced positives give `c_19>c_8` and `c_8>c_19`. For `g=16` B,

`L=c_11 q_0=c_0 q_14`,

`L≥c_0 q_0+c_19 q_13`, `L≥c_11 q_14+c_24 q_1`,

which gives `c_11>c_0` and `c_0>c_11`. Optional incidence terms cannot cancel these inequalities because all multiplicities are nonnegative. This completes the written conditional exclusion of these two original gcd values; the prepared finite program is additional corroboration only if later audited, authorized and actually completed.

## 4. Actual non-target controls and the dilation/orbit lemmas

The following are actual direct tilings, not purported anchored target realizations. For each `g∈{15,16}`, put `n=4g`, `d=g`, `C={0,2g}`, `Q={0,1,…,g-1}` and `P={0,g,2g,3g}`. Every integer in `[0,4g)` has a unique quotient/remainder decomposition `kg+q`, `0≤k<4`, `0≤q<g`, so `P⊕Q=Z_n` and `P={0,d}⊕C`. These controls contain the entire tail anchor set but miss the nonzero head anchors. Here `V={0,…,g-1}`, `L=2`, `c_0=2`, and `q_j=1` for `0≤j<g`; (1) holds exactly. They show why a local selector or weighted projection must not be relabelled as an actual anchored target tiling.

Conversely take `n=32`, `d=3`, `C={0,8}` and `Q={0,2,4,6,16,18,20,22}`. Then `P={0,3,8,11}` has every head anchor, and `P⊕Q=Z_32`: the translates by `0` and `8` of `Q` partition the even residues, and translates by `3` and `11` partition the odd residues. The tail anchors `1,7,13,14` are missing. Here `g=1`, `V={0}` modulo 2, `L=16`, `c_0=2`, `q_0=8`. This is also **NON_TARGET**, not a counterexample to the anchored claim.

For completeness, the actual-object dilation fact being checked at bounded orders has a general written proof. If `A⊕B=Z_n`, `k>0`, and `gcd(k,|A|)=1`, then `kA⊕B=Z_n`, with `k` injective on `A`. For a prime `ℓ∤|A|`, in `F_ℓ[Z_n]` the Frobenius identity and `AJ=|A|J` give

`A(X^ℓ)B(X)=A(X)^ℓB(X)=A(X)^(ℓ-1)J=|A|^(ℓ-1)J=J`.

The integral ordered-sum coefficients on the left are nonnegative, congruent to 1 modulo `ℓ`, and total `|A||B|=n`; all are therefore exactly 1. A repeated dilated `A` element would already make an ordered coefficient at least 2, proving injectivity. Iterate over prime factors of `k`. In particular, a unit modulo `n` may dilate either actual factor alone.

Also, for all `t,s∈Z_n`, there is a unit `u mod n` with `ut=s` if and only if `gcd(t,n)=gcd(s,n)`, interpreting gcd on integer representatives. The forward direction is immediate. For each `p^e||n` in the reverse direction, let the common truncated `p`-valuation be `v`. If `v=e`, take local `u=1`; otherwise divide both residues by `p^v`, choose the ratio of their unit parts modulo `p^(e-v)`, and lift it to a unit modulo `p^e`. CRT joins these local units. This includes zero residues, shared prime factors, and the one-element group. As a consequence, two distinct actual differences from opposite factors cannot have the same gcd with `n`: use a unit to align one difference with the negative of the other, and the dilated direct tiling would have two ordered representations. These are written lemmas, not an inference of an unbounded prime-gcd theorem from finite output.

## 5. UNRUN source, exact coverage, controls, and limits

Prepared source: `exact-selector-incidence-v1.py`. Parent-supplied **administrative** live SHA-256 (not a scientific result): `434dc2877004f3b61948354fd2e967eafa85613d86bd2e805b8871a2afb45c6e`; `19152` bytes, `494` LF. I did not run or hash the source. Parent full-source/narrative read and separate one-shot GO remain required.

The intended finite procedure represents every one of the `2^g` antipodal selectors for each of `g=15,16` by choosing lower or upper elements independently, then filters on the original `S`. For each survivor it independently computes every possible anchor representative whose translated `S` stays inside the same selector, takes the Cartesian product of those anchor choices, computes (2), and compares the complete selector/anchor universe and support supersets to the four written cases. It constructs every row (3) both by distributing all support-superset pairs and by an independent row filter, and emits the exact `E_s` for **all** `s`, including empty/unoccupied rows. The expected tail-selector counts `2^(g-5)` follow because the five `S` residues occupy distinct antipodal pairs; they are expectations, not observed output. A selector surviving these necessary conditions is not a tiling witness.

For each case the program requires the two singleton incidence sets exactly, the occupied-row identities, the matching orientation of the two base products, and two **distinct** positive remainder products from original forced sets. It is designed to reject seven controls under their specified reasons: an added antipode, a swapped-away original tail zero, removed head-3 representative, an extra singleton incident pair, missing base `q_0` positivity, missing strict-remainder positivity, and a fake remainder identical to its base. Expected reasons are respectively `SELECTOR_ANTIPODAL`, `TAIL_ANCHOR_MISSING`, `HEAD_ANCHOR_3_MISSING`, `SINGLETON_INCIDENCE`, `BASE_NOT_FORCED`, `REMAINDER_NOT_FORCED`, and `REMAINDER_NOT_DISTINCT`. They are **planned controls**, not claimed passing mutants.

The program separately checks the three explicitly non-target actual tilings above, including original ordered directness, factor directness, alternation, full fibres and every weighted coefficient. It also enumerates all normalized ordered direct tilings with both factors containing zero for `1≤n≤12`, by covering the least uncovered group element with a disjoint translate of the first factor. Every normalized direct tiling has one and only one such next translate, so the recursion enumerates this explicitly bounded normalized domain without introducing a symmetry or weight assumption. For each emitted tiling the source checks both-factor dilation for all `1≤k≤2n` coprime to the relevant factor cardinality, retaining multiplicities before testing injectivity and directness. Separately it checks every ordered pair `(t,s)∈Z_n²` against every unit for the equal-gcd orbit equivalence. The domain `n≤12` is expressly non-target because the anchored target assumes `n>14`; these checks neither establish the unbounded lemmas nor find an anchored target witness.

The executable uses a sticky signal latch and a monotonic **38-second cooperative internal computation deadline**. Its JSON records `NOT_STARTED`, `RUNNING`, `COMPLETE`, `INCOMPLETE`, `FAIL`, or `ERROR` as appropriate; interrupted sections are not called complete, and an incomplete run has a nonzero exit. It creates no files, subprocesses or network connections. A parent supervising a separately authorized run must impose an outer limit **≤55 seconds**, collect complete stdout/stderr and actual exit, and treat a truncated/absent receipt or external kill as incomplete. The internal guard is cooperative, not a hard guarantee against blocking output or OS descheduling.

## 6. Conditional imports and unresolved boundary

S2's prior `g≤14` disposition is present in the packet, but its full linked fourteen-case author/reviewer/checker bodies are not; any combination with that prior exclusion is conditional on its stated scope and those named missing bodies, not newly independently reconstructed here. S1's general prime-gcd assertion is not certified by this finite assignment and no global infinite-prime theorem is inferred from the prepared verifier. The separate coprime-cardinality-to-CRT-graph route mentioned in the packet remains a named conditional import if ever used; neither it nor linked sources are needed for the `g=15,16` argument above. The RSS/pure-letter bridge and original printed-problem correspondence also remain conditional and outside this candidate. Higher composite gcds, heads without the assumed two-point factor, global anchored tiling existence/nonexistence and maximal-code completion remain open here.

## 7. Read, process and execution declarations

Before any mathematical body read or reasoning, I read the complete F870 manifest, freeze receipt, final binding, parent-live-metadata supply, actual dispatch receipt, and all 22 manifest-listed status-only controls. Initial formatted administrative displays elided lines; complete raw rereads recovered them before the acknowledgement. I wrote `prebody-ack-v1.md` and directly delivered the prebody acknowledgement to Main before opening the mathematical packet. No status-only control is a mathematical premise.

After both acknowledgements, I read the sole literal part serially in raw windows `1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–180, 181–200, 201–220, 221–240, 241–260, 261–280, 281–300, 301–320, 321–340, 341–360, 361–374`, including the ending. Every display had at most 20 LF and was below 30,000 bytes; no packet clipping occurred. This covers all rendered S1 `1–278`, S2 `1–51`, and S3 `1–31` in order. Parent-supplied part SHA-256 is `e4903ba0b42848ed92da00d02dfa00a3be19177f88cf158941def095850d35c5`. Parent-supplied original source pins, not independently rehashed here, are S1 `91f2b1a4d4326feeff89cf6ec6541c1437989a08ea84d60e359a8ba546e16e14`, S2 `45e8f43ab00178a600fd733276bc540164260cf97127c73106a1dc541c8838ad`, and S3 `d8dfa1b1323f81c3c1be627fbf08794144d52b73de3efbcdded64ac6c3ad6d26`. I did not open linked or unlisted mathematical sources. All genuine held episodes and all proof, method, planning, selection, verification, reporting, confidence and downstream consumers remain NONINPUT; no cognition certificate is asserted.

No scientific source was executed, tested, compiled, evaluated, or launched in a child process, and no network, external model, Git or cleanup was used. Source-hash metadata was supplied directly by Main because the worker's no-code-execution/no-child constraint prevents local hashing. No process deviation beyond the recovered administrative display elisions is known.
