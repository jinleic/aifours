# Shor completion: canonical saturated rows force displaced old-row tails

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 17:57:01 PDT 2026**.
**Conditional all-order original-object obstruction; not a global no-go, completion or novelty claim.**

## 1. Branch, actual objects and conclusions

Let D be ANY finite UD factor-complete extension of the literal 16-word Shor code. Let its actual unique pure-a atom be a^n and its actual one-b layer B. Assume the PARTICULAR branch

    n=16m, m>=2,
    J_3=J_8=J_std={0,2,4,6}+16 Z_m,                         (1)

where J_i is the set of suffix residues of actual B-atoms with prefix residue i. Equality in(1) means the full SAME B rows, not independently supplied tilings. The original S already gives the required first four tails in each of rows3 and8. This is a restricted branch, NOT a claim that every completion has canonical rows.

Let H_new be the DISTINCT prefix residues of B outside `A={0,3,8,11}`, and let

    K_missing={k in {1,...,m−2}: 14+16k is NOT in J_0}.

Then:

1. Every r in H_new is either `16h` or `11+16h`, 1<=h<=m−1. The particular residues16 and n−5 are impossible.
2. If `16h` occurs as a new head, tail `14+16(h−1)` is missing from J_0. If `11+16h` occurs, tail `14+16(m−1−h)` is missing. The k=0 tail14 is an ORIGINAL S atom, so both head choices corresponding to it are automatically impossible.
3. `|H_new|<=2|K_missing|`. Since every actual completion requires at least two B-atoms with new heads, H_new is nonempty: hence m>=3 and K_missing is nonempty. A completion in branch(1) MUST displace at least one of the optional row0 tails30,46,...,14+16(m−2). In particular the explicit dead-end supercodes in the predecessor, which retain them all, cannot be completed.
4. The SAME actual tail histogram obeys the paired class-balance identities at d=4 and d=8, unconditionally inside this branch. If 11 divides n and its tails are NOT uniform modulo11, then `|H_new|>=3` and at least TWO of the optional row0 tails above must be missing.

These are necessary constraints on this named canonical-row branch. They do NOT show a completion exists, rule out this branch at every n, justify assuming(1) WLOG, or resolve the original unrestricted Shor question.

## 2. General saturated-row/three-word lemma

For an actual UD B containing a^n, let H be its set of head residues. Let Δ be the set of nonzero differences p−q of two tail residues in any SAME B head row. The old suffix-zero column contains all actual words a^v b with v in A.

**Lemma.** If an actual row u has a direct tiling `J_u+A=Z_n`, then

    H intersect (u+Δ) = empty.                               (2)

To prove it, suppose an actual B atom c=a^i b a^s has i==u+p−q mod n, where p,q come from actual atoms with the same head residue t and p−q!=0. Because J_u+A tiles, choose an actual row-u tail j and an old v in A with j+v==s mod n. Form the two actual three-B-word lists

    (a^t b a^p), (a^u b a^j), (a^v b)
    (a^t b a^q), (a^i b a^s), (b).

The first internal seams are congruent by i−u==p−q, and the second by s==j+v. Their actual first heads and final suffixes may differ by multiples of n if representatives are not canonical; at EVERY outer/interior boundary insert nonnegative copies of the actual pure-a atom a^n to match lengths. The lists are distinct because the first B-atoms have different tail residues p,q. This is an actual UD contradiction. Thus(2) uses all-B-word raw equality, not independence of matrices or formal factors. No factor-completeness is needed for the lemma once a^n and the saturated row exist.

## 3. Classify all new heads under the two canonical rows

For J_std, the 16 sums `A+{0,2,4,6}` are all residues mod16, so `J_std+A=Z_n` uniquely. Also `J_std−J_std` contains exactly the even residue classes modulo16 other than8, across all 16-block offsets: differences0,±2,±4,±6 cover those seven classes, and block-index differences range over Z_m.

Apply(2) to u=3 and u=8, using SAME-row differences already present in J_3. If a head r is even and not0 mod16, then r−8 is an allowed nonzero J_std difference, so r cannot occur. If r is odd and not11 mod16, then r−3 is such a difference, so r cannot occur. Therefore every new head has one of the two forms in §1. The old heads0,3,8,11 remain allowed and are not silently removed.

Row0 contains the original tail1. For a proposed head r=16h, take u=3 and the row0 tail difference

    (14+16(h−1))−1 = r−3.

If the displayed tail were in J_0, lemma(2) would prohibit r. Thus that tail must be absent. For r=11+16h, take u=8 and

    1−(14+16(m−1−h)) == r−8 (mod n).

The analogous tail must be absent. Both formulas cover 1<=h<=m−1. The two head classes are disjoint, and each k=0,...,m−2 occurs at most once per class, so each missing tail is charged by at most two head residues.

At k=0 the tail14 is actually in S; hence r=16 and r=n−5 cannot occur. Every other charge lies among k=1,...,m−2. This proves `|H_new|<=2|K_missing|`. The independent raw completeness/count argument in `frontier-20261028-prefix-layer-obstruction-v1.md`, SHA256 **ef0d973f52ece5365613a8280475e240992ab53d47bca55dd13ea62f573ab0dc**, proves at least two new-head B-atoms in every finite completion, so H_new is nonempty and at least one optional tail must be absent. For m=2 there is no optional k and branch(1) is impossible; nothing follows for all other branches.

## 4. Exact tail balances and the p=11 coupling

Inside branch(1), all actual heads lie in residues0,3,8,11 modulo16. Thus modulo4 the head classes1 and2 are empty, while class0 contains the old b atom. Modulo8 the paired head class4 is empty while class0 is nonempty. The head-folded alternative of the exact two-path Fourier dichotomy therefore FAILS at both d=4 and d=8. By the same actual seam-convolution argument reconstructed in `frontier-20261028-seam-fourier-tradeoff-v1.md`, SHA256 **8169a9e6a7d7823a1c21f05794bf1c9e4c9290ac70a57855a0e4f0d322e19de2**, the SAME tail counts satisfy

    C_a^(4)=C_(a+2)^(4)  for a=0,1,
    C_a^(8)=C_(a+4)^(8)  for a=0,1,2,3.

No head-smallness hypothesis is used for these two branch-specific conclusions.

If additionally 11|n and the tail histogram is not uniform modulo11, the same prime dichotomy forces uniform HEAD counts mod11. The original A occupies only three of the11 residue classes; each other class has n/11 actual B-atoms, so N_out>=8n/11. Any single B row packs with A and has at most n/4 atoms. Therefore at least `ceil((8n/11)/(n/4))=3` DISTINCT new head residues are required. Since each optional missing tail is charged by at most two new head residues, `|K_missing|>=2`. This is a conditional implication if the tails are unbalanced mod11; tail balance is not assumed or refuted.

## 5. Exact bounded witness checks

Executed:

    python3 -B frontier-20261028-canonical-row-displacement-check.py 128

For every n=32,48,64,80,96,112,128, the checker verified the canonical row tiling and directly compared raw equal words for all `(n−4)n` new-head/tail pairs after adding the corresponding necessary row0 anchor when relevant: respectively896,2112,3840,6080,8832,12096,15872 explicit equal-word witnesses. The k=0 anchor is the original tail14; for k>0 these are CONDITIONAL anchor tests, not assertions that a completion contains them. Exact all-n reasoning is §§2–4, not the finite check.

`frontier-20261028-canonical-row-displacement-check.py` SHA256 **5a836440a2c9fde7315fecc21977712cfd9d4f91ca69108dd07b013579015d41**,64 LF /2562 B, natively pinned Wed Oct28 17:57:01 PDT.

## 6. Original residual

A hypothetical full completion can evade this result by using noncanonical rows3/8, or within the branch by omitting the specified row0 tails and solving every other all-list and factor-coverage constraint. No proof establishes that either escape is impossible. The explicit D_n/E_n noncompletable supercodes deliberately have ALL the optional tails and therefore lie in the excluded branch; they do not force S itself to be noncompletable.

This result is written/finite-checked but unreviewed. No historical held outcome is an accepted premise. No original full witness/noncompletion, unrestricted WLOG, independent-model/human/formal/kernel or novelty claim is made.

**END OF CONDITIONAL CANONICAL-ROW DISPLACEMENT CANDIDATE.**
