# Shor completion: an all-order nine-tail border obstruction

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 18:57:07 PDT 2026**.
**WRITTEN collision-table theorem with independently replayed exact symbolic certificates. It does not resolve the unrestricted original problem, establish priority, or claim formal/human/independent-family verification.**

## 1. The theorem

For any finite UD factor-complete extension D of the literal Shor S, let `a^n` be its actual pure-a atom and define the actual b-run borders

    P={i mod n:a^i b^k in D, k>=1},
    Q={j mod n:b^l a^j in D, l>=1}.

The separately reconstructed, classical direct-border factorization gives `P+Q=Z_n` directly and `n>=26`, with

    {0,3,8,11} subset P,      Y={0,1,7,13,14} subset Q.

The predecessor `frontier-20261028-eight-tail-border-obstruction-v1.md` proves `|Q|>=8`. Here we prove `|Q|!=8`, hence **`|Q|>=9` for every feasible n**, with no prime-valuation restriction. All border sets belong to the same actual D.

## 2. Certificate notation and initial split

Assume `Q=Y union {U,V,W}`, with all eight elements distinct. For target `t`, column `s in Q` refers to the candidate `t-s` for P. A table entry `K/(q,q')` means the explicit equality

    (t-s)+q = K+q',     K in P,    q,q' in Q,    q!=q'.

Directness forbids that P-candidate. A `*` denotes a survivor. Coverage forces one of the surviving candidates into P; if a row has no survivor, coverage fails. This remains valid for any cyclic specialization: if a displayed candidate equalled K, the equality with distinct q,q' would itself force q=q'.

Cover `W+1`. Only the three marked candidates survive. The two latter are exchanged by relabeling U and V. Thus it suffices to analyze either `B=W-12 in P` or `B=W-U+1 in P`.

| target t | s=0 | s=1 | s=7 | s=13 | s=14 | s=U | s=V | s=W |
|---|---|---|---|---|---|---|---|---|
| W+1 | 8/(7,W) | 0/(0,W) | 8/(14,W) | * | 0/(13,W) | * | * | 0/(0,1) |

## 3. Case A: `B=W-12 in P`

At target `V+1`, only sources U and W survive, so `T=V-U+1` or `T=V-W+1` lies in P.

| target t | s=0 | s=1 | s=7 | s=13 | s=14 | s=U | s=V | s=W |
|---|---|---|---|---|---|---|---|---|
| V+1 | 8/(7,V) | 0/(0,V) | 8/(14,V) | B/(W,V) | 0/(13,V) | * | 0/(0,1) | * |

### A1. `T=V-U+1`

The following three rows force `D=2+V-W`, `E=2+U-V`, and `F=2-V`, respectively:

| target t | s=0 | s=1 | s=7 | s=13 | s=14 | s=U | s=V | s=W |
|---|---|---|---|---|---|---|---|---|
| V+2 | 3/(1,V) | 8/(7,V) | 8/(13,V) | 3/(14,V) | B/(W,V) | T/(0,1) | 3/(1,0) | * |
| U+2 | 3/(1,U) | 8/(7,U) | 8/(13,U) | 3/(14,U) | B/(W,U) | 3/(1,0) | * | D/(V,U) |
| 2 | 3/(1,0) | 0/(0,1) | 8/(13,0) | 3/(14,0) | 0/(13,1) | T/(V,1) | * | D/(V,0) |

Then `E+0=F+U` violates directness.

### A2. `T=V-W+1`

The first two rows force `D=2+V-U` and `E=1+U-V`; the last row has no survivor.

| target t | s=0 | s=1 | s=7 | s=13 | s=14 | s=U | s=V | s=W |
|---|---|---|---|---|---|---|---|---|
| V+2 | 3/(1,V) | 8/(7,V) | 8/(13,V) | 3/(14,V) | B/(W,V) | * | 3/(1,0) | T/(0,1) |
| U+1 | 8/(7,U) | 0/(0,U) | 8/(14,U) | B/(W,U) | 0/(13,U) | 0/(0,1) | * | T/(V,U) |
| 2 | 3/(1,0) | 0/(0,1) | 8/(13,0) | 3/(14,0) | 0/(13,1) | D/(V,0) | E/(U,1) | T/(V,1) |

## 4. Case B: `B=W-U+1 in P`

The four rows force `D=2+W-V`, `E=2-W`, `F=V-12`, and `G=U-12` in order:

| target t | s=0 | s=1 | s=7 | s=13 | s=14 | s=U | s=V | s=W |
|---|---|---|---|---|---|---|---|---|
| W+2 | 3/(1,W) | 8/(7,W) | 8/(13,W) | 3/(14,W) | B/(13,U) | B/(0,1) | * | 3/(1,0) |
| 2 | 3/(1,0) | 0/(0,1) | 8/(13,0) | 3/(14,0) | 0/(13,1) | B/(W,1) | D/(W,0) | * |
| V+1 | 8/(7,V) | 0/(0,V) | 8/(14,V) | * | 0/(13,V) | B/(W,V) | 0/(0,1) | E/(1,V) |
| U+2 | 3/(1,U) | 8/(7,U) | 8/(13,U) | 3/(14,U) | * | 3/(1,0) | D/(W,U) | E/(0,U) |

Finally `F+U=G+V`, contradicting distinctness of U,V and directness. All cases fail, proving `|Q|>=9` with the predecessor.

## 5. Same-code quantitative consequences

With `N_Y` and `M_Q` exactly as in the eight-tail predecessor (actual one-b atoms with tails outside Y, and actual multi-b border atoms `b^l a^j`, `l>=2`), its same-code row-packing argument yields, for `0<=m<=3`,

    M_Q<=m  ==>  N_Y >= n-5 floor(n/(9-m)).

Every counted multi-b atom has a distinct tail residue outside Y. At n=1320, `|Q|>=9` and `|Q|` divides1320 imply `|Q|>=10`. Thus `M_Q<=0,1,2,3,4` forces `N_Y>=660,590,495,380,220`, respectively. In particular, `N_Y<220` would require at least five actual multi-b prefix-border atoms. No such completion is asserted.

For n=1320, the previously reported necessary P-cardinalities lose165 because Q would have size8. The remaining filtered set is

    |P| in {10,12,15,20,22,24,30,33,40,44,55,60,66,88,110,120,132}.

The set is not a feasibility claim, and no n=1320 exclusion follows.

## 6. Exact checks and provenance

`frontier-20261028-nine-tail-table-check.py`, SHA256 `c956626f892e6d11496751dd98bed817615cce9f92158b0f1807c95166ba6d6d` (84 LF, 3362 bytes), checks every displayed entry and branch in integer coefficient tuples, the two final identities and the root symmetry; actual output PASS.

An additional independently replayable finite proof tree is `frontier-20261028-nine-tail-symbolic-proof-pruned-v1.json`, SHA256 `29229069e18bd5a9f980f21005665526b83b424359ef00ca995c0beb719d1133` (1 LF, 6914 bytes). `frontier-20261028-nine-tail-pruned-replay.py`, SHA256 `7200689e1faa09b3bd0eee9eac48eb8790061a84fa26deb808ea5e31b41ba15c`, invokes the separate replay implementation `frontier-20261028-nine-tail-proof-replay.py`, SHA256 `d0b85e8f99dd22150bd6f7a66684a23cd953f122218997af3be6baba1c3d75a4`; it checked 136 symbolic steps, two branch points, four leaves, with three double hits and one empty coverage clause. The larger generator trace and its proof minimizer are retained but not needed for reading the written tables.

These are exact machine checks of finite identities, not formal proof, independent-model-family review, human review or novelty screening. The general border-factorization theorem is prior literature. The original finite UD factor-completion/noncompletion problem remains OPEN.

**END OF NINE-TAIL BORDER OBSTRUCTION.**
