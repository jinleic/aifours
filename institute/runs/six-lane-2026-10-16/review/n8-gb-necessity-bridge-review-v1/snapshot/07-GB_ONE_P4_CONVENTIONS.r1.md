# GB one-P4 byte conventions and inverse sample — pre-comparison freeze r1

No GB generation has run. No parent's GB hash/binder output has been read. These conventions were chosen in
adapterr1 and remain IDENTICAL in adapterr2, whose only substantive additions are tighter controls and a fixed
source-derived inverse sample. A mismatch with the independent parent binder MUST be reported as a mismatch;
no convention may be adapted after seeing the parent hashes. No solve or native admission is granted here.

## 1. Header and clause counts

Run untouched GB4b593e55…eae0 with exactly:
`--order 8 --quantum 12345 --ngeneric 0 --p4 1 --sb2 --g5`.
No fixg, ROWLEX, all-row or all-column P4 flags. The in-memory encode arguments are frozen in the necessity note.

Let V=the returned GB F.n, including TRUE and EVERY anonymous sequential-counter/conjunction/single variable.
It is NOT just the maximum named g ID or the number of entries in F.tab. Let C=the number of calls to original
F.c during encode. Every call is emitted: constants, tautologies, duplicate literals and duplicate clauses are
not simplified, filtered, deduplicated or reordered. The RAM sink writes precisely GB main's serialization.

- Base header: `p cnf V C\n`.
- Each of16 direct leaf headers: `p cnf V (C+42)\n`.
- Each of6 strengthened headers: `p cnf V (C+42+126)\n`.

All integers use ordinary ASCII decimal, single spaces, no leading plus, one LF. After the header, the byte
parts are: untouched GB base body;42 unit lines; and, only for the6 stronger cases,126 binary lines. No comments
are inserted into the CNF byte stream. The actual numeric V,C are reported only after generation, not guessed.

## 2. Template-unit order and meaning

Source WMAN355b3380…fc74 supplies only the semantic support lists. Its GA `units` field is NEVER used to
construct GB clauses. Iterate i=2,3,4,5,6,7 outermost and c=1,2,3,4,5,6,7 innermost. Look up
`('g',1,(0,c),(i,0))` in the returned GB OWN F.tab; output positive GB ID iff c is in that row's source support,
negative otherwise. Each line is `literal 0\n`. There are exactly42, including negative bits. Manifest case order
is the original WMAN case-list order; this does not change an individual formula's bytes.

## 3. M_s clause order and within-clause sort

Six selected(template,s) pairs remain:
(P1-B1,2),(P1-B2,2),(P1-B2,4),(P1-B3,2),(P1-B5,2),(P1-B5,3).
For each, iterate i=2..7, then lexicographic coordinate pairs(1,2),(1,3),…,(6,7).
Look up BOTH g variables through the GB own table. Sort the TWO SIGNED NEGATIVE integers numerically
ascending within that binary clause; do not sort the126 clauses globally. Emit `a b 0\n`. This convention was
fixed before any parent's GB hashes. It matches our GA generatorr2 convention but NEVER reuses GA IDs.
M_s constrains only column0. The42 unit lines precede all126 M_s binaries.

## 4. Explicit T/−T constants

GB allocates the named TRUE variable first (T=1) and emits the unit `1 0\n` as part of its BASE. Identical cells
return literal T; distinct cells sharing a row/column return−T. GB retains numeric tautological clauses and units
in its original emission. In particular SB2 at coordinate0 emits a TRUE unit, not an omitted Python Boolean.
The42 appended units and126 binaries use c≥1,i≥2, so none is a constant or an ID borrowed from the GA table.
Constant−T is not a newly allocated false variable. The own-name output represents GB's `"TRUE"` key exactly.

## 5. Static inverse-decode sample, fixed before full generation

These are SOURCE-ALLOCATION PREDICTIONS, not a claim that the unrun full GB table has already been observed.
With ngen0, GB first allocates T, then its G1 pre-pass calls glit for all unordered cell pairs in Q order. There
are1568 non-collinear pairs per square. From this OWN GB allocation, for c≥1,i≥1:

`ID_GB(g_s((0,c),(i,0))) = 1 + 1568(s−1) + 49c + 7i − 6`.

This formula is derived directly from GB's loops/new allocator, not a GA offset/mapping. Production construction
STILL uses F.tab exclusively. Adapterr2 requires the actual returned table to match every prediction below;
otherwise it stops and reports a mismatch.

| GB ID/literal | Intended inverse decode |
|---:|---|
|1|named TRUE; positive constant|
|−1|FALSE literal; e.g.g_s((0,0),(2,0)), no separate g allocation|
|2|('g',1,(0,0),(1,1))|
|58|('g',1,(0,1),(2,0))|
|387|('g',1,(0,7),(7,0))|
|1626|('g',2,(0,1),(2,0))|
|3327|('g',3,(0,3),(7,0))|
|4762|('g',4,(0,1),(2,0))|
|6659|('g',5,(0,7),(7,0))|

For example, the first P0-B1 unit is−58 (coordinate1 absent in Q1(2,0)'s support7). The first M2 binary is
`−1675 −1626 0` (shown with typographic minus here; emitted ASCII `-`), with c=1,2,i=2 and signed literals
sorted ascending. These examples are checks, not a substitute for the own-table lookups/decode of ALL literals.
The output mapping includes all245(s,c,i) entries,s1..5,c1..7,i1..7, plus T/−T metadata and this inverse sample.

## 6. Tightened component checks, still not executed

Adapterr2 tests exact nested GB AST without a branch/solver: independent conjunction4cases; counter2 and
atleast3 for every prefix width0..8/all511input patterns each; signed/constant/aliased patterns; G3's no-exactly1
rule256cases, G4's two cardinality implications512cases and P4 threshold256cases. Wrong threshold outputs
for weights2/3 must be rejected. These strengthen controls only; they alter no BASE, header, unit or M_s byte.
The relaxed classical test remains evaluation-only1Q1P4ALO+7nonconstantQ1SB2 relaxations, never an unrelaxed
heavy SAT claim. Positive model/schema checks, hash sign-flips and table decoding still must pass after admission.
