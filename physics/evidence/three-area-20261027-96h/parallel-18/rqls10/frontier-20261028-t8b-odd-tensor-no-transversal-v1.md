# An infinite even-order non-Butson tensor family has no transversal

**WRITTEN + EXACT FINITE AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 22:58:10 PDT 2026**. This is a non-Diţă/non-Butson local construction carried to infinitely many EVEN dimensions; it is not an unrestricted even-order theorem.

## 1. Statement and physical caller

Let K8 be the exact dephased non-Butson, non-2×4-Diţă T8B point `a=b=c=zeta6`, `d=(5+3zeta6)/7` in `frontier-20261028-t8b-generic-and-explicit-no-transversal-v1.md` SHA **bb279c42f4e76a77e9cbcbf980501af140969492d14e174fd0a98f2ea9d69ef9**. For EVERY odd positive integer m, form `K=K8 tensor F_m` in the standard CRT-aligned coordinates for n=8m. Its cyclic Fourier-product QLS has **NO orthogonal transversal**, even when rays repeat.

Because gcd(8,m)=1, F_(8m) is permutation-equivalent to `F8 tensor Fm` by CRT. Specifically, writing `t=m*alpha*t8+8*beta*tm` where alpha=m^(-1) mod8 and beta=8^(-1) mod m, physical rows can be relabelled `(r8,rm)=(alpha*r mod8,beta*r mod m)`. The actual product vectors then factor as

`psi_((r,u),(c,v)) = psi8_(r,c) tensor f_(u+v mod m)`.

A common coordinate permutation/unitary, physical row relabelling and cell phases preserve transversal existence. The claim concerns this CRT-aligned K order, including affine coordinate reindexings and row/column gauges; arbitrary independent source-row permutations of K are NOT assumed.

## 2. Exact local orthobase classification

The64 distinct local rays `psi8_(r,c)` have exactly **24** sets of eight pairwise orthogonal cells:

- the eight complete local rows;
- the eight complete local columns;
- eight rectangles `E×C` or `O×C`, where `E={0,2,4,6}`, `O={1,3,5,7}`, and C is one of `{0,4}`, `{1,2}`, `{3,7}`, `{5,6}`.

`frontier-20261028-t8b-local-cliques-v1.py` SHA **22e1d564c31f52fe69b4dc8d2aeb2102d87bb31f209ed75f75a5401281b91095**, result SHA **441fe54bec15101c8a9f7099c09f8b3d9ddff83dfbe2fa6bf635239b4277254c**, enumerates the actual orthogonality graph by increasing-vertex bitset DFS (1512 nodes). Its output contains all24 literal cliques. Independent `frontier-20261028-t8b-local-cliques-replay-v1.py` SHA **bf7c42942a1fa178b647326447e735116b5a83fc528bbf82a4b7bfb263cf2307**, result SHA **1343dc7d7cf54882f5dde80169ab9f988b43948464682d5cc24f927b8395ce66**, uses the separate Q(zeta24) original-vector Gram implementation and pivoted Bron–Kerbosch (457 nodes); all24 cliques match exactly. The source K8's original norms, row/column Grams,64 distinct rays and non-Butson/Diţă invariants are independently checked in the cited packet.

## 3. Odd-m incidence contradiction

If a transversal existed at n=8m, split its 8m cells by the m mutually orthogonal second-factor rays `f_(u+v)`. In one group, orthogonality must come from the local8 factor, so the group has at most8 cells. Since there are exactly8m cells, EVERY group has8 and is one of the24 cliques above.

Let A_r be the number of groups choosing local row r as their clique; B_c the number choosing local column c; `B=sum_c B_c`; and R_E,R_O the numbers choosing even/odd local-row rectangles. A transversal contains each of the m global rows `(r,u)` exactly once. Counting its cells with fixed local row r gives

`m = 8 A_r + B + 2 R_(r mod2)`.                                   (1)

For any two local rows of the same parity, (1) gives equal A_r. Consequently `A=sum_r A_r=4(A_E+A_O)` is divisible by4.

Similarly let S_c count rectangle groups whose two-column set contains local column c. Each of the m global columns `(c,v)` occurs once. Counting by fixed local column gives

`m = A + 8 B_c + 4 S_c`.                                          (2)

The right side of (2) is even because A is divisible by4; m is odd. Contradiction. This does NOT assume m<8 or forbid a row/column clique when m is large.

The source K8 is outside every finite-Butson equivalence class by its nonroot cross-ratio `-d`, and the same cross-ratio persists in `K8 tensor F_m` by restricting to one Fm row and column. Thus the family genuinely goes beyond root-order exclusions. At m=3 a separate exact local-Gram Z3 search returned UNSAT, `frontier-20261028-n24-t8b-f3-lift-v1.py` SHA **fc9946053353077dc287345917860e8b3e416b64d2ded936a38875fc742973f1**, result SHA **bf5074e91284f09c93e51595c88c1d35d36645263f156e2b8cc6c85415ebd023**; this is only solver-scoped corroboration, not a proof certificate or a premise of (1)–(2).

## 4. Boundary

The proof relies on the exact local clique census and the specified CRT tensor factorization; it does not cover arbitrary source orderings, arbitrary K8, other even n, or any unrestricted QLS10. It gives no general even-order no-go, no counterexample, no novelty clearance and no formal proof. Full review of both clique enumerations, CRT and the parity counts is required.
