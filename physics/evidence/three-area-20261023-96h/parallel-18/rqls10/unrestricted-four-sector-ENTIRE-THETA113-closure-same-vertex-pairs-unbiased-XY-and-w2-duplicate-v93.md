# RQLS10 v93 — ENTIRE THETA(1,1,3) all-sparse topology has NO original MAX1 resolution

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 19:57:34 PDT 2026**. AUTHOR-WRITTEN CANDIDATE, not machine/kernel checked. Written two-projection/tensor/Pauli-commutator/row-column arguments only; no scientific Eval/interpreter/CAS/program/enumeration/solver/replay, approximate scout, chosen angle/state/control/probe or newGO.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption or verdict inheritance.

## 1. Domain and inputs

THETA(1,1,3) (v82): circuits X,Y of length three and a,b of length two; row-pair vertices v1,v2 (X/Y, doubled edge), w1 (X/a), w2 (a/b), w3 (b/Y). Routes X={v1,v2,w1}, Y={v1,v2,w3}, a={w1,w2}, b={w2,w3}. Original MAX1 means ordinary MAX100 plus ONE full TEN-class resolution; each class has four E4 cells forming an ONB of E4 in distinct rows and columns. Imported, with all quantifiers: v79 X/Y interior-isoclinic; v84 §6 exact pattern of 4 PX, 4 PY and 2 N classes, with N = {X+,X- at w1; Y+,Y- at w3}; v86 GLX/route avoidance and §4 same-label a/b parts: every PX a/b part is {a+,a-} at w2, {b+,b-} at w2 or {b+,b-} at w3, every PY a/b part is {a+,a-} at w1, {a+,a-} at w2 or {b+,b-} at w2, the four w3 b-cells lie only in PX classes and the four w1 a-cells only in PY classes. A length-two circuit has its two columns joining its two vertices in opposite directions, so every same-label opposite-orientation pair in one class lies at ONE vertex, in two different rows.

Coordinates (v84 §2, derived, not chosen): H4 = K1 tensor K2 with P_X = |x+><x+| tensor I, P_Y = |y+><y+| tensor I, 0<|<x+|y+>|^2=lambda<1. Every sparse S commutes with its two circuit projections. At v_k, S_vk = I tensor |u_k><u_k|; its rows carry {x+ tensor u_k, x- tensor u_k, y+ tensor u_k-perp, y- tensor u_k-perp} and the complementary row. MAX forces u_2 not in {u_1,u_1-perp}. v84's N-class argument gives S_w1 = span(x+ tensor z, x- tensor z-perp) and S_w3 = span(y+ tensor t, y- tensor t-perp) with t in {z,z-perp}; that is, 2S_w1-I = ±R_X tensor tau and 2S_w3-I = ±R_Y tensor tau with the SAME tau = |z><z|-|z-perp><z-perp|, R_C = 2P_C-I.

## 2. Lemma SV: every PX and PY pair is a same-vertex pair

Since r = 0 in v84, every X-cell at v1,v2 lies in a PX class. Circuit X is a three-cycle, so one X-column joins v1 and v2 directly; it carries X+ at its tail vertex and X- at its head vertex. Hence an X+ cell at the tail cannot pair with an X- cell at the head. Both tail X+ cells therefore pair with both tail X- cells, in opposite rows, and then both head X+ cells pair with both head X- cells. Every PX X-pair is {x+ tensor s, x- tensor s-perp} with s in {u_k,u_k-perp}, and the complement of its span in E4 is

    W(s) = span(x+ tensor s-perp, x- tensor s),     2 Pi_W(s) - I = -R_X tensor sigma_s,

with sigma_s = |s><s|-|s-perp><s-perp|. The same argument holds for Y; every PY class has complement span(y+ tensor s-perp, y- tensor s), with 2Pi-I = -R_Y tensor sigma_s. Each vertex v_k supplies exactly two PX classes, with complements W(u_k) and W(u_k-perp) = W(u_k)-perp, and two PY classes.

## 3. Lemma ONE-VERTEX: w3 b-pairs use one vertex, w1 a-pairs use one vertex

The four w3 b-cells form two opposite-row b-pairs. In each, one cell lies in S_w3 and the other in S_w3-perp, because the b-cells of one actual row lie on one side of S_w3. The two pair spans are span(P_b S_w3-perp,(I-P_b)S_w3) and span(P_b S_w3,(I-P_b)S_w3-perp), which are orthogonal complements. The PX complement of one is therefore the X-pair span of the other. Since x+ tensor s is the only X+ ray in span(x+ tensor s, x- tensor s-perp), both w3 b-pair classes are the two PX classes of ONE vertex v_i. Likewise both w1 a-pair classes are the two PY classes of ONE vertex v_j.

## 4. Lemma U: lambda = 1/2 and z is unbiased to u_i and u_j

W = W(s), s in {u_i,u_i-perp}, is spanned by one cell in S_w3 and one in S_w3-perp. Hence W is invariant under R_Y tensor tau. Write R_Y x+ = r11 x+ + r21 x- with r11 = 2lambda-1 and |r21|^2 = 4lambda(1-lambda) > 0. Then

    (R_Y tensor tau)(x+ tensor s-perp) = r11 x+ tensor tau s-perp + r21 x- tensor tau s-perp

lies in span(x+ tensor s-perp, x- tensor s). As r21 is nonzero, tau s-perp is proportional to s. Thus tau s-perp is not proportional to s-perp, so r11 = 0 and lambda = 1/2. Also tau maps s-perp to s exactly when |<z|s>|^2 = 1/2. The same argument at w1 for the PY complements of v_j gives |<z|u_j>|^2 = 1/2.

Fix the x- phase so that R_X = sigma_z tensor I and R_Y = sigma_x tensor I in the basis (x+,x-). On the Bloch sphere of K2, tau = n_z.sigma, and sigma_{u_k} = n_k.sigma with n_i and n_j orthogonal to n_z.

## 5. Lemma F: P_a and P_b are forced

On W = W(u_i), P_b has rank one and its range is the b+ line of that pair, which is one of the lines W cap S_w3 and W cap S_w3-perp. The same holds on W-perp. P_b cannot agree with S_w3 on both, or with I-S_w3 on both, because tr(P_b S_w3) = 1. Therefore, with commuting reflections s = 2S_w3-I and w = 2Pi_W-I,

    R_b = ± s w = ± (sigma_x sigma_z) tensor (tau sigma_{u_i}) = ± sigma_y tensor (m_i.sigma),    m_i = n_z x n_i.

The w1 argument gives R_a = ± sigma_y tensor (m_j.sigma), m_j = n_z x n_j. Both m_i,m_j are unit vectors orthogonal to n_z; m_i = ±m_j exactly when n_i = ±n_j.

## 6. Theorem: no original MAX1 resolution in ANY THETA(1,1,3) array

Case i = j. Then R_a = ±R_b, so P_b is P_a or I-P_a. At w2 the four a-cells and the four b-cells are the same four products of P_a,I-P_a with S_w2,I-S_w2. These are duplicated rays, contradicting MAX.

Case i different from j. Then n_1 is not ±n_2 because u_2 is not u_1 or u_1-perp, so m_1 is not ±m_2. The algebra generated by R_a = ±sigma_y tensor A and R_b = ±sigma_y tensor B, with A,B anticommuting with tau and not commuting with each other, contains I tensor tau and sigma_y tensor M for every Pauli direction M orthogonal to n_z. It is a copy of M2, and its commutant is

    span{I, sigma_x tensor tau, sigma_y tensor I, sigma_z tensor tau},

whose three nonidentity generators are pairwise anticommuting reflections. Since S_w2 commutes with P_a and P_b and has rank two, 2S_w2-I = alpha sigma_x tensor tau + beta sigma_y tensor I + gamma sigma_z tensor tau with alpha^2+beta^2+gamma^2=1.

The two PX classes at v_j are NOT w3 b-pair classes. Their a/b parts are a-pairs or b-pairs at w2, each spanned by one cell in S_w2 and one in S_w2-perp. Hence W(u_j) is S_w2-invariant, i.e. 2S_w2-I commutes with sigma_z tensor sigma_{u_j}. Direct Pauli algebra gives

    [sigma_z tensor sigma_{u_j}, sigma_x tensor tau] = 0,
    [sigma_z tensor sigma_{u_j}, sigma_y tensor I] = -2i sigma_x tensor sigma_{u_j},
    [sigma_z tensor sigma_{u_j}, sigma_z tensor tau] = 2i I tensor ((n_j x n_z).sigma),

where the first uses n_j orthogonal to n_z. The last two operators are linearly independent, so beta = gamma = 0. Therefore 2S_w2-I = ±sigma_x tensor tau = ±(2S_w3-I), and S_w2 is S_w3 or I-S_w3. Then the four b-cells at w2 are the four b-cells at w3, again duplicated rays. The PY classes at v_i give the symmetric conclusion S_w2 in {S_w1,I-S_w1}, duplicating the a-cells.

Both cases are contradictory. This holds for ALL cyclic orders, orientations, row labels, complex frames, angles, (p_a,q_a) splits and labelings. No resolution, candidate or numerical case was chosen or tested.

## 7. Scope and frontier

New paid result: the ENTIRE all-sparse THETA(1,1,3) topology has no original MAX1 resolution. Lemmas SV, ONE-VERTEX, U and F are proved within it. With v84's FIGURE-EIGHT closure, the remaining all-sparse four-sector topologies are BARBELL(2,1,2), THETA(1,2,2) and the five-cycle C5. Dense d in {2,3,4,5}, other sector placements, minimal-rank-3 and higher-rank families, complementH6, actual100 distinct rays and the SAME TEN-class resolution remain unpaid. All original irreducible10, 4+6 and 5+5 branches remain OPEN.

Imports: v79 repeated-pair isoclinicity; v82 topology list; v84 §2 vertex form, §6 4/4/2 pattern and N-class S operators; v86 GLX, route avoidance and §4 same-label parts; v80 plane bound/strict angles; elementary Pauli and two-projection algebra; the actual primary TEN-transversal/CLASSICAL-mate interface. No NR/classifier/Butson/Gaussian/code premise, measure genericity or chosen frame. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S93, retaining ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including the disclosed v29 parallel-intent minor, the v30 dangling-reference defect and the v34 capture retry. v84/v86's THETA(1,1,3) OPEN statements remain as historically paid and are prospectively superseded here, not edited.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
