# Independent LS(7) 147-main-class completeness check

**Technical checks: PASS. No theorem verdict.** The pinned class file
`898065c8a592a5a3ed1103a2657e3cff25f9588514ad3d286d441dedc95a8158`
contains 147 valid reduced Latin squares, with 147 distinct canonical keys. Every claimed
|Par| and reduced-orbit count matches independently derived values. Their orbit-size sum
is **16,942,080**, matching the previously completed parent Latin-backtracking count.
An additional explicit union check finds exactly 16,942,080 distinct reduced squares and
**zero cross-class duplicate keys**. All science used pinned copies; no lane code was imported/executed.

## Normalization and free action

Write a square as its 49 triples T={(r,c,L(r,c))}. The paratopism group is
G=S7 wr S3: independently relabel each coordinate and permute its role. Par(L) is its
stabilizer of T. A normalization flag consists of an ordered assignment of the three
coordinate classes to (row,column,symbol), an origin point, and an ordering of the six
other points on its chosen row line. There are 6*49*720 = **211,680** flags.

For a conjugate square M and origin (r0,c0), write beta=(c0,ordered other columns).
Define lambda(M[r0,beta[j]])=j and rho(r)=lambda(M[r,c0]); these are permutations.
Set R[rho(r),j]=lambda(M[r,beta[j]]). This is an explicit isotopy of M and is reduced.
Thus each flag uniquely specifies a paratopism sending itself to the standard flag
(role order row/column/symbol, origin(0,0), row0 ordered by columns0..6) of R.
The 36 interior digits determine R uniquely, so taking their least base-7 key is exact.

**Freeness.** If h in Par(L) fixes a flag, it fixes the ordered roles and all seven ordered
points of the chosen row. Each of the column/symbol labels occurs there, so both those
coordinate permutations are identity. Any point is uniquely determined by its column
and symbol (the Latin property); therefore every point, and hence every row label, is
fixed. Thus h is identity. This also shows the action on the 49 points is faithful.

**Fibres and coverage.** Normalization is equivariant. Flags F,F' give the same reduced
square precisely when g(F')^-1 g(F) is an autoparatopism carrying F to F'. Conversely,
an autoparatopism preserves the normalized square. The fibres are therefore free Par(L)
orbits, each of size |Par(L)|. Every reduced square paratopic to L occurs: pull its standard
flag back through a paratopism. Consequently the image has exactly 211680/|Par(L)| keys,
every fixed key has multiplicity |Par(L)|, and its minimum is a complete main-class invariant.
Distinct minima give disjoint main classes. Equality of their orbit-size sum with the full
reduced-square count proves coverage; no assumption on cycle-switching connectivity is used.

## Independent implementations and binding

- `src/ls147_norm.c`: construct all211680 images per class, check each is Latin/reduced,
  check all induced label maps are bijections, sort exact128-bit keys, and count every key's
  multiplicity. Every class has identical min/max multiplicities, equal to both its canonical
  and input-key multiplicities; each input is already its class's canonical representative.
- `src/ls147_autpar.c`: separately enumerate isotopisms from each of the six conjugates to L.
  The image of row0 and a column permutation beta force gamma via row0 and alpha via column0;
  all49 cells are then tested. No normalization keys are used. Found maps are distinct point
  permutations containing identity and closed under **4,157,981** ordered compositions in total.
  All147 explicit orders equal the normalization multiplicity and the claimed |Par|.
  The cyclic-table control has |Atp|=294 and |Par|=1764=6*7^2*6, orbit120.
- `src/ls147_check.py`: separate stdlib parser/Latin validator, bindings and control receipts.
  All per-class keys/counts/groups are recorded in `verdicts/verdict_main.json` and `result.json`.
- The prior full count is reused, **not rerun**. Parent `k1par_nets_v2.c` SHA
  `fae1ebe0f34471d1bb78ca4743ebb2eff523ce9120a6b09493ea71e96d0c2617`
  increments nLS before every mate test (line167); fill visits all legal36 interior choices
  (lines177-187), with row0/column0 fixed (lines252-258). Its output SHA
  `9edb96355f8bbf445b29e2ea9d3c4c1f5bceea0a69a6c3473bb118990f5accd7`
  records reduced_LS7=16942080. The receipt binds source, binary, output and exit0
  (182.52s wall,193019904B RSS). Hash chain: parent RESULT -> route1 receipt -> code/output/time;
  every required link and the binary/stdin hashes match (`inputs/MANIFEST.json`).

## Source labels and K2 symmetry

Egan-Wanless, https://arxiv.org/pdf/1406.3681v2 (pinned text SHA
`4d0d009e6f9f3a573c37c1e3da681de2c4a8212b46ca243b05c8ba4e37251965`):
lines64,143-174 define species/main classes as paratopy classes; lines185-187 define
reduced lists/sets. For k=1 both are the same single reduced Latin square; Thm3.1 has
RS=RL and Thm3.2's factor is 7!*7*3*2*1=211680. Tables6/8 (text lines754/838) both give
(7,1): **16942080 reduced /564 isotopy /324 trisotopy /147 paratopy classes**.
Do not confuse maximal1-MOLS (bachelor squares): Tables5/7 give16765350 and141 main classes;
the difference176730 equals the parent's independently counted L1_with_mate.

No K2 issue found in section3 of frozen `GRAM-ENCODING.r1.md` (SHA
`6724528aeb3ea1600fea423f0818c6b81a1bcc75fad50cbb9676fe0af00cf672`).
A paratopism is a point bijection between the classical3-nets of L and L'. Transport BOTH
quantum assignments by it. The new rows, columns and symbol lines are old ONB lines;
mutual tensor orthogonality is just reindexed, and projective-ray multisets (non-classicality)
are unchanged. The Gram conditions' incidence/count/support formulations transport as well.
This is existence transport using a classical3-net, not an assertion that arbitrary
conjugation belongs to the source's narrower QLS set-isotopy definition. It does not
validate G4's derivation, the encoders, or any UNSAT result. The pinned K2 drivers parse
these keys by the same row-major36-interior-digit convention.

## Controls (record indices are zero-based)

| Fixture | Intended observed outcome |
|---|---|
| Exact duplicate: index5 := index4 | Canonical distinctness FAIL;211680 union duplicates; naive sums still match |
| Disguised duplicate: index6 := another member of index2's class | Raw strings distinct, but canonical distinctness FAIL;105840 union duplicates |
| Corrupt one entry at index10, cell(1,1),0->1 | Latin/input-validity FAIL at index10 in Python and both C programs |
| Swap count/Par claims at indices2,4 | Summed counts/internal consistency still PASS; independent per-class Par/count bindings FAIL at exactly2,4 |
| Change Par claim1->2 at index9 (count changed consistently) | Par/count bindings FAIL at exactly9, despite true coverage still PASS |
| Drop index146 | Coverage/total checks FAIL; union16927968 |
| Replace all147 by other reduced paratopic members | All147 keys change; canonical keys, counts, explicit groups and full coverage match reference |

All specified expected outcomes occurred. Rejection is the named FAIL field in each
verdict, not the process exit (all runs exited0 after producing readable receipts).
The invariance control's literal-representative diagnostics are false: none of its keys
is canonical and the exact cyclic-table key is absent; its structural checks all pass.

## Execution, scope and deviations

Main normalization measurement (before any large allocation):4.21s/5586944B RSS.
Main union:5.17s/276676608B RSS; explicit groups:0.51s/2408448B RSS.
One busy scientific process at a time; peak observedRSS276676608B (<1GiB).
All29 completed execution receipts, exact argv/exit/runtime/RSS and artifact hashes are in
`result.json`/`runs/`. Compiler `TMPDIR` was this slice's `tmp/` and `-save-temps=obj`
preserved .i/.bc/.s/.o; observed per-user xcrun_db timestamp did not change across builds.
Approximately2MB of evidence before final receipts; all sampled free-disk values exceed12e9B.
There was no continuous shared-disk monitor. No timeout, kill, external contact, paid API,
Git mutation, or intentional deletion occurred.

**Operational deviations are not hidden:** initial source creation used the write tool
without an O_EXCL attestation, and `ls147_check.py` was edited three times before first
execution, contrary to the literal creation-only contract. External clang/time output
creation was nonexclusive at prechecked fresh paths. Early read-only scoping used shell
read/list/search commands and inherited TMPDIR; mandatory memory/skills/policy reads were
late. The lane draft changed during scoping; final checks use the frozen r1 pin.
All deviations are detailed in `result.json`. No pre-existing lane/parent evidence was
modified or overwritten. These are technical check results only; parent retains every
theorem/certification verdict. No novelty claim or unrestricted M(7) conclusion is made.
