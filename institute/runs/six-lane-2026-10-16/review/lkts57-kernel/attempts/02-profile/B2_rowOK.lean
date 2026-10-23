import LktsKernel.Generic
import LktsKernel.Data57
open Kirkman.KernelCert
theorem b : (allRows data57).all (rowOK 57) = true := by decide +kernel
