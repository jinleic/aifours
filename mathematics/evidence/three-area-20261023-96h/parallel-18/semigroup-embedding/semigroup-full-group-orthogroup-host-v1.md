# Every original-class orthogroup whose maximal subgroups all map ONTO its group image embeds

Owner MathSemigroup-2, original math-4. Actual `/bin/date` BEFORE this new body: **Mon Oct26 08:14:38 PDT2026**. **NEW AUTHOR-WRITTEN / UNREVIEWED / no novelty claim.** A proper ORIGINAL-class theorem with a complete explicit host, NOT the unrestricted embedding theorem and not an obstruction.

## 0. Provenance and boundaries

Everything in this body was developed AFTER the ACTUAL v123-D RETURN and the NEW whole qualified primary ACK `6486d372cbad61059ea955a6ce9538a62d3888581129aea68186745ca15da8e6`, observed07:52:08, WRITTEN and SENT, under parent direction v42 (`9d406187...`). It is not a pre-receipt or post-receipt exposed lead. The four individually identified own MAJOR occurrences (three v113, one v123 intake pause) and the older read-order finding remain permanent; nothing here cures them.

Scope: the physical Pastijn product with C a GROUP G (singleton Rees indices, sandwich1), so P(B,G)=B⋊G with (b,g)(d,h)=(b alpha_g(d),gh). Bands: V (regular local corners), W_L (left regular local corners), W_R its dual. "Orthogroup" means orthodox completely regular semigroup.

Named standard structure inputs (classical, not re-proved here): an orthogroup is a semilattice Y of rectangular groups S_alpha; an orthodox completely simple semigroup is a rectangular group I×K×Lambda with (i,g,lambda)(j,h,mu)=(i,gh,mu). These are stated, e.g., as Lemmas1.5/1.6 of arXiv1901.08776v1 (citing Petrich–Reilly), which I read in its returned first300 of594 lines; no other part of that paper is used. Everything else is proved below.

## 1. Statements

Let S be an orthogroup, s^0 the identity of the maximal subgroup containing s and E=E(S). Let sigma:S→G be an onto idempotent-pure homomorphism to a group. Purity makes sigma injective on every maximal subgroup H_e: if sigma(s)=sigma(t) for s,t∈H_e, then sigma(st^-1)=1, so st^-1 is an idempotent of H_e, hence e, and s=t.

**Hypothesis FULL:** sigma maps EVERY maximal subgroup H_e ONTO G. Then for every e∈E and w∈G there is a UNIQUE s_(e,w)∈H_e with sigma(s_(e,w))=w, and s↦(s^0,sigma(s)) is a bijection S→E×G.

**Theorem Q (one-sided).** Let S be an orthogroup whose local idempotent bands eEe are all LEFT regular, with sigma as above satisfying FULL. Define on B=E×G

`(e,k)(f,m)=(pi(e,k^-1 m,f),k)`, `pi(e,w,f)=(s_(e,w) f)^0`,

and `alpha_g(e,k)=(e,gk)`. Then B is a band in W_L, each alpha_g is a band automorphism, and

`psi(s)=((s^0,1),sigma(s))`

is an INJECTIVE homomorphism S→B⋊G over the SAME sigma.

**Corollary Q2 (two-sided).** Let S be an orthogroup in the original class (all local idempotent bands regular) with sigma satisfying FULL. Then S embeds over sigma into P(B_L×B_R,G) with B_L∈W_L, B_R∈W_R.

## 2. The key identity P0 for W_L orthogroups

**Lemma P0.** If S is an orthogroup with left regular local idempotent bands, then for ALL x,y∈S

`(xy)^0=(x y^0)^0`.

*Proof.* Put f=y^0 and z=xf. Then xy=xfy=zy, and zf=z. Write S as a semilattice of rectangular groups; let f∈S_alpha and z∈S_gamma, so gamma<=alpha because z=xf.

*Bitranslation form.* For any s∈S_alpha and gamma<=alpha, x↦sx and x↦xs map the rectangular group S_gamma=I×K×Lambda into itself and form a linked bitranslation. For a left translation lambda, writing (i,g,mu)=(i,1,nu)(j,g,mu) gives lambda(i,g,mu)=lambda(i,1,nu)(j,g,mu); hence lambda(i,g,mu)=(F(i),c_i g,mu), independent of nu and j. Dually a right translation is (i,g,mu)↦(i,g d_mu,R(mu)). Linking `(x rho)y=x(lambda y)` gives d_mu=c_j for all mu,j, a common constant a. So multiplication by s acts on S_gamma as

`s(i,g,mu)=(F_s(i),a_s g,mu)`, `(i,g,mu)s=(i,g a_s,R_s(mu))`.

For an idempotent s, rho_s rho_s=rho_s forces a_s=1, and F_s,R_s are idempotent maps.

*Case gamma=alpha.* In S_alpha write f=(j,1,mu) and z=(i,g,lambda). zf=z forces lambda=mu. Every y∈H_f has the form (j,h,mu), so zy=(i,gh,mu) has the same row and column as z. Hence (zy)^0=z^0.

*Case gamma<alpha.* The idempotents of the corner fEf lying in S_gamma are f(i,1,mu)f=(F_f(i),1,R_f(mu)), i.e. the rectangular band F_f(I)×R_f(Lambda). A left regular rectangular band is left zero, so R_f(Lambda) is a single column c. For y∈H_f, yf=y gives rho_y=rho_f∘rho_y on S_gamma, so R_y maps into R_f(Lambda)={c}: R_y is constant c. Also zf=z gives column(z)=R_f(column z)=c. Thus zy=(row z, ·, c) has the same row and column as z, and (zy)^0=z^0. ∎

## 3. Proof of Theorem Q

**Associativity.** For e,f,g∈E and k,m,n∈G, put w=k^-1 m and v=k^-1 n:

`((e,k)(f,m))(g,n)=(pi(pi(e,w,f),v,g),k)`,

`(e,k)((f,m)(g,n))=(pi(e,w,pi(f,w^-1 v,g)),k)`.

Let p=pi(e,w,f)=(s_(e,w)f)^0 and u=w^-1 v. By P0 with x=s_(e,w), y=s_(f,u): (s_(e,w)s_(f,u))^0=(s_(e,w)f)^0=p. The product s_(e,w)s_(f,u) lies in H_p and has sigma-value wu=v, so it EQUALS s_(p,v) by uniqueness. By P0 with x=s_(e,w), y=s_(f,u)g:

`pi(e,w,pi(f,u,g))=(s_(e,w)(s_(f,u)g)^0)^0=(s_(e,w)s_(f,u)g)^0=(s_(p,v)g)^0=pi(p,v,g)`.

So B is associative. Idempotency: (e,k)(e,k)=((s_(e,1)e)^0,k)=((ee)^0,k)=(e,k). Thus B is a BAND.

**Action.** alpha_g((e,k)(f,m))=(pi(e,k^-1m,f),gk)=(e,gk)(f,gm), because (gk)^-1(gm)=k^-1m. Each alpha_g is bijective with inverse alpha_(g^-1), and alpha_g alpha_(g')=alpha_(gg'). So G acts by band automorphisms.

**B∈W_L.** For an element (e,k), a typical corner element is (e,k)(f,m)(e,k)=(pi(p,1,e),k) with p=pi(e,k^-1m,f). Here pi(p,1,e)=(pe)^0=pe, since s_(p,1)=p and S is orthodox. Moreover ep=p: p is the identity of the group containing s_(e,w)f, which lies in eS; hence e fixes it on the left, and e·p=p. So pe=epe∈eEe. On elements (x,k),(y,k) with x,y∈eEe the product is (pi(x,1,y),k)=(xy,k). Therefore the corner at (e,k) is isomorphic to a subband of eEe, which is LEFT regular by hypothesis. Hence every local corner of B is left regular: B∈W_L⊂V.

**psi is a homomorphism over sigma.** ψ(s)ψ(t)=((s^0,1)alpha_(sigma(s))(t^0,1),sigma(s)sigma(t))=((s^0,1)(t^0,sigma(s)),sigma(st)). The first coordinate is (pi(s^0,sigma(s),t^0),1). Since s_(s^0,sigma(s))=s, it equals ((st^0)^0,1)=((st)^0,1) by P0. So ψ(s)ψ(t)=ψ(st), for EVERY pair s,t, including products in different J-classes.

**Injectivity.** ψ(s) determines (s^0,sigma(s)), which determines s by FULL and purity.

**Host properties.** P(B,G)=B⋊G is regular ((b,g) has inverse (alpha_(g^-1)(b),g^-1)), its idempotents are B×{1} because the group projection is pure, its idempotent band is B∈W_L, and it is E-unitary, hence weakly E-unitary and locally r-orthodox. The second coordinate of ψ is exactly sigma. If E and G are finite, B is finite; arbitrary infinite data are allowed. ∎

## 4. Proof of Corollary Q2

Use the supported intrinsic one-sided quotients S_R=S/rho_R, S_L=S/rho_L, with their pure maps over the same sigma and the source spined-product isomorphism (complete one-sided manuscript Part2 Sections13–16). S_R is an orthogroup (a quotient of an orthogroup), and its local idempotent bands are LEFT regular (Part2 Section15). The induced map sigma_R:S_R→G is pure.

FULL passes to S_R: for a maximal subgroup H of S_R containing an idempotent e·rho_R, the image (H_e)rho_R lies in H (it is a subgroup with identity e·rho_R), so sigma_R(H)⊇sigma(H_e)=G; injectivity is purity. Hence Theorem Q gives an injective j_R:S_R→P(B_L,G) over sigma_R with B_L∈W_L.

Dually S_L^op is an orthogroup with left regular local bands and FULL over G^op; Theorem Q gives a W_L host for it, and the explicit opposite-host isomorphism (Part2 Section22) converts it to an injective j_L:S_L→P(B_R,G) over sigma_L, B_R∈W_R. The explicit Part2 Section16 product map

`s↦((b_L(s rho_R),b_R(s rho_L)),sigma(s))`

into P(B_L×B_R,G), with diagonal action, is then an injective homomorphism; B_L×B_R is a band with regular local corners (W_L×W_R⊂V). ∎

## 5. Relation to existing positive results and calibration

- **LG** (supported whole-factor theorem) needs GLOBALLY left regular idempotents; Theorem Q needs only LEFT regular LOCAL corners, but it needs an orthogroup and FULL. They overlap without either containing the other.
- **Theorem P** (the right-group-over-left-group family, `semigroup-induced-host-right-left-group-family-v1.md`, `2af0f8a3...`) with H=G satisfies FULL; Theorem Q recovers it with a different host. Theorem P with H a PROPER subgroup violates FULL and is NOT covered by Theorem Q; conversely Theorem Q covers orthogroups with many J-classes and arbitrary corner structure that are not of Theorem P's two-layer shape.
- Members of Theorem P with H=G, |Lambda|>=2, nontrivial action and differing retractions satisfy FULL and are noncryptic, have a non-inverse least locally inverse reflection, a non-left-regular and non-regular E(S). Hence Theorem Q is genuinely beyond CT, Theorem I, LG and the classical regular-band hypothesis.
- In the current MG/IC representation for completely regular sources, Theorem Q supplies an actual W_L model, so ISEP HOLDS for every one-sided W_L orthogroup with FULL.

## 6. Exact remaining gap

Not covered: orthogroups whose maximal subgroups map onto PROPER subgroups of G in a way not of Theorem P's form; non-orthodox completely regular sources (with nontrivial Rees actor C); non-completely-regular sources; the general normal-row/loaded/multiple-gap/shared-row W_L/W_R completion over the SAME actual pure CS C; or an obstruction to ALL allowed hosts. The arbitrary-infinite pure-CS existence prerequisite is untouched (here sigma is supplied). No claim that FULL is necessary.

## 7. Assurance

All new identities are exact WRITTEN algebra over ARBITRARY data; no chosen numeric instance or probe, scientific interpreter/calculator/eval/program/CAS, enumeration/table/checker, solver/replay, build/test, CLI, nested agent or new GO. Ordinary group/semigroup facts and the two named classical orthogroup structure facts are the only imports; Corollary Q2 additionally uses the supported one-sided source quotient/spine/opposite-host interfaces of the complete one-sided manuscript at their recorded boundaries (Part2's original LI2003 dependence is not used by these specific sections, but no blanket ancestry upgrade is claimed). No frozen/shared file edited. A fresh complete source/dependency/application gate is required before any promotion. Same original18/HOLD/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38, actual <=30min substantive JSON cadence, no early final park. Original unrestricted acceptance remains **UNMET**.
