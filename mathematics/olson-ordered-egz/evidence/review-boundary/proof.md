# Ordered Olson: actual arguments and remaining gap

## Exact target

Let G be a finite group and n=|G|. Given every word a_1,...,a_(2n-1), select indices i_1<...<i_n such that a_(i_1)...a_(i_n)=1, without rearrangement. Equivalently, every list xs of length 2|G|-1 has a List.Sublist ys of length |G| and ordered product 1. No all-groups proof or counterexample has been established by this dossier.

## 1. Sharp lower bound for every odd dihedral parameter (known result, reproduced)

Let m>=1 be odd. In D_(2m)=<r,s | r^m=s^2=1, srs=r^(-1)>, consider the word

    W = r repeated (2m-1) times, then s repeated (2m-1) times.

Its length is 4m-2=2|G|-2, ONE TERM SHORT of the conjecture's hypothesis.

An ordered 2m-term subword of W is r^k s^l with k+l=2m and 0<=k,l<=2m-1. In particular 0<k,l<2m. If its product were 1, projection to D_(2m)/<r> forces l even. Then s^l=1 and r^k=1, so m divides k. The only positive multiple of m below 2m is m itself. Thus k=m and l=m, contradicting oddness. Therefore W has no ordered |G|-term identity-product subword.

The theorem `OlsonPartial.odd_dihedral_sharp_lower_bound` in `work/DihedralLowerBound.lean` proves the full all-m assertion with Mathlib's actual DihedralGroup, including its cardinality, the precise word length, and the universal List.Sublist quantifier. It is not a theorem about the 2|G|-1 bound. Its known-result label is essential: Agarwal–Lou's 2016 primary abstract already reports the odd-dihedral lower bound 4m-1 for the forcing constant. The abstract does not expose their construction or full proof, so this is a reproduced bound, not a claim that their exact proof was recovered.

A genuine false-proposition control is `work/NegativeControl.lean`: it asserts that every length-six ordered sublist of r^5 s^5 1 in D_6 has nonidentity product. Lean's `decide` explicitly proves that assertion false. The exhibited reason is the ordered subword r^3 s^2 1.

## 2. General complementary-cyclic-block obstruction to naive extension

This argument is written only, not separately Lean-certified and not claimed novel. Suppose |G|=n, a and b have orders p and q, their cyclic subgroups intersect trivially, and lcm(p,q)=n. Then a^(n-1) followed by b^(n-1) avoids an ordered n-term identity product: such a product a^k b^(n-k)=1, with 0<k<n, implies a^k=b^k, hence p|k and q|k, so n|k, impossible.

However, inserting an arbitrary c exactly between the two blocks always destroys avoidance. For k=0,...,n-1, define c_k=a^(-k)b^(k+1). The map k -> c_k is injective: equality for j,k gives a^(j-k)=b^(j-k), so p and q both divide j-k, and n divides j-k; the range bound gives j=k. Consequently c_k exhaust G. Choose k with c=c_k. Then

    a^k c b^(n-1-k)=a^k a^(-k) b^(k+1+n-1-k)=b^n=1.

The selected word has k+1+n-1-k=n terms, in the correct order. Thus the most obvious three-block completion cannot refute the conjecture. This argument only covers insertion at that boundary, not arbitrary multiblock or shuffled words.

### 2.1 Stronger boundary-insertion theorem without subgroup hypotheses

In fact, for EVERY finite group G of order n and arbitrary a,b,c in G, the specific word a^(n-1) c b^(n-1) contains an ordered n-term identity product. No cyclic-intersection or generator-order hypothesis is needed.

Consider the n values c_k=a^(-k)b^(k+1), 0<=k<n. If they are all distinct, they exhaust G and the previous construction applies. If c_i=c_j with i<j, cancellation gives a^(j-i)=b^(j-i). Set d=j-i, so 1<=d<n. Skipping c and selecting d copies of a and n-d copies of b gives a^d b^(n-d)=b^n=1. These alternatives cover every case, including n=1 (where the list consists of the identity c in the trivial group).

This proves the exact-length conjecture for this structured word family only. It is an elementary obstruction to a candidate construction, not a proof for arbitrary words. No novelty is claimed. This strengthening was added after the first independent-review snapshot; its separate Lean evidence is recorded with the delivered theorem.

## 3. Exact ordered dynamic-programming invariant

For a prefix a_1,...,a_t define P(t,k) to be the set of group products of its increasing-index k-term selections. Then

    P(0,0)={1}, P(0,k>0)=empty,
    P(t+1,k)=P(t,k) union {g*a_(t+1) : g in P(t,k-1)}.

Proof: every selected index set either excludes the new last index, or includes it after all previously selected indices. Those alternatives give precisely the two terms. This is right multiplication, never multiplication in arbitrary order.

This validates the mathematical transition used by the parent's read-only `feasibility/olson_probe.py`. Two prefixes with the same complete state (P(t,0),...,P(t,n-1)) have identical safe continuations; storing one representative is exact. A state can be pruned when a transition reaches 1 in P(t,n), because an n-term witness survives every extension. At depth t, a layer k<n-(L-t) cannot reach length n by the fixed final depth L and can be dropped permanently. These facts justify the parent's state merging and low-layer pruning. The Python group checker checks associativity and the identity but not inverse existence; this omission is harmless for the explicitly constructed genuine groups, not sufficient validation for arbitrary future tables.

The independent SMT assay `work/ordered_smt.py` uses only forward Horn implications for the same transition. This is sufficient: for a fixed word its least satisfying assignment is the actual reachable-state relation. Any satisfying assignment that omits the final identity therefore corresponds to a genuinely avoiding word. Conversely, if a word avoids identity, the actual relation satisfies every implication. One-hot letters preserve the order. The solver uses no permutation symmetry reduction. A SAT result must pass raw increasing-index subset enumeration and an independent set-DP check before it can be considered a witness. A timeout/UNKNOWN proves nothing.

The two order-12 assays, A4 and C3 semidirect C4 (inversion action), both returned UNKNOWN after their 180-second solver limits. The second had two completed controls: its one-short complementary-generator word was SAT and independently checked on every 12-subset; appending identity was UNSAT with that word fixed. Neither unrestricted search yielded a counterexample or a finite classification.

An additional exact construction assay checked every length-23 word with at most three constant runs in each of A4 and C3 semidirect C4. Words with a run of length at least12 are immediate by Lagrange. Of the remaining parameterizations, 95,832 genuinely three-run words per group were checked, each with a selected-count witness whose actual letters were multiplied again; 18,216 adjacent-equal parameterizations per group collapse to an immediate two-run case. No counterexample was found in this restricted family. `evidence/three-run-search.json` records the witness-stream hashes. This excludes neither words with four or more runs nor any other group.

## 4. Why standard shortcuts do not prove the target

### Reordering disjoint quotient-zero blocks

In a quotient-group EGZ argument, selected blocks may interleave in the original word. Concatenating each block's factors and then multiplying block-products generally reorders the original factors. Even when each block-product belongs to the same subgroup, its factors need not commute with the factors of another block. Gao–Li's solvable-group proof explicitly uses this unrestricted concatenation; it cannot be silently relabelled as an ordered proof.

### Only deleting disjoint identity-product intervals

Equal prefix products identify contiguous identity-product intervals. But the equality pattern of prefix products alone does not ensure disjoint such intervals of total length n. Already for n=2, the prefix-color word (0,1,1,0) permits total disjoint-interval lengths only 0,1,3, not 2. In C2 this corresponds to the word (g,1,g), which nevertheless has the NONCONTIGUOUS two-term identity subword (g,g). Thus this is a counterexample only to a proposed sufficient proof route, not to Olson. `work/interval_route.py` records the small exact obstruction.

## Exact remaining quantifier

The unresolved assertion is still: for EVERY finite group G (including mixed-prime nonabelian groups), EVERY word of length 2|G|-1 contains a |G|-term identity-product ordered subword. The infinite lower-bound family has length 2|G|-2 and cannot settle it. No finite search miss, p-group prior theorem, unordered EGZ result, or conditional recurrence argument fills this gap.
