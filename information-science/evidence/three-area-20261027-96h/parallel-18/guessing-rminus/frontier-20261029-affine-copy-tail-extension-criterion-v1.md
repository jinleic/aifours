# A finite certificate criterion for extending a copy-block LP profile to every larger block

## Required first inputs

Read the historical LP erratum `frontier-20261028-full-source-lp-optimum-v1-erratum-1.md` (SHA-256 `c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9`) before its consumers. The graph/source contract is `frontier-20261029-upper-bound-review-input-v1.md` (SHA-256 `e8c46fc195dd22ebcd28e485587a9872582a99ed89b25ce8d2e2ba4cee9e505a`). The compressed one-block row system is defined in `frontier-20261029-exchangeable-copy-compression-v1.md`. No held review is an input.

**Status: WRITTEN conditional extension lemma.** No witness satisfying its hypothesis has yet been supplied. This note is not a new upper bound, an exact saturation result, or an entropy realization.

## Criterion

Fix the ordinary base B (originals and C0, optionally the final X2 copy D), conditioning set Y and copied original X4 of the compressed one-block system. Let h(U,r) be a rational feasible point of that system with n>=1 copies, including every elemental Shannon row, all copy marginals and independences, and any ordinary-coordinate constraints in the surrounding model.

Suppose there is one number s such that, for EVERY ordinary-base subset U, including the empty subset,

h(U,n) - h(U,n-1) = s.

Then extend to all r>n by

h(U,r) = h(U,n) + (r-n)s.

For every K>=n, its restriction to 0<=r<=K is a feasible point of the same compressed branch with K copies. Original coordinates, surrounding independent branches and their objective are unchanged. If the optional tail copy D is present, its independence row is interpreted at the new endpoint K.

## Proof

The full-copy conditional entropy at n proves s>=0. For every ordinary-variable conditional entropy, its endpoint value is constant after n because the two coordinates have the same slope. The copy-variable conditional entropy is s thereafter.

For two ordinary variables, all four entropy coordinates have the same slope, so the elemental CMI is constant after n and remains nonnegative. For an ordinary variable and a new copy, the CMI is exactly zero once r>=n-1, by the common final increment. For two distinct copies, the second difference is zero once r>=n-1. All earlier CMI rows are already in the finite system. Thus all elemental rows hold for every larger endpoint.

For a copy marginal at the new index r=n, the needed identity is

h(U,n+1) = h(U+X4,n).

The known marginal at r=n-1 says h(U,n)=h(U+X4,n-1); adding the common increment s to both sides proves the new identity. Subsequent identities follow by the same affine extension.

Every new step independence is a difference of two increments, s-s=0. The original first-copy constraints only use r=0 and remain unchanged.

If D is present, its copy-marginal rows have the form h(U+D,r)=h(U+X2,r); their two sides have identical slope s, so they extend from r=n. Its endpoint independence is a sum of four coordinates with signs +,+,-,-, whose slopes cancel; its value is constant for endpoints K>=n. It is zero at n by hypothesis. This exhausts the branch's constraints.

## What a concrete all-orders obstruction would require

An exact rational finite feasible point satisfying the common-increment equations, an independent exact primal-row check, and an independently checked matching upper-bound dual. Those obligations would establish that this SPECIFIED copy-block family cannot improve that dual value at any larger block length. They would not establish entropic realizability or rule out different conditioning sets, other copy protocols or cross-branch constraints.

The common-increment equations are only a PRIMAL WITNESS SEARCH RESTRICTION. They are not valid universal entropy constraints and must never be inserted into an upper-bound certificate as if they were.
