# No degree-seven image: every pair generates G, and no index is seven — candidate v1

Observed before creation: `2026-10-23T14:36:41-0700` (actual `/bin/date` result). **Written CANDIDATE, not unrestricted Sun8 or a genuine counterexample.** This resumes the primary problem after both parent-assigned bounded peer reviews. No scientific execution or modelCLI has occurred.

## 1. Exact dependencies and claims

P7 denotes eight pairwise disjoint left cosets with indices7r_i and pairwise-coprime positive r_i, unrestricted in all other respects. `reduction-and-generation-v1.md` reduces Sun8 exactly to P7 relative to literal internal Sun7. This manuscript consumes:

- The completed candidate **G4** of `four-wise-generation-v1.md`, SHA256 `69f55c231f9d9458370a9c3464e5208e9043e37858c82c3b28820e809433883c`: every four P7 subgroup vertices generate G, both originally and after inversion. Its dependency `four-overgroup-residual-v1.md` retains internal Sun5, Zhu Sun3/4 and Margolis–Schnabel Prop4.5/TheoremB≤4 at exact declared interfaces. G4 is not assumed accepted; everything below is relative to its correctness and those interfaces.
- That same G4 manuscript's elementary LemmaF, binary Fano-plane model, |Aut(Fano)|=168 and even-permutation proof, and the Sylow/normalizer exclusion of orders42/84. Those arguments are independent of the theorem now being proved; no circular use of pair-wise generation occurs.
- The elementary coprime-index intersection lemma and the proved **LemmaQ** of `structural-addendum-v1.md`: quotient cosets remain disjoint when their normal-fibre indices are pairwise coprime.

The new consequences are:

**F7.** No finite subgroup of S7 supports P7.

**G2.** No index-seven subgroup of an arbitrary P7 group contains TWO subgroup vertices. Equivalently, every pair of original subgroup vertices generates G, and the same is true after inversion.

**I7.** Every P7 index is strictly greater than7: r_i=1 is impossible.

These are necessary structural obstructions, not a proof that P7 itself is empty.

## 2. Reduction to a faithful transitive degree-seven action for F7

Suppose a finite Q≤S7 supports P7. Since each n_i=7r_i divides |Q|, its order is divisible by7. Cauchy's theorem gives a7-cycle, so the given action is transitive. The7-part of |Q| is exactly7. Hence every quotient cofactor r_i has prime factors among2,3,5, and at most one cofactor carries each such prime. There are at least FIVE ordinary vertices of index exactly7; call their subgroups ordinary.

If seven or more indices are7, their disjoint cosets already cover all Q, leaving no room for the eighth. Thus in a putative configuration there are five or six ordinary vertices and at least two exceptional vertices. The argument below works with every actual index-seven subgroup, not a guessed conjugacy class.

## 3. An ordinary subgroup with an orbit of size two forces a dihedral image

Let K≤Q have index7 and an orbit B0 of size2 in the natural action on Ω, |Ω|=7. The set stabilizer S of B0 contains K, so [Q:S] divides7. Since Q is transitive, B0 is not invariant under Q; therefore S=K and the orbit of B0 consists of seven distinct unordered pairs.

These seven pairs are the edges of a simple Q-invariant graph on seven vertices. Point transitivity makes its degree2. Its connected components are cycles and are permuted transitively, so their common size divides7; the graph must be one7-cycle. Consequently Q embeds in its automorphism group D14. Now each P7 index divides14, so its cofactor is1 or2, with at most one equal2. At least seven indices are7, contradicting disjointness as above. Thus NO ordinary subgroup can have an orbit of size2.

## 4. An ordinary subgroup with an orbit of size three forces the full Fano group

If an ordinary K has a3-orbit, its set stabilizer is K by the same index7 argument. Its seven conjugate orbit triples form a point-transitive/block-transitive seven-triple structure whose block stabilizers are transitive on their triples. LemmaF from the G4 manuscript proves that structure is a Fano plane. Hence Q≤Aut(Fano), a subgroup of A7 of order168.

Now only primes2,3 can occur in private quotient cofactors. There are at least six indices7. If there were seven, disjointness fails. Thus there are EXACTLY SIX ordinary indices and two exceptional indices7·2^a and7·3^b with a,b positive (both primes on one cofactor would leave seven ordinary indices). Their divisibility into |Q| forces42||Q|. The elementary Sylow7/normalizer argument already written in G4 excludes orders42/84 inside Aut(Fano)≤A7. Therefore Q=Aut(Fano)=GL(3,2), order168, and b=1.

We now exclude its six ordinary cosets without assuming four share a subgroup.

### 4.1 Every index-seven subgroup is a point or line stabilizer

An ordinary subgroup U has order24. It cannot have an orbit7 (7∤24), or an orbit5 (5∤24), or an orbit2 (section3 would force Q≤D14). If it fixes a point, it is the full point stabilizer by equal indices. If it fixes no point, its remaining possible orbit partition on seven points is3+4, so it has a3-orbit B. Its set stabilizer equals U. In the full Fano automorphism group a noncollinear triple has orbit28 and stabilizer order6, whereas a line has orbit7 and stabilizer order24. Thus B is a line and U is its stabilizer. This proves the two stated families exhaust all ordinary subgroups.

GL(3,2) is2-transitive on points because every two distinct nonzero vectors are independent and their ordered images can be extended to a basis map. It is also2-transitive on lines: bases adapted to the intersection point of two distinct lines give the corresponding maps.

An ordinary point-stabilizer coset has the form {g:g(p)=q}; a line-stabilizer coset has the form {g:g(L)=M}. Two cosets of the same family are disjoint exactly when they have the same domain object and different images, or the same image and different domain objects. If both domains and images differ,2-transitivity gives an intersection. A pairwise-disjoint family of at least three such cosets has either one common domain or one common image: after choosing two with common domain and different images, a third with a different domain would have to have both of those different images; the dual argument treats common image.

If at least four of the six ordinary cosets belong to one family, these four therefore share a domain (all original subgroups equal a proper index-seven stabilizer), or an image (all inverted subgroups equal that stabilizer). Either contradicts G4 in Q. Thus exactly THREE ordinary cosets are point-map cosets and THREE are line-map cosets.

### 4.2 Three point cosets and three line cosets leave one entire index-seven coset

Invert the entire configuration if necessary, so the three point cosets share a DOMAIN point p and have three distinct image points q1,q2,q3. Write B={q1,q2,q3}. Inversion preserves the point/line families and disjointness.

For a point-map condition g(p)=q and a line-map condition g(L)=M, simultaneous realization is possible exactly when incidence agrees:

    p∈L iff q∈M.

For incident pairs choose bases consisting of the point, a second point on the line, and an exterior point; for nonincident pairs choose two line-basis points and the exterior point. The corresponding invertible binary linear map proves existence in both allowed cases. Thus disjointness is equivalent to the two incidence bits differing.

Every one of the three line cosets must be disjoint from all three point cosets, so its TARGET line M either contains all three points of B or is disjoint from B.

- **B is noncollinear.** No line contains B. Its four-point complement contains at most one Fano line (two distinct lines have union of size5). Since three line cosets exist, there is exactly one target line M0 disjoint from B, and all three line cosets have that target. Their domain lines must contain p by incidence reversal. Distinct cosets with the same target have distinct domains, so they are exactly the three lines through p. Their union is {g:g(p)∈M0}, because g^{-1}(M0) is then uniquely a line through p. Together with the three point cosets they cover the six point-image values in B∪M0. Their complement is the entire coset {g:g(p)=q0} for the remaining point q0, of index7.
- **B is a line.** No Fano line is disjoint from B. Thus all three line cosets have target B, and their domain lines do NOT contain p. There are four such lines; the three distinct domains occupy three of them. The three point cosets cover precisely {g:g(p)∈B}. Outside those, g^{-1}(B) is one of the four lines not through p; three are occupied by the line cosets. The complement is the remaining whole line-map coset, again of index7.

In either case the two exceptional cosets lie inside ONE left coset xJ of an index-seven subgroup J. Their subgroups lie in J after translation, with indices2^a and3^b inside J. These are coprime, forcing intersection. Contradiction.

Thus an ordinary orbit3 is impossible in a P7-supporting Q as well.

## 5. The remaining orbit partitions force a2-transitive point-stabilizer family

We have excluded any ordinary subgroup orbit2 or3. We use one elementary fact about faithful transitive prime-degree actions: unless the action is regular, two distinct points have different stabilizers. Indeed equality of point stabilizers is a Q-invariant equivalence relation. Its equal-sized classes form blocks and their size divides7. If a class contains two points, all seven point stabilizers coincide; their intersection is the action kernel, which is trivial. The common stabilizer is trivial, so the action is regular.

Take any ordinary K, index7. If it is trivial, |Q|=7 and all eight indices are7, immediately impossible. Otherwise it cannot fix two points (equal order makes it the stabilizer of each, contradicting the preceding fact).

Its orbit sizes sum to7, no orbit has size7 by7∤|K|, and sizes2/3 are excluded. An orbit5 would leave either an orbit2 or two fixed points, both impossible. An orbit4 would leave3,2+1 or1+1+1, again impossible. Hence the only possible partition is1+6. Thus K is a full point stabilizer and is transitive on the other six points; Q is2-transitive. The same argument applies to EVERY ordinary subgroup, so all at least five ordinary cosets are point-map cosets in this single natural action.

The2-transitive same-family clique argument in section4.1 makes these at least five cosets share one common domain or one common image. Four of their original or inverted subgroups are then the same proper index-seven stabilizer, contrary to G4. This exhausts all orbit cases and proves F7. No transitive-group classification was imported.

## 6. From degree-seven impossibility to pair-wise generation in arbitrary G

Suppose P7 holds in an arbitrary group G and some W≤G of index7 contains U_1 and U_2. Their original cosets occupy different left W-cosets because the fibre subgroup indices r_1,r_2 inside W are coprime. For any other vertex i, t_i=[U_i:U_i∩W] lies between1 and7. If t_i=7, its coset meets all seven W-cosets, including both baseline cells. Sharing baseline b requires gcd(r_b,7)>1, hence both r_1 and r_2 would be divisible by7, impossible. Therefore EVERY t_i≤6.

Set N=core_G(W), Q=G/N≤S7, and V_i=U_iN/N. This quotient is finite, faithful and transitive of degree7. Put D_i=[Q:V_i], c_i=[N:N∩U_i], so7r_i=c_iD_i and the V_i-orbit of W/N has size t_i.

If7∤D_i then V_i contains an element of order7 by Cauchy, which is a7-cycle in the faithful action, forcing t_i=7. Hence7|D_i for all i. All primes other than7 in c_i remain private, and7 can occur in at most one c_i, so the c_i are pairwise coprime. LemmaQ therefore preserves disjointness of the eight projected cosets. Since D_i divide7r_i and all contain7, their pairwise gcds remain exactly7. This is P7 in Q≤S7, contradicting F7.

Thus no index-seven W can contain two vertices. The subgroup generated by any pair U_i,U_j has finite index dividing gcd(7r_i,7r_j)=7, so it is G or such a W. The proper option is excluded. Every pair generates G. Apply the same theorem to the inverted left-coset configuration to obtain the second orientation. This proves G2.

## 7. Excluding an actual index-seven vertex

Suppose some U_v itself has index7. Let N=core_G(U_v) and Q=G/N≤S7. The projected coset of U_v is a whole coset of H=U_v/N, index7. The image of every other original coset is disjoint from it: overlap would lift to intersection with its full preimage g_vU_v, impossible.

By the coprime-index intersection lemma in Q, every projected subgroup index D_j must be divisible by7; otherwise gcd(D_j,7)=1 would force intersection with that H-coset. The v-index is7 as well. As in section6, normal-fibre indices c_i are pairwise coprime (their shared7-part can occur only on the one possible higher-7 cofactor). LemmaQ now preserves ALL pairwise quotient disjointness, yielding P7 in Q≤S7. F7 excludes it. Thus r_i>1 for every vertex, proving I7.

## 8. Exact remaining unrestricted barrier

The full target is still NOT solved. Combined with R8 and SN/MIN, a hypothetical Sun8 counterexample now necessarily has:

- n_i=7r_i with arbitrary pairwise-coprime integers r_i>1;
- every PAIR of original subgroups generating G, and every pair of inverted subgroups generating G;
- no subnormal subgroup vertex;
- no realization in ANY subgroup of S7;
- for a least-order finite realization, O_{7′}(G)=1.

No general finite order bound, simplicity, nonsolvability, bounded private-prime universe, normality or index ansatz is imposed. Pair-wise generation is a derived necessary condition, not a theorem that every P7 configuration has an excluded proper join. The remaining consequential obligation is to use actual product-set/intersection geometry when EVERY pair generates G; a local alpha matrix or permissible index pattern is not a group/coset example.

All new manuscripts remain CANDIDATE until actual separate in-harness and parent reconstruction at their full pinned dependency chain. The Fano/Sylow arguments are written proofs, not executable verification. No scientific program, enumeration, old checker, compilation, modelCLI, formal kernel or human review has run here; novelty is not cleared.
