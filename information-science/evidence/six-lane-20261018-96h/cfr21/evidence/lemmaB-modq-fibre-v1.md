# Lemma B (mod-q fibre principle for n = 3q) — text v1

Author ContinueCFR21; frozen 2026-10-19T00:02:21-0700. WORKER PROOF, unreviewed. Necessary conditions only; no CFR(6,21) decision.

Setting. n = 3q with gcd(3,q) = 1 (here q = 7). D a (Z_n,k;1)-DM (rows R, columns C, no normalisation).
alpha_i = D_i mod 3, beta_i = D_i mod q. CRT fact (Lemma 0): for i != j the map c -> (alpha_i - alpha_j,
beta_i - beta_j)(c) in Z_3 x Z_q is a bijection; hence every fibre {c : beta_i(c) - beta_j(c) = t} has exactly
3 columns, on which alpha_i - alpha_j takes the 3 distinct values of Z_3.

B1 (coordinates of column differences). For columns c != c', the vector Delta = D(c) - D(c') in Z_n^R has pairwise
distinct coordinates (else some D_i - D_j is not injective). Hence each residue class mod q contains at most 3
coordinates of Delta, and the coordinates in one class have pairwise distinct residues mod 3.

B2 (set property). If k >= 4, no two distinct columns have mod-q images that differ by a constant vector: otherwise
all k coordinates of Delta lie in one class mod q, contradicting B1 (k >= 4 > 3).
Consequently the mod-q column image is a set of n distinct points of Z_q^R / Z_q·1, and (q prime) its affine rank
is >= 2 (an affine line has only q < n points).

B3 (no four collinear rows mod q). Let Q be a set of rows such that every difference beta_x - beta_y (x,y in Q) is
of the form u_{xy}·L + s_{xy} for ONE function L : C -> Z_q and constants u_{xy} in Z_q^*, s_{xy} in Z_q
("Q collinear mod q"; for q prime: the row points of Q in the affine-rank coordinates lie on one line, i.e. the
mod-q image restricted to Q has affine rank 1). Then |Q| <= 3.
Proof. For x != y in Q the fibres of (x,y) are the level sets of L, so each level set T of L has exactly 3
columns, and for every pair x != y in Q, alpha_x - alpha_y restricted to T is a bijection T -> Z_3. Thus the
|Q| x 3 array (alpha_x(c))_{x in Q, c in T} is a (Z_3,|Q|;1) difference matrix with 3 columns. After subtracting one
row, the other rows are permutations of Z_3 with pairwise differences permutations, i.e. normalised mutually
orthogonal orthomorphisms of Z_3 plus the identity; the only normalised orthomorphism of Z_3 is x -> 2x, so
|Q| <= 3. ∎
In constant-character language (q prime): K_q restricted to any 4 rows has dimension <= 1; equivalently any 4 rows
have mod-q affine rank >= 2. For q = 7 this is the mod-7 companion of L3 (mod 3: no three collinear).

B4 (consequences for CFR(6,21), q = 7, k = 7). The mod-7 image is a set of 21 points; its affine rank is >= 2;
no 4 rows are collinear mod 7. In particular every construction in which four rows are F_7-affine functions of one
column function (e.g. the old 'three repeated linear blocks', and any common-slope CRT pattern with four collinear
row points) is excluded by hand, independently of the old computer exhaustion.

Scope: degenerate configurations only; the generic full-rank stratum is untouched. Priority: B2/B3 are elementary
CRT/pigeonhole facts; no novelty claim.
