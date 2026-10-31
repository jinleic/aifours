# F156 — independent same-harness review of the upper-cone obstruction

## Verdict and exact scope

**Scientific verdict: correct at the requested scope; FATAL 0 / MAJOR 0 / MINOR 0. Confidence: 0.99.** I independently reconstructed the full-product regularity, the idempotent-separating-congruence lemma and order reflection, primitive-actor cell forcing, the embedding of every upper idempotent cone into the band factor, the nine-element locally inverse nonorthodox counterexample, and the WEU upper-cone closure argument. A reviewer-authored exact control actually completed, with positive and intended-reason negative cases and a hash/clock receipt. The finite computation is a control, not the proof of the universal no-host assertion.

This verdict concerns precisely an embedding into an idempotent-separating image of the full Cartesian-product construction defined below, with a group acting by band automorphisms. It does **not** interpret printed Q2, prove Q2 sufficiency or Q1 closure, settle the same-q R/L gap, establish novelty, or certify either of the separately conditional sufficiency/identity imports in the packet. It is same-harness review, not human review, independent-model-family review, formal/kernel verification, or scientific adoption by the parent.

**Process exception, separate from the scientific result:** an earlier direct public-source download created `/tmp/f156/1909.05280v1.html` outside the assigned review artifact directory. This was an output-location violation; it is disclosed rather than described as fully compliant. The public-source scratch is retained, not deleted. No author source was edited, no held mathematical output was used as a premise, no Git operation was performed, and no external model/paid API, author contact, publication, or infrastructure mutation was performed. Early status messages also did not honor the assignment's no-progress-updates instruction. The parent must not infer full procedural compliance from the zero scientific-defect counts.

## 1. Frozen inputs and actual evidence

The manifest was read first, its SHA-256 matched the assignment, both inputs' complete bytes/SHA-256/LF counts were verified before interpretation, and both inputs were then read completely in their declared order: main candidate, then mandatory WEU scope addendum. The scope addendum was applied before reaching the verdict.

| Item | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `manifest-v1.json` | 3004 | 30 | `a4b862a8a5fa78ce20686ae2df5aa0ed87d3d27081c473bfdd52097f1d86b9ef` |
| `frontier-20261028-q2-upper-cone-obstruction-v1.md` | 5332 | 35 | `283fb012e02f730a86aaa72ecbb77f695de5bd572c73dfeed794a0ab77e7720a` |
| `frontier-20261028-q2-upper-cone-weu-boundary-v1.md` | 1813 | 9 | `fb0f8f8ecaec11f3789c145a54b4e7cb1a2ea43291e96ced83017ff4a7eebc70` |

The input directory is `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/semigroup-embedding/`.

Directly read named public reference: Mária B. Szendrei, *Structure theory of regular semigroups*, arXiv:1909.05280v1 (2019):

- [§2, paragraph 3](https://arxiv.org/html/1909.05280v1#S2.p3): precise meaning of a congruence being over a class, and the equivalence of idempotent separation with being over groups for a congruence on a regular semigroup.
- [§5.2, paragraph 5 and its displayed rule](https://arxiv.org/html/1909.05280v1#S5.SS2.p5): the Pastijn product formula, with an automorphism action of the structure group on the band. The survey states this construction for a normal band; below I directly verify the properties needed for its arbitrary-band extension.
- [§5.2, paragraph 4](https://arxiv.org/html/1909.05280v1#S5.SS2.p4): weak E-unitarity means that an element above an idempotent in the natural order must be idempotent.

The source HTML has SHA-256 `dad0f6e52ad97b7986cdf12a01bcfb5149e1634c547d57baf5971c1712cec036`, 334354 bytes, 1655 LF. `reviewer-public-source-receipt-v1.json` preserves these facts, the named paragraph text with MathML alttext, and the scratch-location exception; its SHA-256 is `b0c2af26852f992f56d37afb24471303e0503654cfaf6a3c5f144915c888c73e`.

I did not import or execute the author's Python control. A hash-only check found the cited control and the four other named sibling candidates/erratum at their stated hashes; their contents were not read or used as premises. In particular, the inverse formula, Hartmann sufficiency import, and local-regular/seminormal equivalence below are not accepted merely because their sibling hashes match.

## 2. Construction and regularity reconstructed

Let B be any band, so every b satisfies b²=b. Let D be a completely simple semigroup, written by the Rees–Suschkewitsch representation as M[G; I, Λ; P], with all sandwich entries p_{λi} in the group G. Its multiplication is

(i,g,λ)(j,h,μ) = (i, g p_{λj} h, μ).

Fix an action α:G→Aut(B), writing α_g(b) also as a left action of g. The exact physical construction being checked is the **full set** H=B×D with multiplication

(a,(i,g,λ))(b,(j,h,μ)) = (a α_{g p_{λj}}(b), (i,g p_{λj}h,μ)).

Associativity follows from associativity in B and G and α_{uv}=α_u∘α_v: the first coordinate of a triple product, in either bracketing, is

a α_{g p_{λj}}(b) α_{g p_{λj}h p_{μk}}(c).

No normal-band identity is needed. Projection onto D is an onto homomorphism.

Here is an explicit two-sided inverse calculation, independent of the candidate's sibling formula. For x=(b,(i,g,λ)), choose any j∈I and ν∈Λ and put

w = g p_{λj},
h = p_{λj}^{-1} g^{-1} p_{νi}^{-1},
c = α_{w^{-1}}(b),
y = (c,(j,h,ν)).

Then

xy = (b,(i,p_{νi}^{-1},ν)),
yx = (c,(j,p_{λj}^{-1},λ)),
xyx = x, and yxy = y.

For example, the first coordinate of xy is b α_w(c)=b²=b, and the twist in (xy)x is p_{νi}^{-1}p_{νi}=1. The dual computation gives yxy=y. Thus H is regular for **every** band B and the specified automorphism action; this proof does not use the unreviewed inverse-formula file.

The idempotents of D are exactly d_{iλ}=(i,p_{λi}^{-1},λ). Consequently E(H)=B×E(D). At any fixed actor idempotent d=(i,p_{λi}^{-1},λ), the twist g p_{λi} is 1, so

(a,d)(b,d)=(ab,d).

The twist is 1; the actor's group coordinate p_{λi}^{-1} need not itself be 1. No normalization of the sandwich matrix is assumed.

## 3. Idempotent separation, group fibers, and order reflection

### Precise classical lemma and named reference

**Lemma.** If R is a regular semigroup and ρ a congruence on R, then ρ is idempotent-separating if and only if every ρ-class containing an idempotent e is a group. Its identity is e, and that class is a subgroup of the maximal subgroup H_e. This is precisely the statement that ρ is *over groups* in [Szendrei (2019), §2](https://arxiv.org/html/1909.05280v1#S2.p3).

This does not say every congruence class is a group, or that R/ρ is a group. Regularity of R is essential.

For completeness, the needed direction also has the following direct reconstruction. First, if [x] is idempotent in R/ρ, choose v∈V(x²). Then t=xvx satisfies t²=t and [t]=[x], since x²vx²=x² and vx²v=v. Also t belongs to xR¹∩R¹x. This proves the required idempotent-lifting fact without assuming a unique inverse.

Now assume ρ is idempotent-separating and aρb. Pick a′∈V(a). The element ba′ is congruent to aa′, an idempotent. Applying the preceding lifting construction to ba′ produces an idempotent t∈bR¹ in that same class. Idempotent separation forces t=aa′, so a=ta belongs to bR¹. Applying the dual argument to a′b gives a′a∈R¹b, hence a=a(a′a) belongs to R¹b. Swapping a and b proves a H b. Thus ρ⊆H.

In particular, the class of e lies in the group H_e and is closed under multiplication. If aρe and a# is the inverse of a in H_e, then a#=a#e ρ a#a=e; so the class is also closed under inverses and is a subgroup with identity e. Conversely a group contains only one idempotent, which proves idempotent separation for any congruence over groups.

### Idempotent lifts

Let π:H→U be onto and idempotent-separating. For u∈E(U), take x with π(x)=u and v∈V(x²). The preceding construction gives the idempotent xvx mapping to u. Two idempotents cannot have the same image by hypothesis. Hence each u has exactly one idempotent lift. This applies to idempotents of an arbitrary embedded subsemigroup S⊆U; regularity of S is not required.

### Reflection of the order on idempotents

For idempotents, e≤f means ef=fe=e. If e,f∈E(H) and π(e)≤π(f), then ef and fe both lie in the π-fiber of e. By the lemma this fiber is a group with identity e. Thus (ef)e=ef, giving

(ef)²=(efe)f=(ef)f=ef.

Likewise e(fe)=fe gives

(fe)²=f(efe)=f(fe)=fe.

Both ef and fe are therefore idempotents in that same fiber and must equal e. Hence e≤f. This proves the order-reflection step; it does not rely on surjectivity of the restriction of π to any proposed cone.

## 4. Primitive actor and upper-cone embedding

All idempotents of a completely simple semigroup are primitive. In the Rees coordinates this is immediate: if d=(i,p_{λi}^{-1},λ) and d′=(j,p_{μj}^{-1},μ), then dd′=d forces μ=λ, while d′d=d forces j=i. The unique idempotent in that cell then gives d=d′. This argument is independent of finiteness.

Identify S with an embedded subsemigroup of U. Fix z∈E(S), and define

↑z = {e∈E(S): ze=ez=z}.

Let z̃ be the unique idempotent lift of z. Each e∈↑z has a unique idempotent lift ẽ, and order reflection gives z̃≤ẽ. Projection H→D preserves the idempotent order. Primitivity in D therefore forces the actor of **every** ẽ to be the single actor idempotent d of z̃. Thus ẽ=(b_e,d).

For e,f∈↑z, the fixed-cell formula gives

ẽf̃=(b_e b_f,d)∈E(H).

It follows that ef∈E(S). Moreover z(ef)=(ze)f=zf=z and (ef)z=e(fz)=ez=z. Hence ef∈↑z, so the cone is a subsemigroup. Its unique idempotent lift must be ẽf̃. The map e↦b_e is therefore a homomorphism. It is injective because equal band coordinates, with the already common actor d, give equal lifts and hence equal images in S.

Thus **↑z is isomorphic to a subband of B**. Every variety of bands is closed under subbands and isomorphisms, so if B∈V, then ↑z∈V. In particular B∈SN implies ↑z∈SN. The proof quantifies over every permitted actor and automorphism action, including infinite actors; no assumption that the actor is a syntactic quotient of S occurs. No regularity of S was used.

## 5. Nine-element counterexample and independent exact table

Use additive C₂={0,1}, I=Λ={0,1}, p_{λi}=λi (mod 2). The nonzero multiplication is

(i,g,λ)(j,h,μ)=(i,g+λj+h mod 2,μ).

Adjoin a new absorbing zero ⊥. This gives nine elements. The following table was generated and checked by my own code from this displayed rule, not read from or generated by the author's control.

Labels: 0=⊥, 1=(0,0,0), 2=(0,0,1), 3=(0,1,0), 4=(0,1,1), 5=(1,0,0), 6=(1,0,1), 7=(1,1,0), 8=(1,1,1). Table entry r,c denotes the label of the row element times the column element.

| · | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 2 | 3 | 4 | 1 | 2 | 3 | 4 |
| 2 | 0 | 1 | 2 | 3 | 4 | 3 | 4 | 1 | 2 |
| 3 | 0 | 3 | 4 | 1 | 2 | 3 | 4 | 1 | 2 |
| 4 | 0 | 3 | 4 | 1 | 2 | 1 | 2 | 3 | 4 |
| 5 | 0 | 5 | 6 | 7 | 8 | 5 | 6 | 7 | 8 |
| 6 | 0 | 5 | 6 | 7 | 8 | 7 | 8 | 5 | 6 |
| 7 | 0 | 7 | 8 | 5 | 6 | 7 | 8 | 5 | 6 |
| 8 | 0 | 7 | 8 | 5 | 6 | 5 | 6 | 7 | 8 |

All 9³=729 associativity triples passed. The idempotents are exactly {0,1,2,5,8}. The code verified inverses for all nine elements and uniqueness of inverses within every local corner. The corners are:

| Idempotent identity | Corner labels | Corner idempotents |
|---|---|---|
| 0 | {0} | {0} |
| 1 | {0,1,3} | {0,1} |
| 2 | {0,2,4} | {0,2} |
| 5 | {0,5,7} | {0,5} |
| 8 | {0,6,8} | {0,8} |

Independently of the finite check, at e=(i,λi,λ), the nonzero part of eSe is the two-element group {(i,g,λ):g∈C₂}; shifting the group coordinate by λi identifies its multiplication with C₂. Its zero extension is inverse, and its idempotents {⊥,e} form a semilattice. The zero corner is trivial. Thus S is regular and locally inverse, and, with locally r-orthodox meaning that local idempotent bands are regular bands, it is locally r-orthodox.

Now e=1=(0,0,0), f=8=(1,1,1) are idempotent, but ef=4=(0,1,1) and (ef)²=2=(0,0,1)≠ef. Since ⊥ is below every idempotent, ↑⊥=E(S) is not closed under multiplication. Section 4 consequently rules out an embedding of S in **any** idempotent-separating image of a full P(B,D′), for any band B and any completely simple actor D′. The universal conclusion is supplied by the reconstructed theorem, not by enumerating a set of finite hosts.

## 6. WEU boundary: what is proved, and what remains conditional

For a regular semigroup, the natural order may equivalently be expressed by the Mitsch relation: a≤b if a=xb=by and xa=a for some x,y∈S¹. In particular, if an idempotent z satisfies za=az=z, then z≤a: take x=y=z. Only this sufficient implication is needed here.

If S is weakly E-unitary and e,f∈↑z, then

z(ef)=z and (ef)z=z.

Consequently z≤ef, and weak E-unitarity implies ef is idempotent. The same equations place ef back in ↑z. Thus **every idempotent upper cone of a WEU S is automatically a band**. This is a complete argument for the addendum's closure claim, not an appeal to an author PASS statement.

In a semigroup with an absorbing zero, ⊥≤a for every a, witnessed by x=y=⊥. The four nonidempotents of the nine-element example therefore violate WEU. The exact control found all four violations with that witness. The example cannot be an original WEU Q1 source; the cone-closure condition alone cannot refute the WEU/locally-r class.

If S is also regular and locally r-orthodox, put C=↑z. For each e∈C, the local band eCe is a subband of E(eSe). The latter is a regular band by the locally r-orthodox hypothesis, and a subband satisfies all its identities. Hence C is **locally regular**. This implication is independently checked at the identity/containment level here.

The stronger conclusion C∈SN still depends, in the supplied addendum, on the separate locally-regular/seminormal equivalence candidate **together with its mandatory rationale erratum**. Neither is a manifest input. I have not read or certified that equivalence and do not promote the complete SN obstruction as independently proved automatic for Q1 here. The addendum expressly makes it conditional, so this is a named unverified dependency, not a scientific defect in its stated conditional. The verified band-closure boundary is unconditional for WEU S.

Likewise, main-candidate §3 has an unconditional necessary direction for zero sources: ↑⊥=E(S), so any regular zero source in the target is orthodox with E(S)∈V. Its converse/exact-iff language is expressly conditional on the Hartmann thesis proof import and a separate source-interface review. That sufficiency import, and the conversion to a locally-r formulation via the separate identity candidate/erratum, are **not certified in this review**. No Q1/Q2 closure or sufficiency conclusion is adopted from them.

## 7. Actually executed controls and replay binding

Successful independent program: `reviewer-control-v3.py`, SHA-256 `24e58d36ae08f3ba16ef08b6710505dbda75b487494f09425fd12bca34d6daf9`.

Successful receipt: `reviewer-control-receipt-v3.json`, SHA-256 `a4e864031518b492cd923399c98e8c16d9baec9a341f191b0de500e6a8856d0b`, 22385 bytes, 1464 LF. The receipt records the actual UTC start `2026-10-29T05:02:40.773402+00:00` and finish `2026-10-29T05:02:42.127500+00:00`, interpreter/platform, script hash, full nine-element table, inverse/corner witnesses, and targeted control outcomes. The command `python3 -B reviewer-control-v3.py` completed with exit 0. No floating-point comparison, solver, author-code import, external service, or model call occurs in this control.

| Case actually run | Intended observable result | Observed result |
|---|---|---|
| Requested D⁰ | Associative, regular, locally inverse; five idempotents; ef nonidempotent | All 729 triples and all stated checks passed; e=1,f=8,ef=4,(ef)²=2 |
| Target cone-closure negative | Reject because the zero cone contains two idempotents with a nonidempotent product | `ConeClosureFailure`, exact reason `nonidempotent_product`, witness z=0,e=1,f=8,ef=4 |
| Positive all-zero sandwich variant | A nine-element orthodox rectangular group with zero has band upper cones | All 729 triples passed; zero cone {0,1,2,5,6} closed. This is the same **number** of idempotents as the target, not the same label set |
| One-entry multiplication mutation | The associativity checker itself must reject, not merely a zero test | Changing 0·1 from 0 to 1 yielded `AssociativityFailure`: triple (0,1,2), left result 2, right result 0 |
| Arbitrary-band/nontrivial-action host | Exercise more than the normal-band/trivial-action special case | B is the 15-element left regular band of nonempty repetition-free words on {a,b,c}; product deletes later repeated letters. The swap a↔b fixes c. Associativity and idempotency checked; xyzx=xzyx fails at (a,b,c), so B is not normal |
| Nontrivial idempotent-separating image | Exercise lifting, group fibers, order reflection, and all cone embeddings | H=P(B,D₄), U=P(B,D₂), C₄ acts by parity, sandwich p_{λi}=λi, and π reduces group coordinates mod 2. Orders 240→120; onto homomorphism; 60 unique idempotent lifts; two-element group fibers over all idempotents; all 3600 idempotent-order pairs reflected; every cone's actor cell, closure, unique multiplicative lifts, and injective homomorphic B-map checked |
| WEU positive | Independently exercise the addendum's implication | Exact Mitsch-order exhaustion found H and U weakly E-unitary; all U cones are bands and embed in B |
| Drop idempotent separation | Order reflection should cease to be valid | Actor projection maps distinct idempotents (a,(0,0,0)) and (b,(0,0,0)) to the same actor; their actor images are ordered/equal, but the former is not below the latter upstairs |
| Drop regularity in the group-fiber lemma | Idempotent separation alone should no longer force group fibers | In {0,a} with every product 0, the universal congruence separates the unique idempotent but its class is not a group; precise failure is that 0·a=a·0=0≠a |

The host and quotient associativity checks covered 13,824,000 and 1,728,000 triples respectively. These are bounded concrete controls of the algebraic proof, not a universal computational classification.

### Failed reviewer attempts retained, not counted as successes

- `reviewer-control-v1.py` exited 1 because I incorrectly chose a six-element **normal** band as a non-normal fixture. Its check correctly detected that reviewer premise error. No success receipt was emitted. `reviewer-control-attempt-v1.json` records this and the subsequent failed derivation guard.
- `reviewer-derive-control-v2.py` exited 1 before creating its outputs because its replacement guard expected a receipt filename once although it occurs in both docstring and target. `reviewer-derive-control-v2b.py` fixed that derivation guard, preserving the old file.
- `reviewer-control-v2.py` exited 1 during receipt assembly: an outer-loop e/f binding shadowed the nine-element e/f labels, causing an index error. This was a reviewer receipt-construction bug, not a candidate defect or a successful run. `reviewer-control-attempt-v2.json` records it. `reviewer-derive-control-v3.py` produced v3 with distinct e9/f9 bindings, preserving v2.
- Only the successful v3 receipt above is the claimed completed finite evidence. The earlier failure timestamps in the attempt receipts are explicitly *observed after-failure upper bounds*, not invented exact failure times. The positive-variant comment “same five idempotents” in the script means the same count of five; the actual receipt and table explicitly distinguish their labels, as shown above.

## 8. Load-bearing dependencies, limits, and disposition

| Dependency | Treatment in this review |
|---|---|
| Rees representation of a completely simple semigroup | Standard Rees–Suschkewitsch representation, used explicitly and consistent with the named survey construction; no finiteness/normalization assumption |
| Associativity and regularity of the arbitrary-band physical product | Direct algebraic reconstruction in §2; also exact non-normal-band/nontrivial-action control |
| Idempotent-separating congruences of a regular semigroup are over groups | Precise statement directly read in the named source; an independent proof of the needed direction is supplied in §3 |
| Idempotent lifting and order reflection | Derived explicitly in §3, not inferred from author code or the finite counterexample |
| Primitive actor idempotents and cell multiplication | Direct coordinate proofs in §§2 and 4 |
| Cone injection and variety membership | Direct homomorphism/injectivity proof; closure of equational varieties under subbands and isomorphism |
| Nine-element associativity, regularity, local inverses, zero order, and nonidempotent ef | Independent multiplication table, direct local-group reasoning, and successful exact control |
| WEU implies upper-cone closure | Direct natural-order witness and WEU implication, with positive and negative finite cases |
| Locally-r hypothesis makes the cone locally regular | Direct subband-of-E(eSe) argument |
| Locally regular band ⇔ seminormal band | Not certified; separate candidate and mandatory erratum remain explicit dependencies of the stronger SN boundary |
| Hartmann-based sufficiency / zero-source iff | Not certified; conditional external proof import/source-interface review remains necessary for that separate assertion |

There is no identified mathematical gap in the upper-cone necessity, nine-element no-host conclusion, or unconditional WEU band-closure boundary under the displayed definitions. The conditional SN and zero-source sufficiency claims have the precise unreviewed dependencies named above and must not be folded into this verdict. “New” in the candidate's status is not a novelty conclusion of this review. No author PASS/checked statement is used as evidence.

**Final disposition:** zero scientific defects at the exact admitted scope, with the output-location/process exceptions explicitly disclosed. No printed-Q2 interpretation, no Q1 closure, no all-source sufficiency, no independent-family/formal/human verification, and no novelty or publication claim.
