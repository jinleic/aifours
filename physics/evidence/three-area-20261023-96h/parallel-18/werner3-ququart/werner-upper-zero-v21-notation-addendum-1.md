# Addendum to v21 — distinguish the scalar edge mass factor from the forcing vector

Owner: PhysicsResearch96h-2. Precreation `/bin/date`: **Mon Oct 26 06:45:05 PDT 2026**.

Pinned source: `werner-upper-zero-consolidated-v21-universal-deficit-bound-and-symmetric-closed-form.md`, SHA256 `f412b11d5963499babd03db2bc5afa51fc108bfd6be5cd230fb86776c5a19fed`. Its bytes are unchanged.

The packet uses `g_e` for two different objects. This is a notation defect. Read the formulas with the following distinct names throughout:

- Scalar edge mass factor: `gamma_e = d_e - delta_e^2/4`, so `m_e = x_i x_j gamma_e`.
- Symmetric-sector forcing vector: `b_e = x_i x_j delta_e^2 tau_e/2`.

Thus item 3 reads

`E_c(Z) = Sum_e x_i x_j [2r-d_e(1-d_e)]|tau_e|^2 + Sum_i d_i^2 nu_i |taubar_i|^2 - (1/4)b^dagger K_sigma^-1 b`,

and its mass-only lower bound uses

`mu_e = 2r-d_e(1-d_e)-delta_e^4/(16 gamma_e)`.

In proof steps 6–8 and the consistency paragraph, every vector occurrence of `g` means `b`, and every denominator `g_e` means the positive scalar `gamma_e`. In particular,

`Sum_e |b_e|^2/(4m_e) = Sum_e x_i x_j delta_e^4|tau_e|^2/(16 gamma_e)`.

No mathematical sign is proved by this notation repair. All provenance and assurance limits of v21, including the owner-reported pre-probe status, v24/v29/v33/v36, and cp047 B1–B3, remain mandatory. Written symbolic correction only; no evaluated instance or execution.
