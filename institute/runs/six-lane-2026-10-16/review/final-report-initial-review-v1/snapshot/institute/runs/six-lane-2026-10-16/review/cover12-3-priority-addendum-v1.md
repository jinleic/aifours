# L(12,3) = 36 — priority addendum: an earlier public claim exists

Recorded 2026-10-17 (PT) after a new-surface priority audit ([scout report](info-prior-gap-audit-v1.md)). The original [verdict](cover12-3-parent-verdict.md) is unchanged; this addendum supersedes only its priority and gate status.

**Earlier claim (read directly by the parent in DataCite):** Ruturaj R. Raval (independent researcher), *Exact Determination of the Binary Covering-Sequence Length L(12,3)*, Zenodo software/technical report v0.1.0, [doi:10.5281/zenodo.22639692](https://doi.org/10.5281/zenodo.22639692) (concept 10.5281/zenodo.22639691), issued 2026-09-07, registered 2026-09-07T09:15:28Z. That is about 40 days before this run's L(12,3) contract froze. The abstract reads: "Independent C++ and Rust traversals exclude all 68,719,476,734 binary sequences of positive lengths 1 through 35 through 506,526,514 rotation-reversal-complement representatives. A public attributed 36-bit witness is independently verified." The scout read the companion GitHub README, which uses the same convention (cyclic windows, all 4096 targets).

**Parent check:** the 36-bit witness quoted by the scout from that README, `010100011011000110111110101110010000`, covers all 4096 12-bit words within Hamming distance 3 cyclically, by the parent's exact check. The earlier exhaustive search was not rerun and its validity is not verified by us. The Zenodo files returned 403.

**Status:** CORRECTNESS-ACCEPTED (unchanged: counting through 13 and three independent exhaustive implementations for lengths 14–35). **PRIOR-CLAIM; no longer counted as a contract gate.** Our computation is an independent confirmation of a theorem already claimed publicly.
