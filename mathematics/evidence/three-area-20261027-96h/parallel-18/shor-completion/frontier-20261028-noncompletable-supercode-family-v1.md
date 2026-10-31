# An explicit infinite family of finite noncompletable Shor supercodes

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 17:22:19 PDT 2026**.
**All-order written construction/obstruction, with bounded independent checks. Not yet reviewed, formalized or novelty-cleared.**

## 1. Precise result — a deliberate dead end, NOT a solution for S

Let S be the literal 16-word Shor code and let `n=16m`, m>=2. Define `A={0,3,8,11}` and

    J_3=J_8={0,2,4,6}+16{0,...,m−1},
    J_0={0,1,7,13,14,20,26}
        union ⋃_(k=0,...,m−3) {30,32,36,42}+16k,
    J_11={0,1,2,14,16,18,20}
        union ⋃_(k=0,...,m−3) {30,32,34,36}+16k.

An empty k-range is empty. All displayed tails lie in [0,n−1]. Define the ACTUAL finite set

    D_n={a^n} union {a^i b a^j : i in A, j in J_i},
    E_n=D_n union {b b a^2 b}.

**Theorem. For every m>=2:**
1. D_n is UD, contains the FULL original S, has exactly n−2 one-b words and n−1 total words, and the explicit word `b b a^2 b` is NOT a factor of D_n*.
2. No one-b word outside D_n can be adjoined to D_n while preserving UD. Consequently D_n has NO finite UD factor-complete supercode.
3. E_n is also UD: the missing factor `b b a^2 b` can genuinely be adjoined. Nonetheless E_n has NO finite UD factor-complete supercode, and `b a b a^2 b` is an explicit missing factor of E_n*.

This constructs infinitely many genuine finite UD NONFINITELY-COMPLETABLE supercodes OF S, including ones with an actual legal multi-b addition. It does NOT prove that S itself lacks a finite completion: a completion of S need not contain any of these additional one-b words. Nor does it prove these codes are maximal among all UD codes, assert an infinite-code result, or settle the original all-order question. A discovery/priority claim is not made.

## 2. Exact endpoint ingredients

Write every one-b atom as `a^i b a^j`. If a UD code contains a^n, its distinct one-b atoms have distinct residue pairs `(i,j) mod n`. More generally, two different m-one-b lists with equal initial prefix, final suffix and each internal `suffix+next-prefix` modulo n yield distinct equal raw parses by inserting nonnegative a^n words at the m+1 actual boundaries. No pad is inserted inside an atom.

For ANY finite factor-complete UD code containing S, there is a unique pure-a atom a^n and exactly n one-b atoms. The complete raw proof is in `frontier-20261028-prefix-layer-obstruction-v1.md`, SHA256 **ef0d973f52ece5365613a8280475e240992ab53d47bca55dd13ea62f573ab0dc**, §§3–4: pure-a existence follows from finite maximum length and arbitrary all-a factors; the upper bound uses finite zero-one endpoint-path products and the maximum-entry-count inequality; long guarded b-patterns supply the lower bound. Its actual-word proof is also summarized here: k one-b atoms yield k^m lists; completeness realizes all n^(m−1) internal residue strings, forcing k>=n, whereas the zero-one product maximum forces k<=n.

The old suffix-zero column contains actual a^v b for every v in A. Thus in ANY UD extension with this same a^n, a fixed prefix row J must satisfy injectivity of

    J × A -> Z_n,    (j,v) -> j+v.

A collision supplies an actual two-B-word ambiguity, not merely a failed group relaxation. In particular `4|J|<=n`.

## 3. Verify all four displayed rows and D_n's UD property

For rows3 and8, the 16 sums `A+{0,2,4,6}` are exactly all residues modulo16. Thus `A+J_3=A+J_8=Z_n` uniquely: reduce an equality modulo16 to identify the pair, then identify the 16-block modulo m. Both rows have n/4 tails.

Rows0 and11 each have `7+4(m−2)=n/4−1` tails. Their direct packings admit the following simple induction; raw sum sets below are ordinary integers before reduction modulo n.

**Base n=32.** Directly listing `A+J_0` gives distinct raw sums, missing from [0,31] exactly `{2,5,6,19,27,30}`, with the only raw overflow `{34,37}`. Modulo32 those two overflows fill2 and5. Directly listing `A+J_11` gives distinct raw sums in [0,31], missing exactly `{6,7,15,30}`. The base lists are the definitions in §1.

**Induction n -> n+16.** Row0 adds exactly `{n−2,n,n+4,n+10}`. The new sixteen raw sums relative to n are

    {−2,0,1,3,4,6,7,8,9,10,11,12,13,15,18,21}.

They are distinct, fill the old raw hole n−2, avoid its only old overflows n+2,n+5, cover the new block except n+2,n+5,n+14, and leave the new overflow n+18,n+21. Hence the raw-integer invariant becomes holes `{2,5,6,19,27,n+14}` and overflow `{n+18,n+21}`. Modulo n+16, exactly `{6,19,27,n+14}` remain missing.

Row11 adds `{n−2,n,n+2,n+4}`. Its sixteen new raw sums relative to n are

    {−2,0,1,2,3,4,5,6,7,8,9,10,11,12,13,15}.

They fill the old hole n−2 and all the new block except n+14, with no overflow. Thus its missing residues are `{6,7,15,n+14}`. This proves BOTH row packings, no overlapping pairs, and their four-hole counts for every m>=2.

Now compare any two raw parses using D_n. They have the same number of b's. If that number is zero, they use only a^n and agree. Otherwise their first prefix residues determine the SAME row in A. At each interior b-to-b gap, equality modulo n and injectivity of that row's `J_i×A` identify both the preceding suffix and next prefix; inductively all one-b atoms are identical. The last suffix follows from the final run modulo n. Actual a-run equality then forces the same count of a^n pads in every boundary interval. Therefore the ordered lists coincide: **D_n is UD**.

All mandatory old pairs are present: Y_0={0,1,7,13,14}, Y_3=Y_8={0,2,4,6}, Y_11={0,1,2}. The row sizes sum to n−2. Every word has at most one b except no word has more than one b in D_n itself.

## 4. Every extra one-b atom is impossible

### 4A. Existing prefix rows

For a putative new one-b atom, if its endpoint pair already occurs modulo n, pure-a endpoint padding gives an ambiguity with that existing atom. Otherwise, adding a new tail to row3 or8 would give n/4+1 tails, contradicting `4|J|<=n`.

For row0, targets6 and19 are impossible in J_0+A in EVERY UD supercode retaining the old anchors; for row11, targets6 and7 are likewise impossible. These follow from the explicit four-choice table in the preceding candidate, §5: for each target every possible new tail collides with a DIFFERENT already-present anchor under +A. The present row has n/4−1 tails. One extra tail would create n distinct sums, but the two targets remain missing, impossible. This includes arbitrary actual exponents in the same residue row, not just tails already between0 and n−1.

### 4B. Every new prefix row — an all-order THREE-word certificate

Let c=a^i b a^s be any proposed one-b atom with prefix residue r=i mod n outside A. For each such r there is a choice `u in {3,8}` and two existing tails p,q in one SAME existing row t with

    r−u == p−q (mod n).                                     (2)

To verify this constructively, J_3−J_3 contains EVERY even residue whose class mod16 is not8: differences of {0,2,4,6} cover the seven even classes0,±2,±4,±6 and the 16-block difference ranges over Z_m.

- If r is even and r not congruent0 mod16, take u=8; r−8 has one of those even classes.
- If r is odd and r not congruent11 mod16, take u=3; r−3 has one of those even classes.
- If r=16h with 1<=h<=m−1, take u=3 and use row0 tails `p=14+16(h−1)`, `q=1`; then p−q=r−3. All these p occur in J_0.
- If r=11+16h with 1<=h<=m−1, take u=8 and use row0 tails `p=1`, `q=14+16(m−1−h)`; then p−q==r−8 mod n. These are all valid J_0 tails.

The excluded h=0 cases are the old prefix residues0 and11, not unhandled new rows. Thus (2) holds for EVERY r outside A.

Since J_u+A tiles Z_n for u=3 or8, choose actual j in J_u and v in A with `j+v==s (mod n)`. The following ACTUAL one-b lists have congruent corresponding interior a-runs:

    (a^t b a^p), (a^u b a^j), (a^v b)
    (a^t b a^q), (a^i b a^s), (b).

The first seams agree by (2), the second by the tiling choice, and both outer runs already agree. Insert a^n atoms at the two seams to raise each pair of congruent lengths to its larger value. This produces two distinct equal raw words. The proposed c occurs on only the second side because its prefix residue is not in A. Consequently EVERY one-b addition in any new row violates UD.

Combining 4A and 4B, NO new one-b atom can be added to D_n. Any finite complete UD supercode would have the same unique pure-a atom a^n but exactly n one-b atoms (§2), while D_n already has n−2 and cannot gain even one. Hence no such finite supercode exists. This argument remains valid after adding arbitrary multi-b atoms: an old raw ambiguity cannot be repaired by enlarging a code.

## 5. Explicit missing factor AND a legal multi-b addition

Put w=`b b a^2 b`. In D_n* the first two consecutive b's of w must lie in two different one-b atoms. Their intervening a-gap is0, so the second atom has prefix0. The next b is separated from it by exactly two a's; since n>=32 no pure-a atom fits that gap. Row0 has no suffix2, and the only row0 tails below2 are0 and1; the next one-b head would have to be2 or1, neither in A. Thus **w is not a factor of D_n***.

Despite that, `E_n=D_n union {w}` is UD for ALL n in the family. Its short proof uses actual overlaps, not a guessed Sardinas–Patterson limit. The word w has exactly one nonempty proper border, the one-letter word b; two copies can overlap only in that single b.

Suppose two E_n parses of one raw word contain a w-atom, and consider the earliest starting w-atom among BOTH parses, starting at position t. If the other parse has no w-atom intersecting this copy, the entire w occurs inside a D_n* segment, contradicting the previous paragraph. Because no w-atom in either parse starts before t, the only possible unmatched intersecting copy in the other parse starts at t+4, at the final b of w.

But immediately before such a t+4 atom, that other parse has a D_n* prefix whose final four relevant letters are `b b a^2`. The first two b's belong to different D_n one-b atoms; the second has prefix0. With no a^n fitting inside two a's, ending the prefix at the next w-atom would require its actual row0 suffix to be exactly2, which J_0 does not contain. Contradiction. Therefore the earliest w-atom in both parses starts at t. The preceding D_n* prefixes are equal and D_n is UD, so their atom lists agree; remove that prefix and the common w-atom and repeat. All atom lists agree. This proves E_n UD, including arbitrary repetitions/overlaps of w.

The word g=`b a b a^2 b` is a factor missing from E_n*: its middle b cannot lie in w, because a w-b in its first, second or third position would force respectively a b after it, a b immediately before it, or two a's immediately before it, contradicting the displayed letters of g. Thus the middle b lies in a one-b atom; the preceding one-a gap forces its head0. The next two-a gap again cannot be split using a^n and cannot be written as a row0 suffix0 or1 plus a permitted next head (or the zero head of a w-atom). Hence no such factor exists. This supplies an explicit finite witness that even the legal multi-b insertion does not complete E_n; no shortest-factor claim is needed in the all-order proof.

## 6. Independently executed finite checks

1. `python3 -B frontier-20261028-dead-end-family-check.py 128` ran for n=32,48,64,80,96,112,128. A standalone Sardinas–Patterson set recurrence confirmed each D_n UD; each literal S inclusion and exact n−2 one-b count were checked. Independently constructed actual equal-word witnesses rejected EVERY canonical new-prefix residue pair: respectively896,2112,3840,6080,8832,12096,15872 witnesses. Old prefix saturation was checked by the exact row-packing holes. The all-n proof is §§3–4, not the finite run.
2. `python3 -B frontier-20261028-escape-factor-check.py 128` uses a separate trie/epsilon/subset automaton for factors of D_n*: all trie nodes are initial/final because each is accessible and can complete to the root. For each of the seven n values it reported `bbaab` as a shortest missing factor,17 subset states explored, D_n UD and D_n union {bbaab} UD by a separately implemented SP recurrence. The all-n claims are proved in §5; shortestness is reported ONLY for these checked orders.
3. A separate bounded SP check found `babaab` as a shortest missing factor after adjoining `bbaab` for n=32,48,64,80, and the all-order nonfactor claim for g is separately proved above. These computations are finite scientific evidence, not formal proof or an exhaustive search for all completions.

Live checker pins, native prewrite Wed Oct28 17:22:19 PDT:

| Checker | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-dead-end-family-check.py` | 95206d863b14638c53e1f87e575ccb1c5e292b965cbdb5ecd0495d5d27dc6bff |133 /4954 |
| `frontier-20261028-escape-factor-check.py` | 0284a27a46888da4e100798b36a2e3309bad026f2498cb5ac6ced6a86374b585 |110 /3812 |

## 7. Original gap and assurance

The construction is an explicit unconditional obstruction to a natural route: starting from S and making the displayed legal additions can trap the search in a finite UD code with NO finite complete extension, even after another legal missing-factor insertion. It does not establish that every possible completion must contain D_n or E_n. The actual original witness-or-universal-noncompletion question remains open at this packet's scope.

All reasoning is written and uses raw code definitions, finite word comparison, the earlier independently reconstructed one-b count, and elementary modular arithmetic. Finite SP/automaton checks are honestly scoped. Historical process/quarantine records remain historical and are not presented as prior proof; no external model, novelty authentication, publication or formal/human/kernel gate was performed.

**END OF NONCOMPLETABLE SUPERCODE FAMILY.**
