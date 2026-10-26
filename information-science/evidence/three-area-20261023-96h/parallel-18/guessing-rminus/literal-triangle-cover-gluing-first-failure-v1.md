# R-minus literal decoder/fiber gluing: an exact finite-strategy bridge and its first failure

Owner `InfoGuessingRminus`, info-5. Actual `/bin/date` observation before this freeze: `Sun Oct 25 06:31:46 PDT 2026`.

**WRITTEN ONLY, no scientific interpreter, arithmetic/symbolic program, enumeration, certificate replay or new GO.** This changes attack direction from generic posterior necessary conditions to an ACTUAL finite winning strategy on the literal26-edge graph, and proves precisely where straightforward decoder/fiber augmentation fails. It does not supply an improving trade or change the imported interval20/3..1847/276.

The baseline triangle strategy is OLD, not a discovery. The output is one explicit graph-specific block-trade equivalence, full FD justification, and a precise first-failure result for local/single-syndrome gluing. No positive-Phi control or membership thinning is offered.

## 1. Literal graph, provenance, and all-finite-alphabet scope

Retain `inputs-v1.json`, observed SHA256 `bdc4cd14d20e2401971a7354c2a6239106fbe2be158b50921d5c486c6a086be6`. Its neighbourhoods are exactly:

| v | N(v) |
|---|---|
|1|2,3,4,5,6,7|
|2|1,3,7,9,10|
|3|1,2,4,8,9|
|4|1,3,5,8,10|
|5|1,4,6,9,10|
|6|1,5,7,8,9|
|7|1,2,6,8,10|
|8|3,4,6,7,9,10|
|9|2,3,5,6,8|
|10|2,4,5,7,8|

Thus1 and8 have degree6, all other vertices degree5. No9–10 edge is present.

The literal cover was recovered by reading LF1–62 of the historical `information-science/evidence/six-lane-20261016/guessing-number-r-minus/code/verify_cover_code.py`, observed SHA256 `c90dcc31f720ccd3c0974b6b6b91869bf388c489a145ffbf1d13458bee70d7e1`. The Python file was NOT imported or executed; its old numerical/checker outputs are not verification premises here.

For each integer m>=2 use Z_m, not a finite-field restriction. Each physical vertex symbol will lie in Z_m³. Arbitrary nonlinear competitors on that SAME alphabet are admitted. The final equivalence ranges over every m; Section8 explains why cube alphabets do not restrict the existential question of improving20/3 on arbitrary finite alphabets.

No I1, I2/T300, Latin-closure entropy theorem, group classification or existing finite-certificate replay is required for the proofs below. In particular the inherited T300 executable/triple-verification gate stays UNMET and is not bypassed.

## 2. The ten actual triangles and the complete baseline strategy

Let the chosen triangles be

`T1=123, T2=145, T3=167, T4=239, T5=(2,7,10),`

`T6=389, T7=(4,5,10), T8=(4,8,10), T9=569, T10=678`.

Every edge of every listed triple occurs in Section1's actual neighbourhoods. The incident triangle slots at each vertex are:

| v | incident triangle indices |
|---|---|
|1|1,2,3|
|2|1,4,5|
|3|1,4,6|
|4|2,7,8|
|5|2,7,9|
|6|3,9,10|
|7|3,5,10|
|8|6,8,10|
|9|4,6,9|
|10|5,7,8|

Write x_(v,T) for the component of vertex v's symbol belonging to an incident triangle T, with components ordered by triangle index. Define

`C_m={x: sum_(v in T) x_(v,T)=0 in Z_m for EVERY chosen T}`.

For each of the ten independent triangle constraints, choose two slot values freely; the third is their negative sum. Therefore

`|C_m|=m^20`, with common physical alphabet size `m^3`.

The actual local decoder at v is the three-component function

`f^0_(v,T)(z_(N(v)))=-z_(a,T)-z_(b,T)` for T={v,a,b}.

Both a,b are actual neighbours. These decoders are defined on the ENTIRE neighbour-symbol domain, not just on a tested sample. A word satisfies all ten local vertex equations iff it satisfies every triangle parity relation, so their full winning set is precisely C_m. Thus the known lower rate is exactly20/3. No execution or word enumeration is needed for this construction.

## 3. A literal graph fact: no chosen triangle has a common neighbour

The following ten HAND calculations use Section1's neighbourhoods. In each row, the intermediate set has empty intersection with the neighbourhood of the third triangle vertex:

| T={a,b,c} in the displayed order | N(a) intersect N(b) | intersect N(c) |
|---|---|---|
|1,2,3|{3,7}|empty|
|1,4,5|{3,5}|empty|
|1,6,7|{5,7}|empty|
|2,3,9|{1,9}|empty|
|2,7,10|{1,10}|empty|
|3,8,9|{4,9}|empty|
|4,5,10|{1,10}|empty|
|4,8,10|{3,10}|empty|
|5,6,9|{1,9}|empty|
|6,7,8|{1,8}|empty|

Hence for EVERY vertex v and chosen triangle T,

`|T intersect N(v)|<=2`.                                  (G)

This is actual26-edge content. A claim that a cover-code neighbour fiber is freely glueable would be wrong without checking precisely this property; here the table proves it for the literal cover.

## 4. All neighbour fibers are full, and their exact cardinalities

More generally, fix any vertex set S and all its physical symbols. Each chosen triangle T has r_T=|T intersect S| fixed slots. For r_T=0,1,2 there are respectively m²,m,1 extensions within its parity relation. If r_T=3, an extension exists exactly when the already fixed three values sum to0, and then there is one extension. Different triangles use disjoint slots, even when their physical vertices coincide, so these extensions are independent.

It follows that the projection onto S consists EXACTLY of the assignments satisfying the parity relations of chosen triangles wholly contained in S. Every nonempty such fiber has cardinality

`m^(sum_T max(2-|T intersect S|,0))`.                       (F_S)

For S=N(v), (G) eliminates the r_T=3 obstruction. Thus

`pi_(N(v))(C_m)=(Z_m³)^(N(v))`                            (FULL)

for EVERY v. There is a direct extension recipe: in each triangle with one unspecified slot fill it by the parity relation; with two unspecified slots set one to0 and solve for the other; with three unspecified slots set all to0. The choices for the ten triangles are independent and form an actual baseline word.

Each neighbour vertex occupies exactly three cover slots, so

`sum_T |T intersect N(v)|=3 deg_G(v)`.

Consequently every full neighbour fiber has the exact cardinality

`F_v:=|{c in C_m:c_(N(v))=z}|=m^(20-3deg_G(v))`

`=m² for v=1,8; =m^5 for all other v`.                    (COUNT)

There are no exceptional neighbour tuples: every z occurs. This count is written algebra from the independent triangle relations, not a rank census or finite computational check.

## 5. First failure: no decoder change can adjoin one word while retaining C_m

Suppose an arbitrary FD-consistent code C' contains all of C_m. At vertex v, every possible neighbour tuple occurs in C_m by (FULL). Its vertex value there is already forced to be f_v^0 of that tuple. FD consistency therefore forces the same complete-domain decoder at v for every word of C'. This is true for all ten vertices. Since the simultaneous winning set of the f_v^0 is exactly C_m,

`C' containing C_m and FD-consistent => C'=C_m`.           (SAT)

Thus even arbitrary NONlinear decoder modifications cannot add a single new word while retaining the baseline. This is not an argument that maximum linear dimension equals unrestricted guessing number; it uses literal full neighbour projections and actual decoders.

### Exact deletion cost for one outside word

Let x lie outside C_m. For each vertex define its full-symbol defect by

`v in B(x) iff x_v != f_v^0(x_(N(v)))`.

For a defective v, define the baseline conflict fiber

`F_v(x)={c in C_m:c_(N(v))=x_(N(v))}`.

Every member of this fiber has c_v=f_v^0(x_N), different from x_v. Therefore ALL of F_v(x) must be deleted from the baseline before x can be inserted in any FD-consistent replacement code.

Since x is outside C_m, some chosen triangle T violates its parity relation. Each of its THREE vertices is defective in its corresponding T component, hence belongs to B(x). For two distinct vertices v,w in that triangle, the fibers F_v(x),F_w(x) are DISJOINT: a word in F_v(x) has c_v=f_v^0(x_N)!=x_v, whereas membership in F_w(x) requires c_v=x_v because v is a neighbour of w. This is an actual crossed-decoder contradiction, not a probability inequality.

By (COUNT), the union of these three compulsory deletion fibers has size

- `m²+2m^5` if T contains hub1 or8;
- `3m^5` if T contains neither.

No chosen triangle contains both hubs, as the actual cover shows. For every m>=2,

`|union_(v in B(x)) F_v(x)| >= 2m^5+m²`.                  (COST)

So inserting one word forces deletion of at least2m^5+m² words. In the old alphabet8 instance m=2 this is68 deletions for one insertion, not a rate improvement. This number is a specialization of the symbolic proof, not a new search window or computational result.

More generally any improving replacement must insert at least2m^5+m²+1 outside words. This is a FIRST-FAILURE statement for the proposed local augmentation, not a universal bound on all winning codes.

## 6. Exact necessary-and-sufficient block-trade FD criterion

This is the constructive bridge beyond that first failure. Let A be ANY set of outside words, `A subset (Z_m³)^10 minus C_m`, and put

`R_m(A)=union_(x in A) union_(v in B(x)) F_v(x)`.

This is an explicitly defined subset of the known baseline, using only the literal graph decoders/fibers. Let D be any subset of C_m and consider

`C'=(C_m minus D) union A`.

Then

`C' is FD-consistent`

`iff [A is FD-consistent on the original graph AND R_m(A) subset D]`. (TRADE)

**Proof.** Within the retained baseline there are no FD conflicts. Internal conflicts among outside words are exactly the FD condition on A. For a cross pair x in A,c in C_m minus D, a conflict at v is possible exactly when c_N=x_N and c_v differs from x_v. For a matching baseline neighbour tuple, c_v always equals f_v^0(x_N). Thus cross conflicts occur EXACTLY for defective v and c in F_v(x). Removing R_m(A) is therefore necessary and sufficient to eliminate all cross conflicts. No further gluing hypothesis, coordinate independence or inherited induced-graph decoder is used.

In particular the smallest sufficient deletion set is D=R_m(A). If A is FD-consistent and

`|A|>|R_m(A)|`,                                           (GAIN)

then the actual code

`C_A=(C_m minus R_m(A)) union A`

has more than m^20 words on the common alphabet m³, hence gives a strict lower improvement over20/3.

The deterministic decoders can be completed explicitly: at a neighbour tuple occurring in the retained baseline, use f_v^0; at a tuple occurring only in A, use its unique A-value; if both occur, (TRADE) makes those values identical; at unused tuples output any fixed symbol. This proves actual local strategy existence on the original graph. The resulting full winning set may contain additional words, which only helps the lower bound.

Conversely, any FD-consistent code C' on this same alphabet with |C'|>m^20 defines A=C' minus C_m and D=C_m minus C'. It satisfies (TRADE), so

`|A|>|D|>=|R_m(A)|`.

Thus (GAIN) with FD-consistent A is not merely a necessary-condition screen: it is EQUIVALENT to an improving finite strategy at this alphabet, with exact FD sufficiency proved.

For explicitly given A, all intersections of the baseline fibers in R_m(A) are determined by (F_S): first require agreement of prescribed values on overlapping neighbour sets, then enforce the parity relations of any chosen triangles wholly fixed by their union. If consistent, (F_S) gives their exact intersection cardinality. This is a written description of the ACTUAL overlap problem, not a program run or an assertion that its union size has been computed for an unknown A.

## 7. Second precise failure: one parity-syndrome class cannot gain, even partially

The ambient group is (Z_m)^30 and C_m is the kernel of the ten independent triangle-sum maps. Its cosets are exactly parity-syndrome classes. This uses no finite-field or prime-power assumption.

Let A lie in one nonzero coset C_m+h, possibly a proper arbitrary subset. Some vertex v is defective for h; the same v is defective for every x=c+h in that coset because the decoders f_v^0 are additive.

By (FULL), choose k in C_m with k_N(v)=h_N(v), using the explicit triangle extension recipe in Section4. The fixed map

`x=c+h -> c+k`

is injective into C_m and has the same v-neighbour tuple as x. Since v is defective, c+k is in F_v(x), hence in R_m(A). Therefore

`|R_m(A)|>=|A|` for EVERY A contained in one nonzero syndrome class. (ONE)

So a full coset, a partial coset, a one-word defect, or a translated copy of a single local defect cannot produce (GAIN). A strict trade must combine at least TWO distinct nonzero parity syndromes, while keeping A itself FD-consistent.

The first unsupported step is now precise. The injective maps above depend on the syndrome through the defective vertex v and extension k. Their images for DIFFERENT syndromes may overlap. No compatible global injection A into R_m(A) has been constructed for arbitrary FD-consistent multi-syndrome A. Nor has an actual multi-syndrome A with positive gain been produced. Either assertion would require genuine new graph-specific content; the one-syndrome argument does not silently establish either.

## 8. No restriction of the original all-finite-alphabet question

The full target still permits every common finite alphabet and arbitrary nonlinear decoders. Cube alphabets are existentially sufficient for detecting ANY strict improvement: if a code on an alphabet of size s has |C|>s^(20/3), its coordinatewise three-fold product is FD-consistent on the same graph, with alphabet size s³ and more than s^20 words. Identify the original alphabet with Z_s as a SET, and the product alphabet with Z_s³; no linearity is imposed on that competitor.

Apply Section6 with m=s to that product code. It produces an outside FD set A satisfying (GAIN). Conversely any (GAIN) witness at any integer m>=2 is already an actual finite strategy beating20/3.

Using the inherited definition gn as the supremum over finite alphabet sizes, this gives the exact graph-specific equivalence

`gn(R-minus)>20/3`

`iff there exist integer m>=2 and an FD-consistent outside set A`

`with |A|>|R_m(A)|`.                                    (EQUIV)

This does not claim existence of either side. It preserves every finite alphabet in the unrestricted target and avoids an unjustified field-size or scalar-linear restriction.

## 9. Exact unresolved obligation and honest outcome

The remaining combinatorial alternative is explicit:

- construct a literal FD-consistent multi-syndrome outside set A with (GAIN), then Section6 supplies the actual enlarged code and complete decoder prescription; or
- prove `|R_m(A)|>=|A|` for EVERY m and EVERY such FD-consistent A, which by Section8 would settle the lower endpoint at20/3.

Neither has been proved. In particular no assumption that a mixture/gluing of individually valid syndrome classes remains FD-consistent is permitted. The cross-neighbour fibers and internal FD condition in (TRADE) are the exact gates that must be met.

**Precise first failure delivered:** the literal lower-bound strategy occupies EVERY neighbour input domain, so no pure augmentation can work; every outside word incurs the quantified compulsory deletion cost; one entire or partial syndrome class admits an explicit injective obstruction. The first surviving representation is a genuine multi-syndrome block trade with possible shared deletion fibers, NOT another positive-Phi control or generic minimizer/KL restatement.

This is an exact written attack interface and first-failure result, not numerical guessing-number progress. The certified interval stays20/3..1847/276. The baseline construction is old; novelty of the gluing formulation is not cleared. This packet has no new peer/formal/kernel/cross-vendor/human acceptance and no executed finite-certificate credit. All sources and prior error histories are immutable; T300's independent executable/triple gate remains UNMET. Scientific-launch HOLD, original deadline and exclusive owner write root remain binding.
