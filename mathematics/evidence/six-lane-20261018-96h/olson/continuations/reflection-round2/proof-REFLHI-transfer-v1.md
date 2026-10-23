# From RES-HI exclusions to REFL for initial words with o_F > p: the (g, b)-box transfer (candidate v1)

Owner OlsonReflectionSuccessor.  Written after host clock 2026-10-19T06:20:28-0700.  Status: CANDIDATE_UNVERIFIED (written
only; no computation).  Separate from the v5 delta-review set.  Uses: proof-REFLHI-arcs-v5.md
(4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c) + erratum-1 (512e1d9e...3331) + erratum-2 (b4451461...8820),
and proof-REFLHI-arcs-v5-addendum-SEGk-v2.md (b6d526829c9065eeefe75e8cbf7c12c31c88950f9de8788729a55144810a70d5), all candidates;
the parent-accepted RED (REFL/proof-RED-r2.md c4e7697f...d3d7 with K0star-r2 6681676e...96e1), (SMALLK), and, for clause (g)
only, the accepted B = 0 results (R16/olson-cj-cjx-parent-verdict-v1.md 5cfd6a4f...145f6d with
R16/olson-edge-parent-verdict-v1.md).  REFL/, R16/ as in v5.

## 1. Invariants of the RED process

Let w0 be an avoider of length 4p - 2 whose rotation letters lie in one pair, violating REFL(p).  The proof of Theorem RED
(RED-r2 L136-164) normalises x = 1 and A >= B and applies P1 (FUS), P2 (PM0), P3 (TR-fill), P4 (M0') until none applies; its
terminal state w_T is an avoider in RES_<(p) with kappa_T >= 2 (exits with g = 0 are contradictory there).  Write
D := A - B and g(w) := kappa(w) - B(w) (this g is MXG's kappa - B, not the number of empty runs).
**Lemma INV.**  Along the process D is constant, B and kappa never increase, and g never increases.  Hence
   D_T = D_0,  B_T <= B_0,  1 <= g_T <= g_0,  R_T = D_0 + 2 B_T,  k_T = 2p - D_0 + 2 g_T,  kappa_T = g_T + B_T >= 2,
and R_T >= p (v5 Fact 2.2 for the all-odd avoider w_T).
Proof.  P1 and P2 do not touch rotations; P3 moves one rho_1 rho_-1 pair between runs; P4 deletes one rho_1 and one rho_-1
(RED-r2 L140-147).  So A - B is constant and B changes only under P4, by -1.  kappa changes only through a new same-letter
pair: P4 inserts sigma_y sigma_y (kappa - 1, together with B - 1), and an odd-odd fusion (a double FUS of P1 with both outer
blocks odd, K0star-r2 L95-97, or the neighbour fusion of P4 when both neighbours are odd, fewodd-r5 Sec. 3 m5) lowers kappa
by 1 without changing B; single FUS, PM0 and the other fusions keep H (floor identities of K0star-r2 L95-97, L107-114).  So
g changes by 0 or -1 at each move.  At the terminal, B_T < kappa_T (RES_<), so g_T >= 1; all blocks are odd, so
R_T = 2p - k_T + 2 kappa_T (K0star-r2 (0.1)), i.e. k_T = 2p - (D_0 + 2B_T) + 2(g_T + B_T).  []
Remark.  For the initial word, (0.1) gives D_0 + 2B_0 = R_0 = 2p - o_F(w0) + 2 kappa_0, and the Claim MON of (FEW),
k_T <= o_F(w0), is the special case g_T <= g_0 of k_T = 2p - D_0 + 2g_T.

## 2. Theorem TRANSFER

For integers g, b put  kappa(g, b) := g + b,  R(b) := D_0 + 2b,  k(g) := 2p - D_0 + 2g,  Delta := p + kappa - 1 - R.
Call the cell (g, b) EXCLUDED if one of the following holds (each clause names the result that leaves no avoider in
RES_<(p) with these k, kappa, R and B = b):
 (a) k <= p  [(SMALLK)];
 (b) k >= 2p + 1 and k >= 3 kappa + 3  [v5 Theorem K2P+];
 (c) k >= 4 kappa + 5 and k >= p + floor(R/2) + 1  [SEG-k addendum];
 (d) R = p, kappa >= (p + 1)/4 and p >= 11  [v5 Sec. 6 closing statement];
 (e) R < p  [v5 Fact 2.2];
 (f) b = 0, R >= 4 kappa - 4, and Delta <= 1 or p >= kappa + 5 Delta - 5  [accepted CJ'''' Corollary 2 with EDGE].
**Theorem TRANSFER.**  Let p >= 5 be prime and w0 an avoider of length 4p - 2 over D_(2p) with rotation letters in one pair
{rho_x, rho_-x}, x != 0; normalise so that A_0 >= B_0, and put D_0 = A_0 - B_0, kappa_0 = kappa(w0) (on its maximal constant
blocks, even ones included), g_0 = kappa_0 - B_0.  If every cell (g, b) with 1 <= g <= g_0, 0 <= b <= B_0 and g + b >= 2 is
EXCLUDED, then every maximal cyclic reflection run of w0 is constant.
Proof.  Otherwise Lemma INV gives a terminal avoider w_T in RES_<(p) with parameters k(g_T), kappa(g_T, B_T), R(B_T), B_T for
a cell (g_T, B_T) of the box with g_T + B_T >= 2; the clause that excludes this cell excludes w_T.  []
All clauses except (f) are CANDIDATE results of this round; (a), (e) and (f) rest on parent-accepted results.

## 3. Corollaries (explicit parameter forms)

**Corollary T1 (balanced rotations).**  If |A_0 - B_0| <= 1 and o_F(w0) >= 3 kappa_0 + 3, then w0 has every maximal cyclic
reflection run constant.
Proof.  D_0 <= 1.  For every cell: k = 2p - D_0 + 2g >= 2p + 1 (g >= 1), and k >= 3 kappa + 3 iff g + 3b <= 2p - D_0 - 3,
whose left side is at most g_0 + 3B_0 = kappa_0 + 2B_0 = kappa_0 + R_0 - D_0; and kappa_0 + R_0 <= 2p - 3 iff
o_F(w0) >= 3 kappa_0 + 3 (R_0 = 2p - o_F + 2 kappa_0).  Clause (b).  []
Non-vacuity: a terminal needs R_T = D_0 + 2B_T >= p, so B_0 >= (p - 1)/2 and kappa_0 >= (p + 1)/2; with o_F >= 3 kappa_0 + 3 these
initial words have o_F > p (outside (FEW)) and B_0 >= 2 (outside REFL-B0).
**Corollary T2 (SEG-k transfer).**  If o_F(w0) >= 4 kappa_0 + 5 and A_0 + floor((A_0 - B_0)/2) <= p + 1, then w0 has every
maximal cyclic reflection run constant.
Proof.  Clause (c) for every cell: k >= 4 kappa + 5 iff 2g + 4b <= 2p - D_0 - 5, and the maximum 2g_0 + 4B_0 = 2 kappa_0 + R_0 - D_0
satisfies it iff 2 kappa_0 + R_0 <= 2p - 5 iff o_F >= 4 kappa_0 + 5.  k >= p + floor(R/2) + 1 iff 2g - b >= D_0 + floor(D_0/2) - p + 1,
whose minimum over the box (g = 1, b = B_0) gives B_0 + D_0 + floor(D_0/2) <= p + 1, i.e. A_0 + floor(D_0/2) <= p + 1.  []
**Corollary T3 (mixed).**  If o_F(w0) >= 3 kappa_0 + 3 and D_0 <= 2 g + ... : more generally, a cell (g, b) with 2g >= D_0 + 1 is
covered by (b) under o_F >= 3 kappa_0 + 3, and a cell with 2g <= D_0 - p by (a); so if o_F(w0) >= 3 kappa_0 + 3 the only cells
to check are those with D_0 - p < 2g <= D_0, i.e. the box is reduced to g in ((D_0 - p)/2, D_0/2].  In particular, if
o_F(w0) >= 3 kappa_0 + 3 and g_0 <= D_0/2 ... (no further claim; the reduced box must be covered by (c)-(f)).

## 4. What remains (precise)

For an initial avoider w0 with o_F > p, REFL is now reduced (candidate) to excluding the terminal cells of its box that
satisfy none of (a)-(f).  The uncovered cells are those of v5 Sec. 8 / SEG-k "Remaining": kappa < (p + 1)/4 (the arc-method
limit; for b = 0 partly (f)), the band (p - 5)/2 < kappa < (p + 1)/2 with R > p and k <= 2p, and k >= 2p + 1 with
k <= 3 kappa + 2.  No finite computation is used or claimed.
