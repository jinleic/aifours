# Weak E-unitarity of a Rees source is exactly a reverse-fibre identity

**NEW WRITTEN AUTHOR CANDIDATE; unreviewed and unadopted.** Native prewrite observation **Wed Oct 28 18:07:16 PDT 2026**. The equivalence below treats all sandwich entries and all elements of the relevant fibres, without a chosen faithful band representation. Exact finite checks are supplementary. No full original-target resolution or novelty is claimed.

## 1. Universal characterization

Let A be ANY nonempty semigroup with an onto **idempotent-pure** homomorphism `θ:A→G` to a group: θ(a)=1 iff a∈E(A). No identity or regularity of A is required for the equivalence below. Let I,Λ be nonempty and P any A-valued sandwich matrix. Form the FULL Rees matrix semigroup `S=M[A;I,Λ;P]` with its usual product, and the onto group-coordinate actor

`r:S→D=M[G;I,Λ;θ(P)]`, `r(i,a,λ)=(i,θ(a),λ)`.

Write **WE-condition** for the printed implication `e∈E(S), e≤x ⇒ x∈E(S)`, with e≤x meaning `e=fx=xg` for actual idempotents f,g. On a regular S this is exactly the printed weak E-unitarity property; outside regularity it is only the same algebraic condition, not an original-class source label.

**Theorem.** The following are equivalent:

1. S satisfies the WE-condition.
2. r is idempotent pure.
3. For EVERY matrix position (λ,i), with p=p_(λ,i), and EVERY a in the inverse group fibre `θ(a)=θ(p)^(-1)`,

   `a p a=a`.                                                (RF)

The actor D is always completely simple. If S is regular and its local corners have regular idempotent bands, this is an exact characterization of the original weak E-unitary requirement within this FULL Rees source family. There is no assumption that P's entries are units, no faithful model/tightness hypothesis and no restriction to finite sources.

## 2. All three logical directions

The actor element `(i,θ(a),λ)` is idempotent in D exactly when

`θ(a) θ(p_(λ,i))=1`.

The source element `(i,a,λ)` is idempotent exactly when `a p_(λ,i) a=a`. Thus r-purity is **precisely** (RF); the reverse implication of purity (source idempotent ⇒ actor idempotent) is automatic. This proves 2⇔3, with all positions and all elements of each actual inverse fibre included.

If r is pure and an idempotent e≤x in S, its actual idempotent witnesses map to witnesses `r(e)≤r(x)`. Natural order in a completely simple Rees semigroup is equality: the two product descriptions force the same row/column, and a row-matching idempotent multiplied on the left of an element gives that element. Hence r(e)=r(x) is idempotent; purity gives x idempotent. So 2⇒1. No source regularity or assumed actor injection was used.

Conversely assume the WE-condition. For ANY source x=(i,a,λ) whose actor r(x) is idempotent, let p=p_(λ,i). Then θ(ap)=1, so ap is an actual idempotent by purity of θ. Direct Rees multiplication gives

`x²=(i,apa,λ)`,
`x³=(i,apapa,λ)=(i,(ap)²a,λ)=x²`.

Put d=x². Since x³=x², x⁴=x², so d is idempotent and `d=dx=xd`. Thus d≤x with BOTH actual idempotent witnesses equal to d. The WE-condition gives x idempotent. This proves 1⇒2, including sources that are not regular and arbitrary infinite index sets. It does not assert that every WE-condition source is regular.

## 3. Intrinsic consequences and exact relation to tight lifts

Assume now A is a monoid. The unit image `H=θ(U(A))` is a subgroup of G, and θ is injective on U(A): if two units have the same image, their quotient is an idempotent unit and hence1.

If a sandwich entry p has θ(p)∈H and S satisfies the WE-condition, let u be the unique unit with θ(u)=θ(p). Taking a=u^(-1) in (RF) gives `u^(-1)p u^(-1)=u^(-1)`, hence p=u. Conversely EVERY unit satisfies (RF): for θ(a)=θ(p)^(-1), purity makes ap idempotent and `a=(ap)p^(-1)`, so `apa=(ap)^2p^(-1)=a`.

Consequences:

- Every matrix entry labelled by the **unit-image subgroup H** must be its unique matching unit. In particular an idempotent sandwich entry must be1_A.
- If H=G (equivalently the pure-group monoid is factorizable as E(A)U(A)), every sandwich entry must be a unit. This recovers the necessity step of `frontier-20261028-factorizable-rees-characterization-v1.md`, SHA `76928b45f2b7144d97c75bb22f95a19a377d7a5641ab89bb82fa74c120a2dd27`, without assuming it.
- A nonunit sandwich in an original source can only have a group label outside H; §5 supplies a checked example. This is necessary, not sufficient by itself.

Now suppose A has a faithful model `ι(a)=(b_a,θ(a))` in B⋊G and put e=b_1. The previous note calls p tight if `b_p=e α_(θ(p))(e)`, and proves its full lift identity `b_(apa)=b_a α_(θ(a)θ(p))(b_a)`. If θ(a)=θ(p)^(-1), the latter equals `b_a²=b_a`, and θ(apa)=θ(a). Faithfulness of ι gives apa=a. Thus **tight ⇒ (RF)** for that p.

The converse is false for a particular faithful model: the same 15-element monoid/nonunit p in §5 satisfies (RF), but the alternate faithful enlargement of `frontier-20261028-tight-subset-obstructions-v1.md`, SHA `3abb2c0f33f49edb606fe3188ad460df330bb1fe5b8b7c698c7dd582920a7f2e`, makes p nontight while keeping the SAME θ. Thus (RF) is an intrinsic fibre condition whereas tightness depends on the chosen representation. We do **not** infer that no different simultaneous tight representation exists.

## 4. Actual syntactic actor, and the remaining embedding gap

If any/all equivalent conditions hold, r is onto and pure. Its **source syntactic** kernel satisfies

`s τ_S t  iff  r(s) τ_D r(t)`.

For the forward direction, lift actual D contexts using onto-ness and transfer idempotence both ways via purity; for the reverse, apply r to every actual or absent source context and use purity. Thus the actual actor is `D/τ_D`, not necessarily D itself. This statement uses NO faithful band model and does not assert S is regular or locally r-orthodox.

The unresolved scientific bridge is now explicit: for a **regular original-class** full Rees source satisfying every intrinsic (RF), determine whether there exists a faithful model of its A-factor in a V-band-by-group such that the ACTUAL whole matrix P is simultaneously tight, or find another genuine all-host invariant/obstruction. The RF criterion itself only pays WEU/pure actor; it does not imply local r, regularity, simultaneous tightness, β-separation or faithful embedding.

The displayed source is not claimed to be every original semigroup. Failure of one particular tight representation is not failure of the original embedding problem.

## 5. Exhaustive finite census and a necessary boundary

The same 15-element monoid A used in the tight-sandwich example has actor C2; its unit image is only the identity. A direct program checks all15 possible p against ALL actual inverse-fibre elements and obtains exactly two RF-good entries: `1_A` and the nonunit `p=(None,0,1)`.

`frontier-20261028-reverse-fibre-weu-checker-v1.py`, SHA `f71f6a2b176ca8d7c89308a390aa8373b94b3ec4eb626ac245942db4486e75c5`, executed with `/opt/homebrew/bin/python3 -B` at **Wed Oct 28 18:07:00 PDT 2026**, timeout60s, exit0:

```text
base_size=15 reverse_fibre_good_entries=2 good_elements=[(None, 0, 1), (None, 1, 0)]
sandwich_matrices=50625 WEU=16 nonWEU=50609
WEU_regular=7 WEU_nonregular=9
PASS all failing matrices have explicit x^3=x^2!=x with idempotent order witness
PASS every reverse-fibre-good matrix by all source natural-order tests and pure actor
```

For each bad matrix the code exhibits an actual source x and verifies d=x² is an idempotent distinct from x with d=dx=xd, so the WE-condition fails for the claimed reason. For each of the16 good matrices it directly tests the full natural-order implication for all source elements/idempotents and verifies r-purity; it separately exhausts mutual-inverse regularity, finding seven regular and nine nonregular sources. The printed word “WEU” in the program output is shorthand for the generalized WE-condition; only the seven regular cases can qualify for the printed regular-source definition, and local r still needs its own check.

The checker imports a same-author pinned finite-base multiplication, SHA `0398f9ed436b7fdbe2be250d4f6f07db134bded4ec77c6e58ff2945cf3c70bee`; it is not an independent implementation or a formal verification. It exhausts one finite A and all its 2×2 matrices, not every semigroup, arbitrary P size or the full original target.

## 6. Verification level and limits

The equivalence in §§1–2 is a written universal argument from the stated θ purity, Rees multiplication and elementary natural-order calculation. The named ordinary import is that the Rees semigroup over a group is completely simple; the equality of its natural order is proved above. Earlier held results or independent-model reviews are not premises. Actual computation is only the finite census in §5 and prior explicitly pinned checks.

No peer/independent-model/human/formal/kernel review, complete literature/priority or novelty clearance is claimed. No new faithful host follows from the RF criterion alone. The full printed first question, printed second question and unrestricted registered same-q R/L problem remain open at this note's scope.
