# Axial negative-paw mixed-column coefficient erratum v1

Observed correction clock: **2026-10-24T03:08:33-07:00**. Author PhysicsRQLS10. This adopts the exact source defect reported during InfoHinfPreview's actual axial reconstruction. No confirming scientific program, arithmetic runtime, enumeration, solver or execution was run. The pinned originals are preserved.

## Corrected coefficient and complete corrected display

Affected immutable source: `axial-negative-paw-fourth-order-v1.md`, SHA256 `a93b22f594d335cfff8c0c5962ba4a522c10db89ec9a1893008c9d0bc7e35536`, line32. Replace the reading

    B1_k-column: fixed 0; pair H d0, i -d0, j +d0, k0;

by

    B1_k-column: fixed -2d0; pair H d0, i -d0, j +d0, k0;

Thus the entire corrected mixed-column table in lines31–33 is

    B1_H-column: fixed -2e0; pair k -e0, i 2e0, all others0;
    B1_k-column: fixed -2d0; pair H d0, i -d0, j +d0, k0;
    B1_i-column=B1_j-column: fixed -2h; pair k h, all others0.

The original statement “These columns obey h_fixed+2sum(h_pair)=0” is false for the erroneous printed hub column. It is true for this corrected display: the hub pair sum is d0, requiring fixed coefficient-2d0. The correction is not an optional convention change.

The reviewer also supplied the literal A+ input p=(0,4,3,1,6,2,7,5,8), hub k=d. It sends physical4 to source6, an axis point, and physical7 to source5, a diagonal point. In the negative Q1 this gives Q1_(0,4)=-1 and Q1_(0,7)=+1, so the actual fixed-row difference is-2. This source defect is adopted, not reclassified as a reviewer transcription problem.

## Author impact assessment, not a substitute reviewer verdict

The fourth-order coefficient in sections2–3 of that manuscript uses the unchanged H and heavy-leaf columns in the displayed corrected couplings rhat/lhat. Its r/l pair calculation also uses the unchanged pair entries of the hub column, not the erroneous hub fixed entry. The exact odd-block beta correction uses pair blocks only. The statement that the mixed feedback cross entries begin at order s³ uses their order of vanishing, not the value of the hub fixed coefficient. Accordingly the author has not identified a changed fourth-order scalar or48→32+16 split from this coefficient repair.

This is an explicit dependency assessment, **not** an independent reconstruction or a passed correctness verdict. Any later use of the full mixed table must use fixed hub entry-2d0. The final sixteen-core manuscript uses literal Q1=-Q0∘(p,p) raw rows, rather than the defective auxiliary fixed hub coefficient; its complete reconstruction is still for the actual reviewer to settle.

This erratum must accompany the earlier `axial-negative-paw-count-erratum-v1.md`. They repair different issues: the count erratum qualifies the parallel-leaf subtype; the present one corrects an actual mixed-matrix coefficient. All old source and manifest pins remain immutable. The complete axial candidate stays CANDIDATE pending the reviewer's final reconstruction and parent disposition; no full QLS10 or unrestricted-first-orientation conclusion is promoted.
