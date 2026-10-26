# Physics-6 selection v1 — AME(4,6) product-basis support

Observed clock before this freeze: `2026-10-23T13:59:28-0700`. Agent PhysicsAME46. Written/source work only; no scientific program or certificate replay has run. Contract-v2 and both parent errata govern. This file is immutable.

## Literal target, basis and reductions

For every normalized pure state ψ in (C^6)^⊗4 satisfying ρ_P = I_36/36 for **each of all six** two-element subsets P of {1,2,3,4}, and every product orthonormal basis B = B1⊗B2⊗B3⊗B4, define s_B(ψ) as the number of exactly nonzero expansion coefficients. Determine or improve

    s_min = min_{ψ AME(4,6), B product ONB} s_B(ψ).

Arbitrary complex coefficients and unrestricted local unitary basis changes are allowed. Approximate AME, one-body mixing, a fixed symmetry class, tensor rank and decomposition entropy are different problems.

In a fixed computational basis put A_x = 6ψ_x. For P|Pᶜ in {12|34,13|24,14|23}, write M_P[(x_i)_(i∈P),(x_i)_(i∈Pᶜ)] = A_x. Direct partial tracing gives ρ_P = M_PM_P†/36 and ρ_Pᶜ = (M_P†M_P)^T/36. Hence three unitary flattenings prove all six required marginals, not merely three diagonal or one-body conditions. Local unitaries preserve each condition; minimizing over product bases is equivalent to allowing every AME tensor in a fixed basis.

An officer is a support point with |A_x|=1. Write T for officers, t=|T|, N=S\T, h=36−t and e=s−(72−t). Previously proved e≥0; at e=0 all non-officer components in every flattening are closed 2×2 blocks. These are baseline facts, not new results of this slot.

## Book versus modern source

The source volume is the 2009 Physics volume, ISBN978-7-03-024269-3, registered at `books/README.md`. The exact minimum-support question is **not a literal 2009 book problem**: it is the modern AME/perfect-tensor continuation adopted in the 2026-10-16 phys-2 contract after quantum-code and two-unitary work. The quantum-information book setting motivates the line; neither that bridge nor a support theorem solves the book's general quantum-channel/coding questions. No unverified exact book-page claim is made here.

The literal accessible open statement is Palash Pandya, arXiv:2610.16673v1, §VI: “Whether the gap between38 and60 can be closed is open.” Relevant primary sections read: introduction, TableI construction and §VI (also historical pinned layout lines498–520). Current URL: https://arxiv.org/html/2610.16673v1 .

## Matched current baseline and source screen

1. **Internal rigorous baseline: 48≤s_min.** Parent verdict `institute/runs/six-lane-2026-10-16/review/ame46-lower48-parent-verdict.md` accepts `SUPPORT_LOWER48.r2.md`, SHA256 `70daac01707158b2842159dbdc6713afa33e541c51f100a91034fdf4d432f60e`. It imports the written42 proof and certified46/48 finite exclusions. This is an existing internally checked, computer-assisted result, not formal/kernel or human review and not this round's discovery. The old49 draft was never claimed; t24/e0 proof mode was UNKNOWN after a disk guard.
2. **Accessible current witness benchmark: 60.** Pandya gives12 coefficients of modulus1/6 and48 of modulus1/√72. Wojciech Bruzda's arXiv:2610.16882v1, §II–III, also explicitly gives60 nonzero entries in the rescaled tensor and all three flattenings. Source read: https://arxiv.org/html/2610.16882v1 . Hontarenko–Życzkowski arXiv:2610.17170v1 abstract gives its own96-term representative and compares60-term variants, not a smaller witness.
3. **Refresh, not assertion of exhaustive SOTA.** Fresh arXiv last-updated listing, saved as `arxiv-current-ame-listing-v1.xml`, still returns all three relevant papers as v1 dated2026-10-12. The sole newer matched listing entry, arXiv:2610.28204v1 (read), concerns five-qubit teleportation, not this support target. Two exact-topic web searches located no smaller witness in the accessible results; irrelevant acronym hits show the search's limits. Rather's unpublished announcement remains an access/coverage limitation. Therefore the matched documented gap is48..60; a worldwide-best or priority claim is NOT established.
4. **openai/math claim screen.** The local `math/CONTENTS.md`, `overview.tex` and the fresh remote `https://raw.githubusercontent.com/openai/math/main/CONTENTS.md` were screened for absolutely-maximally-entangled, AME(4,6),2-unitary, quantum/orthogonal Latin and officers terms. No target-matched claim was located in these indexes. This is a bounded index screen, not an exhaustive proof of nonexistence of a manuscript or novelty clearance.

## Consequential delta and first bounded attack

The unrestricted desired delta is a complete lower bound≥49 (ultimately60) or an exact state with≤59 support. The exact minimum remains the target; no ansatz failure is substituted for it.

First written attack: derive new support constraints from **thin non-officer slices and their shared phase transport**, beyond the old doubled-triangle obstruction. In particular, analyze the stalled t=24,e=0 layer's thin-slice overlap graphs and whether a general odd-cycle or projection-rank obstruction eliminates whole deficit profiles analytically. Freeze a complete lemma with its exact hypothesis and bridge before using it. If only a conditional support-structure theorem is obtained, label it PARTIAL and leave48..60 unchanged.

Missing ingredient: a global compatibility obstruction or constructive mechanism controlling all three flattenings simultaneously. Pair coverage and stochastic squared moduli do not imply coherent AME. Old SAT misses and UNKNOWN do not supply this ingredient.

Verification: give a definition-level written derivation of every affected flattening and both marginals per cut; pin the completed candidate for parent plus another agent's reconstruction. Any exact finite witness must provide a number field, explicit coefficients and exact six-marginal/support protocol with baseline and mutation controls. Numerical tensors or search output are not proof. No executable scientific check, solver, enumeration or old native runtime restart without an exact named parent GO; none is currently requested.

Redirect condition: if an actual newer primary source settles the target, report it and propose a distinct roster-disjoint replacement for parent collision approval. If this bounded phase/structure route yields no consequential unrestricted improvement, preserve the exact partial result and unresolved bridge rather than repeatedly restart the old enumeration or silently weaken AME.
