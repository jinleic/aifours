# PURE1 completion: working notes v2 (twin-model reduction; search state)

Written at 2026-10-19T22:00:56-0700. Supplements WORKING-NOTES-v1.md (SHA256 5306f1861bdf58378a925ce31acadf7c26b3ede2e3c243e44e767b7170e4a9f2). Written mathematics only.

## R1 (twin model reduction, proved)
Fix explicit square-1 axes q^0 = e_0, q^1 = (e_1+e_2-e_3)/sqrt3, q^2 = (e_6+e_7)/sqrt2, q^3 = (e_6-e_7)/sqrt2, q^4 = (e_4+e_5)/sqrt2, q^5 = (e_4-e_5)/sqrt2, q^6 = (e_2+e_3)/sqrt2, q^7 = (2e_1-e_2+e_3)/sqrt6 (orthonormal; supports exactly as in the template, S_0={0}, S_1=S_7={1,2,3}, S_2=S_3={6,7}, S_4=S_5={4,5}, S_6={2,3}). Suppose on the assigned cell set Z (rows 0,1,7 and column 0) square 1 has Q_1(0,c) = e_c, Q_1(i,0) = q^i and Q_1(z) = q^{M(z)} for the other z in Z, and squares s=2..5 have Q_s(z) = e_{L_s(z)} with L_s(0,c) = c, and write lambda_s(k) := L_s(k,0). Then every direct equation among cells of Z (row ONB, column orthonormality on Z, and (T) for all pairs of Z) holds iff:
- (a) rows 1 and 7 of M and of each L_s are permutations; column 0 of each L_s is a permutation fixing 0;
- (b) for c >= 1: c not in S_{M(1,c)} and not in S_{M(7,c)}; M(1,c) != M(7,c); L_s(1,c), L_s(7,c), c pairwise distinct;
- (c) for k = 1..7 and s >= 2: lambda_s(k) not in S_k, and lambda_2(k),...,lambda_5(k) pairwise distinct;
- (d) at each z in Z with row in {1,7} and column >= 1: the coordinates L_2(z),...,L_5(z) are pairwise distinct and avoid S_{M(z)}; the own indices lambda_s^{-1}(L_s(z)) are pairwise distinct and differ from M(z);
- (e) for z = (1,c), z' = (7,c'), c != c' both >= 1: at most one of [M(z) = M(z')], [L_s(z) = L_s(z')] (s=2..5) holds.
Proof sketch (complete case list): all inner products are among orthonormal-basis members of the two ONBs {e_d}, {q^k}; <q^m,q^n> = delta, <q^m,e_d> != 0 iff d in S_m. Pairs sharing a row or column need only within-square orthogonality, which is (a),(b) and the column-0 permutation. Non-collinear pairs: ((0,d),(k,0)) gives (c); ((0,d),(i,c)) and ((k,0),(i,c)) give (d) (own index 0 coincides with coordinate 0, own index i of row i is absent by (a)); ((1,c),(7,c')) gives (e). QED
Every square-1 cell in the model is in V_A, V_B = span{e_6,e_7}, V_C = span{e_4,e_5} or span{e_0}; the pure-A corner is M(r,1) = 6 and then (L1) M(r,j) = r'.

## Search state (no claim)
Attempts with p = (4,5,6,7), t = (6,7,4,5) and two column-0 fillings, and with p = (4,5,6,7), t = (5,4,7,6) and filling
 sq2: 4,2,3,6,7,1,5; sq3: 5,1,2,3,6,7,4; sq4: 6,4,1,2,3,5,7; sq5: 7,3,5,1,2,4,6 (rows 1..7),
j = 4, failed at row 1 for the M-placements tried (own-index collisions at cells 1, 2/3, or 6). Search continues.
