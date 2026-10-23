# From RES-HI exclusions to REFL for initial words with o_F > p: the (g, b)-box transfer (candidate v2)

Owner OlsonReflectionSuccessor.  Written after host clock 2026-10-19T06:21:23-0700.  Status: CANDIDATE_UNVERIFIED (written
only; no computation).  Separate from the v5 delta-review set.  Supersedes the unsent v1 (874a3911...6e28, kept unchanged;
its Corollary T3 was left unfinished).
Uses (candidates of this round): proof-REFLHI-arcs-v5.md (4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c)
with erratum-1 (512e1d9e...3331) and erratum-2 (b4451461...8820); proof-REFLHI-arcs-v5-addendum-SEGk-v2.md
(b6d526829c9065eeefe75e8cbf7c12c31c88950f9de8788729a55144810a70d5).  Parent-accepted: Theorem RED and its proof
(REFL/proof-RED-r2.md c4e7697f...d3d7) with K0star-r2 (6681676e...96e1), (SMALLK), Claim MON of (FEW) (fewodd-r5 4615dcb9...5363),
and, for clause (f) only, R16/olson-cj-cjx-parent-verdict-v1.md (5cfd6a4f...145f6d) with R16/olson-edge-parent-verdict-v1.md.
REFL/ and R16/ as in v5.

## 1. Invariants of the RED process

Let w0 be an avoider of length 4p - 2, rotation letters in one pair, violating REFL(p).  The proof of Theorem RED
(RED-r2 L136-164) normalises x = 1 and A >= B and applies P1 (FUS), P2 (PM0), P3 (TR-fill), P4 (M0') until none applies; its
terminal state w_T is an avoider in RES_<(p) with kappa_T >= 2.  Write D := A - B and g(w) := kappa(w) - B(w).
**Lemma INV.**  Along the process D is constant and B, kappa and g never increase.  Hence
   D_T = D_0,  B_T <= B_0,  1 <= g_T <= g_0,  R_T = D_0 + 2 B_T >= p,  k_T = 2p - D_0 + 2 g_T,  kappa_T = g_T + B_T >= 2.
Proof.  P1, P2 do not touch rotations; P3 moves one rho_1 rho_-1 pair; P4 deletes one rho_1 and one rho_-1 (RED-r2 L140-147).
So D is constant, and B changes only under P4, by -1.  kappa changes only when a same-letter pair is created: P4 inserts
sigma_y sigma_y (kappa - 1, with B - 1), and an odd-odd fusion (double FUS of P1 with both outer blocks odd, K0star-r2 L95-97;
the neighbour fusion of P4 when both neighbours are odd, fewodd-r5 Sec. 3) lowers kappa by 1 and keeps B.  Single FUS, PM0 and
fusions involving an even block keep H (K0star-r2 L95-97, L107-114).  So each move changes g by 0 or -1.  At the terminal,
B_T < kappa_T (RES_<), so g_T >= 1; all blocks are odd, so R_T = 2p - k_T + 2 kappa_T (K0star-r2 (0.1)), which with
R_T = A_T + B_T = D_0 + 2 B_T and kappa_T = g_T + B_T gives k_T; R_T >= p is v5 Fact 2.2 for the all-odd avoider w_T.  []
Remark.  (0.1) for w0 gives R_0 = D_0 + 2 B_0 = 2p - o_F(w0) + 2 kappa_0; MON (k_T <= o_F(w0)) is g_T <= g_0 in this form.

## 2. Theorem TRANSFER

For integers g, b put kappa := g + b, R := D_0 + 2b, k := 2p - D_0 + 2g, Delta := p + kappa - 1 - R.  The cell (g, b) is
EXCLUDED if one of the following holds; each names the result showing that RES_<(p) has no avoider with B = b and these
k, kappa, R:
 (a) k <= p  [(SMALLK), accepted];
 (b) k >= 2p + 1 and k >= 3 kappa + 3  [v5 Theorem K2P+];
 (c) k >= 4 kappa + 5 and k >= p + floor(R/2) + 1  [SEG-k addendum];
 (d) R = p, kappa >= (p + 1)/4 and p >= 11  [v5 Sec. 6 closing statement];
 (e) R < p  [v5 Fact 2.2];
 (f) b = 0, R >= 4 kappa - 4, and (Delta <= 1 or p >= kappa + 5 Delta - 5)  [accepted CJ'''' Corollary 2 with EDGE].
**Theorem TRANSFER.**  Let p >= 5 be prime and w0 an avoider of length 4p - 2 over D_(2p), rotation letters in one pair
{rho_x, rho_-x}, x != 0, normalised so that A_0 >= B_0; D_0 := A_0 - B_0, kappa_0 := kappa(w0) on its maximal constant blocks
(even ones included), g_0 := kappa_0 - B_0.  If every cell (g, b) with 1 <= g <= g_0, 0 <= b <= B_0, g + b >= 2 is EXCLUDED,
then every maximal cyclic reflection run of w0 is constant.
Proof.  Otherwise Lemma INV gives a terminal avoider w_T in RES_<(p) whose (k, kappa, R, B) are those of the cell
(g_T, B_T), which lies in the box and has g_T + B_T >= 2; the excluding clause contradicts the existence of w_T.  []

## 3. Corollaries

**Corollary T1 (balanced rotations).**  If |A_0 - B_0| <= 1 and o_F(w0) >= 3 kappa_0 + 3, then every maximal cyclic reflection
run of w0 is constant.
Proof.  D_0 <= 1, so k = 2p - D_0 + 2g >= 2p + 1 for g >= 1.  k >= 3 kappa + 3 iff g + 3b <= 2p - D_0 - 3; over the box the
left side is at most g_0 + 3 B_0 = kappa_0 + 2 B_0 = kappa_0 + R_0 - D_0, and kappa_0 + R_0 <= 2p - 3 iff o_F(w0) >= 3 kappa_0 + 3.
Clause (b) excludes every cell.  []
(When no cell has R >= p, i.e. D_0 + 2B_0 < p, the conclusion already follows from (e); a nontrivial instance needs
B_0 >= (p - 1)/2 and kappa_0 >= (p + 1)/2, so o_F(w0) > p (outside (FEW)) and B_0 >= 2 (outside REFL-B0).)
**Corollary T2 (SEG-k transfer).**  If o_F(w0) >= 4 kappa_0 + 5 and A_0 + floor((A_0 - B_0)/2) <= p + 1, then every maximal cyclic
reflection run of w0 is constant.
Proof.  k >= 4 kappa + 5 iff 2g + 4b <= 2p - D_0 - 5; the box maximum 2 g_0 + 4 B_0 = 2 kappa_0 + R_0 - D_0 satisfies it iff
2 kappa_0 + R_0 <= 2p - 5 iff o_F >= 4 kappa_0 + 5.  k >= p + floor(R/2) + 1 iff 2g - b >= D_0 + floor(D_0/2) - p + 1; the box
minimum of 2g - b (g = 1, b = B_0) satisfies it iff B_0 + D_0 + floor(D_0/2) <= p + 1, i.e. A_0 + floor(D_0/2) <= p + 1.
Clause (c) excludes every cell.  []
**Corollary T3 (box reduction).**  If o_F(w0) >= 3 kappa_0 + 3, then every cell with 2g >= D_0 + 1 is excluded by (b) and every
cell with 2g <= D_0 - p by (a); so only the cells with D_0 - p < 2g <= D_0 remain to be checked against (c)-(f).
Proof.  As in T1, g + 3b <= g_0 + 3B_0 <= 2p - D_0 - 3 on the whole box; (b) needs in addition k >= 2p + 1, i.e. 2g >= D_0 + 1.
(a) is k <= p, i.e. 2g <= D_0 - p.  []

## 4. What remains

For an initial avoider w0 with o_F > p, REFL is reduced (candidate) to excluding the cells of its box that satisfy none of
(a)-(f).  These lie in the uncovered regions recorded in v5 Sec. 8 and the SEG-k addendum: kappa < (p + 1)/4 (arc-method
limit; for b = 0 partly clause (f)), the band (p - 5)/2 < kappa < (p + 1)/2 with R > p and k <= 2p, and k >= 2p + 1 with
k <= 3 kappa + 2.  No finite computation is used or claimed.
