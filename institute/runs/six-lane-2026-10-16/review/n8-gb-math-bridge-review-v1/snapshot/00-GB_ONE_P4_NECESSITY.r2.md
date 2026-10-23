# Independent GB counterpart of the n8 one-P4 leaves — frozen necessity r2

Status: encoding/generation package, NOT solver evidence or an n8 theorem. GB source is read-only:
`code/gram_b_r2.py`, SHA256 `4b593e557fe5b26053537e7107ca5e7a11b3df8ce011bdf78981bc7e068beae0`.
No GB edit is made. The new adapter is `code/gb_one_p4_r2.py`; its source hash is frozen separately before execution.
The contract's positive-answer gate requires two independently written encodings for every exhaustive step.
GA-only facts, GB hashes or an unqualified future kissat status do not by themselves close that gate.

## 1. Exact GB instance and same semantic leaf statements

The exact logical flag list is:

```text
--order 8 --quantum 12345 --ngeneric 0 --p4 1 --sb2 --g5
```

No `fixg`, `p4-all-rows`, `p4-all-cols` or ROWLEX is used. Direct in-memory call:
`encode(8,[1,2,3,4,5],0,[1],True,fixg=None,g5=True,allrows=False,allcols=False)`.
Thus P4 is only for square1 and only in row0's frame. Other squares may be classical or non-classical.
For each of the16 canonical Q1-column0 support tables, append42 signed PRIMARY literals obtained from GB's
OWN `F.tab[('g',s,p,q)]`. The adapter reads the semantic support sets from the frozen WMAN355b3380…fc74,
NEVER its GA `units` IDs. For the six inputs B1.M2,B2.M2,B2.M4,B3.M2,B5.M2,B5.M3 also append exactly126
negative binaries, i=2..7 and1≤c<d≤7, sorted signed literals within each binary. Each ID is a GB allocation.

These formulas assert the SAME support facts as their GA counterparts:
- Q1 template units fix every coordinate1..7 for each Q1(i,0),i2..7, in the row0 basis;
- M_s says each Q_s(i,0),i2..7, has at most one such coordinate; G3 gives nonemptiness, SB2 handles row1,
  and constants handle coordinate0. This is ONE column, not a globally classical square/K4 condition.

Every genuine normalised configuration at the corresponding accepted unified/T16 or normal-form leaf has a
canonical assignment satisfying these GB constraints. Conversely, no arbitrary GB SAT pattern is asserted to
supply vectors. Transfer/reduction acceptance and exact parent solves remain separate obligations.

## 2. Why each GB family is necessary

References below are to the pinned GB file.

- **Constants/G1 (89–97):** one explicit TRUE variable T is forced at36–37. Identical cells map to T;
  distinct cells sharing a row/column map to−T. Each real row/column is an ONB. No classical-net constraints
  appear because ngen0 makes the classical list empty. Primary nonconstant g variables name unordered cell pairs.
- **G2 (146–152):** pairwise MOQLS tensor-product orthogonality forbids two squares' inner products on the same
  distinct cell pair both being nonzero. Skipping a constant−T pair drops only a tautology.
- **Conjunction/counter definitions (99–135):** conj is iff its two inputs. `counter2` represents the running
  “at least1/at least2” predicates by full equivalence; its clauses are the elementary updates
  n1=(oldge1 OR l), n2=(oldge2 OR(oldge1 AND l)). `atleast3` similarly updates all three threshold predicates.
  Assigning these predicates their actual input truth values satisfies every definition.
- **G3 (160–173):** overlaps between any two fixed row/column ONBs have nonempty rows/columns. Orthogonal
  vectors cannot overlap in exactly one nonzero basis coordinate. The counter clause−ge1 OR ge2 expresses
  precisely “not exactly1”, both for rows and for columns. These are necessary support conditions, not PSD sufficiency.
- **G4 (174–183):** in any row/column frame, zero common support forces zero inner product; exactly one common
  nonzero coordinate forces a nonzero inner product. The two threshold clauses express those Parseval consequences.
- **G5 (184–207):** a vector with singleton support in an ONB frame is proportional to that basis vector; all its
  Gram zero/nonzero relations agree. `single` is exactly that singleton condition, and the two conditional
  equality clauses for each p express the same-ray consequence. All row/column frames are included.
- **P4 (208–214):** an actual Q1 weight≥3 entry in row0's frame sets at least one final threshold3 literal true.
  Only Q1's56 off-row0 points are considered. The accepted witness Q1(1,0) has exactly3 support coordinates.
- **SB2 (215–227):** ngen0 leaves coordinates1..7. The allocation is Q1→123,Q2→4,Q3→5,Q4→6,Q5→7,
  exactly the accepted aligned(1,0) pattern. T/−T handling of coordinate0 changes syntax, not meaning.

The written Boolean normal-form proof's local G2/G3 premises and primary relabelling apply to these same
support rules. GB has a different canonical auxiliary extension through its threshold counters and anonymous
single variables. This observation is a necessity argument, NOT a new parent acceptance of that transfer.

## 3. Explicit differences from GA/F_one

1. GB has an explicit TRUE variable and retains numeric constant literals/tautologies; GA uses Python Boolean
   constants and simplifies clause construction. IDs, variable count and clause count are different.
2. GB independently constructs anonymous conjunctions and unary sequential threshold counters for cardinality;
   GA uses named conjunctions and direct no-singleton/six-subset clauses. Their auxiliary assignments differ.
3. GB generates P4 ONLY for square1. GA F_one retains unused one-way P4 implications for squares2–5 after deleting
   their four ALO clauses; they admit all-false flags and impose no primary support restriction. GB omits that
   irrelevant auxiliary family. The primary one-P4 necessity statement is the same, not a byte-clause identity.
4. GB contains NO ROWLEX. Omitting this symmetry-breaking constraint only WEAKENS the corresponding
   normalised problem. It cannot exclude a valid leaf configuration. Full template masks are already sorted,
   but no undocumented GB lex implementation or auxiliary-ID identification is assumed.
5. Generic classical variables have a different label space in GB, but ngen0 means none is present here.
6. GB's own primary-name table is authoritative for EVERY appended literal. No GA primary/auxiliary IDs are
   translated by offsets or reused. Counterpart GA hashes are reference metadata only.

No H3, fixed classical data, P4 on another square/frame, row sorting, extra rank rule or new physical hypothesis is added.

## 4. Storage adaptation and exact in-memory controls

The GB file is unchanged. The adapter subclasses only its clause-storage F: F.new/encode are inherited without
logical edits, while F.c writes exactly the original CLI serialization `join(str(lits)) + ' 0\\n'` into a RAM bytearray.
No literal filtering, simplification, sorting or deduplication occurs in the BASE emission. A small n3 storage
control compares original GB lists versus this sink: every byte, clause/variable count and own name table must match.
This is an I/O control, not an n8 result. Full generation is guarded at1GiB selfRSS/2700s/17:30 science stop;
fresh12.2e9+growth, in-flight12e9 and9.5GiB lane gates remain. No CNF file is written.

**Nonvacuous component controls:** adapterr2 extracts the EXACT pinned nested GB functions as AST, without
changing GB. Fixed-input propagation (no branch/solver) tests conjunction4independent cases; allprefixwidths0..8
forcounter2/atleast3(511cases each); signed/constant/aliased inputs; G3's no-exactly1 rule256cases; G4's two
implications512cases; P4 threshold256cases. Wrong threshold outputs atweights2/3 must fail. These test heavy
thresholds absent from a purely classical positive, but do not replace necessity audit or prove heavy SAT.
No component is yet reported as run/PASS. Adapterr1 is preserved. Formula emission, flags and all byte-order
conventions are UNCHANGED; r2 adds controls/inverse samples only. See GB_ONE_P4_CONVENTIONS.r1.md for the
pre-comparison header/unit/M_s/T conventions and source-derived inverse predictions. Parent hashes will not
be read/adapted to; any independent mismatch must remain a reported mismatch.

**Relaxed classical positive control:** construct five row0-standard MOLS(8) over GF(8), modulus x^3+x+1,
L_s(r,c)=c XOR a_s*r with slopes a_s=(1,4,5,6,7). Independently check every row/column permutation and all64
symbol pairs for each square pair. Fix each GB g bit to classical symbol equality, T=true, and extend auxiliary
counter/conjunction/singleton bits deterministically by forced clause evaluation. No search/solver is used.

A classical set CANNOT satisfy the unrelaxed non-classical witness P4/SB2. The control therefore ignores for
EVALUATION ONLY exactly one Q1 P4-ALO and seven NONCONSTANT Q1-SB2 unit clauses; the coordinate0 tautology
is retained. Every other base clause must be verified. All eight ignored clauses still remain in the generated
base bytes and formula hashes. The manifest records their exact indices/literals/hashes and which are actually
false. This control makes NO claim that the unrelaxed GB base is SAT. If the model extension cannot be fully
verified inside caps, the run fails/records the obstruction rather than faking a positive control.

**Hash controls:** flip one template unit in P0-B1 and one M2 literal in P1-B1.M2, preserving clause counts;
both full formula hashes must change. These are BINDING controls only, not SAT/UNSAT or proof-checker tests.
**Decode controls:** every appended unit and every M_s literal is checked against the inverse GB OWN table;
the245(s,c,i) primary entries and TRUE constant are output as a mapping table, alongside the full own names.

The hash manifest contains16+6 inputs, exact flags, counts, body/name/mapping hashes and control receipts.
All formula hashes are PLANNED input identities, never measured solver/checker-feed hashes. Parent independent
mapping/binding and GB solves/checks remain necessary. No native slot, solve, proof, theorem or novelty claim is supplied.
