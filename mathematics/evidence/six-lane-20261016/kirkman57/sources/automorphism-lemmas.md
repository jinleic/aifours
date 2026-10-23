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
*nontrivial* Sylow 2-subgroup of `Aut(L)` has a unique involution, so every
Sylow 2-subgroup is cyclic (possibly trivial) or generalized quaternion.
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
claim let P be a nontrivial Sylow 2-subgroup and z∈Z(P) of order 2; `P≤C(z)`
has a unique involution; a 2-group with a unique involution is cyclic or
generalized quaternion (standard; e.g. Gorenstein, *Finite Groups*, Thm 5.4.10(ii)).
If |Aut(L)| is odd the Sylow 2-subgroup is trivial (the case of G513). ∎

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
p|56) or f is an admissible order ≤28 carrying an LSTS(f) and p|57−f; f=7 is
excluded by the classical nonexistence of LSTS(7) (at most two pairwise disjoint
STS(7); Cayley 1850 — imported, not reproved here).
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

**Corollary 5a (conditional obstruction for the eight `runs/bpool1` models).**
*Premises (the imposed model, not properties of every LKTS):* layers `L_i=Z19×{i}`;
the base B is an STS(57) invariant under `K=⟨F57,γ_1⟩`,
`γ_1:(x,i)↦(x+ω^i,i+1)`, ω=7; the *chosen* resolution of B is required to be
invariant under `R=⟨μ,γ_1⟩≅Z3×Z3` (μ:(x,i)↦(7x,i+1)) with exactly one R-fixed
class `C_0` and three regular R-orbits of classes. Every element of R and K
shifts all layers by the same amount, so it maps positive blocks to positive
blocks. *Computed facts* (`code/bpool1_facts.py` → `evidence/bpool1-obstruction-facts.json`),
for each of the eight candidates: R has block orbits of sizes 9 (57 orbits),
3 (6) and 1 (1); the 19 blocks in non-regular orbits are exactly the 19
γ_1-cycles (each meets all three layers); all other 513 blocks meet exactly two
layers; they form three K-orbits of 171 blocks, each of a single orientation;
hence the number of positive regular R-orbits is 0, 19, 38 or 57.
*Claim.* No such resolution exists for any of the eight candidates.
*Proof.* A block with nontrivial R-stabilizer lies in a class fixed by that
stabilizer; in this class structure only `C_0` has a nontrivial stabilizer, so
`C_0` contains the 19 γ_1-cycles, which already partition X; thus `C_0` is exactly
them. A regular block orbit contributes one block to each class of a regular
class orbit, or 9 blocks to `C_0` (impossible now). So each representative class
`C_k` (k=1,2,3) consists of 19 two-layer blocks, one from each of 19 regular
orbits, with `P_k` positive and `19−P_k` negative ones. Lemma 5 gives
`P_k≡19−P_k (mod 3)`, i.e. `P_k≡2 (mod 3)`, so `P_1+P_2+P_3≡0 (mod 3)`. But this
sum is the number of positive regular orbits, 19n with n∈{0,1,2,3}; n∈{1,2}
contradicts the congruence and n∈{0,3} forces some `P_k∈{0,19}`, not ≡2. ∎
The eight 600-second UNKNOWN runs therefore concerned infeasible models. This
does **not** cover the separate μ-only and γ-only runs (`runs/exp2`, `runs/exp3`),
which remain UNKNOWN; UNKNOWN is never read as infeasibility.

**Remarks.**
* The prior dossier's exclusions of scalar involutions fixing both infinities
  (fixed points m+2≥3) are the special case of Lemma 3 for automorphisms that
  normalize the development group; its order-5 case is the f=7 case above.
* None of these statements excludes LKTS(57); they restrict symmetric searches.

## Addendum (2026-10-16, after the LKTS(87) construction): the case v=87

`b(87)=1247≡2 (mod 3)`; every proper subsystem has order ≤43.

**Corollary 87-A (odd order).** Every automorphism group of an LSTS(87) has odd
order. *Proof.* By Lemma 3 an involution t has exactly one fixed point and is an
automorphism of its invariant constituent `S_t`, an STS(87). No STS(87) admits
an involution with exactly one fixed point: with m=(v−1)/2=43 transposition
pairs, label the points of each pair by bits; the remaining blocks come in
t-pairs, each giving a triangle on three pair-indices whose xor edge labels
contain 0 or 2 ones, while each index pair needs exactly one xor-1 edge, so
`C(m,2)` must be even; `C(43,2)=903` is odd. (This elementary argument is the
prior dossier's `proof.md` §4; it is the classical reverse-STS condition
v≡1,3,9,19 (mod 24), Doyen/Rosa, Hartman–Hoffman, cited there.) ∎

**Corollary 87-B (order 3).** By Lemma 4 an invariant constituent contains
≡ `2−b_F` (mod 3) of the 3-cycles. f=0: each invariant constituent holds ≡2
(mod 3) of the 29 cycles. f=3: one invariant constituent (all 28 cycles).
f=9: 7 constituents, ≡2 each, 26 cycles: possible. f=15: ≡0 each: possible.
f=21: 19 constituents, ≡1 each, 22 cycles: possible. f=27: 25 constituents,
≡2 each, but only 20 cycles: **impossible**. f=33: ≡0: possible. f=39: 37
constituents, ≡1 each, 16 cycles: **impossible**.

**Corollary 87-C (primes p≥5).** As for v=57 (f≡87 (mod p); f=2 only if p|85 and
then no invariant constituent; otherwise f∈{0,1} or an admissible order ≤43
with an LSTS(f), f≠7): p=5: f∈{2,27,37}; p=7: f∈{3,31}; p=11: f∈{21,43};
p=13: f=9; p=17: f∈{2,19}; p=29: f=0; p=31: f=25; p=37: f=13; p=43: f=1;
p=19,23,41 and 47≤p≤83: none. Hence every prime divisor of `|Aut(L)|` lies in
{3,5,7,11,13,17,29,31,37,43}.

**Proposition 87-D (orbit structure forced for G903).** Let `G=Z43⋊Z21` act on
`{∞}∪Z43×{0,1}` by `(x,j)↦(ax+b,j)`, a in the order-21 subgroup ⟨9⟩ of
`GF(43)*`, ∞ fixed, and suppose G ≤ Aut(L). Then L consists of one G-orbit of 43
constituents with stabilizers the conjugates of `Z21=⟨x↦9x⟩` and two G-orbits
of 21 constituents with stabilizer the translation group Z43.
*Proof.* Every non-translation element of G has order dividing 21 and exactly
the three fixed points `F_c={∞,(c,0),(c,1)}`. By Lemma 2 the order-3 subgroup
`⟨ω_c⟩` fixing `F_c` has exactly one invariant constituent `S_c`, and so does the
order-7 subgroup with the same fixed set, hence `S_c` is the unique constituent
invariant under any nontrivial subgroup of `Z21^(c)`, and `Z21^(c)` stabilizes
it. If `S_c=S_{c'}` with c≠c', it would be invariant under a nontrivial
translation, hence (being also ω_c-invariant) under every ω_{c''}; by Lemma 2 it
would contain all ω_{c''}-cycles, but a pair `{(a,j),(b,j)}` lies in ω_c-cycles
for two values of c, a double cover. So the `S_c` are 43 distinct constituents
forming one orbit with stabilizers exactly `Z21^(c)`. Every other constituent's
stabilizer contains no element of order 3 or 7, so lies in Z43; orbit lengths
are 21 or 903, and 85−43=42 forces two orbits of 21. ∎

The resolution structures used in `code/g87_full.py` are then forced as well for
symmetric resolutions: an ⟨x↦9x⟩-invariant resolution of `S_0` has exactly one
class fixed by the order-3 element (it consists of `F_0` and the 28 ω-cycles)
and two regular orbits of 21; a τ-invariant resolution of a Z43-invariant base
has no fixed class (the 43 blocks through ∞ form one τ-orbit) and hence one
regular orbit of 43 classes.
