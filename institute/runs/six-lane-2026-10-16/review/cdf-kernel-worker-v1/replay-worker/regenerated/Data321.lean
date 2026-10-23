/-
GENERATED FILE - do not edit.  Produced by gen_lean.py from the raw certificate
review/cdf321-parent-inputs-v1/cdf_321.txt (280 bytes, SHA-256 0304c61ba5f0a756259c0d12970f1e0d6c4e4909d931e997c7e37312dc37034b).
Header line `CDF 321 5`.  Entry i of `data321` is raw line i + 2, copied verbatim in raw order.
Nothing is assumed about these numbers here: CdfKernel.Generic states the checker and its
soundness theorem, and CdfKernel.Cert321 runs the checker in the Lean kernel.
-/
namespace Cdf.Kernel

/-- SHA-256 of the raw certificate bytes, recorded by gen_lean.py (documentation only). -/
def data321RawSha256 : String := "0304c61ba5f0a756259c0d12970f1e0d6c4e4909d931e997c7e37312dc37034b"

/-- The header of the raw certificate: order `v` and block size `k`. -/
def data321Header : Nat × Nat := (321, 5)

/-- The 16 raw base blocks of review/cdf321-parent-inputs-v1/cdf_321.txt, in raw order. -/
def data321 : List (List Nat) := [
  [0, 17, 115, 197, 313],
  [0, 4, 11, 103, 203],
  [0, 38, 142, 176, 286],
  [0, 202, 226, 242, 293],
  [0, 41, 173, 178, 250],
  [0, 130, 251, 284, 298],
  [0, 10, 97, 257, 278],
  [0, 80, 134, 193, 235],
  [0, 68, 133, 146, 295],
  [0, 1, 106, 233, 302],
  [0, 22, 83, 85, 131],
  [0, 182, 237, 289, 318],
  [0, 108, 225, 255, 264],
  [0, 36, 111, 126, 171],
  [0, 31, 49, 201, 294],
  [0, 102, 259, 265, 309]
]

end Cdf.Kernel
