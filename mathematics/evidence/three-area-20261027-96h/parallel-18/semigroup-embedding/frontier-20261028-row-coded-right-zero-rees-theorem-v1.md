# Row-coded right-zero Rees sources admit explicit faithful hosts

**NEW AUTHOR WRITTEN THEOREM CANDIDATE; exact finite nonabelian check; unreviewed/unadopted.** Native verification-start observation **Wed Oct 28 18:31:18 PDT 2026**. This gives a general family, including the nonorthodox/non-locally-inverse 45-source which defeats simultaneous tightness. It is not a proof for arbitrary original sources, a printed-question equivalence claim, a novelty claim, or a substitute for an independent mathematical review.

## 1. Family and exact result

Let G be ANY group acting on a nonempty set R on the left. View R as the right-zero band `r s=s`, and adjoin a NEW identity `1_A` to the semidirect product `R⋊G`. Write its other elements `(r,g)` and multiplication

`(r,g)(s,h)=(g·s,gh)`.

Let `θ(1_A)=1_G`, `θ(r,g)=g`. Let I,Λ be nonempty and P a Λ×I matrix over A with the following **row-coded condition**:

1. Each entry is either `1_A` or `(r,g)` with `g≠1_G`.
2. For every fixed row λ and `g≠1_G`, all P entries with θ-value g are equal (i.e. have the SAME r). There is no restriction comparing different rows.

Form the full Rees semigroup `S=M[A;I,Λ;P]` and its onto Rees-group actor `r(i,a,λ)=(i,θ(a),λ)` in `D=M[G;I,Λ;θ(P)]`.

**Theorem.** For ANY such P, whether or not S is regular, the construction in §§2–3 gives an explicit injective homomorphism `S→P(B,D)` with actor r and with B a right regular band. If S is regular, it is weakly E-unitary and locally r-orthodox and hence belongs to the original class. In particular S is regular if every row AND every column of P contains a 1_A. For every regular source in this family, the actual syntactic actor is a pure CS quotient of D; the explicit pure-actor pushforward in §5 gives a faithful host over this **same actual q_τ**, and hence the actual canonical κ_q is injective. Both same-q R- and L-idempotent obligations hold.

No assumption that G is commutative, that the D rows/columns are syntactically separated, that R or G is finite, or that the P entries are all units is made. The row condition is an explicit sufficient hypothesis: its failure is NOT a nonembedding result.

## 2. Band and action

Let `R^1=R∪{⊤}` be R with an identity adjoined, distinct from its points. Thus `x·y=y` when y∈R, and `x·⊤=x`. It is a right regular band: `(xy)x=yx`. Therefore

`B=(R^1)^G`

with pointwise multiplication is a right regular band and hence a regular band, in the required local-regular variety. Extend G's action on R by fixing ⊤, and define

`(α_g F)(k)=g·F(g^(-1)k)` for g,k∈G.                    (2)

Each α_g is a band automorphism, and `α_g α_h=α_(gh)`; the displayed multiplication order is valid for nonabelian G.

For each λ and q≠1_G choose `ρ_λ(q)∈R` as follows: if a P entry in row λ has θ-value q, choose its unique R-label; otherwise choose one fixed arbitrary element of the nonempty set R. The choice on missing labels is not a claim that such a sandwich entry exists.

For source `s=(i,a,λ)` put g=θ(a) and define `C_s∈B` by

`C_s(g) = ⊤` if a=1_A, and `C_s(g)=r` if a=(r,g);

`C_s(k) = g·ρ_λ(g^(-1)k)` for k≠g.                     (3)

The coefficient may depend on λ, and indeed must do so in the 45-source. Unlike the disproved tight-lift bridge, it is NOT required to come from one unmodified faithful A-band coefficient.

## 3. Prove the full physical host multiplication

Take `s=(i,a,λ)`, `t=(j,b,μ)`, set `g=θ(a)`, `q=θ(P_(λ,j))`, `h=θ(b)` and `w=gq`. The actor weight is exactly w. We prove

`C_(st)=C_s · α_w(C_t)` in B.                             (4)

**b is nonidentity.** Write b=(v,h). Formula (3) gives C_t no ⊤ coordinate. Therefore pointwise right-zero multiplication makes the right factor overwrite the left everywhere. The source middle product `a P_(λ,j) b` is the nonidentity `(w·v,wh)`, whether a or P is the identity. At coordinate wh, `(α_w C_t)(wh)=w·v`. At k≠wh it equals

`w·(h·ρ_μ(h^(-1)w^(-1)k))=(wh)·ρ_μ((wh)^(-1)k)`.

These are exactly (3) for st.

**b=1_A.** Here C_t has ⊤ precisely at1_G; α_w C_t has ⊤ precisely at w. At every k≠w the right factor overwrites and gives `w·ρ_μ(w^(-1)k)`, exactly the target value in (3).

At k=w the product retains `C_s(w)`. If q=1_G then the first row-code condition forces `P_(λ,j)=1_A`, so w=g, the middle product is a, and this retained value is the correct a-marker (or ⊤ for a=1_A). If q≠1_G, row coding gives `P_(λ,j)=(ρ_λ(q),q)`; the source middle product has group w and R-label `g·ρ_λ(q)`. Since w≠g, (3) gives precisely `C_s(w)=g·ρ_λ(q)`. This proves (4) in all cases.

Consequently `j(s)=(C_s,r(s))` is a physical host homomorphism. For injectivity, r recovers i,λ,g. The value C_s(g) is ⊤ exactly when a=1_A and otherwise is its R-label r. Together with g it recovers a, so j is injective.

## 4. Regularity and the actual original hypotheses

A is regular: for `(r,g)`, ANY `(s,g^(-1))` is a mutual inverse by the right-zero formula; the new identity is its own inverse. If each P row and column contains 1_A, choose j with `P_(λ,j)=1_A`, μ with `P_(μ,i)=1_A`, and a mutual inverse a' of a. Then `(j,a',μ)` is a mutual inverse of `(i,a,λ)` in S. The theorem also allows ANY other P for which S is established regular; no all-row/column-unit necessity is claimed.

The actor r is idempotent pure. Its actor value is idempotent iff `θ(a) θ(P_(λ,i))=1_G`. If the sandwich is 1_A, this says θ(a)=1_G, whose entire fibre consists of the idempotents 1_A and `(r,1_G)`. If the sandwich is `(u,q)` with q≠1_G, then a=(v,q^(-1)) and direct multiplication gives `a P_(λ,i) a=a`. Conversely a homomorphism carries idempotents to idempotents.

Thus when S is regular, an idempotent below s maps to an idempotent below r(s); the natural order on D is equality, so purity makes s idempotent: S is weakly E-unitary. For e∈E(S), eSe is regular. The actor image of every idempotent of eSe is the identity of the local actor group; their host coefficients therefore multiply inside the regular-band corner of B. Faithfulness transfers idempotent closure and the regular-band identity to E(eSe). Hence S is locally r-orthodox.

The earlier 45-source has G=C2 acting by swapping R={0,1}, identity everywhere in the first row/column, and two distinct nonunit P entries in DIFFERENT rows at the same group label. It is covered although no faithful fixed-A model can make those two entries simultaneously tight. This also demonstrates why the present result is genuinely not a relabeling of that stronger and false premise.

## 5. Actual τ actor and canonical separation, with transport scope

For any onto pure r, source and actor idempotence tests satisfy

`s τ_S t  iff  r(s) τ_D r(t)`,

because each actual actor context lifts to a source context, absent factors are carried as absent factors, and purity reflects idempotence. Hence the source's **actual** q_τ is `f∘r`, where `f:D→D/τ_D`. The syntactic congruence saturates idempotents by the empty context. If f(d) is idempotent, regularity of D gives an idempotent in d's τ-class by the standard `d u d` construction with u an inverse of d²; saturation proves d idempotent. Thus f is pure; its image is completely simple.

The following transport is the exact written candidate `frontier-20261028-pure-actor-finite-band-pushforward-v1.md`, SHA `abdfecbfb03b7931ad8dac0e7912f6c359279fe7afd47662a4f376942b2d9057`, reconstructed here at its needed scope. Any onto pure CS homomorphism restricts to an isomorphism on local groups: surjectivity follows by sandwiching a preimage with the local idempotent; if two group elements have the same image, their quotient maps to an idempotent, hence is itself idempotent by purity, and must be the local identity. In Rees coordinates write

`f(i,g,λ)=(a(i),u_i h(g) v_λ,b(λ))`,
`v_λ Q'_(b(λ),a(j)) u_j = h(Q_(λ,j))`,

where h:G→G' is this group isomorphism up to the usual local gauge. Let the target act by `γ_z=α_(h^(-1)z)` on B, and trivially on the rectangle `I×Λ`. The physical whole-host map

`(b,(i,g,λ)) ↦ (((i,λ),γ_(u_i)b), f(i,g,λ))`

is an injective homomorphism into the host over D/τ_D. Indeed the new action weight is `u_i h(g Q_(λ,j)) u_j^(-1)`, so the B product becomes `γ_(u_i)(b α_(g Q_(λ,j)) c)`; the rectangle retains the original row and column, while the actor and h then recover g. This proof explicitly uses the standard Rees representation of completely simple semigroups and the ordinary Rees homomorphism coordinate identities, not an assumed row/column injection.

Composition with j gives a faithful physical source model over exactly q_τ. The canonical free V-band generator map to that model respects (4) and all V identities, so equal canonical images would have equal faithful physical images. Therefore κ_q is injective and both R- and L-separation hold for this family. If the named actor-transport argument fails review, the explicitly constructed faithful host over the original actor r remains valid independently; the actual-q/canonical conclusion is then **NR-PUSHFORWARD**, not silently promoted.

## 6. Exact nonabelian and collapsed-actor check

`frontier-20261028-row-coded-rees-nonabelian-checker-v1.py`, SHA `314a780364ad02adeafe50871721ffb99903ca7d7850935a0a5600ebfc453d67`, executed with `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 18:31:18 PDT 2026**, exit0. It uses G=S3 and the natural nontrivial action on R={0,1,2}; u=(01) and v=(12) do not commute. Its P is

`((1,1,1),(1,(0,u),(1,v)),(1,(2,u),(0,v)))`.

Every row and column contains the new identity; the two nonidentity group rows are the same but their R-labels differ. The check directly constructs all171 source elements, all32 idempotents, all local corners, the host functions on the six group elements, and the 54-element preliminary actor. It checks every 171² source law and host injection, then all 172² actual/absent contexts per source. The true syntactic actor has only36 elements: the two repeated group rows collapse. A concrete retained-rectangle host over those36 values is directly verified, rather than assuming the preliminary actor is actual q.

```text
G=S3 order6, noncommuting generators= 2 1 ; R=3 nontrivial permutation action
source=171 idempotents=32 original_actor=54 actual_tau_actor=36
PASS regular, weak-E, all local orthodox/regular-band corners; actor purity
PASS all29241 source/actor/physical-host products and same-actor injections
PASS actual quotient and retained-rectangle host, full 172^2 contexts per source
CONTROL same-row same-weight different labels breaks the displayed coefficient law
```

The negative control only shows that equation (4) as written fails when one row has two different R-labels at the same group weight. It does not assert that another coefficient, another action, or another host is impossible. The 45-source and its opposite each have separately checked, explicit eight-band actual-q models in `frontier-20261028-eight-band-original-source-and-dual-v1.md`, SHA `37222f083c7f31af91716a88534de49ff974260f07477293957268f46ac6aed6`.

The written argument covers arbitrary G and R; the finite code checks one S3 witness, not every group. All programs are same-author, no independent witness certification, peer review, formal/kernel proof, cross-vendor review or novelty clearance has occurred. Beyond this declared Rees family, the original full R/L, printed Q1 and Q2 remain open.
