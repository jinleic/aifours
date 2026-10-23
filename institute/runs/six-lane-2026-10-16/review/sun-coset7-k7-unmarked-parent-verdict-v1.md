# Sun k7: unmarked HIGH/CLASS/Q23U accepted

Recorded at 2026-10-18T15:16:05-07:00.

**CORRECTNESS-ACCEPTED:** the narrow P2 dependency, K7-HIGH, K7-CLASS and K7-Q23U, with the scope fixes below. In particular, when no vertex is marked, the Q23 family with at least two2-classes cannot occur. **K7 remains OPEN.** Its unmarked all-2 seven-singleton pattern and Q24 remain, as do unresolved marked Q23/Q24 cases.

## Evidence

- [Candidate](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/K7-unmarked-lemmas-v1.md), SHA256 `ca80d7e5884de3831e35c1fcd69214abaef0c74d18bdd4108937094f41a3f242`.
- [Codex](sun-coset7-k7-unmarked-codex-v1.note.md), SHA256 `f61b6cbba945b8ab4cdc8e70e193ba29704e97ffe17676b9b208e98f21ba0c96`: narrow P2/Q23U ACCEPT; HIGH/CLASS AWF with MINOR presentation fixes; all eight source hashes matched.
- [Claude](sun-coset7-k7-unmarked-claude-v1.note.md), SHA256 `028e88fd75463813f1797d44f1484fb2d8fa835a0c579380f2705c0d99da414f`: all four implications ACCEPT, no mathematical error; status section AWF with one MAJOR scope issue and four MINORs. Hashes not rechecked by Claude.
- [BLOCK/PAIR parent verdict](sun-coset7-k7-blockpair-parent-verdict-v1.md) independently accepts the complete repaired P2 and P3; [Q5+](sun-coset7-k7-q5plus-parent-verdict-v1.md) excludes Q5 at every marking count and controls the COV quantifiers. Those newer verdicts were not premises of the frozen unmarked review packet; both reviews independently proved the narrow P2 needed here.

## Exact statements and parent derivation

Use class K7 with n_i=6r_i, pairwise-coprime r_i, U unmarked and M marked.

1. **Narrow P2:** M=∅, Q23 with at least two2-classes implies every twin block is a singleton. The already accepted full P2 also handles the single-class case, by a separate repaired argument; do not attribute that extra branch to these narrow reviews.
2. **HIGH:** M=∅ and some vertex v with all six incident α_vj≥3 is impossible. Every admissible q_j lies in{1,2,3}, and d_j=q_jw_j gives gcd(d_i,d_j)=gcd(q_i,q_j). Allowed sets are singletons or pure q=2 subsets of size≤2 or pure q=3 subsets of size≤3. For each nonempty group set y_j=1/min(q_j,k_q); absent groups contribute0. This is feasible on every hereditary allowed set, and its group contribution k_q q/(6min(q,k_q))≥k_q/6. Summing gives≥1 for every q, contradicting strict VFC-count.
3. **CLASS:** M=∅, Q23 with at least two2-classes has no2-class of size2,3 or4. Take distinct j,k in such a class C. At every v outside C, triangle(2,3,3) gives τ_min=6 and product intersection measure≥1/2, equal to both product measures. Thus U_vU_j=U_vU_k. For fixed W=⟨U_j,U_k⟩, L6 gives m|6,m≤3,m/2 integral, so m=2 and U_v≤W for every outsider. L5 gives t∈{1,2},λ=3tw; pair gcds are3 except6 for two t=2 pieces. Each W-fibre holds at most three t=1 pieces by Sun(4). If|C|=2 there are seven such pieces in two fibres. If|C|=3, six fill both fibres and the remaining t=2 piece creates a forbidden four-set. If|C|=4, zero/one t=2 reduces to those cases; with two t=2, each fibre can contain at most two t=1 pieces, leaving capacity4 for five. All cases contradict disjointness.
4. **Q23U:** the singleton twin vertices partition into at least two2-classes with sizes in{1,5,6}. At least one class is a singleton, whose vertex has six incident α=3, contradicting HIGH.
5. **Q24 neighbour consequence, M=∅:** every vertex has a neighbour with α≤2. Otherwise HIGH applies. This is a necessary condition, not Q24 exclusion.

## Scope findings and their disposition

- **Claude MAJOR:** the original abbreviated status text omitted single-class Q23 and silently used the separate P3. Corrected: the all-2 single-class case remains OPEN. Its reduction to seven singleton twin blocks now follows from the separately accepted, repaired full P2 in the BLOCK/PAIR verdict—not from Q23U. No circular use.
- HIGH's reciprocal formulas apply only to nonempty groups; explicitly require M=∅. Choose distinct j,k in CLASS; t≤[G:W]=2 follows from the coset count. Keep triangle relaxation notation separate from local d_j.
- Q5 with M=∅ was already excluded and HIGH only reproves that subcase; do not label it unreviewed.
- The example q=(4,4,4,4,4,2) illustrates failure of VFC-count to refute one vertex. It is not an accepted exhaustive residual-q list, global feasible certificate, RPLP result or realizable configuration.
- Q24 restrictions from BLOCK/P3/HIGH have separate accepted sources. No enumeration, quotient-size count or final finite-coverage claim is accepted.
- L5/L6 as used were explicitly rederived; "frozen" alone was never their acceptance. These proofs use only Sun(2)–Sun(4) inside actual subgroups, no least-order frame or subgroup Sun(7). Generic FH execution remains unauthorized.

## Current K7 structural frontier

Q5 is excluded for actual configurations. If M=∅, Q23 with≥2classes is excluded and single-class Q23 reduces to the **seven-singleton all-2** pattern, still OPEN. Q24 stays OPEN with twin blocks≤2, at least three α=4 outsiders per twin pair, and an α≤2 neighbour at every vertex. If M≠∅, blocks≥4 are excluded, but size3 blocks and remaining Q23/Q24 marked incidences need further work. No claim that every marked configuration remains feasible.

Written mathematics only; no new computations, Lean, human review or novelty determination. K6.2*,K6.3 and the pending StageA/K5.3 disposition are unaffected.
