import McdKernel.Controls38

/-!
# Negative control: this module must FAIL to build

The full pipeline run on the corrupted `POINT 5` section `Controls.col5swap` (points `0` and `1`
exchanged between the first two triples of `CLASS 0`): the kernel evaluation of `colCheck`
returns `false`, so `swap_colCheck_true` is rejected, and the colouring of the derived design at
`5` cannot be derived without `sorryAx`.  No root depends on this module.
-/

namespace Mcd.Kernel.Controls

open Mcd.Kernel

theorem swap_colCheck_true : colCheck 38 blocks38 5 col5swap = true := by
  decide +kernel

theorem swap_colouring :
    IsColouring (derivedBlocks (blockSet 38 blocks38) (pt 38 5)) (classSet 38 col5swap) :=
  (colouring_of_check (quadOK_of_sqsCheck blocks38_sqsCheck) (by decide) swap_colCheck_true).1

end Mcd.Kernel.Controls

#print axioms Mcd.Kernel.Controls.swap_colouring
