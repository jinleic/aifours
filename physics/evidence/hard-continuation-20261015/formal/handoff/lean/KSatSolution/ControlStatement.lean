namespace KSatControl
def double (n : Nat) : Nat := n + n
theorem double_eq (n : Nat) : double n = n + n := rfl
theorem two_mul' (n : Nat) : n + n = n * 2 := by omega
end KSatControl
