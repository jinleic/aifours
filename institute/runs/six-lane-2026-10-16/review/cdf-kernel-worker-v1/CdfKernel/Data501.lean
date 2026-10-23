/-
GENERATED FILE - do not edit.  Produced by gen_lean.py from the raw certificate
review/cdf501-parent-inputs-v1/cdf_501.txt (438 bytes, SHA-256 517e02fa330269323f70de11e66ac89aac97da106775efb7dca1d674fd7aab74).
Header line `CDF 501 5`.  Entry i of `data501` is raw line i + 2, copied verbatim in raw order.
Nothing is assumed about these numbers here: CdfKernel.Generic states the checker and its
soundness theorem, and CdfKernel.Cert501 runs the checker in the Lean kernel.
-/
namespace Cdf.Kernel

/-- SHA-256 of the raw certificate bytes, recorded by gen_lean.py (documentation only). -/
def data501RawSha256 : String := "517e02fa330269323f70de11e66ac89aac97da106775efb7dca1d674fd7aab74"

/-- The header of the raw certificate: order `v` and block size `k`. -/
def data501Header : Nat × Nat := (501, 5)

/-- The 25 raw base blocks of review/cdf501-parent-inputs-v1/cdf_501.txt, in raw order. -/
def data501 : List (List Nat) := [
  [0, 92, 193, 242, 475],
  [0, 104, 223, 230, 445],
  [0, 143, 190, 191, 478],
  [0, 107, 227, 325, 343],
  [0, 62, 172, 272, 496],
  [0, 137, 181, 197, 487],
  [0, 29, 178, 305, 490],
  [0, 53, 187, 281, 481],
  [0, 307, 361, 392, 443],
  [0, 322, 346, 368, 467],
  [0, 292, 376, 395, 440],
  [0, 13, 68, 154, 266],
  [0, 4, 32, 163, 302],
  [0, 74, 260, 331, 337],
  [0, 289, 379, 404, 431],
  [0, 59, 275, 313, 355],
  [0, 50, 284, 319, 349],
  [0, 89, 245, 328, 340],
  [0, 37, 113, 130, 221],
  [0, 41, 169, 293, 499],
  [0, 69, 79, 405, 413],
  [0, 33, 168, 297, 429],
  [0, 39, 339, 348, 426],
  [0, 15, 378, 399, 435],
  [0, 3, 183, 246, 357]
]

end Cdf.Kernel
