# Sun k7: single marked vertex with only 3/5 markers excluded

Recorded at 2026-10-19T00:34:30-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIAL.** Theorem K7-M1 excludes every K7 configuration with exactly one marked vertex z whose marker product is m_z=3^A5^B, A,B≥0,A+B>0 (no2-marker). Exponents are arbitrary; capping is used only in label-gcd calculations. This is not Sun(7); the remaining marked classes remain open.

## Record

- [Candidate](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-M1-v1.md), SHA256 `6e9b2d09aa5c55698dd96d95266243701ca077c98ec615aa57b648ebf3f95d63`.
- [Mandatory erratum](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-M1-erratum-v1.md), SHA256 `4094b53783244e8b824dd64409d28380d0a635e76d74035e361f5ca22a26c510`.
- [Codex](sun7-m1-codex-v1.prompt.stdout.txt): ACCEPT-WITH-FIXES,0FATAL/0MAJOR,1MINOR; observedgpt-6.1-sol.
- [Claude](sun7-m1-claude-v1.prompt.note.md): ACCEPT-WITH-FIXES,0FATAL/0MAJOR,8MINOR; observedclaude-opus-5-5. Parent read both and erratum fully.
- Imports: [accepted LFC/INV/ROW-U](sun7-lfc-inv-parent-verdict-v1.md), including its exact hypotheses and mandatory overlay, and the accepted finite-core quotient. No computational output is a premise.

## Parent derivation

At an unmarked vertexv, gcds among the five unmarked-neighbour fibre labels reduce to the alpha gcds. The marked-neighbour label changes only the3/5compatibilities; deletingz from an allowed set preserves allowedness, so feasible weights on the unmarked part can be extended byy_z=0. A row containing1–4fives has value≥5+1=6, impossible underLFC. A row withthrees must have at least3threes and nofours/fives; ifalpha_vz∈{3,4,5}, weights1/3onthrees,1onones,1/2ontwos and1/3onz are feasible on a superset of all allowedsets and yield5+alpha_vz/3≥6. Thusalpha_vz∈{1,2}. If the five unmarked entries are all1/2/4, the odd3/5marker changes no gcd and the ROW-U proof applies to the entire six-neighbour row.

Atz itself, ROW-U applies to bothalpha andalpha*, forcing exactlythree incident4edges on each side and a partitionF⊔F* of the six othervertices. A5edge among thosevertices propagates toall15edges bythe rowlemma; inversion then makesallalpha*=1 there, contradicting the inverse rowlemma. If a3edge exists, everyvertexincidenttoone hasatleastthree3neighbours, yielding≥4suchvertices; the rowlemma placesall of them outsideF, which hasonly3vertices. Thus everyunmarked-unmarkededge is1/2/4. Bothorientations now haveatleastthree4edges at everyvertex; disjointness fromalpha+alpha*≤6 forcesexactlythree. An undirected3regulargraph on7vertices hasodddegreesum21, impossible. The finite-core quotient preserves indices/marking and lifts the exclusion to arbitrarygroups withfinite-indexsubgroups.

## Findings and limits

ErratumF1 listsR0,LFC(a)(c),Sun2 andinverseclasspreservation;F2separatesactualunboundedmarkerexponents fromcappedgcdindicators;F3states theabstractROW-U-degproofcondition;F4fixestheweightnotation;F5usesgcd≤3withthecorrectequalitycondition;F6includesstep0wheninvertingandalpha**=alpha;F7renamesthevertexsetW;F8limitsprobeobservations to their examinedrange. Thesecloseallfindings withoutachangedstatement.

Writtenproof only, relative toacceptedSun(t),t≤6,throughLFC. NoLean,humanreview,priorityorsignificanceclaim. TheoremK7-Z2 isaseparateunreviewedcandidate, notapremise.
