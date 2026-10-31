# Support 48: a two-case branch reduction (t ∈ {27,28} beyond t=24) and an unconditional distance-one interface

Owner **PhysicsAME46-2**. Native clock observed before writing: `Fri Oct 30 04:13:55 PDT 2026`; not an asserted completion time. **WRITTEN author candidate**, not independently reviewed, adopted, formally verified or novelty-cleared. All-variable arguments only; no selected state, array or assignment, no code, no solver, no enumeration, no certificate. No held v203/v124 material, no withdrawn certificate-dependent packet, and no pending review outcome is a premise.

## 0. Adopted interfaces used

- **(A1)** Every normalized complex AME(4,6) state has at most t=28 coefficients of modulus 1/6: item 3 of `institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-ame46-support-47-excluded-and-at-most-28-maximal-coefficients-composition-parent-v1.md`, SHA-256 `4101ae2cdb08aa2c9238b680359dc2793bcccfc3af672fbb92be9dd460a41003`. It inherits the f113 classical no-OLS(6) import and prior t≤30 boundary; that inheritance is restated wherever (A1) is used.
- **(A2)** Conditional no-six-symbol result (f293): `…/dispositions/physics-6-ame48-t24-no-six-symbol-residual-parent-v1.md`, SHA-256 `4f0b0399091d72bd0017a27888f44b4688d04976e72742f5f63e004cb6f5445e`. Its exact content is: **assuming** the N=48, t=24 residual E has no distance-one pair, no party has six E symbols. Used only in §3, only through its contrapositive (six symbols ⇒ a distance-one pair exists), and only at its stated hypothesis scope.

Everything else is proved inline.

## 1. Theorem 1: at support 48 only t ∈ {24, 27, 28} remain

Let ψ be a normalized complex AME(4,6) state in a product basis with N=48 nonzero coefficients and t of modulus 1/6; let E be the other support, n=36−t, |E|=48−t.

**(1.1) Row bound.** In each 2|2 cut, U=6ψ is a 36×36 unitary. A modulus-one entry is the sole nonzero of its row and column. Deleting those t rows and columns leaves an n×n unitary V supported on E with every line of degree at least two (a unitary line with one nonzero would have modulus one and would have been deleted). Hence |E| ≥ 2n and `N ≥ 72−t`; at N=48 this gives t ≥ 24, and (A1) gives t ≤ 28. The row-degree excess `e=|E|−2n=t−24` is identical in the three cuts.

**(1.2) Three support facts, proved inline.** (i) *Unique overlap*: two distinct rows of a unitary sharing exactly one nonzero column have a one-term, nonzero inner product; likewise columns. (ii) *Components are square*: rows of a connected support component are orthonormal vectors supported on its columns, so #rows ≤ #columns, and symmetrically. (iii) *Partner rows*: every row R of a component with a degree-two row ρ in it: any row meeting ρ's column pair {c,c′} in exactly one of c,c′ shares exactly one column with ρ, impossible; a row meeting both c,c′ exists since column degrees are at least two.

**Lemma B′ (no excess-one component).** In a component with row degrees summing to 2m+1, exactly one row R has degree 3 and all others degree 2. Let R have columns a,b,c. By (iii) every other row meeting R is a two-subset of {a,b,c}, and two distinct such subsets intersect in one column, impossible by (i); so all are the same pair, and the remaining column of R then has degree one. Contradiction.

**Lemma C′ (excess-two components).** Row degrees sum to 2m+2. If one row R has degree 4, all others have degree 2; by (iii) they are two-subsets of R's four columns, pairwise equal or disjoint, hence only {c1,c2} and {c3,c4} occur; then column c1 (supported on R and the {c1,c2}-rows) and c3 (supported on R and the {c3,c4}-rows) share exactly the row R, contradicting (i) for columns. If two rows R1,R2 have degree 3: if their supports meet in exactly two columns {c1,c2}, with R1={c1,c2,x}, a further row containing x is a two-subset meeting R1 twice and R2 once, impossible by (i), so x has degree one; hence R1 and R2 have the same three-column support S. Every further row meeting them is a two-subset of S, all equal by (i), say {c1,c2}; the third column of S has degree two (R1,R2) as required, connectivity forces exactly one further row, and the component is 3×3 with 8 entries and row/column degrees (2,3,3).

**(1.3) t=25 and t=26 are impossible.** For t=25, e=1: component excesses are nonnegative (each component is a square unitary block), sum to 1, so one equals 1, excluded by Lemma B′. For t=26, e=2: excesses sum to 2 with none equal to 1, so one excess-two component, a 3×3 eight-entry block (Lemma C′) on 3 rows, and all other components excess zero, hence full 2×2 blocks by (iii)-style two-regularity (each row degree 2 forces disjoint identical pairs). So n=3+2k is odd, but n=10. Contradiction.

So **t ∈ {24, 27, 28}**. This reduction uses (A1) only; the exclusions of t=27 and t=28 remain open here. ∎

## 2. Theorem 2: unconditional distance-one interface at (N,t)=(48,24)

Assume N=48, t=24. Then n=12, |E|=24=2n: every residual row and column has degree exactly two, and every one of the six pair systems has 12 E-carried values, each with exactly two E extensions. For a residual symbol a at party i, the number d_i(a) of its E-partner values is the same in each of the three systems containing i (the six values (a,·) of any such system split into 6−d_i(a) E-carried and d_i(a)... precisely: d_i(a)=|π_j(E_a)| for every j≠i, since |E_a|=2d_i(a) follows by summing the two extensions of each E value, and the count of E values (a,·) is j-independent because P occupies exactly the other values once each).

**Theorem 2.** If E contains two words differing in exactly one coordinate, then either some party has at least six E symbols, or E is the disjoint union of two isolated blocks S×{d0,d1} and C with |S|=6, where S is a set of triples on the other three parties with every pair projection injective and every value occurring exactly twice.

*Proof.* Let the pair be w1=(a,b,c,d0), w2=(a,b,c,d1); they are the two extensions of the values (a,b), (a,c), (b,c).

*Propagation.* Work in the cut with rows the (A,D) values and columns the (B,C) values. Rows (a,d0) and (a,d1) share the column (b,c), so by unique overlap they share a second column. Row (a,d0) has degree two, containing w1 and some u=(a,b°,c°,d0) with (b°,c°)≠(b,c); row (a,d1) contains w2 and some v; the shared second column forces v=(a,b°,c°,d1). So u,v is another distance-one pair over the triple s′=(a,b°,c°) sharing the A coordinate with s=(a,b,c), and the D pair {d0,d1} is preserved. The same argument in the cuts (B,D)|(A,C) and (C,D)|(A,B) gives triples sharing b and c. A triple s″≠s agreeing with s in two base coordinates is impossible: the pair value they share has exactly two extensions, both already used by s. Hence from each triple there are exactly three neighbours, one per base coordinate, and the closure S of this operation is a simple cubic graph on triples. The same row argument in a cut with rows (A,D) shows the two words at value (a,d0) belong to the two triples containing a, so **every base value occurs in exactly two triples of S**, and each pair projection of S is injective (a shared pair value has its two extensions inside one triple).

*Coefficients make S bipartite.* For the two rows (a,d0),(a,d1) above, orthogonality reads ψ(w1)conj(ψ(w2))+ψ(u)conj(ψ(v))=0, i.e. x_s + x_{s′} = 0 with x_s=ψ(s,d0)conj(ψ(s,d1)), which is nonzero. Along the cubic graph the quantity x therefore flips sign, so S has no odd cycle. Hence m=|S| is even; cubic and simple exclude m=2,4; m ≤ 12 since S uses m distinct values of each base pair system. So m ∈ {6,8,10,12}.

*Isolation.* Every pair value used by S×{d0,d1} — of base×base type (one value per triple, extensions both inside) or base×D type (values (s_i,d), two extensions inside) — already has its two extensions inside S×{d0,d1}. No further E word shares any such value, so in every cut S×{d0,d1} is a union of complete unitary blocks, and the complement C with its 24−2m words and 12−m values per system is itself an isolated zero-excess residual.

*Case m=12.* C is empty, E=S×{d0,d1}. The (A,D) system has 12 values (a,d) with d ∈ {d0,d1}, so at least six distinct symbols of A occur; likewise for B and C. This is the six-symbol alternative.

*Case m=10.* C has four words and two values per system, each with both extensions in C. Within C the same fiber identity holds (isolation gives |C_a|=2·(#C values (a,·)), j-independent). If some a had one C value, its two C words would share their value in all three systems containing A, hence be equal — impossible. So all C fiber degrees are at least two; their sum is 2, whence each party's C alphabet is a single symbol of degree 2, C lies in a one-point box and has at most one word, contradicting |C|=4.

*Case m=8.* The same degree bound gives C alphabets of size at most two, and size one is impossible (a single symbol would have four C values in each partner system, more than its two-symbol alphabet provides). So every C alphabet has exactly two symbols, each of C fiber degree two, and C meets every cell of every two-symbol pair exactly twice. In each cut C is then a 4×4 block with all lines of degree two, i.e. a disjoint union of 2×2 unitary blocks; the sub-tensor on C, normalized, has all three 2|2 flattenings unitary: it is an AME(4,2) state. That is impossible: with Pauli weights A_k (A_0=1), two-uniformity forces A_1=A_2=0; each three-qubit marginal has purity 1/2 (its complement is maximally mixed), giving weight-three sum A_3=3·4=12; global purity gives A_4=16−1−12=3; the positive spin-flipped state would have overlap (1−12+3)/16=−1/2 with the original. Contradiction.

Only m=6 remains, with C a twelve-word zero-excess block whose fiber degrees sum to 6 with each at least two, so every C alphabet has at most three symbols. ∎

## 3. Interface consequence and the exact unpaid premises

**Corollary.** At (N,t)=(48,24), conditional on no-OLS(6) and on the adopted f293 statement (A2): if some party has six E symbols then E also contains a distance-one pair; conversely a distance-one pair forces, by Theorem 2, either a six-symbol party or the m=6 decomposition.

So the two hypotheses are **equivalent up to the single m=6 branch**:

`no distance-one pair ⟺ no six-symbol party, unless E = (S×{d0,d1}) ⊔ C with |S|=6.`

**Exact unpaid premises.** (P1, classical, declared): no-OLS(6), needed in Theorem 1 only through (A1) and in §3 through the m=6 branch. (P2, unreviewed): the six-row selection statement — every twelve-word zero-excess residual block with six values per pair system admits a six-word pair-injective selection; with the six words selected from S×{d0,d1} by the bipartition (one D value per part; two triples sharing a base value lie in opposite parts, so no selected pair value repeats) this would compose with the 24 P words into a 36-word pair-injective family, i.e. OA(36,4,6,2), contradicting (P1). P2 is exactly the content frozen for review in the f296 source's six-row component analysis; it is not assumed here. Under P1 and P2, the equivalence above becomes unconditional, and the N=48, t=24 no-distance-one hypothesis is *interchangeable* with the no-six-symbol hypothesis at no additional cost.

## 4. Scope

Theorem 1 leaves t=27 and t=28 open (only (A1) and inline unitary facts are used). Theorem 2 is unconditional and does not use (A2); §3 uses (A2) only at its adopted hypothesis scope. No support-48 exclusion, no ≥49 bound, no witness, and no statement about other N or t is claimed. The author has prior exposure to the f296 source and to earlier withdrawn N=48 work; none of it is a premise. Review should check the propagation and isolation arguments in §2, the two excess lemmas of §1, and the AME(4,2) spin-flip computation.
