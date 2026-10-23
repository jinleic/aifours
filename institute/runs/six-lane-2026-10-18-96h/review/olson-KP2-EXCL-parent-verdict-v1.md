# Olson: terminal k=p+1, kappa-hat=p-2 is impossible

Recorded at 2026-10-19T13:48:18-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL**, written proof relative to accepted NF (forward avoidance preservation), GRX "if" direction and RS(b), with classical Cauchy-Davenport. **CT is not used.** No Lev, S(p), index-one, REFL, ASSEMBLY-P, PP1-EXCL or pending ROT-PP1 result is a premise.

## Exact accepted statements

1. **KP2-EXCL:** for primep>=7, no length4p-2 avoider over D_(2p) has SOME admissible normal form with terminal k=p+1,kappa-hat=p-2. No o_F or reflection-run/nonempty-run hypothesis on the original word.
2. **KP2-EXCL-prime:** no such avoider word has a cyclic representation with p+1 constant reflection blocks, exactly one of length3 and the other p singletons, possibly empty rotation runs, and every empty run separating different reflection values. This word-form statement implies item1 by NF.
3. **EXCL-PM2:** item2 under the additional nonzero pair hypothesis {c,-c} on all rotations; only GRX is imported. Section4 proves item2 independently without that pair premise.
4. Supporting M/P/U, W2 and run-analysis statements at their printed exact-cell hypotheses and corrected local naming/attribution.

## Frozen evidence and reviews

[Proof](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/terminal-pplus1-kp2-exclusion/proof-KP2-EXCL-v1.md) `8be43069c0a7935db902ba2ae4dda533b661ae0c981517f62f0e2b64e518b002` (256lines); [scope](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/terminal-pplus1-kp2-exclusion/KP2-EXCL-scope-v1.md) `20ea30954e76a18bbc6d4b02f826d35e2d285e1619f306997cf18f40447d9390`; [package](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/terminal-pplus1-kp2-exclusion/review-package-KP2-EXCL-v1.md) `2a932483042cf46ccf3915095c1bf108b466dab8056202aa98943891f3f10b77`; [manifest](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/terminal-pplus1-kp2-exclusion/review-excerpts-KP2-EXCL-v1.json) `def71828184913ae743fac75adfbee8b1ebf7d555213958d5e9e54c70b7bbbda`; original freeze `d5447b9e82c542b21b395d9ee56b7bb2b090a1b88904e73f48f7b016f798ed2f`; corrected Claude freeze `654a4eb55bdab58bb5156d8f7233b3ef6845c7df1e830128cef252f507abfb20`. Mandatory [parent erratumv1](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-KP2-EXCL-parent-erratum-v1.md) `4a6128d068b83d56fd6156a6b1e4569dce8a7e96afbbe4ff5c2d37645bd416a7`, then [v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-KP2-EXCL-parent-erratum-v2.md) `e41fd764bb9cfaef32cd0ace0cd55f6b9014c12ba48202eb93e4196501c27bfb`.

- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-KP2-EXCL-codex-v1.prompt.stdout.txt) `5e4eb5ed47c7d45b90a98ff2a27f67a4833c8bac2797b5273726c58535909ce8`: gpt-6.1-sol/max/read-only, all exact-cell theorem proofs ACCEPT; packet0F/1MAJOR scope wording/1MINOR ancillary derivation. The unrestricted multiset-only reading is REJECTED and withdrawn in v1, not retrospectively accepted.
- [Claude v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-KP2-EXCL-claude-v2.prompt.note.md) `1810893f43f4ecab1cdcb4d02aa99e5f647de62bee2aa2d4143fea561a5b5e6c`: claude-opus-5-5/max/no tools, all three theorems ACCEPT;0F/0openMAJOR/6MINOR, disposed in v2. It explicitly concurs that the raw multiset-only consequence was invalid and the scoped replacement is correct.

## Parent independent checks

NF gives H-hat=1, F=p+3,R=3p-5. GRX gives C_max=Phi+2 and allows C=Phi or Phi+2; extra two equal reflections change no sign target. W2 chooses p-1<=n<=2p-4 for EVERY nonconstant pattern; all four feasible-q interval branches contain >=p consecutive values. Pairing p-1 unequal pairs with actual fillers and RS(b) gives dominant multiplicity2p-3; U fixes a nonzero unsigned pair class.

For run analysis the parent re-derived lambda=A-2p+3,Lambda=2p-3-A', their gap p-1+delta_out, the heavy-run first crossing, and light-set contradiction A'>=p-1+delta_out versus A'<=p-2, including delta_out=0. Negative lambda would require p negative letters in p outside runs; hence b<=p-2 without CT. At most b+lambda=p-2 outside runs are nonempty, giving two empty runs. The b=p-2,p-3,p-4 missing-residue cases use full subset sums ONLY when n<=A and nonempty subsets at n=A+1; all filler bounds hold. The adjacent/nonadjacent normalized x contradictions also check. These are written re-derivations, not finite computation or Lean verification.

## Consequences and open boundary

The full antecedent of pending ROT-PP1-TOP (same p>=7,length4p-2 avoider,SOME NF k=p+1,kappa-hat=p-2) is impossible; its rotation-pair conclusion is vacuous only there. This neither accepts the ROT-PP1 proof nor supplies its other P/U/diagnostic statements, and excludes no multiset by itself outside that cell.

Together with separately accepted PP1-EXCL, the two top terminal k=p+1 cells kappa-hat=p-2,p-1 are excluded. Lower kappa-hat, other k, o_F>p assembly, reflection rigidity, unrestricted INV* and full ordered Olson remain open. No p=5, existence, novelty/priority, Lean or human-referee claim.
