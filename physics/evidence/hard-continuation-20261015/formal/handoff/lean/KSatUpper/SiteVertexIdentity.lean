import KSatUpper.TrialVertex

/-! Group site warnings by variable and literal sign, arity `m+1`.

Derived from `SatUpper/SiteVertexIdentity.lean` (yamelton/sat-upper-4268, Apache-2.0). -/

namespace KSatUpper.SiteVertexIdentity

variable {n L m : ℕ}

abbrev Side (u : Fin L → Fin (m + 1) → Fin n × Bool) (v : Fin n) (b : Bool) :=
  {i : Fin L // (u i 0).1 = v ∧ (u i 0).2 = b}

/-- The `m` incoming warnings of every site whose head literal is `(v,b)`. -/
def messages (u : Fin L → Fin (m + 1) → Fin n × Bool) (v : Fin n) (b : Bool)
    (x : (Fin L × Fin (m + 1)) → Bool) (i : Side u v b) : TrialVertex.InnerMark m :=
  fun j => x (i.1, j.succ)

end KSatUpper.SiteVertexIdentity
