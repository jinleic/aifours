import RdsqsKernel.Data52
namespace Rdsqs.Kernel
set_option profiler true
theorem t_range : data52.flatten.all (rangeOK 52) = true := by decide +kernel
theorem t_pairs : insertAll (data52.flatten.flatMap (pairCodes 52)) 0 = some (pairMask 52) := by decide +kernel
theorem t_classes : data52.all (fun c => insertAll (c.flatMap pts) 0 == some (pointMask 52)) = true := by decide +kernel
theorem t_closed : data52.flatten.all (closedOK 52 (tripleMask 52 data52.flatten)) = true := by decide +kernel
theorem t_all : seedCheck 52 data52 = true := by decide +kernel
theorem t_mult : mults52.all (fun p => multCheck 52 data52 p.1 p.2) = true := by decide +kernel
end Rdsqs.Kernel
