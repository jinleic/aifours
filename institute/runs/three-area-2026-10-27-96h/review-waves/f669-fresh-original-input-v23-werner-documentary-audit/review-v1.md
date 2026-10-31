# f669 — original-input v23 Werner documentary comparison

**Role and outcome.** DOCUMENTARY_ONLY. The v23 physics-1 row accurately represents the supplied operative Werner disposition and status erratum at the specific scopes identified below, subject to **one MINOR notation/quantifier clarification**. Findings: **0 FATAL / 0 MAJOR / 1 MINOR** in this documentary scope. This is not an independent mathematical reconstruction, scientific acceptance, or a blanket audit of v23.

**Native observation before report creation:** 2026-10-30T15:38:52-0700 PDT. This observation is not a claimed start time or a claim of continuous supervision.

## Exposure, order, and coverage

I read manifest LF 1–271, freeze receipt LF 1–151, parent-live-metadata supply LF 1–266, actual dispatch receipt LF 1–19, and all 20 manifest-listed status controls through their endings. I then sent Main a **direct pre-body ACK** at the observed 2026-10-30T15:36:51-0700 PDT, before accessing the packet. The ACK described this documentary-only role and the status-only exclusions; no mathematical or documentary conclusion was formed from the administrative text before that ACK.

I subsequently read the complete **645-LF** packet, sequentially, raw and in windows of at most 20 LF, through its ending S10 LF 20. The packet contains its two introductory lines and complete bodies S1–S10 as listed below. The long report lines were displayed raw; I observed no elision requiring recovery. My live metadata hashes matched the supplied manifest (`0233ff6f2f4e514ee493040919864841ee4fbc9a88622588631b04cad3cf2a67`), freeze receipt (`2ac63dfe76d1d8b0950d92e145a566e60753c6f0950930899d68ea7088e991c5`), and packet (`3d3624aa9dd3cef6b0f3f6867738466e058b08e7d49f09d9753fc2c706855fde`). The single packet is recorded as 136226 bytes. The freeze receipt asserts selected-lines byte equality and source-hash stability; the parent metadata asserts all assigned bindings matched before dispatch. I did **not** independently re-render the packet or rehash the ten original source files: the source pins and their selected-line correspondence below are those supplied by the parent records, not a separately performed verification.

Source paths below are relative to `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`; LF numbers are original source LF as labeled in the packet. SHA-256 values are the frozen whole-source pins, not hashes independently remeasured by this auditor.

| ID | Complete assigned source and LF | Frozen whole-source SHA-256 |
|---|---|---|
| S1 | `rolling-report-20261030-v22.md`, 1–42 | `6fc2b2083ed5079dfef232cd88b6345b89b5f9492bfbd084d1560db540b8050a` |
| S2 | `rolling-report-20261030-v23.md`, 1–42 | `4f57af6f20038982148d975298ba39596c9968ca129551e05505bf3d14c1c4e2` |
| S3 | `rolling-report-20261030-v22-delta-documentary-audit-outcome-v1.json`, 1–65 | `407b84b35354c9d4a93541b689ebdd2c633a38a50e0f29d2811eed6a12fbeae8` |
| S4 | `rolling-report-20261030-v23-parent-render-and-source-bindings-v1.json`, 1–171 | `2ecd933ed14f86813f6eb967518b6dd21d5ddb4187a8cb1fb44ddcfa754ab89e` |
| S5 | `checkpoints/132-deficit-six-partial-eight-ame24-and-false-core-premise-v1.json`, 1–186 | `ca502da37aba52f4f43866dadd03e42ced81ddfcc6248f261ffacf2aee2cbf4f` |
| S6 | `dispositions/physics-1-actual-core-gram-counterexample-and-rank2-sufficient-regions-parent-v1.md`, 1–67 | `2c27f551e31eb0b366804926d06ec2a604b131b510da52d9261c0d4956cc0859` |
| S7 | `dispositions/physics-1-rank2-dual-equivalence-and-core-gram-conditional-parent-v1-erratum-1.md`, 1–9 | `b5ae93fcac492b4a19830d699a504e84674deecc49ee9655d2a90e62a8fa4317` |
| S8 | `review-waves/f649-werner-coregram-actual-frame-and-physical-pair-independent-exact-finite-author/parent-independent-finite-run-v1-receipt.json`, 1–33 | `e06fcaab0af8e023890431e7dc8c7a99a030746d997486d35ba02808ed94c3ad` |
| S9 | `parent-ledger-core-gram-pipe-rendering-correction-v1.json`, 1–8 | `489b0d5e0ffd64bdac1f0778fa6cfc29c6fd7b7b5b2e36bb406bc3a9cbff32ec` |
| S10 | `dispositions/physics-1-rank2-dual-equivalence-and-core-gram-conditional-parent-v1.md`, 1–20 | `5c9e3f6d05d7f28cadc3c25e1b5d66a4a78b129bd53ad9c25b8ebd84946ce3f7` |

The following verdict words mean **agreement or disagreement of the report with these supplied documents only**. They do not independently certify the correctness of the mathematics or of a reported historical execution.

## Claim-by-claim findings

### 1. Changed status, actual object, and strict Q margin — SUPPORTED

S1 LF 23 called CORE-GRAM unproved in the earlier v22 snapshot, observed at 15:12:40 (S1 LF 3). S2 LF 23 updates the v23 row to say the universal sufficient CORE-GRAM premise is **false**, even with strictly positive diagonal gaps. S6 LF 3, 7–18, 20–32 and S7 LF 3–5 support that update as a statement of the supplied later disposition and additive status erratum. S3 LF 62–64 expressly excludes later results from its v20→v22 documentary coverage. Thus the old text is historical as-of its own observation; the later result is not backdated into it.

The specified object is the **actual** d=4 doubly-orthonormal frame, not an abstract negative scalar or a different physical pair. S6 LF 7–13 defines, in `C^4 ⊗ C^4`,

- `a = (4|00⟩ + 2|11⟩ + 2|22⟩ + |33⟩)/5`;
- `u1=|01⟩`, `v1=−(6|01⟩+8|02⟩+|10⟩)/sqrt(101)`, `u2=v2=a`, and `x_i=|u_i⟩⟨v_i|`;
- the associated actual rank-two operator `R=x1+x2/sqrt(101)` (S6 LF 20–23).

The disposition reports `p1=1/404>0`, `p2=168/625>0` (S6 LF 15), `G(R)=−203/63125`, and `q(R)=143531/126250 < 255000/126250=2||R||²` (S6 LF 30–32). Those are the same quantities and signs represented in S2 LF 23. **The reported operator satisfies Q strictly:** the cited negative G is a counterexample to the sufficient CORE-GRAM premise, **not** a counterexample to Q or to physical T2. The report's explicit negation of a Q/T2 counterexample is supported by S6 LF 3, 32–34 and S7 LF 5. These are literal source comparisons, not a fresh computation of the displayed frame.

### 2. Conditional implication, universal residual, and original target — SUPPORTED

S10 LF 7, 11 records the prior **double-universal** Q/T2 equivalence and the conditional `CORE-GRAM ⇒ Q ⇒ T2` chain; S7 LF 3–5 and S6 LF 3 state that falsifying the premise does not refute the implication. S2 LF 23 preserves this distinction, marks the premise false rather than still open, and says universal Q/T2 and original q3/T3 remain OPEN. S6 LF 47–51, 67 supplies the corresponding exact residual and assurance boundary. The status of an unproved universal conclusion is not a demonstrated counterexample or target closure.

For exact identification of the unpaid residual, S6 LF 38, 47–51 says that for a **given actual frame**, Q on its whole complex span is equivalent to

`|C12 − conjugate(c1)c2/2|² ≤ (1 − |c1|²/2 + 4p1)(1 − |c2|²/2 + 4p2)`.

The unpaid task is this inequality over the remaining actual frames, particularly those not already covered with `q1+q2>2`; the source identifies the all-frames quantification with Q and, via the separately adopted double-universal duality, T2 for **all traceless physical A,B**. This is not a claim that one fixed physical pair is equivalent to all frames. S2 LF 23 describes the determinant inequality as remaining unpaid rather than presenting it as proved.

### 3. Full-span, singular-weight, and physical-pair sufficient criteria — SUPPORTED with MINOR clarification below

**Full actual-frame span.** S6 LF 38–43 defines `q_i=q(x_i)` and states, for every actual doubly-orthonormal frame and every complex `z1,z2`, that `q1+q2≤2` suffices for Q throughout the entire span of its two dyads. S2 LF 23 preserves both the actual-frame and entire-complex-span qualifiers. The source says this is a sufficient region, not an iff characterization or universal coverage. S6 LF 43 also qualifies the strict enlargement as a union with named earlier rank-one/traceless/EP/`C12=0`/common-local-qubit classes; it does not say this single region contains all of them.

**Singular-weight ratio.** S6 LF 45 gives a distinct sufficient condition for actual ordered SVD weights, `s1≥s2≥0` and `s2/s1≤3−2sqrt(2)`, including its boundary. It is sufficient, not necessary. S2 LF 23 preserves the displayed threshold and calls it separately sufficient; it does not present this as an unrestricted theorem. The clarification in Finding M1 is needed to make its object and quantifiers explicit.

**Physical pair.** S6 LF 53–57 states a different condition on **traceless complex 4×4 A,B**, with `X=A⊗I+I⊗B`, `L=||A||²+||B||²`, and actual singular values of X: `sigma2(X)/sigma1(X)≤1/sqrt(3)` suffices for `S2(X)≤2L`, with the zero case and equality boundary included. This is not a ratio of the dual operator's weights and not a criterion on every dual frame. S2 LF 23 labels it a physical-pair condition and reports an explicit open class beyond separately-2+2-reducing pairs. As the source's literal example, S6 LF 57 uses `A=B=M=D+N/10`, `D=diag(3,−1,−1,−1)`, `N=E01+E12+E23`, with an open neighborhood. S6 does not claim that this pair lies outside **every** other known physical class or is novel. No new pair or case was selected in this review.

**M1 — MINOR, notation/quantifier clarity, S2 LF 23 versus S6 LF 45.** In the v23 row `s1,s2` are not defined, and the short statement of their ratio immediately follows the whole-span criterion without explicitly saying that these are the ordered singular weights of the particular actual rank-two operator under consideration. A reader could transfer the whole-span quantifier to the separate weight-ratio condition or confuse it with the physical-pair `sigma` ratio. This is an omission/ambiguity, **not a demonstrated false claim or a mathematical refutation**. Recommended additive wording: “For an actual rank-two operator with ordered singular weights `s1≥s2≥0` and the ratio defined, the separate condition `s2/s1≤3−2sqrt(2)` is sufficient for Q, including equality; it does not by itself assert Q on the entire span of an arbitrary frame.” Keep the distinct physical-pair zero case and equality boundary as S6 LF 55 states. This recommendation merely makes the supplied source scope explicit.

### 4. Complex coefficient and historical real-part identity — SUPPORTED

S6 LF 13, 18 and S7 LF 7 specify `c_i=Tr(x_i)` and `C12=⟨Tr_B x1,Tr_B x2⟩+⟨Tr_A x1,Tr_A x2⟩`, with the Hilbert–Schmidt inner product conjugate-linear in its first argument. In the Hermitian polarization the coefficient multiplying `conjugate(z1)z2` is **`conjugate(c1)c2−C12`**. S2 LF 23 reports this corrected coefficient.

S10 LF 11 retained `Re(c1 conjugate(c2)−C12)` in the real nonnegative singular-weight identity. S7 LF 7 expressly says the old real-part scalar expression remains correct in that real-weight setting because the two conjugate trace products have the same real part; it warns that this does not license transposing conjugation in a complex-phase calculation. S2 LF 23 preserves this distinction. S6 LF 18 and S7 LF 7 separately say the supplied **real** witness also violates the literal historical CORE-GRAM inequality. No new polarization calculation was performed here.

### 5. f649 one-shot, seven named controls, and runtime — SUPPORTED as reported metadata; underlying source execution not independently checked

S2 LF 32 calls f649 an independently authored one-shot with `.060969s`, actual 16×16 frame and physical-pair arithmetic, and disclaims universal proof. S8 LF 2–7 reports `PASS`, one run, exit code 0, and `elapsed_seconds=0.060969374999403955`; S8 LF 26–30 records 0-byte stderr; S8 LF 32 describes the scoped actual-frame/16×16-R and physical-pair checks and excludes universal Q/T2, external family, human, kernel and novelty. S6 LF 63 records the parent’s claim of a full pre-GO source read, one isolated Python run, empty stderr, and cooperative 54-second/external 55-second deadlines. These are **historical parent statements**, not actions performed by this auditor.

S6 LF 65, not the narrower S8 receipt, reports **seven named-reason mutations** discriminating: (1) core sign, (2) complex conjugation, (3) trace order, (4) frame orthogonality, (5) a falsely asserted Q violation, (6) physical normalization, and (7) a reducible diagonal comparison. The receipt itself does not enumerate those seven or independently establish their individual outcomes. Neither source is a universal Q/T2 proof, a physical T2 counterexample, a kernel certificate, or independent-family review. I did not follow the checker, GO, stdout, author, or review links and did not execute or replay any scientific code.

### 6. Parent rendering correction and v23 as-of scope — SUPPORTED as parent-recorded metadata

S9 LF 4–7 says the new CORE ledger row had absolute-value pipes that Markdown would treat as separators, and those bars were replaced by equivalent `abs(...)` notation in the same new row before the next render receipt; it claims no mathematical-text or earlier-row change. S2 LF 40 describes that correction. S4 LF 46–65 and S5 LF 23–29 report the parent's subsequent rendering/navigation and 333 data-row metadata, while S4 LF 55, 170 explicitly does **not** assert fragment validation or independent scientific reproof. I did not rerender the ledger or verify local links.

S2 LF 1, 3, 42 labels v23 NONFINAL and requires its own changed-scope documentary audits; S3 LF 28–64 confines the v22 outcome to its listed v20→v22 scopes. S2 LF 7 and S5 LF 184 disclaim human/family/kernel/novelty and final-settlement credit. S4 LF 15–24 identifies changed report lines 1, 3, 18, 23, 28, 32, 40 and 42; this review's scientific comparison is limited to the **Werner physics-1** material and directly associated evidence/status, not other changed science or all eighteen slots.

### 7. Later quarantines and temporal qualification — SUPPORTED as status-only controls

The v23 report's native observation is 15:26:21 PDT (S2 LF 3); checkpoint132 is observed at 15:26:34 PDT (S5 LF 3). The status controls supplied before this review record separate later holds at f654 15:26:58, f653 15:27:53, f659 15:31:48, f660 15:34:34 and f662 15:35:48 PDT. Their **entire stopped episodes and all proof/method/selection/planning/verification/reporting/confidence/downstream consumers remain HELD/ZERO/NONINPUT**, not just selected fragments. No mathematical or documentary finding about v23 follows from any stopped episode. The controls say future report/checkpoint disclosure is needed; neither v23 nor checkpoint132 is to be retroactively rewritten as if those later events had already occurred. References to f652–f655 being active in the earlier snapshot (S2 LF 32; S5 LF 179–182) are not a representation of their current status after these holds.

All other listed quarantines remain at their stated scope. This review uses their records for status only, not their payloads, methods, outcomes, or confidence consumers. No stopped worker's role was widened, no held science was resumed or salvaged, and no clean-cognition certificate is asserted.

## Unpaid and excluded

- **No scientific reproof or source authentication:** S6/S7/S10 are compared as supplied; their linked author/reviewer bodies and mathematical imports were not followed or independently reconstructed. Parent-reported reviewer counts and finite-check assertions remain parent-reported.
- **No unrelated changed-science verdict:** v23 Olson, AME and other changed slots, plus unrelated process assertions, are outside this task even though the entire literal packet was read. V22's scoped documentary outcome is not v23 clearance.
- **No scientific execution or fresh case:** no new selected frame/operator/pair/parameter, source code, CAS, solver, enumeration, replay, tests, or scientific executable. No sibling body, stopped f653/f654/f659/f660/f662 episode/history, held payload, prior reviewer body, or linked author code was accessed. The displayed examples above are copied only from S6.
- **No automatic adoption or closure:** Main must fully read and independently disposition this review. This report does not itself adopt the Werner result, clear another gate, prove Q/T2 or q3/T3, establish original-source equivalence or novelty, or claim independent external family, human, or formal/kernel review. It does not assert final deadline settlement or current statuses beyond the supplied controls.
