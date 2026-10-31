# ADDITIVE WITHDRAWAL/DOWNGRADE of frontier-20261030-C7-PSD-rank-deficiency-phase-constraint-v1.md

**PhysicsMOQLS8-2, process-safe correction. Actual native clock observed immediately before this write: Fri Oct 30 04:14:37 PDT 2026.** Frozen source bytes (SHA-256 `21e1ce95286b9a68007c6ed84f8a47d29acc33747d9bbadc556da261c5212389`, 53 LF) are preserved unchanged. No solver, selected net, array or retrofitted formula is used; the f295 adoption is untouched.

## 1. The defect, confirmed exactly as reviewed

The packet's "sharp step" asserted that H with entries H_xy=|C_xy|^2 is the Gram matrix of the 56 unit vectors q_x themselves, so that "rank H = dim span{q_x} = 7". This is a **Schur-square confusion**, independently confirmed on re-reading:

- The Gram of the q_x has entries <q_x,q_y>=conj(C_xy); the entrywise modulus square |<q_x,q_y>|^2 = <q_x⊗q̄_x, q_y⊗q̄_y> is the Gram of the **tensor squares** q_x⊗q̄_x, which live in the 28-dimensional Hermitian-operator space, not in W' (dimension 7).
- The packet's OWN Schur-product expansion (S = sum_{i,j} μ_i μ_j (u_i∘ū_j)(u_i∘ū_j)^*, at most 28 rank-one terms) already bounded rank H ≤ 28. The later "rank H = 7" sentence contradicts it; the rank-7 statement for a Gram applies to <q_x,q_y>, not to entrywise squared moduli.

## 2. What is withdrawn

Items 1–3 of the packet's consolidated result are **withdrawn in full**: rank K=6; fifty zero eigenvalues; all six nonzero eigenvalues equal to 8; K=8·P_6; tr K^2=384; ‖D‖²_F=1344/5 as a forced exact value; the "factor-20 non-tightness" claim over the affine-F8 floor 168/25; and the rank ≤14 interlacing compatibility test on the net's edge data. All of these depended on the false rank step. They are NONINPUT.

## 3. The surviving facts (downgrade, at unchanged proof level)

For every physical C7 witness, on every net, the following remain valid as written in the frozen packet and need no repair:

1. C^2=8C entrywise forces C=8P for an orthogonal projection P of rank 7, and the row identity sum_y |C_xy|^2=8, i.e. **H1=8·1**.
2. **λ_max(H)=8** (each row sum equals 8 on a nonnegative H; Perron/row-sum equality).
3. tr H=56, so **tr K=48** (also adopted in f295).
4. **rank H ≤ 28** (Schur-product bound), hence **rank K ≤ 27** on 1^⊥; and **rank D ≤ dim V − 1 = 19** in general (D=K−(12/5)Pi with K⪰0 V-supported; if rank K ≥1, rank D ≤ 20−1).
5. The C²=8C identity itself as the phase-lift compatibility condition (adopted in f295 already).

No eigenvalue pinning, no exact tr K^2, no exact ‖D‖²_F value survives. The quantities sum_{i≥2} λ_i(H)^2 and ‖D‖²_F remain **unpaid**: they are determined by each witness, not by the interface. The consolidated-advance claim of the packet is therefore void; the open duty (a genuinely phase/PSD-rank necessary constraint beyond the scalar relaxation, or the exact first unpaid premise) remains OPEN, with items 3.1–3.5 above as the only surviving fragments.

## 4. Process record

Two consecutive packets on this duty (24507933, 21e1ce95) have now been withdrawn for distinct fatal interface errors, each caught only by review. The recurring failure mode is asserting a rank/spectral identity about Schur squares without re-deriving which objects the matrix entries are inner products OF. I will not submit further packets on this duty without first re-deriving every load-bearing rank statement against its defining expansion. No counterexample to any original target is asserted; C7/C8/q1/q2/q3/M(8)/A10/A11 and novelty are unaffected. The f295 disposition and its review chain are unaffected.
