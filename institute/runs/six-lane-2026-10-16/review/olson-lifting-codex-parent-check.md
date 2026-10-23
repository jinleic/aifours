# Parent check of Codex Olson lifting note

Input: `olson-lifting-codex.note.md`, returned by Codex `gpt-6.1-sol` at maximum effort from an empty read-only directory after 646 seconds. Receipt: `olson-lifting-codex.receipt.json`. Status: independent unverified input, not a proof review.

## Read and checked by hand

The parent checked the note's elementary universal bound line by line:

- Words avoiding an ordered n-term identity subword contain each element at most n−1 times.
- For an element g of order d>2, selected copies of g and g⁻¹ commute. If their combined count is at least n+δ−1, where δ=d/gcd(d,2), an integer interval of k-values contains a multiple of δ; choosing k copies of g and n−k copies of g⁻¹ gives g^(2k−n)=1 because d divides n. Thus their count is at most n+δ−2.
- Elements are partitioned by generated cyclic subgroup. For a cyclic subgroup of order d, all entries generating it lie in that abelian subgroup; the standard cyclic N+d−1 lemma bounds them by n+d−2. For phi(d)≥4 this is at most ((n−1)/2)phi(d); orders 3, 4 and 6 use the separate g/g⁻¹ bound.
- For even n=2k with t elements satisfying g²=1, more than kt entries from that set give an ordered identity n-term subword: identities supply an even part, and successive windows of length t among nonidentity involutions each contain an equal pair. Pairs in different windows have separated supports, so their concatenation preserves original order.
- For odd n, order-three classes are bounded by n+1 without identities and by n−1 when at least one identity occurs, using the three residue cases written in the note.

Resulting bound:

- n odd: z(G) ≤ (n²+1)/2;
- n even: z(G) ≤ (n(n+1)−t)/2+1 ≤ n(n+1)/2.

This is correct on the parent read, but it is only a factor-two improvement of the trivial n(n−1)+1 bound. It is quadratic, does not approach the 2n−1 conjecture, and has unknown novelty. It is not promoted as a breakthrough.

## Lemma obstructions checked

- In S3, the alternating length-11 word shows that five separated quotient-identity pairs need not exist, while the word still has an ordered identity subword.
- In S3, interleaved blocks `(rs, s, rs, s, 1, 1)` have block products 1 but original-order union product r².
- In D8 with central H=⟨r²⟩, interleaved blocks `(r,s,r⁻¹,s,1,1,1,1)` have block products 1 but full product r².

These falsify proposed proof lemmas, not Olson's conjecture.
