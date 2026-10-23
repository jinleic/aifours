import PC100Kernel.Controls100

/-!
# Negative control: this module must FAIL to build

The full pipeline run on two corrupted literals of `PC100Kernel.Controls100`:

* `cert100swap` (the points `1` and `2` exchanged between the first blocks of `CLASS 0` and
  `CLASS 1`): the kernel evaluation of `certCheck` returns `false`, so `swap_check_true` is rejected;
* `tz64trade` (the published v = 64 resolution with a four-block subpartition exchanged between
  `CLASS 0` and `CLASS 12`; block set and class partitions intact, classes no longer mapped to classes
  by `x ↦ x + 1`): the kernel rejects `trade_check_true` as well.

Nothing about the corrupted data can then be derived without `sorryAx`.  No root depends on this
module.
-/

namespace PC100.Kernel.Controls

open PC100 PC100.Kernel

theorem swap_check_true : certCheck 100 cert100swap = true := by
  decide +kernel

theorem swap_isDesign : IsDesign241 (blocks 100 cert100swap) :=
  (sound_of_check swap_check_true).1

theorem trade_check_true : certCheck 64 tz64trade = true := by
  decide +kernel

theorem trade_shift : IsResolutionAutomorphism (blocks 64 tz64trade) (classes 64 tz64trade) (shift 64) :=
  (sound_of_check trade_check_true).2.2.1

end PC100.Kernel.Controls

#print axioms PC100.Kernel.Controls.swap_isDesign
#print axioms PC100.Kernel.Controls.trade_shift
