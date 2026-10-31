# Dihedral frontier — exact reflection-only count and a full-word double-extreme obstruction

Owner **MathOlson-2-2**, original math-2. Actual native `/bin/date` before writing: **Wed Oct 28 17:14:36 PDT 2026**.
Status: written all-variable candidate with bounded independent checks; not an original avoiding word, final theorem acceptance or novelty claim.

## 1. Original-order scope

Let p be any ODD prime, and write `D_(2p)=<r,s | r^p=s²=1, srs=r^−1>`. The original problem is to select exactly2p actual indices in increasing order with identity product from every actual word of length4p−1.
The following results test TWO specific construction modes. Their failure is NOT failure of the original problem.

## 2. Exact count of failing reflection-only words

Consider ANY ordered sequence of exactly `N=2p+1` actual reflections `r^(y_j)s`, with y_j∈F_p. For each j, let E_j be the exponent of the ORIGINAL-order product of the2p reflections obtained by omitting occurrence j.
Set `A_i=(-1)^(i−1)y_i`. Then

`E_j = ∑_(i<j) A_i − ∑_(i>j) A_i`,
`E_(j+1)−E_j = A_j+A_(j+1)=(-1)^(j−1)(y_j−y_(j+1))`.    (1)

These identities follow directly from the alternating sign of the actual reflection product; no permutation of occurrences is allowed.

**Theorem A.** Among all p^(2p+1) ordered reflection-exponent words, the number with NO identity product after omitting one occurrence is exactly

`(p−1)^(2p+1) − (p−1)`.

**Proof.** The linear map y↦E has kernel exactly the constant words: if every E_j=0, (1) gives y_j=y_(j+1) for every j; a constant word indeed has each even-length reflection product1.
Hence its rank is N−1. Its image lies in the hyperplane

`∑_(j=1..N)(−1)^(j−1) E_j=0`:                         (2)

for each input coordinate i, its coefficient in this sum is `(-1)^(i−1)[∑_(j>i)(−1)^(j−1)−∑_(j<i)(−1)^(j−1)]`, which is0 because N is odd. This hyperplane has dimension N−1, so the image is EXACTLY it, with p preimages per E-vector.

For all E_j nonzero, set `b_j=(-1)^(j−1)E_j`. Multiplication by the signs is a bijection on F_p^× and (2) becomes `∑b_j=0`.
Let A_N be the number of N-tuples of nonzero F_p elements summing to0. Scaling shows that each nonzero target has the same number B_N of tuples, so `A_N+(p−1)B_N=(p−1)^N`.
Appending a nonzero element gives `A_(N+1)=(p−1)B_N=(p−1)^N−A_N`, with A_1=0. Induction gives

`A_N=[(p−1)^N+(p−1)(−1)^N]/p`.

N=2p+1 is odd; multiplying by the p preimages proves the formula. ∎

The formula counts only failure of the **reflection-only omit-one mode**. It is not the number of full original D_(2p) avoiding words, nor a probability of any group-theoretic conjecture failing.

## 3. A fully explicit ALL-prime family defeating BOTH extreme modes

Let p≥5 be any prime, and a∈F_p^× ANY nonzero value. Take the ACTUAL full-length word

`w = s^(2p−1), r^a s, r^(2a)s, (r^a)^(2p−3), r^(2a)`.

Powers in this display denote separately labelled repeated occurrences. It has F=2p+1 reflections and R=2p−2 rotations, all rotation exponents nonzero, hence exactly4p−1 original positions.

**Claim B1 — no2p reflection-only selector.** If a zero-labelled reflection is omitted, or the final `r^(2a)s` is omitted, the ordered exponent is `−a`. If `r^a s` is omitted it is `−2a`. Both are nonzero for odd p.

**Claim B2 — no all-rotations-plus-two-reflections selector.** All rotations lie AFTER all reflections and their total exponent is

`[(2p−3)+2]a=(2p−1)a=−a`.

For ANY increasing pair of reflection positions, the ordered potential difference `y_j−y_i` belongs to `{0,a,2a}` because their exponents are ordered as `0,…,0,a,2a`.
For p≥5 the target `−a` is not any of these values. Hence the actual product cannot be1.

Thus both extreme modes fail simultaneously in the ORIGINAL count band `R=2p−2,F=2p+1`, not merely on a shortened or rearranged word.
The p=3 boundary is excluded from B2: there `−a=2a`, so the two-reflection mode can succeed. No extrapolation across that boundary is made.

**Crucial original-selector control.** The word itself IS NOT avoiding. Select the first p+1 copies of s (an even number), then p−2 copies of r^a and the final r^(2a). This is exactly

`(p+1)+(p−1)=2p`

actual increasing indices, and their product is `1·r^(pa)=1`.
Thus every solution on this particular word must use an interior even reflection count rather than either tested extreme, and one such interior selector is supplied. This is not a group counterexample or a proof that every word has an interior selector.

## 4. Uniform sufficient reflection-only word class

For an arbitrary actual sequence of2p+1 reflections, recurrence (1) gives its actual omission-exponent walk E_1,…,E_(2p+1).
If for some j there is a stretch of p−1 consecutive increments all equal to the SAME nonzero δ∈F_p, the p successive E-values in that stretch cover F_p, hence one is0. Omitting its actual occurrence gives exactly2p reflections in original order with identity product.

In particular, if the reflection subsequence contains p CONSECUTIVE reflection occurrences alternating between two distinct exponents, their signed consecutive increments are one common nonzero value. If the original word has at least2p+1 reflections, include this block and any additional reflections outside it to form a2p+1-reflection subsequence; the block remains consecutive in that selected reflection order. The criterion then gives an original-order2p-reflection selector, independently of all intervening rotations.
This is a proper all-prime WORD class, not a claim that every word in the full count band has such an alternating block.

## 5. Exact bounded evidence and independent checks

Reflection-only assay:
- producer `frontier-20261028-reflection-omission-experiment.py`, SHA256 `0fddaa6c9e2440a15c98c765ccf7c24ae2570ed8b834316c3106163d3c3aabe0`;
- independent recurrence/direct-product checker `frontier-20261028-reflection-omission-checker.py`, SHA256 `aa640ea8069e4bfb2c8c846a343ceae7e3c352c0fafd26b78079464d0944f704`;
- saved result `frontier-20261028-reflection-omission-results.json`, SHA256 `5ed093a09bec37a41965b70eede8cb3e33c748adfbc82765d3fb464e46066516`.

The producer exhaustively checked ALL `3^7=2187` p=3 exponent words: exactly126 had no identity omission, matching `(3−1)^7−(3−1)=126`. For p=5 and p=7 it sampled5000 words each, finding441 and539 respectively without an identity omission; these are SAMPLE counts, not exhaustive formulas.
The independent checker imported no producer code, recomputed the omission recurrence and direct original products, replayed seed2026102803 and returned `PASS_BOUNDED_OMISSION_RECOUNT` for12187 actual sequences.

Full-word double-extreme assay:
- producer `frontier-20261028-dihedral-double-extreme-experiment.py`, SHA256 `e6d6ec7574fdcf61548d0161485d0639f9cb5bb77c85c1775605bff85b3d4d9e`;
- independent checker `frontier-20261028-dihedral-double-extreme-checker.py`, SHA256 `d84470fd616ff0cfc66bbd4d627faaad463bc96f57dc970fcaa9f75b294dbf6a`;
- saved actual words and indices `frontier-20261028-dihedral-double-extreme-results.json`, SHA256 `72ac419b2fe750d29d22494354a22cb8f167e09463683b71a97a2a3cb7489eb4`.

Both programs checked p=3,5,7,11,13. For p≥5 they found zero identity choices in BOTH specified extreme modes, and independently verified the actual interior selector. The p=3 boundary control found5 all-rotation/two-reflection selectors, confirming why that case is excluded from Claim B2. The independent checker returned `PASS_INDEPENDENT_FULL_WORD_CHECK` on the saved result hash.

These finite computations validate only the stated bounded checks; the uniform claims are the explicit proofs above. They do NOT establish novelty, all-word coverage, a full group counterexample or stronger human/formal acceptance.

## 6. Immediate frontier

The two extreme mechanisms cannot alone resolve the full R=2p−2 class: the all-prime family above forces an interior mixture even though it still has a correct original selector.
The exact omission-walk hyperplane/count supplies a genuinely complete invariant for the reflection-only mode, but does not control mixed selections.
The next mathematical requirement is a uniform actual-value/order argument for INTERIOR reflection/rotation counts, without replacing original occurrences by arbitrary formal coefficient data.

No held historical outcome is adopted by this packet. Scientific computation was bounded and expressly authorized by the latest owner direction; no deletion, external model/API, secret, Git push, publication or infrastructure mutation was used. No novelty/current-world-openness assertion is made.

**END — exact reflection-only failure count and original-word double-extreme obstruction.**
