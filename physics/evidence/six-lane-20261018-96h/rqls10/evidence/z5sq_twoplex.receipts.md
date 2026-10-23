# Receipts: z5sq_twoplex_probe_v1 and z5sq_twoplex_real_v1 (initial-scope stdlib exact probes)

Recorded 2026-10-19T01:08:21-0700.
1. code/z5sq_twoplex_probe_v1.py sha256 828fed02d2f8ebb7bccb5d7dd768a91aa196e972dada113ee3bf3da309eec6d1; launch record
   evidence/z5sq_twoplex_probe_v1.launch.json sha256 ba5e00cb6848a948cd13939b5772ff864085a172e877b886880991f6ee40ca95;
   command env -i TMPDIR=<lane>/tmp python3.14 -I -B ...; START/END 2026-10-19T01:05:28-0700; PID/PGID 28511; EXIT 0;
   0.222 s; output evidence/z5sq_twoplex_probe_v1.result.json sha256 d85e622a2958ace74762d4d050e1492dda6c58fec12e0675f636d684a8458890 (0444).
   Result: 130 2-plexes of the cyclic Latin square of order 5 (points in Z_5^2, two per line in the directions
   mu, nu, mu-nu); union graphs: {'((10, False),)': 100, '((10, True),)': 30}; GF(2) phase system solvable for 0 of 130.
2. code/z5sq_twoplex_real_v1.py sha256 fb3b62d503532b5598c2400f106c7f170eebb8d400847ffa8cb24359e12854b7; launch record
   evidence/z5sq_twoplex_real_v1.launch.json sha256 f1f7f693bb96432841c9da4d0f056bdfd88acf3fff80e56733d3b24ad6c31897;
   START/END 2026-10-19T01:07:05-0700; PID/PGID 28644; EXIT 0; 0.037 s; output sha256 34547de92e94e510ca20badc01c2c3ff99658b7b740b73c783bcdf423fed8d56 (0444).
   Result: for all 130 2-plexes the 30 x 40 integer system has rank 27 (integer left kernel of rank 3) and the parity
   vector of the left-kernel basis is never all even ({'(27, (1, 0, 1))': 47, '(27, (0, 1, 1))': 83}), so the phase system
   M phi = pi * 1 (mod 2 pi) has NO real solution for any 2-plex.
Both runs settled (single processes, outputs closed, lane tmp/ empty). Exact integer/rational arithmetic, single kernel
(CPython 3.14.3); the two computations agree (GF(2) unsolvable is implied by real unsolvability).
