# Single-frequency skew noise, single input, ANY output, any even dimension: exact robust gain, exact mean-square value and the equality locus via planar reduction

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 08:16:43 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Author-written and unreviewed; not adopted; no gate.
- Value side only, under v209 (`1ec52034…`).
- All-variable, source-fixed conventional proof. No machine-checked identity.
- No chosen numeric probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- Frozen v27–v32 untouched. No v220 file, live review or assignment read.

## 0. Statement

**Class SF-1.** Uncontrolled constant data with:

- n even;
- A0 real skew with A0^2 = −σ^2 I and σ ≠ 0;
- Ā = μI with μ < 0;
- a single input column c ≠ 0 and an ARBITRARY output map D0 ∈ R^{q×n};
- any preview δ ≥ 0;
- canonical one-Brownian filtration.

The class is EMS (v40).

**Compressed plane data.** Put V_c := span(c, A0c), with orthonormal basis (ĉ, A0ĉ/σ). Let D0' := D0|_{V_c}, and let M' := (D0')^T D0' be the 2×2 compressed weight in that basis.

**Theorem SF1.** For every preview:

1. **(Exact robust gain.)** G_rob = (|c|/|μ|) √Λ', where Λ' is v45's Λ computed from M', with the input direction e_1 = ĉ.
2. **(Exact mean-square value, eigen-aligned.)** If ĉ is an eigenvector of the compressed weight, i.e. M'_12 = 0, then with x := M'_11 and y := M'_22,

   `G2,∞^2 = |c|^2 c_*(c_* x + ((a−b)/2) y)`.

3. **(Equality locus.)** In the eigen-aligned case, G1,∞ = G2,∞ iff y > 2x and x/y = r/(1+r), i.e. σ^2 = |μ|(1−2ρ)/ρ with ρ = x/y ∈ (0, 1/2). Otherwise G2,∞ < G1,∞.
4. **(Literal certificate.)** In all cases G2,∞ ≤ G1,∞ ≤ min(√2·G2,∞, |c|√Λ'/|μ|).

Here a, b, r and c_* are as in v43.

**NOT delivered.**

- Multi-input data.
- Multi-frequency skew noise.
- Exact G2 when ĉ is not an eigenvector of M'.
- Exact G1 off the locus.
- Controlled data, a controller, synthesis, or an RMS-to-literal transfer. C1–C3 and R4 STOPPED.

## 1. Inputs and separation

**Adopted inputs** (read completely this session):

| Input | LF | Pin |
|---|---|---|
| v25 | 348 | `8c381b1f…` |
| v26 | 308 | `6666f555…` |
| parent | 74 | `1f00e0c6…` |

**Cited author packets** (unreviewed):

| Packet | Pin | Used for |
|---|---|---|
| v42 | `eadc0444…` | invariant-plane reduction |
| v43 | `b4e13943…` | exact G2 |
| v44 | `796c420a…` | equality characterization |
| v45 | `d7c9814c…` | exact G_rob for a single input |
| v34 | `6fcca986…` | Theorem R |

**Separation.** None of the following is used: storage, Riccati/LMI, Gramian certificate, controller, selected control, changed output, quarantined guidance, RMS source.

## 2. Proof

**Reduction (v42 §2, Steps 1–3).**

- V_c is a 2-dimensional A0-invariant plane on which A0 acts as σJ.
- The state stays in V_c pathwise, for the actual noise and for every noise path ℓ.
- Hence D0 X = D0' X, and the original plant and the planar plant have identical input–output maps, both pathwise and for adapted inputs. The planar plant is (V_c, σJ, μI, input |c| e_1, output map D0' with weight M').
- So G1, G2 and G_rob coincide for the two plants.

**Items.**

1. v45 Theorem RG1 applied to the planar plant.
2. v43 Theorem EX applied to the planar plant.
3. v44 Theorem EQ applied to the planar plant.
4. v34 item 1 and v27 C1. ∎

## 3. Meaning (value side only)

The equality locus discovered in v44 is not a planar accident. Take any even dimension and a single-input channel driven through single-frequency rotation noise, with the input direction an eigenvector of the compressed output weight. Then the printed E path-L2 level equals the mean-square level exactly at one noise level per compressed anisotropy ratio (when y > 2x), and the gap is strict otherwise. For non-eigen-aligned compressed data, only the sufficient strictness test of v45 RG1b and the exact robust certificate are available.

No controller or synthesis statement is made.

## 4. Process and assurance

- Written exact mathematics only, after v209 was read FIRST and the adopted inputs were read completely.
- Frozen v27–v32 untouched. No v220 file, review or assignment was opened.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not an early final park.

**END OF COMPLETE v47.**
