# Same-gap ordered selector — bounded independent verification addendum

Owner **MathOlson-2-2**. Actual native `/bin/date` before this write: **Wed Oct 28 17:31:29 PDT 2026**.

This is an ADDITIVE verification record for the immutable69LF candidate `frontier-20261028-dihedral-same-gap-pair-selector-v1.md`, SHA256 `4e53b8fa3eb8b1050a8cd5d8922edcfc363a7ad228e9e83c3c2553673c955765`. That candidate's statement that no check had yet run was true at its own17:26:19 observation and is not backdated or edited.

## 1. Scientific computation actually performed

After finishing and returning the priority f30 review, I wrote TWO separate standard-library Python programs in this root:

| Artifact | SHA256 | Function |
|---|---|---|
| `frontier-20261028-dihedral-same-gap-experiment.py` | `0664ca9c2bc1cb03f3cc8cdf4ddee9fdc1653773b49307c5bbe3eb366c6a1077` | Generate/reconstruct actual words, gap pairs, omissions and selectors |
| `frontier-20261028-dihedral-same-gap-checker.py` | `a5091f9cf8a616685ce6e417c01a0aaaf7f4fa6a1bbff7f4a5313e07c52247f9` | Independently replay source seed and check actual gap matching/cardinality/original products; no producer import |
| `frontier-20261028-dihedral-same-gap-results.json` | `1eea685f1a5b17a5ac303c15e1dd8dec559157103887fbad10877e827615f55b` | Complete compact saved actual words, gap pairs and selector indices |

Actual command, run once on completed code:

```text
python3 -B frontier-20261028-dihedral-same-gap-experiment.py --output frontier-20261028-dihedral-same-gap-results.json && python3 -B frontier-20261028-dihedral-same-gap-checker.py frontier-20261028-dihedral-same-gap-results.json
```

The producer returned `PASS_BOUNDED_SAME_GAP`; its deterministic seed is2026102804. The independent checker returned `PASS_INDEPENDENT_SAME_GAP_REPLAY` and confirmed the SAME result SHA above.

## 2. Actual finite scopes and outputs

The random corpus contained40 full original words for EACH of the following eight `(p,R)` domains:

| p | R | random words | satisfying the exact gap-pair hypothesis |
|---:|---:|---:|---:|
| 3 | 6 | 40 | 22 |
| 3 | 7 | 40 | 31 |
| 5 | 12 | 40 | 30 |
| 5 | 13 | 40 | 38 |
| 7 | 18 | 40 | 34 |
| 7 | 19 | 40 | 38 |
| 11 | 30 | 40 | 40 |
| 11 | 31 | 40 | 40 |

Thus **320** actual random words were replayed and **273** met the stated sufficient hypothesis. For EVERY pair of reflection positions in each qualifying word, the producer saved an actual increasing-index selector; it reported **9,654** such random-word/reflection-pair products checked.
Four separately specified structured-family instances at p=3,5,7,11 contributed145 more reflection-pair selectors. The independent checker verified all **9,799** saved selectors' exact2p cardinality, strict index order, same-gap unequal-exponent pair conditions, actual omitted occurrences and original group products.

The checker separately reconstructs each actual gap's exponent multiplicities and verifies that the producer's number of disjoint unequal-value pairs equals

`sum_g min(floor(r_g/2), r_g−M_g)`.

For every verified reflection pair it independently computes the set of attainable signed omission sums and checks that it is all F_p, then directly multiplies the selected original group elements. It does not merely check a formal sumset label.
A deliberately duplicated selected index was rejected for the intended `bad selector indices` reason.

For illustration, one p=5 structured word has R=12,F=7, four disjoint initial-gap pairs `[(0,1),(2,3),(4,5),(6,7)]`, and the saved selector for actual reflections8 and10 is the increasing zero-based index list

`1,3,5,7,8,9,10,11,13,15`.

The checker directly obtained the group identity for that original word. The complete word and every other checked selector are in the pinned result file.

## 3. What these checks establish — and do not

The bounded replay supports the correctness of the actual implementation, gap-pair criterion and original-index caller on the listed finite corpus. The random inputs are a diagnostic corpus, not a distributional claim.
The independently written script is a different implementation but the SAME model/harness, not independent-model-family or human review. It is not a formal proof and does not check all primes or all words.
The uniform all-p result rests on the written prime-field translation-growth and actual sign/omission proof in the immutable candidate. It still needs full scientific review before adoption.
No result here proves every word satisfies the gap condition, resolves the entire R=3p−3 or3p−2 band, produces an original avoiding word, or establishes novelty.

The latest owner direction authorized these bounded local scientific checks prospectively. Historical quarantine/failure records are not reclassified or accepted by this addendum. No external model/API, deletion, Git push, publication, secret or infrastructure mutation was used.

**END — same-gap actual-word check and limits.**
