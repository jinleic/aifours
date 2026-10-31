# Book pp.674–676: literal criterion compared with the admitted interpretation

**LOCAL SOURCE-COMPARISON RECORD, NOT A SCIENTIFIC THEOREM.** Actual native prewrite observation: **Tue Oct 27 15:37:24 PDT 2026**. Owner InfoHinfPreview-2, info-3. The scope is exactly the three supplied original page images and the supplied dossier/S1 excerpt, not the full volume, linked papers, historical proof corpus or current state of the art.

## 1. Actual order, full visual coverage and pins

I reread the entire S0 and entire frozen audit manifest before writing `book-literal-prebody-ack-v1.json` at the actual **15:34:57 PDT** observation, BEFORE opening any image or making this new comparison. ACK SHA-256: `0f009de6cb1f1c0d98efee05c9302a0a7c16f5eb410c20bb424d24da15e7949a`.

All exact image hashes were observed and matched before visual inspection. I then visually opened the complete images in printed-page order **674, 675, 676**, including each page's end, and reread the complete 55-LF supplied comparison packet. No OCR, underlying PDF, other book page, original dossier beyond its supplied excerpt or bibliography item was opened. Visual reading of these supplied pages is not an independent-human or cross-model transcription audit.

| Actual admitted input | SHA-256 observed | Scope |
|---|---|---|
| `written-releases/info-3-original-book-literal-audit-v1.json` | `f2a8341a54192239c0dd3b1ea34cc58430f88b7e92f977c9a9c157ac7dc615bd` | Entire manifest |
| `public-sources/preview-book-literal-pages-pin-v1.json` | `139dea77718d6d15d12836ebb814ad0bfca4bf380973d6a28fbba965c49192b5` | Entire provenance/guard qualification |
| `public-sources/source-book-preview-0695.png` | `bfbd0a13408bdf814add703c911f56323867d38d3271c7101b6c3ba91ca375e7` | PDF p695 / printed p674; 346937 bytes |
| `public-sources/source-book-preview-0696.png` | `f2e84bd77d6e38d23b3f598edacdebcd7648a37ba8148f9207be87b8ed70624b` | PDF p696 / printed p675; 454740 bytes |
| `public-sources/source-book-preview-0697.png` | `ddbf1cea4f9c17a2a43c4a766f86fff012411f47e053f47e56987a18ebcc8a90` | PDF p697 / printed p676; 282151 bytes |
| `written-releases/info-3-literal-criterion-packet-v1.md` | `888307a4a094bc5fa7aca45484334f8a12b75e9fb3e86259d81acf31cad629f3` | Supplied entire 55-LF controls/dossier excerpt; no source-link expansion |

The PDF path/hash/edition are attributes reported in the provenance record; I did NOT independently open or hash the underlying whole PDF. The image page headers visibly identify the printed page numbers.

## 2. Minimal literal transcription of the mathematical question

**Printed p674, section 2, norm-definition paragraph:**

`||f||_(L2[a,b]) := [ integral_a^b f(t)' f(t) dt ]^(1/2)`.

The paragraph states a,b are real, the prime denotes transpose, and the matrix operations involved are assumed compatible. I do not infer additional dimensions or regularity declarations from that statement.

**Printed p674, equation (1), at the bottom:**

`dx(t)=[A x(t)+B u(t)+C w(t-h)]dt+[A0 x(t)+B0 u(t)]dW`,

`z(t)=D0 x(t)+D1 u(t)`.

Immediately below, the text asks, for a given gamma>0, to find a full-information controller (the phrase “寻找全息控制器”).

**Printed p675, equation (2), at the top:**

`u(t)=F(x(t), w(s) | t-h<=s<=t)`.

**Printed p675, equation (3):**

`[ E ||z||_(L2[a,b]) ] / [ E ||w||_(L2[a,b-h]) ] < gamma`.

The accompanying text explicitly identifies x,w,u,z as state, external disturbance input, control input and regulated signal; h is a nonnegative real preview-window width, W is Brownian motion, and E is mathematical expectation.

**Printed p675, note immediately after (3):** finite a,b give the finite-horizon problem; b tending to infinity gives the infinite-horizon problem. The actual strict sign is `<`, not `<=`.

These displayed formulas contain NO displayed supremum and NO squared-norm expectation or square root of an expected squared norm. The norm's square root is INSIDE each expectation. This confirms the dossier's literal expected-path-L2 ratio rather than an RMS/Hilbert replacement.

## 3. Comparison with the supplied dossier excerpt

| Item | Visual comparison at exact scope |
|---|---|
| Plant and regulated output | Dossier source LF11 / packet S2 LF15 matches printed p674 eq.(1), including w(t-h), state/control diffusion, and D0x+D1u. Typographic prime-versus-transpose notation is equivalent in the norm definition. |
| Broad full-information arguments | Dossier LF13–14 / packet S2 LF17–18 matches p674 final question and p675 eq.(2): current x and disturbance values across t-h<=s<=t are explicitly displayed. |
| Ratio and intervals | Dossier LF16 / packet S2 LF20 matches p675 eq.(3), including expectation OUTSIDE each path norm, output [a,b], disturbance [a,b-h], and `<gamma`. No supremum is printed in either excerpt or source equation. |
| h and W | Nonnegative preview width and Brownian W are explicitly identified below p675 eq.(3), consistent with the dossier summary. |
| Both horizons | Dossier LF18 matches the explicit note on p675. This is not merely an inferred limiting case. |
| N&S wording | The p674 background explicitly refers to “控制器的充要条件” (necessary and sufficient conditions for controllers). The formal question itself is the given-gamma/find-controller statement around eqs.(1)–(3). Dossier LF19 is a prose summary of the N&S goal, not an additional verbatim formally quantified theorem. |
| Scope of this confirmation | It authenticates the displayed model/law/ratio/horizon transcription against THESE images. It does not authenticate the old dossier's later theory, any historical proof or all original model conventions. |

Two precision distinctions matter for the packet's S2 LF25 statement that various matters are interpretations: the **broad x/window arguments** in eq.(2) and the **literal strict sign `<`** in eq.(3) are actually printed. What remains interpretive is the technical implementation/admissibility of that information and the all-input/pointwise-versus-common-margin quantifier convention, not whether the window or strict sign appears.

## 4. Printed declarations versus the explicit research interpretation

Every “not explicitly specified” entry below is LIMITED TO THESE THREE INSPECTED PAGES. It is not a claim about the entire book, cited literature, usual H-infinity conventions or all possible interpretations.

| Topic | Literal status in printed pp674–676 | Status of the currently bound research choice |
|---|---|---|
| Probability filtration/completion | W is called Brownian motion; a filtration, completion and its relation to information are not explicitly specified in these pages. | Completed canonical Brownian filtration is an adopted interpretation. The pages do not separately formalize the covariance/dimensional convention. |
| Disturbance measurability/adaptedness | w is called external disturbance input; progressive/adapted/predictable definitions are not explicitly specified in these pages. | Canonical progressive inputs are an explicit choice. |
| Disturbance moment class | E||w|| appears in the ratio, but an E2 or E1 admissible process-space definition is not explicitly specified in these pages. | The released main comparison uses E2; the new E1 comparison-domain theorem does not certify the original source domain. |
| Nonzero denominator | Zero-input exclusion and a convention for zero/infinite denominator are not explicitly specified in these pages. | Finite positive E||w|| is required in the proved gain problems. |
| Initial state/history | Zero initial state and zero disturbance history are not explicitly specified in these pages. | Zero state/history is an adopted hypothesis, not established book wording. |
| Zero extension | Extension of w outside [a,b-h] is not explicitly specified in these pages. | The chosen zero extension is a research interpretation. |
| Finite interval geometry | a,b finite and h>=0 are stated, but a separate condition b-h>a is not explicitly specified in these pages. | T>h>=0 ensures a nonempty positive-measure disturbance interval in the bound finite-horizon problem. |
| Universal disturbance quantifier | The text says to find a controller making (3) hold; an explicit formula “for every nonzero progressive E2 w” is not printed in these pages. | That universal quantifier is stated explicitly in the research interpretation. I do not deny a conventional H-infinity reading; I do not certify it as literal process-space wording. |
| Pointwise versus uniform strictness | `<gamma` is explicit; whether one common margin below gamma is required over all inputs is not explicitly specified in these pages. | Pointwise strictness and uniform G<gamma remain separately tracked. |
| Controller functional class | Eq.(2) explicitly displays F of current state and the whole disturbance window; linearity, K/taps/L2-kernel form and regularity/growth definitions are not explicitly specified in these pages. | The deterministic stationary linear two-endpoint/L2-kernel class is a deliberately bound subclass, not source-equivalent general F. |
| Controller private information/memory | No additional argument is displayed in eq.(2); a formal allowance/exclusion of private randomness, Brownian history or internal memory is not explicitly defined in these pages. | No extra Brownian history/private randomness/memory is the chosen implementation rule. |
| Well-posedness/nonexplosion/control integrability | Strong solution, nonexplosion and expected/pathwise control-L2 admissibility definitions are not explicitly specified in these pages. | These are proved or assumed explicitly in each research theorem; the source comparison cannot pay them for an arbitrary F. |
| Matrices/parameters | The displayed matrices are unparameterized by t and matrix operations are assumed compatible; their dimensions and a formal admissible coefficient class are not enumerated in these pages. | Fixed compatible finite real matrices are the explicit bound class; no unrestricted coefficient-domain equivalence is inferred. |
| Horizon scope | Both finite and b->infinity problems are explicitly stated. | The new adopted physical gap and newer linear-class candidates are finite-horizon results, not solutions of the infinite-horizon task. |

## 5. Scientific scope preserved, no method mining

The supported fixed-law progressive-versus-deterministic gap remains supported ONLY at its bound zero-state/history, canonical progressive E2, finite-horizon, fixed linear preview-law interpretation. Formula agreement does not promote that result into existential synthesis, all source controller/admissibility conventions, infinite horizon or an exact literal gain.

The general original task remains unresolved. This audit pays a narrow displayed-transcription check that was previously only a dossier import; the unresolved technical interpretation/domain equivalences above remain explicit. It does not certify a book-wide absence of definitions or authorize consulting cited sources.

As required for whole-page visual inspection, the surrounding background/method discussion and bibliography on pp675–676 were visible. They are NOT transcribed or consumed as scientific method/selection/confidence guidance in this audit or a later proof. No reference was followed. Historical statements in those pages are not used as present-day SOTA or novelty evidence. Old stopped/held/withdrawn/zero material remains NONINPUT.

## 6. Source-render guard qualification and local rights boundary

The complete provenance record explicitly qualifies its imaging guard: the pre-render no-overwrite shell guard checked unpadded `-695/-696/-697` filenames, while pdftoppm emitted the actual zero-padded `-0695/-0696/-0697` paths. Therefore that guard did NOT establish absence of the actual output paths; pre-existing-output absence is UNESTABLISHED. The currently observed images are retained and their hashes matched, but neither an overwrite nor no overwrite is asserted or reconstructed. The parent-owned new directory is not a filesystem access census.

The original volume and these pages are local copyrighted source. The directory name `public-sources` is not a publication/license grant. No image was copied outside the authorized roots, no full PDF or other page was opened, and no publication/contact/push/deletion occurred. Only the requested minimal literal transcription/comparison is written in this exclusive owner root.

No scientific calculation, OCR, CAS, enumeration, solver, replay, build, test, nested agent, external model CLI, formal/kernel/human/configured-family/novelty verification or source-wide proof is claimed. All existing STOP/HOLD/ZERO/process findings, N4 UNKNOWN historical exit and aux214 STOP persist.
