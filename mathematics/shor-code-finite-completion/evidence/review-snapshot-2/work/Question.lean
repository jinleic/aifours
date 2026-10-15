import Mathlib.Data.List.Basic
import Mathlib.Data.Finset.Basic

namespace ShorCompletion

abbrev Word := List Bool

def bayonet (i j : ℕ) : Word :=
  List.replicate i false ++ [true] ++ List.replicate j false

def original : Finset Word :=
  {bayonet 0 0, bayonet 0 1, bayonet 0 7, bayonet 0 13, bayonet 0 14,
   bayonet 3 0, bayonet 3 2, bayonet 3 4, bayonet 3 6,
   bayonet 8 0, bayonet 8 2, bayonet 8 4, bayonet 8 6,
   bayonet 11 0, bayonet 11 1, bayonet 11 2}

def UniquelyDecipherable (X : Finset Word) : Prop :=
  ∀ xs ys : List Word,
    (∀ x ∈ xs, x ∈ X) → (∀ y ∈ ys, y ∈ X) →
    xs.flatten = ys.flatten → xs = ys

def Complete (X : Finset Word) : Prop :=
  ∀ w : Word, ∃ u v : Word, ∃ xs : List Word,
    (∀ x ∈ xs, x ∈ X) ∧ xs.flatten = u ++ w ++ v

def HasFiniteCompletion : Prop :=
  ∃ X : Finset Word, original ⊆ X ∧ UniquelyDecipherable X ∧ Complete X

end ShorCompletion
