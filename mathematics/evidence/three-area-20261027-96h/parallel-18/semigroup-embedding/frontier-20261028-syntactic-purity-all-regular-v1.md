# Syntactic idempotence quotients are automatically pure on regular sources

**Status: NEW AUTHOR WRITTEN GENERAL LEMMA; UNREVIEWED / UNADOPTED.** This simplifies the hypothesis of `frontier-20261028-finest-pure-cs-actor-v1.md`, SHA `772cf39e2d5c6aab1c127ed73edaf3e7c2e617deda8f3113b8059df19f4c83ab`. It does not prove that its quotient is completely simple or that the original sources embed.

Let S be any regular semigroup. Define the syntactic congruence τ by equality of idempotence truth values of all two-sided S¹-contexts, and let `q:S→S/τ`. Then q is always **idempotent-pure**.

If q(s) is idempotent, choose an inverse z of s² in S. The element `p=s z s` is idempotent since `p²=s z s² z s=s z s`, and its q-image is q(s): q(z) is an inverse of `q(s²)=q(s)`, so `q(s)q(z)q(s)=q(s)`. Since p and s are τ-equivalent, the empty left/right contexts give the same idempotence truth value; p is idempotent, hence s is idempotent. The converse is true for every homomorphism. □

If S admits an onto pure homomorphism `r:S→T` to a completely simple semigroup T, then `q=f r` for an onto homomorphism f, because equal r-images have identical idempotence contexts by purity. A homomorphic image of a CS semigroup is CS. Therefore **S has some pure CS quotient iff its actual syntactic quotient is CS**; the reverse direction uses the automatic purity just proved. In that case S is weakly E-unitary: a natural-order witness `e=u s=s v` with e,u,v idempotent maps to such a witness in the CS quotient, whose natural order is equality, so q(s)=q(e) is idempotent and purity yields s idempotent.

Thus, for regular S, the finest-pure-CS actor and pure quotient-lattice theorems require checking only the single structural condition `S/τ is CS`; q-purity need not be separately assumed or computed. In the original WEU/local-r problem, the difficult SQ-E source import is the direction establishing that CS condition. The converse `WEU⇒S/τ CS` without local-r is NOT asserted here: a corrected same-author exploration of 145 weakly-E regular transformation semigroups on three points found no counterexample, but that finite sample has no universal force. See the natural-order erratum `frontier-20261028-natural-order-weu-audit-erratum-v1.md`, SHA `801f699bb640bd1e58eed095779c05b882e7d9eddd0ea1c470b522ecbc345c28`, for a withdrawn earlier false alarm and the correct order witnesses.

The quotient and Rees facts are at their displayed scopes and remain unreviewed; no independent proof, novelty clearance or general Q1/Q2 conclusion is claimed.
