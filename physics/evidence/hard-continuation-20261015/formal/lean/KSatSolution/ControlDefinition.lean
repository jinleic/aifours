namespace KSatControl
def double (n : Nat) : Nat := 2 * n
theorem double_eq (n : Nat) : double n = n + n := by unfold double; omega
theorem two_mul' (n : Nat) : n + n = 2 * n := by omega
end KSatControl
