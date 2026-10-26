# Physics-4 selection v1 — full MOQLS(8) problem, global Gram-defect route

Status: FROZEN WRITTEN-RESEARCH TARGET; no scientific execution is admitted. Owner: PhysicsMOQLS8. Deadline remains 2026-10-27T12:35:38-07:00. Startup clock and ACK are in startup-v1.json. This selection deliberately does not timestamp its creation using an estimated clock.

## Literal primary target and definitions

For EVERY five arrays Q_s : {0,...,7}^2 -> C^8, s=1,...,5, assume:

1. Every row and column of every Q_s is an orthonormal basis of C^8.
2. For every s != t, the 64 vectors Q_s(x) tensor Q_t(x), x in {0,...,7}^2, form an orthonormal basis of C^8 tensor C^8.

Prove the family is classical: entry phases, a simultaneous row/column permutation, and a separate output unitary for each square turn every entry into a computational basis vector. Alternatively exhibit an EXACT family satisfying both conditions and a nonclassicality invariant. No finite phase alphabet, real-only condition, predetermined support, whole-square classicality, or K4/K5 assumption is added.

Accessible primary open statement: Ball–Simoens, *Large sets of mutually orthogonal quantum Latin squares*, arXiv:2607.12933v2, 27 July 2026, Problem 16: “Is a set of n − 3 MOQLS(n), n ≠ 4, necessarily classical?” At n=8 this is exactly the target above. Primary definitions are §§2.2–2.3. Their Theorem 5 proves the SIX-square case; it does not prove this five-square case.

## Book relationship — not a verbatim 2009 statement

The repository's books/README.md identifies the physics volume, edition, PDF and page offsets. The existing physics/phys-quantum-code-construction/README.md links this research lineage to Feng Keqin's quantum-error-correcting-code chapter, printed pp.601–604. The book asks broad code-construction/decoding questions. Problem 16 is a modern, precisely quantified quantum-combinatorial follow-on, NOT a conjecture printed in the 2009 volume and NOT a solution of its chapter. Musto–Vicary arXiv:1804.04042v3 explains the orthogonal-QLS/quantum-code relationship. No additional book equivalence is asserted.

## Current matched baseline and status

- Ball–Simoens v2 Table 2 gives 2 <= M(8) <= 5; Problem 16 is explicitly open there. Theorem 5 only bounds M(8) <= 5. Their Fourier/Frobenius-ring construction does not supply a five-square nonclassical witness here.
- The actual repository authority is final-v17 §5.1 plus its mandatory operative-delivery erratum, not the stale moqls8 README. It records GA18/18 and GB15/18 at their exact-input boundaries; GB P1-B2.M2, P1-B2.M4 and P1-B3.M2 remain UNKNOWN. B2.M4 had solver UNSAT but its checker hit the RSS cap; that is NOT a checked refutation. Some proof streams were digested but not retained. No old certificate is replayed in this assignment.
- The global U/T16/WMAN/NF-to-target composition and A10/A11 remain open at their stated trust boundaries. Genuine-image implications are not Boolean-model equivalences. K1/K2/K3 exclusions do not solve K4/K5. M(7)=2 is completed historical baseline, not new credit.
- Accepted B3 written work gives necessary support/one-cell/one-line/mass constraints and a 22-cell partial construction. It does not furnish a full grid or full B3 exclusion. The present route neither assumes their sufficiency nor rehabilitates withdrawn overclaims or unauthorized old arithmetic.
- Fresh primary reads: Ball–Simoens full v2; Musto–Vicary full text through Theorem18; Lv–Zhang–Cao arXiv:2609.29070 abstract (pairs, not five); Hontarenko–Zyczkowski arXiv:2610.17170v1 through §5.3 (entangled quantum-officer arrays, not five product-cell MOQLS). No later settling source was located in this bounded screen; that is NOT proof of present openness or novelty.
- Required corpus screen: local math/lean/docs and math/preprints were searched for quantum Latin/MOQLS/Ball–Simoens/Latin-square terms. The relevant-looking returned Latin-square citation concerns coboundary expanders, not this target. Remote openai/math README, lean/docs tree, preprints tree and complete CONTENTS.md were read/searched; no matched MOQLS claim was located. Generic “Latin” also returns “simulating”, which is irrelevant. No completeness claim is made about inaccessible/unindexed work.

## Frozen missing global theorem / exact representation

Let Omega={0,...,7}^2. Write G_s[x,y]=<Q_s(x),Q_s(y)> and h_s[x,y]=|G_s[x,y]|^2. Define

    Defect(Q) = sum_{s=1}^5 sum_{x,y in Omega} h_s[x,y](1-h_s[x,y]).

The missing GLOBAL theorem is: every family in the primary target has Defect(Q)=0. A positive defect is an isotopy-invariant certificate of nonclassicality, not a mere support artifact. This all-family statement is the primary problem in a different representation, not a silently narrowed B3 task.

First bounded attack: derive an EXACT support-free Hermitian-Gram idempotent system equivalent in BOTH directions to the full target, then derive the orthogonal projector-span/rank budget in the 49-dimensional row/column-contrast complement. As a substantive application, compute BY WRITTEN ARGUMENT the exact axis-span dimension for the still-open P1-B3 template and identify what a minimum-span completion would force. The B3 consequence is explicitly partial and imports H1–H4 as hypotheses only.

Missing ingredient: a reason the resulting global positive defect cannot occur, or an exact positive-defect point of the equivalent system. The existing GA/GB support predicates discard the phases and global positive-semidefinite realization; they do not supply this ingredient.

Consequential delta sought: an exact construction/certificate representation with a proved reconstruction map, plus a new necessary global spectral constraint usable on the genuine continuous problem without U/T16 or old native chains. No theorem count, solved-template count, novelty, priority or SOTA improvement will be claimed for a reformulation alone.

## Verification, imports and redirect

All derivations are written; no Python/Fraction cell, enumeration, solver, compilation, certificate replay or numerical experiment will run. Completed candidate bytes will be hashed as metadata and handed to Main for parent and actual separate reconstruction. No nested agent or external-model CLI is authorized. Spectral theorem, finite-dimensional Gram factorization, elementary positive-semidefinite trace facts and dimension formulas will be proved/identified at their exact import boundaries; no unverified classification is made load-bearing.

If the spectral route yields only the familiar n-1 size bound, say so rather than calling it a discovery. If a current primary source already settles the FULL target, immediately report the source and propose a distinct replacement for parent collision checking. If the B3 rank condition leaves all full configurations possible, report the precise unresolved saturation/interior-completion clause, not a claimed exclusion. The old runtime HOLD, preservation and UNKNOWN obligations remain unchanged.
