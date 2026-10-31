# An OA(10,4) contains at most one OA(3,4) subarray

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` before writing: **Wed Oct 28 18:42:04 PDT 2026**. This strengthens the earlier all-arrays *disjoint*-pocket result `frontier-20261028-suboa-intersection-obstruction-v1.md` SHA **50c98f25fba210725c2ca768a85fbf677cd3d4390a71bc01fde6e84639aa9dc6**: even two overlapping OA3 pockets are impossible in the same classical OA10. This is NOT an unrestricted quantum QLS10 no-go.

## 1. Statement

An OA(n,4,n,2) consists of n² 4-tuples, each coordinate using n symbols, and each ordered pair in two distinct coordinates appearing exactly once. Such an array is a pair of orthogonal Latin squares and specifies a classical 1-resolvable QLS.

An OA(3) subarray P is a subset of9 tuples which, using3 symbols in each coordinate, has the same pair-bijection property. **Claim:** any OA(10,4,10,2) contains AT MOST ONE such P. This covers every possible intersection pattern, not just disjoint pockets or a particular published table. The Parker example has exactly one.

## 2. Elementary subarray facts

If P has coordinate alphabets S_i, any ambient tuple outside P has at most ONE coordinate belonging to its respective S_i: two such memberships would give a coordinate pair already present in P and hence the same ambient tuple. Each symbol occurs10 times in the ambient array and3 times in P, so outside P there are `4*3*(10-3)=84` S-memberships.

For two OA3 subarrays P,Q with Q alphabets T_i, write `t_i=|S_i intersect T_i|` and `r=|P intersect Q|`. For every i!=j,

`r=t_i*t_j`.                                                    (1)

Indeed, for every shared pair of coordinate symbols, P and Q each contain a tuple with that pair and ambient uniqueness makes those tuples identical; conversely every common tuple has shared symbols. If r>0 then every t_i>0, and comparing products in (1) makes all four equal to a common t∈{1,2,3}; r=t². Their intersection is itself an OA(t) subarray: every pair of its shared coordinate alphabets appears exactly once.

If t=2, an OA(2,4,2,2) would exist, impossible: the two order-two Latin squares cannot be orthogonal (alternatively the proper-subarray counting bound `n>=3k` applied inside P gives 3>=6). If t=3, P and Q have all9 tuples in common. Therefore DISTINCT P,Q, if not disjoint, must have **exactly one common tuple and exactly one common symbol in EACH coordinate**.

## 3. Disjoint case, included for self-containment

Suppose P,Q are disjoint. Then t_i can be positive in at most one coordinate, since shared symbols in two coordinates would force a common tuple. Let t be that one intersection size, or0. Let X be the82 tuples outside P union Q. For x∈X let A mean x has one S-membership, and B one T-membership; by §2 neither can have more than one.

`|A|=|B|=84-3t`: Q contains 3t S-memberships. For x in both A and B, count memberships in different positions. The 12 ordered pairs of distinct positions give `12*3²=108` cross memberships in the whole OA; P and Q contribute `9t` each, so `I-J=108-18t`, where I=|A intersect B| and J counts coincident-position memberships. The t common symbols in the one shared coordinate occur `10-3-3=4` times outside P union Q, so J=4t and `I=108-14t`.

Consequently the two genuine set cardinalities satisfy

`|A\\B|=-24+11t >=0`,
`|X\\(A union B)|=22-8t >=0`.

For t∈{0,1,2,3} the first demands t>=3 and the second t<=2: contradiction. Thus P,Q cannot be disjoint.

## 4. One-common-cell case: the new obstruction

Suppose P,Q share exactly one tuple and have precisely one shared symbol in EACH of four coordinates. Let X be the `100-(9+9-1)=83` tuples outside P union Q. Define A and B as above.

Outside P there are84 S-memberships. Q excluding the common tuple contributes exactly `4*(3-1)=8` such memberships: each of its four shared symbols appears3 times, one of which is the common tuple. Thus

`|A|=|B|=84-8=76`.                                            (2)

Let I=|A intersect B|, J counting its tuples with S and T memberships in the SAME coordinate. Among all tuples there are `12*3²=108` cross memberships in distinct ordered positions. P contributes36 (four T-shared symbols, each occurring3 times and paired with3 other S positions); Q similarly contributes36; the common tuple's12 cross memberships were counted twice. Hence outside P union Q,

`I-J = 108-(36+36-12)=48`.                                    (3)

For EACH coordinate, its common symbol occurs10 times in the ambient array and `3+3-1=5` times in P union Q, leaving5 outside. The four same-coordinate counts are disjoint on X because every x has at most one S- and at most one T-membership. Hence

`J=4*5=20`, `I=68`.                                           (4)

Inclusion–exclusion now gives `|A union B|=76+76-68=84`, but X has only83 tuples. Contradiction. This proves the one-common-cell case impossible, completing the all-pattern theorem.

Independent exact arithmetic `frontier-20261028-overlapping-pocket-count-v1.py`, SHA **f7dd9bef5693651914ac831abf13fac65e7222efd67b17b4ff77877417a9fd68**, computes the disjoint cardinalities for t=0,1,2,3 and the one-cell count `(X,A,B,I,union)=(83,76,76,68,84)`. It checks arithmetic only; §§2–4 are the mathematical argument.

## 5. Implication and limits

For proper OA(k) pockets in OA10, the elementary bound `10>=3k` gives k<=3; OA2 does not exist, so any nontrivial proper pocket is OA3, and by the new theorem there is at most one. An independent-pocket rotation applied directly to a single classical OA10 therefore cannot be expanded by finding an overlapping second OA3: the required second subarray does not exist. The existing exact13-ray Parker rotation is consistent and reaches the one-pocket bound; it remains far short of100 rays.

The theorem does NOT exclude non-OA local trades, changes of incidence, surgeries whose later pockets exist only after a genuinely quantum transformation, nonlocal/entangled deformations, or starting directly from a nonclassical array. It does not bound all 1-RQLSs or all constructions, and prior broken SMT outcomes remain untrusted as already recorded. Independent review, novelty screening and the original exact100-ray target remain open.
