All 14 SHA-256 hashes match. **No FATAL or MAJOR mathematical defect found.** The MINOR repairs below should be made before implementing the independent checker.

| Component | Verdict |
|---|---|
| L9 hereditary Sun | **ACCEPT** |
| L10 XE | **ACCEPT** |
| L11 N2-6 | **ACCEPT-WITH-FIXES** |
| L12 RPLP | **ACCEPT** |
| Cumulative erratum | **ACCEPT-WITH-FIXES** |
| CERT-FORMAT | **ACCEPT-WITH-FIXES** |

These verdicts concern the written implications. Actual implementation, certificate validity and enumeration coverage remain **INCONCLUSIVE**: none was supplied or executed.

**L9.** The two translations are correct (`SOURCE02:L31–51`).

For a left \(H\)-coset \(C\), choosing \(y_l\in g_lU_l\cap C\) gives the piece \(y_l(U_l\cap H)\). Common left translation places every piece in \(H\), without conjugating its subgroup, and its index is \(\lambda_l\).

For a right \(U_v\)-coset \(C\), the piece is
\[
A_jw_j,\qquad A_j=U_v\cap w_jU_jw_j^{-1}.
\]
Its index is
\[
[U_v:A_j]=|D_j|/|U_j|=q_jr_j.
\]
Common right translation followed by inversion gives disjoint **left** cosets in \(U_v\). Both operations are bijections. The index is independent of the chosen \(w_j\).

Applying Sun separately to **every subset** proves the hereditary condition. In \(U_v\), there are at most five pieces; Sun(6) is unnecessary. Six pieces occur only in the \(H\)-fibre setting, where properness and ambient minimality supply Sun(6).

The maxgcd calculation is actually exact for the stated markers (`SOURCE02:L62–66`). A shared prime must come from a \(q\)-factor, hence is 2 or 3. At most one cofactor contains each prime. Its contribution therefore saturates at the other endpoint’s \(q\)-valuation: at most two for 2 and one for 3. Class-1 E2 remains exact. Coincident markers cause no interference between prime valuations.

Thus L9 preserves every genuine FH5 assignment and every genuine RLP/RPLP support. Restricting supports to hereditary-allowed sets is justified.

**L10.** Every step passes (`SOURCE01:L9–17`; `SOURCE02:L75–81`).

Equality of the products makes \(X\) right-invariant under \(\langle U_j,U_k\rangle=W\), giving \(X=U_vW\). Since \(\mu(X)<1\), \(W\) is proper. Both subgroup inclusions imply
\[
[G:W]\mid\gcd(5r_j,5r_k)=5,
\]
so the index is five. Inclusion \(U_jU_k\subseteq W\), together with its measure \(\alpha_{jk}/5\), forces \(\alpha_{jk}=1\) and equality with \(W\). The final product formula gives \([U_v:U_v\cap W]=\alpha_{vj}\). No normality or distinct-subgroup assumption is hidden here.

**L11.** Step 1 is sound (`SOURCE02:L99–104`). L0.5 supplies the relevant double-coset decomposition; L0.4 gives granularity \(1/5\), since
\[
\gcd(5r_v,5r_jr_k\alpha_{jk})
 =5\gcd(r_v,\alpha_{jk})=5.
\]
The T lower bound gives intersection measure at least \(1/5\); XE excludes equality of the two \(2/5\)-sets. Granularity then forces intersection measure exactly \(1/5\), and equality with \(Z_{jk}\).

The assertion about prime factors of \(\tau\) is **justified in this setting**, but its short proof should be inserted. Up to edge order, the neighbour triangles have:

| Edge labels | \(\tau_{\min}\) | T-admissible \(\tau\) |
|---|---:|---|
| 222 | 2 | 2, 4 |
| 224 | 2 or 4 | 2, 4, or just 4 |
| 244 | 4 | 4, 8 |
| 444 | 4 | 4, 8, 12, 16 |

For the last two rows, at most one edge can have its 4-part reduced by the opposite E2 marker; another 4 remains in the lcm. This covers both E2 classes and absence. Consequently every prime factor of every relevant \(\tau\) is 2 or 3.

Therefore odd \(r_v\) is automatically coprime to these \(\tau\)’s when \(v\ne E3\). When \(v=E3\), excluding divisibility by 3 suffices. E5 and primes \(\ge7\) in \(r_v\) introduce no exception. Condition (iv) cannot simply be dropped: a 444 triangle permits \(\tau=12\).

**MINOR — `SOURCE01:L27`, `SOURCE02:L93`, `SOURCE04:L162`.** The alternative \(3\mid\tau_{\min}\) points in the wrong direction: it would force every admissible \(\tau\) to be divisible by 3. It is unreachable here because \(\tau_{\min}\) is a power of two, so the existing N26 predicate gains no invalid witnesses. Replace the whole sufficient test by:

> If \(v=E3\), require \(\tau_{\max}(jkl)<3\tau_{\min}(jkl)\) for every neighbour triple.

Insert the table argument above to justify the prime-support assertion.

With this justification, Step 2’s coprimality and lcm argument is correct (`SOURCE02:L106–112`): \(Q\ge r_v[G:W]\), hence \(\mu(U_vW)\ge1/5\), forcing the three \(Z\)’s to coincide. Step 3 correctly connects all ten pairs and counts one common fifth plus five disjoint fifth-sized petals.

**L12.** The type construction and column set preserve every realizable type (`SOURCE02:L123–150`; `SOURCE04:L174–179`).

Left \(U_v\)-invariance gives unions of right cosets without requiring normality. R1 gives \(S_C\subseteq A_C\); L9 gives hereditary allowedness. An actual type with \(A_C=\varnothing\) necessarily has \(S_C=\varnothing\), contributes nothing to \(\bigcup Y_j\), and can be omitted. Crucially, **empty \(S\) with nonempty \(A\) is included**.

The forced-containment orientation is correct. The hypothesis and T2 pin
\[
\tau=\alpha_{vw}\alpha_{wj}.
\]
T3 then identifies \(X_w=U_v(U_w\cap U_j)\subseteq X_j\), giving \(Y_j\subseteq Y_w\). Thus excluding columns with \(j\in A,w\notin A\) is safe for every actual \(\tau\).

E1 counts \(D_j\), E2 counts \(Y_j\), and B counts \(Y_j\cap Y_k\). The bounds transform correctly by complementation. TOT is strictly below one because \(U_v\) lies in every \(X_j\). Relaxing the discrete coset masses to arbitrary nonnegative rationals only enlarges feasibility.

The PB/Ppair bounds supporting B are sound (`SOURCE05:L91–101`). The T lower bound at \(\tau_{\min}\) is conservative for every admissible \(\tau\). Granularity is exact. The containment bars use the correct K2 inequalities, including both directions at equal sizes. Using upper intersection bounds in Bonferroni lowers its expression, so a PB violation remains valid.

The RPLP dual signs are correct: upper-bound multipliers enter negatively, lower-bound multipliers positively, and equality multipliers are free. Summing the column inequalities proves weak duality directly. The Farkas argument is valid: an infeasibility direction has column coefficients at most zero and positive objective; positive rational scaling gives objective one while preserving the required inequalities (`SOURCE02:L154–166`).

Every \(q\) must be handled separately. The product range and the permitted mixture of RLP and RPLP witnesses cover every actual \(q\); no monotonicity shortcut is justified.

**Erratum.** The substantive v1 findings are correctly folded (`SOURCE03:L13–61`): units, both subgroup inclusions, fibre translations, properness, saturation, unrestricted trace choices, coincident markers, necessary-only admissibility, and the controls’ reversed logic.

E10 correctly distinguishes the old support predicate from L9. Hereditary allowedness is an explicitly versioned strengthening in v2, rather than a retrospective description of v1. Maximal-support dual constraints suffice under either definition because weights are nonnegative. The text supplies no evidence that any engine actually implements these specifications.

**MINOR — `SOURCE03:L13–17`; `SOURCE07:L33,L46–47`.** The accepted dependency is correctly rebound to proof-v4 and its errata, but the frozen contract still names proof-v3. Add an explicit dependency-supersession note identifying those contract clauses and the binding in `SOURCE11:L11`. Preserve the frozen contract unchanged.

**CERT-FORMAT.** Under the intended rounding convention, its mathematical witness checks are sound. The eight types exhaust marker placements; the stabilisers preserve each distinguished marker. T uses the correct table and necessary interval. The format requires independent orbit coverage rather than trusting the engine’s canonical code.

FH5 includes every actual assignment: H5 forces the specified \(t\)’s; only \(a\)’s singleton label is fixed; every other prescribed or free trace ranges over all subsets of its size. F3 applies at every assigned \(t_i=1\). The hereditary rejection test and all seven E5 placements are correct (`SOURCE04:L135–154`). Saturation of the \(t\)-valuations makes fgcd exact, including arbitrary powers and coincident markers.

**MINOR — `SOURCE04:L118–119`.** Make grid rounding unambiguous:
\[
L=\max\!\left(\frac{\tau_{\min}}{5\alpha_{jk}},x_j+x_k-1,0\right),\quad
lo=u\lceil L/u\rceil,\quad
hi=u\left\lfloor\min(x_j,x_k)/u\right\rfloor,
\]
then apply the stated containment decrement. Ordinary integer ceiling/floor followed by grid rounding would be unsafe. For local cyclic-index-five data, the correct bounds are both \(1/5\); ordinary ceiling/floor would instead produce 1 and 0, manufacturing a pair contradiction.

The checker also needs explicit fail-closed requirements:

- Validate vertex domains, distinctness, subset membership and absence of duplicate members; enforce vector lengths, finite rational entries and required signs.
- Independently regenerate all T-consistent leaves and establish exact orbit coverage. Counts or worker hashes alone do not discharge this obligation.
- Generate every admissible \(q\); recompute its marker key and evaluate its objective on that \(q\). Reject missing or mismatched entries.
- Check RLP supports over all 31 nonempty subsets, including every hereditary subtest. For RPLP include all permitted \((A,S)\), especially empty \(S\).
- Exhaust FH5 assignments independently for all seven E5 placements; counts are informational.
- Reject unknown or malformed rules. A SURVIVE line prevents the global exclusion conclusion.

The N26 repair above should be copied into this format. No additional substantive column or \(q\)-coverage obligation was found.

I independently audited L9–L12, their supporting T/K/P/F specialisations, saturation arguments and certificate implications. Zhu’s Sun(3/4), accepted Sun(5), and the k5 computational acceptance are imports; that acceptance was not replayed. Static reads and hashes were confined to the supplied snapshot. **No k6 theorem, survivor conclusion or novelty conclusion follows from this audit.**