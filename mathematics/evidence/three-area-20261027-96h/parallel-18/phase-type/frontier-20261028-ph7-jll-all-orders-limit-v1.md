# Critical 8/9: one real-hidden-root spectrum satisfies ALL Johnson–Loewy–London moment inequalities

**EXACT NECESSARY-CONDITION COUNTERPOINT; not a nonnegative-matrix or PH witness.** MathResearch96h-2. This extends the exact p=8,q=15 point of `frontier-20261028-ph7-newton-trace-obstruction-limit-v1.md` and `frontier-20261028-ph7-trace23-obstruction-limit-v1.md`. Those files separately check all six normalized Newton inequalities and the centered trace-two/three comparison. No conclusion below assumes the point is realizable by a matrix.

## 1. Statement and why it matters

At `z=8/9`, take the seven spectral values

    G-spectrum: 0, -3, -5, -1 +/- i sqrt(8/9) each twice.     (G*)

Their hidden quadratic is `(y+3)(y+5)`. If any Metzler G with this spectrum had spectral bound0, then `N=G+12I` would necessarily be entrywise nonnegative: each `G_ii<=0`, the diagonal sum is -12, hence each `G_ii>=-12`. The spectrum of N would be

    12, 9, 7, 11 +/- i sqrt(8/9) each twice.                (N*)

Define `s_k` as its kth spectral power sum. This file proves EXACTLY, for EVERY integer k>=1 and m>=2,

    s_k>0,        s_k^m < 7^(m-1) s_(km).                  (ALL-JLL)

The second is the Johnson–Loewy–London necessary inequality for a nonnegative 7-by7 matrix; a self-contained derivation is in §2. Together with the previously exactly checked ALL six normalized M-matrix Newton inequalities and the strict centered trace-two/three comparison, this shows that even these combined spectral-only tests do not exclude 8/9. The strict feasibility of these inequalities is not existence of G or N: (G*) might violate another spectral condition or fail nonnegative inverse-eigenvalue realization, and no PH input/exit has been exhibited.

## 2. Moment identities and JLL necessity

Let `beta=sqrt(8/9)` and write

    (11+i beta)^k=C_k+i beta D_k,
    C_0=1, D_0=0,
    C_(k+1)=11 C_k-(8/9)D_k,
    D_(k+1)=C_k+11 D_k.

Thus every C_k,D_k is rational and exactly

    s_k=12^k+9^k+7^k+4 C_k.                                (MOM)

For any actual entrywise nonnegative 7-by7 matrix N, `s_k=tr N^k>=0`; writing `a_i=(N^k)_ii>=0`, the diagonal of `(N^k)^m` contains at least `a_i^m`, so Jensen gives

    s_(km) >= sum_i a_i^m >= 7^(1-m) (sum_i a_i)^m = 7^(1-m) s_k^m.

This proves the necessary JLL inequality without importing any external spectral assertion.

## 3. A finite exact check plus a rigorous infinite tail

Let

    R=12/13,
    A20=1+(3/4)^20+(7/12)^20+4 R^20,
    A1 =1+3/4+7/12+4 R,
    B40=1-4 R^40.

Since `|11+i beta|/12=sqrt(1097)/36<R`, for every k>=1,

    s_k/12^k >= 1-4 R^k,
    s_k/12^k <= 1+(3/4)^k+(7/12)^k+4 R^k.               (BOUND)

The exact Fraction checker verifies

    1-4 R^20>0,  B40>0,  A20<7, A1<7,
    A20^2 < 7 B40,       7(A1/7)^40 < B40.                 (RAT)

These five simple rational bounds cover ALL the infinite cases:

* If k>=20, positivity follows from(BOUND). For any m>=2, `km>=40`, and the normalized JLL left side is bounded by `7(A20/7)^m <= A20^2/7 < B40`, which is below `s_(km)/12^(km)`.
* If 1<=k<=19 and m>=40, `km>=40`; similarly `7(A1/7)^m <= 7(A1/7)^40 < B40`.
* For the remaining 722 pairs `1<=k<=19, 2<=m<=39`, the checker verifies the STRICT inequality directly from the exact rational recurrence(MOM). It separately checks `s_k>0` for k=1,...,19.

There are no unverified infinitely many exponents left. The tail uses the rational upper bound12/13, not a floating approximation.

## 4. Actual verification, dependencies and limits

The checker `frontier-20261028-ph7-jll-all-orders-check.py`, **35LF/1547B**, SHA256 `0547dff4a80d67748936df45b860c9a2fa46e7076ffdd8cc50a79a0d43209f4c`, was actually run:

    Exact Fraction PASS: all positive moments and all JLL inequalities; finite pairs 722
    Tail via rational ratio 12/13, k>=20 or m>=40; no matrix-existence claim

Its certificate `frontier-20261028-ph7-jll-all-orders-certificate.json`, **21LF/525B**, SHA256 `e773f6a0f408b1262eaa3a9180b3d6d4521b4fc41d3b81c8a62012a1df11e237`, records the finite range and tail predicates. Both are exact standard-library rational arithmetic; they do not check an actual matrix, a nonnegative inverse eigenvalue theorem, or the PH transfer. The separately imported Holtz theorem and all six exact Newton margins are detailed and cited in the Newton/trace companion file, not silently assumed as an original result.

This is no all-topology impossibility proof; it is a precise reason the FULL infinite JLL family, normalized Newton list, and centered trace-two/three inequality cannot by themselves close the target. More matrix structure, stronger constraints, or same-matrix transfer/shortest-path conditions are required. No independent review, formal verification, source/novelty clearance, or actual 8/9 decision is claimed. Held outputs remain nonpremises and historic findings survive.

END — a single strict 8/9 spectral counterpoint passes all orders of the basic nonnegative moment inequalities.
