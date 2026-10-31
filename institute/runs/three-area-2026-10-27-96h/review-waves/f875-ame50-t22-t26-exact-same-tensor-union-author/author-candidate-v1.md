# F875 author candidate: conditional exact N50 union on one physical tensor

**Status.** Prospective GENERAL AUTHOR candidate, not a parent disposition. The conditional union and the two explicit support/phase formulations below do not assert either residual branch is populated or empty. In particular they do **not** exclude N=50, prove a minimum of 51, exhibit a 50-term state, or confer independent-family, human, formal/kernel, source-identity, novelty, priority or publication acceptance. All assumptions and missing load-bearing bodies are identified below. The inequalities and low-excess arguments in §§2–3 and the constructive equivalences in §§5–6 are written derivations here; the named earlier entire-branch exclusions are not silently reproved by citing their abbreviated dispositions.

## 1. Object, quantifiers, and explicit imports

Throughout fix **one** arbitrary normalized pure complex AME(4,6) state, **one** fixed choice of four local orthonormal six-symbol bases, and write its coefficient tensor as ψ and U=6ψ in that basis. For a physical pair of parties I, its complementary pair is Iᶜ; the three balanced flattenings of U are 36×36 unitary matrices. Every statement about a word, phase, modulus, pair line or cut below refers to this same U. Let N be its number of nonzero entries; P={w:|U_w|=1}, t=|P|, and E={w:0<|U_w|<1}. We are concerned with N=50, so |E|=50−t. The count t and both word sets are tensor properties, not cut-dependent choices. The E alphabet size q_i is the number of actual symbols occurring at party i in E; q=4444 means these four sizes are all 4, not that four entries in a matrix have degree 4.

The following are **separate conditional mathematical imports**; all apply to the same actual normalized state/basis just fixed, with arbitrary complex phases and moduli. S1–S7 refer to the complete literal packet bodies listed in §9, not to the linked underlying source files. S1 is explicitly an unadopted parent candidate; S2–S7 are scoped parent dispositions. Their status is reported, not independently certified by this candidate.

* **C28, global upper-count import.** Every normalized complex AME(4,6) tensor in a fixed local orthonormal product basis has t≤28. Its retained chain includes the classical no-OLS(6) assertion, f113, and the prior t≤30/count argument, as qualified in S2. The actual load-bearing earlier proofs of that chain are not in this packet. Neither the elementary count nor any isolated exact-t exclusion below proves C28. If the chain needs further transitive premises, they remain part of C28; this candidate does not silently discharge them.
* **I25 and I27, separate exact-case imports.** The S3 dispositions exclude respectively N=50,t=25 and N=50,t=27 for actual complex tensors. I25 uses the same physical P/E words in all six pair systems and three cuts; I27 uses one actual unitary cut. Their full underlying author/checker bodies are not in the packet. In particular the connected excess-five order-5 and order-7 impossibilities used by I27 are imported rather than asserted proved by our short component calculation.
* **I28, separate exact-case import.** S4 excludes the entire actual N=50,t=28 branch, on one common P/E tensor in all six pair systems and three cuts, with arbitrary complex entries. The detailed common-hole/closure and earlier excess-six bodies are not in this packet; their use is conditional. S4 is a later separate disposition, not an inference from S3's explicitly unadopted F799 extra claims. It does not require C28 or no-OLS as its exact-case premise.
* **I26, separate alphabet import.** S5 states that every actual N=50,t=26 tensor has q=4444. Its q5 exclusion and complete alphabet reduction depend on the full common-core/alphabet arguments whose bodies are linked but not included; they are conditional imports here, not consequences of our t23/t24 proof. This is an alphabet restriction, not exclusion or realization of any 4444 support.

The S3/S4/S5 branch dispositions state their scopes independently of a global t-bound; the union uses C28 additionally to dispose of t>28. Parent-reported F800 and F842 results are local necessary-condition/geometry checks, not exhaustive common-P/E tensor or phase searches, and are not rerun here. S4 expressly says the earlier F812 zero prefix was **INCOMPLETE**, not absence evidence. Nothing in this candidate turns any of these local checks into a global search proof.

**Claim under C28 + I25 + I27 + I28 + I26.** For every actual normalized complex AME(4,6) tensor/basis with N=50, either (a) t=22 and its actual P22/E28 support obeys the exact same-support common-phase criterion of §5, or (b) t=26, q=4444 and its actual P26/E24 amplitudes/phases obey the exact common-tensor system of §6. Conversely, a physical support satisfying §5's criterion, or a support and variables satisfying §6, constructs a normalized complex AME(4,6) state with exactly 50 nonzeros. Thus, conditional on the named imports, **existence** at N=50 is equivalent to the disjunction of those two explicit residual feasibility problems. This is not a claim that either problem is feasible. The converse is a direct construction and does not use C28 or the exclusions.

## 2. Saturation, norm count and actual unitary components

Fix one balanced cut. An entry of a unitary matrix has modulus at most 1. If |U_w|=1, its whole row and column have no other nonzeros. Therefore, for each of the six physical two-party projections π_I, the t P words have t distinct pair values, no E word has one of those values, and the complementary projection has the analogous property. Deleting those t actual rows and t actual columns leaves an n×n unitary residual matrix with

\[
 n=36-t,\quad |E|=50-t,\quad e=|E|-2n=t-22.
\]

A residual row or column has no degree-one support line: its only nonzero would have modulus 1 by its norm and so would have belonged to P. Hence every residual line has at least two E words. Even without N=50 this gives N≥t+2(36−t)=72−t; with N=50, **t≥22**. C28, not this norm count, supplies the opposite endpoint. The pair values occupied by P and E together cover all 36 values of each physical pair, since every row and column of every cut has norm one.

A connected component of the bipartite row/column support graph is square: after permuting rows/columns it is an isolated rectangular block, whose rows and columns are both orthonormal, forcing the two cardinalities equal. Two distinct rows, and likewise two columns, cannot have exactly one common nonzero position. If all degrees in a component are 2, take any degree-2 row with columns c,d. Every other row incident with either c or d must be incident with both. Both columns have degree 2, so they have the same unique other row; the resulting K₂,₂ is isolated. Thus every zero-excess component is a full 2×2 block, not merely an abstract even cycle.

For a connected component of order m>2 write e_c=E_c−2m and let k be the number of degree-2 rows. Since every other row contributes at least one to the excess, k≥m−e_c. Each degree-2 row has a pair of columns with identical row neighborhoods: otherwise another row would overlap it in exactly one position. That common column degree is at least 3, since degree 2 would isolate a 2×2 unitary block. Two distinct degree-2 rows have disjoint column pairs: intersection in one position is forbidden; equal pairs would span their two-column space and isolate a 2×2 block. The disjoint paired columns each contribute at least 1 to column excess, so 2k≤e_c. Consequently

\[
 m-e_c\le k\le\lfloor e_c/2\rfloor,\qquad m\le e_c+\lfloor e_c/2\rfloor. \tag{1}
\]

All component excesses are nonnegative and sum to e. In particular no positive-excess component has e_c=1. If e_c=2, (1) forces m≤3; since m=2 permits at most four entries, m=3 and the component is 3×3 minus one entry. If e_c=3, (1) gives m≤4. For m=4 it forces k=1. The twin pair's common column degree is either at least 4, contributing at least 4 to excess, or exactly 3. In the latter case a row outside their common neighborhood can meet only the other two columns and thus has degree at most 2, giving a second degree-2 row, contradiction. So m=3 and the component is the full 3×3. These statements use actual complex unitarity, not just a no-one-overlap graph filter.

## 3. The entire t23 and t24 exclusions, and the union

At t=23, n=13 and e=1. All component excesses are nonnegative, and no positive component can have excess 1 by (1), contradiction. At t=24, n=12 and e=2. Exactly one component has positive excess; it has excess 2 and is a 3×3-minus-one block. All others are 2×2 blocks. The remaining 12−3=9 rows cannot be partitioned into pairs, contradiction. These exclusions apply directly to each actual unitary cut, including arbitrary phases and moduli, and do not assume C28, no-OLS, an alphabet profile or a phase ansatz.

For a consistency check on the separately imported I25/I27, at t=25 one has n=11,e=3 and §2 forces one full 3×3 plus four 2×2 components in each cut; S3's further all-six-pair incidence and matching argument is the load-bearing I25 import. At t=27, n=9,e=5. Since excess 1 cannot occur, positive-component excesses are either 3+2 or 5. In the first case §2 gives two order-3 components, leaving an odd number of rows for 2×2 blocks. In the second, (1) gives m≤7; the remaining zero-excess blocks make m odd, and m=3 cannot hold 2m+5=11 entries. Thus only orders 5 or 7 could remain, and their genuine-unitary exclusions are explicitly imported in I27. These observations do not replace I25's global argument or I27's order-5/7 proof.

Now the integer t lies in {22,23,24,25,26,27,28} by §2 and C28. The above proof removes 23 and 24; I25 removes 25, I27 removes 27, and I28 removes 28. This leaves exactly the **possible count strata** 22 and 26. I26 then restricts the t26 stratum to actual q=4444. The words “possible” and “remaining” mean not excluded by this union; they do not prove realization.

For traceability, S4's t28 disposition describes the nontrivial common-hole/closed-block route: its low-low eight E words form one closed binary four-party subtensor in all three actual cuts, followed by a four-qubit obstruction. The implication to such a common closed block is part of I28, not independently established here. The final obstruction can be checked in writing: a pure four-qubit state with all two-qubit marginals I₄/4 has Pauli weight sums A₀=1, A₁=A₂=0, A₃=12 (each three-party marginal has purity 1/2), and A₄=3 (global purity). Its spin-flipped positive density then has overlap (1−12+3)/16<0 with the original positive density, impossible. This does not show that an arbitrary local binary mask is closed in all cuts. Similarly S5's q5 proof uses an actual common binary core and a full alphabet argument; the same obstruction cannot by itself replace I26.

## 4. Physical incidence convention for the two exact residuals

Let Ω=[6]^4. For any word set X and party pair I let π_I(X) be its set of pair values, and for a pair value a write X(I,a)={w∈X:π_I(w)=a}. In both residuals require disjoint P,E⊂Ω, the stated cardinalities, and for **every** one of the six physical pairs I:

1. |π_I(P)|=|P| (each P value has one P word);
2. π_I(P)∩π_I(E)=∅ and π_I(P)∪π_I(E)=[6]^2.

The complementary pairs are the rows and columns of the same actual flattening. Thus P fixes singleton rows and columns in all three cuts. No relabeling or independently chosen pair graph is allowed to replace a physical word; a global permutation of an original party's labels is harmless only if applied consistently everywhere. The pair-line equations below must use one E-word variable in all the places that word appears.

## 5. The exact t22 physical-support/common-phase iff

Let |P|=22, |E|=28 and impose §4. Require, for every pair I, exactly two E extensions at each of the 14 values of π_I(E). Equivalently in an actual t22 tensor this follows from equality in the norm bound. In each of the three actual E flattenings also require that the entire support graph be seven K₂,₂ components; this is forced by §2 for an actual tensor but is stated explicitly for a prospective support.

For each of the 21 **cut-indexed** K₂,₂ squares choose an orientation

\[
\begin{pmatrix}a&b\\c&d\end{pmatrix}
\]

of its four actual E words. Build A∈Z^{21×28}, one row per square and one column per E word, with +1 at a,d and −1 at b,c. Do not deduplicate rows arising from different cuts. The phrase “square matrix” in S6 refers to square incidences; dimensionally A is a 21×28 rectangular matrix.

**Fixed-support iff.** Such a physical P/E support carries some normalized complex AME(4,6) tensor with N=50,t=22 **if and only if**

\[
 \text{for every }y\in\mathbb Z^{21}\text{ with }A^T y=0,\quad \sum_{j=1}^{21}y_j\equiv0\pmod2. \tag{2}
\]

For necessity start with the original tensor. Its P moduli are 1. In any E square, put s_w=|U_w|². The four unit row/column equations imply s_a=s_d=p and s_b=s_c=1−p with 0<p<1. Writing U_w=√s_w z_w, |z_w|=1, row orthogonality is

\[
 \sqrt{p(1-p)}(z_a\overline{z_c}+z_b\overline{z_d})=0
 \quad\Longleftrightarrow\quad z_a z_d+z_b z_c=0. \tag{3}
\]

Equation (3) is a **phase** identity; U_aU_d=−U_bU_c is generally false when p≠1/2. Write z_w=e^{2πiθ_w}. Across the same 28 word phases, the 21 equations are Aθ=(1/2)1 in (R/Z)^21. Pairing with any integral left-kernel vector yields (2).

For sufficiency, take an integral Smith normal form LAR=D with L,R unimodular. Multiplication by each nonzero diagonal integer of D is surjective on R/Z. The zero rows impose precisely (L(1/2)1)_j=0 mod 1, and those zero rows of L form an integral basis of ker_Z(Aᵀ). Thus (2) supplies a common θ solving all 21 equations. Assign |U_w|=1/√2 for every E word, |U_w|=1 for every P word, use those common E phases and arbitrary P phases, and put zero elsewhere. In every cut the P rows/columns are isolated and the seven E squares are unitary by (3); hence all three 36×36 flattenings are unitary. The norm is 22+28/2=36, so ψ=U/6 is normalized and has precisely 50 nonzeros and t=22.

This iff is an **existence criterion on one fixed support**, not an assertion that the original tensor had flat E moduli. More generally the original moduli may be retained if one common family 0<s_w<1 satisfies s_w+s_{w'}=1 for every actual E pair line; opposite square entries then have equal squared moduli, and (3) is again sufficient together with the same common phase vector. The flat choice simultaneously solves all these norm equations. A merely mod-2 left dependency is not automatically an integral-kernel obstruction, and sign-only phase assignments are a stronger, different system. Changing a square's orientation reverses a row and does not change the even-sum condition.

S7 separately records further **necessary**, not sufficient, t22 refinements: every binary box contains at most seven E words; the E agreement components have size 28 or sizes 12+16; a 12-component's local profile may be 2333 **or 3333**. Its remaining global E-alphabet profiles up to party permutation are 3566, 3666, 4456, 4466, 4555, 4556, 4566, 4666, 5555, 5556, 5566, 5666, 6666. These are optional conditional S7 imports, not assumptions needed for the iff above; S7's stronger F805 gadget/connectedness claims remain unadopted there. They cannot eliminate an actual support merely by treating an arithmetic profile or a partial local gadget as a completion.

## 6. The exact t26/4444 same-tensor residual

Let |P|=26, |E|=24, impose §4 and require every E alphabet to have exactly four symbols. For every w∈E introduce **one shared** squared modulus s_w∈(0,1) and **one shared** phase z_w∈C, |z_w|=1. For each of the six physical pairs I and each a∈π_I(E), impose the norm equation

\[
 \sum_{w\in E(I,a)}s_w=1. \tag{4}
\]

For each such I, distinct pair values a,b, and complement J=Iᶜ, impose the actual row orthogonality equation

\[
 \sum_{c\in[6]^2:\,(a,c),(b,c)\in E}
 \sqrt{s_{(a,c)}s_{(b,c)}}\,z_{(a,c)}\overline{z_{(b,c)}}=0, \tag{5}
\]

where (a,c) denotes the unique four-coordinate word obtained by placing a in I and c in J. An empty sum is zero. Varying I over all six pairs includes both row and column systems of all three cuts. The same s_w and z_w occur in all of them; the saturated P phases are arbitrary. Equations (4)–(5) automatically preclude one-word E lines and one-term overlaps. In an actual t26 cut, S3's separately imported structure gives either two 3×3-minus-one plus two 2×2 blocks, or one connected 4×4/12-entry plus three 2×2 blocks; hence the nontrivial overlap equations have two, three or four terms. The structural classification is a necessary refinement, not a substitute for (4)–(5).

**Fixed-support iff.** A physical q=4444 P26/E24 support carries such an AME tensor exactly when common variables satisfying (4)–(5) exist. Necessity is the norm and orthogonality of the original cut matrices. For sufficiency, use U_w=√s_w z_w on E, any unit phase on each P word, and zero elsewhere. By §4 each P row and complementary P column is isolated; distinct P rows use different columns. Equations (4)–(5) make all remaining rows orthonormal in every balanced cut. Thus all three square flattenings are unitary. Summing (4) over the 10 E pair values of any I gives ∑_{w∈E}s_w=10; hence ||U||²=26+10=36 and ψ=U/6 is normalized, with exactly the stipulated 26 saturated and 24 nonunit entries. The q=4444 restriction is necessary for every actual t26 tensor only by I26; this construction itself is valid without that import.

For an actual t26 tensor S5 additionally gives each party's E-degree multiset 2224 or 2233 and the same-P moment vectors (n₀,n₁,n₂,n₃,n₄)=(0,2,18,6,0), (0,1,21,3,1), or (0,0,24,0,2). These are necessary moment solutions, not realizations. The integral-left-kernel even-parity criterion decides the **two-term phase subsystem only** here; equations involving three/four terms remain coupled to the same positive amplitudes and phases. No choice of separate cut matrices, local graph survivors, or independently consistent per-cut phases proves (4)–(5) jointly feasible.

## 7. Dependency and provenance audit

The union's load-bearing implication is exactly C28 + the written t23/t24 proof + the separately scoped I25, I27, I28, I26. The t22/t26 constructive directions use actual unitary equations and no global t-bound. In every branch the count and pair systems belong to the original U=6ψ; in particular there is no use of a normalized four-qubit subblock as a replacement for the full original tensor. Any such subblock appears only inside the conditional I28/I26 obstruction. S3's historical F800 enumeration and S4/S5's F842 runs are reported local corroboration only; underlying code and results were not opened or independently executed. The S4/S5 same-harness authors are not independent-family, human or kernel reviews.

The historical source caveat is precise: S2 says the separate historical **F127 manifest was not located in the review directory; absence is not proved**. F182's separate implementation followed exposure to the author checker and is **not clean-room**. Route A to the earlier lower-49 statement directly inherits the F127 computer-assisted 4444 normal-form/enumerator coverage boundary. Route B does not directly import F127 in S2's displayed disposition graph, but absence from every transitive input is unestablished; other computer-assisted inputs remain, and neither route is certified computation-free. S2 does not establish that F127 is a necessary input of C28 itself, and no such stronger dependency is asserted here.

If one additionally quotes S2's conditional minimum interval 50–60, one must also import an explicitly scoped universal N≥49 route, the separate actual N49 exact-case exclusions, C28, and the reported 60-support witness with its stated Gram properties; those load-bearing underlying bodies/witness are not in this packet. The optional interval does not follow from the N50 union alone. S2's local N49/t28 F763 check retained six 3444 one-cut support patterns; they were not phase-realizable witnesses and their reported exclusion required the common-complex-tensor argument. No historical exclusion, receipt, prior finding, or transport/process qualification is upgraded by this candidate.

## 8. Exact unresolved boundary

The two complete physical residuals are §§5 and 6, with all their quantifiers over actual four-coordinate words and common variables. The first unresolved decision is whether there exists any P22/E28 incidence support satisfying the 21-row **integral** kernel parity criterion. The other is whether there exists any P26/E24 q=4444 physical support and common positive s/phase z satisfying all six pair systems (4)–(5). Neither existence nor nonexistence is established here. Without C28, exact t>28 branches also remain outside this union. No claim of an unconditional lower bound 50 or a minimum 51 follows merely from this candidate.

## 9. Read declaration, process and scope

Before any mathematical body or reasoning, I read the complete manifest, freeze receipt, final pre-dispatch binding, parent-live metadata, actual-dispatch receipt, and every one of the 22 manifest-listed controls as status/permissions only. I wrote `prebody-ack-v1.md` and separately sent the direct acknowledgment to Main before packet access. I then read the only literal part in order, raw windows 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–150, 151–165, 166–180, 181–182, including its ending. Each display was below 30,000 bytes and at most 15 LF; no clipping occurred and no clipping recovery was needed. These windows include every line of every complete source block:

| ID | Complete packet source | Parent-supplied SHA-256 | Source LF read |
|---|---|---|---|
| S1 | `parent-ame50-t23-t24-entire-excess-and-t22-t26-union-candidate-v1.md` | `5aca1a1ed6d733dad4f17e2c24955829cc177056de57b751b86aaa8ccf7c88dd` | 1–12 |
| S2 | `dispositions/physics-6-conditional-minimum-support-50-to-60-same-tensor-union-parent-v1.md` | `ccbadbf970b31c199b08f8adeeca03e489f345052d204b31a6192af69aa1e6f0` | 1–29 |
| S3 | `dispositions/physics-6-actual-AME50-t25-t27-exclusion-and-excess-frontier-parent-v1.md` | `9dcffb913663a29d438d53354e44aaacff0ba7cd0c5b37d4b803ea98936af336` | 1–33 |
| S4 | `dispositions/physics-6-actual-AME50-t28-entire-common-hole-closed-binary-obstruction-parent-v1.md` | `44a750bb54cf2736b7e170910e7172578587f9338f204b9ce4d450afbaf09619` | 1–19 |
| S5 | `dispositions/physics-6-actual-AME50-t26-entire-q5-exclusion-and-4444-frontier-parent-v1.md` | `67e216de5e5878d13448c261c3ec87ca4e000a9df235f878093bd246043e8321` | 1–22 |
| S6 | `dispositions/physics-6-actual-AME50-t22-common-support-phase-integer-kernel-criterion-parent-v1.md` | `85878560f5fb5cb5b60893aa774b1f961322f8ea10c79aef792c93264e8cd8f9` | 1–21 |
| S7 | `dispositions/physics-6-actual-AME50-t22-binary-box-component-and-alphabet-frontier-parent-v1.md` | `4ae01f3ce54accaff22bc43bffbad6008b8fbd46e210252ddfd6552417c016bb` | 1–16 |

Paths in the table are relative to `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`. The part's parent-recorded SHA-256 is `1f2b9dbdf034ea53e96856e6728631cb6946d3b5c358c198e88247efd24e099e`, 45,583 bytes/182 LF. The supplied binding/receipt hashes and their round-trip claims are administrative evidence, not independent hashes calculated by me and not scientific correctness certificates. The original source bodies and linked files were not opened outside the literal packet. I did not read any genuine held episode or its proof/method/selection/planning/verification/reporting/confidence/downstream consumers. I used no network, external model, scientific code execution, test, compiler, scientific eval, subprocess or child scientific process. No code was prepared, so no prepared-code hash applies. No process deviation is known in this assignment; prior source/process findings remain as recorded, not cured or backdated here.
