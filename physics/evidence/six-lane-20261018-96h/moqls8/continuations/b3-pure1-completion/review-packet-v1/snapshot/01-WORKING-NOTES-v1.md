# PURE1 completion: working notes v1 (proved lemmas and the old-witness extension obstruction)

Written at 2026-10-19T21:53:27-0700 under `SCOPE-FREEZE-v1.json` (SHA256 `e1af028ec4a123426fa2f21af3991dd63bd7194fa27f1b4c0ce7708d0fa2c3cb`). Written mathematics only; no candidate is a premise. Not a result package.

Notation: H1 (actual QLS, pairwise orthogonal; tensor rule (T): for distinct cells z,z' and squares s != t, <Q_s(z),Q_s(z')><Q_t(z),Q_t(z')> = 0), H2 (Q_s(0,d) = w e_d), and template supports supp q^1 = supp q^7 = {1,2,3}, supp q^6 = {2,3}, supp q^2 = supp q^3 = {6,7}, supp q^4 = supp q^5 = {4,5}, where q^i := Q_1(i,0), q_s^i := Q_s(i,0). D := {0,4,5,6,7}, W := {4,5,6,7}, V_A := span{e_1,e_2,e_3}. r in {1,7}, r' the other.

Elementary rules, each from (T) and orthonormality:
- (C1) Q_s(i,c) has zero coordinate c (i,c >= 1).
- (C2) At an interior cell, at most one square has a nonzero coordinate d (pair with (0,d)); at (i,0), likewise for d != 0 (pair (i,0),(0,d)).
- (C3) At (i,c), c >= 1, and k != i, at most one square has <q_s^k,Q_s(i,c)> != 0 (pair with (k,0)).

## L1 (column-1 pure corner shape)
If Q_1(r,1) is in V_A then Q_1(r,1) = w q^6, and there is exactly one j in W with Q_1(r,j) = w' q^{r'}; the other five interior cells of row r form an ONB of span{e_d : d in D}; Q_1(r',1) is A-free.
Proof. P_A Q_1(r,1) is orthogonal to e_1 and q^r inside V_A; q^6 is such a vector (supp {2,3}, q^6 orthogonal to q^r), and the intersection is a line, so Q_1(r,1) = w q^6. Every other row-r cell has A-part in V_A minus span{q^r,q^6}, i.e. on q^{r'}. A-part at (r,2) or (r,3) lies on the line orthogonal to q^r and e_c (support A minus {c}), which is not parallel to the full-support q^{r'}; so those are A-free. Row-r A-content is |q^6><q^6| + |q^{r'}><q^{r'}|, so total q^{r'}-mass 1 sits on W-cells. Slot count in row r: 18 A-slots; squares 2..5 need 12 (each has q_s^r orthogonal to V_A by C2 at (r,0), so A-mass 3 in row r); square 1 uses 2 at (r,1) and 3 at each q^{r'}-carrying cell; so at most one such cell, which carries mass 1 and equals w' q^{r'}. A-freeness of (r',1): its A-part is orthogonal to e_1 and q^{r'}, hence on q^6, and column orthogonality with w q^6 kills it. QED

## L2 (column 0 of squares 2..5)
For s >= 2: q_s^1 = phase e_{p_s}, q_s^7 = phase e_{t_s}, with p, t bijections {2,3,4,5} -> W and p_s != t_s; q_s^2, q_s^3 have no coordinates 0,6,7; q_s^4, q_s^5 no 0,4,5; q_s^6 no 0,2,3. For each s there are rows a_s != b_s in {2,3,4,5} with q_s^{a_s} = phase e_2, q_s^{b_s} = phase e_3, and s -> a_s, s -> b_s are bijections.
Proof. C2 at (i,0) against square 1's supports; four disjoint nonempty supports in the four-set W at rows 1, 7; column-0 orthonormality. Coordinate 2 of square s >= 2 has column-0 mass 1 and can only occur at rows 2..5 (rows 1,7: W-vectors; row 6: square 1 holds coordinate 2); each of these four rows admits at most one square; so each square has it at exactly one row with full mass, i.e. a pure vector. Same for 3. QED

## O1 (the old column-1 partial assignment has no full column-0 extension)
Let OW be the assignment of `B3-PURE-CORNER-PARTIAL-CANDIDATE-v1.md` section 4 (rows 0 and 1 of all squares; column 0 rows 0,1,6,7), with square 1 completed in column 0 by the template (q^2,q^3 of support {6,7}; q^4,q^5 of support {4,5}; any phases and amplitudes). Then no choice of q_s^2,...,q_s^5 (s = 2..5) satisfies column-0 orthonormality together with (T) for all pairs among the assigned cells.
Proof. In OW, Q_1(1,5) = e_6 and Q_1(1,6) = e_7; both have nonzero overlap with q^2 and q^3. By C3 at (1,5),(1,6), Q_2(1,5) = e_3 and Q_2(1,6) = e_5 are orthogonal to q_2^2, q_2^3. With q_2^0,q_2^1,q_2^6,q_2^7 = e_0,e_4,e_6,e_5, the vectors q_2^2..q_2^5 are an ONB of span{e_1,e_2,e_3,e_7}; rows 2,3 also lack coordinate 7 (C2 against q^2,q^3) and 3,5; hence q_2^2,q_2^3 is an ONB of span{e_1,e_2} and q_2^4,q_2^5 is an ONB of span{e_3,e_7}. For square 3 (q_3^0,q_3^1,q_3^6,q_3^7 = e_0,e_5,e_1,e_4), q_3^2..q_3^5 is an ONB of span{e_2,e_3,e_6,e_7}; rows 2,3 lack 6,7, so q_3^4,q_3^5 is an ONB of span{e_6,e_7}. Coordinate 7 has mass 1 over rows 4,5 in both squares 2 and 3, and C2 allows each row to only one of them; so there is rho in {4,5} with q_2^rho = phase e_7 and q_3^rho' = phase e_7 at the other row rho', whence q_3^rho = phase e_6. Now Q_2(1,1) = e_7 and Q_3(1,1) = e_6 both have nonzero overlap with their own rho-axis, contradicting (T) at the pair (1,1),(rho,0). QED

O1 says the obstruction is caused by the dense square-1 entries e_6, e_7 (each overlapping two own axes) in row r; any extension must be built differently.
