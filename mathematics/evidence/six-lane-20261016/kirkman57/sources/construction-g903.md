# LKTS(87): self-contained construction note

## 0. Claim, evidence level, limits

**Claim.** There is a large set of Kirkman triple systems of order 87: 85 KTS(87)
on one 87-set whose block sets partition all 105,995 triples. An explicit
labelled certificate is pinned below. **Evidence level:** finite-exact
(computer-found, checked by independent programs). **Validity rests only on the
certificate check (§6)**; §§3, 7, 8 explain the construction. Not peer
reviewed; priority: no earlier construction located (parent priority screen,
`institute/runs/six-lane-2026-10-16/review/lkts57-87-priority-audit.md`).
Earlier 87-models in the prior dossier (cyclic Z85+2, C29 on Z29×Z3) used other
point structures.

## 1. Definitions

As in `construction-g513.md` §1 (STS, KTS, LKTS; v−2 = 85 constituents, 43
classes of 29 triples each).

## 2. Points

`X = {∞} ∪ Z43×{0,1}`; `(x,j)` is the integer `43j+x`, ∞ is 86. In Z43, 9 has
order 21; ω=9^7=36 (order 3), λ=9^3=41 (order 7).

## 3. Group

    τ:(x,j)↦(x+1,j),   m:(x,j)↦(9x,j),   ∞ fixed.

`G=⟨τ,m⟩≅Z43⋊Z21`, order 903. Every non-translation fixes exactly
`{∞,(c,0),(c,1)}` for one c.

## 4. The three base systems

(`sources/appendix-lkts87-orbits.md`, self-checked by `code/make_appendix.py`.)

| Base | block set | resolution |
|---|---|---|
| S0 | ⟨m⟩-orbits of 63 representatives (58 of length 21; four of length 7 = the 28 ω-cycles `{e,36e,6e}_j` (ω²=6); the line `{∞,(0,0),(0,1)}`) | images under ⟨m⟩ of 3 classes (orbit lengths 1, 21, 21); the fixed class is the line plus the 28 ω-cycles |
| B1 | τ-orbits of 29 representatives | the 43 τ-translates of one parallel class |
| B2 | τ-orbits of 29 representatives | the 43 τ-translates of one parallel class |

B1 contains the τ-orbit of `{∞,(0,0),(16,1)}` and B2 that of `{∞,(0,0),(2,1)}`
(cross differences of opposite quadratic character, as forced by
`framework-2q1.md`).

## 5. The large set

Order G lexicographically; for each base with stabilizer H (⟨m⟩ for S0, ⟨τ⟩
for B1, B2) take the least element g of each coset gH and the system g(base)
with the image resolution: 43+21+21=85 KTS(87). G permutes the 85 block sets;
the transported resolutions are not G-invariant.

## 6. Pinned files, reproduction and verification

| Object | Path | SHA256 |
|---|---|---|
| Certificate | `evidence/lkts87-g903/lkts87_g903.txt` | `65ab29ae6d24545c4ed41c3a4ea027becdf497b6810384b728379cfd0cae273e` |
| Seed (JSON) | `evidence/lkts87-g903/lkts87_g903_seed.json` | `d967896610216e16f70981e762b80c533d1f597b8c653da95474801bd3f16cef` |
| Expander | `code/expand_seed.py` | `f776c276df903b8e3de5de8b58144617c5ac2ecadf6515290c03c164b4518d4e` |

Seed format as for 57, plus `"v": 87`. From the lane directory:

```sh
python3 code/expand_seed.py evidence/lkts87-g903/lkts87_g903_seed.json /tmp/r87.txt evidence/lkts87-g903/lkts87_g903.txt
shasum -a 256 /tmp/r87.txt                                   # 65ab29ae…273e
python3 code/check_lkts57.py evidence/lkts87-g903/lkts87_g903.txt                      # lane, Python (any v)
python3 ../../../kirkman-large-sets-57-87/work/check_lkts.py evidence/lkts87-g903/lkts87_g903.txt   # prior dossier
clang -O2 -o /tmp/chk code/check_lkts57.c && /tmp/chk evidence/lkts87-g903/lkts87_g903.txt         # lane, C
```

Receipts: `evidence/lkts87-g903/{lane-checker-receipt.json,prior-checker-receipt.json,c-checker-receipt.txt}`;
16 mutation/positive controls: `evidence/lkts87-g903/mutations/mutation-results.json`.
Parent: independent checker and seed replay (run directory `review/`).

## 7. How it was found

`PYTHONHASHSEED=0 python code/g87_full.py DIR 20` (Kramer–Mesner over G-orbits,
kissat 4.0.4, symmetric base resolutions): 61 s; two runs (`code/runs/g87_full1`,
`g87_full2`) produced the byte-identical pinned file.

## 8. Lemma dependencies (explanation only)

`sources/automorphism-lemmas.md` Corollaries 87-A–C and Proposition 87-D:
any LSTS(87) has an odd-order automorphism group; for this G the orbit
structure 43+21+21 and the symmetric class structures are forced. The general
reduction for v=2q+1 is `sources/framework-2q1.md` (Theorem A, Proposition B).
None of this is used to verify the certificate.

## 9. Limits

A single finite object; no family theorem is claimed (the 2q+1 framework is
proved only as a reduction; packages are known by computer for q=19, 31, 43 and
impossible for q=7). "New" means only that no earlier LKTS(87) was located.
