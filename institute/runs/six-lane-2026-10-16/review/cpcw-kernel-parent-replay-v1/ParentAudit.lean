import CpcwKernel.Bridge

/-! Parent-authored target. The family condition spells out all differences and counts;
no worker predicate appears in the statement. In addition to existence at the stated floor,
the theorem quantifies over EVERY other family and proves the upper bound. -/
namespace ParentCpcwAudit

def Family {v k n : Nat} (B : Fin n → Fin k → Fin v) : Prop :=
  (∀ i : Fin n, ∀ j l : Fin k, B i j = B i l → j = l) ∧
  (∀ d : Fin v, d.val ≠ 0 →
    (((Finset.univ : Finset (Fin n × Fin k × Fin k)).filter fun t => t.2.1 ≠ t.2.2).val.map
      fun t => B t.1 t.2.1 - B t.1 t.2.2).count d ≤ 1) ∧
  (∀ d : Fin v, d.val = 0 →
    (((Finset.univ : Finset (Fin n × Fin k × Fin k)).filter fun t => t.2.1 ≠ t.2.2).val.map
      fun t => B t.1 t.2.1 - B t.1 t.2.2).count d = 0)

def Statement (v k n : Nat) : Prop :=
  (∃ B : Fin n → Fin k → Fin v, Family B) ∧
  n = (v - 1) / (k * (k - 1)) ∧
  (∀ m : Nat, ∀ B : Fin m → Fin k → Fin v, Family B → m ≤ (v - 1) / (k * (k - 1)))

theorem optimal122k6 : Statement 122 6 4 := by
  obtain ⟨B, hB, hsize⟩ := Cpcw.Kernel.exists_cpcw122k6
  exact ⟨⟨B, hB⟩, hsize, fun _ _ h => Cpcw.IsCPCW.le_bound (by decide) h⟩

theorem optimal123k6 : Statement 123 6 4 := by
  obtain ⟨B, hB, hsize⟩ := Cpcw.Kernel.exists_cpcw123k6
  exact ⟨⟨B, hB⟩, hsize, fun _ _ h => Cpcw.IsCPCW.le_bound (by decide) h⟩

theorem optimal124k6 : Statement 124 6 4 := by
  obtain ⟨B, hB, hsize⟩ := Cpcw.Kernel.exists_cpcw124k6
  exact ⟨⟨B, hB⟩, hsize, fun _ _ h => Cpcw.IsCPCW.le_bound (by decide) h⟩

theorem optimal143k5 : Statement 143 5 7 := by
  obtain ⟨B, hB, hsize⟩ := Cpcw.Kernel.exists_cpcw143k5
  exact ⟨⟨B, hB⟩, hsize, fun _ _ h => Cpcw.IsCPCW.le_bound (by decide) h⟩

theorem optimal144k5 : Statement 144 5 7 := by
  obtain ⟨B, hB, hsize⟩ := Cpcw.Kernel.exists_cpcw144k5
  exact ⟨⟨B, hB⟩, hsize, fun _ _ h => Cpcw.IsCPCW.le_bound (by decide) h⟩

theorem optimal146k5 : Statement 146 5 7 := by
  obtain ⟨B, hB, hsize⟩ := Cpcw.Kernel.exists_cpcw146k5
  exact ⟨⟨B, hB⟩, hsize, fun _ _ h => Cpcw.IsCPCW.le_bound (by decide) h⟩

theorem optimal162k5 : Statement 162 5 8 := by
  obtain ⟨B, hB, hsize⟩ := Cpcw.Kernel.exists_cpcw162k5
  exact ⟨⟨B, hB⟩, hsize, fun _ _ h => Cpcw.IsCPCW.le_bound (by decide) h⟩

theorem optimal167k5 : Statement 167 5 8 := by
  obtain ⟨B, hB, hsize⟩ := Cpcw.Kernel.exists_cpcw167k5
  exact ⟨⟨B, hB⟩, hsize, fun _ _ h => Cpcw.IsCPCW.le_bound (by decide) h⟩

end ParentCpcwAudit

#print axioms ParentCpcwAudit.optimal122k6
#print axioms ParentCpcwAudit.optimal123k6
#print axioms ParentCpcwAudit.optimal124k6
#print axioms ParentCpcwAudit.optimal143k5
#print axioms ParentCpcwAudit.optimal144k5
#print axioms ParentCpcwAudit.optimal146k5
#print axioms ParentCpcwAudit.optimal162k5
#print axioms ParentCpcwAudit.optimal167k5
