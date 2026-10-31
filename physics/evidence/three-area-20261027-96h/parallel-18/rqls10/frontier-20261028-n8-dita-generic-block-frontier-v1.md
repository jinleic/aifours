# Order-eight two-block Fourier products: arbitrary H4 block frontier

**PARTIAL COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 21:48:54 PDT 2026**. This extends the all-delta F4/F4 family `frontier-20261028-n8-dita-allphase-no-transversal-v1.md` SHA **c229312414dcd582bb607608f43c19c97c8d1550aefa3a7381d7cb47726b8402** toward TWO arbitrary four-dimensional Hadamard blocks. It is explicitly NOT a no-go for the larger family: **30720 normalized both-free branches remain**.

## 1. Generalized family

Write

`H(z)=[[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]]`, `|z|=1`.

Let `K_((a,t),(0,b))=H(alpha)_(t,b)` and `K_((a,t),(1,b))=(-1)^a delta_t H(beta)_(mu(t),b)`, where alpha,beta,delta_t are arbitrary unit complex numbers, mu∈S4, and the eight source rows have arbitrary physical ordering. An unconditional statement here concerns this explicit family. A separate extension to ALL two-block Diţă Hadamards would import and independently review the order-four complex-Hadamard classification and its precise dephased/gauge caller; this is NOT assumed established here.

The same normalization as the F4/F4 packet sets source order O[0]=0, h0 row assignment R0[0]=0, mu(0)=0 and delta_0=1. For the mu normalization, dephase its t=0 B row by column gauges, absorb row phases into delta, and allow permutations of the other B rows/columns; the standard dephased H4 family is stable under this renormalization. This is a review obligation, not a reason to ignore unreduced orderings.

## 2. Exact same-group phase reduction

Each within-h0 transversal Gram equation is `A+B*alpha=0` or `A+B*alpha^(-1)=0`, where A,B are in Z[zeta8]. A unit alpha is therefore either completely free (all such equations vanish identically) or is uniquely fixed. Exact 4-component field arithmetic in `frontier-20261028-n8-dita-generic-block-h0-v1.py` SHA **374e04f33737276dfbe9e2a32abb9d8c714ef0cb8b49a275af19414b355a52ee**, result SHA **4b8120fe38182f73dca30029bd83705366087c750f19b3f788c8152a4d7a454d**, checks all5040 normalized row orders ×210 h0 assignments: among14592 feasible assignments, **1280 have free alpha and every constrained alpha is an eighth root**. It checks exact phase consistency and `|A|²=|B|²`; no sampled-alpha extrapolation is used.

The identical result applies to h1/beta after source t-relabelling by mu and subtracting its first assigned physical row: both preserve the same-group equations. Complete normalized extension `frontier-20261028-n8-dita-generic-rank-v2.cpp` SHA **dd1b99b8e9cdf8c560b9996a9c8ea81727845cc164263d33638599c83aabcbee**, result SHA **67974450b2315937544122a79561dfe192b170cb090005e0ac2bd5e9338d343a**, has **651264** branches with both within-group systems feasible:

```text
alpha,beta both fixed eighth roots 421888
one free, one fixed               172032
both free                           57344
```

## 3. Cross equations: reductions and remaining branch

For fixed/fixed branches, the 16×4 cross-coefficient matrix over Z[zeta8] is checked modulo65521. The full-rank/minor norm method of the preceding packet rejects all421888. For one-free/one-fixed branches, use only cross rows independent of the free parameter; this rejects131072 by modular rank4. On the remaining40960, `frontier-20261028-n8-dita-freeblock-gate-v1.py` SHA **c5da59980b97a97f65c38ef43e23a38c8d472bf005b367df84cd3c14f2bec621**, result SHA **3327c1f32d1b55e89d5ca616f7894815fa7ee1af8adefc82c19893dbc9ef1523**, rejects32768 by incompatible linear equations in the free phase, leaving8192 rank-two gates.

For those8192, every 4×4 cross minor is a polynomial of degree at most2 in x=alpha^(-1) or beta, because x occurs in only two columns. `frontier-20261028-n8-dita-rank2-root-gate-v1.py` SHA **e939089f340e4813d4277f8202a8304b432da8446fd6b887aecc128fe3937cf1**, result SHA **7a7f0ac62b2d6c75b4e33af1aee28a616f1be0d37bad4bc0688531c745addd90**, supplies ONE exact Z[zeta8] minor per branch whose roots are only0 or eighth roots; all8192 have a gate. Since a unit phase is nonzero and all fixed/fixed branches are rejected, these one-free branches are excluded. The explicit minor-row/root factors are retained in SHA **87a7e7701c748e1b7feaa76a000a9a0747bd1988f8c57cea797b6fb9f648321d**. Mod-p is used only to locate candidate minors; their factorization is exact integer field arithmetic.

For the57344 both-free branches, `frontier-20261028-n8-dita-freefree-gate-v1.py` SHA **5f395a8fbc4861d0cef607e6557ccc101af9f751fc993c7cea91d1d1688707ec**, result SHA **ef22df3a442d0ed380c536462be98f8db6624d7f4f173c17d6bc064759e8c1b2**, uses 2×2 cross-parity blocks whose two free phases factor as invertible unit diagonal scalings. It rejects22528 by rank4 and4096 by phase-independent cofactor incompatibility. **30720 both-free branches remain**, explicit JSONL SHA **65a3bacaf8c2feaae3e0d72b00d80b9f51a227130369d09a7e56ec4beb4dfe93**. Nothing about these unresolved branches is implied by the listed rejections.

## 4. Evidence and honest boundary

The source programs/counters above are one computational desk, not an independently regenerated end-to-end proof of the enlarged family. The exact F4/F4 predecessor has a separately written full replay, but that does NOT independently replay the new arbitrary-block census. Some exploratory selected-resultant tests returned no exclusions; they are not counted. A real nonzero-delta continuous solution in any remaining branch would be an even-order Fourier-transversal counterexample, requiring independent actual-vector verification. Conversely all30720 must be closed and the enlarged proof independently replayed before claiming no-T for this family. No claim is made about all even orders, arbitrary order8 Hadamards, or unrestricted QLS10.
