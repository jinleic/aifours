**COMPLETE-COMPOSITION ACCEPT-WITH-FIXES.**

**Yes:** the accepted imports, supplied observed finite verification, and audited mathematical bridge establish the stated Sun(6) result for **every group**, with possibly equal subgroups and no cover hypothesis. I found one **MAJOR checker reporting defect** that does not invalidate the supplied completed replay, plus a documentation clarification. General acceptance of the checker as fail-closed requires the fix below.

All 22 snapshot files match their supplied SHA-256 hashes. My work used static reads and hashes within the snapshot only. I executed no interpreter, checker, tests or network requests, made no writes, and used no delegation.

- **MAJOR — [SOURCE08:L1141–1143](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset6-composition-final-v1-review-v1/snapshot/08-primary-checker.py:1141), SOURCE08:L1203–1213: an incomplete witness replay can produce PASS.** The deadline branch increments `rs["incomplete"]` and skips the certificate, but does not append to `rep["incomplete"]`. Final verdict selection consults only the global failure and incomplete lists. Its bookkeeping check allows incomplete certificates because `verified + failed + incomplete == lines`.

  A concrete counterexample is a deadline expiring immediately after the last universe/coverage check: all subsequent witnesses can be skipped, while the final verdict remains PASS. This is a static control-flow counterexample, not an executed experiment.

  **Fix:** record each skipped witness globally and require, independently at verdict selection, `verified == total_lines`, `failed == 0`, and `incomplete == 0`. Add a regression that expires the clock after coverage and before witness checking; it must return INCOMPLETE with a nonzero exit status. Preserve this frozen checker and publish the correction as a new version.

  **Effect here:** SOURCE11:L1073–1083 explicitly records 61,124 verified witnesses, zero failed, and zero incomplete. Its recorded runtime is 57.4 seconds against a 3,300-second budget. Those stronger completion facts exclude this defective path; acceptance does not rest on the word PASS alone.

- **MINOR, documentation only — SOURCE02:L83–88:** describe `code` explicitly as an informational engine label without a typed-orbit guarantee. The observed fields generally are not representatives of their line’s typed stabilizer orbit. The existing instruction to compute coverage independently from `rep` is correct and is implemented.

**No FATAL defect or unresolved MAJOR mathematical gap remains.**

I independently audited the reductions, rule implications, saturation arguments, closure, checker implementation and supplied control code. I import Zhu’s Sun(3/4), the accepted Sun(5) verdict, and the actual successful finite evaluations recorded in SOURCE10–12. I have not independently rerun either the k5 or k6 computations.

R0 preserves the exact target. Each finite-index subgroup has a finite-index normal core, and the intersection \(N\) of the six cores is normal, finite-index, and contained in every subgroup. Each original coset is the full inverse image of its quotient coset. Thus quotienting by \(N\) preserves subgroup indices, coset disjointness and the relevant intersections. Infinite groups therefore introduce no additional case. No normality of the original subgroups is assumed. SOURCE07:L23; SOURCE14:L41–45.

R1 is sound group by group. Suppose all fifteen pairwise gcds are at most five. Coprime indices cannot support disjoint cosets, so each gcd belongs to \(\{2,3,4,5\}\). Define \(A_p=\{i:p\mid n_i\}\), for \(p=2,3,5\). Every pair belongs to exactly one such clique: sharing two different primes would make its gcd at least six. Consequently distinct cliques intersect in at most one vertex and
\[
\sum_{p=2,3,5}\binom{|A_p|}{2}=15.
\]
If every clique has at most five vertices, the only possible three summands are \(6+6+3\), requiring sizes \(4,4,3\). Two four-sets intersecting in at most one point require at least seven vertices. Therefore some prime divides all six indices. SOURCE07:L31–43.

For common prime two, every pairwise gcd is two or four; for common prime three, every gcd is three. **Any five cosets contradict the accepted Sun(5) statement in either branch.** This shortcut avoids needing Prop 4.5 separately in this composition. The original Zhu/Prop 4.5 branches are also consistent with the accepted repaired text. For common prime five, every gcd is exactly five, so \(n_i=5r_i\) with pairwise coprime positive \(r_i\). This is precisely Core5(6).

The dependency substitution is explicit. SOURCE20:L33,L46–47 freezes a proof-v3 dependency. SOURCE01:L35 and SOURCE00:L12 discharge it through the accepted parent verdict, hash `2cf02436…`, which binds proof-v4 and its cumulative erratum. Those hashes match SOURCE14 and SOURCE16. The frozen contract has not silently been amended. SOURCE13:L8–15,L33–35 supplies the required full-group Sun(5) acceptance.

The minimal-counterexample frame is correct. After R0, choose a finite counterexample of least order to the **full Sun(6) statement**. Group-by-group R1 supplies Core5(6) in that same group. Every proper subgroup then satisfies Sun(6). FH5 constructs an index-five subgroup \(H<G\), so its six-piece fibre application is legitimate. RLP and RPLP have at most five pieces and use only Sun(2–5). Sun(6) is never assumed in the ambient counterexample. C4, C15 and C18 repair the relevant hypotheses and closure wording. SOURCE00:L31–54; SOURCE01:L63–82.

The pattern reduction loses no configurations. Intersection indices are multiples of the corresponding least common multiples. The product formula gives
\[
\mu(U_iU_j)=\alpha_{ij}/5.
\]
Disjointness forces this product to be proper, hence every \(\alpha_{ij}\) is an integer in \(\{1,2,3,4\}\). Pairwise coprimality permits at most one E2, E3 or E5 vertex. E2 has exactly the necessary two classes, valuation one and valuation at least two. Absence and coincidence yield the eight listed E2/E3 types, with stabilizers \(S_6\), five copies of \(S_5\), and two copies of \(S_4\). SOURCE02:L16–42.

This includes \(r_i=1\), arbitrary prime powers and coincident markers. Equal subgroups are not excluded: in Core5(6), equality forces their two cofactors to be one, and their pattern remains among the enumerated possibilities.

Saturation is valid, rather than an unsupported bounded-representative argument. Since \(q\le4\), common primes of \(q_jr_j,q_kr_k\) lie in \(\{2,3\}\). Since \(t\le5\), fibre gcds involve only \(\{2,3,5\}\). For each prime, at most one cofactor contributes; its valuation minimum therefore saturates at the other endpoint’s bounded \(q\)- or \(t\)-valuation. Class-one E2 is represented exactly. The larger-marker cases saturate at exponents two, one and one respectively. Arbitrarily large cofactors introduce no extra cases. C5 and C16 correctly repair the earlier justification.

E5 is irrelevant outside FH5: neither \(\alpha\) nor \(q\) has a factor five, and the cofactors share no prime. N26’s additional τ dependence is handled by C14. FH5 explicitly considers all seven E5 placements, including coincidences. SOURCE01:L68–87.

The original T/K/P rules retain their stated scopes. T follows from intersection divisibility, the product formula and product-set inclusion. Its admissible τ values are **necessary-condition candidates**, not claimed group realizations. At \(\tau_{\min}\), a K link pins the actual τ by the corresponding upper bound; K then counts pairwise disjoint enlarged cosets missing the distinguished coset, giving \(\sum\alpha\le4\).

P uses the correct double-coset grid
\[
u=\frac1{5\gcd(r_v,\alpha_{jk})}.
\]
The corrected bounds are \(lo=u\lceil L/u\rceil\) and \(hi=u\lfloor\min(x_j,x_k)/u\rfloor\), followed by the correctly oriented K2 decrement, including both directions when sizes agree. Replacing intersections by upper bounds lowers the Bonferroni expression, so PB rejection is sound. SOURCE04:L41–101; SOURCE01:L36.

H5 is also sound. Equal \(a,b\)-edge labels \(c\), together with \(\alpha_{ab}=1\), force \(\tau=c\). The resulting common product is invariant under both \(U_a\) and \(U_b\), hence under their generated subgroup \(W\). Its measure \(c/5<1\) makes \(W\) proper. **Both** subgroup inclusions imply \([G:W]\mid5\), so the index is five, and cardinality identifies \(W=U_aU_b\). The forced fibre sizes follow. C2 repairs the missing second inclusion explicitly. SOURCE04:L118–137.

L9 correctly moves left-fibre pieces into \(H\), and right-fibre pieces into \(U_v\) by common right translation followed by inversion. Disjointness and local indices are preserved. Applying the appropriate accepted Sun statement to **every subset** gives the hereditary condition. The old v1 allowed family need not be downward closed; the v2/v3 family is. C10 and C17 distinguish them correctly. SOURCE03:L28–66; SOURCE01:L33,L75–78.

**The Claude MAJOR N26 gap is repaired.** Among neighbours, the possible triangle labels give:

| Labels | T-admissible τ |
|---|---|
| 222 | \(2,4\) |
| 224 | \(2,4\), or only \(4\) |
| 244 | \(4,8\) |
| 444 | \(4,8,12,16\) |

At most one edge has its divisibility reduced by the opposite E2 marker. Thus, with at least two 4-edges, another 4 remains in \(\tau_{\min}\). The table follows and excludes every prime at least five. Only τ=12 introduces a factor three. For \(v=E3\), requiring \(\tau_{\max}<3\tau_{\min}\) on every neighbour triple excludes exactly the problematic 444 case. C11 deletes the reversed disjunct; C14 supplies the missing proof. SOURCE01:L40–61.

N26 then follows: odd \(r_v\), granularity and XE force every pairwise \(X_j\)-intersection to have measure \(1/5\). The repaired coprimality step makes the three intersections of each neighbour triple coincide. All ten intersections coincide, leaving five disjoint petals of measure \(1/5\) around a common fifth: total \(6/5\), impossible. SOURCE03:L99–117.

RLP and RPLP have sound exact certificate implications. The double-coset facts give \(D_j\subseteq Y_j\), \(\mu(D_j)=q_j/5\), and \(1\le q_j\le5-\alpha_{vj}\). Every possible actual q is therefore in the checked product range.

For RPLP, ordered forced pairs correctly encode \(Y_j\subseteq Y_w\). Every realizable column has nonempty \(A\), satisfies these containments, and has hereditary-allowed \(S\subseteq A\); **empty S is included**. Equality multipliers are free, upper-bound multipliers enter negatively, and lower-bound multipliers positively. Summing the column inequalities proves the stated lower objective bound. A scaled Farkas direction satisfies the same check, so solver optimality need not be trusted. SOURCE03:L123–172.

The strict mass contradiction holds for every finite cofactor:
\[
\mu(\text{relevant union})\le1-\mu(U_v)
=1-\frac1{5r_v}<1.
\]
A uniform gap over unbounded \(r_v\) is unnecessary. This justifies objective thresholds of one and the strict PB bound.

The checker reconstructs the complete universe. Its star enumeration tries every star and filters only completed triangles; its edge DFS independently traverses the fifteen edges with the scalar T predicate. The two ordered leaf lists are compared exactly. Stabilizer orbits are expanded from representatives; summed orbit sizes must equal union size, and that union must equal the independently generated leaf set. Representative membership and scalar T-consistency are checked separately. Counts and hashes supplement these set equalities. SOURCE08:L219–295,L335–413,L1056–1118.

Crucially, **all mathematical decisions use `(type,rep)`**. The engine `code` contributes only syntax validation and informational diagnostics. Neither witness evaluation nor coverage relies on its orbit membership. For example, SOURCE11:L216–226 reports 2,268 lines for the E3-only type but only 402 `code` fields in their representatives’ typed orbits. This discrepancy therefore does not undermine coverage.

Semantic input checks enforce the eight types, integer vertex domains excluding booleans, distinct vertices, duplicate-free subsets, exact line keys, witness/vector lengths, rational-string syntax, required signs, and duplicate-key rejection. Duplicate-key fallback parsing preserves a permanent failure. Every q key is recomputed; every hereditary support is checked. RPLP rebuilds ordered containments, all columns, bounds and objectives. N26 examines every admissible τ directly. SOURCE08:L154–168,L428–745,L881–917.

FH5 recomputes V, uses SAT=30 including prime five, fixes only a’s trace, and gives every other vertex all prescribed subsets. Its shared seven-placement search prunes only persistent F3 failures or already failing hereditary subsets. Any surviving complete assignment rejects the witness. DFS and FH5 incompleteness, malformed inputs and certificate failures block PASS; the early witness-deadline omission identified above is the exception.

The imported execution evidence binds the audited checker hash and consistent input hashes. SOURCE11 records both enumeration routes agreeing for all eight types, exact disjoint orbit coverage, 1,575,031 leaves, and all 61,124 witnesses verified: K 55,159; RLP 5,513; FH5 134; N26 108; PB 55; RPLP 155. There are no survivors. It records 324,428 RLP q checks, 9,371 RPLP R entries and 385 P entries. All 1,275 used dual keys passed; the 71 unused entries are not acceptance premises. SOURCE11:L1006–1083.

SOURCE12 records **68 tests total**, including 43 mutation demonstrations, all behaving as expected. These cover missing/duplicate orbits, malformed inputs, missing q entries, empty-S columns, τ=12, and SAT5. They support the implementation audit but do not prove completeness or cover the newly found deadline defect.

Finally, mathematical correctness and process acceptance remain separate. The disclosed NumPy auxiliary route violates the standard-library restriction for primary evidence; the supplied primary checker uses the standard library and supplies the required finite evidence. The malformed pre-execution draft and ill-posed exploratory mutations are disclosed process history, not counterexamples to this completed route. SOURCE21:L14–20.

SOURCE19 is a bounded priority screen, with explicit inaccessible sources and a later refresh still pending. It establishes neither novelty nor exhaustive absence of prior claims. SOURCE17/18 are rule-delta reviews, not supplied final whole-composition reviews from both families. Those gate formalities remain separate from the correctness conclusion above. This audit supplies no Lean certification, human peer review, publication acceptance or novelty claim.