# LKTS(57): self-contained construction note

## 0. Claim, evidence level, limits

**Claim.** There is a large set of Kirkman triple systems of order 57: 55 KTS(57)
on one 57-set whose block sets partition all 29,260 triples. An explicit labelled
certificate is pinned below. **Evidence level:** finite-exact (a computer-found
object, checked by independent programs). **Validity rests only on the
certificate check (§6)**; the group theory and lemmas in §§3, 8 explain how it
was found and why it is compact, and are not needed to accept it. Not peer
reviewed; priority: no earlier construction located (parent priority screen,
`institute/runs/six-lane-2026-10-16/review/lkts57-87-priority-audit.md`).

## 1. Definitions

An STS(v) is a set of 3-subsets (blocks) of a v-set in which every pair lies in
exactly one block. A KTS(v) is an STS(v) with a partition of its blocks into
(v−1)/2 parallel classes (each class partitions the points). An LKTS(v) is a
collection of v−2 KTS(v) on the same points whose block sets are pairwise
disjoint (equivalently, they partition all C(v,3) triples).

## 2. Points

`X = Z19 × Z3`; the point `(x,i)` is the integer `19i+x` (0…56). ω=7 has order 3
and ζ=4 has order 9 modulo 19 (ζ³=ω).

## 3. Groups

    τ:(x,i)↦(x+1,i)     ν:(x,i)↦(4x,i+1)     ρ:(x,i)↦(x,i+1)
    μ:(x,i)↦(7x,i+1)    μ':(x,i)↦(11x,i+1)
    γ_c:(x,i)↦(x+c·ω^i,i+1),   γ'_c:(x,i)↦(x+c·ω^(−i),i+1)

`G = ⟨τ,ν,ρ⟩ ≅ (Z19⋊Z9)×Z3`, order 513, transitive on X. Subgroups:
`P27=⟨ν,ρ⟩`, `F57=⟨τ,μ⟩`, `F57'=⟨τ,μ'⟩` (orders 27, 57, 57). The γ's are **not**
in G; they are extra symmetries of individual base systems only.

## 4. The five base systems

Each base is a KTS(57) given in the seed as 28 classes. Compactly
(`sources/appendix-lkts57-orbits.md`, self-checked by `code/make_appendix.py`):

| Base | block set = orbits of … | resolution = images under … of … |
|---|---|---|
| S0 | 22 orbit representatives under P27 | 4 classes under ⟨ν⟩ (orbit lengths 1,9,9,9) |
| B1 | 4 representatives under ⟨τ,μ,γ_1⟩ | 8 classes under ⟨μ,γ_1⟩ (orbit lengths 1,3×6,9) |
| B2 | 4 representatives under ⟨τ,μ,γ_2⟩ | likewise with γ_2 |
| B3 | 4 representatives under ⟨τ,μ',γ'_1⟩ | likewise with μ',γ'_1 |
| B4 | 4 representatives under ⟨τ,μ',γ'_2⟩ | likewise with μ',γ'_2 |

Example: B1 is the union of the ⟨τ,μ,γ_1⟩-orbits of `{(0,0),(1,0),(10,2)}`,
`{(0,0),(2,0),(6,2)}`, `{(0,0),(4,0),(16,1)}` (171 blocks each) and
`{(0,0),(1,1),(8,2)}` (19 blocks).

## 5. The large set

List G in increasing lexicographic order of its permutations (as tuples of
images of 0…56). For each base with stabilizer H (P27 for S0, F57 for B1, B2,
F57' for B3, B4), take the least element g of each left coset gH; the
constituent is g(base) with the image resolution. This gives 19+9+9+9+9=55 KTS.
G permutes the 55 **block sets**; the transported resolutions are **not**
G-invariant (the parent's action audit counts the exceptions).

## 6. Pinned files, reproduction and verification

| Object | Path | SHA256 |
|---|---|---|
| Certificate | `evidence/lkts57-g513/lkts57_g513.txt` | `09a9d8ca0602ed28541e170ada7f096871311c29fd4515b6fea3e25f72b05f09` |
| Seed (JSON) | `evidence/lkts57-g513/lkts57_g513_seed.json` | `7c032dd406017a8cb17018ece32fcc2532db05c7d7fc4224a05cbb022df7cbb8` |
| Expander | `code/expand_seed.py` | `f776c276df903b8e3de5de8b58144617c5ac2ecadf6515290c03c164b4518d4e` |

Seed format: `G_generators` (three permutations of 0…56), `bases`: list of
`{name, stabilizer_generators, classes}` (classes = lists of point triples),
`certificate_header` (first line of the file). From the lane directory:

```sh
python3 code/expand_seed.py evidence/lkts57-g513/lkts57_g513_seed.json /tmp/r57.txt evidence/lkts57-g513/lkts57_g513.txt
shasum -a 256 /tmp/r57.txt                                   # 09a9d8ca…2f09
python3 code/check_lkts57.py evidence/lkts57-g513/lkts57_g513.txt                      # lane, Python
python3 ../../../kirkman-large-sets-57-87/work/check_lkts.py evidence/lkts57-g513/lkts57_g513.txt   # prior dossier
clang -O2 -o /tmp/chk code/check_lkts57.c && /tmp/chk evidence/lkts57-g513/lkts57_g513.txt         # lane, C
```

Each checker assumes no symmetry and checks: v≡3 (mod 6); 55 systems; 28
classes; each class partitions X; each system covers every pair exactly once;
no triple occurs twice; union = all 29,260 triples. Receipts:
`evidence/lkts57-g513/{lane-checker-receipt.json,prior-checker-receipt.json,c-checker-receipt.txt}`;
16 mutation/positive controls on all three checkers:
`evidence/lkts57-g513/mutations/mutation-results.json`. Parent: independent
checker, action audit, seed replay and Codex gpt-6.1-sol verification
(receipts and verdict `review/lkts-57-87-parent-verdict.md` in the run directory).

## 7. How it was found (reproducibility of the search, not needed for validity)

`code/g513_full.py` builds a Kramer–Mesner exact cover over G-orbits of triples
with the five bases (`code/km2.py`), solves it with kissat 4.0.4, then solves
small SAT models for the base resolutions with the stated symmetries
(`code/resolve.py`) and develops (`code/assemble.py`). The pinned file came from
run `code/runs/full1` (32 s) without a fixed Python hash seed, so the search run
itself is not byte-reproducible; with `PYTHONHASHSEED=0` the search is
deterministic and gives another valid LKTS(57) (`evidence/lkts57-g513-deterministic/`,
sha `15e44165…69c2`).

## 8. Lemma dependencies (explanation only)

`sources/automorphism-lemmas.md`: Lemmas 2–4 explain why, if G acts on the large
set, the constituents must split 19+9+9+9+9 with these stabilizers; Lemma 5 and
Corollary 5a explain why earlier resolution models failed and which class
structures can work. None is used to *verify* the certificate.

## 9. Limits

A single finite object; no family or general theorem is claimed; G acts on the
underlying large set of STS, not on the resolved systems; "new" means only that
no earlier LKTS(57) was located in the recorded searches.
