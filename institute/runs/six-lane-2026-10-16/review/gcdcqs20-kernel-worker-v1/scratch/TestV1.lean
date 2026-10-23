import scratch.DataT

namespace Mcd.Kernel

def tbF : List RawQuad := List.flatten [tblocks_0, tblocks_1, tblocks_2, tblocks_3, tblocks_4, tblocks_5, tblocks_6, tblocks_7, tblocks_8, tblocks_9, tblocks_10, tblocks_11, tblocks_12, tblocks_13, tblocks_14, tblocks_15, tblocks_16, tblocks_17, tblocks_18, tblocks_19, tblocks_20, tblocks_21, tblocks_22, tblocks_23, tblocks_24, tblocks_25, tblocks_26, tblocks_27, tblocks_28, tblocks_29, tblocks_30, tblocks_31, tblocks_32, tblocks_33, tblocks_34, tblocks_35, tblocks_36, tblocks_37, tblocks_38, tblocks_39, tblocks_40, tblocks_41]

def pairCodesOfCode (v k : ℕ) : List ℕ :=
  [k / v, k / v / v * v + k % v, k / v % v * v + k % v]

def pairListAt (v x : ℕ) (hole : ℕ → Bool) : List ℕ :=
  (List.range v).flatMap fun p => (List.range' (p + 1) (v - (p + 1))).filterMap fun q =>
    if p = x ∨ q = x ∨ (hole p = true ∧ hole q = true) then none else some (p * v + q)

def holeCheck (v : ℕ) (bl : List RawQuad) (x : ℕ) (hole : ℕ → Bool) : Bool :=
  insertAll ((bl.filterMap (eraseCode v x)).flatMap (pairCodesOfCode v)) 0 ==
    some (orAll ((pairListAt v x hole).map (2 ^ ·)))

theorem tv0 : (colCheck 80 tbF 0 tcol0 && holeCheck 80 tbF 0 (fun _ => false)) = true := by
  decide +kernel

theorem tv79 : (colCheck 80 tbF 79 tcol79 && holeCheck 80 tbF 79 (fun _ => false)) = true := by
  decide +kernel

end Mcd.Kernel
