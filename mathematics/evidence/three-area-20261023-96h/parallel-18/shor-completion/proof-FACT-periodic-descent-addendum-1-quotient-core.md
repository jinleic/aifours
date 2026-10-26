# Addendum 1 to FACT descent — the quotient-primitive core

Actual preceding `/bin/date`: `Sun Oct 25 13:51:00 PDT 2026`. Additive to `proof-FACT-periodic-descent-v1.md`, SHA-256 `187c674ded82831bcec0ba9e15bfaab29d4dd83721188e001fffcf6753682b8e`. WRITTEN candidate; no computation or new GO. This does not solve FACT or any raw completion.

## 1. All proper quotient projections, not only periods

Let (A,B) satisfy FACT in Z_n. For each divisor m of n, let pi_m be reduction modulo m, and write

    A_m = pi_m(A), B_m = pi_m(B),
    a_m(u) = #{a in A : pi_m(a)=u},
    b_m(v) = #{b in B : pi_m(b)=v}.

These are SUPPORT sets and positive integer fiber counts, respectively. They must not be interchanged.

Projection of A+B=Z_n gives

    A_m+B_m=Z_m as a COVER,
    a_m*b_m = n/m pointwise on Z_m.

The second identity counts the n/m possible lifts of each quotient element and uses uniqueness in the original factorization.

It follows that |A_m||B_m| >= m. Equality holds exactly when the SUPPORT sum A_m+B_m is direct.

**Quotient-descent theorem.** If 1<m<n and |A_m||B_m|=m, then (A_m,B_m) is a smaller FACT solution. Their projected seed residues are initially allowed to coincide; the bootstrap lemma in the main proof §2 forces m>=1320 and proves all named seed residues distinct. Thus the exact endpoint condition, with its unknown added elements, descends.

Repeatedly descend whenever a proper quotient has equality. The modulus strictly decreases, so one reaches a FACT pair for which

    |A_m||B_m| > m  for EVERY proper divisor 1<m<n.    (QP)

Equivalently, for each such m there is a genuine collision among DIFFERENT quotient SUPPORT pairs. This collision is not an ambiguity in A+B at modulus n: different kernel lifts distinguish it.

In particular every least-modulus FACT pair satisfies QP. The original question has a FACT solution iff it has a QP solution: one direction is inclusion, the other is this finite descent. No existence of either side is asserted.

## 2. The exact fiber structure at a direct quotient

Suppose A_m+B_m is direct, and let k=n/m. If u in A_m and v in B_m, their quotient sum u+v has exactly ONE support representation. Therefore the weighted convolution identity gives

    a_m(u) b_m(v) = k for EVERY pair (u,v).

Fix v and then u. There exist positive INTEGERS r,s with

    a_m(u)=r for all u in A_m,
    b_m(v)=s for all v in B_m,
    r*s=k.

This uniformity was not an assumption. After choosing one lift of each u/v, the actual kernel fibers of sizes r,s tile the cyclic kernel H=ker(pi_m) for EVERY u/v combination (with a possible carry translation of H, which does not affect its full coverage). Thus a direct quotient corresponds to a rectangular family of coupled kernel factorizations, not merely to a scalar count inequality.

When k is a PRIME p, r*s=p forces r=p,s=1 or r=1,s=p. In the first case every occupied A fiber is the ENTIRE kernel coset, so A+H=A; in the second B+H=B. Conversely such a period produces a direct quotient by the main proof. Hence, for each prime p|n, projection modulo n/p is direct IF AND ONLY IF at least one factor has the order-p kernel as a period.

For composite k, no global period is asserted: both r and s can exceed1 and kernel fibers can vary. QP therefore records the full support-projection obstruction and should not be replaced by an unproved claim that every direct quotient comes from one period.

## 3. Concrete unknown-factor implications

- Both factors of a QP pair are aperiodic, by §2 and the main proof.
- For EVERY prime power p^j properly dividing n,

      |A mod p^j| * |B mod p^j| >= p^j+1.

  These are support counts of the ENTIRE unknown factors. The fixed seeds alone do not establish them.
- A triangular fiber construction whose first-coordinate projected supports tile a proper cyclic quotient cannot be the least FACT witness: it descends to a smaller literal FACT pair. This is stronger than checking a single fixed-order or CRT-product example.
- Conversely, multiplier-based section quotients of the form A+(B intersect a residue class, divided by p) are NOT these support projections. They need not retain B's0/1 seed. For instance division of the B0 residue1 fiber modulo3 gives the forced set{0,2,4}, not{0,1,7,13,14}. They cannot be silently treated as a FACT descent.

## 4. Exact new first step for a sufficient negative route

A uniform theorem that EVERY FACT pair admits SOME proper direct support quotient would contradict QP by descent and prove not-FACT at all orders. That statement remains UNPROVED; neither periodicity of an arbitrary factorization nor a source-reported classification is being assumed.

A positive endpoint search must instead provide a QP pair with all seed inclusions, or a larger pair whose descent gives one. Even a successful QP/FACT witness still leaves the actual all16-word cbc/delay/PR/STAB realization gap. This addendum supplies no raw finite code, no termination argument and no all-order noncompletion proof.
