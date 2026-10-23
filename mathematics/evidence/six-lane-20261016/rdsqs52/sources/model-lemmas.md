# Model lemmas for the RDSQS(52) lane (written proofs, unreviewed)

Restricted-model statements only; none concerns RDSQS(52) existence. No novelty claimed.

## Lemma R2-a (no resolution invariant under an involution fixing one point of Y∖{0})

Setting: SQS(v) (Y, B) on Y=Z_v... more generally any SQS(u) on a set Y with a point 0;
D = derived design at (0,0) of the doubled SQS(2u) on Y×F2 (blocks: 8 even-parity lifts
of each block of B, and {(x,0),(x,1),(y,0),(y,1)} for all pairs). Let S be the derived
STS(u−1) of (Y,B) at 0. Let t be an automorphism of (Y,B) fixing 0, of order 2, with
exactly one further fixed point z∈Y∖{0}; let t act on Y×F2 by (y,i)↦(t(y),i).
**Claim.** D has no resolution invariant under t (as a set of classes).

*Proof.* ω=(0,1) is fixed by t. Every class contains exactly one triple through ω, and
those triples are W_y={ω,(y,0),(y,1)}, y∈Y∖{0}. If the resolution is t-invariant, t maps
the class K_y containing W_y to the class containing W_{t(y)}; hence K_y is t-fixed iff
t(y)=y iff y=z. A t-fixed triple of D lies in a t-fixed class (its class C and t(C) both
contain it). S is t-invariant and t has exactly one fixed point z on Y∖{0}, so the
blocks of S through z are {z,a,t(a)} (the block through {a,t(a)} is t-invariant, hence
contains a fixed point, i.e. z). Their internal lifts {(z,0),(a,0),(t(a),0)} are t-fixed
triples of D, so all of them lie in the unique fixed class K_z. But K_z contains (z,0)
in W_z already. Contradiction (there is at least one such block since u−1≥3). ∎

For Y=Z26 and t: y↦−y, the fixed points are 0 and 13, so every R∋−1 is excluded.
This matches the 8 R2 batches with R∋−1 (all UNSAT, `code/runs/r2b1_*`). U(26) has
−1 as its only involution, so only R∈{1,⟨9⟩} remain in R2 with multiplier symmetry.

## Lemma F (fixed points of SQS automorphisms)

If g is an automorphism of an SQS(v), its fixed-point set F is closed under completing
triples to blocks, so |F|≤2 or (F, blocks inside F) is an SQS(|F|) (|F|≡2,4 mod 6), and
v≥2|F| for a proper subsystem. For v=52 an element of odd prime order p fixing a
point must fix f≡52 (mod p) points with f∈{1,2,4,8,10,14,16,20,22,26}: p=3 (f=1,4,10,16,22),
p=5 (f=2,22), p=7 (10), p=11 (8), p=13 (26), p=17 (1), p=19 (14); p=23 and p≥29
cannot occur in a point stabilizer. (Elementary; used only to choose search groups.)
