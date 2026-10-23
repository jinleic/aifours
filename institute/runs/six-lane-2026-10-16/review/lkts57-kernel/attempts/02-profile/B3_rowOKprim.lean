import LktsKernel.Generic
import LktsKernel.Data57
open Kirkman.KernelCert
def rowOKp (t : Row) : Bool := and (Nat.blt t.1 t.2.1) (and (Nat.blt t.2.1 t.2.2) (Nat.blt t.2.2 57))
theorem b : (allRows data57).all rowOKp = true := by decide +kernel
