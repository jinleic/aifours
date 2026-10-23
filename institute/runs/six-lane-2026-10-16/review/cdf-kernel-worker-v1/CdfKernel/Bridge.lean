import CdfKernel.Facts
import CdfKernel.Audit
import CdfKernel.Audit801
import CdfKernel.Audit901

/-!
# Kernel-checked bridges for the six concrete orders

Corollaries only: each theorem applies the data-free `Cdf.bridge_of_target` (`CdfKernel.Facts`) to
an audited root.  For each order, the family is a cyclic `(v, 5, 1)` difference family, its
development is a strictly cyclic `S(2, 5, v)`, and its base blocks form a perfect `(v, 5, 1)`
optical orthogonal code, in the senses defined in `CdfKernel.Facts`.
-/

namespace Cdf.Bridge

open Cdf

theorem bridge321 : ∃ n : ℕ, ∃ B : Fin n → Fin 5 → Fin 321,
    IsCDF B ∧ IsStrictlyCyclicSteiner B ∧ IsPerfectOOC B :=
  bridge_of_target Cdf.Audit.target321

theorem bridge501 : ∃ n : ℕ, ∃ B : Fin n → Fin 5 → Fin 501,
    IsCDF B ∧ IsStrictlyCyclicSteiner B ∧ IsPerfectOOC B :=
  bridge_of_target Cdf.Audit.target501

theorem bridge621 : ∃ n : ℕ, ∃ B : Fin n → Fin 5 → Fin 621,
    IsCDF B ∧ IsStrictlyCyclicSteiner B ∧ IsPerfectOOC B :=
  bridge_of_target Cdf.Audit.target621

theorem bridge681 : ∃ n : ℕ, ∃ B : Fin n → Fin 5 → Fin 681,
    IsCDF B ∧ IsStrictlyCyclicSteiner B ∧ IsPerfectOOC B :=
  bridge_of_target Cdf.Audit.target681

theorem bridge801 : ∃ n : ℕ, ∃ B : Fin n → Fin 5 → Fin 801,
    IsCDF B ∧ IsStrictlyCyclicSteiner B ∧ IsPerfectOOC B :=
  bridge_of_target Cdf.Audit.target801

theorem bridge901 : ∃ n : ℕ, ∃ B : Fin n → Fin 5 → Fin 901,
    IsCDF B ∧ IsStrictlyCyclicSteiner B ∧ IsPerfectOOC B :=
  bridge_of_target Cdf.Audit.target901

end Cdf.Bridge

#print Cdf.devBlock
#print Cdf.IsStrictlyCyclicSteiner
#print Cdf.IsPerfectOOC
#check @Cdf.sub_eq_iff_modEq
#check @Cdf.IsCDF.existsUnique
#check @Cdf.IsCDF.card_eq
#check @Cdf.bridge_of_target
#print axioms Cdf.sub_eq_iff_modEq
#print axioms Cdf.IsCDF.existsUnique
#print axioms Cdf.IsCDF.card_eq
#print axioms Cdf.bridge_of_target
#print axioms Cdf.Bridge.bridge321
#print axioms Cdf.Bridge.bridge501
#print axioms Cdf.Bridge.bridge621
#print axioms Cdf.Bridge.bridge681
#print axioms Cdf.Bridge.bridge801
#print axioms Cdf.Bridge.bridge901
