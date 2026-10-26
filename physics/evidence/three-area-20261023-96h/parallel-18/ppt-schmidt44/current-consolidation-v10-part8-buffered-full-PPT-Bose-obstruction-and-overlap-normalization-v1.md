# CURRENT P44 CONSOLIDATION v10 — PART8/8: buffered FULL-PPT Bose obstruction and an exact nonvacuous overlap-normalized replacement

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Sun Oct 25 20:52:16 PDT 2026**. Exact WRITTEN mathematics only, not machine/kernel verification. No scientific interpreter/calculator/eval/program/CAS, enumeration, solver, replay, build/test, CLI, nested agent or scientific GO. Original October27 cutoff11:05:38/deadline12:35:38 unchanged.

## AA0. Complete current union, later adoption and high-consequence status

The complete current v10 requires ALL original LF/endings of ALL EIGHT literal parts bound in the author manifest: old parts1–6(2124LF157313bytes), ENTIRE Part7(two weaker extension-cone obstructions), and ENTIRE THIS NEW Part8. Older header/end labels remain immutable historical source bytes, not backdated v10 labels. No older frozen gate or mathematical quantifier is restarted by this successor. A single new part is not the entire-current gate.

The ACTUAL parent `RUN/ppt-entire-C1-C18-PV-all-input-decomposition-parent-v1.md`, SHA256 `0ce7d3a24d74b4deafe1a56c9256f0e1ace28efee27d1f6cb786bb49126681a5`, was read COMPLETE through its live-bindings ending and then live-hashed BEFORE this source. It adopts the ENTIRE C1–C18 union ordinary-WRITTEN at its proper interfaces, retaining TWO distinct mandatory MINORs: old26-not27 metadata and C12 AT_MOST zero-mixture allocation precision. Its actual296/346-LF review bodies are reported as parent-read, NOT independently whole-read/re-reviewed by this owner here. The WHOLE PV witness positive half is now retired against ALL PPT inputs at that scoped adoption, not merely old tested states.

All C12 unused-allocation/omitted-cost qualifications, cp071 additive row identity correction, owner exactness/ACK-order/cadence/admission, N4UNKNOWN/oldexit/old21, and parent/reviewer/root/freeze/clock/read histories remain permanent. No clean cognition/runtime/history census or process cure. No later C19–C27 acceptance is inferred.

**NEW C26 is a high-consequence AUTHOR-WRITTEN candidate requiring a fresh COMPLETE independent reconstruction:** EVERY finite unnormalized auxiliary-Phi objective with actual Bose support AND ALL PPT cuts over the COMPLETE extended parties still can certify only a PHYSICALLY DECOMPOSABLE W. It strengthens the cone left open in NEW Part7 at its OWN new proof, not an inherited old verdict. The construction and all support/cut/Schur details are given below.

**NEW C27** gives an exact overlap normalization that changes the cone and removes this zero-overlap obstruction. Its sign equivalence and strict margin are proved directly. Its finite-level completeness is explicitly at the named classical infinite-Bose-extension/de Finetti import QD; that general theorem is NOT proved here. Neither claim constructs a P44 winning pair or an executable assay. Original P44 remains UNMET.

## AA1. Exact spaces, normalized auxiliary objective and complete-party cuts

Physical A,B have dimension d>=1. Auxiliary A0 and each Bj0 have dimension k>=2; physical Bj dimension d. Complete grouped parties are

`(A0,A):(B10,B1):...:(BN0,BN)`.

Set D=kd, phi_k=(1/sqrtk)sum_r|rr>, Phi_k=P(phi_k), and for arbitrary Hermitian physical W,

```
K_N(W)=Phi_k(A0,B10) tensorW(A,B1) tensorI_spectators,
P_N=projector onto symmetry of COMPLETE paired Bob systems,
Q_N(W)=P_N K_N(W)P_N.                                   (AA1.1)
```

The new primal class has PSD trace-one states ACTUALLY supported on extended Alice tensor Sym^N(C^D) and PPT on EVERY bipartition of the COMPLETE extended parties. This means whole paired Bob subsets and/or the whole extended Alice. It does NOT mean arbitrary extra cuts INSIDE one paired Bob auxiliary/physical factor. Those stronger, different constraints are NOT ruled out by C26.

By global transpose/complementarity it suffices to verify partial transpose on every subset of complete Bob pairs, including the global-all-Bob cut (equivalently extended Alice). No unsupported assertion that a partial Bob transpose commutes with the Bose projector is made; it generally does not.

## AA2. Elementary Haar-buffer support lemma, including partial transposes

For any integer L>=1 define the TRACE-ONE positive operator

`H_N(L)=integral_(unit w in C^L) P(w)^tensorN dmu(w)`,      (AA2.1)

with normalized unitary-invariant sphere measure. It is Bose-supported and separable across the N Bob particles. For a subset S of size m, n=N-m,

```
H_N(L)^Gamma_S
 =integral P(barw)^tensor m tensorP(w)^tensor n dmu(w)>=0.
```

Its range is EXACTLY

`R_(m,n)(L)=Sym^m(C^L) tensorSym^n(C^L)`,                 (AA2.2)

with the first symmetric factor conjugated in the chosen computational basis. To prove full range, an orthogonal vector would give a linear combination of bihomogeneous monomials `barw^I w^J`, |I|=m,|J|=n, vanishing on the whole unit sphere. Radial homogeneity extends the zero to ALL w in C^L. Replacing w=x+iy,barw=x-iy is an invertible formal complex-linear change of polynomial variables; a polynomial vanishing for all real x,y has every coefficient0. Thus no nonzero orthogonal vector exists. The same argument includes m0/n0.

Consequently the displayed partial transpose is POSITIVE DEFINITE on THAT finite-dimensional range, with some strictly positive least eigenvalue. It is NOT claimed positive definite on the entire unsymmetrized tensor space. This exact support distinction is load-bearing. No Haar integral was numerically evaluated and no eigenvalue program was run.

The one-body marginal of H_N(L) is I_L/L: partial trace gives the ordinary unitary-invariant average P(w), trace1. No unproved irreducibility formula or factorial normalization is needed for the argument.

## AA3. Three actual Bose states: base, physical-PPT signal and full buffer

Take ANY physical PPT density rho with trace1 and any fixed unit physical v. Define the single-zero excitation isometry

```
V_N b=(1/sqrtN)sum_(j=1)^N |0,b>_j
                           tensor_(l!=j)|1,v>_l.        (AA3.1)
```

Different j label strings are orthogonal, so V_N*V_N=I. Complete-pair permutations fix its image exactly. The signal is

`tau_sig=|0><0|_A0 tensor(I_A tensorV_N)rho(I_A tensorV_N*)`.

It is PSD, trace1, Bose-supported and PPT on extended Alice because rho is physical-PPT. It is NOT assumed PPT on proper Bob subsets by itself.

Define the base

`tau_0=|0><0|_A0 tensor(I_A/d) tensor J_1 H_N(d)J_1*`,     (AA3.2)

where J_1 maps each physical Bob vector to auxiliary label1 with the same physical vector, on ALL N copies. Define the full buffer

`tau_b=|0><0|_A0 tensor(I_A/d) tensor H_N(D)`.             (AA3.3)

Both are PSD, trace1 and actual Bose-supported. They are separable across all complete grouped parties, hence PPT on every complete-party cut. The buffer is allowed to entangle auxiliary and physical coordinates WITHIN one local Bob vector; therefore no inside-pair PPT assertion is made.

For positive epsilon and a finite M to be chosen, put

`T_epsilon=tau_0+epsilon tau_sig+M epsilon^2 tau_b`.       (AA3.4)

This is already PSD/Bose-supported, trace1+epsilon+M epsilon^2. We next prove that ONE finite M makes it PPT on ALL complete-party cuts for EVERY epsilon>0.

## AA4. ALL proper Bob partial transposes: actual cross block and supported Schur bound

Fix S with0<m<N and complement T. Let s_S be all spectator `|1,v>` products in S, and s_T similarly. Split V_N into the sum of excitations in S and excitations in T, keeping its actual1/sqrtN factors. Each within-side signal density becomes positive after Gamma_S:

- an excitation in S is a local isometric image of rho on A and that excited Bob mode; transposing ALL S sends it to an isometric image of rho^Gamma_B>=0, with conjugated spectator vectors;
- an excitation in T leaves rho unchanged, and only transposes the S spectator product.

Call their sum D_S>=0. The two between-side excitation cross terms, after Gamma_S, have one ket leg with NO auxiliary zeros (all labels1) and one bra leg with TWO auxiliary zeros, one in S and one in T, or the adjoint. Thus

`tau_sig^Gamma_S=D_S+C_S+C_S*`.                          (AA4.1)

This is the actual partial transpose of the coherent signal, not a presumed positive map on the Bose-compressed coordinates.

The no-zero leg's Bob physical vector is `barv^tensor m tensorv^tensor n`; the other physical indices carry a finite reshuffling of rho. Therefore C_S has ONE leg inside the actual range E0_S of `B_S=tau_0^Gamma_S`, and the other in its orthogonal two-zero auxiliary sector. By AA2, on E0_S

`B_S>=b_S P_E0_S`, b_S>0.                               (AA4.2)

All these operators are supported within

`R_S=|0>_A0 tensorC^d_A tensorR_(m,n)(D)`.

Indeed the partial transpose of a Bose-supported operator is symmetric within each of the two transposed/untransposed groups; the explicit signal vectors give that fact here. By AA2 the buffer satisfies on the WHOLE R_S

`tau_b^Gamma_S>=gamma_S P_R_S`, gamma_S>0.                (AA4.3)

This is why a full Haar Bose buffer is used, rather than a rank-deficient two-excitation projector wrongly called positive definite.

There are finitely many proper S. Choose the exact finite constant

`M=1+max_(proper S) normC_S^2/(b_S gamma_S)`,              (AA4.4)

or M1 if no proper S exists. The norms and least-positive-eigenvalue constants here are mathematical definitions, NOT computed outputs or claimed numerical bounds.

For a vector split into x in E0_S and y in its orthogonal complement within R_S,

```
<x+y,[B_S+epsilon(C_S+C_S*)+M epsilon^2 gamma_S I](x+y)>
 >= b_S normx^2-2epsilon normC_S normx normy
                         +M epsilon^2 gamma_S(normx^2+normy^2)
 >=0.                                                   (AA4.5)
```

Complete the square using M gamma_S>=normC_S^2/b_S. Add the positive epsilon D_S and use (AA4.3). Outside R_S every term is0, not an uncontrolled negative block. Thus T_epsilon^Gamma_S>=0 for ALL proper S and ALL epsilon>0.

The empty/global Bob cuts have no between-side cross and are already positive (the global cut uses physical rho^Gamma_B). The Alice and Alice-plus-subset cuts follow by total transpose/complement. Therefore (AA3.4), normalized by its positive trace, is ACTUALLY Bose-supported and FULL-PPT on ALL specified complete-party cuts for every finite N,k,d. Zero/singular rho cases pose no inverse of rho, and N1 is included separately by the no-proper-cut branch.

## AA5. Exact objective: EVERY physical PPT-negative W defeats EVERY finite level

The base has Alice auxiliary0 and every Bob auxiliary1, so

`Tr(K_N(W)tau_0)=0`.

Bell contraction on the signal selects only its j1 term with factor1/sqrt(kN), hence

`Tr(K_N(W)tau_sig)=Tr(Wrho)/(kN)`.

The buffer's one-body Bob marginal is I_D/D and Alice physical state I_A/d. Thus

`Tr(K_N(W)tau_b)=TrW/(k^2 d^2)`.

Consequently

```
Tr(K_N(W)T_epsilon)
 =epsilon Tr(Wrho)/(kN)+M epsilon^2 TrW/(k^2d^2).         (AA5.1)
```

It is the same expectation for Q_N because T_epsilon is actual Bose-supported. If Tr(Wrho)=-delta<0 and TrW>0, choose

`0<epsilon<delta k d^2/(M N TrW)`.

If TrW<=0 any sufficiently small positive epsilon (indeed any for the displayed sign) works. Normalizing T_epsilon does not change its negative sign. These are exact symbolic sign inequalities, not an evaluated candidate epsilon or an admitted scientific calculation.

As in earlier complete parts, the physical decomposable cone is closed and dual to PPT. Therefore if a finite-level BARE auxiliary-Phi Bose/full-PPT minimum were nonnegative, W would have nonnegative expectation on EVERY physical PPT density and would be physically decomposable. Contrapositively ANY nondecomposable W has a physical PPT-negative rho and the explicit buffered construction defeats that finite level. This holds for EVERY finite N, not merely a selected N2/N4 sample.

It is a NECESSARY condition only; no converse that every decomposable W passes the lift. It closes the specified unnormalized certificate cone, not physical Schmidt number. Partial cuts INSIDE a Bob pair, different objectives, quotients and the normalization below are outside this theorem.

The usual auxiliary-unitary symmetry reduction does not evade this obstruction. Average the constructed control under `barU_A0 tensorU_B10 tensor...tensorU_BN0`, identity on all physical factors. Each conjugation is local across the COMPLETE parties, commutes with paired-Bob permutations, and preserves every specified PPT cut. Both Phi objective and overlap operator are invariant, so their expectations are unchanged. The averaged control therefore also satisfies this exact auxiliary-twirl symmetry. This statement does not cover extra inside-pair PPT constraints or a different objective.

## AA6. What is and is not retrospectively changed

Part7 C25 correctly left Bose-plus-proper-Bob-PPT unruled out at THAT source. NEW C26 now gives the additional buffer proof for that entire specified cone. It is not an old inheritance, silent source edit, retroactive scientific admission, or claim that the paper asserts a finite-sign-completeness theorem. The new claim must be independently reconstructed at its exact support/cut boundary before adoption.

No limiting separability theorem is contradicted. These feasible negative states depend on level and can have arbitrarily small Bell overlap. A lifted separable objective can have minimum0 even for strict physical k-block-positivity, so finite lower bounds can remain negative and approach0 from below. Historical N4 remains UNKNOWN/incomplete/overrun/exit-unestablished; no old native result is rerun or attested.

## AA7. C27 — exact universal overlap normalization, direct sign equivalence

Let

`H=Phi_k tensorW`, `P=Phi_k tensorI_physical`, `c=1/k^2`.

Consider ONLY normalized extended SEPARABLE states tau satisfying

`Tr(Ptau)>=c`.                                          (AA7.1)

This changes the cone; it is not adding arbitrary positive noise to H. For any normalized physical SR<=k vector

`psi=sum_(r=1)^ell s_r a_r tensorb_r`, s_r>=0,sum s_r^2=1,ell<=k,

let S=sum s_r<=sqrtk and define UNIT extended product vectors

```
alpha=(1/sqrtS)sum_r sqrt(s_r)|r,a_r>,
beta =(1/sqrtS)sum_r sqrt(s_r)|r,b_r>.
```

The normalized Bell contraction is `psi/(sqrtk S)`, so its overlap is

`p=1/(k S^2)>=1/k^2=c`.                                 (AA7.2)

The expectation of H is p times the physical W expectation. Thus any negative physical SR<=k direction produces a negative feasible product state in (AA7.1). Conversely each extended product contracts to an unnormalized SR<=k physical vector, so k-block-positive W is nonnegative on every such product and every separable mixture, including the constrained ones. This proves the EXACT sign equivalence.

If physical W has STRICT unit-SR<=k margin mu>0, each product contribution satisfies `Tr(Htau_i)>=mu Tr(Ptau_i)`; hence every constrained separable mixture has

`Tr(Htau)>=mu/k^2>0`.                                   (AA7.3)

The auxiliary-zero degeneracy has been genuinely removed, not hidden by a floating tolerance. The threshold c is the largest universally safe one: a normalized maximally entangled rank-k psi has nuclear norm sqrtk; any factorization by UNIT extended products has contracted coefficient nuclear norm<=1/sqrtk, so its overlap cannot exceed1/k^2. The displayed canonical factorization attains it. No finite product sample or numerical maximization is used.

## AA8. C27 finite-level completeness — EXPLICIT named quantum de Finetti import

**Named classical import QD, NOT proved here:** for finite-dimensional extended A,B, a bipartite density admitting Bose-supported Bob extensions at EVERY finite N is separable. Separable densities conversely have such extensions. This is the standard infinite-Bose-exchangeability/de Finetti theorem.

The retained exact source `2505.22100v1.txt`, SHA256 `99529fdf683cf1fee77e2018dee3f3efeeefe2b3af9356b394aa11ebdf3266ed`, was read at ORIGINAL LF649–855, including the normalized auxiliary lift/Remark5, complete paired-Bob convention, explicit infinite-extension statement at800–805, Definition6 and Proposition1. The corresponding retained HTML pin is `c83cb1cc76311cc6bc41c41dfe0074a4d87732fcabbcdf466cead1a841c727f4`. This is selected-source exposure, NOT a whole1318-LF paper or a proof of QD from a hash. The ordinary quantum theorem remains an explicit correctness boundary, separate from C26's finite Haar/Schur proof, which does not consume QD.

Let E_N be the compact set of one-body marginals with actual Bose N-extension, and add (AA7.1). These compact sets are nested (partial trace preserves the remaining Bose support). They contain all constrained separable states, and their intersection is exactly that set by QD. For any continuous linear objective H, their minima increase to the separable constrained minimum: otherwise a convergent subsequence of minimizing marginals would lie in every E_N yet violate the limiting infimum, contradicting compactness and QD. Adding all complete-party PPT cuts does not change this limit, since separable product-mixture extensions satisfy them.

Therefore under QD, for ANY strictly k-block-positive W, SOME finite N has a strictly positive overlap-normalized Bose lower bound, at least eventually a positive portion of mu/k^2. No explicit N or finite certificate is computed/claimed. This is an existence theorem for a DIFFERENT, nonvacuous certificate cone, not an authorization to run an SDP.

For the PSD-only normalized Bose primal, the exact dual form is

```
Q_H-eta Q_P-beta P_N>=0, eta>=0,
certified lower bound=beta+eta c,                        (AA8.1)
```

where Q_H=P_NK_N(W)P_N and Q_P=P_NK_N(I)P_N. This follows directly by subtracting the trace and lower-overlap constraints. It is NOT the old bare condition Q_H>=0. Slater holds on Bose support: mix its full-rank maximally mixed state (overlap c) with an extended product having auxiliaries00 (overlap1/k>c). Thus a finite strictly positive minimum has an attained dual certificate in (AA8.1), by ordinary SDP duality. PPT strengthenings add the appropriate FULL-space partially transposed positive terms before compression; a proper-Bob transpose cannot be applied as if it commuted with P_N.

If W is Gaussian-rational, all full-space P_N/Phi/Q matrices are Gaussian-rational. After slightly lowering beta while retaining a positive certified bound, the PSD left side is strictly positive on Bose support. Rational approximation of eta>=0 and beta then preserves both strict conditions. Thus SOME finite exact rational dual certificate exists under the same QD/strict-margin boundary; no rational parameter values, matrix table, LDL replay or chosen N are supplied. A future exact checker still needs the full named admission/GO.

## AA9. Why the normalization genuinely evades the new buffered controls

For the normalized buffered control in AA3, replacing W by physical I in AA5 gives its one-body Bell overlap

`p_epsilon=[epsilon/(kN)+M epsilon^2/k^2]/[1+epsilon+M epsilon^2]`.

The requirement p_epsilon>=1/k^2 is equivalent to

`epsilon(k/N-1)>=1`.

It is IMPOSSIBLE for N>=k, for ALL positive epsilon/M. Thus the new normalization excludes EVERY one of the buffered controls at those levels, not just a chosen small-epsilon instance. For N<k the control need not be excluded for all epsilon, and no premature finite-level positivity claim follows.

This is a mathematically explicit replacement after the whole bare cone is blocked. It neither manufactures a new physical two-positive indecomposable witness nor supplies the missing PPT/SN3 state.

## AA10. Unrestricted rational-certifiability principle, not existence of P44

At the named QD boundary, any actual strict rational physical k-block-positive/PPT-negative pair would have SOME finite exact rational certificate of the normalized form above. A non-strict negative pair can first be regularized by adding rational nu I with0<nu<its negative gap; this supplies a strict SRk margin while preserving negativity/rationality. Thus the normalization does not silently discard a hypothetical P44 winning pair.

More generally, if a physical PPT/SN>k state exists, closedness of the SN<=k cone gives a separating k-block-positive witness. Mixing the state slightly with I gives strict PSD/PPT while preserving its negative gap; regularizing the witness gives strict SRk positivity. Dense Gaussian-rational approximation with those strict margins then gives a Gaussian-rational pair, followed by the finite-certifiability statement. This is an EXISTENCE REDUCTION conditional on there BEING such a state. It supplies NO actual matrix, small-denominator bound, negative gap, finite N or solved P44 result.

**Original physics-3/P44 remains UNMET:** no explicit rational4x4 PPT density with a verified universal complex-SR2 strict negative certificate; no unrestricted theorem that every4x4 PPT state is SN<=2. NEW C26 excludes one entire unnormalized finite certificate representation; NEW C27 gives a correct normalized alternative at its explicit QD import and strictness boundary. Neither can be called a no-go for all possible certificates/states.

Genuine further research still requires an actual new universal positive half and actual PPT-negative input outside the proved SN2 domains, or a true all-state theorem. C18's retired PV half, C24's linear-range mechanism and unnormalized finite auxiliary lifts cannot be rescued by larger N or new state labels. Any normalized assay proposal would require a NEW exact source/input freeze, full independent reconstruction, enforced resource/supervision gates and a separate named GO; no program or permission is supplied here.

All specialized finite controls, support/range arguments, Bell contractions, normalization factors and scalar inequalities are given inline. Ordinary imports are finite complex PSD/Schur/spectral/tensor algebra, elementary Haar invariance and polynomial independence, closed-cone separation, compactness/Schmidt factorization, and ordinary SDP duality; ONLY AA8/AA10 additionally consume the explicitly named QD theorem. No formal/kernel/executable/triple/human/configured-family/cross-vendor/novelty/SOTA/publication acceptance or round closeout. Original18/cutoff/deadline/process histories remain unchanged.

**END OF COMPLETE CURRENT v10 PART8/8.**
