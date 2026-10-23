# Olson word-level assembly on o_F <= p

Recorded at 2026-10-19T13:16:22-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL**, for prime p>=7, relative to the recorded classical imports. **S(p) remains at secondary-statement trust** (KPS-SLZ item 1/M-1: Xia-Yuan2010 through Peng-Sun2014, primary proof unread). **Lev2022 Theorem2 remains at statement-level trust** exactly in the cells below; its proof was not replayed. At p=7 the result is Lev-free, **not S(7)-free**. Full ordered Olson and unrestricted INV* remain OPEN.

## Accepted word statements

Let o_F(w) count the ODD blocks in the maximal cyclic CONSTANT reflection-block decomposition, not the number of reflection runs. An avoider has no identity product from 2p letters selected in increasing original index order.

- **ASSEMBLY-P (A):** every avoider of length 4p-2 over D_(2p) with o_F(w)<=p has all rotations in one nonzero pair {rho_c,rho_-c}, and every maximal cyclic reflection run is constant (INV* at this restricted word class).
- **ASSEMBLY-P (B):** every word of length 4p-1 over D_(2p) with o_F(w)<=p has an identity 2p-subword in increasing original index order.
- **ROT-P:** if SOME admissible normal form of a length-(4p-2) avoider has terminal k=p, its rotation multiset lies in one nonzero pair; no o_F hypothesis is required for this rotation-only proposition.

The review snapshots prove these implications conditional on ONE-SHORT-LS and ROT-SING. Their exact premises are now separately accepted and discharged:

| Premise | Accepted scope and record |
|---|---|
| ONE-SHORT-LS | [Verdict](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ONE-SHORT-LS-parent-verdict-v1.md) `4116007e28f6362b9b6a0907f5601da3f058348ae53209b4c9b2d46d8d8f7be8` with erratum `35bcae46`: odd Y of EXACT length p+2kappa, floor(2p/3)+1<=kappa<=p-2, ZP implies S1. Lev-conditional in case (I), every e>=2. The assembly invokes it only at kappa-hat in U(p). |
| ROT-SING | [Verdict](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ROT-SING-parent-verdict-v1.md) `12781c7c879bc1bcb8216aff73fd461c91cec8d177ec2a5bc0e0cf0121bc194f` with errata `aad62a16`, `ef93d8c1`: SOME admissible normal form k=p,kappa-hat=p-1 gives exactly rho_c^(2p-1)rho_-c^(p-1), c!=0. No o_F condition, Lev or S(p) input. |

This is a logical discharge of the two stated hypotheses, not a new proof of either premise or a changed composition.

## Auxiliary statements and dependency refinement

Accept **DEP** and **ASSEMBLY-P0 (A0)/(B0)** at their printed scopes, with all trust qualifications from [parent erratum v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ASSEMBLY-P-parent-erratum-v2.md) `86f27fb81e06de0f99434637e202c9f6fad4e0b35b37c67477349b9614acc147`. Define

U(p) = {kappa: floor(2p/3)+1<=kappa<=p-3, p<10(p-kappa)-13, and NOT (p=1 mod3 and kappa=(2p+1)/3)}.

Outside U(p) in the stated high-kappa interval, DEP replaces ONE-SHORT-LS by LS+2, LS+ linear band or BASE1+ at their accepted scopes. U(7) is empty and U(p) is nonempty for prime p>=11. P0 consists of words with o_F<=p-1, or o_F=p and kappa(w)=p-1-(F-o_F)/2 outside U(p) union {p-1}. Its inverse and word-level conclusions need neither formerly pending premise, but still carry the recorded classical/Lev/S(p) dependencies where invoked.

## Cell-specific trust

- Invoked k<=p-1 normal form: ROT-LS has Lev only for p>=11 and floor(2p/3)+1<=kappa-hat<=p-3; no S(p) is added by this branch.
- k=p,kappa-hat in {0,1}: ROT-KP, avoiding S(p).
- k=p,2<=kappa-hat<=p-2: ROT-KP+ uses S(p). Lev is used only if kappa-hat is in U(p), through ONE-SHORT-LS; DEP routes elsewhere retain their declared Lev-free interfaces.
- k=p,kappa-hat=p-1: ROT-SING, without Lev or S(p) on this route.
- Restricted REFL, the deletion ledger and RGR-LONG enter at word level at their original accepted scopes. Classical index-one results, EGZ, Davenport constants and Cauchy-Davenport retain their recorded import boundaries. No exhaustive transitive-proof audit is claimed.

## Text and reviews

- [Proof v2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/assembly-p/proof-ASSEMBLY-P-v2.md) `059033b00b669e10f0fa49bdb2fdb55a135a85644f792ef2b3b3d6eb61dacfb5`; [initial freeze](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ASSEMBLY-P-review-freeze-v1.json) `22e2850a44f67be71886e6cf326dde0fabd275dccda2dd925e83b6b85bb796e2`; [corrected Claude freeze](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ASSEMBLY-P-claude-v2-freeze-v1.json) `40921011910cda4e7ee6ecbf9ddf83ec79baad09b0584deaf6736bb8260a420a`. The parent verified every frozen source pin against disk.
- Mandatory [erratum v1](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ASSEMBLY-P-parent-erratum-v1.md) `d6fe328fb804dd21d17cf29a11b17ba1a03c7804659a1ea2eab442a07fbfe10d` and [v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ASSEMBLY-P-parent-erratum-v2.md) `86f27fb81e06de0f99434637e202c9f6fad4e0b35b37c67477349b9614acc147` applied in that order. Prior "pending" labels remain historical snapshot status, superseded only by this verdict at the exact scopes above.
- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ASSEMBLY-P-codex-v1.prompt.stdout.txt) `59d1d744a77f45fb6790f4da5c70f787a849f6e4621074b4c7c627a2955a3a22`: gpt-6.1-sol/max/read-only, six implications ACCEPT under their stated conditions, 0 FATAL/0 MAJOR/3 MINOR, disposed by v1.
- [Claude v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ASSEMBLY-P-claude-v2.prompt.note.md) `e6086a55a354263354e954d6326aa765e7092cd51ba8a7d384438476948df531`: claude-opus-5-5/max/no tools, same mathematical implications ACCEPT-WITH-FIXES, no FATAL/MAJOR, five MINOR groups (two optional), disposed by v2. Parent erratum v1 accepted; no interface-domain violation found.

## Parent independent checks

At k=p, all-plus GRX gives C_max=2H-hat and ZP for rotation length R=p+2kappa-hat; DAV gives 0<=kappa-hat<=p-1. The four routes partition that entire interval. DEP length contradictions are 3p-4>3p-5; 3kappa+e>=3kappa+3>3kappa+1; and (7p+2)/3>2p+2 for p>4. At p=7, U is empty because its lower endpoint5 exceeds its upper endpoint4.

For (A), NF gives k<=o_F<=p; ROT-LS/ROT-P supply the pair and REFL applies to the ORIGINAL word. For (B), R<=2 gives F-o_F>=3p-3>=2p, enough adjacent equal-reflection pairs; an odd-block deletion lowers o_F by1, while a rotation deletion never raises it. With R>=3 a shared third nonzero rotation identifies the same pair in both deletions, and existing unequal adjacent reflections could not disappear under a rotation deletion. P0 preservation uses the explicit o_F-drop-or-unchanged-kappa split, not monotonicity in kappa. These are written checks, not runtime or Lean verification.

## Open and calibration

No result at p=5 is asserted. o_F>=p+1 reflection/word assembly and unrestricted INV* remain open; ROT-P covers only the rotation half at terminal k=p even when o_F is larger. Neither forthcoming k=p+1 candidate exclusion is used. The (B) dependency is retained conservatively rather than adopting the reviewer's unreviewed strengthening. This extends the internal accepted word class from o_F<=p-1 to o_F<=p; it is not a literature-wide novelty or matched-SOTA claim, nor full ordered Olson for D_(2p) or arbitrary groups. No Lean or human-referee claim.
