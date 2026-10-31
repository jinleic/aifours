# info-6: maximal-magnitude layer couples every phase and every shift

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Actual `/bin/date` observed before this write: **2026-10-27T15:00:45-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** This gives conditional structural constraints on all actual original-target spectra; it is not an unrestricted exclusion, witness, new nonlinearity bound, rank/type classification, formal/kernel or novelty claim. No scientific program, selected numeric state, direction or diagnostic was used.

## Claim

Suppose f is balanced on F₂⁹ with |W_f|≤28, put k=W_f/4, and let T=Σ_{x:f(x)=1}x.

- If T=0, at least 411 frequencies have |k|=6. Under **every** character modulation χ_x, at least 151 of these are positive and at least 151 are negative. For **every** nonzero b, there are at least 44 unordered pairs {a,a+b} of |k|=6 coefficients with equal signs and at least 44 with opposite signs.
- If T≠0, at least 34 frequencies have |k|=7.

Both parity branches, every modulation and every shift are included; no attainability of any bound is claimed.

## Proof

The released actual-object caller gives k(0)=0, Σ_a k(a)²=2¹⁴, |k|≤7, and zero shift autocorrelation at every b≠0. Its parity identity is k(a) mod 2=a·T.

If T=0, all k are even and |k|≤6. Let n₆ be the number with |k|=6. All remaining nonzero coefficients have square at most 16, and there are at most 511 nonzero frequencies. Thus

    2¹⁴≤36n₆+16(511−n₆),  so n₆≥411.                            (1)

For an arbitrary phase χ_x, let A,B be positive and absolute negative sums of kχ_x. The Boolean inverse gives |A−B|=128 and energy gives A+B≥2¹⁴/6. Hence A,B≥3904/3. Of all frequencies outside the |k|=6 layer, at most 511−n₆≤100 carry a nonzero coefficient, each of magnitude at most 4. If p₆(x) is the number of positive |k|=6 coefficients in this phase, then

    6p₆(x)+4(511−n₆)≥A≥3904/3,

which forces p₆(x)≥151. The same holds for negative |k|=6 coefficients. Nothing here chooses x.

For an arbitrary nonzero b, the number m of unordered {a,a+b} pairs wholly in the |k|=6 layer is at least n₆−256≥155. Let p,n count their equal-sign and opposite-sign cases. Their signed autocorrelation contribution is 36(p−n). Every other one of the 256 unordered pairs contributes magnitude at most 24, so zero total autocorrelation gives

    36|p−n|≤24(256−m),  and  min(p,n)≥(5m−512)/6≥263/6.

The integral counts are therefore at least 44 each, for every b≠0.

If T≠0, exactly 256 k-values are odd. Let n₇ count |k|=7. The other odd coefficients have square at most 25, and the even half contains k(0)=0 and at most 255 other coefficients with square at most 36. Thus

    2¹⁴≤49n₇+25(256−n₇)+36·255,

which forces n₇≥34. ∎

## Limits

These are necessary conditional phase/support constraints and do not establish that either parity branch occurs. They do not exclude every possible spectrum or supply the exact Boolean inverse. The original alternative remains an actual balanced peak-28 witness or a universal no-go covering all arrays and all rank/weight cases, including `(24,24,2)`.

Inputs are the S1 supplied definitions and the exact actual-object autocorrelation/parity caller in `prerequisite-derivation-v1.md`, SHA-256 `075f61ffe1b5cfb000bb3bbda9ddd7fefea04e27806f19bedd9c5a2318fa3df9`, 87 LF, together with elementary inequalities. No old Gate-I/candidate/held source or selection/method guide is an input. Source/book equivalence, independent full-scope written review, human, formal/kernel, executable and novelty gates remain unperformed. All S1 STOP/HOLD/ZERO, N4 UNKNOWN and aux214 STOP persist.
