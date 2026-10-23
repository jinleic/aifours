import LktsKernel.Generic
import LktsKernel.Data57
open Kirkman.KernelCert
theorem p2 : chunkOK 57 (46300 * 0) (46300 * (0 + 1)) 0 (allRows data57) = true := by decide +kernel
