import LktsKernel.Generic
import LktsKernel.Data57
open Kirkman.KernelCert
theorem b : (allRows data57).all (fun t => decide (code 57 t < 200000)) = true := by decide +kernel
