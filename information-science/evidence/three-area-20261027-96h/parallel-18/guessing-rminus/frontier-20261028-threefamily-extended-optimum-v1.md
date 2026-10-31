# The exact star relaxation after additional tested entropy cuts

**Status: WRITTEN with exact rational primal/dual and independently structured finite scans; scientific review of the universal inequalities and source-theorem interpretations is pending.** This is a separate, unadopted extension of the LP packets; it does not modify f110 or its frozen review inputs. It establishes no new original-graph guessing-number upper bound or entropy realization.

## Exact LP scope and result

The underlying `30,719`-coordinate star LP is the pair of full 14-variable Shannon/copy systems `(X,U,V)` and `(X,U,W)` sharing all nonempty `(X,U)` entropy coordinates, with source FDs, symmetry, caps, and the two seven-row conditional-independence families described in `frontier-20261028-crossbranch-star-optimum-v1.md` (SHA-256 `1fb4cb0a74fd288e7fd96aaa2aba50b21901cd4385fa845ba28aa4a1656a54bf`). No Shannon rows mixing `V` and `W` are included.

Add precisely these inequalities:

| Family and substitution scope | Exact instances checked at the primal |
|---|---:|
| First 16-term gluing inequality: every ordered choice of four distinct original active variables and nine singleton `V`/`W` auxiliary pairs | 45,360 |
| Second 18-term gluing inequality: every ordered choice of five distinct original active variables and nine singleton auxiliary pairs | 272,160 |
| Third 18-term gluing inequality: every ordered choice of seven distinct original active variables and nine singleton auxiliary pairs | 5,443,200 |
| Five-variable gluing inequality `Psi`: all pairwise-disjoint nonempty original-variable role blocks with optional disjoint conditioning | 67,609,080 |
| `Psi` on cross-copy singleton auxiliary pairs, with nonempty disjoint original blocks `C,R,H` and conditioning the remaining originals | 7,870,500 |
| Named `F_n`: all disjoint original block substitutions modulo `A/B`, all positive `n` | 13,729,980 |
| The two pinned 2026 source families: all stated disjoint original-block/conditioning substitutions modulo `A/B`, every finite staircase / positive `k` | 47,534,520 |

All gluing inequalities are valid for entropy laws by the conditional-product argument in the separately pinned proofs; their independent scientific review is pending. The 2026 theorem proofs retain the source-review boundary in `frontier-20261028-five-variable-source-screen-v1.md`. The exact LP statement itself concerns the listed linear constraints, independently of whether a graph-theoretic improvement is inferred.

The exact optimum of this **specified** augmented LP remains `1847/276`. The primal uses `frontier-20261028-crossbranch12-exact-candidate.json` SHA-256 `1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739` and `frontier-20261028-crossbranch13-threefamilies-exact-candidate.json` SHA-256 `e31643a10db9556bf8394d7b7d2a9cf1b20fa9380bf3da98b57bd2c655ca8474`, agreeing on all `2,047` nonempty `(X,U)` subsets. Both full 14-variable elemental/copy systems and the source signed dual are independently checked. Exact scanners bind the further listed instances to this same primal, with minimum slacks zero except the third gluing family minimum `1697/1725000`.

The old star and all-first-family star points are separately excluded from projected almost-entropic vectors by different gluing inequalities, but their auxiliary values differ from this primal. Passing these families does **not** establish that this new primal is entropic, almost-entropic, or extendible to the full 17-variable Shannon system. It also does not rule out other gluing/copy inequalities, overlapping `Psi` substitutions, different conditioning patterns, or an actual positive-balance-gap FD law.

## Source-order corrections and evidence

* Read `frontier-20261028-full-source-lp-optimum-v1-erratum-1.md` SHA-256 `c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9` **before** its frozen source packet: the publisher cross-branch remark is Remark **5.4**, not 3.8.
* Read `frontier-20261028-third-cross-cut-independent-label-erratum-v1.json` SHA-256 `e6b01fe0362c99ad0a35dff4aea4a16bda7f0586a38144d1110c152913f7ed7a` **before** `frontier-20261028-third-cross-cut-independent-result.json`, SHA-256 `c11773bfc9e3106ace76b8553fd13d308875951848e9198f5d460f332665a76c`: its limits text says “second” but the checked inequality is the **third**. The numerical count and minimum are unchanged.
* Exact primal/dual core binder `frontier-20261028-crossbranch-threefamilies-combined-check.py` SHA-256 `31db30219cbb9d9769739cbf8d9736721a74dc94217d22fde507b6a651eaa398`; receipt SHA-256 `e9f004685bb2a7eee151d5803e347a954bdcb451eb2a9a41b05076d491145ddf`.
* Extended receipt binder `frontier-20261028-threefamily-extended-binding.py` SHA-256 `5b2c4711b72ae6dbcd433b74f9d65094cfeb43c9c54c510c57bb96033c9c31f4`; receipt SHA-256 `0e7fc001ab106169e0ef60cd080abafc50ed840a9eb0dc531a8e5179e321a9c6`. It reads both required corrections first, pins every producer/replay receipt and the common primal, checks exact coverage/minima and rejects four in-memory mutations. It binds prior checks; it does not itself re-enumerate millions of rows.
* The independent cross-`Psi` scan `frontier-20261028-psi5-cross-copy-round3-independent.py` has SHA-256 `13cfb25f92994801c37aaa62015301156c90d228ba4efcb14ac34698edeaacff`, receipt SHA-256 `ecad42eb005f40f2e08387627b82e786ccc99558ac76aea61288e88e05fba64a`. All other paired scan/dual receipts are listed in the binder source and predecessor packets.

No cross-model review, proof-assistant formalization, literature-novelty clearance, or true entropy-law witness has been obtained for this extension.
