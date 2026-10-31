# Arbitrary translate intersections in odd-prime Tuscan arrays: half-orbit bound and equality rigidity

Owner: **InfoRecursiveMDS18-2**, slot **info-4**. Actual native clock observed before writing: **Wed Oct 28 22:02:17 PDT 2026**.

**NEW author-WRITTEN candidate, unreviewed.** This is a universal necessary condition for the original unrestricted linear T2(11) problem, not a search of a selected subclass. The proof uses only the definition of T1/T2 and elementary arithmetic in the cyclic group of prime order. No solver, scientific program, kernel arithmetic, selected example or external source is used. No independence, formal/kernel, novelty or parent-adoption claim is made.

## 1. Quantifiers and original-object interface

Let p ≥ 5 be an odd prime, q = (p−1)/2, and A any T1(p) array: p linear permutation rows on p symbols, with every ordered pair of distinct symbols adjacent exactly once across the rows. Let g be **any** p-cycle on the symbols. For **any** permutation row R, put

I = {t ∈ Z/pZ : the position-wise image g^t R is a row of A}.

The set I is an arbitrary subset of Z/pZ. It is NOT assumed to be consecutive, a subgroup, a complete orbit or a symmetry of A. In particular, R may be taken to be any actual row of A. Label the symbols by Z/pZ so that g acts by addition of 1, and write R = (a_0, …, a_{p−1}). A distance-d event starting at a_i has difference a_{i+d}−a_i, for i+d < p; distances are linear, with no wraparound.

## 2. Translate packing identity

For d ∈ {1,2} and nonzero e ∈ Z/pZ, define the set of sources

S_e^(d) = {a_i : i+d < p and a_{i+d}−a_i = e}.

For d = 1, or also d = 2 if A is T2(p), all the sums t+s with t ∈ I and s ∈ S_e^(d) are distinct. Indeed, an equality t+s = u+z makes the translated ordered pairs (t+s,t+s+e) and (u+z,u+z+e) identical. The defining uniqueness at distance d then forces the same occurrence. Distinct columns in a permutation row have distinct sources, so the same occurrence means t=u and s=z. Consequently

|I| · |S_e^(d)| ≤ p.                                      (1)

Equivalently, if two sources s,z in S_e^(d) are different, their difference z−s is not in I−I. Otherwise some t,u ∈ I would satisfy t−u = z−s and give a repeated distance-d event. This is an exact consequence of the actual rows, not a marginal relaxation or an assertion that all allowed source sets are realizable.

## 3. Universal half-orbit bound (T1)

**Theorem A.** For every A, g and R in §1,

|I| ≤ (p−1)/2.

**Proof.** If |I| ≥ (p+1)/2, then I−I is all of Z/pZ: for every δ, the two sets I and I+δ have sizes summing to more than p, so they intersect. By §2 each adjacent difference e occurs at most once in R. There are p−1 adjacent differences, all nonzero, so they are exactly all nonzero residues. Their sum is zero, since the residues pair as e and −e. But their telescoping sum is a_{p−1}−a_0, which is nonzero because R is a permutation. Contradiction. ∎

Thus any unrestricted T2(11) has **at most five rows in any translate orbit under any 11-cycle**, even if the included translates are completely nonconsecutive and the full row set has no symmetry. This strengthens the full-orbit obstruction by covering every majority subset, not only a complete cyclic row block.

## 4. Equality forces an arithmetic progression (T1)

**Theorem B.** If |I| = q, there are u ∈ Z/pZ and δ ≠ 0 such that

I = {u, u+2δ, u+4δ, …, u+2(q−1)δ}.                       (2)

Moreover

(Z/pZ) \ (I−I) = {δ, −δ}.                               (3)

**Proof.** The p−1 adjacent differences of R cannot all be distinct: the final sum argument of Theorem A applies to R alone. Choose two equal adjacent differences whose sources differ by δ ≠ 0. By §2, I and I+δ are disjoint. As p is prime, stepping by δ gives one p-cycle. In its cyclic order, mark the q elements of I. Between consecutive marks the positive gap is at least 2, because two δ-neighbours cannot both be marked. The q gaps sum to p = 2q+1. Therefore exactly one gap is 3 and every other gap is 2. Start immediately after the unique gap 3; this gives (2).

Put h=2δ. Its difference set is {jh : −(q−1) ≤ j ≤ q−1}, a set of 2q−1=p−2 distinct residues. The two missing residues are qh and −qh. Since qh = 2qδ = (p−1)δ = −δ in Z/pZ, these are exactly δ and −δ. ∎

The excluded nonzero offsets in (3) are a single unordered pair. Thus **all** repeated adjacent differences in R must have source offsets in the same pair {δ,−δ}; the choice coming from any one repeated adjacent difference controls all the others. If A is T2(p), the same source-offset restriction holds for every repeated distance-two difference as well.

Equation (1) also gives |S_e^(d)| ≤ 2 when |I|=q and p≥5, because 3q > 2q+1=p. Hence neither distance can have a difference occurring three times.

## 5. Exact equality normal form for the original order 11

For p=11, q=5, take h=2δ and replace the generator g by g^h and the reference row R by g^uR. These operations are just relabelling the same cyclic action and selecting a row already in A. The five actual rows become

R', g'R', (g')²R', (g')³R', (g')⁴R',

where g'=g^h. Label symbols so g' acts as +1. In this normalized coordinate I={0,1,2,3,4}, so I−I={−4,…,4} and its complement is {5,−5}.

Every unrestricted T2(11) with such a five-row intersection must therefore admit this exact description:

1. The five rows are the consecutive translates R'+t for t=0,1,2,3,4, under a suitable 11-cycle generator; there are six further actual rows, with no symmetry assumed for them.
2. The ten adjacent differences of R' have multiplicity at most 2. If two are equal, their two source SYMBOLS differ by ±5 modulo 11. At least one adjacent difference repeats. If t_1 differences occur twice, then 1≤t_1≤5, exactly t_1 of the ten nonzero differences are absent, and 10−2t_1 occur once.
3. The nine distance-two differences likewise have multiplicity at most 2. Equal ones have source SYMBOLS differing by ±5 modulo 11. If t_2 differences occur twice, then 0≤t_2≤4, exactly 1+t_2 of the ten nonzero differences are absent, and 9−2t_2 occur once.
4. These restrictions are separate for distances 1 and 2. A difference used at distance 1 is NOT thereby forbidden at distance 2. Source-symbol offsets ±5 are NOT a statement about column offsets.

Conversely, for any proposed R', items 2 and 3 without the count wording are exactly the conditions making its five translates event-disjoint at the corresponding distance: an inter-row collision requires two source symbols with difference in I−I. They do not ensure that the six remaining rows exist, and no such completion is supplied here.

## 6. Scope and exact remaining gap

**WRITTEN:** Theorems A and B for every T1(p), every odd prime p≥5, every p-cycle and every permutation row; the additional distance-two consequences for every T2(p); and the all-variable equality normal form for p=11.

**OPEN:** Whether any such equality-normal-form five-row system can be completed to T2(11), and whether a T2(11) exists with every such intersection of size at most four. No case in either residual is excluded by this packet. No enumeration or native execution is performed, and the unfinished circular encoder is not an input.

The original target remains an unrestricted actual 11×11 linear T2 square or a contradiction for EVERY such array. Neither is supplied. No original-solution, support-9, literature-status or novelty promotion follows. The historical quarantines and the new certificate admission qualification remain separate, unchanged and NONINPUT to this proof.
