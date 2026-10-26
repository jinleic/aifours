# R-minus: uniform two-syndrome transport and no-positive-gain theorem

Owner `InfoGuessingRminus`, info-5. Actual `/bin/date` before this freeze: `Sun Oct 25 08:20:36 PDT 2026`.

**NEW WRITTEN CANDIDATE. No scientific eval/interpreter, arithmetic/symbolic program, enumeration, solver, certificate replay, external-model CLI or nested agent.** All finite tables and algebra below are written deductions from the literal26-edge graph. Metadata clocks/hashes/source reads only. No named GO exists.

## 1. Exact theorem and assurance boundary

Fix ANY integer m>=2, including composite m. Let C=C_m be the actual ten-triangle parity strategy on the physical alphabet Z_m³ from the accepted literal trade interface. Let sigma,tau be ANY TWO DISTINCT NONZERO vectors of Z_m^10, and write C_sigma,C_tau for their parity-syndrome classes. Let

`A_sigma subset C_sigma`, `A_tau subset C_tau`, `A=A_sigma union A_tau`.

The subsets may be arbitrary and nonlinear; neither class need be fully used. Suppose A satisfies ALL original graph FDs.

**Theorem TWO.** There are two translations, chosen from m,sigma,tau and the literal graph and INDEPENDENT of the chosen subsets, whose restriction gives an injection

`I:A -> R_m(A)`.

Here R_m(A) is the ACTUAL baseline-conflict union of the prior trade theorem. Consequently

`|A|<=|R_m(A)|`,                                         (TWO)

so no replacement using at most TWO nonzero syndrome classes improves |C_m|=m^20. Equivalently every FD-consistent code contained in C_0 union C_sigma union C_tau has at most m^20 words.

The overlap control is proved, not assumed: any coincidence between the two translation images forces the original FULL-neighbour FD to fail at one specified physical vertex. The separate one-syndrome injections are NOT merely summed.

This proves a uniform two-syndrome obstruction only. It does NOT prove a global Hall inequality for three or more nonzero syndromes, unrestricted gn=20/3, or any change to the imported interval20/3..1847/276. The new theorem has not received its own independent written reconstruction, formal/kernel/human/cross-vendor review, finite-certificate or novelty clearance.

### Named structural inputs and actual readings

- `literal-triangle-cover-gluing-first-failure-v1.md`, SHA256 `9db0186860b6ef04bc485830a6e49efd5043031f49d144453a733da70c378b06`: actual C_m, full-neighbour projection, exact F_S and replacement criterion.
- Complete actual239-LF PhysicsRQLS10 reconstruction, `physics/evidence/three-area-20261023-96h/parallel-18/rqls10/peer-review-rminus-literal-fiber-trade-v1.md`, observed SHA256 `66257abf863029177d0316293885ef5c1f674301e04915480033f6bafb6e1fec`.
- Complete actual33-LF parent disposition `nl242-intrinsic-rminus-trades-parent-v1.md`, observed SHA256 `c5ce43eb645e390863d4bf47e8b71f043b6c97e2724ddd777ecd6527580af928`, Section2. These sources support only the previous structural interface, not the new C4/transport theorem.
- Literal graph input `inputs-v1.json`, frozen SHA256 `bdc4cd14d20e2401971a7354c2a6239106fbe2be158b50921d5c486c6a086be6`.

The needed slot/extension facts are restated with proofs below. No I1, I2/T300, entropy/KL minimizer, group classification or historical program is used. T300's independent executable/triple gate remains UNMET.

## 2. Literal graph and parity coordinates

The physical neighbourhoods are

`N1={2,3,4,5,6,7}; N2={1,3,7,9,10};`

`N3={1,2,4,8,9}; N4={1,3,5,8,10};`

`N5={1,4,6,9,10}; N6={1,5,7,8,9};`

`N7={1,2,6,8,10}; N8={3,4,6,7,9,10};`

`N9={2,3,5,6,8}; N10={2,4,5,7,8}`.

The chosen actual cover triangles are

`T1=123, T2=145, T3=167, T4=239, T5=(2,7,10),`

`T6=389, T7=(4,5,10), T8=(4,8,10), T9=569, T10=678`.

Each physical vertex has three incident slots. The incident index lists are

`1:123; 2:145; 3:146; 4:278; 5:279;`

`6:3,9,10; 7:3,5,10; 8:6,8,10; 9:4,6,9; 10:5,7,8`.

Here e.g. `2:145` means triangle indices1,4,5, not vertex labels. All neighbour equalities below concern ENTIRE physical three-component symbols, not selected scalar slots.

For any word x define the triangle syndrome

`sigma_T(x)=sum_(u in T) x_(u,T) in Z_m`.

The ten sums involve disjoint slot triples, so every syndrome is attainable, and each class C_sigma is a translate of the kernel C. For each vertex define the three-component defect vector

`d_v(sigma)=(sigma_T : T incident to v)`

in its physical slot order. The baseline decoder on that neighbourhood is

`f^0_(v,T)(z_N(v))=-z_(a,T)-z_(b,T)` for T={v,a,b}.

For EVERY x in C_sigma,

`x_v=f_v^0(x_N(v))+d_v(sigma)`.                           (D)

Thus each syndrome class itself has exact full-domain graph decoders f_v^0+d_v(sigma), and every subset of one class is FD-consistent. The new constraint is the interaction between classes.

## 3. EXACT cross-class A-FD and exact confusion-fiber overlap

### 3.1 Cross-class FD is a full-neighbour projection exclusion

Take x in C_sigma,y in C_tau. If x_N(v)=y_N(v), (D) gives

`x_v-y_v=d_v(sigma)-d_v(tau)`.

Therefore A_sigma union A_tau is FD-consistent IFF, for every vertex with distinct defect vectors,

`pi_N(v)(A_sigma) intersect pi_N(v)(A_tau)=empty`

`whenever d_v(sigma)!=d_v(tau)`.                          (CFD)

When the defects agree, equal full-neighbour tuples give equal physical values and are safe. Within-class FDs already hold by (D). Thus (CFD) is an exact necessary-AND-sufficient cross-syndrome constraint, including zero defects and composite moduli. It is not a projection-count relaxation.

### 3.2 Exact baseline-fiber intersection

For d_i(sigma)!=0 put

`F_i(x)={c in C:c_N(i)=x_N(i)}`;

for d_j(tau)!=0 define F_j(y) similarly. Their intersection has the following exact form. Let S=N(i) union N(j). First the prescriptions from x and y must agree on N(i) intersect N(j). If not, the intersection is empty. If they agree, combine them into a prescribed physical assignment z on S.

For each chosen T, exactly r_T=|T intersect S| of its OWN slots are fixed. A baseline extension exists IFF every fully fixed T (r_T=3) already has parity0. When it exists, the exact intersection size is

`m^(sum_T max(2-r_T,0))`.                                (FS)

Indeed a triangle with0,1,2 prescribed slots has m²,m,1 completions; with3 it has one iff its parity vanishes. Slots of distinct triangles are independent, even when physically packaged at a common vertex. This proves the stated iff and count without a program.

Different-vertex confusion fibers CAN overlap under these tests. Nothing below assumes that the whole sets R_m(A_sigma),R_m(A_tau) are disjoint. We instead choose two specific translation images whose coincidences violate (CFD).

### 3.3 The full-neighbour extension fact

For every chosen T and every vertex v, T is not contained in N(v): the literal common-neighbour table in the previous packet proves this. It also follows for the peripheral vertices used below from the explicit trace tables. Consequently every assignment on N(v) extends to C by (FS). One can fill available free slots with0 and solve the last triangle slot by subtraction. This is the actual FULL property, not an alphabet-field rank assertion.

## 4. A literal C4 trace lemma for disjoint chosen triangles

Write `U_v=V minus (N(v) union {v})`, the FOUR anti-neighbours at any peripheral vertex v used here. The following are induced4-cycles, with NO diagonals, directly from the26-edge neighbourhood list:

|v|U_v, in cyclic order|Cycle edges|Absent diagonals|
|---|---|---|---|
|2|4,5,6,8|45,56,68,84|46,58|
|5|2,3,8,7|23,38,87,72|28,37|
|6|2,3,4,10|23,34,4-10,10-2|24,3-10|
|9|1,4,10,7|14,4-10,10-7,71|1-10,47|
|10|1,3,9,6|13,39,96,61|19,36|

Here is the COMPLETE literal table needed for the lemma. For each first triangle T0 choose v in T0 as shown; the table lists EVERY chosen triangle disjoint from T0 and its trace on U_v. Every nonsingleton trace is an EDGE of that induced C4, and there is at most ONE singleton trace.

|T0|chosen v|ALL disjoint chosen triangles and their traces T intersect U_v|Possible singleton|
|---|---:|---|---|
|T1=123|2|T7:{4,5}; T8:{4,8}; T9:{5,6}; T10:{6,8}|none|
|T2=145|5|T4:{2,3}; T5:{2,7}; T6:{3,8}; T10:{7,8}|none|
|T3=167|6|T4:{2,3}; T6:{3}; T7:{4,10}; T8:{4,10}|{3}|
|T4=239|2|T2:{4,5}; T3:{6}; T7:{4,5}; T8:{4,8}; T10:{6,8}|{6}|
|T5=(2,7,10)|2|T2:{4,5}; T6:{8}; T9:{5,6}|{8}|
|T6=389|9|T2:{1,4}; T3:{1,7}; T5:{7,10}; T7:{4,10}|none|
|T7=(4,5,10)|5|T1:{2,3}; T3:{7}; T4:{2,3}; T6:{3,8}; T10:{7,8}|{7}|
|T8=(4,8,10)|10|T1:{1,3}; T3:{1,6}; T4:{3,9}; T9:{6,9}|none|
|T9=569|6|T1:{2,3}; T5:{2,10}; T8:{4,10}|none|
|T10=678|6|T1:{2,3}; T2:{4}; T4:{2,3}; T7:{4,10}|{4}|

These rows are obtained by comparing the ten explicit vertex triples with T0 and intersecting with the displayed U_v. For example, T4=239 is disjoint exactly from T2,T3,T7,T8,T10; for v2 their traces are45,6,45,48,68. T8=4810 is disjoint exactly from T1,T3,T4,T9; for v10 their traces are13,16,39,69. The table makes both the disjointness universe and every trace visible; no unlisted triangle catalogue or source-graph symmetry is used.

**Lemma TRACE.** Fix T0 and its selected v. For EVERY nonempty family B of chosen triangles disjoint from T0, there is a physical vertex w such that

1. w lies in U_v and in at least one triangle of B;
2. NO triangle in B is wholly contained in N(v) union N(w).

**Proof.** If B contains the row's possible singleton trace{a}, take w=a. Otherwise take w to be any vertex of any trace in B. Then w is in U_v and in a triangle of B. A singleton trace, when present, is{w}, not contained in N(w) because the graph is loopless. Every other trace is a C4 edge. The neighbours of w WITHIN an induced C4 are an independent pair, so no C4 edge is contained in N(w) intersect U_v. Thus for every T in B, some vertex of T intersect U_v lies outside N(w). It also lies outside N(v), by definition of U_v. Hence T is not contained in their union. This proves BOTH required properties. ∎

This is the essential NEW graph-specific overlap lemma. It concerns the literal ten triangles and actual non-neighbour4-cycles, not arbitrary linear codes or generic minimizers.

## 5. Constructing actual syndrome representatives with prescribed zeros

For any syndrome eta choose a canonical word h_eta by placing eta_T at the lowest-labelled vertex slot of each T and0 at the other two. Thus its syndrome is eta.

For any vertex v, FULL supplies k in C with k_N(v)=(h_eta)_N(v). Set r_eta=h_eta-k. Then

`(r_eta)_N(v)=0`, `(r_eta)_v=d_v(eta)`.                   (R1)

The second equality follows from (D) with the zero neighbourhood input, since f_v^0(0)=0. No denominator or scalar division is used.

More generally, suppose for vertices v,w no NONZERO triangle of eta is wholly contained in S=N(v) union N(w). Every chosen triangle fully contained in S then has eta_T=0, so the prescribed values (h_eta)_S satisfy every fully fixed baseline parity. By (FS) they extend to some k in C. Set r_eta=h_eta-k. This gives

`(r_eta)_N(v)=(r_eta)_N(w)=0`,

`(r_eta)_v=d_v(eta)`, `(r_eta)_w=d_w(eta)`.               (R2)

The baseline extension can be chosen deterministically: match the fixed slots, put any available free slot to0 in label order, and solve the last slot in each triangle by subtraction. These choices depend only on eta and the selected vertices, not on A_sigma,A_tau. Thus the transports below have the full uniform quantifiers in Theorem TWO.

## 6. Proof of Theorem TWO — all exact cross-syndrome overlaps controlled

### Case I: a common vertex distinguishes all three classes

Suppose some vertex v has

`d_v(sigma)!=0`, `d_v(tau)!=0`, `d_v(sigma)!=d_v(tau)`.

Use (R1) to choose representatives r_sigma,r_tau of the respective syndromes, both zero on N(v). Define

`I_sigma(x)=x-r_sigma`, `I_tau(y)=y-r_tau`.

Each is a fixed translation into C. It is injective on its own class, preserves the FULL N(v) tuple, and changes the vertex value by its nonzero defect. Hence

`I_sigma(x) in F_v(x) subset R_m(A_sigma)`,

`I_tau(y) in F_v(y) subset R_m(A_tau)`.

If I_sigma(x)=I_tau(y)=c, then x_N(v)=y_N(v)=c_N(v), while

`x_v-y_v=d_v(sigma)-d_v(tau)!=0`.

This contradicts the actual FD on A at v, equivalently (CFD). Therefore the two image sets are disjoint. Their combined translation map is the required injection A into R_m(A).

### Case II: no vertex distinguishes all three classes in that way

Suppose Case I never occurs. Since sigma and tau are distinct, choose a triangle T0 where their syndrome entries differ. They cannot BOTH be nonzero and unequal there, since any vertex of T0 would satisfy Case I. After swapping the two syndrome names if necessary, we have

`sigma_(T0)!=0`, `tau_(T0)=0`.

For EVERY vertex u in T0, d_u(sigma) is nonzero. If d_u(tau) were nonzero, the two vectors would differ at component T0 and give Case I. Hence

`d_u(tau)=0 for EVERY u in T0`.                          (EX)

Therefore EVERY nonzero triangle of tau is DISJOINT from T0. Let B be the nonempty family of those triangles (tau is nonzero). Select v from T0 by the literal table in Section4; then

`d_v(sigma)!=0`, `d_v(tau)=0`.

Lemma TRACE supplies w in U_v on a nonzero tau triangle, so d_w(tau)!=0, and ensures no nonzero tau triangle is wholly contained in N(v) union N(w).

Use (R2) for tau and these vertices to choose r_tau zero on BOTH full neighbourhoods. In particular

`(r_tau)_v=0`, `(r_tau)_w=d_w(tau)!=0`.

Use (R1) for sigma at v to choose r_sigma zero on N(v), with

`(r_sigma)_v=d_v(sigma)!=0`.

Define the same fixed translations

`I_sigma(x)=x-r_sigma`, `I_tau(y)=y-r_tau`.

The first maps every x into its actual conflict fiber F_v(x). The second maps every y into its actual conflict fiber F_w(y), because it preserves the FULL N(w) tuple and changes w by a nonzero defect. Both map into the baseline C and are individually injective.

Now suppose their images coincide at c. BOTH representatives are zero on N(v), so

`x_N(v)=y_N(v)=c_N(v)`.

But at v their values differ by

`x_v-y_v=(r_sigma)_v-(r_tau)_v=d_v(sigma)!=0`.

Again the original full-neighbour FD on A is violated. Thus these image sets are disjoint too. The union gives an injection A into R_m(A), proving (TWO) in Case II. ∎

### What has and has not been assumed about image overlap

The maps are defined by two fixed translations on the two WHOLE syndrome classes. They need not be jointly injective on their unrestricted union; any cross coincidence would itself be a forbidden FD pair. Their restriction is jointly injective on EVERY FD-consistent A. This is exactly the qualifier needed and exactly where A-FD is used.

No claim that R_m(A_sigma) and R_m(A_tau) are disjoint was made. Other points of those removal sets may overlap arbitrarily under (FS). The explicit translations pick disjoint subsets of the removal union, with collisions ruled out at the SAME chosen v. This is why the argument is not the invalid summation of two separately available injections.

## 7. Consequences for actual finite strategies and exact remaining gap

For any retained baseline set C minus D and outside A, the already supported replacement criterion is

`(C minus D) union A is FD-consistent`

`iff A is FD-consistent and R_m(A) subset D`.

It also follows directly by splitting word pairs into baseline/baseline, outside/outside, and cross pairs, so no extra higher-order compatibility premise is needed. With at most two nonzero syndromes, Theorem TWO gives

`|(C minus D) union A|=m^20-|D|+|A|<=m^20`.

Thus arbitrary nonlinear FD subsets of the union of two nonzero classes cannot improve the baseline, for EVERY integer m>=2. No field property, scalar-linear restriction, full-coset assumption, independent physical vertices or generic entropy assertion enters the proof.

An improving strategy relative to this literal baseline must now use at least THREE distinct nonzero triangle syndromes. The old cubic-alphabet equivalence continues to preserve the existential strict-improvement question over all finite alphabets, but a general competitor may use arbitrarily many syndromes. A two-syndrome theorem alone is therefore NOT global20/3 optimality.

The first remaining obstruction is explicit. With three or more classes, choosing pairwise transports separately does not make their images simultaneously disjoint: the representatives and comparison vertex can depend on the pair. No common multi-class transport, global Hall expansion, or positive-gain multi-syndrome FD trade is supplied. Proving either requires new literal-graph content and cannot be inferred from this pairwise result.

The imported certified interval remains20/3..1847/276. This is new scoped WRITTEN structural mathematics, not a numerical guessing-number improvement, a negative-Phi witness, a full optimality theorem or a fresh executable-certificate acceptance. Original HOLD/deadline, immutable sources, exclusive write root, actual review histories and unmet T300 finite/triple gate remain unchanged.
