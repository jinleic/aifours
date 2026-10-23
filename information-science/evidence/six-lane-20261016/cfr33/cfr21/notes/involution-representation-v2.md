# Exact nested-cover and affine reduction for paired involutions

Recorded 2026-10-17 20:24:25 PDT. Same seven-row model as v1; no heuristic or multiplier-specific exclusion.

For a fixed h, each legal g assignment on one h-orbit covers that orbit marker and every value it contributes to g, g-id, g-mu*h, g-mu*g(h). AlgorithmX over these slot/value items is exactly equivalent to the v1 mask enumeration. The implicit zero column supplies value0 in all four families. Every full cover yields one g; paired-row swapping chooses its canonical representative, and all retained pairs are tested directly. The v2 audit mode enumerates V completely for a specified h and checks all four maps independently.

Affine existence symmetry: for any unit u and fixed point a of h, set x=u*(t-a), h_new(x)=u*(h(u^-1*x+a)-a). Translate rows by the group-fixed vector (0,a,mu*a,b,mu*b,c,mu*c), then scale all entries by u and reindex. Choose b=g(a), c=j(a), obtaining h_new(0)=g_new(0)=j_new(0)=0. Thus search only lex-min h under these transformations. This is a true group-preserving row translation, not an assumed multiplier hypothesis.

Controls: brute Python permutations reproduce total H, affine representative H, exact V sets and every compatible V pair for n7 mu1/-1 and n9 mu1/-1. Both prime13 controls pass the full definition/event/position/mutation/action gate. Native boundaries/overflows still return UNKNOWN. Source/binary hashes are pinned in the dated README addendum before target use.
