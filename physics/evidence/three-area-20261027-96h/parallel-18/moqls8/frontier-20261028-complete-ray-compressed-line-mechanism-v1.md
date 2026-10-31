# Exact compressed-line mechanism for a member with complete rays

**WRITTEN AUTHOR CANDIDATE; independent review pending.** This packet changes representation from chosen-row support graphs to the actual noncomplete part of one member. The main line/ONB identities below hold for any ordinary complex four-MOQLS(8), without assuming the other members are classical, any specific complete-ray counts, a source catalogue or a numerical model. The final coverage corollaries are explicitly conditional on the separate unreviewed all-cell complete-ray-cover theorem; they are not used to prove the main mechanism.

## Ordinary definitions

Each ordinary QLS is an 8×8 array of unit vectors in its own C^8 with every row and column an ONB. Four QLS Q,R,S,T are mutually orthogonal if, for every pair M,N, the 64 same-cell vectors M_x⊗N_x form an ONB of C^8⊗C^8. A *complete ray* of one member occurs once in every row and column. Such a ray is perpendicular to every other entry ray of that member, because every row contains it. Complete rays within one member therefore form an orthonormal ray set. Individual phases are irrelevant.

Let Q have c complete rays. Let D be their orthogonal complement, of dimension d=8−c, and Ω the cells where Q is not one of its complete rays. Then Ω has exactly d cells in every row and every column, every Q_x for x∈Ω lies in D, and those d rays form an ONB of D on each board row and column. There are 8d points in Ω. A chosen actual Q row may be used to give D a coordinate basis, but no selected instance or particular row is assumed.

## Complete rays from other members give actual D-bases

Let τ be a complete ray of R. For all eight occurrences of τ, the corresponding Q rays are pairwise orthogonal by the actual Q⊗R ONB and hence form an ONB of C^8. Each complete Q ray ρ appears with τ in exactly one cell: a same-cell product Q_x⊗R_x has nonzero overlap with ρ⊗τ only when both complete rays occur, in which case that squared overlap is 1; the full product ONB gives total squared overlap 1. Thus τ meets c distinct Q-complete cells and d cells in Ω. The d actual Q rays at those Ω cells are an ONB of D.

The same conclusion holds for every complete ray of S or T. Define *external lines* on Ω by these d-cell sets. Distinct external lines in the same member are disjoint. External lines from different members meet in at most one Ω point because the original complete rays meet in exactly one board cell. Board-row lines, board-column lines and external lines pairwise meet in at most one point whenever they are distinct. In particular these are actual orthonormal Q-vector lines, not just a finite support filter or an abstract replacement for the original arrays.

Let C=c_Q+c_R+c_S+c_T be the total number of complete rays. There are 8 row lines, 8 column lines and C−c external lines. For x∈Ω let k_x be the number of the other three members whose entry at x is complete, so x is on exactly 2+k_x of these lines. With P_x=|Q_x><Q_x| acting on D, actual ONB resolutions yield

`Σ_(x∈Ω) P_x = 8 I_D`,

`Σ_(x∈Ω) k_x P_x = (C−c) I_D`,

and hence

`Σ_(x∈Ω) (k_x−1) P_x = (C−c−8) I_D`.  (∗)

The second identity sums all external-line ONB projectors; no vector Gram or operator has been numerically sampled.

## Conditional covering and exact saturation

Assume the separately review-pending theorem that every board cell of the four-family has a complete entry in at least one member. It is proved with all inputs embedded in `frontier-20261028-four-family-complete-ray-cover12-self-contained-v1.md`, SHA256 b2064ef68320e3526056650f83948b5ca5b717684fb25bbf303906084520ec52. It is **not** adopted or proved by this filename reference. Then k_x≥1 for every x∈Ω, because Q_x is not complete. Equation (∗) is a sum of positive semidefinite rank-one operators and gives C−c≥8 whenever d>0.

If C−c=8, equality forces every k_x=1, not merely an average-one count: every nonzero (k_x−1)P_x would make the positive semidefinite sum nonzero. The external lines are therefore a disjoint partition of Ω into exactly eight actual D-ONBs. Together with the row and column partitions, Ω is a three-parallel-class incidence object with eight lines of size d per class and 8d points; any two lines from different classes meet at most once. When d<8 this is not a full Latin square or a d×d board, and no unsupported classification or classicality theorem is applied to it. If C−c=9, the overlap-excess weighted actual Q rays instead satisfy `Σ (k_x−1)P_x=I_D`; neither integral combinatorial coverage nor this resolution alone gives collinearity.

For example, the candidate all-nonclassical C=12 case with one c=4 member has d=4 and C−c=8. Its noncomplete part would be an **actual 32-point/three-parallel-class D=4 ONB design**, with external lines drawn from the complete rays of the other three original members. This is a precise remaining bridge: one must reconstruct those other members and all their pair-product ONBs, or exclude the resulting D-vector design together with its original complete-ray incidences. A proof only about a single compressed array, or an abstract incidence table without actual complex vectors and all three other arrays, would not settle the original four-family question.

## Current barrier

No contradiction for these 32-point designs or their nonsaturated variants is established here, and no fourth-mate construction is delivered. The operator identities quantify the missing coupling rather than silently assuming the compressed incidence object is a classical Latin square. This is not an independent review, parent adoption, configured-family/formal/human/executable or novelty certificate. The exact A10 GB15/18 and three literal UNKNOWNs, stronger A11, original q1/q2/q3/q4 and numerical M(8) questions remain unchanged and OPEN.
