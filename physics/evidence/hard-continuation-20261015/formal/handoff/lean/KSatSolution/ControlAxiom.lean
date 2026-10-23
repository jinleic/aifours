namespace KSatControl
def double (n : Nat) : Nat := n + n
axiom helper : ∀ n : Nat, n + n = 2 * n
theorem double_eq (n : Nat) : double n = n + n := rfl
theorem two_mul' (n : Nat) : n + n = 2 * n := helper n
end KSatControl
