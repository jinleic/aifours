/-! Comparator negative-control challenge (independent of the k-SAT development). -/
namespace KSatControl
def double (n : Nat) : Nat := n + n
theorem double_eq (n : Nat) : double n = n + n := by sorry
theorem two_mul' (n : Nat) : n + n = 2 * n := by sorry
end KSatControl
