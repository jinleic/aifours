# An actual Sun8 counterconfiguration descends, label by label, to a simple factor

**NEW WRITTEN COMPOSITION CANDIDATE, not reviewed/adopted/formally verified or novelty-cleared.** Native prewrite clock **Wed Oct 28 17:35:51 PDT 2026**. This strengthens the immediately preceding global P7 existence reduction to a simple composition factor of the SAME finite-core quotient with every private index divisibility retained. It composes an explicit `Sun_7(G)` hypothesis with the already parent-supported direct-P7 normal-section mechanism; it does not itself eliminate any simple group or solve Sun8.

## 1. Precise theorem

Let G be ANY group satisfying `Sun_7(G)`, and suppose there are EIGHT actual pairwise-disjoint LEFT cosets `g_i U_i` of finite-index subgroups whose original indices have pairwise gcd<=7. Write `[G:U_i]=7r_i` as justified below.

Let K be the intersection of the eight actual subgroup cores and let F=G/K. Then F has a finite NONABELIAN SIMPLE composition factor S carrying EIGHT actual pairwise-disjoint LEFT cosets of finite-index subgroups with corresponding indices

    [S:V_i]=7s_i,       s_i | r_i     for EVERY original label i,

where all s_i are positive and pairwise coprime. Thus the resulting simple factor and cosets depend on the same original configuration, with EACH private-index divisibility retained; no statement about the original ambient group having the size/order of S is implied. The simple group's eight cosets are a direct P7 configuration and hence an actual Sun8 counterconfiguration if they exist.

Consequently, conditional on the explicitly stated universal Sun7 import, a proof that NO finite nonabelian simple group carries a direct P7 configuration would prove Sun8 for EVERY group. This is an exact source-preserving reduction, not an assertion that this remaining exclusion is proved.

## 2. All-original seven labels and finite quotient

The complete elementary proof is in `frontier-20261028-global-p7-simple-reduction-v1.md`, SHA256 `a79167480dae75b5962d54a58c9d5fa4f74d96d42ea4d54e98ad531f4c8e1ca7`, Sections2–4; its full content is summarized and the used facts are recapitulated here.

Sun7 on every seven-subfamily forces at least THREE original n_i divisible by7, because the pair's gcd must equal7 under the <=7 counterconfiguration bound. Disjoint finite-index cosets always have noncoprime subgroup indices. If any n_j were seven-free, its gcd with each seven-label would have to contain a different prime among2,3,5: two different seven-labels have mutual gcd exactly7. There are therefore exactly three seven-labels, and every remaining n_j is divisible by30; at least two such indices share30, contradiction. All eight n_i are divisible by7, and their pairwise gcds equal7, so n_i=7r_i with pairwise-coprime r_i.

Each subgroup core is finite index and contained in its subgroup. Their finite intersection K is finite-index normal, lies in all U_i, and makes every original coset the full inverse image of its image in F=G/K. Thus the eight images remain disjoint actual F-cosets with EXACTLY the same indices 7r_i. F is finite and itself carries the labelled direct P7 family.

## 3. One actual normal step retains all labels

Suppose a finite group H carries eight ACTUAL P7 cosets with indices `7t_i`, the t_i pairwise coprime, and let `1<N<H` be normal. Let

    c_i=[N:N∩U_i],     d_i=[H/N:NU_i/N],     c_i d_i=7t_i.

At most one t_i is divisible by7; designate that label e or any e if none is. For the other seven, the single factor7 sits wholly in either c_i or d_i. Opposite placements for two regular labels would give both coprime quotient indices and coprime kernel indices, contradicting actual original disjointness by the two-coset diagonal-map fact first in H/N and then in the same N-fibre. So the seven regular placements are uniform.

If they are on the QUOTIENT side, every pair among all eight c_i is coprime, including the exceptional c_e, because one member of each pair is regular and seven-free and the private t's are pairwise coprime. Thus every quotient overlap would lift to an original overlap, so the eight actual quotient cosets are pairwise disjoint. The exceptional d_e must contain7, since otherwise it is coprime to a regular d_i and those quotient cosets must intersect. Every quotient index is `d_i=7t_i'` with `t_i'|t_i`; the eight new private t_i' remain pairwise coprime.

If the regular placements are on the KERNEL side, every pair among all eight d_i is coprime, including d_e. The diagonal multi-coset map is onto because its finite domain index is a multiple of the product of pairwise-coprime d_i and at most that product. It supplies ONE quotient point in all eight ACTUAL projected cosets. In that common fibre are eight actual disjoint N-cosets with subgroup indices c_i. The exceptional c_e must contain7, else its index is coprime to a regular c_i and their fibre cosets intersect. Therefore `c_i=7t_i'` with `t_i'|t_i`, again all private factors pairwise coprime.

Thus EITHER the proper quotient H/N OR the proper subgroup N carries a new actual direct P7 family with **the SAME eight labels and private factors each dividing its own preceding factor**. No selected finite tuple, arbitrary local fibre packing or private-seven exception is discarded.

## 4. Iteration gives a composition factor, not just an unrelated example

At each non-simple finite group carrying the labelled family, select ANY proper nontrivial normal subgroup and apply Section3. Choose the one of its normal subgroup or quotient that carries the descended family. Its group order strictly decreases and every new private index divides its own previous label's private index. Therefore iteration terminates after finitely many strict decreases at a finite simple group S with labelled private indices s_i|r_i.

S is a composition factor of the original finite quotient F. To see this without assuming simple subgroups of F are factors, induct UP the chain of chosen normal subgroups/quotients: a composition series for a normal subgroup followed by lifted refinements of the quotient gives one for H; a composition series of H/N likewise appears after lifting to H. At each step every factor of the chosen subgroup or quotient is consequently a composition factor of H. Hence the terminal simple S occurs as a composition factor of F.

S cannot be cyclic of prime order. If |S|≠7, its subgroup indices are not divisible by7; if |S|=7, each required subgroup index is7 and the eight nonempty disjoint cosets would be eight singletons in a seven-element group. Thus S is finite nonabelian simple. The proof is an existence assertion about an actual factor and its actual cosets; it is not an index bound on G or a claim that every composition factor has this property. □

## 5. Named existing bound, if separately admitted

The prior parent `sun-rank-free-P7-bounded-simple-existence-entire-parent-v1.md` records an independently scoped direct-P7 conclusion: such an actual simple factor S has order below `169^5971968`, with its complete grid/unitary-packing/normal-section dependencies. I have NOT re-reviewed its entire proof union in this continuation. If that separately parent-supported theorem is admitted at its exact named scope, it may be composed with the present seven-saturation bridge to infer the existence of a simple labelled P7 factor below that bound from any Sun8 counterconfiguration satisfying Sun7(G). The bound applies to S ONLY, not to G or all its finite quotient factors, and is not evaluated or used for an exhaustive search. It excludes no simple factor and does not solve Sun8.

## 6. Evidence and limitations

Section2's prime-support arithmetic is independently overapproximated by `frontier-20261028-global-seven-support-check.py`, SHA256 `882e6cb61e7baccd76216301a14a0428dc15ffe805672738e6398768db39d5b3`: all205 eight-label squarefree small-prime support multisets with pairwise gcd between2 and7 were enumerated; of the15 with at least three seven labels, NONE has a seven-free label. Actual run was recorded at Wed Oct28 17:32:48 PDT2026. This finite arithmetic is not a check of Sun7 or the group descent.

The all-label simple-factor/direct-P7 content already has a separate parent-supported ancestor in the bounded-existence disposition; the novel CURRENT composition is conditional on `Sun_7(G)` and supplies the previously unverified global counterconfiguration-to-P7 interface. No firstness, new family or retrospective ancestry claim is made. The universal Sun7 written-composition verdict and its FULL dependency closure are not independently reverified here. Parent must inspect/review the full bridge and normal-section proof before any adoption. The open target is exclusion of actual direct P7 families in ALL finite nonabelian simple groups, not merely verification of the displayed bound, a finite list, or a numerical score.
