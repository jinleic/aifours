# Information-science selection v1

Before-creation clock observed: **2026-10-23T12:48:49-07:00**. Owner: `InfoResearch96h`. Governing contract: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/contract-v1.json`. Only this lane root is writable. Source extraction and written reasoning have occurred; **no scientific program, solver, compilation, enumeration or certificate replay has run**.

## 1. Decision and chronology

**Primary: sharp bounds for a bounded real primary outcome in the strong-surrogate paradox model. Reserve: generic static-output-feedback stabilizability at (m,p,n)=(2,4,8).** These are not PA19/CFR21/MOLS39/NL242 retries. The causal article was screened, but not attacked, in the 2026-10-14 inventory; this bounded-real target is fresh relative to the immediately preceding 96-hour round and its evening continuation.

**Chronology disclosure:** exploratory symbolic derivation was already considered during source screening, before this selection file was frozen. The first complete manuscript will be subsequent to this file. Thus this is not claimed to be a pristine pre-derivation registration. No computational result informed selection. This timing departure is preserved rather than backdated.

The primary is a scoped mathematical question arising directly from the book's surrogate-paradox discussion, **not a full solution to causal inference or every surrogate model**. The previous repository screen correctly marks the all-binary reading solved by prior work; the new target changes the primary endpoint domain, not the binary result's priority.

## 2. Exact candidate comparison

| Candidate | Exact statement | Primary-source status and comparable baseline | Decision |
|---|---|---|---|
| **A. Bounded real surrogate endpoint bounds** | For every two subprobability measures mu_0,mu_1 on [0,1] with total mass 1, q in [0,1], and compatible gamma, determine the complete attainable interval of delta=E[Y_(S_1)-Y_(S_0)] among all laws of (S_0,S_1,Y_0,Y_1) with binary S_0,S_1, 0<=Y_0,Y_1<=1, law(S_0,Y_(S_0)) given by the mu_s, P(S_1=1)=q, and E[Y_1-Y_0]=gamma. No individual monotonicity, rank invariance, parametric outcome model or independence of the surrogate and counterfactual outcomes is imposed. | [Yin–Liu–Geng–Luo, arXiv:1607.05454v1](https://arxiv.org/html/1607.05454v1), Theorem 1, gives seven-piece sharp bounds for **binary Y** and Discussion explicitly leaves continuous Y/survival outcomes to future work. Published version: [doi:10.1111/sjos.12398](https://doi.org/10.1111/sjos.12398), journal 2020. [Hsiao–Tian–Parast 2025, §1.3.1](https://arxiv.org/html/2506.12194v1) still distinguishes the binary bounds from sufficient-condition work; its model is controlled cross-study conditional-mean deviation, not this fixed-gamma full-data identified set. [Hsiao–Tian–Parast 2025, JNPS](https://pmc.ncbi.nlm.nih.gov/articles/PMC12382359/) develops tests for sufficient stochastic-order/monotonicity assumptions, not this unrestricted sharp set. **Uncertified-open** for the exact bounded-real question; the checked sources do not establish absence of another equivalent theorem. | **Primary.** A complete quantile-tail formula with constructive attainment would be a defensible theorem delta over the matched binary theorem, even if later classified as a classical-method extension. |
| **B. Generic static output feedback, first even rectangular case** | Construct a non-degenerate real polynomial matrix V(z) of size 2x6, whose maximal minors have no common polynomial factor and maximum degree 8, such that no real four-plane L has det[V(z);L]=c z^8 for any c!=0; or prove no such V exists. | [Eremenko, 3 Oct 2026, pp.2–4](https://www.math.purdue.edu/~eremenko/dvi/gpolep.pdf) asks for which m,p the generic n=mp system is stabilizable, states Anderson–Byrnes' equivalence, and supplies only the (2,2) stabilizability counterexample. Eremenko–Gabrielov's 2002 both-even result concerns some pole-placement targets, not automatically the repeated target z^mp or lack of stabilizability. Current author's open question is primary evidence. **Uncertified-open** specifically at (2,4), pending further source comparison. | **Reserve.** New ingredient required: an explicit real-fibre obstruction with non-degeneracy, not another Grassmannian/QE encoding or the old (2,2) example. |
| **C. Recursive MDS code at alphabet size 18** | Find a Latin square L on 18 symbols such that D(x,y)=L(y,L(x,y)) is also Latin. Equivalently find the 324-word full recursive [4,2,3]_18 code {(x,y,L(x,y),L(y,L(x,y)))}. | [Klimov, arXiv:2604.01105v2, 16 Jun 2026](https://arxiv.org/html/2604.01105v2), Introduction/Conjecture 1 and conclusion, resolves q=26 and retains 14,18. Prior local screen records an Aug/July 2026 public q=14 claim, which does not solve 18. The older perfect-Mendelsohn-design implications have unresolved primary-access holes; no adoption on the basis of their absence. | **Not selected.** Exact finite witness has value, but the book bridge is less direct and prior-art accessibility is weaker. A symbolic prolongation obstruction considered during screening is not an existence result. |
| **D. Fresh covering-array screen** | Does a binary 17x17 array contain every triple of bits in every three columns? | [Hiess–Kampel, arXiv:2510.17596v1, 20 Oct 2025](https://arxiv.org/html/2510.17596v1), Contribution: CAN(3,k,2)=18 for k=17,18,19,20. Thus the exact 17x17 question is already answered **no** by prior work. | **Screened out, not attacked.** No repetition of its classification. |

## 3. Exact book provenance and scope bridge

Source volume: *10000 Selected Problems in Sciences: Information Science*, Science Press 2011, ISBN 978-7-03-031911-1; PDF SHA-256 as routed by `books/README.md`: `9b3f16ee6b558f7c289a7208cec01a9811091863631d09908b8f4cb66d2027db`.

**Primary:** article **Causal inference** (Chinese title: 因果推断), author **Zhi Geng (耿直)**, printed pp.596–599, PDF pp.617–620. Printed **p.597 / PDF p.618** explicitly describes the positive A->B, positive B->C, negative A->C surrogate/intermediate-endpoint paradox, and calls for causal scrutiny of surrogate criteria. The article is a research programme, not a claim that all the formal parameters below appear in the book. The exact modern target A instantiates that paragraph using the same strong-surrogate, randomized-treatment model as Yin et al., retaining binary treatment and surrogate but replacing binary Y by an arbitrary bounded real endpoint. The bounded support is an explicit restriction; unbounded/survival outcomes, continuous surrogate and non-strong surrogacy are not claimed covered.

The p.597 image was actually opened: `sources/book-causal-0618.png`; unedited extracted source: `sources/book-causal-596-599.txt`. The book's relevant reference is Ju–Geng 2010. New Markdown is English; the quoted Chinese title serves only bibliographic identification.

**Reserve:** article **Disturbance decoupling by static output feedback**, Chen Benmei, printed pp.631–632 / PDF pp.652–653. The internally stable formulation includes ordinary SOF stabilization by taking all disturbance/controlled-output channels zero. The reserve is a generic-dimensional subquestion of this included problem, not the complete arbitrary-plant synthesis problem. Source extraction: `sources/book-sof-631-632.txt`; original authoritative dossier images and exact feedthrough convention remain read-only.

**Candidate C bridge:** code construction is related to the coding/decoding articles, printed pp.394–395 and pp.464–466 / PDF pp.415–416 and pp.485–487. Recursive MDS existence is **not** the same as the former's average-case decoding-complexity question or the latter's quantitative iterative-decoding question. This weaker bridge is one reason C was not chosen.

## 4. Frozen primary obligations

### Claim, data and quantifiers

All quantifiers and exclusions in candidate A are operative. Treatment T is randomized independently of the four potential variables; consistency gives S=S_T and Y=Y_(S_T). The supplied data are population laws, not estimates. The gamma value is an external causal-mean input, not purportedly identified from the untreated joint law alone. Every compatible law must be retained, including atoms, zero-mass surrogate strata and arbitrary hidden confounding.

Success requires:

1. a necessary-and-sufficient data-compatibility condition;
2. explicit endpoint formulas, preferably a one-dimensional convex/concave quantile optimization, **not merely an infinite LP restatement**;
3. a full constructive proof that both endpoints and every intermediate value are realizable while preserving the exact observed law and gamma;
4. the exact distinction between excluding negative delta (lower bound >=0) and forcing positive delta (lower bound >0);
5. a matched reduction to the existing all-binary baseline and a real-outcome example that cannot be recovered from just the untreated means.

### Missing ingredient and first bounded attack

Write the unobserved individual surrogate effect as a known lower endpoint plus Z in [0,1], so that the only extra causal-mean constraint fixes E[Z]. Split the population by S_0 and S_1. For fixed switch masses, allocate Z to negative, zero and positive coefficient groups and optimize the observed outcome contribution by upper/lower quantile tails. Prove simultaneous attainability, including atoms, rather than integrating separately sharp thresholdwise inequalities whose optimizers might be incompatible.

### Verification and promotion

First deliver the complete written argument and explicit analytic examples. Parent reconstruction and independent in-harness checking are required before WRITTEN_CHECKED. No finite/formal verification is claimed. If a finite support implementation later helps falsify a formula, submit an exact resource/command/hash/control request before executing it; no present GO exists. Parent may consolidate comparison with the 16-type binary LP after a complete candidate is available.

Novelty is **NOVELTY_UNCLEAR**, separate from mathematical correctness. The optimal-allocation and trimmed-mean ingredients are classical; neither a new general causal framework nor publication priority is claimed. In particular, the earlier binary theorem remains prior art even if rederived as a corollary.

### Redirect condition

Redirect to B if an accessed primary theorem already supplies this same identified set under matched data/hypotheses, or if simultaneous attainment exposes a genuine unresolved coupling obstruction not closed by the fixed-switch-mass allocation. Preserve the failed formula and issue a numbered successor before changing the target. Do not narrow A silently to a finite-support or atomless case. A failed priority gate does not mean the mathematical problem is exhausted.

## 5. Screening receipts and access limits

- Current `openai/math` main catalog was retrieved and preserved as `sources/openai-math-CONTENTS-20261023.md` (719 manuscripts / 372 result families stated by that snapshot). Complete title/abstract text was screened for surrogate, causal inference, partial identification and instrumental variable, as well as candidate B/C keywords. No matching family was located. This is a catalog screen, not a proof audit or a guarantee against unindexed equivalents.
- Primary full bodies read: Yin et al.'s model, Theorem 1 and Discussion; Klimov Introduction and displayed definitions; Eremenko's 5-page question; Hiess–Kampel's explicit contribution; modern Hsiao et al. abstracts/introductions and model distinctions.
- Kuroki 2013, doi:10.1002/sim.5873, has a primary abstract on sharp surrogate bounds; its complete theorem hypotheses have **not** yet been authenticated. This is an explicit priority-comparison obligation before novelty promotion.
- The published Yin paper's DOI metadata/abstract was read; its journal PDF was not independently authenticated. The actual proof interface used is the retained arXiv v1 text.
- Zenodo q=14 page returned HTTP 403 in this round. The historical q=14 record is only a prior screened lead, not a newly authenticated theorem.
- Historical PA19/CFR21/MOLS39 UNKNOWNs, all earlier process failures, and the old runtime HOLD retain their status. No new runtime framework or historical-engine execution is authorized or attempted.
