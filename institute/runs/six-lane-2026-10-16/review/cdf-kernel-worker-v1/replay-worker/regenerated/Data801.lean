/-
GENERATED FILE - do not edit.  Produced by gen_lean.py from the raw certificate
review/cdf801-parent-inputs-v1/cdf_801.txt (701 bytes, SHA-256 0a75e7d93920415f04a51967bd5a4033765f040f3b19af9f603d16b6d616186c).
Header line `CDF 801 5`.  Entry i of `data801` is raw line i + 2, copied verbatim in raw order.
Nothing is assumed about these numbers here: CdfKernel.Generic states the checker and its
soundness theorem, and CdfKernel.Cert801 runs the checker in the Lean kernel.
-/
namespace Cdf.Kernel

/-- SHA-256 of the raw certificate bytes, recorded by gen_lean.py (documentation only). -/
def data801RawSha256 : String := "0a75e7d93920415f04a51967bd5a4033765f040f3b19af9f603d16b6d616186c"

/-- The header of the raw certificate: order `v` and block size `k`. -/
def data801Header : Nat × Nat := (801, 5)

/-- The 40 raw base blocks of review/cdf801-parent-inputs-v1/cdf_801.txt, in raw order. -/
def data801 : List (List Nat) := [
  [0, 90, 366, 387, 633],
  [0, 442, 620, 720, 738],
  [0, 225, 239, 328, 378],
  [0, 289, 334, 448, 709],
  [0, 56, 216, 270, 412],
  [0, 38, 300, 407, 768],
  [0, 208, 338, 374, 415],
  [0, 6, 84, 183, 528],
  [0, 283, 498, 570, 607],
  [0, 506, 658, 740, 766],
  [0, 129, 138, 560, 686],
  [0, 101, 344, 520, 637],
  [0, 128, 275, 317, 437],
  [0, 91, 319, 532, 571],
  [0, 292, 598, 743, 770],
  [0, 390, 582, 678, 753],
  [0, 524, 600, 722, 735],
  [0, 136, 487, 533, 713],
  [0, 247, 640, 643, 784],
  [0, 202, 452, 688, 794],
  [0, 5, 307, 561, 746],
  [0, 233, 316, 507, 707],
  [0, 256, 272, 604, 744],
  [0, 19, 173, 591, 634],
  [0, 22, 51, 124, 668],
  [0, 67, 232, 483, 578],
  [0, 266, 564, 638, 691],
  [0, 341, 446, 466, 771],
  [0, 8, 195, 538, 597],
  [0, 170, 339, 471, 619],
  [0, 2, 12, 400, 682],
  [0, 255, 443, 475, 490],
  [0, 11, 259, 465, 563],
  [0, 69, 97, 149, 434],
  [0, 4, 44, 655, 689],
  [0, 23, 85, 134, 502],
  [0, 1, 25, 218, 627],
  [0, 227, 331, 622, 708],
  [0, 284, 354, 596, 664],
  [0, 428, 493, 650, 714]
]

end Cdf.Kernel
