# Shor completion: the 48-head branch at order 2640

Owner **MathShor-2**, math-5. Native clock of the exact check: **Wed Oct 28 20:20:02 PDT 2026**.
**WRITTEN conditional branch obstruction with exact finite residue checks; no order-2640 or all-order no-go, peer/formal/cross-family verification or novelty claim.**

## 1. Statement

For a hypothetical finite UD factor-complete extension of the literal Shor code with actual pure-a order2640, let its same-code actual b-run border factors P,Q tile `Z_2640` directly and contain the old anchors `A={0,3,8,11}` and `Y={0,1,7,13,14}`. These are the classical actual-border theorem and its independently written reconstruction. **The cardinality branch `|P|=48, |Q|=55` is impossible.** No other order-2640 branch is decided here.

## 2. Four fully forced head classes

Since `2640=2^4*3*5*11` and |Q|=55 is odd, each of `Phi_2,Phi_4,Phi_8,Phi_16` divides the P-mask. Their product is `1+X+...+X^15`, so P has exactly3 elements in each class modulo16.

The old-anchor gcd screen has exactly3 candidates in EACH of the following classes, hence all twelve residues are forced:

    mod16=1: {33,913,1793}
    mod16=2: {418,1298,2178}
    mod16=5: {693,1573,2453}
    mod16=9: {473,1353,2233}.

Together with old heads0,3,8 these forced residues supply the following actual P-difference gcd classes:

    gcd(1793-8,2640)=15,    gcd(1353-3,2640)=30,
    gcd(2178-1793,2640)=55, gcd(2178-0,2640)=66,
    gcd(2453-1793,2640)=660, gcd(1793-473,2640)=1320.

By the classical Sands gcd-difference criterion, independently reconstructed in the earlier order-1320 packet, Q must avoid all six classes as well as the old head classes `{3,5,8,11}`.

## 3. A five-candidate tail contradiction

Since |Q|=55 and P is coprime to11, Q is uniform modulo11 with exactly5 tails in each class. Under the old-anchor screen and the ten forbidden gcd classes from §2, the ENTIRE screened mod11 class7 is exactly

    {7,337,997,1657,2317}.

All five would have to be Q-elements. But `gcd(997-337,2640)=660`, one of the classes forced in P. Contradiction. This uses only the actual P/Q factorization, not any separate array or all-order claim.

## 4. Check and limits

`frontier-20261028-2640-p48-screen-check.py`, SHA256 `a9b9bca67bbcba274cc4dba20a35af274b1f74c3424698e61ab63030f720e4ef` (18 LF, 972 bytes), enumerates the screened head/tail residues and checks all six forced gcd classes, the exact five-tail list and the final gcd660 collision with exact integers. Its actual output was PASS. This computation is not a proof assistant, peer review or independent-family review. The class sizes for other hypothetical P-cardinalities and the original finite-completion problem remain OPEN.

The prospective `n>=2640` candidate floor depends on separate unreviewed order660/1320/1980/2310 packets and is not a premise here.

**END OF ORDER-2640 P48 BORDER OBSTRUCTION.**
