# Independent joint extension search — source-only freeze

`ext_search_joint.py` implements `ext_search_joint_v1`. **Unexecuted:** no
compilation, tests, formatter, probe, or search has been run. Normative input is
`ext-search-spec-v2.md`, superseding v1, plus certificate-format-v2 section 1
(G1) and the parent's 4096-started-chunk/post-publication amendments.

## Method and completeness

Work directly over Z_n. Item `x*n+v` means row x must use value v once.
Option `(c,w)`, c>0, hits all k items `(x,(D[x][c]-w)%n)`. Fixing f[0]=0
covers `(x,D[x][0])`; chunk digits fix columns 1..m. An active option has an
unassigned column and no covered item. Disabling an option decrements all its
item counts; a packed trail reverses exactly those changes on backtracking.

At each node scan uncovered items in index order and choose minimum active
count, retaining the first tie. A zero count is a dead leaf. Branch over its
active options in increasing column order (there is exactly one possible w for
a given item and column). A fully covered leaf is directly rechecked against
EXT(D) and its fixed chunk before retention; failure is INTERNAL_ERROR.

Any extension of a partial assignment contains exactly one option hitting the
chosen item. Thus these branches partition its extensions: none is lost and no
extension occurs twice. Every selected column covers k previously uncovered
items, so depth is at most r=n-1-m; all covered implies all n columns assigned.
Forced-prefix conflict is a dead root. Exhausting the tree therefore enumerates
exactly that chunk. Chunk base-n encoding partitions the requested range.

The tree includes the root, dead leaves, and solution leaves; forced assignments
are preprocessing, not extra tree nodes. An inconsistent prefix still has one
dead root. Search and estimate visit precisely this same tree. Each chunk starts
`random.Random(seed)` anew; its probes share that stream. Uniform child ranks
produce the Knuth recurrence `1+b*child_estimate`, including terminal-node 1.
Per-chunk means use complete probes only. A sampled witness is verified,
retained, and immediately stops the job, rather than being hidden in an estimate.

## CLI, output, and exit codes

Run later, from a separately verified fresh job directory:

```text
python3.14 -I -B /absolute/path/ext_search_joint.py --raw PATH --raw-sha256 HEX --m M --chunk-lo LO --chunk-hi HI --max-solutions K --budget-s S [--mode search|estimate] [--probes P --seed SEED]
```

Each flag occurs at most once, exclusively in flag/value pairs. `0<=m<n`;
`0<=LO<HI<=n**m`; K>=0 (0 unlimited); finite `0<S<=10000`. Estimate requires
P>=1 and integer SEED. Search accepts optional individually supplied probes/seed
values, validates them, and does not use them. HEX is 64 case-insensitive hex
characters. G1 retains Python's existing integer-string conversion limit.

Only plain `result.json` is created, with O_CREAT|O_EXCL|O_NOFOLLOW. Canonical
JSON is byte-identical to `json.dumps(obj,sort_keys=True,separators=(',',':'))`
plus LF; stdout normally contains those exact bytes. Solutions are sorted and
unique; their hash binds the compact ASCII list. `extra={}`. Unestablished
metadata is null; a loader lacking `__file__` gets a null informational program
hash. Normal standalone use hashes the source file. No human-readable dates
or timestamps are generated.

| Status | Exit |
|---|---:|
| COMPLETE / ESTIMATE | 0 |
| STOPPED_AT_SOLUTIONS | 1 |
| BAD_INPUT / INPUT_PIN_MISMATCH / IO_ERROR | 2 |
| NOT_DM | 3 |
| INTERNAL_ERROR | 4 |
| INCOMPLETE_BUDGET | 5 |
| INCOMPLETE_OUTPUT | 6 |

Stop immediately at the Kth retained solution, leaving its chunk NOT_COMPLETE.
Retain at most 4096 solutions and 4096 started chunk records. Discovering the
4097th solution, or attempting to start the 4097th chunk, stops with exit 6.
Only started chunks are listed. Finished estimate chunks keep ESTIMATE records;
an interrupted estimate's last chunk uses NOT_COMPLETE/nodes/solutions, with no
partial estimate. A serialized result over 16 MiB instead produces compact
INCOMPLETE_OUTPUT with empty solutions/chunks and the hash of `[]`.

The shared budget starts on entry to main, including argument parsing, setup,
serialization, and publication. Check every node, during setup, throughout
encoding, before first write, and after file/stdout publication. **Never rewrite
an already-written artifact.** If publication consumes the remaining deadline,
return exit 5 even if the immutable JSON still says COMPLETE/ESTIMATE (or stopped
at a witness). Such a status/exit mismatch is ERROR/UNKNOWN, never acceptance.
Publication I/O failures similarly try a structured IO_ERROR; existing or partly
written artifacts are not replaced. A failed device or pre-existing result may
make file/stdout equality impossible; the supervisor must reject that outcome.
Already established input/internal errors retain their specific error status.

## Exact resource accounting

Let C=4096, I=kn, M=n(n-1), r=n-1-m, and
`T(r)=sum(r!/(r-j)! for j=0..r)`. Every item has at most one option per free
column, hence a search has at most T(r) nodes. For estimate, P probes visit at
most P(r+1) nodes. Set N=T(r) in search or N=P(r+1) in estimate, and
`b=max(1,ceil(bit_length(N)/8))`. Let h and d be array('H') and array('d')
item widths in bytes (2 and 8 on the intended macOS CPython build).

The **exact allocated element-payload formula** for retained search state is:

```text
B = [h(k+1)+1]M + (h+2)I + (C+1)n + C(b+h+d+1).
```

This accounts for: incidence table hkM; trail hM; active M; counts hI; matrix
and covered 2I; assignment n; retained solutions Cn; ledger nodes Cb, solution
counts Ch, estimates Cd, and status bytes C. It includes the full capacities,
not merely used records. Publication additionally allocates exactly O=16,777,216
payload bytes. Raw parsing precedes these buffers and releases raw bytes before
publication, including on rejection.

For a whole owned-data upper bound including Python overhead, use the following
explicit parameterized formula; Python does not specify portable exact RSS:

```text
A + H + max(4R+I+260*Hb+L(13)+2L(121)+2J(4R),
            B+O+E+(r+1)F+V)
E = 2L(C)+C*L(n)+Cn*J(7)+floor(C/2)*p
    +C*[D(5)+J(ceil(log2(n**m+1)))+J(bit_length(N))+J(13)+Hf].
```

R=1,048,576. A is argv and parsed-scalar storage; H is fixed imported/program
object and packed-buffer-header overhead; Hb/Hf are bytes/float object
headers; p is pointer width; L(t)/D(t) bound allocated list/dict storage at
length t, including allocator growth; J(t) bounds a t-bit Python integer; F
bounds one DFS frame plus its suspended candidate generator and fixed scalar
locals; V bounds JSON encoder/IO temporaries for one emitted token, including
integer-to-decimal workspace. All are runtime-layout terms, not omitted payload
buffers. E deliberately allows uncached small integers and both record schemas.
The parse term permits two adjacent token lists and optional-sign copies.
Allocator arenas, interpreter baseline, OS stacks, and runtime layout must be
added/measured separately for a process-RSS reservation; no exact-RSS claim is
made by the source-only figures below.

### Exact counted per-node work bound

Define one unit as one packed-cell read or write. Charge an incoming branch's
assign/undo pair to its child; charge candidate enumeration to its parent.
Let `U=min(M,n+k(n-2))`. A selected column disables at most n options, and each
selected item adds at most n-2 outside-column options. Only first disables
update counts and enter the trail. Therefore a non-solution node costs at most:

```text
W = 2I + 2(n-1) + n + 2k(n-1) + 4k + 2U(3k+2) + 2.
```

These terms cover item selection; candidate enumeration; column and item
invalidation probes; selected-item marks; disable/restore counter work; and
assignment writes. A retained leaf additionally costs at most
`2I+3n+m+1` cells for direct recheck and copying, hence the uniform bound
`W_all=W+2I+4n`. Scalar/index/loop operations have constant multiplicity per
counted operation; bigint costs additionally depend on the displayed bounded
node/index/estimator integers. This is an exact logical-operation upper bound,
not a machine-cycle promise. Input validation, table construction (2kM matrix/
incidence accesses), forced-prefix setup, ledger flushing, and output assembly
are separate once-per-input/chunk/publication work, not hidden search nodes.

Search-mode figures below use m=0, the worst node-counter width for each n;
other m may reduce b. They are payload bounds, not measured RSS.

| (n,k) | b | B bytes | B+O bytes | W | W_all |
|---|---:|---:|---:|---:|---:|
| (39,6) | 19 | 305829 | 17083045 | 11505 | 12129 |
| (21,5) | 8 | 169741 | 16946957 | 4437 | 4731 |

## Desk-check map (source line numbers; not exercised verification)

| Specification section | Source lines |
|---|---|
| v1 §1 / v2 Input: read once, same-byte pin, limits, G1, DM | 149–220; 674–688 |
| Certificate format-v2 §1: G1 | 168–205 |
| v1 §2 / v2 Problem: normalized EXT(D), independent leaf recheck | 368–398; 424–452 |
| v1 §3 / v2 Chunking: arbitrary m, base-n digits, range/order | 368–398; 507–530; 682–686 |
| v1 §4 / v2 Arguments: exact flag pairs and domains | 72–131; 682–686 |
| v1 §4 / v2 Tree/estimator: deterministic joint tree, full Knuth probes | 322–365; 400–492; 507–530 |
| v1 §4 / v2 Immediate K / estimate witness / shared deadline | 41–59; 424–452; 546–581; 635–660 |
| v1 §5 / v2 Retention/output: exact keys, hashes, caps, canonical output | 18–69; 134–146; 233–289; 495–505; 533–660 |
| v1 §5 / v2 Status/exit/errors, fail-closed publication | 24–30; 594–660; 663–711 |
| v1 §6 / v2 Agreement/claims | Lexicographic export/digest: 495–505; 533–538; no comparison or gate is run here |
| v2 Current artifacts | Provenance only; no beta program was consulted or executed |
| Parent amendments: 4096 chunks, partial estimates, immutable late-publication failure | 252–289; 507–530; 594–660 |

Ambiguities resolved: v2 overrides v1's m<=3 and delayed-K semantics; earlier
completed estimate records remain ESTIMATE; seeds reset per chunk; optional
search-mode estimator flags are accepted/validated; unavailable metadata is
null. Parent-authorized post-publication exit 5 takes precedence over matching
a pre-write success code without altering the immutable artifact. The stated
RAM unit distinguishes exact packed payload from runtime-dependent process RSS.

Independence: no other producer/search engine, run, or institute source was
read. The initial certificate-format read incidentally returned later sections;
only its section 1 supplies the parsing contract. Nothing is scientifically
qualified by this source-only freeze.
