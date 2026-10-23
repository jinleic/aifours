import scratch.DataT

namespace Mcd.Kernel

theorem t3 : (insertAll (tcol0.flatten.map (codeT 80)) 0).isSome = true := by
  decide +kernel

end Mcd.Kernel
