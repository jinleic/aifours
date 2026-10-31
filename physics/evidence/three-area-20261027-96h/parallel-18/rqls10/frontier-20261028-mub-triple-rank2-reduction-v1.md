# A five-dimensional rank-two formulation of the Weyl-orbit target

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` before writing: **Wed Oct 28 18:52:09 PDT 2026**. This is a further EXACT reformulation of the restricted Weyl-orbit construction in `frontier-20261028-weyl-mub-qls-equivalence-v1.md` SHA **f063984a0ac5ff0a51e064b8e32eb901ba2e7edaff6e2667e0f6c7f47ad43a5d**. It does not prove a 1-RQLS exists or does not exist.

## 1. Maximal entanglement is forced

Use the CRT identification `C10=C2 tensor C5` from that packet. The three fixed mutually unbiased bases `I10,F10,D10 F10` factor respectively into the qubit Z, X and Y bases and the 5-dimensional bases

`I5`, `U_(t,b)=omega^(3tb)/sqrt(5)`, `V=D5 U`,
`D5=diag(omega^(4t²))`, `omega=exp(2*pi*i/5)`.

If a unit vector phi is unbiased to all three PRODUCT bases, summing the equal joint probabilities over the5 outcomes on the second factor shows its reduced qubit state has equal outcome probabilities in the Z, X and Y bases. Its three Bloch components all vanish; hence the reduced state is exactly `I2/2`. Thus every putative vector is MAXIMALLY ENTANGLED across `2×5`, with entropy one bit and Schmidt coefficients `1/sqrt(2),1/sqrt(2)`.

Write it uniquely relative to the qubit Z basis as

`phi=(|0> tensor a + |1> tensor b)/sqrt(2)`,
`||a||=||b||=1`, `<a,b>=0`.                                  (1)

Unbiasedness to `I2 tensor I5` is exactly `|a_t|²=|b_t|²=1/5` for every t.

## 2. Necessary AND sufficient 5D equations

Set `u=U†a`, `v=U†b`, `u'=V†a`, `v'=V†b`. Then phi is unbiased to the entire fixed triple **if and only if**, for every t∈F5,

```text
|a_t|² = |b_t|² = 1/5,          <a,b>=0,
|u_t|² + |v_t|² = 2/5,          Re(conjugate(u_t) v_t)=0,
|u'_t|² + |v'_t|² = 2/5,        Im(conjugate(u'_t) v'_t)=0.
```

The X-basis amplitudes are `(u_t±v_t)/2`, and the Y-basis amplitudes are `(u'_t∓i v'_t)/2`; expanding their squared magnitudes gives precisely these real equations. Conversely these equations give each of the30 joint probabilities 1/10. Any exact solution a,b directly yields a phi and hence, by the previous packet's written stabilizer proof, 100 distinct rays and the full cyclic resolution.

Equivalently let `P=|a><a|+|b><b|` and `S=|a><b|`. P is an orthogonal rank-two projection whose diagonal is `2/5` in ALL of I5,U,V. Additionally, the Z-basis diagonals of `|a><a|-|b><b|` vanish, the U-basis diagonal of `S+S†` vanishes, and the V-basis diagonal of `i(S-S†)` vanishes. These cross-phase gates are essential; flatness of P alone is not enough.

## 3. Explicit flat rank-two projector that FAILS the needed cross gate

Take `W=D5² U`, and let a,b be its columns0,1. Then a,b are orthonormal and separately unbiased to I5,U,V. Consequently P has diagonal `2/5` in all three bases: the tempting simpler claim “no such flat rank-two projector exists” is FALSE.

For completeness, entries of `U†D5^s U` for s=1,2 are quadratic Gauss sums over F5. For nonzero quadratic coefficient q,

`|sum_t omega^(q t²+ell t)|²
 = sum_h omega^(q h²+ell h) sum_v omega^(2 q h v) = 5`.

So those matrices are flat. In the U basis, completing the square shows the ratio `v_t/u_t` is a fifth root of unity (with u_t,v_t nonzero). It cannot be ±i, hence `Re(conjugate(u_t)v_t)!=0` for every t: this explicit P fails the X cross gate and does NOT furnish phi or a QLS witness.

Independent exact integer check `frontier-20261028-rank2-mub-counterexample-check-v1.py`, SHA **ed7f1d5b0ff3feb36f1c1aed7b14a7d2232c800dcf54cab1ad6043465da42c1f**, reduces all relevant F5 Gauss sums modulo `Phi5=1+x+x²+x³+x⁴`, checks squared modulus5, orthogonality, and finds U-basis ratio exponents `(3,2,1,0,4)`. It is a check of this ONE explicit feasible projector, not a classification of such projectors.

## 4. Remaining gap

Solve or prove inconsistent the entire coupled 5D system in §2. In particular, merely finding a rank-two projection with three constant diagonals is insufficient: the example in §3 supplies one. No uniqueness theorem for flat projections, general nonexistence result, or novelty claim is assumed. Even resolving this system would address only the specified Weyl/diagonal-transversal ansatz unless it produces the explicit target witness.
