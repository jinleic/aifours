# Parent decision — measured RSS escalation for the M8 (n8) lane (2026-10-18T08:16:24-07:00)

**Contract basis:** `contract.json` resource_contract: per-lane target RSS 8 GiB, aggregate worker target 48 GiB, rule "Escalate measured memory/disk needs before exceeding targets". This file is that escalation; it applies to the M8 lane only and only from now until native end (17:57 PDT).

**Measured needs:**
- Parent GA desk (`review/moqls8-strengthened-parent-replay-v1`, P1-B1.M2 under replay v2): desk aggregate peak 4.66e9 B; projected strengthened/leaf reservation 4.6 GiB (1.3 GiB for P0-B4/P0-B5).
- Worker GB probe r2 (PhysDepolarizing; SUMMARY `b84717ff…1734`): aggregate pipeline peaks 3.69 GB (GB P1-B4) and 5.38 GB (GB P0-B3).

**Decision:** the M8 lane may run at most ONE parent GA pipeline and at most ONE worker GB pipeline concurrently, with a lane aggregate RSS limit of **11 GiB** (11,811,160,064 B) and at most **4 busy** native processes. Each pipeline keeps its own RSS-capped supervision (GB pipeline cap ≤ 6 GiB). The GA desk has priority: a GB launch must reserve its cap against the GA desk's declared reservation; if the sum would exceed 11 GiB, the GB launch waits. All other rules are unchanged (fresh free-space gate ≥ 12.2e9 B + growth; in-flight floor 12e9 B; long-job stability rule per the 07:32 amendment; no launch after 17:29; native end 17:57; SIGTERM-only stops; UNKNOWN on any stop).

**Why this is safe:** the host has 96 GiB RAM; the aggregate worker target (48 GiB) is unchanged and not approached (M7 ≈ 6.3 GiB reserved, other lanes small). The escalation is bounded by measured peaks plus margin.

**Evidence status:** worker GB runs are worker evidence (parent drat-trim binary, measured feeds, hashed proof streams) and do not by themselves meet the parent-replay requirement; GB S6 completion by 17:57 is unlikely and will be reported as an incomplete gate condition if not met.
