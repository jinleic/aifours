# Status: approved deficit-five parentage subproblem

Snapshot: 2026-10-14 (America/Los_Angeles).

## Approved scope and prior-art screen

The original chapter is Bao Chengguang's “Solve the Recurrence Relation of the Fractional Parentage Coefficients,” *10000 Selected Problems in Sciences: Physics* (Science Press, 2009), pp. 348–349. The unedited excerpt is `source/problem.zh.txt`. The user subsequently approved precise scoped subproblems. This slot was reassigned after the cone/Fermat-spiral density mechanism was identified as already solved; that screening and its certificates remain in `../phys-fibonacci-cone-spirals/`.

The target here is **all signed reduced one-body CFPs** for identical integer-spin `f>=3` bosons at maximal seniority `v`, parent total spin `L=f*v-5`, into every daughter of seniority `v-1`. The stable domain is `v>=6`; the low-degree cases `v=3,4,5`, and absence at `v<=2`, are part of the contract. Multiplicity bases are fixed covariants followed by Gram–Schmidt, not claimed canonical. This does not solve arbitrary deficit, the low-spin missing-label problem, or the `v -> v+1` branch at larger particle number.

**Openness/novelty boundary:** no primary source located explicitly declares this exact general-f, deficit-five table open. The dated search below did not locate its closed form, which is not a proof of nonexistence. The contribution is therefore **NOVELTY-UNCLEAR**, and must not be marketed as the first such formula. Correctness of a completed formula is a separate question.

## Primary sources checked

1. **Feng Pan, Lina Bao, Yao-Zhong Zhang, Jerry P. Draayer**, “Construction of Basis Vectors For Symmetric Irreducible Representations of O(5) superset O(3),” [arXiv:1309.2654](https://arxiv.org/abs/1309.2654); *European Physical Journal Plus* **129**, 169 (2014). The [full manuscript](https://arxiv.org/pdf/1309.2654), introduction and the declared table scope were read. It proposes a general recursive construction but explicitly focuses on `l=2`; its analytic top-family tables are `O(5)`/spin-2 and reach deficit six. These are prior art, not general-f deficit-five coefficients.
2. **P. Van Isacker and S. Heinze**, “Seniority in quantum many-body systems. I. Identical particles in a single shell,” *Annals of Physics* **349**, 73–99 (2014), [arXiv:1406.4094](https://arxiv.org/html/1406.4094). Sections 1 and 5 were read. Equation (108) already treats a specially chosen spin-3 state at `J=3N-5`, and equations (115)–(116) give general-spin solvable energies. The multiplicity-two space, its seniority property, and existence of special solvable states are therefore not discoveries here. Those energy expressions are not the full signed one-body CFP matrices in our two-state basis.
3. **P. Van Isacker**, “Boson Models with Interactions of Arbitrary Order,” [arXiv:2606.04055v1](https://arxiv.org/html/2606.04055v1) (2026). Introduction and Section II were read. Despite the abstract's closed Hamiltonian-matrix-element formulas, Section II still constructs one-particle CFPs by the Redmond recursion and orthonormalization. Its use of single-j CFPs as ingredients does not by itself provide the requested all-v deficit-five table.
4. **Hong-Zhou Sun, Mei Zhang, Qi-Zhi Han, Gui-Lu Long**, “A new recursion relation of CFP for the system of identical bosons,” *Journal of Physics A* **22**, 4769 (1989), DOI [10.1088/0305-4470/22/22/008](https://doi.org/10.1088/0305-4470/22/22/008). Publisher-deposited bibliographic metadata read; no inaccessible theorem is attributed to it. This is the book's recursive baseline.
5. **Teruo Kishimoto and Taro Tamura**, “Coefficients of fractional parentage of many-boson systems,” *Nuclear Physics A* **163**, 100–112 (1971), DOI [10.1016/0375-9474(71)90523-9](https://doi.org/10.1016/0375-9474(71)90523-9). The [Elsevier-supplied abstract in INSPIRE](https://inspirehep.net/api/literature/1438239) was read after the DOI record supplied metadata only. It describes a compact calculation for quadrupole phonons (spin 2), not an announced general-f deficit-five table. The full article was not inspected; novelty clearance remains incomplete.

Searches used the exact combinations “boson fractional parentage analytic,” “maximum angular momentum,” “near stretched,” “arbitrary angular momentum,” and deficit-five variants, including current 2026 material. Results predominantly concerned spin 1, spin 2, recursion, or unrelated fractional statistics. This is a search log, not an open-status certificate.

## Comparable local baseline and bounded obligation

The sibling project `../phys-fractional-parentage-coefficients/` already certifies general-f deficits two, three, and four, with a pair-first deficit-four basis. Its `top_family_symbolic.py`, `general_f_k4.py`, and `fpc_core.py` were read and remain read-only. The new target reuses their conventions and imports their interfaces for independent checks; it does not copy or fork their core.

At fixed deficit five there are seven partitions and a stable highest-weight kernel of dimension `p(5)-p(4)=2`. Since `2f>5`, a singlet-pair annihilator cannot map that weight to degree `v-2`; every state in the block has seniority `v`. The missing obligation is a fixed-size rational Gram/insertion calculation, orthonormalization, complete daughter coverage and low-v domains. This is why the scoped task is bounded; it is not an argument that the full book problem is easy.

## Frozen derivation and verification contract

- Parent raw basis: degree-three deficit-five covariant first; the product of the deficit-two and deficit-three covariants second when `v>=5`.
- Daughter blocks: deficits `0,2,3,4,5`; deficit one is absent. Deficit-four uses the existing pair-first raw basis. Remove a raw basis vector only when its polynomial degree exceeds the number of bosons; do not silently substitute a limiting singular formula.
- Deliver explicit rational Gram and insertion matrices and a two-by-two square-root normalization formula for every entry, not a recursion or numerical fit. Derive the stable symbolic identity over `Q(f,v)` and each low-v identity over `Q(f)`.
- Independent controls: existing full occupation-polynomial engine for `f=3,4,5,6,7`, `v=3..10`, all present daughter entries, signs, multiplicities, and completeness; a first-quantized contraction check for a small case; deliberate normalization/phase/basis perturbations must be detected.
- One core, no optimization, no seeds. Use the already-existing parentage Python environment because the shared ai4s environment lacks `python-flint`; no installation or environment mutation. The observed existing runtime is Python 3.13.9, SymPy 1.14.0, python-flint 0.9.0.
- Independent Codex hostile review is required after the expressions and proof are ready. Finite controls remain separate from the universal algebraic proof.
