# Exact cardinality and short normal form of the free seminormal band

**Status: NEW AUTHOR WRITTEN GENERAL THEOREM plus exact finite replay; UNREVIEWED / UNADOPTED.** This strengthens the bound-only statement in `frontier-20261029-seminormal-paired-signature-model-v1.md`, SHA `ea44a79d83bdaf7e129bb9c8c40ee3b908362339aa9669994de46fc16f8d8b44`, with a complete count and canonical short representative. It does not prove canonical source mixed quotients faithful, and is not claimed novel.

## 1. Exact result

Let SN be the band variety `abcda=abcacda`. For a fixed k-letter content set, the number of free SN elements is

`c₁=1`,  `c_k=k²((k−1)!)⁴` for k≥2.

Therefore the free SN band on n generators has exactly

`F_SN(n)=Σ_(k=1)^n binom(n,k)c_k`.

Every element with k≥2 letters has a canonical representative of length at most4k−4; a one-letter element has length1. The first sizes are

`F_SN(1..6)=1, 6, 159, 21,340, 8,399,565, 7,515,040,386`.

Only n≤4 was actually enumerated in this run; the last two values are exact formula arithmetic, not enumeration results.

## 2. Boundary decomposition of the paired signature

The named predecessor proves a word's SN class is exactly its correlated pair of right/left recursive signatures. Write R(w) for its rightSN signature and `L(w)=R(reverse w)`. For a word w on a content set A with |A|=k≥2, let:

* d be the LAST new letter discovered scanning w left-to-right; s the prefix strictly before its FIRST occurrence. Then `content(s)=A\{d}`.
* c be the letter whose LAST occurrence is EARLIEST; e the suffix strictly after that last occurrence. Then `content(e)=A\{c}`.

Both s and e are nonempty. By definition

`R(w)=(head(s),c,R(e))`,
`L(w)=(last(e),d,L(s))`.

The head of s is determined by L(s): it is the last letter of reverse(s), which is recoverable by following the right signature's tail to its final one-letter node. Similarly last(e) is determined by R(e). Thus the ENTIRE paired signature is completely and injectively determined by the four independent data

`(c,d, R(e), L(s))`,                                    (D)

where c,d∈A, R(e) is a full-content rightSN signature on A\{c}, and L(s) a full-content leftSN signature on A\{d}.

## 3. Every four-tuple is realized

Choose arbitrary data(D). Use the one-sided canonical normal representatives from `frontier-20261029-right-seminormal-normal-form-v1.md`, SHA `c2a5f4d9de295deed8e28282b2456f6d274886856224dccd68208bae0c2fe6be`: choose s as the reverse of the right normal representative of L(s), and e as the right normal representative of R(e). Define

`N(D)=s d c e`.                                          (N)

The letter d is absent from s, but every other A-letter occurs in s. Hence d is the last newly encountered letter and the prefix before its first occurrence is exactly s. Likewise c is absent from e and every other letter occurs in e; the displayed c is the last c and is the earliest last occurrence of all A-letters. This remains correct when c=d, with the adjacent identical middle letters interpreted by the band law. Therefore N(D) has exactly the prescribed paired signatures, proving that every four-tuple occurs. Distinct tuples yield distinct paired signatures.

There are k choices each for c,d. Each of R(e),L(s) has `((k−1)!)²` possibilities by the complete one-sided theorem. Thus `c_k=k²((k−1)!)⁴`. Summing over content sets proves the total count. The two one-sided representatives each have length at most `2(k−1)−1`; with the two middle letters, (N) has length at most4k−4. The one-letter case is separate and has one state. □

This proof uses exactly the predecessor's universal paired-word characterization and one-sided normal form, not a new assumption that arbitrary independently chosen signature pairs are correlated. Correlation is enforced and counted precisely by the four-tuple(D).

## 4. Exact replay and algorithmic scope

`frontier-20261029-seminormal-count-normal-replay-v1.py`, SHA `1b141f5c39695ad84e402b188842253efaa9c9255e5e4a15113bafc39a809f90`, executed in the Python eval kernel before Thu Oct29 00:24:07 PDT2026. It independently constructs the complete correlated generator closure for n≤4, checks every short representative's two signatures and length, and verifies fixed-full-content counts1,4,144,20,736 as well as total counts1,6,159,21,340. It computes the n5,n6 formula values with integers only and explicitly does not enumerate those large sets.

The construction gives an exact finite SN free-word representation smaller than the unrestricted band, but at six symbols it already has7.5billion states. The one-sided rightSN6 canonical computation used only614,226 states; this quantitative difference matters and forbids labelling a full-SN source computation as performed when only one-sided words were enumerated. The matching original source R/L theorem remains open. All universal proofs and finite implementations are same-author unreviewed, nonformal and without novelty clearance.
