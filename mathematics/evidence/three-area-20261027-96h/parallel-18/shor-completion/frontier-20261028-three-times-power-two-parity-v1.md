# Shor completion: all-order parity structure for a `3*2^a` head border

Owner **MathShor-2**, math-5. Native clock of the exact coefficient controls: **Wed Oct 28 21:22:43 PDT 2026**.
**ALL-ORDER WRITTEN necessary condition with an explicitly named classical import; no general completion/noncompletion, formal/peer/cross-family acceptance or novelty claim.**

## 1. The theorem

Let `P+Q` be a direct tiling of `Z_n`, with old heads `0,3 in P`, `v_3(n)=1`, and

    |P|=3*2^a,     a>=1.

Then `Phi_2` divides the P-mask, and in EACH residue class modulo3 P has equally many even and odd elements. For the literal Shor problem, this is a necessary condition on the SAME actual multi-b border factorization. In particular it applies to the two still-open even-Q branches `|P|=12` and24 at n2640. It is a structural condition, not an exclusion of either branch or any whole order.

## 2. Explicit classical import

We use the **Coven–Meyerowitz (T2) theorem for finite tiles whose cardinality has at most two DISTINCT prime factors**, as explicitly stated in [Łaba–Londner, Theorem1.1](https://arxiv.org/html/2106.14044v3). It applies because P tiles the integers with periodic complement `Q+nZ` and `|P|=3*2^a`. This is a named prior theorem, not a new proof or novelty claim.

Since `v_3(n)=1` and 3 divides |P| but not |Q|, the direct tiling identity puts `Phi_3` in P. Hence P is uniform modulo3, with exactly `2^a` elements per class.

Let `v_2(n)=k`. For each `j=1,...,k`, the tiling identity puts `Phi_(2^j)` in P or Q. Their evaluations at1 and `v_2(P(1)Q(1))=k` show that exactly a of these factors lie in P, the others in Q, and none is shared. Let I be P's set of a indices.

## 3. Why `Phi_2` belongs to P

Suppose instead `1 not in I`. By T2, for every `s in I`, `Phi_(3*2^s)` also divides P. The elementary identity

    Phi_(2^s)(X) Phi_(3*2^s)(X) = 1+X^(3*2^(s-1))            (1)

shows that P is divisible by

    R(X^3),   R(Y)=product_(s in I) (1+Y^(2^(s-1))).

All factors are distinct and monic, so the product divides the integer mask polynomial. Decompose that polynomial uniquely as

    P(X)=P_0(X^3)+X P_1(X^3)+X^2 P_2(X^3).

Division in the free `Z[X^3]`-module with basis `1,X,X^2` shows R divides EACH `P_j(Y)` in `Z[Y]`. Because every s in I is at least2, R is a polynomial in `Y^2` and `R(1)=2^a`. Therefore the sums of even-index and odd-index coefficients of `P_0(Y)` are each multiples of `2^a`.

But P's mod3-class0 has exactly `2^a` elements and contains the distinct old heads0 and3, which correspond to the even and odd Y-exponents0 and1. Both sums are positive, so they cannot each be multiples of `2^a` and total only `2^a`. Contradiction. Hence `1 in I` and `Phi_2` divides P.

## 4. Balanced parity within each mod3 class

T2 now also puts `Phi_6` in P. Their product is `1+X^3`. The same mod3 polynomial decomposition shows that EACH `P_j(Y)` is divisible by `1+Y`. Evaluating at Y=-1 gives equal sums of its even- and odd-index coefficients. Since each actual head in residue j has exponent `3v+j`, this is equivalent to equal numbers of even and odd heads within every mod3 class (the parity labels swap when j=1, but equality is unchanged).

## 5. Checks and boundary

`frontier-20261028-three-times-power-two-check.py`, SHA256 `31c717ad1d93d77a41f171b4a5f75553ee3636ce69b10310e864771a7ca1853c` (25 LF, 1007 bytes), checks25 finite choices of owned indices, exact coefficient cancellations in (1), and the value/parity of R. These are finite controls only; §§2–4 are the written all-order argument and do not independently prove the imported T2 theorem.

The theorem does not assert that any named border tiling or completion exists, and it does not settle the original unrestricted finite UD factor-completion problem. No peer, human, formal, independent-family or novelty gate is claimed.

**END OF THREE-TIMES-POWER-TWO PARITY STRUCTURE.**
