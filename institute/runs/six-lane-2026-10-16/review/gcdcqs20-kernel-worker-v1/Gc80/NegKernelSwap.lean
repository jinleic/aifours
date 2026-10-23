import Gc80.Controls80

/-!
# Negative control NegKernelSwap (this module must FAIL to build)

The colouring checker run on the corrupted gcDCQS `POINT 5` section `Controls.gcCol5swap` (the
first points of the first two triples of `CLASS 0` exchanged): the kernel evaluation of
`colCheck` returns `false`, so `gc_swap_colCheck_true` is rejected by the kernel, and the
colouring of the derived design at `5` cannot be derived without `sorryAx`.  No root depends on
this module.
-/

namespace Mcd.Kernel.Controls

open Mcd.Kernel

theorem gc_swap_colCheck_true : colCheck 80 blocksGc80 5 gcCol5swap = true := by
  decide +kernel

theorem gc_swap_colouring :
    IsColouring (derivedBlocks (blockSet 80 blocksGc80) (pt 80 5)) (classSet 80 gcCol5swap) :=
  (colouring_of_check gc_quadOK (by decide) gc_swap_colCheck_true).1

end Mcd.Kernel.Controls

#print axioms Mcd.Kernel.Controls.gc_swap_colouring
