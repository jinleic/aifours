# RQLS10 v53 — BOTH signed and unsigned prime5 Gaussian pairs: one affine physical block already forbids a maximal full resolution

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE writing this NEW manuscript: **Mon Oct 26 12:00:04 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact Gauss-sign/MUB/tight-frame/permutation/completed-square/difference-collision proof only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty/accepted finite-witness claim.

This is a genuinely larger tenth-root family than v49's UNSIGNED nonsquare-ratio phase5 matrices. The signs are retained throughout; deleting them or silently applying a fifth-root theorem would be wrong.

## 1. Complete16-matrix family and exact conditional relative-pairing theorem

Let r0,r1 be ANY nonzero elements ofF5 (equality allowed). Put

    d_r=r1-r0, l_r=d_r/(4r0r1),
    delta_r=-Legendre(r1/r0) in{+1,-1}.

Define the literal unit-entry Hadamard H_r by

    A_i(L_j)=zeta^(i*j),
    A_i(R_j)=zeta^(l_r*i^2+i*j);
    B_k(L_j)=zeta^(r0*j^2-2r0*k*j),
    B_k(R_j)=delta_r*zeta^(r1*j^2-2r1*k*j+d_r*k^2).

The same completion-of-squares proof asv49 works with its ACTUAL sign: the two mixed-row Gauss sums have ratioLegendre(r1/r0), canceled exactly by delta_r. Thus every parameter pair gives a true Hadamard. There are16choices; eight have delta+ and eight delta-. No equivalence or classification between them is presumed.

Choose H_r,H_s INDEPENDENTLY. Let their relative coordinate permutation map the two physical5-blocks SETWISE (preserve or exchange), and suppose AT LEASTONE of its two induced F5 permutations is AFFINE. Form their actual Hadamard-pair QLS.

**Theorem.** No such pair is a MAXIMAL1-RQLS10. If exactlyone block map is affine, fifty same-type cells admit no quantum transversal. If both are affine, a preserving quantum transversal would force a repeated-ray collision or an impossible degenerate case. Every full resolution must cover those same-type cells, so maximality plus resolution is impossible.

No conclusion is claimed here for BOTH block maps nonaffine or relative permutations mixing the physical blocks. For two signed TypeII matrices the mixed-cut case is independently closed byv52, but aligned nonaffine and mixed-type cases remain explicitly separate.

## 2. ANY quantum transversal must preserve or swap A/B types

Use the affine physical block. If its output-block B-row quadratic coefficient is c_out and its input coefficient from H_s is c_in, the four cell types A/A,A/B,B/A,B/B have chirp coefficients

    0, -c_out, c_in*a^2, c_in*a^2-c_out,

with a!=0. Bottom-row SIGNS are constant on a physical block and do not alter these rank-one chirp projectors.

An actual ten-ray basis restricts to a2I5 tight frame. Distinct quadratic chirp bases are mutually unbiased by the exact Gauss norm identity. Their traceless projector spaces are orthogonal, so the integer count of each chirp label must be uniform within its basis; each distinct basis is used a MULTIPLE OF5 times.

A full transversal has cell-type counts(x,5-x,5-x,x). As c_in*a^2/c_out runs overF5^*, the four coefficients have the same three/four-basis patterns spelled out inv48: ratio1 collapses only A/A withB/B; ratio-1 only A/B withB/A; the other two ratios give four distinct bases. In ALLcases divisibility by5 forces x0or5.

Thus every quantum transversal is wholly A/B-type PRESERVING or wholly SWAPPING. A full resolution must cover the fifty same-type cells, which can occur ONLY in preserving transversals. No covariance or cyclicity of the resolution is assumed.

## 3. ExactlyONE affine block and one NONaffine: complete obstruction independent of all signs

A preserving transversal has allfive A/A cells. They are FIFTH-root vectors on BOTH physical blocks, because both input top rows have no minus sign. On the affine block their chirp frequencies a*i-f(i) must be distinct: repeating a frequency would put FIVE identical fifth-root phases in a full inner product that would need each fifth root exactlyTWICE. Hence f and a*id-f are permutations ofF5.

The complete permutation lemmav48 gives f(i)=v*i+w, v!=0. (Its proof kills the quartic coefficient by the sum, kills the cubic coefficient by the squared-sum identity, and rules out a quadratic permutation over oddF5.) Their affine-block restrictions are mutually orthogonal; therefore their other-block inner products must vanish too. Those differences are(i-j)[sigma(t)-v*t] plus a constant, forcing sigma-v*id to be a permutation. The same lemma forces the allegedly NONAFFINE sigma to be affine, contradiction.

All top-row quadratic constants and bottom-row signs are irrelevant to this A/A contradiction but were NOT deleted from the full array. Thus no preserving transversal exists in this entire one-affine/one-nonaffine branch; fifty cells are untransversalizable.

## 4. Both blocks affine: exact normalization and all quadratic degeneracies

If the physical blocks are exchanged, absorb that exchange into H_s: swapping s0,s1 negates l_s,d_s, with the same delta_s, and dephasing by row constants restores the displayed form. Thus write the coordinate maps as L_j->L_(a*j+b),R_j->R_(c*j+e), with a,c nonzero and b,e ARBITRARY.

A preserving transversal again has five A/A cells, and its top matching f is affine f(i)=v*i+w, v!=0, by section3's A/A argument on either affine block. Pick any one of its bottom/bottom cells. Relative to each top/top cell its two quadratic coefficients are

    qL=s0*a^2-r0,
    qR=s1*c^2-r1.

If EXACTLYONE iszero, that block's five-term linear sum is either0or5times a unit phase; the other quadratic sum has squared modulus5 and is nonzero. They cannot cancel (squared moduli0or25 versus5). No preserving transversal exists.

If BOTH arezero, their square characters show delta_s=delta_r, so A/A andB/B rays have the SAME binary parity class and become fifth-root representatives. ALL ten restricted vectors on the chosen physical block lie in the SAME five-element Fourier basis. Two must be proportional on that block. FIVE identical fifth-root terms then prohibit full orthogonality. Thus no preserving transversal exists in this double-zero case either.

It remains to analyze BOTH qL,qR nonzero with their signs retained; this is where a fifth-root-only shortcut would fail.

## 5. Gauss signs and the leading phase equation force a nonsquare equality

The bottom/bottom right-block sign relative to the top/top vector is

    kappa=delta_s*delta_r
          =Legendre(s1*r1/(s0*r0)).

The mixed inner product is the left Gauss sum PLUS kappa times the right Gauss sum. Since-1 is NOT a fifth root, vanishing requires BOTH

    Legendre(qR/qL)=-kappa,

and equality of the completed phases. The coefficient of i^2 in that phase equality is exactly

    l_s-l_r*v^2+(c-v)^2/(4qR)-(a-v)^2/(4qL)=0.   (LEAD)

All coordinate shifts and the matching intercept w affect only linear/constant terms, so LEAD is a necessary condition for the five exact inner products. This uses the actual sign condition rather than assuming two quadratic Gauss sums cancel automatically.

Using4l_r=1/r0-1/r1 and4l_s=1/s0-1/s1, complete this coefficient algebraically:

    (r1-s1*c*v)^2/(s1*r1*qR)
       =(r0-s0*a*v)^2/(s0*r0*qL).                (SQUARES)

For example the left-block contribution has numerator-(r0-s0*a*v)^2 after taking the common denominator s0*r0*qL; the analogous right block gives the other square. No code alignment or identical-matrix parameter was used.

The multiplier relating these squares has Legendre character

    Legendre[(s1*r1*qR)/(s0*r0*qL)]
       =kappa*Legendre(qR/qL)=-1.

Therefore BOTH squared factors inSQUARES must beZERO:

    r0=s0*a*v,        r1=s1*c*v.                 (ALIGN)

This is the whole sign-sensitive obstruction, valid for unsigned/unsigned, signed/signed AND mixed-sign parameter pairs.

## 6. ALIGN contradicts maximality, or fails the Gauss sign condition in the final linear case

The original H_r B-row phase differences have block-linear direction

    v_r=-2r0X-2r1Y

and curvature d_r*t. The transformed H_s B-row differences have block-linear direction

    v_s'=-2s0*aX-2s1*cY=v_r/v

byALIGN, plus a possible linear t-component from coordinate shifts, and curvature d_s*t.

If d_r!=0, its differences for each nonzero row-parameter difference fill ALL t-components along that nonzero block-linear direction. Hence they meet a nonzero transformed B-row difference. If d_s!=0, the same argument with the roles reversed gives an intersection. Within B-type rows the minus signs cancel, so this common phase difference produces an ACTUAL collision of two Hadamard-pair projective rays. Maximality fails.

This covers every case where AT LEASTONE curvature is nonzero, including arbitrary affine shifts. A global linear plane or common sector is not inferred from that collision.

If d_r=d_s=0, then r0=r1 and s0=s1; bothdelta values are-1, so kappa=+1. ALIGN forces a=c, hence qL=qR. Their Legendre ratio is+1, contradicting the necessary Gauss condition Legendre(qR/qL)=-kappa=-1. Thus the last purely linear possibility cannot contain a preserving transversal either.

Therefore EVERY preserving transversal in the nondegenerate quadratic case contradicts either maximality or the exact Gauss-sign condition. Together with section4 all affine cases are exhausted.

## 7. Original full-resolution consequence and precise residual

Every full resolution would need preserving transversals to cover the fifty same-type cells. In exactly-one-affine cases there are none; in both-affine cases they imply repeated rays or are impossible. Thus no MAXIMAL1-RQLS10 exists in this entire block-setwise/atleast-one-affine family of ALL16signed/unsigned Gaussian matrices, with the two parameter choices independent.

This does NOT claim that every nonmaximal branch is unresolvable. It also does NOT exclude both-nonaffine aligned signed pairs, mixed-sign pairs with genuinely mixed physical blocks, arbitrary tenth-root Hadamards or unrestricted original arrays. The minus signs and quadratic degeneracies were essential to the proof and cannot be discarded as in a phase5-only argument.

The original intrinsic10/4+6/5+5 possibilities remain OPEN, as do those explicit residual phase models. No actual100-ray1-RQLS witness or unrestricted no-go.

## 8. Entire gate and assurance

Review ALL EIGHT sections/endings: universal signed parameter Hadamard; ALL chirp-count coefficient collisions; top/top fifth-root permutation proof independent of bottom signs; both block orientations/exchanges; EXACT one-zero and double-zero handling; kappa/Legendre condition; FULLshift-independent leading equation and exactSQUARES factorization; curvature-plane difference collision; BOTHzero-curvature sign contradiction; and maximality-versus-resolution limits. A nonzero quadratic or unsigned sample is not the theorem.

The operative MUB/permutation/Gauss proofs are printed in this packet and ENTIREv48/v49 as used. No unprovided classifier is a premise. All arithmetic is exact WRITTEN, NOT machine-checked. No scientific execution/private approximate scout/finite enumeration/independent finite-witness checker/control/vendor/priority gate used or called passed. No formal/kernel/family/human/current-openness/novelty/original-witness promotion. All old process/math findings, v9/v14 withdrawals, frozen histories and ZERO-credit quarantines persist. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; primary continues genuinely remaining aligned/nonaffine/mixed geometry, no early pending-review park.
