# Parent mathematical spot check: universal generic configurations

Parent reading after the 2026-10-18 00:12:21 PDT resource-gate observation. This is a direct written derivation, **not acceptance of the new theorem**. Both hostile CLI reviews and the full RUNS assembly audit still need to run once the resource gate permits them. No new solver, checker, reviewer CLI or enumeration was launched for this note.

Source: `mathematics/evidence/six-lane-20261016/olson/inverse-run-count/mixdef-high/c6/proof-GC.md`, SHA-256 `f968a396facf396854662cbcb566c614e7e1e1dac415ca23ae70309878998425`; imported GS/TS/NW read directly in `proof-SEEDG-r2.md` LF69–99. The source's setting is the **NMH** setting, including k≥p+1 and its normalization hypotheses; do not extend this to arbitrary run words by omitting that import.

## 1. The diamond criterion

Write g=kB, κ=g+B, Δ=2p−R≥3, E=R−k=Σe_i, D=A−B and e_i=r_i−1≥0. For a proper pattern with m blocks and mass y, both floor terms are minimal precisely when

    2g+B+1 ≤ 2m+y ≤ 2p−B+1,
    2κ+1−A ≤ 2m−y ≤ 2p−A+1.

The one-unit shifts incorporate the exact parity restrictions from the floors; they are not a real-valued relaxation. Both intervals have radius p−κ. With centered coordinates

    a1=2m+y−(p+g+1),
    a2=2m−y−(p+κ+1−A),

one has a1+a2=4m−(k+2), a1−a2=2y−D and 2(p−κ)=E+2Δ. Hence the genericity condition is exactly

    |4m−(k+2)| + |2y−D| ≤ E+2Δ.

Complementing a proper pattern preserves genericity.

## 2. A linear-length boundary walk

Fix target run t, weight d=d_t, and list the other L=k−1 runs as a path. Take m=floor((k+4)/4), so c=|4m−(k+2)|≤2, m≥2 and 2m≤L−1.

Use colourings with first colour X, last colour Y, and m nonempty blocks of each colour. The initial block lengths are

    (1,...,1,L−2m+1).

Swap all colours and restore the two endpoint colours. The resulting block lengths are

    (2,1,...,1,L−2m,1),

again with m blocks of each colour. For the X-mass v, their sum is

    v_initial+v_final = D−d+d_(t+1)−d_(t−1).

Their boundary vectors are b_j=j initially, and b*_j=j+1 for j<2m−1, b*_(2m−1)=L−1. Moving the last boundary right first, then each earlier boundary right one position in descending order, preserves strict boundary order. Each move recolours one nonendpoint run. **For these particular endpoints the walk has exactly L−2=k−3 moves**, a stronger explicit justification of the source's “linear” remark than its loose quadratic bound.

All colourings have both colours nonempty. Thus Q=X avoids t, Q and Q+t are proper, and Y is the complement of Q+t. Both X and Y have m cyclic blocks; Q+t also has m. No isolation of t from Q is required by Lemmas TS or GS.

## 3. The mass window cannot be skipped

Put W=E+2Δ−c. The desired masses form the integer interval

    lo=ceil((D−W)/2)+max(0,−d),
    hi=floor((D+W)/2)−max(0,d).

This is the rounding of the real interval centered at (D−d)/2 with width W−|d|. It contains at least W−|d| integer values.

Let τ=E+2−|d|. A single-run move has size at most E−e_t+1≤τ (the balanced-pair target gives an even smaller bound). Since Δ≥3 and c≤2,

    hi−lo+1 ≥ W−|d| ≥ τ+2.

The endpoint-mass sum differs from D−d by δ=d_(t+1)−d_(t−1). Distinctness of the three runs gives

    |δ|+|d| ≤ E+3 < W.

Their average is therefore strictly inside the real target interval. Either an endpoint is in the integer interval or the walk crosses it. A step of size≤τ cannot jump over an interval containing≥τ+2 integer values. One colouring consequently gives generic X and generic Y, hence generic Q and Q+t.

## 4. Conditional implication

The accepted GS(b) applies to **any** proper Q avoiding t for which Q+t is proper and both are generic; it does not require a separate block, nonadjacency or m(Q+t)=m(Q)+1. With NW/GS(a), the actual configurations give a quality seed at each run, or an actual empty interval that directly contradicts avoidance. The accepted count-free corollary of A0/C0-all then excludes NMH words with R≤2p−3.

This checks the new core argument conditionally on the stated NMH identities and accepted imports. It does not by itself prove NMH for the complementary R range, RUNS, INV* or full ordered Olson. The assembly must independently check those branches and every use of inherited hypotheses. Finite tests and the earlier315-row E2 certificate are not premises of this derivation.
