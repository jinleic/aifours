# math-p0039 — bounded research continuation

**Outcome: partial. The all-orders conjecture is neither proved nor refuted here. Novelty is unknown.**

Question: Does every finite flag-transitive projective plane have to be Desarguesian?
Under the imported reduction, the target is to exclude the planar difference set
mu_(n+1) in F_p for every n>8 with p=n²+n+1 prime. No universal exclusion or
counterexample plane was found.

## Results and exact scopes

| Evidence | Interval in n=8 (mod 24) | Verification limit |
|---|---|---|
| Complete Python replay | [200000000000,251539607552) | Every stated decision recomputed |
| Paired C executions | [200000000000,2582236504064) | Entire interval not Python-replayed |
| Inherited C execution | [200000000000,10341223092224) | One entire-range run; only subsets corroborated |
| Complete Python boundary window | [1999859732480,2000201326592) | Separate window; no general-bound increase |
| Complete Python bit-boundary block | [2198910672896,2199111999488) | Separate window; no general-bound increase |

The complete Python arithmetic replay in this visit covers the contiguous class
n=8 (mod 24) in **[200000000000,251539607552)**. Each member has either an exact
proper factor of p or a complete ordinary residue 2^(n+1) mod p different from 1.
Together with the imported below-200000000000 baseline and congruence reduction,
this excludes non-Desarguesian flag-transitive planes of every order
**n<251539607552**, conditional on those imported premises and the usual correctness
assumptions for the exact computation.
The code and bounded replay commands are in claims.json. It is partial progress,
not resolution of the question.

A further complete Python replay covers all 14,233,088 decisions in the separated window [1999859732480,2000201326592), joining the last target block to the first continuation block without gap or overlap. The actual divisor 7 and full ordinary residue at n=2000000000000 are checked against both arithmetic logs. This does not fill the large gap after the general prefix. See evidence/epoch2/boundary-window.json and its independent replay command.

Python also completely rechecked all 8,388,608 decisions in [2198910672896,2199111999488), the block containing n=2^41. This tests the transition from 41- to 42-bit exponents and from 82- to 83-bit natural moduli. Both C digests matched. It is a second separated window, not a general-bound increase.

Two preserved runs report no unsieved base-two survivor on n=8 (mod 24) in [200000000000,2000000000000). Their complete decision digests agree over 8941 target blocks and 75000000000 target members. A capped continuation agrees through 2582236504064 over 2892 further common blocks. Assuming the imported premises **and correctness of these executions**, the combined order exclusion for non-Desarguesian flag-transitive planes is n<2582236504064. This is a preserved computational report, not a full Python replay or independent certification of that entire interval.

One inherited C run reports no unsieved base-two survivor in
[200000000000,10341223092224). **Conditional on the imported premises AND on
that single entire-range run being correct**, it gives n<10341223092224.
Its entire range remains unreplicated. The old header contains no binary hash.
New computations corroborate only the explicit intervals above. Counts and file
hashes establish bookkeeping and integrity, not correctness of omitted decisions.

The prior referee externally replayed the old no-sieve pow prefix only through
201440000000, and both old Python control flows only through 201200000000.
The inherited later-chunk/window statements are not promoted to externally
confirmed results here. The new Python replay stated above was run in this visit;
its external referee status remains to be determined.

## Imported premises and target fidelity

The ledger is evidence/PREMISES.md. The staged Thas–Zagier reader conversion,
Sections 1–2 and the numerical appendix, was rechecked. It explicitly reports
the baseline n<200000000000, the seven even base-two exceptions below 5000000000,
Kantor's classification-dependent reduction, and the errors in the apparent older
power-of-two/prime-power resolutions. The source hash is recorded in the staged
SOURCES.json. The original PDF and later full texts are not staged. The contract's
dated literature screen is background data; no new literature/novelty search is
possible offline.

Imported: Kantor (1987), relying on the classification of finite simple groups,
leaves a nonclassical Frobenius/sharply flag-transitive case with even n and prime
p=n²+n+1. Thas–Zagier identify this case with the additive planar subgroup
D=(F_p*)^n=mu_(n+1); n=2,8 give classical planes. Feit's valid conditions give
8|n and d^(n+1)=1 (mod p) for every positive divisor d of n. The identity
n³-1=(n-1)p gives ord_p(n)=3; taking d=n yields 3|(n+1). Hence n=8 (mod 24).
Feit's invalid power-of-two exclusion and Ott's invalid prime-power argument are
not used. The full below-200000000000 computational baseline is imported, not
rerun here.

Base-two necessity also has a short proof. Planarity makes the set of x with
x,x+1 in D a singleton. Inversion preserves it, so x=x^(-1)=±1. The value -1
would require 0 in D, so x=1 and 2 belongs to D. Thus 2^(n+1)=1 (mod p).
Passing this necessity alone does not establish planarity.

The book page image was checked. Its literal graph wording has two defects:
reflection-generated dihedral Cayley graphs are bipartite with two parts of size
p and degree n+1<p, so opposite-part nonneighbors have odd distance at least
three and diameter two is impossible. Also, an unspecified reflection set does
not characterize non-Desarguesian planes: classical Singer difference sets give
diameter-three incidence Cayley graphs (Li 2005, as cited in the supplied source
screen). The valid geometric reduction is credited to Kantor plus Thas–Zagier,
not to those printed graph assertions.

## Computations, controls, and arithmetic independence

The 33 supplied gzip parts reconstruct all three missing inherited logs, matching
every compressed/raw-part and concatenated manifest hash without importing the
producer code. Raw sizes are 9,239,886, 46,531,770 and 9,257,179 bytes. Replay
restores them from the delivered parts; none of the claim commands executes a
local binary. One of the inherited manifests was the producer's own delivery
manifest; these hashes prove integrity only.

The new 128-bit scan is derived from the inherited C program and keeps its
two-64-bit-limb, full-256-bit-product Montgomery arithmetic. The separate scan32.c
uses three 32-bit limbs and only 64-bit intermediate products for modular
multiplication, a different Montgomery radix (2^96), and Tonelli–Shanks roots
instead of cube roots. It includes/imports no producer code. Both share author,
compiler, OS, left-to-right exponentiation recurrence, hash format and CommonCrypto
SHA-256. Their independence is explicitly partial. The binary SHA-256 is in each
new log header and the source/binary build ledger is preserved.

Every decision hashes this 32-byte little-endian record: n:u64, q:u32, tag:u32,
residue:u128. For a factor decision, q is the actual smallest sieve factor and
residue zero explicitly means **uncomputed**; no complete power is claimed there.
Every unsieved decision hashes the complete ordinary residue, not a Boolean or a
Montgomery representation. Selected factor audits compute complete residues too.
Matching digests compare every such decision, subject to SHA-256's collision
assumption, but are not proof that the executions were correct.

The independent Python replay derives roots using Cipolla's algorithm and
Eratosthenes, and uses arbitrary-precision pow. It imports no scanner code and
executes no scanner binary. NumPy only stores the fixed-width digest records;
all modular exponentiation uses exact Python integers. A separate manual
exponentiation loop was checked on one complete benchmark block and all stored
wide vectors. That loop shares CPython's big-integer multiplication/reduction with
pow; it is a separate control flow, not separate underlying arithmetic.

The sieve rejects only 1<q<p. The 32-bit scanner checks that guard at every mark
and verifies q|p for every marked production member. Full Python replay derives
and checks all proper-factor classes in its stated blocks. Every block's exact
class size, start/end, ID and sieved+tested=count identity are checked; the identity
alone is only bookkeeping. Only a last common, consecutive, completed block is
admitted as a capped endpoint.

| Scope | Sample records | Factor / unsieved | Contiguous windows |
|---|---:|---:|---:|
| main | 40166 | 34631 / 5535 | 71 |
| extension | 12994 | 11240 / 1754 | 23 |

Every block contributes its first two and last two members. Every 128th block contributes its first 64 members, and a completed planned final block also contributes its first 64. Every member of those windows, including factor rejections, has its full ordinary power and actual smallest divisor recomputed and included in a window hash. These samples partially overlap the full Python prefix and do not certify the gaps between windows. We retain the declared prefix at its complete-block boundary. Exact endpoints, counts and full-residue hashes are in the sample-check JSON files.

Controls passed before main production:

* All seven isolated controls have exact witness checks. The verifying command
  is check_controls.py; make_controls.py is only a separate regeneration tool.
* Both new unsieved C runs covered every even n in [2,5000000000), exactly
  2,499,999,999 members, reporting precisely 2,8,24,90,512,134217728,297474474.
  All full-residue block digests agree. Python rechecks 1,384 recorded residues
  only. This covers the small-modulus unsieved path, p<2^65.
* All 9,999 even n in [2,20000) received Python full decision/power checks.
  The q=p self-factor corruption is rejected, preserving the prime controls.
* All 960 full-residue vectors passed, including 90 synthetic positive vectors
  at 65–94-bit moduli. These test the power routine at large widths, not natural
  n-shaped survivors at those widths.
* The full 67,108,864-member production-sized benchmark matched both C digests
  under Python replay; the first 8,388,608-member block also matched the manual
  Python control flow. Negative residue/hash controls failed as required.

## Survivors and mathematical attempts

No unsieved base-two survivor is reported in the completed new production scopes.
The inherited production run also logged none. Thus the survivor/elimination
table for those scopes has zero rows and zero unresolved logged cases. This is a
log fact for un-replayed orders, not independent evidence that no hit was missed.
The explicit machine-readable table is evidence/epoch2/survivors.json.
A future hit must be eliminated by an exact proper factor, valid divisor-power
failure, or another proof. Probable primality never eliminates a survivor.

The isolated exceptions are resolved exactly: n=2,8 have every ordered difference
checked; n=24,90,512 have explicit collisions inside D; n=134217728 has
p=2593*71119*97685839; n=297474474 fails both the congruence class and the valid
d=n power condition. See evidence/controls.json.

The closure lemma excludes factors 3,5,7,17,31 of n under the valid multiplier
premise by duplicating the unique difference-1 pair (2,1). It likely overlaps
classical multiplier work, including Hall (1947), and is not used in the scan.
For n=2^a, primality of p forces a=3^t. Exact factors for t=3,...,9 and the
n=512 collision exclude this family for 3<a<59049. Those factors probably
reproduce known Cunningham-type factorizations. This is a sparse-family result,
not a general bound of 2^59049.

The next exponent a=59049 received a bounded factor-progression search through
q<=10^14 without a witness. Its failure is not a primality/nonexistence result.
A supplementary 300-second search stopped at q=499603472252929 without a factor; the planned 10^15 bound was not exhausted. It gives no primality conclusion.
The raw search log's last_k is a loop cursor one beyond the tested index on
exhaustion; no claim depends on it. The fixed-filter lemma proves why these
methods cannot settle all orders: sufficiently large n=2^(3^t) pass every
divisor-power condition and any fixed finite factor sieve, whether p is prime
or composite. This asserts no counterexample plane.

A finite-field moment/Vandermonde argument gives the exact binomial criterion
in evidence/epoch2/MOMENT-CRITERION.md. It supplies no general inconsistency
proof and direct evaluation is too costly for these production orders. It is
likely classical and is not used to omit any candidate. No universal obstruction
was obtained from these or the staged Gaussian-period/Fermat-curve reformulations.
Its small controls retain n=8; n=24 first fails at t=4, and n=90,512 fail at
t=2. These are alternate checks of already known isolated exceptions.

An initial Python checker attempted to import SymPy, which is absent from the
active python3 despite the resource list. Replacing it with standalone Cipolla
root derivation removed that dependency; no package was installed.
Process discovery was unavailable when a temporary resource-balancing pause was
considered. No signals were sent; the Python prefix workers instead wait for
the faster C scanner to finish.

## Remaining gap and replay limits

The all-orders conjecture remains unresolved. Outside the exact Python prefix,
the new large-range statement depends on the preserved C executions; the larger
inherited endpoint still depends on a single entire-range execution. Sampling,
zero logged hits, hashes, and matching aggregate counts do not fully certify the
omitted arithmetic. The imported classification and baseline remain dependencies.
The best next verification step is a fully replayable exact certificate or an
external exhaustive reexecution for those remaining decisions. A universal solution
needs mathematics beyond the fixed filters. No continuation or refill is scheduled.

The final claim commands were run on an actual delivery-limited copy: 33 commands, 1257.646 seconds summed wall time, longest command 150.159 seconds. All required successes and deliberate nonzero failures were observed. This is a self-run delivery replay, not an external referee verdict. The tested copy contained 336 files totaling 38228609 bytes; the three skipped oversized inherited logs were reconstructed from their delivered gzip parts. See evidence/epoch2/snapshot-replay.json.

Each final command is Python-only and must run in <=300 seconds; the complete
set must total <=1800 seconds. Separated historical windows and redundant old
pow/manual chunk claims are archived rather than charged again to this replay
budget. Completed new sample logs have byte-exact deterministic gzip versions
below the 5 MB cap; their raw copies are removed only after byte-for-byte checks.
The packaging check enforces the 50 MB/2000-file limits and rejects missing
load-bearing artifacts. All work stays in this directory, with at most four
CPU-intensive scanner/replay workers; no network, delegation, installation,
credentials, commits, pushes, or external contact is used.

Status: complete. Updated UTC: 2026-10-16T00:01:23.122984+00:00.
Started 2026-10-15 21:23:55 UTC; deliverables due by minute 173,
2026-10-16 00:16:55 UTC; hard stop 00:47:55 UTC.
