# In-harness written reconstruction: Olson selected-K gauge and critical ladder

Observed before creation: **2026-10-23T14:19:43-0700 PDT**. Reviewer: **MathShor**, primary slot math-5; this is the single bounded review assigned in `peer-review-wave-eighteen-v1.json`, not a reviewer-only scientific slot. No scientific executable, parameter test, solver, kernel or independent-model CLI was run.

## Verdict and exact pin

**No FATAL, MAJOR or substantive MINOR defect found at the explicit scopes reviewed.** The gauge identity, switch lemmas, matching obstruction, critical ladder and original-cut restoration reconstruct correctly for every stated prime p≥7 and every actual selected even K. The manuscript remains **CANDIDATE partial mathematics**, not full MIX, whole R=p+1 coverage, unrestricted prime-dihedral Olson, all finite groups, strict new provider coverage, novelty, or formal proof.

Complete author source read: `mathematics/evidence/three-area-20261023-96h/parallel-18/ordered-olson/proof-GAUGE-SWITCH-AND-CRITICAL-LADDER-v1.md`, all 257 lines. Independently observed SHA256:

    cfc59821268165483319fdbc69f01c5f626904b3332f13076e33f97dc29c9f75

This exactly matches the rotation assignment. The exact `selection-v1.md` and complete `selection-addendum-1-gauge-and-prior-arcs.md` were read. The prior ARC/ETA file was read in full, all 161 lines; SHA256 `667e4373eb4854bd4c085127ff970ca066cca998b0712e7bc1690614a8bdf4ed`. For the old B1 interface I read the lower-band manuscript sections 1–3 and 7–8, and its complete parent written check/sign-frame qualification, not the entire transitive OLD dependency graph. Their observed hashes are respectively `80d43628cd3f1773a8cd5826be436259ab843bd4147b07164796b53794d55c3f` and `a732ea4a88cef2666754f2c07664994fc8175e31f079362ab4afa3af81eeb292`.

## Independent reconstruction of the load-bearing arguments

### 1. Gauge identity respects original order (author lines 24–50)

Write the rotation sums between the selected reflections as u_0,…,u_C, and t_n=u_0+…+u_(n-1). The telescoping product of conjugated reflections followed by rho_S gives exactly the original selected word, because every adjacent factor contributes rho_(-t_n)rho_(t_(n+1))=rho_(u_n). Direct multiplication in the displayed group law gives

    rho_t sigma_y rho_(-t)=sigma_(y+2t).

For even C, the reflection product has exponent z_1-z_2+…-z_C, and its parity is +1, so appending rho_S adds S rather than -S. For the two-reflection case this expands to u_0-u_1+u_2+y_1-y_2, matching the direct original-order product symbolically. This is an algebraic reconstruction, not an executed point test.

Only selected rotations enter t_n. No step commutes actual selected terms, removes a zero-valued rotation, or assumes a common nonzero opposite pair. A selected rotation inside a binary reflection packet changes the two endpoint gauges differently, which is precisely why straddling is allowed after gauging.

### 2. Binary growth and the exact p-2 inverse (lines 56–81)

A nonempty proper subset invariant under a nonzero translation in F_p would contain the whole translation orbit, hence all F_p. Thus each nonzero binary increment raises a proper sumset's size by at least one.

If two increments a,b are not equal up to sign, their four subsums are distinct. With t=p-2 increments, the other p-4 switches then grow four residues to all p. Conversely, when all increments are ±d, writing m negative signs translates the ordinary interval of subset counts to

    -md+{0,…,p-2}d,

which misses exactly -(m+1)d. Thus zero is absent from B+U exactly when B=(m+1)d. The sign reversal d↦-d changes m to p-2-m and leaves this critical offset unchanged modulo p. This proves both directions, including the missing residue; it is stronger than a cardinality-only bound but elementary classical additive reasoning, not novelty certification.

### 3. Packets produce actual size-2p selections (lines 85–113)

Choosing one reflection per ordered packet preserves packet order for every endpoint choice. Each binary choice changes only that packet's signed gauge contribution. The baseline B and increments in (5) therefore describe the actual option set, not an unordered shadow. Adding fixed K gives exactly k+C=2p positions and even reflection parity.

The three GS cases follow respectively from p-1 growth, the non-± critical inverse, and avoidance of its unique missing scalar. The converse at lines 110–111 is correctly restricted to this packet family.

### 4. Adjacent matchings and odd components (lines 117–153)

For an actual even k between 2 and p+1, p-1 adjacent unequal-gauge pairs use 2p-2 reflection occurrences, leaving exactly p available outside them. The required singleton count is p+1-k, which is nonnegative and at most p-1. Adjacency is in the reflection subsequence; hence no chosen outside reflection can lie inside a pair, even though selected rotations may lie there. This constructs the required noncrossing packets.

If no GS selection is available, every such K must have matching number at most p-2. A path component of L vertices has matching number floor(L/2); summing yields nu=(F-o)/2. At F=3p-2, nu≤p-2 is exactly o≥p+2. Both F and o are odd, so the next larger branch is o≥p+4. The zero-edge count follows from components=zero-edges+1≥o.

For a critical matching of p-2 pairs, the number of remaining singleton slots is p+2-k and the number of outside occurrences is p+2, so every stated filler choice is admissible. Changing filler positions changes the signs and baseline, but the manuscript explicitly quantifies over every resulting signed system. It does not fix signs before choosing filler occurrences. Equation (9) includes exactly the selected rotation values between consecutive actual reflections.

### 5. Critical-ladder recurrence and empty gaps (lines 157–207)

Put s=(-1)^(j-1) when the singleton advances past pair j. That pair's sign changes from -s to s, so

    ΔP=2s z_(a_j),       Δm=-s epsilon_j.

For C_j=S+P_j-(m_j+1)d this gives

    C_j-C_(j-1)=s(2z_(a_j)+epsilon_j d)
               =s(z_(a_j)+z_(b_j)).

The initial value is C_0=-A_0. If C_(j-1)=(-1)^j A_(j-1), the displayed increment yields C_j=(-1)^(j+1)A_j with exactly the author's recurrence. Hence the missing option scalar is

    M_j(u)=(-1)^j(z_u-A_j).

Zero is absent precisely when the singleton gauge equals its gap's A_j. Quantifying over all actual unpaired occurrences proves the claimed iff for this matching family. Empty gaps only transport virtual recurrence values and impose no fictitious occurrence constraint. Every selection in this family uses p+1 rotations and p-1 reflections.

### 6. The all-rotation counterexample is correctly scoped (lines 211–233)

The explicit w_p has p+1 rotations, 3p-2 reflections and total length 4p-1. Its total rotation sum is p+2=2 modulo p. Gauging all rotations gives 2p-3 zero labels followed by p+1 one labels: the labels 1-2i in the displayed product have prefix rotation sum i, and the final -3 label has prefix sum p+2.

An even reflection subsequence has alternating gauge sum 0 or -1 according as its number of ones is even or odd; with S=2 its total exponent is 2 or 1. Thus the all-rotation branch really fails for every choice in that branch.

The proposed reflection-only selection exists in the original order because i=(p+3)/2 is an integer in [2,p], and its corresponding reflection label is a=-2. Its product is

    sigma_a sigma_(a+1) sigma_a sigma_(a-1)=rho_0.

It has exactly 2p reflections. Hence w_p is already REF-covered, as stated; it proves no B1/B2 nonemptiness and is not an Olson counterexample. The p+2 cyclic constant blocks are indeed odd: one has length 2p-3, all the others are singletons, with unequal cyclic neighbors. The highest reflection multiplicity is 2p-2, so this is not the older 2p-1 equal-reflection insertion family.

For a cut AB↦BA, identity P_B P_A=1 implies P_A P_B=1 by conjugation. This restores the same actual indices, not a rearranged selection. Gauges are correctly recalculated for each cut.

## Historical overlap and boundary audit

Historical `proof-REFLHI-arcs-v2.md` lines 54–81 already vary actual reflection arcs and invoke additive sumset growth in its restricted setting. Its lines 130–144 already use prefix-mass eta labels. Therefore the mechanism “gauge reflections and vary ordered packets” is prior internal baseline, as the current manuscript expressly acknowledges at lines 18–20.

The current selected-K identity removes the historical common nonzero rotation-pair/all-odd restrictions and allows selected rotations inside packet spans. Its p-2 inverse/missing-residue and explicit recurrence are fully supplied here. This establishes what is proved in the packet, **not** that a strict new B1 word class outside all historical providers has been exhibited or that no source already contains these elementary extensions.

The B1/B2 definitions retain their old provider trust. The new self-contained GS/OM/CL implications do not require S(p), Lev, EGZ, Theorem P or IPGEN as mathematical premises; old residual comparisons still do. I have not certified the whole transitive OLD graph or the universal availability of any packet. The manuscript's lines 249–255 correctly leave the first universal MIX existence implication unproved, including the deeper o≥p+4 branch and simultaneous profiles over all K/cuts.

## Findings and disposition

- **FATAL:** none at the stated written boundary.
- **MAJOR:** none at the stated written boundary.
- **MINOR:** none requiring repair for the scoped statements.
- **Scope:** route/selection criteria plus necessary critical profiles only. Not full-band or full-book acceptance.
- **Novelty/significance:** unresolved; ARC/ETA and elementary additive growth are explicit baselines. No strict independent coverage count is supported.
- **Verification level:** actual in-harness reconstruction by a separate task agent using the supplied pinned author proof. Shared input, not blind, cross-vendor, human or kernel verification. Parent review remains separate.

I now resume the raw-word finite-realization obligation of my own Shor primary slot.
