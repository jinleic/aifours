# K7-A2-ZT5-erratum-v4: reverse t-row bound and the missing all-(2,2) transfer audit

Written: 2026-10-19T08:12:27-0700 (`/bin/date` immediately before exclusive create). Owner: Sun7K62Successor.
No computation. Candidate written steps, pending parent-owned R3. Read after ZE1-ZE3:

- ZA: `D/K7-A2-ZT5-A-v1.md` `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`; ZB: `D/K7-A2-ZT5-B-v1.md` `f482090adae221ea7bcaa23e1102aa4d3d4081933fd762f756f190d4ddf1f3a8`.
- ZE1: `D/K7-A2-ZT5-erratum-v1.md` `82d01721688ad10dfa44ed01aca0b914c515f0c508e24345587e063c6dca6dc4`; ZE2: `D/K7-A2-ZT5-erratum-v2.md` `c7c0d9bc61009421b79e817ac4c69d27e40a3914f04ba0b1d1b013b1abbf4f47`; ZE3: `D/K7-A2-ZT5-erratum-v3.md` `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667`.
- A22: `D/K7-TC-A22-v1.md` `9ebec2797485ac18ff1f1080cafd0634edd86117d166338631e04c4db1a46b41`; TC: `D/K7-TC-v1.md` `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117`; OV: `D/K7-A1-A2-delta-erratum-v1.md` `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`.
- K23 corrected R3' display: `D/K7-CASEA-K23-erratum-v1.md` `15b1516d7bc5d124565c8e16ea686b2b9b4947080aa059f37fd02d83040e14e1`.

## Scope of the missing audit

K23 classifies Case A **after** the all-(2,2) type has been excluded by A22. ZA did not explicitly audit that transfer.
Also, after ZW establishes the entry types, invoking the full Cor L in the reverse orientation is not automatic:
its extra z-label is 5*2^E w_z and can share 5 with p. The needed reverse at-least-two-fours conclusion nevertheless
has a direct capacity proof below. We do not import the entire old Cor L at this new scope.

## Lemma ZTR (reverse t-row bound) [NEW]

In normalized (a2-zt5), if Gamma^alpha* is connected, then at least two of the five alpha_tu (u in W) equal 4.

*Proof.* Work at t in C^alpha*. Its W masses are b_u/6 with b_u=alpha_tu, and its extra z mass is 5/6. By F7,
b_u in {2,4} for u in W', and b_p in {1,2,4}. The W-local indices are d_u=b_u r_u and the z-local index is
5*2^E w_z. The same spanning-tree index argument as ZT, now with pair parameters alpha*, gives PFG-t(i)-(ii):
no abstract row-type assumption is needed for that index chain. Every W-set weight vector has value <=5, with the
usual weight-1 condition on every occupied W fibre when equality holds.

If exactly one b is 4, put weight 1 on any one and 1/2 on every two and the four. This is feasible: the one is coprime
to the others, and three class elements cannot coexist with only one four (Sun(3)). There are at least three twos
by F7, and the value is 6, contradiction. If there is no four, W' consists of four twos and p is 1 or 2. Put weight
1 on p if b_p=1, or 1/2 if b_p=2, and 1/2 on the four W' twos. The value is exactly 5. Thus their union Q has measure
5/6 and each occupied W-set has weight 1: it is a single p (if b_p=1), or a pair of twos. If a right U_t-coset in
D_z cap Q did not hold p, it would hold two W' twos together with z; their three local indices have all pairwise
gcds 2, impossible by Sun(3). Hence D_z cap Q is contained in D_p. But mu(D_z)=5/6 and mu(Q)=5/6 imply
mu(D_z cap Q)>=4/6, whereas mu(D_p)<=2/6. Contradiction. QED

## Lemma ZA22 (all-(2,2) exclusion transfers to the T*=W branch) [NEW AUDIT]

In normalized (a2-zt5) with T*=W, no configuration has two alpha-fours and two alpha*-fours at every vertex of W.
This is a conditional transfer of A22, using FG-zf, ZW, ZT and ZTR, not an assertion that its (a1) statement already
covers the new family.

*Proof (complete dependency audit).* ZW and the alpha-side W3/E3 argument give every W-W and W-t entry in {1,2,4}
in both orientations. Under the degree hypothesis, F and F* are complementary 5-cycles. The odd ell-divisor triangle
rule (also for p, whose extra factor is 5^B) excludes entries 1 on W exactly as A22 section 1(b): twins would have the
same cycle-neighbourhood. Hence the W rows are (2,2,4,4) in both orientations.

A22 section 1(c) uses rows (2,2,4,4|e) with e<=2. For e=2 the TC R1 vectors vanish on z (OV TC.4); for e=1 both displayed
vectors in A22 vanish on z. Each has value 5 and its relevant four fibres contain a vertex other than z, so FG-zf's
z-free equality clause gives the same L_f1=L_f2. Fibres consisting solely of z need no containment. The labels at p
carry only their unique 5^B factor, so no pairwise gcd or feasibility test of those vectors changes.

Both cycle complements are connected. ZT gives |P*|>=2 and ZTR gives |P|>=2, for P={u:alpha_tu=4} and
P*={u:alpha*_tu=4}. They are disjoint by INV. On a 5-cycle, a two-set has a vertex whose two neighbours avoid it.
If |P|=2, choose such a vertex u in F; if |P|>=3, disjointness forces |P*|=2 and choose it in F* instead. At each of its
two cycle-neighbours the above equality of four fibres applies. TC transfers those equalities to the same disjoint
D-pairs used in A22 section 2. The count is unchanged: the two masses 4/6 and two masses 2/6 require union measure
at least 1. Indeed, if K is the overlap mass of the two 4/6 sets, their union mass is 8/6-K; at most
2 min(4/6-K,2/6) of the 4/6 small total mass is absorbed there, and remaining small mass needs half its measure in
additional fibres. Thus

    mu(union) >= K + 2(4/6-K) + max(0,2K-4/6)/2 >= 1.

The local triple exclusions are just Sun(3) on two twos with either z or t. The relevant z index at a W-apex is
3*2^E w_z in both orientations (since T=T*=W); t has an even-or-one coefficient in {1,2,4}, and the unique p factor
5^B has no other partner here. Thus all these gcds are still at most 2. V4 says the union avoids U_u and has measure
<1, contradiction. This uses V4, not a stronger full-FG union bound. QED

## Exact active audit additions for ZA

Insert before invoking K23/CELL-A:
1. Lemma ZW (with ZT before its connected-Gamma t-row step) supplies the missing alpha*-side entry prerequisites.
2. Lemma ZA22 above transfers and proves the all-(2,2) exclusion at the available partial-granularity scope.
3. In K23 Lemma CL, the |P*| conclusion uses ZT and the |P| conclusion uses ZTR; do not invoke the full old Cor L for
   the reverse orientation. After K23 obtains a K2,3 structure in either orientation x, its final t-row filter needs
   only to exclude 44411: weights 1/3 on its three fours and 1 on its two ones have value 6, against the corresponding
   PFG-t(i). The needed complement graph is connected as in K23 section 4. This kill is independent of the z-label's
   5-collision with p. It leaves 44412 or 44422 exactly as required, also when the K2,3 orientation x is alpha*.
4. Use K23E for the corrected R3' vectors. The rest of ZA's z-free/t-free transfer audit is unchanged.

## Dependency and verification boundary

PENDING R1 premises: A1 PFG-t index argument, TC/R1/TC transfer and A22's written count through OV.
PENDING R2 premises: K23+K23E, CELL+CELLE. PENDING R3: FG-zf/ZS, ZT/ZW/ZTR/ZA22 and the resulting ZA/ZB exclusion
candidates. New direct Sun uses in ZTR and ZA22 are Sun(2)/Sun(3) only; ZT retains its stated Sun(4) instance.
No theorem conclusion is accepted here. No computational output, full-family closure, novelty or Lean/human check is claimed.
