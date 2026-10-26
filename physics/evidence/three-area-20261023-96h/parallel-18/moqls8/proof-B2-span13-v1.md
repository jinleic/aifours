# B2 continuation — projector-span dimensions11 and12 excluded, candidate v1

Status: AUTHOR-WRITTEN CANDIDATE, not separately or parent-accepted. This is a NON-LOAD-BEARING strengthening of the frozen full conditional assembly: that assembly still uses only B2 a>=12. It changes no GB Boolean status, old qualification or gate. No scientific execution, CLI or nested agent.

## Exact hypothesis and imports

Q_1,...,Q_5 are actual pairwise-orthogonal QLS(8), row0 standard up to phases, with literal P1-B2 column0 supports

    {0}, {1,2,3}, {7}, {6}, {4,5}, {4,5}, {2,3}, {1,2,3}.

Every displayed coordinate is nonzero. Put blocks Z={0}, A={1,2,3}, B={4,5}, D={6}, E={7}. Let S be the real span of all square1 rank-one cell projectors. The row0/column0 axis span S_axis has dimension11 by the actual ONB-diagonal-algebra intersection argument: its bipartite graph has five components. Every member of S_axis is block diagonal across these five blocks.

The two new mathematical dependencies are stated at their CANDIDATE boundaries:

- ISOLATE, §§2–3 of `proof-isolated-sector-exclusion-v1.md`, SHA256 `34e5eca0a0d7ebac81b67c39cde758591513c79bf848d3bf9263c27126d1855d`: a globally isolated two-space with two distinct orthonormal ray-pairs is impossible for n8,t5.
- ONE-CHANNEL, §3 of `proof-low-span-rigidity-v1.md`, SHA256 `d64f57609450e2c6afbff5ddf3a6d768b1bb9c23d3159a8bf7a19604475380a6`: if every square1 cell is B-pure, B-perp or mixed in one fixed F=span(b,c), b in B,c in B-perp, and both a mixed cell and a B-pure ray outside{b,b-perp} occur, then n>=2(t+1). Its proof uses two dimension-saturated ray-pair decompositions, with every OTHER square's subspaces kept separate.

No T16 exhaustiveness, old K1/K2/K3 result, old exact-input UNSAT or global covariance budget is a premise of this B2 statement. The template is an explicit antecedent, not the whole primary problem.

## Claim

    dim_R S>=13.

### 1. Dimension11 already fails by whole-vector isolation

If dim S=11, then S=S_axis. For every full-cell vector v, vv* is block diagonal, so its B/B-perp outer product v_B v_{B-perp}* vanishes. This forces v_B=0 or v_{B-perp}=0. Thus B is globally isolated in the EXACT sense used by ISOLATE.

The standard row0 B-pair is{e4,e5}; column0 gives q^4,q^5, an ONB whose two vectors both have both coordinates4,5 nonzero. These are different ray-pairs, contradicting ISOLATE. Since S contains S_axis, smaller dimensions were impossible from the start.

### 2. Suppose dim S=12

Let pi delete the five diagonal blocks of a Hermitian matrix. Then pi(S_axis)=0 and dim pi(S)<=1.

If pi(S)=0, every full-cell projector is block diagonal and the preceding isolation contradiction still applies. Thus pi(S)=R M for a nonzero Hermitian off-block matrix M. Choose a mixed unit vector v and scale M=pi(vv*). Every mixed unit vector w satisfies

    pi(ww*)=lambda M

for a real nonzero lambda.

### 3. At least three active blocks are impossible

Let J be the blocks where v has nonzero component. The off-block nonzero positions force w to have exactly the same active blocks. For each X in J, rank-one outer products show w_X=c_X v_X for a nonzero complex scalar c_X, with

    c_X conjugate(c_Y)=lambda for all distinct X,Y in J.

If |J|>=3, choose X,Y,T distinct. The equations for X,Y and X,T give c_Y=c_T. Their mutual equation then gives lambda=|c_Y|^2>0; all c_X coincide. Therefore w is parallel to v and normalization forces lambda=1. ALL mixed projectors have off-block part M, while all pure-block projectors have off-block part0.

A row containing a mixed cell would consequently have a positive integer multiple of M as the off-block sum of its cell projectors. But its ONB resolution is the block-diagonal identity. Contradiction. Hence exactly TWO active blocks occur globally.

### 4. The one channel must touch B

With two active blocks X,Y, the column/row spaces of M's rank-one X,Y block fix unit rays b_X in X and c_Y in Y. Every mixed vector lies in span(b_X,c_Y), with both components nonzero; every other cell vector is pure in one coarse block.

If neither X nor Y were B, every cell would again be wholly in B or wholly perpendicular to B. The two different B-axis bases would contradict ISOLATE. Thus one active block is B. Rename its fixed ray b and the other block's fixed ray c; c belongs to B-perp.

We have exactly ONE-CHANNEL's whole-vector hypothesis: every cell is B-pure, B-perp or mixed in F=span(b,c). A mixed cell exists because pi(S)!=0. A B-pure ray outside beta={b,b-perp} exists because the two actual B-axis ray-pairs{e4,e5} and{q^4,q^5} are different; beta cannot contain all of them. No amplitudes or phases were fixed to obtain this fact.

ONE-CHANNEL now gives8>=2*(5+1)=12, a contradiction. This rules out dim S=12 and proves the candidate bound13.

## Exact scientific consequence and remaining obstruction

This removes two genuine B2 full-configuration span branches, retaining arbitrary interior vectors and all permitted phases. It does NOT exclude B2 configurations of span at least13, prove either B2 strengthened Boolean input UNSAT, or prove a counterexample. GB B2.M2 and B2.M4 remain UNKNOWN.

At span13 the off-block image may be two-dimensional. It may contain a true three-dimensional rank-one cone or two coupled rank-one channels; the one-dimensional cancellation argument above does not cover it. Treating two real dimensions as one fixed complex ray channel without proof would be a silent restriction. That exact coherence case is the next K4/B2 obstruction, if the complete conditional assembly's more global per-square-rank argument does not pass review.

The full conditional assembly remains immutable and does not rely on this strengthening. Correctness, import trust, full-target closure, novelty and significance remain separate; no acceptance or priority claim follows from this author proof.
