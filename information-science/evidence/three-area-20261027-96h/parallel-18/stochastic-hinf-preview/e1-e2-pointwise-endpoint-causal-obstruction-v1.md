# E2-to-E1 pointwise endpoint: exact causal regularization obstruction and a positive subclass

**WRITTEN AUTHOR RESULT/OBSTRUCTION, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 18:02:18 PDT 2026**. This does NOT prove the full endpoint implication and does NOT give a physical counterexample. It supplies an exact missing step with universal actual-input identities and a separately proved transfer subclass. No deterministic-reference/calibration or stopped controller method is used.

## 1. Exact release/order, inputs and question

The entire S0 and release `info-3-e1-e2-pointwise-endpoint-release-v1.json` (live SHA `7f94e11b6ef89380506b127a354a372e041c30641d96c82a72b46706c89616ef`) were read first. The actual pre-body ACK was written at **17:55:00 PDT** and pinned BEFORE source bodies/new mathematics: `e1-e2-pointwise-endpoint-prebody-ack-v1.json`, SHA `95b92eca7fd899e60860e59e330c1c18cd4e51bacb0fc0329500563249669ca9` (19 LF / 4093 bytes).

Every permitted source was then read COMPLETELY after its exact hash matched: class packet `cbf78426d65a0c373cbc11d31d7eda200478025e5beafa4c970ffc86aa358ed7` (37 LF); full output-only E1/E2 source `857ec99cc1be5d4ce2cd204fd7b0b01983d8bb8b3c8e633854b75370fb78da28` (89 LF, raw1–60 and61–89); own STOP/status `0ec88430...` (29 LF) and parent L1 quarantine/status `ba6b4bb9...` (23 LF). The latter two are controls ONLY. No source links or candidate review were opened; release is not adoption.

Fix EVERY allowed real compatible plant tuple, positive dimensions, finite T>h>=0, zero state/history and ONE deterministic stationary linear law

`dx=[Ax+Bu+Cw(t-h)]dt+[A0x+B0u]dW`, `z=D0x+D1u`,

`u=Kx+L0w(t)+Lh w(t-h)+integral_0^h H(r)w(t-r)dr`.

H is deterministic L2; at h=0 combine the endpoints and omit H. Input J=[0,T-h], output I=[0,T], input zero on all other times including (T-h,T]. Filtration is canonical Brownian; input classes are progressive E2 (`E||w||_J^2<infinity`) and progressive E1 (`E||w||_J<infinity`). Controls require ONLY local pathwise L2/nonexplosion in this comparison. Denominator is finite positive E||w|| in both domains. No RMS gain is used.

At the finite COMMON gain endpoint gamma>0, assume the E2 gain is gamma and EVERY nonzero E2 input satisfies the literal strict inequality. The question is whether EVERY E1 input must do so. All following statements quantify the same law/matrices and actual original output, not different controllers for different inputs.

## 2. Reconstruct the used output-domain facts instead of assuming the source adopted

The causal deterministic window map R has pathwise L2 bound `||L0||+||Lh||+sqrt(h)||H||_L2` and preserves progressiveness. For an E1 input define its causal accumulated-energy stops tau_N, capped at T, and `w_N=w1_(t<tau_N)` on J. The total energy is finite almost surely; each stopped input has energy<=N and is an actual E2 input. Same inputs/window terms through a stop give identical actual states/controls there by strong linear-SDE uniqueness. Consistent stopped solutions patch to the unique nonexplosive local strong E1 solution; no global expected state/control energy is inferred.

The finite E2 output-gain hypothesis gives `E||Z(v)||<=gamma E||v||` for EVERY E2 v, including zero by zero initial state/linearity. Also `E||w-w_N||->0` by dominated convergence. On E2, actual strong linearity gives `Z(w_M)-Z(w_N)=Z(w_M-w_N)`, so the stopped outputs are Cauchy in the complete Banach space L1(Omega;L2(I)). The limit is the actual patched output: each path eventually has no energy stop, and stopped uniqueness identifies the whole response. Thus

**E||Z(w)||<=gamma E||w|| for EVERY E1 input**,               (B)

with L1(L2) convergence of the actual stopped outputs. This reconstructs the finite used source claim. Extension/uniqueness also preserves actual linearity on E1. No NR-GAIN/first-moment/state-energy theorem is imported.

Consequently failure of the requested strict transfer could only be an ACTUAL E1 norm attainer: a nonzero w outside E2 with `E||Z(w)||=gamma E||w||`. An E1 ratio ABOVE gamma is impossible by (B). This is an exact reduction, not a claim that such an attainer exists.

Define the finite nonnegative deficit

`D(v)=gamma E||v||_J-E||Z(v)||_I`, for v in E1.

The hypothesis gives D(v)>0 for every nonzero E2 v. The issue is whether D(w) can vanish at an E1-only input.

## 3. Exact causal energy-split identity — why stopped strictness does not pass by density

For ANY E1 w put `r_N=w-w_N`. These two pieces have disjoint TIME supports on each path and remain actual progressive E1 inputs. Write

`a_N=||w_N||_J`, `b_N=||r_N||_J`,

`A_N=E[a_N+b_N-sqrt(a_N^2+b_N^2)]>=0`,

`B_N=E[||Z(w_N)||_I+||Z(r_N)||_I-||Z(w)||_I]>=0`.

The input identity `||w||=sqrt(a_N^2+b_N^2)` is pathwise time-L2 orthogonality. Actual output linearity and the triangle inequality give B_N>=0. All terms are finite by (B). Direct rearrangement, with NO stochastic or norm relaxation, gives the universal identity

**D(w)=D(w_N)+D(r_N)+B_N-gamma A_N.**                        (S)

In particular an endpoint E1 attainer would satisfy

**D(w_N)+D(r_N)+B_N=gamma A_N for EVERY N.**                  (E)

This does NOT imply D(w_N)=0: the input norm is not additive across a time split.

The energy geometry is explicit. Let U=integral_J|w|^2, finite almost surely. Continuity of accumulated energy gives

`a_N=sqrt(min(U,N))`, `b_N=sqrt((U-N)_+)`.

If w is genuinely E1 but NOT E2, then E U=infinity. For EVERY finite N, P(U>N)>0, so A_N>0: on that event both a_N and b_N are positive and their sum strictly exceeds the square root of their squared sum. Also the tail remains outside E2 for EVERY N, because `U<=N+(U-N)_+` forces `E(U-N)_+=infinity`.

Yet `A_N<=E b_N->0` by dominated convergence with the integrable sqrt(U). Thus any such hypothetical attainer has nonzero E2 truncations satisfying

**0<D(w_N)<=gamma A_N->0**,                                 (Q)

while its remainders are never in E2. The upper bound follows from (E), not a guessed deficit value. There is no contradiction with strictness for every separate E2 input, and no uniform positive deficit supplied by that hypothesis. No physical realization of (E) with D(w)=0 is claimed; (S)–(Q) identify the exact unpaid equality case for the actual system.

## 4. Probability cuts do preserve deficits — but the needed cutoff is not licensed

For any event A measurable at the INITIAL sigma field, `1_Aw` is progressive, and zero initial state plus the actual linear SDE give

`Z(1_Aw)=1_A Z(w)`.

For bounded initial factors this follows directly from linearity of time/Itô integrals; local uniqueness extends it to E1. Since probability-disjoint path norms add, the deficits satisfy

**D(w)=D(1_Aw)+D(1_(A^c)w).**                               (P)

Therefore an E1 attainer would give an E2 attainer if it admitted a nonzero initial-event slice with finite second input moment.

That route cannot regularize a genuinely non-E2 input in the completed NATURAL canonical Brownian filtration at time zero: F0 is probability-trivial (W0 is fixed and only null sets are completed). An initial event is zero or one modulo null sets. Its nonzero slice is the same w and still has infinite expected energy. This initial-event no-go is universal, not a chosen input test.

The bounded TOTAL-energy event `{U<=N}` would make the product input square-integrable, but it is a TERMINAL information cutoff. The supplied hypotheses do not make it initial/predictable at every earlier input time, and do not give `Z(1_(U<=N)w)=1_(U<=N)Z(w)`. Multiplying through an Itô integral by an unrevealed terminal factor is not the licensed initial-factor identity. I do not assert that every particular such product is inadmissible; the point is that its required universal adaptedness/actual-output caller is UNPAID. Substituting this terminal cut for the legal causal stop is exactly the invalid proof step to avoid.

## 5. A positive transfer theorem for ALL revealed-amplitude/future-shape inputs

There is a useful nontrivial subclass where the causal caller DOES pay the endpoint. Fix ANY deterministic t0 with 0<=t0<T-h. Let v be any nonzero E2 input supported in [t0,T-h], progressive with respect to the filtration generated ONLY by Brownian increments after t0. Let Y be ANY real F_t0-measurable scalar with `0<E|Y|<infinity`; Y need not have a finite second moment. Put w=Yv.

**Lemma.** The actual output satisfies `Z(Yv)=Y Z(v)`, and

**E||Z(Yv)||/E||Yv|| = E||Z(v)||/E||v|| < gamma.**            (F)

Proof: before t0 the input/control/state are zero. For bounded Y, an initial-factor argument applied at t0 to the actual zero-start equation gives the identity. For unbounded Y, localize its F_t0-measurable magnitude, apply uniqueness on the corresponding revealed-amplitude events and let those events exhaust the space; Y is finite almost surely. This is the same original law and local admissibility, not a controller that simulates different states.

The base v and its actual response can be constructed in the post-t0 Brownian-increment filtration by the permitted strong linear-SDE theorem. Embedded into the original filtration, uniqueness identifies the same response. Hence ||v|| and ||Z(v)|| depend only on those future increments and are independent of F_t0. Brownian increment independence and ordinary factorization of expectations give the equality in (F); the final strict inequality is the E2 hypothesis on the actual base input. All required norms are integrable, and E||Yv|| is finite positive.

If E Y^2 is infinite, Tonelli/independence and nonzero v give E||Yv||^2=infinity; (F) still proves strict transfer for that WHOLE class of E1-only inputs. No particular distribution, parameter, plant or operator is selected/evaluated. At t0=0 canonical initial information makes this an initial-amplitude special case; at any admissible positive t0 it is the general revealed-past amplitude theorem. Neither factorization nor independence is asserted for an arbitrary E1 input.

Thus a counterexample, if one exists, cannot be supplied just by adding an integrable heavy amplitude known BEFORE an independent future input shape starts. This rules out one entire shortcut while proving actual strictness on that positive subclass.

## 6. Exact remaining implication and scope of this deliverable

The full requested implication remains UNPROVED and UNREFUTED here. What is missing is an actual-SDE norm-attainer regularization/equality-case theorem: from an E1-only w with D(w)=0, either produce a nonzero actual E2 input with zero deficit, or rule out the positive energy-split budget (E) by a further property of the actual dynamics. The permitted source's gain equality, output continuity and causal uniqueness do NOT by themselves supply that step. The probability-local regularization identity (P) has no useful initial energy slice in the canonical model, while the legal causal cutoff has the strictly positive budget (E)–(Q). The revealed-amplitude theorem covers only its expressly factored inputs.

These are exact universal actual-object obstructions to the two natural endpoint arguments, not merely the statement that density loses strictness. They are not a physical counterfamily and do not establish that full transfer is false. No abstract selected operator or small-case construction is used to suggest one. Any stronger conclusion needs a new proved regularization/equality-case argument rather than a confidence claim from approximating ratios.

This additive output is the requested first result/precise obstruction at the supplied model. It does not change the original input ratio, introduce a global state/control E1 bound, solve general synthesis, certify book admissibility or adopt the supplied source/w93 review. Zero denominators remain excluded; gamma>0 is the stated finite common endpoint. h=0 and h>0, degenerate/zero matrices and the same controller across all comparisons are covered. If zero gain is paired with a positive gamma there is a common margin and transfer is already immediate, not this endpoint problem.

## 7. Provenance/actions and continuing controls

Only the explicitly listed released sources were opened and used; linked older papers/results were not followed. The used output/localization facts were reconstructed above. Named ordinary facts are linear-SDE strong existence/uniqueness/linearity, causal energy localization, bounded revealed-factor identities from Itô linearity, dominated convergence, completeness/triangle properties of L1(Omega;L2), and defining Brownian independent increments. No strong-Markov, adjoint/dual-risk, stochastic-reference optimization, calibration, controller realization or diffusion-annihilation method is imported.

No selected numeric/operator/state/control/frequency/parameter/sanity probe EVEN PRIVATELY, scientific interpreter/Eval/calculator/CAS/program/enumeration/solver/replay/build/test, external source/model CLI/nested agent, author contact, Git/delete/publication occurred. Metadata native clocks/hashes/counts only. The entire selected-reference episode and consumers, diffusion-annihilation/C1-C3/R4/v209, parent physics-2 L1 episode/all consumers and every prior STOP/HOLD/ZERO/process/cadence/N4 UNKNOWN/aux214 STOP remain. Same retained owner; no clean cognition or stronger verification/novelty/general-target claim.
