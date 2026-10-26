# Consolidated written semigroup transport: N3 closure and one sandwich-descent attack

MathSemigroup-2, math-4. Actual clock observed before creation: **Sun Oct 25 04:57:57 PDT 2026** (`/bin/date`).

**WRITTEN / PARTIAL / NOVELTY_UNCLEAR.** This is ONE consolidated manuscript after the three resumption packets, not a fourth freestanding increment. It consolidates their proved claims, removes the superseded open-N3 gap, and carries out ONE next attack: an explicit quotient-preserving sandwich factorization of every noncomposable product. It does NOT deliver the requested full embedding or a genuine nonembedding obstruction. Independent reconstruction and parent acceptance of the new semigroup mathematics remain separate gates.

No scientific interpreter/eval, arithmetic program, enumeration, symbolic program, checker, table execution, solver, replay, native scientific process, external-model CLI or nested agent was used. Only written reasoning, source reads and metadata clocks/hashes. Parent v7 and HOLD v2 are binding. All pinned predecessors remain unchanged.

## 1. Provenance and named imports

The three consolidated resumption sources are:

- `n3-local-band-transport-v1.md`, SHA-256 `81648c29fd4d97085f6dc440c213fd031f24db206fac2b3dcc18349df8c28aae`.
- `n3-transport-closure-addendum-v1.md`, SHA-256 `d46130c78fa34a414289c4717426bf137afcdf33b3d1eab93af6bd88e7edaf6d`.
- `principal-idempotent-transport-v1.md`, SHA-256 `ff534d655e5d695d0bd9421f6fa2b7e4971b36f86bf28494d0b54bac927c7b07`.

The second closes the first's formerly open band transport question; that open question is NOT carried forward here. The first's Rees-local and cyclic-birth results remain and are included below. The third's noncomposable-product gap is sharpened by Section7, not silently declared solved.

Baseline fixed-quotient canonical construction: `construction-gap-v1.md`, SHA-256 `eea9fe1352cf9e1cb83200f114209103f75d1266c022f6fdf4aad699f8a12b10`. Baseline path result: `path-separation-attack-v1.md`, SHA-256 `60d967621f44e20f36f25c4ce402446ff4d4bd6f5f7dbf4c6a0fe68a4451ff4d`. Parent coherent-birth and contextual-load dispositions retain their exact conditional scopes; all-later-context compatibility was not established there.

Nontrivial classical imports, kept explicit:

1. An E-unitary regular semigroup is orthodox and its least group congruence sigma is idempotent pure (Hartmann2007 thesis Theorem2.1, retained PDF SHA-256 `3a7e7cea4516f8afb1ead44d42eb78e1d88672155619cd7db924edb5899d42b2`). The earlier dossier's orthodox weak-to-strong E-unitarity reduction is the named bridge from the orthodox book subclass to this hypothesis; no such bridge is assumed for arbitrary nonorthodox S.
2. Green R and L are congruences on a regular band. Equivalently use the standard regular-band spined-product theorem: regular bands are subdirect products of left regular and right regular bands; R is equality in the former and D in the latter, with the dual L statement. No R/L-congruence assertion on an arbitrary locally regular band is imported.
3. The natural order on a regular semigroup is antisymmetric. For idempotents, `x R y` means `xy=y,yx=x`, and `x L y` means `xy=x,yx=y`; R is a left congruence and L a right congruence in every semigroup.
4. Rees representation for a completely simple semigroup and existence of free bands in a band variety. Neither is a source-free or formalized claim here.

The imported Billhardt/Hartmann N3 NECESSARY host criterion identifies why Section5 retires a witness route. Its proof is not used to prove the new universal N3 implication. No sufficiency of N3 for embedding is imported or inferred.

## 2. Exact target and the actual canonical Pastijn map

The book target ranges over every nonempty regular S, finite or infinite, weakly E-unitary and locally r-orthodox. The latter says every eSe is orthodox and its idempotents form a regular band, with identity `xyxzx=xyzx`. The target band variety V consists of bands D for which each dDd is regular; equivalently it has the band identity

    e z e x e z e y e z e = e z e x e y e z e.

The fixed P product uses `C=M[G;I,Lambda;P]`, group action alpha by automorphisms, and

    (b,(i,g,lambda))(d,(j,h,mu))
       =(b alpha_(g p_(lambda,j))(d),(i,g p_(lambda,j)h,mu)).

The sandwich entry acts on the band AND in the group coordinate. The fixed R reading retains its restricted carrier, not the full Cartesian product; none of the following claims a new P/R equivalence.

Suppose an ACTUAL idempotent-pure surjection q:S->C is supplied, and write `q(s)=(i_s,g_s,lambda_s)`. Its existence for every arbitrary infinite nonorthodox book-class S is NOT proved here. The old finite/covered pure-quotient results retain their original named boundaries.

Take the free V-band on `X_(u,s)`, u in G, s in S, and impose

    X_(u,st)=X_(u,s) X_(u g_s p_(lambda_s,i_t),t).  (M)

Call the quotient B_q. Left shifts `alpha_v(X_(u,s))=X_(vu,s)` preserve the presentation and have inverse alpha_(v^-1); hence they are actual band automorphisms. Put beta(s)=[X_(1,s)]. Then

    beta(st)=beta(s) alpha_(g_s p_(lambda_s,i_t))(beta(t)),
    kappa_q(s)=(beta(s),q(s))                      (KAPPA)

is a genuine homomorphism to B_q odot C, and B_q is locally regular by its construction in V. This is the explicit map, NOT a proved injection.

With q pure, it is enough to separate idempotents in each idempotent q-fibre. Indeed, if kappa(s)=kappa(t), choose s' in V(s). Equal q makes `s't,ts'` idempotents by purity. Idempotent separation gives

    s't=s's,       ts'=ss'.

It follows that `t(s's)=s=(ss')t`, hence s<=t. The symmetric argument gives t<=s, and antisymmetry gives s=t. Thus the real unresolved condition is

    q(e)=q(f), beta(e)=beta(f), e^2=e, f^2=f
        ==> e=f.                                 (SEP)

When diagnosing a collapse as a nonembedding obstruction, the previous least-quotient pullback argument must be retained: failure over an arbitrarily coarser quotient is not enough. No collapse or source counterexample is supplied here.

## 3. Actual principal idempotent bands, without global orthodoxy

For an idempotent e of a regular S define

    B_e={x in E(S):ex=x},
    D_e={x in E(S):xe=x}.

**Theorem 3.1.** S is locally r-orthodox iff every B_e is a regular band; equivalently iff every D_e is a regular band. Thus the idempotents in every principal one-sided ideal form a globally regular band, although E(S) itself need not be closed.

**Proof.** Take x,y in B_e. The elements xe,ye are idempotents in eSe, since `(xe)^2=xexe=xe` and they are fixed by e on both sides. Local orthodoxy makes `(xe)(ye)=xye` idempotent. Right multiplying `(xye)^2=xye` by y and using ex=x,ey=y gives `(xy)^2=xy`. Also e(xy)=xy; hence B_e is a band.

The map `rho_e:B_e->E(eSe)`, `rho_e(x)=xe`, is multiplicative. The target's regular identity gives

    rho_e(xyxzx)=rho_e(xyzx).

Both words end in x, and xex=x. Right multiplication by x recovers both words from their rho images, proving the regular identity in B_e. The D_e statement is dual. Conversely E(eSe) is a subband of B_e, and eSe is regular: for a in eSe and a' in V_S(a), ea'e is a mutual inverse there. This is exactly local r-orthodoxy. Finally `aS=aa'S`, `Sa=Sa'a` for a' in V(a), so every principal ideal is covered. QED.

This does NOT assert that eS or Se themselves are regular semigroups.

A band-only corollary used in Section5: if D is locally regular, every vD and Dv is a REGULAR band. The same proof applies to `rho(x)=xv` on the left-unital band vD; the regular words have the same last letter and are recovered after rho. No global regularity of D is inferred.

Define the actual coordinate bands

    L_e=B_e/R,       R_e=D_e/L.

They are respectively left regular and right regular. In any band `xy R xyx`, as `(xy)(xyx)=xyx` and `(xyx)(xy)=xy`; quotienting by R gives `xyx=xy`. The dual gives `xyx=yx` after quotienting by L. The congruences exist here by Theorem3.1 and named import2.

For idempotents e,f, the bi-local band

    B_(e,f)={x in E(S):ex=x=xf}

has an explicit injective band homomorphism

    x |-> ([x]_R in L_e, [x]_L in R_f).            (LOCAL-SEP)

Equality of both coordinates gives R- and L-related idempotents, hence xy=y and xy=x, so x=y. This is true LOCAL separation; it is not (SEP) for the global canonical presentation.

## 4. Complete inverse-pair transport and supplied-quotient faithfulness

Let Gamma(S) have objects E(S), arrow `(s,s')` from e=s's to f=ss' for every mutual inverse pair, inverse `(s',s)`, identities `(e,e)`, and composition

    (s,s') o (t,t')=(st,t's') when s's=tt'.

Writing e for that common middle idempotent verifies the inverse equations and endpoints:

    st(t's')st=s e e t=st,
    (t's')st(t's')=t' e e s'=t's',
    (t's')st=t't,       st(t's')=ss'.

This is a genuine groupoid, with associativity inherited from S.

For an arrow e->f put `theta_s(x)=sxs'`. It sends B_e to B_f and is multiplicative:

    (sxs')^2=s x e x s'=sxs',
    theta_s(x)theta_s(y)=s x e y s'=sxy s'.

The inverse composite is `theta_(s')theta_s(x)=exe=xe`, which is R-related to x. Thus theta induces an actual isomorphism `L_e->L_f`. On D_e the same formula induces `R_e->R_f`; now the round trip is ex, L-related to x. For composable arrows,

    theta_s(theta_t(x))=st x t's'=theta_(st)(x).

These are two explicit functors to isomorphisms of one-sided regular bands, not unspecified faithful-functor hypotheses. They require neither global orthodoxy nor E-unitarity.

If the actual pure completely simple quotient q of Section2 is supplied, the induced functor Gamma(S)->Gamma(C) is faithful on every hom-set. To prove it, let `(s,s'),(t,t')` have the SAME endpoints e,f and q(s)=q(t). Then t's is in eSe, has idempotent q-image q(e), and is idempotent by purity. It is also a unit there, with inverse s't:

    (t's)(s't)=t'(ss')t=e,
    (s't)(t's)=s'(tt')s=e.

Thus t's=e and `s=tt's=t`. Endpoint-fixed inverses are unique: `s'=s'(st')=(s's)t'=t'`. QED.

This faithfulness concerns parallel groupoid arrows. It does not identify coordinate bands at DIFFERENT source endpoints, nor prove a multiplication-compatible global gluing. Section7 addresses the actual noncomposable-product interface explicitly.

## 5. Universal N3 closure in the entire orthodox book subclass

**Theorem 5.1.** Let S be an E-unitary orthodox regular semigroup whose band E(S) is locally regular. Suppose

    a sigma b, A in V(a), B in V(b), e,f,g in E(S),
    eaA=e=ebB,
    Bb f Aea f g=f Aea f g.                       (N-PREM)

Then

    ea f g=eb f Aea f g.                          (N3)

No finiteness, C2/helper-grade, global regular-band or `Aafg=fg` premise is needed.

First prove the needed band transport. Let p,k,l,r lie in a locally regular band D and satisfy

    kl=p, kr=k, lr=r, rl=l.

Let v satisfy vr=r, and Y satisfy vY=Y. Then `vl=vrl=rl=l`, so l,r,Y all lie in the REGULAR band vD. There `l R r`; R-congruence gives `lY R rY`. Since R is a left congruence in every semigroup, left multiplying by k gives

    pY R kY.                                     (TR)

For R-related idempotents P,Q we have QP=P. If also QP=Q, equality follows.

To apply this to (N-PREM), use the pure least group map pi and put

    x=ea, y=eb, c=Ae, t=Be.

Then `xc=e=yt`, ex=x,ey=y,ce=c,te=t. Because pi(a)=pi(b), the inverse-grade product cy is idempotent. Multiplying `(cy)^2=cy` by x on the left and t on the right gives

    (xc)y c(yt)=(xc)(yt),
    e y c e=e,
    yc=e.

Similarly `(tx)^2=tx` gives xt=e. Put

    p=cx, k=cy, l=tx, r=ty, v=Bb.

All these are idempotents; the four equations `xc=yc=xt=yt=e` give

    kl=p, kr=k, lr=r, rl=l,
    vr=BbBeb=r.

Let H=pfg and Y=fpfg=fH. The last premise of (N-PREM) is vY=Y. Since pf is idempotent,

    pY=(pf)^2 g=H.

Apply (TR): `H R K`, where K=kY=kfH. But `KH=kfH^2=K`; R-related idempotents also satisfy KH=H. Therefore H=K. Finally left multiply by x:

    xH=ea f g,
    xK=eb f Aea f g.

This proves (N3). QED.

The entire formerly proposed N3 countermodel route is thereby WRITTEN-excluded throughout the orthodox book subclass at the named imports. The old protocol remains a historical unchanged document; another N3 table search cannot advance this class if the theorem is accepted. N3 is ONLY a necessary host condition, so its universal validity is NOT an embedding theorem. It does not exclude a DIFFERENT nonembedding invariant, especially in the nonorthodox class.

## 6. Rees-typed local regularity and one contextual birth

Let S be regular locally r-orthodox, with the actual pure q:S->C of Section2. No global orthodoxy is assumed. If p,z,x,y in S satisfy

    q(ptp)=q(p) for each t in {z,x,y},              (INNER)

choose p' in V(p), e=pp', and put c_t=pte. Then c_t belongs to eSe. Writing a=q(p), a'=q(p'),

    q(c_t)=a q(t) a a'=(a q(t) a)a'=aa'=q(e).

Purity makes c_t idempotent. The regular band E(eSe) satisfies

    c_z c_x c_z c_y c_z=c_z c_x c_y c_z.

Right multiplication by p and ep=p give the actual source identity

    p z p x p z p y p z p=p z p x p y p z p.       (REES-LR)

If `q(p)=(i,h,lambda)`, `q(t)=(j,k,mu)`, condition(INNER) is exactly

    h p_(lambda,j) k p_(mu,i)=1.

The row/column sandwich factors and their noncommutative order are retained. No mutual-inverse condition on q(t) beyond(INNER) is needed.

For a nonempty word w with contexts ell,r, at least one present, suppose q(ell w r) is idempotent. Let beta be the nonempty cyclic complement r ell, omitting absent contexts rather than treating them as elements of S. Purity gives the exact whole-word equation

    ell w beta w r=(ell w r)^2=ell w r.             (BIRTH)

This beta also has the correct Rees inner-inverse type. When both contexts are present, write q(ell),q(w),q(r) with group labels g_L,g_W,g_R and row/column labels i_L,lambda_L etc. Whole-loop idempotency says

    g_L p_(lambda_L,i_W) g_W
        p_(lambda_W,i_R) g_R p_(lambda_R,i_L)=1.

Set A=g_L p_(lambda_L,i_W), B=g_W and D=p_(lambda_W,i_R)g_R p_(lambda_R,i_L). Then ABD=1, hence BDA=1. The group label of q(w r ell w) is B D A B=B and its endpoints are those of q(w). Therefore q(w beta w)=q(w). With one context absent, the same two-factor Rees calculation applies. With both absent this is ordinary loop idempotency, not a nonloop birth requiring beta.

These are complete LOCAL identities and ONE designated birth solution. Compatibility of all later contextual equations is not inferred from them.

## 7. ONE consolidated next attack: quotient-preserving sandwich descent

This section makes the multiplication across noncomposable inverse-pair arrows explicit, rather than merely restating that it is missing.

Take arbitrary s,t in a regular S, with chosen inverses s',t'. Put

    e=s's,       f=tt'.

The arrows for s and t are not composable unless e=f. Nevertheless choose ANY mutual inverse z of ef and define

    h=f z e.

Everything is an actual source element; ef is regular because S is regular. The inverse equations for z give

    h^2=f z e f z e=f z e=h,
    he=h,       fh=h,
    e h f=ef z ef=ef.                             (SAND)

Consequently

    s h t=s e h f t=s e f t=st.                   (PRODUCT)

The pairs

    (sh,hs') : h -> shs',
    (ht,t'h) : t'ht -> h

are actual inverse pairs. For example `(sh)(hs')(sh)=s h e h=sh` and `(hs')(sh)(hs')=h e h s'=hs'`; the ht pair is dual. They ARE composable, and

    (sh,hs') o (ht,t'h)
       =(sht,t'h s')=(st,t'h s').                 (COMPOSE)

Thus t'h s' is an explicit mutual inverse of st, with endpoints t'ht and shs'. Every originally noncomposable product is represented by a genuine composable product of source restrictions. Moreover

    sh=(shs')s=s h <= s,
    ht=h t=t(t'ht) <= t

in the regular natural order.

There is no hidden uniqueness assumption about h. The set of all idempotents satisfying(SAND) is nonempty and is a rectangular band: for two choices h,k,

    h k h=h e k f h=h(ef)h=(he)(fh)=h,
    k h k=k.

Hence hk is idempotent. It still satisfies(SAND), since `(hk)e=hk`, `f(hk)=hk`, and

    e h k f=e h f k f=ef k f=e k f=ef.

If S is orthodox, the canonical choice `h=fe` works, since ef and fe are idempotent and `e(fe)f=(ef)^2=ef`. Thus no inverse-of-ef choice is even needed in that subclass.

Now supply the pure Rees quotient q. In fact the following typing needs only that q is a homomorphism. Every h satisfying(SAND) has the same q-image: its row is that of q(f), its column that of q(e), and it is idempotent. Since the Rees H-class has one idempotent,

    q(h)=(i_t,p_(lambda_s,i_t)^(-1),lambda_s).

This is the actual crossed sandwich idempotent, not a guessed group inverse. Direct multiplication gives

    q(sh)=q(s),       q(ht)=q(t).                  (Q-PRESERVE)

So the factorization(PRODUCT)/(COMPOSE) uses restrictions that preserve BOTH original factor quotient values. The new local transport functors apply to the composable arrows and satisfy

    theta_(st)=theta_(sh) o theta_(ht)

on the corresponding endpoint coordinate band, with inverse t'h s'. This is a proved multiplication-interface formula, not a claimed global embedding.

**The single remaining descent obligation.** Glue the one-sided coordinate bands of Sections3–4, their inclusion/restriction maps and these sandwich squares into one locally regular band with the actual Rees/group action, so that every(SAND) choice induces the same globally multiplicative map AND every idempotent q-fibre stays separated. Different h may have different source idempotents t'ht and target idempotents shs', even though their q-images agree. Faithfulness on one fixed groupoid hom-set does not compare those DIFFERENT objects. Rectangular choice and(Q-PRESERVE) therefore do not supply the missing descent by themselves.

In the canonical presentation this is still the real(SEP) obligation: its mixed multiplication relations must preserve every actual fibre band, including all sandwich choices. No arbitrary off-path inverse recipe, common endpoint-only inverse, or blanket solvability of every contextual load is assumed. This is ONE sharpened construction attack, not a different problem or a new computational request.

## 8. Current settled scope, external review and park boundary

Complete WRITTEN arguments in this consolidation:

- actual regular principal one-sided idempotent bands, without global orthodoxy;
- explicit local separating coordinates and inverse-pair transport functors;
- supplied pure quotient faithfulness on parallel inverse-pair arrows;
- universal N3 closure throughout the orthodox book subclass, without the extra Aafg premise;
- sandwich-correct Rees local identity and one cyclic contextual birth;
- every product's explicit quotient-preserving composable restriction factorization, including its nonunique rectangular sandwich choices.

The inverse-pair/transport/sandwich ideas have classical Hall/Munn/inductive-groupoid analogues. No priority or novelty claim is made for these constructions or this specialization. Named imports and written algebra are not proof-assistant checking.

The canonical map(KAPPA) is still not proved injective; the full P/R embedding target and a genuine alternative nonembedding obstruction are NOT delivered. The arbitrary infinite nonorthodox pure-quotient prerequisite remains open beyond the existing covered classes. The next action is exactly the sandwich-square descent/SEP proof in Section7, not another N3 search or another freestanding local increment.

Assigned cross-domain review v32-A was completed and returned FIRST, before this primary continuation: own-root `peer-review-ame4555-two-F-v1.md`, SHA-256 `249dfe9cc00578c48b04925878e7afb2675a5c9957394f71abd269d51959c62f`. Its0F/0M/0m verdict concerns only the reconstructed AME two-F subfamily and supplies no semigroup correctness or novelty premise. The present semigroup consolidation remains a written candidate pending its own actual reconstruction.
