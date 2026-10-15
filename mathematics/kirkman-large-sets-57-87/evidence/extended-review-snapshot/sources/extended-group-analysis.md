# Extended group actions: exact reductions, not target constructions

Date: 2026-10-14 (PT). Scope: LKTS(57)/LKTS(87), with the development actions explicitly stated below. No novelty is claimed for these elementary deductions. In particular, the reverse-STS obstruction at 87 is classical, not a newly discovered existence obstruction. The full target problems remain unresolved here.

## 1. Block automorphisms are stronger constrained than the previous resolution argument showed

Put `X=Z_n ∪ {u,w}`, with `gcd(n,6)=1`, and let translations fix both infinities. A **transversal STS** contains one triple from every translation orbit. Its translates form a large set of STSs; it gives an LKTS only if this base STS has a resolution. All arguments in this section concern the **block set alone**.

### 1.1 Fixed-orbit versus fixed-block lemma

**Lemma.** A nonidentity scalar involution `g:x↦ax` on `Z_n`, fixing u and w individually, cannot preserve a transversal STS on X.

Write `m=gcd(a−1,n)`, `f=m+2`, and `t=(n−m)/2`. The point permutation has f fixed points and t transpositions.

1. Every translation orbit of triples is free: a triple stabilizer has order dividing both n and 6. For a triple T with k finite points (`k=1,2,3`), define its finite-point center by

   `c(T)=k^(-1) Σ_{x∈T∩Z_n} x mod n`.

   The inverse exists. We have `c(T+s)=c(T)+s` and `c(gT)=a c(T)`. Consequently every translation orbit has a unique centered representative, and scalar multiplication acts equivariantly on centered representatives.

2. A g-fixed translation orbit has a g-fixed centered representative T. Its translate `T+s` is g-fixed precisely when `(a−1)s=0`: otherwise `T+as=T+s` would give a nontrivial translation stabilizer. Thus every fixed orbit has exactly m setwise-fixed triples, and a nonfixed orbit has none.

3. Among *all* triples on X, exactly `binom(f,3)+ft` are g-fixed. They have either three fixed points or one fixed point together with one point-transposition. Hence the number of fixed translation orbits is

   `O = [binom(f,3)+ft]/m = f(f−1)/6 + ft/m`.

4. In any g-invariant STS, fixed points carry an STS(f), accounting for `f(f−1)/6` fixed blocks. Each transposition pair completes with a fixed point, accounting for exactly t further fixed blocks. There are no others. Thus

   `B = f(f−1)/6 + t`.

5. A g-invariant transversal supplies an equivariant bijection from its blocks to translation orbits, so it would require `O=B`. Instead

   `O−B = 2t/m = n/m−1 > 0`.

This contradiction uses no resolution or class action.

The following counts were independently enumerated from the actual triples and translation orbits by `work/group_screen.py`, rather than inferred only from the formula:

| n | a | m | Fixed points f | Fixed triple orbits O | Required fixed STS blocks B |
|---:|---:|---:|---:|---:|---:|
| 55 | 21 | 5 | 7 | 42 | 32 |
| 55 | 34 | 11 | 13 | 52 | 48 |
| 55 | 54 | 1 | 3 | 82 | 28 |
| 85 | 16 | 5 | 7 | 63 | 47 |
| 85 | 69 | 17 | 19 | 95 | 91 |
| 85 | 84 | 1 | 3 | 127 | 43 |

The receipt is `evidence/group-arithmetic.json`. The previously conceivable block-set-only involutions 34 and 69 are therefore excluded, not merely their invariant resolutions.

### 1.2 Consequence: every nonidentity scalar is excluded, even without a resolution

Every even-order scalar has a nonidentity involution power, so §1.1 eliminates it. `U(85)` has order 64, eliminating all its nonidentity elements.

For n=55, `U(55)≅U(5)×U(11)` has exponent 20. A remaining nonidentity odd-order element must have order 5; it is 1 modulo 5 and has order 5 modulo 11. Its finite fixed set is the subgroup H of order 5. The fixed points `H∪{u,w}` would carry a transversal STS(7) for H-translations. This is impossible by `proof.md` §3: after normalizing `{u,w,0}`, the only perfect matching of `H\{0}` using both unsigned differences is `{{1,4},{2,3}}`, forcing the same finite pairs at both infinities.

Thus **no nonidentity scalar fixing both infinities preserves the base block set at either target**, regardless of how a resolution is chosen. This strengthens, and does not invalidate, the previous invariant-resolution theorem. It does not eliminate arbitrary cyclic base KTSs or automorphisms outside the normalizer of the specified translation action.

### 1.3 An independent order-four matching obstruction

This simpler intermediate argument is useful independently of cyclic transversality. Suppose an STS automorphism has f fixed points, t odd point 4-cycles, and no point 2-cycles. For a fixed point z, blocks through z and moving points induce a g-invariant perfect matching on the 4t moving points. An individual 4-cycle must either be paired to another whole 4-cycle, or be internally matched by its two opposite edges. Because t is odd, at least one internal opposite matching is needed for every z. Different fixed points cannot use the same opposite pair. Hence `f≤t`.

For multiplier 12 modulo 55, `(f,t)=(13,11)`; for multipliers 18/52 modulo 85, `(f,t)=(19,17)`. These models are impossible already as STSs. This was the reason for stopping the first new scalar search before §1.1 was found; the general fixed-orbit argument now subsumes it.

## 2. Complete affine-normalizer classification at the two targets

Consider an affine action on finite points, `x↦ax+b`, preserving the set `{u,w}`. If it preserves the base STS, the unique block `{u,w,r}` forces `ar+b=r`. Translating r to 0 makes the finite action scalar. Thus §1 also excludes every nonidentity affine block automorphism fixing both infinities individually.

The kernel of the induced action of an affine base-automorphism group on `{u,w}` is therefore trivial. Such a group has order at most two. In particular, **any surviving nonidentity affine base automorphism must be an involution exchanging the infinities**; allowing higher-order affine maps introduces no additional case.

For completeness, a finite affine map is involutory exactly when

`a²=1 mod n`, `(a+1)b=0 mod n`.

Since n is odd, `c=b/2` is a fixed point: `ac+b=c`. Conjugating by the translation to c removes b. This identity was checked for every allowed b for the four involutive multipliers at each n in `group_screen.py`.

With the infinities **exchanged**, the fixed-point count is now `m=gcd(a−1,n)`, not m+2:

| n | Scalar a after translation | Fixed finite points | Disposition |
|---:|---:|---:|---|
| 55 | 1 | 55 | A proper fixed STS(55) inside STS(57) is too large |
| 55 | 21 | 5 | STS(5) is inadmissible |
| 55 | 34 | 11 | STS(11) is inadmissible |
| 55 | 54=−1 | 1 | Not excluded; the surviving reverse model |
| 85 | 1 | 85 | A proper fixed STS(85) inside STS(87) is too large |
| 85 | 16 | 5 | STS(5) is inadmissible |
| 85 | 69 | 17 | STS(17) is inadmissible |
| 85 | 84=−1 | 1 | No reverse STS(87) exists |

For the proper-subsystem bound, a point outside a fixed subsystem of order f must pair its f fixed neighbours with distinct other outside points, so `f≤v−f−1`. This applies here to f=55 or 85. Fixed sets of size 5,11,17 cannot be STSs because their orders are 5 modulo 6.

The last row is a **classical reverse-STS obstruction**, not a new theorem of this investigation. Hartman–Hoffman, *Steiner Triple Systems with an Involution*, [DOI 10.1016/S0195-6698(87)80045-8](https://doi.org/10.1016/S0195-6698(87)80045-8), records the one-fixed-point spectrum `v≡1,3,9,19 mod24`; the author's [primary page](https://research.ibm.com/publications/steiner-triple-systems-with-an-involution) states it. The elementary parity necessity in `proof.md` §4 suffices here: for `(v−1)/2=43`, `binom(43,2)=903` is odd. The classical spectrum permits 57, but says nothing about cyclic transversality or resolvability.

**Exact remaining normalizer possibilities:** a cyclic-transversal base STS(87) must have trivial affine-normalizer stabilizer. At 57 that stabilizer is trivial or generated by negation exchanging the infinities, after normalizing the infinity-pair block. This is not a claim about arbitrary STS automorphisms.

## 3. Negation exchanging the infinities at 57

Let τ negate `Z_55`, exchange u and w, and fix 0. The 28 point-transposition pairs are `{u,w}` and `{d,−d}`, `1≤d≤27`.

### 3.1 Exact block-set reduction, with no invariant resolution

All 28 blocks through 0 are forced: `{0,u,w}` and `{0,d,−d}`. Every other block uses one point from each of three different transposition pairs, and occurs together with its τ-image. Collapsing each transposition pair to one of 28 vertices gives a signed twofold triple system:

- A row chooses three distinct pair-indices and three endpoint bits, modulo simultaneous complementation: four signings per index triple.
- Its two physical triples cover three edges on the index set. Label an edge by the xor of its endpoint bits. The three labels have xor zero.
- For each pair of indices, its xor-0 and xor-1 edges must each occur exactly once.
- A selected signed row must occupy two distinct cyclic triple orbits, neither already occupied by one of the 28 forced blocks; all 504 remaining cyclic triple orbits must be occupied exactly once.

There are exactly 252 selected signed rows (`28+2·252=532` blocks). These conditions are necessary and sufficient for a τ-invariant cyclic-transversal **STS**, not yet a KTS. This is the first-stage object searched by `work/group_blockset.py --multiplier 54 --swap-infinities`, using full block-orbits rather than assuming any class action.

A second-stage unrestricted resolution has one color per physical block, 28 colors, and all incident blocks at every point have distinct colors. Each point is incident with 28 blocks, so each color is a parallel class. Color names are fixed only by sorting the 28 blocks through point 0. **The two blocks of a τ-orbit are allowed different colors.** This enlarges the original reflection search, which forced every class to be τ-fixed.

Each returned first-stage block set is checked directly for exact pair coverage, one representative of every cyclic triple orbit, and τ-invariance. On a successful coloring, the program develops all 55 translates in the existing plain `LKTS/KTS/CLASS` format and invokes `work/check_lkts.py`.

### 3.2 The stricter invariant-resolution object

If a chosen resolution is τ-invariant, the one-fixed-point incidence lemma in `proof.md` §7 forces all 28 classes to be fixed. Class i contains the block `{0,p_i,τp_i}`. Its other 18 blocks are nine signed rows partitioning the remaining 27 pair-indices.

Thus the stricter model is exactly a signed near-resolution of a `2-(28,3,2)` index design: class i omits index i; every index-pair appears with xor 0 and xor 1; each triangle has xor-zero edge labels; and the cyclic triple-orbit restrictions of §3.1 hold. An unsigned near-resolution alone is insufficient: sign compatibility and cyclic transversality remain essential.

The involution itself is not eliminated by the new fixed-orbit count: its fixed cyclic triple orbits are the one infinity-pair orbit and the 27 finite arithmetic-progression orbits, exactly matching its 28 forced fixed blocks.

## 4. C29 on three 29-point orbits at order 87

Here the group acts on the **entire large set and its chosen resolutions**. A block-set automorphism of a fixed constituent without an invariant resolution does not suffice for the following argument.

Let f constituents be fixed. Since `85−f` is divisible by 29, initially `f∈{27,56,85}`. A fixed KTS has 43 classes. Its class action has either 14 fixed classes and one 29-orbit, or 43 fixed classes. A fixed parallel class is a full 29-block orbit and must contain only triples transversal to the three point-orbits. All 43 classes cannot be fixed, since then within-layer point-pairs would never be covered. Thus **each fixed constituent has exactly 14 fixed classes and one free 29-orbit of classes**.

Take a seed parallel class P for the free class orbit. Its 29 blocks represent 29 distinct block-orbits: two representatives from the same orbit would make P overlap one of its nontrivial translates. Let A,B,C count its block-orbits of types AAA, AAB, ABC. Covering the 42 within-layer pair-orbits gives

`A+B+C=29`, `3A+B=42`, hence `B=42−3A`, `C=2A−13`.

Therefore `A≥7`. In each individual layer there are `binom(29,3)/29=126` triple-orbits, but exactly 14 are arithmetic-progression orbits. An AP orbit repeats a within-layer pair orbit, so cannot occur in any fixed STS. Conversely, a triple with repeated unsigned pair difference is an AP; there are no other rejected AAA orbits. There are only

`3·(126−14)=336`

usable AAA orbits in all. Consequently `7f≤336`, eliminating both f=56 and f=85. **Only 27 fixed constituents and two free 29-orbits can survive.** The full finite enumeration and the 14 forbidden canonical AP representatives appear in `evidence/group-arithmetic.json`. The C19 sibling independently used the analogous stronger AP bound to eliminate 36 fixed constituents at 57; its proof and search are owned separately.

### 4.1 Exact seed incidence signatures

Let `A_i` count AAA seed blocks in layer i; let `B_ij` count blocks with two points in layer i and one in layer j. Put `S_i=Σ_{j≠i}B_ij`, `T_i=Σ_{j≠i}B_ji`. Pair coverage and the seed class point partition respectively give

`3A_i+S_i=14`, `3A_i+2S_i+T_i+C=29`.

Thus

`0≤A_i≤4`, `S_i=14−3A_i`, `T_i=3A_i+1−C`, `C=2ΣA_i−13`.

In particular, `7≤A≤12`. For fixed A_i, all nonnegative off-diagonal integer matrices B can be specified by `x=B_01`. Set `K=T_1−S_2+T_0`. Then

`max(0,K−S_1,K−T_0) ≤ x ≤ min(S_0,K,S_2+K−T_0)`.

The other five entries follow from the row and column sums. Exact enumeration gives respectively **18,12,7,6,3,1** feasible ordered A_i signatures for A=7,8,9,10,11,12. These are only aggregate signatures, not constructed blocks.

### 4.2 The exact missing global object

A construction in this action requires:

1. 27 pairwise disjoint fixed KTSs, each specified by 14 fixed transversal class-orbits and one 29-class orbit with the seed signature above.
2. Two ordinary resolved KTS seeds, each containing at most one triple from any C29 orbit, whose 29 translates are pairwise disjoint.
3. Across these fixed and free constituents, every one of the 3,655 triple-orbits assigned exactly once: a fixed constituent consumes full orbits, while a free seed consumes one representative per assigned orbit.

The fixed constituents consume `27·43=1,161` triple-orbits. The two free seeds must consume the remaining `2·1,247=2,494`. In particular **all 42 forbidden-AAA AP orbits must occur in the two free seeds**, never in the fixed constituents. No such coupled package is constructed here; eliminating the 56-fixed pattern does not solve the surviving 27-fixed case.

## 5. A genuinely noncyclic regular route at 57

Changing from `Z_55` to CRT coordinates `Z_5×Z_11` changes nothing. A genuinely different regular group of order 55 is

`G=C_11 ⋊ C_5`, `(x,y)(x',y')=(x+3^y x' mod11, y+y' mod5)`.

Here `3^5=1 mod11` and 3 has order 5. The group is nonabelian. Let it act by left multiplication on its 55 points and fix u,w. All triple orbits have length 55, because their stabilizers have order dividing both 55 and 6. The infinity-pair completion map bijects the 55 constituents of any G-invariant LKTS with G, so its constituent action is necessarily regular. Equivalently, this route requires one resolved KTS transverse to the G triple-orbits.

This is not the scalar model eliminated in §1: G is the **development group**, not a group fixing one base block set. At 87 there is no analogous nonabelian group of order 85: Sylow counting makes both the order-5 and order-17 subgroups normal, hence the group is cyclic. Smaller development groups or other point-orbit decompositions are not excluded.

### 5.1 Exact two-infinity starter package

Normalize the base infinity-pair block to `{u,w,e}`. For a finite edge `{a,b}`, its left-translation pair orbit is the inverse class `[a^(-1)b]={a^(-1)b,b^(-1)a}`. There are 27 such nonidentity classes.

A sufficient and necessary auxiliary package for the regular G route is:

- Two edge-disjoint perfect matchings `M_u,M_w` on `G\{e}`, each using every nonidentity inverse-difference class exactly once.
- A bijection π from M_u to M_w pairing only edges with disjoint endpoints.
- 477 finite triangles, covering exactly once every edge of `K_G − M_u − M_w`, and representing exactly once every G-orbit of finite triples.
- A partition of those triangles into one class of 18 triangles partitioning `G\{e}`, and 27 classes of 17 triangles: for each `E∈M_u`, its triangles partition `G\(E∪π(E))`.

Attach `{u,w,e}` to the first class and `{u}∪E`, `{w}∪π(E)` to the other classes. The pair conditions give an STS, the point partitions give its resolution, and orbit transversality gives the full LKTS by G-development. Conversely every such base KTS yields this package.

The π condition itself is not an additional obstruction once the two starters are edge-disjoint: an edge of one matching meets exactly two edges of the other, so the allowed bipartite graph is 25-regular and has a perfect matching. The difficult still-missing object is the **simultaneous transverse triangle decomposition and its specified point-disjoint class complements**, not just a pair of starters. No Frobenius construction is claimed, and the extended solver allocation was instead directed to the surviving reflection model of §3.

## 6. Executable evidence and interpretation

- `work/group_screen.py`: standard-library exact enumeration of all 104 units, the six scalar involutions' fixed triples/orbits, all affine involution offsets, and the C29 forbidden orbits/signatures. Output: `evidence/group-arithmetic.json`.
- `work/group_blockset.py`: exact block-orbit pair/triple-orbit cover followed by unrestricted block coloring. It records source/helper/checker hashes, every model hash, precise restrictions, parameters, seeds, deadlines, solver calls, and any candidate block sets. An UNKNOWN coloring excludes no resolution; its base is skipped only as a bounded search decision, not certified nonresolvable.
- `evidence/group-blockset9-a2.*`: the initial pipeline produced a full checked LKTS(9).
- `evidence/group-reflection9.*`: the infinity-swapping pipeline likewise produced a full checked LKTS(9).
- The short new a12 and a34 runs were stopped as soon as the proofs above eliminated them. Original incomplete receipts/logs are preserved; `group-blockset57-a12-cancellation.json` and `group-blockset57-a34-cancellation.json` record cancellation and honest runtime bounds. Neither is labelled solver-UNSAT. Their original source is `evidence/group-blockset-initial-source.py`.

Reproduce the surviving target search from the project directory, using a fresh output prefix:

```sh
env UV_CACHE_DIR=/tmp/lkts-uv-cache OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  uv run --offline --with ortools==9.15.6755 python work/group_blockset.py \
  --v 57 --multiplier 54 --swap-infinities --seconds 7200 --block-seconds 7200 \
  --resolution-seconds 240 --max-candidates 1000 --threads 2 --seed 2905 \
  --output /tmp/group-reflection57-replay
```

The 7,200-second total deadline includes construction and all staged solver calls; no resolution invariance is imposed. A target success requires the final expanded certificate to pass `check_lkts.py`, not merely finding a transversal STS.

## 7. Additional F55 search slice

The later allocation explicitly added a Frobenius slice, superseding only the earlier allocation statement at the end of §5.1; the mathematical package there is unchanged.

`work/group_frobenius.py` implements the full staged package without imposing any base automorphism:

1. Two perfect matchings of the 54 nonidentity points, with every inverse-difference class appearing once per matching and no shared edge.
2. An exact cover of all remaining finite pairs and all 477 finite triple-orbits by finite triangles, with each sampled matching pair frozen for that stage.
3. The same unrestricted 28-color resolution model used by the reflection runner. A positive result is developed by **left multiplication in F55**, not cyclic addition, and checked with the existing independent checker.

The code validates the complete 55-element multiplication table for identity, two-sided inverses, associativity and noncommutativity. It explicitly enumerates all full triple-orbits, checking 532 orbits of length 55, of which 477 are finite. Every CP-SAT call saves its **actual `.pbtxt` instance**, instance hash, exact solver parameter text, stage identifiers, limits and observed result in a JSONL ledger. Sampled matching pairs and any base STSs are preserved with their hashes.

The 40-second preliminary run `evidence/group-frobenius57-smoke.json` found **three verified edge-disjoint inverse-difference starter pairs**. Its three finite-triangle calls returned UNKNOWN; no base STS or KTS certificate was produced. Thus the infinity-starter prerequisite was actually constructed in this nonabelian action, while the transverse finite-triangle completion remained missing.

The additional long slice is configured for 7,200 total seconds, **one solver worker**, seed 5501, 5 seconds per starter call, 300 seconds per finite-triangle call, 180 seconds per unrestricted-resolution call, and at most three base candidates per starter. Its prefix is `evidence/group-frobenius57-extended`. The reflection slice remains independent and uses two workers. Every OMP/BLAS thread environment limit is one. The same caveat applies to this staged search: changing a frozen starter after UNKNOWN is a search decision, not a proof that it has no completion.

```sh
env UV_CACHE_DIR=/tmp/lkts-uv-cache OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  uv run --offline --with ortools==9.15.6755 python work/group_frobenius.py \
  --seconds 7200 --starter-seconds 5 --triangle-seconds 300 --resolution-seconds 180 \
  --candidates-per-starter 3 --threads 1 --seed 5501 --output /tmp/group-frobenius57-replay
```
