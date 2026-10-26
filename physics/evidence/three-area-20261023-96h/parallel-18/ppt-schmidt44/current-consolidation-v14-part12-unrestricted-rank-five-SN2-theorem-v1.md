# CURRENT P44 CONSOLIDATION v14 — PART12/12: an UNRESTRICTED low-rank theorem — every 4x4 PPT state with rank(rho)<=5 or rank(rho^Gamma)<=5 has Schmidt number <=2

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Sun Oct 25 22:32:17 PDT 2026**. Exact WRITTEN mathematics plus EXPLICITLY NAMED published imports. No scientific interpreter/calculator/eval/program/CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO. Same original cutoff and deadline.

## L0. Scope and union rule

NEW claim C31 is not a covariance class or a chart. It applies to EVERY 4x4 PPT state, restricted only by rank:

**Theorem C31.** Let rho be any (unnormalized) PPT operator on C^4 tensor C^4. If rank(rho)<=5 or rank(rho^Gamma)<=5, then SN(rho)<=2.

Consequently any 4x4 PPT state with Schmidt number three must have BOTH rank(rho)>=6 and rank(rho^Gamma)>=6. This narrows the original P44 search space. It is not a solution of P44 and not an all-rank theorem. The proof composes the peel-off theorem (proved inline) with four NAMED imports (L1). Each import is quoted at the exact statement used and was read in this session. **Their correctness is imported, not re-proved.** No novelty or priority is claimed: the combination may be folklore.

The complete current union is ALL TWELVE parts and endings:
- the eleven parts bound in `checkpoint-086-complete-current-v13-eleven-part-manifest-v1.json` (SHA256 6bb6813659e9ba85aa6781c67e8ccb2b77368e4cb9cac0aa53c083801db7c706);
- THIS part;
- every mandatory overlay named there.

All process findings remain permanent, including cp083 (cadence miss + exactness MAJOR) and cp085 (later exactness occurrence). Parts 9–12 are LATER UNREVIEWED; nothing is inherited.

## L1. Named imports, at exact statement

- **I1 (Chen–Đoković, arXiv:1203.1364, abstract read this session).** Let E_r^{M,N} be the extreme points of the PPT state set with rank r and reduced ranks (M,N). Then E_r^{M,N}=∅ for 1<r<=min(M,N), and "E_{N+1}^{M,N} is empty if M,N>3". For M=N=4 this gives E_r^{4,4}=∅ for r=2,3,4,5. E_1 consists of pure product states.
- **I2 (Yang–Leung–Tang, arXiv:1603.03534, Theorem 3.2 and the stated equivalence of Conjectures 1.1/1.2, read this session).** Every 3x3 PPT state has SN<=2.
- **I3 (Kraus–Cirac–Karnas–Lewenstein, arXiv:quant-ph/9912010, Lemma 7, read this session).** If a PPT operator on C^2 tensor C^N, supported on C^2 tensor C^N, has a product vector in its kernel, then rho=rho~+rho_s, where rho_s is a product projector, rho~ is PPT and supported on C^2 tensor C^(N-1), and rho~ is separable iff rho is. Together with the Peres–Horodecki 2x3 theorem: **every 2x4 PPT operator with a product vector in its kernel is separable.** If the Bob support is <=3, apply 2x3 directly. Lemma 6(i) is the reduced-support case.
- **I4 (classical projective dimension theorem).** Any linear subspace of C^3 tensor C^4 of dimension >=7 contains a nonzero product vector. The Segre variety P^2 x P^3 has projective dimension 5 in P^11, and a linear P^6 meets it. Equivalently, completely entangled subspaces of C^m tensor C^n have dimension <=(m-1)(n-1)=6.
- **I5 (KCKL Lemma 5, same source).** For PPT rho, a product vector e tensor f lies in ker(rho) iff its partially conjugated partner lies in ker(rho^Gamma). With Bob transposition this partner is e tensor conj(f). Proof: <e,f|rho|e,f> = <e,conj f|rho^Gamma|e,conj f>, and both operators are PSD.

## L2. Peel-off lemma, proved inline

**Lemma P.** Let rho be PSD on C^m tensor C^n, e a unit vector in C^m, and P the projector onto e-perp. If (P tensor I)rho(P tensor I) is separable, then SN(rho)<=2. The same holds with the roles of Alice and Bob exchanged.

Proof. Let W be any two-block-positive Hermitian operator. Write its blocks relative to the Alice splitting e-perp ⊕ Ce as W_pp, W_pe, W_ep, W_ee.

For a in e-perp and arbitrary b, y, the vector a tensor b + e tensor y has Schmidt rank <=2. So the quadratic form in y,

`<ab|W_pp|ab> + 2Re<ab|W_pe|y> + <y|W_ee|y>`,

is nonnegative for all y. This forces:
- W_ee>=0;
- W_ep(a tensor b) in range(W_ee), and by linearity W_ep maps everything into range(W_ee);
- <ab|R|ab>>=0, where R=W_pp-W_pe W_ee^+ W_ep (Moore–Penrose pseudoinverse).

Put `U=[W_pe; W_ee] W_ee^+ [W_ep, W_ee] >= 0`. The range inclusion gives W_ee W_ee^+ W_ep=W_ep and W_ee W_ee^+ W_ee=W_ee, so W=U+(R direct-sum 0). Since U>=0 and R is block-positive on e-perp tensor C^n,

`Tr(W rho) = Tr(U rho) + Tr(R (P tensor I)rho(P tensor I)) >= 0`.

The SN<=2 cone is closed, convex and dual to the two-block-positive cone. By the bipolar theorem rho lies in it. QED.

## L3. Proof of Theorem C31

**Step 1 (3x4 kernel lemma).** Let sigma be a PPT operator supported on C^3 tensor C^4 (or C^4 tensor C^3) with a product vector alpha tensor beta in its kernel. Choose any two-dimensional subspace A_2 of the three-dimensional side containing alpha. The compression sigma'=(P_A2 tensor I)sigma(P_A2 tensor I) is PPT (local congruence) and PSD. It has alpha tensor beta in its kernel, because <alpha beta|sigma'|alpha beta>=<alpha beta|sigma|alpha beta>=0. By I3 sigma' is separable. Passing from the three-dimensional side to A_2 is one hyperplane compression, so Lemma P gives SN(sigma)<=2.

**Step 2 (rank(rho)<=5).** The PPT trace-one set is compact and convex in finite dimension, so rho is a finite positive combination of extreme PPT states sigma_k (Krein–Milman/Carathéodory). Each sigma_k <= rho/p_k, hence range(sigma_k) ⊆ range(rho) and rank(sigma_k)<=5. Let (M',N') be its reduced ranks. Restricted to its local supports, sigma_k is still extreme there.
- min(M',N')<=2: every vector in its range has Schmidt rank <=2, so SN<=2.
- (3,3): I2 gives SN<=2.
- (3,4) or (4,3): its kernel inside the 12-dimensional support has dimension >=7, so by I4 it contains a product vector. Step 1 gives SN<=2.
- (4,4): rank<=5 with I1 forces rank 1, so sigma_k is a pure product state.

The SN<=2 cone is convex, so SN(rho)<=2.

**Step 3 (rank(rho^Gamma)<=5).** tau=rho^Gamma is itself a PPT operator, since tau^Gamma=rho>=0. Decompose tau into extreme PPT states tau_k as in Step 2, and note rho=sum p_k tau_k^Gamma. Each tau_k^Gamma is PSD and PPT on the same local supports.
- Product tau_k: tau_k^Gamma is a product projector.
- 3x3 tau_k: tau_k^Gamma is a 3x3 PPT state, SN<=2 by I2.
- Reduced rank <=2: trivial.
- 3x4/4x3 tau_k of rank<=5: it has a kernel product vector alpha tensor beta (I4). By I5, alpha tensor conj(beta) lies in ker(tau_k^Gamma), and Step 1 applies to tau_k^Gamma.
- Full (4,4) local ranks: product by I1.

Hence every tau_k^Gamma is SN<=2, and so is rho. QED.

## L4. Consequences, sharpness boundary and non-claims

1. **Rank floor.** A 4x4 PPT state with Schmidt number 3, if one exists, has rank(rho)>=6 and rank(rho^Gamma)>=6. Each of its extreme PPT components either has full local ranks (4,4) and rank >=6, or is 3x4/4x3 of rank >=6. In I1 terms, the full-rank case needs E_r^{4,4} with r>=6 (nonempty for r=6 by I1's proved Leinaas–Myrheim–Sollid first part). For the 3x4 case, rank >=6 means the kernel has dimension <=6 and may avoid product vectors.
2. **Relation to the original chart.** Every R_x has rank nine, so C31 does not touch the open balanced core of Parts 10/11.
3. **Why rank 5 is the natural boundary of this method.** The rank-5 range of a 4x4 state would meet the SR<=2 locus (codimension 4, degree 20) in finitely many points. That would make the SN<=2 states on that range a cone of dimension <=20 inside 25. **C31 shows this tempting mechanism never produces SN3: every rank-5 4x4 PPT state already decomposes through products and lower-dimensional SN2 extremes.** This is recorded because it closes a natural new route, not as a separate claim.
4. **NOT claimed:** no statement about rank 6 or higher, no all-state SN2 theorem, no solution of P44, and no novelty/priority. The imports are trusted at their quoted statements and are not independently re-proved here.

**Original physics-3/P44 remains UNMET.** This is an author-WRITTEN composition pending fresh complete reconstruction, including a reviewer's own reading of I1, I3 and I5. It is not formal/kernel/executable/triple/configured-family/human/cross-vendor/novelty acceptance, not a park and not a closeout.

**END OF COMPLETE CURRENT v14 PART12/12.**
