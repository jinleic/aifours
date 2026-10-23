The structural arguments are sound, but K7-COV has a **MAJOR hypothesis mismatch**, and K7-Q needs a disjointness repair. All seven supplied SHA256 hashes match. Only snapshot reads and hashes were used; no executable mathematics, network, writes, or delegation were used.

**K7-TRI — ACCEPT.**  
The formulas at [SOURCE00:35–62](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset7-k7-structure-review-v1/snapshot/00-K7-structure-v1.md:35) correctly specialize T and Ppair.

Since \(r\le5\), its prime factors lie in \(\{2,3,5\}\), so \(\gcd(r,\ell_v)=d_v(r)\). The three T upper bounds are \(ac,ab,ab\), giving \(\tau_{\max}=ab\).

The stronger grid identity is also correct. For example, when \(v\) carries marker 2, the other two vertices have 2-valuation exactly 1, hence
\[
v_2\!\left(\gcd(n_v,I_{jk})\right)
=\min(1+\varepsilon_2(v),1+v_2(r_v))
=1+\min(\varepsilon_2(v),v_2(r_v)).
\]
Without that marker, the minimum is 1. The analogous 3- and 5-parts give exactly \(6d_v(r_v)\); pairwise coprimality excludes every \(w\)-contribution.

The containment orientation and grid-step subtraction agree with accepted F6, including equal adjacent measures: equality then requires both containments. These conclusions concern T and Ppair; they do not replace the profile-dependent VFC/RPLP allowed-set tests.

**K7-U — ACCEPT.**  
The 16 T-survivor types at [SOURCE00:72–94](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset7-k7-structure-review-v1/snapshot/00-K7-structure-v1.md:72) are correct. Directly separating the least label \(a=1,2,3,4,5\) gives respectively \(5,5,3,2,1\) types.

For an unmarked apex with adjacent labels \(s,t\), opposite label \(r\), and \(L=\operatorname{lcm}(a,b,c)\), the bounds simplify to
\[
6\,lo=\left\lceil\max(L/r,s+t-6,0)\right\rceil,\qquad
6\,hi=\min(s,t)-\mathbf1_{\min(s,t)+r\ge6}.
\]
This verifies the five exclusions explicitly:

| Type | \(lo\) | \(hi\) |
|---|---:|---:|
| \((1,5,5)\) | \(1/6\) | \(0\) |
| \((2,5,5)\) | \(2/6\) | \(1/6\) |
| \((3,4,4)\) | \(3/6\) | \(2/6\) |
| \((3,5,5)\) | \(3/6\) | \(2/6\) |
| \((4,5,5)\) | \(4/6\) | \(3/6\) |

The remaining 11 pass at every apex. In particular, \((5,5,5)\) has \(lo=hi=4/6\), while \((2,2,4)\) has equality intervals \(2/6\) opposite a 2 and \(1/6\) opposite the 4. This is survival of these two tests, not realizability or survival of all active rules.

**K7-TWIN — ACCEPT.**  
The proof at [SOURCE00:98–125](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset7-k7-structure-review-v1/snapshot/00-K7-structure-v1.md:98) handles marked third vertices correctly. If \(x,y\) are unmarked and \(\alpha_{xy}=1\), then \(d_z(1)=1\) regardless of \(z\)’s markers. Thus T gives
\[
\operatorname{lcm}(\alpha_{xz},\alpha_{yz})
\le\min(\alpha_{xz},\alpha_{yz}),
\]
forcing equality. Taking another unmarked vertex proves transitivity.

The prohibition of a 5-edge also survives arbitrary markings of \(z\): at apex \(x\), the grid remains \(1/6\), the lower bound is \(1/6\), and K2 bars containment because \(1+5=6\), giving upper bound zero.

Finally, at apex \(z\), the opposite edge is 1 and \(\tau_{\min}=b\). Therefore the intersection has measure at least \(b/6\), equal to both product-set measures. Finite-set equality proves \(U_zU_x=U_zU_y\). No commutativity or normality is needed.

**K7-Q — ACCEPT-WITH-FIXES.**  
The substantive classification and the 3/4 incompatibility argument at [SOURCE00:141–158](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset7-k7-structure-review-v1/snapshot/00-K7-structure-v1.md:141) are correct. A 5-edge propagates through quotient triangles and forces singleton blocks. If a 3-edge and a 4-edge coexist, the stated intermediate triangles force a \((2,2,3)\) triangle, which fails T because \(6>4\). Every 2/4 quotient colouring passes the all-unmarked triangle table.

**MINOR — SOURCE00:133–139:** “Exactly one” contradicts the acknowledged overlap. A single twin block satisfies both Q23 and Q24; so does any quotient with every edge labelled 2.

Concrete fix: assign all-2 and one-block cases to Q23, and require Q24 to contain at least one 4-edge. Also define the equivalence precisely as
\[
B\equiv B'\iff B=B'\ \text{or}\ \beta(B,B')=2.
\]
The prohibition of simultaneous 3 and 4 labels applies to the unmarked quotient, not the full marked pattern.

**K7-Q5 — ACCEPT.**  
The weighted argument at [SOURCE00:162–185](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset7-k7-structure-review-v1/snapshot/00-K7-structure-v1.md:162) respects the necessary quantifiers: **for every admissible \(q\), there exists a feasible weight vector**.

Each unmarked neighbour has \(q=1\), local index \(w_j\), and gcd 1 with every other local index. Hereditary allowedness therefore makes it isolated, validating its full \(1/6\) contribution.

For two marked neighbours, their marker factors are coprime. If their pair is forbidden, both receive weight 1; if allowed, they cannot both have \(q=1\), so weighting a neighbour with larger \(q\) supplies at least \(2/6\). Together with four isolated neighbours this reaches 1, contradicting the strict VFC inequality.

The limited \(|U|=4\) caveat is justified. Taking marked factors \((3,5,2)\) and \(q=(2,2,1)\) gives local indices \((6,10,2)\). Every marked pair is allowed, but the triple is forbidden. The maximum marked weighted contribution is \(5/12\); three isolated unmarked neighbours add \(1/2\), totaling \(11/12<1\). This demonstrates weakness of this VFC bound alone, not compatibility with every other rule.

**K7-COV — ACCEPT-WITH-FIXES.**  
The configuration-level coverage argument works, and evaluating every active rule on the full lift is essential. However:

**MAJOR — SOURCE00:189–205:** the stated pattern hypothesis includes only T and Ppair, while item (i.3) removes Q5 patterns using VFC. Consequently, “The reduction removes nothing that T and Ppair keep” is false.

Concrete counterexample: take seven unmarked profiles \((1,1,0)\) and every edge label 5. Every triangle passes T, with \(5\le25\), and Ppair, with \(lo=hi=4/6\). All twin blocks are singletons. Yet the reduced family excludes this pattern because \(|U|=7\).

Fix either by retaining unrestricted Q5 in the T/Ppair representation theorem, or by adding survival of VFC at unmarked vertices to its hypotheses. In the latter version, replace (iv)’s opening sentence with: “Only patterns refuted by T, Ppair, or the proved VFC exclusion are removed.” Actual configurations satisfy these necessary conditions, so completeness for configurations remains valid.

**MINOR — SOURCE00:202–203:** explicitly fix the capped marking data before stating the orbit “iff.” Equal quotient data and marked rows cannot identify different marked profiles. With that scope fixed, the stabilizer is indeed \(\operatorname{Sym}(U)\times\{\mathrm{id}_M\}\).

The relaxation example at [SOURCE00:219–223](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset7-k7-structure-review-v1/snapshot/00-K7-structure-v1.md:219) is correct: \(\tau_{\min}=\tau_{\max}=2\), and the three apex intervals are respectively \([1/12,1/6]\), \([1/6,1/6]\), and \([2/6,2/6]\).

No enumeration, orbit implementation, finite coverage, or realizability claim is verified. FH and section 7 remain UNUSED and receive no acceptance. **K7 remains OPEN.**