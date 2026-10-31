# F872 author candidate: actual nine-run selectors, offsets, and all-selection transfer

**Status.** Fresh written author candidate, for independent reconstruction and parent disposition; no family, human, formal, kernel, or publication acceptance is asserted. The scope is exactly the actual-word domain below. In addition to reconstructing the frozen F849 direction and offset tests, this candidate gives a written proof that **every H=1 word is selectable**, that every H≤3 word whose increments belong to one sign-class is selectable, that the H=2 case is selectable if its two end increment-segments both have length at least three, and that every H≤3 word with all increment-segment lengths at least three is selectable. The remaining H=2,3 restrictions are necessary, not an assertion of an avoiding word or of their sufficiency. The all-selection coefficient at the end is an exact iff, not a computed verdict.

## 1. Domain, occurrences, and indexing

Let p≥7 be prime, F=3p−2, and write

`D_(2p) = F_p ⋊ {0,1}`, `(x,e)(y,f)=(x+(−1)^e y,e+f)`,
`r_y=(y,0)`, `s_x=(x,1)`.

Quantify over **every actual linear ordered word** W having F reflection occurrences and R≥p+1 rotation occurrences, with at most one rotation in each original cyclic reflection gap. Rotation exponent zero is allowed and its occurrence still counts. Its cyclic reflection projection has exactly one maximal constant run A1,…,A9, all of label a, and every other maximal run has length one. Let the outside occurrences in cyclic order be b1,…,bm, where

`m=3p−11`, `n=m+1=3p−10`, `x0=a`, `xi=bi (1≤i≤m)`, `xn=a`, `di=xi−x_(i−1) (1≤i≤n)`.

Thus every di is nonzero and `Σ_(i=1)^n di=0`. Conversely these two conditions give exactly this run structure; nonadjacent labels may coincide, including with a. A cyclic triple `(a',b',c')` is rich when its three pair differences are distinct. The only potentially rich windows are centered at bi, with difference set `T_i={−di,−d_(i+1),−di−d_(i+1)}`. Since the increments are nonzero, this triple is rich iff `di≠d_(i+1)`. Hence

`H = #{i∈{1,…,n−1}: di≠d_(i+1)}`.

This candidate assumes H≤3. If H=0 then closure gives `−10d1=0`, impossible for p≥7, so H≥1. Write the changes `1≤k1<…<kH≤n−1`, segment lengths `ell0=k1`, `ell_i=k_(i+1)−ki`, `ell_H=n−kH`, and nonzero segment slopes `v0,…,vH`. Adjacent slopes differ and `Σ ell_i vi=0`; these are exact input conditions, not a realizability claim for arbitrary lengths.

## 2. Actual cuts, local rotations, and the sumset selector

For j=1,2,3 omit the actual Aj, cut immediately after it in the cyclic word, and partition the remaining 3p−3 reflections into p−1 chronological triples. The two original physical gaps adjacent to Aj remain distinct and occur at opposite ends of the cut. Each partition has exactly two constant triples. The unique possible nonconstant triple with an equal adjacent pair is `(a,a,b1)` for j=1, none for j=2, and `(bm,a,a)` for j=3. The other nonconstant blocks come from the outside windows. A rich center i occurs in phase j exactly when `i≡j−1 (mod 3)`; write its count r_j. Thus `Σ r_j=H`.

A useful exact indexing of the p−3 nonconstant blocks in phase `s=j−1∈{0,1,2}` is

`C_s={i: 0≤i≤n, i≡s (mod 3)}`.

Each C_s has p−3 indices because n=3(p−3)−1. Index 0 denotes `(a,a,b1)` and has direction `[d1]`; index n denotes `(bm,a,a)` and has direction `[dn]`; an interior non-rich i denotes the triple centered at bi and has direction `[di]=[d_(i+1)]`. Here `[d]={d,−d}`. A change index is a rich block instead of a two-point direction. This indexing refers to actual blocks, not merely abstract increments.

For a block `(a',b',c')` with selected rotations of exponents u,v in its first and second interior gaps, respectively, the actual pair contribution sets, when the other interior gap is empty, include

* first gap u: `{a'−c'−u, a'−b'−u}`, distinct iff `b'≠c'`;
* second gap v: `{b'−c'−v, a'−c'−v}`, distinct iff `a'≠b'`.

All block prefixes have an even number of selected reflections. Thus the selected rotation in an inter-block gap or either physical end gap contributes `+y`; the displayed internal signs are not freely chosen. For j=1 the only unsafe gap is the outside gap A9–b1; for j=3 it is bm–A1; for j=2 there is none. Protected rich gaps and these physical unsafe gaps are forbidden, with duplicates counted only once. With r protected rich blocks, at most 2r+1 physical gaps are forbidden. Choose two remaining actual rotations, at most one interior to each block; this is possible when r≤2: for r=2 at least `R−5≥p−4≥3` rotations remain, and the graph of compatible pairs is complete minus a matching (a block has at most two interior gaps). For r≤1 the stronger bounds used below hold. Constant blocks are not forbidden; they always have an actual local choice.

For nonempty finite subsets A,B of F_p, `|A+B|≥min(p,|A|+|B|−1)`. For completeness: choose subsets A',B' with `(a−1)+(b−1)=N=min(p−1,|A|+|B|−2)`, where a=|A'| and b=|B'|. If their sumset lay in an N-element C, `∏_(c∈C)(X+Y−c)` would vanish on A'×B' although its coefficient of `X^(a−1)Y^(b−1)` is `binom(N,a−1)≠0 mod p`. The finite-grid Lagrange coefficient identity makes that coefficient zero, contradiction. Iteration gives the multi-sum bound.

If any phase has r_j≥2, protect two rich blocks. The two constants contribute ≥1 value each, the two rich blocks ≥3 each, and the other p−5 blocks ≥2 each. The sumset has at least `1+2+2+(p−5)=p` elements, so it cancels the **actual** boundary offset. The resulting 2p selected occurrences multiply to identity in cut order; moving the cut back to the original linear start only cyclically rotates their selected product and hence conjugates it. Identity is preserved. Consequently an avoiding word must have r_j≤1 in every phase, so its change indices have pairwise distinct residues modulo three.

## 3. Complete direction tests and p=7 boundaries

Fix a phase with r=r_j∈{0,1}, protect its rich block if any, and choose any compatible eligible rotation pair. Each nonconstant non-rich block has an actual two-point local set with direction independent of the chosen pair: its unrotated two-value set, or one of the safe two-value sets above, is translated by the selected internal rotation. Let D_j be its multiset of sign-classes. Its size is `p−3−r`.

The following are sufficient for an original-order identity selector using exactly two rotations, for every actual rotation placement and exponent:

* r=0: at least two entries lie outside every one sign-class; or there is a unique exceptional entry outside a class `[d]`, and it is not `[2d]`.
* r=1: D_j contains two sign-classes; or its one class is `[d]` and the actual rich set is not `{t,t+d,t+2d}` for any t.

Proof. For r=0 there are p−3≥4 pairs. Two disjoint unequal-direction pairs give two four-element sums; the other pairs and the sumset bound give `4+4−1+(p−7)=p`. Such disjoint pairs exist unless one class has at least p−4 entries. In that exceptional case the p−4 equal pairs form an interval of p−3 consecutive d-points, whose three-point complement cannot contain a translate by e unless e is 0, ±d, or ±2d. Thus an outlier not `[2d]` fills the field. With no outlier the direction test is inconclusive.

For r=1, two unequal pair directions give a four-point sum; together with the protected three-set and the remaining p−6 pairs this gives `4+2+(p−6)=p`. If all pairs have direction d, a nonconsecutive three-set has at least two components in the cyclic d-order and its sum with `{0,d}` has at least five elements; the remaining pairs give `5+(p−5)=p`. At p=7 there are four pairs for r=0 and three for r=1, so none of these arguments uses a large-p limit.

For nonzero unequal neighboring increments u,v the rich set is `{−u,−v,−u−v}`. It is a consecutive three-set of step ±d **exactly** when one of

`u=2v and [d]=[v]`; `v=2u and [d]=[u]`; `v=−u and [d]=[u]`

holds. These are obtained by testing each of the three actual elements as the midpoint. They remain valid at p=7; no division by p−7, or distinctness of nonadjacent labels, is used. For p≥7, `[u]≠[2u]` for u≠0.

## 4. Exact restricted offsets, inclusion/exclusion, and rotation-pair graph

A **bad phase** below means one surviving the tests in §3. For it define E to be all actual rotations remaining after forbidding the protected rich interior gaps and the at-most-one unsafe gap. A pair of vertices of E is compatible unless both lie in the same triple's interior. Thus its compatibility graph is `K_M` minus a matching, with `M=|E|≥p` for r=0 and `M≥p−2≥5` for r=1. Every vertex has a compatible partner; no artificial rotation is introduced.

Fix a representative d of the common class. In the one-outlier r=0 case choose the unique majority d and orient the outlier as step 2d; for p≥7 that majority is unambiguous. Orient each unrotated non-rich two-set as `{b,b+d}`, or in the outlier case `{b,b+2d}`. For r=1 orient the rich set as `{b_T,b_T+d,b_T+2d}`. Let B0 be the sum of these actual bases; the two unrotated constant blocks have value zero.

For an eligible rotation q of exponent y define its **actual offset set**

`A_q={y}` in a physical inter-block or end gap;
`A_q={−y}` in a safe interior gap of a nonconstant non-rich block;
`A_q={y,−y}` in a constant-block interior gap.

The minus sign for a non-rich interior follows directly from the two safe choices in §2: because the unrotated block has exactly two distinct values, those choices are precisely that two-set translated by −y. If y=0, the last set is the singleton {0}, but the rotation occurrence remains selected. For every compatible pair Q={q,q'}, its actual offset set is

`B_j(Q)=B0+A_q+A_q'`.

The restricted-family attainable exponent sets, and their **exact** zero-exclusion conditions, are:

| Bad pattern | attainable set | zero absent iff |
|---|---|---|
| r=0, all `[d]` | `B_j(Q)+{0,…,p−3}d` | `B_j(Q)⊆{d,2d}` |
| r=0, one `[2d]` outlier | `B_j(Q)+{0,…,p−2}d` | `B_j(Q)⊆{d}` |
| r=1, all `[d]`, rich consecutive d-set | `B_j(Q)+{0,…,p−2}d` | `B_j(Q)⊆{d}` |

For the outlier, `{0,…,p−4}+{0,2}={0,…,p−2}` as p≥7. The table is not merely a cardinality estimate: every listed sum is realized by actual omissions and the two selected actual rotations. For finite B and the applicable interval I, an exact inclusion/exclusion indicator for a successful restricted Q is

`1_{0∈B+I} = Σ_{∅≠J⊆B} (−1)^(|J|+1) ∏_(b∈J) 1_{−b∈I}`.

B here is a set of **distinct actual offsets**; using the product avoids counting one Q several times when different offsets work. Summing this indicator over compatible Q counts successful pairs, not all possible subsequences. The table is its explicit two- or one-missing-offset form. It neither discards the two physical end gaps nor treats an offset as freely variable.

For multiplicities, fix one actual omission for each of the two chosen non-rich values. In `Z[X]/(X^p−1)`, the exact number of restricted identity selections for Q is the X^0 coefficient of

`X^B0 · ∏_(q in Q, boundary) X^(y_q) · ∏_(q in Q, non-rich interior) X^(−y_q) · ∏_(constant blocks C) K_C(X) · L_j(X)`,

where K_C=3 if Q has no interior rotation in C and `K_C=X^y+2X^(−y)` if Q selects its interior rotation y; `L_j=(1+X^d)^(p−3)` in the uniform r=0 case, `(1+X^d)^(p−4)(1+X^(2d))` in the one-outlier case, and `(1+X^d)^(p−4)(1+X^d+X^(2d))` for r=1. The coefficient uses actual omissions, including multiplicity when y=0, and its positivity is exactly the support test above.

### 4.1 A complete compression of the all-Q offset restrictions

For either singleton-target case, the table's condition for **every** compatible Q is equivalent to the following simpler actual-rotation condition:

1. every eligible rotation in a constant-block interior has exponent 0;
2. there is a single h∈F_p such that each eligible boundary rotation has exponent h, each eligible non-rich interior rotation has exponent −h, and `B0+2h=d`.

Proof. Any constant-interior nonzero y gives two distinct A_q values; since q has a compatible partner their sum cannot be a singleton. After excluding that possibility write `A_q={h_q}`. The graph has at least five vertices and at most one missing neighbor per vertex, so any two vertices have a common neighbor. The equations `B0+h_q+h_q'=d` on all edges imply all h_q are the same h. The converse is immediate. In particular, an eligible constant-block rotation forces h=0 and then all eligible rotation exponents are 0.

The two-missing-offset r=0 case also has the following exact all-Q description. Put `T={d−B0,2d−B0}` and M≥7.

* If every A_q is a singleton `{h_q}`, either all h_q=c with `2c∈T`; or there are two values c,e with `e−c=±d`, `{2c,c+e}=T`, and the e-vertices number one or two, with two allowed only when they are the two incompatible interiors of one triple. Every other vertex has value c.
* If some constant-interior A_q has two values, all such vertices lie in one constant block, all eligible rotations in that block have exponents ±d/2, every vertex outside it has singleton offset `{c}`, and `B0∈{d,2d}`, `c=3d/2−B0`. These conditions are also sufficient. In particular an eligible rotation in the other constant block is impossible in this case.

To prove the first bullet, take distinct singleton values u,v. They have at least M−4≥3 common neighbors. For every such neighbor z, the two distinct values u+z,v+z are exactly T, so all common neighbors have one common value c and `v−u=±d`. Two common neighbors are adjacent, so `2c∈T={u+c,v+c}`, giving c=u or c=v. Any other vertex is either a common neighbor or the unique nonneighbor of u or v; in the latter case it is adjacent to every common neighbor. Its sum with c lies in `{u+c,v+c}`, so it also has value u or v. The other value e cannot occur at two compatible vertices since 2e is neither 2c nor c+e; hence at most two, and if two they are the matching pair. Conversely the stated edge sums are in T.

For the second bullet, two nonzero constant-interior offset sets from different blocks have a sumset of at least three points, impossible inside the two-point target. A compatible singleton neighbor of `{±y}` forces `2y=±d` and has offset c equal to the target's midpoint, `3d/2−B0`. At least five vertices lie outside that block, including a compatible pair, so `B0+2c∈{d,2d}`, i.e. `B0∈{d,2d}`. A zero rotation in the same block would pair with an outside vertex to give `3d/2`, neither target value, so every eligible rotation in that block is nonzero of the stated form. The converse follows by checking within-outside and outside-outside edges.

When two phases have singleton targets, their eligible sets intersect in at least `R−6≥p−5≥2` actual rotations. In each phase let σ=+1 for a boundary gap and −1 for a safe non-rich interior gap. On any common eligible rotation that is nonconstant in both, `h_j=σ_j σ_k h_k`. If a common rotation is interior to a constant block in either phase, both h-values are zero. Thus two common nonconstant rotations with opposite products σ_jσ_k also force both h-values to zero. These are necessary consequences of actual offsets, not an assertion that avoiding words exist.

## 5. A zero-rotation selection lemma

The following written construction will be used repeatedly. Suppose W has at least p−3 actual identity rotations and either (i) an outside consecutive arithmetic-progression piece of at least 2p−6 reflection occurrences, or (ii) two disjoint outside consecutive arithmetic-progression pieces with the same nonzero step and at least 2p−5 occurrences in total. Then W has an original-order length-2p identity selection.

Put `q=(p−5)/2`. For p=7, the ten outside reflections have a repeated label by pigeonhole; select those two, eight of the nine equal run reflections, and four identity rotations. For p≥11, q≥3. In an AP piece of length L, q_i disjoint chronological pairs can have any total index-gap S in `[q_i,L−q_i]`: give each pair a positive gap, put one unused index step between consecutive pairs, and distribute the desired gap total. In case (i), `p+q≤2p−6`, so q pairs with gap total p fit. In case (ii), if one piece has length one, discard it and use the other, whose length is at least 2p−6. Otherwise allocate q_i≥1 pairs to both pieces with `q_1+q_2=q`, `q_i≤floor(L_i/2)`. Such an allocation exists because `Σ floor(L_i/2)≥p−3≥q`; their attainable total gaps cover `[q,L_1+L_2−q]`, which contains p. The alternating sum of the selected outside reflection labels is ±p times the common step, hence zero. Add any eight run reflections and any p−3 identity rotations. The number selected is `8+2q+(p−3)=2p`; both reflection blocks have identity product, identity rotations do not alter it, and cyclic conjugation returns to original order. The proof uses actual occurrences, including any repeated outside labels.

## 6. New written eliminations within H≤3

Throughout this section assume, for contradiction, that the actual W has no length-2p identity selection. Then no direction test or restricted eligible pair can succeed. All changes have distinct residues modulo three.

### 6.1 H=1 is completely selectable

Let k be its change and u,v the two nonzero slopes. If `[u]≠[v]` and `3≤k≤n−3`, the rich phase samples both classes at indices k−3 and k+3 in C_s, including an endpoint if equality holds, and §3 gives a selector. If k=1 or 2, all non-rich entries of the rich phase have class `[v]`; the midpoint criterion then forces u=2v. Closure gives `(n+k)v=0`, i.e. p divides 10−k, which is 9 or 8, impossible. If k=n−1 or n−2, all non-rich entries have class `[u]`; the midpoint criterion forces v=2u, and closure gives `(n+(n−k))u=0`, again p divides 9 or 8. Hence v=−u.

Closure now gives `2k≡n≡−10`, so `k≡−5 (mod p)` and, in the actual range, `k=p−5` or `k=2p−5`. Orient the rich phase by d=u and write k=3q0+s, 0≤s≤2. Its C_s has q0 positive-slope non-rich entries before k and `p−4−q0` negative-slope entries after k. For a positive interior slope the unrotated oriented base is −2u, for a negative one +u; the boundary index 0 changes its positive base by +u, and index n changes its negative base by −u. The rich set `{−u,0,u}` has base −u. Therefore

`B0/u ≡ −2q0+(p−4−q0)+1_{s=0}−1_{s=2}−1 ≡ −k−4 ≡ 1 (mod p)`.

The singleton-target equivalence in §4.1 therefore makes every eligible rotation in this rich phase an identity rotation. There are at least p−2. If k=p−5, the final negative-slope outside piece has 2p−6 occurrences; if k=2p−5, the initial positive-slope outside piece has 2p−5. The lemma in §5 gives an identity selection, contradiction. Thus **every H=1 word in the stated domain is selectable**.

### 6.2 One sign-class, H=2 or 3, is completely selectable

Suppose all increments belong to one sign-class. Choose u=d1; every change flips sign. Let P and M be the counts of +u and −u increments. Closure and `P+M=n≡−10` give `P≡M≡−5 (mod p)`. Both are positive, so `{P,M}={p−5,2p−5}`.

For H=2 write changes k<l, L=l−k. The slopes are +u,−u,+u, and `L≡−5 (mod p)`. If k,l share a residue, §2 already gives a selector. Otherwise put `t=L mod 3∈{1,2}` and `q0=floor(L/3)`. In either rich phase, exactly q0 of the p−4 non-rich indexed blocks have negative slope. With d=u the rich base is −u, and each of the two possible boundary corrections is +u, since both endpoint slopes are positive. Hence for phase residue s,

`B0/u ≡ 7+3q0+δ_s ≡ 2−t+δ_s`, where `δ_s=1` for s=0,2 and `δ_1=0`.

If either rich phase has B0=u, §4.1 yields at least p−2 identity rotations. The negative-majority case L=2p−5 supplies the single AP piece `x_k,…,x_l`; the positive-majority case L=p−5 supplies disjoint +u pieces `x_1,…,x_k` and `x_l,…,x_(n−1)`, with total length 2p−5. Section 5 gives a selector.

The only remaining residue pattern is `t=1`, `k≡2`, `l≡0`, where both rich phases have B0=2u and therefore common singleton offset h=−u/2≠0. They are phases j=3 and j=1. In these two phases the constant-block interior gaps together cover seven of the eight gaps A1–A2,…,A8–A9; an eligible rotation in any such gap would force h=0, so none occurs. The remaining run gap A1–A2 is a phase-1 end gap and a safe phase-3 non-rich interior gap; the opposite offset signs and equal nonzero h forbid a rotation there as well.

Index the outside gaps by i=1,…,n, from x_(i−1) to x_i. In phases 1 and 3, any outside gap eligible in both has opposite signs unless i≡0 mod 3. There are p−4 gaps of residue 0. The only extra outside gaps where one phase can exclude a rotation are the two unsafe gaps i=1,n, and the rich protected gaps `{k,k+1,l,l+1}`. Since k≡2 and l≡0, the latter contribute at most two gaps outside residue 0, namely k and l+1. Thus there are at most `(p−4)+2+2=p` gaps in the entire cyclic word that can carry rotations, contradicting R≥p+1. This handles the exceptional pattern without assuming the forbidden gaps are occupied.

For H=3, write k<l<t for the changes; their residues are the three distinct classes. The slopes are +u,−u,+u,−u. In phase s let V_s count negative-slope non-rich entries of C_s. Then

`V_s = #({i∈C_s:k<i<l} ∪ {i∈C_s:t<i≤n})`, `Σ_s V_s=M−1`,
`B0_s/u ≡ 7+3V_s+1_{s=0}−1_{s=2} ≡ 1+W_s`,
`W_s=3V_s−(M−1)+1_{s=0}−1_{s=2}`.

The endpoint corrections are +u at index 0 and −u at index n, and the rich base is −u. Directly distributing the two indicated integer intervals among residue classes gives the following **complete** table; entries are ordered as `(W_0,W_1,W_2)`:

| `(k,l,t) mod 3` | W |
|---|---|
| (0,1,2) | (1,0,−1) |
| (1,2,0) | (−1,1,0) |
| (2,0,1) | (0,−1,1) |
| (0,2,1) | (−1,1,0) |
| (1,0,2) | (0,−1,1) |
| (2,1,0) | (1,0,−1) |

For example, an interval of length divisible by three contributes equally to the three V_s, while a one- or two-point remainder contributes to its displayed starting residues; n≡2 mod 3. Thus some phase has W_s=0 and B0_s=u. By §4.1 it supplies at least p−2 identity rotations. If the +u increments are the majority, the disjoint outside pieces `x_1,…,x_k` and `x_l,…,x_t` have total P+1=2p−4; if the −u increments are the majority, `x_k,…,x_l` and `x_t,…,x_(n−1)` have total M+1=2p−4. Section 5 applies. Hence **all one-sign-class words with H≤3 are selectable**.

### 6.3 Further complete regions with unequal sign-classes allowed

For H=2 with changes k<l and slopes u,v,w, suppose both end lengths satisfy `k≥3` and `n−l≥3`. If l−k is divisible by three the two rich windows occur in one phase, settled by §2. Otherwise, if l−k≥3 it is at least 4. The non-rich indices k−3,k+3 in the first rich phase show `[u]=[v]`; l−3,l+3 in the other show `[v]=[w]`. Section 6.2 applies.

It remains to consider l−k∈{1,2}. Each rich phase samples both end classes at its indices ±3, so badness forces `[u]=[w]`; write w=±u. The midpoint criterion at the first change, with common phase class `[u]`, gives `v∈{2u,−u}`, and at the second gives `v∈{2w,−w}`. For p≥7 the two sets are disjoint if w=−u. Thus w=u. If v=−u, all increments have one sign-class and §6.2 applies; if v=2u, closure gives `(n+l−k)u=0`, requiring p to divide 10−(l−k), either 9 or 8, impossible. Therefore **H=2 is selectable whenever both end segment lengths are at least three**, even if the middle segment is short.

More generally, if H≤3 and every segment length is at least three, then an avoiding word has distinct change residues; hence every internal segment length is actually at least four. For each change, the non-rich indices three before and three after it in its rich phase sample its two adjacent segment slopes, including boundary indices 0 or n when appropriate. Badness forces the two slopes into the same sign-class. All slopes therefore have one sign-class, contrary to §6.2. Thus **all segment lengths at least three** is another complete region for H≤3.

At p=7, the proof uses F=19, n=11, at least eight actual rotations, five eligible in a rich phase, and the explicit repeated-label argument in §5. The restricted uniform r=0 set has five d-points and misses two offsets; the outlier and r=1 sets have six and miss one. No p=7 case is inferred from an asymptotic theorem.

## 7. Full actual two-rotation family and all-selection transfer

The preceding pair restrictions are only a subfamily. For any triple `(a',b',c')`, let u,v be selected rotation exponents in its first and second interior gaps, with an absent rotation written as 0 **while separately tracking selection count**. The full actual one-omission set is

`T(a',b',c';u,v)={b'−c'+u−v, a'−c'−u−v, a'−b'−u+v}`.

This follows by omitting a', b', or c' in physical order. For any two distinct actual rotations, even two in one triple, zero in the sum of these full sets plus the actual inter-block/end offsets is necessary and sufficient for that fixed cut's two-per-triple identity family. It is not a test for every possible length-2p selection.

For the full word, use `Z[X]/(X^p−1)` and matrices

`S_x=[[0,X^x],[X^(−x),0]]`, `R_y=diag(X^y,X^(−y))`.

Cyclically start at A1, list the F actual reflections xi in order, and let ρ_i∈{0,1} and y_i record the actual rotation, if any, in the following original cyclic gap. Form the ordered, noncommutative matrix product

`P(t,z)=∏_(i=1)^F (I+t S_(xi)) (I+ρ_i t z R_(yi))`.

When ρ_i=0 the second factor is I; its undefined y_i is immaterial. Define

`N(W)=Σ_(r even, 0≤r≤min(R,2p)) [t^(2p) z^r X^0] P(t,z)_(1,1)`.

The identities `S_x S_y=R_(x−y)`, `S_x R_y=S_(x−y)`, `R_y S_x=S_(x+y)` realize the actual dihedral product. Expanding each factor selects or omits that occurrence exactly once; all coefficients are nonnegative integers, even when a rotation exponent is zero. A top-left term has an even reflection count; since total length 2p is even, the rotation count is even. Therefore N(W) is **exactly the number** of length-2p identity subsequences in the cut order, including zero, two, four, and all other feasible even numbers of rotations. A cyclic cut induces a bijection on occurrence subsets; the selected products differ by cyclic rotation and hence conjugation. Thus the count is unchanged by returning to W's actual linear start, and

`N(W)=0  ⇔  every original-order length-2p selection has nonidentity product`.

No cancellation or computation is being asserted.

## 8. Exact remaining frontier and limits

Any avoiding word must simultaneously satisfy the original actual-word hypotheses, closure and nonzero increments, and:

* H=2 or 3; all rich change indices have distinct residues modulo three;
* at least two different increment sign-classes occur;
* for H=2, `k1≤2` or `n−k2≤2`; for H=3, at least one of the four segment lengths is 1 or 2;
* every phase has one of the bad patterns in §3, and **every** compatible actual pair satisfies its applicable §4 offset restriction, equivalently the detailed graph conditions in §4.1;
* the full-family conditions of §7, in particular `N(W)=0`.

The first four bullets are necessary only. Adding the last coefficient equation makes this an exact characterization of the surviving actual-word avoidance set, because N=0 is itself equivalent to actual ALL-selection avoidance; no implication from the first four bullets to N=0 is claimed. The first unresolved global obligation is to prove positivity of N for every remaining actual word, or supply a separately validated actual word with N=0. Neither existence nor nonexistence of such a word is asserted here. No result beyond the given nine-run/H≤3 domain follows.

## 9. Read declarations, conditional imports, and process limits

Before any packet body read or mathematical reasoning I read the entire manifest, freeze receipt, final binding, parent metadata supply, actual dispatch receipt, and all 22 listed controls as status/permissions only. The actual dispatch names this agent. I wrote `prebody-ack-v1.md` and directly delivered the prebody acknowledgement to Main before opening the packet. The owner-directory listing showed both new output names absent before their creation; the available write tool has no atomic exclusive-create option, so this is not an `O_EXCL` claim.

After acknowledgement I read the sole literal part completely through its ending in raw windows `1–20`, `21–40`, `41–60`, `61–80`, `81–100`, `101–120`, `121–140`, `141–160`, `161–180`, `181–200`, `201–220`, `221–234`. The `21–40` window was accidentally read a second time consecutively before advancing to `41–60`; there was no skipped packet content or early access to the ending. Each display was at most 20 LF and below 30,000 bytes; no clipping was observed and no clipping recovery was needed. The part contains S1 F849 complete source LF 1–186 and S2 disposition complete source LF 1–38. Initial compact administrative reads elided portions; the five administrative records were re-read in full raw form before acknowledgement. Parent-reported whole-part SHA256 is `e111ad17a59fd3d0de15c33a45f11fd0a1a7096f6b0f4fcf514afd3bddb18f45`; S1 is `f73071bc6938c20a7f6b2be5f99b76f686b54fb6aef44c34ce0670950e85cfbb`, S2 is `e1931d621a04153d8b90bf5cf25220ad8baee57b7758a826e047472cfd143f00`. These are parent-supplied metadata, not independently executed hashes.

No source links or unlisted mathematical bodies were opened. In particular the f603 author, f638/f639 reviews, and f640 narrative/source/run receipt named in S2 are missing load-bearing bodies **if** their historical claims or separate results are imported; those imports remain conditional and are not used in the proofs above. Complete-original-source correspondence and novelty are unassessed. The f602 status control was read only for exclusion; its held episode and all genuinely held proof/method/selection/planning/verification/reporting/confidence/downstream consumers remain NONINPUT. No peer science, network, external model, code, scientific execution, test, compilation, child subprocess, or prepared verifier was used; hence there is no prepared-code hash. The memory summary and general protocol were nonmathematical administrative context. No private-cognition or historical nonexposure certificate is claimed. Parent disposition and independent checking are separate obligations.
