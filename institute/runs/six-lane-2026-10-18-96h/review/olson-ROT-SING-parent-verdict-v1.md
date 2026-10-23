# Olson terminal k=p singleton endpoint: ROT-SING

Recorded at 2026-10-19T12:25:13-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL**, written mathematics relative to the accepted normal form, CT at its explicit full scope, GRX and classical Cauchy-Davenport. No Lev, S(p), (S1), ONE-SHORT-LS or pending lemma is a premise. This does not accept reflection rigidity, INV*, an o_F assembly or ordered Olson.

## Exact accepted statement

Primep>=7. Let w be an avoider of length4p-2 over D_(2p), with no identity2p-subword in increasing original index order. If SOME admissible normal form has terminal k=p and kappa-hat=p-1, then the rotation multiset of w is exactly **rho_c^(2p-1) rho_-c^(p-1)** for a nonzero c. In particular all rotations lie in one nonzero pair. No hypothesis on o_F(w); no existence of such avoiders asserted; p=5 not claimed.

## Frozen text and mandatory overlays

| Item | SHA256 |
|---|---|
| [Original review freeze](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ROT-SING-review-freeze-v1.json) | `e8ae90a285013c66e24e8b6a12eb306d35bd9fd2ab17f5c0f8646a8b5103acf1` |
| [Proof v2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/terminal-p-singletons/proof-ROT-SING-v2.md) | `ae5feaa1cd99aad9d2c0c35d1521ec27c3a1e5516225b102b4cb4bb793a4b1f1` |
| [Corrected second-family freeze](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ROT-SING-claude-v2-freeze-v1.json) | `10d65c6d984530dc7f9a2a1964a96f9b098de92d8be5cd2cf46bca04b175e868` |
| [Parent erratumv1](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ROT-SING-parent-erratum-v1.md) | `aad62a162f1fb25cc786ea0b96f1ceaeacf8cad8532bd16a36c15058d612d25b` |
| [Parent erratumv2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ROT-SING-parent-erratum-v2.md) | `ef93d8c1476e3a28071325c770c36f54ad4789d0c75fa57e6bee029f7f3a200b` |

Read both overlays after the immutable proof. Only commentary/wording/scope notes change: the particular selection family is not every possible selection.

## Reviews

- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ROT-SING-codex-v1.prompt.stdout.txt) `e6fc106e0d2a7fbfcff1e5b0c73e5e3352b7dc1d1e22ee111d30026272a3383e`: gpt-6.1-sol/max/read-only, main/strengthened conclusion ACCEPT; whole file ACCEPT-WITH-FIXES,0F/0M/1commentaryMINOR fixedbyv1.
- [Claude](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ROT-SING-claude-v2.prompt.note.md) `f53a8a78d056177cef70c76949adea85e77ca5999e1c9bfec96c45683c97ee0a`: claude-opus-5-5/max/no tools, main/strengthened conclusion ACCEPT,0F/0M/4nonblockingMINOR fixedbyv2. All interfaces in scope; both selections independently re-derived from the group law.

## Parent checks

kappa-hat=p-1 gives H-hat=0, every terminal block length1, F=p,R=3p-2. The all-plus pattern excludes a2p rotationzero-sum. CT at n=p-2 has |Y|-n=2p and truncated total<=2p-4. Positiveexcess excludeszeroheavy; oneheavy would give2p copies; twoheavy exhaustthebound and multiplicities are2p-1,p-1.

In any proper arc one side has at leastp dominant a-letters. Omit exactlyp rotations (om+y+z'=p) to select2p-2 rotations andthetwo arc-boundary reflections. The signed sums are D-[(a+b)y+(a-b)z'] or D+[(a+b)y+(a-b)z']; ifa+b!=0, both coefficient directions are nonzero and Cauchy-Davenport gives allp residues since beta_++beta_-=p-1. This contradicts avoidance, so b=-a and a!=0. Cyclic cut changes conjugate the selectedproduct, preserving identity and original linear order.

## Boundaries

NF and CT remain importedwritteninterfaces; this is not a fresh kernel/replay of their transitive bodies. Prior records carry no computer-assisted premise for these inputs, and no new finite computation is used. The classical Cauchy-Davenport theorem is imported. No Lean, human-referee or priority/novelty claim. Together with the accepted ONE-SHORT-LS it discharges the two formal pending premises of candidate ASSEMBLY-P at their exact scopes, but ASSEMBLY-P still requires its own second-family verdict and parent review; no automatic word-class promotion.
