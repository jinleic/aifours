# Strict chiral norm whenever either local square is nonnormal

**WRITTEN, UNREVIEWED additive corollary** of `frontier-20261029-d4-chiral-irreducible-strict-norm-v1.md` (SHA-256 c1acbffc0dbb1baeb2a93e396345ef5d9d6b6f77da3285d670e45fa1f77bfd00), which itself uses the named rank-one swap identity. Earlier pinned packets and frozen review scopes are unchanged.

Let traceless `A,B∈M4(C)`, `X=A⊗I4+I4⊗B`, `L=||A||_F²+||B||_F²`. Suppose a top singular pair `Xv=σ1u`, `||u||=||v||=1`, has `u⊥v`. The preceding proof establishes

`σ1²=L  ⇒  A,B are each supported on a local reducing subspace of dimension at most two`.  (1)

Because each factor is traceless, its nonzero at-most-2×2 reducing block is traceless. By Cayley–Hamilton its square is a scalar on that block; on the orthogonal complement it is zero. Thus **both `A²` and `B²` are normal**. Taking the contrapositive gives

**If `A²` OR `B²` is nonnormal, then `σ1²<L` and `σ1²+σ2²<2L`.**  (2)

For `X=0`, tracelessness forces both factors zero, so the nonnormal-square hypothesis excludes it. Every chiral pair has an orthogonal top singular pair by the preceding source. Therefore (2) is strict on the **entire arbitrary chiral class with at least one nonnormal square**, in particular the full BOTH-squares-nonnormal chiral complement. No local-rank, irreducibility, block-reducibility, genericity or magnitude assumption is needed.

This strengthens the preceding rank≥3/irreducibility sufficient condition using only its already-written mixed-minor support proof. It does not establish that any chiral member is outside f274's whole optimized `η≤2L` region, or prove unrestricted T2/T3/Z2/q3, a physical counterexample, external-source correctness, formal/kernel or stronger-family/human review, execution, selected numerical/physical q, or novelty. The corollary and its prerequisites require disjoint written review.
