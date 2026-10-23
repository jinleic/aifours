# Attempt v1 (kept for provenance; superseded, not deleted)

First complete design: one `dataOK 57 data57` kernel evaluation plus four `chunkOK` code windows
scanning all 29,260 rows.  `lean` exit 0, `exists_lkts57` axioms [propext, Classical.choice,
Quot.sound]; 41.35 s wall, 5.29 GB peak RSS (see Cert57.build.time).

Superseded because per-declaration kernel memory scales with the rows touched by one declaration
(profiling in ../02-profile: ~120 KB/row for dataOK, ~20 KB/row just to traverse the rows), which
would not fit LKTS(87) (105,995 rows) in one declaration.  v2 splits the per-system checks into one
declaration per system and replaces the windows by a chained colex-rank bitmask fold proving
`(allRows d).Nodup`, with kernel-checked intermediate accumulators.
