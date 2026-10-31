# Shor completion: 2-adic prefix packing strengthens the compulsory new atoms

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 17:10:58 PDT 2026**.
**All-order written candidate plus exact bounded checker; no completion, noncompletion or novelty claim.**

## 1. Main new theorem and exact quantifiers

For every finite UD factor-complete extension D of the literal 16-word Shor code S, let a^n be its unique pure-a atom, B the SAME actual one-b layer, and A={0,3,8,11} the four old prefix residues. Let N_out be the number of atoms of B with prefix residue not in A. The preceding independently reasoned candidate `frontier-20261028-prefix-layer-obstruction-v1.md`, SHA256 **ef0d973f52ece5365613a8280475e240992ab53d47bca55dd13ea62f573ab0dc**, proves the necessary caller n>=26, |B|=n and N_out>=2 (>=3 if n odd).

**Strengthening.** If k=v_2(n) is 1,2 or3, then

    N_out >= 2^k.

In particular, if n is divisible by4 but not8 there are at least FOUR such new one-b atoms; if n is divisible by8 but not16 there are at least EIGHT. Every atom and every residue here belongs to the SAME hypothetical full D; no n/FACT factorization is asserted sufficient or independently recovered.

**Independent cyclic-tiling characterization.** For every n>=12, the four DISTINCT residues A tile Z_n uniquely by translations with some set J if and only if 16 divides n. When n=16m, one explicit tiling complement is

    J={0,2,4,6}+16{0,...,m−1}.

This is a genuine full all-order iff for this ONE cyclic set, not a finite maximal-code theorem or an assertion that the original S has a completion.

## 2. Same-D injection — exact input to both claims

For each prefix residue i in B, write J_i for its set of suffix residues. Unique endpoint pairs follow from raw UD with actual pure-a pads. The four old atoms a^v b, v in A, all have suffix0. If two pairs `(j,v),(j',v')` in `J_i×A` have equal sum modulo n, the corresponding two actual two-one-b lists have the same outer residues and same internal residue. Nonnegative a^n pads at the ends and seam turn them into distinct equal raw parses, unless both pairs were identical. Therefore

    (j,v) -> j+v mod n   is injective on J_i×A,
    |J_i+A|=4|J_i|.                                        (1)

This is a packing of ACTUAL endpoint data, not a new independently selected group factorization. If a row achieves equality `4|J_i|=n`, it gives an actual cyclic tiling complement of A.

## 3. Parity of occupied congruence classes

Assume 1<=k=v_2(n)<=3 and put d=2^k. Then n/d is odd. As a FOUR-ELEMENT MULTISET, A modulo d has even multiplicity in every residue: for d=2,4,8 its two copies are respectively at residues0 and3 modulo d. This statement is checked algebraically from A, not from a selected completion.

For ANY J with the injection property in (1), let N_r count the actual residues of J+A in class r modulo d. Since each j contributes the even multiplicity pattern of A,

    N_r is even for every r mod d.

The entire class r contains exactly n/d residues, an ODD number. Hence `N_r<=n/d−1`, so at least one residue is missing in EACH of the d congruence classes. Summing gives the exact all-order bound

    4|J|=|J+A|<=n−d.                                      (2)

This holds for every individual row of EVERY actual hypothetical D, not only row0 or row11. The original prefix set A contains four distinct residues because n>=26. Summing their row counts and using |B|=n gives

    N_out >= n−4 floor((n−d)/4) >= d = 2^k.

No hypothesis of a row attaining its upper bound is needed, no floor is silently cancelled, and no selected n underlies the universal implication. When k=2 or3, n−d is divisible by4 and the displayed lower bound is exactly4 or8 respectively. The k=1 case supplies2; for odd n and 16|n the earlier result remains the applicable displayed bound.

## 4. Full cyclic-tiling iff, including the boundary and explicit converse

Suppose n>=12 and A+J is a direct unique cyclic tiling. A's four residues are distinct, so `4|J|=n`; in particular 4 divides n. If 16 did not divide n, v_2(n) would be2 or3, and (2) would say `|A+J|<=n−2^v2(n)<n`, a contradiction. Thus 16 divides n. This argument pays the whole necessity without importing a cyclotomic/factorization theorem.

Conversely let n=16m and take `J={0,2,4,6}+16{0,...,m−1}`. Modulo16 the sixteen sums from

    A+{0,2,4,6}

have one representative of every residue: the shifts of0 and8 cover all evens, and those of3 and11 cover all odds. If two sums `a+y+16k` and `a'+y'+16k'` agree modulo16m, reducing mod16 forces `(a,y)=(a',y')`; then `k=k' mod m`. With k,k' in the displayed range, the pairs coincide. The 4*4*m sums are therefore all n residues once. This proves sufficiency, including m=1, with no claim about any other rows, multi-b atoms or factor-completeness of D.

For n=16m this complement contains the old suffix set {0,2,4,6} of prefix rows3 and8, so the generic single-row packing bound can actually be saturated for those rows as an isolated cyclic layer. It does NOT satisfy all original row0 constraints by assertion and does not give a common completed one-b layer.

## 5. Actual bounded checker and precise limitations

Executed:

    python3 -B frontier-20261028-2adic-packing-check.py 2000

Exact output: it checked residue multiplicities/odd class sizes for all n=26..2000 with v_2(n)=1,2,3 (respectively494,247,123 orders); verified the explicit A-tiling for all125 multiples of16 from16 through2000; and reported the n=660 and n=1320 lower bounds4 and8. Those are finite checks of the displayed formulas/construction. The proof in §§2–4, not finite sampling, is the all-order argument.

Checker pin observed with native prewrite clock:

    frontier-20261028-2adic-packing-check.py
    SHA256 118842d79ab3e0bc61e7f090ac085332905ed2d130537d2b860a140f0808bb35
    58 LF /2079 bytes.

The n=660/1320 illustrations are NECESSARY-only conditional statements about a hypothetical completion with that actual order, not evidence that either order is attainable. Earlier parent FACT/660 statements are not used in this derivation. These results do not force a newly required atom into the separate 400 forbidden pairs, do not decide full-list UD/completeness, and do not close the original all-order question. Mathematical review and novelty remain outstanding; all earlier failure/quarantine records remain historical, not retroactively validated.

**END OF 2-ADIC FRONTIER ADDENDUM.**
