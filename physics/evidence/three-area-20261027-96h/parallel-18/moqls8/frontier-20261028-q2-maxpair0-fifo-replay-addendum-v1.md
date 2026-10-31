# Addendum: owner-local measured replay of the q2 support proof

This is additive to `frontier-20261028-q2-maxpair0-support-candidate-v1.md` (SHA256 f2bc1cce50e85f575a2a30cd729c258018b0121fa1aec30d01fc27be88ef5d08). Its physical/encoding claim is unchanged. This records **owner-local** measured transport and drat-trim replay; it is not a disjoint parent replay, mathematical review, or global q2 theorem.

`frontier-20261028-q2-measured-fifo-replay-v3.py` SHA256 **0e2b5e95f5cf25a8c4a4e9b175b60d8165bfa29257467c399647d1ce11508945**; complete receipt `frontier-20261028-q2-measured-fifo-replay-receipt-v3.json` SHA256 **bd8a9eaa2913dffaf784f958fdf51f654d5150e28c41ecfc1498259ceab6a4f9**; actual-process receipt `frontier-20261028-q2-measured-actual-v3-receipt.json` SHA256 **5d726a081bc791218d2137c3789d0488a5bdeddce48fd1d8c083ef4a3194c5d6**.

The driver checks the pinned 4,448,734-byte ASCII trace's final empty clause, converts all 70,359 steps to binary DRAT, and independently decodes the binary stream back to the identical step sequence. The generated binary stream is **2,039,543 bytes**, SHA256 **52f15e57fef8123d21c2d2f76302664c5283bb2d874ea9fec93f23efc9a58d38**; it is not written to disk. The pinned 698,608-byte CNF was sent through a named FIFO, and the binary proof was sent through the checker's stdin. The sender reports exactly 698,608 CNF bytes/hash `0194fa8d...e318791a` and 2,039,543 proof bytes/hash above, both writers closed without error; a retained non-reading FIFO descriptor reported **0 unread CNF bytes**. A held writer was closed after observed FIFO drainage while the checker was running. The checker parsed exactly 6,160 variables and 27,538 clauses, reported reading exactly 2,039,543 proof bytes, returned exit 0 and exactly `s VERIFIED`, with no stderr, safety stop or warning. CNF, ASCII trace and checker hashes matched again afterward. No measured resource-RSS interpretation or future/parent result is inferred.

The same measured harness exercised five prior controls:

- tiny UNSAT/RUP: exact transport and `s VERIFIED`, exit 0;
- tiny satisfiable formula with bogus empty proof: exact transport, `s NOT VERIFIED`, exit 1;
- proof for the wrong formula: exact transport, `s NOT VERIFIED`, exit 1;
- truncated CNF: checker output contained `s VERIFIED` but exit 1 and transport mismatch; strict predicate **rejected**;
- truncated proof: checker output `s VERIFIED`, exit 0, but proof byte/hash/count mismatch; strict predicate **rejected**.

These controls make the delivery predicate, rather than an isolated checker status, essential. FIFO nodes were retained; no deletion was performed. The earlier two failed preflights remain recorded: v1 failed before retaining its internal control state (`frontier-20261028-q2-fifo-v1-failure-v1.json`, SHA256 ff32579b1c503e19fd06ef5c06b94029d4180fe742f751daf131131014be462a); v2 measured its tiny positive feed but falsely rejected carriage-return-prefixed `s VERIFIED` because of a status parser bug (`frontier-20261028-q2-fifo-v2-failure-v1.json`, SHA256 dc9eb38518eb014f431f519c69b26e65b3ef9c6f5fba07a31fa1127c0ac5d77e). V3 removes only CR characters before exact status-line comparison and uses fresh FIFO names. Neither failed preflight is reclassified as successful.

Remaining acceptance obligations: a separately owned replay from independently regenerated input under the parent protocol, disjoint review of the physical support reduction, the CNF and its auxiliary-variable/triangle clauses, conversion/replay driver and controls, and no inference beyond the one specified two-MOLS net.
