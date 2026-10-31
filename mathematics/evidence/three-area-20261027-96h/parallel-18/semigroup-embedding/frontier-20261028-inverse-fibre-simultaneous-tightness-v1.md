# A canonical semilattice model makes every inverse-fibre maximum tight simultaneously

**NEW WRITTEN AUTHOR CANDIDATE; unreviewed and unadopted.** Native prewrite observation **Wed Oct 28 18:13:30 PDT 2026**. This supplies an explicit construction for a classical locally-inverse subclass and an exact bridge from the source RF condition to a simultaneously tight Rees model. No novelty, independent-model review or full original-target closure is claimed.

## 1. Exact theorem and its scope

Let A be ANY nonempty inverse semigroup, finite or infinite and not necessarily unital, with an onto idempotent-pure group homomorphism θ:A→G. Let I,Λ be nonempty, P any A-valued sandwich matrix, and let the FULL Rees semigroup `S=M[A;I,Λ;P]` be regular and satisfy the printed weak-E condition.

**Claim.** S has an explicit faithful physical host with a **semilattice** band and a completely simple Rees actor. Under the separately written pure-onto-CS pushforward in §8, this host transfers to the SAME actual syntactic quotient q_τ, so κ_q is faithful and both same-q R/L idempotent separations hold.

The construction is simultaneous for **every** matrix entry: it does not choose one best fibre, assume P consists of units or require a group-homomorphic choice of fibre maxima. S is locally inverse by the direct local-corner argument recalled in §7; thus this is within the already known locally-inverse/printed-Fact-1 subclass. It is not a new solution of the full locally r-orthodox problem or printed Question 2.

The ordinary E-unitary inverse-semigroup band-by-group embedding is classical: see O'Carroll's embedding theorem as summarized in [Szendrei's 2019 survey §5](https://arxiv.org/html/1909.05280v1#S5), and the [Hartmann thesis, Theorem 2.6](https://doktori.bibl.u-szeged.hu/id/eprint/1183/3/HM_angtezis.pdf). The proof below reconstructs an explicit model and the **additional simultaneous-tightness property** directly. Whether that property/argument is previously known has not been cleared; no claim of novelty or independent clean cognition is made.

## 2. Reduce the source hypothesis to exact fibre maxima

The exact theorem in `frontier-20261028-rees-reverse-fibre-weu-v1.md`, SHA `96b34ec43125dabe1e9cc33cdc7055c37b0933a1f5c81a424913b5dd5230f52b`, proves for any pure-group base that S's weak-E condition is equivalent to

`a p a=a` for EVERY p in P and EVERY a with `θ(a)=θ(p)^(-1)`. (RF)

For an inverse A, `frontier-20261028-rees-local-corner-fibre-maxima-v1.md`, SHA `af71b4d3c7765ada362b99b6dbfc096d6635b165486800d8a6620b901c4b3133`, proves RF for p iff p is the **greatest element** in its own θ-fibre in the natural partial order. Those prior records are current written candidates, not peer-adopted imports; the decisive algebra is as follows. For θ(a)=θ(p)^(-1), both ap and pa are idempotent. If apa=a, commuting source idempotents give `(a^(-1)a)p=a^(-1)=p(aa^(-1))`, so a^(-1)≤p. Conversely if x=a^(-1)≤p, inverse-semigroup order gives `x=p x^(-1)x`; multiplying `x=p a x` on both sides by a yields apa=a. Thus all actual P entries are fibre maxima, with no finite-fibre or unique group-section assumption.

We first work with a MONOID. If A lacks identity, adjoin a formal 1 and extend θ(1)=1_G; purity and inverse-semigroup structure persist. Any P entry with θ(p)≠1 remains the maximum of the same unchanged fibre. If some P entry has θ(p)=1, RF makes p the maximum of all idempotents of A. Then for every a, the idempotents aa^(-1),a^(-1)a lie below p, so `pa=a=ap`; p is already an identity and A was a monoid. Thus EVERY P entry remains a fibre maximum in the appropriate monoid A¹, including the identity-image boundary. We do not silently identify a formal adjoined unit with an existing source element.

Henceforth A denotes this monoid, with identity1; restriction back to the original nonunital source is addressed in §7.

## 3. An explicit group-indexed idempotent preorder

Let E=E(A), a semilattice. On G×E define `(g,e)~(h,f)` iff there is an actual s∈A with

`h=g θ(s)`,   `e≤s s^(-1)`,   `f=s^(-1)e s`.                 (3)

This is an equivalence, not an informal path quotient. Reflexivity uses s=1. Symmetry uses s^(-1): if (3) holds, then `f≤s^(-1)s` and `s f s^(-1)=e`. For transitivity, if e is carried to f by s and f to k by t, then `f≤tt^(-1)` implies `e≤s tt^(-1)s^(-1)=(st)(st)^(-1)`, and `(st)^(-1)e(st)=t^(-1)ft=k`. Thus a single witness st realizes the composite. These equalities use the standard inverse-semigroup law `(st)^(-1)=t^(-1)s^(-1)` and commuting idempotents.

Let Y=(G×E)/~. Define a relation on Y by

`[g,e] ≼ [h,f]` iff some s∈A satisfies
`θ(s)=g^(-1)h`, `e≤ss^(-1)`, and `s^(-1)e s≤f`.          (4)

It is a well-defined preorder. To verify representative independence, suppose `(g,e)~(gθ(u),u^(-1)eu)` and `(h,f)~(hθ(v),v^(-1)fv)`. If s witnesses (4), then `u^(-1)s v` has the required new group coordinate. The bounds `e≤uu^(-1)`, `s^(-1)e s≤f≤vv^(-1)` imply the new source support condition, and conjugation gives

`(u^(-1)sv)^(-1)(u^(-1)eu)(u^(-1)sv)`
`=v^(-1)s^(-1)e s v≤v^(-1)f v`.

Reflexivity uses1. For transitivity, witnesses s,t have the composable group labels; `s^(-1)e s≤f≤tt^(-1)` gives the support condition for st and `(st)^(-1)e(st)≤t^(-1)ft≤k`. Antisymmetry is NOT assumed or needed.

Left translation `L_z[g,e]=[zg,e]` is a well-defined order automorphism for every z∈G: the label ratio `g^(-1)h` is unchanged. It acts on the powerset semilattice `B=P(Y)` by `α_z(A)=L_z(A)`, with multiplication intersection. For z∈Y write `↓z={y:y≼z}`.

## 4. The universal semidirect coefficient identity

For any s∈A define `e_s=ss^(-1)` and

`b_s=↓[1_G,e_s] ∈B`.                                        (5)

We prove for ALL s,t∈A,

`b_s ∩ α_(θ(s))(b_t)=b_(st)`.                              (6)

The right-hand side is contained in b_s because `e_(st)=s(tt^(-1))s^(-1)≤e_s`. It is contained in α_(θ(s))(b_t) because s itself witnesses `[1,e_(st)]≼[θ(s),e_t]`.

For the reverse inclusion take an arbitrary `[k,d]` in both sides of the left-hand intersection. The two preorder witnesses give elements a,b with

`θ(a)=k^(-1)`, `d≤a e_s a^(-1)`,
`θ(b)=k^(-1)θ(s)`, `d≤b e_t b^(-1)`.

Put `v=a^(-1)d a` and `c=a^(-1)b`. Then d=a v a^(-1), `v≤e_s`, `v≤c e_t c^(-1)`, and θ(c)=θ(s). Purity makes `z=s^(-1)c` idempotent. Consequently

`v ≤ ss^(-1)c e_t c^(-1)ss^(-1)`
`  = s z e_t z s^(-1) ≤ s e_t s^(-1)=e_(st)`.

Thus a witnesses `[k,d]≼[1,e_(st)]`. This proves (6) for arbitrary (possibly noncommuting) G and every source element. It uses only the purity of θ and semilattice order of actual idempotents.

## 5. Faithfulness of the base model

If `↓[1,e]=↓[1,f]` for idempotents e,f, each generator lies in the other's downset. A witness for `[1,e]≼[1,f]` has group label1 and hence is an idempotent by purity. Its support condition then gives e≤f. Conversely 1 witnesses the relation whenever e≤f. Symmetrically f≤e, so e=f. Therefore the principal downsets in (5) separate all source idempotents.

The map

`ι:A→B⋊G`,     `ι(s)=(b_s,θ(s))`

is a homomorphism by (6). To prove it faithful, suppose the two coordinates agree for s,t. Then `e_s=e_t` by the preceding paragraph. Also `d=s^(-1)t` has θ(d)=1, so it is idempotent by purity, and `d≤s^(-1)s`. Equality of range idempotents gives `t=(ss^(-1))t=s d`. Thus

`tt^(-1)=s d s^(-1)=ss^(-1)`.

Conjugating by s^(-1),s and using `d≤s^(-1)s` gives `d=s^(-1)s`, so t=s. This proves a faithful model over the ACTUAL θ, without postulating an embedding theorem, a finite witness, or an abstract quotient map.

## 6. Every fibre maximum is tight, simultaneously

Let p be the maximum of its θ-fibre g. Put `e0=b_1=↓[1,1]`. We prove

`b_p=e0 ∩ α_g(e0)`.                                        (7)

The inclusion from right to left is immediate: `e_p≤1`, and p witnesses `[1,e_p]≼[g,1]`.

Conversely let `[k,d]∈e0∩α_g(e0)`. Its two witnesses a,b satisfy

`θ(a)=k^(-1)`, `d≤aa^(-1)`,
`θ(b)=k^(-1)g`, `d≤bb^(-1)`.

Put `v=a^(-1)d a` and `c=a^(-1)b`. Then θ(c)=g and `v≤cc^(-1)`. By maximality c≤p. In an inverse semigroup c≤p implies `cc^(-1)≤pp^(-1)` (write c=f p for an idempotent f and compute `cc^(-1)=f pp^(-1)`). Hence `v≤e_p`, and a witnesses `[k,d]≼[1,e_p]`. This proves (7) simultaneously for EVERY fibre in which a greatest element exists.

The equality is the tight condition `b_p=e0 α_(θ(p))(e0)` required by the preceding Rees lift. It does **not** say every group fibre has a maximum, that the maximal elements form a subsemigroup, or that tightness is independent of the chosen representation. The same finite source can have a different faithful model in which p is nontight, as the previously pinned tight-subset counterexample shows.

## 7. The actual regular Rees source and physical host

Return to the original A, possibly without an identity. By §2 every P entry is a maximum in its corresponding θ-fibre, and remains so in the monoid A¹. The source elements themselves still have middle coordinates in A. Construct the exact actor

`D=M[G;I,Λ;θ(P)]`

and define `j(i,a,λ)=(b_a,(i,θ(a),λ))` in the whole physical product `P(B,D)`. Equation (6) gives ι_A as a faithful semidirect-product representation, and (7) makes every P entry tight **at once**. The exact tight-lift calculation yields

`b_(a p c)=b_a ∩ α_(θ(a)θ(p))(b_c)`

for every a,c in A¹ and every P entry p. Therefore j is a homomorphism on EVERY actual source product. Equal j-images have the same source row/column and the same ι_A(a), so j is injective.

The band B=P(Y) is a semilattice, hence a normal/seminormal band. D is completely simple. This is a genuine explicit printed-Fact-1-compatible physical host for S. S was assumed regular and weakly E-unitary; it is also locally inverse: for e=(i,a,λ) idempotent and p=P_(λ,i), the map `(i,b,λ)↦b p` injects the actual regular local monoid eSe into the inverse-semigroup corner `(ap)A(ap)`. An inverse in eSe exists by regularity and must coincide with the unique inverse in A. Thus this family is not presented as escaping the known locally-inverse subclass.

The construction does not assume the Rees actor r is literally τ_S. It is pure: in the physical product, an element over an idempotent actor has self-weight1 and is idempotent; source faithfulness reflects this. The full-context calculation then gives `τ_S=r^(-1)(τ_D)`. The separately written pure-onto-CS pushforward `frontier-20261028-pure-actor-finite-band-pushforward-v1.md`, SHA `abdfecbfb03b7931ad8dac0e7912f6c359279fe7afd47662a4f376942b2d9057`, constructs an injective host over D/τ_D using a rectangular enlargement of B, so the actual canonical κ_q and both same-q R/L obligations are faithful. That pushforward is a current unreviewed dependency, not an accepted external review or a proof that r itself equals τ_S.

## 8. Exact finite experiment and assurance boundary

`frontier-20261028-inverse-fibre-globalization-checker-v1.py`, SHA `543edc15cc0029f257b9fc59ea6cbec933579503943a1d5656649d1859546826`, independently constructs the stated relation, preorder, downsets, shifts and actual Rees multiplication for the three-element inverse monoid `{1,z,p}`, with p²=z and actor C2. Actual run **Wed Oct 28 18:12:32 PDT 2026**, timeout30s, exit0:

```text
inverse_A_size=3 equivalence_classes=3 preorder_pairs=5
downset_sizes={'1': 2, 'z': 1, 'p': 1} nonunit_max_tight=True
Rees_source_size=12 idempotents=7 actual_actor_classes=8
PASS full finite equivalence/preorder, action, base injection, all Rees contexts and host law
CONTROL omitting nontrivial group shift fails tightness as intended
```

The 12-element source includes a nonunit maximal sandwich, is regular and has nonclosed global idempotents; its actor is computed by ALL actual/absent source contexts. The checker is same-author code, not an independent finite-witness certification. Its single finite run does not establish the universal infinite quotient/preorder or full original theorem; those are the written arguments above.

Classical inverse-semigroup properties used explicitly are uniqueness of inverses, commuting idempotents, `(st)^(-1)=t^(-1)s^(-1)`, and the standard natural order. Rees representation and the separately named pure-actor pushforward remain structural/review boundaries. No proof assistant, external-model/human review, triple finite-witness verification, complete source-history or novelty clearance was performed.

## 9. The real remaining original problem

This note closes the **inverse-base Rees subclass** only. The global printed first question includes locally r-orthodox sources not shown to be locally inverse or Rees over an inverse base, and the printed second question is not addressed. The exact next gap is the analogue of §6 for a noncommutative regular-band/local-V base: idempotents no longer form a semilattice and the idempotent support conjugation/preorder intersection argument cannot be imported without proof. RF alone on a general orthodox base does not yet give a simultaneously tight faithful model. No failed numerical search, unproved partial-action globalization, arbitrary product decomposition or past quarantined verdict is substituted for that missing theorem.
