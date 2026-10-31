# Shor code: a saturated old row is uniquely forced and constrains every head

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 18:01:01 PDT 2026**.
**All-order written UD theorem and conditional completeness callers; bounded exact raw-word checks. Not an original completion or universal no-go.**

## 1. Exact actual-code statements

Let X be ANY UD code, finite OR infinite, containing the literal Shor code S and the actual atom a^n, with n>=26. Let B be its actual one-b atoms; for each prefix residue i let J_i be the set of their suffix residues modulo n. Unique decipherability prohibits duplicate endpoint residue pairs. The four old suffix-zero atoms have prefix residues

    A={0,3,8,11}.

**Theorem A — unique saturated old row.** If either old row u=3 or u=8 has `|J_u|=n/4`, then 16 divides n, and that ENTIRE SAME actual row is uniquely forced:

    J_u={0,2,4,6}+16 Z_(n/16).                              (1)

No other A-tiling containing the four original row tails is possible. This concerns any UD supercode already containing a^n; finite factor-completeness is not used.

**Theorem B — actual head restrictions.** If row3 is saturated, EVERY odd prefix residue of a one-b atom is either the literal residue3 or is congruent11 modulo16. If row8 is saturated, EVERY even prefix residue is either the literal residue8 or is congruent0 modulo16. These statements are unconditional UD consequences within the respective saturated branch; they do not assume both rows saturate.

**Completion callers.** If X is a finite factor-complete UD completion D, SATURATION OF EITHER ONE of these two old rows forces the SAME actual one-b suffix histogram to satisfy all paired-class balances modulo4 and modulo8. If BOTH old rows saturate, all conclusions of `frontier-20261028-canonical-row-displacement-v1.md`, SHA256 **96a9750e100d25b53835f831375266ab38a17cbeff937454305b7bdbca4a4671**, follow WITHOUT separately assuming their canonical shapes: any new head is confined to the two stated classes and forces a specific optional row0-tail omission.

These are conditional branch statements. Neither row is proved saturated in an arbitrary original completion, and no WLOG/case-exhaustion or unrestricted original noncompletion follows.

## 2. The row injection and order16 prerequisite

For any prefix residue i, suppose j,j' in J_i and v,v' in A satisfy j+v==j'+v' modulo n. The actual two-one-b paths using those row atoms followed by old a^v b/a^v' b have congruent outer residues and internal seam; nonnegative a^n atoms pad boundaries to equal raw words. UD forces the pairs identical. Thus

    J_i × A -> Z_n, (j,v)->j+v  is injective.               (2)

If `|J_u|=n/4`, this injection is a bijective tiling. The independent elementary proof in `frontier-20261028-2adic-prefix-strengthening-v1.md`, SHA256 **d77fd47e36166d51b22ffb6d1ff977e60549116e20068c79f26e8f30ba5b6e44**, shows a direct A-tiling requires16|n: if v2(n)=2 or3, A has even multiplicity in every class mod4 or8, while each class has odd size, leaving at least one hole per class. Cardinality already forces4|n. The proof is repeated here rather than assuming a general cyclic-factorization theorem.

## 3. Four forced shifts propagate the ENTIRE tiling

Put n=16m. Both literal old rows3 and8 contain actual tails0,2,4,6, so their J_u contains those four residues. Their A-translates cover the following ordinary relative positions (all modulo n):

    {0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17}.

A shift j already COVERED by one of these translates cannot itself be in J_u: since0 belongs to A, its own translate would cover j again. To cover16, the only possible shifts are16,13,8,5. The latter three are already covered, hence forbidden; 16 MUST be in J_u.

Now cover18: its possible shifts are18,15,10,7; the latter three are already covered, so18 is forced. Similarly20 has candidates20,17,12,9, forcing20. Finally22 has candidates22,19,14,11; 19 is covered by the forced shift16 plus3, and the others by the original block, so22 is forced.

This entire argument translates by16k. Starting from each forced block `{16k,16k+2,16k+4,16k+6}`, it forces the next block. For k=0,...,m−2 the displayed positions are within [0,n−1] except for the understood cyclic sums; no alternative unknown tile can cover a target, because all its OTHER possible shifts already overlap a known tile. Induction gives all4m residues `{0,2,4,6}+16 Z_m`. Since `|J_u|=n/4=4m`, no other tail remains. This proves the actual row equality(1), without enumerating cyclic tilings.

## 4. A single saturated row already forbids many heads

Let H be all actual B head residues and let Δ contain every nonzero tail difference within ANY one head row. For any saturated row u with direct `J_u+A=Z_n`,

    H intersect (u+Δ)=empty.                                (3)

Indeed, for r=u+p−q with p,q distinct tails in a SAME existing row t, and any actual atom c of head r/tail s, choose j in J_u and v in A with j+v==s mod n. The two three-B lists

    (a^t b a^p), (a^u b a^j), (a^v b)
    (a^t b a^q), c,                 (b)

have congruent corresponding endpoint and seam residues. Inserting nonnegative a^n atoms at the actual boundaries makes equal raw words. Their first B-atoms differ, so UD is contradicted. This also works if c has an original head; no head values are assigned independently.

For canonical J_u, differences of its tails cover ALL even residue classes modulo16 except8, with every 16-block offset: the within-block differences0,±2,±4,±6 cover precisely those seven classes, and block differences range over Z_m. Exclude zero differences in(3).

If u=3 and r is odd, then r−3 is even. Except for r=3 itself, it lies in Δ unless `r−3==8 mod16`, i.e. r==11 mod16. This proves the row3 statement. If u=8 and r is even, the same argument says that except for r=8 itself, r must be0 mod16. This proves the row8 statement. The other parity remains unrestricted under a SINGLE-row hypothesis.

## 5. Consequences only for an actual finite completion

The raw same-object conservation proof in `frontier-20261028-seam-fourier-tradeoff-v1.md`, SHA256 **8169a9e6a7d7823a1c21f05794bf1c9e4c9290ac70a57855a0e4f0d322e19de2**, gives for every 2-power d|n: either the actual head counts or actual tail counts are equal on all residue pairs separated by d/2.

If row3 is saturated, §4 implies there are no heads1 mod4 and no heads7 mod8, but head3 is present. Thus the HEAD equality is impossible for both d=4 and d=8; the TAIL equalities follow. If row8 is saturated, there are no heads2 mod4 and no heads4 mod8, while head0 is present; again both head alternatives fail and the same tail equalities follow. This argument uses the full finite-completion conservation, not merely UD and a single saturated row.

If BOTH rows saturate, Theorem A makes them precisely the canonical pair in the prior displacement theorem. Its conclusions apply to the actual D: new heads are only0 or11 mod16, residues16 and n−5 are excluded, and at least one optional row0 tail must be absent. If additionally 11|n and tails are not uniform modulo11, the prior prime tradeoff forces at least3 distinct new head residues and at least2 optional row0-tail omissions. No converse is asserted.

If a separately established condition `660|n` is assumed, saturation also implies `16|n`, hence `2640|n`; this is just an elementary conditional arithmetic composition, not a fresh proof of the older 660 premise. Without that named premise the theorem itself only says16|n.

## 6. Independently executed bounded checks

    python3 -B frontier-20261028-saturated-row-forcing-check.py 128

For each n=32,48,64,80,96,112,128, the checker verified every local forced-shift step and the final n/4-element canonical tiling. It also generated and directly compared raw equal-word certificates for every tail residue and every head excluded by a SINGLE saturated row. For each of rows3 and8, respective orders yielded416,960,1728,2720,3936,5376,7040 exact ambiguity witnesses. These are finite validations of the formulas, not a proof of a general completion or all-n enumeration; §§2–5 provide the all-order reasoning.

Checker `frontier-20261028-saturated-row-forcing-check.py`, SHA256 **5a69ddd87113343fcbe2ba7cb6f164e3c3f660af3a93d10a9b011015baea7ce4**,59 LF /2731 B, natively pinned Wed Oct28 18:01:01 PDT.

## 7. Open boundary

It remains completely possible, on the present evidence, that a genuine completion has neither old row saturated, or that it satisfies the forced head/tail conditions while omitting the required optional tails. These results do not prove all n impossible or exhibit a finite complete D. They are written mathematical candidates requiring independent review; no novelty, formal/kernel/human or configured-independent-model acceptance is claimed. Historical process findings remain records, not newly validated premises.

**END OF UNIQUE SATURATED-ROW CANDIDATE.**
