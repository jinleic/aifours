import McdKernel.Data38
namespace Mcd.Kernel
set_option profiler true
theorem t_blocks_ok : blocks38.all (quadOK 38) = true := by decide +kernel
theorem t_sqs : sqsCheck 38 blocks38 = true := by decide +kernel
theorem t_col0 : colCheck 38 blocks38 0 col38_0 = true := by decide +kernel
theorem t_col37 : colCheck 38 blocks38 37 col38_37 = true := by decide +kernel
theorem t_sts : stsColCheck 37 col38_37 = true := by decide +kernel
end Mcd.Kernel
