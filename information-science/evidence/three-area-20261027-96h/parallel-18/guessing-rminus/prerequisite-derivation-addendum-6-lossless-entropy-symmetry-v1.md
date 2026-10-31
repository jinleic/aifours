# Addendum 6 — lossless entropy-profile symmetry with the actual alphabet cost paid

InfoGuessingRminus-2, original info-5. Actual native clock immediately before writing: **Tue Oct 27 15:22:33 PDT 2026**. AUTHOR-WRITTEN UNREVIEWED, S1 definition-first work only.

No new source, excluded guide, selected parameter/law evaluation or program is used. This proves an actual finite-law/decoder coupling, not a symmetry ansatz or an assertion that averaging entropy vectors automatically realizes a law. It does not by itself improve an original bound. Classical-method novelty is not claimed.

## 1. Universal finite construction for any original graph

Let G be any fixed nonempty finite loopless digraph and let K be a finite group of actual automorphisms of G. Let X be ANY finite joint law satisfying every original neighbour FD. For each g in K take an independent copy X^(g) of the ENTIRE law X, and put

`Y_v=(X^(g)_(g(v)))_(g in K)`.

This is a finite tuple-valued variable at each original vertex v, not a blowup of the vertex set or a new observation graph. Each component has its original finite alphabet, and different vertices may initially have different tuple alphabets; v1's type-class/common-alphabet construction handles that cost explicitly.

### Exact FDs on the original neighbourhoods

An automorphism satisfies N(g(v))=g(N(v)). For each component g, the original FD gives X^(g)_(g(v)) as a function of the variables X^(g)_(g(u)), u in N(v), all of which are observed in the tuple Y_neighbours. Apply those component functions and collect their outputs. This defines Y_v as a function of its ENTIRE original observed tuple; no neighbourhood or mixed coordinate is omitted.

Hence every original FD holds exactly. This is independent product on EXPANDED finite tuple alphabets, not a same-alphabet Latin/quasigroup collapse or an unproved closure operation.

### Exact entropy profile

Independence between the whole g-copies gives, for EVERY vertex subset A,

`H(Y_A)=sum_(g in K) H(X_(g(A)))`.   (Sym)

Consequently H(Y_(h(A)))=H(Y_A) for every h in K by reindexing the finite group. In particular,

`H(Y_V)=|K|H(X_V)`,
`max_v H(Y_v)=max_v sum_(g in K) H(X_(g(v))) <= |K| max_v H(X_v)`.

For nonzero marginal-entropy scale, the homogeneous gain ratio does not decrease. If that scale is zero, the original law is deterministic and both total entropies are zero. No division is made there.

Thus EVERY strict-gain finite FD law can be converted into one with an exactly automorphism-invariant ENTROPY PROFILE. No claim that the original law or its support is pointwise invariant is needed or made.

## 2. Exact forward and converse original-target caller

Suppose one proves `H(Y_V)<=c max_v H(Y_v)` for ALL finite original-FD laws whose entropy profiles are K-invariant, with c>=0. Applying it to the constructed Y gives

`|K| H(X_V) <= c max_v sum_g H(X_(g(v))) <= c |K| max_v H(X_v)`.

This proves the full all-law inequality for arbitrary X, and hence the universal original word-count bound by v1. Conversely any all-law bound of course covers the invariant-profile subclass.

For a lower gain, a strict ratio above c in any such Y yields an actual finite common-alphabet strategy through v1's explicit type-class construction. Thus this symmetry reduction is lossless for existence of an original strict-gain law AND for proving a universal upper bound.

It is not legitimate instead to take a convex mixture of permuted laws and assert the same FDs or average entropies. The proof uses independent whole-law copies and the exact tuple observation structure, so its entropy additivity and FD retention are paid rather than assumed.

## 3. The source-defined reflection of R-minus

The already displayed Fig. 1 transcription has the involution

`rho=(3 7)(4 6)(9 10)`, fixing 1,2,5,8.

The displayed neighbour lists in v1 satisfy N(rho(v))=rho(N(v)) for every vertex. Equivalently the 26-edge set consists of the fixed edges 1–2, 1–5 and pairs exchanged by rho:

- 1–3 / 1–7; 1–4 / 1–6;
- 2–3 / 2–7; 2–9 / 2–10;
- 3–4 / 6–7; 3–8 / 7–8; 3–9 / 7–10;
- 4–5 / 5–6; 4–8 / 6–8; 4–10 / 6–9;
- 5–9 / 5–10; 8–9 / 8–10.

This is a literal identity of the fixed graph definition, not an enumeration of candidate strategies or a diagnostic state/control. The deleted edge 9–10 is invariant as a nonedge under rho. The claim relies on the written Fig. 1 transcription, not an independent machine or original-book graph audit.

Taking K={identity,rho}, set

`h_rho(X)=max{H(X1),H(X2),H(X5),H(X8),`
`              [H(X3)+H(X7)]/2, [H(X4)+H(X6)]/2, [H(X9)+H(X10)]/2}`.

For the actual two-copy Y,

`H(Y_V)=2H(X_V)`, `max_v H(Y_v)=2 h_rho(X)`.

Thus v1's lower caller can be strengthened, for ANY finite original FD law, to

`H(X_V)>c h_rho(X) => an actual finite original code with |W|>q^c`.

This does not require H(X_V)>c max_v H(X_v) for the ORIGINAL unbalanced law: the explicit whole-law product first pays the balance and alphabet costs, then v1 pays the finite common-alphabet realization.

Conversely an actual strict-gain code at threshold c gives a uniform original-FD law with H(X_V)>c log q and h_rho(X)<=log q, so the displayed strict criterion holds. Hence the reflection-averaged denominator gives another exact original existence criterion, not merely a sufficient condition in a proper architecture.

## 4. Direct finite-decoder version, without an entropy shortcut

If the original X comes from an actual q-alphabet strategy, take independent words of that strategy, one per automorphism. At each original vertex store their relabelled components as a q^|K|-symbol tuple. The componentwise original decoders then have the entire original neighbour domains and yield exactly the product winning set (up to the relabelling), with |W|^|K| words.

This direct construction preserves the original exponent; it does not by itself create a strict gain. The potentially smaller entropy-normalized alphabet cost of §3 is realized only by the separate proven type-class construction. No improvement is inferred from tuple grouping alone.

## 5. What changed and next gap

This proves that searching only for automorphism-invariant entropy profiles is not an unjustified symmetry WLOG: every finite law is coupled to an actual new FD law with no loss of its original gain ratio, and both word-count callers are supplied. It also supplies the exact reflection-averaged entropy denominator rather than discarding alphabet costs.

It does NOT assert that any improving law exists, that the optimum is attained among finite alphabets, that an averaging mixture is FD-consistent, or that any bound has improved. A graph-specific full entropy certificate or actual finite law satisfying the strict criterion remains missing.

Inputs: released game/graph definitions, finite independent product laws, entropy additivity, elementary graph automorphism identities, and v1's displayed finite type-class/decoder construction. All remain author-written pending full union review. No source/history/novelty or stronger acceptance is silently imported.

Scientific HOLD, STOP outside S1, every HELD/ZERO/finding, N4 historical outcome/exit UNKNOWN, aux214 STOP and the original successor-window deadline persist.
