# Shor completion: double-saturated old rows force exact column and head-class conservation

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 18:08:58 PDT 2026**.
**All-order written necessary consequences of a specified branch; bounded integer checks. No full completion/noncompletion or novelty claim.**

## 1. Actual branch and exact new conclusions

Let D be ANY finite UD factor-complete extension of the literal Shor S. Let a^n be its actual pure-a atom, B the SAME one-b layer, `r_i` and `c_j` its head/tail residue multiplicities modulo n. Assume BOTH original rows3 and8 attain their maximal n/4 one-b atoms.

The prior all-order unique-row theorem `frontier-20261028-unique-saturated-old-row-v1.md`, SHA256 **87921649471a5e734199a5d776831f17611b6b39c4bea9d8542e3698fbe46f5f**, forces n=16m>=32 and

    J_3=J_8=J_std={0,2,4,6}+16 Z_m,  r_3=r_8=4m.

The SAME finite completion has |B|=n and its actual ordered two-b paths obey `sum_i r_i c_(gamma−i)=n` for EVERY seam gamma. Under these hypotheses:

1. **Exact five columns and seven zero columns:**

       c_0=4, c_1=2, c_2=3, c_6=2, c_7=1,
       c_5=c_8=c_9=c_10=c_(n−3)=c_(n−2)=c_(n−1)=0.

   The five nonzero columns are exactly filled by the already present original S atoms. Thus every new one-b atom with a new head has a tail outside `{0,1,2,6,7}`.
2. For EVERY actual head residue i other than3 or8,

       c_(8−i)=c_(9−i)=c_(10−i)=0  (indices mod n).       (3)

3. If `R_a` denotes the actual HEAD count folded modulo16, then

       R_0=R_3=R_8=R_11=4m,   R_a=0 otherwise.          (4)

   Thus the head polynomial has Phi_16 as a factor, while the actual tail polynomial does NOT. This is forced by SAME-array two-path conservation; it is not a choice of Fourier branch.
4. Let N_out count one-b atoms with heads outside the four original residues. At least one such atom is in head class0 mod16 and at least one in class11 mod16. IF N_out=3, exactly two are in the first class and one in the second, while the actual old row sizes are `|J_0|=4m−2`, `|J_11|=4m−1`.

All claims are CONDITIONAL on BOTH saturated original rows. They are not WLOG for the original problem and do not assert a valid B or full D exists.

## 2. Three seams force exact columns on the SAME B

The old S words imply

    r_0>=5, r_11>=3,
    c_0>=4, c_1>=2, c_2>=3, c_6>=2, c_7>=1.

At seam gamma=8, the contributions from heads8 and3 alone are

    4m c_0+4m c_5 >=16m=n.

Every term in the actual seam convolution is nonnegative and the total is n. Therefore `c_0=4,c_5=0` and ALL contributions from other heads vanish. In particular c_8=0 (r_0>0), c_(n−3)=0 (r_11>0), and c_(8−i)=0 for every actual head i outside {3,8}.

At seam9 the two saturated contributions are `4m(c_1+c_6)>=16m`, so `c_1=2,c_6=2`, all other-head contributions vanish, and in particular `c_9=c_(n−2)=0`. At seam10 the contributions are `4m(c_2+c_7)>=16m`, giving `c_2=3,c_7=1`, `c_10=c_(n−1)=0` and the corresponding general zero in(3). These are literal integer equalities, not an inferred sign or a selected atom.

The stated old atoms already meet each nonzero column's exact count, so no further atom can occupy one of those five tail residues. Because n>=32 all seven zero residues listed in §1 are distinct and none hides an original nonzero tail.

## 3. The order16 TAIL alternative is impossible

Let C_a be the sum of actual c_j over tails j==a mod16. Each saturated canonical row contributes exactly m atoms to each of the four classes0,2,4,6 and none to8,10,12,14. The original row0 and11 atoms outside these saturated rows additionally contribute TWO to class0 and ONE to class2. Therefore

    C_0>=2m+2, C_2>=2m+1, C_4>=2m, C_6>=2m.

If the tail polynomial vanished at a primitive16th root, its folded counts would satisfy `C_a=C_(a+8)` for a=0,...,7, since `Phi_16=X^8+1`. In particular the four classes8,10,12,14 would contain at least

    (2m+2)+(2m+1)+2m+2m = 8m+3

atoms. NONE can be in the two saturated rows, whose tails occupy only classes0,2,4,6. But there are exactly `n−8m=8m` atoms outside those two rows. Contradiction. Hence the TAIL alternative at every primitive16th root is impossible.

The actual seam-convolution Fourier identity therefore forces the HEAD polynomial to vanish at the primitive16th roots: `Phi_16|R` and `Phi_16` does NOT divide C. Equivalently the actual folded head counts satisfy `R_a=R_(a+8)` for all a<8.

## 4. All four head-class masses are EXACT

The single-saturated-row head theorem says a saturated row3 permits odd heads only at literal3 or in class11 mod16, and a saturated row8 permits even heads only at literal8 or in class0 mod16. Consequently every head lies in one of the four classes0,3,8,11; the classes3 and8 consist of their single literal saturated rows. Thus `R_3=R_8=4m`.

The forced HEAD pairing from §3 gives `R_11=R_3=4m` and `R_0=R_8=4m`, proving(4). All other class counts are zero. In particular there are new heads of both kinds because old rows0 and11 each have at most4m−1 atoms by their explicit two-hole packings. If e/o count the number of atoms at new head residues congruent0/11 modulo16, then

    e=4m−|J_0|>=1,    o=4m−|J_11|>=1,
    N_out=e+o.

This is an exact count identity for the SAME B, not a statement about the number of DISTINCT new head residues.

## 5. Exact structure IF the global minimum N_out=3 occurs

The preceding computer-assisted all-order result `frontier-20261028-extremal-row-three-new-heads-v1.md`, SHA256 **8f0ab81e2a7e11f1127d06d1130cd7be0b82e0aa05c862302f74d6507847a704**, proves N_out>=3 for all 16-divisible orders. Suppose equality holds in the present double-saturated branch.

The two old row deficits e,o are positive integers with e+o=3. If e=1, row0 is extremal with4m−1 tails. Its flagged transfer certificate forces every optional tail `14+16k`, 1<=k<=m−2, present. But the canonical-row displacement theorem says ANY actual new head forces one of those tails missing; contradiction. Thus e=2,o=1, and the two row counts are exactly as in §1. This implication depends on the named computer-assisted predecessor and does NOT establish that such a three-atom completion exists. The possibility that the two even-class atoms share one new head is not excluded.

## 6. Exact bounded check, scope and residual

Executed:

    python3 -B frontier-20261028-double-saturation-balance-check.py 2640

The independent integer checker validated the canonical tail-class lower counts and strict `8m+3>8m` contradiction for all164 multiples of16 from32 through2640; it also checked the stated N_out=3 deficit accounting. At n=2640 the tail-balance alternative would require at least1323 atoms in opposite classes while only1320 atoms lie outside the two saturated rows. These are finite checks of the elementary inequalities; §§2–5 are the all-order reasoning.

Checker `frontier-20261028-double-saturation-balance-check.py`, SHA256 **cf66f349b78a9e7d030ea5beafa57104617d8202e253b953cf82f3a602b0ab55**,48 LF /2077 B, natively pinned Wed Oct28 18:08:58 PDT.

The original completion may have neither or only one saturated old row, and even in this branch the forced exact histograms are NOT a proof of inconsistency. No original finite completion, unrestricted all-order noncompletion, source novelty or stronger assurance follows. The indicated flagged-DP predecessor needs independent certificate review; no historical held outcome is promoted as a premise.

**END OF DOUBLE-SATURATION CONSERVATION CANDIDATE.**
