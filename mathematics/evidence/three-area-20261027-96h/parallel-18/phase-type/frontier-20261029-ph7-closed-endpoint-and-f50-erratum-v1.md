# Erratum: closed right endpoints for every supremum bracket; f50 lower end

MathResearch96h-2, original math-1. Actual native clock observed before writing: **Thu Oct 29 08:23:59 PDT 2026**. Additive; no pinned byte changes. It applies the parent erratum `dispositions/math-1-ph7-supremum-bracket-closed-endpoint-erratum-v1.json` and the parent disposition `dispositions/math-1-ph7-algebraic-endpoint-closed-band-parent-v1.md` (f50) to this owner's packets.

1. **Closed right endpoints.** Excluding every ratio z>=z0 proves only `sup Z7 <= z0`; it gives no gap below z0. Hence every bracket for the supremum of PH7-realizable ratios has a CLOSED right endpoint. Read
   - `frontier-20261029-ph7-impossibility-above-0p8765-v1.md` (SHA256 `8084804cabea6159bf5bebe588c593d87abcf43090313a07483ef278a86cc7ff`): "[0.8204, 0.8765)" as **[.., 1753/2000]**;
   - `frontier-20261029-ph7-impossibility-above-0p85-v1.md` (SHA256 `a624b358c71e838963c8250bfb82af2e54b06f3bc886332abcc3891a3e24f133`): "[0.8204, 0.85)" as **[.., 17/20]**;
   - `frontier-20261029-ph7-impossibility-above-0p83-v1.md` (SHA256 `f9e9847de445dc8887c54ec29b72d34e579268b079dc8e146c1b357f7d6c67a5`): already closed ("[41/50, 83/100]", "[41/50, 0.83]"); no change of endpoint type.
   Phrases such as "existence region lies in z<0.85" mean only that no z>=0.85 is realizable.
2. **Lower end after f50.** The parent has adopted the v4 closed band `[7/9, z_*]` with `820420341/10^9 < z_* < 820420541/10^9`. Therefore the lower end in all these packets and in the MINOR-fix addendum (`frontier-20261029-ph7-f159-f160-minor-fixes-addendum-v1.md`, SHA256 `a447c10752b9c876b8eaa9754ce5246bda11e40778f26bf98fa5c4fd345ac4d1`, §5, which still called v4 "unreviewed-by-disposition") is now z_*: the adopted bracket is **[z_*, 17/20]**, and the unreviewed 0.83 candidate would give **[z_*, 83/100]**.

No mathematical statement, certificate or digest changes. No review, formal, novelty or priority claim.

END - closed right endpoints; lower end z_* after f50.
