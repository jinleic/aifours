# Shor completion: a unified all-order even-tail fibre theorem

Owner **MathShor-2**, math-5. Native clock of exact synthetic controls: **Wed Oct 28 21:39:32 PDT 2026**.
**ALL-ORDER WRITTEN necessary structure with an explicitly named classical import; no unrestricted noncompletion, formal/peer/cross-family acceptance or novelty claim.**

## 1. The complete odd-part split

Let `k>=2`, `1<=a<k`, `b=k-a`, and `n=165*2^k`. Suppose P,Q are the SAME actual direct b-run border factors of a finite UD factor-complete extension of the literal Shor code, with BOTH cardinalities even. Write

    |P|=d*2^a,   |Q|=e*2^b,   d*e=165,   d,e odd.

Since165 is squarefree, `d` ranges over `{1,3,5,11,15,33,55,165}` and `e=165/d`; in particular gcd(d,e)=1. The old anchors are `A={0,3,8,11} subset P` and `Y={0,1,7,13,14} subset Q`.

For each `0<=i<d` and `0<=j<e`, form normalized exponent multisets modulo `m=2^k` from actual representatives in `[0,n)`:

    P_i={ (p-i)/d mod m : p in P, p==i mod d },
    Q_j={ (q-j)/e mod m : q in Q, q==j mod e }.

Then **all `d*e=165` pairs `P_i,Q_j` are direct SET factorizations of Z_m**, with cardinalities `2^a,2^b`. Thus neither folded multiset has repeated residues. This is an all-k SAME-D statement; it does not construct any completion.

## 2. Named import and proof

The actual-word border theorem and necessary Sands gcd-difference criterion are classical and independently reconstructed in prior packets. We explicitly import [Łaba–Londner, Corollary6.2](https://arxiv.org/html/2106.14042v1): in a cyclic tiling where at most two primes divide BOTH tile cardinalities, both tiles satisfy Coven–Meyerowitz T2. The only common prime of `d*2^a` and `e*2^b` is2.

Each odd prime dividing d belongs to P, and each dividing e belongs to Q, by prime-root vanishing and cardinalities. T2 gives all composite odd cyclotomic factors as well. Therefore the products `(X^d-1)/(X-1)` and `(X^e-1)/(X-1)` divide the respective masks, yielding uniformity mod d/e and actual fibre counts `2^a,2^b`. The product is1 when d=1 or e=1.

The two-power prime factors of P,Q partition s=1,...,k by evaluation at1. For each s owned by P, T2 with ALL subsets of the odd primes in d gives

    Phi_(2^s)(X^d) = product_(h|d) Phi_(2^s*h)(X)  divides P(X).

The analogous identity holds for Q with e. Decomposing each mask in its free module over `Z[X^d]` or `Z[X^e]` shows the owned `Phi_(2^s)` divides every normalized fibre polynomial. The two sides' fibre spectra vanish at every nontrivial m-th root, and their values at1 multiply to m. Fourier inversion gives convolution1 for EVERY pair. Nonnegative integer coefficients then force both folded fibres to be 0/1 sets, proving the theorem.

## 3. Old-anchor parity consequences and exact limits

If `d in {1,3,5,11}`, two actual old heads share a mod-d fibre and their normalized difference is odd: use `(0,3)` for d=1 or3, `(3,8)` for d=5, and `(0,11)` for d=11. Sands applied to each associated two-power fibre tiling forces EVERY Q_j into one parity class. Here `e>=15`, so every old tail j is its own representative in `[0,e)`, and its actual fibre contains normalized0. Therefore

    q==j mod (2e)  whenever q in Q, q==j mod e, j in Y.        (2)

The cases d=3,5,11 and sharper old-head gcd congruences are the three separately pinned fibre packets. Equation(2) adds the d=1 case: when `|P|=2^a`, every Q-tail in an old mod165 fibre obeys `q==j mod330`.

At the reciprocal endpoint `d=165,e=1`, old tails0 and1 lie in the SAME Q_0 fibre with normalized odd difference. Sands instead forces every P_i into one parity class. Each old head i in A supplies normalized0 in its mod165 fibre, so

    p==i mod330  whenever p in P, p==i mod165, i in A.         (3)

For d=15,33,55, the fibre tiling theorem still holds, but this packet does NOT claim any old-anchor parity pin. It does not exclude any cardinality branch or assert a complete code.

## 4. Exact controls and original gap

`frontier-20261028-even-tail-unified-fibre-check.py`, SHA256 `bd744cd4ab54dea615c1d4d78cf2bd54d80148a58f97b294a8f0aae1a6880ff9` (20 LF, 1096 bytes), checks all165 fibre-pair tilings for each of the eight divisor splits at a synthetic n2640 tiling. It also checks a separate reciprocal endpoint control with Q containing0,1. None is a Shor completion. These finite checks do not prove the imported classical corollary or replace the all-order written reasoning.

The original unrestricted finite UD factor-completion problem remains OPEN. No peer, human, formal, independent-family or novelty acceptance is claimed.

**END OF UNIFIED EVEN-TAIL FIBRE THEOREM.**
