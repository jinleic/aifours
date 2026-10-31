# All 30 standard rank-two MUB projectors are isolated

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at completed exact check: **Wed Oct 28 19:25:06 PDT 2026**. This extends the ONE-projector local theorem `frontier-20261028-flat-projector-local-isolation-v1.md` SHA **7100ab2bcad58ce964a75c48ac762e11d54fe409bc2eeb65ee931bd45a366718** to 30 explicit projectors. It does NOT assert that those are all feasible projections or settle unrestricted MUB/QLS10 existence.

## 1. Statement

Let `B_q=diag(omega^(q t²)) U`, `U_(t,j)=omega^(3tj)/sqrt(5)`, `omega=exp(2*pi*i/5)`. The fixed 5D triple is I,B0,B4. For each `q in {1,2,3}` and each pair `i<j` in F5, define

`P_(q,i,j)=|B_q[:,i]><B_q[:,i]|+|B_q[:,j]><B_q[:,j]|`.

These are 30 actual rank-two orthogonal projections, each having diagonal2/5 in I,B0,B4 by quadratic Gauss sums. **Claim:** EACH of the30 is isolated in the set of rank-two projections with those three flat diagonals. Moreover EACH has a neighborhood containing no Schmidt-support projector of a common unbiased vector for the fixed 10D Weyl MUB triple.

## 2. Three exact representative certificates

The cited one-projector packet gives the complete Grassmann chart, rank10/2D-kernel, nonzero left-null-quadratic resultant and sequence-normalization proof for representative `(q,i,j)=(3,0,1)`. The successor checker `frontier-20261028-rank2-isolation-orbits-v1.py`, SHA **210bdf70640ec251e1ed65bb2a3a49ff40b9170f4f78e24565aada7a7a83d573**, imports that exact Q(zeta20) number-field machinery and repeats the SAME 12×12 rank and resultant calculation for representatives `(1,0,1)` and `(2,0,1)`. Each representative's `sqrt5*B†W` coefficients are exact and checked unimodular. Observed output:

```text
PASS Phi20 arithmetic; exact 12x12 Jacobian rank 10 and real 2D kernels
PASS two left-null quadratic forms have nonzero exact resultant, including infinity
PASS q 1 pair (0, 1) rank10, nonzero quadratic resultant
PASS q 2 pair (0, 1) rank10, nonzero quadratic resultant
PASS 30 standard WH pair projectors split into three 10-element symmetry orbits
```

The exact computations are an executable certificate, not a substitute for independent inspection of the graph-chart Taylor expansion, number-field implementation, quadratic resultant and limiting argument in the preceding packet.

## 3. Triple-preserving symmetries cover all30

For c∈F5^*, d,nu∈F5, let

`(T v)_t=omega^(eta t²+nu t) v_(c t+d)`,

where eta=0 if c²=1 and eta=4 if c²=4. T preserves I and permutes B0,B4 up to basis-vector phases and permutations. It sends a B_q column j to a column of B_q' with

`q'=eta+q c²`, `j'=2*(2q c d+3c j+nu)` mod5.

The checker exhaustively enumerates these finite transformations and verifies that the30 pairs form THREE disjoint 10-element orbits represented by `(3,0,1)`, `(1,0,1)`, `(2,0,1)`. Unitary conjugacy preserving the three diagonal-flatness constraints carries local isolation from each representative to its whole orbit. This is an exact finite symmetry covering, not numerical clustering.

## 4. Excluding common 10D vectors near all30

If P=P_(q,i,j), any standard-basis-flat unit a in its range is a phase multiple of one of the two B_q columns: for `a=alpha B_q[:,i]+beta B_q[:,j]`, all five equal coordinate magnitudes force

`Re(conjugate(alpha)*beta*omega^(3(j-i)t))=0` for every t,

so alpha*beta=0. An orthogonal flat b is the other column up to phase, and b_t/a_t is a nontrivial character times a global phase. The exact odd-cycle cross-gate obstruction `frontier-20261028-character-ratio-obstruction-v1.md` SHA **ae331153fb2b082ab50382e12531c2766b288e4cc654aacca11b86cdaf4036b8** excludes a common 10D unbiased vector. Since each P_(q,i,j) is isolated among flat P, a neighborhood of each is excluded.

## 5. Scope

No proof is offered that every rank-two P with three flat diagonals is in these30 isolated neighborhoods. The previous floating search found no reliable counterexample, but floating clustering does not classify an algebraic set. Any common MUB vector, and hence any associated Weyl-orbit QLS10, must avoid these neighborhoods; arbitrary other projection components, irrational phases, other resolutions and general nonproduct 1-RQLS10 remain open. The complete result requires independent review and novelty assessment.
