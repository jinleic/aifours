# Stable case bindings v1

Frozen after host clock 2026-10-19T14:01:21-0700. Only metadata reads and hashes; no encoder execution or generated case analysis.

## Source pins and interpretation
- S = /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/cycle2/skel-b/skeletons-b-ms09.json; SHA256 7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0. One physical line (no terminating LF); byte ranges are ZERO-based half-open, not line ranges.
- V = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/pa19-parent-frontier-v9.json; SHA256 0cc25f735a19eadd346f7599974ed69091eb44762e57026dda6f906317962225. Line ranges below are ONE-based inclusive. Its `current_counts_parent` at lines5110-5114 is the current snapshot; the historical header `frontier_counts` is not current. The four entries are under `ms09_undecided` and are targets frozen by transition f3fa55e8, not a promise that this remains the latest frontier forever.
- Encoder E = /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19/code/vendor/encode_skel_b.py; SHA256 d0002e60d11ef5cba568309fde5b15e29280ca127bc0e6bb1f4d22929a5628e5. Read only. Lines3-8 specify type/private/empty row order; lines77-99 construct membership sets and fix the P0 quad membership. This is a definition bridge, not reliance on any computed CNF or list.

S header bytes[0,433) specify five P0 profiles (4,3,3,3,3,3), three P1 profiles (4,4,3,3,3,2), c0=5,L=0 and71 skeletons. Index b is ZERO-based position in its `skeletons` array.

## Exact S case excerpts (verbatim)

b63 = ms09_s00050; bytes[4256,4338); V lines4738-4785:
{"types": [[0, 1, 2], [0, 4], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], "empty": 7}

b65 = ms09_s00052; bytes[4421,4503); V lines4833-4880:
{"types": [[0, 1, 2], [0, 3], [0, 4], [1, 3], [1, 4], [2, 3], [2, 4]], "empty": 7}

b66 = ms09_s00066; bytes[4505,4592); V lines4881-4931:
{"types": [[0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], "empty": 7}

b68 = ms09_s00068; bytes[4686,4773); V lines4984-5034:
{"types": [[0, 1], [0, 2], [0, 4], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], "empty": 7}

## Full labelled rows for the proof (not abstract counts)
Each listed type denotes one distinct row. A private p_i denotes a distinct row of singleton type{i}; p0' is a second such row, not another name for p0. Empty rows e1,...,e7 are distinct labelled rows of type empty.

| case | degrees of listed types at0..4 | private rows | full row count; total quad memberships |
|---|---|---|---|
| b63 | (2,3,3,3,4) | p0,p0',p1,p2,p3 | 7+5+7=19; 15+5=20 |
| b65 | (3,3,3,3,3) | p0,p1,p2,p3,p4 | 7+5+7=19; 15+5=20 |
| b66 | (2,3,3,4,4) | p0,p0',p1,p2 | 8+4+7=19; 16+4=20 |
| b68 | (3,3,3,3,4) | p0,p1,p2,p3 | 8+4+7=19; 16+4=20 |

For every c the fixed Q_c is EXACTLY the set of these labelled rows whose type contains c; it has4 members. The seven E rows are the actual distinct rows, not interchangeable occurrence slots when filling blocks. The proofs quantify over every arrangement of these19 rows into the column profiles, modulo only the explicit b65 permutations of indices0,1,2 and identical-profile P1 column renamings.

No first-P1 placement list, denominator, solver count or encoder output is used as a proof premise. V binds status/identity only; S+E bind the actual case definition. All four remain unclosed by this continuation.
