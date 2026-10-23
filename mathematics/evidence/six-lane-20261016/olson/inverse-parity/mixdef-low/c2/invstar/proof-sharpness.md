# A rigid-rotation non-RGR avoider of length 4p-3 (all primes p >= 5)

Owner OlsonParity2.  Written after host clock 2026-10-17T19:33:30-07:00.  Status: [W], UNREVIEWED.  No
literature/novelty claim.  This is sharpness for the length in INV*b-rig(p), not a counterexample to INV*(p),
whose target length is 4p-2, or to ordered Olson, whose target length is 4p-1.

**Proposition SH.**  For every prime p >= 5 and v in Z_p, the word
    w_p = sigma_(v-2) rho_1^(2p-3) sigma_v^(2p-1)
has no identity 2p-subword.  Its rotations are rigid (all rho_1), but its maximal cyclic reflection run
sigma_v^(2p-1) sigma_(v-2) is not constant.  Its length is 4p-3.
Proof.  Select a 2p-subword; it can be an identity only with an even number of reflections.
If the first reflection sigma_(v-2) is not selected, the number m of selected rotations is even,
2 <= m <= 2p-4 (the constant reflection block has at most 2p-2 selected reflections of even parity;
the rotation run has length 2p-3).  The product is rho_m, never 1 (p is odd; among 0..2p only 0, p, 2p
are 0 mod p and none is an even number in this range).
If sigma_(v-2) is selected, the selected count c in the last block is odd, m = 2p-1-c is even, and
0 <= m <= 2p-4.  The product is sigma_(v-2) rho_1^m sigma_v = rho_(-2-m), which is 1 iff m = -2 mod p.
The p-1 even numbers 0, 2, ..., 2p-4 have distinct residues mod p and omit precisely the residue of
2p-2 = -2 mod p.  So the product is not 1 in this case either.  []

Three natural one-letter extensions at length 4p-2 all have explicit identity 2p-subwords:
1. Add a rho_1 to the rotation run: sigma_(v-2) rho_1^(2p-2) sigma_v has product rho_(-2-(2p-2)) = 1.
2. Add a sigma_v to the long block: its 2p letters already multiply to 1.
3. Add a sigma_(v-2) to the short block: take both letters there and 2p-2 letters of the long block;
   both selected constant blocks have even length, so their ordered product is 1.
Thus these extensions do not answer INV*b-rig(p); SH shows why a length reduction by one is impossible.
