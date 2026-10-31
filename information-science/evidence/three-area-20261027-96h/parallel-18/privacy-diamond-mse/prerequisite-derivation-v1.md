# MDA printed-primary correspondence: all-law coupling and the first unpaid objective edge

Owner InfoResearch96h-2, SAME info-1. Actual native clock immediately before writing: **Tue Oct 27 14:45:09 PDT 2026**. **AUTHOR-WRITTEN, UNREVIEWED** under the narrowly frozen S1 release. This is a source/model correspondence and a written all-variable coupling/obstruction, NOT a new proof of LAW642, an external-source equivalence clearance, novelty or stronger verification.

## 1. Inputs, actual coverage and noninputs

Pre-body exposure ACK was written at 14:41:18, before the new definition packet or primary body was read and before this derivation: `pre-body-exposure-ack-v1.json`, SHA256 `568f21a2919f85fd452d8994af589badaf415908d89320f6722840791bbd5532`, 29LF/4261B. Prior authorship and source contacts remain; no blindness, clean cognition or independent-model reconstruction is claimed.

Controls: `info-1-mda-primary-controls-v1.md` (19LF, `2f7f08bbec42ed5e1bb733a90d3fb01b0a188eff9cbf81bbda564e91be4caff3`); release `info-1-mda-primary-release-v1.json` (37LF, `ffe762273ffb118ada58895b08b4cebcab938b6eb3bc9ba74aff565b277f5deb`); complete packet (35LF/5723B, `01699abc42edd112ad2bd6bf782332fc87831ceee41c0d330e05b167455e44e1`); complete equality receipt (11LF/451B, `cd5742126e2b0624deb90dcb6836cb2381d5a6544aa3f65f38542378c6852446`). The packet binds Main's definitions, not a printed-source theorem by itself.

Admitted primary actually read: James Melbourne, Mario Diaz and Shahab Asoodeh, *Optimality of Staircase Mechanisms for Vector Queries under Differential Privacy*, **arXiv:2601.14597v1**, served versioned HTML `https://arxiv.org/html/2601.14597v1`. Main's retained native response pin was checked: `6fbdda7381be0daec59aadf3b22954031ad8111cc0a49f1a8735281417336781`, 3762LF/892541B. The fresh served reader is `artifact://41287`, SHA256 `d2c986cb8d53a000259a3b4587833002d703481ab5c72481ad1d4bc7f122dccb`, 1998LF/1999 logical lines/169478B. Reader conversion is not native-byte equality or proof verification. The version/title/author identity matches the admitted literal; no claim about other versions.

Actual reader coverage: **1–600, 600–636, 816–1046, 1047–1344, 1345–1557, 1558–1809, 1810–1999**, every requested range returned through its ending. This covers the full model, all operative statements, Theorem 6's proof, normalization subsection V-A, and **ALL Appendices A–F through the final Lemma 9 proof/end**. Subsections V-B/V-C and bibliography LF637–815 were not used or read as bodies; no simulation, sampling or numerical figure is evidence here. Appendix B-C's printed illustration was encountered in reading the whole proof, but was not recomputed, quoted or used as a diagnostic premise. Native HTML LF1790–1816 was additionally read to confirm that the Appendix A inequality issue below is present in the native MathML/TeX, not introduced by the reader.

No bibliography link, other paper, old proof/review/park/checkpoint/alternative proof or protected guide was opened. LAW642/NORM148/v241/v253 are status-level comparison targets from the safe envelope only, NOT fresh proof inputs. Original threshold-v2, v214-A, selected checks and all consumers remain ZERO/NONINPUT. Ordinary named facts used below: translation/change-of-variable invariance of Lebesgue measure, Tonelli's nonnegative integral theorem, the Radon–Nikodym theorem and Lebesgue differentiation for norm balls, countable limsup measurability, norm homogeneity/triangle inequality and elementary algebra. These are ordinary analysis imports, not newly formalized library proofs; Appendix A itself explicitly invokes Lebesgue differentiation.

## 2. Exact models and query quantifier

Let `N` be any genuine norm on `R^n`, `n>=1`, let `Delta>0`, `0<epsilon<infinity`, and put `K={h:N(h)<=Delta}` and `C=exp(epsilon)`. Define `F_K` to be ALL Borel probability laws satisfying

`mu(A)<=C mu(A+h)` for every Borel `A` and every `h in K`.

The registered caller is `n=2`, `K=D={h:||h||_1<=1}`, and objective `c(x)=||x||_2^2`, at every finite positive epsilon. Events, shifts and laws remain unrestricted; no radiality is built into `F_K`.

MDA §II-A Definition 1 is dataset-neighbour DP for `M_X(Dataset)=q(Dataset)+X`, with noise independent of the dataset and query dependence only through norm sensitivity. Its equation (5) explicitly imposes ALL Borel events and ALL shifts with `N(h)<=Delta`; equation (7) defines the source density class `M_n^N(Delta,epsilon)` by a pointwise density ratio for all pairs at that distance. Appendix A-C's forward proof explicitly says **for every query with that sensitivity**.

For a fixed actual query `q`, write `K_q={q(D')-q(D):D~D'}`. Translation of the output event proves both directions:

- `M_X` is dataset-DP iff `mu(A)<=C mu(A+h)` for every Borel `A` and every actual difference `h in K_q` (use the symmetry of neighbouring pairs to choose the sign).
- `K_q subset K` therefore makes `F_K` sufficient for that query. Merely knowing `sup N(K_q)=Delta` does NOT assert `K_q=K`, nor by itself prove the converse for every shift in `K`.

Thus the primary's robust **all-shift class** matches the registered privacy quantifier; its introductory fixed-query “iff” must be read at the universal-query/actual-full-shift boundary used in Appendix A-C, not as an automatic theorem that a scalar sensitivity bound fills a query's difference set. Constant/zero-sensitivity queries are not callers of Theorem 6, which assumes `Delta>0`.

## 3. Lemma A — exact all-Borel-law to pointwise-density coupling

**WRITTEN; imports the ordinary measure facts named in §1.** For every `n,N,Delta,epsilon` above, `F_K` equals the Borel laws admitting a finite, strictly positive, measurable density representative `fhat` satisfying

`fhat(x)<=C fhat(y)` for ALL `x,y` with `N(x-y)<=Delta`.

No exceptional shift or boundary point is removed. In particular the source's density restriction does not intrinsically shrink the registered all-law class, provided “a density” means the existence of a suitable representative, not every version of a Radon–Nikodym derivative.

**Forward coupling, full proof.** Let `mu in F_K`; no density is initially assumed. `K` has finite positive volume. Integrating the event inequality over `h in K` and using Tonelli gives, for every Borel `A` of finite Lebesgue measure,

`|K| mu(A) <= C integral_K mu(A+h) dh`

`= C integral_(R^n) |K intersect (z-A)| mu(dz) <= C |A|`.

For infinite-volume `A` the resulting bound is automatic. Therefore `mu(A)<=C|A|/|K|` for all Borel `A`, so `mu` is absolutely continuous and has an essentially bounded Radon–Nikodym derivative. This is an all-variable averaging argument, not evaluation of a selected parameter or state.

Let `B_t` be the open `N`-ball of radius `t>0` and set `f_t(x)=mu(x+B_t)/|B_t|`. Fix ANY deterministic sequence `t_j>0` tending to zero; this is a quantified differentiation sequence, never an executed list of probes. Every `f_t` is measurable and bounded by `C/|K|`. For every `x,y` with `N(x-y)<=Delta`, the original event inequality, applied to the translated ball, gives `f_t(x)<=C f_t(y)` for every `t>0`. Define

`fhat(x)=limsup_(j->infinity) f_(t_j)(x)`.

It is measurable, finite everywhere and equal to the Radon–Nikodym derivative almost everywhere by Lebesgue differentiation. Taking limsup in the inequalities gives the ratio bound simultaneously for every actual pair `x,y`; there is no interchange of an uncountable union of exceptional sets.

There exists a point `z` with `fhat(z)>0`, because its integral is one. For any `x!=z`, divide the line segment from `z` to `x` into `k=ceil(N(x-z)/Delta)` equal parts. Every displacement belongs to the CLOSED `K`; chaining the ratio bounds gives `fhat(z)<=C^k fhat(x)`, hence positivity at `x`. At `x=z` positivity already holds. Thus `fhat` is strictly positive everywhere and represents the SAME law `mu`.

**Converse coupling.** If a probability density `fhat` has that pointwise bound, integrate `fhat(x)<=C fhat(x+h)` over every Borel event, then use translation invariance to obtain `mu(A)<=C mu(A+h)` for every `h in K`. This proves both actual-law directions, including boundary shifts and unbounded events. Null-set changes of the density do not change the law, although arbitrary such versions need not retain the all-pairs pointwise inequality.

**Normalization caller.** The pushforward of `mu` by `x -> x/Delta` has shift set `{h:N(h)<=1}` iff `mu` has shift set `K`; the inverse pushforward restores it. For a squared homogeneous cost its expectation scales by `Delta^2`, including infinity. No endpoint `Delta=0` or infinite privacy budget is claimed. The registered target is the literal `N=||.||_1, Delta=1` caller, not a comparison with a circumscribed Euclidean ball.

This proves a real model bridge at written assurance. It is not attributed verbatim to MDA and does not silently repair or certify its printed proof.

## 4. Lemma B — the cost/shift coupling obstruction, including coordinate changes

**WRITTEN; elementary norm/gauge facts and algebra only.** There is no genuine norm `N` and `Delta>0` with BOTH

1. its exact source shift ball `{h:N(h)<=Delta}` equal to the registered full diamond `D`; and
2. the registered objective `||x||_2^2` of the form `phi(N(x))`, even for an arbitrary function `phi` (therefore not for a nondecreasing one).

**Proof with all variables.** Equality of the balls forces `N(x)=Delta ||x||_1` for every `x`: both sides are the gauge of the same closed ball, using norm homogeneity, with the zero vector included. For arbitrary real `u>0,v>0`, let `x=(u,v)` and `y=(u+v,0)`. Then `N(x)=N(y)=Delta(u+v)`, so a radial objective would have equal values there. But

`||y||_2^2-||x||_2^2=(u+v)^2-(u^2+v^2)=2uv>0`.

This is a symbolic identity for the entire positive quadrant, not a selected numerical state/check. If either component is zero, the difference vanishes; those degenerate axis cases do not remove the contradiction for all positive components required by a function identity on the whole plane. Extended values of `phi` cannot evade it because the target cost is finite everywhere.

The obstruction also survives any invertible linear coordinate change `z=T x`. Exact source shift set `T D` forces `N(Tx)=Delta||x||_1`; transformed objective is `||T^{-1}z||_2^2`. Applying the same arbitrary `x,y` above gives equal source radii and unequal transformed objective. Thus no invertible linear renormalization pays both edges simultaneously. Using `N=||.||_2` instead pays the cost hypothesis but changes the shift ball and therefore the original feasible class. Nonlinear/nonadditive transformations are outside the source theorem, not an escape proved impossible here.

**The first unpaid registered-objective edge is therefore MDA Assumption 1**, not a missing numerical gamma search. Source §II-A explicitly requires `Phi(x)=varphi(N(x))`, with nondecreasing `varphi:[0,infinity)->[0,infinity]`. For `N=||.||_1` it admits squared-`l1` cost, not the squared-Euclidean cost of the registered model. The argument proves a precise failure of theorem application, NOT that the paper cannot have any further implication or that no external source could match.

## 5. Printed theorem/hypothesis correspondence

Reader LF ranges below refer only to the fresh pinned reader in §1. “Printed” means a statement actually present, not a new adoption of every proof step.

| Registered edge | Exact primary anchor and hypotheses | What is paid / not paid |
|---|---|---|
| Query/noise independence | §II-A, Definition 1, equation (4), LF188–213 | Dataset-independent additive noise, with query dependence only through sensitivity. Not a general data-dependent/nonadditive channel theorem. |
| Events and shifts | §II-A equations (5)–(7), LF215–241; Appendix A-C LF960–1046 | All Borel events and CLOSED norm ball. On the full-diamond caller, no missing directed shift. A bound on a particular query's actual difference set is only the sufficient direction unless the actual/all-query premise is paid (§2). |
| All Borel laws vs densities | Theorem 7, Appendix A-A LF829–918; Appendix A-C differentiation | The source asserts all-law absolute continuity and a pointwise version. Lemma A above pays the actual-law bridge at a separately displayed ordinary-analysis cut. The printed Appendix A proof has the specific gap in §6 below; arbitrary density versions are not automatically pointwise DP. |
| Any dimension/norm | §I-C notation; Theorem 6, LF530–545 | `n>=1`, genuine norm, `epsilon>0`, `Delta>0`; registered `n=2,l1,Delta=1` is geometrically allowed. No zero/infinite epsilon or zero-sensitivity endpoint. |
| Cost | Assumption 1, LF291–299; used explicitly in Theorem 6 proof LF549–554 | Nonnegative extended-valued SAME-norm radial nondecreasing cost. `phi(r)=r^2` pays squared-`l1` under diamond sensitivity. Squared Euclidean fails by Lemma B, even after invertible linear reparameterization. |
| Radialization | Theorem 4 §III LF446–457, proof ALL Appendix B LF1047–1344 | DP-preserving rearrangement and domination of `N(X)` as printed. It does not assert Euclidean-cost domination for diamond rearrangement. Theorem 3 uses `d=epsilon ceil(N(x-y)/Delta)` with full closed-step privacy, not Lipschitz metric privacy proportional to arbitrarily small Euclidean distance. |
| Radial density / log condition | Proposition 2 §III LF459–478; ALL Appendix C LF1345–1394 | Radial decreasing representation, and the proof uses **log rho** Lipschitz in the staircase metric. The proposition's sentence says rho is Lipschitz, unlike its Appendix C proof; this textual distinction is not silently suppressed. |
| Maximal-decay restriction | Definition 7, Lemma 1 §IV LF496–518; ALL Appendix D LF1395–1557 | `rho` nonincreasing, lower semicontinuous, nonnegative; normalization/integrability against `r^(n-1)`; `rho(t+Delta)=exp(-epsilon)rho(t)` for every `t>=0`. Lemma 7 supplies the mass-matching parameter in the printed argument; its missing tail-balance justification is in §6. No old alternative proof imported here. |
| Compactness/extreme points | Theorem 5; ALL Appendix E LF1558–1888, Theorems 8–10, Lemma 8, Corollary 1 | Weakly compact convex maximal-decay radial class; extreme points staircase as printed. Uses Krein–Milman, Prokhorov, Lebesgue differentiation, dominated convergence, norm-coordinate facts in Appendix F. These named library theorems are source imports, not newly formalized proofs. Lemma 8 gives a uniform exponential envelope at fixed `(epsilon,Delta,n)`. |
| Cost continuity needed for attainment | Appendix E Corollary 1 LF1643–1669, Theorem 6 proof LF547–583 | If one maximal-decay radial law has finite cost, the common envelope makes all such costs finite and weakly continuous; otherwise the source handles the identically-infinite case. No additional continuity of `phi` is stated. |
| Existence / optimizer | Theorem 6 equations (13)–(14), Definition 2 | Equality of all-admissible and staircase-family cost infima, with some minimizing `gamma in [0,1]`, for Assumption 1. Printed source proof dependency gaps remain named (§6); prior alternative-proof adoption is not withdrawn or promoted by this audit. |
| Equality / unique law / explicit selector | Theorem 6 LF530–583; Theorem 10 | Existence of a minimizing gamma, not an explicit finite-epsilon squared-Euclidean selector, exhaustive equality or unique law for the original mismatched cost. Extreme-point classification of the radial subclass is not classification of EVERY global optimizer. The two gamma endpoints represent the same law per Definition 2's footnote. |
| Rounded-core solution / mixed-cost implication | Same theorem statements/proofs just read | No theorem in the operative chain pays the registered squared-Euclidean lower bound plus rounded selector: the cost hypothesis already fails. The safe-status v253 result requires LAW642 and its stated union; it is not a result printed here nor an independent source proof of LAW642. |

Theorem 2 is explicitly a cited earlier `n=2,l1` first-power-cost result; it is not this paper's proof of the present squared-Euclidean target. No external cited source was fetched to strengthen it.

## 6. Specific as-printed proof obligations NOT independently cleared

These are source-proof observations from the newly admitted primary, not a claim of mathematical falsity of Theorem 6, a new severity classification or a withdrawal of earlier adopted alternative proofs.

### NR-A — Appendix A-A, Theorem 7, transition to equation (19)

The paragraph after equation (18) derives `mu(I)<=C mu(Q)/|Q|`. Taken by itself this implies a LOWER bound `mu(Q)>=mu(I)|Q|/C`. The next paragraph sets `M=C mu(I)` and asserts the UPPER bound `mu(Q)<=M|Q|` in equation (19). That asserted upper bound does not follow from the displayed preceding inequality. This direction mismatch is present in the retained native HTML LF1790–1816 (MathML/TeX alttext), not merely a damaged rendered glyph. It does not show that the absolute-continuity theorem is false: §3 supplies an explicit all-variable averaging proof at named analysis imports. That proof must be credited separately, not silently called the paper's printed argument.

### NR-D — Appendix D-A, Lemma 7, the global integral comparison

Let `T=int_0^infinity r^(n-1)rho(r)dr` and `y=m Delta` as in the primary's quantified large-integer argument. Definition 8 anchors `rho_y=rho` on `[y,y+Delta)`, and Proposition 3 gives `rho_y>=rho` before `y` and `rho_y<=rho` after `y`. The printed proof then asserts a global inequality `psi(y)>=T+` a positive head integral. The exact identity instead retains the tail term:

`psi(y)-T = int_[0,y] r^(n-1)(rho_y-rho)dr - int_[y,infinity) r^(n-1)(rho-rho_y)dr`.

The second term is nonnegative and is SUBTRACTED. The printed local sign information alone does not justify dropping it in the lower bound. Its sentence saying `rho_(m Delta)` coincides with `rho` on the earlier whole interval is also not what Definition 8 states. A sufficient eventual head-surplus-versus-tail estimate is not displayed at this step. The paper proceeds to continuity/IVT and uses this conclusion in Lemma 1 and Theorem 6; that as-printed dependency remains **NAMED_NOT_RECONSTRUCTED** here. Targeted native-source grep also locates the coincidence sentence at native LF2823 and the conclusion `psi(m Delta)>T` in native LF2851; the complete integral-comparison argument was read in the reader through its ending, not fully reread as native HTML. No selected profile, numerical countercontrol, old alternative proof or protected guide is used to fill the gap.

This stops adoption of the full printed-proof chain in this submission. It does not stop the source-statement/hypothesis comparison or the elementary independent coupling/obstruction proved in §§2–4. The original general STOP is not self-released for a new optimality repair.

## 7. Exact result, first failed implication and current residual

**Delivered written result:** a full all-law/event/closed-shift to universally pointwise-density coupling (Lemma A), robust-query quantifier separation, and a whole-variable simultaneous cost/shift obstruction invariant under invertible linear coordinates (Lemma B), together with the actual printed theorem/hypothesis/dependency map. These go beyond merely renaming the source's coordinates. No numerical instance or fresh optimality proof was substituted for the gate.

**First failed application edge:** set the norm/scale to preserve the original diamond, then MDA Theorem 6's **Assumption 1 does not admit the original squared-Euclidean objective**. If the cost is changed to squared-`l1`, the printed theorem states an attaining staircase optimizer for the all-law same-norm cost, at its proof dependencies; it supplies no independent registered mixed-cost lower bound, rounded-core selector or exhaustive original-law equality. A source theorem with an unsatisfied hypothesis cannot be called source-equivalent merely because a separate conditional union using LAW642 exists.

**Still required:** actual closure/assessment of the printed-proof NR-A/NR-D interfaces if printed-proof verification is desired, and an actually covered independent external-source implication for SOURCE-MATCH-U1. Whether some other part or combination of publications implies the registered result is not decided by this first failed edge. No worldwide absence, firstness, priority or novelty finding follows.

**Unchanged:** inherited LAW642/NORM148/separated v241/v253 adoptions remain only at the safe final-report cuts; their old bodies were not reread. Original threshold-v2/v214-A, selected-check consumers, administrative exposure consumers and every historical finding stay HELD/ZERO as directed. N4 UNKNOWN/historical child exit unestablished, aux214 STOP, scientific HOLDv2 and original STOP outside this narrow task persist. No scientific execution, calculator/interpreter/CAS/Eval, enumeration, solver/replay, selected state/control/boundary probe, build/test, nested agent/modelCLI/new GO, Git/deletion/contact/infrastructure action. All computations in this document are universally quantified written identities/inequalities with named imports, not kernel checks.
