# f678 additive correction: parent v1 failure, exact successor, and indicator sign

This addendum preserves the original author narrative, v1 source and parent evidence without modification. The original narrative's statement that the **child** had not run scientific code remains true. Its then-current statement that the parent run was still unpaid is now historical: the parent has since performed one v1 run, which **failed**. No successful finite-source result or adoption follows.

## Parent-observed v1 run

The parent reports full source read and GO followed by one run of `independent-boolean-physical-profile-v1.py`, SHA-256 `4ee2939d220fecce13afe08a65de3b8e6c2513507ea8ae64ab679fe2bf1dc460`. The retained [parent receipt](parent-independent-finite-run-v1-receipt.json) records exit 1 after 0.11781558400392532 seconds, empty stderr, 64 physical case records, zero profile-vector records and two negative-control records. Parent's reported terminal failure is `CONTROL_WRONG_REASON_independent-u`. The receipt pins the retained stdout SHA-256 `60a5f7bb48fbbf5dbcdb8a08ce869275e2d35f2a5185011ed1f13108b251ca8d`. Those 64 records are partial run evidence, not a complete checker PASS or an independently accepted theorem.

The two controls reached before that failure were `wrong-normalization` and `free-balance-instead-of-specified-t`. The independent-u control failed its **expected-reason check**, and the subsequent graph-y-relation, odd-J, U3-residue, actual-U0-cap, six-span scope, and false-witness controls were **not reached**. The 1,136-vector enumeration and COMPLETE marker were **not reached**. The written classification `16 + 14*8 = 128` remains a written derivation, not an observed v1 census. The capped-instance mod-16 test, V and the original caller remain unpaid; no capped witness or five-span exclusion is established.

The failure is explained by the source itself. `check_common_u` examines each c in increasing order and checks x, then `3a`, then g, then y. For its all-zero-u mutation at the first block c=0, the requested x and `3a` are zero, but the requested g is 4. Thus the first actual violation is `COMMON_U_G`, not `COMMON_U_X`. The intended control remains meaningful: it rejects a separately supplied zero u because it does not produce the common physical g fibre. It is a deliberately invalid input/scope control, not a scientific counterexample.

## Standalone v2: one-line change only

The new standalone source is [`independent-boolean-physical-profile-v2.py`](independent-boolean-physical-profile-v2.py), SHA-256 `f98a3733b451264b18d8bf402021c5b9f029bed1a61bd1c4abca7a9f003d3411`. It was created as a copy of v1 and then changed by the following exact line replacement at line 500; neither the mutation nor its checker order is changed:

```diff
-    expect_reject("independent-u", "COMMON_U_X",
+    expect_reject("independent-u", "COMMON_U_G",
```

No other source change is intended. In particular, the source still emits the actual 64 physical cases and individually enumerates all 1,136 energy-four profiles; it still labels the uncapped example's Theorem 3 mod-16 case `NOT_TESTED`, enforces its cooperative 45-second deadline, and makes no full-caller or V claim. The correction has **not** been executed, imported, compiled, tested, linted or formatted by this child. It is a prepared successor, not a passing result. Parent must read the complete v2 source and exact change, bind its actual bytes/hash and interpreter/argv, issue a **new** GO, and supervise a new bounded run before treating any v2 output as evidence. The earlier v1 failure, receipt and retained output remain permanent.

## Correction to the graph-indicator Walsh sign

The original narrative's sentence in §3 saying that `hat(1_S)` at h-frequency zero is “0 or 16” omitted the ell-frequency sign. The correct statement is **0 or ±16**. If `(A,H0,J,B)` are the covectors on `(ell,h,j,b)`, then for H0=0,

```
hat(1_S)(A,0,J,B)
  = (-1)^A * sum_(j,b) (-1)^(J dot j + B dot b)
  = 16*(-1)^A  if J=B=0, and 0 otherwise.
```

For H0=1, summing over b first gives zero unless B=0; then the sum is four times a two-bit bent transform, with the additional `(-1)^A` factor, so it is 0 or ±8. Therefore the original conclusion that **every graph-indicator coefficient is divisible by 8** is unchanged, but the sign qualification above must accompany that claim. This correction is written reasoning, not a new scientific execution.

The original five-span/carry/common-u boundaries, all held-episode and consumer exclusions, and the absence of novelty, original-target closure, external-family, human, or formal/kernel acceptance remain unchanged.
