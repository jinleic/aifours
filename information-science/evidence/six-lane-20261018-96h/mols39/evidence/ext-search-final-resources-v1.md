# Final extension per-input operation/payload table (source arithmetic only)

The package overlays supersede approximate/omitted earlier beta scans. No source has run and no RAM/time measurement
has occurred. Counter-byte width is ceil(bit_length(T(r))/8) for full search or ceil(bit_length(256(r+1))/8) for joint
calibration. Packed payload follows the independent source/README exact formula, with h=2,d=8; sizes are conditional
on that intended platform item width. The algorithm uses array widths from runtime where necessary.

|case|n|k|m|node counter bytes|joint packedB|joint B+16MiB JSON|jointW|jointW_all|beta Bnode bound|beta Hnode bound|
|---|---|---|---|---|---|---|---|---|---|---|
|N6|6|2|0|2|78088|16855304|294|342|105|96|
|N12|12|2|9|1|99336|16876552|648|744|130|192|
|P21|21|5|18|1|141069|16918285|4437|4731|499|714|
|P57|57|7|54|1|338541|17115757|22113|23139|1845|2622|
|anchor calibration|39|6|0|2|236197|17013413|11505|12129|9554|1560|

N6/N12 parity proofs and planted chunks are in ext-search-controls-resources-v1.md; corrected beta counted-scan
bound and units are in ext-search-package-overlay-v1.md. Counts W refer packed-cell read/write primitives in the
joint source; beta B/H use stated item/predicate units, not directly comparable CPU instruction costs.
For calibration, joint max9984 visited nodes for256 full probes at r38 (apart from setup/output); beta max19968 nodes
for256 probes including38 assignments in each stage and the unary transition. These are path node bounds only,
not limits on full-tree estimates. Finite estimate may be enormous; it is never an exclusion or full-run admission.
Both runtimes use cap256MiB and reservation100MB independently enforced by the eventual qualified supervisor.
Interpreter baseline, allocator, Python containers/frames/bigints and IO temporary overhead prevent an exact
portable RSS inference from source. Source-buffer payload adds <=2MiB raw and <=2MiB algorithm-load copies transient;
cooperative deadlines/operational caps handle deviations fail-closed, never scientific negatives.
Data maker has bounded raw1MiB plus at most8*57 integer values and small fixed controls/manifests. Final gate reads
at most20 declared result/control artifacts (each<=16MiB cap) sequentially; retained state contains parsed tiny
control solution sets. Planted r2 limits solution counts to n^2<=3249 before global4096 cap; source retains actual
COMPLETE counts or declares incomplete. No measured gateRSS bound, cap256MiB; artifact cap is per file, not a claim
that arbitrary adversarial giant sets fit. A resource trip blocks qualification.
BAD_DM/BAD_PIN stop before search-state allocation. No full target search or completion time is projected.
