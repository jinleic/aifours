# Same-fibre R-pairs in sources made of a group over a completely simple ideal

**Status: NEW AUTHOR WRITTEN THEOREM with an exact finite check; UNREVIEWED / UNADOPTED.** This settles item4 of `frontier-20261029-Q1-reduction-state-v1.md` (SHA `231a862f484d1d304d7094319e98f715fa5f5442522d227a7a87ac0df9a66157`) for one narrow class of sources only. It is a step on the same-fibre separation bridge, not a proof of Q1. No novelty is claimed.

Notation. `D=M[G;I,Λ;P]`. For `x∈S`, write `q(x)=(i_x,g_x,λ_x)` and `w(s,t)=g_s p_(λ_s,i_t)`. A *twisted host* is a band B with G acting by automorphisms, together with `β:S→B` such that `β(st)=β(s)·^(w(s,t))β(t)`. Then `x↦(β(x),q(x))` is a homomorphism into the physical product `P(B,D)`.

## 1. Theorem

Let S be a semigroup with an idempotent-pure onto homomorphism `q:S→D`. Suppose `S=H⊔K`, where H is a subgroup with identity h and K is an ideal that is completely simple. Then there is a twisted host `β:S→B` with B right seminormal (every local monoid right regular) such that `β(e)≠β(f)` for every pair of distinct idempotents with `e R f` and `q(e)=q(f)`.

Regularity and the RRL hypothesis are not used. If S is RRL, every same-fibre R-pair of S lies in K: H has only the idempotent h, and h is not R-related to any element of K. So S satisfies item4.

## 2. Data

- Write ColK for the set of L-classes of K. These are the columns of the completely simple K. Write `c(k)` for the column of k. H acts on ColK on the right by `c(k)·t=c(kt)`; this is well defined because L is a right congruence. Every element of a column c has the same D-column, written `μ(c)`.
- Put `ĝ_t=g_t p_(λ_h,i_h)` for `t∈H`. Purity makes q injective on H, so `ĝ:H→G` is an injective homomorphism. Write `Ĥ=ĝ(H)`.
- A *real point* is a pair `ω=(m,c)∈G×ColK`. Its entry label is `v_ω=m p_(μ(c),i_h)`. Call ω *h-fixed* if `c·h=c`; in that case `μ(c)=λ_h`.
- The top band is `T=G×G` with the rectangular product `(a,b)(a',b')=(a,b')`. G acts diagonally by left multiplication.

## 3. The point set and the action of T

For an h-fixed ω, its orbit is `O(ω)={(v_ω ĝ_t g_h, c·t) : t∈H}`, where `g_h=p_(λ_h,i_h)^(-1)`. The coset `v_ωĤ` is constant on an orbit.

Points are:
- real points;
- orbit phantoms `⟨O,b⟩`, for an orbit O and `b∉v_OĤ`;
- moved phantoms `⟨ω,a,b⟩`, for a real ω that is not h-fixed and `a≠v_ω`.

The action of `(a,b)∈T`:

1. **h-fixed real ω.** If `b=v_ω ĝ_t` for some `t∈H`, then `ω·(a,b)=(b g_h, c·t)`; otherwise `ω·(a,b)=⟨O(ω),b⟩`. The result does not depend on a.
2. **Real ω that is not h-fixed.** If `a=v_ω` and `b=v_ω ĝ_t`, then `ω·(a,b)=(b g_h,c·t)`. If `a=v_ω` but `b∉v_ωĤ`, then `ω·(a,b)=⟨O(ω·(v_ω,v_ω)),b⟩`. If `a≠v_ω`, then `ω·(a,b)=⟨ω,a,b⟩`.
3. `⟨O,b⟩·(a',b')=ω_0·(v_(ω_0),b')` for any `ω_0∈O`.
4. `⟨ω,a,b⟩·(a',b')=ω·(a,b')`.

**Well-definedness.** The t in rules 1–2 is unique because ĝ is injective. In rule 1, the image `ω'=(b g_h, c·t)` is h-fixed, since `c·t·h=c·t`. Its entry label is `v_(ω')=b` (because `μ(c·t)=λ_h`), so it lies in `O(ω)`. Rule 3 does not depend on the choice of `ω_0`: if `ω_0'=ω_0·(·,b_0)`, then `ω_0'·(v,b')=ω_0·(v,b')` by the computation in case A1 below.

**Act axiom (A): `π·(a,b)·(a',b')=π·(a,b')`.**

- *A1, π h-fixed real.* Suppose `b=v_ω ĝ_t`. Then `π·(a,b)=ω'` with `v_(ω')=b`. If `b'=bĝ_(t')`, then `ω'·(a',b')=(b'g_h, c·t t')`. Here `v_ω ĝ_(tt')=b'`, so this equals `ω·(a,b')`. If `b'∉bĤ=v_ωĤ`, both sides are `⟨O(ω),b'⟩`. If instead `b∉v_ωĤ`, apply rule 3.
- *A2, π real but not h-fixed.* When `a=v_ω` and `b∈v_ωĤ`, the image is the h-fixed real point `ω·(v_ω,b)`, and A1 gives `ω·(v_ω,b')`. When `a=v_ω` and `b∉v_ωĤ`, rules 2 and 3 give `ω·(v_ω,v_ω)·(v_ω,b')=ω·(v_ω,b')`, again by A1. When `a≠v_ω`, rule 4 gives `ω·(a,b')`.
- *A3, π a phantom.* Rules 3 and 4 reduce this to A1 and A2.

**Equivariance.** G acts on labels by left multiplication, `^g⟨O,b⟩=⟨^gO,gb⟩` and `^g⟨ω,a,b⟩=⟨^gω,ga,gb⟩`. Every rule commutes with this action.

## 4. The band and the host

Let `B=T⊔Ω`, where Ω is the point set made into a right-zero semigroup (`ωω'=ω'`). The mixed products are `xω=ω` and `ωx=ω·x` for `x∈T`. Associativity follows from (A) and the right-zero and rectangular rules, and every element is idempotent. This is the two-layer lemma of checkpoint-0740 with a single row.

**B is right seminormal.**
- For `x∈T`, the local monoid is `xBx={x}∪Ω·x`. For `u,u'∈Ω·x` we have `uu'u=u=u'u`. Also `xux=ux` and `uxu=u=xu`. So xBx is a right-zero band with an identity adjoined, which is right regular.
- For `ω∈Ω`, the local monoid is `ωBω={ω}`.

**The host.** Put `β(t)=(1,ĝ_t)` for `t∈H`, and `β(k)=κ(k):=(g_k,c(k))` for `k∈K`.

1. *`t,t'∈H`.* `w(t,t')=ĝ_t`, and `(1,ĝ_t)(ĝ_t,ĝ_tĝ_(t'))=(1,ĝ_(tt'))`.
2. *`s∈S`, `k∈K`.* Here `sk L k` inside K, since `sk=(skk')k` with `skk'∈K`. Also `g_(sk)=w(s,k)g_k`. Hence `κ(sk)=^(w(s,k))κ(k)=β(s)·^(w(s,k))β(k)`.
3. *`k∈K`, `t∈H`.* `v_(κ(k))=g_k p_(λ_k,i_h)=w(k,t)`. So `^(w)β(t)=(w,wĝ_t)` acts by rule 1 or 2 with the matching element t. It gives `(wg_t, c(k)·t)=(g_(kt),c(kt))=κ(kt)`.

**Separation.** Distinct same-fibre idempotents e, f with `e R f` lie in one row of K and in different columns, and `g_e=g_f`. Hence `κ(e)≠κ(f)`. □

## 5. Exact check and scope

`frontier-20261029-group-top-two-level-host-checker-v1.py`, SHA `8bb675ea17a9558a0dda889e1da1a0127b12991a6a6efd6951247afd2c9b81c3`, ran with python3.14 before Thu Oct 29 08:04:05 PDT 2026, exit 0. It generated 10 distinct two-generated regular sources of the form `H⊔K` inside `P(B5,D8)`. For each it checked:
- that the source has this form;
- that the constructed band (4 top elements and 10 points: 6 real and 4 phantom) satisfies associativity on all triples;
- right regularity of every local monoid;
- that the C2 action is by automorphisms;
- every source-host product equation;
- separation of every same-fibre R-pair.

The 10 points match the 10 bottom columns of the 44-element canonical band computed earlier for such a source. This is same-author finite evidence for the written proof.

The class is narrow: the top is one group, and K is a prime ideal. A completely simple top T with K prime is expected to work by the same rectangular-band bookkeeping, using T-fixed real points. This is only sketched (checkpoint-0759) and is not claimed. The S45 pattern, where the top is not closed and its twisted translates meet in K, is not covered. Neither are three or more levels.

A naive induction on the minimal ideal fails for a stated reason. Collapsing K's fibres first already identifies R-pairs that are products of upper elements, as `e=(1,4,1)(1,4,1)` and `f=(1,4,1)(2,4,1)` are in S45.
