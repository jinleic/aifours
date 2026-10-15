# Problem 1: actor results and integration corrections, 2026-10-14 PT

**The original goal is not resolved in this attempt. The mathematical reviewer must return `done:false`.** No unconditional embedding of every weakly E-unitary, locally r-orthodox regular semigroup has been constructed, and no genuine counterexample to that assertion has been obtained. This report does not certify that the problem is open in the literature.

The unchanged target is embeddability in `B ⊙ C`, or equivalently under the adopted interpretation in `B ⊙* C`, with `B` a seminormal/locally regular band and `C` completely simple. The book does not define this semidirect product. The two products formalized here are the dossier's fixed readings; their equivalence as embeddable classes is an externally attributed result, not a new Lean theorem in this file.

## Achieved scope

`Formal.lean` contains actual associative multiplication constructions for band-by-group semidirect products, Rees coordinate semigroups, Pastijn products, and the restricted products over these Rees semigroups. It proves the necessary direction in both fixed readings, the exact characterization of local idempotents, the local-regularity iff for the group and Pastijn cases, and an explicit derived-functor wreath embedding criterion with its converse. These are prerequisites and conditional criteria, not the required sufficient direction.

The 32 reported roots, including three associative semigroup instances, are individually specified in `claims.json`. Every reported statement and its transitive axiom dependencies are printed in `Formal.lean`. The observed axiom union is exactly `{propext, Quot.sound}`; no reported root uses `Classical.choice`. The final immutable checker records its own observations and hashes in `verification/receipt.json`.

Most of the mathematical content formalizes `proof.md` §§0 and 2. The elementary additions are the converses for the group/Pastijn local characterizations, the converse derived-functor criterion, removal of the unnecessary surjectivity hypothesis in Lemma 3, and carrier independence for any inner inverse in the restricted construction. No claim of literature novelty is made for these additions.

## Definition audit

All ambient associativity and all group laws use Mathlib's `Semigroup` and `Group`. `Band B` explicitly asserts `b*b=b` for every element. There is no commutativity or identity assumption on the band. `Action` specifies `act 1=id`, `act(gh)=act(g)∘act(h)`, and multiplication preservation. Its bijectivity is proved from `g⁻¹`; it is not supplied as an assumed conclusion.

`NaturalLE a b` is exactly the book's witness condition `a=e*b=b*f` for idempotent `e,f`. `InLocal e x` is the fixed-point condition `e*x=x=x*e` used for local membership. `LocallyRegular` uses the book identity `a*x*a*y*a=a*x*y*a` on all three members of `eBe`; the separate `Band B` hypotheses ensure that every `e` is idempotent. Only the 32 roots listed in `claims.json` are reported as separately printed/audited Lean claims.

`LocallyROrthodox S` asserts global regularity and, at each idempotent `e`, closure of local idempotents and the same regular-band identity on them. It does not assert global orthodoxy. This is faithful to the book because every local `eSe` of a regular semigroup is regular: if `y` is inverse to `x∈eSe`, then `eye` is a local inverse of `x`. This fact is proved in `regular_local`. The use of two inverse equations in `Regular` is audited by `regular_iff_innerInverse`, which proves equivalence with the book's `aba=a` existence condition using the witness `bab`.

The completely simple factors are represented by the adopted Rees coordinates with group-valued sandwich matrix `p`, without a zero. The necessity results work even if an index type is empty; for the book factor, use nonempty row and column types. The Pastijn iff result supplies an actual row and column. The general Rees representation theorem for abstract completely simple semigroups is not formalized here.

## Written argument

### Semidirect construction and local characterization

Let `G` act multiplicatively on a band `B`. Define

`(a,g)(b,h) = (a·act(g,b), gh)`.

Associativity follows because the first coordinates of a triple product are respectively

`(a·act(g,b))·act(gh,c)` and `a·act(g,b·act(h,c))`,

which agree by multiplication preservation, the action law, and associativity in `B`. The second coordinates agree by the group law. A two-sided inverse witness for `(a,g)` is `(act(g⁻¹,a),g⁻¹)`; both inverse equations reduce to band idempotence and the inverse action law.

Idempotence forces `g²=g`, hence `g=1` by cancellation. Conversely `(a,1)²=(a,1)` by band idempotence. This gives both E-unitarity and weak E-unitarity: if an idempotent left or right factor turns an element into an idempotent, its group coordinate must be `1`; the natural-order version follows from the left witness.

For `e=(b,1)`, an idempotent `x` in `eSe` has group coordinate `1`. The equations `ex=x=xe` then become `b·base(x)=base(x)=base(x)·b`. Thus the local idempotents are exactly `(z,1)` for `z∈bBb`, with ordinary band multiplication. They form a regular band exactly when `bBb` does. This proves the group local-regularity iff. For injective homomorphisms, idempotence is reflected and local membership is preserved; the identity on local idempotents is pulled back by injectivity. Source regularity is explicitly assumed, since arbitrary subsemigroups need not be regular.

### Rees natural order and Pastijn product

For `C=M[G;I,L;p]`, an element `c=(i,g,l)` is idempotent iff `g p(l,i)=1`. If `s=e t=t f` with idempotent `e,f`, the row of `s` is both the row of `e` and the row of `t`, while its column equals the column of `t`. The group coordinate in `e t` is

`(grade(e) p(col(e),row(t))) grade(t) = grade(t)`,

because `row(t)=row(e)` and `e` is idempotent. Therefore `s=t`. This proves that the natural order is equality in the Rees model.

The Pastijn multiplication is exactly

`(a,(i,g,l))(b,(j,h,m)) = (a·act(g p(l,j),b), (i,g p(l,j)h,m))`.

Associativity uses the action coefficient `g p(l,j) h p(m,k)` on both sides. Projection to `C` preserves multiplication. A Pastijn element is idempotent iff its Rees coordinate is idempotent: in that case the coefficient acting on its own base coordinate is `1`, so its square reduces to `a²=a`.

For regularity, put `k=g p(l,i)` and choose

`t=(act(k⁻¹,a), (i,k⁻¹ p(l,i)⁻¹,l))`.

The Rees inverse equations hold by group cancellation. The first coordinates in the two semigroup inverse equations reduce to `a²=a` and `act(k⁻¹,a)²=act(k⁻¹,a)`. These are explicitly proved, without a choice of inverses as an additional assumption.

At an idempotent `e=(b,c)`, any local idempotent `x` has `π(x)≤π(e)`, so `π(x)=c`. Multiplication in this fibre is ordinary multiplication in `B`, because `c` is idempotent and its action coefficient is `1`. Therefore the local idempotents are precisely the elements with projection `c` and base in `bBb`. Local regularity follows from that of `B`. Conversely, fixing any row `i` and column `l` gives the injective homomorphism `b↦(b,(i,p(l,i)⁻¹,l))`; its local bands recover the local bands of `B`. This proves the Pastijn local-regularity iff and the necessary direction for regular embedded semigroups.

### Restricted product: actual carrier and closure

Let `θ` be an endomorphism action of `C`. Write

`u(i,l)=(i,p(l,i)⁻¹,l)`, `u_x=u(row(x),col(x))`.

The carrier is `{(a,x):θ(u_x)(a)=a}`. For the explicit Rees inverse used above, `xx'=u_x`. For any inner inverse `y` with `xyx=x`, the element `xy` is idempotent and has row `row(x)`, hence `xy=u(row(x),col(y))`.

For a fixed row, `u(i,m)u(i,l)=u(i,l)`. If `θ(u(i,l))(a)=a`, then

`θ(u(i,m))(a)=θ(u(i,m))θ(u(i,l))(a)=θ(u(i,l))(a)=a`.

Thus the fixed sets are independent of the chosen column. This proves that the canonical carrier condition agrees with the condition using `xy` for every inverse, and even for every inner inverse. It does not redefine the restricted carrier as all of `B×C`.

Define `(a,x)(b,y)=(a·θ(x)(b),xy)`. The row-column idempotent for `xy` fixes `a` by the preceding calculation, and is a left identity for `x`. Its action therefore fixes both factors of `a·θ(x)(b)`. This proves carrier closure. Associativity follows from `θ(xy)=θ(x)θ(y)` and multiplication preservation.

For regularity, choose the canonical inverse `y` of `x` and put `t=(θ(y)(a),y)`. This lies in the carrier because `u_y y=y`. Also `θ(xy)(a)=a`. The first inverse equation reduces to `a³=a`; the second reduces to `θ(y)(a)³=θ(y)(a)` using `yxy=y`. The Rees coordinates obey their inverse equations as well.

If `x` is idempotent, then `u_x=x`, so the carrier fixes `a` under `θ(x)` and the square of `(a,x)` has first coordinate `a²=a`. The converse follows by projection. Natural-order equality in `C` again proves weak E-unitarity.

At a restricted-product idempotent `e`, local idempotents have the same projection as `e`. Each of their bases is fixed by that projection's action. Their multiplication is consequently ordinary band multiplication, and their local bases lie in `base(e) B base(e)`. They form a subband of that local band, so they satisfy its regular-band identity. Pullback along an injective homomorphism gives the necessary direction in reading (R). An iff with local regularity of the entire original base band is not asserted for a general restricted action; the action can have a proper image.

### Derived-functor criterion and its converse

Let `σ:S→G` be a homomorphism. Suppose a locally regular band `B0` and a function `F:G×S→B0` satisfy

`F(g,s) F(gσ(s),t)=F(g,st)`,

and `F(1,s)=F(1,t)` together with `σ(s)=σ(t)` implies `s=t`. These are explicit hypotheses in the conditional theorem, not consequences supplied by the P1 assumptions.

Equip `B0^G` with coordinatewise multiplication and the action `(h·f)(g)=f(gh)`. The action law follows from `(gh)k=g(hk)`; its inverse is shifting by `h⁻¹`. Every band identity and each local regular-band identity hold coordinatewise, so `B0^G` is a locally regular band. Define

`φ(s)=(f_s,σ(s))`, `f_s(g)=F(g,s)`.

The displayed functor equation proves the homomorphism law at every coordinate. Equality of `φ(s)` and `φ(t)` gives equality at coordinate `1` and equality of grades; faithfulness gives `s=t`. Surjectivity of `σ` is nowhere used.

Conversely, for an embedding `φ(s)=(β(s),σ(s))` into a semidirect product, define `F(g,s)=act(g,β(s))`. The homomorphism equation for `β(st)` and the action laws give the functor equation. At `g=1`, the action is the identity. Equality of `F(1,s),F(1,t)` and of grades therefore gives equality of `φ(s),φ(t)`, hence `s=t`. This converse needs no band or local-regularity hypothesis to produce the functor.

## Exact remaining obstruction

For the orthodox part, the existing dossier's Theorem A reduces the full problem to `Q_orth`. This run has not formalized or replaced that reduction. What is still needed is a construction of a locally regular band `B0` and a **faithful** `F` satisfying the functor equation for every E-unitary orthodox `S` with locally regular `E(S)`. The formal criterion proves what such a construction would give; it does not produce it from those source hypotheses. In the canonical presentation approach, the missing step is proving that the band congruence does not identify distinct parallel arrows. Universality of the canonical map does not prove injectivity.

In particular, no general argument is supplied for at least three D-classes, including a V-shaped structure semilattice with a group interchanging maximal classes. The dossier's regular-band, monoid, and at-most-two-D-class cases are not extended here. The integration owner's [Theorem X](xi-purity.md), independently audited by the parent, now proves finite ξ-purity (and the completely-simple-ideal case) by a written coordinate argument; **it is not Lean-checked**. The non-orthodox gap is therefore (i) constructing an embedding from the pure completely simple quotient in the finite case, and (ii) ξ-purity as well as embeddability for infinite semigroups without a completely simple ideal. The actual Billhardt example's local regularity has not been verified, so its known nonembeddability cannot be promoted to a P1 counterexample.

## Bounded obstruction attempts

The actor's accessible Hartmann text restates Billhardt's necessary embeddability condition and recalls a finite graph construction attributed to Szendrei. The exact original Billhardt construction was not recovered. The integration owner recovered and preserved the exact Theorem 6 excerpt from the actual actor tool output and an accessible author-thesis corroboration. [The condition audit](obstruction-condition.md) gives the complete statement, the line-by-line constraint mapping and a source-dependent coordinate transfer to `B⋊G`. See `references.md` and `source-access.md` for the separate access outcomes and attribution limits.

Two fresh searches used that condition, not the previous 357-construction/48-certificate suites. They looked for Z2-graded regular orthodox semigroups whose even idempotent band is locally regular and which violate the condition. Three distinguished even elements and four distinguished odd elements were required to be distinct. Associativity, mutual inverse witnesses, grading, local regularity, all condition premises, and the wrong-conclusion inequality were encoded explicitly. Products of the two odd witnesses lie in the idempotent kernel, ensuring equality under every group image as required by the condition.

| Attempt | Setup | Bound | Observed result |
|---|---|---|---|
| `attempts/search_obstruction_7_4.py` | 7 even, 4 odd; 3,994 constraints | one solver thread; 60,000 ms | UNSAT; total wall 1.976 s |
| `search_obstruction.py 9 8` | 9 even, 8 odd; 12,078 constraints | one solver thread; 60,000 ms | UNKNOWN, reason `timeout`; total wall 64.425 s including setup |

The first result excludes only that encoded setup: no case with coincident members of `e,f,g`, or coincident members of `a,b,a′,b′`, was searched. Its UNSAT answer has no proof-logged certificate. The second excludes nothing. Neither is an exhaustive search of all semigroups of those orders, an embedding certificate, a ξ-purity proof, or a general P1 result. No candidate table was produced. The scripts and actual logs/JSON reports are preserved in `attempts/`; the pre-existing solver package was read with bytecode writes disabled, and nothing was installed.

## Negative control and verification

`NegativeControl.lean` copies the actual `Action`/`SD` multiplication and associativity construction from `Formal.lean`. The mutation removes the necessary `Band B` hypothesis from the idempotent characterization, specializing the base to multiplicative natural numbers and the group to `PUnit`. The element `(2,1)` has group coordinate `1`, while its square has base coordinate `4`. The control contains a valid proof of this concrete failure before the deliberately invalid universal theorem.

The observed semantic rejection in `attempts/15-negative.log` is at the false goal `s.base*s.base=s.base`: `Tactic rfl failed`. The valid countermodel proof compiles. There is no missing import, identifier, or dependency error. This is a countermodel to a **weakened prerequisite**, not a counterexample to Problem 1.

The positive source compiled in `attempts/17-axioms.log` and printed all 32 roots with permitted axioms. Earlier failed elaborations and the first negative-control elaboration are retained; they were corrected without proof placeholders or additional axioms. Some failed patch applications made no file changes and remain in the HMZ tool journal.

The exact final artifact check is:

```sh
python3 verify.py
```

The actor executed this immutable checker once; the original receipt is preserved in `hmz/actor-snapshot/verification/`. The integration owner executes it once more after the review's documentation/source-evidence corrections, without changing the Lean sources or the frozen checker. The integrated positive/negative return codes, source hashes and all 32 axiom reports are retained in `verification/receipt.json`, `verification/formal.log`, and `verification/negative.log`. A passing receipt is partial-artifact verification only. Comparator and nanoda were not exercised.

The direct Lean command used for proof iteration was:

```sh
cd /Users/jinleic/jinleic-workspace/scratch/rh-quasi-lean-2026-10-07/lean
/Users/jinleic/.elan/bin/lake env lean /Users/jinleic/jinleic-workspace/scratch/ai4s-math-hmz-20261014/semigroup/repo/Formal.lean
```

The toolchain is Lean 4.34.1. No cached project or OAI source was modified, copied, rebuilt, or updated. The known cached-package warnings were retained. Positive imports are only `Mathlib.Algebra.Group.Hom.Basic` and `Mathlib.Algebra.Group.Pi.Basic`; the negative source additionally imports the narrow `PUnit` and natural-number algebra modules.

## Ownership and HMZ handoff

Baseline commit: `19e7a6670a637565c73e46a920aca746bf44f275`. No further commit was made. Frozen SHA-256 values are:

* `TASK.md`: `670a30e463149a1b742e956c46d4fbbd6052f1c6bf9d7018ccc7b59f4e9bdd2a`.
* `verify.py`: `b6b6fcffb62cc2f0434d245ea4c467e9ce2cbd18b6d3d8c9071e25e05b907f7a`.

The actual authorized run used `run_hmz.py` and the frozen 3600-second timeout. Worker/reviewer pairing was `codex/gpt-6.1-sol:max` / `claude/claude-opus-5-5:max`; runtime revision `3d3e21b0da89ef5f6247cd7b3f88ad178fbac94a`, official flowverse revision `2c37d06df3e356807adb93b5a9fdca170a5d0be8`. It ended after 3600.387 seconds with process exit 143 and journal `ended how:"stopped"`. The actual reviewer returned **`done:false`** after independently compiling the Lean source and accepting its partial scope; the resumed actor was interrupted before completing another round. `hmz/reviewer-verdict.json`, the exact wrapper output, both journals and `hmz/process.json` retain this failed full-goal attempt. Frozen TASK/checker hashes stayed unchanged. No nested HMZ, extra reviewer CLI, or subagent tree was launched by the actor.

The actor wrote only inside the fresh scratch repository. The integration owner subsequently copied the reviewed artifacts into this authorized target directory, preserved the original snapshot, corrected the review's three documentation objections, and added the separate parent-audited written Theorem X. Reference/dependency and frozen-file hashes are in `attempts/provenance.json`; the post-run process check found no matching remaining actor/reviewer/repository processes. `math/`, shared caches/configuration, credentials, policies and sibling targets were not mutated by this assignment.
