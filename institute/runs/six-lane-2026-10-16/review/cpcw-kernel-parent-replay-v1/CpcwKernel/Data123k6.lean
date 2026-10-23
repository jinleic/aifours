/-
GENERATED FILE - do not edit.  Produced by gen_lean.py from the raw certificate
review/cpcw123-parent-inputs-v1/cpcw_123_6.txt (74 bytes, SHA-256 d499ac51efb27249b22c807ff15db8e0cc55f84dc2aae79e6d99ebed48855a83).
Header line `CPCW 123 6`.  Entry i of `data123k6` is raw line i + 2, copied verbatim in raw order.
Nothing is assumed about these numbers here: CpcwKernel.Generic states the checker and its
soundness theorem, and CpcwKernel.Cert123k6 runs the checker in the Lean kernel.
-/
namespace Cpcw.Kernel

/-- SHA-256 of the raw certificate bytes, recorded by gen_lean.py (documentation only). -/
def data123k6RawSha256 : String := "d499ac51efb27249b22c807ff15db8e0cc55f84dc2aae79e6d99ebed48855a83"

/-- The header of the raw certificate: length `v` and weight `k`. -/
def data123k6Header : Nat × Nat := (123, 6)

/-- The 4 raw codewords of review/cpcw123-parent-inputs-v1/cpcw_123_6.txt, in raw order. -/
def data123k6 : List (List Nat) := [
  [0, 1, 3, 7, 84, 99],
  [0, 5, 19, 56, 74, 94],
  [0, 8, 21, 30, 53, 65],
  [0, 10, 26, 62, 73, 90]
]

end Cpcw.Kernel
