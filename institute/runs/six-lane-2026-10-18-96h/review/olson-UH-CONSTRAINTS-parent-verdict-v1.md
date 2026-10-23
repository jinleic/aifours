# Olson upper-half terminal k=p+1: six partial results accepted, full exclusion open

Recorded at 2026-10-19T16:27:57-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL**, outcome **O3 only**. UH-EXCL remains OPEN. This packet excludes a multiplicity subcase at each parameter, not a whole (p,kappa) cell; no unrestricted rotation multiset, o_F, REFL, INV* or ordered-Olson theorem follows.

## Shared exact antecedent

Prime p>=7, (p-1)/2<=kappa<=p-3, e=p-kappa. A length4p-2 avoider has **some admissible NF** with terminal k=p+1,kappa_hat=kappa. All odd-block pair distributions H=e-1 are allowed; empty runs separate different reflection values. Every conclusion retains this antecedent. The arbitrary word-form proof is stronger; no unsupported converse NF property is used.

## Accepted statements

| Result | Exact scope and conclusion |
|---|---|
| UH-A | Nonzero common unsigned dominant class {a,-a}, oriented A>=A'. Then2kappa+3<=A<=2p-1,A'<=kappa,p-2e<=b=R-A<=p-4,0<=delta=R-A-A'<=p-2. Excludes A<=2kappa+2, not an entire kappa cell. |
| MW | For each nonconstant sign pattern with2m changes and any nonzero signed value s, phi=v_s,w0=R-phi, K_min=max(0,p-1-2e+2m),K_max=p-3+2m. For the even K with max(w0,K_min)<=K<=min(phi,K_max), q>=1 implies w0+q<=p-1. No conclusion if q=0 or s=0. |
| SH | If3e<=p+2, there is a run h with alpha_h-beta_h>=p+1+delta; every nonempty set avoiding h is ordinary-low and at least two runs are empty. Structure only. |
| L | **Requires delta=0.** For proper low arcP, epsilon=A'+d(P), U(P)=min(p-1,floor((R-epsilon)/2)); attainable normalized sums are exactly[kappa-epsilon,U(P)] modp. Avoidance gives unique lift in[U(P)+1-p,kappa-epsilon-1]; lifts add only along paths of at mostp runs whose every nonempty consecutive subarc is low. Empty lifts need not be positive. |
| PH | **Requires all rotations equal and some run with at leastp rotations**, in addition to shared antecedent. That pure-heavy subcase is impossible. Pure words with every run<p are not excluded here. |
| E | For empty-negative patterns, exclude exactly the minority-subset sums with both |J|<=n and n-|J|<=A at each allowed evenn; only b<=n<=A permits substitution of the full subset-sum set. Its missing-set bound is<=max(0,p-1-b). |

## Frozen evidence and reviews

[Proof](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/terminal-pplus1-upperhalf-exclusion/proof-UH-CONSTRAINTS-v1.md) `56327b678bf9f7fe62d6f518499ab692f00897a3ecff2c62ddecac4a42a5115c`; [obstruction](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/terminal-pplus1-upperhalf-exclusion/obstruction-UH-EXCL-v1.md) `f2f1a232c98b3ef6eb45fa0486912bd54170521e5adc00e09c436b1fb8c7849d`; [original freeze](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UH-CONSTRAINTS-review-freeze-v1.json) `45058686ec916ff91761466737240e288b501983fa08a567d62bee4ccbc08f4a`.
Mandatory [erratumv1](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UH-CONSTRAINTS-parent-erratum-v1.md) `8f1ea491eb2ab8ab4d4f1006896cb9aad63d6c51e270acb190de7bdaf4074ee3`, [v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UH-CONSTRAINTS-parent-erratum-v2.md) `ac2a7f26ef941366e70e939545bae07a5baea6564005af29e5c9185560aaaa50`, [v3](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UH-CONSTRAINTS-parent-erratum-v3.md) `0dc678867d10f28abc2f1681b21805658318fa9fc3a4c379062152cc1aef813f`.

- [Codex gpt-6.1-sol/max](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UH-CONSTRAINTS-codex-v1.prompt.stdout.txt) `3bc39a9447eebce3787ec731cb86e72cdaf1589f47888b81d28b9414c90ac025`:0F/0M/2m, all six scoped results accepted after v1; final wording covered by v2.
- [Claude claude-opus-5-5/max](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UH-CONSTRAINTS-claude-v2.prompt.note.md) `58d9dd134b0137d0599e0fc335b9ef6d4025ecc0edcc2dae575fe7f9631232d5`:0F/0M, all six scoped results accepted after v1/v2; ten final minor items disposed in v3. Both receipts exit0 and exact corrected prompt binding verified.
- Parent original freeze records whole proof/obstruction read, source/range pins and independent SR/P/U, heavy/light, missing-residue, omission/filler, lift/additivity and PH budget checks. Current parent read all new finding anchors and exact statements, confirmed lambda=c-1, the distinction between ordinary and m=e windows, low-path/delta conditions and the absence of a whole-cell conclusion.

Only accepted NF/GRX(if direction)/RS(b) plus classical Cauchy-Davenport are load-bearing; CT, Lev, S(p), endpoint candidates, RPdelta and assembly results are not premises. No scientific computation, formal Lean check, human review or novelty conclusion. The remaining R-UH is a named unfinished word-level target, not a smallest/mathematically necessary lemma; failed route notes remain preserved. Runtime remains HOLD.
