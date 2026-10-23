# info-p0403: closure of the 252 screened fixed-half classes

**Partial book result; the balanced nine-variable maximum remains 240 or 242.** This continuation excludes all 252 fixed-half classes that **passed** the epoch-2 necessary-condition screen. It does not prove global nonexistence, and it supplies no balanced NL242 witness. No novelty or Lean-verification claim is made.

## Exact new result

For each pinned `(source,normal)` pair, fix the 256 source values on `normal.x=0`, permit arbitrary values on the other 256 points, and then permit any linear output addition. Every formerly unresolved class has exact balanced maximum **240**, attained by its original balanced NL240 source.

| New exclusion stage | Classes |
|---|---:|
| Quadratic square-residue bit plus Parseval and a necessary zero | 152 |
| Odd-weight autocorrelation residue plus energy budget | 71 |
| Canonical spectral signs plus inverse-transform energy/L1 bound | 28 |
| Complete correction-parity coset enumeration | 1 |
| **Resolved / UNKNOWN / unattempted among the 252** | **252 / 0 / 0** |

The accepted old screen excluded the other 31,492 listed classes. Thus all **31,744 listed `(source,normal)` classes** are closed when that imported result is combined with this new proof. These overlapping families are not a distinct-function count and are not all degree-eight Boolean functions.

The old three proof-capped attempts remain `UNKNOWN`; they are not relabeled UNSAT. The new result is a different complete necessary-condition proof. Experimental Z3 LP/exact attempts were superseded without a certified solver result; their incomplete SMT inputs remain in `results/`, and no solver status supports a negative claim.

## Attribution and priority

The 2-adic/canonical-sign tools are **not claimed new**. Wang–Lou–Wang, [arXiv:2610.17871v1](https://arxiv.org/abs/2610.17871), proof of Theorem 1, equations (31)–(32), already normalize an odd spectrum by an affine sign character to two modulo eight and use the quadratic bit `(W-2)/8 mod2` with a pointwise majorant and Parseval. Our `J_H` is exactly that quadratic bit of the canonical spectrum. Their Lemma 4 already applies the paired-half capacity identity with Parseval. The accepted elementary `{240,242}` restriction is also not presented as a novel theorem. The contribution claimed here is the explicit, independently replayable finite exclusion of this fixed-half corpus, using these known tools and the complete final correction-parity computation. The preprint's unrestricted covering-radius theorem is **not** imported as a premise. Novelty of any specialized cap-28 application remains unestablished.

## Mechanism and independently checked correspondence

For odd-weight eight-variable half spectra `G,H`, the full Walsh bound is exactly `|G(a)|+|H(a)|<=28`; a full Walsh zero is equivalent to `|G(a)|=|H(a)|` somewhere. The latter permits explicit balancing by a linear output shift. The complementary half must have odd weight, so its coefficients are two modulo four.

Three useful structural facts replace repeated truth-table swap searches:

1. `J_H(a)=(H(a)^2-4)/32 mod2` is a quadratic Boolean function. Wherever `|G|=26`, it must vanish. The forced-zero evaluation ranks are 31–36 in the 37-dimensional quadratic space, leaving only 2–64 possible quadratics per class.
2. The signs of an odd spectrum, up to an affine sign character, are fixed by its magnitudes: take `K=m` for `m=2 mod8`, and `K=-m` for `m=6 mod8`. A genuine spectrum has inverse character sums exactly `+256` or `-256`.
3. In the last class, source 96 / normal 511, the maximal canonical spectrum gives an exact correction budget of 56. Mixed differences modulo 32 force its 166 active correction parities into an affine binary space of rank 147 and dimension 19. All **524,288** patterns are exhausted: the smallest unavoidable local correction cost is **140**, attained six times. Since `140>56`, no completion exists.

The complete elementary proof and finite-domain correspondence are in [`proof.md`](proof.md). `code/check.py` imports neither producer nor solver code: it reconstructs fixed halves with a separate coordinate implementation, uses direct character sums, support-moment formulas, opposite elimination pivots, explicit mixed-difference corner sums, and a different parity enumeration order. It compares the entire cost histogram, not just a producer's minimum or a solver's CNF verdict.

## Input pin, indexing, and deduplication

The byte-for-byte staged epoch-2 input is `inputs/slice-screen.json.gz`:

`SHA-256 200a4997f0a1bcc5c63eaf53f2602118395950ddb951b5bee43c23c92f32cf6d`.

It was read programmatically as JSON; survivors are exactly records with an empty `rejections` list, checked against `unresolved_case_records`. It contains all 124 indexed source tables, their hashes, the 31,744 case definitions, and the exact 252 survivors. Original path:

`institute/runs/hard-2026-10-15/problems/info-p0403/attack-e2/results/slice-screen.json.gz`.

All bits use `bits[x]=f(x)`, `x=0,...,511`, `x_i=(x>>i)&1`. The eight-variable slice basis and the complementary-coset origin are explicit per class in `results/screen.json.gz`. No input permutation is implicit.

There are **154 literal absolute-spectrum arrays** among the 252 classes. The identity spectral-coordinate map is a rigorously checked equivalence for equal arrays. A mapping back to all 252 is retained. No more general EA/affine equivalence is assumed, and no claim says the 154 groups are mutually inequivalent. Every class was processed explicitly, so deduplication cannot hide an unattempted case.

## Replay and controls

Only Python 3's standard library is required for the proof/checker. Z3 was used only in the superseded exploratory script and is not needed for replay.

From this directory:

```sh
python3 code/check.py
```

To regenerate the producer certificates from the pinned input (not necessary for independent replay):

```sh
python3 code/screen.py
python3 code/parity_certificate.py
```

The single final verification receipt is `result.json`. Its commands include the direct checker and three **expected-to-fail** corruptions:

```sh
python3 code/check.py --mutate-spectrum
python3 code/check.py --mutate-certificate
python3 code/check.py --mutate-final-certificate
```

Controls include deterministic genuine odd truth tables checked by direct sums; all 252 original balanced bound-32 planted completions; a published unbalanced bound-28 NL242 table that genuinely satisfies the paired-spectrum constraints but has no Walsh zero; and a bound-32 planted completion of the final class that passes the exact mixed-moment correspondence. The published bound-28 table has support XOR zero and even-weight halves: it is a positive control for the general paired-spectrum identity, **not** for the odd-spectrum lemmas. An initial control mistakenly expected an odd slice from that table and failed; `results/failed-final-replay.json` preserves the failure, and only that fixture assumption was corrected. Corruption tests change a recorded spectrum by eight, invalidate a quadratic certificate, and alter a final mixed-difference certificate. Missing files are not used as negative controls.

The final receipt records actual return codes, elapsed times, input/source/certificate hashes, controls, and exact scope. `results/check.json` contains the independent numerical audit. No build/lint/formatter or old accepted computation is rerun just for reproduction. Working files and prior snapshots are preserved; no old records or navigation are edited.

## FRONTIER and engine seed bundle

**FRONTIER: PROOF-OBLIGATION / GLOBAL-CONSTRUCTION-OR-EXCLUSION.** These 31,744 fixed halves are exhausted. Repeating their old SAT timeouts or balanced swaps has no remaining claim-changing obligation.

The high-value next obligation is to choose genuinely new degree-eight halves outside this corpus, using the residue/canonical hierarchy as an early exact feasibility screen, or derive a universal theorem constraining pairs of odd eight-variable spectra. The mechanism has an exact positive target: two odd half spectra satisfying `|G|+|H|<=28`, with equality of their magnitudes at at least one index. Any construction must reconstruct 512 indexed bits, exhibit the linear balancing shift, and independently pass both direct 512-character sums and a FWHT, with weight 256 and all magnitudes at most 28. A failure in this restricted corpus cannot stand in for a global theorem.

`seed-bundle.json.gz` provides the explicit coverage mapping, input pin, completed classes, the finite-domain mechanism, controls, and a concrete requeue obligation. `handoff/` is a compact self-contained copy of only the new load-bearing proof/checker/data plus a manifest; it excludes incomplete solver experiments and dependencies. The parent owns any engine requeue and shared records/navigation.

## Later results in this evidence root (pointer)

Work after the corpus closure lives in [`quadratic-distance/`](quadratic-distance/README.md). It contains a universal residue necessary condition: the intrinsic quadratic of a balanced peak<=28 target has one of eight rank/weight types. Under separately reviewed lemmas, [`quadratic-distance/zero-geometry/`](quadratic-distance/zero-geometry/README.md) excludes type (rank4,weight128) and proves that a nine-variable function with 1–3 Walsh zeros has NL<=240. Seven types remain open, so the balanced NL242 question is unresolved. [`quadratic-distance/remaining-types/`](quadratic-distance/remaining-types/README.md) holds unreviewed partial results on those seven types. The gates are model reviews only, not peer review or formal verification. The methods are prior art (Wang–Lou–Wang, Lou–Xu–Wang), and novelty is unestablished. The corpus result, certificates and handoff above are unchanged.
