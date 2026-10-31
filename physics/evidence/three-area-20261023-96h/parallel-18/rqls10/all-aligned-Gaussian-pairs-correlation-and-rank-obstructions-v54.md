# RQLS10 v54 — CLOSE every aligned Gaussian pairing, including BOTH nonaffine blocks; only mixed-sign/block-mixing remains in the16-matrix model

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE writing this NEW manuscript: **Mon Oct 26 12:07:25 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact phase-difference moments/permutation interpolation/block-count/rank proof only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty/accepted finite-witness claim.

## 1. Exact larger aligned theorem and candidate family census

Use the COMPLETE16 signed/unsigned Gaussian Hadamards ofv53, with independent nonzero parameters(r0,r1),(s0,s1), ratios

    rho_r=r1/r0, rho_s=s1/s0,
    delta=-Legendre(rho).

Allow ANY relative coordinate permutation mapping the two physical5-blocks SETWISE, preserve or exchange. The blocks may have COMPLETELY arbitraryF5 permutations; no affine assumption remains.

**Aligned theorem.** NONE of these pairs produces a MAXIMAL1-RQLS10. The at-least-one-affine branch is ENTIREv53. Here the BOTH-NONAFFINE branch is closed by new moment conditions and an exact rank obstruction.

Candidate union consequences, requiring joint review:

- two UNSIGNED(nonsquare-ratio) Gaussian matrices: ALL relative pairings already closed byv49;
- two SIGNED(square-ratio) Gaussian matrices: misaligned physical cuts closed byv52, aligned cuts byv53+this packet; therefore ALL relative pairings closed;
- one unsigned and one signed: ALL block-setwise pairings closed here; genuinely BLOCK-MIXING relative permutations remain OPEN.

These are the explicit Gaussian16-matrix models, NOT allBH(10,10) or originalarrays. The original maximal1-RQLS10 remains UNKNOWN.

## 2. Nonaffine permutations have nonzero linear correlation overF5

Assume both block coordinate permutations sigma_L,sigma_R are NONAFFINE. Absorb a physical block exchange into H_s by swapping its parameters (with the correct row phases/sign retained). Define

    C_L=sum_(j inF5) j*sigma_L(j),
    C_R=sum_(j inF5) j*sigma_R(j).

Both are NONZERO. Indeed a permutation of F5 has a unique polynomial of degree<=4; its sumZERO kills the fourth-degree coefficient. If its cubic coefficient also vanished it would have degree<=2, and a nonconstant quadratic is not a permutation in odd characteristic. Thus a NONAFFINE permutation has NONZERO cubic coefficient. Multiplying byj and summing extracts its negative (sumj^4=-1), giving the claim.

This is a complete proof, not a finite list of nonaffine permutations or a numerical correlation.

## 3. Four exact phase-moment constraints for ANY transversal contingency

Let X=(j onL,0 onR),Y=(0 onL,j onR),T=(0 onL,1 onR). Put

    U_r=X+Y,       V_r=-2r0X-2r1Y;
    U_s'=P(X+Y),   V_s'=P(-2s0X-2s1Y).

Each of these four vectors has squared coordinate sumZERO inF5, because permutations preserve the sums of j,j^2. They are all orthogonal to T, and Q(T)=5=0. Constant quadratic offsets cancel when subtracting two rays in the SAME cell-type block.

Within one cell-type block, its two Gaussian sign masks are the SAME, so signs cancel in inner products. Orthogonality is then an ACTUAL fifth-root sum and implies the squared exponent-difference sumZERO. For two cells in a transversal's same type, both row/column parameter differences are NONZERO. Therefore if that block contributes at leastTWO cells, the corresponding dot product must vanish:

    A/A:   C_L+C_R=0;
    B/B:   s0*r0*C_L+s1*r1*C_R=0;
    A/B:   r0*C_L+r1*C_R=0;
    B/A:   s0*C_L+s1*C_R=0.                      (FOUR)

For example A/A differences are Delta_i*U_s'-Delta_j*U_r plus a multiple ofT; their square is-2Delta_i Delta_j*dot(U_s',U_r), with dot equal C_L+C_R. The other three identities follow from V_r,V_s' and retain every parameter/sign. No common complex sector is inferred from these finite moments.

Let a hypothetical transversal have counts

    A/A:x, B/B:x, A/B:5-x, B/A:5-x.

If x>=2, the first two equations ofFOUR both apply. Since C_L,C_R!=0, they force

    C_R=-C_L,     rho_r*rho_s=1.                (SAME)

If x<=3, the last two apply and force

    rho_r=rho_s.                               (CROSS)

The threshold2 is essential; a one-point cell-type subset supplies no pairwise constraint, and no such nonexistent equation is assumed.

## 4. Full-resolution counting closes every ratio pair except equal square ratios

Across a full ten-transversal resolution, the A/A25cells are covered exactlyonce, so

    sum_(ten transversals) x=25.

If rho_r*rho_s!=1, SAME forbids x>=2 in EVERY transversal, hence all x<=1 and their sum<=10, impossible.

If rho_r!=rho_s, CROSS forbids x<=3 in EVERY transversal, hence all x>=4 and their sum>=40, impossible.

Thus a full resolution in this both-nonaffine branch necessarily has

    rho_r=rho_s AND rho_r^2=1,
    rho_r=rho_s=+1 OR-1.

In particular all unsigned/unsigned nonsquare ratios and all mixed signed/unsigned ratios are excluded here without an affine-block assumption. Equal square ratios are the ONLY genuine remainder and are handled next; none is silently included in these counting contradictions.

## 5. Equal ratio-1 signed matrices: preserving and swapping transversals require incompatible correlations

If rho_r=rho_s=-1=4, both Hadamards are SIGNED TypeII. Their block-setwise pairing aligns the physical cuts, so ENTIREv52 forces EVERY transversal to be PURE: x5(preserving)orx0(swapping), with exactlyFIVE of each type in a full resolution.

A preserving transversal has x5, so A/A forces C_R=-C_L. A swapping transversal has x0, so A/B forces

    r0*C_L-r0*C_R=0 => C_R=C_L.

A full resolution would need BOTH conditions. They give2C_L=0, impossible since2!=0 and C_L!=0. Thus no full resolution exists. We do not falsely say that both individual types are always absent; they simply cannot both be present for a fixed pair as required.

This closes the equal ratio-1 case for all both-nonaffine permutations and all parameter values.

## 6. Equal ratio+1 signed matrices: every PURE transversal has forbidden phase rank<=3

Now r0=r1 and s0=s1, so d_r=d_s=l_r=l_s=0 and both matrices are TypeII. Their UNSIGNED phase row sets have only two parallel affine5-lines:

    originaltop:  i*U_r,
    originalbottom: W_r-2r0*k*U_r;
    permutedtop: i*U_s',
    permutedbottom: P W_s-2s0*k*U_s'.

Their fixed bottom signs are STILL present in the actual Hadamards; they are not deleted to assert unsigned row ONBs.

Aligned cuts force every candidate transversal PURE byv52, x5or0. Within either pure class, one common coordinate sign pattern makes its ten vectors FIFTH-root representatives. Put E=span_F5(U_r,U_s'), of dimension<=2.

For a preserving transversal its five A/A phase words lie in E and its five B/B words lie in

    P W_s-W_r+E.

For a swapping transversal its five A/B words lie in-W_r+E and its five B/A words inP W_s+E. In BOTH cases the affine span of ALL ten words has dimension at mostTHREE (one2-space plus one offset), even after quotient by constant words and legitimate phase dephasing.

But ENTIREv40–v42 proves EVERY fifth-root10-ray ONB has dephased affine phase rankEXACTLYFOUR. Contradiction. Thus no quantum transversal exists in this aligned ratio+1 family, independent of maximality and independent of whether its block permutations are affine. It is not necessary to assert a monomial equivalence with F10.

Together withv52's misaligned-cut obstruction, the entire ratio+1/ratio+1 signed Gaussian pair family has no quantum transversal for ANY relative pairing.

## 7. Complete aligned and signed-pair unions, with all original limits

Sections2–6 close ALL both-nonaffine block-setwise cases. ENTIREv53 closes all cases with at leastONE affine component (some via repeated rays, not blanket nonresolution). Thus all aligned physical-block Gaussian pairings are excluded for MAXIMAL1-RQLS10.

For TWO signed Gaussian matrices, a physical-block-mixing relative permutation gives MISALIGNED cuts and no quantum transversal byv52. Therefore the entire signed/signed Gaussian family, with independently chosen parameters and arbitrary monomial pairings, is excluded for maximal1-RQLS10. The unsigned/unsigned full family was separately closed byv49. For a MIXED signed/unsigned pair, block-mixing relative permutations are NOT covered by the two-cut contradiction because one matrix has only one binary class; that remains an explicit live residual.

These are CANDIDATE JOINT UNIONS, not automatically adopted from separate branch returns. Review must reconstruct every stated scope, hypothesis, sign/phase conversion, rank import and full-resolution count. No Gaussian or flat-root assumption is WLOG for arbitrary originalarrays. The unrestricted intrinsic10/4+6/5+5 branches remain OPEN, and no100-ray1-RQLS witness or unrestrictedno-go is supplied.

## 8. Entire gate and assurance

Read ALL EIGHT sections/endings and ENTIRE operativev51/v52 parity-normalform/purity,v53 one-affine analysis andv40–v42 phase-rank proof. New required claims include C_L,C_R nonzero from NONaffine permutation interpolation; actual same-type sign cancellation; ALLFOUR squared-difference moment equations; precise2/3 thresholds; sumx25 coverage rather than unjustified fixed contingency; all remaining square-ratio cases; ratio-1 incompatible pure types; ratio+1 two-parallel-line affine-rank<=3 with the correct pure-class normalization; and only the stated Gaussian pair unions. A sampled correlation or ignored one-point block does not accept the theorem.

No classifier/executable arithmetic/private approximate scout was used. All operative reasoning is exact WRITTEN, NOT machine-checked. Independent finite-witness/checker/control/vendor/priority gates NOT PERFORMED underHOLD. No formal/kernel/family/human/current-openness/novelty/original-witness promotion. All old process/math findings, v9/v14 withdrawals, frozen histories and ZERO-credit quarantines persist. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; primary continues genuinely MIXED-sign/block-mixing or unrestricted original geometry, no early pending-review park.
