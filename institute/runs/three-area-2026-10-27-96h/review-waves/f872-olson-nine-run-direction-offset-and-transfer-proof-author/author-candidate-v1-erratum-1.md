# F872 author erratum 1 to `author-candidate-v1.md`

Additive; v1 bytes are unchanged and remain the pinned candidate. After writing v1, I completed a written self-recheck of every derivation, without executing code. It found the following author defects. None changes a stated region theorem, because every downstream use was already correct.

## E1 (MINOR, statement): §4.1 singleton-target equivalence

V1's conditions 1–2 are necessary but **not sufficient** as worded: an exponent-0 constant-interior eligible rotation together with h≠0 satisfies them, yet pairing that rotation with a boundary rotation gives B=B0+h=d−h≠d. Replace them by:

> There is h∈F_p with `B0+2h=d` such that every eligible boundary rotation has exponent h, every eligible safe non-rich interior rotation has exponent −h, every eligible constant-interior rotation has exponent 0, **and h=0 whenever an eligible constant-interior rotation exists**.

Equivalently, `A_q={h}` for every eligible q. The v1 proof establishes this forward; the converse is then immediate because every edge sum is `B0+2h=d`. Downstream uses in §6.1–6.2 invoke only the forward direction, including the v1 sentence that a constant-interior eligible rotation forces h=0, so they are unaffected.

## E2 (MINOR, numerical wording): §6.1 piece length

For k=p−5 the final negative-slope outside piece is `x_k,…,x_(n−1)` with `n−k=2p−5` occurrences, not 2p−6. Its subpiece `x_(k+1),…,x_(n−1)` has 2p−6. Either satisfies hypothesis (i) of §5, so the conclusion stands.

## E3 (clarity): §6.1 case structure

The k∈{1,2} and k∈{n−2,n−1} arguments are made inside the branch `[u]≠[v]` (with the middle range 3≤k≤n−3 already settled). In that branch the midpoint criterion leaves only u=2v, respectively v=2u, because v=−u would give `[u]=[v]`. Both closures fail since p≥7 divides neither 9 nor 8. Hence `[u]≠[v]` is impossible, which is what "Hence v=−u" means.

## E4 (clarity): §3 one-outlier coverage sentence

Replace "whose three-point complement cannot contain a translate by e…" with: for `I={0,…,p−4}d` and `e=εd`, `I∪(I+e)=F_p` iff the complementary 3-arcs `{−3,−2,−1}d` and `{ε−3,ε−2,ε−1}d` are disjoint, iff `ε∉{0,±1,±2}`. Since an outlier has `e∉{0,±d}`, it fills the field exactly when `[e]≠[2d]`.

## E5 (clarity): §4 orientation and notation

"Or in the outlier case `{b,b+2d}`" applies only to the single outlier set. All other non-rich sets are `{b,b+d}`. In the two-missing-offset bullets, the target `T={d−B0,2d−B0}` is unrelated to the rich sets `T_i`/`T(a',b',c';u,v)`. In the first-bullet proof, "u+z" means u plus the value `h_z` at a common neighbor z.

## E6 (process disclosure)

V1 was written before this complete self-recheck, not after it; this erratum is the additive correction, not a backdated revision. The self-recheck used no code, execution, new source, peer content or held material.

Status unchanged: AUTHOR CANDIDATE only; parent disposition and independent checking remain separate.
