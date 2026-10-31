# f262 review B: six-coset nonabelian non-Helly obstruction

Reviewer: ReviewF262SixCosets. Native clock observed before creating this review: 2026-10-29T15:40:21-0700 PDT. Target B SHA-256 `bba2c656d770e13d37d576dcca9fc25366080c1cfff2d1704115658f5fc5c6d7`.

**Result at the reconstructed mathematical scope: 0 FATAL / 0 MAJOR / 0 MINOR.** The six specified LEFT cosets, non-Helly quotient triangle, three exact finite packing values, arbitrary-surjection pullback, and infinite rational-factor example all follow by the arguments below. This is a same-harness written review with one reviewer-owned finite implementation, not human, independent-model-family, formal/kernel, novelty/priority verification, or parent adoption. Historical adoption/provenance and global open-status claims are **INCONCLUSIVE** in this frozen input scope, not findings of falsity.

## Input and process boundary

The entire manifest was SHA-256 checked as `fa7c1dc175cab440eda3e3fc2ce70f2c6f4107c52cc97d6c996cf795076affca`. All seven input SHA-256/byte/LF triples were checked against it **before any source-body read**. The inputs were then displayed completely in manifest order, in raw windows of at most 15 lines, including their endings:

| Order | Input role | SHA-256 | Bytes | LF |
|---:|---|---|---:|---:|
| 1 | Alternating arithmetic overlay | `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793` | 6883 | 56 |
| 2 | Alternating repeated-unit fatal overlay | `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04` | 3056 | 11 |
| 3 | Alternating cardinality overlay | `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218` | 3164 | 10 |
| 4 | f243 CRT additive correction | `775e251a582ffd01de3d1bd3a6e5af770d6be7cf3252cc10c64c201aaf64c26e` | 2329 | 12 |
| 5 | f253 gcd additive correction | `c0e21498f56ebe292ef8745a2d8457f6dcf508ecb567cd0de6f0b7a9bf5540f3` | 2825 | 25 |
| 6 | Target A, read only, **not a premise** | `5365b7b6b7713ff4b500b8186ed556615d1f45de7920545be100711bad3adc7e` | 9144 | 174 |
| 7 | Target B, reviewed here | `bba2c656d770e13d37d576dcca9fc25366080c1cfff2d1704115658f5fc5c6d7` | 8822 | 170 |

The pre-body acknowledgement is `reviewer-B-prebody-ack-v1.json`, SHA-256 `b3217718af218348e1babbe2293dc943626089032c5ecdef079475436eccea81`. It followed manifest and source-metadata verification and preceded source-body reads and derivation. No linked sources, held/f161/f162/selected prime-2/3 bodies, author checker/PASS, prior review bodies, sibling conclusions, external models/APIs, Git, deletion, or publication were used. In particular, the author's disclosure of earlier exposure is preserved, not independently certified or erased. Target A supplied no mathematical premise to this review.

## Per-claim disposition

The entries marked supported mean **F=0, M=0, m=0** at exactly the stated claim; they are not broader acceptance claims.

| Target B claim | Exact verdict |
|---|---|
| Nonabelian `G0=S3 x C2 x C2`, normal `N0`, and quotient `C2^2` | Supported: F=0, M=0, m=0. |
| Three actual order-four subgroups and six specified actual LEFT cosets, indices 6, pairwise disjoint and partitioning `G0` | Supported: F=0, M=0, m=0. |
| Six quotient image lines, non-Helly triple, and factor indices `2*3=6` | Supported: F=0, M=0, m=0. |
| `B7(N0)=6`, `B7(Q0)=4`, `B7(G0)=6` in the stated predicate sense, hence each satisfies Sun8 | Supported: F=0, M=0, m=0. |
| Pullback along **every** surjection onto `G0`, including infinite/nonsplit source groups | Supported: F=0, M=0, m=0 for cosets, indices, partition, quotient images; no arbitrary-source Sun8 or exact packing preservation is inferred. |
| `G0 x (Q,+)` and `N0 x (Q,+)` preserve all three exact values | Supported: F=0, M=0, m=0. |
| Scope exclusions: six is not eight; factors do not both have `B7<=2`; no unrestricted composition disproof | Supported: F=0, M=0, m=0 for this witness. |
| Author's historical exposure descriptions, historical adoption/status of other packets, literature novelty/priority, or global open status of the eight-label problem | **INCONCLUSIVE**: not established by the allowed seven bodies and not needed as a premise. |

## Independent reconstruction of the actual left cosets

Write elements of `G0` as `(t,e,x,y)` for `(r^t s^e,x,y)`, with `t mod 3` and `e,x,y mod 2`. The relation `srs=r^-1` gives

`(t,e,x,y)(u,f,z,w)=(t+(-1)^e u, e+f, x+z, y+w)`.

In particular `sr=r^2 s != rs`, so this group is not abelian. The map `pi(t,e,x,y)=(e,x)` is a surjective homomorphism, with kernel `N0={(t,0,0,y)}` of order 6. Thus `N0` is normal, `N0` is `C3 x C2`, and `G0/N0` is `C2^2`.

Independently spelling out the generators yields, with `b,e,x in F2`,

* `U0={(0,0,x,b)}`;
* `U1={(0,e,0,b)}`;
* `U2={(0,e,e,b)}`.

They are subgroups of order 4: `U0` is the last two factors, and for each of `U1,U2` the listed involutions commute. Right multiplication by an element of one of these subgroups leaves the representative's `t` unchanged; that statement is specifically about **left cosets** `gU`, not `Ug`.

| Label | Representative and subgroup | Exact members `(t,e,x,y)` | Image in `(e,x)` |
|---|---|---|---|
| `C0` | `(1,0,0) U0` | `t=0,e=0`, arbitrary `x,y` | `e=0` |
| `C1` | `(r,0,0) U1` | `t=1,x=0`, arbitrary `e,y` | `x=0` |
| `C2` | `(r^2,1,0) U2` | `t=2,e+x=1`, arbitrary `e,y` | `e+x=1` |
| `C3` | `(s,0,0) U0` | `t=0,e=1`, arbitrary `x,y` | `e=1` |
| `C4` | `(r,1,0) U1` | `t=1,x=1`, arbitrary `e,y` | `x=1` |
| `C5` | `(r^2,0,0) U2` | `t=2,e+x=0`, arbitrary `e,y` | `e+x=0` |

Here `(1,0,0)` and the other three-component representatives in the second column mean elements of `S3 x F2 x F2`; the third column uses four-component coordinates. Each row has four elements, hence index `24/4=6`. Each `t`-layer is split by its two rows, so the six rows are disjoint and cover all 24 elements; every pair has index gcd 6. Orientation is genuinely material: `rU1` contains `rs` but not `r^2s`, whereas `U1r` contains `sr=r^2s`.

For `A_i=pi(C_i)`, the three intersections are

`A0 intersect A1={(0,0)}`, `A0 intersect A2={(0,1)}`, and `A1 intersect A2={(1,0)}`;

there is no common point. Every projected subgroup has index 2. For all three original subgroups, `N0 intersect Ui={(0,0,0,y): y in F2}`, of order 2 and index 3 in `N0`. Thus the original and factor indices are exactly `6=2*3`, not hypothetical index labels.

## Exact packing values

`B7(X)<=k` means that any `k+1` pairwise-disjoint actual finite-index left cosets contain two whose subgroup indices have gcd at least 8. For `N0`, six singleton cosets all have index 6, so `B7(N0)<=5` is false; seven nonempty disjoint cosets cannot fit into its six elements, so `B7(N0)<=6`. Similarly, four singleton cosets of `Q0` have index 4, and five nonempty disjoint cosets cannot fit, giving `B7(Q0)=4`. Repeated subgroups are allowed.

The constructed family proves `B7(G0)<=5` false. For the upper bound, suppose seven disjoint cosets have every pairwise index gcd at most 7. Their indices divide 24. Index 1 cannot occur alongside a second disjoint coset. The remaining possibilities are `2,3,4,6,8,12,24`. Call `8,12,24` high. No high index can repeat, and 24 cannot coexist with 8 or 12, so there are at most two high indices, the pair being 8 and 12 if there are two. Disjointness imposes `sum 1/index <= 1`:

* no high index: the sum is at least `7/6>1`;
* one high index: the other six already sum to at least 1, plus a positive term;
* two: the sum is at least `5/6+1/8+1/12=25/24>1`.

All cases are impossible. Hence `B7(G0)<=6`, and the six-coset lower bound gives equality. Any larger bad family would contain a bad seven-subfamily, so this example produces no seven- or eight-coset bad family in `G0`. This is not an eight-coset counterexample, and the exact factor values 6 and 4 are **not** both at most 2.

## Arbitrary surjection and infinite rational pullback

Let `rho:G -> G0` be any surjective homomorphism, set `N=rho^-1(N0)`, and choose `g_i` mapping to each displayed representative. Put `V_i=rho^-1(U_i)`. Then

`g_i V_i = rho^-1(C_i)` and `[G:V_i]=[G0:Ui]=6`.

These equalities prove actual left-coset orientation, the six-way partition, and all pairwise gcds directly, without finiteness or a splitting of `rho`. Normality of `N` and the first isomorphism theorem give `G/N ~= G0/N0`; consequently the same six images and non-Helly triangle occur. This argument does **not** give arbitrary `G` or `N` an upper packing bound or Sun8.

For the stronger infinite example let `D` be any group with no proper finite-index subgroup, in particular `(Q,+)`, and let `G=G0 x D`, `N=N0 x D`. If `W` is finite-index in either direct product, the natural map of left-coset **sets** `D/(W intersect D) -> G/W` (or the analogous map into `N/W`) is injective. Therefore `W intersect D` has finite index in `D` and equals `D`, even when `W` is not normal. A subgroup containing `1 x D` is exactly the full preimage of its projection to `G0` or `N0`. Thus finite-index subgroups, their left cosets, indices, disjointness, and possible bad-family sizes correspond in both directions to those of the finite factor. `G/N ~= Q0`, so the exact values remain `6,4,6`.

For `D=(Q,+)`, if `H` has finite index `m`, then for any rational `q`, the order of `q/m+H` in the finite quotient divides `m`; hence `q=m(q/m)` lies in `H`. Therefore `H=Q`. The six pulled-back cosets are infinite actual subsets of the infinite group, not finite cosets relabelled as infinite.

## Final reviewer-owned exact controls

After the written reconstruction, a standard-library-only reviewer implementation was run, without reading author code or candidate bodies. Checker: `reviewer-B-finite-control-v1.py`, SHA-256 `63bce021f585950e310ba5f4af00e2f10c354c798941ca5db6901514c82752c8` both before and after execution. Receipt: `reviewer-B-finite-control-receipt-v1.json`, SHA-256 `a62c8f649c0781cf74d54648af41ef3ff8bbf3f9d5f012706ee2c48ee31cd3b9`. Native clocks: start `2026-10-29T15:39:49-0700 PDT`, end `2026-10-29T15:39:50-0700 PDT`; total monotonic elapsed `0.46493691578507423` seconds, under the 120-second cap. Each listed case was a separate process; receipt records its actual command, exit, output, reason, native clocks, and hashes.

The positive case **exited 0**. It used actual permutation composition for `S3`, not the written `(t,e)` multiplication formula; checked group laws, actual generated subgroups and left cosets, normal kernel and quotient homomorphism, exact partition, projected lines and triple intersections, and singleton and six-coset lower witnesses. It enumerated 54 subgroups, obtained proper indices `2,3,4,6,8,12,24`, and checked all 428 seven-index multisets with pairwise gcd at most 7 using exact rational masses: the minimum was `25/24`. The handwritten packing proof above is independent of that enumeration. The checker does not execute or prove the arbitrary/infinite universal assertions; those are the written argument above.

Every intended negative below **actually exited 2** and reported its own exact expected reason, rather than an arbitrary exception:

| Mutation | Required observed reason |
|---|---|
| Replace `rU1` by `U1r` | `ORIENTATION_NOT_LEFT` |
| Duplicate one coset | `PARTITION_OVERLAP` |
| Drop a coset | `PARTITION_COVERAGE` |
| Change a claimed index from 6 to 7 | `COSET_INDEX` |
| Replace the projected diagonal line | `PROJECTED_LINE_MISMATCH` |
| Supply a disjoint pair in the supposed triangle | `NONHELLY_PAIR_EMPTY` |
| Supply a triangle with a common point | `NONHELLY_TRIPLE_NONEMPTY` |
| Corrupt the quotient map | `QUOTIENT_HOMOMORPHISM` |
| Replace the kernel by the nonnormal `U1` | `KERNEL_NOT_NORMAL` |
| Duplicate a singleton in a bad family | `BAD_FAMILY_OVERLAP` |
| Replace nonabelian multiplication by the abelian exponent rule | `S3_CONJUGACY_RELATION` |
| Change the threshold to 8 | `PACKING_POSSIBLE_SEVEN` |

For the last control the code first constructs seven distinct actual cosets of an index-8 subgroup and verifies their gcds are at most 8. Its arithmetic search also rejects the mutated seven-type bound with a mass-1 index multiset `[3,8,8,8,8,8,24]`; this multiset is an arithmetic compatibility control, not asserted to be an actual partition.

## Remaining gap and assurance ceiling

The finite and infinite witnesses establish an actual low-original-gcd non-Helly six-label obstruction while both factors satisfy Sun8, but they do not settle any eight-label implication, produce eight bad cosets, or meet the much stronger `B7(N),B7(Q)<=2` assumptions. Whether a broader theorem is already known or new is outside this input-only review. The target's references to prior adoption, prior reviews and historical provenance are not independently certified here; all existing holds and restrictions remain in force. There is no independent model-family or human review, formal/kernel checking, priority search, or parent adoption in this result.
