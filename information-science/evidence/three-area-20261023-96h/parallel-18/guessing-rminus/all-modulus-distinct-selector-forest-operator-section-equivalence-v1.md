# ORIGINAL R-minus: arbitrary complex single-fibre transport with at most FOUR DISTINCT selectors is exactly a fixed confusion SECTION

Owner **InfoGuessingRminus-2**, info-5. Actual preceding returned `/bin/date`: **Mon Oct 26 09:02:48 PDT 2026**. The complete proof was saved in `resume-checkpoint-076-v1.json` after its actual08:42:34 observation; this is the standalone body, not a backdated freeze.

**Complete exact WRITTEN architecture equivalence, AUTHOR-UNREVIEWED.** ALL integers m>=2, including composites/nonunits. Arbitrary word-dependent complex amplitudes, phases and zeros are allowed. There is **NO** coherence bound, flatness, Fourier, covariance or field assumption. This closes a genuinely broader architecture slice than bounded-coherence transport: with at most four nonzero classes and pairwise DISTINCT prescribed defective physical vertices, universal single-fibre operators cannot bypass the classical simultaneous-SECTION problem.

It does not prove that the required section exists or fails on the four-class hard family. Repeated selectors, multi-fibre support, five-or-more-class cycles and matching depending on the ACTUAL FD subset A remain outside the theorem. **Certified20/3..1847/276 and T300 unmet are UNCHANGED.** No new bound, positive trade, global Hall/no-SECTION theorem, physical quantum witness or numerical result is asserted.

No scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/build/test/CLI/nestedagent/newGO. Every count and finite-dimensional argument below is WRITTEN, not machine-checked.

## 1. Full original graph, baseline and exact conflict interface

The original FULL neighbourhoods are

`N1=234567`, `N2={1,3,7,9,10}`, `N3={1,2,4,8,9}`,

`N4={1,3,5,8,10}`, `N5={1,4,6,9,10}`, `N6={1,5,7,8,9}`,

`N7={1,2,6,8,10}`, `N8={3,4,6,7,9,10}`,

`N9={2,3,5,6,8}`, `N10={2,4,5,7,8}`.

All26 edges, including34, remain; edge9–10 remains absent. Use the ten chosen triangles

`A123, B145, C167, D239, E(2,7,10), F389, G(4,5,10), H(4,8,10), I569, J678`.

Physical tuple orders are `1:ABC,2:ADE,3:ADF,4:BGH,5:BGI,6:CIJ,7:CEJ,8:FHJ,9:DFI,10:EGH`.

Fix ONE integer m>=2. All triangle slots lie in the SAME Z_m. C is the set whose ten triangle sums are zero, of size M=m^20. A syndrome eta prescribes those ten sums; its entire class C_eta is a translate of C and has size M. Every full-neighbour decoder obeys

`x_v=f_v^0(x_N(v))+d_v(eta)`.

Here d_v(eta) is the three-tuple of eta entries for the three triangles containing v. This follows by solving each triangle slot from its other two corners. It implies that an ENTIRE syndrome class is original-FD: two words agreeing on the full N(v) agree at v.

Two different words are **confusing** when some original v has equal FULL neighbour tuple but different FULL own tuple. They are **FD** when no such v exists. For an outside word x the TRUE compulsory deletion set is

`R(x)=union_(v:d_v(eta(x))!=0) F_v(x)`,

`F_v(x)={c in C:c_N(v)=x_N(v)}`.

Thus `(C\D) union A` is original-FD iff A is original-FD and the ACTUAL union `R(A)=union_(x in A)R(x)` is contained in D. We do not replace this union by counts of projections or separately chosen deletion sets.

Define

`K_v={c in C:c_N(v)=0}`.

Baseline decoding forces c_v=0 too, so K_v is supported on the literal anti-neighbours `U_v=V\(N(v) union{v})`.

## 2. The complete positive kernel-intersection graph has girth FIVE

For every distinct v,w put an edge v–w in G_K precisely when `K_v intersect K_w` contains a NONZERO baseline word. Zero intersection here means the subgroup{0}, of cardinality1, not an empty set.

### 2.1 Full local kernel models over every composite modulus

The two hub kernels have all solutions

- K1: `8=(s,t,0),9=(0,-s,0),10=(0,0,-t)`, all other sites0;
- K8: `1=(s,t,0),2=(-s,0,0),5=(-t,0,0)`, all other sites0.

Thus both have exactly m^2 words, with active supports{8,9,10} and{1,2,5}. These formulas are free-parameter descriptions over Z_m; no rank over a field is assumed.

The peripheral anti-neighbours and ALL two-corner triangle traces are

|v|U_v in its actual C4 order|ALL two-corner traces|
|---|---|---|
|2|4,5,6,8|B:45,G:45,H:48,I:56,J:68|
|3|5,6,7,10|C:67,E:7-10,G:5-10,I:56,J:67|
|4|2,7,6,9|C:67,D:29,E:27,I:69,J:67|
|5|2,3,8,7|A:23,D:23,E:27,F:38,J:78|
|6|2,3,4,10|A:23,D:23,E:2-10,G:4-10,H:4-10|
|7|3,4,5,9|B:45,D:39,F:39,G:45,I:59|
|9|1,4,10,7|B:14,C:17,E:7-10,G:4-10,H:4-10|
|10|1,3,9,6|A:13,C:16,D:39,F:39,I:69|

No chosen triangle is wholly in one U_v. A singleton trace forces its slot0. A two-corner trace has one free parameter and its negative at the other corner. Different chosen triangles use disjoint slots, even when packaged at one physical site. Consequently each peripheral K_v has exactly m^5 words for EVERY m; all the displayed parameters are genuinely free.

Two distinct peripheral U-sets intersect in at most two sites. On a two-site intersection, the only surviving baseline freedoms are the chosen triangles containing BOTH sites. On at most one site, there is no nonzero baseline word. This proves the following ENTIRE nonzero-intersection table directly from the ten triangles and eight displayed U-sets:

|kernel pair|two shared physical sites|surviving independent triangle freedoms|intersection cardinality|
|---|---|---|---|
|2–3|5,6|I|m|
|2–7|4,5|B,G|m^2|
|3–4|6,7|C,J|m^2|
|3–9|7,10|E|m|
|4–5|2,7|E|m|
|4–10|6,9|I|m|
|5–6|2,3|A,D|m^2|
|6–9|4,10|G,H|m^2|
|7–10|3,9|D,F|m^2|

For completeness, the only remaining two-site peripheral intersection is `U6 intersect U7={3,4}`. NO chosen triangle contains both3 and4, so `K6 intersect K7={0}`. Every other peripheral pair has at most one shared site and hence zero intersection. Each hub active-support set meets every other U-set in at most one site; all hub/peripheral intersections and the hub/hub intersection are zero. This covers ALL unordered pairs, not a sample of them.

The table reproduces the more general free-intersection calculation in `all-modulus-fixed-fibre-bounded-coherence-obstruction-v1.md`, but the actual table and its reason are supplied here. That theorem's coherence argument is NOT needed below.

### 2.2 Exact global graph shape and the selector consequence

G_K is exactly the union

`3–4–5–6–9–3` and `3–4–10–7–2–3`,

two FIVE-cycles sharing only edge3–4, together with isolated vertices1 and8. The first alternative path from3 to4 is `3–9–6–5–4`, length4; the second is `3–2–7–10–4`, length4. Hence the only simple cycles have lengths5,5,8: either one of those length4 paths plus edge3–4, or both length4 paths. In particular G_K has NO triangle or four-cycle.

> **Kernel-forest fact.** The graph induced by ANY set of at most FOUR DISTINCT physical vertices is a forest.

The word DISTINCT is indispensable. Four classes mapped to fewer physical vertices can produce a class-interaction graph with cycles through duplicated groups. No acyclicity assertion is made about those duplicated labels.

## 3. Universal complex single-fibre certificates and fixed sections

Let eta1,...,eta_k be ANY distinct nonzero syndromes, with `1<=k<=4`. This is not restricted to a selected coefficient region or the thirteen-parameter hard family. Choose pairwise DISTINCT physical vertices v1,...,v_k satisfying `d_(v_j)(eta_j)!=0`.

A universal certificate at these prescribed selectors means assigning EVERY word x of EVERY entire C_(eta_j) a unit vector `z_x in C^C` such that

1. `supp(z_x) subset F_(v_j)(x)` for x in class j;
2. `z_x perpendicular z_y` whenever two DISTINCT outside words x,y are original-FD.

The support condition uses THAT word's actual fibre, not an arbitrary translated or projected deletion set. Amplitudes may depend on the entire x, may vanish arbitrarily, and may be complex. There is NO common phase, locality, covariance, flatness or coherence hypothesis.

A **section at the prescribed witnesses** is ONE set of actual words

`r0=0 in C, r_j in C_(eta_j), r_j,N(v_j)=0`,

such that EVERY pair among r0,...,r_k is confusing. The nonzero selected defects already make r_j confusing with r0 via v_j. The remaining condition is one globally simultaneous pairwise-confusing representative system, not separate pair completions.

> **Theorem FOREST-SECTION-IFF.** A universal certificate at the prescribed DISTINCT selectors exists **if and only if** a fixed section at those SAME prescribed witnesses exists.

Both directions retain every original physical symbol and all full-neighbour observations, over all m>=2.

## 4. Operator-to-section direction: total relations plus the ACTUAL forest

### 4.1 Exact row mass at a single baseline anchor

Each ENTIRE class C_(eta_j) is FD and has M words. Its M assigned unit vectors are pairwise orthogonal in the M-dimensional space C^C. They therefore form an orthonormal BASIS. This is forced, not assumed from a Fourier construction.

At the actual baseline coordinate0 put

`S_j={x in C_(eta_j):z_x(0)!=0}`.

The basis row identity gives

`sum_(x in S_j)|z_x(0)|^2=1`.                  (ROW)

In particular S_j is nonempty. Actual support gives `x_N(v_j)=0` for every x in S_j. Since the selected defect is nonzero, `x_(v_j)=d_(v_j)(eta_j)!=0`; hence EVERY x in S_j is confusing with baseline0. Further, `supp(z_x) subset K_(v_j)` because its fibre has zero full neighbourhood.

### 4.2 A zero kernel intersection makes ALL active endpoint pairs confusing

Suppose `K_(v_j) intersect K_(v_l)={0}`. For x in S_j and y in S_l, their vector supports meet at only the coordinate0. Both coefficients there are nonzero. Therefore

`<z_x,z_y>=conj(z_x(0)) z_y(0)!=0`.

They cannot be an original-FD pair, by the certificate orthogonality condition. Thus

`EVERY (x,y) in S_j × S_l is confusing`.        (ZERO-EDGE)

No generic-phase argument or support count is being substituted for this exact one-coordinate inner product.

### 4.3 Every positive-edge relation is total in BOTH directions

For any two different classes j,l and any x in S_j, there is at least one y in S_l confusing with x. Otherwise x would be original-FD with EVERY y in S_l. Within S_l all words are already FD. The vector family `{z_x} union {z_y:y in S_l}` would consequently be orthonormal. Bessel's inequality at coordinate0 and (ROW) would imply

`|z_x(0)|^2 + sum_(y in S_l)|z_y(0)|^2 <=1`,

that is `|z_x(0)|^2+1<=1`, contradicting x in S_j. The same argument with j,l exchanged proves the reverse assertion.

Thus the actual confusion relation between S_j and S_l has **NO isolated endpoint in either side**. This is stronger than merely knowing one confusing pair exists. The stronger quantifier is exactly what the recursive global construction requires.

### 4.4 One consistent global choice, without pairwise pasting

On the k CLASS labels draw an edge j–l when the corresponding distinct selectors v_j–v_l form an edge of G_K. Because the selectors are injective and k<=4, this class graph is an induced subgraph of G_K and is a FOREST by §2.2.

Root each nontrivial tree. Choose ANY r_j in S_j at its root. Recursively, after a parent r_j has been chosen, choose r_l in the child's S_l confusing with that ALREADY chosen r_j; §4.3 guarantees it for every such parent choice. Choose any element at an isolated class label. Each label is selected exactly once, so no contradictory local choices are glued.

Every graph edge now compares confusingly by construction. Every NONedge has zero kernel intersection and hence EVERY endpoint pair is already confusing by (ZERO-EDGE), including endpoints in different tree components. All chosen representatives also confuse baseline0 by §4.1. They have exactly their original syndromes and the prescribed zero neighbourhoods.

This is ONE full section at the prescribed witnesses. The use of the actual kernel forest, together with total relations, is the complete simultaneous-consistency argument. Pairwise existence alone would not be enough on a cyclic interaction graph.

## 5. Section-to-operator direction: actual true-removal support

Given such a section, for x in class j define

`z_x=|x-r_j>`,

the standard unit vector indexed by the baseline word x−r_j in C. Its full N(v_j) equals x's because r_j is zero there. Its own v_j value differs from x's by the nonzero `d_(v_j)(eta_j)`. Therefore it lies in THAT x's actual conflict fibre `F_(v_j)(x)`, not just the union of a convenient deletion family.

Within each class, x↦x−r_j is injective. For words x,y of different classes, an equal output would imply `x−y=r_j−r_l`. The right side is a confusing difference by the fixed section; therefore x,y cannot be an original-FD pair. Thus all required FD pairs have distinct standard basis vectors and are orthogonal.

The certificate uses the SAME prescribed distinct selectors. This proves the converse and completes **FOREST-SECTION-IFF**. ∎

## 6. Genuine scope boundary and next original representation

This theorem is not the bounded-coherence obstruction in another notation. It allows arbitrarily concentrated, sparse, non-Fourier and entirely WORD-DEPENDENT complex vectors. It uses a different exact mechanism: one-coordinate support intersections, Bessel-totality and the original kernel graph's girth5. It covers any at-most-four-class family when prescribed selectors are distinct, even when the coefficients are degenerate or composite.

It does NOT exclude a section itself. Such a section could lie outside the earlier five-dimensional span and could prove a genuine family Hall theorem. The conclusion is precisely that the stated universal operator architecture is no easier than constructing that SAME full section.

The necessary next representation for a genuinely nonsection operator advantage is therefore one of:

- repeated physical selectors with their simultaneous actual overlap constraints retained;
- support mixing more than one actual conflict fibre per word;
- five-or-more nonzero classes, where the actual kernel-intersection five-cycles can appear;
- transport depending on the ACTUAL chosen FD subset A, rather than one universal assignment to every potential word.

Repeated selectors must NOT be declared solved by the physical-vertex forest: class labels can duplicate a kernel, and the resulting class graph need not be a forest. Distinct defects at a repeated vertex make that particular pair confusing automatically, but this alone does not resolve all constraints to other duplicated groups. Equal-defect pairs may carry further actual no-confusion obstructions, as separately proved in the214LF bounded-coherence packet; none is silently waived.

The original full guessing-number/strict-improvement problem remains open. No full four-class all-selector Hall theorem, arbitrary-family expansion, positive-gain code, upper-bound certificate, entropy-sign theorem, or numerical interval improvement follows from this architecture equivalence. This is the requested exact documented barrier and explicit next representation, not a necessary-condition count advertised as gn progress.

**Certified20/3..1847/276 UNCHANGED; T300 UNMET.** Ordinary finite group/basis/Bessel facts are the named mathematical imports. The graph, triangle decoder, complete kernel-intersection calculation and simultaneous construction are reproduced above. The earlier075 sparse collapse/173 Fourier/214 coherence/M5 negative results are NOT correctness premises; no old title/hash is being used as a reconstructed proof.

All new work is AUTHOR-WRITTEN/UNREVIEWED, not formal/kernel/human/configured-family/executable/novelty/priority or parent adoption. The actual v120 RETURN→NEW062→separate06:45:36 ACK/SEND sequence preceded resumed primary source/math. Permanent v25/024/034,parentv101,allv9/v10/v11/laterthroughv34/ZEROscience/N4 UNKNOWN and every correction history remain. No old frozen file was edited, no clock/backdating/global cognition-runtime census or process cure is claimed.

Same original18/exclusive ownroot/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38/HOLD/actualsubstantivecheckpoints<=30min. No early final park, publication/Git/config/deletion/CLI/nestedagent/scientific program or newGO. Original research continues at the actual repeated-selector/multiple-fibre/A-dependent Hall or positive-trade gap.
