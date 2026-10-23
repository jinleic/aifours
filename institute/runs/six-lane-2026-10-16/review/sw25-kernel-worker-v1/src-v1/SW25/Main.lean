import SW25.Data

/-!
# A symmetric weighing matrix of order 25 and weight 16: kernel-checked existence

The witness `SW25.W` is defined in the generated module `SW25.Data` (see its header for the raw
file, its size and its SHA-256).  Every property below is proved by `decide +kernel`: the Lean
kernel evaluates the `Decidable` instances of Lean core on the literal.  Only Lean core (`Init`)
is imported: no Mathlib, no `native_decide`, no added axioms.

The root statement `SW25.exists_symmetric_weighing_matrix` is self-contained.  Besides `∃`, `∀`,
`∧`, `∨`, `=` and `if`, it mentions only `Fin`, `Int`, `List.finRange`, `List.map` and
`List.sum` from Lean core.
-/

namespace SW25

/-- Audit aid: the summation index list `List.finRange 25` is `0, 1, ..., 24` (each once, in order). -/
theorem finRange_vals : (List.finRange 25).map Fin.val = List.range 25 := by decide +kernel

/-- Binding: tabulating `W` row by row gives back exactly the generated literal `rows`, so the
fallback values of `List.getD` in the definition of `W` are never used. -/
theorem W_table :
    (List.finRange 25).map (fun i => (List.finRange 25).map (fun j => W i j)) = rows := by
  decide +kernel

/-- Every entry is `-1`, `0` or `1`. -/
theorem W_entries : ∀ i j : Fin 25, W i j = -1 ∨ W i j = 0 ∨ W i j = 1 := by decide +kernel

/-- `W` is symmetric. -/
theorem W_symm : ∀ i j : Fin 25, W i j = W j i := by decide +kernel

/-- `W Wᵀ = 16 I` entrywise: the inner product of rows `i` and `j` is `16` if `i = j`, else `0`. -/
theorem W_gram : ∀ i j : Fin 25,
    ((List.finRange 25).map (fun k => W i k * W j k)).sum = if i = j then 16 else 0 := by
  decide +kernel

/-- Audit aid: every row has exactly 16 nonzero entries (also implied by `W_entries` and `W_gram`). -/
theorem W_rowWeight :
    ∀ i : Fin 25, ((List.finRange 25).filter (fun k => W i k != 0)).length = 16 := by
  decide +kernel

/-- **Root.**  A symmetric weighing matrix of order 25 and weight 16 exists: a `25 × 25` integer
matrix with all entries in `{-1, 0, 1}`, symmetric, and with `∑ k, W i k * W j k = 16 δ_ij`. -/
theorem exists_symmetric_weighing_matrix :
    ∃ W : Fin 25 → Fin 25 → Int,
      (∀ i j : Fin 25, W i j = -1 ∨ W i j = 0 ∨ W i j = 1) ∧
      (∀ i j : Fin 25, W i j = W j i) ∧
      (∀ i j : Fin 25,
        ((List.finRange 25).map (fun k => W i k * W j k)).sum = if i = j then 16 else 0) :=
  ⟨W, W_entries, W_symm, W_gram⟩

end SW25

#print SW25.exists_symmetric_weighing_matrix
#print SW25.W
#print axioms SW25.exists_symmetric_weighing_matrix
#print axioms SW25.W_table
#print axioms SW25.W_rowWeight
#print axioms SW25.finRange_vals
