# f123: independent finite actual-block review

Observed native clock before creation: `2026-10-28T20:05:45-0700 PDT`.

## Result and limits

**Finite distinction confirmed for the four specified words**, with exact reflection-only product distributions and full-token cyclic block/graph calculations. For `p=11,13,17`, the words also have nonzero rotations, only empty/singleton actual rotation gaps, and raw matching at most `p-3`; all have actual `(o_F,e_F)=(p+2,0)` and no identity among their `2p`-reflection selectors. Thus these concrete instances refute an unconditional lift from those actual block counts to a reflection-only identity even when those separately enumerated raw conditions hold. At `p=7` the same block/REF distinction holds, but the matching is `5>p-3=4`; it is **not** a lower-matching example.

This is finite validation, not a proof of the stated all-prime family, a full `L_RES` classification, or an original Olson closure/counterexample. Actual mixed `2p`-identity selectors were independently found in **all four original words**, so none of these four words is a counterexample to the original ordered identity-selection property. No human, independent-family, formal/kernel, priority or novelty conclusion is claimed. The entire f111 adoption and all its application/profile/floor/selection/confidence consumers remain **withdrawn and HELD/ZERO/NONINPUT**; neither the old review nor any fragment or control is credited here.

**SEL dependency:** The frozen f123 excerpt does not supply the complete literal definition of the named SEL predicate. For each instance this review verifies exactly that the zero reflection occurs `2p-1` times and that actual `Z r Z` triples occur at original indices `[0,1,2]` and `[2,3,4]`, with nonzero rotation `r`. The correction reports that these conditions imply SEL coverage, but that named predicate import is **not independently established here**. In particular, the report does not infer membership or nonmembership in full `L_RES` from SEL. The direct original mixed identity selectors are independently verified without that dependency. No additional source access was authorized.

## Frozen inputs and execution

The manifest and all seven listed inputs were read in the declared order; the withdrawal and fatal correction were read before the other mathematical inputs. Full SHA-256, byte and LF counts matched before reading and again during the finite diagnostic. The script read the author code as pinned bytes only; neither author checker was imported or executed. No held f111 mathematical material was used.

| Input, in order | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `manifest-v1.json` | `71777b4b6013d9775a9fd78e1ea6b27602f2e707a9d903cd19cabee504155e39` | 3849 | 60 |
| mandatory withdrawal | `f38d40d612caffc0cb305d96c3b9651816a5da5ab6ae36f939d6dab384dc27f4` | 3755 | 38 |
| fatal correction | `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e` | 9278 | 92 |
| literal definition excerpts | `efcc70ab455c6afed065e2be0967b950668e279cf696893a93089e380f1b115d` | 4870 | 61 |
| author full-word checker, not executed | `2e6b9d6151c901d694eef36130e2623feb7d23c9bead86a3d0b7b54472f58425` | 3923 | 102 |
| author audit, not executed | `2983b5fbadbaf45d0006d8cbefea60a2f779353f4628b1d48e3c9984fe8b72a5` | 3623 | 100 |
| first author receipt | `90b0342741902ca88390f80723b7a47771d5385a6108cffd76fbd9bf82f43223` | 2969 | 202 |
| second author receipt | `1a885bada1cfd8cdfd6438bcf5a845d63742a6bbc43b101f9d3bf7c897e0682d` | 2304 | 146 |

A fresh standard-library diagnostic constructed each full word. Its process actually exited `0`, with empty stderr, at `2026-10-28T20:04:03-0700 PDT`. A separate original-word mixed-selector reachability control actually exited `0`, with empty stderr, at `2026-10-28T20:05:22-0700 PDT`. Both use exclusive output creation and retain their observed command, clocks, output hashes, stdout and stderr in the following same-directory artifacts:

| Artifact | SHA-256 | Bytes / LF |
|---|---|---:|
| `finite-check-v1.py` | `ae44a7b0beda67dc82f3999ba88e972c4624618e7b900c1c39d16bca3dc8c21c` | 21363 / 462 |
| `finite-results-v1.json` | `8107905a7fc10830aa607ff3f1854940ce542b56f728c6f82f611b60776c8375` | 84284 / 4158 |
| `finite-run-receipt-v1.json` | `8baba2a28affe5d0fbc0888a66f657d5546df215753709baf3326dea802eade4` | 1561 / 24 |
| `finite-mixed-controls-v1.py` | `0e8e51ff8136000e39826ab3b4010cfd75ccdaa18e2ba24a2eae91dfa01f47c6` | 5009 / 121 |
| `finite-mixed-results-v1.json` | `691becefab9ac432ecf0311067f56c38091b3dbf48ab885850209faa99326910` | 4741 / 295 |
| `finite-mixed-run-receipt-v1.json` | `7a76ee9acfe675db8b6717fb388cbf461eb1ce768a0d8f690eb201d4dbea5cb9` | 1582 / 24 |

## Exact finite observations

Write a token `(a,b)` for `r^a s^b` in `⟨r,s | r^p=s^2=1, srs=r^-1⟩`. The directly constructed full word is

`Z r Z r Z^(2p-3) r (T_1 r) ... (T_(p-2) r) T_(p-1)`,

where `Z=s`, `T_j=r^j s`. The result artifact records the full indexed tokens, actual block positions, projected run positions, every cyclic raw gap, graph matching witnesses, and the full exact product-count distributions. Actual blocks are obtained from full-token cyclic predecessor boundaries, whereas projected runs are separately calculated only after filtering out rotations. Edges are formed from each actual cyclic reflection gap iff it is occupied or its endpoint values are unequal; exact maximum matching uses a skip-or-match vertex-subset recurrence, independently of the component-size formula.

| p | N / F / R | Actual odd/even | Projected odd/even | Raw components | Edges / exact matching | `ν≤p−3` | All original-index `2p`-reflection choices |
|---:|---:|---:|---:|---|---:|:---:|---:|
| 7 | 27 / 19 / 8 | 9 / 0 | 7 / 0 | path of 10; 9 isolates | 9 / 5 | no | 11,628 |
| 11 | 43 / 31 / 12 | 13 / 0 | 11 / 0 | path of 14; 17 isolates | 13 / 7 | yes | 20,160,075 |
| 13 | 51 / 37 / 14 | 15 / 0 | 13 / 0 | path of 16; 21 isolates | 15 / 8 | yes | 854,992,152 |
| 17 | 67 / 49 / 18 | 19 / 0 | 17 / 0 | path of 20; 29 isolates | 19 / 10 | yes | 1,575,580,702,584 |

For each row the exact support of the selected `2p` reflections is precisely the rotations `{r,r^2,…,r^(p-1)}`; its identity multiplicity is zero. A right-to-left full-group DP **counts** every original-index subsequence, selecting or omitting each reflection exactly once; row totals are checked against `binomial(F,k)` for every `k≤2p`. This is an exact compressed recurrence, not a claim that the larger combinations were individually enumerated. As an independent small control, all 11,628 original-index `p=7` reflection choices were individually multiplied and exactly matched the DP's full residue-count distribution.

## Selector and mutation controls

- The exact specified **original** `p=11` selector, in 0-based full-word indices, is `[0,1,2,3,4,5,6,7,8,9,23,24,25,27,29,31,33,35,37,38,39,41]`. It has 12 rotations and 10 reflections; explicit left-to-right multiplication gives `(0,0)`, the identity. All 22 intermediate products are retained in `finite-results-v1.json`. Replacing index `0` by `28`, retaining 22 distinct ordered indices, changes the product to `(3,0)` and is rejected as nonidentity.
- The additional full-word reachability control finds a mixed identity for each original instance: in each case the actual original indices `0,...,2p-1` multiply to `(0,0)`. Each uses 2 rotations and `2p-2` reflections. Its individually replayed selectors and one-index nonidentity mutations are in `finite-mixed-results-v1.json`. These are controls for the original full words, not claims about SEL.
- A separate positive reflection-only control changes the first nonzero tail reflection to `Z` and selects the first `2p` actual reflection indices. Direct multiplication is identity, and the reverse DP counts exactly one identity selector in each modified instance. This verifies that the DP can detect an identity; it is not attributed to the original REF-failing words.
- To expose the precise actual/projection error, move the occupied rotation between equal reflection vertices `0,1` into the originally empty equal gap between vertices `2,3`. The complete reflection projection and exact reflection product distribution remain unchanged. In each case actual zero-block lengths change from `1,1,2p-3` to `2,1,2p-4`, so actual `(o_F,e_F)` changes from `(p+2,0)` to `(p,2)`. At `p=11`, the raw components change from a 14-path plus 17 isolates to a 12-path, a 3-path and 16 isolates; the exact matching remains 7. Thus neither projection nor matching alone determines the actual block profile.
- For cyclic word `[Z,r,T_2,Z]`, the equal endpoint letters across the array boundary form one length-2 actual block: correct odd/even counts are `1/1`, whereas the deliberately wrong linear-cut interpretation gives `3/0`. The empty equal wrap gap has no raw edge. In `[r,Z,T_2,Z]`, the equal wrap gap contains rotation index `0` and **does** have a raw edge.
- For `[Z,Z,r,Z,T_2]`, the correct cyclic edge-presence vector is `[false,true,true,true]`. Incorrectly treating all empty gaps as occupied yields `[true,true,true,true]`; incorrectly retaining only occupied gaps yields `[false,true,false,false]`. Both wrong interpretations are distinguished explicitly, including unequal endpoints at empty gaps.
