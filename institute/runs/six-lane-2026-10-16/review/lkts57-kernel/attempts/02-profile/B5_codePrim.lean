import LktsKernel.Generic
import LktsKernel.Data57
open Kirkman.KernelCert
def codeP (t : Row) : Nat := Nat.add (Nat.add (Nat.mul 3249 t.1) (Nat.mul 57 t.2.1)) t.2.2
theorem b : (allRows data57).all (fun t => Nat.blt (codeP t) 200000) = true := by decide +kernel
