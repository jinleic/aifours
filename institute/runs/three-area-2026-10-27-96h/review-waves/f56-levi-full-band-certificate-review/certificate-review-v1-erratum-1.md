# Erratum 1 to certificate-review-v1.md (line-citation corrections only)

Applies to `certificate-review-v1.md` SHA-256 `9987f8d2fb98f5e54c3857355eb1b2597f312fc9c00e1134b96bf264ce4dd107` (230 LF / 34732 B). Observed `/bin/date` before this write is printed by the shell log that created this file (2026-10-28, ≈18:42 PDT). No finding, verdict, number or table changes; only four source-line citations in §3 ("Correct as implemented") are corrected after a grep re-check:

- `frontier-20261028-levi-lie-engine.py`: `lower3` is **L84–97** (written "L80–97"); `ideal_bases` is **L118–138** (written "L116–136"); `target_ideal` is **L141–149** (written "L139–147").
- `frontier-20261028-levi-critical-minors.py`: pivot selection/`BASELINE_SINGULAR`/`rows=sorted(piv.rows)` is **L49–53** (written "L44–48"); complement loop L32–35 and horizontal kernel L37–40 stand.

All other citations (critical replay L105–118, L225, L243, L248; 214 replay L225–231; horizontal replay L88–92; central-predecessor replay L17 and L19–27) were grep-verified and stand.
