import McdKernel.Data38
namespace Mcd.Kernel
set_option profiler true
theorem t_all_cols : (List.range 38).all (fun x => colCheck 38 blocks38 x (colour38.getD x [])) = true := by decide +kernel
end Mcd.Kernel
