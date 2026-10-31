# Uniform QLS(10): composite root-of-unity phase obstructions

**NEW WRITTEN AUTHOR CANDIDATE, unreviewed.** Native `/bin/date` immediately before writing: **Wed Oct 28 17:45:57 PDT 2026**. The results concern EVERY physical uniform-overlap lift and EVERY Latin resolution L, but only the stated finite root-of-unity phase alphabets after allowed gauges. Uniform overlap or finite alphabet is NOT asserted WLOG for the original QLS10 problem. No unrestricted no-go, novelty or independent-review claim follows.

## 1. Two independent general lemmas and QLS caller

A hypothetical physical uniform M_* lift at n=10 has, relative to any row ONB, exactly two zero coordinates and eight equal-modulus nonzero coordinates for each other cell. For two nonreference cells in the SAME column, their two zero sets share exactly the column coordinate and their other zeros differ; hence they have exactly7 common nonzero coordinates and must have inner product ZERO. For a nonsharing pair whose zero sets share exactly one coordinate (there are at least14 such partners for each nonreference cell), the same seven-coordinate sum must have squared modulus8 after removing its 1/8 normalization. The all-L incidence proof is given in `frontier-20261028-uniform-phase-obstructions-v1.md`, SHA **11ae022040c391e2d4151446a6a88e47ab5feefcb27e5d38815d85e54c4dd945**, and can also be read directly from the stated two-zero/Latin incidence: choose two distinct nonreference cells in one column for the ZERO case; for the nonsharing case use a different reference transversal as in its §4.

Assume all such nonzero coordinates, after arbitrary per-cell phases and a common coordinate-diagonal unitary, are powers of a single q-th root of unity. The cell phases factor out of any pairwise inner product and coordinate phases cancel. Each relevant seven-term sum is therefore a sum of seven q-th roots. We prove:

**Lemma A (two-prime zero-sum length).** If q=p^a r^b with distinct primes p,r and a,b>=1, every vanishing sum of q-th roots of unity has length in the nonnegative integer semigroup `p Z_>=0 + r Z_>=0`. Thus a length7 vanishing sum can occur ONLY if one prime is7, or `{p,r}={2,3}` or `{2,5}`.

**Lemma B (two-adic norm).** Let m>1 be odd and suppose `2^t ≡ -1 (mod m)` for some t>=1. For q=m OR q=2m, there is NO algebraic integer S in `Z[zeta_q]` satisfying `S*conjugate(S)=8`; in particular no sum of any number of q-th roots has squared modulus8.

**Consequences for uniform QLS10.** The SAME-column seven-term zero condition excludes every two-prime q for which7 is not in the semigroup in Lemma A. The nonsharing seven-term magnitude condition excludes every q in Lemma B. Therefore q=15, every `3^a 5^b` with a,b>=1, and all other two-prime alphabets outside the three explicitly excepted prime patterns are impossible. Also q=6,10,18,22,26,34,50 and all other q=m or2m satisfying Lemma B are impossible. Prime-power q were already excluded by `frontier-20261028-uniform-prime-power-phase-obstruction-v1.md`, SHA **2b9ac43797a5720e01746dda9f3343c3ea9227f7dcae36f2f1d7c9ddcd7c8467**. These are conditional phase restrictions, not an unrestricted exclusion.

## 2. Complete two-prime zero-sum proof

Let q=p^a r^b, p!=r. Put `h=p^(a−1)`, `k=r^(b−1)`. Every q-th root has a UNIQUE representation `alpha^u beta^v`, where alpha is primitive p^a-th and beta primitive r^b-th, `0<=u<p^a`, `0<=v<r^b`. Group terms by `u=u0+i h`, `v=v0+j k`, with `0<=u0<h`, `0<=v0<k`, `0<=i<p`, `0<=j<r`. Let N_ij be the nonnegative multiplicity matrix within one (u0,v0) group.

The products

`alpha^(u0+i h) beta^(v0+j k)` with `i<p−1`, `j<r−1`

and all u0,v0 form a Q-basis of Q(zeta_q): each factor is a power basis of its prime-power cyclotomic field, and the product contains `phi(p^a)phi(r^b)=phi(q)` elements spanning the compositum Q(zeta_q). This uses the standard cyclotomic degree/irreducibility theorem, explicitly named here; no numerical phase sample stands in for it.

Use `alpha^((p−1)h)=−sum_(i=0)^(p−2)alpha^(i h)` and the analogous r identity. If the total root sum is zero, basis independence says, within EVERY group,

`N_ij-N_(p−1,j)-N_(i,r−1)+N_(p−1,r−1)=0`

for all i<p−1,j<r−1. The same additive form trivially includes the last row/column. Choose i* minimizing N_(i,r−1), put `a_i=N_(i,r−1)-N_(i*,r−1)>=0` and `b_j=N_(i*,j)>=0`. The identity implies `N_ij=a_i+b_j` for all i,j. Consequently the group's number of terms is

`sum_ij N_ij = r sum_i a_i + p sum_j b_j`.

Summing over all u0,v0 gives the total length in `pN+rN`, proving Lemma A without an external classification or a selected q. For length7 and distinct primes, the only possibilities are a prime7, 2+5, or 2+2+3; all other two-prime patterns are excluded.

## 3. Complete two-adic norm proof

First q=m odd. Since `2^t ≡ -1 mod m`, complex conjugation on zeta_m reduces modulo2 to the t-th Frobenius map: `conjugate(zeta_m)=zeta_m^(-1)=zeta_m^(2^t)`. Thus for any S in Z[zeta_m], its residue s in

`R=F2[X]/(Phi_m(X))`

satisfies `conjugate(s)=s^(2^t)`.

R is REDUCED: Phi_m divides `X^m-1`, and m odd makes the latter squarefree over F2 because its derivative is `X^(m-1)` and has gcd1 with `X^m-1`. Thus R is a finite product of fields and has no nonzero nilpotents.

If `S conjugate(S)=8`, reduction modulo2 gives `s^(1+2^t)=0`, so s=0 in R. Because Phi_m is monic and the integral power basis has unique representatives, S is divisible by2 in Z[zeta_m]: write S=2T. The exact complex equality becomes `T conjugate(T)=2`. The same reduced-ring argument makes T divisible by2, T=2U; then `1=2U conjugate(U)`, whose reduction modulo2 is impossible. Thus no such S exists.

For q=2m with m odd, `zeta_(2m)=-zeta_m^((m+1)/2)`, and conversely zeta_m=zeta_(2m)^2, so `Z[zeta_(2m)]=Z[zeta_m]`; the same proof applies. This proves Lemma B for ANY odd m with the stated modular condition, not merely a finite list and not merely sums of seven roots. It also rules out any integer squared modulus with odd 2-adic valuation by the same repeated divisibility argument, but only the value8 is used in the QLS caller.

Examples, checked by exact modular exponentiation: m=3,5,9,11,13,17,25 admit such t; m=7 and15 do not. Therefore q=2m gives6,10,18,22,26,34,50 among the excluded composite/prime-power cases. This list is illustrative, not an assertion that the condition holds for all odd m.

## 4. Direct examples and exact bounded experiments

The exact cyclotomic arithmetic checker `frontier-20261028-composite-phase-check-v1.py`, SHA **a069a45bb790692676492ba275d3a9777f6d7a15657ce6114afa4303920c8993**, result JSON SHA **c1f97e47da5eef995abf5d15990fe921eceaf6738c28c83ded50e759ac996d85**, independently checked the following finite facts:

```text
Phi5 mod2 has no monic degree1/2 factor: irreducible degree4 PASS
q6 norm a²+ab+b² residues mod3 exactly {0,1}; 8 impossible PASS
q 6 zero-sum seven-root multisets 12
q 10 zero-sum seven-root multisets 10
q 12 zero-sum seven-root multisets 84
q 15 zero-sum seven-root multisets 0
q12 separate zero-sum and squared-magnitude-8 seven-term examples PASS
```

For q=6, `S=a+b zeta_6` has norm `a²+ab+b² ≡(a−b)² mod3`, which cannot equal8. For q=10, `Z[zeta_10]=Z[zeta_5]`, and Phi5 is irreducible mod2; this is the m=5 instance of §3. For q=15, §2 gives length in3N+5N, which cannot equal7; the finite exhaustive result corroborates, not proves, the universal prime-power-exponent generalization.

At q=12 the individual zero and magnitude conditions do have exact seven-term examples, e.g.

`3·1 + zeta_3 + zeta_3² + 2·(-1)=0`,

`1+1+i+i+(1+zeta_3+zeta_3²)=2+2i`, whose squared modulus is8.

These are DIFFERENT single-pair examples and need not be globally compatible. An exact Z3 model for a single dephased order-9 q12 conference matrix, `frontier-20261028-conference9-q12-smt-v1.py` SHA **ec715e89f846e799444751e0671b08016c93a79985e3289a2b233f82fb42b415**, returned **unknown (timeout)** after25.025s; result SHA **ab8854e4340af9668a9d81d6213c60a8533bd9e71791f18698cb40dffb6e9926**. UNKNOWN is neither feasibility nor impossibility, and a conference block would still not be a complete QLS.

## 5. Residual and verification boundary

The open finite-phase classes include alphabets with factors2 and3 with higher 2-power such as12, factors2 and5 not covered by Lemma B, and two-prime alphabets containing7 when the two-adic norm condition fails; q with three or more distinct primes also remains. Nothing establishes that a solution must use any root-of-unity alphabet. More importantly, nonuniform original QLS10 arrays remain entirely outside these M_* branch exclusions.

All actual statements above are written proofs, with named cyclotomic facts, exact program checks at their stated finite scope, and explicitly unverified historical novelty. Independent full review is needed before adoption. No original100-ray witness, unconditional all-L obstruction, external-model review, formal proof, publication or infrastructure action is claimed.

**END — composite finite-phase obstructions; unrestricted QLS10 remains open.**
