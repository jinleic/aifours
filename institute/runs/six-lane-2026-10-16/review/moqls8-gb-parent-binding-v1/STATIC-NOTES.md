# MOQLS(8) GB parent binding v1: static notes

These notes were written before any execution, at 2026-10-18 07:35 PDT. The desk is parent-owned. It was
created at 07:17:00 PDT with exclusive mkdir.

This is an exact-formula binding: bytes, counts and SHA256 of the 16 GB template formulas and the six GB
strengthened formulas. It makes no SAT/UNSAT, transfer, n=8 or Problem-16 claim, and no solver or checker is run.

The worker adapter `code/gb_one_p4_r1.py` (952c761c…bd88c) and its outputs were not opened, copied or run. They
remain comparison targets only. The worker necessity note `review/GB_ONE_P4_NECESSITY.r1.md` (e4dd33f4…703ed) was
read once, for its stated conventions. The script never opens it.

## Frozen scripts (sha256 recorded before any execution)

- `scripts/bind_gb_v1.py`: `7818a04f2475cad69529e836b8572d5d775af95b7b09c4d3d05528a2c5c333f0` (56174 B).
  It runs in two modes:
  - `--selftest`: a pre-flight check. It runs the pins, the source checks, the n=5 storage control and
    synthetic composition/controls. It does no n=8 encode and writes only `receipts/SELFTEST.v1.json`.
  - generation: a single run.
- `scripts/launch_gb_v1.py`: `dcda4f42be08ef7e50546aa4b7d00c4fadf99785247aa6411d3b13c5302f0b2a` (11555 B).
  It is the single-run launcher. It runs the gate checks, then writes `receipts/PRE-EXEC.v1.json`, then starts one
  child, supervises it (SIGTERM only) and finally writes `receipts/POST-EXEC.v1.json`.
- Interpreter: `/opt/homebrew/opt/python@3.14/bin/python3.14 -I -B` (3.14.3, OpenSSL 3.6.4).

## Pinned inputs (verified by the script; it stops on mismatch)

| input | sha256 |
|---|---|
| `physics/…/moqls8-problem16/code/gram_b_r2.py` (GB) | `4b593e557fe5b26053537e7107ca5e7a11b3df8ce011bdf78981bc7e068beae0` |
| `…/evidence/n8_one_p4_templates_v1/MANIFEST.json` (WMAN) | `355b33801640e39ab86946c51ab58c9c843370083ca896dd6d8ee5b09e90fc74` |
| `…/review/P1_COLUMN0_BOOLEAN_NORMAL_FORM.r2.md` | `8ae0ac01de7ea5883111e8dcc4f84246813d8599b1e8af782e0498104a449e8f` |
| `review/moqls8-one-p4-parent-binding-v1/RESULT.json` | `65311ab0b3109412383b47113b36c6a4b3d74f8132fc334cb2f5194b480928b0` |
| `review/moqls8-one-p4-parent-binding-v1/parent_binding_v1.py` | `6b085b9050893171a2135baa22fc14e1ce8d0664cc8cf718d9dee3823ea75a51` |
| `review/moqls8-strengthened-parent-replay-v1/scripts/bind_v1.py` | `b010baa4dd5c7620f7c6215beeb052af80846bfd6c3ee0a80e8d8a235144786c` |
| `review/moqls8-strengthened-parent-replay-v1/BINDING.json` | `5e1116e8311bfe4b2e06554edd0c77fc564574b06c1320334373648171f5f98c` |

The pin for `parent_binding_v1.py` is the `script_sha256` that its own desk recorded in `PRE-EXEC.json`. The brief
did not list it.

## Exactly what of GB (`gram_b_r2.py`) is relied on

Line numbers refer to the pinned file. The script checks every quoted line for exact presence.

1. **`class F` (18–31).**
   - `new(key)` increments `n` and stores `tab[key] = n` when a key is given.
   - `c(*lits)` appends `list(lits)` to `cl`.
   - It has no other methods, no bases and no decorators (AST check).
2. **`encode` (34–228) creates its store by `F_ = F()` (35).** This is a module-global lookup made at call time.
   AST facts, all of which the script checks:
   - inside `encode` and all its nested functions, the instance `F_` is used only through `F_.new(...)` calls and
     through `F_.c(...)` calls that are expression statements, so return values are discarded;
   - it is assigned once and returned once (228);
   - it is never aliased, and `F_.cl`, `F_.n` and `F_.tab` are never read there;
   - the class `F` is referenced only by that bare `F()` call.

   Therefore the clause sequence, the clause order and the variable numbering do not depend on how `F.c` stores
   clauses.
3. **The constant `T = F_.new("TRUE")` (36).** It has id 1, and the unit `F_.c(T)` follows at 37.
4. **`glit` (89–97).** Equal cells give `T`. Distinct cells in the same row or column give `-T`. Otherwise the
   result is the lazily allocated variable with key `("g",) + (s,) + tuple(sorted((p, q)))` (94, 96).
   - For p=(0,c) and q=(i,0) with c,i ≥ 1, the name is `('g', s, (0, c), (i, 0))`. The binding reads every
     appended id from `F.tab` under exactly these keys.
   - Not relied upon: the G1 loop (137–145) calls `glit` for every pair of every square, so all g ids are
     allocated first. This predicts id = 1568(s−1)+49c+7i−5, i.e. GA id + 1. The prediction is recorded only as
     an observation.
5. **`main` (231–257) maps the flags to the call.**
   - The script evaluates main's own `ArgumentParser`/`add_argument` statements and its `Q`/`p4`/`fixg`/encode
     argument expressions (244–247) on
     `--order 8 --quantum 12345 --ngeneric 0 --p4 1 --sb2 --g5 --cnf NOT-WRITTEN.cnf`. Any file open by those
     statements is refused.
   - Result: `encode(8, [1,2,3,4,5], 0, [1], True, None, True, False, False)`, compared type-exactly with the
     brief's call.
6. **CLI serialization (248–253), which the sink reproduces.**
   - Header: `"p cnf %d %d\n" % (F_.n, len(F_.cl))`.
   - Per clause: `" ".join(map(str, cl)) + " 0\n"`.
   - Text-mode `'x'` file: the content is ASCII and `os.linesep` is LF on this host (both checked).
   - The name map is `json.dump({json.dumps(k): v ...})`. Its SHA is computed in memory and no file is written.
7. **Determinism.** `encode` iterates lists, ranges and `itertools.combinations` only. Sets and dicts are used for
   membership or lookup, and dict order is insertion order. So the bytes do not depend on the hash seed.

## The replacement, and why it cannot change the encoding

In a private module object built from the verified bytes, the global `F` is rebound to a subclass of that
module's own `F`. The subclass overrides only two methods:

- `__init__`: it adds the sink and sets `cl = None`, so any list use would raise.
- `c(*lits)`: it appends `(" ".join(map(str, lits)) + " 0\n").encode("ascii")` to a bytearray segment. A full
  16 MiB segment is frozen as bytes, and segment boundaries fall on clause boundaries. The method counts the
  clause and returns `None`.

`new`, `n`, `tab`, `encode` and all nested GB functions run unchanged. The base header is
`b"p cnf %d %d\n" % (F.n, count)`.

This argument is item 2 plus item 6. It is confirmed empirically by the **n=5 storage control**:
`encode(5,[1,2],0,[1],True,fixg=None,g5=True,allrows=False,allcols=False)`.

- n=5 is used because SB2 needs len(Q)=n−3. The CLI's `--order` choices are bypassed by calling `encode` directly,
  which is the same in-memory path as at n=8.
- The module's own list storage, serialized by main's lines through `io.TextIOWrapper(newline=None)`, must be
  byte-identical to the sink at segment sizes 64 KiB and 16 MiB. The vars, clause count and name table (including
  its order) must be equal too.
- A sorted-literal mutant sink must differ.

## Composition conventions (GA parent bindings; exact lines checked) and choices

- **Template T** = `p cnf V C+42` + GB body + 42 lines `%d 0`.
  - Order: i = 2..7 ascending, then c = 1..7 ascending.
  - Literal: `+v` if c ∈ WMAN `supports_row2to7[i−2]`, else `−v`, with v = GB `F.tab[('g',1,(0,c),(i,0))]`.
  - Source: `parent_binding_v1.py`, `for i,S in enumerate(supports,2): … units.append(v if c in S else -v)` and
    `'%d 0\n'`.
- **Strengthened `T.Ms`** = `p cnf V C+168` + GB body + T's 42 unit lines + 126 lines `%d %d 0` of
  `tuple(sorted((-a,-b)))`.
  - Order: i = 2..7, then (c,d) in `combinations(1..7, 2)`.
  - a = `g_s((0,c),(i,0))` and b = `g_s((0,d),(i,0))`, taken from GB's table.
  - Source: `bind_v1.py` and `BINDING.json`. The serialization string and the composition rule are checked, and
    the (i,c,d) row order is compared row by row.
- V = GB `F.n`. Every appended id is an existing GB primary id, so V does not change. There are no comment lines.
  Lines end in LF and literals are separated by single spaces.
- **Documented choices:**
  - "12 direct templates" is read as WMAN's 16 minus the four normal-form sources P1-B1/B2/B3/B5. Controls (c)
    and (d) run on all 16 templates and on the unit sections of the six strengthened formulas.
  - M_5 is hashed for reference only.
  - The GA ids in WMAN are used only in control (f), a cross-check of sign pattern and position. They never enter
    a GB formula.

## Controls (in memory)

Required, per the brief:

- (a) Negating each of the 42 units in turn, in all 22 formulas (924 mutants), changes the hash. No mutant equals
  any genuine hash.
- (b) Putting the M_3 tail (square-3 ids) into each s=2 formula changes its hash. For P1-B5.M2 the mutant must
  equal the genuine P1-B5.M3 hash, a composition-consistency identity.
- (b2) Flipping the first tail literal changes the hash.
- (c) Every appended unit and tail line is decoded through the inverse of GB's `F.tab` and must give the intended
  (s,c,i,sign) in order, with the two negative tail literals in ascending order.
- (d) Supports decoded from the unit lines without using positions must equal WMAN for all 16 templates (including
  the 12 direct ones). A first-unit flip must decode differently.
- (e) C_formula = C_base + 42 (+126) must equal body LF count + unit lines (+ tail lines). The body's LF count must
  equal its `" 0\n"` count and the stored clause count. The byte lengths must add up.

Added here:

- (f) Cross-check with GA, used only as a reference:
  - sign patterns equal the WMAN GA units;
  - GA unit positions follow 49c+7i−6;
  - the GA tail row order equals GB's;
  - the GA formula list equals the six;
  - the GA leaf RESULT reports `template_table_equal`/`units_equal` for all 16.

## Limits and gates

- **Child:** single-threaded. It self-aborts on peak RSS > 1 GiB, wall > 2700 s or SIGTERM. Its internal
  free-space backstop is 11.5e9 B, read at ≥10 s intervals. Its start gate is 12.0e9 B, following the parent's
  clarification for this in-memory job.
- **Launcher:** enforces the frozen gates: a fresh reading ≥ 12.2e9 B + 2 MB of growth before the launch, and
  SIGTERM when the in-flight free space drops below 12e9 B. It also sends SIGTERM at 2715 s. After any SIGTERM it
  waits at most 120 s and never escalates.
- Launches stop at 17:30 PDT.
- No CNF or proof bytes reach disk. The only outputs are `GB-PRIMARY-MAP.v1.txt`, `GBBINDING.json` and small
  receipts and logs, all created exclusively.
