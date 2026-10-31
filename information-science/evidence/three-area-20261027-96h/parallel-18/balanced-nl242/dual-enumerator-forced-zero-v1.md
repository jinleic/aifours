# info-6: dual divisibility forces a nonzero Walsh zero

Owner **InfoBalancedNL242-2-2**, same original slot. Native `/bin/date` observed before this write: **2026-10-27T17:36:50-0700 PDT**. **ADDITIVE UNREVIEWED AUTHOR CANDIDATE**, explicitly permitted under the current dual-enumerator release. This uses no selected distribution, function, code, frequency, boundary case, small-case probe, numerical LP/CAS, solver, enumeration or scientific executable. It does not alter the frozen union or expand w97b's review scope.

## The all-array claim

For every formal solution of the released nonnegative integer A_t / dual-divisibility constraints, −7≤t≤7,

    Σ_{t=−7}^{−1} A_t ≡0 (mod 2),     Σ_{t=1}^{7} A_t ≡0 (mod 2),
    A₀ is odd,                 1≤A₀≤147.                        (1)

Consequently every **actual** balanced nine-variable Boolean function with Walsh peak ≤28 has an odd, nonzero number A₀ of nonzero-frequency zeros W_f(a)=0. Including a=0, the total number of zero Walsh coefficients is even and lies in [2,148]. This is a universal necessary condition; it asserts no witness, formal-system consistency, global exclusion or novelty.

## Proof of the two parity relations

The pinned exact congruence reduction gives, coefficientwise in Z/512Z[z],

    B(z)+H(z) ≡0,
    B(z)=Σ_{t=−7}^7 A_t(1−z)^{7+t}(1+z)^{7−t},
    H(z)=(1−z²)^7+256z(1−z²)^6.                               (2)

These are formal changes of polynomial variables applied to **every** A_t; neither change evaluates a selected distribution or state.

First put z=1−u and write r=7+t. Then

    B(1−u)=Σ_{r=0}^{14} A_{r−7}u^r(2−u)^{14−r},
    H(1−u)=u^7(2−u)^7+256(1−u)u^6(2−u)^6.

The coefficient of u^6 in H(1−u) is 256·2^6, divisible by 512. The same coefficient of B(1−u) is

    2^8 Σ_{r=0}^{6}(−1)^{6−r} binom(14−r,6−r) A_{r−7}.        (3)

Every displayed binomial is odd: binom(14−r,6−r)=binom(14−r,8), and for 8≤n≤14, writing n=8+s with 0≤s≤6 gives (1+x)^n≡(1+x^8)(1+x)^s (mod 2), whose x^8 coefficient is 1. Divisibility of (3) by 512 therefore makes the total of **all seven negative-t counts** even.

Second put z=u−1. Then

    B(u−1)=Σ_{t=−7}^7 A_t(2−u)^{7+t}u^{7−t},
    H(u−1)=u^7(2−u)^7+256(u−1)u^6(2−u)^6.

Again the u^6 coefficient of H is divisible by 512. The u^6 coefficient of B is

    2^8 Σ_{t=1}^{7}(−1)^{t−1} binom(7+t,t−1) A_t.             (4)

Here binom(7+t,t−1)=binom(7+t,8) is odd by the same all-range argument. Hence the total of **all seven positive-t counts** is even. Since the released first moment count is Σ_tA_t=511, A₀ is odd and at least one. ∎

## Exact upper bound and original-object implication

The 256 odd-weight terms have t²≤49, so their square sum is at most 49·256. The total square sum is 16384; the even-weight terms therefore contribute at least 3840. All 255 even-weight words include A₀ terms with t=0 and each remaining term has t²≤36. Thus 36(255−A₀)≥3840, so A₀≤148; oddness sharpens this to A₀≤147.

For an actual original Boolean f, the gated code equivalence first translates its 256-point one-support by an arbitrary point outside it; this preserves every Walsh magnitude. Its nonzero codeword deviation t equals W_f(a)/4 up to the translation sign, at every nonzero frequency. Thus A₀ counts precisely the nonzero Walsh zeros, and W_f(0)=0 adds exactly one more. This uses the reviewed source's complete code direction, not mere formal scalar feasibility. Neither the translated support nor any frequency is selected or evaluated.

## Further exact triangular form, all indices

The same change z=1−u rewrites **all** 15 divisibility coefficients into the following nine simultaneous congruences for e=6,…,14; degrees e=0,…,5 are automatically divisible by 512. Let

    C_e=Σ_{r=0}^{e}(−1)^{e−r} binom(14−r,e−r) A_{r−7}
        + 1_{e≥7}(−1)^{e−7} binom(7,e−7)
        + 2^{e−6}(1_{e=12}−1_{e=13}).

Then every solution satisfies C_e≡0 (mod 2^{e−5}) for all e=6,…,14, and conversely these nine congruences recover all 15 coefficients of (2). To see this, the first two terms are the coefficient of u^e after factoring out 2^{14−e}; modulo 512 the last term of H(1−u) is 256(u^{12}−u^{13}) because (2−u)^6≡u^6 (mod 2). This is a purely symbolic equivalent lattice representation; it does not decide whether any nonnegative A exists, and all dual nonnegativity/realization qualifications in the pinned positivity result remain.

## Pinned inputs and limits

Before writing, the native pins were: `dual-enumerator-symbolic-v1.md` SHA-256 `7a05f4b954bacaf5ba865fa3559dd0ab5ff4f130f32383d60d9245ded0c92897`, 99 LF; `dual-enumerator-congruence-reduction-v1.md` SHA-256 `6817ccf924a52f42fe5d860b936f79b021e6dd095efbd1b10c5a8a2facb74dad`, 70 LF; `dual-enumerator-central-positivity-v1.md` SHA-256 `b03f9280f64d50b4325e59fdfb03d2d1f8bb6914e24db7e4bfa0b2fed5d48066`, 91 LF; and `walsh-projective-code-equivalence-v1.md` SHA-256 `b68e9f6bc546872e96066625ebfb7872f92f7a78d0187e9fa1925045148dbfeb`, 50 LF. W81 reconstructed the latter at its exact written scope but did not certify method noninfluence; no subsequent author result is adopted by that fact.

No sector/half-split/canonical transform, truth-degree/ANF, Gate-I, post052/post054 route, L1, held source or consumer was used. Both owner PROCESS MAJORs, parent L1 quarantine, all prior STOP/HOLD/ZERO/NONINPUT, N4 UNKNOWN and aux214 STOP remain. No clean-cognition, independent-model, external-human, formal/kernel, executable or novelty claim is made; the original witness-or-unrestricted-exclusion, all ranks/weights and `(24,24,2)` remain open.
