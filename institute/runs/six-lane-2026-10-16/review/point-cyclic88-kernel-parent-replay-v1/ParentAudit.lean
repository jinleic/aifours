import PC88Kernel.Audit

/-!
Parent-authored statement: no design or resolution vocabulary is hidden in its hypotheses.
Every block is a four-subset, every pair occurs once, every class partitions the points,
and the classes partition the blocks. A single full-support cycle preserves both partitions.
The kernel must unfold the worker definitions to accept its root as a proof of this statement.
No assumption about T1, short blocks, stabilizers or derived cardinalities is supplied.
-/
namespace ParentPointCyclic88

universe u

theorem no_point_cyclic_resolution
    {V : Type u} [Fintype V] [DecidableEq V]
    (hpoints : Fintype.card V = 88)
    (B : Finset (Finset V)) (R : Finset (Finset (Finset V)))
    (σ : Equiv.Perm V)
    (hblocks : ∀ X ∈ B, X.card = 4)
    (hpairs : ∀ x y : V, x ≠ y → ∃! X, X ∈ B ∧ x ∈ X ∧ y ∈ X)
    (hclasses : ∀ P ∈ R, P ⊆ B ∧ ∀ x : V, ∃! X, X ∈ P ∧ x ∈ X)
    (hpartition : ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P)
    (hcycle : σ.IsCycle)
    (hsupport : σ.support = Finset.univ)
    (hblock_image : B.image (fun X => X.map σ.toEmbedding) = B)
    (hclass_image : ∀ P ∈ R, P.image (fun X => X.map σ.toEmbedding) ∈ R) : False :=
  PC88.Audit.root_unfolded hpoints B R σ
    ⟨hblocks, hpairs⟩ ⟨hclasses, hpartition⟩ hcycle hsupport hblock_image hclass_image

end ParentPointCyclic88

set_option pp.funBinderTypes true in
#print ParentPointCyclic88.no_point_cyclic_resolution
#print axioms ParentPointCyclic88.no_point_cyclic_resolution
