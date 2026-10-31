# Additive erratum 2 — the unproved two-28-coset fibre-shape bridge

Owner MathShor-2. Actual `/bin/date` before composing: **Mon Oct 26 04:58:38 PDT 2026**. Exact WRITTEN symbolic arithmetic only. No scientific execution or new GO.

The frozen summary `shor-FACT-size-frontier-summary-v1.md`, SHA256 `3822f4c3ea77f1d94fec3451481df5542aebf3b67120ad1bdb59d6167104fe9d`, remains unchanged. Main reported that v112-C/D returned with a distinct unproved bridge at its LF58. Parent complete reading/adoption is PENDING; I do not inherit either review's verdict or infer a counterexample from that notification.

## 1. Withdraw the universal shape assertion as established

The LF58 sentence asserts that EVERY parity-constant fibre with several residues mod7 has the form

    b + {0,delta} + 28 Z_N,  delta = 2 mod4,  7 not dividing delta.

The delivered proof does not establish this for every fibre. Withdraw its unconditional proof/acceptance status. It is **NOT_RECONSTRUCTED**, not an independently certified false statement or a new FACT witness. This does not withdraw the separately written R2 congruence argument or the mod4 count balance; those require their own full gates and are not promoted by this erratum either.

## 2. Exact consequence of the existing halving argument

Here |A|=14, N=2^v 7^w, and a fibre X has size N/14. The prime-size leaf argument in Theorem C §3 uses only that q is odd, so its fibre calculation also applies with q=7. Its first leaf is at level ell<=3, because the two normalized seed sets carry 0,4 then0,2 then0,1. If v=2 the level-2 group has odd order, and2 itself is a unit as in erratum E1; there is no level-3 requirement in that case.

At leaf ell, every nonempty recursively halved piece is a FULL coset of7Z_(N/2^ell). Lifting gives a union of exactly2^(ell-1) distinct cosets of2^ell*7 Z_N: this number is the ratio (N/14)/(N/(2^ell*7)). R2 excludes ell=1 if R2's proof is accepted, but it does not exclude ell=3.

- **ell=2:** exactly two28Z_N cosets. They occupy the two even residues mod4 after translating the fibre to contain0. Their difference is2 mod4. If the fibre has several residues mod7, that difference is not divisible by7. Thus LF58 is supported IN THIS SUBCASE.
- **ell=3:** exactly four56Z_N cosets. After translating to contain0, they occupy residues0,2,4,6 mod8, one coset at each residue. Their mod7 offsets are not fixed by the leaf argument. A merger into two28Z_N cosets would require additional translation relations between the representatives differing by28. Those relations were not proved.

In particular, the existing halving proof establishes a finite union of56Z_N cosets, not the universal two-28-coset form. No assignment of the remaining offsets, actual FACT example, or global nonexistence conclusion is supplied here.

## 3. Exact remaining boundary

Either prove the missing merger relations from the FULL FACT/three-mate constraints, or retain the four-coset level-3 possibility. Restating the smaller-period filter is not progress toward the original all-order finite-code question. The general raw PR, isolated-word, higher-gap, heterogeneous-delay and STAB/GP obligations remain unchanged.

H* stays FALSE/WITHDRAWN. The I3/I4 proof boundaries and the distinction FACT660-divisibility versus inherited full-code1320-divisibility remain. Own permanent v109-A exactness MAJOR and all earlier histories are preserved. No source/shared/frozen file is edited. This is unreviewed WRITTEN correction, not parent adoption, formal/kernel/human/configured-family/executable/novelty acceptance. Original cutoff and deadline unchanged.
