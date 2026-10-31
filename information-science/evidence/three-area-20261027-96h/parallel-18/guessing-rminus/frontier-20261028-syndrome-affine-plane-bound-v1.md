# Every affine syndrome plane has q=8 FD capacity at most 2^20

**Status: WRITTEN corollary of the pinned exhaustive syndrome-triangle witnesses; scientific review pending.** In the standard fixed q=8 triangle-factor labeling, any original-FD-consistent support contained in an **affine two-dimensional plane** of the ten-bit syndrome space—that is, in the four classes

\[
a,\quad a+s,\quad a+t,\quad a+s+t
\]

for distinct nonzero `s,t`—has at most `2^20` words. Thus, if a q=8 fixed-point set beating the standard triangle code meets exactly four syndrome classes, those four syndrome vectors must be **affinely independent**. The result is a cardinality constraint, not a nonuniform entropy-gap exclusion or unrestricted guessing-number bound.

## Proof

The pinned theorem `frontier-20261028-triangle-code-three-coset-bound-v1.md` SHA-256 `3b29b8f3eebb6f66e729e3de2d6f998108ca755c83f8ff177fd30139cf574403` supplies, for every distinct nonzero `s,t`, words `u,v` of syndromes `s,t` such that `u,v,u xor v` are all confusable with zero. Consequently the four words

\[
0,\quad u,\quad v,\quad u\mathbin{\mathrm{xor}}v
\]

form a conflict clique: every nonzero pairwise difference is one of `u,v,u xor v`. Their syndromes are exactly `0,s,t,s+t`. Translating this four-word clique by every codeword in the kernel `W0` tiles those four syndrome classes into `2^20` disjoint 4-cliques. An ambient translation handles an arbitrary affine offset `a`. An FD-consistent support meets each clique at most once, so it has at most `2^20` words.

The preceding theorem's independent exact witness replay is SHA-256 `6c254cb53fdbf004ac0c784fb3d5ee3398dacd9a5377a74e7ae972594f17f10b`; no new enumeration or unverified maximum-clique claim is needed. Scientific review and novelty clearance remain pending.
