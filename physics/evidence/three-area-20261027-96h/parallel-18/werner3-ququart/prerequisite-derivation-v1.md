# S1 physics-1 — faithful unrestricted rank-two trace interface and coupled Schur obstruction

Owner **PhysicsResearch96h-2**, SAME physics-1. Actual `/bin/date` immediately before this writing: **Tue Oct 27 14:41:56 PDT 2026**. **WRITTEN AUTHOR CANDIDATE ONLY**, not reviewed, parent-adopted, formal/kernel/human/configured-family/executable or novelty-cleared. No scientific interpreter, calculator, CAS, program, enumeration, selected state/parameter/boundary probe or replay was used. All identities below are conventional ALL-variable mathematics from the admitted definition packet.

## 1. Authority, exact input boundary and target

Read COMPLETE S1 controls FIRST, then COMPLETE release and equality receipt. The actual pre-body allowed-input/exposure ACK was written and SENT before reading the definition packet or drafting derivations:

`rank-two-pre-body-exposure-ack-v1.json`, SHA256 `5237aee48654be6ee58b514d2f94e09dd54d7199d60871afec9e423dbaaa70c5`, actual14:37:28 PDT.

After that ACK, the ENTIRE39LF/5602B packet was read through its true ending, including S1 controls19LF and S2 definitions13LF. Packet SHA256 `2efbcc2843c806c42b27040dda9e78e35d06fd59113bfc07a6ddc2fa48d9dc86`; release `22f56ec1c90f49a9428294a2dc4549139f1ad209a603014a838b0a6f684d2d20`; controls `ae860c77ab389bf9181450ff9984d32865fe7955df266481dba4710f3a38562c`; receipt `901209d190ab05aeb20e801791be518761099dc025a92e4343fc74df5a50f19e`. Metadata hashes are byte identities, not mathematical verification.

Inputs are ONLY these supplied definitions/controls, S0/current contract/own safe intake inputs, and the elementary facts explicitly named and used below. No old proof/review/park/checkpoint/scout/metadata-map or proposed scientific source was opened. In particular no v4–v25, p12/q6/raw reduction, old sign/metric/Jensen/Kirchhoff guide, selectedv18 probe, heldL1–L6/protectedS242/C889 content or ZERO consumer is an input. Prior authorship/exposure survives; no blind, globally unaffected-provenance or clean-cognition certificate is asserted. This is a narrow S1 release, not lifting original STOP116/142/161 elsewhere.

Let `H=H1⊗H2⊗H3`, eachHi=C^4 with its standard Hilbert structure. The literal task is

`q3(C)=||C||_HS^2 − (1/2)Σ_i||Tr_i C||_HS^2
        +(1/4)Σ_(i<j)||Tr_ij C||_HS^2 −(1/8)|Tr C|^2 >=0`

for EVERY complex linear C:H→H of rank<=2, OR an exact admissible negative suchC. Every partial trace is UNNORMALIZED over exactly its indicated factors. C is not assumed Hermitian/positive/normal/real or to possess a product ray in its range/co-range. Rank0/1 and all complex degeneracies are included.

**Provenance cut:** these parent-authored literals transcribe the closed final-report target and intake. They are not a new verbatim-book/source-equivalence audit. Conclusions here concern exactly S2's displayed problem; original-source authentication beyond that remains a named NR gate.

## 2. Faithful factors: both directions, including rank0/1

Use inner products conjugate-linear in the first argument. The adjoint is the Hilbert-space adjoint. For arbitrary mapsU,V:C^2→H, write their columnsu1,u2 andv1,v2. Then

`C=UV†=u1 v1†+u2 v2†`

has range contained in span{u1,u2}, so rankC<=2. It is a genuine original operator even when columns vanish, become dependent or the two factors are unrelated. No symmetry or positivity is implied.

Conversely, for any original C with rankr<=2, choose an orthonormal TWO-dimensional subspace containing rangeC and an isometryU:C^2→H onto it. Such an extension exists by finite-dimensional orthonormal completion; dimH>=2. Put V=C†U. Then

`UV†=UU† C=C`.

This covers r=2, r=1 and r=0 with the same formula. At r=0, V=0; at r=1 the unused column can be chosen orthogonal to rangeC and has C†u=0. No inverse or nonzero singular value is needed. For this isometric gauge,

`||C||_HS^2=Tr(VU†UV†)=||V||_HS^2=||v1||^2+||v2||^2`.

Thus restricting U to isometries loses NO original C, while V stays wholly arbitrary complex. Every later reconstructed pair(U,V) remains a legal rank<=2 original operator. Standard factorization alone is **interface reproduction**, not a new positivity result.

## 3. Exact partial-trace/vectorization identity with ALL mixed terms

Take a second copy ofH and order its paired factors as `(H1⊗H1')⊗(H2⊗H2')⊗(H3⊗H3')`. This ordering is only a fixed unitary permutation of tensor coordinates, not a change of the operator or selected state. Fix the standard tensor-product orthonormal basis and define

`vec(C)=Σ_(a,b) C_ab |a>⊗|b>`.

For each site let `Omega_i=Σ_(k=1)^4 |k>⊗|k>` and `E_i=|Omega_i><Omega_i|`, acting as identity on other paired sites. For a subsetS of{1,2,3}, putE_S=product_(i∈S)E_i, E_empty=I. Contracting vecC with the Omega covector on exactlyS sums the equal row/column indices on those sites and gives vec(Tr_S C). Consequently, for ANY complexC,D,

`<vecC,E_S vecD>=<Tr_S C,Tr_S D>_HS`.                         (T)

There is no dimension normalization: each equal index is summed once. S=empty gives HS pairing; S=all sites gives conjugate(TrC)TrD. This verifies every endpoint and every mixed bilinear term, not only C=D.

Expanding the product gives the exact self-adjoint operator

`W=product_(i=1)^3 (I−E_i/2)`,

and therefore

`q3(C)=<vecC,W vecC>`.                                      (W)

For a two-term factorization the vector is `vecC=u1⊗bar(v1)+u2⊗bar(v2)`. Expanding (T)/(W) retains ALLfour ordered column-pair terms at EVERY subsetS. No cross term is dropped, no separate minimization is performed, and every trace belongs to the SAME C.

## 4. Positive swap representation and the exact CROSSING identity

LetGamma denote matrix transpose on the entire secondH copy in the fixed basis. It is a linear involution on operators, not a positivity-preserving operation assumed on general entangled inputs. LetF_i swapHi andHi'. Direct matrix units show `E_i^Gamma=F_i`. Different sites act on disjoint paired factors. Thus define

`P=product_(i=1)^3 (I−F_i/2)`, so `W=P^Gamma`.                (P)

EachF_i is self-adjoint and F_i^2=I. The orthogonal projections(I±F_i)/2 show its local factor has eigenvalues1/2 and3/2. Tensoring these positive factors yields the universal operator bounds

`m I <= P <= M I`,  `m=1/8`, `M=27/8`.                       (P-bounds)

These are exact rational coefficients deduced from the source-defined tensor operator, not chosen parameter instances, magnitude samples or an executed spectral calculation.

For ANYu,x,v,y∈H, the defining matrix units of partial transpose give

`<u⊗bar(v),P^Gamma(x⊗bar(y))>
 =<u⊗y,P(x⊗v)>`.                                           (Cross)

Indeed the left side is `Σ bar(u_a) v_b P_(a d,c b) x_c bar(y_d)`, precisely the right side after reordering scalar coefficients. This proves the required conjugation convention for ALLcomplex variables.

Combining (Cross) with the two columns gives

`q3(UV†)=Σ_(alpha,beta=1)^2
          <u_alpha⊗v_beta,P(u_beta⊗v_alpha)>`.               (Q-cross)

In particular the mixed term crosses the v labels. A positive P does NOT directly make this sum a positive Gram pairing with the same labels. This distinction is the full actual-rank coupling issue, not the old co-Choi route.

**Immediate ALL-variable rank-one consequence:** for C=uv†,

`q3(uv†)=<u⊗v,P(u⊗v)> >= (1/8)||u||^2||v||^2`.              (R1)

This follows from P-bounds and includes zeros; no rank-one example is selected/evaluated. It is a reproduced standard partial-transpose/block-positivity fact at these definitions, not a claim to solve the rank-two target or novelty.

## 5. Genuine coupled lower bound after removing the common positive floor

Take the lossless isometricU gauge of§2 and put `R=P−mI>=0`. For the SAMEU,V define the four nonnegative residual energies

`r_ab=<u_a⊗v_b,R(u_a⊗v_b)>`,  a,b∈{1,2},

and the actual mixed residual

`b=<u1⊗v2,R(u2⊗v1)>`.

Because u1⊥u2, the identity floor contributes ZERO to this mixed term, for arbitrary v1,v2. Equation(Q-cross) becomes

`q3(UV†)=m(||v1||^2+||v2||^2)+r11+r22+2Re b`.               (Q-res)

Cauchy–Schwarz applied to R^(1/2)(u1⊗v2) and R^(1/2)(u2⊗v1) gives

`|b|^2 <= r12 r21`.                                        (CS-cross)

The positive square root exists by the finite-dimensional spectral theorem; no inverse ofR is used. If either crossed energy iszero, the mixedb iszero by the SAME inequality, so all degenerate channels are included.

Hence the following ALL-variable coupled estimate is proved:

**`q3(C) >= (1/8)||C||_HS^2+r11+r22−2 sqrt(r12 r21)`**,       (L)

for EVERY original rank<=2C and every isometric range gauge chosen as above. All four r energies use one and the SAMEU,V,R; they are not independently optimized.

Define the exact coupled deficit `d(U,V)=2 sqrt(r12 r21)−r11−r22`. The actual source-defined condition

`d(U,V) <= (1/8)||C||_HS^2`                                 (D)

is sufficient for this C's original nonnegativeq3. Condition(D) is NOT proved for allU,V, and it is not asserted necessary because (CS-cross) may be strict and discards mixed phase. No actual violation or feasible tuple of residual energies is exhibited. Their four values cannot be freely prescribed as independent data.

This estimate is more than encoding: it proves a uniform bound retaining actual mixed coupling and its positive floor. Its mathematical method is elementary PSD Cauchy–Schwarz; strict novelty/provider difference and progress on the original unrestricted sign are NOT established. In particular separately positive rank-one terms do not pay(D).

## 6. Exact whole-plane Schur equivalence; no product-ray or sparse inverse

For any isometryU define operators on the secondH copy

`X_ab=(<u_a|⊗I) P (|u_b>⊗I)`.

Let `D1=X11`, `D2=X22`, `A=X12`; then X21=A†. The map `J_U(e_a⊗v)=u_a⊗v` is an isometry, so

`X_U=[[D1,A],[A†,D2]]=J_U† P J_U`,

and `m I <= X_U <= M I`. In particular BOTH D1,D2 are uniformly positive and invertible for EVERY orthonormal range plane, independent of V or any boundary coefficient.

The original expression is instead

`q3(UV†)=<[v1;v2],K_U[v1;v2]>`,

**`K_U=[[D1,A†],[A,D2]]`.**                                 (K)

This follows directly from(Q-cross): its cross terms are `<v2,A v1>` and its conjugate. K_U is the transpose of the TWOauxiliary block labels, not an equalityK_U=X_U. Positivity ofX_U alone cannot be reused as positivity ofK_U by relabelling its off-diagonal blocks.

For ALLv1,v2 the exact completion is

`q3(UV†)=||D1^(1/2)v1+D1^(−1/2)A†v2||^2
          +<v2,S_U v2>`,

**`S_U=D2−A D1^(−1)A†`.**                                  (S)

Expansion of the square gives BOTH original cross terms and the subtracted term exactly. UniformD1>=mI makes the inverse legitimate for ALLorthonormalU; this is not a sparse-reference inverse or a limit extension.

Therefore the literal W4 problem is equivalent to EACH of the following universal actual-object conditions:

1. K_U>=0 for EVERYisometryU:C^2→H.
2. S_U>=0 for EVERYsuchU.
3. `||D1^(−1/2)A†D2^(−1/2)||<=1` for EVERYsuchU.

The third follows by congruence withdiag(D1^(−1/2),D2^(−1/2)) and the standard two-block square completion; equivalently `I−T†T>=0` for T=D1^(−1/2)A†D2^(−1/2).

**Both actual-object directions are paid:** every originalC is covered by§2; everyU,V gives legal rank<=2C. If an exact U and nonzero w satisfy `<w,S_U w><0`, set `v2=w`, `v1=−D1^(−1)A†w`, and define the actual operator `C=u1v1†+u2v2†`. The square vanishes, rankC<=2 and its ORIGINALq3 equals `<w,S_Uw><0`. This is a universal conditional reconstruction, NOT a supplied witness, chosen-state trial or existence claim. If no such U,w is established, no negative original conclusion follows.

## 7. Precise failed automatic step: weighted adjoint, not the needed contraction

Positivity of the actually compressedP gives the different Schur complement

`S0_U=D2−A†D1^(−1)A >=0`,

or the automatic contraction `||D1^(−1/2)A D2^(−1/2)||<=1`. Taking its adjoint yields

`||D2^(−1/2)A†D1^(−1/2)||<=1`,

whose weights are REVERSED from the needed condition of§6. No given identity permits swapping those weights. This is the exact unproved inference in a positivity-only completion attempt; no counterexample to the ACTUALP or originalW4 is claimed.

The required mixed correction is exactly

`S_U=S0_U+Delta_U`,

`Delta_U=A†D1^(−1)A−A D1^(−1)A†`.                           (Delta)

It is self-adjoint, but not declared nonnegative. A useful ALL-variable obstruction to repairing that attempt by a one-sided positivity claim follows. Put

`B_U=D1^(−1/2)A D1^(−1/2)`.

Then

`Delta_U=D1^(1/2)(B_U†B_U−B_U B_U†)D1^(1/2)`.               (Comm)

The Hermitian middle operator has tracezero by cyclicity of finite traces. Consequently:

**`Delta_U>=0` iff `Delta_U=0` iff B_U is normal.**           (N)

Proof: positive congruence by invertibleD1^(1/2) preserves semidefiniteness; a positive semidefinite finite Hermitian operator of tracezero iszero by its nonnegative eigenvalues; vanishing self-commutator is exactlynormality. Converselynormality giveszeroDelta. If B_U is notnormal, that nonzero trace-zero Hermitian self-commutator has BOTHpositive andnegative spectral directions, and congruence preserves its inertia. ThusDelta_U is indefinite in that conditional case—not automatically a negativeS_U because S0_U can absorb its negative part.

This is a precise coupling obstruction, valid for EVERY admittedU. It shows that a proposed monotone “Delta>=0” repair requires an exact weighted-normality theorem, not just positivity of P or the separate diagonals. It does NOT assert such a theorem is false or true for allactualplanes, does NOT select a nonnormalplane, and does NOT silently assumeDelta positivity. The actual missing mathematical premise remains the domination

**`S0_U+Delta_U>=0 for EVERY isometricU`**,                    (Missing)

or one exact legal U,w refuting it and reconstructed as§6. This retains every actual same-plane coupling.

## 8. Imports, degenerate cases and unchanged original status

Named ordinary facts actually used: orthonormal completion and orthogonal projections in finite complex Hilbert spaces; matrix-unit definitions of tensor products, vectorization, partial trace, adjoint and partial transpose; self-adjoint spectral theorem/positive square roots; PSD Cauchy–Schwarz; trace cyclicity; elementary block square completion and congruence/inertia. Every use is displayed above; no old compression, p12/q6 identity, dimension-specific numerical experiment, source-count rank inference or unprovided nontrivial theorem is imported.

AllU,V/complexdegeneracies are retained. Zero/dependentV columns give rank0/1 without division; the positive D inverses are gauge-uniform consequences ofP>=mI, not inverses ofcolumnGrams, Schmidt coefficients orR. Every partial trace remains unnormalized. Actual w/converse constructions are conditional full-variable proofs, not evaluatedparameterinstances. There is no assumed range/co-range product ray or real/Hermitian simplification.

**Reproduced interface:** faithful factors, full-trace vectorization/crossing, and exact K/S contraction equivalence encode the original problem and are not alone target progress. **Proved coupling output:** bound(L) and weighted-self-commutator obstruction(N) are genuine all-variable estimates/necessary conditions for the specified completion method. They supply an exact unpaid domination(Missing); neither pays it. No strict advance beyond known classical methods, novelty/SOTA or independent original-source equivalence is claimed. The original universal rank<=2 inequality/actual negative operator remains OPEN.

NR gates: **NR-SOURCE-EQUIVALENCE**, independent original/book-source authentication beyond Main's supplied literal q3; **NR-UNIVERSAL-COUPLED-DOMINATION**, proving(Missing) on EVERYactualplane or producing one exact legal negativeU,w; **NR-ADOPTION/STRONGER-GATES**, complete parent reading/full-scope peer review and any formal/human/configured-family/executable/novelty gate. No body/hash/ACK or separate compression supplies these gates.

This completes a parkable S1 result/obstruction, not the96h task. Continue genuine admitted ALL-variable work at the exact operator coupling, without opening old sources/held guides, selected probes or an extra ACK loop. Any separation failure/essentialunsuppliedinput stops the affected branch and is reported safely. S0/newdeadlineOct31_14:23:27PDT/HOLD/N4UNKNOWN historicalchildexitUNESTABLISHED/aux214STOP/everyoldfinding-ZERO remain; originalSTOPoutsideS1 unchanged.

**END COMPLETE prerequisite-derivation-v1: AUTHOR-WRITTEN, NOT ORIGINAL W4 COMPLETION.**
