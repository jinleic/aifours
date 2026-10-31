# Shor completion: two compulsory new prefix atoms and a three-boundary obstruction

Owner **MathShor-2**, math-5. Native prewrite clock **Wed Oct 28 17:06:49 PDT 2026**.
**All-order mathematical candidate; exact finite experiments separately identified. Not independently reviewed or novelty-cleared.**

## 1. Original problem and main conclusions

Let

    S = b{1,a,a^7,a^13,a^14}
        union {a^3,a^8}b{1,a^2,a^4,a^6}
        union a^11b{1,a,a^2}.

A code is uniquely decipherable (UD) when distinct ordered atom lists have distinct concatenations. It is factor-complete when every binary word is a contiguous factor of some word in D*. The original question is whether ANY finite UD factor-complete D contains this actual 16-word S, or whether ALL such finite extensions are impossible.

**Theorem A — compulsory new prefixes.** For every such hypothetical D, there is one pure-a atom a^n, necessarily n>=26. Let B be ALL of its one-b atoms. Then |B|=n and there are at least TWO atoms `a^i b a^j` in B with

    i mod n not in {0,3,8,11}.

If n is odd there are at least THREE such atoms. Thus every hypothetical completion must introduce genuinely new one-b PREFIX RESIDUES; it cannot fill the whole obligatory one-b layer merely by adding suffixes to the four original prefix rows. This assertion concerns the SAME actual D, not an abstract tiling alone.

**Theorem B — 400 individually invisible two-boundary traps.** For every n>=37, there are 400 explicitly described residue pairs (i,j) such that adjoining a one-b atom of that pair to S and a^n passes the full two-atom endpoint/residue collision test, yet is NOT UD: an exact three-one-b-word ambiguity, with legal pure-a padding where needed, exists. The actual example `a b a^3` already has an unpadded ambiguity for every n. Thus a two-boundary admissibility test cannot substitute for all-list UD even on the literal original code.

Neither theorem exhibits a finite completion or excludes all finite D. No claim that an actual D exists, that its forced new atoms lie in the 400 forbidden pairs, or that 400 is the full forbidden set follows. Novelty and all stronger formal/human/kernel/independent-model gates remain unestablished.

## 2. Literal data and a raw two-boundary lemma

Write the old one-b pairs as

    A={0,3,8,11},
    Y_0={0,1,7,13,14},
    Y_3=Y_8={0,2,4,6},  Y_11={0,1,2}.

For one fixed n, and an actual one-b subcode B, denote the endpoint residues of an atom by `(i mod n,j mod n)`. Assume D contains a^n. Two distinct atoms cannot share BOTH residues: pad their two ends by nonnegative a^n words to make the raw words equal.

More generally, two different ordered lists of two B-atoms with the same triple

    (first prefix residue, internal (suffix+prefix) residue,
     final suffix residue)

produce equal raw words after inserting nonnegative a^n atoms at the outer and internal boundaries. Equalize each congruent a-run independently by taking the larger of its two lengths. The two ordered lists of D-atoms are distinct, so this is an actual UD violation. This lemma uses the actual word lists, not a real/factorization relaxation.

Let Δrow be all nonzero suffix differences occurring within one prefix row, and Δcol all nonzero prefix differences occurring within one suffix column, modulo n. Assuming unique endpoint pairs, two-list residue uniqueness is equivalent to `Δrow intersect Δcol=empty`: a collision has a common first row and common second column and requires the corresponding two differences to coincide; conversely equal nonzero differences give such a collision. The use of both signs is implicit in these difference sets.

## 3. Derive n>=26 directly, without an old FACT import

The old rows realize every positive suffix difference in

    D={1,2,4,6,7,12,13,14}.

The old suffix-zero column contains the four heads A and realizes every positive prefix difference in

    E={3,5,8,11}.

If n divides d+e for d in D,e in E, choose an old row with tails p,q such that p-q=d, and choose v,w in A with v-w=e. All four participating atoms are in S. Since `p+v=q+w+(d+e)`, the actual equality

    (a^t b a^p)(a^v b)
      = (a^t b a^q)(a^n)^((d+e)/n)(a^w b)

is a pair of distinct D-parses. Therefore no UD D containing S and a^n can have such n.

The set D+E contains EVERY integer from4 through25 except8: its four e-rows are

    e=3:  4,5,7,9,10,15,16,17
    e=5:  6,7,9,11,12,17,18,19
    e=8:  9,10,12,14,15,20,21,22
    e=11: 12,13,15,17,18,23,24,25.

Orders1,2 divide4; order3 divides6; order8 divides16. Every n in1..25 therefore has an actual ambiguity. Consequently every UD D containing S and a^n has n>=26. This is an elementary necessary bound, not the inherited stronger FACT/660 claim.

## 4. Reconstruct the SAME-completion one-b count

For a finite complete D, a pure-a atom exists: if every atom contains b, a sufficiently long all-a factor cannot fit inside a single atom or cross more than one atom boundary. Two different pure-a atoms commute and contradict UD, so the unique one is a^n.

Let k=|B|, and W be its n-by-n zero-one incidence matrix of unique endpoint pairs. For every internal residue word, ordinary integer products `W J_gamma1 W ... J_gamma W` count actual lists by endpoint pair; the raw two/list padding argument makes every entry zero or one. The family of these products is finite and closed under joining two products with a seam J_gamma. Let a maximum product have K entries. The n joined products have at most K entries each, whereas their total number of entries is K² because `sum_gamma J_gamma` is the all-one matrix. Thus K²<=nK and k<=K<=n.

Conversely, let L be the maximum atom length. For every m and every prescribed sequence of m−1 residues, choose raw internal a-gaps above2L with those residues and put a guard of L a's before the first b and after the last. Factor-completeness embeds that raw word into D*. The guards and gaps force every displayed b to belong to its own one-b B-atom, and any atoms between consecutive such atoms are pure-a atoms a^n. Thus every internal residue sequence is realized by some actual B-list. Hence `k^m>=n^(m-1)` for every m; if k<n this fails for sufficiently large m. Therefore **k=n**. All arguments are on one D, and multi-b D-atoms are not discarded as possible other atoms.

## 5. A packing lemma and four forced missing residues

For each prefix residue i let

    J_i={j mod n : a^u b a^v in B, u==i, v==j mod n}.

The four ORIGINAL atoms `a^v b`, v in A, have common final suffix0. For every row i the map

    J_i × A -> Z_n,  (j,v) -> j+v

is injective: a repeated sum would give two different actual two-B lists with identical endpoint/internal residues, violating §2. Thus

    4|J_i|=|J_i+A|<=n                                         (P)

for EVERY row. Since n>=26, the original four prefix residues in A are distinct.

There is a stricter bound for rows0 and11. Row0 already contains Y_0; row11 contains {0,1,2}. In each case the following sums are IMPOSSIBLE to cover by `J_i+A`:

    row 0: 6 and 19;          row 11: 6 and 7.

Here is an explicit finite certificate, valid modulo EVERY n>=26. To cover target t, the only possible new tail j is t-v for v in A. Each listed j is forbidden because it collides under +A with a DIFFERENT already-present row tail. A dash indicates a negative integer interpreted modulo n; n>=26 keeps every displayed candidate distinct from the indicated anchor.

| row | t | possible j=t−A | conflicting anchor in the SAME row | equality of sums with A |
|---|---:|---|---|---|
| 0 or 11 | 6 | 6, 3, −2, −5 | 1, 0, 1, 0 | 6+3=1+8; 3+0=0+3; −2+3=1+0; −5+8=0+3 |
| 0 | 19 | 19, 16, 11, 8 | 14, 13, 0, 0 | 19+3=14+8; 16+0=13+3; 11+0=0+11; 8+0=0+8 |
| 11 | 7 | 7, 4, −1, −4 | 2, 1, 2, 1 | 7+3=2+8; 4+0=1+3; −1+3=2+0; −4+8=1+3 |

Each equality violates injectivity of (P) if both candidate and anchor belong to that row. The two targets within a row are distinct modulo n, so

    |J_0|, |J_11| <= floor((n−2)/4),
    |J_3|, |J_8|   <= floor(n/4).

The total number of actual one-b atoms is n by §4. Consequently the number whose prefix residue lies OUTSIDE A is at least

    n − 2 floor((n−2)/4) − 2 floor(n/4)
      = 2 when n is even, and 3 when n is odd.

This proves Theorem A for ALL n and ALL finite D satisfying the original definitions. It rules out an entire family of proposed completions, but does not decide whether a larger-prefix D exists.

## 6. Exact three-boundary forbidden rectangle

Put

    Δ={±1,±2,±4,±6,±7,±12,±13,±14},
    T=Y_0+(A−A),
    A−A={0,±3,±5,±8,±11}.

Every member of Δ is a difference p−q of two old tails in one SAME old row t. Let c=a^i b a^s be a proposed additional atom with i mod n in Δ and s mod n in T. Choose p,q in the same old row, j in Y_0 and v,w in A satisfying

    i == p−q (mod n),     s == j+v−w (mod n).

Compare the actual three-one-b lists

    (a^t b a^p), (b a^j), (a^v b)
    (a^t b a^q), (a^i b a^s), (a^w b).

Their two internal a-runs have congruent lengths: p versus q+i, and j+v versus s+w. Insert copies of the actual atom a^n at EACH boundary independently until these lengths match. Their outside runs already match. For n>=26, Δ does not meet the four old prefix residues A, so c is not one of the old atoms; the two lists are distinct. Thus **NO UD D containing S and a^n can include c**, regardless of any other atoms or completeness.

For n>=37, all 16 residues in Δ are distinct. The 33 integer offsets in T are

    −11,−10,−8,−7,−5,−4,−3,−2,−1,
    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,
    21,22,24,25.

They remain distinct modulo n. The full old suffix set is `J_old={0,1,2,4,6,7,13,14}`, all contained in T, leaving 25 residues of T outside the old columns. Thus there are exactly `16*25=400` pairs in Δ×(T\J_old).

For EVERY n>=37, all these pairs use a new prefix row and a new suffix column. The original same-row differences have positive parts D in §3, and the original same-column differences have positive parts E. Their signed sets are disjoint modulo every n>=26: same-sign equality would require an equal integer in D and E, and opposite-sign equality would require n<=14+11=25. Adding one atom in a new row AND new column introduces no within-row or within-column difference. Hence each of the 400 individual additions passes the full m=2 residue-key uniqueness test, yet the three-list construction above rejects it.

A direct unpadded example, independent of n, is

    (b a)(b)(a^3 b) = (b)(a b a^3)(b) = b a b a^3 b.

All atoms except `a b a^3` are in the ORIGINAL S. The candidate is outside the old row and column sets, so for n>=37 it passes the stated two-boundary filter; the displayed equality proves it cannot be added to ANY UD supercode of S. This is a concrete failed implication on the original problem's own code, not a small-code analogy.

## 7. Exact bounded independent checks and reproducibility

The following are scientific executions performed now under the 2026-10-28 owner direction. They are exact finite checks, NOT substitutes for the all-order arguments above, formal verification, exhaustive completion search or novelty review.

1. `python3 -B frontier-20261028-boundary-probe.py 660 20`: ordinary Sardinas–Patterson residual search with validated actual equal-word certificates. Output: base `S union {a^660}` UD;425 distinct proposed additions in the0..20 squared grid;150 two-boundary collisions; of the275 two-boundary-clear additions,206 rejected by full SP and69 UD. Eight printed rejected witnesses were explicitly checked as equal concatenations. These69 one-atom extensions are NOT claimed complete. This is only one chosen finite order and bounded grid.
2. `python3 -B frontier-20261028-three-boundary-check.py 660`: separate independent direct word-concatenation/two-key checker, constructed from the product spelling of S. It checked all400 claimed new-row/new-column residue pairs, each passing m=2 keys and each having a raw three-atom ambiguity after a^660 padding. It reported16 head residues,33 total forbidden tail residues,25 outside old columns, and400 exact checked witnesses. The displayed `a b a^3` witness has zero pads.
3. `python3 -B frontier-20261028-prefix-layer-check.py 660`: independent finite checker emitted explicit actual-word ambiguity certificates for all25 orders1..25 and checked all four row-hole claims for every n=26..660. The symbolic equalities in §§3–5—not this finite interval—supply the all-order inference.
4. Separately, exact Python integer set calculation returned D, E and the33 offsets of T listed above; no floating point was used. Sardinas–Patterson was also run on each n in1..100, finding UD for `S union {a^n}` exactly for n=26..100 in that bounded interval. No claim is made for other n based solely on this run.

Live source pins at native Wed Oct28 17:06:49 PDT:

| Source | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-boundary-probe.py` | f3ca1eb7e0ca9ceb4468b147d32cdd592b57f45798c9f5e934cfbc1f14c2804b |126 /4560 |
| `frontier-20261028-three-boundary-check.py` | 428ba99815a1281a84c110c598e2c29216b79e870221bd0cbd1d840a677e683a |94 /3942 |
| `frontier-20261028-prefix-layer-check.py` | 20a3dfa47db2f6262d8735a49cce1329cc8a06d7f1b9b738cd1e9f16b143710b |77 /3165 |

## 8. Exact unresolved bridge and next work

Theorem A forces at least2 new one-b atoms outside the original four prefix residues (at least3 for odd n). Theorem B rules out a sizeable explicit class of such atoms and demonstrates that two-boundary checking alone accepts false candidates. The missing original-target bridge is whether EVERY way to place ALL required new one-b atoms and all multi-b atoms either leads to an actual ambiguity or fails factor-completeness; the present arguments DO NOT establish that bridge. Conversely, a positive answer needs a concrete finite D with independently verified full UD and factor-universality, not merely a residue solution or 69 locally UD additions.

Inputs: supplied literal book-transcription packet and independently reconstructed raw UD/factor-completeness arguments in this file. The earlier recorded selected-control/unprinted-continuation and parent source/program events remain historical process findings; none is treated as validated science merely by the new direction. No use of their held outcome as a premise is claimed. This new written candidate and finite checker outputs have not received a peer or parent mathematical disposition.

**END OF FRONTIER CANDIDATE.**
