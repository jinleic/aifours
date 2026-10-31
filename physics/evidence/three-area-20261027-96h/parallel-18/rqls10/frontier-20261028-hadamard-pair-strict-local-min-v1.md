# Exact nonzero strict local minimum for the Fourier-product Hadamard-pair loss

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at completed certificate: **Wed Oct 28 18:44:18 PDT 2026**. This explains a numerical-search trap inside the Fourier-product ansatz; it does NOT prove a global lower bound or prevent a target 1-RQLS by another point/ansatz.

## 1. Exact claim and checkpointed object

For the two-Hadamard physical caller in `frontier-20261028-hadamard-pair-caller-and-near-family-v1.md` SHA **e67862876e8e876edbe7d55400bed94b3ba901cbee965cb0ffe7864d8081543c**, write

`H_(t,c)=exp(i theta_(t,c))/sqrt(10)`, `J=H∘F10`,
`C(theta)=||H†H-I||_F²+||J†J-I||_F²`.

Fix the 19 continuous row/column gauge phases by `theta_(0,c)=theta_(t,0)=0`; there are81 free real phase coordinates. Let E be the EXACT 10×10 exponent table in `frontier-20261028-near-hadamard-pair-exact-v1.py` SHA **be0a9fe04893282e8491e2804a7e40bfc354ed324fe5e33530216095c68dcdd3**, and set `theta*_(t,c)=pi*E_(t,c)/10`.

**Claim:** theta* is a STRICT LOCAL MINIMUM of C on this full 81-dimensional dephased flat-phase torus, not just on the earlier one-phase interpolation. Its exact value is `10*(1-cos(pi/10))>0`. Its actual Fourier-product cells have100 distinct rays but H and J each have five nonorthogonal unordered column pairs; it is NOT a QLS or a target witness. Continuous row/column gauge transforms give the corresponding gauge orbit of local minima in the undephased parameter space.

## 2. Differentiation and exact stationarity

For c<d and t<s, put

`v = e_(t,d)-e_(t,c)-e_(s,d)+e_(s,c)`

restricted to the81 free coordinates. For shift a=0,1 the phase of the Gram square term is

`alpha_a = theta_(t,d)-theta_(t,c)-theta_(s,d)+theta_(s,c)
          + (2*pi/10)*a*(t-s)*(d-c)`.

After accounting for both column orders and both coordinate orders, t=s terms contribute no derivatives, and the exact gradient and Hessian are

`grad C = -(4/100) sum_(c<d,t<s,a) sin(alpha_a)*v`,
`Hess C = -(4/100) sum_(c<d,t<s,a) cos(alpha_a)*v v^T`.       (1)

At theta*, each alpha is an integer multiple of pi/10. For each of81 gradient coordinates, the checker forms the integer polynomial representing the corresponding sum of `(zeta20^k-zeta20^-k)` and verifies its exact remainder is zero modulo `Phi20(x)=x^8-x^6+x^4-x²+1`. Hence **every free gradient entry is exactly zero**; this is not a finite-difference stationarity test.

## 3. Rigorous rational positive-definiteness certificate

`frontier-20261028-near-pair-hessian-cert-v1.py`, SHA **d4f2aa1fec0892a5a424a7222147d6a1e6f103515915cf025cc6acd2caf5f462**, imports the exact E table and implements (1). The observed complete output is

```text
PASS rigorous cos brackets via Machin arctan fractions and alternating Taylor
PASS 81 exact gradient polynomials vanish modulo Phi20
PASS 81 positive Bareiss pivots for Happrox - (1/200)I
entrywise Hessian error <=180/10^12; operator error <=14580/10^12
STRICT LOCAL MINIMUM of full dephased flat-matrix loss; NO GLOBAL CLAIM
```

The certificate uses exact Python integers and `fractions.Fraction` only for proof steps:

1. By the elementary Machin identity `pi=16 atan(1/5)-4 atan(1/239)`, alternating rational arctan series bracket pi. Rational cosine Taylor series with a rigorous remainder and the 1-Lipschitz bound give intervals for every `cos(k*pi/10)`; each interval lies wholly inside ONE rounding bin at denominator 10^12.
2. Formula (1) gives an integer symmetric matrix M and `D=100*10^12`, so `Happrox=M/D` is the Hessian assembled with those rounded cosines.
3. The 81 leading-principal-minor signs of `M-(D/200)I` are checked positive by exact fraction-free Bareiss elimination, including exact divisibility of every division. Thus `Happrox-(1/200)I` is positive definite by Sylvester's criterion.
4. There are at most18000 ordered cosine summands before the 1/100 factor, and each coordinate coefficient in v is 0 or ±1. Each Hessian entry has absolute rounding error at most `180/10^12`; its operator norm is bounded by the 81-row sum, `14580/10^12 < 1/200`. Therefore the TRUE exact Hessian is positive definite.

The smooth second-derivative test now establishes a strict local minimum. Separately, an untrusted-for-proof floating finite-difference Hessian independently agreed with a direct floating analytic assembly to about 4.3e-11 maximum entry error; this checks transcription only. The certificate is an executable arithmetic argument, not formal kernel verification or peer review.

## 4. Limits

The exact nonzero minimum is LOCAL around one gauge class. There may be other minima or a genuine zero elsewhere; the 24 numerical restarts do not exclude them. Even a global positive lower bound on this loss would concern only the chosen Fourier-product ansatz, not every 1-resolvable quantum Latin square. Full independent mathematical and script review is requested before adoption.
