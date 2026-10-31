# Prime-field PSL2: actual seven-coset geometry and packing

**Status: unadopted, nonblind GENERAL PROOF AUTHOR candidate.** This is a complete written reconstruction, conditional on the precisely stated maximal-subgroup import below, not a reviewer pass, finite-assay result, or parent disposition. The actual object throughout is a family of pairwise-disjoint **left coset sets**, not a multiset of indices or a quotient shadow. No identification of `PSL(2,7)` with `GL(3,2)` is assumed or used.

A native clock observed before composing this body was **2026-10-30T15:49:59-0700 PDT**; this is not its completion time. Section 8 gives the actual input/derivation chronology and assurance limits.

## 1. Statement and the only non-elementary import

For a group `X`, write `B_7(X) <= r` when any `r+1` pairwise-disjoint actual left cosets of finite-index subgroups contain two whose subgroup indices have gcd at least 8. Write `J_7(X) <= s` for the corresponding conclusion for any `s+1` proper finite-index subgroup **labels**, repetitions allowed, without a disjointness assumption. A **bad** family is a pairwise-disjoint family of actual left cosets whose every pair of indices has gcd at most 7.

**Candidate theorem.** For every prime `p`, `B_7(PSL(2,p)) <= 7`, conditional at `p=7` on the following classification. For `p>7` the stronger `J_7 <= 2` holds without this import. For `p=2,3,5,7`, no finite `J_7` bound holds. At `p=7` the actual bound is sharp in the explicit sense `B_7 <= 7` but not `B_7 <= 6`.

The import used at `p=7` is exactly this specialization of the displayed Giudici/Béltran–Viudez classification in packet S3: the maximal subgroups of `G=PSL(2,7)` comprise the projective-line Borel of index 8 and two conjugacy classes of subgroups isomorphic to `S4`, each of index 7, with no other maximal types. In the excerpt the Giudici theorem explicitly gives two `S4` classes; the HTML excerpt supplies the `q != 7,9` dihedral restriction lost in PDF extraction. We rely on the correctness of that displayed import and its application, not on a reconstructed classification proof or independent source authentication. The excerpts' source references are M. Giudici, *Maximal subgroups of almost simple groups with socle PSL(2,q)*, Theorems 2.1–2.2, <https://arxiv.org/pdf/math/0703685v1>, and A. Beltrán and F. Viudez, Theorem 3.2, <https://arxiv.org/html/2607.09144v2#S3.Thmtheorem2>; neither link was followed in this duty.

The separately adopted conditional result for `q=p^f`, `f>=2`, in packet S2 remains exactly as it stood. Combining that result as an import with this candidate would cover all prime powers, subject to their respective qualifications; it does not make this prime-field candidate adopted or discharge any of S2's unpaid gates.

## 2. Elementary group and coset facts

We use the standard Sylow, Cauchy, orbit–stabilizer and Lagrange theorems and elementary matrix elimination. Counting nonzero first columns and compatible determinant-one second columns gives

`|SL(2,p)| = p(p^2-1)`,  `|PSL(2,p)| = p(p^2-1)/(2,p-1)`.

For `p>=5`, `SL(2,p)` is perfect: choose `t` with `t^2 != 1`, set `D=diag(t,t^-1)`, and obtain every upper unipotent as `[D,U(s)] = U((t^2-1)s)`. The lower unipotents are conjugates of the upper ones by the determinant-one Weyl matrix; elementary row elimination shows that upper and lower unipotents generate `SL(2,p)`. Thus its quotient `PSL(2,p)` is perfect too. A perfect group has no nontrivial solvable quotient. In particular an action of a perfect group on at most four points has trivial image, since `S4` and its subgroups are solvable; consequently such a group has no proper subgroup of index 2, 3, or 4.

We need two actual-coset lemmas. First, if `[X:A]=m` and `[X:B]=n` are finite and coprime, **every** left `A`-coset meets **every** left `B`-coset. Indeed the map

`X/(A intersect B) -> X/A x X/B`,  `x(A intersect B) -> (xA,xB)`,

is injective. The size of its domain is divisible by both coprime `m,n` and at most `mn`; it is therefore exactly `mn`, and the map is onto. Second, if `xU subset yV`, then `y^-1 x in V` and `U <= V`, because the identity and all elements of `U` lie in `(y^-1 x)^-1 V=V`. Thus after the common translation by `y^-1`, an actual coset contained in `yV` is an actual left `V`-coset of `U`.

In a finite group the densities of disjoint cosets sum to at most 1. All groups used in this proof are finite.

## 3. The prime fields other than 7

For `p>7`, the upper unipotent subgroup `P` has order `p` and fixes exactly the point at infinity on the projective line. Its normalizer is the upper-triangular Borel: normalization preserves the unique fixed point, and the Borel normalizes `P`. The Borel has index `p+1`. Its conjugate root groups are indexed by the `p+1` projective points. Any two distinct root groups generate `PSL(2,p)`: the projective action is 2-transitive (the translations in the stabilizer of infinity act transitively on the other points), so their fixed points can be moved to infinity and zero, and the corresponding upper and lower elementary matrices generate.

Let `H<G` have index not divisible by `p`. Since `p` divides `|G|` exactly once, `H` contains a Sylow `p`-subgroup. It cannot contain two distinct root groups, since those generate `G`; hence that Sylow subgroup is unique in `H`, is normal in `H`, and `H` lies in its normalizer, a Borel. Therefore every proper index is divisible by `p` or by `p+1`. Both exceed 7. Given any three proper subgroup labels, assign to each one such divisor; two assigned divisors coincide, so their indices have gcd at least 8. This proves `J_7 <= 2`, and hence the actual-coset assertion.

For `p=2`, `|G|=6`, so eight disjoint nonempty subsets cannot exist. For `p=3`, `|G|=12`. At most one member of a bad family has index 12, because two such indices have gcd 12. In an eight-family the other seven would each have index at most 6, already contributing density at least `7/6>1`, impossible.

For `p=5`, `|G|=60` and `G` is perfect. An index-1 coset is all of `G`, so deal only with proper subgroups. The possible indices form the overinclusive list

`5, 6, 10, 12, 15, 20, 30, 60`,

since 2, 3, 4 are excluded by perfectness. If index 5 occurs, every other index is divisible by 5 by the actual coprime-coset lemma. At most one index among `10,20,30,60` can occur, because every pair has gcd at least 10, and at most one index 15 can occur. Five index-5 cosets fill the group; with at most four there are at most six members altogether.

If index 5 does not occur, there are at most three members of index other than 6: at most one from `10,20,30,60`, at most one of index 12, and at most one of index 15. Six index-6 cosets fill the group, and at most four allow at most seven members. If there are exactly five index-6 cosets, an eight-family would need all three other types. Compatibility with 15 rules out 30 and 60, so their indices are 12, 15, and either 10 or 20. Their combined density is at least `1/12+1/15+1/20=1/5`, while five index-6 cosets leave only `1/6`. Thus eight are impossible.

For each of `p=2,3,5,7`, the projective-line point stabilizer has index `p+1` for the first three and the imported `S4` subgroup has index 7 for the last. Repeating the same proper label arbitrarily often has pairwise gcd at most 7, so no finite `J_7` bound exists in these cases. This repetition statement does not claim infinitely many disjoint cosets.

## 4. Both degree-seven actions for `PSL(2,7)`

Now let `G=PSL(2,7)`, of order `168`, perfect by Section 2. Let `H` be one of the imported index-7 `S4` subgroups. It is maximal: an intermediate subgroup has index dividing 7. Its normalizer is therefore either `H` or `G`; the latter would make `H` normal and yield a nontrivial solvable quotient of order 7, impossible. Thus `N_G(H)=H`. Each of the two conjugacy classes contains exactly seven distinct subgroups, naturally the seven point stabilizers in the corresponding action on `G/H`.

Let `P` be the upper unipotent Sylow-7 subgroup. Its unique fixed point on the projective line is infinity, so its normalizer is the projective Borel `N`, of order `7*3=21`. Explicitly `N/P` acts by the square scalars `{1,2,4}` on the translation parameter: `diag(t,t^-1) U(s) diag(t,t^-1)^-1 = U(t^2 s)`. For either degree-seven coset action, `P` is regular: its intersection with each stabilizer of order 24 is trivial, and its orbit therefore has seven points.

Choose an origin and label the seven points by `P`-translation parameters in `F_7`. The normalizer acts as the affine maps `z -> az+b` with `a in {1,2,4}` and arbitrary `b`. Its two orbits on ordered distinct pairs are determined by whether the difference belongs to `{1,2,4}` or its negative `{3,5,6}`. Every `G`-orbit on ordered distinct pairs is a union of these two `N`-orbits. If there are two `G`-orbits, each gives exactly one orientation to every unordered pair, hence a `G`-invariant tournament.

That alternative is impossible. The image `T` of `G` in the seven-point permutation action is nontrivial, transitive, and perfect. If its order were odd, it would be divisible by 7 and divide the odd part 21 of 168. Its Sylow-7 subgroup would then be normal (`n_7` divides 3 and is 1 modulo 7), with quotient of order at most 3; hence `T` would be solvable, contrary to nontrivial perfectness. Therefore `|T|` is even and, by Cauchy, `T` contains a nonidentity involution. In its faithful permutation image that involution swaps some pair of vertices, reversing the directed edge between them, which no tournament automorphism can do. Thus each degree-seven action is **2-transitive**. This argument does not assume the action is faithful before passing to its image.

## 5. Constructing the seven-point incidence geometry

Call the seven points of the first action points. Choose `K ~= S4` from the other class, acting on these points. It fixes no point: a fixed point would put `K` inside a conjugate of the first `S4`, and equality of their orders would identify the two classes. Its orbit lengths divide 24. An orbit of length 2 would have as kernel an index-2 subgroup of `S4`, necessarily `A4` of order 12; it would fix two points. But a two-point stabilizer in the 2-transitive action has order `168/(7*6)=4`, a contradiction. (The uniqueness of `A4` follows because a homomorphism from `S4` to `C2` sends all conjugate transpositions alike.) The available orbit lengths at most seven are therefore 3, 4, or 6, and their sum is seven, so they are exactly **3+4**.

For each of the seven conjugates of `K`, define its **line** to be its 3-point orbit. The assignment is equivariant under `G`. Counting initially with multiplicity, each of the seven lines has three points. Point 2-transitivity makes the number `lambda` of lines containing any unordered point pair constant. Thus

`lambda * binom(7,2) = 7 * binom(3,2)`, so `lambda=1`.

In particular the seven line sets are distinct: coincident 3-sets would count each of their pairs twice. Point transitivity and incidence counting show each point belongs to three lines. Two different lines meet in at most one point; a fixed line's three points each lie on two other lines, giving six distinct other lines, so every pair of lines meets in exactly one point. Thus this is a `2-(7,3,1)` incidence plane, derived here rather than imported.

The action on lines is the second degree-seven action and is 2-transitive by Section 4. A line stabilizer has its two point-orbits of sizes 3 and 4, so the group is transitive separately on incident flags `(point,line)` and nonincident antiflags. The dual structure also has seven points and seven lines, three of each through/on the other, and every two dual points have a unique dual line. Consequently every later argument remains valid after exchanging the words point and line.

## 6. Exact transporter and all six-cell cases

For point labels `x,y` and line labels `a,b`, define the actual subsets

`P(x,y) = {g in G : g(x)=y}`,  `L(a,b) = {g in G : g(a)=b}`.

Each is a nonempty left coset of its source stabilizer, and every actual index-7 left coset has exactly one of these descriptions, since every index-7 subgroup is maximal and belongs to one of the two imported classes. Every such set has cardinality 24 and density `1/7`.

For two **distinct** cells of the same type, their sets are disjoint exactly when they have the same source or the same target: equality of one coordinate forces the other to differ, which is incompatible with a permutation, whereas when both coordinates differ 2-transitivity supplies an element realizing both mappings. A point cell `P(x,y)` and a line cell `L(a,b)` are disjoint exactly when the truth values of `x in a` and `y in b` differ. Different truth values are impossible for an incidence-preserving element; equal truth values are realized by flag or antiflag transitivity. These are assertions about the actual sets, not just about their indices.

Any at least three pairwise-disjoint distinct cells of one type lie in a single row or a single column. For example, if two share a source but have different targets, a third disjoint from both must share that source: sharing both different targets is impossible. The column case is symmetric. Inversion is a bijection on `G` and sends `P(x,y)` to `P(y,x)` and `L(a,b)` to `L(b,a)`; hence it preserves actual left-transporter form and turns a common column into a common row.

**Six-cell completion.** Every six pairwise-disjoint actual index-7 cosets have as their complement one actual index-7 coset.

* If all six cells have one type, the row/column observation makes them six cells in a seven-cell row or column. The missing cell is disjoint from them, and all seven density-`1/7` sets partition `G`.
* Otherwise interchange point/line roles if needed, using the explicitly established dual properties, so at least three are point cells. Invert all six sets if needed, and write the point cells as `P(x,y)` with distinct `y` in `Y`. A line cell `L(a,b)` is disjoint from all these point cells exactly when either `x in a` and `Y` is disjoint from `b`, or `x notin a` and `Y subset b`. Since a line contains three points and its complement four, `|Y|>=5` is impossible in a mixed family. It remains to cover `|Y|=4` and `|Y|=3`.
* If `|Y|=4`, only the first alternative is possible, and `Y` is the entire complement of the target line `b`. This `b` is unique, if such a line exists. Both line cells have that same target and distinct source lines through `x`. There are exactly three such source lines; the remaining one, mapped to `b`, is disjoint from both line cells and from all four point cells. If no `b` exists, this mixed family cannot occur.
* If `|Y|=3` and `Y` itself is a line `b`, the first alternative would require a line disjoint from `b`, impossible because any two lines meet. Thus the three line cells have target `b` and distinct source lines **not** through `x`. Exactly four lines avoid `x`; using the fourth with target `b` gives the seventh cell.
* If `|Y|=3` and `Y` is not a line, the second alternative would require a line containing all three points, impossible. There is exactly one line `b` disjoint from `Y`: the three distinct pair-lines of `Y` each meet it twice; the incidence count `3*3` therefore gives `3*3-3=6` distinct lines meeting `Y`, leaving one of the seven. Each of the three line cells has target `b` and a source through `x`; their sources are distinct, so all three such lines are used. The disjoint sets `Y` and `b` each have size 3, leaving a unique point `y0` outside both. `P(x,y0)` is disjoint from all six cells.

In every feasible case the seventh cell is an actual index-7 left coset. Its density and the six existing densities sum to 1, proving it is exactly the complement. If inversion was used, invert the completed partition back; the missing set remains an actual left transporter. The duality step covers both `4+2` and `3+3` mixed compositions in either type and for both original row and column orientations.

## 7. Actual bad-family consumer at index seven

By the imported maximal list, every proper subgroup index is a multiple of 7 or 8. Moreover, a subgroup `U` whose index is not divisible by 7 contains a Sylow-7 subgroup `P_U`: the full factor 7 of `|G|` lies in `|U|`. In **both** degree-seven actions `P_U` is regular, because a point or line stabilizer has order 24. For any actual left coset `gU`, any source point `x`, and any target point `y`, choose `u in P_U` with `u(x)=g^-1(y)`; then `gu` lies in both `gU` and `P(x,y)`. The same argument applies to `L(a,b)`. Thus every coset with index prime to 7 meets every actual index-7 coset, not merely a common quotient image.

An index-1 coset is all of `G` and makes the family a singleton, so consider proper subgroups. For every index divisible by 7 write it as `7m` with `m` dividing 24, by Lagrange. If two such indices occur in a bad family, then `7 gcd(m,n) <= 7`, i.e. `gcd(m,n)=1`. For `m,n>1`, each has a prime factor 2 or 3, so there can be at most two such members in total, with repetitions counted.

If a bad family contains an index-7 member, every other member has index divisible by 7 by the preceding actual-intersection argument. With at most five index-7 members, at most two larger members give at most seven altogether. Six index-7 members leave one actual index-7 coset `zK` by Section 6. If two further actual cosets `gU,hV` were present, both would be contained in that complement; the containment lemma gives `U,V<=K`. After the same translation by `z^-1`, they are disjoint actual left `K`-cosets, with relative indices `m=[K:U]`, `n=[K:V]`. Their original indices are `7m,7n`, so badness implies `gcd(m,n)=1`, contradicting the coprime-index actual-coset lemma inside `K`. Seven index-7 members already fill `G`; more are impossible.

If no index-7 member occurs, the preceding `m>1` argument gives at most two members whose indices are divisible by 7. All remaining proper indices are multiples of 8, and two of them would have gcd at least 8, so at most one remains. Thus this case has at most three members. Altogether no bad eight-family exists: `B_7(G)<=7`.

Sharpness is witnessed without an enumeration: the seven distinct left cosets of any one imported index-7 subgroup partition `G`, and all seven subgroup indices equal 7. They form a bad seven-family, so `B_7(G)<=6` is false. This is an actual family of left coset sets, not seven repeated abstract labels.

## 8. Chronology, unrun checks, and exact unpaid boundaries

* Before the pre-body acknowledgment I read the complete assigned manifest, freeze receipt, parent-prepared metadata and actual-dispatch receipt, and all 20 listed status/permission controls through their endings. I personally hashed the manifest and freeze receipt, matching respectively `2fdc071fd2ae452d9c655f7402687894718beb6a7f963e92b121e447cc87edfb` and `c637cbf5ffe6de94416f5a0c3f04be494d75e543c106ba4dc6a20055ef5e18e9`; these were metadata operations. The manifest's research-task wording had already exposed the requested proof roadmap, but I had not read any packet/source body, selected a case, or derived mathematics. I then sent Main the direct pre-body ACK.
* After that ACK and before derivation, I read the complete literal packet in strictly ordered raw windows of at most 20 LF: packet LF 1–265, including its ending, carrying complete S1 LF 1–147, S2 LF 1–41, and S3 LF 1–75. The parent freeze reports packet SHA-256 `9f2f95d93c426af4aac5d43aa161a090fb9417c8fecbddc4dfdfc42284733fb6`; I did not separately child-hash the packet or the sources. This is a **nonblind** reconstruction: S1 and the research-task roadmap were read before the proof was developed. No cognitive-isolation certificate is asserted.
* The calculations and case splits in this body are written mathematical reasoning, including the line/nonline and row/column alternatives; they are not program output. **Child scientific execution: NOT RUN.** No finite enumeration, scientific program, CAS, solver, test, build, lint, formatter, external model, external source-following, sibling proof/code, held scientific payload/history/consumer, package installation, or deletion was used. Parent-observed metadata are not represented as child scientific execution. All stopped episodes and all of their consumers remain HELD/ZERO/NONINPUT.
* **Paid here, subject to independent checking and the classification import:** the displayed prime-field written argument, including all seven-point orbital, incidence, actual-transporter, mixed-completion, coprime-inside-complement, and packing cases. `Paid` means supplied as written proof, not externally certified.
* **Unpaid:** independent source authentication/full classification proof; disjoint written review and parent disposition of this body; an independent actual finite check of the `q=7` claims. Any child-prepared finite code remains unrun and requires the separately authorized parent GO before execution. No no-selected-WRITTEN score, prior stopped-gate clearance, external-family/human/kernel verification, novelty, priority, original normal-extension closure, or unrestricted Sun8 result is asserted. The adopted conditional `f>=2` theorem and its prior assurance are not changed by this candidate.
