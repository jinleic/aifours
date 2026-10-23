# Receipt: numeric_structure_probe_v1 (the single parent-GO float probe)

NOT A CERTIFICATE. A numeric miss is UNKNOWN. Nothing here excludes any ansatz, restricted or unrestricted.

## Admission and inputs

- Authority: parent GO for ONE <=5-minute standard-library float/complex probe (Main IRC, after 14:11 PDT).
- Pre-registration: numeric_structure_probe_v1.prereg.json, sha256
  da184627296edbb6f2cb803109eb78c143d82ee8db08b0cf7e8e4b608f3ff07e, frozen read-only 14:15:29 PDT.
- Script: numeric_structure_probe_v1.py, sha256 268edffc29703fe9ccdd73de5a3c0f7bacf3e89299073a78162f21db2a454910,
  frozen read-only. py_compile was run before freezing and created __pycache__ (lane-local, retained).
- Admission free space (df -k, 14:15:29 PDT): 13,481,033,728 bytes, which is >= 12.2e9 + 1 MiB projected growth.
- Interpreter: /opt/homebrew/bin/python3.14 (3.14.3), standard library only. One process. TMPDIR = lane tmp/.
- Bash tool deadline disabled (timeout 0). No subprocess timeout, SIGKILL or ulimit.

## Execution

Actual command:

```
cd <lane>/probes && /bin/date '+START ...' && /usr/bin/env TMPDIR=<lane>/tmp /opt/homebrew/bin/python3.14 numeric_structure_probe_v1.py numeric_structure_probe_v1.result.json; echo "EXIT=$?"; /bin/date '+END ...'
```

- Host times: START 2026-10-18T14:15:38-0700, END 2026-10-18T14:19:49-0700. EXIT=0. In-script elapsed 251.2 s.
- stop_reason: **DISK_FLOOR free=11999363072**. The in-run statvfs guard (floor 12e9, checked every 5 s) fired. This was
  a cooperative stop, not a completion.
- free_bytes_start 13,479,632,896; free_bytes_end 11,999,064,064. Fresh df at 14:20:05 PDT: 11,771,092,992.
- The lane wrote about 50 KB in total, so this probe was not the writer. No causal writer is established. The breach
  was reported to the parent at 14:20 PDT.

## Output

- numeric_structure_probe_v1.result.json, sha256
  b854adf9a9fa8adc80bbb3f07a120f1495f9ffdf14fc00e00390b86e748d6346, 9141 bytes.
- frontier []: every pre-registered sub-run started.
- The G10 time slice was cut short by the disk stop: about 161 s used of 170 s, 7 starts. Every G10 start had already
  ended by step-size collapse (eta < 1e-14) at a local minimum.

## Numeric residuals

| run | result | meaning |
|---|---|---|
| W5 control (d=5, lam=1) | best f = 6.7e-32 over 6402 starts in 6 s | candidate; method works on known-solvable WH case |
| W10 lam=1 | best f = 0.20201113333 (41 starts) | no candidate |
| W10 lam=3 | best f = 0.05228313137 (43 starts) | no candidate |
| W10 lam=7 | best f = 0.05228313137 (40 starts) | no candidate (equal to lam=3, consistent with lam -> -lam symmetry) |
| W10 lam=9 | best f = 0.20201113333 (40 starts) | no candidate (equal to lam=1) |
| G8 control (B = i XOR j) | f = 1.23e-8, maxdev 8.5e-6 after 22080 iterations (40 s); still decreasing sublinearly | **did not reach the 1e-9 candidate threshold**; it approaches a degenerate solution with 48 rays at tol 1e-6 |
| G6 calibration (Cay(Z6)) | stalled at f = 4.8231, maxdev 0.173 | as expected (no 1-RQLS(6)) |
| G10 (Cay(Z10)), 7 starts | stalled at f = 11.45 .. 13.25, maxdev 0.19 .. 0.24 | no candidate |

## Interpretation (pre-registered rules applied)

- WH10 orbit ansatz: no numeric candidate. The best residuals repeat across starts (0.0523 and 0.2020), which suggests
  a positive minimum. This is a lead for an exact impossibility proof of the R4 open sub-case. It is not a proof.
- G10: plain projected descent from random starts stalls far from zero. The G8 control shows the method converges only
  slowly even where solutions exist, so the G10 miss carries little information. Quantum orthogonal mates of Cay(Z10)
  remain **UNKNOWN**.
- No reconstruction lead for a maximal-cardinality 1-RQLS(10) came out of this probe.
