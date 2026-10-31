# The five-band generates rightSN, with explicit equivariant word separators

**Status: NEW AUTHOR WRITTEN UNIVERSAL WORD-SEPARATION PROOF and finite control; UNREVIEWED / UNADOPTED.** Likely classical; no novelty is asserted. This proves a VARIETY/free-object representation, not that arbitrary quotient bands embed in five-band powers. The distinction is crucial for the genuine matching source problem.

## 1. Exact result and notation

Let B5 be the symmetric band `B_(2)` with labels x=0, u₁=1,u₂=3,v₁=2,v₂=4 and table

```text
0 2 2 4 4
0 1 2 1 4
0 2 2 2 4
0 3 2 3 4
0 4 2 4 4
```

Then `var(B5)` is exactly the right-seminormal band variety `abc=acabc`. For a finite n-letter alphabet A, the free rightSN band embeds in a direct power of B5 with at most

`n²+n·2^(n−1)` coordinates.

The coordinate set can be chosen invariant under EVERY permutation of A. Hence any group acting on A acts on that power by coordinate permutations, and the free-band embedding is equivariant. For n=6 the bound is228 coordinates, rather than all5⁶=15,625 assignments; no228-coordinate614,226-state table was enumerated here.

## 2. Constructive separation of different signatures

The rightSN signature theorem `frontier-20261029-right-seminormal-normal-form-v1.md`, SHA `c2a5f4d9de295deed8e28282b2456f6d274886856224dccd68208bae0c2fe6be`, says a word's class is its recursion of first letter and earliest last-occurrence letter. Unroll this signature as the permutation `c₁,...,c_k` listing letters by increasing LAST-occurrence position, and the sequence h_j of first letters of the suffix after the last c_(j−1), with h₁ the original first letter. Each h_j lies among `{c_j,...,c_k}`. These two sequences are exactly the recursive signature; the complete normal reduction proves equal signatures are identities in rightSN.

Different signatures are separated by one of three explicitly B5-valued assignment families:

**Content family (n assignments).** For a∈A assign a↦v₁ and all other letters↦u₁. The subband `{u₁,v₁}` is a two-element semilattice, so a word evaluates to v₁ iff it contains a. Thus different contents are separated.

**Last-order family (n(n−1) assignments).** For distinct a,b assign a↦v₁,b↦v₂ and all other letters↦u₁. The corner `{u₁,v₁,v₂}` is a right-zero band with identity u₁, so the result is the value of whichever of a,b appears LAST. Any two different last-occurrence permutations have a pair whose relative order differs; that assignment separates them.

**Suffix-head family (n·2^(n−1) assignments).** For any X⊆A and h∈A\X assign every X-letter↦x, h↦u₁ and every other letter↦u₂. Suppose two words have the SAME content and last-order permutation but differ at h_j. Take `X={c₁,...,c_(j−1)}` and choose h to be the first word's h_j. For j=1 there is no x and multiplication of the upper left-zero letters returns the word's first letter, separating h₁. For j>1 the last X-letter is precisely the last occurrence of c_(j−1). The product resets to x there; the remaining upper-only suffix evaluates to v₁ if its first letter is h and v₂ otherwise. The two different h_j values are therefore separated.

B5 itself satisfies the rightSN identity by the symmetric-band word rule and literal table check. Thus no two different rightSN signatures have the same evaluations in B5, whereas equal signatures give every rightSN identity. This proves `var(B5)=rightSN` and embeds the free band in the displayed finite power by the simultaneous evaluation map. The coordinate count is exactly the sum of the three listed family bounds (some assignments may coincide, so it is an upper bound).

## 3. Equivariance and HSP consequence

Permuting A preserves each assignment family: singleton selectors, ordered pairs, and subset/head selectors are taken to selectors of the same type. Let Ω be their set, and for a group G acting on A define `(α_g F)(χ)=F(χ∘g)`. Then `α_g(eval(w))(χ)=eval(gw)(χ)`, so the simultaneous word-evaluation embedding is equivariant under the coordinate permutation action. The group law follows from composition of the alphabet action; no internal action on B5 is needed.

Consequently ANY rightSN band B with a G-action is an equivariant homomorphic image of a G-invariant subband of a B5 power: use the free G-band on symbols `(g,b)`, evaluate `(g,b)↦g·b` onto B, and apply the free-band embedding above (for infinite alphabets use all B5 assignments, which still separate finite words). Its kernel is G-invariant. This is an **HSP/quotient representation**, not an SP representation of B itself.

The zero-enriched C6=B5⁰ used in the successful S68 host has exactly the SAME identities but violates the quasiidentity Q true in all B5 powers/subbands. Thus C6 is in HSP(B5), not SP(B5); the distinction is witnessed by the actual source, not an abstract caveat. Restricting evaluations only to assignments satisfying source M-relations could miss canonical quotient distinctions—quotients of a free residual-B5 band need not be residual-B5. No claim here replaces canonical congruence closure by ordinary five-band model enumeration.

## 4. Exact finite control and remaining gap

`frontier-20261029-rightSN-fiveband-separator-checker-v1.py`, SHA `9afb88de40dee2ecb5bab21ad0ffab89876af7f9ffca748f01481e42b8d439eb`, ran in the Python eval kernel before Thu Oct29 00:59:07 PDT2026. It checks B5's associativity/rightSN law; constructs the three coordinate families and the complete free-signature state sets for n≤4; verifies all1,6,51,748 states have different evaluation vectors; and checks the assignment set is invariant under all alphabet permutations. Coordinate counts are2,8,21,48. This is same-author finite control, not the proof of the universal separator construction.

The remaining source challenge is exactly the canonical quotient/one-sided Green distinction, not free-word separation. The source's mixed relations may force new quotients requiring zero enrichment or more general homomorphic images. No full originalQ1/Q2, formal proof, independent review or novelty is claimed.
