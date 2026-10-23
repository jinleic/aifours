# K5 semantic normal forms/templates/imports and inactive H3 — versioned review repairs r1

All original notes/receipts remain unchanged. This addendum is to be read with K5 normal-form r2, template-cover r1,
normal-form r3-IMPORTS and HALL3 r1. It closes the MINOR findings in the parent static Claude reviews:

- `moqls8-k5nf-claude-review-v1.note.md`, SHA2565ff9add0bafb8d249d0f79ede6a27f30ac3608d4c76a72a35a38b8d452bcb2af;
- `moqls8-k5tpl-claude-review-v1.note.md`, SHA2569c23628b7a9b8625380b37f5b7612ac799344e0b94aaebc1887ff0f1dc5a5fe6.

Their dispositions are static model review, not peer review or an exclusion. The parent reported Codex ACCEPT/zero
findings. Repairs do not change a clause, unit list, case count, algorithm or solver receipt. Parent disposition and
strict independent replays remain required. H3 stays INACTIVE and has no follow-up run/certificate here.

## A. Normal-form r2 minors1–4

**A1: add square relabelling and use the bridge in property form.** Add move rho: relabel squares2–5. It is lossless:
the objects form an unordered set, mutual orthogonality/Prop1 is symmetric in the pair of labels, and QLS-ness,
row0 standard form, frame weights and reduced-K5 membership are per-square properties. For the unified bridge,
initially relabelling the chosen weight3-containing square as Q1 is justified by the same unordered-set argument.

The old-F bridge is used in PROPERTY form: any genuinely labelled reduced-K5 set in row0 standard form, with every
square having a row0-frame weight3 entry, supports at(1,0) equal toA,{4},{5},{6},{7}, and the exact non-strict Q1
column0 ROWLEX property, has a canonical auxiliary extension satisfying F. This is a reformulation, not a verbatim
quote from the soundness note. It follows from its§4 (G2–G5 for every QLS),§§1,6 (P4 from reduced-class definition),
the auxiliary definitions, and the actual-CNF C7 finding that SB2+ROWLEX are the only extra normalisers. A set already
meeting these hypotheses is its own output of the normalisation moves with identity choices; the history/path used
to reach it does not matter.

**A2: inline rightmost-k proof.** Let C_k={8-k,...,7}, k=1,2,3. For S⊆B with |S|≥k and S≠C_k, S cannot be a subset
of C_k (otherwise its cardinality would force equality). Thus S contains a coordinate m<8-k. At S's first1,
which occurs no later than m, C_k has0 and both vectors are0 before that position; hence S is lexicographically
larger. A support meetingA is larger for the same first-difference reason, at a position1,2 or3. The residual sigma
preserves A,B as sets and |sigma(S)|=|S|, so minimum pure-B cardinality and pure-B-ness are preserved.

**A3: wording/indexing.** The final row permutation IMPOSES ROWLEX (or re-imposes it if the initial presentation was
already sorted); no prior row sort is needed. Write V1[c-1]=g_1((0,c),(2,0)), c=1,...,7. Cube b sets this variable
to bit c-1 of b, so support S has label sum_{c∈S}2^(c-1). These labels are not ROWLEX ranks; ROWLEX uses the opposite
significance, coordinate1 most significant and False<True. Parseval uses the sum of absolute squares |(w_i)_b|².
Every minimal key has support C_k, so tie-breaking is immaterial.

**A4: direct, fully pinned c112 import.** Parent verdict
`review/moqls8-k5-root-parent-verdict.md`, SHA256e619e3c839040432209505325543461af66802634ca546f322961bc77eb2e790,
lines5 and19, accepts the122 roots including c112 (c112 is not among the six UNKNOWNs). The final receipt is
`review/moqls8-k5-root-parent-replay-v1/final-a1/FINAL.json`, SHA256
88cac42131dd8a41ce2e2565033ba1f1c9e8ad00756e29132ff14f4ce5e62905. Its per-root entry is JSON pointer
`/per_root/106` (id c112,statusPASS,accepted=true), whose direct receipt is
`review/moqls8-k5-root-parent-replay-v1/corpus-a1/c112.json`, SHA256
ad191697357d5f36b471c735f6c695400aff35da662d380e877590d1fa639603 (freshly matched to the FINAL pin).
The seven units are[-57,-106,-155,-204,+253,+302,+351], leaf SHA c95a34c2…cd83. The retained mapping is directly
in root-cover audit lines99–104 and manifest65f6e0dd…3b5e: `all/cube112.drat.zst`, SHA256
b6b1e6d23c5f4a1bbd7630027463d3bc2f398fb245ff6b450a718fd3305d14bd; raw proof SHA256
d5fd6fd0fff305ab34a2aed064836d7682ee07ee253b25fa93dc93a525af63c2. This import applies ONLY to the all-five-P4 F,
not to the later weakened F_one; all three c112 templates must be run anew there.

## B. Template-cover r1 minors1–4

**B1: larger residual group acts on SUPPORT SETS.** For sigma∈Sym(A)xSym(B), extended by sigma(0)=0, put
Q'_s(i,sigma(j))=P_sigma Q_s(i,j). Then Q'_s(0,sigma(j))=|sigma(j)>, so standard form is preserved, and
supp Q'_1(1,0)=sigma(A)=A. The VECTOR Q1(1,0) is not claimed fixed under Sym(A); its coordinate values may change.
Relabel square s∈{2,...,5} to sigma(s+2)-2, a bijection because sigma(B)=B, restoring the singleton SB2 supports.
Finally sort rows2–7. For normal-form r2's smaller Sym(B) subgroup only, sigma fixes A pointwise and v actually is
fixed; that statement must not be imported for the larger template group. Reduced-K5 P4 weights are preserved.

**B2: exact class/conclusion.** All OLD-F coverage conclusions in template-cover r1 mean "a member of the reduced
class K5, after the accepted row0/SB2 moves". Thirteen old-F refutations plus c112 and the reviewed bridge/theorem
would imply reducedK5=empty, not K4=empty or the full n8 problem. The separate unified F_one bridge supplies the
stronger target quantifier only after its own reviews and ALL16 new refutations.

**B3: c112 is imported directly from A4 above, not by trusting a document under review.** All16 templates satisfy
one of root64,96,112; precisely P0-B6,P1-B6,P2-C4 imply the seven c112 units. Their old-F formulas are therefore
excluded by the parent-accepted old-F c112 root proof.

**B4: explicit degree2 symmetry.** In the proof with R={u,v,w}, if any extra neighbour exists, rename v,w WLOG so v
has it. If only w had z, columns x,z would have N(x)∩N(z)={w}, contradicting the column pair-overlap rule. If v has
z, the same rule forces w also to have z. The remaining closure/rank argument is unchanged.

## C. r3-IMPORTS minors1–4

**C1: source attribution.** ROWLEX orientation, False<True, non-strictness and absence of a secondary key follow
from `code/gram_a.py`248–270 (encoder SHA bf1aada1…d05a), not from C9. C9 binds only the V1 variable-name meanings;
the root-cover audit20–23 checks the declared sign/bit convention and explicitly labels its hash comparisons as
declared (83,152). These establish decoding and cube labels, not comparator orientation. Fresh root proof hashes
come from FINAL/c112 in A4, not from the root-cover audit's declared-mapping comparison.

**C2: complete active families/auxiliaries.** The bound clause families are G2,G3,AND_DEF(b3/c4 full-equivalence
AND definitions;1411200clauses),G4,G5(including u5 equivalence triggers and same-ray implications),P4(including
w3 one-way implications and ALO),ROWLEX(including lexeq prefix-equivalence definitions),SB2. G1/common-line/self
values are exact constants. Named variable families are g,b3,c4,u5,w3,lexeq; no unlisted counter/XNOR helper is
active. Generic classical Latin families and W1 are inactive. SB2+ROWLEX remain the only active extra normalisers.

**C3: exact-hypothesis wording is the restatement justified in A1, with the identity/fixed-point remark there.**
It is not a direct quote of three assumptions from the original soundness note.

**C4: advisory/binding pins.** The own prompt-only advisory is
`review/K5_NORMAL_FORM_CLAUDE_v1.stdout.json`, SHA256c8aeaa56aa2ec468b637f61b7bfeafdf5bec16cdbcf1609ae6a8dfec4eb553bb.
Its stated verdict is a self-report by that model, not an additional parent correctness verdict or a fresh replay.
The actual-CNF binding receipt is parent `review/moqls8-encoder-binding-v1/binding-result.v2.json`, SHA256
dce638a92804bd04f2c3e9f64c61ba35e1d5e7c098df9323ebdac57c56bb6112. These hashes were computed from the actual
respective files; they must not be interchanged.

## D. Inactive HALL3 r1 minors1–3 (no new run)

**D1: exact constants/folding.** Self-pair overlap is exactlyTrue; distinct common-row/common-column overlap is
exactlyFalse for every QLS. Dropping a clause containingTrue or dropping False literals therefore preserves
necessity. In a parallel transition pair at most3 of18 selected literals are constantFalse. In an intersecting pair,
if the clause does not contain the shared-point True, at most6 are False (the shared point's row/column), so at least
12 survive. Independently an empty folded clause would fail every QLS, including a classical one, contrary to the
rank argument. No empty clause is generated by the family.

**D2: permitted/countable statements.** A strictly checked F_H3+cube refutation excludes genuine configurations in
that cube, using the original necessity bridge plus H3. It does not refute F+cube. An F+cube refutation implies the
stronger F_H3+cube is UNSAT semantically, by monotonicity, but its DRAT BYTES do not automatically transfer: RAT
partners may change on added clauses; the reverse direction may use absent premises. A fresh exact-CNF check is a
new certificate, not a transfer. A separately validated genuine-configuration cover may mix exact F/F_H3 leaf
certificates only with a common full-product partition/identical units, all input/body hashes and both bridges
pinned, and independent replay for each. No F_H3 certificate enters the F Boolean ledger, no old UNKNOWN changes
state by relabelling, proof-free runs never count, and SAT support models are not vector counterexamples. None of
this is currently used: the H3 pilot was UNKNOWN and H3 remains inactive.

**D3: unambiguous literal domains.** Let l_b be the b-th cell of the other line. Row family:
OR g_s((0,a),l_b) over a∈R⊂{0,...,7},|R|=3 and b∉C⊂idx(l),|C|=2. Transposed family:
OR g_s((0,a),l_b) over b∈R'⊂idx(l),|R'|=3 and a∉C'⊂{0,...,7},|C'|=2. Indices and cells are never conflated.

These repairs change no computational conclusion. Semantic coverage is still pending parent disposition and
certificate replay; neither reducedK5 nor the full n8 target is declared solved by this addendum.
