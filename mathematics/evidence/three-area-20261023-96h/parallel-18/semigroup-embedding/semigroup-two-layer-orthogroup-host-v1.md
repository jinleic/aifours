# Every original-class E-unitary orthogroup with at most two J-classes embeds

Owner MathSemigroup-2, original math-4. Actual `/bin/date` BEFORE this new body: **Mon Oct26 08:19:05 PDT2026**. **NEW AUTHOR-WRITTEN / UNREVIEWED / no novelty claim.** A proper ORIGINAL-class theorem with an explicit host; it strictly generalizes the earlier Theorem P family. It is NOT the unrestricted embedding theorem and not an obstruction.

## 0. Provenance and boundaries

Developed entirely AFTER the ACTUAL v123-D RETURN and the NEW whole qualified primary ACK `6486d372cbad61059ea955a6ce9538a62d3888581129aea68186745ca15da8e6` (07:52:08, WRITTEN and SENT), under parent direction v42 (`9d406187...`). Not a pre- or post-receipt exposed lead. The four individually identified own MAJOR occurrences and the older read-order finding remain permanent.

Hosts are P(B,G)=B⋊G, (b,g)(d,h)=(b alpha_g(d),gh), the physical Pastijn product with C=G. "Orthogroup" = orthodox completely regular semigroup. Named classical structure inputs, as in `semigroup-full-group-orthogroup-host-v1.md`: an orthogroup is a semilattice of rectangular groups, and an orthodox completely simple semigroup is a rectangular group. The bitranslation form of multiplication by an element of a higher component on a rectangular group, and its W_L consequences, are proved there in Lemma P0's proof and re-derived where used below.

## 1. Structure of a two-J-class W_L E-unitary orthogroup

Let S be an orthogroup with exactly two J-classes, idempotent-pure sigma:S→G onto a group, and left regular local idempotent bands. Then S=S_1 ⊔ S_0, a semilattice {1>0} of rectangular groups with S_0 an ideal.

1. **Lower group.** sigma(S_0) is a subgroup K_0 of G and, for s∈S_1, x∈S_0, sigma(s)sigma(x)=sigma(sx)∈K_0 forces sigma(s)∈K_0. Thus sigma(S)=K_0, and ontoness gives sigma(S_0)=G. Purity makes sigma injective on each maximal subgroup, so S_0=I_0×G×Lambda_0 with sigma the middle coordinate.
2. **Upper group.** S_1=I_1×H×Lambda_1 with H=sigma(S_1)<=G, sigma the middle coordinate.
3. **Mixed products.** Left and right multiplication by s∈S_1 is a linked bitranslation of S_0. As proved in Lemma P0 of the full-group body, it has the form

   `s(j,g,mu)=(F_s(j),sigma(s)g,mu)`, `(j,g,mu)s=(j,g sigma(s),R_s(mu))`,

   where the common group constant equals sigma(s) because sigma(sx)=sigma(s)sigma(x). Since x↦sx and x↦xs compose as actions, F_(ss')=F_s∘F_(s') and R_(ss')=R_(s')∘R_s.
4. **W_L forces constant right maps.** For an upper idempotent e, the idempotents of the corner eEe in S_0 form F_e(I_0)×R_e(Lambda_0); a left regular rectangular band is left zero, so R_e is constant. For s∈H_e, se=s gives R_s=R_e∘R_s, so R_s is constant with the same value. From R_(ss')=R_(s')∘R_s, the constant value c(s) satisfies c(ss')=c(s'); applied to s=(i,x,nu),s'=(i',x',nu') with ss'=(i,xx',nu') this shows c depends only on the column label: c(i,x,nu)=c(nu).

Conversely, call the following a **two-layer datum**: a rectangular group S_1=I_1×H×Lambda_1, a group G containing H, nonempty sets I_0,Lambda_0, a homomorphism s↦F_s from S_1 into the monoid of self-maps of I_0 under composition, and a map c:Lambda_1→Lambda_0. Define S=S_1 ⊔ (I_0×G×Lambda_0) with the rectangular-group products inside each part and

`(i,x,nu)(j,g,mu)=(F_(i,x,nu)(j),xg,mu)`, `(j,g,mu)(i,x,nu)=(j,gx,c(nu))`.

**Lemma D.** Every two-layer datum gives a semigroup S which is an orthogroup, E-unitary over sigma (middle coordinate) onto G with sigma pure, and whose local idempotent bands are all left regular; and every two-J-class W_L E-unitary orthogroup over G is of this form (items1–4).

*Proof of the converse direction.* Associativity, all mixed patterns (s,s' upper; x,y lower):
- s s' x: F_(ss')=F_s∘F_(s') and group parts multiply.
- s x s': both give (F_s(j),xgx',c(nu')).
- s x y: both give (F_s(j),xgg',mu').
- x s s': both give (j,gxx',c(nu')), since ss' has column nu'.
- x s y: both give (j,gxg',mu').
- x y s: both give (j,gg'x,c(nu)).
Patterns inside one part are rectangular-group products. Idempotents are exactly the elements with middle coordinate1; their products again have middle coordinate1, so S is orthodox; it is a disjoint union of groups, hence completely regular; sigma is a homomorphism with sigma^-1(1)=E(S), hence pure, and S is E-unitary. For an upper idempotent e=(i,1,nu), e(j,1,mu)e=(F_e(j),1,c(nu)): the corner's lower idempotents lie in ONE column, a left-zero band with identity e adjoined, hence left regular; lower corners are trivial. ∎

## 2. Theorem T2 — explicit host for every two-layer datum

Fix a left transversal T of H in G containing1, and write each w∈G uniquely as w=t_w x_w, t_w∈T, x_w∈H. Let

`B=(I_1×Lambda_1×G) ⊔ (I_0×G×Lambda_0)`

with products

- upper: `(i,nu,k)(i',nu',m)=(i,nu',k)`;
- lower: `(j,n,mu)(j',n',mu')=(j,n,mu')`;
- upper·lower: `(i,nu,k)(j,n,mu)=(F_(i,x_w,nu)(j),k t_w,mu)`, where w=k^-1 n;
- lower·upper: `(j,n,mu)(i,nu,k)=(j,n,c(nu))`,

and G-action alpha_g(i,nu,k)=(i,nu,gk), alpha_g(j,n,mu)=(j,gn,mu).

**Theorem T2.** B is a band in W_L, each alpha_g is a band automorphism, and

`psi(i,x,nu)=((i,nu,1),x)`, `psi(j,g,mu)=((j,1,mu),g)`

is an INJECTIVE homomorphism S→B⋊G over sigma.

### 2.1 B is a band

Each part is a rectangular band (upper: (I_1×G)×Lambda_1; lower: (I_0×G)×Lambda_0). Idempotency is clear. The only nontrivial mixed pattern is u u' l. Take u=(i,nu,k), u'=(i',nu',m), l=(j,n,mu). Then uu'=(i,nu',k) and

`(uu')l=(F_(i,x_(k^-1 n),nu')(j),k t_(k^-1 n),mu)`.

On the other side, write m^-1 n=t_1x_1, so u'l=(F_(i',x_1,nu')(j),m t_1,mu); then write k^-1 m t_1=t_2x_2, so

`u(u'l)=(F_(i,x_2,nu)(F_(i',x_1,nu')(j)),k t_2,mu)`.

Since k^-1 n=k^-1 m t_1 x_1=t_2(x_2x_1) with x_2x_1∈H, uniqueness gives t_(k^-1 n)=t_2 and x_(k^-1 n)=x_2x_1. Finally F_(i,x_2,nu)∘F_(i',x_1,nu')=F_((i,x_2,nu)(i',x_1,nu'))=F_(i,x_2x_1,nu'), because (i,x_2,nu)(i',x_1,nu')=(i,x_2x_1,nu') in the rectangular group. The two sides agree.

The remaining mixed patterns: u l u' gives (F(...),kt,c(nu')) both ways (the F-part ignores columns); u l l' gives (F(...),kt,mu') both ways; l u u' gives (j,n,c(nu')) both ways (uu' has column nu'); l u l' gives (j,n,mu') both ways; l l' u gives (j,n,c(nu)) both ways. Hence B is associative.

### 2.2 Action, W_L and the map

alpha_g preserves every product: upper and lower products are coordinatewise in the G-slot; for upper·lower, (gk)^-1(gn)=k^-1n, so the F-part and t_w are unchanged and the G-slot becomes gk t_w. Each alpha_g is bijective, alpha_g alpha_(g')=alpha_(gg').

Corners: for u=(i,nu,k), u u' u=u for upper u', and u l u=(F(...),k t,c(nu)): all lie in one column, form a left-zero band, and u is an identity on them (u(u l u)=u l u by the u u' l pattern with u'=u; (u l u)u=u l u). So the corner is a left-zero band with an identity adjoined: left regular. For lower l, l x l=l. Hence B∈W_L⊂V.

Products of psi, with x,x'∈H, g,g'∈G:
- UU: ((i,nu,1)(i',nu',x),xx')=((i,nu',1),xx')=psi(i,xx',nu').
- LL: ((j,1,mu)(j',g,mu'),gg')=((j,1,mu'),gg')=psi(j,gg',mu').
- LU: ((j,1,mu)(i,nu,g),gx)=((j,1,c(nu)),gx)=psi(j,gx,c(nu)).
- UL: ((i,nu,1)(j,x,mu),xg). Here w=x∈H, so t_w=1, x_w=x, giving ((F_(i,x,nu)(j),1,mu),xg)=psi(F_(i,x,nu)(j),xg,mu).

Each equals psi of the actual source product. Injectivity: the upper/lower tag and the coordinates (i,nu) or (j,mu), together with the second coordinate x or g, recover the element. The host B⋊G is regular, orthodox, E-unitary with idempotent band B∈W_L, hence an ORIGINAL-target host over the SAME sigma. ∎

### 2.3 Relation to Theorem P

Theorem P is the special case I_1 and Lambda_0 singletons, F_(h,lambda)(i)=h·phi_lambda(i). T2 gives a different and simpler host (a transversal instead of an induced set). The calibration of Theorem P (noncryptic members, non-inverse least locally inverse reflection, non-regular E(S)) therefore applies to T2's class as well. T2 also covers data where different upper ROWS conjugate a shared lower row differently, which is outside Theorem P's shape; there the upper translates (i,nu,k) are genuinely moved by G while upper products ignore translates.

## 3. Corollary T2' — every original-class E-unitary orthogroup with at most two J-classes

**Corollary.** Let S be an orthogroup in the original class (regular local idempotent bands) with an idempotent-pure sigma onto a group G, and with at most two J-classes. Then S embeds over sigma into P(B_L×B_R,G) with B_L∈W_L, B_R∈W_R.

*Proof.* Use the supported one-sided quotients S_R=S/rho_R and S_L=S/rho_L with pure maps over sigma and the source spined-product isomorphism (complete one-sided manuscript Part2 Sections13–16; the sections used are proved there directly). S_R is an orthogroup with at most two J-classes (a homomorphic image), left regular local bands (Part2 Section15), and pure sigma_R onto G.

If S_R has one J-class, it is a rectangular group I×G×Lambda (onto G by purity and ontoness as in §1), and (i,g,lambda)↦((i,lambda),g) embeds it into P(I×Lambda,G) with trivial action; a rectangular band is in W_L. If it has two J-classes, Lemma D presents it as a two-layer datum and Theorem T2 embeds it. Dually, S_L^op is an orthogroup with at most two J-classes and left regular local bands over G^op; applying the same to it and the explicit opposite-host isomorphism (Part2 Section22) gives an embedding of S_L into P(B_R,G), B_R∈W_R, over sigma_L. The explicit Part2 Section16 product map then embeds S into P(B_L×B_R,G) over sigma, with B_L×B_R∈V. ∎

## 4. Exact scope and remaining gap

T2/T2' cover ALL E-unitary orthogroups (with group sigma) of the original class having at most two J-classes, with no hypothesis on subgroup images, crypticity, the least locally inverse reflection or global regularity of E(S). Together with the full-group theorem (any number of J-classes under FULL) this is the current positive orthogroup coverage. NOT covered: orthogroups with three or more J-classes whose maximal subgroups map onto proper subgroups (the transversal construction does not obviously compose across several coset decompositions; an iterated induced-set construction is a natural next attempt, not claimed); non-orthodox completely regular sources and nontrivial Rees actors; non-completely-regular sources; the general normal-row/loaded/multiple-gap/shared-row completion over the SAME actual pure CS C; and any obstruction to ALL allowed hosts. The arbitrary-infinite pure-CS existence prerequisite is untouched.

## 5. Assurance

Exact WRITTEN algebra over ARBITRARY data; the transversal is an arbitrary choice and no numeric instance or probe was used. No scientific interpreter/calculator/eval/program/CAS, enumeration/table/checker, solver/replay, build/test, CLI, nested agent or new GO. The two named classical orthogroup structure facts and the supported one-sided quotient/spine/opposite-host interfaces are the only imports; no LI2003, CG/RU-LU or band-globalization theorem is used. No frozen/shared file edited; no novelty claim. A fresh complete source/dependency/application gate is required before promotion. Same original18/HOLD/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38, actual <=30min substantive JSON cadence, no early final park. Original unrestricted acceptance remains **UNMET**.
