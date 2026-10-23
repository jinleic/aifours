import RdsqsKernel.Data76
namespace Rdsqs.Kernel
set_option profiler true
theorem t_all : seedCheck 76 data76 = true := by decide +kernel
theorem t_mult : ∀ p ∈ mults76, multCheck 76 data76 p.1 p.2 = true := by decide +kernel
theorem t_shape : data76.length = 37 ∧ ∀ c ∈ data76, c.length = 25 := by decide +kernel
end Rdsqs.Kernel
