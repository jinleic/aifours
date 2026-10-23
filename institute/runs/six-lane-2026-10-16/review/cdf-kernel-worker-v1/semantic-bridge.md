# Semantic bridge for the CDF kernel roots

Each item below is marked **[kernel]** if a Lean theorem in this directory proves it, or **[written]** if it is an argument in this note that no kernel has checked.

## 1. The formal target

`CdfKernel/Target.lean` imports only `Mathlib.Data.Fintype.Prod` and no certificate data. **[kernel]**

- Residues mod v are the elements of `Fin v`. `a - b` is core `Fin.sub`, whose value is `(v - b + a) % v`. The audit's `pp.explicit` print shows that the instance is `Fin.instSub`.
- `Cdf.diffs B` is the multiset of `B i j - B i k` over all `(i, j, k) : Fin n × Fin 5 × Fin 5` with `j ≠ k`.
- `Cdf.IsCDF B` is the conjunction of three conditions:
  - every `B i` is injective;
  - `count d (diffs B) = 1` whenever `d.val ≠ 0`;
  - `count d (diffs B) = 0` whenever `d.val = 0`.
- `Cdf.Target v` is `∃ n, ∃ B : Fin n → Fin 5 → Fin v, Cdf.IsCDF B`.

The roots are `Cdf.Kernel.exists_cdf{v} : ∃ B : Fin n → Fin 5 → Fin v, Cdf.IsCDF B` for (v, n) = (321, 16), (501, 25), (621, 31), (681, 34), (801, 40) and (901, 45). The audits `Cdf.Audit.target{v} : Cdf.Target v` derive the target statement from them. **[kernel]**

Sanity facts proved from the definition alone in `CdfKernel/Facts.lean` **[kernel]**:

- `Cdf.sub_eq_iff_modEq`: `a - b = d ↔ d ≡ a - b [ZMOD v]`, with integer casts of the values. So `Fin v` with `-` is ℤ/vℤ.
- `Cdf.IsCDF.existsUnique`: every nonzero residue equals `B i j - B i k` for exactly one triple `(i, j, k)` with `j ≠ k`.
- `Cdf.IsCDF.card_eq`: `20 * n = v - 1`, so the number of blocks is forced to be (v − 1)/20.

## 2. Identification with the literature notion **[written]**

A cyclic (v, k, 1) difference family is a collection {B_1, …, B_t} of k-subsets of ℤ_v such that every nonzero element of ℤ_v occurs exactly once among the differences x − y (x, y ∈ B_i, x ≠ y, 1 ≤ i ≤ t). This is the standard definition used by Abel–Costa–Finizio (2004) and in the later status papers.

- **ℤ_v.** `Fin v` with `Fin.sub` is ℤ_v, by the kernel lemma above.
- **k-subsets.** A k-subset is the same as an injective 5-tuple listing it. Choosing an order does not change the multiset of differences, because the index set contains every ordered pair of distinct positions.
- **Ordered pairs.** For an injective tuple, ordered pairs of distinct positions correspond bijectively to ordered pairs of distinct elements. Hence `diffs B` is exactly the literature's list of differences, counted with multiplicity.
- **"Exactly once".** This is `count = 1` for each nonzero residue. The residue 0 never occurs. That already follows from injectivity, and the definition also states it explicitly.

## 3. CDF ⇒ strictly cyclic S(2, 5, v)

The development has blocks `devBlock B (i, s) = {B i j + s}`.

`Cdf.IsCDF.steiner : IsCDF B → IsStrictlyCyclicSteiner B` proves four properties **[kernel]**:

1. every block has 5 points;
2. any two distinct points lie in the blocks of exactly one index (i, s);
3. the indexing is injective, so there are n·v distinct blocks;
4. translation by t maps block (i, s) to block (i, s + t).

Properties 1–3 give an S(2, 5, v) on ℤ_v. Property 4 with t = 1 makes x ↦ x + 1 an automorphism of order v. By property 3, each of the n block orbits {(i, s + t)} has full length v, which is the meaning of "strictly cyclic". **[written]**

Only the direction CDF ⇒ design is formalized. Existence needs nothing more.

## 4. CDF ⇒ perfect (v, 5, 1) optical orthogonal code

`Cdf.IsCDF.ooc : IsCDF B → IsPerfectOOC B` proves three properties **[kernel]**:

1. each codeword `devBlock B (i, 0) = {B i 0, …, B i 4}` has weight 5;
2. `|C_i ∩ (C_{i'} + τ)| ≤ 1` for every (i, i', τ) except i = i' with τ = 0;
3. `20 * n = v − 1`.

For 0/1 sequences of length v, the periodic correlation at shift τ is |C_i ∩ (C_{i'} + τ)|. The theorem quantifies over all τ, so the sign convention of the shift does not matter. "Perfect" means the Johnson bound ⌊(v − 1)/(k(k − 1))⌋ = (v − 1)/20 is attained. Baicheva–Topalova (*Axioms* 15(1):35, 2026, p.2, per the parent's excerpt `cdf-latest-primary-excerpt.txt`) call these perfect (v, k, 1) CPCW codes, and state that they are equivalent both to strictly cyclic 2-(v, k, 1) designs and to cyclic (v, k, 1) difference families. **[written]**

`CdfKernel/Bridge.lean` applies `Cdf.bridge_of_target` to the six audited roots: `Cdf.Bridge.bridge{v} : ∃ n B, IsCDF B ∧ IsStrictlyCyclicSteiner B ∧ IsPerfectOOC B`. **[kernel]**

## 5. Not covered by the kernel

- **Reading the target.** Whether `Target.lean`, `Facts.lean`, `IsStrictlyCyclicSteiner` and `IsPerfectOOC` match the literature definitions rests on sections 2–4 of this note.
- **Raw-to-literal binding.** `gen_lean.py` regenerates the literals byte-identically, and an independent regex reader in `replay.py` compares them with the raw files. Both run in Python, not in Lean.
- **Kernel independence.** `lean` and `leanchecker --fresh` belong to one Lean 4.34.1 toolchain. This is not Comparator and not a second, independent kernel. `decide +kernel` relies on the kernel's GMP-accelerated `Nat` literal arithmetic, which is part of that trusted kernel.
- **Priority, open status and significance.** These are separate parent audits (`cdf-k5-parent-verdict.md`, `cdf-k5-priority-audit.md`) and are unaffected by this work.
