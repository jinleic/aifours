# R-minus: every five-word confusion section uses at most eight comparison vertices

Owner `InfoGuessingRminus-2`, slot info-5. Verbatim `/bin/date` immediately before this write: `Sun Oct 25 13:07:50 PDT 2026`.

**NEW WRITTEN GLOBAL reduction, not a guessing-bound theorem.** Arbitrary physical alphabets, arbitrary five words, all simultaneous actual full-neighbour comparisons. No field, linearity, triangle-coset, support or particular five-syndrome assumption is needed. No scientific interpreter/program/replay/CLI, enumeration, symbolic kernel or nested agent was run. Metadata clocks/hashes/read/write only; v9/v10/v11/HOLD and the original deadline remain binding.

## 1. Exact theorem and remaining primary

Let b_0,...,b_4 be five words on the ORIGINAL R-minus graph. Suppose each unordered label pair ij has a witness vertex f(ij), meaning

`b_i|N(f(ij))=b_j|N(f(ij))` but `b_i,f(ij)!=b_j,f(ij)`.

These are actual full physical-symbol equalities and inequalities, not defect-only or projection-count constraints.

**Theorem8.** EVERY such valid choice of ten witnesses uses at most EIGHT distinct original physical vertices.

The proof eliminates ALL ten-colour and nine-colour assignments at once, using the SAME global array and exact graph structure. It is not an enumeration of selected input syndromes or a theorem merely for full outside cosets. If the words are section representatives, they may use every original coordinate; no omitted witness vertex is assumed to be a zero representative coordinate.

This is a necessary global palette reduction only. Sections with at most eight witnesses, general non-section Hall maps, and actual positive-gain FD trades remain unresolved. The original arbitrary-five-label/allm>=2 problem and arbitrary-class optimum are not settled, and20/3..1847/276 is unchanged. It does not supply an entropy certificate or T300 stronger-gate evidence.

## 2. Literal graph facts used

The full neighbourhoods are

`N1={2,3,4,5,6,7}`,

`N2={1,3,7,9,10}`, `N3={1,2,4,8,9}`,

`N4={1,3,5,8,10}`, `N5={1,4,6,9,10}`,

`N6={1,5,7,8,9}`, `N7={1,2,6,8,10}`,

`N8={3,4,6,7,9,10}`,

`N9={2,3,5,6,8}`, `N10={2,4,5,7,8}`.

The two hubs1,8 have degree6 and are nonadjacent. Define their anti-neighbour sets INCLUDING themselves:

`A1=V\N1={1,8,9,10}`,

`A8=V\N8={1,2,5,8}`.

Thus `A1 intersection A8={1,8}`.

Peripheral types according to adjacency to(hub1,hub8) are exactly

- L={2,5}, type(1,0);
- R={9,10}, type(0,1);
- Q={3,4,6,7}, type(1,1).

Two simultaneous full-star observations will be decisive:

`{1,9,10} subset N2 intersection N5`,                       (LSTAR)

`{8,2,5} subset N9 intersection N10`.                       (RSTAR)

Everything in the proof is invariant under exchanging the displayed hub roles, L/R and LSTAR/RSTAR. No triangle-cover or syndrome invariance is asserted or needed.

## 3. One label-connectivity system for the whole section

Let K be the complete graph on the FIVE labels0,...,4. Each of its ten distinct edges ij receives the original physical colour f(ij).

For EVERY physical vertex u, define a graph E_u on these SAME five labels by

`ij in E_u iff f(ij) in N(u)`.

The original neighbour equality for witness f(ij) makes b_i,u=b_j,u along every E_u edge. Therefore all symbols at physical u are constant on every connected component of E_u.

**Connectivity obstruction.** If u is used as a witness, E_u MUST be disconnected. Otherwise all five physical-u symbols agree, contradicting the own-symbol inequality for any pair coloured u.

This is a single simultaneous obstruction, including all actual full physical coordinates; no independent local partition is selected for different pairs.

A disconnected simple graph on five labels has at most6 edges. If it has5or6, its components must have sizes4and1: other nontrivial splits have at most C(3,2)+C(2,2)=4 edges. The four-label component is connected, with a unique isolated label a.

Write S_a for the FOUR label edges incident to a. If the complement edge set R_u=K\E_u has size4, then R_u=S_a. If it has size5, then R_u=S_a plus ONE extra edge not incident to a.

In both cases, EVERY pair actually coloured u must be incident to a: pairs among the other four labels have equal physical-u symbols and cannot use u. Distinct stars S_a,S_b meet in exactly their single edge ab; identical stars meet in4 edges. A star itself connects all five labels.

## 4. All ten physical colours are impossible

If f is bijective onto all ten original vertices, E1 and E8 each have6 edges. Since both hubs are used, the preceding classification gives

`R1=S_a`, `R8=S_b`.

But by exact preimages,

`R1 intersection R8=f^-1(A1 intersection A8)=f^-1({1,8})`,

which has exactly2 edges. Two stars intersect in1or4, never2. Contradiction.

No assumption about a syndrome family or a preferred pair witness was made.

## 5. Nine colours: exact count interface and both hubs used

If f uses exactly nine vertices, let t be the ONE omitted vertex and s the ONE doubled colour. Every other used colour has one pair, s has two, and s!=t.

For any physical u the distinct edge count is exactly

`|E_u|=deg(u)-1_(t in N(u))+1_(s in N(u))`.                 (COUNT)

First suppose BOTH hubs1,8 are used. Then t is peripheral. Each hub has at least5 observed edges, so by connectivity it has at most6. Hence

`1_(s in N(h))<=1_(t in N(h))` for h=1,8.                 (DOM)

Moreover

`|R_h|=4+1_(t in N(h))-1_(s in N(h))` is4or5.

Let a,b be the unique isolated labels for E1,E8. Both R1,R8 contain their corresponding stars. Their exact intersection is again

`R1 intersection R8=f^-1({1,8})`.

It has3 edges if s is a hub, and2 otherwise. Thus a!=b, since a common star would put4 edges in the intersection.

### 5.1 The doubled colour is hub1 or hub8

Take s=1 first. Because hubs are nonadjacent, (COUNT) gives

`|R1|=4+1_(t in N1)`, `|R8|=4+1_(t in N8)`.

If t belongs to L or R, these sizes are(5,4)or(4,5). A star and a distinct star-plus-one-edge intersect in at most2 edges, contradicting the actual3-edge intersection. Therefore t belongs to Q, and BOTH complements have size5.

Two distinct stars plus one extra each can have3 common edges only in the form

`R1 intersection R8={ab, ax, by}`,

where x,y are among the other three labels, with no requirement that x and y differ. The extras are ax for R8 and by for R1: each lies in the opposite star, not its own. If either extra did not have that form, intersection size could not reach3.

Hub1 owns TWO of these three pairs, and both must be incident to its isolated label a. Thus its two pairs are exactly ab,ax; hub8 owns the remaining by.

Consequently, in `R1=S_a union {by}`, the FOUR edges of S_a are exactly the preimage of physical colours{1,9,10}: physical1 carries ab,ax and physical9,10 carry the two remaining star edges. Physical8 carries only the extra by.

By(LSTAR), E2 AND E5 therefore contain the entire connected spanning star S_a. But2and5 are both used because the omitted t lies in Q. This contradicts the connectivity obstruction.

For s=8, interchange hub roles and L/R in the SAME count argument. The omitted t is again in Q. The four star edges are then carried by{8,2,5}, all observed by BOTH9and10 through(RSTAR). These used vertices have connected E9,E10, the same contradiction. All doubled-hub cases are excluded.

### 5.2 The doubled colour is peripheral

Now s,t are peripheral. Their types are the three nonzero binary types in Section2. (DOM) requires the type of s to be coordinatewise at most the type of t.

If their types agree, both R1,R8 have size4 and are distinct stars. Their intersection would be1 edge instead of the actual2. Thus types cannot agree.

The only remaining dominated types are

`t in Q, s in L` OR `t in Q, s in R`.

Take s in L. Then R1 has size4 and R8 has size5, so

`R1=S_a`, `R8=S_b union {ax}`,

and their2-edge intersection is exactly{ab,ax}, for some x distinct from a,b. The hub8 pair must be incident to b. Of these two edges only ab is incident to b; hence physical8 carries ab and physical1 carries ax.

The FOUR star edges of S_b are therefore carried exactly by physical{8,2,5}: hub8 carries ab, while physical2,5 together carry the other three, with the doubled one carrying two. By(RSTAR), used physical9and10 each observe the full connected star. This is impossible.

For s in R, the same explicit role exchange gives the four edges of the hub1 star carried exactly by{1,9,10}; used physical2and5 observe them all through(LSTAR). Again impossible.

This exhausts ALL peripheral s when both hubs are used. No individual omitted-Q choice or label assignment has been dropped.

## 6. Nine colours: one hub omitted

Suppose t=8; hub1 and ALL eight peripherals are used. As hubs are nonadjacent, (COUNT) gives

`|E1|=6+1_(s in N1)`.

Connectivity requires this to be at most6, so s is not in N1. Since s is used, it is one of{1,9,10}. In particular |E1|=6, and R1 is exactly one full star S_a.

The anti-neighbours A1 are{1,8,9,10}, and8 is omitted. Hence the FOUR edges of R1 are carried entirely by{1,9,10}, regardless of which of these colours is doubled.

(LSTAR) puts the whole spanning star inside E2 and E5. Both vertices are used, contradiction.

If t=1, the used hub8 instead has six observed edges; its four complement-star edges are carried by{8,2,5}. (RSTAR) makes the used vertices9,10 connected, contradiction.

Exactly one physical vertex is omitted in the nine-colour case, so either both hubs are used as in Section5, or precisely one is omitted as here. There is no unhandled case with both omitted.

Sections4–6 rule out10and9 used colours. Theorem8 follows. ∎

## 7. Exact interface to the original five-syndrome and arbitrary-family problems

The proof is purely relational. It applies to ANY actual representative section on the original graph, over allm>=2, over composite or noncyclic alphabets and to nonlinear choices, without assuming linear independent slots, full cosets or support-limited words. It also applies before any choice of syndrome values: actual different representatives are required only to be pairwise confusing.

For the frozen actual five-label family, its global W0–W2 system may therefore be restricted to witness assignments whose used set has size at most8. This does NOT mean the omitted physical coordinates are zero. Their E_u may be connected or disconnected, and their symbols must remain in the actual syndrome equations. One must not delete these vertices from the graph or replace full-neighbour observations by reduced ones.

For fewer than nine colours the complement-star counts can drop below5 observed edges; new component types such as3+2 genuinely become possible. The complete nine-colour proof cannot simply be repeated without those cases. Closing ALL assignments with at most8 comparison colours (or finding an actual section) is the exact remaining section task. Even a no-section result for a chosen family would not settle simultaneous Hall or yield a positive-gain trade.

An actual positive-gain construction still requires original FD outside data A and its actual removal union R(A), with |A|>|R(A)|. A universal no-gain theorem still needs the arbitrary-family injection/Hall statement. Neither has been obtained here. Interval20/3..1847/276 and T300 remain unchanged.

This paper has no correctness dependence on pending same-harness no-common-pivot, independent-palette, matching-palette or four-section-nonextension papers: its graph and full proof are self-contained. The only imported connection is the previously supported actual SECTION-to-removal interface, NOT a conclusion that every Hall injection must be a section. This NEW WRITTEN result requires fresh review and is not formal/kernel/configured-family/human/executable or novelty acceptance.
