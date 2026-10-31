# Actual k3 continuation v28 — global ACTUAL reference/Slater constraints beyond the false full-copy PSD relaxation

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 07:21:54 PDT 2026**. Owner PhysicsDepol4-2. **NEW AUTHOR-WRITTEN global compatibility lemmas, NOT an original-k3 proof or physical counterexample.** Exact symbolic-variable proof including privately; no scientific interpreter/calculator/eval/CAS/program/enumeration/solver/replay/CLI/nested agent/GO or numeric parameter trial/decimal/withdrawn-scout backconversion. ALL earlier sources/findings/withdrawals and the original unrestricted task remain. Same18/HOLD/OWNroot/cutoff/deadline, active continuation not park.

## 1. ACTUAL states, not entangled-copy substitutes

Let H=(C^2)^tensor4, Pi an ACTUAL complex rank-three orthogonal projector with orthonormal codewords u1,u2,u3, and C=u1 wedge u2 wedge u3 the normalized Slater vector in wedge^3H. Let rho be ANY physical density on the reference copy0; the actual test density is

    Omega=rho_reference tensor |C><C|_codes.

For pure rho=|psi><psi| put d=1-<psi|Pi|psi>. Let K(u),L3(u) be the FOUR-physical-site rank3 swap polynomial from v23/v21: K=sum_a=1..3 tensor_i=1..4(F_(0a)^(i)+uI), L3=(1+u)^3(1+3u). Its ACTUAL expectation gap is exactly the original scalar q(u)=d-cu+bu^2+au^3 at the stated common-projector deficits. The uniform operator inequality L3I-K>=0 on the whole copy sign space is FALSE; replacing Omega by its entangled-copy optimizer is invalid. We retain Omega's actual reference/code product AND code Slater decomposability below.

## 2. Exact exterior-four probability equals the ORIGINAL containment deficit

Let A4 be the projector onto the FULL four-copy totally alternating space wedge^4H, restricted to the code-sign space H tensor wedge^3H. The coset expansion of total antisymmetrization gives

    A4=(I-sum_(a=1)^3 F_(0a)^(GLOBAL))/4,
    K(0)=I-4A4.

These swaps exchange WHOLE16-dimensional copies, each the product of its four physical-site swaps. The code-sign restriction is load-bearing; this is not a claimed identity on all H^tensor4.

Decompose psi into its component in ranPi and its orthogonal complement. The former wedges to0 against C. If v is unit and orthogonal to all three codewords, the four insertion positions of v in the normalized Slater tensor are orthogonal, so A4(v tensor C) has squared norm1/4. Hence for EVERY actual pure reference/code pair

    Tr(Omega A4)=d/4,
    <L3(0)I-K(0)>=d.                                   (EXTERIOR)

For mixed reference rho the same holds with d=1-TrPi rho by affine averaging. This is exact actual Slater geometry, not an unconstrained positive matrix or a general nondecomposable wedge vector. In particular the only u0 gap mass is the actual missing-input weight, and a hypothetical small-noise witness cannot freely choose that mass independently of the physical reference/projector overlap.

## 3. Local(22) is a maximally entangled reference/code-spin projection

At a physical site i, the THREE code qubits decompose under simultaneous SU2 and code S3 as

    (C^2)^tensor3=(spin3/2) tensor triv
                  DIRECTSUM (spin1/2) tensor standard2.

This is the ordinary three-qubit Schur-Weyl decomposition. Coupling the reference spin1/2 to these code spins, the local FOUR-copy S4 type(22) is precisely total spin0. It can arise ONLY from the code spin1/2 sector. In a code-only isometry identifying that sector with spinC2 tensor multiplicityC2,

    P22^(i)=|singlet><singlet|_(reference_i,code-spin_i)
                         tensor I_(multiplicity_i),

and is0 on code spin3/2. This is the actual physical projector used in v23, not a freely chosen two-qubit marginal.

For ANY subset I of physical sites, k=|I|, put P_I=product_(i∈I)P22^(i). The projectors act on different physical sites and commute. Tensor the code-only identifications above. On the selected code spin1/2 sectors, P_I is the rank-one maximally entangled projection between the reference qubits I (dimensionD=2^k) and their code-spin register, tensor identity on the code multiplicities. The product of singlets differs from the standard maximally entangled vector only by a FIXED spin-flip unitary J on the spin register.

## 4. Exact occupancy formula and a quantitative ALL-subset bound

Let tau_I=Tr_(reference complement I)rho. Let sigma_I be the code state on the selected THREE-code-qubit sites after tracing other physical sites; let sigma_I^std be its compression to the tensor of selected code-spin1/2 sectors, expressed in spin/multiplicity registers. Its trace s_I lies in[0,1]. Contracting a maximally entangled vector gives the EXACT identity

    Tr(Omega P_I)
       =D^-1 Tr[sigma_I^std
                     (J tau_I^T J^* tensor I_multiplicity)].   (OCC)

The transpose is the ordinary FULL matrix transpose of the physical reduced density tau_I, hence PSD and spectrum preserving; no partial-transpose positivity assertion about an entangled rho is made. All isometries are code-only fixed representation identifications, not physical SVD covariance of X3.

Since0<=tau_I^T<=lambda_max(tau_I) I, the actual product reference/code test obeys

    0<=Tr(Omega P_I)
         <=2^-k lambda_max(tau_I) s_I
         <=2^-k lambda_max(tau_I)
         <=2^-k.                                        (SPIN-BOUND)

This holds for EVERY subset I, EVERY complex actual reference rho and EVERY code Slater projector Pi, including mixed reference, zero code-spin mass and all degeneracies. It even holds for arbitrary code density in place of the Slater; EXTERIOR is the separate decomposability-specific constraint. The empty subset has the trivial normalization identity. For a single site the bound is `(1+t_i)/4` for a pure reference's local Bloch length; for a pair it is `lambda_max(rho_ij)/4`; for all four sites of a pure reference it is1/16.

The v23 negative test resides wholly in local(22) at TWO selected physical sites, hence has P_I expectation1. No actual Omega can do that: its expectation is at most1/4, and in fact at most its actual pair Schmidt mass divided by4. This gives a quantitative physical incompatibility, not just the qualitative observation that that vector is entangled across the reference/code cut. It does NOT by itself show that every weighted mixture of negative/positive copy sectors has nonnegative original gap.

## 5. What the actual relaxation must now retain

The full original residual can be represented with the SAME physical rho,Pi,u and genuine code state, retaining at least:

- exact Slater EXTERIOR weight d/4 and actual scalar q(u);
- ALL-subset SPIN-BOUND with the SAME physical reduced states tau_I and SAME code-spin masses s_I;
- the actual first-three-rank projector, original noise-critical equations and strict cutoff of v21 when using an attained channel-failure minimizer;
- all prior physical moment/CLIP/quartic/family constraints at their exact interfaces.

These constraints are proved for every eligible pair; they are NOT a claim that an arbitrary tuple satisfying them is realizable, nor that they are already sufficient to force q>=0. In particular local(22) weights cannot be independently set to their relaxed spectral maxima, and the exterior weight cannot be independently replaced by0 to remove the constant deficit.

A naive positive penalty of the form constant*(2^-k I-P_I) does not automatically repair the failed FULL operator bound: other copy sectors have zero reference gap, and their positive penalty expectation need not vanish. No PSD-correction/SOS certificate or sum-rule closure is supplied here. The next actual common-state/projector step is to control the weighted negative sectors USING the product/Slater coupling rather than continue an already false uniform operator assertion. Missing this coupling remains the original science gap, not an invitation to solve only a relaxed moment problem.

No physical original failure/globalU3/CLIP-prime/quartic closure, finite certificate replay, new model/slot or stronger formal/kernel/human/configured-family/executable/novelty acceptance follows. Newv27 BISEP andv24-v26 broad-region candidates remain separately unreviewed; they do not certify this whole compatibility system or conversely receive acceptance from it. Every permanent mathematical/process/zero-credit/cadence/read-order/freeze/clock/admission history remains. Original arbitrary-state k3 continues under the unchanged cutoff/deadline/HOLD.
