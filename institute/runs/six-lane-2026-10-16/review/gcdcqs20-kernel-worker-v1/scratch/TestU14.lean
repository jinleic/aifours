import scratch.DataBig

namespace Mcd.Kernel

noncomputable def lenR (l : List RawQuad) : ℕ := List.rec 0 (fun _ _ ih => ih + 1) l

theorem t14 : Nat.beq (lenR tbig) 20540 = true := by
  decide +kernel

noncomputable def fmTest (x : ℕ) (bl : List RawQuad) : List ℕ :=
  List.rec [] (fun b _ ih => cond (Nat.beq b.1 x) (code3 80 b.2.1 b.2.2.1 b.2.2.2 :: ih)
    (cond (Nat.beq b.2.1 x) (code3 80 b.1 b.2.2.1 b.2.2.2 :: ih)
    (cond (Nat.beq b.2.2.1 x) (code3 80 b.1 b.2.1 b.2.2.2 :: ih)
    (cond (Nat.beq b.2.2.2 x) (code3 80 b.1 b.2.1 b.2.2.1 :: ih) ih)))) bl

theorem t15 : Nat.beq (fmTest 0 tbig).length 1027 = true := by
  decide +kernel

end Mcd.Kernel
