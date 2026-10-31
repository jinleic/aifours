# Weyl-triple vectors give maximal 1-RQLSs in every dimension 2p

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at finite CRT checks: **Wed Oct 28 19:26:36 PDT 2026**. This is a conditional construction/reduction for every odd prime p; it generalizes the dimension10 derivation `frontier-20261028-weyl-mub-qls-equivalence-v1.md` SHA **f063984a0ac5ff0a51e064b8e32eb901ba2e7edaff6e2667e0f6c7f47ad43a5d**. It does NOT exhibit a vector, assert a fourth MUB exists, or classify all 1-RQLSs.

## 1. Conditional theorem

Let p be an odd prime, n=2p, k∈Z_n^*, `zeta=exp(2*pi*i/n)`, `xi=exp(pi*i/n)`, `Z|t>=zeta^t|t>`, `X|t>=|t+1 mod n>`, `D_k|t>=xi^(k t²)|t>`, and F_n the normalized Fourier matrix. The three bases I,F_n,D_k F_n are mutually unbiased.

For a unit vector phi, the following are equivalent:

1. phi is unbiased to these three bases;
2. the actual vectors `psi_(r,c)=Z^r X^c phi` have n ONB rows, n ONB columns, and the transversal `(r,c)=(k c,c)` is an ONB.

Whenever they hold, **all n² Weyl-orbit rays are distinct**, and translating r gives a full 1-resolution. The n vectors `{X^c phi}` also form an entire fourth MUB for the fixed triple. Conversely this equivalence is only for this Weyl-orbit, specified-slope construction.

## 2. MUB and ONB equivalence

Since n is even, `xi^(k(t+n)²)=xi^(k t²)`. Furthermore

`D_k X D_k† = xi^(-k) Z^k X`.

The chirp autocorrelation is `xi^(k h²) sum_t zeta^(k h t)=0` for 0<h<n because k is invertible. Therefore its Fourier transform has constant modulus sqrt(n), making F_n and D_k F_n mutually unbiased; each is flat against I.

As in the dimension10 packet, an orbit under a unitary with n distinct equally spaced eigenvalues is an ONB iff phi has uniform probabilities in its eigenbasis. Apply this to Z, X, Z^k X; the vector `Z^(k c)X^c phi` differs from `(Z^k X)^c phi` by a phase. Since k is invertible, the diagonal r=k c meets all rows and columns once, and its Z shifts partition all n² cells. The cyclic shift X permutes the three Weyl eigenbases up to phases, so its n translates of phi form a fourth MUB.

## 3. All orbit rays are automatically distinct

If two rays coincide, phi is an eigenvector of nontrivial `Z^m X^s`. If m or s is odd, its p-th power is, up to phase, one of `Z^p`, `X^p`, `Z^p X^p`. Since k is odd, the last is a phase times `(Z^k X)^p`. Uniformity in the three eigenbases forces the relevant nontrivial p-th moment to be0, contradicting an eigenvector expectation of modulus1.

If m,s are both even and not both0 mod2p, CRT splits the displacement as `I2 tensor W_p`, with nontrivial p-dimensional Weyl W_p. It has simple spectrum: a nonzero shift is one p-cycle and a nonzero pure modulation has p distinct diagonal entries. Hence phi is a product across `C2 tensor Cp`. The three fixed bases factor into qubit Z, X and ±Y bases times p-dimensional bases, so the qubit factor would be unbiased to all three Pauli bases, impossible for a pure qubit. Thus no nontrivial Weyl stabilizer exists, proving distinctness.

For the CRT details, put `r=(p+1)/2` and `t=p a+2r b mod2p`. Up to relabeling,

`F_(2p)=F2 tensor Fp^(2r²)`,
`D_k=diag(1,i^(k p)) tensor diag(omega_p^(k r² b²))`,

where the exponent on Fp means entry `(b,d)` is `omega_p^(2r² b d)/sqrt(p)`. Thus the qubit chirp exponent kp is odd. Exact `frontier-20261028-two-prime-weyl-crt-check-v1.py` SHA **553dc4d507f37442cc12497cd0e03a91fa921e87334190ec04c72bdf94d8686d** checks these exponent identities and all Weyl parity labels for p=3,5,7,11,13; the all-prime reasoning above is written mathematics, not inferred from the five cases.

## 4. Limits

For p=3 the earlier odd-cycle lemma excludes a common vector for the corresponding product triple. For p=5 the all-root-relative-phase obstruction is recorded in `frontier-20261028-mub-unit-slopes-allroot-v1.md`; arbitrary irrational relative phases remain open. For other p no existence or nonexistence conclusion is claimed. The construction is potentially stronger than the original task, since a successful vector would simultaneously provide four MUBs and a maximal 1-RQLS in dimension2p. No general converse or novelty clearance is asserted.
