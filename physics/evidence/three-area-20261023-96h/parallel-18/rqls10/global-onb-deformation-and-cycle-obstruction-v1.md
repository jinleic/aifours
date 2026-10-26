# Global ONB deformation theorem: complete local coordinates, rigidity and the actual mixed-pair obstruction

**PhysicsRQLS10-2 / physics-5.** Actual pre-write `/bin/date`: **Sun Oct 25 09:24:35 PDT 2026**. **NEW WRITTEN RESULT WITHIN THIS DOSSIER; independent reconstruction and novelty clearance NOT performed.** No scientific interpreter/eval/program, enumeration, symbolic program, solver, certificate replay or native scientific launch was used. Source reads, written mathematics and metadata hashes/clocks only.

This is ONE consolidated successor under the0853 primary continuation. The registered target remains an unrestricted maximal1-RQLS10:100 pairwise nonparallel complex rays with all row, column and resolution-transversal ONBs. **No such100-ray witness or unrestricted impossibility is claimed here.** The completed result is a global classical-seed deformation/rigidity theorem, with an EXACT nonlinear residual system and its full second-order criterion. It is not another fixed-Paley-core case closure.

## 1. Why this is a new route, and its exact limit

The earlier RT problem remains open/unaccepted at its literal fixed-C/rho scope. The earlier236/52 data remain unadmitted/unreconstructed; none is a premise here. The current genuine-family analytic packet also retains its exact R0/R1/R2 gaps. Repeating those cases is not proposed.

Likewise `candidate-PROJECTOR-INVARIANT-v1.md` ALREADY contains the all-object incidence kernel,425/2 fourth-moment defect, universal feasible H0 and missing rank-one lift. Those are baselines, not new results of this note. No larger PSD/Gram feasibility claim is substituted for a vector construction.

The present input is instead a WHOLE resolved classical seed: an orthogonal Latin pair(L,M), with M labeling the complete transversal resolution and L labeling a computational-basis seed. Every row, every column and every M-symbol fiber is kept as an exact ONB context simultaneously. Only a common unitary and harmless independent ray phases normalize the first row. There is no fixed conference C, rho, first-column overlap, uniform H0 magnitude or field-valued physical phase assumption.

The new mechanism was frozen in `global-onb-route-freeze-v1.json` before choosing or arithmetically testing any concrete order10 seed or ray parameters. Preliminary written route reasoning was disclosed; no preregistration of the idea is claimed. That record also additively consumes parent v10, which was read before this new theorem/checkpoint and is NOT represented as part of the original0853 contract or old packets. V1–v9 and HOLD remain binding.

This route does NOT assume every nonclassical solution is connected to a classical seed. Local rigidity of a seed is therefore not a global no-go. The exact final100-ray construction gap, including this possibility, is stated in Section10.

## 2. Complete global input and legitimate normalization

Let n>=3, and let L and M be orthogonal classical Latin squares of order n. A context is one of the n rows, n columns or n M-symbol fibers. Every context contains exactly one cell of each L-symbol: for the first two partitions this is Latinity of L, and for the third it is orthogonality of L,M.

Assign a ray [q_c] in C^n to every cell c. Requiring the n rays in EVERY context to be an ONB is EXACTLY the resolved quantum problem with this specified resolution M. Conversely every1-resolvable QLS has such a classical M: label each of its disjoint transversals by one symbol; each label occurs once in every row and column. This is the source's transversal/classical-mate equivalence, not a new restrictive ansatz.

The classical seed is `q_c^0=e_(L(c))`. Its first row contains each computational ray once. Near the seed, a common unitary sends the first-row ONB to these same ordered computational rays. Choosing individual phases fixes the leading coefficient at each cell to be positive real. Thus every nearby normalized ray has the UNIQUE chart

    q_c(z)=[e_a+sum_(k!=a) z_(c,k)e_k]
             /sqrt(1+sum_(k!=a)|z_(c,k)|²), a=L(c),
    z_(c,a)=0, and z_(c,k)=0 for first-row cells.

All z coordinates are otherwise arbitrary complex numbers. The chart removes per-ray phases, not physically distinct complex directions. A residual diagonal common-unitary stabilizer may act on these coordinates; no smooth quotient-moduli dimension is inferred from the tangent count below.

Because the displayed denominators are positive, orthogonality for two context cells c,d of distinct seed symbols a,b is EXACTLY the quadratic equation

    z_(d,a)+conjugate(z_(c,b))
      +sum_(k!=a,b) conjugate(z_(c,k))*z_(d,k)=0.       (O)

There is no truncated orthogonality approximation in(O). Unit lengths are already imposed by the chart, and n orthogonal unit vectors in C^n form an ONB. Hence all(O) are sufficient as well as necessary for the whole3n-context design in this chart.

## 3. The three-matchings graphs — genuine incidence, no profile census

For each unordered pair of seed symbols a<b, define Gamma_ab on the2n cells whose L-symbol is a or b. Connect the a-cell to the b-cell in each row, each column and each M-symbol fiber. These are THREE perfect matchings.

Their edges are distinct. An a/b cell pair cannot share both row and column, since it would be one cell; sharing row and M-symbol or column and M-symbol contradicts Latinity of M. Thus Gamma_ab is a SIMPLE3-regular bipartite graph, with n vertices of each symbol.

Each connected component has the same number k of a- and b-vertices by counting its3k edges on either side. Simplicity gives k>=3. If c_ab denotes its number of components,

    c_ab<=floor(n/3).

This is a proved all-input graph bound, not an enumeration of Latin pairs. The two first-row vertices are joined by their row edge and belong to one distinguished component C_ab^0.

## 4. Theorem A — the ENTIRE normalized infinitesimal space

For a first-order direction x_(c,k), write the chart coordinates as z=t x+O(t²), with t real. Define one node variable on Gamma_ab by

    w_ab(c)=x_(c,b)                 when L(c)=a,
    w_ab(d)=−conjugate(x_(d,a))     when L(d)=b.

Then the FULL first-order ONB system is equivalent to:

    w_ab is constant on EVERY component of Gamma_ab;
    that constant is0 on C_ab^0.                       (T1)

There are no other linearized constraints. In particular the first-row-fixed ray-chart Jacobian kernel has real dimension

    2 sum_(a<b)(c_ab−1).                               (Tdim)

**Proof.** The linear coefficient of(O) is `x_(d,a)+conjugate(x_(c,b))`. Its vanishing says precisely w_ab(c)=w_ab(d) on the corresponding matching edge. Every context contains each symbol once, so these are exactly all linearized constraints for that unordered symbol pair. Connectedness propagates equality; different symbol pairs involve disjoint off-diagonal coordinates.

First-row normalization sets both endpoints of its a/b row edge to zero, hence the constant is zero on that whole component. Every other component carries one arbitrary complex value. Conversely any such collection reconstructs all x coordinates and satisfies every linearized edge equation. This proves both completeness and the stated REAL dimension. QED.

Tdim is a transverse/Jacobian-kernel statement, NOT a claim that every tangent vector integrates or that the singular quotient moduli space has this dimension.

## 5. Theorem B — exact local rigidity criterion and exact nonclassical escape

For the fixed resolved seed(L,M), the following are equivalent:

1. Every Gamma_ab is connected.
2. The normalized seed is isolated among nearby resolved quantum arrays with this SAME resolution.
3. Some neighborhood of the seed contains only its common-unitary/per-ray-phase classical equivalents with this resolution.

If any Gamma_ab is disconnected, there is an explicit arbitrarily small EXACT nonclassical deformation preserving ALL3n ONBs, not merely a formal tangent.

### 5.1 Connected graphs imply genuine local rigidity

Collect the real and imaginary parts of all(O) in a real-analytic constraint map F. By Theorem A its derivative at zero is injective when all graphs are connected. On a finite-dimensional real unit sphere, injectivity gives a constant c>0 with `|DF(0)z|>=c|z|`. Differentiability gives `F(z)=DF(0)z+o(|z|)`. In a sufficiently small ball the remainder has norm at most c|z|/2, so F(z) cannot vanish for nonzero z.

Thus the normalized seed is genuinely isolated, not just free of curves with a nonzero first derivative. No numerical singular-value calculation, regularity assumption for the full overdetermined equation list, or unsupported “infinitesimal implies rigid” step is used. Undoing the legitimate first-row normalization gives the stated equivalence-class conclusion.

### 5.2 Disconnected graphs give an explicit exact escape

Choose a component C of Gamma_ab other than C_ab^0. For any complex parameter u, replace its a- and b-cells respectively by

    q_a(u)=(e_a+u e_b)/sqrt(1+|u|²),
    q_b(u)=(−conjugate(u)e_a+e_b)/sqrt(1+|u|²),

and leave all other cells at their seed rays. The two displayed vectors are orthonormal. A context has either BOTH its a/b cells in C or neither, because their matching edge lies entirely in one component. Its other n−2 rays lie in the orthogonal complement of span(e_a,e_b). Therefore every context remains an exact ONB. The first row is untouched.

For u nonzero and finite, both new rays differ from all computational rays and from each other. A proper component leaves occurrences of BOTH a,b outside it. Thus the whole array has exactly n+2 distinct rays, and tends to the classical seed as u tends to zero. This proves nonclassical local escape, hence the converse of rigidity. It is not maximal cardinality.

More generally every component of ONE Gamma_ab may receive its own such2-dimensional basis, with the distinguished component fixed. These are known-type unitary switches, not a claim of priority for the elementary switching mechanism. Their role here is to prove the complete converse to the local criterion.

### 5.3 The resolution itself is not silently fixed in a negative conclusion

For a classical L with at least one classical mate, nonclassical1-resolvable arrays occur arbitrarily near its seed IF AND ONLY IF there exists SOME classical mate M for which some Gamma_ab is disconnected.

The positive direction is Section5.2. For the negative direction, there are finitely many Latin resolution patterns M. A non-mate has two equal L-symbols in one M-fiber; their seed inner product is1, so that pattern cannot support nearby ONBs. Every mate with all graphs connected has its rigidity neighborhood from Section5.1. Intersecting these finitely many neighborhoods proves the claim for ALL possible resolutions near L. This is a finite logical argument, not an executed census or a claim that any order10 mate set has been enumerated.

## 6. Theorem C — EXACT nonlinear graph reduction, not only tangent data

The next result retains mixed-symbol interactions that independent switching would lose.

For arbitrary chart coordinates z, define w_ab on Gamma_ab by the SAME sign/conjugation convention as in Section4. This is a real-linear bijection between all off-diagonal chart coordinates and all graph-node variables, with the first-row graph nodes fixed to zero. Conversely,

    z_(c,k)=w_(a,k)(c)                     if a=L(c)<k,
    z_(c,k)=−conjugate(w_(k,a)(c))          if k<a.

Orient an edge e=(c,d) from its a-vertex to its b-vertex and define the homogeneous REAL-quadratic edge function

    R_e(z)=−sum_(k!=a,b) z_(c,k)*conjugate(z_(d,k)).

Conjugating(O) proves the EXACT equivalence

    w_ab(c)−w_ab(d)=R_e(z).                          (N)

All complex phases remain present. R_e involves other symbol pairs but is not dropped merely because a/b-only switches have zero mixed term.

### 6.1 Complete tree elimination

For each Gamma_ab choose a spanning tree in its distinguished component CONTAINING the first-row row edge e0. Delete e0: the result is a two-root forest, rooted at its two first-row nodes, both fixed at zero. In each other component choose one root and a spanning tree. The complex root values u_(ab,C), C!=C_ab^0, are free parameters.

Keep equation(N) on these forest/tree edges. The first-row edge e0 is identically satisfied: both endpoint coordinates and all their mixed products vanish. All other edges are retained as chord constraints.

The Jacobian of the kept tree equations with respect to the non-root node variables is invertible at zero. Indeed its linear part is precisely an oriented tree incidence map with root values prescribed; ordering leaves gives a triangular elimination with diagonal entries±1. Across symbol pairs these linear blocks are independent. The quadratic right sides have zero derivative at zero.

The real-analytic implicit function theorem therefore gives a UNIQUE small real-analytic assignment

    z=Z(u), Z(0)=0,

solving every tree equation, with the specified root values. Analyticity here is in real and imaginary parts; holomorphic dependence is NOT claimed because conjugates occur. This is a classical finite-dimensional analytic theorem with its invertible-Jacobian hypothesis explicitly verified, not an interpreter solve.

For every omitted chord define its actual residual

    Omega_e(u)=w_ab(c;Z(u))−w_ab(d;Z(u))−R_e(Z(u)).

Then, in a sufficiently small neighborhood,

    ALL row/column/M-fiber ONBs
      iff u is small AND every Omega_e(u)=0.            (EXACT)

Every nearby normalized solution is represented uniquely this way, because its root values determine the unique tree solution. Conversely a zero of all residuals satisfies every edge equation and hence all original ONBs after normalization. No chord is omitted or called redundant without the identically-zero first-row argument. The residuals need not be independent; no dimension of their common zero locus is asserted.

Thus this is an EXACT analytic reduction of the complete global ONB system, not a magnitude relaxation, truncated formal series or claim that every free root vector is realizable.

### 6.2 Complete second-order obstruction

Let x satisfy Theorem A. Seek a second-order ray-chart jet

    z(t)=t x+t² y+O(t³).

The coefficient of t² in(N) is

    w_y(c)−w_y(d)=−sum_(k!=a,b) x_(c,k)*conjugate(x_(d,k))
                 =:R_e(x).                            (J2)

For EVERY Gamma_ab this has a solution y if and only if the oriented sum of R_e(x) is zero around EVERY cycle (equivalently around a full set of fundamental cycles): traverse an a-to-b edge positively and the reverse negatively. Necessity is telescoping of the potential w_y. Sufficiency follows by path integration from a root; vanishing cycle sums makes it path-independent. In the distinguished component the first-row edge has R_e(x)=0, so both prescribed first-row values can simultaneously be zero. Other component roots are freely chosen.

Norms impose no extra equation: the projective chart normalizes each ray exactly. Its diagonal normalization term never changes the off-diagonal numerator equations(O). Hence (J2) is NECESSARY AND SUFFICIENT for all3n ONBs THROUGH second order, with every mixed complex interaction retained.

This is a jet criterion, not an actual finite-t witness. In the exact reduction the Omega_e have zero constant and first derivatives; their quadratic obstructions are precisely these cycle circulations after tree elimination. Higher orders are contained in the EXACT residuals, not assumed to vanish because the quadratic conditions pass.

## 7. Theorem D — a complete FIRST-ORDER ray-separation criterion

For a fixed classical symbol a, give each of its occurrence cells c its component signature

    Sig_a(c)=(component of c in Gamma_ab)_(b!=a).

A tangent direction can distinguish ALL repeated occurrence rays at FIRST ORDER if and only if every Sig_a is injective.

If two same-symbol cells have identical signatures, Theorem A forces every off-diagonal first-order coordinate to agree, so they cannot split at that order. Conversely, if all signatures are injective, choose DISTINCT complex constants on the components of each Gamma_ab, using zero on its distinguished component and nonzero distinct values elsewhere. For any two a-cells, some b-component differs and hence their b-coordinate differs (or its negative conjugate differs when the symbol ordering reverses). This supplies a single tangent vector separating all repeated pairs simultaneously. No claim of second-order or actual integration is made by this choice.

If there is an ACTUAL analytic curve u(t) in the exact zero set Omega=0 whose induced first derivative is separating, then its normalized arrays have all n² rays pairwise nonparallel for every sufficiently small nonzero t. Different seed symbols already have distinct limiting rays. Same-symbol chart coordinates differ by a nonzero first-order term, so their difference is nonzero for small t; the finite number of pairs allows one common punctured interval. This is a rigorous sufficient extraction rule for a maximal-cardinality family, not a proof such a curve exists for n10.

Failure of first-order injectivity alone does NOT rule out higher-order separation or a nonclassical component disconnected from every classical seed. Those alternatives remain in the unrestricted primary.

## 8. What the exact switches can and cannot achieve at n10

The graphs are simple3-regular bipartite, so each component uses at least three occurrences of each symbol. For n10, c_ab<=3. If independently switching ONLY one pair, each component supplies at most two rays in its fixed2-dimensional span; all other n−2 computational rays stay unchanged. Thus its cardinality is at most

    n−2+2c_ab <=14 at n10.

A single proper-component switch gives12, not100. If several DISJOINT symbol pairs are switched, the same argument gives at most `n−2k+2sum c_ab` for k disjoint pairs. At n10 this is at most `10+4k<=30`. These bounds apply to those exact elementary switches, not to general solutions of the mixed residual system.

Therefore merely composing independent disjoint2-dimensional controls cannot reach the primary acceptance criterion. A maximal construction by this route must genuinely handle OVERLAPPING symbol-pair interactions (or leave this local mechanism entirely). The cycle terms in(N)/(J2), rather than an independently chosen list of pair angles, are the actual coupling that has to be solved.

These are symbolic all-input graph bounds. No finite seed/profile census, Herm14 table or order10 component list has been executed or declared exhausted.

## 9. Sources, priority boundaries and normalization scope

The original target definition and classical-mate equivalence are read in Zhang–Cao, [arXiv:2608.29201v2](https://arxiv.org/html/2608.29201v2), local extracted source LF86–165. Its Theorem1.2 explicitly lists10 among the unresolved exceptional orders. Local source SHA256 is `007602beff6de09a2643a55494b29f765e986f217d22c99fcb2e9cec4e5bbdd6`. This is the round's source boundary, not a proof of current openness from a search miss.

A bounded related-work read also covered Musto–Vicary, [arXiv:1804.04042v3](https://arxiv.org/html/1804.04042v3), Definition4, Example5 and Definitions11/Lemma12 on orthogonality, unitary modifications and equivalence. Basic unitary switching is established framework; no priority is claimed for it. The whole article was not read or novelty-audited here.

A newer bounded source read covered Lv–Zhang–Cao, [arXiv:2609.29070v1](https://arxiv.org/html/2609.29070v1), Theorem1.2 and Construction2.8 plus the beginning of Construction3.1. Its two stated order families do not supply order10, and a pair with BOTH members maximally nonclassical is not automatically a pair with a CLASSICAL mate/resolution. No whole-literature/current-status clearance follows from this bounded check.

The written tangent, local-rigidity, exact tree reduction and second-order cycle criteria are new results within this dossier, derived in full above. Whether an equivalent formulation is known elsewhere is UNCLEAR. The only named analytic import is the ordinary real-analytic implicit function theorem at its explicitly invertible tree Jacobian; no proof-assistant or configured-family gate is claimed.

The chosen first-row normalization is valid for EVERY actual ONB array near the seed and leaves all other amplitudes/supports arbitrary. The route is outside the fixed-C/rho ansatz: it permits highly nonuniform overlaps, variable support patterns and every resolution pattern. It nevertheless is not WLOG that every maximal array lies in one of these classical-seed neighborhoods. Negative local conclusions never close the unrestricted problem.

## 10. Exact first unproved step and current primary state

The completed theorem is the full global local-deformation structure above, including EXACT nonlinear equivalence and the complete second-order criterion. The first concrete construction step still unproved is:

> Provide an actual order10 orthogonal Latin seed(L,M) and root parameters/analytic curve u(t) satisfying EVERY exact Omega_e=0, with its reconstructed rays separating every repeated occurrence (at first or higher order), or produce a genuinely nonclassical global component directly. The component signatures alone, a tangent vector, a second-order jet or an implicit parameter count does not supply this.

No literal order10 seed table or nonzero mixed root vector is claimed to have been evaluated here. In particular no actual100-ray family, full rank-one Gram lift or complete RT obstruction is supplied. To prove a global no-go instead, one would have to cover ALL resolutions and ALL nonclassical components, not only classical-seed germs.

This is not indefinite parking after a gate: the old route was explicitly recognized as stalled at its real missing identities; a different exact global mechanism was frozen; the complete local/second-order theorem has been proved; and its precise nonlinear construction bottleneck is now exposed. The next mathematical work is to solve that bottleneck, not repeat the known projector relaxation or already-closed conference families.

### Current immutable/evidence bindings

- Route freeze: `global-onb-route-freeze-v1.json`, SHA256 `ef124028be32d86e37c73cd3236b11f05d3cc63ceaa06b6c5a9c8239485e33f0`.
- Prior projector baseline, NOT new progress: `candidate-PROJECTOR-INVARIANT-v1.md`, SHA256 `032a900df29722b71e8806524291e665cb16331c359b5538c7db957958d57ad9`.
- Prior exact Gram protocol, still without a witness: `candidate-GRAM-CERT-v1.md`, SHA256 `34e0b24211496c503cab5d0d0f6e774a4c995deb8deed2365cfb7a00a84ddb21`.
- Additive v10, read completely LF1–31 before this claim: SHA256 `d61acbf77fefa3a8d55d0cf74e9ebe0b680edb28d273f5b22255d09cbd66aa62`. Its Olson chronology/formula-href correction does not alter this mathematical scope and is not inserted retroactively into the0853 contract or older proof packets.

Unrestricted maximal1-RQLS10 and all-P RT remain unproved/unaccepted. No independent reconstruction, formal/kernel/human/cross-vendor, executable-certificate, novelty or publication acceptance is claimed. Earlier unadmitted computations stay disclosed with zero retroactive credit. No new scientific GO or change of original cutoff/deadline follows.
