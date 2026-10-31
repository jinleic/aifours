# Actual AME(4,6), N=50, t=26, q=4444: local P-incidence checks, an unrun verifier, and r=2 P-only structure

**Prospective GENERAL AUTHOR candidate F878. Nonblind, same harness. Not a parent disposition, review or acceptance.**

## Setting

Fix one normalized complex four-party tensor ψ in one local orthonormal product basis, and put U=6ψ. Assume:

- the three balanced 36×36 flattenings of U are unitary;
- the support of U has 50 words;
- exactly 26 of those words have |U_w|=1 (the set P);
- the other 24 words (the set E) use actual E alphabets Q_i of size 4 at every party.

Put O_i=[6]∖Q_i. A coordinate is *inside* when its symbol lies in Q_i and *outside* when it lies in O_i. Every statement concerns this one tensor and its same P and E. Finite statements labelled *projection* are relaxations of that object. Notation follows S2 with the S1 erratum: v_i counts triple words, and b_i denotes a degree-two symbol. The moment parameter is r=n_4.

## Results in brief

**R1. Written re-derivations with complete finite solution lists:**

- the same-P moment profiles and the partywise counts (§1);
- every per-symbol option for r=0, 1, 2 (§2);
- the r=1 exclusion (§3);
- the r=2 all-inside bit lemma (§4);
- the surplus restrictions and classes A/B/C (§5);
- the r=2 layer form (7) and the parity lemma (§6);
- the type-B consequences (§7), including a new forced pattern (B) for f_ij at a type-B party.

**R2. New written P-only results for r=2 (§8):**

- Proposition H: every triangle holonomy f_xz^{-1}∘f_yz∘f_xy is a single 4-cycle.
- Example W: an explicit 26-word set meets every P-only condition of the r=2 class. Same-P incidence alone therefore cannot exclude r=2.

**R3. A new complete standard-library verifier v2, unrun (§9).** It has seven flushed stages, controls in which each check fails for its intended reason, an internal 39 s bound, and outputs predicted by the author in advance.

Nothing here supplies an E support, a phase solution or an AME witness. It does not exclude r=0 or r=2 completely, and it proves no global minimum.

## 0. Actual premises and named imports

Each elementary fact below follows from actual unitarity. The pair system ij is the row index of the cut ij|kl.

**(F1)** In each pair system the 26 P pair values are distinct, and no E word takes one, because a unit-modulus entry exhausts its unitary row and column. Every one of the 36 values is taken, since unitary rows are nonzero. The remaining 10 values are therefore E values. Each has at least two extensions; otherwise its row would contain a single entry of modulus one. Since E⊂∏Q_i, every value with an outside coordinate is a P value. Thus each system has 8 inside/outside, 8 outside/inside and 4 outside/outside P values, plus exactly 6 P values and 10 E values among its 16 inside/inside cells.

**(F2)** For a∈Q_i, let d=d_i(a) be the number of E values (a,b) in a system ij. Row a has 2 outside cells and 4−d inside cells that are P values, so a lies in exactly 6−d P words. Hence d does not depend on j. Also:

- Σ_a d=10 and d≥2, since d=1 would allow only one E word;
- s_i(a)=2d+h_i(a), with h≥0 and Σh=4;
- the degree multiset at each party is 2,2,2,4 or 2,2,3,3.

**(F3)** Two distinct unitary rows, or two distinct columns, never share exactly one support position.

**Conditional imports, not re-derived here:**

- **(CUT)** S2 §1's actual-unitary cut lemma. In each pair system the ten E multiplicities are either four 3's and six 2's (*four-three*) or two 4's and eight 2's (*two-four*). In a two-four system the two 4-rows have the same four complementary values. S3 records this alternative as parent-scoped written support.
- **(H4)** S2 §5's exclusion of d=2, h=4 up to its final three-bit step. That exclusion uses an actual phase/orthogonality argument and CUT. Only the three-bit step is checked here, in §4.

## 1. Moments and partywise counts

Let n_k count P words with exactly k inside coordinates. By F1, each system contains 14 P values with i inside and 6 with both coordinates inside. π_ij is injective on P. Hence

```
Σ n_k = 26,   Σ k·n_k = 4·14 = 56,   Σ C(k,2)·n_k = 6·6 = 36.
Second minus first:  n2+2n3 = 30+n0−3n4;   third:  n2+3n3 = 36−6n4.
n3 = 6−n0−3n4,   n2 = 18+3n0+3n4,   n1 = 2−3n0−n4.                    (M)
```

Every integer solution is fixed by (n0,n4)∈[0,26]². The constraint n1≥0 forces n0=0 and r=n4≤2. The constraint n3≥0 then holds automatically. The solutions are exactly:

- r=0: (0,2,18,6,0);
- r=1: (0,1,21,3,1);
- r=2: (0,0,24,0,2).

At the boundary, n0=1 gives n1≤−1 and r=3 gives n1=−1.

Define u_i as the number of single-inside words at i, v_i as the number of triple words missing i, and p_ij as the number of words inside exactly at i and j. The six inside/inside P values of system ij come from p_ij words, from the triple words missing k or l, and from r words that are all inside. Hence

```
p_ij = 6−r−v_k−v_l,     Σ_{j≠i} p_ij = 18−3r−2(n3−v_i),
14 = u_i + Σ_{j≠i} p_ij + (n3−v_i) + r   ⇔   u_i+v_i = n3+2r−4 = 2−r.     (P)
```

The complete solution lists are:

- **r=0:** u is any of the 10 compositions of 2 into four parts, and v=2−u.
- **r=1:** u=e_h for 4 choices of h, and v=1−e_h.
- **r=2:** u=v=0.

All of these have p_ij≥2+r. The number of triple words containing i is t_i=n3−v_i=4−2r+u_i.

## 2. Per-symbol identities and complete option tables

Let z_m(a) count the P words that contain a∈Q_i and have exactly m inside coordinates. Row a has 4−d inside P cells in each of the three systems at i. Counting the 6−d P words that contain a, and their inside incidences, gives

```
z1+z2+z3+z4 = 6−d,   z2+2z3+3z4 = 3(4−d),   z1−z3−2z4 = 2(d−3);
z1 = 2(d−3)+z3+2z4,   z2 = 12−3d−2z3−3z4;                               (Z)
0≤z1≤u_i,  0≤z3≤t_i,  0≤z4≤r;     Σ_{a∈Q_i} z(a) = (u_i, 14−u_i−t_i−r, t_i, r).
```

The complete options, listed as z=(z1,z2,z3,z4), are:

| r | d=2 | d=3 | d=4 |
|---|---|---|---|
| 0 | (0,2,2,0); (1,0,3,0) if u_i≥1 | (0,3,0,0); (1,1,1,0) if u_i≥1 | (2,0,0,0) iff u_i=2 |
| 1 | (0,2,2,0), (0,3,0,1); (1,0,3,0), (1,1,1,1) if u_i=1 | (0,3,0,0); (1,1,1,0) if u_i=1 | none |
| 2 | (0,3,0,1) | (0,3,0,0) | none |

Below are the numbers of assignments of options to the four ordered symbols, with degree-two symbols first, that meet the party total:

| pattern \ (r,u_i) | (0,0) | (0,1) | (0,2) | (1,0) | (1,1) | (2,0) |
|---|---|---|---|---|---|---|
| 2,2,3,3 | 1 | 4 | 6 | 2 | 8 | 1 |
| 2,2,2,4 | 0 | 0 | 1 | 0 | 0 | 0 |

These counts follow from two observations:

- **r=0:** relative to the base options (0,2,2,0) and (0,3,0,0), every option with z1=1 shifts (z2,z3) by (−2,+1). Any u_i of the four symbols may therefore carry it, giving C(4,u_i)=1, 4, 6. The degree-four case is (2,0,0,0) together with three base degree-two symbols.
- **r=1:** exactly one degree-two symbol carries z4=1. When u_h=1, the singleton lies either:
  - on that symbol, giving (1,1,1,1);
  - on the other degree-two symbol, giving (1,0,3,0);
  - on one of the two degree-three symbols, giving (1,1,1,0).

  This gives 2·(1+1+2)=8 assignments.

**Consequences.**

- **(C1)** d=4 occurs iff r=0, u_i=2 and z=(2,0,0,0); that is, both singletons sit at party i on the same symbol. Conversely, z1=2 forces d=4. Hence r∈{1,2} implies that every party has degree multiset 2,2,3,3.
- **(C2)** r=1:
  - The all-inside word w* has z4=1 at w*_i, so d(w*_i)=2 at every party.
  - At j≠h, where u_j=0, the other degree-two symbol b_j has z=(0,2,2,0). So z3(b_j)=2=t_j, and both triple words containing j carry b_j.
  - At h, where u_h=1, all eight assignments give z3(b_h)∈{2,3}.
- **(C3)** r=2: z(a)=(0,3,0,3−d). Each degree-two symbol lies in exactly one all-inside word, so D_i:={d=2}={w^0_i,w^1_i} and w^0_i≠w^1_i. Put T_i=Q_i∖D_i. Every other P word has exactly two inside coordinates, and every symbol lies in exactly three of those words.

## 3. r=1 is excluded

**Statement.** No tensor in the setting has n4=1.

**Proof.** By (P), u=e_h, v_h=0 and v_j=1 for j≠h. So the triple words are T_j for j≠h, where T_j misses exactly j. By C2, two of them carry b_h at h; call them T_j and T_k with j≠k. Let l be the fourth party. Both words contain l, and by C2 both carry b_l there. Thus π_hl(T_j)=π_hl(T_k)=(b_h,b_l), although T_j≠T_k since they miss different parties. This contradicts F1. The proof uses only F1, F2 and §§1–2. It needs no CUT, E multiplicity, phase or q5 premise.

**Abstract finite check (v2 stage 3).**

- **Setup.** Number the parties 0=h and 1, 2, 3. Relabel symbols within each Q so that b_h=b_j=0; relabelling preserves every pair collision. Word T_m has h-symbol s_m∈{0,1,2,3}, outside value 4+β_m at party m, and symbol 0 at its other two inside parties.
- **Exhaustion.** There are 4³·2³=512 configurations. Exactly (3·3+1)·8=80 have at least two s_m equal to 0, and each of the 80 has an actual pair collision. Every other configuration fails only the repeat premise.
- **Controls.** Each fixture fails exactly its named check and passes when only that check is disabled:
  - s=(0,1,2) fails the repeat premise;
  - T_2 carrying symbol 1 at party 3 fails the forced-symbol premise, and is collision-free when that premise is disabled;
  - s=(0,0,0) fails injectivity.
- **Limit.** The premises are built in by relabelling. Their derivation is C2, which is written here; stage 2 reports the option sets that support it but does not separately assert them.

## 4. r=2 all-inside symbol bits (v2 stage 4)

For r=2, the 12 values (w^β_i,w^β_j), with β∈{0,1} and i<j, are P values, so by F1 no E word takes any of them. Give an E word bit β at each party where its symbol is w^β_i. Its coordinates in D then carry pairwise different bits. Hence an E word has at most two such coordinates, and when it has two their bits are opposite.

The check runs over all 4⁴ words, with Q={0,1,2,3}, w^0=0000 and w^1=1111. The numbers of allowed words with exactly k coordinates in D are

```
k=0: 2⁴=16;   k=1: 4·2·2³=64;   k=2: C(4,2)·2·2²=48;   k=3: 0;   k=4: 0.
```

No three binary bits are pairwise different: all 8 elements of {0,1}³ fail.

- **Controls.** For each β, the word (β,β,2,3) fails exactly on the w^β pair. The bit triple (0,1,0) fails on its (0,2) pair. Disabling the named check accepts each fixture.
- **Limit.** Only the all-inside constraints are modelled. The layer cells (a,f_ij(a)) impose further constraints that this stage does not include.

## 5. Surplus restrictions and classes A/B/C

**(2) d=2 implies h∈{0,2,4}.** Written here; not checked in v2.

The E slice of a lies in the binary cube {a}×H_j×H_k×H_l, where H_j is the pair of E neighbours of a at j. For each j, the lines (a,x) with x∈H_j partition the slice, and each line has at least two words by F1. The overlap of rows (a,x) and (a,x') in cut ij|kl equals the number of cube edges in direction j inside the slice.

- **h=1 (five words):** in every direction the lines have sizes 2 and 3. So the overlap is at least 1, hence at least 2 by F3. That requires at least 6 induced edges. But deleting three vertices of the cube removes at least 9−2=7 of its 12 edges, leaving at most 5.
- **h=3 (seven words):** one system would contain lines of sizes 3 and 4, which CUT forbids.

So h=1 is excluded by F1 and F3 alone, while h=3 needs CUT.

**(6) for d=3, by CUT.** Suppose h=4 with d=3. A four-three row has surplus at most 3, so every system at i must be two-four with both of its 4-lines in row a. Row a's lines then have multiplicities 4, 4 and 2. In cut ij|kl the two full rows share one complementary 4-set S, and the low row has two words, with projections (k1,l1) and (k2,l2). For each κ, the (a,κ) line in system ik has even multiplicity, equal to 2·|S∩({κ}×Q_l)| + #{r: k_r=κ}. So k1=k2, and likewise l1=l2. The two low words would then coincide, which is impossible. For d=2, (6) is the import (H4).

**Surplus projection (v2 stage 2).** Consider vectors h∈{0..4}⁴ with Σh=4 and degree-two entries in {0,2,4}; for r=2, also require max≤3. The counts are:

- r=0, pattern 2,2,2,4: 10;
- r∈{0,1}, pattern 2,2,3,3: 14 each;
- r=2, pattern 2,2,3,3: 10, split into the classes below.

With degree-two positions listed first, the r=2 classes are:

- **A:** (2,2,0,0), (2,0,2,0), (2,0,0,2), (0,2,2,0), (0,2,0,2), (0,0,2,2);
- **B:** (0,0,3,1), (0,0,1,3);
- **C:** (2,0,1,1), (0,2,1,1).

These are necessary classes, not realizations.

**Controls.** Each fixture fails only its named check:

- (1,1,1,1) fails the degree-two parity check;
- (0,0,4,0) fails the r=2 no-four check;
- (0,0,0,0) fails the total.

## 6. r=2 layers, the form (7), and the parity lemma (v2 stage 5)

**Layer form.** Let r=2 and fix a pair ij with complement {k,l}.

- By C3, every word of P∖{w^0,w^1} is inside at exactly two parties. Let P_ij be the words inside exactly at i and j. These are the P words in the outside/outside cells of system kl. So |P_ij|=4 by F1, and g_ij, mapping a word to (o_k,o_l), is a bijection onto O_k×O_l.
- In system ij, row a∈Q_i has 4−d inside P cells, and for a∈D_i one of them is (w^β_i,w^β_j). So exactly one P_ij word has i-symbol a, and f_ij:Q_i→Q_j is a bijection.
- **(i)** f_ij(w^β_i)≠w^β_j, by injectivity.
- **(ii)** The P words that have i-symbol a and are outside at j are exactly the P_ik and P_il words with i-symbol a. Each of the two cells (a,o) with o∈O_j is taken exactly once. Those two words therefore use the two different O_j values.

**Converse.** Given data satisfying (i) and (ii), each system's cells are filled exactly once, by cell type:

- the 2+4 inside/inside cells by (i) and the bijectivity of f;
- the 8 inside/outside and 8 outside/inside cells by (ii);
- the 4 outside/outside cells by g.

Cells of different types never collide. So (7) holds with exactly 26 words, the projection is injective in all six systems, the profile is that of r=2, and every value outside the inside/inside block is a P value.

**Local layer check.** Take Q={0..3}, w^0=0000, w^1=1111, O={4,5} and the layer {0,1}. The valid f are the 24−6−6+2=14 permutations with f(0)≠0 and f(1)≠1. For each valid f, all 24 bijections g make the six words {w^0,w^1}∪P_01 injective in all six systems, giving 336 layers.

Controls: the fixtures f=(2,2,0,1), g=(0,0,2,3) and f=g=identity each fail their named guard. Each passes with only that guard disabled and then exhibits an actual pair collision.

**Parity lemma.** Fix i.

- **b-functions.** For j≠i, the layers inside at i and outside at j are P_ik and P_il. Let b_ij(a) be the O_j bit of the i-symbol-a word in a fixed one of them. By (ii), the word in the other layer carries the complement.
- **Bijectivity.** The P_ij word with i-symbol a has outside bits b_ik(a) and b_il(a), up to fixed complements. Since g_ij is a bijection, a↦(b_ik(a),b_il(a)) is a bijection Q_i→{0,1}², for each of the three pairs {k,l}.
- **Lemma.** Suppose four words of {0,1}³ have all three two-coordinate projections bijective. For fixed x the two words with first bit x have different third bits, and likewise for fixed y. So the third bit equals x⊕y⊕c. The four words form one parity class, and any two differ in exactly two coordinates.

Stage 5 checks the lemma over all 8⁴ ordered 4-tuples. Exactly 48=2·4! are accepted; all have common parity, and every pair is at distance 2.

Controls:

- ((000),(010),(101),(111)) fails only the (0,2) projection. It has mixed parity, so that projection is load-bearing.
- Four copies of 000 show that common parity alone is not sufficient.

Limit: stage 5 checks the abstract lemma and one layer. The derivation of the b-functions from the actual P is the written argument above.

## 7. r=2 type B: neighbours, forced f values, mixed bits (v2 stages 6–7)

**Setup.** In system ij with r=2, relabel so that D_i=D_j={0,1}, w^β=ββββ and T={2,3}. The ten E values are Q_i×Q_j minus (0,0), (1,1) and the graph of f_ij. Row and column degrees are (2,2,3,3). The surplus h_i(a)=Σ_b(m(a,b)−2) equals the number of 3-cells in row a of a four-three system, and twice the number of 4-cells in a two-four system.

**Neighbours.** Let party i be type B, with surplus-three symbol c and surplus-one symbol t in T_i.

1. Every system at i is four-three, because two-four surpluses are even.
2. Row c has degree 3, and all three of its cells are 3-cells, lying in distinct columns. So party j has three positive-surplus symbols and must be type C. Let b_j=w^β_j be its surplus-two degree-two symbol.
3. c's cells hit b_j and both T_j columns once each. Column b_j needs one more 3-cell, and the T_j columns are already full. Hence t's single 3-cell is (t,b_j).

**New consequence.** Column b_j has degree two, and its E cells are (c,b_j) and (t,b_j). So its two P cells lie in rows D_i, and one of them is (w^β_i,w^β_j). Row c's E cells are Q_j∖{f_ij(c)}={b_j}∪T_j. Therefore

```
f_ij(w^{1−β}_i) = w^β_j = b_j,     f_ij(c) = w^{1−β}_j,     f_ij({w^β_i, t}) = T_j.     (B)
```

**Mixed bits.** We have s_i(t)=2·3+1=7. If b_j and b_k carry equal bits, (b_j,b_k) is the P value of w^β in system jk, so no E word contains both. If all three bits were equal, the three 3-lines (t,b_j) would be pairwise disjoint and would need 9>7 words. So the bits split 2+1. Since the other three parties are type C, at most one party is type B.

**Stage 6 (projection).** For all 14 valid f, it takes every 4-subset of the ten E cells (210 of them) and every 2-subset (45) whose row and column surplus vectors pass the r=2 filter of §5. It asserts:

- the E-cell degrees;
- B on one side implies C on the opposite side;
- the neighbour sets;
- (B), for a party that is B on the row side;
- every two-four placement is A/A with disjoint endpoints.

**Stage 7 (projection).** For every bit pattern and every ordered triple of 3-subsets of the 7 E words at t, lines with equal bits must be disjoint. Monochrome patterns admit no triple, and mixed patterns admit some.

**Controls.** Each fails only its named check:

- an odd surplus in a two-four system;
- overlapping same-bit lines;
- a line of size 2;
- three disjoint lines occupying 9 words, which pass only when the 7-word bound is disabled.

**Limit.** Each projection handles one pair system and one symbol at a time. It does not use CUT's component structure, any other system, or E words beyond these counts.

## 8. New P-only structure for r=2 (written; not checked by v2)

**Proposition H.** In every actual r=2 tensor of the setting, and indeed in every P set of the form (7), the following holds for every m∈I. Write {x,y,z}=I∖{m}. Then h=f_xz^{-1}∘f_yz∘f_xy is a single 4-cycle on Q_x. Changing the base party or the orientation only conjugates or inverts h.

**Proof.**

**(a) h has only even cycles.** Join two of the 12 words in P_xy∪P_xz∪P_yz when they lie in different layers and share an inside symbol. Each word then has exactly two neighbours. Walking xy→yz→xz→xy applies h once, so the graph is a union of cycles whose lengths are 3ℓ, where ℓ runs over the cycle lengths of h. Condition (ii), applied at x, y and z with outside party m, says that adjacent words carry different O_m values. That is a proper 2-colouring, so every ℓ is even and h has no fixed point.

**(b) h is affine with a transvection as linear part.**

1. **Coordinates.** By the parity lemma we can choose coordinates v∈F₂² on each Q_p such that the O_r bit of every layer word at p equals τ_p(r)(v)+const. Here τ_p is a bijection from the three other parties onto the three nonzero functionals of F₂².
2. **Affine maps.** Equate the two outside bits of each P_pq word as seen from both of its ends. This shows f_pq(v)=A_pq·v+δ_pq, where τ_q(r)∘A_pq=τ_p(r) for both outside parties r. It follows that τ_q(p)∘A_pq=τ_p(q), since each nonzero functional is the sum of the other two.
3. **Linear part.** H=A_xz^{-1}A_yzA_xy satisfies τ_x(m)∘H=τ_x(m), τ_x(y)∘H=τ_x(z) and τ_x(z)∘H=τ_x(y). So H is the transvection whose fixed space is exactly ker τ_x(m).
4. **Cases.** Write h(v)=Hv+t; then h²(v)=v+(H+I)t.
   - If t∈ker τ_x(m)=ker(H+I), h is an involution with two fixed points.
   - Otherwise h² is a nonzero translation, and h is a 4-cycle.

Part (a) excludes fixed points, so h is a 4-cycle. Equivalently, (ii) forces τ_y(m)(δ_xy)+τ_z(m)(δ_yz)+τ_z(m)(δ_xz)=1=τ_x(m)(t). □

**Example W (fresh author example).** At every party the inside symbols are Q={0,1,2,3} and the outside symbols are O={4,5}. The following 26 words form an r=2 P set:

```
w^0 0011   w^1 3202
P12 0244 1355 2045 3154     P13 0405 1424 2514 3535
P14 0552 1540 2451 3443     P23 4004 4115 5225 5334
P24 5053 5142 4250 4341     P34 5501 5410 4523 4432
```

The author checked every pair system by hand. In each row of the table:

- the six inside/inside values are distinct;
- the eight inside/outside values are all of Q×O;
- the eight outside/inside values are all of O×Q;
- the outside/outside layer supplies all of O×O.

| system | inside/inside | inside/outside | outside/inside | outside/outside |
|---|---|---|---|---|
| 12 | 00 32 · 02 13 20 31 | 04 14 25 35 05 15 24 34 | 40 41 52 53 50 51 42 43 | 55 54 45 44 |
| 13 | 01 30 · 00 12 21 33 | 04 15 24 35 05 14 25 34 | 40 41 52 53 50 51 42 43 | 55 54 45 44 |
| 14 | 01 32 · 02 10 21 33 | 04 15 25 34 05 14 24 35 | 53 52 40 41 51 50 43 42 | 44 45 55 54 |
| 23 | 01 20 · 00 11 22 33 | 24 35 04 15 05 14 25 34 | 40 42 51 53 50 41 52 43 | 55 54 45 44 |
| 24 | 01 22 · 03 12 20 31 | 24 35 05 14 04 15 25 34 | 52 50 41 43 51 40 53 42 | 45 44 54 55 |
| 34 | 11 02 · 01 10 23 32 | 05 24 14 35 04 15 25 34 | 52 40 51 43 53 42 50 41 | 44 55 45 54 |

Hence:

- all six projections are injective;
- the profile is (0,0,24,0,2);
- every value outside Q_i×Q_j is a P value;
- D_1={0,3}, D_2={0,2}, D_3={0,1} and D_4={1,2}.

The four holonomies, with base party 1 for m=4,3,2 and base party 2 for m=1, are:

| m | holonomy |
|---|---|
| 4 | (0 1 3 2) |
| 3 | (0 1 2 3) |
| 2 | (0 2 1 3) |
| 1 | (0 3 1 2) |

Each is a 4-cycle, as Proposition H requires.

**Consequence.** The form (7) is nonempty, and r=2 survives every same-P condition used in S2 and here. Any exclusion of r=2 must use E, the unitary cut structure (CUT), or phases. W supplies no E set: its ten E values per system, its multiplicities and its CUT compatibility are all untested.

## 9. Prepared verifier v2

**Identity.** The verifier is `finite-ame50-4444-p-incidence-v2.py`. The parent supplied, as administrative metadata only, SHA-256 `9b3f10e2c240da22b4749a76c079295922fbb23dc4006b1eba3e2cc8025b6977`, 22599 bytes, 568 LF; the author did not recompute it.

**Status and requirements.**

- v2 is UNRUN. It needs Python 3.10 or newer, because it uses `int.bit_count`, and a POSIX system providing SIGALRM/setitimer.
- It uses the standard library only, and creates no files, subprocesses, network connections or randomness.
- It enforces an internal 39 s bound via an alarm armed from process start plus monotonic checks. The parent must also impose an external bound of at most 55 s.

**Output events and exit codes.** Output is JSON lines, flushed after each line.

| event | exit code |
|---|---|
| `begin`, `stage-start`, `stage-complete` | — |
| `complete` | 0 |
| `check-failed`, `error` | 1 |
| `incomplete` (deadline reached) | 2 |

The `begin` event states the scope `necessary-local-projections-only`. The `complete` event's result is `NECESSARY_LOCAL_PROJECTIONS_ONLY_NOT_GLOBAL_P_E_OR_AME`. The verifier also has guards that stop if a checked domain is empty.

**Stages:**

1. moments and partywise counts;
2. per-symbol options and surplus;
3. the r=1 pigeonhole;
4. r=2 all-inside bits;
5. r=2 layer and parity;
6. r=2 high-edge projection;
7. type-B seven-word lines.

**History.** v1 (`fd7e5c3d…`) remains unrun and is superseded; `design-correction-1-v1.md` records why.

**Predicted outputs.** The author predicted these by hand, before any run. A mismatch would be a disclosed author slip, to be dispositioned by the parent.

| stage | predicted output |
|---|---|
| 1 | profiles [[0,0,24,0,2],[0,1,21,3,1],[0,2,18,6,0]]; party assignments {"0":10,"1":4,"2":1} |
| 2 | assignment counts as in §2; surplus counts 10/14/14/10; classes {"A":6,"B":2,"C":2} |
| 3 | 512 enumerated / 80 eligible / 80 rejected |
| 4 | [16,64,48,0,0]; 0 bit triples accepted |
| 5 | 14 valid f / 336 layers / 48 signatures, parity {"0":24,"1":24} |
| 6 | four-three {"AA":32,"AC":28,"BC":8,"CA":28,"CB":8,"CC":32}; two-four {"AA":406}; B_C=C_B=8 |
| 7 | 4900 for each of the six mixed patterns, 0 for 000 and 111 |

Stage 6's figures come from three symmetry orbits of valid f, of sizes 2, 8 and 4, each having 10, 10 and 9 four-three placements respectively. Stage 7's figure is 35·4·35=4900. [INFERENCE] The run should take a few seconds, mostly in stage 7's 343,000 line checks.

## 10. Reads, process and limits

**Before the packet.**

- Process context, not mathematical input: the memory summary and the protocol skill.
- The manifest, freeze receipt, final binding and metadata supply. Their first non-raw displays elided blocks, which complete raw reads recovered (LF 1–213, 1–199, 1–181 and 1–212). The dispatch receipt was read in full (LF 1–48).
- All 22 status-only controls, raw and complete. These are status and permissions only.
- A listing of the wave directory (names only).

I then wrote `prebody-ack-v1.md` and delivered a direct acknowledgement to Main.

**The packet.** I read it in raw windows of LF 1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–180, 181–200, 201–220, 221–240 and 241–248, the last including the ending. Every display was under 30,000 bytes; the part is 44,571 bytes. No clipping occurred, so no recovery was needed. The packet renders complete:

- S1, LF 1–3;
- S2, LF 1–172;
- S3, LF 1–22;
- S4, LF 1–33.

**Own outputs.**

- v1 was written and not re-read.
- v2 was written, then re-read raw in windows of LF 1–150, 150–300, 300–450 and 450–568 to audit it.
- `design-correction-1-v1.md` was written.
- The parent supplied hashes for v1, v2 and the note as metadata only.

**Sources not opened.** No linked or unlisted source was opened: not F826, F841, F842, F856, F857, F787, F798, F799 or F800, not the parent's q5 draft, and no held episode or held consumer. S1 and S2 are earlier nonblind author candidates, re-derived here without finding a discrepancy. S3 and S4 are parent dispositions used only for the scoped interfaces named above.

**Process deviations.**

- **v1 checker expectation.** In v1 the expected r=1 total was 320 instead of 80. The parent classified this as one pre-run DESIGN MINOR. I disclosed it before writing v2, and v1 is preserved unchanged.
- **Methods used under owner addendum 2.** Example W is a fresh author example. I also reasoned through the source's fixtures by hand to design them and to predict the outputs.

**Nothing executed.** No code execution, test, compilation, subprocess, network, external model, deletion, Git, or edit of an existing file was used. No native clock was observed.

**Limits.** Every finite stage is a necessary projection, not a full P/E support, 4444 support or AME feasibility check. Specifically, this candidate provides:

- no E set, including none for W;
- no phase solution;
- no exclusion of r=0 or r=2;
- no exclusion of t26 or N50;
- no minimum-support result;
- no family, human or formal acceptance;
- no priority claim.

The surplus conclusions remain conditional on CUT and H4. The r=1 exclusion and Proposition H use only F1–F3 and same-P counting. This is an author candidate; parent disposition and an independent check are separate.
