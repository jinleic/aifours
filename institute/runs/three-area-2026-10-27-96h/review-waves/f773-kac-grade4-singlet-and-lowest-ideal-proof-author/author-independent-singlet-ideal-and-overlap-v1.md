# Independent grade-four singlet, submodule, ideal criterion, and overlap bounds

**GENERAL AUTHOR; unadopted, nonblind same-harness written reconstruction.** The observed native clock before creation was 2026-10-30T18:01:48-0700 PDT; this is not a claimed completion timestamp. The conclusions below are conditional on the precise imports in §1, require a separate complete parent reading and disposition, and do not establish all of grade four or global Serre equality. No scientific executable was run or proposed. The six remaining radical types at r=3, and the corresponding remaining whole-copy questions for r=1,2, are not evaluated by this note.

## 1. Domain and imports

Let
\[
 A(r,s)=\begin{pmatrix}2&-1&-1\\-1&2&-1\\-r&-s&2\end{pmatrix},\qquad r\in\{1,2,3\},\quad s\in\mathbb Z,\ s>r.
\]
For **every full complex Cartan realization**, including singular cases with additional Cartan directions, let G be the displayed preliminary Chevalley algebra, J the ideal of **both signs of all** Serre relations, S=G/J, τ the unique maximal ideal disjoint from the **whole** Cartan, and R=τ/J. Write S_(a,b,n) for the entire homogeneous root component; E_i,F_i are the actual adjoint Chevalley operators. Put
\[
 L_{a,b}=\{v\in S_{(a,b,4)}:F_1v=F_2v=0\}.
\]
These spaces include every equivalent irreducible copy and every diagonal mixture.

The named inputs are: S6's actual ordinary-free-Lie source L(V), its positive/negative whole-Serre ideal bridge and full-Cartan injection; S4 and S5's actual quotient/character and **entire grade-three** radical-zero import, with their own stated qualifications; S7's letter/action identities; and characteristic-zero tensor embedding, finite-dimensional sl₃ complete reducibility, and the Weyl/Witt formulas. In particular the grade-three theorem is imported through the expressly stated S4/S5 interface; this note has not opened their linked underlying proofs. S2 and S3 are the complete **unadopted** candidate and addendum being reconstructed, not imported conclusions. No preliminary-G PBW theorem, global J=τ, source identity, or external review is assumed.

Use the S7 letters V=⟨x,a,b,c,d,e,f,g⟩ with horizontal degrees (0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2). Put
\[
 q=[x,a],\quad q'=[x,b],\quad Q=U(\mathfrak{sl}_3)q\cong L(0,3),\quad Q'=U(\mathfrak{sl}_3)q'\cong L(3,0).
\]
The letters are free-Lie/tensor letters, not matrix products. Q,Q′ are the two distinct ten-dimensional summands of Λ²V. S7 supplies the complete lowering/raising table, the Q_i identities below, and the grade-three relation at each boundary; §2 recomputes the load-bearing actual F₃ images rather than supposing F₃ Levi-equivariant.

## 2. The two whole degree-three bracket modules are disjoint

Define U=[V,Q] and U′=[V,Q′] in the **free** L₃(V). The bracket maps V⊗Q→U and V⊗Q′→U′ are injective. For the first map, its four distinct tensor-product types are L(1,4), L(2,2), L(0,3), L(1,1). Set Q₁=E₂q, Q₂=E₂²q, Q₃=E₁E₂q, Q₄=E₁E₂²q. Lowest representatives are
\[
 [x,q],\quad 3[b,q]-[x,Q_1],\quad [c,q]-2[d,q]+[a,Q_1]-[x,Q_3],\quad
 [x,Q_4]-2[a,Q_2]-4[b,Q_3]+4[d,Q_1]-12[f,q].
\]
The S7 lowering table annihilates each representative; each is nonzero in the free tensor embedding: respectively it contains a nonzero xxa, xxd, xxe, or xxg tensor contribution unavailable from the other displayed terms. Thus all four multiplicity-one summands of V⊗Q survive, and the map is injective. The formal interchange of Levi arms gives the same statement for Q′. It is a substitution in the universal Levi/action table, **not** an automorphism of a fixed nonsymmetric A(r,s). Hence
\[
\begin{aligned}
 U&\cong L(1,4)\oplus L(2,2)\oplus L(0,3)\oplus L(1,1),\\
 U'&\cong L(4,1)\oplus L(2,2)\oplus L(3,0)\oplus L(1,1).
\end{aligned}
\]
Only the 27 and 8 types are common. Their lowest vectors must be compared **inside the free Lie space**. For the 27s take
\[
 t=3[b,q]-[x,Q_1],\qquad t'=3[a,q']-[x,E_1q'].
\]
Using F₃q=2(r−1)a, Q₁=[x,d]−[a,b], and the actual derivation table gives
\[
 F_3t=(6-3r-4s)[x,d]+(2-5r+4s)[a,b],\quad
 F_3t'=(6-4r-3s)[x,c]+(5s-4r-2)[a,b].
\]
For r=2,3 and s>r, S₂=Λ²V and the three exterior pairs displayed are independent. The coefficients of [x,d] and [x,c] are respectively strictly negative, so t and t′ are independent. This uses a common linear map to detect independence; it does **not** require that F₃ intertwine the Levi action.

For the 8s, let z denote the last representative above and let z′ be its formal arm swap with r,s swapped in the actual-action formulas. To expose the key calculation, set P=[x,g], W=[a,f], H=[b,e], T=[c,d]. The S7 table yields
\[
 Q_4=2(P+W-H+T),\quad F_3Q_1=2(r-1)d,\quad F_3Q_2=4(r-1)f,\quad
 F_3Q_3=-2(r-1)e,\quad F_3Q_4=4(r-1)g.
\]
Here F₃ commutes with E₁,E₂ only because [f₃,e₁]=[f₃,e₂]=0; no commutation with the lowerings is asserted. In particular E₂Q₃=E₁₂Q₁=Q₄/2. Expanding the five brackets in z gives
\[
 F_3z=(6r+4s-4)Q_4+4(r-1)P+16(r-1)W+8(r-1)H.
\]
In the ordered basis (P,W,H,T), the two actual images therefore are
\[
\begin{aligned}
 v&=(16r+8s-12,\ 28r+8s-24,\ -4r-8s,\ 12r+8s-8),\\
 v'&=(8r+16s-12,\ 8r+4s,\ 24-8r-28s,\ 8-8r-12s).
\end{aligned}
\]
This gives a simpler independently checkable two-coordinate minor than the candidate's three-vector determinant: v_P,v_T,v′_P are positive while v′_T is negative throughout r=2,3 and s>r. Thus v_Pv′_T−v′_Pv_T<0. P and T are independent exterior pairs in the actual degree-two source, so the two 8 lowest vectors are independent as free words. Together with the 27 argument and complete reducibility,
\[
 U\cap U'=0\quad\text{in }L_3(V) \qquad(r=2,3,\ s>r).
\]
Although U,U′ themselves are parameter-independent, this proof of disjointness uses actual F₃ at the indicated allowed parameters. For r=3 the actual grade-three quotient is free. For r=2 its **whole** relation is the L(1,4) contained in U, so the images of U/L(1,4) and U′ remain disjoint and V⊗Q′→S₃ remains injective. No disjointness of the two grade-four seed ideals is assumed.

## 3. The 100-dimensional bracket, singlet and whole-submodule intersection

The map
\[
 \beta:Q\otimes Q'\to L_4(V),\qquad u\otimes v\mapsto[u,v]
\]
is injective. Indeed choose projections V⊗V→Q,Q′ which annihilate the other module. In the associative tensor embedding, applying their tensor product to uv−vu recovers u⊗v. The identity holds on all sums, not merely a preferred pure tensor. Standard symmetric-cube tensor decomposition gives
\[
 Q\otimes Q'\cong L(0,0)\oplus L(1,1)\oplus L(2,2)\oplus L(3,3),\qquad \dim=1+8+27+64=100.
\]
For r=3 the whole grade-four relation is the one L(2,5) (S4/S6), with no shared type, so all 100 dimensions embed in the actual S₄. For r=2, the first relation is an image of
\[
 V\otimes L(1,4)=L(2,5)\oplus L(3,3)\oplus L(0,6)
 \oplus2L(1,4)\oplus L(2,2)\oplus L(0,3).
\]
At s=3 the second relation is L(5,2); for s≥4 it has higher grade. Neither contribution contains a singlet or adjoint, so the L(0,0)⊕L(1,1) part of β embeds for every r=2,s≥3, even if arbitrary relation contributions overlap elsewhere.

Now let B denote the embedded part just specified. For a Levi-lowest z∈B suppose F₃z=0. Let N be the negative grade-one Levi module generated by f₃ under ad f₁,ad f₂. Since F₁z=F₂z=0, Jacobi inductively gives [N,z]=0. Write the unique free preimage of z as \(\sum_i u_i\otimes v_i\), choosing the v_i∈Q′ independent. For w∈N,
\[
 0=[w,z]=\sum_i[[w,u_i],v_i]+\sum_i[u_i,[w,v_i]].
\]
The first sum lies in the actual U′ image and the second in the actual U image; §2 makes them disjoint, including after the r=2 relation. Injectivity V⊗Q′→S₃ then forces [w,u_i]=0 for all i and w. The common annihilator K={u∈Q:[N,u]=0} is a Levi submodule by Jacobi, and is proper because
\[
 [f_3,q]=2(r-1)a\ne0 \quad(r=2,3).
\]
As Q is irreducible, K=0, contradicting z≠0. Therefore **actual F₃ is injective on each complete lowest space inside B**. This proof uses the actual F₃ action and the full N; it does not assert F₃-injectivity on all raised vectors.

The free singlet multiplicity is one. From S4's complete character array it equals 84−65−65+36+36−25=1 at (a,b)=(4,4). β supplies its nonzero free representative. At r=1 the entire Q is a degree-two relation, so this representative dies and no quotient can acquire a new singlet. At r=2,3 it survives by the preceding type argument and its one-dimensional lowest map has rank one. Consequently the **actual entire singlet multiplicity is 0 for r=1 and 1 for r=2,3**, and its whole isotypic component is disjoint from R using R∩S₃=0.

Moreover B∩(R∩S₄)=0 for the full 100-dimensional B at r=3 and for its L(0,0)⊕L(1,1) part at r=2. Indeed the intersection is a finite-dimensional Levi submodule; any nonzero intersection has a nonzero lowest vector, but F₃ sends R into R∩S₃=0, contradicting the injectivity just proved. **This is a whole-submodule intersection, not an all-copy exclusion:** a radical copy can be diagonal between B and equivalent outside copies. In particular the one controlled 27 direction among seven and one adjoint direction among eight at r=3 do not by themselves settle the other directions.

## 4. Actual homogeneous lowest kernel is exactly the radical lowest space

For every homogeneous v∈L_(a,b), the imported entire grade-three result and ideal stability give v∈R ⇒ F₃v=0. Conversely suppose F₁v=F₂v=F₃v=0. Let I₊ be the span of v and all words of positive simple adjoints applied to v. It is stable under all e_i and the whole Cartan. Inducting on word length with
\[
 [f_i,[e_j,w]]=-\delta_{ij}[h_i,w]+[e_j,[f_i,w]]
\]
and the three base annihilations proves stability under **every** f_i. Hence I₊ is an ideal of the full S, not merely a Levi module. Each of its roots is the root of v plus a nonnegative simple-root combination; its α₃ coefficient is at least four. The full realization separates simple-root degrees, so no such root is zero and I₊∩Cartan(S)=0, including extra Cartan directions.

Let π:G→S. The preimage π⁻¹(I₊) is an ideal of G. If h in the original whole Cartan lies in that preimage, π(h) lies in I₊∩Cartan(S), hence π(h)=0; S6's **whole-Cartan injection** then gives h=0. Thus π⁻¹(I₊) is itself Cartan-disjoint; it contains J but J contributes no Cartan element. By the unique maximal Cartan-disjoint ideal property, π⁻¹(I₊)⊆τ, so v∈R. Therefore, at the named actual quotient and imports,
\[
 \boxed{v\in R\quad\Longleftrightarrow\quad F_3v=0\quad(v\in L_{a,b}).}
\]
No assumption J=τ or global Serre conjecture is used. Both Serre signs matter in the named bridge and in the definition of S; the positive-ideal argument is performed in that actual quotient. A nonzero lowest kernel vector would prove a nonzero radical vector. The known ten-dimensional **root-space** F₃ kernel at (2,2,4) is not enough without both F₁,F₂ annihilations.

## 5. Complete grade-four relation cases and new overlap bounds

All statements in this section concern whole Levi modules in the free L₄(V), not individual root-weight rows. Let A be the degree-four part generated by the first seed, B₂ the degree-four part generated by the second; write α_λ,β_λ,γ_λ for the multiplicities of type λ in A,B₂,A∩B₂. Semisimplicity gives the exact all-copy relation
\[
 \operatorname{mult}_\lambda(A+B_2)=\alpha_\lambda+\beta_\lambda-\gamma_\lambda,\qquad
 \max(0,\alpha_\lambda+\beta_\lambda-f_\lambda)\le\gamma_\lambda\le\min(\alpha_\lambda,\beta_\lambda),
\]
where f_λ is the free multiplicity. No pairwise-disjointness assumption is built into this formula.

The cases exhaust every r=1,2,3 and integer s>r:

* **r=3, s≥4:** A is exactly one L(2,5); B₂=0.
* **r=2, s≥3:** the first degree-three seed is W=L(1,4); A is the image of V⊗W with the decomposition displayed in §3. For s=3, B₂ is one L(5,2); for s≥4 it is zero. These two contributions have no common type and thus intersect trivially.
* **r=1, s≥2:** the first degree-two seed is Q, and A is the image of V⊗U, U=[V,Q]. Jacobi expresses brackets of L₂(V) with Q by iterated brackets of letters with Q, so this covers the entire degree-four first ideal. For s=2, B₂ is the image of V⊗L(4,1). For s=3, B₂ is one L(5,2); for s≥4 it is zero. At s=3 the first ideal has no type L(5,2): every first-ideal word has horizontal a≥1 while its lowest position is (0,1). Thus its intersection with B₂ is zero. The s=2 case needs the following simultaneous accounting.

The table lists **all 13** dominant grade-four lowest positions from S4, including the free-absent types. A blank entry is zero. The α columns are for r=1 and r=2 respectively; the β column is the r=1,s=2 second contribution. Entries headed ≤ are proven upper bounds on whole isotypic multiplicity, not evaluated ranks. For r=3 use the first case above. For r=1,s=3 or r=2,s=3 the second column is instead the single L(5,2) just described; otherwise the second contribution is zero.

| (a,b) | λ=(p,q) | f_λ | α, r=1 | α, r=2 | β, r=1,s=2 |
|---|---|---:|---:|---:|---:|
| (0,0) | (4,4) | 0 | 0 | 0 | 0 |
| (0,1) | (5,2) | 1 | 0 | 0 | 1 |
| (0,2) | (6,0) | 0 | 0 | 0 | 0 |
| (1,0) | (2,5) | 1 | 1 | 1 | 0 |
| (1,1) | (3,3) | 3 | 2 | 1 | 1 |
| (1,2) | (4,1) | 4 | ≤1 | 0 | ≤2 |
| (2,0) | (0,6) | 0 | 0 | 0 | 0 |
| (2,1) | (1,4) | 4 | ≤4 | ≤2 | 0 |
| (2,2) | (2,2) | 7 | ≤5 | ≤1 | ≤1 |
| (2,3) | (3,0) | 6 | ≤2 | 0 | ≤1 |
| (3,2) | (0,3) | 6 | ≤4 | ≤1 | 0 |
| (3,3) | (1,1) | 8 | ≤4 | 0 | 0 |
| (4,4) | (0,0) | 1 | 1 | 0 | 0 |

For the bounds, decompose V⊗U using the four summands in §2 and the standard adjoint tensor rule. At s=2 the second source decomposes as
\[
 V\otimes L(4,1)=L(5,2)\oplus L(3,3)\oplus L(6,0)
 \oplus2L(4,1)\oplus L(2,2)\oplus L(3,0).
\]
L(6,0) and L(0,6) cannot survive in the free target because f=0. The α_(2,5)=1 statements follow from the nonzero free tensor word (ad x)³a; α_(0,0)=1 at r=1 follows from the β singlet in §3. The β_(5,2)=1 statement follows analogously from (ad x)³b. For the exact (3,3) entries, S5 explicitly gives a three-dimensional first-relation root space at (1,1) for r=1 and a two-dimensional one for r=2. Each contains the one weight contributed there by L(2,5), leaving respectively two and one L(3,3) lowest copies. At (r,s)=(1,2), S5 also states the two second-seed consequences complete the five-dimensional free (1,1) root space. The second contribution has at most one L(5,2) weight and one L(3,3) lowest weight there, so it has both and its intersection with the first contribution at that weight is zero.

It follows that even in the only potentially overlapping case r=1,s=2, **all** common types except possibly L(4,1), L(2,2), L(3,0) are excluded, and the intersection has at most one copy of each. In particular
\[
 \gamma_{3,3}=0,\quad \gamma_{4,1},\gamma_{2,2},\gamma_{3,0}\le1,\quad
 \dim(A\cap B_2)\le35+27+10=72.
\]
This is a rigorous upper bound, not an assertion that any of the three overlaps actually occurs. Their exact values, and the upper-bound entries of the table, remain unevaluated. The case coverage neither asserts that every free type survives nor subtracts the two ideals separately without overlap.

## 6. Reproducible whole-copy rank formula and remaining radical bounds

For n≤4 and a horizontal degree (a,b), let B_(n,a,b) have as columns all right-nested n-letter Lie brackets of the indicated degree in the ordinary associative tensor basis. Let I_(n,a,b) have all columns obtained from each seed q_r=(ad x)^r a or q_s=(ad x)^s b of degree ≤n by: apply any E₁,E₂ word of length at most 4n to the seed, then apply n−deg(seed) ordered outer adjoints of letters in V, and retain the requested horizontal degree. A longer raising word cannot contribute because it strictly increases total horizontal degree, bounded by 4n; Jacobi and Levi stability account for arbitrary outer brackets and translates. Put both seed families in the **same** matrix. The S6 whole-ideal bridge identifies its span with the actual relation, including both-sign consequences; no overlap needs to be chosen or assumed.

For a fixed (a,b), write
\[
 B=B_{(4,a,b)},\quad I_0=I_{(4,a,b)},\quad I_1=I_{(4,a-1,b)},\quad I_2=I_{(4,a,b-1)},\quad I_3=I_{(3,a,b)},
\]
with empty matrices for negative indices, and let
\[
 M=\begin{bmatrix}F_1B\\F_2B\\F_3B\end{bmatrix},\qquad
 T=\operatorname{diag}(I_1,I_2,I_3).
\]
The F₃ block is computed by the **actual** derivation table, not a Levi-equivariant map: for a letter of horizontal degree (i,j), D_x=ri+sj−2, D_a=−rE₁, D_b=−sE₂, D_c=−s[E₁,E₂], D_d=r[E₁,E₂], D_e=D_f=D_g=0, extended as derivations on words; F₃[u,v]=D_uv−D_vu and F₃[u,w]=D_uw+[u,F₃w] for a longer word w. Then the entire lowest/radical multiplicity is
\[
 \boxed{k_{a,b}=\operatorname{rank}B-\operatorname{rank}I_0
 -\operatorname{rank}[M\ T]+\operatorname{rank}I_1+\operatorname{rank}I_2+\operatorname{rank}I_3.}
\]
The formula is independent of redundant bracket columns: the source is im(B)/im(I₀), while the image rank of the simultaneous maps modulo the whole three target relations is rank[M T]−rank T. Stability of the actual ideal ensures I₀ maps into T. Omitting the third block and I₃ gives the whole lowest multiplicity m_(a,b); the F₃-rank on that whole space is m−k. Section 4 supplies the nontrivial ideal equivalence needed to interpret k as a radical multiplicity. This is an **unevaluated exact criterion** for all r,s and all copies, not a computed uniform rank.

At r=3, S4 gives the seven possible post-adoption multiplicities 4,4,7,6,6,8,1 at positions (1,2),(2,1),(2,2),(2,3),(3,2),(3,3),(4,4). This note gives k_(4,4)=0, k_(2,2)≤6 and k_(3,3)≤7: each of the latter two whole lowest spaces has an embedded one-dimensional direction on which F₃ is injective. Together with the other multiplicity bounds, this yields the conditional coarse bound
\[
 \dim(R\cap S_4)\le4\cdot35+4\cdot35+6\cdot27+6\cdot10+6\cdot10+7\cdot8=618.
\]
At r=2, the relation table proves the total adjoint multiplicity is exactly eight, and the selected adjoint direction gives k_(3,3)≤7; the singlet multiplicity is one and its k is zero. At r=1 the singlet multiplicity is zero. These are **bounds**, not an all-copy vanishing theorem. In all cases the six other lowest-type kernels/ranks require the full formula or another independent argument. There is no nonzero radical witness here.

## 7. Findings, coverage and verification boundary

**Findings.** Within the stated imports, the candidate's U∩U′, β injection, singlet, selected-submodule intersection, homogeneous-lowest ideal equivalence, and simultaneous whole-copy rank formula have been reconstructed in §§2–6; no mathematical defect was found in those reconstructed claims. The sign-separated two-coordinate minor and the complete case/type overlap bounds above are this author's written derivations. S4's broader character, grade-three radical import and actual source bridge remain explicit imports, not newly independently established here. The candidate's three-vector determinant is not needed by this reconstruction; its separate determinant factorization was not rechecked. The individual unknown upper-bound entries, the actual r=1,s=2 overlap, the six remaining lowest kernels, the ten root-kernel vectors' lowest intersections, all higher grades and global J=τ are **NOT DETERMINED**. A separate complete parent read and independent disposition are mandatory before any adoption.

**Actual source coverage.** After reading actual dispatch and the complete manifest, freeze receipt, final binding, prepared metadata and all 23 listed status/permission controls through their endings, I sent Main a direct prebody acknowledgment. Then I read both literal parts serially in order, raw windows of at most 20 LF, through part 1 LF1–765 and part 2 LF1–1027, exactly 1,792 LF, before content comparison or research. No outgoing linked source, unspecified sibling proof, old code, held history or genuinely held episode, nor any proof/method/selection/planning/verification/reporting/confidence/downstream consumer of such an episode, was used. Control documents were permission/status only. No unobservable-cognition certificate is asserted.

The packet contained the following **complete** source bodies; paths are relative to `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`. The whole-source SHA-256s below are frozen parent metadata, not an independent rehash of the original bodies.

| ID | Path | LF | Frozen SHA-256 |
|---|---|---:|---|
| S1 | `review-waves/f756-kac-grade4-character-and-exact-kernel-proof-author/author-independent-grade4-character-and-exact-kernel-v1-erratum-1.md` | 1–14 | `a3f70e77a55faf10ace7f31bf56b984151e64bfbda24f644b2e403d6f96e8c92` |
| S2 | `review-waves/f757-kac-grade4-complete-lowest-map-frontier-author/author-complete-lowest-map-frontier-v1.md` | 1–231 | `490561e0239e568534190175fc2c889887390ded133fe1b9dd6c0804a5a8d8fb` |
| S3 | `review-waves/f757-kac-grade4-complete-lowest-map-frontier-author/author-complete-lowest-map-frontier-v1-addendum-1.md` | 1–15 | `6c8f33ad9fce860868482e06ff821baac8cf1381900941436e795cb487aea5eb` |
| S4 | `dispositions/math-3-actual-grade4-complete-character-and-root-kernel-ten-parent-v1.md` | 1–25 | `f8cf56158c127497bdd75487b9dbc99d26e5e32a8fadcbbd818b663f4049d889` |
| S5 | `dispositions/math-3-actual-grade4-low-components-isotypics-and-kernel-bound-parent-v1.md` | 1–33 | `34f2fd44c33d2c481c8ea112f636e4692812559f393c1ff5ede5ef1b89ab3ce0` |
| S6 | `dispositions/math-3-actual-free-source-and-full-serre-ideal-at-displayed-presentation-parent-v1.md` | 1–27 | `09d94aacd14c652568da68facca73f79121fb8b2f0a7b30a4cdd703204230c0e` |
| S7 | `review-waves/f703-kac-grade3-radical-f3-multiplicity-independent-author/author-independent-reconstruction-v1.md` | 1–314 | `f856b62e2f8261ff0c272ccff33431cdbd014aa4ef7a6f27aca6f445c288ab5e` |
| S8 | `review-waves/f758-kac-grade4-all-multiplicity-exact-finite-author/author-grade4-all-multiplicity-finite-v1.md` | 1–72 | `3491bf3827a20ad6b0d458123a94ca844443dfd6894af21edfc087dba32bce40` |
| S9 | `review-waves/f758-kac-grade4-all-multiplicity-exact-finite-author/parent-all-multiplicity-v1-run-v1-receipt.json` | 1–1021 | `4238fad39894abb8525616c33488f1eefa0f4aba99205f6706c618ae2b732e68` |

S9 reports a parent-run finite check at **only** (r,s)=(3,4),(3,5), not a uniform proof; I did not read its linked executable or full stdout or rerun it. Administrative SHA-256s independently observed after the complete packet read: manifest `3919b30f8a14a27acb90b8d099f7a68bec96e71d04e59cec655721726cc0638b`; freeze `f833c1a27f87b79820f12ece1e8a1983188186c5143019f06a1780f63371c0de`; final binding `c1175d896bcb4f785d8af2bb73a6ef104c3c81fe6681b61ba127e41149a31f71`; prepared metadata `23825069c1df3c41b3abd81d32cc529c3340384abdc784467e31b2a0f1cc5d0b`; actual dispatch `6f25d4f4d1e5e956d357c7821dd5b3600d42b1b6d2fdfbcba393f09216228078`; packet part 1 `ee0465851389947e169b65aec49b31ffb9e1d390a4a5411e46ae2a007216c6e4`; part 2 `04bdf0cc34a25e5833ae9d6569d006bf330bbae91025995291044022d89e1a4d`.

**NOT TESTED / NOT RUN:** no child scientific code, scientific interpreter execution, compile, build, test, formatter, linter, solver, external model CLI, installation, Git, deletion, heavy or paid run. The administrative SHA/date observation and this exclusive final-byte text creation are not scientific execution. This return does not establish a human, independent-model-family or formal/kernel pass, priority/novelty, source identity, or automatic parent acceptance.
