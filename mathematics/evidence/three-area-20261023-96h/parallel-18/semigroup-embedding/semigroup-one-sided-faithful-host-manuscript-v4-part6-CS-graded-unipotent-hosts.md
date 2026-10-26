# One-sided faithful-host manuscript — additive complete Part6, CS-graded R-unipotent hosts

Owner MathSemigroup-2, slot math-4. **AUTHOR-WRITTEN / UNREVIEWED later extension.** Derived after the separate post-v104 primary resumption ACK (actual `Sun Oct 25 18:32:33 PDT 2026`) and after complete Part5. Actual `/bin/date` before this new mathematics: `Sun Oct 25 18:50:54 PDT 2026`. All work is exact WRITTEN regular-semigroup/Rees/band algebra; no interpreter, calculator, program, CAS, enumeration, solver, replay, test or scientific GO. This part does not edit Parts1–5 or any pinned record.

## 51. Statement: an exact theorem replacing the group hypothesis in Part5

Part5's theorem LG needed a pure GROUP image and a globally left-regular idempotent band. Both hypotheses are removed below. Let

`C=M[G;I,Lambda;P]`, `q(s)=(i_s,g_s,lambda_s)`,

be a Rees matrix completely simple semigroup and let A be ANY regular semigroup with an idempotent-pure homomorphism q:A->C (surjectivity is not needed). Call A **q-R-unipotent** if

`(CRU)` e R f in E(A) and q(e)=q(f) imply e=f.

Equivalently, inside every R-class distinct idempotents have distinct q-columns (R-related idempotents have the same q-row, and a C-idempotent is determined by its row/column).

**Theorem CG.** (i) If A satisfies CRU, an explicit LEFT REGULAR BAND B with a G action by automorphisms and an explicit INJECTIVE homomorphism

`Phi:A->P(B,C)`, `Phi(s)=(b_s,q(s))`,

exist, with second coordinate EXACTLY q. (ii) Conversely, if A embeds in a physical product P(B',C') with B' a left regular band, then the second-coordinate map q':A->C' is pure and A satisfies CRU for q'. (iii) Consequently A embeds in P(LRB,CS) for SOME data iff its least completely simple congruence xi is pure and A satisfies CRU for xi.

No band hypothesis on E(A) is made, and no existing embedding theorem is used as a correctness input. If A and G are finite, B is finite.

Here P(B,C) is the fixed physical product of Part1 Section0:

`(b,(i,g,lambda))(d,(j,h,mu))=(b alpha_(g p_(lambda,j))(d),(i,g p_(lambda,j)h,mu))`.

## 52. Proper R-classes: CRU is exactly R-injectivity of q

**Lemma 52.1.** Under purity, CRU holds iff q is injective on every R-class.

If q is R-injective, apply it to idempotents. Conversely let a R b and q(a)=q(b). Choose an inverse a'. Since R is a left congruence, a'a R a'b. Their q-images are equal to the idempotent q(a'a), so purity makes a'b idempotent. CRU gives a'b=a'a. Because aa' is a left identity on R_a, b=aa'b=a(a'b)=a(a'a)=a.

For every R-class rho let `row(rho)` be the common first coordinate of q on rho; it is well defined since q preserves R and the R-classes of C are its rows. For s in A, R_s denotes its R-class and e_rho an idempotent of rho (regularity supplies one; no choice matters below).

## 53. The actual partial band X=(A/R) cross G

For x=(rho,u), y=(sigma,v), declare `x circle y` defined iff there exists s in rho with

`g_s p_(lambda_s,row(sigma))=u^(-1)v`,                         (DEG)

and then put

`(rho,u) circle(sigma,v)=(R_(s e_sigma),u)`.                   (CGP)

The domain depends on rho, u, v and only the ROW of sigma.

**Well-definedness.** If e,e' are idempotents of sigma, then e R e' gives se R se'. If s,s' in rho both satisfy(DEG) with j=row(sigma), and q(e)=(j,p_(mu,j)^(-1),mu), then

`q(se)=(row(rho),u^(-1)v p_(mu,j)^(-1),mu)=q(s'e)`,

and s R s' gives se R s'e. Lemma52.1 gives se=s'e. Thus even the element se, not only its R-class, is independent of every choice.

**(P1) idempotency.** For x=(rho,u), any idempotent e of rho satisfies(DEG) with target row row(rho): `g_e p_(lambda_e,row(rho))=1`. Its value is R_(ee_rho)=rho, because R-related idempotents satisfy ee_rho=e_rho.

**(P2) associativity with domains.** Let x=(rho,u),y=(sigma,v),z=(tau,w), with xy realized by s and yz by t. Then st realizes(xy)z: t R e_sigma and left compatibility give st R se_sigma, so st lies in the R-class of xy, and

`g_(st)p_(lambda_t,row(tau))=g_s p_(lambda_s,row(sigma))g_t p_(lambda_t,row(tau))=u^(-1)w`.

The product yz has row row(sigma), so x(yz) is realized by the same s. Its value is R_(se') for an idempotent e' R te_tau; left compatibility gives se' R ste_tau. Both sides equal(R_(ste_tau),u).

**(P3) domain recovery.** If yz and x(yz) are defined, xy is defined: row(yz)=row(sigma), so the two(DEG) conditions are identical.

**(P4) action.** For k in G put k.(rho,u)=(rho,ku). Since (ku)^(-1)(kv)=u^(-1)v, domains, realizers and values are preserved, with inverse k^(-1).

**(P5) total left-regular slices.** For each u in G and row i put `Y_(u,i)={(rho,u):row(rho)=i}`. Any two members multiply: an idempotent e of rho satisfies(DEG) because row(sigma)=row(rho). The value has row i, so the slice is closed, with product (R_(ee_sigma),u). It is a band by(P1),(P2). It is LEFT REGULAR: if xy=(rho',u), rho'=R_(ee_sigma), and f is an idempotent of rho', then ef=f because rho' lies in eA. Hence fef=f, so fe R f and

`(xy)x=(R_(fe),u)=(rho',u)=xy`.

Every partial product stays in the slice of its FIRST factor, by(CGP) and row(R_(se))=row(rho).

These five properties are exactly the ones used in Part5 Section44, with the total slices Y_g there replaced by Y_(u,i). The left-fold prefix values of any defined word lie in the slice of its first letter.

## 54. Free left-regular completion — the Part5 conservativity proof applies verbatim

Let B be the quotient of the free semigroup X+ by the left-regular-band identities and every relation xy=z for a defined product x circle y=z. Then B is a left regular band. Repeat Part5 Sections44.1–44.4 with Y_(u,i):

- prefix values decrease in their slice: if a=b circle x then b circle a=a by(P2), and a circle b=(b circle a)circle b=b circle a=a in the left-regular slice;
- a repeat letter x after a prefix containing x preserves definedness and value: with b the value through the first x, b circle x=b, a circle b=a, so a circle x=(a circle b)circle x=a circle(b circle x)=a;
- a relation xy=z inside a prefix preserves definedness and value in both directions by(P3),(P2);
- every congruence derivation from a defined word therefore stays defined with the same X value.

Hence the canonical map X->B is INJECTIVE and respects every defined product. The G action(P4) preserves all relations and induces band automorphisms alpha_k. First-occurrence normal forms make B finite when X is finite.

## 55. The explicit faithful map

Define `b_s=[(R_s,1)]` and `Phi(s)=(b_s,q(s))`. For s,t in A the base coordinate of Phi(s)Phi(t) is

`[(R_s,1)] alpha_(g_s p_(lambda_s,i_t))[(R_t,1)]=[(R_s,1) circle(R_t,g_s p_(lambda_s,i_t))]`.

That partial product is realized by s itself, with value (R_(se_t),1). Since t R e_t, st R se_t; thus the value is (R_(st),1)=b_(st) and

`Phi(s)Phi(t)=Phi(st)` for EVERY s,t in A.

If Phi(s)=Phi(t), injectivity of X->B gives R_s=R_t and q(s)=q(t); Lemma52.1 gives s=t. This proves Theorem CG(i).

The host is in the original target class: Part1 Section2 proves P(B,C) regular, locally r-orthodox and weakly E-unitary for every band B; a left regular band has left-regular local corners, so B is an allowed W_L (and V) base. No restricted-carrier reading is used.

## 56. Necessity and the intrinsic criterion

**(ii).** Idempotents of P(B',C') are exactly the elements (b,c) with c idempotent, because their product is (b alpha_1(b),c)=(b,c). Hence the second-coordinate projection is pure, and so is its restriction q' to an embedded copy of A. If e R f in A and q'(e)=q'(f)=c=(i,p_(lambda,i)^(-1),lambda), write their images (b,c),(d,c). R-relatedness persists in the host, and the products give bd=d, db=b. In a left regular band this forces b=db=(bd)b=bdb=bd=d, the fourth equality being the identity xyx=xy. Injectivity gives e=f.

**(iii).** For regular A, arbitrary direct products and regular subsemigroups of completely simple semigroups are completely simple (the latter is Part1 Section8), so the intersection xi of all completely simple congruences is the least one. If A embeds in P(LRB,CS), its second coordinate has a completely simple image, its kernel contains xi, purity of that kernel makes xi pure, and CRU for the coarser kernel implies CRU for xi. Conversely apply(i) to q_xi.

The criterion is sharp: the positive source E5 of Part3 Section27 lies in W_L and embeds with base E5 over its least quotient LZ2, but its upper elements0,1 are R-related idempotents with the same least-CS image. By(iii) E5 has NO embedding with a left regular base over ANY completely simple semigroup. Hence a W_L base with nontrivial Green R is NECESSARY there; this is a positive-source route boundary, not a nonembedding witness.

## 57. Application to the original one-sided factors and to S

Keep the original data of Parts1–2: S regular, locally r-orthodox, with actual pure q:S->C; T=S/theta its least locally inverse reflection with descended pure q_T; S_R=S/rho_R, S_L=S/rho_L, with pure p_R:S_R->T (kernel in L) and p_L:S_L->T (kernel in R), Part2 Section15.

**Lemma 57.1.** S_R is q-R-unipotent iff T is q_T-R-unipotent. Dually S_L is q-L-unipotent iff T is q_T-L-unipotent.

By Part2 Section17(RCOV), p_R restricts to a bijection R_(S_R)(a)->R_T(p_R(a)), and the lift of an idempotent in that prescribed class is idempotent. If T satisfies CRU and e R f are idempotents of S_R with equal q-images, then p_R(e) R p_R(f) are idempotents with equal q_T-images, hence equal, and RCOV injectivity gives e=f. Conversely distinct R-related idempotents of T with one q_T-image lift, inside one source R-class, to distinct idempotents with one q-image. The dual uses the L-class bijections of p_L.

**Theorem RU-LU.** If the locally inverse reflection T satisfies BOTH

`(CRU_T)` R-related idempotents with equal q_T-image are equal, and
`(CLU_T)` L-related idempotents with equal q_T-image are equal,

then S embeds in P(B_L cross B_R,C) OVER THE SAME q, with B_L a left regular band and B_R a right regular band, by an explicit map.

Proof. Lemma57.1 and CG(i) give j_R:S_R->P(B_L,C) over the descended q. In the opposite semigroup, S_L^op is q^op-R-unipotent over the completely simple C^op; CG gives an LRB host there, and the explicit opposite-host coordinate isomorphism of Part2 Section22 converts it to j_L:S_L->P(B_R,C) with B_R the opposite, a right regular band, over the SAME C. Part2 Section16 then gives the injective map s->((b_L(s rho_R),b_R(s rho_L)),q(s)) through the source spined-product isomorphism J. B_L cross B_R is a regular band, hence lies in V.

Special case: if T is INVERSE, every R- and L-class has one idempotent, so CRU_T and CLU_T hold and the embedding follows. If T=C with q_T the identity, they hold as well.

RU-LU uses CG, Part2 Sections15–17 (quotient sources, spined product and RCOV) and Section22 (opposite host), at their existing written assurance. It does NOT use an embedding of T into P(N,C), the canonical normal-base identification or the substantial Billhardt–Szendrei import as an input of the new argument. If a future gate finds any cited older section transitively consuming that import, the import remains in the union; this part does not certify the old ancestry anew.

## 58. Exact remaining gap after Part6

The constructive region now includes EVERY original source whose locally inverse reflection is q_T-R- and q_T-L-unipotent, and, one-sidedly, every factor whose reflection satisfies the corresponding condition. The remaining original problem is exactly the complement on at least one side: T has two distinct R-related (or L-related) idempotents with the same q_T-image. For the R side, by 56(iii) and Lemma57.1 such a factor has NO left regular host over any completely simple semigroup, so a faithful W_L base with nontrivial Green R must be built, as for the positive E5; the dual holds on the L side. The general faithful W_L/W_R completion with every(M), loaded/multiple-gap consequence, shared lower row and source-idempotent separation, or a genuine canonical negative witness, remains OPEN. Separately, existence of a pure completely simple quotient for arbitrary infinite nonorthodox input remains OPEN; CG/RU-LU assume an actual pure q.

The local-monoid charts of Part5 are a special case of CG (group-valued q, R-unipotent), so their non-covering control in Part5 Section48 remains a statement about charts only; T=Y semidirect C2 there is inverse and is covered globally by RU-LU.

## 59. Assurance

Every load-bearing step above is written out. Classical inputs are ordinary Rees/Green/inverse facts, free-band quotients and the old Part1–2 sections named in Section57. The constructions are classical in style and NO novelty or literature priority is claimed. This Part6 is later than every frozen source and parent decision, is AUTHOR_WRITTEN/UNREVIEWED and requires its own complete union gate before promotion. It is not formal/kernel proof, configured-family or human acceptance, an executable certificate, a solution of the full original problem, or a round closeout. All process findings, M1, the HOLD and the original cutoff/deadline remain.
