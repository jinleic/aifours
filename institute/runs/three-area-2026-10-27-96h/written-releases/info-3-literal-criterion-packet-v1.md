## S1 /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/written-releases/info-3-literal-criterion-controls-v1.md
SHA256 5eaca2843af8d54701b9a8b8d2741d7dd8953a4562ccf00a73dd35d99416cb18
LF1-19 COMPLETE
S1|1|# S1 info-3 — narrow prospective definition-first written release
S1|2|
S1|3|Observed clock before writing: 2026-10-27T14:43:38-0700 PDT. Read this WHOLE overlay BEFORE the supplied definitions. New source/written permission is limited to the exact definition-first prerequisite below. No original STOP is lifted outside it, no candidate adopted, no compute admitted.
S1|4|
S1|5|## Exact task
S1|6|
S1|7|Definition-first on the literal criterion: state the exact admissible disturbance/controller classes you adopt (with the alternatives you do NOT cover), then seek a genuinely new result on the literal synthesis question itself—e.g. an exact universal relation between literal-criterion feasibility and an explicitly defined synthesis condition for a stated plant class, or an exact obstruction showing that some proposed N&S condition cannot hold for the literal ratio. Prior written-supported sandwich/value statements in your envelope may be cited AS STATED there only. A ledger of quantifiers alone, an RMS restatement, or a single selected plant/value is NOT the target.
S1|8|
S1|9|## Input boundary
S1|10|
S1|11|Only this overlay, the supplied problem-definition literals, S0/current contract/own safe intake inputs, and ordinary explicitly named elementary mathematical facts are inputs. The definitions are not a verbatim-book certification unless their provenance says so. No old proof/review/park/checkpoint/scout/metadata-map expansion, legacy candidate, held or withdrawn source, special tested state, private method/selection/confidence guide or ZERO consumer may be used. The corrective packet freeze for old v33–v57, C1–C3/R4 realization STOP, v209 STOP, v248-reported material and all ZERO/HELD consumers remain. Do NOT open the dossier beyond LF19, work/theory.md, old evidence roots, the 2014/2020 comparison papers or any other source in this release.
S1|12|
S1|13|Prior authorship/exposure survives; NO clean-cognition or independent-reconstruction claim. Write an actual pre-body exposure/allowed-input ACK in your new root before drafting a derivation. If the intended method is guided by an excluded episode or an essential definition/import is not supplied, stop that branch and report the exact missing premise. Do not reconstruct protected guidance from memory or a paraphrase.
S1|14|
S1|15|## Deliverable and continuation
S1|16|
S1|17|Write prerequisite-derivation-v1.md ONLY in /Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/stochastic-hinf-preview/. Full original quantifiers, all variables/couplings and degenerate cases, forward and converse actual-object caller, every named import/NR gap, and exactly what is or is not changed. A coordinate restatement/encoding/normal-form proposal alone is NOT scientific progress: seek a materially useful coupling lemma/obstruction, or identify the exact failed implication without claiming the original problem solved. First substantive result/obstruction target<=20min; do not manufacture progress, selected probes or heartbeat loops. Continue the next genuinely admitted all-variable step rather than ending at one file. Science ends only at 2026-10-31T21:23:27.000Z. Main must read complete author sources and actual full-scope peer returns before adoption.
S1|18|
S1|19|Scientific HOLDv2 / N4UNKNOWN historical exit unestablished / aux214STOP / every STOP-HOLD-ZERO-finding persist. No scientific interpreter/calculator/CAS/program/enumeration/solver/replay/build/test/typechecker, selected numeric/control/decimal/boundary probe, nested agent/modelCLI/paidAPI, Git/delete/contact/infrastructure action. Metadata clocks/hashes/file counts only. Same-harness written work is not stronger verification or novelty.

## S2 /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/written-releases/info-3-literal-criterion-definitions-v1.md
SHA256 891ab168ce9b2b0c551dfa35b83ae99acef4b7ca5a1c71420e6d9c19f0633fad
LF1-29 COMPLETE
S2|1|# Source-bound original definitions — info-3
S2|2|
S2|3|Literal canonical-dossier statement of the printed problem, /Users/jinleic/repos/aifours/information-science/stochastic-hinf-preview-control/README.md SHA256 bacb92ff14af3757ffb6e78f11a72fb479460546f3c7a288455c810cf856d1e7, LF1-19 (prefix = source line number):
S2|4|
S2|5|1| # Stochastic H∞ preview control (随机系统 H∞ 预演控制)
S2|6|2| 
S2|7|3| Book: 《10000个科学难题·信息科学卷》 (Science Press, 2011), pp. 674–676 (PDF pp. 695–697), problem by
S2|8|4| 张焕水 (Zhang Huanshui) and 王宏霞 (Wang Hongxia). Page images: [`sources/book/`](sources/book/).
S2|9|5| Work done 2026-10-14 (PT).
S2|10|6| 
S2|11|7| ## 1. The problem as printed
S2|12|8| 
S2|13|9| The system is
S2|14|10| 
S2|15|11|     dx(t) = [A x(t) + B u(t) + C w(t−h)] dt + [A0 x(t) + B0 u(t)] dW(t),    z(t) = D0 x(t) + D1 u(t),
S2|16|12| 
S2|17|13| where W is a Brownian motion and h ≥ 0 is the preview length. For a given γ > 0, find a full-information
S2|18|14| controller u(t) = F(x(t), w(s) | t−h ≤ s ≤ t) such that
S2|19|15| 
S2|20|16|     E‖z‖_{L2[a,b]} / E‖w‖_{L2[a,b−h]} < γ,    with ‖f‖_{L2[a,b]} := (∫_a^b f(t)ᵀf(t) dt)^{1/2}.
S2|21|17| 
S2|22|18| Both the finite horizon (a, b bounded) and the infinite horizon (b → ∞) are asked for. The book asks
S2|23|19| for necessary and sufficient (N&S) solvability conditions and the controller.
S2|24|
S2|25|The criterion is the PRINTED expectation of pathwise L2 norms (an L1(Omega;L2) ratio), NOT the mean-square/RMS Hilbert replacement. Adaptedness, zero initial state, disturbance window/zero-extension, strictness and the controller information pattern are INTERPRETATIONS to be stated explicitly, never silently imposed.
S2|26|
S2|27|## Provenance and limits
S2|28|
S2|29|The quoted lines are the 2026-10-14 canonical dossier transcription of book pp.674–676 (page images exist; not re-read by Main). An earlier scout display past LF19 incidentally included the dossier's later theorem opening; that material is NOT supplied and is NONINPUT here. This packet certifies no book-image equivalence or result.
