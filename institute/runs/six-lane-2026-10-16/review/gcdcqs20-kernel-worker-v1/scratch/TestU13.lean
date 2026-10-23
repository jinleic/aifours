import scratch.DataT

namespace Mcd.Kernel

def tbF : List RawQuad := List.flatten [tblocks_0, tblocks_1, tblocks_2, tblocks_3, tblocks_4, tblocks_5, tblocks_6, tblocks_7, tblocks_8, tblocks_9, tblocks_10, tblocks_11, tblocks_12, tblocks_13, tblocks_14, tblocks_15, tblocks_16, tblocks_17, tblocks_18, tblocks_19, tblocks_20, tblocks_21, tblocks_22, tblocks_23, tblocks_24, tblocks_25, tblocks_26, tblocks_27, tblocks_28, tblocks_29, tblocks_30, tblocks_31, tblocks_32, tblocks_33, tblocks_34, tblocks_35, tblocks_36, tblocks_37, tblocks_38, tblocks_39, tblocks_40, tblocks_41]

noncomputable def lenR (l : List RawQuad) : ℕ := List.rec 0 (fun _ _ ih => ih + 1) l

theorem t13 : Nat.beq (lenR tbF) 20540 = true := by
  decide +kernel

end Mcd.Kernel
