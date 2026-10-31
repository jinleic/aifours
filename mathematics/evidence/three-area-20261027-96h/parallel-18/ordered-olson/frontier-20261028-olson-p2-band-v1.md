# The o_π=p+2 projection stratum: reflection-only or a two-rotation selector

Owner **MathOlson-2-2**. Native `/bin/date` immediately before writing: **Wed Oct 28 21:34:41 PDT 2026**. NEW **WRITTEN candidate**, self-contained, with bounded same-model checks (§7). Not a reviewer verdict, formal proof, novelty claim, full L_RES result or ordered-Olson proof. Mandatory before-source: `frontier-20261028-olson-actual-block-fatal-correction-v1.json`, SHA256 `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e`. All run notions are cyclic reflection-only PROJECTION notions; no historical actual `o_F/e_F`, f111 material or floor is used.

Conventions as in `frontier-20261028-olson-spare-sector-band-v1.md` (SHA256 `7ba998ffad4b8c52754675f92e8ed34ceb70f96728420bceeadbd85ec3b20802`) but NOTHING from that file is an input here: `ρ_y=(y,0)`, `σ_y=(y,1)`, `(x,e)(y,b)=(x+(−1)^e y,e+b)`; a rotation lies in the gap after the preceding reflection and that gap is assigned to the preceding reflection's projected run; singleton gaps = no two rotation letters cyclically adjacent. An identity selection may be exhibited in any cyclic cut order.

## 1. Theorem P2

Let p be an odd prime and W a word with exactly F=3p−2 reflections, R>=p+1 rotations and singleton gaps. If its cyclic projection has exactly `o_π=p+2` odd runs, then W has an original-order identity subsequence of exactly 2p letters; it is reflection-only or uses exactly two rotation letters.

No rotation value is restricted (0 allowed). No caller predicate (OLD/SEL/IPGEN/GS/DS3/REF) is assumed.

## 2. Tools

**Lemma C (two-rotation piece criterion).** Let r1≠r2 be rotation letters with exponents u,v; cut before r1; let X (resp. Y) be the linear reflection sequence strictly between r1 and r2 (resp. after r2), each split into maximal constant **pieces**; let `o_pc` be the number of odd-length pieces of X and Y together. Let T_X, T_Y be sets of pieces, `T=T_X∪T_Y`, `|T|` even, `|T|<=2p−2`, with

* (cap) `o_T−e_T >= o_pc−p` (odd-/even-length pieces in T), and
* (eq) `u+v+alt(T_X)+alt(T_Y)=0` if `|T_X|` is even, `u−v+alt(T_X)−alt(T_Y)=0` if `|T_X|` is odd,

where `alt(t_1,…,t_k)=t_1−t_2+t_3−…` of labels in linear order. Then W has an identity selection consisting of r1, r2 and 2p−2 reflections.

*Proof.* Choose `k_π≡[π∈T] (mod 2)`, `0<=k_π<=|π|`, `Σk_π=2p−2`: the minimum is `|T|`, the maximum is `F−e_T−(o_pc−o_T)>=2p−2` by (cap), and every value of the right parity between is reached in steps of 2. Select the first k_π reflections of each piece. They are consecutive in selection order with one label, so a piece contributes σ_label if k_π is odd and 1 otherwise; unselected rotations are skipped. Hence X contributes `ρ_(alt T_X)` or `σ_(alt T_X)` and Y likewise, and `ρ_uρ_aρ_vρ_b=ρ_(u+a+v+b)`, `ρ_uσ_aρ_vσ_b=σ_(u+a−v)σ_b=ρ_(u+a−v−b)`. QED.

**REF step.** If four odd runs have labels with cyclic alternating sum 0, take one reflection of each (each odd run of length L keeps `(L−1)/2` disjoint consecutive equal pairs besides it) and all `(F−o_π)/2=p−2` equal pairs: `4+2(p−2)=2p` reflections with product 1.

**Directed differences.** If a linear sequence contains every element of F_p, then for every t!=0 it has entries `y_i` before `y_j` with `y_i−y_j=t` (first occurrences form a linear order of F_p; otherwise each `x−t` precedes x, impossible around the t-cycle). Write `D(t)`.

**Three-c pigeonhole.** If a linear sequence contains three entries c and an entry τ!=c (or three c's when τ=c), then two c's lie on one side of τ, so `(c,c,τ)` or `(τ,c,c)` (resp. `(c,c,c)`) has alternating sum τ.

## 3. Lemma Q (multiplicity)

Let z be a cyclic sequence of `p+2` elements of F_p with NO zero quadruple (four positions in cyclic order with alternating sum 0). Then some c occurs exactly three times and every other element of F_p exactly once.

(M1) No value occurs four times (`a−a+a−a=0`). (M2) If a occurs three times and b!=a twice, the two b's cut the cycle into two arcs, one containing two a's, giving cyclic order `a,a,b,b`, sum 0. (M3) Two values occurring twice must interleave (`a,b,a,b`), else `a,a,b,b` again. (M4) If no value occurs three times, let s be the number of doubled values; support `p+2−s<=p` forces s>=2. Fix doubled a and any doubled b!=a, in cyclic order `a1,b1,a2,b2`, and put `x=2a−b` (distinct from a,b as p is odd). An occurrence of x in arc `(b2,a1)` gives `x,a1,b1,a2` with sum `x+b−2a=0`; in `(a1,a2)` (either side of b1) gives `a1,x,a2,b2` with `2a−x−b=0`; in `(a2,b2)` gives `a1,b1,a2,x`. So the s−1 distinct values `2a−b` are absent, while only `p−(p+2−s)=s−2` values are absent: contradiction. Hence a value c occurs three times (M1: not four), every other value at most once (M2), so the remaining `p−1` entries are the distinct elements of `F_p∖{c}`. QED.

## 4. Proof of Theorem P2

Pair capacity is `(F−o_π)/2=p−2`. If the cyclic odd-run label sequence has a zero quadruple, the REF step finishes. Otherwise, by Lemma Q, the odd-run labels are (★): c three times and every other value once.

### 4.1 Some projected run has two occupied gaps (H)

Let G (label e) be such a run, and r1, r2 its first two occupied gaps in G's order. Write `G=P⁻ r1 X r2 P⁺` with `a=|P⁻|>=1`, `x=|X|>=1`, `b=|P⁺|>=0`. X is one piece; Y starts with P⁺ (if b>0), ends with P⁻, and every other projected run is one whole piece of Y. Let S be the pieces of the other odd runs. By (★): if G is even, S has labels c×3 and all values; if G is odd with e=c, S has c×2 and all values; if G is odd with e!=c, S has c×3 and all values except e. Then `o_pc−p = 2−[G odd]+#odd{a,x,b}`; set `s=u+v`.

* **H-i** G even, a,x,b even (`o_pc−p=2`): T_X=∅, T_Y=`D(−s)` in S, or two c's if s=0.
* **H-ii** G even, x odd (`=4`): T_X={X}, T_Y=`(c,c,τ)` or `(τ,c,c)` in S with `τ=u−v+e`.
* **H-iii** G even, x even, a,b odd (`=4`): T_Y=`(P⁺,y,y',P⁻)` with `y,y'∈S`, `y−y'=s` (`D(s)`, or c,c). Then `alt=e−y+y'−e=−s`.
* **H-iv-a** G odd, only x odd (`=2`): if `β=e+u−v` labels a piece of S take T_X={X}, T_Y={β}. Otherwise e!=c and u=v (only e can be missing); take T_X={X} and T_Y=`(P⁺,c,c)` if b>0, else `(c,c,P⁻)` (a is even, so a>=2). Here `o_T−e_T=1+2−1=2` and `alt T_Y=e`.
* **H-iv-b/c** G odd, x even, exactly one of a,b odd (`=2`): the odd Y pieces (S plus the odd P-piece, label e) contain every value and a repeated label; T_Y=`D(−s)` or two equal labels.
* **H-v** G odd, a,x,b odd (`=4`): T_X={X}, `τ=u−v+e`. If τ=e: T_Y=`(P⁺,c,c)`. Otherwise τ labels a piece of S, and Y has at least three c-labelled odd pieces (three in S, or two in S plus P⁺,P⁻ when e=c): three-c pigeonhole.

### 4.2 Every projected run has at most one occupied gap (sectors)

Canonical spares: an odd run with no gap spares its last reflection; one with its unique gap after its k-th reflection is cut there and spares the last reflection of its odd piece. Each odd run then has `(L−1)/2` pairs not crossing its gap; an even run is paired from its start. The p+2 spares cut the cycle into p+2 sectors. For selected r1, r2 assigned to runs G1≠G2, X contains `G1⁺` (start) and `G2⁻` (end), Y starts with `G2⁺` and ends with `G1⁻`; λ := number of even `G_i` cut after an odd-indexed reflection; such cuts create two odd pieces, one in X and one in Y. Every odd run contributes exactly one odd piece (the one holding its spare) and each λ-cut contributes two, so `o_pc=(p+2)+2λ` and `o_pc−p=2+2λ`.

**Case A: a sector holds two rotations**; r1, r2 the first two in it. No odd run lies strictly between them, an odd `G1` has its spare in `G1⁻` and an odd `G2` in `G2⁺`, so all p+2 spares lie in Y and the odd pieces of X are exactly the λ split pieces.
* λ=0: T_Y=`D(−s)` among spares (all values present) or two c-spares.
* λ=1: the split piece `x_in` (label e) is X's only odd piece; T_X={x_in}, T_Y=`(c,c,τ)`/`(τ,c,c)` among spares with `τ=u−v+e`; `o_T=4`.
* λ=2: X's odd pieces are `G1⁺` (e1, first) and `G2⁻` (e2, last); Y's first and last odd pieces are `G2⁺` (e2) and `G1⁻` (e1). T_X both, T_Y=`(G2⁺,y,y',G1⁻)` with spares `y−y'=s` (or c,c): `alt T_X+alt T_Y=(e1−e2)+(e2−y+y'−e1)=−s`; `o_T=6`. (For p=3 this case cannot occur: F=7, o_π=5 leave only one even run; for p>=5, `|T|=6<=2p−2`.)

**Case B: every sector holds at most one rotation.** Then R<=p+2 and at most one sector is empty; at most two spares border it, so some c-spare z borders two nonempty sectors. Let r1, r2 be their rotations; z is the only spare between them. X's odd pieces: z's piece and the λ split pieces; Y holds the other p+1 spares (c twice and every other value, so all of F_p) and the split partners.
* λ=0: T_X={z}, T_Y={spare labelled `c+u−v`}.
* λ=1: T_X = z and the split piece, `alt T_X=±(c−e)`; T_Y=`D(t)` or c,c with `t=−(s+alt T_X)`; `o_T=4`.
* λ=2: X's odd pieces in order `G1⁺(e1), z(c), G2⁻(e2)`; T_X all three; `τ=u−v+e1−c+e2`; Y's first odd piece is `G2⁺` (e2); T_Y=`(G2⁺,y,y')` with spares after it, `y−y'=e2−τ` (or c,c), so `alt T_Y=τ`; `o_T=6`. As in Case A, λ=2 needs two even runs, hence p>=5 and `|T|=6<=2p−2`.

In every case (cap) holds with equality and (eq) holds by the displayed arithmetic; Lemma C gives the selector. QED.

## 5. Consequence and remaining frontier

With the separate, unreviewed, CONDITIONAL `o_π<=p` band of `frontier-20261028-olson-spare-sector-band-v1.md` (SHA256 `7ba998ffad4b8c52754675f92e8ed34ceb70f96728420bceeadbd85ec3b20802`, which itself names unreviewed inputs for one subcase), every word with F=3p−2, R>=p+1 and singleton gaps and `o_π<=p+2` would have a selector. Theorem P2 itself needs none of those inputs. **Open: `o_π>=p+4`.** A bounded exploratory kernel probe (not frozen, not relied on) found reflection-only-failing projections with `o_π=p+4` at p=5, so that stratum is not vacuous for REF; this is stated as an observation only.

For REF-failing words with `o_π=p+2`, Lemma Q and the REF step give exactly the multiset (★). A recorded finite check (§7) also confirms, for p=3,5 exhaustively, that a cyclic length-(p+2) sequence has no zero quadruple iff it is a rotation of `c,c,c,c+d,…,c+(p−1)d`; this sharper AP shape is NOT used in the proof above.

## 6. What is not claimed

No claim about historical actual-block counters, OLD/SEL/IPGEN/GS/DS3, R=p+1 words with `o_π>=p+4`, non-singleton gaps, L_RES as a whole, ordered Olson, or novelty. Not independently reviewed.

## 7. Exact bounded checks (integers mod p)

* Structure check: `frontier-20261028-olson-p2-ref-structure-experiment.py` SHA256 `31f8a926150fa3306e92e830585aaea4150a65ec50e84cf3488587c18006a0b4`, data SHA256 `3f9ae02e732f4adbf28ce1ec8ae8b7fe55b8d1ef19fadfe362ef9e84e8356793`; independent checker `frontier-20261028-olson-p2-ref-structure-checker.py` SHA256 `19d2bb5ec86e9f70a2e7b3b18e04bfe8ecbd554d4806744860df92912d70dedb`, result SHA256 `7a6a57cca81b9661b2dcf788da269f84dec0d822af312e57eb48bfc078f8f3d0`: for p=3,5 the zero-quadruple-free normalised sequences (10 and 28) equal the generated AP-with-triple class; 100 sampled REF-failing p=5,7,11 projections were re-decided by an independent RUN-level piece-criterion DP; two controls.
* Construction checks: random producer `frontier-20261028-olson-p2-band-experiment.py` SHA256 `bbb46b620978088dd762ccc29581a4ba43ca1b716173501ba57120d1322e1744` (data `f1f7997679fbfc0fefa5038cd776b47e612d44c7216b8fcfb0ab9b8fd5a706ad`, 1800 words), direct designs `frontier-20261028-olson-p2-band-design-experiment.py` SHA256 `5962e483a9940d23df8c8f0546424cd9b36deb524b46cb336daf1e0f750ea2df` (data `4f0466b61c82214faa998386b3f064a7288aaeb768669e774ba4ea4ed1901147`, 560 words) and `frontier-20261028-olson-p2-band-design-b0-experiment.py` SHA256 `b85707bff7d88345dd90aa736adb2ecc0a90ba078ae3d36ebe594e5fe2c3b901` (data `959ca1710e64262218ddecb99a48aeaa5d7d7c623ce5225f3c4b35ba90c82a83`, 160 words). The design scripts import the random producer's `construct()` (same producer family) and the gamma generator of `frontier-20261028-olson-p2-band-targeted-experiment.py` (SHA256 `b04c01cedd5240b7bd2b64bda6201d02fc4955c05e95bccb96cb025d6d7cdbc4`), whose own main run timed out at 900 s with NO output and is superseded.
* Separately written checker `frontier-20261028-olson-p2-band-checker.py` SHA256 `eb61a4f6485a7c787068d255e061f78d4ce8e7f9f6fefb7912d1c5cce356db50` imports no producer code; result SHA256 `650a2ff568f367dfcbeb66efe923136ce1278cef246b170c80f7627c0329b8b9`: `PASS_INDEPENDENT_P2_BAND`, 2520 words at p=5,7,11,13, every branch re-derived from the word and every original-order product multiplied: REF 1197, H-i 13, H-ii 313, H-iii 23, H-iv-a 55, H-iv-a(γ) 123, H-iv-b/c 48, H-v 78, A/λ0 32, A/λ1 189, A/λ2 121, B/λ0 164, B/λ1 124, B/λ2 40; duplicate-index, altered-rotation and altered-branch controls failed as intended. p=3 is not in these checks.

**END — Theorem P2; o_π>=p+4 open.**
