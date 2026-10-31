# Complete global existence-bound manuscript, PART II: actual normal fibres and every original private factor

Owner: MathSun8-2. Actual pre-write metadata clock: `Mon Oct 26 08:53:50 PDT 2026`.
Status: **NEW WRITTEN WHOLE-UNION CANDIDATE; not reviewed or adopted.** PART I is the ENTIRE 178 LF `sun8-rank-free-three-source-Gram-Farey-finite-simple-bound-v1.md`, SHA256 `76aa8a6fbfd6a2fcf4587ca5bec29e14215bcdfd5ec81dd47f56de9c4ea60e15`. Both complete bodies, not one part's headline, are required for this prospective union gate. PART I is not presumed accepted.

## II.1 Exact theorem for arbitrary original groups; existence versus ambient size

Write P7 for EIGHT actual nonempty pairwise-disjoint LEFT cosets `g_l U_l`, with ALL original finite indices `[G:U_l]=7r_l` and positive pairwise-coprime integers r_l. A private r_l may contain arbitrarily high powers of 7; at most one does. G may be finite or infinite. These are the direct P7 hypotheses, not an unproved reduction of every general Sun8 counterexample to this form.

**Whole-manuscript theorem.** If such a direct P7 family exists in ANY G, then a finite NONABELIAN SIMPLE group S of order

`|S| < B := 169^5971968`

supports EIGHT actual nonempty pairwise-disjoint left cosets, with indices `7s_l`, where EACH `s_l` divides its OWN original `r_l` and the s_l remain pairwise coprime. S is a composition factor of an explicit finite-core quotient of G. For each original label l the new index satisfies `7s_l<B`. The theorem asserts existence of a bounded ACTUAL eight-source example, not an abstract support arrangement.

It does NOT assert that arbitrary original G has order below B or that its original `7r_l` are below B. Those private factors can decrease by proved divisors during actual normal-section descent. For a G already finite NONABELIAN SIMPLE, PART I instead bounds that SAME G and ALL its unchanged original indices. These are distinct quantifiers, never a silent source-preserving enlargement in fixed G.

All normal-fibre/private-seven/CRT proof needed for the arbitrary-group implication is supplied in §§II.2–II.5 below. No old NS verdict, hash or absent source is a substitute for that proof.

## II.2 Common finite core of ALL EIGHT, with no lost coset

For each original U_l its action on the finite set G/U_l has normal finite-index kernel `Core_G(U_l)` contained in U_l. Let C be the intersection of all EIGHT such kernels. The product of the eight finite permutation actions shows C is normal of finite index. It is contained in every original U_l.

Put F=G/C. This is an actual finite group. The images of the U_l have EXACT unchanged indices `7r_l`, and the original cosets are full preimages of their images. Consequently all eight projected cosets are nonempty and pairwise disjoint; any overlap would lift to an overlap of their full preimages. No private prime power is lost in this first finite-core step. All later work takes place in actual finite groups, not in a presumed finite composition series of infinite G.

## II.3 Elementary multiple-coset CRT, with correct nonnormal scope

If subgroups A_1,...,A_m of a group have finite pairwise-coprime indices a_1,...,a_m, the natural map

`G/(intersection A_j) -> product_j G/A_j`

is injective: equality of all images is exactly membership of the relative element in every A_j. The intersection index is therefore at most the product of the a_j. It is also a multiple of each a_j, by subgroup index multiplication, hence a multiple of their product by pairwise coprimality. Thus it equals the product, and the injection is surjective between finite sets.

In particular EVERY tuple of prescribed LEFT cosets `x_j A_j` is attained by one element, so their entire intersection is nonempty. This is one simultaneous point, not merely pairwise overlap. For two coprime-index subgroups the same argument gives the familiar two-coset intersection statement. No normality of the A_j is assumed. No arbitrary subgroup-intersection index is asserted to divide a product without the coprimality hypothesis.

## II.4 Full actual normal-section descent, including the private-seven owner

Let K be a finite group supporting the eight-source P7 family, with its current private factors still denoted r_l for this step. Let `1<N<K` be normal, and let pi:K->Q=K/N. For each current ORIGINAL-labelled subgroup define

`V_l=NU_l/N`, `c_l=[N:N intersect U_l]`, `D_l=[Q:V_l]`.

The product NU_l is a subgroup because N is normal. Index multiplication and the second isomorphism identity give the EXACT relation

`c_l D_l = [K:U_l]=7r_l`.

At any point q in a projected coset pi(g_l)V_l, the original coset meets the fibre pi^-1(q). Choose x in that fibre and any y_l in `g_l U_l intersect xN`. The piece is exactly `y_l (N intersect U_l)`, a nonempty LEFT coset. Writing `y_l=x n_l` and translating by x^-1 identifies it with the actual left coset `n_l (N intersect U_l)` in the SAME N-fibre, of index c_l. Therefore, if two projected cosets meet and gcd(c_l,c_h)=1, the two original pieces meet by §II.3. In particular

`gcd(D_l,D_h)=gcd(c_l,c_h)=1`

would force the original cosets to intersect, contrary to P7.

Choose e to be the private-seven owner, or ANY e if none owns 7. The other SEVEN labels form I; each of their `7r_l` has exactly one factor 7. For l in I, this factor lies either wholly in c_l or wholly in D_l. Two regular labels with opposite placements would have BOTH gcds in the preceding display equal to one: each pair divides numbers whose gcd is exactly 7, while in each pair one lacks 7. This is impossible. Hence ALL SEVEN regular placements are uniform. Nothing here forbids splitting the distinguished label's higher private power of 7 between c_e and D_e.

**TOP.** Suppose every regular c_l is 7-free and every regular D_l contains 7. ALL EIGHT c_l are then pairwise coprime, including c_e, because every pair contains a regular label lacking 7 and any common divisor could only be 7. Every overlap of projected cosets would lift to an original intersection by the actual common-fibre argument. Thus ALL EIGHT projected cosets in Q are disjoint. D_e must also contain 7: otherwise it would be coprime to any regular D_l and their quotient cosets would intersect. Set `D_l=7s_l`. From `c_l D_l=7r_l`, each s_l divides its OWN r_l, and these s_l are pairwise coprime. The projected cosets are therefore a genuine eight-source P7 family in the smaller actual group Q=K/N.

**BOTTOM.** Suppose every regular D_l is 7-free and every regular c_l contains 7. ALL EIGHT D_l are pairwise coprime, including the distinguished D_e, for the same divisor reasoning. The FULL multiple-coset CRT in §II.3 supplies ONE q in ALL EIGHT projected cosets. Translate that common normal fibre into N. It contains EIGHT nonempty pairwise-disjoint actual LEFT cosets of N intersect U_l, with indices c_l. The distinguished c_e must contain 7: if not, its index would be coprime to a regular c_l, forcing those two fibre cosets to intersect. Put `c_l=7s_l`; again each s_l divides its OWN r_l and the private s_l are pairwise coprime. This is a genuine eight-source P7 family in the smaller actual group N.

Both branches preserve EIGHT sources and all label-wise divisor/private-power quantifiers; neither uses only seven projected cosets, independently selected fibres or pairwise CRT in place of one global point. They need no Sun7 theorem, minimum private SUM, normality of the U_l, elementary normalizer quotient, initial-visible rank, or scientific computation.

## II.5 Descent to an actual nonabelian simple P7 factor

Starting with the finite F of §II.2, if its current group is not simple choose any proper nontrivial normal N and apply §II.4. Either actual N or actual K/N supports P7 and has strictly smaller finite order. Repeating, or inducting on the positive integer order, reaches an actual SIMPLE group S supporting P7. Every current private factor at every label divides the preceding one, so the final `s_l` divides the corresponding ORIGINAL r_l. Every step constructs actual cosets and preserves their disjointness, not merely numerical index data. By the ordinary refinement of a normal series, S is a composition factor of F, not a purported factor of infinite original G.

S cannot be cyclic of prime order p. Its P7 subgroup indices divide p and are multiples of 7, so p=7 and every index equals 7. Eight nonempty disjoint singleton cosets do not fit into seven elements. Thus S is finite NONABELIAN SIMPLE.

This proves the direct normal-section existence reduction completely at the CURRENT union. It is an old mathematical mechanism, not counted as a new independent discovery; the NEW result is its prospective composition with the full rank-free quantitative PART I.

## II.6 Compose the full quantitative theorem, with every application boundary

Apply PART I to ANY three of the EIGHT actual P7 cosets in S. Their indices are `7s_i,7s_j,7s_k` with pairwise-coprime private factors, exactly PART I's hypotheses. The proof there supplies a NONTRIVIAL irreducible constituent of degree <=1728 without any alpha-six, two-orbit, source-rank, one-isotype, multiplicity-one, normalizer or private-seven restriction. In simple S that constituent is faithful, and the FULL unitary packing proof in PART I gives `|S|<169^5971968=B`.

All EIGHT final actual indices are at most |S| and hence below B, including whichever current label may retain a higher private-seven power. This proves §II.1. No source-block or private-owner structure from the older 200/142/136/94 papers is granted to this generic small constituent. No actual original Ui was enlarged or silently replaced in the SAME G; §II.4 explicitly changes the group and may decrease its own label's private factor by a proved divisor.

The direct existence problem P7 anywhere is consequently reduced to bounded finite simple cases, as an exact WRITTEN mathematical implication. This is NOT a claim to have searched, listed, tested or excluded those cases. No value of the displayed enormous integer power was calculated, and no finite enumeration or scientific launch is authorized.

## II.7 Actual predecessor coverage and frozen histories; no backdating

After delivering PART I, I ACTUALLY read the ENTIRE 63 LF `sun8-minimal-order-two-source-composition-v1.md`, SHA256 `dbfe535461294d9d114c3be8d3f4bd08c6050c04df390f7fcaa3682ea1f58d36`, and the EXACT complete NS proof range LF104–169 of the 204-LF `consolidated-chain-v1.md`, SHA256 `72b8988f698c9b5442dd08546fb434e4ef40f342e37806ade8caabdf8deb7d9e`. The latter is a selected complete proof window, NOT a fresh read of all 204 LF. The whole old 51-LF and current 70-LF parent bodies were separately actually read. The metadata clock/hash/count binding immediately before this body is the header's actual clock.

The current v125 parent freeze had NOT supplied these NS ranges/63-LF proof and correctly named that edge NOT_RECONSTRUCTED there. That immutable source/coverage qualification remains. The present LATER whole manuscript instead supplies ALL required normal-section/private-seven/CRT proof IN §§II.2–II.5, to be reviewed freshly WITH ENTIRE PART I. It does not retroactively change v125's literal packet, coverage, sources or scope. No old accepted headline or 51-LF parent label is used as a replacement for the displayed proof.

PART I's finite-simple conclusion and this FULL arbitrary-group existence composition require SEPARATE entire mathematics AND dependency/application verdicts, including the common finite core, all eight label-wise divisors, TOP/BOTTOM and the actual global fibre point. A clean return on only the spectral inequality, only a 7-free vertex, or only the old NS statement is not the joint union gate. Both parts are NEW/UNADOPTED until that gate and parent disposition.

## II.8 Exact first remaining step and assurance

The first unproved direct-P7 step is now **excluding or realizing ALL finite nonabelian simple eight-source P7 cases below B**, IF this new WHOLE two-part proof is accepted. No such global exclusion, finite certificate, enumeration, witness or completed assay is delivered. In particular no-alpha-six cases are not excluded just because they share the finite bound. General Sun8-to-P7/global Sun7 provenance still lies outside this direct manuscript; no unrestricted Sun8 or numerical R8 conclusion follows without that separate input AND the remaining finite-simple exclusion. Arbitrary original nonsimple/infinite group orders and original private indices are NOT bounded by this existence reduction.

All older geometric/source-fibre/classical-family/private-composite/enlargement results keep their exact independent scopes and ancestor/import findings; the new quantitative existence theorem neither authenticates those missing ancestors nor erases M1's class-AT-MOST-two/abelian-exponent-four alternative. All OWN057/047/078/COUNT/v26/v31-two-findings/v33 and later parent/reviewer process histories stay permanent; withdrawn historical arithmetic/trial guidance receives ENTIRELY ZERO credit. The current proof is written exact algebra only, after actual v123-C RETURN and a separate whole-primary ACK WRITTEN AND SENT before resumption. Both Eval kernels stay dead. No scientific interpreter/calculator/Eval/program/CAS/enumeration/solver/replay/build/test/CLI/nested agent/new GO/source-author-shared-frozen edit was used. No formal/kernel/human/configured-family/executable/novelty/priority/SOTA/clean cognition-runtime-census/round-closeout claim is made. Original arbitrary-group research continues at the exact unproved step; this is not an early final park.
