# Stochastic H-infinity preview: value-side descriptor union and a strict literal-versus-RMS gap

Parent observation before writing: **2026-10-27T08:20:27-0700 PDT**.

**The complete v220 value-side union v27–v32 is WRITTEN_SUPPORTED at the ordinary foundations and exact model domains below, with two mandatory precision qualifications for v32 and the inherited Q1 terminal-information qualifier.** Its main new conclusions are:

- the adapted input-quotient norm is equivalent to a conditional future-energy norm within factors `1` and `sqrt(2)`, so the full risk descriptor is evaluated up to `sqrt(2)`;
- on canonical constant data, the descriptor equals, up to `sqrt(2)`, the plain Hilbert norm of the annihilating adjoint and is capped by `sqrt(2)` times the open-loop RMS relaxation;
- for every uncontrolled exponentially mean-square-stable plant, the mixed RMS-input/path-norm-output gain equals the RMS gain;
- for such a plant, the printed path-norm gain equals the RMS gain exactly when RMS is an almost-sure pathwise bound; the AHEAD condition gives `G2 < G1 <= sqrt(2) G2`.

For the gate-I scalar multiplicative-noise family, AHEAD is proved directly. Therefore `G2 < G1 <= sqrt(2) G2` for that family without using the value of `G2`; the exact identification `G2 = gamma_star = 2cd/q0` remains conditional on the earlier adopted gate-I import. Thus the mean-square replacement is strictly optimistic for that uncontrolled class.

This is **not** a controller, a common causal or stationary policy, internal-EMS synthesis, prescribed-gamma necessary-and-sufficient theorem, RMS-to-literal synthesis transfer, exact value of the literal gain, sharpness of `sqrt(2)`, novelty clearance or stronger verification. The realization routes C1–C3 and R4 remain STOPPED.

## Complete reads and bindings

Main read all six new bodies and both actual reviews completely, through their endings, in serial returned raw windows; the three requests and documentary addendum had already been read completely earlier in this session. Live SHA-256 pins matched after the reads.

| Input | LF | SHA-256 |
|---|---:|---|
| [v27 BMO evaluability](../../../information-science/evidence/three-area-20261023-96h/parallel-18/stochastic-hinf-preview/literal-preview-synthesis-consolidated-v27-descriptor-BMO-evaluability.md) | 283 | `af2abd51001ca6d16dd3d4415d49104c25110b7f16415689052329f1a77f55b5` |
| [v28 controlled open-loop cap](../../../information-science/evidence/three-area-20261023-96h/parallel-18/stochastic-hinf-preview/literal-preview-synthesis-consolidated-v28-controlled-descriptor-open-loop-RMS-cap.md) | 186 | `e30bdd3d196883dd1b7842472c7f9ab1386a06e4ac78ff96cff3a820f64ac87b` |
| [v29 nonexactness and EMS sandwich](../../../information-science/evidence/three-area-20261023-96h/parallel-18/stochastic-hinf-preview/literal-preview-synthesis-consolidated-v29-BMO-nonexactness-and-uncontrolled-EMS-sandwich.md) | 175 | `f1e2a0575ef5f76a25690b4e21574ea631565c4e13f88da50f23d677b2b9bc4c` |
| [v30 full descriptor L2 sandwich](../../../information-science/evidence/three-area-20261023-96h/parallel-18/stochastic-hinf-preview/literal-preview-synthesis-consolidated-v30-full-descriptor-L2-adjoint-sandwich.md) | 194 | `42d86d0d2c88d9d0faaf52c0d8295c9fb4b66970877c5434c78fe347ac243940` |
| [v31 mixed-gain identity](../../../information-science/evidence/three-area-20261023-96h/parallel-18/stochastic-hinf-preview/literal-preview-synthesis-consolidated-v31-uncontrolled-EMS-mixed-gain-identity.md) | 186 | `4c2a7b9b2101efc49e29e1bc445eb8d0b3a5daaa9d32ace96999de1ade5d9cea` |
| [v32 strict gap characterization](../../../information-science/evidence/three-area-20261023-96h/parallel-18/stochastic-hinf-preview/literal-preview-synthesis-consolidated-v32-strict-literal-RMS-gap-characterization.md) | 259 | `2cdf4de9dee6ec2ed06111a7992abca56fd7a2d2d779a4eb8cfc0ac1ed28676d` |
| [Review A — InfoSPR7-2](../../../information-science/evidence/three-area-20261023-96h/parallel-18/robust-spr7/peer-review-v220-A-v1.md) | 307 | `8b4362c3e37c3c3616c2a6325c442b8fce1b80c9f47c0ee01e7cc3e8918bb581` |
| [Review B — MathKacMoody-2](../../../mathematics/evidence/three-area-20261023-96h/parallel-18/kac-moody/peer-review-v220-B-v1.md) | 319 | `5f4b7f6a7ccdf2b359fa54aed02ab8d387c3e751fe9d71db4d6e9b252b259caf` |

The operative [v25](../../../information-science/evidence/three-area-20261023-96h/parallel-18/stochastic-hinf-preview/literal-preview-synthesis-consolidated-v25-stochastic-universal-dual.md) (348 LF) and [v26](../../../information-science/evidence/three-area-20261023-96h/parallel-18/stochastic-hinf-preview/literal-preview-synthesis-consolidated-v26-risk-output-quotient.md) (308 LF) inputs remain at the scope of the earlier [v21/v25/v26 parent](preview-v21-v25-v26-stochastic-risk-entire-parent-v1.md); both current reviews reconstruct their specialized operative bridges again. The [v220 manifest](peer-review-wave-eighteen-v220.json) and [packet receipt](peer-review-wave-eighteen-v220-packet-receipt-v1.json) bind the full scope.

## Gate decisions

| Packet | Mathematical result | Dependency/application boundary |
|---|---|---|
| v27 A/A1 | For every progressive E2 input-adjoint process, `||r||_* <= nu(r) <= sqrt(2) ||r||_*`. | Holds on any filtration satisfying the usual conditions; the proof uses event-localized test inputs, a Stieltjes partition lemma and pathwise weighted Cauchy–Schwarz. No martingale representation, path-supremum norm or minimax step. |
| v27 B | The supremum of `||r_phi||_*` over the actual annihilating dual family equals the localized quotient gain `beta1`, and `beta1 <= kappa_risk <= sqrt(2) beta1`. | Uses the adopted SUPPORT/PAIR/EXACT-RISK interfaces and independent suprema. Actual unknown-controller lower bounds still need CP; outside CP only the bounded-test value applies. |
| v27 C/D | On uncontrolled data, `G1 <= sqrt(2) G2`; on canonical constant data, localization removal gives `g12 <= G1 <= sqrt(2) g12`. | C needs no EMS; D needs the canonical one-Brownian filtration and constant data. The gate-I numerical bracket is conditional on gate I. |
| v28 L/E/F/F1 | Localization includes the `B0 u dW` term; `kappa_risk <= sqrt(2) beta2`; on canonical constant data `beta2` equals the adapted open-loop RMS relaxation `g2_ol`; every law with E2 actual controls has `kappa_risk <= sqrt(2) G2(F)`. | F uses the independent initial sigma-field tensor structure and a Hilbert projection, not a controller selector. F1 limits what the necessity descriptors can certify; it is not a literal-gain or synthesis claim. |
| v29 O/U | For the whole symbolic late-window family, `nu(r) > ||r||_*`; hence the best constant lies in `(1, sqrt(2)]`. On uncontrolled EMS data, `G2 <= G1 <= sqrt(2) G2`. | O is a norm statement, not descriptor strictness. U's historical lower citation to the v14 theorem remains a named import, but the current union independently proves the same lower bound in v31. |
| v30 D′ | On canonical constant data, `beta1 = g12^Q`, both supremum identities hold, and `g12^Q <= kappa_risk <= sqrt(2) g12^Q <= sqrt(2) g2_ol`. | Bochner–Fubini sections, the module identity, closure of the localized range and a countably valued output near-selection are paid. This is not a nearest physical control or common policy. |
| v31 G/G1/G2 | For every uncontrolled EMS plant with canonical constant data, `g12_inf = G2_inf < infinity`; consequently `G2_inf <= G1_inf <= sqrt(2) G2_inf`, and descriptor equality is equivalent to `G1_inf = G2_inf`. | Finite RMS gain by conditional EMS, Minkowski and Young; equality by independent concatenated blocks, EMS tail bounds and the i.i.d. L1 law of large numbers. G2's exact gate-I value is conditional. No controlled analog. |
| v32 S | Literal gain equals RMS gain iff RMS is an almost-sure pathwise bound iff AHEAD fails; under AHEAD, `G2 < G1 <= sqrt(2) G2`. | Supported with **Q-rho** and **Q-zero** below. The adversary uses only progressive disturbance inputs, not controls or a state reset. |
| v32 S1/S2 | Every positive gate-I plant satisfies AHEAD, so its literal gain is strictly above its RMS gain; the named L2/BMO descriptor surrogate is strict after the supremum. | The AHEAD proof is direct. The equality `G2 = gamma_star` and every numerical gamma-star form are conditional on the earlier gate-I import. No exact `G1`, controlled extension or general synthesis. |

Both complete reviews found **0 new FATAL / 0 new MAJOR** mathematical defects and identified the same two localized MINORs. Neither review is blind or independent-family evidence: both disclose earlier specific contact with this author.

## Mandatory qualifications

1. **Q-rho / M1.** v32 LF115 states only `rho < G2_inf`. The construction needs `0 < rho < gamma`; for negative `rho` with `rho^2 > gamma^2`, the asserted block energy is impossible. The strict-gap proof uses only `rho` increasing to the positive `gamma`, after AHEAD has shown `gamma > 0`.
2. **Q-zero / M2.** Lemmas 1 and 2 state positive input energy, while the caller's first-phase energy `Y1` may vanish. On that branch the first response and `Z1` are zero, the dilution level is zero and the appended train is zero; every inequality reads `0 >= 0`.
3. **Inherited Q1.** Cylinder-dual density applies to raw output duals first conditioned on `F_T`, not to arbitrary `F_infinity` information. No current argument uses the overbroad earlier density sentence.

These are additive overlays on immutable author files, not mathematical falsity of the operative conclusions.

## Parent hand checks

1. **BMO duality:** for `w = 1_A 1_(s,L] r`, Cauchy–Schwarz gives `nu(r) >= (E[1_A integral_s^L |r|^2]/P(A))^(1/2)`. For the upper bound, `(integral f)^2 = 2 integral f(s) integral_s^L f`; the partition argument proves `E integral |r|^2 B <= ||r||_*^2 E B_L`, and `B = (epsilon + integral_0^t |w|^2)^(1/2)` gives the factor `sqrt(2)`.
2. **Nonexactness example:** with `m = p(1-sigma_c)`, the difference between the squared test ratio and `||r||_*^2`, multiplied by `(sigma_c+m)^2/m`, is exactly `sigma_c^2(1-sigma_c) - sigma_c^2 m - m^2(1+sigma_c)`; the symbolic bound on `p` makes it positive.
3. **Mixed-gain equality:** independent shifted blocks have i.i.d. leading energies, while cross-tails are bounded only by Minkowski and the EMS slab sum. The order is fixed: `N -> infinity` for fixed window length, then the window length increases.
4. **Dilution lemma:** substituting the chosen `y*` gives `-sqrt((rho^2 Y - Z)(gamma^2-rho^2))/rho`; the other branch gives at most `(gamma^2-rho^2)/gamma` times `sqrt(Y)` loss. The strategy stops on the AHEAD event and otherwise appends an independent future dilution train, with parameters chosen in the order `rho`, wait time, window, block count.
5. **Gate-I AHEAD:** a unit deterministic pulse gives `X1 > 0` almost surely; on a positive-probability later Brownian tube the free-decay output energy exceeds any fixed finite threshold. Because the RMS gain is finite by EMS, this already proves AHEAD relative to `G2`; only its numerical identification uses gate I.

## Named cuts and remaining problem

- **NR-GATE-I-WHOLE-V21:** the 284-LF v21 proof is not supplied in v220. All gamma-star value statements remain conditional; the general theorems and the gate-I AHEAD construction do not depend on it.
- **NR-HISTORICAL-V14:** v29's historical lower citation stays at the earlier v14 boundary; v31 supplies the current independent lower proof. No backdating.
- **NR-V15:** v32's consistency remark about the earlier v15 family is not a proof of that whole source.
- **NR-LARGER-FILTRATION-BSD:** Theorem A is filtration-general, but the two-process BSDE descriptor applications remain on the canonical one-Brownian filtration.
- **NR-POLICY / CP:** no common causal/stationary printed controller, internal EMS, prescribed-gamma synthesis, or application of the risk value to unpriced non-E1 controls outside CP.

Open value-side problems include the exact adapted quotient, the best constant in `(1, sqrt(2)]`, exact actuated descriptor values, the exact gate-I literal gain in `(G2, sqrt(2) G2]`, a structural classification of AHEAD from general matrices, and any controlled analog of v31/v32. The original synthesis problem remains open.

## Process and assurance boundaries

Review A carries its specific earlier preview-review contact and its original SPR primary findings; Review B carries its specific earlier preview contact and the full 43m50 idle gap. All author findings, the v182 self-release MAJOR, post56/post60/postS126 ZERO guidance, the protected S242 window, HELD_C889 and parent transport/exposure findings remain permanent. The later owner candidates v33–v38 are not part of this freeze and are not adopted.

Only written all-variable reasoning plus file/hash/LF/clock metadata were used. N4 remains UNKNOWN with historical child exit unestablished; auxiliary214 STOP and the scientific HOLD remain. Same eighteen owners, science cutoff **2026-10-27T11:05:38-07:00** and delivery **12:35:38-07:00** are unchanged. No early final park, round closeout, formal/human/configured-family/executable or novelty acceptance.
