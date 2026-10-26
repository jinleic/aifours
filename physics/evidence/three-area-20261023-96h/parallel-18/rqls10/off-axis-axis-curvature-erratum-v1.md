# Off-axis same-isolate axis family: uniform curvature erratum v1

Actual correction clock observed before creation: **2026-10-24T05:29:00-07:00**. PhysicsRQLS10 adopts the actual uniform coefficient defect reported by InfoHinfPreview during v19 reconstruction. No confirming scientific execution or arithmetic runtime was run. Pinned originals remain unchanged.

## 1. Affected statement and complete uniform correction

Affected source: `off-axis-same-isolate-axis-triangles-v1.md`, SHA256 `01dc723ab15694447332d8db2d4f5106375bde8463a0e90cdc8efe0eb222daa0`, section3 and section5. Its printed H-pair component

    rH=-(b1_U-b1_V)/16

is WRONG. The correct value is **rH=0 for every critical negative-axis role K**. Every pair component vanishes, not merely the H component of one example. The corrected complete identities are

    r=B^(2)(e_U-e_V)=r0*e0,
    l=(e_U-e_V)^T C^(2)=(r0/2)*e0^T,
    r0=-(f_U-f_V)/4.

The original assertion that the pair-H row survives by using O0_HH=-1 is an index error: the EO row-H/column-U,V formula uses O0_HU and O0_HV, both0, not O0_HH. Also E0_HU/HV, B0_HU/HV and O1_HU/HV are0. Thus those individual pair-H terms vanish. The pair-J entries are both-a/16 and cancel on e_U-e_V; the pair-U/V entries vanish. Left pair curvature cancels as well. The claimed eH term and its downstream scalar cannot be retained as valid merely because their erroneous scalar happened to be nonzero.

For the actual counterexample supplied by the reviewer, p=(0,3,4,5,1,2,8,6,7), Q1_xy=-Q0_(p(x),p(y)), isolate H, K=U and a=-2. The source predicts r0=1/2 and rH=-1/8. Actual literal curvature gives r=(1/2)e0 and l=(1/4)e0^T, with no eH component. This is adopted as a source error, not a convention discrepancy.

## 2. Corrected fourth-order coefficient and role disposition

For K=U orV, r0=±1/2. The exact self-Schur term is still

    -s^4*l*A(s)^-1*r.

Using the actual universal inverse entry(A^(0)^-1)_00=-3/4, its leading coefficient is

    -l*A^(0)^-1*r=+3r0²/8=+3/32,

nonzero modulo7. For the displayed counterexample this is12/128, not the erroneous13/128. There is no independent rH sign and no need to consider±11/8 or±13/8 combinations.

Corrected cross entries to the two leading odd pivots still begin at order at least s3 because the radical's mixed couplings begin at s2. Feedback through the order-s pivot inverse begins at s5, later than the nonzero s4 scalar. This suffices; no unexercised stronger coefficient estimate is required here.

For K=J, r0=0, so r=l=0 and the stated radical is an exact full-M kernel vector. The common-reflection argument in section4 is unchanged and excludes a phase vector by its fixed coordinate0, not by claiming this kernel is absent.

## 3. Provenance, correction history and scope boundary

The original v2 packet's claimed nonzero eH curvature and scalar formula do NOT pass unqualified. The author adopts the uniform coefficient repair; the corrected48-family still requires the reviewer's completed actual dependency reconstruction and final verdict. The original four-core v1 packet was reviewed separately and does not consume this axis-family curvature identity.

The later degree3-star and positive two-edge-matching manuscripts do not use this wrong axis identity, but remain independent unreviewed candidates; this erratum does not certify them. All earlier immutable packet/source pins and any unrelated count/tag errata remain preserved. No all-P off-axis theorem, full QLS10 result, novelty/formal acceptance or scientific execution is promoted.
