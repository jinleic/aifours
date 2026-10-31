# R-minus: exact replay of Gürpınar’s published 1847/276 certificate

**Result and scope.** Two separately written same-harness checkers, using exact `Fraction` accumulation and separately scaled-integer accumulation, respectively, replay all **1920** source-PDF coefficient expressions for the original ten-vertex R-minus graph. Both classify every row as a valid entropy inequality or an equality from the explicitly transcribed original-graph/copy/symmetry premises, and both obtain the exact identity

```
weighted sum of all 1920 left-hand sides = H(X_1,...,X_10),
weighted sum of their right-hand sides    = 1847/276.
```

With the row directions and coefficients checked individually, this supplies an independently reconstructed computational proof route to the **already published** upper bound `gn(R-minus) <= 1847/276`. It is **not a tighter bound, new theorem, formal verification, independent human/cross-model review or novelty/SOTA claim**. Both implementations were authored in the same harness, use the same `pdftotext` source extraction, and use the same documented transcription of the source graph and copy protocol; shared-input/shared-author errors remain possible. The original publication, not this replay, has priority.

## 1. Source and provenance

The 2024 article’s Theorem 5.2 is in `public-sources/gurpinar-kybernetika60-2024-553-575.pdf`, SHA256 `373e8a2567fc7de9d40d0e5fabca9655cbb7b689a162005262b4f4d432bb46d8`. Its Appendix C links the author’s [Internet Archive certificate item](https://archive.org/details/anx-c-rmns-1847ovr-276crtfcte). The author-listed original files were fetched in this session, with actual local bytes pinned:

| Local source copy in this exclusive root | SHA256 | Bytes |
|---|---|---:|
| `frontier-20261028-gurpinar-annexc-original.txt` | `b0bd3f614397ed11edd475efdc4acb6e8f326c6722ede71d5a08760d84578b22` | 51890 |
| `frontier-20261028-gurpinar-annexc-original.pdf` | `8befddb0faba71dbae9221956939d883946649e07a261c036ff7514dfea9ec6b` | 100501 |
| `frontier-20261028-gurpinar-annexc-original.zip` | `09b3bcbd76be65257adba4a69ea5d26cc2cb686e2fdac7b5bb1963ef2a4e6fd0` | 106412 |

The ZIP contains exactly `AnnexC.pdf` and `Rminus1847over276certificate.txt`; both member byte strings equal the separately fetched PDF and TXT. The local SHA-1 values also matched the archive’s metadata at fetch time. No ZIP member was executed.

`pdftotext -layout` produced `frontier-20261028-gurpinar-annexc-pdf-layout.txt`, SHA256 `6ff906bb54ddf33e46d5bfcddf50ffa0680c0315e118d6530e6f13f36adc2ca5`. The strict second checker separately reran `pdftotext -layout` on the pinned PDF and matched the derivative **byte-for-byte**. It strictly consumed all 1920 PDF expression/coefficient records, matched each coefficient in order to the 1920 original TXT rows, and rejected unrecognized row syntax or names. This is a machine extraction/binding check; it is not a manual visual verification of every glyph on every page.

The 2024 paper’s graph figure was visually revisited on printed p570. The locally encoded labelled graph is the ten-neighbour transcription in `frontier-20261028-weighted-law-certificate-v1.md`, with 26 edges, 3–4 present and 9–10 absent. Each checker independently verifies the two specified vertex permutations preserve this encoded graph and generates their **eight-element subgroup**. No claim that this subgroup exhausts every graph automorphism is needed.

## 2. Exact constraint conventions

Write original variables `a,b,c,d,e,f,g,h,i,j` for vertices 1 through 10. The archive PDF uses auxiliary names `b'0`, `d'1`, `e'1`, `g'2`, `f'3`, `g'3`, `h'4`. The checked copy protocol is:

| Step | Fresh copy of | Conditioning base | Past before copy |
|---|---|---|---|
| 0 | `b'0` of `b` | `a d e f g h i j` | originals |
| 1 | `(d'1,e'1)` of `(d,e)` | `a b c f g h i` | originals |
| 2 | `g'2` of `g` | `a b c d e'1 f h i` | originals, `d'1,e'1` |
| 3 | `(f'3,g'3)` of `(f,g)` | `a b c d e h i j` | originals |
| 4 | `h'4` of `h` | `a b c d e f f'3 i j` | originals, `f'3,g'3` |

Steps 0, 1–2 and 3–4 are three branches on the same original marginal. These are the source Theorem 5.2 copies, with its differently numbered primes translated into the archive PDF’s names. In each step, sample the fresh tuple from the conditional law of the old tuple given the stated base, independently of the whole already existing past conditional on that base. This standard finite conditional-kernel construction preserves the past and supplies every checked marginal-copy equality and the checked conditional-independence equality. The three branches can be sampled conditionally on the original variables and then extended sequentially within each branch. Thus all 17 variables can coexist in one finite joint law; no cross-branch independence is assumed by the certificate.

The exact row classifications and counts agree across the two checkers:

| Classification | Count | Checked direction |
|---|---:|---|
| Conditional mutual information | 958 | nonnegative; certificate coefficient negative |
| Conditional entropy | 22 | nonnegative; coefficient negative |
| Original functional-dependence equality written as `>= 0` | 3 | zero under the graph FDs; coefficient negative |
| Original-graph automorphism equality | 456 | zero; coefficient may have either sign |
| Conditional-copy equality | 478 | zero; coefficient may have either sign |
| Original singleton entropy cap | 3 | `<= 1`; coefficient positive |
| **Total** | **1920** | **0 unrecognized; 0 coefficient mismatches** |

The CMI recognizer checks the actual set-union/intersection form, and the conditional-entropy recognizer checks actual subset inclusion. The three apparent reverse conditional-entropy rows are checked against the **exact original neighbour set** of the indicated vertex, not accepted as generic Shannon inequalities. Each equality is checked either as an original-set permutation under the verified subgroup or as a matching-marginal/conditional-independence relation generated by one of the five explicit copy steps. Caps apply to original singletons only.

Each displayed `>= 0` row has a negative coefficient, each `<= 1` cap a positive coefficient, and equality coefficients are unrestricted. Thus multiplying each actual row by its coefficient makes its weighted left-hand side at most its weighted right-hand side. The final three source cap multipliers are `191/138`, `743/276`, `361/138`, summing exactly to `1847/276`.

## 3. From the certificate to the actual arbitrary-decoder game

For any finite alphabet of size q and any deterministic full-neighbour strategy, let W be its winning set. If W is empty, the upper bound is immediate. Otherwise take X uniform on W: every original FD holds, `H(X_V)=ln|W|`, and every original singleton entropy is at most `ln q`.

To pay for the certificate’s symmetry equalities, take independent copies of the **whole** law, one per element g of the verified eight-element automorphism subgroup, and define the tuple-valued original vertex variable `Y_v=(X^{(g)}_{g(v)})_g`. Every original FD remains valid because each g maps neighbourhoods to neighbourhoods. For every original subset S, `H(Y_S)=sum_g H(X_{g(S)})`, so this entropy profile is subgroup-invariant; `H(Y_V)=8 ln|W|` and `H(Y_v)<=8 ln q`. This is independent whole-law tensoring, **not** an unproved mixture of FD distributions.

Add the finite copy branches of §2. Divide every entropy in the certificate by `8 ln q`: all equalities and nonnegative inequalities are homogeneous and every original singleton cap is at most 1. The exact weighted identity then gives

```
ln|W| / ln q <= 1847/276.
```

This is an all-q, all-full-domain-decoder upper-bound argument relative to the checked graph/source/row transcription and finite-copy construction. The existing type-class/supremum bridge is not required for this winning-set upper-bound direction. Neither this proof nor the replay asserts that the bound is optimal.

## 4. Independent implementations and mutation controls

- `frontier-20261028-gurpinar-certificate-audit.py`, SHA256 `2a13ac7bf692b835b6f6bb3509a98f0654ab917cae6807ae730ca8afea76f595`, uses exact Python `Fraction` sparse accumulation. Result: `frontier-20261028-gurpinar-certificate-audit-result.json`, SHA256 `09804654739b7b6494f8d791b714d642dd47f5607cafa8213d5bde8f86b42024`.
- `frontier-20261028-gurpinar-certificate-independent.py`, SHA256 `a15a4c8d637044d751f49927349c9efa9f963601f60eefabb261b75ad32eb4ed`, imports no first-checker code, uses a different strict full-expression parser and scales all rational multipliers to **integer denominator 79488**. Result: `frontier-20261028-gurpinar-certificate-independent-result.json`, SHA256 `b5c33e3f97f405eed9d6518cd714a25b6b9cae914cdd799089256339752b102b`.

The second checker performs six in-memory negative controls without changing the pinned inputs: dropped row → `ROW_COUNT`; flipped CMI weight → `INVALID_WEIGHT_SIGN`; zeroed cap RHS → `INVALID_ROW`; changed FD neighbourhood → `INVALID_ROW`; changed but still signed CMI coefficient → `WEIGHTED_IDENTITY`; wrong bytes → `INPUT_HASH_MISMATCH`. Each produced the intended rejection. The checkers' first results were observed at **17:17:47 PDT** and **17:19:40 PDT**, respectively, on 2026-10-28. No output is claimed from a cross-vendor checker or formal kernel.

**Remaining verification boundary.** Independently review the graph figure and variable/prime mapping, the complete copy protocol and mathematical caller, PDF text extraction fidelity, both checker implementations and controls. In particular, the original TXT row names have been matched to the PDF **coefficients by position**, but their internal names have not been independently decoded into the PDF expressions. The row proof uses the strictly parsed PDF expressions, not an assertion that TXT names alone are self-describing. The proof does not reclassify historical quarantine records or purport to independently verify a solver’s LP optimum.

**END.**
