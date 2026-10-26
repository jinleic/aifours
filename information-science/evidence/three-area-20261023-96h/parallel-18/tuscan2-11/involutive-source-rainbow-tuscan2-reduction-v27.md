# Tuscan-2 by Cutting Method from an involutive source: multiplicity at most two and exact pairing of destroyed triples

Actual `/bin/date` before this body: **Sun Oct 25 23:20:54 PDT 2026**. InfoRecursiveMDS18-2, slot info-4. NEW WRITTEN CANDIDATE (reduction), not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO.

## 1. Setting and notation

As in v26 (SHA256 `df5ab1c9332880cca1dabd070b746b44e776804080dc480e1f439aa5056e7977`): source cycles partition the 110 arcs; the pattern P=(p_0,...,p_10); C^(k) is the cycle containing (p_k,p_(k+1)) and is cut there; B_k is the predecessor of p_k and A_(k+1) the successor of p_(k+1) in C^(k). A source triple (a,x,b) is three consecutive symbols of a source cycle; mu(a,b) counts source triples with ends a,b. A triple is destroyed (not an interior triple of the final rows) iff one of its two arcs is a pattern arc, since each pattern arc is the cut of the unique cycle containing it. The destroyed triples are exactly

`tau1_k=(B_k,p_k,p_(k+1))`, `tau2_k=(p_k,p_(k+1),A_(k+1))`, k=0..9.

The source is **involutive** if every source neighbour permutation K^src_x is an involution (for example every reversal-closed source); then (a,x,b) is a source triple iff (b,x,a) is, and mu(a,b)=mu(b,a). M_0 is the set of pairs with mu=0, M the final square's missing distance-2 set, P2 the pairs (p_i,p_(i+2)), R9 their reverses (p_(i+2),p_i), i=0..8.

## 2. Reverse survival

**Lemma 1.** In an involutive source the reverses (p_(k+1),p_k,B_k) and (A_(k+1),p_(k+1),p_k) of the destroyed triples are source triples and are not destroyed.

Proof. (p_(k+1),p_k) is never a pattern arc (it would need p_(k+2)=p_k). (p_k,B_k) is a pattern arc only if B_k=p_(k+1), and (A_(k+1),p_(k+1)) only if A_(k+1)=p_k; both are impossible in a cycle of length eleven.

## 3. Multiplicity at most two

**Theorem 2.** If a Cutting-Method square from an involutive source is Tuscan-2, then:

1. mu(a,b)<=2 for every pair; when mu(a,b)=2, exactly one middle of (a,b) and the OTHER middle of (b,a) are destroyed.
2. P2 ∪ R9 ⊆ M_0 and R9 ⊆ M.
3. |M_0|=20-F_d, where F_d is the number of mu=1 pairs whose only triple is destroyed; F_d<=2, so |M_0| is 18 or 20 and |M_0|=2·#(unordered mu=2 pairs).

Proof. (1) Let X be the common middle set of (a,b) and (b,a), |X|=mu. By Lemma 1 a middle destroyed for one direction survives for the other, so the destroyed sets D_ab, D_ba are disjoint; Tuscan-2 gives |D_ab|,|D_ba|>=mu-1. Hence 2(mu-1)<=mu. (2) Pattern distance-2 pairs have mu=0 by the rainbow Theorem 1 (packet SHA256 `553831a49b73388c5bf72b5440b9a3f39124550920a277150944857e95728014`), so their reverses also have mu=0; a reverse (p_(i+2),p_i) is not itself in P2, so it is absent from the final square. (3) The final square has 90 distinct pairs from surviving source triples and 9 from P; counting surviving pairs gives |M_0|+F_d=20. M has eleven pairs and contains R9 (nine) and the F_d pairs, so F_d<=2. Since mu sums to 110 over 110 pairs, #(mu=0)=#(mu=2 ordered).

## 4. Exact pairing of destroyed triples

**Lemma 3.** Every destroyed triple with mu=2 is paired with exactly one other destroyed triple killing the reverse pair, and the pair has one of three forms:

- (i) tau1_k with tau2_(k+1) (0<=k<=8), iff B_k=A_(k+2)=w; the pair {w,p_(k+1)} has middles p_k,p_(k+2).
- (ii) tau1_k with tau1_j, iff B_k=p_(j+1) and B_j=p_(k+1); then |j-k|>=3.
- (iii) tau2_k with tau2_j, iff A_(k+1)=p_j and A_(j+1)=p_k; then |j-k|>=3.

Proof. For tau1_k the reverse pair (p_(k+1),B_k) keeps its middle p_k (Lemma 1), so its other middle y must be destroyed, i.e. (p_(k+1),y,B_k) is some tau1_j or tau2_j. Matching coordinates gives (ii) or (i). The case of tau2_k is symmetric and gives (i) or (iii). The distance bounds come from B_k not in {p_(k-1),p_k,p_(k+1)}, A_(k+1) not in {p_k,p_(k+1),p_(k+2)} (distinct cycles carry distinct arcs) and from mu=2 pairs not lying in P2 ∪ R9. In particular tau1_9 and tau2_0 can only be of types (ii), (iii) or fully destroyed.

## 5. Column multisets

Column 9 of the final rows is (B_0,...,B_9,p_9) and column 1 is (A_1,...,A_10,p_1). By the identity deg_out_M=c_9, deg_in_M=c_1 (v24 §7.3, SHA256 `e1fa1bd4dc53a90559b7b40a41bfbcab35ad31f96057f7d0121fb15a37194422`) and R9 ⊆ M with |M|=11:

`B-values = {p_2,...,p_8,p_10} plus the tails of the two arcs of M minus R9`,
`A-values = {p_0,p_2,...,p_8} plus the heads of those two arcs`.

## 6. Status and nonclaims

This is a reduction of the involutive Cutting-Method family for Tuscan-2(11), not an obstruction: the conditions of §§3–5 were not shown inconsistent, and no source realizing them was constructed. Developed sources remain excluded (v24 Corollary 6.3). Non-involutive sources are not covered. No Tuscan-2(11) table and no all-array obstruction is supplied; original target, HOLD, cutoff/deadline and all process histories, including the checkpoint045 withdrawal, are unchanged. This candidate needs its own complete source-bound gate.
