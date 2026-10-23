**DISPOSITION: ACCEPT-WITH-FIXES.** FATAL: 0. MAJOR: 0. MINOR: 1.

The argument establishes the claimed **literal Boolean-model-existence transfer**, subject to the expressly imported source-to-base binding. It does not require a unitary realization or a permutation of whole-CNF auxiliary IDs.

**MINOR M1 — classification premise wording.** `SOURCE00:LF54–58` says the residual classification uses “ONLY(A),(B)”. Those two properties also admit the full \(K_{33}\): all rows and columns are nonempty, and every intersection has size three. Excluding it uses the distinguished degree bounds already proved at `SOURCE00:LF51–52`.

Concrete repair: replace that phrase with “using (A), (B), and the distinguished row/column degree bounds from LF51–52.” Explicitly list full \(K_{33}\) as the additional unrestricted case, then exclude it by those bounds. The existing proof supplies the required bounds, so this is a premise-accounting defect rather than a failure of the normal form.

1. **Local Boolean support lemma passes with that clarification.**

   The row0/column0 overlap matrix has one isolated true common-point entry; its remaining common-point row and column entries are false constants (`SOURCE01:LF127–138`). G3 therefore gives nonempty rows and columns of \(X_s\).

   AND is exact, including its constant simplifications (`SOURCE01:LF63–76`). Consequently, `exactly_one_forbidden` forbids precisely intersection cardinality one, including cases involving constants (`SOURCE01:LF172–190`). G2 gives entrywise disjointness across all five matrices (`SOURCE01:LF150–153`). Thus (A), (B), and (C) hold for arbitrary satisfying Boolean assignments.

   In any row or column, five disjoint nonempty supports occupy seven positions. Each individual degree is therefore at most three. Where \(X_1\) has degree three, all four others have degree one. A singleton row isolates its column by (B), and conversely.

   The four forced isolated edges are distinct: rows1,7 use distinct B columns; columns2,3 use distinct rows in2–5. Deleting their rows and columns loses no remaining edges, so the residual \(3\times3\) matrix stays nonempty in every row and column. Row6 and column1 remain, each with degree at most two (`SOURCE00:LF41–52`).

   All residual cases are covered:

   - A singleton isolates an edge. The remaining nonempty \(2\times2\) matrix is a permutation or full \(K_{22}\); a three-one pattern violates (B).
   - Without singletons, every degree is at least two. Two zeros sharing a row or column violate that bound; two zeros in distinct rows and columns produce intersection size one. Hence there are either zero zeros or one.
   - Zero zeros gives full \(K_{33}\), excluded by the distinguished bounds. One zero must simultaneously lie in distinguished row6 and column1.

   Thus the three stated residual forms follow. Outside \(A_1\cup A_6\), a nonpermutation residual must have its isolated edge at \((6,1)\). Disjointness allows this in at most one square. The capacity bounds give \(|A_1|,|A_6|\le1\), hence \(k\le3\) (`SOURCE00:LF60–64`).

   The nine-one lower bound also holds: seven ones force a permutation; eight would leave one degree-two row and six isolated singleton rows, leaving insufficient columns for that degree-two row. The six P1 support totals from `SOURCE03:LF523–545,601–625,681–707,763–791,847–874,930–960` give:

   | Template | \(m\) | Guaranteed permutation matrices among \(X_2,\ldots,X_5\) |
   |---|---:|---:|
   | B1 | 12 | 1 |
   | B2 | 14 | 1 |
   | B3 | 16 | 2 |
   | B4 | 18 | 3 |
   | B5 | 17 | 2 |
   | B6 | 20 | 4 |

   These follow from \(m+28+2k\le49\) and \(k\le3\). No unitarity, phase, rank, G4, or G5 premise enters this local argument.

2. **The primary transformation and core auxiliary extension pass.**

   \(T\) and \(\tau\) are bijections. They preserve equality, common-row/common-column status, and unordered cell pairs. Thus variables map to variables, true constants to true constants, and false constants to false constants (`SOURCE00:LF73–79`; `SOURCE01:LF127–138`).

   They permute all sixteen fixed lines. Reversal of an unordered line-pair orientation merely transposes its overlap matrix, which G3 handles symmetrically. G2 includes every quantum-square pair; G4 depends only on the relabelled intersection cardinality and \(g(p,q)\); G5 depends only on singleton support and the corresponding primary equalities (`SOURCE01:LF150–153,165–206,207–232`).

   The AND name-reuse shortcut requires scrutiny. It is safe here:

   - A `b3` key determines the same two overlap inputs whenever reused.
   - A `c4` key determines its anchor and unordered external pair, hence the same conjunction.
   - Family prefixes separate these from other auxiliary families.

   Therefore canonical conjunction values satisfy every repeated definition. The `u5` clauses force exactly the singleton-support predicate, and the remaining clauses impose exactly its conditional primary equalities (`SOURCE01:LF220–232`). This proves existence of a consistent auxiliary extension without inventing an auxiliary-ID permutation.

   The recorded arguments select generic order8, quantum12345, ngeneric0, G5 and ROWLEX, with no fixg (`SOURCE07:LF7–25`). Hence CL is empty and the classical branches introduce no additional constraints (`SOURCE01:LF83–125,140–149`).

3. **Every retained P4 clause is handled.**

   Only frame row0 is generated: `--p4-all-rows` is absent, and its parser action defaults false (`SOURCE01:LF234,293`; `SOURCE07:LF7–25`).

   Each flag has only its six-subset implications and its square’s ALO participation (`SOURCE01:LF239–247`). Setting all flags false except Q1’s \((1,0)\) flag satisfies every other implication. SB2 gives that witness support exactly \(\{1,2,3\}\); every six-subset of eight coordinates intersects this three-set. Its implications and Q1’s retained ALO therefore hold.

   Deleting the other four ALOs leaves no unsatisfied flag requirement (`SOURCE02:LF50–81`; `SOURCE04:LF12–19`). No reverse flag implication, other frame, or retained other-square ALO is silently omitted.

4. **SB2, all42 template units, ROWLEX, and the representative selection pass.**

   SB2 assigns Q1 support123 and square \(s\ge2\) support \(\{s+2\}\). Under the transformation, that singleton becomes
   \(\{\sigma(s+2)\}=\{\tau(s)+2\}\), exactly the required support for its new label (`SOURCE01:LF271–281`).

   The numeric template units also match the stated supports. Static allocation order gives, for Q1 and \(i,c\ge1\),
   \[
   \operatorname{ID}\bigl(g_1((0,c),(i,0))\bigr)=49c+7i-6.
   \]
   The six seven-literal rows in each selected unit block assign every coordinate1–7 with the advertised signs (`SOURCE03:LF546–590,626–670,708–752,875–919`). Coordinate0 is already false.

   Writing \(S_i\) for Q1’s support in row \(i\), preservation requires
   \(S_{\rho(i)}=\sigma(S_i)\). The displayed generators satisfy this requirement:

   | Template | Direct generator check | B-label orbits | Selected properties |
   |---|---|---|---|
   | B1 | \(S_{r(b)}=\{b\}\), with \(\rho(r(b))=r(\sigma(b))\) | \(\{4,5,6,7\}\) | M2 |
   | B2 | Swap45 preserves both45 supports; swap67 exchanges the singleton rows2,3 | \(\{4,5\},\{6,7\}\) | M2 or M4 |
   | B3 | Within-block swaps preserve67 and45; the double swap exchanges their row pairs | \(\{4,5,6,7\}\) | M2 |
   | B5 | Swap56 preserves7,56,456,456 in their existing rows | \(\{4\},\{5,6\},\{7\}\) | M2 or M3 |

   These checks use the exact supports at `SOURCE03:LF523–545,601–625,681–707,847–874` and generators at `SOURCE00:LF121–126`.

   Every final-row mask is identical, including its negative bits. Thus all ROWLEX inputs are identical. Their listed order is nondecreasing with coordinate0 most significant. The actual clauses define **inclusive** prefix equality,
   \(e_{i,k}=\bigwedge_{h=0}^{k}(A_h=B_h)\); these values provide the extension (`SOURCE01:LF248–270`; clarification `SOURCE06:LF31`).

   B5’s second guaranteed permutation column is essential to this selection argument: one available permutation could occupy label7 alone. With at least two, one occupies4,5,or6 and reaches M2 or M3. Thus six formulas suffice. This establishes coverage, without asserting that six is a minimal possible cover.

5. **The126-clause encoding and Boolean-UNSAT transfer pass.**

   There are \(6\binom72=126\) distinct negative binary clauses. They enforce at most one coordinate1–7 in rows2–7. G3 supplies nonemptiness; SB2 supplies the singleton in row1; constants handle row0 and coordinate0 (`SOURCE00:LF144–150`).

   Consequently these clauses express exactly the stated column0 property over the existing base. They impose no additional whole-square-classical requirement. The resulting clause count is \(5,740,394\).

   For each selected template \(C\), the construction proves
   \[
   \operatorname{SAT}(F_{\rm one}\land C)
   \iff
   \bigvee_{s\in R_C}\operatorname{SAT}(F_{\rm one}\land C\land M_s),
   \]
   with \(R_C=\{2\},\{2,4\},\{2\},\{2,3\}\), respectively. Refuting all six exact stronger inputs therefore suffices to refute the four original Boolean leaves. Neither target refutations nor strengthened CNFs are supplied here.

6. **Binding and scope remain explicit.**

   **Audited directly:** the inline proof, encoder clause semantics and name reuse, weakening-producer logic, selected support/unit lists, deletion specification, instance arguments, and the new Boolean-model construction.

   **Imported:** the original CNF/source/name-table binding and independent weak-base/leaf-byte verification accepted in `SOURCE06:LF27–28,35–37`. The large original CNF, name table, map, and parent-checker artifacts were not independently read or replayed here. Supplied hashes were not recomputed.

   A8 and the genuine-QLS T16 reduction remain accepted background (`SOURCE05:LF36–89`; `SOURCE06:LF12–14`). They provide no prior acceptance of this new arbitrary-Boolean transformation. The new result begins with a fixed template \(C\); it does not establish a Boolean T16 cover of bare \(F_{\rm one}\).

This is a static mathematical and encoder-semantics disposition. It establishes neither a whole-CNF automorphism nor an n=8 exclusion, and it amends no ledger or certification contract. No tools, computation, solver, network, delegation, or writes were used; no gate or native-launch authority is granted.