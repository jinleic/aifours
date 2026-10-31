# RQLS10 v50 — return to the UNRESTRICTED4-sector: qutrit-neighborhood rigidity and at mostSIX four-common-neighbor outsiders

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE writing this NEW manuscript: **Mon Oct 26 11:33:00 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact complex orthogonality/context-incidence/unitary-zero/plane-completion proof only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty or accepted finite-witness claim.

This is a genuinely UNRESTRICTED necessary geometry result for the actual remaining4+6 branch, not another closed Gaussian/Pauli/A5 ansatz. It does NOT exclude that branch or supply a100-ray witness. It retains actual complex projective rays and every original row/column/designated-transversal incidence.

## 1. Exact graph model and theorem

Assume an ACTUAL common4-sector of a maximal1-RQLS10. It has forty DISTINCT rays, with three original sector ONB contexts through each ray and four rays per context. Two different original contexts intersect in at mostONE actual cell/ray.

Define the SELECTED CONTEXT graph G: join two rays iff their cells belong to a common original context. This is NOT the full orthogonality graph; unselected orthogonal pairs may exist. G is simple9-regular. For a vertex v, its nine selected neighbors split into three DISJOINT orthonormal triples

    B0,B1,B2 in the actual3-space v-perp.

**Theorem.**

1. Between any two triples B_i,B_j there is at mostONE ACTUAL orthogonal pair, not merely at mostone selected edge. Thus the nine-neighbor induced full orthogonality graph has its threeK3's and at mostTHREE cross pairs.
2. For ANY selected NONNEIGHBOR x!=v, the number c(v,x) of common SELECTED neighbors is at mostFOUR. If the actual rays v,x are orthogonal despite being a selected nonedge, the bound improves toTHREE.
3. If a selected nonneighbor x has c(v,x)=4, the actual cross-orthogonality pairs among B0,B1,B2 MUST form a triangle with one vertex in each triple. There is at mostONE such triangle for fixedv.
4. For fixedv, there are at mostSIX selected nonneighbors x with c(v,x)=4. They lie in at mostTHREE explicitly defined2-planes, with at mostTWO possible ray cells in each, determined by actual original-context completions of the triangle's opposite pairs.

The cross-triangle and planes are DERIVED, not a symmetry normalization. These2-planes are NOT asserted common sectors, and no rank2 global obstruction may be copied onto them.

## 2. Two disjoint C3 ONBs can have at mostONE orthogonal pair

Let U be the3x3 unitary transition matrix between two ONBs in C3 sharing NO projective ray. An entry of modulus1 would mean a shared ray, so no such entry occurs. If two zero entries occur in one row or one column, normalization immediately gives an entry of modulus1. If they occur in distinct rows and columns, permute them to positions(1,1),(2,2). Orthogonality of rows1,2 has only the third-column term left, so

    U_(13)*conj(U_(23))=0.

One of those entries iszero. Then row1 or row2 has two zeros and an entry of modulus1. Contradiction. Thus U has at mostONE zero entry.

A zero is precisely an orthogonal pair of rays across the two bases. The neighbor triples B_i share no ray because all forty actual ray cells are distinct and their contexts meet only atv. This proves claim1, including ACTUAL rather than selected cross edges.

## 3. Common-neighbor boundFOUR, without conflating graphs

Take any selected nonneighbor x. The rays v,x are distinct, hence independent. Every common selected neighbor lies in

    P=(span(v,x))-perp,      dimP=2.

In each selected basis through v, at mostTWO of its other three rays can lie in P. If two do, they are an ONB of P. The third ray of that basis is the UNIQUE ray

    w in span(v,x) intersect v-perp.

This w is independent of which context throughv is considered. Therefore at mostONE v-context can contribute two common neighbors: two such contexts would both contain v and that same actual w ray, violating the one-cell intersection rule. The other two contexts contribute at mostone each. Thus c(v,x)<=2+1+1=4.

If v is actually orthogonal to x, the unique w is exactlyx. A context contributing two common neighbors would then contain BOTHv,x, contradicting x being a selected nonneighbor. Hence all three contexts contribute at mostone, giving c<=3. This includes unselected-but-actually-orthogonal x and does not assume every orthogonal pair is selected.

## 4. EqualityFOUR forces the complete cross-triangle normal form

Suppose c(v,x)=4. The actual rays v,x are NONorthogonal by section3. Relabel the v-contexts so its four common neighbors are

    u,u_perp in B0,
    h in B1,
    h' in B2.

Here u,u_perp form an ONB of P, and B0={u,u_perp,w}, with w the unique span(v,x) ray perpendicular tov. The four common rays are DISTINCT.

Apply the same2+1+1 bound to the three contexts throughx. One of those contexts must contain TWO common rays. It CANNOT contain u,u_perp: then that x-context and the different v-context already containing u,u_perp would share two actual cells, forbidden. The only remaining possible orthogonal pair among these four rays is h,h': within the2-plane P, each ray's perpendicular ray is UNIQUE, so neither u nor u_perp can be orthogonal to a different h orh'. Thus

    h'=h_perp.

The third B0 ray w is perpendicular to P, so it is orthogonal to BOTHh,h_perp. Therefore the three ACTUAL cross pairs are

    (w,h), (w,h_perp), (h,h_perp),

one between each pair of the three qutrit ONBs. This is the required triangle. Section2 allows at mostONE cross pair for each basis pair, so no other cross pair exists. In particular there cannot be a second such triangle for the samev.

Some of the triangle pairs need not be SELECTED edges. The pair h,h_perp IS selected (it occurs together in x's double-common-neighbor context); the other two are used only as actual orthogonality facts. This distinction is essential.

## 5. At mostSIX equality outsiders, in three exact completion planes

Fixv and its possible cross-triangle(t0,t1,t2), with t_i inB_i. If x has c4 and B_i is its double-common-neighbor context atv, the two OTHER rays of B_i span a2-plane P_i. Its perpendicular is

    P_i-perp=span(v,t_i).

The two common neighbors in the other v-contexts are exactly the OTHER triangle vertices t_j,t_k. The x-context containing both t_j,t_k is an ACTUAL original context. An orthogonal pair of actual rays can occur together in at mostONE original context, because two contexts sharing that pair would share two cells.

If that actual context exists, its other TWO rays form an ONB of span(v,t_i). Consequently x must be one of those TWO actual cells. This gives at mosttwo possibilities for each choice of i, and therefore at mostSIX selected outsiders in total.

A completion containingv itself would be a fourth context throughv, impossible; a completion containing t_i would also forcev as its other ray. Thus when such outsiders exist, the two remaining rays genuinely mix the two lines v,t_i and are not silently copies of existing neighbor rays. Their selected adjacency to all four required common neighbors must still be checked; the completion gives an upper bound on candidates, not sufficiency.

If the actual cross-triangle is absent, NO selected outsider can have c4; all have c<=3. This follows from the equality classification, not a search over forty rays.

## 6. Exact selected-graph census and remaining global constraint

Among N_G(v)'s nine vertices, the selected graph has its threeK3's(nine edges) plus at mostthree cross edges. Hence it has at most12 edges. Counting from the nine degree9 neighbors, the number of selected edges from N_G(v) to vertices outside {v} union N_G(v) is

    9*(9-1)-2*edges(G[N_G(v)])>=72-24=48.

For an actual40-ray sector there are30 outside vertices. Their common-selected-neighbor counts sum to that same edge number; each is at most4, at mostsix can reach4, and every actually orthogonal selected outsider has count<=3. These are literal constraints on the ACTUAL context graph and its COMPLEX embedding.

They are NOT inconsistent by themselves and no claimed new bound40<something is made. The point is the rigid equality normal form and six-candidate limit, useful when pushing remaining unrestricted4-sector geometry. No finite enumeration, failed search or timeout is being presented as proof of global absence.

## 7. Original gap and full acceptance boundary

A complete gate must read/reconstruct ALLseven sections/endings: selected-versus-actual graph definition; C3 unitary two-zero lemma; the unique span(v,x) completion; the nonedge/actual-orthogonal3 case; BOTHcontext distributions in c4; why the repeated u-pair context is forbidden; the forced h-perpendicular pairing; exact ACTUAL cross-triangle; the three opposite-pair completions/atmostsix; and selected-edge census without global-sector promotion.

Only the literal original common-sector/context trace model from parent-adoptedv15/v16 is imported; the local complex-linear-algebra proof is printed fully. No Pauli/A5/Gaussian/Hadamard/finite-code normal form is a premise. No common2-sector is inferred from a local plane, no unrestricted4-sector no-go, no100-ray witness, no formal/kernel/family/human/current-openness/novelty or unperformed finite-witness gate promotion.

The arbitrary4+6 branch remains OPEN, as do5+5 and irreducible10. All claims remain AUTHOR-WRITTEN pending entire mathematics/application review. No scientific execution/private approximate scout/independent checker/control/vendor/priority gate performed or passed. All old process/math findings, v9/v14 withdrawals, frozen histories and ZERO-credit quarantines persist. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; primary continues actual unrestricted geometry/construction rather than retrying a closed finite model, no early pending-review park.
