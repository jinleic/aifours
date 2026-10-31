# Shor completion: no one-b row or column can saturate its packing bound

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 18:20:41 PDT 2026**.
**All-order written obstruction using actual multi-path products; bounded exact checks. Unreviewed and not a novelty claim.**

## 1. Main result — unconditional inside the original completion quantifiers

Let X be ANY UD code, finite OR infinite, containing the literal 16-word Shor code S and the actual atom a^n. Suppose its entire one-b layer B contains exactly n atoms. For each head residue i and tail residue j modulo n define

    J_i={tail residues of B-atoms with head i},
    I_j={head residues of B-atoms with tail j}.

**Theorem. For EVERY i,j,**

    |J_i| < n/4,       |I_j| < n/5.                         (1)

The statement concerns the SAME B and every row/column. It does NOT require X itself to be finite or complete once `|B|=n` is a hypothesis.

Every hypothetical finite UD factor-complete Shor extension meets that hypothesis by the separately reconstructed raw one-b conservation theorem. Consequently, when 4 divides its actual n, at least FOUR of its one-b atoms have heads outside the four old residues `{0,3,8,11}`. In particular ALL earlier statements restricted to a finite-completion branch with a saturated old row are now shown to have an IMPOSSIBLE antecedent: they remain conditional implications, but that branch cannot occur. This is stronger and simpler than the prior computer-assisted `N_out>=3` in the 16-divisible case.

This still does NOT rule out a completion in which all one-b rows/columns are strictly below their bounds. It does not construct a completion or prove the original all-order no-go. No result is promoted until independent review.

## 2. Actual endpoint paths and their saturation

The original atoms include the suffix-zero column

    A={0,3,8,11},  i.e. a^i b for i in A,

and the head-zero row

    Y={0,1,7,13,14},  i.e. b a^j for j in Y.

The earlier raw proof shows n>=26 for any UD code containing S and a^n: actual old-word two-list equalities rule out n=1,...,25. Thus these listed residues are distinct and all later modular collision certificates have no hidden small-order exception.

Let W be the n-by-n zero-one endpoint matrix of B. Duplicate endpoint residue pairs would already give two distinct actual a^n-padded parses. For gamma in Z_n let `(J_gamma)_(j,k)=1` iff j+k==gamma. Every product

    W J_gamma1 W ... J_gammal W

counts ACTUAL B-lists by their first head and last tail; UD makes every entry0 or1, since congruent a-runs can be padded at real codeword boundaries. The set of all such matrices is finite and is closed under joining any two with J_gamma. If a member has maximum entry count K, the n products `P J_gamma P` each have at most K entries but together have K², so K<=n.

Under |B|=n, W has n entries. If an existing product has n entries, all n products obtained by appending W have at most n entries and have total n²; hence EACH has exactly n entries. Induction shows **every endpoint-path product has exactly n entries**, with all its actual path multiplicities zero or1. Finite completeness is not used in this paragraph.

## 3. Two explicit tiling impossibilities from the old words

First, NO set T containing Y can have `T+A=Z_n` as a direct unique sum. To cover residue6, its T-element must be one of `6,3,−2,−5`. Each would collide with a DIFFERENT mandatory tail in Y:

    6+3=1+8,   3+0=0+3,
    −2+3=1+0,  −5+8=0+3.                                  (2)

All entries of A are genuine old heads, and 0,1 are genuine old tails. For n>=26 the candidate residues are distinct from their conflicting anchors. Therefore residue6 cannot be covered in a direct sum. This argument needs only the old tails0,1, but all of Y is retained for the next proof.

Second, NO set U containing A can have `U+Y=Z_n` as a direct unique sum. To cover residue2, its U-element must be one of `2,1,−5,−11,−12`. Each collides with a DIFFERENT mandatory head in A:

    2+1=3+0,    1+0=0+1,
    −5+13=8+0,  −11+14=3+0,  −12+13=0+1.                 (3)

Again the identities are exact modulo EVERY n>=26 and the relevant candidate and anchor residues differ. Thus residue2 cannot be covered. These are logical universal impossibilities, not claims about a numerically chosen cyclic tiler.

## 4. No row can attain n/4

For any row J_i, the map `J_i×A -> Z_n`, `(j,a)->j+a`, is injective: a duplicate sum gives two distinct ACTUAL two-B-list parses with equal outer residues and equal seam. Hence `4|J_i|<=n`.

Suppose equality holds for some actual row u, and set `J=J_u`, `|J|=n/4`. In the product `W J_u W` (the middle J indexed by seam u), all four original tail-zero atoms followed by all row-u atoms give `4|J|=n` distinct paths. Since the whole product has exactly n paths and is zero-one, they exhaust it. Its endpoint matrix is the FULL rectangle

    Q=A × J.                                                (4)

Choose any actual t in J. Consider `P=Q J_t W`, itself a three-B-word path matrix. For each B atom with head r satisfying `t−r in J`, there is one qualifying Q tail and FOUR possible Q initial heads in A. If two qualifying B-atoms shared a final tail, P would have two paths with the same endpoints, contradicting UD. Therefore these atoms' tails form a set T, and the exact n-entry count of P gives `|T|=n/4` and

    P=A × T.                                                (5)

Every original row0 atom `(0,y)`, y in Y, qualifies because t−0=t in J, so `Y subset T`.

For EVERY seam gamma, the product `P J_gamma P` is a six-B-word path product, hence zero-one. If two pairs in T×A had the same sum gamma, fixing any initial head in A and any final tail in T would give two different P/P paths with the same endpoints. Thus T×A is injective. Its cardinality is n, so it is a direct tiling of Z_n. This contradicts(2). NO row can attain n/4.

The proof uses exact SAME-B products, not a purported arbitrary rectangle completion: Q and P are path products of the original W, and their entries represent unique actual lists. It also includes a saturated row with no original prefix label.

## 5. No column can attain n/5

Symmetrically, for any column I_j the map `I_j×Y -> Z_n` is injective by actual two-B paths using the old head-zero row. Hence `5|I_j|<=n`.

Suppose a column j has size n/5. Its n/5 B-atoms followed at seam j by the five original row0 atoms give n distinct paths. Thus the full path matrix is

    Q=I_j × Y.                                              (6)

Choose any h in I_j and consider `P=W J_h Q`. Each B atom with tail s satisfying h−s in I_j gives one qualifying Q head and FIVE possible final tails in Y. Zero-one paths force their initial heads to be distinct; n total entries give a set U of size n/5 and `P=U×Y`. Each original suffix-zero atom `(a,0)`, a in A, qualifies because h−0=h, so `A subset U`.

Every `P J_gamma P` is a zero-one six-B path product. Hence Y×U is injective; its cardinality is n, so U+Y tiles Z_n. This contradicts(3). NO column can attain n/5.

## 6. Original completion caller and strengthened head bound

For every finite UD factor-complete Shor extension, the raw proof in `frontier-20261028-prefix-layer-obstruction-v1.md`, SHA256 **ef0d973f52ece5365613a8280475e240992ab53d47bca55dd13ea62f573ab0dc**, gives the SAME actual pure-a atom a^n and |B|=n. Thus(1) is necessary at the FULL original quantifiers.

If 4|n, write q=n/4. The four old prefix rows each have at most q−1 atoms, so they contain at most n−4 of the n actual one-b atoms. At least FOUR atoms have new head residues. The earlier 2-adic argument gives the stronger bound8 when v_2(n)=3; the new argument gives4 when v_2(n)>=4 as well. For odd n or v_2(n)=1, the earlier3/2 bounds remain; no false global4 assertion is made.

The prior `frontier-20261028-unique-saturated-old-row-v1.md` and double-saturation packets are valid conditional derivations at their stated mathematical scope, but if this theorem is correct their saturated-row completion antecedents are impossible. They do NOT force the original completion to have such a row. The present theorem does not claim non-saturated branches are impossible.

## 7. Actual bounded independent checks

Executed:

    python3 -B frontier-20261028-rectangular-saturation-check.py 660

For every n=26,...,660, the checker verified all four target6 row-conflict equalities and all five target2 column-conflict equalities using exact residues. It also directly composed all seams of two SYNTHETIC full rectangular bayonet sets: order32 with A×canonical A-complement,1024 path endpoints, and order20 with a5-tail rectangle,400 endpoints. Both were stable zero-one positive controls. NEITHER synthetic rectangle contains the full original S. The all-order result is the written product/tiling proof in §§2–5, not a claim that finite sampling covers all n.

Checker `frontier-20261028-rectangular-saturation-check.py`, SHA256 **b7bf995f2f1ec0943e4058b1a0cbac67ee29f6e24792f019246c9fa4a7b32aa7**,63 LF /2121 B, natively pinned Wed Oct28 18:20:41 PDT.

## 8. Exact remaining gap and assurance

The result forces every actual one-b row/column strictly below the maximal A/Y packing bound and gives at least4 new-head atoms whenever4|n. It does not prove that all such nonsaturated layers violate a longer path or cannot support a complete raw code. Nor does it prove an alleged complete D exists. Full all-order noncompletion versus an explicit finite UD complete supercode remains the original unresolved target.

These statements are written/finite-checked but unreviewed, not kernel/formal/human/configured-family or novelty accepted. Earlier historical source/episode records are not accepted as premises. The proof uses literal old S, actual word equality, finite one-b path conservation and elementary cyclic arithmetic only.

**END OF GLOBAL NO-SATURATION CANDIDATE.**
