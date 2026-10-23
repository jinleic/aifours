import Brd26.Target
import Brd26.Witness

namespace Brd26.Probe

set_option profiler true

theorem listRows : brd26Rows.all (fun r => (r.filter (· ≠ 0)).length == 25) = true := by
  decide +kernel

end Brd26.Probe
