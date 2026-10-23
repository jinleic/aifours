# Addendum 1 to the final lane summary (corrections only)

Written after `/bin/date` read 2026-10-18T16:45:23-0700. It corrects `cycle2/pa19-lane-final-summary-20261018T1641.md` (SHA-256 f5f6cfb817a67657f68d1a67dd936794d2bd81c79685d144ed256c58c72584df), which stays unchanged. No science is added.

## Correction 1 — floor STOP markers exist (summary §6 and §7)

The summary's §7 says "There are no HALT or STOP flags". That is WRONG.

- The lane's own passive watchdog `src/rss_watchdog4.py` (pid 60597; SHA b178c185ceba2f20e9b61abf51eeb81746e170659225dd7b3f1044ee24875b28; FLOOR = 12000000000; lines 31, 32 and 157) created two resource-stop markers at 2026-10-18T13:58:01-0700. Both have content "watchdog4 disk floor" and SHA 94b56f04b59849923b41db6929760de00a33c12f077983faa2670a2080015bb2:
  - `cycle2/STOP-hard12`;
  - `cycle2/STOP-m2r12`.
- Both names belong to the runtime RESOURCE_STOPS registry, which refuses every new native admission.
- The watchdog's own floor reading at 13:58:01 is not in the parent monitor's below-floor list; the two monitors sample independently.
- The same incompleteness affects my 14:20:30 checkpoint ("no HALT/STOP flag") and the summary's 16:40:43 state line: both checked only the m2k3 flags and STOP-K1. My "no HALT/STOP flag" statements at 12:05 and 13:32 predate the markers and were accurate when made.
- STOP-K1 does not exist yet; the timer (pid 60602) will create it at 17:20.
- No HALT or veto flag (m2k1-*/m2k3-*) exists.

**Consequences:**
- No native work ran after 13:30:46. The v6_4 pilot's prelaunch at 13:28:56 saw an empty registry, before the markers existed.
- My later metadata-only, pure-Python, no-native-child probes ran after the markers were created:
  - GPS-1 at 14:00:07;
  - GPS-1|C1 at 14:08:08;
  - GPS-2|C1 at 14:10:48;
  - the list-binding check at 14:14:54;
  - the cross-check at 14:18:18.

  Each passed its own fresh statvfs admission (>= 12.2e9 + 16 MiB), but they did NOT consult the resource-stop registry. Their outputs are small receipts.
- No marker has been removed or altered.

## Correction 2 — scope of the M2H item estimate (summary §8 item 3)

"about 5,573 items, roughly 43 h" concerns only the M2H re-solve contract: 5,580 items minus the 7 attempted. It must not be read across coverage layers.
- The 151 lane-original cases have different denominators and routes.
- The v6_3 count (3 of 5,424 cases) and the isolated v6_4 count (1 of 5,424) stay separate.
- The figure is a planning estimate, not a measured or accepted quantity.
