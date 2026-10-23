# PURE corner: working notes v1 (proved lemmas so far; not a result)

Written at 2026-10-19T18:15:51-0700 under `SCOPE-FREEZE-v1.json` (SHA256 `0481f24b0e0dc75321220584d7e5db2914589db5c1749a723621040e3e14d99a`). Written mathematics only. No candidate is a premise; every fact below is re-proved here.

**Notation.**
- H1: genuine pairwise-orthogonal QLS(8), Q_1,...,Q_5. H2: Q_s(0,c) = w e_c. H4 (part): q^1, q^7 ∈ V_A = span{e_1,e_2,e_3} have full support, and q^6 ∈ span{e_2,e_3} has support {2,3}. Column 0 is orthonormal.
- Square-1 vectors are written q^k := Q_1(k,0) and Q(i,c) := Q_1(i,c).
- r ∈ {1,7}, and r' is the other element of {1,7}. Rows 1 and 7 play symmetric roles in every fact used below; H3 (SB2) is never used.
- a^r_d := <e_d,q^r>, all nonzero. P_r := V_A ⊖ q^r = span{q^6, q^{r'}}.
- Columns 1 and 2/3 are NOT interchanged: column 1's corner line is span{q^6}.

## N0. Re-proved basics

- **(F1)** Coordinate c and own index i are absent at (i,c).
- **(F2)** At a cell z = (i,c) with i, c >= 1, and for d != c, at most one square has <e_d,Q_s(z)> != 0. Proof: H1 on z and (0,d). Likewise, for k != i at most one square has <q_s^k,Q_s(z)> != 0. Proof: H1 on z and (k,0).
- **(AX)** For s >= 2, q_s^1, q_s^7 ⊥ V_A ⊕ span{e_0}, and q_s^6 ⊥ e_0, e_2, e_3.
  - The first two follow from H1 on (r,0),(0,d) with d ∈ supp q^r, which gives <e_d,q_s^r> = 0. The e_0 part follows from column-0 orthonormality.
  - For q_s^6 the same argument applies with d ∈ {2,3} = supp q^6.
  - It follows that, in row r, every square s >= 2 has mass exactly 1 on each e_d with d ∈ {1,2,3}.
- **(L) Corner lines.** P_A Q(r,c) ∈ span{ℓ_{r,c}}, where ℓ_{r,c} := conj(a^r) × e_c has support exactly A \ {c}. Moreover:
  - <ℓ_{r,c},ℓ_{r,c'}> = −a^r_{c'} conj(a^r_c) for c != c' (same row);
  - <ℓ_{1,c},ℓ_{7,c'}> = −a^1_{c'} conj(a^7_c) for all c, c'.

  *Proof.* P_A Q(r,c) ⊥ q^r and ⊥ e_c; the explicit vector is orthogonal to both. The bilinear Lagrange identity gives (a^s · conj a^t)δ_{cc'} − a^s_{c'} conj(a^t_c), and a^1 · conj a^7 = <q^7,q^1> = 0, while a^r · conj a^r = 1. All the numbers are nonzero.

  For c = 1, ℓ_{r,1} ∝ q^6, because q^6 ⊥ q^r and q^6 ⊥ e_1.

## N1. Pure-A cell: row structure (Lemma P1)

Let (r,c) be pure-A, i.e. Q(r,c) = ω ℓ̂_{r,c} ∈ V_A. Then:
- (a) The partner cell (r',c) is A-free.
- (b) All cells of row r other than (r,c) and exactly one further cell (r,c*), with c* ∈ {4,5,6,7}, are A-free.
- (c) Q(r,c*) = ω' m, where m := the unit vector of P_r orthogonal to ℓ_{r,c}. For c = 1, m ∝ q^{r'}. For c ∈ {2,3}, m has full support {1,2,3} and nonzero coefficients on both q^6 and q^{r'}.
- (d) span{Q(r,c),Q(r,c*)} = P_r. The five other cells of row r form an ONB of Z⊕B⊕C = span{e_0,e_4,...,e_7}.
- (e) In row r, the A-support excess of squares 2..5 is at most 1.

*Proof.*
- **(a).** 0 = <Q(r,c),Q(r',c)> = conj(ω) z <ℓ̂_{r,c},ℓ̂_{r',c}> by column orthonormality, where z is the coefficient of P_A Q(r',c) along ℓ̂_{r',c}. The inner product is nonzero by (L), so z = 0.
- **Other A-parts of row r lie on span{m}.** Row orthonormality gives <ℓ̂_{r,c},Q(r,x)> = 0 for x != c, so P_A Q(r,x) ∈ P_r ⊖ ℓ_{r,c} = span{m}.
- **Other corner cells are A-free.** For a corner x = c' != c, P_A Q(r,c') ∈ span{ℓ_{r,c'}} ∩ span{m}. This is 0, because ℓ_{r,c'} is not ⊥ ℓ_{r,c} by (L), so it is not parallel to m.
- **Support of m.**
  - m contains no e_d alone, because e_d ∉ P_r.
  - The only support-2 lines of P_r are the three ℓ_{r,x}: P_r ∩ span(A \ {x}) is the line ℓ_{r,x}.
  - m ∥ ℓ_{r,x} would need ℓ_{r,x} ⊥ ℓ_{r,c}, which is false for x != c by (L), and impossible for x = c.
  - So |supp m| = 3.
- **Slot count.**
  - Row r has 18 A-slots, (cell, d ∈ A \ {col}). By (F2), each slot is used by at most one square.
  - Squares 2..5 need mass 1 on each of the 12 pairs (s,d) by (AX), so they use at least 12 slots.
  - Square 1 uses 2 slots at (r,c) and 3 at each of the k >= 1 cells carrying the m-direction, which has mass 1.
  - So 2 + 3k <= 6, hence k = 1. That single cell carries m-mass 1, so it equals ω' m. Since m has full support, c* ∉ {1,2,3}.
  - The excess is at most 18 − 12 − 5 = 1.
- **Own coefficients of m.**
  - For c = 1, P_r = span{q^6, q^{r'}} and ℓ ∝ q^6, so m ∝ q^{r'}.
  - For c ∈ {2,3}, m ∝ q^6 would force ℓ_{r,c} ∥ q^{r'}, which is impossible by support. m ∝ q^{r'} would force ℓ_{r,c} ∥ q^6, which is impossible because ℓ_{r,c} has a nonzero e_1-entry for c ∈ {2,3}.
- **(d).** Row r spans the 7-dimensional space orthogonal to q^r. Removing P_r leaves Z⊕B⊕C.
QED

## N2. Purity of squares 2..5 at (r,c*) (Lemma P2)

At (r,c*), every square s >= 2 has Q_s(r,c*) = ω e_d, and the four d's are exactly {0,4,5,6,7} \ {c*}.

*Proof.* Square 1 occupies the coordinates {1,2,3} at (r,c*), because supp m = A, so by (F2) no square s >= 2 has an A-coordinate there. By (F1), coordinate c* is excluded. That leaves the four coordinates {0,4,5,6,7} \ {c*} for four squares with nonempty, pairwise disjoint supports (F2). So the supports are singletons, and all four coordinates are used. QED

At (r,c) itself, squares 2..5 lie in span{e_0,e_4,...,e_7} with pairwise disjoint nonempty supports in a 5-set, so at most one of them has support of size 2.

## N3. Column-c structure (Lemma P3)

Column c's A-content is the projector onto span(A \ {c}). (r,c) carries ℓ̂_{r,c} with mass 1. So every other cell of column c has its A-part on n_c, the unit vector of span(A \ {c}) orthogonal to ℓ_{r,c}, and these carry n_c-mass 1 in total.
- For c = 1: n_1 = v ⊥ q^6 in span{e_2,e_3}, with support {2,3}.
- For c ∈ {2,3}: n_c ∝ P_{A \ {c}} q^r, with support A \ {c}. This holds because ℓ_{r,c} ⊥ q^r and ℓ_{r,c} ∈ span(A \ {c}).

The corner (6,c) for c ∈ {2,3} has corner line span{e_1}, by q^6 ⊥ and e_c ⊥. Its A-part lies in span{e_1} ∩ span{n_c} = 0, since n_c has two nonzero entries. So (6,c) is A-free when c ∈ {2,3}.

## N4. Column 1 twin facts (c = 1 only)

If (r,1) is pure-A, then Q(r,1) = ω q^6 = ω Q(6,0). This is a twin of (6,0). For every cell z, G_1((r,1),z) = conj(ω) <q^6,Q(z)>. Since (r,1) and (6,0) share no line, H1 gives Q_s(r,1) ⊥ q_s^6 for s >= 2. Likewise Q(r,c*) = ω' q^{r'} is a twin of (r',0), and Q_s(r,c*) ⊥ q_s^{r'} for s >= 2.

(Open beyond this point. The next step is the cross-row and full five-square analysis.)
