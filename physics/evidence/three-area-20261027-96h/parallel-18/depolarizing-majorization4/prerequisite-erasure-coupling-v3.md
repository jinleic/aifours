# physics-2 — exact SAME-state two-erasure coupling and three-erasure Ky-Fan formula

Actual native prewrite clock: **Tue Oct 27 15:14:46 PDT 2026**. Owner PhysicsDepol4-2. NEW additive **WRITTEN candidate under the same frozen S1**, not an adopted result, original majorization closure, formal/kernel/executable check or novelty claim. v1 and v2 remain unchanged. Main's standing15:08:03 direction keeps autonomous written continuation INSIDE S1, not a release of any excluded old source or guide.

This cycle moves beyond the trace-only barrier proved in v2: it gives an OPERATOR bound and an EXACT positive SAME-rho/P remainder, plus a sharp state-dependent Ky-Fan formula for another term in the original channel. Both are universal, not a selected noise/state calculation or a new proper-family original-channel result. One further sufficient one-erasure inequality remains unpaid; it is explicitly not assumed.

## 1. Allowed definitions and all quantifiers

Only the confirmed original channel, current controls/definition packet, safe intake and ordinary elementary operator/permutation facts are inputs. No primary-paper proof or new external source was read. No legacy proof, scout, park, checkpoint, candidate, old common-projector line or method/selection/confidence guide is cited or reconstructed as an input. Prior exposure is not denied; no clean-private-cognition/noninfluence assertion is made.

PRIMARY [Song–Wang–Tomamichel–Fang, arXiv:2609.37240v1, Introduction Eqs.(1)–(2)](https://arxiv.org/html/2609.37240v1) was read ONLY for conventions. It defines `D_(p,d)(X)=(1-p)X+(p/d)Tr(X)I`, physical `0<=p<=d²/(d²-1)`, and conjectures that arbitrary output is majorized BY the product-reference output. Thus here `D_p(X)=(1-p)X+(p/2)Tr(X)I`, physical0<=p<=4/3, with the same majorization direction. No transcription mismatch was found before derivation.

Let rho be ANY four-qubit density (mixed or pure), P ANY complex rank3 orthogonal projector, p ANY physical parameter. Define normalized conditional expectations

`E_S(A)=I_S/2^|S| tensor Tr_S(A)`,
`F_j(A)=sum_(|S|=j) E_S(A)`,
`r=Tr(P rho)`, `f_j=Tr(P F_j(rho))`.

Indices S are subsets of the four labelled physical sites, not independently chosen copies or manufactured scalar data. E_S are the commuting compositions of the single-site E_i. Ordinary facts used: finite swap trace identities, commuting Hermitian involutions and their orthogonal spectral projections, positivity/trace of products, Hilbert–Schmidt squared norm, Pauli/qubit spectral decomposition and elementary Ky-Fan variational principle. No scientific enumeration, arithmetic interpreter or selected instance is used.

## 2. A full two-copy positive identity, proved in every sector

On TWO copies of the four-qubit space let S_i swap the two copies of site i. These are commuting Hermitian involutions. Put S_all=product_i S_i, the global copy swap. Let Q_2 be the orthogonal projection onto the joint sector with EXACTLY TWO local swaps having eigenvalue-1; it is the sum of the corresponding joint spectral projectors. This is a definition of a full operator, not a hypothesis that a relaxed sector is physical.

**Lemma5.** The exact full-space identity is

`3(I+S_all)-sum_(i<j) S_i S_j =8 Q_2 >=0`.          (E1)

**Every sector.** If m of the four swap signs are negative, their sum is4-2m and

`sum_(i<j) s_i s_j=((4-2m)^2-4)/2`.

For m0 and4 this pair-sum is6 and the global sign is+1, so the difference is0. For m1 and3 the pair-sum is0 and global sign-1, again difference0. For m2 the pair-sum is-2 and global sign+1, giving8. These exhaust the joint spectrum and prove(E1), including all multiplicities and all complex vectors. No unprovided sector list or machine check is invoked.

For ANY two densities rho,sigma, the swap trace identity gives

`Tr[(rho tensor sigma) S_i S_j]=Tr(rho_(ij) sigma_(ij))`,
`Tr[(rho tensor sigma) S_all]=Tr(rho sigma)`.

The identities follow by writing matrix entries on the swapped and untouched tensor factors; no purity or shared eigenbasis is needed. Taking(E1)'s expectation yields the exact nonnegative relation

`3(1+Tr(rho sigma))-sum_(i<j)Tr(rho_(ij)sigma_(ij))`
` =8 Tr[(rho tensor sigma) Q_2]>=0`.                 (E2)

## 3. Universal two-erasure OPERATOR bound with exact actual-projector slack

Each two-site erasure leaves the complementary two-site marginal with identity factor1/4. The pair-complement operation permutes all six pairs, so(E2) implies, for EVERY rho,

`F_2(rho) <= (3/4)(I+rho)`.                         (E3)

This is an OPERATOR inequality, not a total-trace surrogate: test it against every unit-vector density sigma in(E2), noting `Tr[sigma F_2(rho)]=(1/4)sum_(i<j)Tr(rho_(ij)sigma_(ij))`. The resulting nonnegative quadratic forms prove the operator difference positive.

For the ACTUAL original rank3 P, substitute sigma=P/3. Multiplying(E2) by the normalization factors gives the precise SAME-object identity

`9/4+(3/4)r-f_2`
` =2 Tr[(rho tensor P) Q_2]`
` =2 || Q_2 (rho^(1/2) tensor P) ||_HS^2 >=0`.       (E4)

The square root is the ordinary positive matrix square root, not a computational operation. Thus `f_2<=9/4+3r/4<=3`. No r=1 containment is assumed to obtain the stronger r-dependent bound. It holds for EVERY mixed rho and complex P, with zero or repeated eigenvalues and arbitrary off-containment.

**Complete equality caller.** Equality in the FIRST bound of(E4) is equivalent to `Q_2(rho^(1/2) tensor P)=0`, by the exact squared norm. For pure rho=|psi><psi| this is equivalent to `Q_2(psi tensor v)=0` for EVERY v in Range(P). This is an actual common-code/reference annihilation condition, not a free choice of marginal overlaps or an assertion that all scalar feasible points are physical. Equality f2=3 additionally requires r1, equivalently support(rho) contained in Range(P). No classification of all these annihilating codes is assumed or claimed here.

The finite two-copy operator is POSITIVE on its whole space by(E1); no nonphysical negative block is produced, counted as progress or treated as a channel counterexample. The actual pair is only tested through the proven trace identity. This completely reconstructs(E3)–(E4) from ordinary swap algebra without an inherited old theorem or reviewed label.

## 4. Exact three-erasure Ky-Fan3 formula for EVERY actual density

Write each actual single-qubit marginal as `rho_i=(I+b_i dot sigma)/2`, and set s_i=||b_i|| in[0,1]. Sort the FOUR lengths as s1>=s2>=s3>=s4; this is only a labelling in the proof, not a chosen test input. Erasing the other three qubits gives

`F_3(rho)=[4I+sum_i b_i dot sigma^(i)]/16`.           (E5)

The four local Hermitian terms commute; their eigenvalues are the signed sums of the lengths. As in v2's ordinary variational argument, the top three COUNTING multiplicity have sum3s1+3s2+s3+s4. Therefore the exact formula is

`K_3(F_3(rho))=[12+3s1+3s2+s3+s4]/16<=5/4`.         (E6)

Consequently EVERY original common P obeys

`f_3<= [12+3s1+3s2+s3+s4]/16<=5/4`.                 (E7)

This is state-conditioned on the SAME rho, not just a projector-purity estimate. It covers arbitrary GME and mixed inputs; no proper physical family is substituted for the original rho domain.

**All zero/tied cases and exact actual-object converse.** For nonnegative sorted lengths the largest signed sum uses no flip, the second and third use the two smallest flip costs. If a cost is zero, the signs give distinct eigenvectors with repeated eigenvalues; the same formula still counts the correct three eigenvalues. If further lengths tie, the threshold eigenspace expands. In ALL cases equality in the first inequality(E7) holds exactly when P contains the eigenspaces STRICTLY above the third-largest eigenvalue, annihilates those below it, and takes the remaining required dimension inside its threshold eigenspace. Such projections exist, are actual complex rank3 orthogonal projectors, and give equality. This spectral statement includes the all-zero case, where EVERY rank3 P attains the same value. No fictitious unique projector at a degenerate threshold is asserted.

**Complete equality for the global cap.** Since every coefficient in3s1+3s2+s3+s4 is positive and each s_i<=1, the cap5/4 is attained IFF all FOUR marginals are pure. A density with a pure marginal is supported on that one-dimensional local factor tensor the rest: positivity and vanishing trace on its orthogonal complement prove this directly. Iterating over all four sites makes rho a pure PRODUCT density. Conversely any pure product density has all s_i1.

For such an arbitrary product input define Omega as its product vector, and V_1 as the four-dimensional span of its one-site-orthogonal excitations, with no particular local vector chosen. The top eigenspace in(E5) is the Omega line, followed by the entire four-dimensional V1. Thus ALL global-cap maximizing P have

`Range(P)=span{Omega} direct-sum W`,

where W is ANY complex two-dimensional subspace of V1. Conversely every such P is a genuine rank3 maximizer. This is the entire equality family forced by a UNIVERSAL theorem, not a chosen product-state viability check or a new restricted-family original-channel result.

## 5. Complete simultaneous maximizer of r, f2 and f3

The three independent caps are r<=1, f2<=3 and f3<=5/4. Their simultaneous equality set is EXACTLY the product-input/P family just described. Necessity follows from equality f3=5/4 and its complete spectral characterization, which already gives r1.

For sufficiency, retain ARBITRARY four local product factors and ARBITRARY W<=V1 of dimension2. Every two-site-erasure operator is diagonal in the corresponding local product/orthogonal basis. F2(rho) acts by6/4 on Omega, because all six erasures contain its component. On each one-site-orthogonal excitation it acts by3/4: exactly the three erased pairs containing that site contribute. Hence on ALL of V1 it is the scalar3/4, so any W contributes the same trace. Thus f2=6/4+2*(3/4)=3 for the ENTIRE class, not one selected vector or phase choice. Together with r1 and f3=5/4 this proves the full actual-object converse.

This does NOT say an arbitrary nonproduct pair nearly saturating one cap can be replaced by one of these maximizers. No quantitative neighbourhood, numerical margin or source-guided product-tube claim is made. It supplies an exact compatibility/equality boundary, not the missing original GME inequality.

## 6. Direct original-channel application and the exact unpaid sufficient edge

Put t=1-p. From the confirmed local definition and commuting E_i, the exact channel identity for EVERY physical p is

`Lambda_p(rho)=t^4 rho+p t^3 F1(rho)+p²t² F2(rho)`
`                +p³t F3(rho)+p^4 I/16`.             (E8)

All scalar coefficients and matrices belong to the SAME actual rho and parameter. Testing against the SAME original P gives

`Tr[P Lambda_p(rho)]=t^4 r+p t^3 f1+p²t² f2`
`                         +p³t f3+(3/16)p^4`.        (E9)

(E4) and(E7) are genuine proved state/projector couplings for two of those terms, not independent coefficient assignments. They include the actual original-rank3 caller and every mixed/complex input.

For0<=p<=1, all coefficients in(E9) are nonnegative. If one could additionally prove the STILL UNPAID universal actual-pair inequality

`Tr[P F1(rho)]<=3 for EVERY rho and complex rank3 P`, (E10)

then r<=1,(E4),(E7) would give

`Tr[P Lambda_p(rho)]<=t^4+3p t^3+3p²t²+(5/4)p³t+(3/16)p^4`
` =(t+p/2)^3(t+3p/2)`.

The last expression is exactly the original product TOP THREE reference sum when p<=1: its local eigenvalues are a=t+p/2 and b=p/2, and the top3 sum is a^4+2a³b. This is a conditional theorem with an EXPLICIT unproved sufficient premise, not original closure. It never takes a free tuple (r,f1,f2,f3) as an actual pair. The exact Ky-Fan variational forward/converse from v1 applies to every actual trace comparison, including degenerate eigenvalues.

For p>1, t is negative and the odd-t coefficient signs in(E8) must be respected. Multiplying an upper bound by a negative coefficient reverses it; the preceding coefficientwise sufficient argument is NOT claimed there. No old unreplayed high-noise interface is silently invoked to promote this partial implication to the full physical target. All identities(E1)–(E9), the actual-pair bounds and the equality classifications themselves retain their full parameter-independent/physical scopes.

**Unpaid edge:** (E10) is NOT proved by the new two-copy pair-sector identity, the exact three-erasure formula, the total-purity budgets or the common maximizer classification. Even a physical failure of that stronger sufficient premise would not automatically violate original majorization because the original channel combines all four terms on the same pair. No original rho/p/P violating (E10) or majorization is selected, evaluated or supplied. The next valuable admitted step is a genuinely universal SAME-pair bound at the one-erasure interface, or an exact failure of an attempted implication on the actual carrier; do not infer it from different-sector positivity or recycle a nonphysical block.

## 7. Result scope and continuing controls

This packet supplies two fully reconstructed nontrivial state-conditioned inputs: an exact positive common-pair two-erasure remainder and an exact three-erasure top3 formula, with complete actual-projector and equality converses. It advances from v2's TOTAL-trace route to operator/actual-state control. Whether these elementary lemmas are known or already implicit in historical constraints is NOT a novelty/SOTA claim or an old-source audit; no old body or guide was opened to compare them. No parent adoption or original scientific-success count follows from this write.

Original all-density/all-physical-noise/all-index majorization, genuinely-entangled global k3 and an actual physical witness remain OPEN. This is not a new proper-state/noise-region original result. Every outside-S1 STOP, HOLDv2, N4UNKNOWN/historical exit unestablished, aux214STOP, old author/reviewer/parent finding and ENTIREZERO consumer remains. Prior exposure/nonblindness is retained; no source-method-independent cognition census. The correctness inputs above are admitted definitions and explicit elementary derivations only, not the excluded old common-projector line. Any material input-separation concern requires branch STOP/report; otherwise Main's standing direction permits the next genuine S1 step without a generic per-step ACK.

NEWOWN append-only files; v1/v2 unchanged; old roots read-only. No scientific interpreter/calculator/CAS/program/enumeration/solver/replay/build/test/typechecker, selected numeric/control/state/noise/boundary/decimal probe, nested agent/modelCLI/paidAPI/newGO, Git/delete/contact/publication/infrastructure action or stronger human/formal/kernel/family/executable/novelty acceptance. Full-source/full-scope review and Main complete reads remain prerequisites to adoption. Science ends2026-10-31T21:23:27.000Z; continue substantive cycles, not heartbeat/timer/fake-progress loops.
