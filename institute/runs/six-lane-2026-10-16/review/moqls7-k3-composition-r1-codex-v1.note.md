**DISPOSITION: ACCEPT-WITH-FIXES, as a conditional proof.**

I found no FATAL or MAJOR mathematical defect in the five audited links. The specified encoder branches admit canonical auxiliary assignments for every represented K3 configuration. With the stated certificate and parent-replay premises, the composition excludes K3 and yields \(M(7)=2\).

This is a static audit disposition. It discharges no certificate or parent gate. All snapshot source hashes match the supplied SHA-256 pins; verification used only permitted snapshot reads and hashes.

**Findings: FATAL none; MAJOR none; MINOR three.**

1. **MINOR — make the lex group cube-specific.**  
   `SOURCE00:LF189–191; SOURCE01:LF372–373; SOURCE11:LF25–34`.

   “All 22 generators preserve base, cube and cuts” needs qualification. The code lists seven generators for C311, seven for C321 and eight for C411. These are cube-specific lists.

   For example, C321’s column swap \(4\leftrightarrow5\), applied alone to C311, moves square 2’s required support \(\{4\}\) to \(\{5\}\), violating C311’s signed units. C311 uses that column swap **combined with** square exchange \(2\leftrightarrow3\).

   **Repair:** define
   \[
   H_{311}=\langle\texttt{generators("C311")}\rangle
   \]
   and say that each cube’s own listed generators preserve its conjunction. The code already does this.

2. **MINOR — distinguish `--sym` normalization from cube normalization.**  
   `SOURCE00:LF127–130; SOURCE01:LF358–371`.

   `--sym` alone does not establish one of the three canonical signed cube assignments. For example, the local support assignment
   \[
   S_1=\{1,2,3\},\quad S_2=\{4\},\quad S_3=\{6\}
   \]
   satisfies the fixed heavy triple but requires a residual column permutation to become canonical C311.

   **Repair:** state: “Every `--sym`-normalized K3 triple satisfies both bases; after the residual normalization supplied by Link 6, its Gram values additionally satisfy the chosen cube and G6.” Link 14 already uses this correct quantifier.

3. **MINOR — A’s G2 clauses are not direct clauses solely on \(g\).**  
   `SOURCE01:LF361–364; SOURCE08:LF95–99`.

   The statement that all remaining Gram clauses are direct on \(g\) overlooks the G2 clauses containing \(h\).

   **Repair:** explicitly say that, after setting \(h\) to its defining conjunction, the G2 clauses hold by frame consistency. This changes no auxiliary assignment or CNF.

The per-link audit verdicts are:

| Link | Verdict | Basis |
|---|---|---|
| **3** | **ACCEPT** | Minimality and simultaneous partner preservation give G4 on every own line. |
| **7** | **ACCEPT-WITH-FIXES** | Every active clause family has a necessary-condition or canonical-auxiliary justification; apply findings 2–3. |
| **10** | **ACCEPT, conditional on G1/G2** | Transport reaches the exact canonical cubes; the described cuts follow. |
| **11** | **ACCEPT-WITH-FIXES** | The comparator works at arbitrary length; use the cube-specific group in finding 1. |
| **14** | **ACCEPT, conditional on all stated premises** | The case split is exhaustive, and the C0 argument gives the claimed upper bound. |

For **Link 3**, the minimality argument is valid (`SOURCE03:LF54–78; SOURCE02:LF52–65`).

Assume a non-classical triple exists. K1 and K2 force its number of individually non-classical members to be three, so every K3 triple attains the minimum. If one member were light in any ONB, the Lemma 10 replacement would classicalize that member while preserving both partner orthogonalities.

The simultaneous preservation step is justified: the replacement preserves every previously zero inner product of the changed square. Consequently, every tensor-product orthogonality retains its former zero factor, regardless of which partner supplied the other factor. Changing the chosen square’s basis by a global unitary also preserves its Gram inner products.

The replacement therefore produces a non-classical triple with fewer non-classical members, a contradiction. Applying this to each own-line ONB gives G4 on all 14 lines. Entries on the chosen line have weight one, so every heavy witness lies off the line.

For **Link 7**, the following accounts for every clause family in the specified base instantiations.

| Family | Encoder A | Encoder B | Justification |
|---|---|---|---|
| **Gram variables / G1** | `SOURCE08:LF55–73` | `SOURCE09:LF102–123` | Exactly the non-collinear unordered pairs are represented. Distinct collinear pairs have constant value false. |
| **Products** | `SOURCE08:LF75–86` | `SOURCE09:LF126–135` | Each three-clause definition is the full equivalence \(h\), or \(m\), \(=g(p,r)\land g(q,r)\). Assign the actual conjunction. |
| **G2** | `SOURCE08:LF88–99` | `SOURCE09:LF136–157` | Zero common neighbours force \(g(p,q)=0\); exactly one forces \(g(p,q)=1\). For collinear \(p,q\), exactly one is forbidden. |
| **G3** | `SOURCE08:LF100–114` | `SOURCE09:LF158–183` | Every transition row has a neighbour. A singleton transition coefficient has modulus one and excludes other entries in its transition column. |
| **G5** | `SOURCE08:LF115–118` | `SOURCE09:LF184–187` | Pairwise negative clauses express the necessary disjointness of Gram supports between squares. |
| **G4** | `SOURCE08:LF45–51,119–137` | `SOURCE09:LF60–89,188–202` | Guards or counter outputs select a point with at least three neighbours on each line. Link 3 supplies such a point. |
| **`--sym`** | `SOURCE08:LF123–126` | `SOURCE09:LF191–194` | The three positive units hold after the accepted normalization and themselves supply that line’s heavy witness. |

More specifically:

- **A’s G2 clauses:** \(\bigvee h_r\lor\neg g(p,q)\) expresses the zero-count implication. Each \(\neg h_r\lor\bigvee_{s\ne r}h_s\lor g(p,q)\) expresses the singleton implication. Omitting the last literal when \(g(p,q)\) is a collinear constant correctly forbids a singleton count.
- **A’s G4 guards:** set \(w_{\ell,p}=[\text{neighbour count}\ge3]\). Requiring every four-subset of the six candidates to contain a true literal is equivalent to requiring at least three true candidates. The guard disjunction holds by G4.
- **B’s `counter2`:** `SOURCE09:LF41–57` correctly implements the prefix recurrences
  \[
  A'_1=A_1\lor x,\qquad A'_2=A_2\lor(A_1\land x).
  \]
  Assigning actual prefix thresholds satisfies all equivalences.
- **B’s `counter_ge3`:** assign every register its actual prefix threshold and the output its actual final threshold. The recurrence implications at `SOURCE09:LF73–88` all hold. Full equivalences are unnecessary for this extension argument.

The problematic B branch at `SOURCE09:LF150–151` is unreachable here. On a row frame, two off-line points structurally exclude at most their two columns; the column-frame argument is identical. Thus the G2 product list has five or six items. Transition and heavy lists have six candidates. Appended cube units do not change these construction-time list lengths.

The specified calls have no classical \(L\) and no fixed-support input, so the symbol-line and `fix-json` branches add nothing. Active clauses never use a diagonal Gram entry as a false constant.

The three constructions allocate the same \(g\)-prefix: square order, earlier cell, later cell, skipping common rows and columns (`SOURCE08:LF65–71; SOURCE09:LF113–118; SOURCE10:LF58–67`). This establishes static correspondence; runtime oracle evidence remains imported.

After residual cube normalization, `SOURCE10:LF75–79` emits exactly the signed cube assignment. Its remaining clauses are the singleton equalities, including the correct negative unit when one side is structurally false (`SOURCE10:LF82–98`). These follow from the same-ray argument, or from G1/G2 as corrected by the errata (`SOURCE07:LF5–22; SOURCE06:LF46–56`).

**No active clause identified here excludes a genuine K3 configuration satisfying the stated premises.**

For **Link 10**, the transport is valid (`SOURCE01:LF133–165`).

For any own frame \(\ell\) and off-line point \(p\), all three support counts are positive. Their supports are pairwise disjoint and avoid the intersection with \(p\)’s other own line, so their sum is at most six. Consequently:

- a count at least four forces exactly \((4,1,1)\);
- distinct counts at least three and at least two force exactly \((3,2,1)\).

Simultaneous transposition, followed by the stated row, column and square permutations, maps these cases to the full signed C411 and C321 assignments respectively. These transformations preserve QLS axioms, pairwise orthogonality, individual non-classicality and G4. Link 7 supplies both auxiliary extensions; G6 follows. Thus the transformed configuration satisfies the exact gate inputs, contradicting their assumed accepted UNSAT status.

There is no circular use of the cuts: the gate inputs are the unstrengthened cube inputs.

The described cut counts follow symbolically from `SOURCE01:LF168–170`:

\[
N_{\le3}=14\cdot42\cdot3\binom64=26{,}460,
\]
\[
N_{\mathrm{mixed}}
=14\cdot42\cdot(3\cdot2)\binom63\binom32
=211{,}680.
\]

Their sum is the stated 238,140. An at-most-three clause forbids four selected neighbours in one square; a mixed clause forbids three selected neighbours in one square together with two disjoint selected neighbours in another.

Distinctness also follows statically. Each clause is a star of unordered cell pairs whose common endpoint recovers \(p\). Its leaves recover the frame; square labels and literal multiplicities recover the roles and subsets. The two families have different clause lengths. This verifies the described family, while faithfulness of the external serialized block remains imported.

For **Link 11**, the comparator works at every finite length (`SOURCE11:LF54–69`).

After removing identical-literal positions, write the compared pairs as \((x_i,y_i)\). Let \(e_0=\mathrm{true}\). The code imposes

\[
e_{i-1}\Rightarrow(\neg x_i\lor y_i)
\]

and, except at the final position,

\[
e_{i-1}\land(x_i=y_i)\Rightarrow e_i.
\]

If the first unequal pair is \((1,0)\), all preceding equalities force the incoming prefix true, and the comparison clause fails. Hence satisfiability implies lexicographic order.

Conversely, when the comparison holds, set \(e_i\) to the actual equality of the preceding prefixes. Every clause holds. This also handles an empty comparator, skipped positions and variables shared between comparison positions. The argument does not depend on the bounded truth-table controls.

For C311, its seven listed generators preserve:

- the row/column incidence structure and all Gram conditions;
- the signed cube assignment and the `--sym` requirements;
- G6, either directly or through its G1/G2 derivation;
- the cut family, by permuting frames, off-line points, square roles and subsets.

Auxiliaries can be reconstructed after transformation. Preservation of their original internal assignments is unnecessary.

The finite \(H_{311}\)-orbit therefore contains a lex-minimal Gram vector satisfying every generator comparison simultaneously. Pullback versus active relabelling creates no gap: inverse transformations belong to the same group. Fresh prefix auxiliaries for different comparators do not conflict. This representative satisfies base, cube, G6, cuts and lex together.

For **Link 14 and C0**, the conclusion follows (`SOURCE00:LF222–250`).

Every hypothetical K3 triple normalizes into a covering cube. C321 and C411 contradict the gate premises. In C311, transport supplies the cuts, Link 7 supplies both base extensions, and Link 11 supplies the strengthened A lex representative. The required exact strengthened-input UNSAT premises then exclude this final case under the stipulated A+B standard.

C0 also supports the passage from triples to arbitrary \(t\)-sets (`SOURCE03:LF9–14`). If every member is individually classical, independent global unitaries and entry phases straighten each member in place. These operations preserve tensor orthogonality, producing a classical MOLS set. Therefore a non-classical set contains an individually non-classical member. For \(t\ge3\), that member and any two others form a non-classical mutually orthogonal triple.

Thus exclusion of K1, K2 and K3 gives \(M(7)\le2\). The imported published non-classical pair gives \(M(7)\ge2\), hence conditionally \(M(7)=2\). The earlier four-square upper bound is unnecessary for this deduction.

**Audited versus imported:** I audited the supplied source identities, minimality application, active encoder clauses and auxiliary extensions, cube/G6 construction, transport, described cut family, general comparator, relevant symmetry preservation, composition and C0 subset argument. I imported the accepted K1/K2 results and their trust/provenance caveats, source definitions and published lower bound, accepted parent dispositions and A-cube formula facts, and external block/oracle evidence. Pending B-cube and strengthened C311 certificates, exact-input regeneration and parent replays remain premises; none was executed or newly accepted here.