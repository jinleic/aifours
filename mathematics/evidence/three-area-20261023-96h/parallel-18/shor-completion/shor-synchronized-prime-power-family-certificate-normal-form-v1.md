# A complete synchronized recursive certificate for prime-power common-complement families

Owner MathShor-2. Actual `/bin/date` immediately before this NEW write: **Mon Oct 26 13:06:27 PDT 2026** (precreation observation).

**NEW COMPLETE WRITTEN CANDIDATE, at J_sync below, NOT parent-adopted.** This gives an IFF recursive characterization for ENTIRE mutually complementary prime-power families in an arbitrary finite cyclic group, with ALL branches synchronized against ALL complementary fibers. It retains the previously open proper-subgroup branch rather than assuming it absent. Its FACT application covers the whole unbounded-exponent lift families of the108LF packet; it supplies NO original Shor completion/noncompletion, new size exclusion or raw stabilization.

## 0. Actual authority and dependency boundary

Parent v94 was actually read completely before this continuation; every future write uses the verified absolute owner root `.../parallel-18/shor-completion/`. Both mislocated originals stay unchanged at their actual paths; no move/copy/delete/overwrite/retarget or process cure. All seven own findings, three precise provenance blockers and all ZERO consuming guidance remain.

The COMPLETE new parent `RUN/shor-Sands-I2-I3-general-no-unit-B-entire-parent-v1.md`, SHA256 `6eac76c8e123bf8aa41bda5cd14f898fe1713874d29bdbf4380a61f318bbe59f`, was actually read through END BEFORE operative use. Its four ordinary-WRITTEN M/UO-I2/GD-I3/general-no-unitB gates are now adopted at their exact elementary cuts. No coauditor body or pending review was opened or consumed. This adoption does not promote the108LF family theorem or a new composition.

Define **J_sync** to contain:

1. The collective-family theorem CF in ENTIRE `shor-collective-prime-power-complements-and-FACT-lift-dichotomy-v1.md`,108LF, SHA256 `d4dfde05236327702cf15a4ecf8dc0c9cb5adaee05d439e87fcc06d739151e49`, and its exact M/I3 input/application cuts. **CF is still an UNREVIEWED named candidate in this owner state**, not an adopted theorem supplied by the four-gate parent. The results below are conditional on that displayed written proof being sound until a fresh whole joint gate settles it.
2. For the original FACT application only, the SAME actual quotient families derived in that packet §2 at the qualified F/F1 ordinary accepted-statement interface. No R2 LF58 shape or I4 assertion is used.
3. The complete NEW recursive necessity/sufficiency/termination proof HERE. A gate of108LF alone does not audit this new source or joint import union.

This is finite cyclic-group mathematics, not a raw coefficient/Taylor/parser/source-control reinterpretation. Lam1996's actual twelve-page source read is separately characterized; its ELEMENTARY no-wrap normal form is NOT a premise here. The cyclic wraparound case below is handled by actual subgroup cosets, not an assumed lift to integer no-wrap sums. No novelty/priority claim is made.

## 1. Input class and certificate definition

Let G=Z_n, n>=1, p prime, and alpha>=0. Let nonempty finite families `{S_i:i∈I}` and `{Y_j:j∈J}` consist of normalized subsets of G, with `|S_i|=p^alpha`. The numbers n,alpha,|I|,|J| are UNBOUNDED. The target property is

**(CT)** `S_i ⊕ Y_j=G` for EVERY i,j.

All cross-factorizations concern the SAME actual families; different branch pairs may not be assigned independent replacement complements.

Define a **synchronized certificate of exponent alpha** recursively.

**Leaf alpha=0.** Every S_i is{0} and every Y_j is ALL of G. G may be the trivial group. This is the entire leaf condition, not a placeholder.

**Node alpha>=1.** Choose a cyclic subgroup H of G of order h divisible by p^alpha, with ALL S_i contained in H. Then H is nontrivial and pH has index p in H. Write g=n/h and use the exact isomorphism

`eta:Z_(h/p) -> pH`, `eta(t)=g*p*t (mod n)`.

For EACH i and EACH residue r∈H/pH, choose a representative `a_(i,r)` of that residue, with `a_(i,0)=0`. For EACH j and EACH coset c∈G/H, choose `y_(j,c)∈c`, with `y_(j,H)=0`. There must be normalized child sets `S'_(i,r),Y'_(j,c)⊂G'=Z_(h/p)` satisfying

`S_i = disjoint_union_(r∈H/pH) (a_(i,r)+eta(S'_(i,r)))`,

`Y_j = disjoint_union_(c∈G/H) (y_(j,c)+eta(Y'_(j,c)))`.

The child S sets have cardinality p^(alpha−1). **ONE shared synchronized certificate of exponent alpha−1 must certify the ENTIRE child family** indexed by ALL(i,r) against the ENTIRE child family indexed by ALL(j,c) in G'. Separate certificates for selected pairings are NOT enough. Every parent representative and every coset fiber remains part of the data.

This is a complete finite recursive definition. Each node lowers alpha by ONE. The groups can change by subgroup restriction and quotient, but no unbounded same-alpha recursion is allowed.

## 2. The full characterization theorem

**Theorem SYNC. At J_sync, (CT) holds IFF such a synchronized certificate exists. In the necessity construction one may take H=⟨union_i S_i⟩ at EVERY node. Every certificate terminates after exactly alpha prime-branch stages.**

The statement quantifies ALL cyclic orders, normalized set families, arbitrary coset representatives and all actual cross-family factorization constraints; it does not presume an individual generating S_i or unit element.

### 2.1 Necessity: retain the entire collective subgroup and every outside coset

Assume CT and alpha>=1. Put `H=⟨union_i S_i⟩`, of order h. For fixed j and ANY c∈G/H, all targets in c can use only the Y_j fiber in c, because every S_i lies in H. Thus that fiber X_(j,c) is nonempty, and for any chosen point y_(j,c) in it,

`S_i ⊕ (X_(j,c)−y_(j,c)) = H` for EVERY i.

Cardinality gives `|X_(j,c)|=h/p^alpha`, so p^alpha divides h. This is an exact fiber statement for EACH c, not an average profile. Choose y_(j,H)=0, possible because Y_j is normalized.

The family of S_i collectively generates H by definition. Their cardinality is p^alpha, and EVERY normalized X_(j,c) is a common complement of EVERY S_i in H. Apply CF in the CYCLIC group H to this ENTIRE family. It yields

`X_(j,c)−y_(j,c) ⊂ pH` for EVERY j,c.

No proper-subgroup branch was discarded: a proper H in the original G is explicitly retained, with EVERY one of its outside cosets. CF is used only after H, not G, is actually generated by the family.

### 2.2 Necessity: all prime branches and all child cross-factorizations

Fix one normalized X fiber X0⊂pH. For each i and r∈H/pH, covering that residue by `S_i⊕X0=H` forces

`|S_i∩r|*|X0|=|pH|`, hence `|S_i∩r|=p^(alpha−1)`.

Thus EVERY prime residue is present with the required cardinality. Choose a_(i,r) from it and a_(i,0)=0. Define the ACTUAL normalized children by

`S'_(i,r)=eta^(-1)((S_i∩r)−a_(i,r))`,

`Y'_(j,c)=eta^(-1)(X_(j,c)−y_(j,c))`.

For EVERY(i,r),(j,c), the original tiling restricted to the relevant residue coset gives

`S'_(i,r) ⊕ Y'_(j,c)=G'`.

Indeed, in H a target with residue r has its S point necessarily in S_i∩r because the normalized X fiber lies in pH. Subtract its actual a_(i,r), pass through eta^(-1), and retain the unique representation. This proves whole coverage AND uniqueness for EACH child pair. It does not independently assemble different cuts/fibers.

By induction at alpha−1, these ENTIRE child families have ONE synchronized certificate. The node identities are exactly their definitions, establishing necessity. At alpha=0 normalization already forces S_i={0}, and CT forces Y_j=G. This proves the base as well.

### 2.3 Sufficiency: reconstruct one actual unique representation at EVERY node

Assume a certificate node and the induction hypothesis that its whole child certificate implies EVERY child cross-factorization. Fix arbitrary i,j and target z∈G.

First z determines a unique coset c of G/H. Since S_i⊂H, only the c-fiber of Y_j can contribute. Subtract its actual representative y_(j,c), obtaining a point of H. Its residue in H/pH determines the unique r, and hence the S branch a_(i,r)+eta(S'_(i,r)).

Now `z−y_(j,c)−a_(i,r)` lies in pH. Apply eta^(-1). The ENTIRE child property supplies a unique pair in `S'_(i,r)×Y'_(j,c)` with that sum. Mapping back supplies a representation of z by S_i+Y_j. Any second representation would have the SAME forced c and r and then contradict child uniqueness. Thus S_i⊕Y_j=G for EVERY i,j.

All unions in the node are genuinely disjoint, because S branches occupy different pH residues and Y fibers occupy different H cosets. The zero-representative rules retain normalization. Each parent S cardinality is p*p^(alpha−1)=p^alpha; the complement cardinality follows from actual child tilings. At a leaf the assertion is immediate. This proves sufficiency, not merely a necessary restriction. ∎

### 2.4 Termination and exact information retained

Alpha is a nonnegative integer and decreases once per node; after exactly alpha stages every S child is a singleton and every Y child is the full remaining cyclic group. Group orders, subgroup choices and expanding family indices can still be arbitrarily large. No uniform bound on n,alpha,code length or a scientific search cutoff follows.

The certificate is a SYNCHRONIZED family chain with branching indices, not permission to choose separate normal forms for different children. It retains all a_(i,r), all y_(j,c), every outside H coset, and the shared descendant families. Erasing those representatives would erase exactly the coupled data still needed in the original completion problem.

## 3. Exact application to the original FACT lift residual

In the actual108LF construction for q∈{5,11}, let N be the full2/q part of n, k=2q, and G0=Z_(N/k). The SAME actual A_N is equidistributed modulo k and EVERY actual B_y is in one k-coset. The normalized quotient sets T_r/Y_y therefore satisfy EVERY cross-tiling, with `|T_r|=|A|/(2q)`.

When `|A|=2^(gamma+1)q` or `|A|=2q^(gamma+1)`, gamma>=1, that size is respectively2^gamma or q^gamma. SYNC applies to the ENTIRE actual family with p=2 or p=q. It yields a full gamma-stage synchronized cyclic certificate, including the formerly open root proper-subgroup branch and all of its outside fibers. This strengthens a single root dichotomy to a COMPLETE iff representation of those quotient-family tilings, at J_sync.

No claim is made that the original Shor seed determines or contradicts these subgroup/representative data. The ordinary A generating Z_n does NOT force the within-class T_r to generate G0; the first subgroup may be proper. Neither the certificate nor the existence of binary branches supplies a global p-group action on the original completion, a closed tensor/code sector, or freedom to discard inter-fiber phases/carries. Such an action would need an actual definition and proof preserving all representatives; it is NOT inferred from the word tree.

Likewise the construction is on existing FACT lifts, not a new finite-code witness. It does not prove the other mates D2/D3 fit the same certificate or that every arbitrary-short-gap raw word is realizable. The q=3/7 cases are not widened to F1's all-fiber hypothesis. No new FACT cardinality, period, I4 proof, three-prime theorem, finite completion/noncompletion or rawSTAB follows.

## 4. Assurance and exact first unpaid step

The first unpaid original bridge is whether the coupled subgroup/representative families required here can coexist with the literal Shor one-b entries, the other common mates and ALL raw finite-code conditions, or whether those actual constraints force an obstruction. All orders, gamma, family counts, lengths, b-counts, arities, gaps, delays and memory remain unbounded. No concrete family/certificate parameter was selected, tried, computed or replayed.

CF and this NEW SYNC composition still need their exact full gates. The four-gate M/I3/generalB parent is an actual prospective accepted input, not an automatic review of CF, SYNC or their FACT application. Original I4 CARDINALITY-form proof remains NAMED_NOT_RECONSTRUCTED; Sands1979 GROUP ORDER is not substituted. Bare FACT660|n,n>=1320 NOT1320div; H*FALSE/WITHDRAWN; R2LF58 universal two28-coset shape NR/depth3/56 bridge missing/U1 not counterexample. All old FACT/rawPR/isolated/delay/STAB/597LF candidates and every process/unknown-runtime qualification remain.

Only conventional exact WRITTEN symbols/fractions/integer products were used, including private reasoning. **No identity was machine-checked.** No scientific interpreter/calculator/CAS/program/enum/solver/replay/build/test/modelCLI/nested agent/newGO, new chosen finite code/state/control/parameter/boundary/limit/magnitude/decimal viability probe, frozen edit, Git/deletion/publication, or global clean-provenance/cognition/runtime census. All seven majors/three provenance blockers/ZERO consuming guidance remain; new correct mathematics is not process rehabilitation. Same18/exclusiveOWN/HOLD/actual substantive checkpoints<=30min/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 unchanged. Not formal/kernel/configured-family/human/executable/novelty acceptance, an early park or96-hour closeout.
