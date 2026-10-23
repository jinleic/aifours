# Continuation state (not an additional user instruction)

Session start 2026-10-15 21:23:55 UTC. Deliver by 2026-10-16 00:16:55 UTC,
minute 173. Hard stop 00:47:55 UTC, minute 204. No network, outside-workdir
reads, installs, delegation, commits or external contacts. Four CPU-intensive
workers maximum; 4 GB RAM, 1 GB disk. All-orders conjecture remains unresolved.

At 22:17:39 UTC, main paired C scan was running in exec session 59024:
`python3 code/run_epoch2.py main --cap 7200`. It started 21:43:13 UTC.
Two workers per scanner = four CPU workers. Latest common complete prefix had
4423 matching blocks through 1090467516416. No logged survivors. Do not restart.
Inspect cheaply with `python3 code/live_epoch2.py`, or poll session 59024.

Both full control runs completed first: every even n in [2,5e9), 2499999999
members, 299 blocks, matching FULL-residue hashes; exactly the published seven
values. Times 392.57/666.27 s. All 960 arithmetic vectors passed, including 90
synthetic large positive vectors. Tiny 9999 even-n controls and all 67108864
benchmark members received Python replay. Current fully replayed prefix is
[200000000000,201610612736); current root claims.json has 10 scoped claims.

Expected next work:

1. Faster scan128_digest should finish around 22:33 UTC. Only after its REAL
   footer exists, launch `python3 code/prefix_epoch2.py --no-pause`. It uses two
   Python processes while scan32 still uses two CPU threads, so total stays four.
   It completely replays groups 00..07, each 32 blocks, total 256 blocks,
   2147483648 progression members, final prefix end 251539607552. Uses Cipolla
   roots and Python pow; each group estimated 160-200 s, below 295 s timeout.
   The checker can read completed numbered blocks from a still-running scan
   without inventing a footer. No signals are used: earlier pgrep was unavailable
   and no process was paused. The no-pause helper waits for faster completion.
2. Both main scans should finish around 22:52 UTC (target [2e11,2e12), exactly
   75 billion n=8 mod24 members, 8941 blocks). Wait for real footer and run:
   `python3 code/check_epoch2.py compare --task main --output evidence/epoch2/main-log-check.json`
   `python3 code/check_epoch2.py samples --task main --output evidence/epoch2/main-sample-check.json`
   Only add these CPU tasks when slots are free. Samples check full ordinary
   residues AND actual smallest factors, and hash every member of each 64-n
   audit window including factor members. Whole decision streams use zero
   (explicitly uncomputed power) for factor records, full residues for unsieved.
3. An optional capped continuation is authorized by the research task and is
   prepared: `python3 code/run_epoch2.py extension --cap CAP`. It starts at 2e12,
   plans 4e12, uses ONE thread each (two total), and compares only the last common
   unbroken completed prefix. Choose CAP<=2700 s and also <= remaining time to
   minute173 minus 1800 s complete replay budget and 600 s final margin. Main plus
   extension max elapsed production must remain <9000 s. Do not sacrifice replay.
   Target 2e12 itself is the required priority; an incomplete extension is fine.
4. Run compare/samples for extension after it ends, writing extension-log-check
   and extension-sample-check JSON analogously. `deliver_epoch2.py` requires those
   files before publishing each completed production claim.
5. `python3 code/deliver_epoch2.py` updates REPORT and atomically replaces claims.
   It preserves completed new sample logs as byte-exact deterministic gzip,
   verifies decompression, then removes redundant RAW copies. Checker reads gzip.
   It is safe to rerun, reconstructing integrity metadata from the gzip versions.
6. Test EVERY final claim command on an actual delivery-limit copy:
   `python3 code/snapshot_epoch2.py` (single Python CPU). Expect about 23-26 min
   total, <=1800 s; each command <=295 s. It runs only python3, never a local
   binary. Negative controls must fail with CHECK FAILED. Prefix groups are
   fully replayed once more here because the user explicitly requires copy tests.
   If too slow, reduce claimed prefix groups; never overstate a skipped replay.
   Only then `python3 code/deliver_epoch2.py --final`; it asserts all current
   command strings were tested and all expected outcomes passed.

Delivery currently about 33 MB, 287 files, only 3 inherited oversized logs
skipped. Old logs are restored from 33 manifest-checked gzip parts. Final
sample compression should keep the delivery <50 MB with margin. Package-only
test leaves a hidden .delivery-epoch2 copy, removed automatically by the next
snapshot run. Workdir disk remains far below 1 GB.

The root REPORT/claims are authoritative and supersede inherited archives.
The inherited entire endpoint 10341223092224 is still one entire-range C report:
conditional on the imported premises AND that single entire execution being
correct. Hashes/aggregate counts are not arithmetic proof. New paired C runs
share author/compiler/OS/SHA and exponentiation recurrence; modular multiplication
and root algorithms differ. Do NOT call the whole target Python-replayed or
externally certified. Manual Python control flow shares CPython arithmetic.

Pure/related mathematics retained: Hall-type closure corollary (likely prior
art Hall 1947), power-of-two family 3<a<59049 via known-looking factors, and
fixed-filter limitation. Next exponent a=59049 factor progression found no
factor through q=1e14 in 60 s; this is no primality claim. Raw last_k is loop
cursor, one beyond tested index on exhaustion; unused by claims. Moment proof
is elementary but likely classical: all even binomial moments characterize
planarity; n=8 passes, n=24 first fails t4, n=90/512 fail t2. No universal proof.

Important checker hardening already applied before full prefix work:
fixed task scopes, real coverage, matching actual factors/full unsieved residues,
explicit failure on ANY unresolved main/benchmark/extension base-two hit, per-window
full-residue hashes, and correct common prefix when capped runs differ in length.
SymPy is NOT installed in active python3; use existing standalone Cipolla code.

Keep concise commentary at least every minute during ongoing work. No need to
ask permission. Final answer must say partial and link REPORT/claims; no all-orders
resolution or novelty claim. Ensure deliverables complete before minute173.

Update 22:35 UTC: scan128_digest finished target, real footer at 3063.443535 s. Prefix helper is RUNNING in exec session 46381 (started 22:34:30), two Python workers, while scan32 uses two CPU threads. Main wrapper remains session 59024; do not restart either. Latest common prefix 6671 blocks through 1543049695232, no hits. Poll prefix output or evidence/epoch2/prefix-groups. Publish as groups complete.

Update 22:45:33 UTC: ALL eight prefix groups PASSED (163.5-166.5 s each). Prefix session 46381 is complete. Fully replayed prefix end 251539607552, 2147483648 decisions. Published root claims now 17 claims. Main scan32 still running about 7900/8941 blocks, faster scanner complete. A one-CPU 300-second factor witness search is started using code/try_factor_epoch2.py; expect it finished by 22:51 before main around22:53. No more than scan32 two CPU threads plus factor one.

Update 22:55 UTC: BOTH main scans COMPLETE, 8941 matching blocks, 75000000000 members, zero hits, end2000000000000. Times128=3063.443535,32=4203.038957. All8 Python groups complete, exact prefix end251539607552. Main compare output evidence/epoch2/main-log-check.json; main sample check complete40166 records (34631 factor/5535 unsieved),71 windows,29.27sec. Publisher ran: claims18, main records preserved as gzip and redundant raw removed after byte-exact check.
Extension is RUNNING in exec session23592 via code/continue_epoch2.py, cap2592sec, started22:53:42.767UTC, ends about23:36:55UTC. One scanner thread each=2CPU workers. Main wrapper59024 done; prefix46381 done; sample7006 done; factor23413 done (300s, no factor through lastq499603472252929, planned1e15notexhausted). No extra workers currently.
After extension finishes, run compare and samples --task extension --output evidence/epoch2/extension-log-check.json and extension-sample-check.json; then publisher. Must test ALL final commands with python3 code/snapshot_epoch2.py, estimated23min (<1800sec), everycommand<=295sec. Publisher now sorts expensive python-prefix claims LAST, so cheap integrity/controls fail early. Final publisher --final checks allcommandstrings matched successful snapshot replay and limits. All current code changes saved.

Update 23:15:33UTC: Added complete independent boundary-window replay [1999859732480,2000201326592),14233088 decisions, main8940+extension0,10.001s. At n2e12 checked full residue3579568361430832764278755 and actual proper factor7 against both C first audit records. Artifact evidence/epoch2/boundary-window.json; checker code/check_boundary_epoch2.py, verify default, negative --broken (endpoint) fails. Publisher includes separated-window claim and explicitly does NOT enlarge contiguous bound. Root claims19 now; final20 after extension claim. Expect31 total final replaycommands and about23minutes, still <1800sec. Boundary checker auto-reads extension gzip after publisher removes raw. All new code saved, no producing C code changed.

Update 23:21UTC: Added full Python extension block988 audit containing n=2^41, exact interval[2198910672896,2199111999488),8388608 decisions,5.762s, all matched, no hits. Artifact evidence/epoch2/power-boundary.json; verify python3 code/check_epoch2.py blocks --task extension --blocks 988; negative same with --broken. Publisher activeclaims20 before finalextension, final21claims,33 replaycommands. Generalprefix remains251539607552; new windows separated only. Final totalreplay estimated23minutes~1400seconds(<1800), maxgroup166.5s(<300). Still no extra CPU workers aside from two continuation scanners.

Update23:38UTC: ContinuationCOMPLETE, common2892blocks,24259854336members, end2582236504064,zero hits. C1284011blocks seconds2592.342876; C32 2892blocks seconds2592.452717. Session23592done. Both extension-log-check and extension-sample-check JSON produced;12994 samples(11240factor/1754unsieved),23windows,8.366s. Publisher nowfinal21claims,33commands; allrawnewrecordsgzpreservedbyte-exact and rawremoved. Only remainingtask runFULL python3 code/snapshot_epoch2.py on finalcopiedsnapshot,estimated23min (~1400s total,<1800),then python3 code/deliver_epoch2.py --final and finalschema/packcheck. No C production running. Deadline minute173=00:16:55UTC; startingtestabout23:39 leaves38min. Finaluniversaloutcomepartial, no all-orders proof. Expectedactualfinisharound00:02.

FINAL REPLAY ACTIVE: exec session71464, started23:39:17UTC, currentfinal21claims33commands. Cheapcontrols/main sample26.65s/extsample8.45s/oldmetadata6.99s/joinwindow9.18s passed on actualdeliverycopy. Prefix groups (~160s each) now running. DO NOT restart whole replay. Poll session71464 or evidence/epoch2/snapshot-replay.json. No C production remains. All outputsfromcopy are captured in ledger; finish expectedabout00:02, harddelivery00:16:55. Once ALL PASSED, run publisher --final, finalschema/packagemarginchecks, finalbriefpartialanswer.

COMPLETE 2026-10-16 00:01:23UTC (minute157.5): ALL33 final commands passed on actual delivery-limit copy. Total1257.646s, max150.159s. All10 negative controls rejected;23 positive commands passed. Publisher --final and final schema passed; phasecomplete, outcomepartial. N_python251539607552; N_paired2582236504064 conditional on imports AND executions; all-orders unresolved. No background computation remains. Final package-only check and short final answer are the only housekeeping left.
