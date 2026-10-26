# Information-science selection v2: generic SOF at eight states and port pair {2,4}

Before-creation clock observed: **2026-10-23T13:31:28-07:00**. Owner `InfoResearch96h`; exclusive write root unchanged. This activates the reserve **after the parent's explicit directive**, following completion of the bounded-real surrogate obligations. It does not silently narrow or withdraw the first target.

The first target's five-result stack is integrated in `delivery-bounded-outcome-v2.md`, SHA-256 `8295503b1ac4d79e1e3193da59e9f60c8e454eae6bff6c40240c58740107d76a`. Those results are in-harness WRITTEN_CHECKED, with the new consolidation itself awaiting a fresh integration read; **Kuroki ACCESS_BLOCKED / NOVELTY_UNCLEAR** remains operative. All originals and historical deficiencies are preserved. The parent timestamp erratum governs affected parent labels; none is adopted here as an observed clock.

## 1. Exact active primary question and notation

To eliminate the incompatible input/output letter conventions in the sources, fix the actual dimensions:

    x in R^8, u in R^4, y in R^2,
    xdot=A x+B u, y=C x, u=K y,
    A:8x8, B:8x4, C:2x8, K:4x2.

Thus the geometric Eremenko convention is (m,p,n)=(2,4,8), with m rows of V / measured outputs and p inputs. The NASA/AIM convention reverses the port letters; transposition interchanges the ports and preserves the unordered dimension pair. No disagreement about the number of gain entries is involved: there are eight.

Let S be the set of real triples (A,B,C) admitting a real constant K for which A+BKC is Hurwitz. The primary is:

> **P24. Is S dense in the Euclidean space of all such triples?**

Since S is open, a negative answer must yield a genuine nonempty open family of unstabilizable eight-state plants, not one nongeneric uncontrollable/hidden-mode example. The book's full arbitrary-dimension synthesis problem and the all-port-pair generic classification are broader than P24.

### First bounded full-negative route

Seek an explicit real polynomial matrix V(z) of size 2x6 satisfying:

1. its 2x2 minors have no common complex polynomial factor and their maximum degree is exactly 8;
2. **complex non-degeneracy:** no rank-4 complex constant matrix L makes det[V(z);L] identically zero;
3. **empty real repeated-pole fibre:** no real rank-4 L and real c!=0 satisfy

       det[V(z);L]=c z^8.

A complete V with full proofs would supply an unconditional empty-real-fibre theorem. Its implication for P24 uses the separately named classical generic-stabilizability/deadbeat bridge, authenticated at statement level below. A final P24 claim must also bind the polynomial-matrix realization to an ordinary degree-eight real plant; it cannot simply rename a Grassmannian calculation as stabilization.

A preferred search representation is

    V(z)=[D(z),N(z)],
    D(z)=z^4 I_2+D_3 z^3+D_2 z^2+D_1 z+D_0,
    N(z)=N_3 z^3+N_2 z^2+N_1 z+N_0,

with real/rational 2x2 D_i and 2x4 N_i. This balanced monic chart provides an explicit eight-state observable companion realization. It is an **attack representation**, not a new hypothesis on the full P24 question. Failure in it would not prove the positive answer or exclude every counterexample.

A positive answer to P24 instead requires a theorem for **every** relevant non-degenerate degree-eight real V / generic plant class, with the precise compactification and real-gain chart accounted for. No such result is presumed.

## 2. Full book provenance and matched baseline

Book: *10000 Selected Problems in Sciences: Information Science*, Science Press 2011, ISBN 978-7-03-031911-1. Article *Disturbance Decoupling Problem with Static Output Feedback*, Chen Benmei, printed pp.631–632 / PDF pp.652–653. The actual p.631 image was rendered and opened in this lane: `sources/book-sof-0652.png`. The text extraction is `sources/book-sof-631-632.txt`.

The printed internally stable variant requires all eigenvalues of A+BKC_1 to lie in the left half-plane. Set all disturbance/controlled-output channels E,C_2,D_1,D_2,D_22 to zero, retaining y=C_1 x and D_11=0. Then decoupling holds for every K and the remaining question is exactly SOF stabilization. P24 is therefore a precise generic-dimensional subquestion of an included book problem, not a claim that the article itself states P24.

Actual repository baseline: `information-science/ddp-static-output-feedback/README.md` gives prior per-instance real-algebraic decision, the classical determinant/Grassmannian reformulation and restricted **unstabilized** synthesis for min(port counts)=1 or both counts=2. It does not solve stable real selection at this port pair. Repeating its lifted polynomial/QE formulation, an isolated special plant, NP-hardness or the already-known (2,2,4) example would not advance P24.

## 3. Exact candidate comparison at this transition

| Candidate | Exact statement | Strongest matched source/baseline and missing ingredient | Decision |
|---|---|---|---|
| **P24: port pair {2,4}, n=8** | Density of stabilizable triples specified in Section 1; negative route requires a non-degenerate degree-eight empty z^8 real fibre plus ordinary-plant binding. | Original Byrnes–Anderson manuscript Theorem 1 gives the nondegenerate deadbeat equivalence at mp=n. Eremenko–Gabrielov 2002 proves some even-even pole-placement omissions, not omission of every stable spectrum. Eremenko's current question still asks the generic stabilization classification. Missing: a repeated-pole real-fibre obstruction retaining degree eight/nondegeneracy, or a universal real-selection theorem. | **Primary.** A new port-pair decision is consequential; a failed restricted ansatz is only route evidence. |
| **P33: port pair {3,3}, n=9** | Is the set of real 9-state, 3-input, 3-output SOF-stabilizable plants dense? Negative route: a non-degenerate 3x6 polynomial matrix of degree 9 with no real rank-3 z^9 fibre, with plant binding. | Same classical criterion; its Schubert degree is 42, so the odd-degree criterion does not force a real fibre. No exact generic stabilization classification was found in the sources read; this is UNCERTIFIED-OPEN, not a claim of global absence. The nonlinear Plucker surface is larger than P24. | **Reserve.** Activate only after a new selection/parent redirect, not in parallel with P24. |
| **CGMN at q=18** | Find a Latin square L on 18 symbols such that L(y,L(x,y)) is Latin, hence a 324-word recursive [4,2,3]_18 MDS code. | Klimov arXiv:2604.01105v2 retains q18 after constructing q26; q14 has a historical separate claim. Perfect-Mendelsohn implication/source access holes remain. Its coding-book bridge is less direct than P24's stabilization inclusion. | Not selected; do not rerun old finite-code cases or infer openness/priority from a search miss. |

The earlier source-complete bounded-real primary is not disguised as an unsolved reserve. Its remaining Kuroki gate is a source/novelty gate, not a mathematical-exhaustion argument or permission for publication.

## 4. Primary sources actually read and exact status limits

### 4.1 Original Byrnes–Anderson access now obtained

A new lawful primary route was found through the current AIM problem record: [NASA CR-166441 / 19830010078](https://ntrs.nasa.gov/api/citations/19830010078/downloads/19830010078.pdf), containing the submitted *Output Feedback and Generic Stabilizability* manuscript at printed pp.105 onward.

- Retained report: `sources/nasa-19830010078.pdf`, 277 pages, SHA-256 `5782ab5cbc308d1a62c266ec2c1b8f2ecdaf925b18d84f8edbb15cd9eb835301`.
- Source text: `sources/nasa-19830010078.txt`.
- Actual images opened: `sources/byrnes-anderson-theorem-113.png`, `sources/byrnes-anderson-example-134.png`, `sources/byrnes-anderson-example-136.png`.
- Theorem 1 on p.113 states, in the mp<=n regime and in particular at mp=n, equivalence between generic stabilizability and assigning s^n for every non-degenerate plant. Question 2 uses exclusion of a proper algebraic exceptional set.
- Section 4, pp.132–133, was read for the closed-image argument and the **complex-linear** non-degeneracy definition. This is why the active target explicitly retains complex, not merely real, non-degeneracy.
- This authenticates the original statement/interface beyond the living author's summary. It is not an independent replay of every proof in the 1984 publication, nor automatic authentication of every displayed coefficient/sign in the scan.

The generic-stabilizability/empty-fibre consequence is a named classical theorem-level import. The local algebraic claims must remain independently proved.

### 4.2 Current author question and the pole-placement distinction

[Eremenko's author-hosted note](https://www.math.purdue.edu/~eremenko/dvi/gpolep.pdf), currently displaying 3 October 2026, was read in full. The problem itself is older; the current [AIM problem 319](https://raw.githubusercontent.com/MColbrook/AIM/main/problems/319-generic-static-output-feedback-stabilization.md), dated check 17 September 2026, identifies a 2010 version. Do not describe the underlying problem as first posed in 2026.

[Eremenko–Gabrielov 2002](https://www.math.purdue.edu/~eremenko/dvi/polep72.pdf), Introduction/§2 and the explicit missing-spectrum argument, was opened. It proves nonsurjectivity for some prescribed real spectra at even-even port counts, while separately retaining generic stabilizability as an unsolved question. A missing non-Hurwitz spectrum or the known Wronski map is not a P24 counterexample.

The AIM record is a dated status/route inventory, not an independently authenticated theorem. Its primary NASA link materially improves source access. Recent unrestricted SOF complexity sources [Liu arXiv:2610.00390v2](https://arxiv.org/html/2610.00390v2) and [Barkai–Shames arXiv:2609.38728v1](https://arxiv.org/html/2609.38728v1) were read at abstract/Introduction/theorem-interface scope. Worst-case variable-dimension hardness, even with two inputs, does not decide generic density for the fixed critical triple here; no hardness proof is imported.

**Dated active status:** P24/P33 are **UNCERTIFIED-OPEN / NOVELTY_UNCLEAR** within this bounded primary screen. The exact current author question supports headroom; neither an expert problem list nor search misses certify priority or exclude an overlooked later classification.

## 5. Mandatory corrected calibration and chronology

The current Eremenko note literally displays z+1 in its 2x4 (2,2) control. That is not a negative control: the exact rank-2 real plane built using b^2-b-1=0 gives determinant z^4. The actual PDF page 3 image was opened, so this is not an OCR-inferred sign change.

`reserve-source-control-correction-v1.md` supplies the complete one-parameter coefficient derivation and complex non-degeneracy proof. The parent's `information-source-correction-parent-v1.md` has checked that correction, subject to the parent timestamp erratum. Its approval is cited by path, not its estimated clock label.

**Operative negative calibration:**

    V_-(z)=[ z^2, 1, z, 0
              z-1,z^2,1,z ].

Its z^4 fibre must lie in [K,I_2], and the full coefficients force a=-1,d=1,c=1+b and b^2+b+1=0. The six minors prove complex non-degeneracy. Thus this is an exactly proved rational negative control. The literal V_+ is instead a **positive** control with the explicitly known real planes. No original 1984 exact-matrix attribution is inferred from changing the sign.

Chronology: this source-control falsification and some exploratory polynomial/Plucker ideas occurred during the transition before this v2 freeze. They are selection input, not falsely represented as post-registration discovery. There was no scientific program or solver. The source correction is an internal calibration only: **no external contact or publication is authorized or performed**.

## 6. Missing ingredient and first written attack

The central missing ingredient is a **real decomposable-point exclusion that is realizable by the full degree-eight polynomial curve**, with no complex base locus. A generic linear subspace avoiding real rank-2 bivectors is not enough: the first eight determinant coefficient forms must actually arise as the jet of a decomposable polynomial 2-plane curve, and the ninth coefficient must preserve degree/non-degeneracy.

First bounded direction: use the 15-dimensional real bivector space Lambda^2 R^6 and the coefficient map of the pole polynomial. A real z^8 fibre is a decomposable point in the common kernel of the first eight coefficient forms. Seek an exact positive/definite Plucker certificate for that kernel. A materially different ingredient from the old (2,2) quadric is the Hermitian/primitive-form representation on R^6=C^3, where trace-free Hermitian (1,1) forms give large subspaces without real simple 2-forms. The attack must determine whether such a real-avoidance certificate is compatible with a balanced degree-eight curve; merely observing the subspace avoidance is **not** a result on P24.

In parallel symbolic terms within the same target, retain coefficient-level elimination in the monic D,N chart as a route to a rational exact sum-of-squares contradiction. No random parameter sweep or numerical infeasibility will be called nonexistence. If the primitive-form jet ansatz is impossible, prove its precise impossibility and redirect the representation while leaving P24 intact, rather than repeating small coefficient changes.

## 7. Verification and acceptance

A negative candidate must include all of:

1. explicit exact V (preferably rational coefficients), all minors and exact degree/gcd check;
2. a proof of **complex** non-degeneracy, not just a finite-gain check;
3. a complete real z^8-fibre exclusion accounting for every Grassmannian chart, or a proof that every such fibre lies in one complete chart;
4. explicit ordinary state-space realization/binding and the exact imported theorem consequence for P24;
5. corrected positive/negative controls above, including the original-plus-sign rejection as a negative control;
6. parent and independent in-harness reconstruction plus matched primary prior-art comparison. Finite/formal/human and scientific-priority labels remain distinct.

A positive P24 theorem has the stronger universal burden; a failure of one constructed V or ansatz never proves it. No degree, state count, real-versus-complex, finite-versus-infinite gain or open-neighborhood condition may be dropped.

All work is **written-only** at present. Before any scientific program, compilation, solver, enumeration or load-bearing executable certificate replay, submit exact commands, source/input pins, controls, resources and settlement to the parent for a named GO. Source extraction and metadata hashes are the only native operations so far; they do not confer a scientific execution GO. No nested agent, model CLI or historical runtime is authorized.

## 8. Redirect condition

Stop or change the active target only through a preserved numbered selection/parent decision if a matched primary source already decides P24, or a substantive argument establishes the desired answer. A complete obstruction to one representation earns an explicit NEEDS-NEW-REPRESENTATION disposition, not full-target closure. If the negative route cannot provide a realizable curve/nondegeneracy certificate, retain that exact obstacle; do not substitute some omitted spectrum, a special unstable plant, a QE restatement or another existing control-theory result. P33 remains reserve rather than a second simultaneous attack.
