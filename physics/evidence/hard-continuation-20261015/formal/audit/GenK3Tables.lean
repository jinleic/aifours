import KSatUpper.TrialDataK3
import KSatUpper.NumericalCriterion

/-! Evaluation (not proof) printing the dyadic literals materialized in `KSatUpper.K3Data`:
the table entries `NumericalCriterion.bounds`, the alternating lower moments `momentLower`, and
the edge term rounded on the grid `2^-96` both down and up. Every literal used is re-proved by
`decide +kernel`. -/

open KSatUpper

def dump (name : String) (α : ℚ) (N : ℕ) (u : ℚ) : IO Unit := do
  let T := TrialDataK3.trialT128
  let tbl := NumericalCriterion.table T 2 α 128
  for j in List.range 129 do
    let e := tbl.getD j (0, 0)
    IO.println s!"{name} T {j} {e.1.num} {e.1.den} {e.2.num} {e.2.den}"
  for k in List.range 129 do
    let mk := VertexEnclosures.momentLower (NumericalCriterion.lowerOf tbl)
      (NumericalCriterion.upperOf tbl) k
    IO.println s!"{name} M {k} {mk.num} {mk.den}"
  let E := NumericalCriterion.edgeLower T 2 N u
  let lo : ℚ := (Rat.floor (E * 2^96) : ℚ) / 2^96
  let hi : ℚ := (Rat.ceil (E * 2^96) : ℚ) / 2^96
  IO.println s!"{name} Elo {lo.num} {lo.den}"
  IO.println s!"{name} Ehi {hi.num} {hi.den}"
  let V := VertexEnclosures.vertexUpper 128 (NumericalCriterion.lowerOf tbl)
    (NumericalCriterion.upperOf tbl)
  IO.println s!"{name} valueLo_e12 {Rat.floor ((V + (-2) * α * lo) * 10^12)}"
  IO.println s!"{name} valueHi_e12 {Rat.floor ((V + (-2) * α * hi) * 10^12)}"

#eval dump "A" (2667/625) 256 (239949/250000)
#eval dump "B" (213359/50000) 256 (239949/250000)
#eval dump "C" (42671/10000) 256 (239949/250000)
#eval dump "D" (426717/100000) 256 (239949/250000)
