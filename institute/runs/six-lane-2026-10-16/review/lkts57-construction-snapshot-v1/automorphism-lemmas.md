# Automorphisms of a large set of Steiner triple systems (v odd)

Written 2026-10-16 (lane `kirkman57`). Elementary; **no novelty is claimed**
(similar facts may be folklore). Proof-level evidence only; not Lean-checked.

Setting. `L={S_1,…,S_{v−2}}` is an LSTS(v) on X, |X|=v odd: the block sets are
pairwise disjoint STS(v) whose union is all triples. `Aut(L)` = permutations of
X permuting the block sets. An automorphism of an LKTS (preserving block sets,
with or without resolutions) is in particular in `Aut(L)`. `b(v)=v(v−1)/6`.

**Lemma 0.** If `g∈Aut(L)` fixes a triple T setwise, the constituent containing
T is g-invariant. *Proof.* `gS` is a constituent containing `gT=T`; constituents
are disjoint, so `gS=S`. ∎

**Lemma 1.** If `g` is an automorphism of an STS S then `Fix(g)` is closed: for
fixed p≠q the third point of their block is fixed. Hence `|Fix(g)|≠2`, and if
`|Fix(g)|≥3` it carries a sub-STS; for a proper subsystem `v≥2|Fix|+1`.
*Proof.* `g{p,q,r}={p,q,gr}` is the block through p,q, so `gr=r`. ∎

**Lemma 2 (prime order, many fixed points).** Let `g∈Aut(L)` have prime order p,
`F=Fix(g)`, `3≤f=|F|<v`. Then exactly `f−2` constituents are g-invariant, their
restrictions to F are pairwise disjoint STS(f) forming an LSTS(f) on F, and the
other constituents are permuted in orbits of length p (so `p | v−f`).
*Proof.* Every triple inside F is g-fixed, so lies in a g-invariant constituent
(Lemma 0). Each g-invariant constituent restricts to an STS(f) on F (Lemma 1),
i.e. contains `f(f−1)/6` triples of F; distinct ones are disjoint. Hence their
number is `C(f,3)/(f(f−1)/6)=f−2`. A non-invariant constituent has orbit length
p. ∎

**Lemma 3 (involutions).** Let `t∈Aut(L)` be an involution. Then `|Fix(t)|=1`,
say `Fix(t)={p}`; exactly one constituent `S_t` is t-invariant; its blocks
through p are exactly the `(v−1)/2` triples `{p,a,ta}`; the centralizer `C(t)`
stabilizes `S_t` and contains no involution other than t. Consequently every
Sylow 2-subgroup of `Aut(L)` has a unique involution, hence is cyclic or
generalized quaternion.
*Proof.* v odd ⇒ f odd. Suppose `f≥3`. Choose a transposition (a b) of t (exists
as f<v) and c∈F. In a t-invariant constituent the block through {a,b} is
t-invariant, hence `{a,b,x}` with x fixed. So such a constituent contains exactly
one triple `{a,b,x}`, x∈F, while each of the f triples `{a,b,c}` (c∈F) is t-fixed
and lies in a t-invariant constituent: at least f invariant constituents,
contradicting Lemma 2 (exactly f−2). So f=1. Now every t-invariant constituent
contains all `{p,a,ta}` by the same argument, so at most one exists, and Lemma 0
gives existence. For `c∈C(t)`, `cS_t` is t-invariant, so `cS_t=S_t`. If
`t'∈C(t)` is an involution, `t'p∈Fix(t)`, so `t'p=p`; `t'` stabilizes `S_t`, whose
blocks through p are then both `{p,a,ta}` and `{p,a,t'a}`; so `t'=t`. For the Sylow
claim take z central of order 2 in a Sylow 2-subgroup P; `P≤C(z)` has a unique
involution; such 2-groups are cyclic or generalized quaternion. ∎

**Lemma 4 (order 3, block count).** Let `g∈Aut(L)` have order 3, f fixed points.
In a g-invariant constituent S the g-fixed blocks are the blocks inside F and
the 3-cycles of g that are blocks of S; the rest form g-orbits of length 3. Hence
`(#3-cycles of g in S) ≡ b(v) − b_F (mod 3)`, `b_F=f(f−1)/6` (0 if f≤1). Every
3-cycle of g lies in some g-invariant constituent (Lemma 0).

**Corollary (v=57).** `b(57)=532≡1 (mod 3)`, f≡0 (mod 3), and f≤28 for f<57.
* f=0: each g-invariant constituent contains ≡1 (mod 3) of the 19 cycles, so the
  number n of g-invariant constituents satisfies `n≡1 (mod 3)`, `1≤n≤19`.
* f=3: one invariant constituent; it contains Fix(g) and all 18 cycles.
* f=9: 7 invariant constituents, each with ≡1 (mod 3) of the 16 cycles: possible.
* f=15: 13 invariant constituents need ≡2 (mod 3), i.e. ≥2 cycles each: 26>14.
  **Impossible.**
* f=21: 19 invariant constituents, ≡0 (mod 3) of the 12 cycles each: possible.
* f=27: 25 invariant constituents need ≥1 of the 10 cycles each. **Impossible.**

**Corollary (prime p≥5, v=57).** If g fixes no constituent then it fixes no
triple, so f≤2 and `p | 55` (f=2, p∈{5,11}). Otherwise f∈{0,1} (then p|57 or
p|56) or f is an admissible order ≤28 with an LSTS(f) (so f≠7) and p|57−f.
Enumerating: p=5: f∈{2,27}; p=7: f∈{1,15}; p=11: f∈{2,13}; p=19: f∈{0,19};
p=13,17,23,29,…,53: none. Hence **every prime divisor of |Aut(L)| for an
LSTS(57) lies in {2,3,5,7,11,19}**, and involutions have exactly one fixed point.

**Lemma 5 (orientation mod 3; any KTS on three equal layers).** Partition the
points of a KTS into layers `L_0,L_1,L_2` of equal size, indices mod 3. A block
with two points in `L_i` and one in `L_{i+1}` is *positive*, one with two points
in `L_i` and one in `L_{i−1}` is *negative*. Then **in every parallel class
#positive ≡ #negative (mod 3)**.
*Proof.* In a class let `x_i` count blocks inside `L_i`, `p_i` (resp. `m_i`)
blocks with two points in `L_i` and one in `L_{i+1}` (resp. `L_{i−1}`), z blocks
meeting all layers. Covering `L_i` once: `3x_i+2(p_i+m_i)+p_{i−1}+m_{i+1}+z=|L_i|`.
Subtract the i=1 equation from the i=0 equation; since `|L_0|=|L_1|`, mod 3:
`2p_0+2m_0+p_2+m_1−2p_1−2m_1−p_0−m_2 ≡ p_0+p_1+p_2−(m_0+m_1+m_2) ≡ 0`. ∎

Executable sanity check (not a proof): all 476 classes of the prior dossier's
independently checked 17-system C19 packing satisfy it (`code/scratch/orient_lemma_check.py`).

**Corollary 5a (used to prune G513 resolutions).** If a group R acts on the
classes preserving the cyclic layer order and a class orbit is regular, each
of its classes takes one block from each of 19 regular block orbits, so the
number of positive block orbits it uses is ≡ (number of negative ones) mod 3.
For a class made only of two-layer blocks this forces both ≡ 2 (mod 3). In the
γ-symmetric B candidates (three K-orbits of two-layer blocks, hence 0, 19, 38
or 57 positive regular R-orbits) the structure "fixed class + three regular
9-orbits" is impossible: three classes each ≡2 cannot sum to 0,19,38,57 with
both signs present. This explains the eight 600-second UNKNOWN runs of
`code/runs/bpool1`; they were infeasible models, not hard instances.

**Remarks.**
* The prior dossier's exclusions of scalar involutions fixing both infinities
  (fixed points m+2≥3) are the special case of Lemma 3 for automorphisms that
  normalize the development group; its order-5 case is the f=7 case above.
* None of these statements excludes LKTS(57); they restrict symmetric searches.
