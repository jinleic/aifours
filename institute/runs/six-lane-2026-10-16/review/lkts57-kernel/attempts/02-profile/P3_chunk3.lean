import LktsKernel.Generic
import LktsKernel.Data57
open Kirkman.KernelCert
theorem p3 : chunkOK 57 (46300 * 3) (46300 * (3 + 1)) 0 (allRows data57) = true := by decide +kernel
