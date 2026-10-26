# SPR7 written continuation — hybrid/full-space alternative and the exact first missing implication

Actual `/bin/date` observation before creation: **Sun Oct 25 04:20:57 PDT 2026**. Owner InfoSPR7 / info-2. **WRITTEN CANDIDATE, no scientific arithmetic, eval, enumeration, symbolic program or certificate replay.** Metadata clocks/hashes and source reads only. The parent correction and `parent-evidence-erratum-v7.md` are binding. This packet uses no result from the unadmitted new SPR arithmetic as an established premise.

## 0. Scope, imports and assurance

This gives an exact written alternative for the four-component hybrid cone, with **all coefficient corners, the entire finite frequency half-line, zero, and the forced positive leading coefficient** included. It also identifies precisely why an obstruction in that cone is not automatically an obstruction to all eight numerator coefficients. The alternative is uniform in the input box; it is **not** a universal positive SPR7 theorem or a characterization by the even profile alone.

Named profile-definition imports:

- `even-euler-comparator-candidate-v1.md`, SHA256 `ec744ccc6b269bb935aaa95e075cc559cda0ca6c44cc6bd580144306edc3c61a`, §§1–3: actual normalized midpoint-even F, `H=4F-tF'`, and the component pairing convention. Its sufficient scalar budget is not assumed universally applicable.
- `even-euler-entire-profile-obstruction-v1.md`, SHA256 `cf7d75fac33d83ffa93cf5af5d3f277753585375345fb38f4a18e6e511a2368f`, §7: fixed profile failure leaves arbitrary numerator coefficients admissible. Its reciprocal witness is not needed here.
- `owner-execution-scope-erratum-v1.md` and parent erratum v7: all new explicit union-box/certificate assertions from the earlier owner eval remain candidates pending written reconstruction, with no executable-verification credit. This packet does **not** import that box, its coefficient table, margin or claimed crossed completion as a theorem.

Classical imports for the new written argument are strict separation/nearest-point separation of a compact convex set from zero, finite-dimensional Carathéodory, compactness, and elementary polynomial algebra. Their use is explicit below. All eight numerator coefficients remain real. No rational certificate, rational dual weights or algebraic dual frequencies are asserted to exist merely from the alternative. Novelty is UNCLEAR; compactification and convex alternatives are classical.

The assigned v29-F Sun8 supplied-proof review was returned before this primary continuation; its separate verdict is not an SPR premise.

## 1. Literal box and unrestricted target

Let

`K={a(s)=s^7+a_1 s^6+...+a_7 : l_j<=a_j<=u_j, j=1,...,7}`,

with finite real endpoints and every member strictly Hurwitz. Degenerate intervals are allowed. Let V be its finite set of coefficient corners, with duplicates discarded. There are at most `2^7` corners; this is a definition, not an executed enumeration.

Write

`E_a(t)=-a_1 t^3+a_3 t^2-a_5 t+a_7`,

`O_a(t)=-t^3+a_2 t^2-a_4 t+a_6`,

`P_(a,b)(t)=E_a(t)E_b(t)+t O_a(t)O_b(t)`.

For a Hurwitz denominator,

`Re(b(iw)/a(iw))=P_(a,b)(w^2)/|a(iw)|^2`.

Thus the original target is one real polynomial b of exact degree seven with `P_(a,b)(t)>0` for every a in K and every **finite t>=0**, including zero. The denominator is known stable before any cancellation. A real monic Hurwitz polynomial has positive coefficients, for example by factoring it into stable real linear/quadratic factors. Hence the midpoint coefficient m_1 is positive and the actual anchors below are defined.

For a fixed b, P is affine in all seven denominator coefficients. Every a is a convex combination of corners, with weights depending on a but not on t or b. Therefore positivity at **every corner and every t>=0** is equivalent to positivity throughout K. This reduction never replaces a correlated family by a new coefficient hull: K is the original independent box.

## 2. Actual midpoint anchors and the four-column map

Put `m_j=(l_j+u_j)/2` and

`F(t)=E_mid(t)/m_1=-t^3+f_2 t^2-f_1 t+f_0`,

`Q(t)=O_mid(t)=-t^3+q_2 t^2-q_1 t+q_0`.

These are fixed by the input box. Define

`D(t)=(tQ(t))'=-4t^3+3q_2 t^2-2q_1 t+q_0`,

`H(t)=4F(t)-tF'(t)=-t^3+2f_2 t^2-3f_1 t+4f_0`.

The hybrid numerator has the one common coefficient quadruple theta=(alpha,beta,gamma,zeta):

`E_b=alpha F+beta D`,

`O_b=gamma H+zeta Q`.

No coefficient may depend on the denominator corner or frequency. Its degree-seven leading coefficient is

`h=gamma+zeta`.

A genuine exact-degree-seven SPR numerator must have h>0: h<0 makes its degree-seven pairing leading term negative and hence fails at sufficiently large finite t; h=0 is not exact degree seven. Positive scaling then normalizes h to one.

For the unrestricted numerator use its actual s-coefficient vector

`c=(e_0,e_1,e_2,e_3; o_0,o_1,o_2,o_3)`,

so that

`E_b(t)=e_0-e_1 t+e_2 t^2-e_3 t^3`,

`O_b(t)=o_0-o_1 t+o_2 t^2-o_3 t^3`.

Here o_3 is the degree-seven leading coefficient. The hybrid coefficient vector is `c=T theta`, where the four columns of T are, in this fixed coordinate order,

`T_alpha=(f_0,f_1,f_2,1; 0,0,0,0)`,

`T_beta =(q_0,2q_1,3q_2,4; 0,0,0,0)`,

`T_gamma=(0,0,0,0; 4f_0,3f_1,2f_2,1)`,

`T_zeta =(0,0,0,0; q_0,q_1,q_2,1)`.

No general rank-four assumption is made: F,D or H,Q can be dependent in special input boxes. All subsequent statements remain valid in the ambient four-coordinate parameter space even then.

## 3. Compactified full and hybrid evaluation vectors

Set `x=t/(1+t)`, so finite t>=0 corresponds to `0<=x<1`. Let `rho(t)=(1+t)^(-7)`. At a corner v and finite t define the full vector

`W_8(v,x)=rho(t)*( E_v, -t E_v, t^2 E_v, -t^3 E_v;`

`                         t O_v, -t^2 O_v, t^3 O_v, -t^4 O_v )`.

Then the normalized pairing is exactly

`c dot W_8(v,x)=P_(v,b)(t)/(1+t)^7`.

Every component extends continuously to x=1. Because O_v is monic with leading coefficient -1 while E_v has degree at most three,

`W_8(v,1)=(0,0,0,0; 0,0,0,1)=:e_infty`,

independently of v. At zero,

`W_8(v,0)=(a_7(v),0,0,0; 0,0,0,0)`.

Define the hybrid evaluation vector

`W_4(v,x)=T^T W_8(v,x)`.

For finite t its four entries are exactly

`rho(t)*( E_v F, E_v D, t O_v H, t O_v Q )`.

Its endpoints are therefore

`W_4(v,0)=a_7(v)*(f_0,q_0,0,0)`,

`W_4(v,1)=(0,0,1,1)`.

Thus retaining x=1 enforces h>0 rather than permitting a degree-six escape. Retaining x=0 enforces the actual strict constant-frequency condition. Neither endpoint may be dropped.

### Compact strictness lemma

A fixed exact-degree-seven numerator satisfies the original strict finite-frequency criterion if and only if there is eta>0 with

`c dot W_8(v,x)>=eta` for all v in V and all x in [0,1].

For necessity, its leading coefficient is positive as above; its normalized pairing is continuous and strictly positive at every finite x and at x=1. A finite union of compact intervals has a positive minimum. Sufficiency is immediate. The same statement with `c=T theta` gives hybrid strictness.

This does **not** add a new independently imposed infinity condition to the book target: positive leading coefficient is forced by exact degree seven and finite-tail positivity. Conversely no uniform margin can be inferred if one silently relaxes exact degree and permits leading coefficient zero.

## 4. Exact hybrid alternative, with ALL half-line and corner quantifiers

Let

`Z_K=conv{W_8(v,x): v in V, x in [0,1]}`,

`L_K=ker(T^T)`.

The generating set is compact; its convex hull is compact in finite dimension. The following two alternatives are mutually exclusive and exhaustive.

### H+ — one genuine hybrid common numerator

There exist one theta in R^4 and eta>0 such that

`theta dot W_4(v,x)>=eta`

for **every** corner v and **every** x in [0,1]. Equivalently, a single hybrid polynomial of exact degree seven is a common strict SPR numerator for all a in K and all finite real frequencies, including zero. Its h is automatically positive by evaluation at x=1 and can be normalized to one.

### H0 — a positive finite projected-moment obstruction

There are k<=5, corners v_1,...,v_k, compactified frequencies x_1,...,x_k in [0,1], and positive weights lambda_i with sum one such that

`sum_i lambda_i W_4(v_i,x_i)=0`.

Repeated corners/frequencies are permitted; zero and infinity atoms are permitted. No atom is required to be a denominator zero, an anchor root, or a stability-boundary contact. The weights and frequencies are real; rationality is not claimed.

### Written proof

H0 contradicts H+ by taking the weighted sum of its strictly positive inequalities. Conversely, if H0 fails then zero is outside the compact convex set `conv(W_4)=T^T Z_K`. Let y be a nearest point of that convex set to zero. Then y is nonzero and the elementary nearest-point inequality gives

`y dot w >= ||y||^2 > 0`

for every w in that convex set. Taking theta=y and eta=||y||^2 proves H+. If zero belongs to that convex set, Carathéodory in the ambient R^4 gives a convex representation using at most five generators; dropping zero weights yields H0. This proof does not execute an optimization or search for y.

Consequently the exact set criterion is

`hybrid feasible  <=>  Z_K intersect L_K is empty`.             (H)

This is a feasibility alternative for the named hybrid cone, **not** a theorem that robust Hurwitzness excludes H0.

## 5. Exact unrestricted alternative and why H0 is insufficient

The identical compact separation argument in R^8 gives

`unrestricted exact-degree-seven SPR feasible  <=>  0 notin Z_K`.  (U)

If unrestricted feasibility fails, Carathéodory gives at most nine corner/frequency atoms with

`sum_i lambda_i W_8(v_i,x_i)=0`.

Again these atoms can include zero and infinity. Nine is a safe ambient bound, not an asserted optimal contact rank or a new theorem about existing critical-boundary certificates.

For a hybrid obstruction put

`z=sum_i lambda_i W_8(v_i,x_i)`.

It only establishes `T^T z=0`. Written in the fixed coefficient order `z=(z_E0,z_E1,z_E2,z_E3; z_O0,z_O1,z_O2,z_O3)`, its four constraints are

`f_0 z_E0+f_1 z_E1+f_2 z_E2+z_E3=0`,

`q_0 z_E0+2q_1 z_E1+3q_2 z_E2+4z_E3=0`,

`4f_0 z_O0+3f_1 z_O1+2f_2 z_O2+z_O3=0`,

`q_0 z_O0+q_1 z_O1+q_2 z_O2+z_O3=0`.                          (R)

An unrestricted obstruction needs **all eight coordinates of z zero**, not merely these four equations. In particular an exact failure of every hybrid numerator is still not an unrestricted SPR7 verdict.

There are precisely three relevant cases:

1. `Z_K intersect L_K` is empty: hybrid and unrestricted synthesis both succeed.
2. `0 in Z_K`: unrestricted synthesis, hence hybrid synthesis, fails.
3. `0 notin Z_K` but `Z_K intersect L_K` is nonempty: unrestricted synthesis succeeds but the hybrid cone fails.

A nonzero z in the intersection does not by itself establish case 3, since Z_K might also contain zero elsewhere. The full zero-membership question still has to be answered. This distinction prevents promoting a four-coordinate dual certificate to an eight-coordinate one.

### Why projection or dimension alone cannot bridge the gap

T has at most four independent columns, so its annihilator has dimension at least four. It is not legitimate to conclude that a projected zero must be a full zero. Even keeping the two forced endpoint directions does not make this an abstract linear implication: choose a nonzero z in the annihilator with a nonzero coordinate outside the two endpoint directions. Such a choice exists by the dimension bound. The abstract convex hull of z and the two positive endpoint vectors contains z in the annihilator but does not contain zero; the middle nonzero coordinate forces the z weight to vanish in any putative zero combination, after which the two positive endpoint vectors cannot cancel.

That abstract convex set is **not asserted realizable by a stable SPR box**. Its sole purpose is to show why a Hurwitz-specific geometric theorem is essential. The actual restriction that the generators arise from all corners of one robustly stable independent box is the missing information, not something supplied by a generic projection argument.

## 6. Exact first unproved uniform step

For the hybrid mechanism to prove universal SPR7, the required statement is

> For every robustly Hurwitz independent monic degree-seven box K, its actual midpoint map T satisfies `Z_K intersect ker(T^T)=empty`.

By §4 this is exactly the claim that **no positive balance of at most five actual corner-frequency vectors can make all four moment sums vanish**. This formulation includes every corner, every finite half-line frequency, zero and the leading-coefficient endpoint. It does not restrict the search to anchor roots, a selected scalar sign, a finite grid or a presumed stable interval hull.

**First missing proof:** derive this projected-moment exclusion from all-member Hermite–Biehler interlacing of the original box. The current accepted profile theorems supply sufficient budgets and sign data, not such an exclusion. They cannot be cited as giving a common separating quadruple for every robustly stable box.

There are two honest continuations:

- Prove the projected-moment exclusion, using the actual whole-box Hurwitz structure. This would prove the hybrid mechanism universal, and therefore prove unrestricted SPR7.
- Construct a literal robustly Hurwitz box and an exact H0 balance. This would refute the hybrid mechanism only. To refute unrestricted SPR7 one must additionally establish full zero membership as in §5; a nonzero annihilator residual does not suffice.

If one assumes unrestricted synthesis for a particular box and tries merely to compress its numerator into the hybrid cone, the exact additional implication needed is

`0 notin Z_K  =>  Z_K intersect ker(T^T)=empty`.

No positive cone-preserving projection of arbitrary numerator coefficients onto `im T`, and no such implication, is proved here. Pointwise existence of a favourable direction at each corner/frequency would also be insufficient: it exchanges the common-numerator quantifier with the frequency quantifier.

## 7. Parkable outcome and non-claims

The delivered written result is the **exact compactified hybrid/full-space alternative**, explicit four moment equations (R), and the first genuinely unproved uniform implication above. It does not claim to resolve that implication. This is a new analytic front beyond adjusting the two Euler scalars; it is not another enumeration or an unsupported universal verdict.

All mathematical manipulation in this packet is written reasoning. No new numeric endpoint, coefficient list, rational certificate or finite count was computed or replayed. The standard separation and Carathéodory arguments are named imports, not proof-assistant verification. The packet requires its own separate supplied-proof reconstruction and parent disposition. The older unadmitted candidate is preserved with its assurance withdrawn as stated in the owner erratum; no old computation is retroactively promoted.

Unrestricted universal SPR7 remains unresolved. The first missing step is exactly the Hurwitz-specific exclusion of H0, or a real stable-box realization of it; the full eight-coordinate alternative remains the correct boundary for an unrestricted negative verdict.
