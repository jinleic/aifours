# Exact CRT lifting experiment C21-CRT1

Recorded at 2026-10-17 19:18:03 PDT by InfoCFR27Lift; restricted experiment, not an unrestricted nonexistence method.

Let q be coprime to3 and n=3q. A beta matrix over Z_q with k rows and n columns has exactly three copies of each
row-pair difference. Normalise beta row0 to0 columnwise. Choose alpha over F3, alpha row0=0. For each row pair (i,j)
and beta residue d, let its three columns be a,b,c. The lift works iff delta_a,delta_b,delta_c (delta=alpha_i-alpha_j)
are distinct. In F3 this is equivalent to delta_a+delta_b+delta_c=0 and delta_a-delta_b!=0.
Fix alpha_i(column0)=0 by row translations, leaving (k-1)(n-1) variables (120 for k=7,n=21). All 147 sum equations are
homogeneous. If K spans their kernel, the remaining conditions are B K z !=0 coordinatewise.
Choose independent rows Q of BK and a right inverse R (Q R=I). Their values y=Qz can be arbitrary, and every possible
inequality image equals BK R y: directions in ker(Q) are killed by all rows of BK. Each y coordinate is itself an
inequality value and therefore is1 or2; uniform scaling fixes y0=1. Exhaustive binary DFS on y, checking each form
as soon as determined, is exact. An identically zero projected form proves no lift. A timed-out DFS is UNKNOWN.
Reconstruct alpha=K R y, and x=(3*inv(3 mod q)*beta + q*inv(q mod3)*alpha) mod3q. Every produced matrix is then checked
directly on all row pairs, independently of these equations.

Implementation: code/crt3_lift_c21v1.py. Calibration receipts under calib/crt3-v1/: reductions modulo7/11 of the pinned
Sage cyclic DMs of orders21/33 lift successfully (kernel dimensions7/6 after the gauge). Boundary q=1 gives a3-row
Z3 DM and rejects the4-row case. Three repeated linear field7 blocks are rejected (the zero-residue triples would
force a Z3,7;1 DM). A damaged beta multiplicity is rejected. These are solver controls, not target discoveries.

Restricted target pattern families (code/crt3_affine_sample_c21v1.py): columns(t,c), t=0,1,2 and c inF7,
beta_i(t,c)=a[t][i]*c+b[t][i]. Each a[t] is a permutation, so every row-pair difference is a permutation per block.
a[0]=id, b[0]=0; a[1],a[2] fix0,1; offsets fix rows0,1. Rotate three families:
(0) independent random offsets on rows2..6 in blocks1,2;
(1) b=u*(a^2-a)+v*(a^3-a), random u,v per block;
(2) same polynomial formula but a[t]=id in all blocks.
All are explicit restrictions; no assertion they cover general Z7,7;3 patterns or general cyclic DMs.
Seed and Python version are pinned; exact lift timeout2s per pattern. Rank/inequality histograms and first pattern
of every signature are retained; a candidate records beta, alpha-derived DM and SHA before stopping.
