# Checkpoint 011 (rqls10 continuation, successor worker) - hand-off

Recorded 2026-10-19T02:47:03-0700 (from /bin/date). Owner ContinueRQLS10b. Target OPEN / UNKNOWN; no candidate; no
process running; lane tmp/ empty; every new file 0444. R9 GO requested from Main at ~02:28 (no answer received yet);
this worker launched only stdlib probes and will not launch R9 unless the parent's GO names it as owner.

## Actual results since 010
- Float analysis w8_exotic_structure_v1 (EXIT 0): the 100 exotic flat planes are each invariant under exactly one of 25
  WH-conjugates of an order-3 Clifford U (cycling X -> Z -> T), 4 planes per conjugate, each = line(E_omega) (+)
  line(E_omega^2); compatible exotic b-couples change the stabiliser label by an element of L_b; 0 all-exotic K4 patterns.
- evidence/w8-decision-v1-addendum-1.md: Lemma 5 (exact): under that label rule all four representatives share one
  stabiliser, so W8 would reduce to a finite exact check (4^4 assignments for U_0); exact closure plan (E1)-(E4).
- README-addendum-1.md (navigation).

## New files of this worker (sha256)
checkpoints/008 e273d3e4...1153, 009 ce153c6b...7ece, 010 d72f1bb1...bf94, 011 (this file)
code/rqls_assay_v9.py e907968609f9e90c1c25891068227f3117a7ec44691338494b5d99cd772164db
code/z5_flat_rank2_projectors_v1.py be9dd762...a190; code/w8_flat_planes_couples_v2.py 7e5b5fd2...626b; v3 232b202f...1c16;
v4 8d0c715e...64e9; v5 09ea8ab1...0f73; code/w8_exotic_structure_v1.py 2c0bff3d...9ded; code/z9p1_resolution_classes_v1.py
f2dcfead...7186
evidence/w8-decision-v1.md b24334cf9a255bab9fb08aa49a583f5ca6c654dcd2f776f74e2cf361fe595829
evidence/w8-decision-v1-addendum-1.md 716051d982f4e6ceed6664148cd0ce5077701dda9264a8952e34c5c4123797f5
evidence/structure-and-wh10-ansatz-proposal-v1.md 68a6c9c313a468c31e0fe7ca77769789c6829a9f9396ea7bc979b8bbcd31db37
evidence/rqls_assay_v9.r9.supervisor-config-v2.json a0f04bc00be375f6c9023808131024b7d5b0c7c0a14f2b8ab33e3c405c9fc3e7
evidence/z5_flat_rank2_projectors_v1.{launch.json 19527d81...3add, result.json 193bbc47...335, receipt.md 3fa2eead...fa39}
evidence/w8_flat_planes_couples_v2.launch.json 8b75b1bb...1571 (crash, no result)
evidence/w8_flat_planes_couples_v3.{launch.json 0364c585...84d2, result.json 241219fd...4e5e, receipt.md 6f43db55...e5a}
evidence/w8_flat_planes_couples_v4.{launch.json 4a608259...60f7, result.json 039ea5e5...c9d}
evidence/w8_flat_planes_couples_v5.{launch.json 9d55893a...d7f0, result.json 0e20ee96...68fd}
evidence/w8_flat_planes_couples_v4_v5.receipt.md eedbadb9...443a
evidence/w8_exotic_structure_v1.{launch.json e231d901...81d5, result.json b13532bf...7ce0}
evidence/z9p1_resolution_classes_v1.{launch.json 9e11e233...601d, result.json 23ebb08a...93f8, receipt.md c3ed1c98...8221}
review/rqls10-r9-GO-request-v1.md 44552471981da4145d9d69ba3c9cbece3fa9897fb1aff1f03d9aca8b2010e4db
review/rqls_assay_v8_to_v9.diff 291edc71228bafc598a368d345b3ff785f5c2bc67ede294c7169cfc7c48bf157
review/deviations-ContinueRQLS10b-v1.md 272d54e4...09fe9; v2 b2c9e42c1b84e57a12c25aa4049843d938d5d31337ac2562444ddd23a7272ce2
README-addendum-1.md 1415d8dbb06069aee4f4535164b93cb20062e5aadb2525ff83cf8119fdf7569f

## What remains
1. R9: parent GO (owner named) -> fresh stability gate + owned supervisor -> receipt; gates A9/A9m/K9P/K9R must pass.
2. W8 exact closure (no GO needed): (E1) exact classification of flat rank-2 projectors (30 MUB-pair + U_w-invariant
   exotic, nothing else); (E2) label rule or exact couple graph; (E3) exact 4^4 check for U_0; (E4) Prop. B without the
   order-5 import.
3. WH_10 single-orbit ansatz: GO for a float search with its d = 2, 6 negative and d = 5, 7, 9 positive controls, or
   exact work via bi-unimodular sequences of length 10.
Deviations D-1..D-4 (review/deviations-ContinueRQLS10b-v2.md).
