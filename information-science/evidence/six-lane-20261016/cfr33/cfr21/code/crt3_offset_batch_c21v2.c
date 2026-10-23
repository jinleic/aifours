/*
 * crt3_offset_batch_c21v2.c
 *
 * Catalog consumer and batch solver for the CFR21 common-parallel-line offset
 * family of notes/offset-arcs-protocol-v1.txt (sha256
 * cd7de0679b8c9d1b1d3ca3eb93c7ab88c734badaa721a8c48a7d7d79a4a76ec5).  Family
 * goal: a cyclic (Z_21,7;1) difference matrix.  All matrix arithmetic is
 * cyclic mod 21, never GF(21).
 *
 * PROVENANCE.  The exact GF(3) + Gray-code core (P1-P8) is a port of the
 * separately authored code/crt3_graycheck_c21v1.c (sha256
 * 5c3719fa85dfb2969a19bd1087d74ae07c7d9296c735d3dac90723c359e1a411), which is
 * NOT edited.  It keeps the same equalities and forms, Gauss-Jordan with
 * certificate, nullspace basis, greedy form basis with lambda, section,
 * self-checks, rank cap, sign fix, sparse Gray traversal with periodic
 * recomputation and direct witness check.  Port changes: v1's process exits
 * became return codes, and every per-pattern variable lives in one struct
 * (ge) that eng_reset zeroes before each pattern.  Port map, v1 -> v2:
 *   validate_beta -> eng_validate_beta, build_crt -> eng_build_crt,
 *   build_rows -> eng_build_rows, eq_eliminate -> eng_eq_eliminate,
 *   check_equalities -> eng_check_equalities, build_basis -> eng_build_basis,
 *   compute_G -> eng_compute_G, ineq_basis -> eng_ineq_basis,
 *   check_lambda -> eng_check_lambda, build_section -> eng_build_section,
 *   check_section -> eng_check_section, build_lists -> eng_build_lists,
 *   build_dm -> eng_build_dm, dm_ok -> eng_dm_ok,
 *   recompute_check -> eng_recompute_check,
 *   traverse -> eng_traverse + scalar_report,
 *   on_solution -> on_solution_scalar | on_solution_batch,
 *   poll_build -> ENG_POLL (returns instead of exiting);
 *   read_beta_file, parse_beta and print_y_forms are unchanged in substance.
 * The catalog consumer, canonical-pair enumeration and batch driver are new
 * and were written from the protocol text only.  The author read no
 * primary-lift source or result (crt3_lift_c21v1.py and its runs) and no
 * catalog-generator source.  C11 + POSIX (_XOPEN_SOURCE 700), no libraries,
 * no heap allocation.
 * NOT compiled or executed by its author.  Every statement below was derived
 * by hand and must be confirmed by Main.
 *
 * SCOPE.  ZERO for a case means that no alpha in F_3^(7x21) makes
 * CRT(alpha, beta) a (Z_21,7;1) difference matrix for that exact beta.  A
 * completely ZERO range is restricted one-program evidence about the
 * canonical cases of one frozen catalog until it is independently checked.
 * It is never an unrestricted CFR, difference-matrix or MOLS nonexistence
 * claim, and never a novelty claim.  UNKNOWN keys are undecided.  FOUND is a
 * producer claim: Main re-checks the written matrix with the copied checkers.
 *
 * ================================================================== CORE
 * P1 D in Z_N^(K x N) is a (Z_N,K;1) difference matrix iff, for all rows
 *    i < j, c -> D[j][c] - D[i][c] is a bijection onto Z_N.
 * P2 N = 3Q, gcd(Q,3) = 1, D = CRT(alpha, beta).  Let C(i,j,rho) = {c :
 *    beta[j][c] - beta[i][c] = rho mod Q}.  P1 holds iff (a) |C(i,j,rho)| = 3
 *    for every i < j and rho, and (b) on each C the three alpha differences
 *    are distinct.  (a) concerns beta only.
 * P3 a, b, c in F_3 are distinct iff a + b + c = 0 and a != b.  So each
 *    triple (its columns in increasing order) gives one EQUALITY
 *    dlt_1 + dlt_2 + dlt_3 = 0 and one FORM dlt_1 - dlt_2 != 0.
 * P4 Fixing the gauge alpha[0][*] = alpha[*][0] = 0 loses nothing (it is a
 *    free action of order 3^(N+K-1)).  Unknowns: alpha[1..K-1][1..N-1].
 * P5 [A | I] is reduced to [R | P].  CHECKED: RREF structure, R = P A, and
 *    A b = 0 for the nullspace basis.  G[e][m] = l_e(b_m).  A greedy basis of
 *    G gives lambda, CHECKED for every form.  A section M is built, CHECKED
 *    A M = 0 and l_sel(M u_k) = u_k.  Lifts exist iff
 *    Y = {y in {1,2}^r : sum_k lambda[e][k] y_k != 0 for all e} is
 *    nonempty, where r = ineq_rank.
 * P6 The symmetry x -> -x means only y_0 = 1 is visited.
 * P7 Reflected Gray order over {1} x {1,2}^(r-1), with sparse residue
 *    updates.  Residues are recomputed in full every 2^16 steps and at the
 *    end; the visit count and final Gray word are checked.
 * P8 Every point of Y becomes D = CRT(alpha, beta).  D is checked against P1
 *    on ALL row pairs, and D mod Q = beta, D mod 3 = alpha are checked,
 *    before anything is written.  Rank cap: r > RANK_CAP is UNKNOWN, never
 *    an exclusion.  Full proofs: header of crt3_graycheck_c21v1.c.
 *
 * ================================================================ FAMILY
 * B1 Pattern.  Rows i = 0..6, column 7t + c (t = 0,1,2, c in F_7):
 *    beta[i][7t+c] = i*c + f_t(i) mod 7, where f_0 = 0 and f_1, f_2 are
 *    normalized (f(0) = f(1) = 0).  For i < j and each block t,
 *    c -> (j-i)c + f_t(j) - f_t(i) is a bijection of F_7.  So every residue
 *    occurs exactly once per block, P2(a) holds for all offsets (a violation
 *    is an INTERNAL error), and every triple has one column per block.
 * B2 ARC filter (protocol proof).  Suppose four rows share
 *    beta_i(c) - beta_i(d) for two columns.  Their full differences have only
 *    three F_3 digits, so two of those rows have equal full row-pair
 *    differences at both columns, contradicting P1.  For this family the
 *    condition is that f_1, f_2 and f_1 - f_2 are ARC, where f is ARC iff,
 *    for every s in F_7, no value of i -> f(i) - s*i occurs more than 3
 *    times.  The zero function is not ARC; ARC is closed under negation.
 * B3 Group G: 252 actions (a,b,l) with a,l in 1..6 and b in 0..6, index
 *    ((a-1)*7 + b)*6 + (l-1), identity (1,0,1) = index 0:
 *      T(f)(i) = l*(f(a*i+b) - f(b) - i*(f(a+b) - f(b))) mod 7.
 *    Applied to f_0, f_1, f_2 this is the composition of the DM operations:
 *    row i <- row a*i+b; subtract row b from every row; multiply every entry
 *    by the CRT unit L (1 mod 3, l mod 7); then in block t reindex
 *    c' = l*a*c + l*(f_t(a+b) - f_t(b)).  Each operation preserves P1 and is
 *    invertible, so lifts correspond bijectively.  These are
 *    validity-preserving cyclic-DM operations, not CFR row-isotopy claims.
 *    T(f) = l*Nrm(f o sigma), with sigma(i) = a*i + b and
 *    Nrm(h)(i) = h(i) - h(0) - i*(h(1) - h(0)), which kills affine
 *    functions.  Hence T is F_7-linear, composition stays in G, and G acts as
 *    a group.  T preserves normalization, ARC (multiplicities of f(i) - s*i
 *    move between slopes) and P23.  For f != 0, T_(1,0,l) f = l*f != f when
 *    l != 1, so Stab(f) meets the scaling subgroup trivially: |Stab| <= 42
 *    and |orbit| * |Stab| = 252.
 * B4 Block orders.  For s in S_3 (table g_perm, f_0 = 0) the pair
 *    (f_s1 - f_s0, f_s2 - f_s0) is reached by permuting column blocks and
 *    subtracting CRT(0, f_s0(i)) from row i, which also preserves P1.
 *    Family pairs map to family pairs, because +-f_1, +-f_2, +-(f_1 - f_2)
 *    are all ARC.  T is linear and commutes with these operations, so
 *    G x S_3 acts on family pairs.
 * B5 Canonical pair.  Define nrm(h1,h2) = (rep(h1), min over st in
 *    Stab(rep(h1)) of id(T_st T_g h2)) for any g with T_g h1 = rep(h1).  Such
 *    g form a coset Stab*g, so nrm does not depend on g.  canon(f_1,f_2) is
 *    the lexicographic minimum of nrm over the six block orders.  It equals
 *    the minimum of (id T h1, id T h2) over the whole G x S_3 class, so it
 *    is a class invariant, and each class has exactly one member with
 *    canon = (first, second).  Those members are the CASES.  Equivalent
 *    pairs have bijective lift sets, so a class has a lift iff its case does.
 * B6 P23 = {u(i^2-i) + v(i^3-i)} is a G-invariant 2-dimensional subspace
 *    with 49 normalized elements (CHECKED).  span{f_1, f_2} is invariant
 *    under B3 and B4, so "both offsets in P23" is a class property.  Those
 *    classes were scanned before and are EXCLUDED, as are the catalog's
 *    EXCLUDE pairs (completed sampler inputs).
 * B7 Key = first*N + second, where N = catalog size.  The scan visits every
 *    key in [START_KEY, END_KEY) once, in increasing order, and decides each
 *    as exactly one of: first_not_representative, difference_not_arc,
 *    noncanonical, inside_p23, exclude_list, zero, unknown_rank_above_cap,
 *    unknown_case_time.  keys_accounted CHECKS that these classes sum to
 *    resume_key - START_KEY.
 * Self-checks beyond P5-P8: code/decode round trip; zero not ARC; 49
 * distinct normalized P23 functions, G-invariant; identity action fixes every
 * function; the B3 derivation for all 252 actions on four offset pairs
 * (entrywise, with c -> c' a bijection; T(0) = 0; images normalized); every G
 * image of a catalog function lies in the catalog; |Stab| <= 42 and the
 * identity in Stab; |orbit| * |Stab| = 252; canon never exceeds a
 * representative-first pair; a full validate scan meets every EXCLUDE pair
 * exactly once; the transformed pair of the beta mode keeps its canonical
 * key.  A failed self-check is INTERNAL_ERROR (exit 3), never a verdict.
 *
 * =============================================================== CATALOG
 * Plain text C21_ARCS_V1 (protocol ABI).  The file is at most 8 MiB,
 * refused before parsing.  Every line consists of canonical decimals (no
 * sign, no leading zero, at most 9 digits) separated by single spaces and
 * ends with one LF, the last line included.  No CR, tab, comment, blank
 * line or trailing byte.
 *   line 1  C21_ARCS_V1
 *   line 2  N R S E        1 <= N <= 16807, 1 <= R <= N, 1 <= S <= 252 R
 *   N lines id P rep_id a b l f0 f1 f2 f3 f4 f5 f6
 *   R lines rep_id stab_count a b l a b l ...
 *   E lines first_rep_id second_id
 * The consumer REJECTS (exit 2), never a NO-LIFT, unless all of these hold:
 * id = line index; vectors strictly increasing (base-7 f2..f6, f2 most
 * significant, f0 = f1 = 0); every listed function ARC and N = the
 * independent count of ARC functions among all 7^5 (so the list is exactly
 * the ARC set); P = P23 membership; rep_id = least id in the G orbit; the
 * normalizer (any valid one) maps f to f_rep; R = number of representatives;
 * stabilizer lines in increasing rep order, one per representative, actions
 * in any order, duplicate-free, each fixing the representative, count =
 * full stabilizer size; S = sum of counts; EXCLUDE keys strictly increasing,
 * each pair a canonical non-P23 family case (CLS_CASE); nothing after the E
 * lines.
 *
 * =================================================================== CLI
 * Every mode prints key=value lines to stdout, each flushed, starting with
 * tool=crt3_offset_batch_c21v2.  Integers are canonical decimals.
 * (1) scalar MODE Q K BETA OUTPREFIX WALL_SECONDS RANK_CAP
 *     v1-compatible single-pattern control, for calibration only.  After the
 *     word scalar it has the same arguments, key names and key order, the
 *     same witness file OUTPREFIX.dm.txt and the same exit codes as
 *     crt3_graycheck_c21v1: 10 FOUND, 20 ZERO_FOR_THIS_BETA, 30 UNKNOWN,
 *     2 REJECT, 3 INTERNAL_ERROR.  Extra lines: core_port_of and
 *     interface (and the tool name differs).
 * (2) validate CATALOG WALL_SECONDS
 *     Full catalog validation, then enumeration of the whole range [0, N*N)
 *     without solving.  Prints class counts, cases_enumerated (the
 *     production inventory), first/last case key, case_keys_checksum and
 *     cases_by_first_representative.  Exit 0 CATALOG_VALID, 30 stopped,
 *     2, 3.
 * (3) beta CATALOG KEY BETA_OUT WALL_SECONDS [A B L S]
 *     Decodes KEY = first*N + second (any pair of catalog ids, KEY < N*N).
 *     Optionally it maps the pair by block order S (0..5, table g_perm) and
 *     then action (A,B,L); the canonical key must stay the same (CHECKED).
 *     Prints the pair's class and canonical key.  Writes its 7 x 21 beta
 *     exclusively to BETA_OUT: dm-raw style, residues mod 7, column 7t + c,
 *     usable as v1/v2 scalar input.  Exit 0 BETA_WRITTEN, 30, 2, 3.
 * (4) batch CATALOG OUTPREFIX WALL_SECONDS RANK_CAP START_KEY END_KEY
 *           [CASE_SECONDS [TRACE_CASES]]
 *     Production.
 *     WALL_SECONDS 1..10800: monotonic clock from process start, including
 *       catalog validation; never reset.
 *     RANK_CAP 0..26.
 *     START_KEY < END_KEY <= N*N; END_KEY may be the word end (= N*N).
 *     CASE_SECONDS 0..10800; 0 or absent means no per-case bound.
 *     TRACE_CASES 0..4096 (default 0) prints one trace_case line for each
 *       of the first TRACE_CASES completed cases; calibration only.
 *     Files: OUTPREFIX.unknown.txt is always created (O_EXCL, mode 0444) and
 *     may stay empty.  OUTPREFIX.dm.txt and OUTPREFIX.seed.txt (O_EXCL,
 *     0444) are written only on FOUND.  None of the three may exist at
 *     start.
 *     Exit codes:
 *       10 FOUND
 *       20 ZERO_FOR_RANGE: range complete, every case ZERO, no UNKNOWN
 *       30 UNKNOWN: range incomplete, or complete with UNKNOWN keys
 *        2 REJECT: usage, invalid catalog, bad range, existing output
 *        3 INTERNAL_ERROR: failed self-check or output I/O
 * Signals SIGTERM, SIGINT, SIGHUP and SIGXCPU only set a flag, which is
 * never cleared.
 *
 * =========================================================== BATCH OUTPUT
 * Startup prints CLI, catalog and self-check lines.  After that, at most
 * one heartbeat line per 300 s, emitted between keys or cases, and the
 * optional trace lines.  At every exit after the scan began, one summary
 * block:
 *   - range keys, current_key (the case in progress at a stop, else none),
 *     resume_key, range_complete, keys_accounted (pass or MISMATCH; a
 *     mismatch turns exit 0/20/30 into INTERNAL_ERROR; FOUND is kept);
 *   - class counts and outcome counts;
 *   - eq_rank/null_dim/ineq_rank histograms, counting only cases where the
 *     value was computed;
 *   - rolling_checksum: sum mod 2^64 of per-case digests over completed
 *     cases (key, outcome, ranks, zero forms, Gray visits; time-outs digest
 *     key and outcome only); additive over chunks; diagnostic only;
 *   - case_keys_checksum: sum mod 2^64 of mix64(key) over completed cases,
 *     comparable with the validate mode;
 *   - the UNKNOWN registry: count, bytes, first 64 keys, checksum, sync;
 *   - stop_stage and stop_reason.
 * UNKNOWN registry line: "KEY rank|time INEQ_RANK ZERO_FORMS_ON_L", with -1
 * for "not computed", at most 23 bytes.  It is written with write(2) BEFORE
 * the case counts as decided, and fsynced at heartbeats and at exit.
 * Seed file on FOUND: key=value lines seed_format=C21_OFFSET_SEED_V1, tool,
 * catalog_fnv1a64, catalog_N, key, first_id, second_id, f1, f2,
 * beta_columns=7t+c, beta_row0..beta_row6.  The dm file holds 7 lines of 21
 * residues mod 21.
 *
 * ========================================================= EDGE SEMANTICS
 * - A stop (signal or wall) during catalog validation exits 30 with no scan
 *   summary; the next START_KEY is unchanged.
 * - A stop between keys exits 30: resume_key = first undecided key,
 *   current_key = none.
 * - A stop inside a case exits 30.  That case is not counted:
 *   resume_key = current_key = its key.  It is never skipped.
 * - CASE_SECONDS reached first: a 'time' registry line is written, the case
 *   counts as unknown_case_time and the scan advances.  If the global stop
 *   and the case limit are due at the same poll, the global stop wins (the
 *   case is partial).
 * - ineq_rank > RANK_CAP: a 'rank' registry line with ineq_rank and
 *   zero_forms_on_L, then the scan advances.  zero_forms_on_L > 0 is
 *   reported as metadata only and never turned into a verdict here.
 * - Registry already holding 262144 lines in this run: stop before
 *   recording.  resume_key = current_key = that key, stop_reason
 *   unknown_registry_full.
 * - Registry write failure: INTERNAL_ERROR, resume at that key.
 * - First checked lift: the DM is checked on all 21 row pairs mod 21, and
 *   its beta is re-derived from the offsets.  Then dm and seed are written
 *   exclusively and the program exits 10 at once with
 *   resume_key = current_key = that key.  If writing fails, the unwritten
 *   texts are dumped to stdout between unwritten_*_begin/end markers and
 *   the program exits 3.
 * - A range without cases ends ZERO_FOR_RANGE with cases_completed=0
 *   (vacuous; see the counts).  START_KEY >= END_KEY is refused.
 * - Stop polls: at least every 256 keys during enumeration, every 64
 *   catalog lines, every 64 functions of the orbit check, at every
 *   elimination/check loop step, and every 2^16 Gray steps.
 *
 * ============================================================= RESOURCES
 * Memory: static only, no heap.
 *   - engine struct ge: about 414 KB (v1 sizes QMAX = 11, KMAX = 7), zeroed
 *     once per case;
 *   - catalog buffer: 8 MiB + 1;
 *   - EXCLUDE keys: 8 MiB of BSS, of which only 4*E bytes are touched;
 *   - function tables: about 1.3 MB;
 *   - scalar BETA buffer: 64 KiB.
 *   Resident: about 2 MB + the catalog size + 4*E bytes (<= 19 MB in the
 *   worst legal case).
 * Disk per batch run: registry <= 262144 * 23 = 6,029,312 bytes; dm <= 441
 *   bytes; seed < 1 KiB.  No per-case files or processes.
 * stdout per batch run: about 100 fixed lines + <= 36 heartbeats + <= 4096
 *   trace lines.  Below 40 KB without trace.
 * Time [INFERENCE, unmeasured]: catalog validation applies 252 actions to
 *   each of the N functions, about 1e8 small operations.  The case scan
 *   evaluates canon (6 block orders x |Stab|) for each of the R*N keys of
 *   representative rows.  Per case: the Gauss-Jordan certificate costs
 *   about 1e7 byte operations, then 2^(r-1) <= 2^25 Gray steps.
 *
 * =============================================================== RECIPES
 * For Main; nothing here has been run.
 *   C21=/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/cfr33/cfr21
 *   env TMPDIR=$C21/tmp-cc /usr/bin/clang -O3 -std=c11 -Wall -Wextra \
 *     -Wpedantic $C21/code/crt3_offset_batch_c21v2.c \
 *     -o $C21/bin/crt3_offset_batch_c21v2
 * Scalar parity: use the calib/crt3-gray-v1 fixtures q1-k2, q1-k3, q1-k4,
 *   q1-k7 (Q=1), p21-k6-mod7 (Q=7, K=6) and sage33-k6-mod11 (Q=11, K=6),
 *   plus q1-k3 with RANK_CAP 1.  Run v1 and "v2 scalar" in first and count
 *   modes with identical arguments and fresh OUTPREFIXes.  Every key from
 *   mode= to stop_reason= must match, except paths and elapsed time, and so
 *   must the exit codes.  Witness files must be byte-identical (same
 *   algorithm, same first Gray point).  v1's rejection list (CRLF, "07",
 *   double space, Q=3, K=8, WALL 0, RANK_CAP 27, ...) must reject in v2.
 * Catalog: "v2 validate CATALOG 600" must exit 0.  Record N R S E and
 *   arc_functions_independent (= N).  Check orbit_size_hist (sizes divide
 *   252, are >= 6, and sum size*count = N), cases_enumerated,
 *   case_keys_checksum, canonical_exclude_list_excluded (= E, checked) and
 *   keys_accounted pass.  Mutation controls: each of the following must
 *   exit 2 with its reject_reason.
 *   - flip one P; change one rep_id; give one non-normalizing normalizer;
 *   - drop or duplicate one stabilizer action;
 *   - swap two function lines; delete one;
 *   - N, R, S or E off by one;
 *   - trailing space, CRLF, "07", a blank last line;
 *   - one EXCLUDE pair replaced by a noncanonical or a P23 pair;
 *   - two EXCLUDE lines swapped; a file above 8 MiB.
 * Family vs v1: pick case keys K (first_case_key, last_case_key, trace
 *   keys).  Run "v2 beta CATALOG K OUT 600", then "v1 count 7 7 OUT NAME
 *   10800 26" and "v2 batch CATALOG P 10800 26 K K+1 0 1".  The trace_case
 *   line must match v1's eq_rank, null_dim, ineq_rank, kernel_dim,
 *   zero_forms_on_L, expected_assignments and verdict: zero <-> exit 20,
 *   unknown_rank_above_cap <-> exit 30 with stop_reason rank_above_cap.
 * Metamorphic: "v2 beta CATALOG K OUT2 600 A B L S" for several actions and
 *   block orders.  The canonical key is unchanged (checked), and v1 on OUT2
 *   must reproduce OUT's invariants and verdict.
 * Reset: run v2 batch over a range holding >= 3 cases with
 *   TRACE_CASES >= 3.  Each trace line must equal the corresponding
 *   single-key run.  The same range split into two chunks must give the
 *   same cases_completed and the same sums (mod 2^64) of rolling_checksum
 *   and case_keys_checksum.
 * Stops:
 *   - SIGTERM in a long case: exit 30, current_key = resume_key;
 *   - small WALL: stop_reason wall_limit_<W>s;
 *   - CASE_SECONDS 1 on a slow case: a 'time' line, and the scan goes on;
 *   - RANK_CAP 0: every case with ineq_rank >= 1 becomes a 'rank' line,
 *     registry lines = unknown_case_count, exit 30 with range_complete=yes;
 *   - existing OUTPREFIX.* files: exit 2.
 * The batch FOUND path has no positive fixture in this family.  It shares
 *   format_dm and write_exclusive with scalar mode, which the positive
 *   fixtures exercise; the seed writer itself is unexercised.
 * Production: chunks <= 10800 s.  Each chunk uses a fresh OUTPREFIX and
 *   START_KEY = the previous resume_key.  Keep every registry.  The family
 *   status stays UNKNOWN while any registry line or untiled key remains.
 */

#define _XOPEN_SOURCE 700

#include <errno.h>
#include <fcntl.h>
#include <signal.h>
#include <stdarg.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <time.h>
#include <unistd.h>

#define TOOL "crt3_offset_batch_c21v2"
#define CORE_PORT "crt3_graycheck_c21v1.c sha256 5c3719fa85dfb2969a19bd1087d74ae07c7d9296c735d3dac90723c359e1a411"
#define PROTOCOL "notes/offset-arcs-protocol-v1.txt sha256 cd7de0679b8c9d1b1d3ca3eb93c7ab88c734badaa721a8c48a7d7d79a4a76ec5"
#define ULL(x) ((unsigned long long)(x))

/* Engine sizes: identical to crt3_graycheck_c21v1.c. */
enum {
    QMAX = 11,
    KMAX = 7,
    NMAX = 3 * QMAX,
    VMAX = (KMAX - 1) * (NMAX - 1),   /* gauged unknowns: 192 */
    PAIRMAX = KMAX * (KMAX - 1) / 2,  /* 21 */
    EMAX = PAIRMAX * QMAX,            /* triples = equalities = forms: 231 */
    DMAX = VMAX,                      /* dim null(A) */
    RMAX = EMAX < DMAX ? EMAX : DMAX, /* rank of the forms on L */
    AUGW = VMAX + EMAX,               /* width of [A | I] */
    RANK_CAP_MAX = 26,
    WALL_MAX = 10800,
    FILE_MAX = 65536,
    PATH_BUF = 4096,
    TEXT_BUF = 4096,
    POLL_MASK = 0xFFFF                /* poll every 2^16 Gray steps */
};

/* Family and batch sizes. */
enum {
    FP = 7,                    /* rows, residues mod 7, columns per block */
    FCOLS = 3 * FP,            /* 21 columns, index 7t + c */
    NFUN = 16807,              /* 7^5 normalized offset functions */
    GACT = 252,                /* |G| */
    STAB_MAX = 42,             /* B3: |Stab(f)| <= 252/6 for f != 0 */
    TOK_MAX = 2 + 3 * GACT,    /* longest legal catalog line */
    UNKNOWN_FILE_MAX = 262144, /* UNKNOWN registry lines per run */
    UNKNOWN_PRINT_MAX = 64,
    TRACE_MAX = 4096,
    PROGRESS_SECONDS = 300,
    ENUM_POLL_MASK = 0xFF,     /* scan: poll at least every 256 keys */
    CAT_POLL_MASK = 0x3F       /* catalog: poll every 64 lines or functions */
};

#define CATALOG_MAX_BYTES ((size_t)8 * 1024 * 1024)
#define EXCL_CAP (CATALOG_MAX_BYTES / 4) /* an EXCLUDE line has >= 4 bytes */

enum { RC_OK = 0, RC_REJECT = 2, RC_INTERNAL = 3, RC_FOUND = 10, RC_ZERO = 20, RC_UNKNOWN = 30 };
/* Engine and traversal results. */
enum { RUN = 0, STOP_GLOBAL = 1, STOP_CASE = 2, TRAV_COMPLETE = 3, TRAV_FIRST = 4, ENG_CAP = 5 };
enum { MODE_NONE, MODE_SCALAR, MODE_VALIDATE, MODE_BETA, MODE_BATCH };
enum { CLS_CASE, CLS_FIRST_NOT_REP, CLS_NOT_ARC_DIFF, CLS_NONCANONICAL, CLS_P23 };
enum { OUT_ZERO = 1, OUT_RANK = 2, OUT_TIME = 3 };

static const char *const g_cls_name[] = {
    "case", "first_not_representative", "difference_not_arc", "noncanonical", "inside_p23"
};

/* ------------------------------------------------------- process state */
/* Never reset: the incoming stop flag and the outer (process) clock. */
static volatile sig_atomic_t g_signal;
static struct timespec g_t0;
static int g_mode = MODE_NONE;
static int g_wall;              /* global wall seconds from process start */
static int g_case_limit;        /* nonzero only while a batch case runs */
static double g_case_start;     /* elapsed() at the start of that case */
static char g_stop_reason[64];  /* signal_N | wall_limit_Ws | case_time_limit_Ws */
static char g_msg[512];
static int g_scan_started;      /* once set, every exit prints the scan summary */

/* Scalar mode and witness text (the witness path is shared with batch). */
static int g_count_mode;
static const char *g_beta_path;
static char g_file[FILE_MAX + 1];
static char g_dm_path[PATH_BUF];
static char g_dmtext[TEXT_BUF];

/* ------------------------------------------------- per-pattern engine state */
/* Everything one beta pattern touches; eng_reset zeroes all of it. */
struct engine {
    int Q, K, N, V, E, cap;
    int eqrank, d, r, zero_forms, zc;
    int have_eq, have_r, trav_started, dm_written;
    const char *stop_stage;
    uint64_t expected, visited, found, dm_checked, rechecks;
    uint8_t beta[KMAX][NMAX];
    uint8_t tri_i[EMAX], tri_j[EMAX], tri_c[EMAX][3];
    uint8_t A[EMAX][VMAX];          /* equalities, never modified */
    uint8_t L[EMAX][VMAX];          /* forms, never modified */
    uint8_t aug[EMAX][AUGW];        /* [A | I] reduced in place to [R | P] */
    int pivcol[EMAX];
    uint8_t ispiv[VMAX];
    uint8_t B[DMAX][VMAX];          /* basis of L = null(A) */
    uint8_t G[EMAX][DMAX];          /* G[e][m] = l_e(b_m) */
    int sel[RMAX], wpiv[RMAX];
    uint8_t W[RMAX][DMAX];          /* reduced selected rows, W = T H */
    uint8_t T[RMAX][RMAX];
    uint8_t lam[EMAX][RMAX];        /* l_e = sum_k lam[e][k] y_k on L */
    uint8_t M[VMAX][RANK_CAP_MAX];  /* section: x = M y */
    uint32_t off[RANK_CAP_MAX + 1];
    uint16_t le[EMAX * RANK_CAP_MAX];
    uint8_t lc[EMAX * RANK_CAP_MAX];
    uint8_t v[EMAX], y[RANK_CAP_MAX];
    uint8_t crt[3][QMAX];
    uint8_t x[VMAX];
    int dm[KMAX][NMAX];
};
static struct engine ge;

/* ------------------------------------------------------- output and exits */
static void out(const char *fmt, ...) __attribute__((format(printf, 1, 2)));
static _Noreturn void finish(const char *status, int rc);
static _Noreturn void reject(const char *fmt, ...) __attribute__((format(printf, 1, 2)));
static _Noreturn void internal_error(const char *fmt, ...) __attribute__((format(printf, 1, 2)));
static int scan_summary(void);

static double elapsed(void)
{
    struct timespec t;
    clock_gettime(CLOCK_MONOTONIC, &t);
    return (double)(t.tv_sec - g_t0.tv_sec) + 1e-9 * (double)(t.tv_nsec - g_t0.tv_nsec);
}

static void out(const char *fmt, ...)
{
    va_list ap;
    va_start(ap, fmt);
    vprintf(fmt, ap);
    va_end(ap);
    putchar('\n');
    fflush(stdout);
}

static const char *scope_text(void)
{
    switch (g_mode) {
    case MODE_BATCH:
        return "canonical common-parallel-line offset cases of this catalog with keys in "
               "[range_start_key, resume_key) only, decided by this one program; UNKNOWN keys "
               "are undecided; restricted evidence until independently checked; not a "
               "CFR(6,21), difference-matrix or MOLS nonexistence claim and no novelty claim";
    case MODE_VALIDATE:
    case MODE_BETA:
        return "catalog validation and case enumeration only; no lift was searched";
    default:
        return "CRT Z_3 lift of this exact beta pattern only; "
               "not a CFR, difference-matrix or MOLS nonexistence claim";
    }
}

static _Noreturn void finish(const char *status, int rc)
{
    if (g_scan_started) {
        g_scan_started = 0; /* no recursion through a failing summary */
        if (!scan_summary() && (rc == RC_ZERO || rc == RC_UNKNOWN || rc == RC_OK)) {
            out("internal_reason=key accounting mismatch (see keys_accounted)");
            status = "INTERNAL_ERROR";
            rc = RC_INTERNAL;
        }
    }
    out("elapsed_seconds=%.3f", elapsed());
    out("status=%s", status);
    out("scope=%s", scope_text());
    out("exit_code=%d", rc);
    exit(rc);
}

static _Noreturn void die_with(const char *status, int rc, const char *key, const char *msg)
{
    fprintf(stderr, "%s: %s: %s\n", TOOL, key, msg);
    out("%s=%s", key, msg);
    finish(status, rc);
}

static _Noreturn void reject(const char *fmt, ...)
{
    char msg[512];
    va_list ap;
    va_start(ap, fmt);
    vsnprintf(msg, sizeof msg, fmt, ap);
    va_end(ap);
    die_with("REJECT", RC_REJECT, "reject_reason", msg);
}

static _Noreturn void internal_error(const char *fmt, ...)
{
    char msg[512];
    va_list ap;
    va_start(ap, fmt);
    vsnprintf(msg, sizeof msg, fmt, ap);
    va_end(ap);
    die_with("INTERNAL_ERROR", RC_INTERNAL, "internal_reason", msg);
}

/* ------------------------------------------------------- stop polling */
static void on_signal(int sig)
{
    g_signal = sig;
}

static void install_one(int sig, const struct sigaction *sa)
{
    if (sigaction(sig, sa, NULL) != 0)
        internal_error("sigaction(%d) failed: %s", sig, strerror(errno));
}

static void install_signals(void)
{
    struct sigaction sa;
    memset(&sa, 0, sizeof sa);
    sa.sa_handler = on_signal;
    sigemptyset(&sa.sa_mask);
#ifdef SA_RESTART
    sa.sa_flags = SA_RESTART;
#endif
    install_one(SIGTERM, &sa);
    install_one(SIGINT, &sa);
    install_one(SIGHUP, &sa);
#ifdef SIGXCPU
    install_one(SIGXCPU, &sa);
#endif
}

/*
 * RUN, STOP_GLOBAL (signal or outer wall clock; the case in progress stays
 * partial) or STOP_CASE (per-case bound, only while a batch case runs).
 * The signal flag and the outer clock are only read here, never reset.
 */
static int poll_stop(void)
{
    const int sig = (int)g_signal;
    if (sig != 0) {
        snprintf(g_stop_reason, sizeof g_stop_reason, "signal_%d", sig);
        return STOP_GLOBAL;
    }
    const double now = elapsed();
    if (now >= (double)g_wall) {
        snprintf(g_stop_reason, sizeof g_stop_reason, "wall_limit_%ds", g_wall);
        return STOP_GLOBAL;
    }
    if (g_case_limit > 0 && now - g_case_start >= (double)g_case_limit) {
        snprintf(g_stop_reason, sizeof g_stop_reason, "case_time_limit_%ds", g_case_limit);
        return STOP_CASE;
    }
    return RUN;
}

/* ------------------------------------------------------- CLI and I/O helpers */
static int parse_u64(const char *s, uint64_t lo, uint64_t hi, uint64_t *val)
{
    const size_t n = strlen(s);
    uint64_t v = 0;
    if (n == 0 || n > 12 || (n > 1 && s[0] == '0'))
        return 0;
    for (size_t k = 0; k < n; k++) {
        if (s[k] < '0' || s[k] > '9')
            return 0;
        v = 10 * v + (uint64_t)(s[k] - '0');
    }
    if (v < lo || v > hi)
        return 0;
    *val = v;
    return 1;
}

/* v1 rule: canonical decimal of at most 6 digits in lo..hi. */
static int parse_uint(const char *s, int lo, int hi, int *val)
{
    uint64_t v;
    if (strlen(s) > 6 || !parse_u64(s, (uint64_t)lo, (uint64_t)hi, &v))
        return 0;
    *val = (int)v;
    return 1;
}

static void make_path(char *buf, const char *prefix, const char *suffix)
{
    if (prefix[0] == '\0')
        reject("output path or OUTPREFIX must be nonempty");
    const int w = snprintf(buf, PATH_BUF, "%s%s", prefix, suffix);
    if (w < 0 || w >= PATH_BUF)
        reject("output path or OUTPREFIX too long");
}

/* The outputs are created only at the end; refuse early instead of losing them. */
static void preflight_output(const char *path)
{
    static char dir[PATH_BUF];
    struct stat st;
    const char *slash = strrchr(path, '/');
    if (lstat(path, &st) == 0)
        reject("output %s already exists; refusing to overwrite", path);
    if (errno != ENOENT)
        reject("cannot check output %s: %s", path, strerror(errno));
    if (slash == NULL) {
        strcpy(dir, ".");
    } else if (slash == path) {
        strcpy(dir, "/");
    } else {
        const size_t n = (size_t)(slash - path);
        memcpy(dir, path, n);
        dir[n] = '\0';
    }
    if (stat(dir, &st) != 0 || !S_ISDIR(st.st_mode))
        reject("output directory %s does not exist", dir);
    if (access(dir, W_OK | X_OK) != 0)
        reject("output directory %s is not writable", dir);
}

static int write_all(int fd, const char *p, size_t n)
{
    size_t off = 0;
    while (off < n) {
        const ssize_t w = write(fd, p + off, n - off);
        if (w < 0 && errno == EINTR)
            continue;
        if (w <= 0) {
            if (w == 0)
                errno = EIO;
            return -1;
        }
        off += (size_t)w;
    }
    return 0;
}

/* O_EXCL create (mode 0444), full write, fsync, close: 0, or -1 with g_msg. */
static int write_exclusive(const char *path, const char *text, size_t n)
{
    const int fd = open(path, O_WRONLY | O_CREAT | O_EXCL, 0444);
    if (fd < 0) {
        snprintf(g_msg, sizeof g_msg, "cannot exclusively create %s: %s", path, strerror(errno));
        return -1;
    }
    if (write_all(fd, text, n) != 0) {
        snprintf(g_msg, sizeof g_msg, "write to %s failed: %s", path, strerror(errno));
        close(fd);
        return -1;
    }
    if (fsync(fd) != 0) {
        snprintf(g_msg, sizeof g_msg, "fsync/close of %s failed: %s", path, strerror(errno));
        close(fd);
        return -1;
    }
    if (close(fd) != 0) {
        snprintf(g_msg, sizeof g_msg, "fsync/close of %s failed: %s", path, strerror(errno));
        return -1;
    }
    return 0;
}

static void dump_unwritten(const char *label, const char *text, size_t n)
{
    out("unwritten_%s_begin", label);
    fwrite(text, 1, n, stdout);
    out("unwritten_%s_end", label);
}

/* splitmix64 finalizer: diagnostic digests only, never a verdict. */
static uint64_t mix64(uint64_t z)
{
    z += 0x9e3779b97f4a7c15ULL;
    z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
    z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
    return z ^ (z >> 31);
}

/* =================================================================== ENGINE
 * Port of crt3_graycheck_c21v1.c P2-P8.  Each step returns RUN or the stop
 * code from poll_stop.  Self-check failures are fatal (INTERNAL_ERROR). */
#define ENG_POLL(stage)              \
    do {                             \
        const int st_ = poll_stop(); \
        if (st_ != RUN) {            \
            ge.stop_stage = (stage); \
            return st_;              \
        }                            \
    } while (0)

/* Reset ALL per-pattern state.  Never touches g_signal or the outer clock. */
static void eng_reset(int Q, int K, int cap)
{
    memset(&ge, 0, sizeof ge);
    ge.Q = Q;
    ge.K = K;
    ge.N = 3 * Q;
    ge.V = (K - 1) * (ge.N - 1);
    ge.cap = cap;
    ge.stop_stage = "none";
}

/* P2(a) and the triples C(i,j,rho), columns increasing: 0, or -1 with g_msg. */
static int eng_validate_beta(void)
{
    int e = 0;
    for (int i = 0; i < ge.K; i++)
        for (int j = i + 1; j < ge.K; j++) {
            int cnt[QMAX] = {0};
            uint8_t pos[QMAX][3] = {{0}};
            for (int c = 0; c < ge.N; c++) {
                const int rho = (ge.beta[j][c] - ge.beta[i][c] + ge.Q) % ge.Q;
                if (cnt[rho] == 3) {
                    snprintf(g_msg, sizeof g_msg,
                             "beta rows %d,%d: residue %d occurs more than 3 times (need exactly 3)",
                             i, j, rho);
                    return -1;
                }
                pos[rho][cnt[rho]++] = (uint8_t)c;
            }
            for (int rho = 0; rho < ge.Q; rho++) {
                if (cnt[rho] != 3) {
                    snprintf(g_msg, sizeof g_msg,
                             "beta rows %d,%d: residue %d occurs %d times (need exactly 3)",
                             i, j, rho, cnt[rho]);
                    return -1;
                }
                ge.tri_i[e] = (uint8_t)i;
                ge.tri_j[e] = (uint8_t)j;
                memcpy(ge.tri_c[e], pos[rho], 3);
                e++;
            }
        }
    ge.E = e;
    return 0;
}

static void eng_build_crt(void)
{
    uint8_t seen[3][QMAX];
    memset(seen, 0, sizeof seen);
    for (int x = 0; x < ge.N; x++) {
        const int a = x % 3, b = x % ge.Q;
        if (seen[a][b])
            internal_error("CRT map Z_%d -> Z_3 x Z_%d is not injective", ge.N, ge.Q);
        seen[a][b] = 1;
        ge.crt[a][b] = (uint8_t)x;
    }
}

static int var_index(int i, int c)
{
    return (i == 0 || c == 0) ? -1 : (i - 1) * (ge.N - 1) + (c - 1);
}

static void add_term(uint8_t *row, int i, int c, int coef)
{
    const int v = var_index(i, c);
    if (v >= 0)
        row[v] = (uint8_t)((row[v] + coef) % 3);
}

/* P3: dlt_k = alpha[j][c_k] - alpha[i][c_k]; coefficient -1 is stored as 2. */
static void eng_build_rows(void)
{
    for (int e = 0; e < ge.E; e++) {
        const int i = ge.tri_i[e], j = ge.tri_j[e];
        const int c1 = ge.tri_c[e][0], c2 = ge.tri_c[e][1], c3 = ge.tri_c[e][2];
        add_term(ge.A[e], j, c1, 1);
        add_term(ge.A[e], i, c1, 2);
        add_term(ge.A[e], j, c2, 1);
        add_term(ge.A[e], i, c2, 2);
        add_term(ge.A[e], j, c3, 1);
        add_term(ge.A[e], i, c3, 2);
        add_term(ge.L[e], j, c1, 1);
        add_term(ge.L[e], i, c1, 2);
        add_term(ge.L[e], j, c2, 2);
        add_term(ge.L[e], i, c2, 1);
    }
}

/* P5(i): Gauss-Jordan on [A | I]; afterwards R = left block, P = right block. */
static int eng_eq_eliminate(void)
{
    const int E = ge.E, V = ge.V, W = V + E;
    int row = 0;
    for (int e = 0; e < E; e++) {
        memcpy(ge.aug[e], ge.A[e], (size_t)V);
        ge.aug[e][V + e] = 1;
    }
    for (int col = 0; col < V && row < E; col++) {
        ENG_POLL("equality_elimination");
        int p = row;
        while (p < E && ge.aug[p][col] == 0)
            p++;
        if (p == E)
            continue;
        if (p != row)
            for (int t = 0; t < W; t++) {
                const uint8_t h = ge.aug[p][t];
                ge.aug[p][t] = ge.aug[row][t];
                ge.aug[row][t] = h;
            }
        if (ge.aug[row][col] == 2) /* 2^-1 = 2 in F_3 */
            for (int t = 0; t < W; t++)
                ge.aug[row][t] = (uint8_t)((2 * ge.aug[row][t]) % 3);
        for (int i = 0; i < E; i++) {
            const int f = ge.aug[i][col];
            if (i == row || f == 0)
                continue;
            for (int t = 0; t < W; t++) /* row_i -= f * pivot row */
                ge.aug[i][t] = (uint8_t)((ge.aug[i][t] + (3 - f) * ge.aug[row][t]) % 3);
        }
        ge.pivcol[row] = col;
        ge.ispiv[col] = 1;
        row++;
    }
    ge.eqrank = row;
    ge.d = V - row;
    return RUN;
}

static int eng_check_equalities(void)
{
    const int E = ge.E, V = ge.V;
    for (int i = 0; i < ge.eqrank; i++) {
        ENG_POLL("equality_rref_check");
        if (i > 0 && ge.pivcol[i] <= ge.pivcol[i - 1])
            internal_error("RREF pivot columns not increasing at row %d", i);
        for (int i2 = 0; i2 < E; i2++)
            if (ge.aug[i2][ge.pivcol[i]] != (i2 == i))
                internal_error("RREF pivot column %d is not a unit vector", ge.pivcol[i]);
    }
    for (int i = ge.eqrank; i < E; i++)
        for (int v = 0; v < V; v++)
            if (ge.aug[i][v] != 0)
                internal_error("RREF row %d beyond the rank is nonzero", i);
    for (int i = 0; i < ge.eqrank; i++) {
        ENG_POLL("equality_certificate");
        for (int v = 0; v < V; v++) {
            int s = 0;
            for (int e = 0; e < E; e++)
                s += ge.aug[i][V + e] * ge.A[e][v];
            if (s % 3 != ge.aug[i][v])
                internal_error("certificate R = P*A fails at row %d column %d", i, v);
        }
    }
    return RUN;
}

/* Standard basis of null(R): one vector per free column f. */
static int eng_build_basis(void)
{
    int m = 0;
    for (int f = 0; f < ge.V; f++) {
        if (ge.ispiv[f])
            continue;
        ge.B[m][f] = 1;
        for (int i = 0; i < ge.eqrank; i++)
            ge.B[m][ge.pivcol[i]] = (uint8_t)((3 - ge.aug[i][f]) % 3);
        m++;
    }
    if (m != ge.d)
        internal_error("nullspace basis has %d vectors, expected %d", m, ge.d);
    for (int k = 0; k < ge.d; k++) {
        ENG_POLL("nullspace_check");
        for (int e = 0; e < ge.E; e++) {
            int s = 0;
            for (int v = 0; v < ge.V; v++)
                s += ge.A[e][v] * ge.B[k][v];
            if (s % 3 != 0)
                internal_error("basis vector %d violates equality %d", k, e);
        }
    }
    ge.have_eq = 1; /* eq_rank and null_dim are now certified */
    return RUN;
}

static int eng_compute_G(void)
{
    for (int e = 0; e < ge.E; e++) {
        int nonzero = 0;
        ENG_POLL("form_projection");
        for (int m = 0; m < ge.d; m++) {
            int s = 0;
            for (int v = 0; v < ge.V; v++)
                s += ge.L[e][v] * ge.B[m][v];
            ge.G[e][m] = (uint8_t)(s % 3);
            nonzero |= ge.G[e][m];
        }
        if (!nonzero)
            ge.zero_forms++;
    }
    return RUN;
}

/*
 * P5(ii): greedy row basis of G with coefficient tracking.  Invariants:
 * W[k] = sum_j T[k][j] G[sel[j]], T lower triangular with nonzero diagonal,
 * W[k][wpiv[k]] = 1 and W[k][wpiv[j]] = 0 for j < k.  Relies on lam and T
 * being zero on entry (eng_reset).
 */
static int eng_ineq_basis(void)
{
    const int d = ge.d;
    uint8_t g[DMAX], c[RMAX], lp[RMAX];
    for (int e = 0; e < ge.E; e++) {
        const int r = ge.r;
        int p = 0;
        ENG_POLL("form_basis");
        memcpy(g, ge.G[e], (size_t)d);
        for (int k = 0; k < r; k++) { /* g -= g[wpiv[k]] * W[k] */
            const int f = g[ge.wpiv[k]];
            c[k] = (uint8_t)f;
            if (f != 0)
                for (int t = 0; t < d; t++)
                    g[t] = (uint8_t)((g[t] + (3 - f) * ge.W[k][t]) % 3);
        }
        for (int j = 0; j < r; j++) { /* lp = sum_k c[k] T[k] */
            int s = 0;
            for (int k = 0; k < r; k++)
                s += c[k] * ge.T[k][j];
            lp[j] = (uint8_t)(s % 3);
        }
        while (p < d && g[p] == 0)
            p++;
        if (p == d) { /* G[e] = sum_j lp[j] G[sel[j]] */
            memcpy(ge.lam[e], lp, (size_t)r);
            continue;
        }
        const int sc = g[p]; /* sc^-1 = sc in F_3 */
        for (int t = 0; t < d; t++)
            ge.W[r][t] = (uint8_t)((g[t] * sc) % 3);
        for (int j = 0; j < r; j++) /* W[r] = sc * (G[e] - sum_j lp[j] G[sel[j]]) */
            ge.T[r][j] = (uint8_t)((sc * (3 - lp[j])) % 3);
        ge.T[r][r] = (uint8_t)sc;
        ge.wpiv[r] = p;
        ge.sel[r] = e;
        ge.lam[e][r] = 1;
        ge.r = r + 1;
    }
    return RUN;
}

static int eng_check_lambda(void)
{
    for (int e = 0; e < ge.E; e++) {
        ENG_POLL("form_basis_check");
        for (int m = 0; m < ge.d; m++) {
            int s = 0;
            for (int k = 0; k < ge.r; k++)
                s += ge.lam[e][k] * ge.G[ge.sel[k]][m];
            if (s % 3 != ge.G[e][m])
                internal_error("form %d is not sum_k lambda G[sel[k]] at coordinate %d", e, m);
        }
    }
    ge.have_r = 1; /* ineq_rank and zero_forms_on_L are now certified */
    return RUN;
}

/*
 * P5(iii): column k of M is B z with G[sel[j]].z = [j = k].  Since W = T H,
 * solve W z = T u_k on the pivot coordinates by back-substitution.
 */
static int eng_build_section(void)
{
    const int r = ge.r, d = ge.d;
    uint8_t z[DMAX];
    for (int k = 0; k < r; k++) {
        ENG_POLL("section");
        memset(z, 0, sizeof z);
        for (int kk = r - 1; kk >= 0; kk--) {
            int s = ge.T[kk][k];
            for (int j = kk + 1; j < r; j++)
                s += 2 * ge.W[kk][ge.wpiv[j]] * z[ge.wpiv[j]];
            z[ge.wpiv[kk]] = (uint8_t)(s % 3);
        }
        for (int v = 0; v < ge.V; v++) {
            int s = 0;
            for (int m = 0; m < d; m++)
                s += z[m] * ge.B[m][v];
            ge.M[v][k] = (uint8_t)(s % 3);
        }
    }
    return RUN;
}

static int eng_check_section(void)
{
    for (int k = 0; k < ge.r; k++) {
        ENG_POLL("section_check");
        for (int e = 0; e < ge.E; e++) {
            int s = 0;
            for (int v = 0; v < ge.V; v++)
                s += ge.A[e][v] * ge.M[v][k];
            if (s % 3 != 0)
                internal_error("section column %d violates equality %d", k, e);
        }
        for (int j = 0; j < ge.r; j++) {
            int s = 0;
            for (int v = 0; v < ge.V; v++)
                s += ge.L[ge.sel[j]][v] * ge.M[v][k];
            if (s % 3 != (j == k))
                internal_error("section column %d gives y_%d != [%d = %d]", k, j, j, k);
        }
    }
    return RUN;
}

static void eng_build_lists(void)
{
    uint32_t n = 0;
    for (int k = 0; k < ge.r; k++) {
        ge.off[k] = n;
        for (int e = 0; e < ge.E; e++)
            if (ge.lam[e][k] != 0) {
                ge.le[n] = (uint16_t)e;
                ge.lc[n] = ge.lam[e][k];
                n++;
            }
    }
    ge.off[ge.r] = n;
}

static void print_y_forms(void)
{
    printf("y_forms=");
    for (int k = 0; k < ge.r; k++)
        printf("%s%d", k ? "," : "", ge.sel[k]);
    out("%s", ge.r ? "" : "none");
}

/* ------------------------------------------------------- witness (P8) */
static void eng_build_dm(void)
{
    for (int v = 0; v < ge.V; v++) {
        int s = 0;
        for (int k = 0; k < ge.r; k++)
            s += ge.M[v][k] * ge.y[k];
        ge.x[v] = (uint8_t)(s % 3);
    }
    for (int i = 0; i < ge.K; i++)
        for (int c = 0; c < ge.N; c++) {
            const int v = var_index(i, c);
            ge.dm[i][c] = ge.crt[v < 0 ? 0 : ge.x[v]][ge.beta[i][c]];
        }
}

/* Direct definition check (P1) on every row pair mod N, and the CRT components. */
static int eng_dm_ok(void)
{
    for (int i = 0; i < ge.K; i++)
        for (int c = 0; c < ge.N; c++) {
            const int v = var_index(i, c), a = v < 0 ? 0 : ge.x[v], x = ge.dm[i][c];
            if (x < 0 || x >= ge.N || x % ge.Q != ge.beta[i][c] || x % 3 != a)
                return 0;
        }
    for (int i = 0; i < ge.K; i++)
        for (int j = i + 1; j < ge.K; j++) {
            uint8_t seen[NMAX] = {0};
            for (int c = 0; c < ge.N; c++) {
                const int dl = (ge.dm[j][c] - ge.dm[i][c] + ge.N) % ge.N;
                if (seen[dl])
                    return 0;
                seen[dl] = 1;
            }
        }
    return 1;
}

static size_t format_dm(char *buf, size_t cap)
{
    size_t n = 0;
    for (int i = 0; i < ge.K; i++)
        for (int c = 0; c < ge.N; c++) {
            const int w = snprintf(buf + n, cap - n, "%d%c", ge.dm[i][c], c + 1 < ge.N ? ' ' : '\n');
            if (w < 0 || (size_t)w >= cap - n)
                internal_error("witness text buffer overflow");
            n += (size_t)w;
        }
    return n;
}

/* ------------------------------------------------------- Gray traversal (P6, P7) */
static void eng_recompute_check(void)
{
    int zc = 0;
    for (int e = 0; e < ge.E; e++) {
        int s = 0;
        for (int k = 0; k < ge.r; k++)
            s += ge.lam[e][k] * ge.y[k];
        s %= 3;
        if (s != ge.v[e])
            internal_error("incremental residue of form %d differs from recomputation", e);
        zc += (s == 0);
    }
    if (zc != ge.zc)
        internal_error("incremental zero count %d differs from recomputation %d", ge.zc, zc);
    ge.rechecks++;
}

/*
 * Visits {1} x {1,2}^(r-1) in reflected Gray order and calls on_sol at every
 * point of Y.  Returns TRAV_COMPLETE (all points visited and checked),
 * TRAV_FIRST (count_mode 0 and a point was found; on_sol returned) or a stop
 * code.  verbose prints v1's sign_fix and expected_assignments lines.
 */
static int eng_traverse(int count_mode, void (*on_sol)(void), int verbose)
{
    const int r = ge.r;
    const int F = r >= 1 ? r - 1 : 0;
    int state = RUN;
    ENG_POLL("gray_start");
    ge.trav_started = 1;
    ge.expected = (uint64_t)1 << F;
    if (verbose) {
        out("sign_fix=%s", r >= 1 ? "y0=1 (x -> -x symmetry; totals are doubled)" : "none (ineq_rank 0)");
        out("expected_assignments=%llu", ULL(ge.expected));
    }
    for (int k = 0; k < r; k++)
        ge.y[k] = 1;
    ge.zc = 0;
    for (int e = 0; e < ge.E; e++) {
        int s = 0;
        for (int k = 0; k < r; k++)
            s += ge.lam[e][k];
        ge.v[e] = (uint8_t)(s % 3);
        ge.zc += (ge.v[e] == 0);
    }
    ge.visited = 1;
    if (ge.zc == 0) {
        on_sol();
        if (!count_mode)
            state = TRAV_FIRST;
    }
    if (state == RUN)
        for (uint64_t s = 1; s < ge.expected; s++) {
            const int k = 1 + __builtin_ctzll(s);
            const int delta = ge.y[k] == 1 ? 1 : 2; /* 1 -> 2 adds 1, 2 -> 1 adds 2 */
            ge.y[k] = (uint8_t)(3 - ge.y[k]);
            for (uint32_t q = ge.off[k]; q < ge.off[k + 1]; q++) {
                const int e = ge.le[q];
                const int old = ge.v[e];
                const int nw = (old + ge.lc[q] * delta) % 3;
                ge.zc += (nw == 0) - (old == 0);
                ge.v[e] = (uint8_t)nw;
            }
            ge.visited++;
            if (ge.zc == 0) {
                on_sol();
                if (!count_mode) {
                    state = TRAV_FIRST;
                    break;
                }
            }
            if ((s & POLL_MASK) == 0) {
                eng_recompute_check();
                const int st = poll_stop();
                if (st != RUN) {
                    ge.stop_stage = "gray_traversal";
                    state = st;
                    break;
                }
            }
        }
    eng_recompute_check();
    if (state != RUN)
        return state;
    const uint64_t last = ge.expected - 1, word = last ^ (last >> 1);
    if (ge.visited != ge.expected)
        internal_error("visited %llu assignments, expected %llu", ULL(ge.visited), ULL(ge.expected));
    if (r >= 1 && ge.y[0] != 1)
        internal_error("fixed coordinate y0 changed");
    for (int b = 0; b < F; b++)
        if (ge.y[1 + b] != (uint8_t)(1 + ((word >> b) & 1)))
            internal_error("final assignment differs from Gray word %llu", ULL(word));
    return TRAV_COMPLETE;
}

/* ================================================================== SCALAR
 * v1-compatible single-pattern control (calibration against v1). */
static size_t read_beta_file(void)
{
    struct stat st;
    size_t len = 0;
    const int fd = open(g_beta_path, O_RDONLY);
    if (fd < 0)
        reject("cannot open BETA %s: %s", g_beta_path, strerror(errno));
    if (fstat(fd, &st) != 0 || !S_ISREG(st.st_mode))
        reject("BETA %s is not a readable regular file", g_beta_path);
    for (;;) {
        const ssize_t n = read(fd, g_file + len, sizeof g_file - len);
        if (n < 0 && errno == EINTR)
            continue;
        if (n < 0)
            reject("cannot read BETA: %s", strerror(errno));
        if (n == 0)
            break;
        len += (size_t)n;
        if (len == sizeof g_file)
            reject("BETA is larger than %d bytes", FILE_MAX);
    }
    close(fd);
    out("beta_bytes=%zu", len);
    return len;
}

/* Strict dm-raw parse: K lines, N single-space-separated canonical residues. */
static void parse_beta(size_t len)
{
    size_t p = 0;
    if (len == 0 || g_file[len - 1] != '\n')
        reject("BETA must be nonempty and end with LF");
    for (size_t q = 0; q < len; q++) {
        const char ch = g_file[q];
        if (ch != '\n' && ch != ' ' && (ch < '0' || ch > '9'))
            reject("BETA byte %zu is not a digit, space or LF", q);
    }
    for (int i = 0; i < ge.K; i++)
        for (int c = 0; c < ge.N; c++) {
            const size_t s = p;
            while (p < len && g_file[p] >= '0' && g_file[p] <= '9')
                p++;
            const size_t tl = p - s;
            if (tl == 0)
                reject("BETA row %d entry %d is missing (need %d rows of %d entries)", i, c, ge.K, ge.N);
            if (tl > 2 || (tl == 2 && g_file[s] == '0'))
                reject("BETA row %d entry %d is not a canonical decimal below %d", i, c, ge.Q);
            const int v = tl == 1 ? g_file[s] - '0' : 10 * (g_file[s] - '0') + (g_file[s + 1] - '0');
            if (v >= ge.Q)
                reject("BETA row %d entry %d = %d is not in 0..%d", i, c, v, ge.Q - 1);
            ge.beta[i][c] = (uint8_t)v;
            const char want = c + 1 < ge.N ? ' ' : '\n';
            if (p >= len || g_file[p] != want)
                reject("BETA row %d: entry %d must be followed by %s", i, c,
                       want == ' ' ? "one space" : "LF (exactly N entries per row)");
            p++;
        }
    if (p != len)
        reject("BETA has more than K=%d rows", ge.K);
}

static void on_solution_scalar(void)
{
    ge.found++;
    eng_build_dm();
    if (!eng_dm_ok())
        internal_error("y-space solution %llu failed the direct DM check; nothing written", ULL(ge.found));
    ge.dm_checked++;
    if (!ge.dm_written) {
        const size_t n = format_dm(g_dmtext, sizeof g_dmtext);
        if (write_exclusive(g_dm_path, g_dmtext, n) != 0) {
            dump_unwritten("dm", g_dmtext, n);
            internal_error("%s", g_msg);
        }
        ge.dm_written = 1;
        out("dm_written=%s", g_dm_path);
        out("dm_bytes=%zu", n);
    }
}

static _Noreturn void scalar_stop(void)
{
    out("stop_stage=%s", ge.stop_stage);
    out("stop_reason=%s", g_stop_reason);
    finish("UNKNOWN", RC_UNKNOWN);
}

static void scalar_step(int st)
{
    if (st != RUN)
        scalar_stop();
}

static _Noreturn void scalar_report(int st)
{
    const int complete = st == TRAV_COMPLETE;
    out("visited_assignments=%llu", ULL(ge.visited));
    out("gray_rechecks=%llu", ULL(ge.rechecks));
    out("solutions_y0_fixed_found=%llu", ULL(ge.found));
    out("dm_checked_witnesses=%llu", ULL(ge.dm_checked));
    out("traversal_complete=%s", complete ? "yes" : "no");
    if (complete) {
        const unsigned long long total = ULL(ge.r >= 1 ? 2 * ge.found : ge.found);
        out("solutions_y_total=%llu", total);
        out("gauged_lifts=%llu*3^%d", total, ge.d - ge.r);
        out("all_lifts_of_beta=%llu*3^%d", total, ge.d - ge.r + ge.N + ge.K - 1);
    }
    out("witness_written=%s", ge.dm_written ? "yes" : "no");
    out("stop_reason=%s", complete ? "complete" : st == TRAV_FIRST ? "first_found" : g_stop_reason);
    if (ge.found > 0)
        finish("FOUND", RC_FOUND);
    if (complete)
        finish("ZERO_FOR_THIS_BETA", RC_ZERO);
    finish("UNKNOWN", RC_UNKNOWN);
}

static _Noreturn void scalar_main(int argc, char **argv)
{
    int Q, K, cap;
    g_mode = MODE_SCALAR;
    out("core_port_of=%s", CORE_PORT);
    out("interface=scalar (v1-compatible arguments, keys, witness and exit codes)");
    if (argc != 9)
        reject("usage: %s scalar first|count Q K BETA OUTPREFIX WALL_SECONDS RANK_CAP", TOOL);
    if (strcmp(argv[2], "first") == 0)
        g_count_mode = 0;
    else if (strcmp(argv[2], "count") == 0)
        g_count_mode = 1;
    else
        reject("MODE must be first or count");
    if (!parse_uint(argv[3], 1, QMAX, &Q) || Q % 3 == 0)
        reject("Q must be a canonical integer in 1..%d with gcd(Q,3)=1", QMAX);
    if (!parse_uint(argv[4], 2, KMAX, &K))
        reject("K must be a canonical integer in 2..%d", KMAX);
    g_beta_path = argv[5];
    if (argv[6][0] == '\0')
        reject("OUTPREFIX must be nonempty");
    const int w = snprintf(g_dm_path, sizeof g_dm_path, "%s.dm.txt", argv[6]);
    if (w < 0 || (size_t)w >= sizeof g_dm_path)
        reject("OUTPREFIX too long");
    if (!parse_uint(argv[7], 1, WALL_MAX, &g_wall))
        reject("WALL_SECONDS must be a canonical integer in 1..%d", WALL_MAX);
    if (!parse_uint(argv[8], 0, RANK_CAP_MAX, &cap))
        reject("RANK_CAP must be a canonical integer in 0..%d", RANK_CAP_MAX);
    eng_reset(Q, K, cap);
    out("mode=%s", g_count_mode ? "count" : "first");
    out("Q=%d", ge.Q);
    out("K=%d", ge.K);
    out("N=%d", ge.N);
    out("beta_file=%s", g_beta_path);
    out("dm_path=%s", g_dm_path);
    out("wall_seconds=%d", g_wall);
    out("rank_cap=%d", ge.cap);
    preflight_output(g_dm_path);
    parse_beta(read_beta_file());
    if (eng_validate_beta() != 0)
        reject("%s", g_msg);
    {
        int row0_zero = 1;
        for (int c = 0; c < ge.N; c++)
            row0_zero &= (ge.beta[0][c] == 0);
        out("beta_row0_zero=%s", row0_zero ? "yes" : "no");
    }
    out("beta_check=pass (all %d row pairs: every residue mod %d occurs exactly 3 times)",
        ge.K * (ge.K - 1) / 2, ge.Q);
    eng_build_crt();
    eng_build_rows();
    out("variables=%d", ge.V);
    out("equalities=%d", ge.E);
    scalar_step(eng_eq_eliminate());
    scalar_step(eng_check_equalities());
    scalar_step(eng_build_basis());
    out("eq_rank=%d", ge.eqrank);
    out("null_dim=%d", ge.d);
    out("check_equalities=pass (RREF structure, R = P*A on pivot rows, A*basis = 0)");
    scalar_step(eng_compute_G());
    scalar_step(eng_ineq_basis());
    scalar_step(eng_check_lambda());
    out("inequalities=%d", ge.E);
    out("ineq_rank=%d", ge.r);
    out("kernel_dim=%d", ge.d - ge.r);
    out("zero_forms_on_L=%d", ge.zero_forms);
    out("check_inequalities=pass (every form = sum_k lambda[e][k] * selected form k on L)");
    if (ge.r > ge.cap) {
        out("rank_cap_status=exceeded (ineq_rank %d > rank_cap %d)", ge.r, ge.cap);
        out("stop_reason=rank_above_cap");
        finish("UNKNOWN", RC_UNKNOWN);
    }
    out("rank_cap_status=ok");
    print_y_forms();
    scalar_step(eng_build_section());
    scalar_step(eng_check_section());
    out("check_section=pass (A*M = 0, selected forms of M u_k = u_k)");
    eng_build_lists();
    out("gray_list_entries=%u", (unsigned)ge.off[ge.r]);
    const int st = eng_traverse(g_count_mode, on_solution_scalar, 1);
    if (st != TRAV_COMPLETE && st != TRAV_FIRST && !ge.trav_started)
        scalar_stop(); /* v1: stopped at gray_start, before any traversal line */
    scalar_report(st);
}

/* ================================================================== FAMILY */
static uint8_t g_ga[GACT], g_gb[GACT], g_gl[GACT];
/* S_3 block orders s: pair (f_s1 - f_s0, f_s2 - f_s0), f_0 = 0; row 0 = identity. */
static const uint8_t g_perm[6][3] = {{0, 1, 2}, {0, 2, 1}, {1, 0, 2}, {1, 2, 0}, {2, 0, 1}, {2, 1, 0}};

static int act_index(int a, int b, int l)
{
    return ((a - 1) * FP + b) * (FP - 1) + (l - 1);
}

static void init_actions(void)
{
    for (int a = 1; a < FP; a++)
        for (int b = 0; b < FP; b++)
            for (int l = 1; l < FP; l++) {
                const int g = act_index(a, b, l);
                g_ga[g] = (uint8_t)a;
                g_gb[g] = (uint8_t)b;
                g_gl[g] = (uint8_t)l;
            }
}

/* B3 on one normalized function; every intermediate kept nonnegative. */
static void act_apply(int g, const uint8_t f[FP], uint8_t res[FP])
{
    const int a = g_ga[g], b = g_gb[g], l = g_gl[g];
    const int nfb = FP - f[b];                         /* -f(b) */
    const int nsl = FP - (f[(a + b) % FP] + nfb) % FP; /* -(f(a+b) - f(b)) */
    for (int i = 0; i < FP; i++)
        res[i] = (uint8_t)((l * (f[(a * i + b) % FP] + nfb + i * nsl)) % FP);
}

/* Base-7 code of f2..f6, f2 most significant: numeric order = vector order. */
static int code_of(const uint8_t f[FP])
{
    int code = 0;
    for (int i = 2; i < FP; i++)
        code = FP * code + f[i];
    return code;
}

static void decode(int code, uint8_t f[FP])
{
    f[0] = 0;
    f[1] = 0;
    for (int i = FP - 1; i >= 2; i--) {
        f[i] = (uint8_t)(code % FP);
        code /= FP;
    }
}

static void vec_sub(const uint8_t p[FP], const uint8_t q[FP], uint8_t res[FP])
{
    for (int i = 0; i < FP; i++)
        res[i] = (uint8_t)((p[i] + FP - q[i]) % FP);
}

/* B2: for every slope s, no value of f(i) - s*i occurs more than 3 times. */
static int arc_vec(const uint8_t f[FP])
{
    for (int s = 0; s < FP; s++) {
        int cnt[FP] = {0};
        for (int i = 0; i < FP; i++)
            if (++cnt[(f[i] + FP * FP - s * i) % FP] > 3)
                return 0;
    }
    return 1;
}

/* ================================================================= CATALOG */
static char g_cat[CATALOG_MAX_BYTES + 1];
static size_t g_cat_len, g_cat_pos;
static long g_cat_line;
static uint32_t g_tok[TOK_MAX];
static const char *g_cat_path;
static uint64_t g_cat_fnv;
static int g_cN, g_cR, g_cE, g_arc_total;
static long g_cS;
static uint8_t g_arc_code[NFUN];         /* independent ARC flag, by code */
static uint8_t g_p23_code[NFUN];         /* independent P23 membership, by code */
static int32_t g_id_of_code[NFUN];       /* catalog id or -1, by code */
static uint16_t g_code[NFUN];            /* by id */
static uint8_t g_fv[NFUN][FP];           /* function vector, by id */
static uint8_t g_pflag[NFUN];            /* P flag, by id (validated) */
static uint8_t g_norm[NFUN];             /* normalizer action index, by id (validated) */
static int32_t g_rep[NFUN];              /* rep_id, by id (validated) */
static uint32_t g_orbit[NFUN];           /* orbit size, by representative id */
static uint32_t g_soff[NFUN];            /* stabilizer offset, by representative id */
static uint8_t g_scnt[NFUN];             /* stabilizer size, by representative id */
static uint8_t g_sact[STAB_MAX * NFUN];  /* stabilizers computed here, increasing index */
static uint32_t g_excl[EXCL_CAP];        /* EXCLUDE keys, strictly increasing */
static uint64_t g_start, g_end;          /* batch/validate key range [g_start, g_end) */

static void poll_or_stop(const char *stage)
{
    if (poll_stop() != RUN) {
        out("stop_stage=%s", stage);
        out("stop_reason=%s", g_stop_reason);
        if (g_mode == MODE_BATCH)
            out("resume_key=%llu (START_KEY unchanged; no key was decided)", ULL(g_start));
        finish("UNKNOWN", RC_UNKNOWN);
    }
}

/* S1, S2: all 7^5 normalized functions, ARC flags, identity action, P23. */
static void enumerate_functions(void)
{
    uint8_t f[FP], h[FP];
    int np = 0;
    for (int code = 0; code < NFUN; code++) {
        decode(code, f);
        if (code_of(f) != code)
            internal_error("code/decode round trip fails at %d", code);
        act_apply(0, f, h);
        if (memcmp(f, h, FP) != 0)
            internal_error("identity action (1,0,1) moves function code %d", code);
        g_arc_code[code] = (uint8_t)arc_vec(f);
        g_arc_total += g_arc_code[code];
        g_id_of_code[code] = -1;
    }
    if (g_arc_code[0])
        internal_error("the zero function was classified ARC");
    for (int u = 0; u < FP; u++)
        for (int v = 0; v < FP; v++) {
            for (int i = 0; i < FP; i++)
                f[i] = (uint8_t)((u * (i * i - i) + v * (i * i * i - i)) % FP);
            if (f[0] != 0 || f[1] != 0)
                internal_error("P23 element (%d,%d) is not normalized", u, v);
            const int code = code_of(f);
            if (g_p23_code[code])
                internal_error("P23 parametrization is not injective at (%d,%d)", u, v);
            g_p23_code[code] = 1;
            np++;
        }
    for (int code = 0; code < NFUN; code++) {
        if (!g_p23_code[code])
            continue;
        decode(code, f);
        for (int g = 0; g < GACT; g++) {
            act_apply(g, f, h);
            if (h[0] != 0 || h[1] != 0 || !g_p23_code[code_of(h)])
                internal_error("P23 is not G-invariant (code %d, action %d)", code, g);
        }
    }
    out("arc_functions_independent=%d", g_arc_total);
    out("selfcheck_enumeration=pass (7^5 codes round-trip, identity fixes all, zero not ARC)");
    out("selfcheck_p23=pass (%d distinct normalized functions, G-invariant)", np);
}

/*
 * S3: for all 252 actions and four offset pairs, the B3 DM operations applied
 * entrywise to beta equal the beta of the transformed offsets under
 * c' = l*a*c + l*(f_t(a+b) - f_t(b)), a bijection of each block.
 */
static void selfcheck_derivation(void)
{
    static const int pairs[4][2] = {{2401, 343}, {49, 7}, {1, 16806}, {12345, 6789}};
    uint8_t F[3][FP], TF[3][FP];
    for (int p = 0; p < 4; p++) {
        memset(F[0], 0, FP);
        decode(pairs[p][0], F[1]);
        decode(pairs[p][1], F[2]);
        for (int g = 0; g < GACT; g++) {
            const int a = g_ga[g], b = g_gb[g], l = g_gl[g];
            for (int t = 0; t < 3; t++) {
                act_apply(g, F[t], TF[t]);
                if (TF[t][0] != 0 || TF[t][1] != 0)
                    internal_error("action %d does not keep block %d normalized", g, t);
            }
            for (int i = 0; i < FP; i++)
                if (TF[0][i] != 0)
                    internal_error("action %d does not fix the zero offset", g);
            for (int t = 0; t < 3; t++) {
                int seen = 0;
                for (int c = 0; c < FP; c++) {
                    const int cp = (l * (a * c + F[t][(a + b) % FP] + FP - F[t][b])) % FP;
                    seen |= 1 << cp;
                    for (int i = 0; i < FP; i++) {
                        const int src = (a * i + b) % FP;
                        const int bs = (src * c + F[t][src]) % FP;
                        const int bb = (b * c + F[t][b]) % FP;
                        if ((l * (bs + FP - bb)) % FP != (i * cp + TF[t][i]) % FP)
                            internal_error("B3 derivation fails: action %d pair %d block %d column %d row %d",
                                           g, p, t, c, i);
                    }
                }
                if (seen != (1 << FP) - 1)
                    internal_error("column reindex of action %d block %d is not a bijection", g, t);
            }
        }
    }
    out("selfcheck_action_derivation=pass (252 actions x 4 offset pairs: entrywise B3 DM operations "
        "= beta of T(f) under a bijective c -> c', T(0) = 0, images normalized)");
}

static void read_catalog(void)
{
    struct stat st;
    size_t len = 0;
    uint64_t h = 0xcbf29ce484222325ULL;
    const int fd = open(g_cat_path, O_RDONLY);
    if (fd < 0)
        reject("cannot open CATALOG %s: %s", g_cat_path, strerror(errno));
    if (fstat(fd, &st) != 0 || !S_ISREG(st.st_mode))
        reject("CATALOG %s is not a readable regular file", g_cat_path);
    if (st.st_size < 0 || (uint64_t)st.st_size > (uint64_t)CATALOG_MAX_BYTES)
        reject("CATALOG is %lld bytes, above the %zu-byte limit", (long long)st.st_size, CATALOG_MAX_BYTES);
    for (;;) {
        const ssize_t n = read(fd, g_cat + len, sizeof g_cat - len);
        if (n < 0 && errno == EINTR)
            continue;
        if (n < 0)
            reject("cannot read CATALOG: %s", strerror(errno));
        if (n == 0)
            break;
        len += (size_t)n;
        if (len > CATALOG_MAX_BYTES)
            reject("CATALOG grew above the %zu-byte limit while being read", CATALOG_MAX_BYTES);
    }
    close(fd);
    g_cat_len = len;
    for (size_t k = 0; k < len; k++) {
        h ^= (uint64_t)(unsigned char)g_cat[k];
        h *= 0x100000001b3ULL;
    }
    g_cat_fnv = h;
}

/*
 * One catalog line at g_cat_pos: canonical decimals (no sign, no leading
 * zero, at most 9 digits) separated by single spaces, terminated by one LF.
 * Returns the token count (<= maxtok); anything else is a REJECT.
 */
static int cat_line(int maxtok)
{
    size_t p = g_cat_pos;
    int n = 0;
    g_cat_line++;
    if (p >= g_cat_len)
        reject("CATALOG line %ld is missing (the file ends early)", g_cat_line);
    for (;;) {
        const size_t s = p;
        uint32_t v = 0;
        while (p < g_cat_len && g_cat[p] >= '0' && g_cat[p] <= '9') {
            if (p - s == 9)
                reject("CATALOG line %ld token %d has more than 9 digits", g_cat_line, n + 1);
            v = 10 * v + (uint32_t)(g_cat[p] - '0');
            p++;
        }
        if (p == s)
            reject("CATALOG line %ld token %d is empty or not a decimal", g_cat_line, n + 1);
        if (p - s > 1 && g_cat[s] == '0')
            reject("CATALOG line %ld token %d has a leading zero", g_cat_line, n + 1);
        if (n == maxtok)
            reject("CATALOG line %ld has more than %d tokens", g_cat_line, maxtok);
        g_tok[n++] = v;
        if (p >= g_cat_len)
            reject("CATALOG line %ld does not end with LF", g_cat_line);
        if (g_cat[p] == '\n') {
            p++;
            break;
        }
        if (g_cat[p] != ' ')
            reject("CATALOG line %ld: byte 0x%02x after token %d (need one space or LF)", g_cat_line,
                   (unsigned)(unsigned char)g_cat[p], n);
        p++;
    }
    g_cat_pos = p;
    return n;
}

/*
 * B5: canonical (first, second) ids of a family pair (x1, x2, x1 - x2 ARC):
 * lexicographic minimum over the six block orders of
 * (rep(h1), min over st in Stab(rep(h1)) of id(T_st T_norm(h1) h2)).
 */
static void canonical_pair(const uint8_t x1[FP], const uint8_t x2[FP], int *c1, int *c2)
{
    static const uint8_t zero[FP] = {0};
    const uint8_t *F[3] = {zero, x1, x2};
    uint8_t h1[FP], h2[FP], y[FP], z[FP];
    int best1 = NFUN, best2 = NFUN;
    for (int s = 0; s < 6; s++) {
        vec_sub(F[g_perm[s][1]], F[g_perm[s][0]], h1);
        vec_sub(F[g_perm[s][2]], F[g_perm[s][0]], h2);
        const int i1 = g_id_of_code[code_of(h1)];
        if (i1 < 0)
            internal_error("block order %d maps a family pair to a non-ARC first offset", s);
        const int r1 = g_rep[i1];
        if (r1 > best1)
            continue;
        act_apply(g_norm[i1], h2, y);
        int m = NFUN;
        for (uint32_t q = g_soff[r1]; q < g_soff[r1] + g_scnt[r1]; q++) {
            act_apply(g_sact[q], y, z);
            const int j = g_id_of_code[code_of(z)];
            if (j < 0)
                internal_error("block order %d maps a family pair to a non-ARC second offset", s);
            if (j < m)
                m = j;
        }
        if (r1 < best1 || m < best2) { /* here r1 <= best1 */
            best1 = r1;
            best2 = m;
        }
    }
    *c1 = best1;
    *c2 = best2;
}

/* B5-B7 class of a key's pair; the EXCLUDE list is applied by the caller. */
static int classify_pair(int first, int second)
{
    uint8_t dv[FP];
    int c1, c2;
    if (g_rep[first] != first)
        return CLS_FIRST_NOT_REP;
    vec_sub(g_fv[first], g_fv[second], dv);
    if (g_id_of_code[code_of(dv)] < 0)
        return CLS_NOT_ARC_DIFF;
    canonical_pair(g_fv[first], g_fv[second], &c1, &c2);
    if (c1 > first || (c1 == first && c2 > second))
        internal_error("canonical pair (%d,%d) exceeds the representative-first pair (%d,%d)",
                       c1, c2, first, second);
    if (c1 != first || c2 != second)
        return CLS_NONCANONICAL;
    if (g_pflag[first] && g_pflag[second])
        return CLS_P23;
    return CLS_CASE;
}

/* First index with g_excl[index] >= key. */
static size_t excl_lower_bound(uint64_t key)
{
    size_t lo = 0, hi = (size_t)g_cE;
    while (lo < hi) {
        const size_t mid = lo + (hi - lo) / 2;
        if (g_excl[mid] < key)
            lo = mid + 1;
        else
            hi = mid;
    }
    return lo;
}

static void load_catalog(void)
{
    static const char magic[] = "C21_ARCS_V1\n";
    const size_t ml = sizeof magic - 1;
    uint8_t img[FP];
    read_catalog();
    if (g_cat_len < ml || memcmp(g_cat, magic, ml) != 0)
        reject("CATALOG line 1 must be exactly C21_ARCS_V1 followed by LF");
    g_cat_pos = ml;
    g_cat_line = 1;
    if (cat_line(4) != 4)
        reject("CATALOG line 2 must be 'N R S E'");
    {
        const uint32_t hN = g_tok[0], hR = g_tok[1], hS = g_tok[2], hE = g_tok[3];
        if (hN < 1 || hN > NFUN)
            reject("CATALOG N=%u is not in 1..%d", (unsigned)hN, NFUN);
        if (hR < 1 || hR > hN)
            reject("CATALOG R=%u is not in 1..N", (unsigned)hR);
        if (hS < 1 || (uint64_t)hS > (uint64_t)GACT * hR)
            reject("CATALOG S=%u is not in 1..252*R", (unsigned)hS);
        if ((size_t)hE > EXCL_CAP)
            reject("CATALOG E=%u exceeds %zu", (unsigned)hE, EXCL_CAP);
        g_cN = (int)hN;
        g_cR = (int)hR;
        g_cS = (long)hS;
        g_cE = (int)hE;
    }

    /* N function lines: exactly the ARC set, in vector order. */
    for (int id = 0; id < g_cN; id++) {
        if ((id & CAT_POLL_MASK) == 0)
            poll_or_stop("catalog_function_lines");
        const int nt = cat_line(13);
        if (nt != 13)
            reject("CATALOG line %ld: a function line needs 13 tokens, found %d", g_cat_line, nt);
        if (g_tok[0] != (uint32_t)id)
            reject("CATALOG line %ld: id %u, expected %d", g_cat_line, (unsigned)g_tok[0], id);
        if (g_tok[1] > 1)
            reject("CATALOG line %ld: P must be 0 or 1", g_cat_line);
        if (g_tok[2] >= (uint32_t)g_cN)
            reject("CATALOG line %ld: rep_id %u is not below N", g_cat_line, (unsigned)g_tok[2]);
        if (g_tok[3] < 1 || g_tok[3] > 6 || g_tok[4] > 6 || g_tok[5] < 1 || g_tok[5] > 6)
            reject("CATALOG line %ld: normalizer (a,b,l) out of range", g_cat_line);
        for (int i = 0; i < FP; i++) {
            if (g_tok[6 + i] > 6)
                reject("CATALOG line %ld: f%d is not a residue mod 7", g_cat_line, i);
            g_fv[id][i] = (uint8_t)g_tok[6 + i];
        }
        if (g_fv[id][0] != 0 || g_fv[id][1] != 0)
            reject("CATALOG line %ld: f0 and f1 must be 0 (normalized)", g_cat_line);
        const int code = code_of(g_fv[id]);
        if (id > 0 && code <= (int)g_code[id - 1])
            reject("CATALOG line %ld: functions are not in strictly increasing vector order", g_cat_line);
        if (!g_arc_code[code])
            reject("CATALOG line %ld: function id %d is not ARC", g_cat_line, id);
        g_code[id] = (uint16_t)code;
        g_id_of_code[code] = id;
        g_pflag[id] = (uint8_t)g_tok[1];
        g_rep[id] = (int32_t)g_tok[2];
        g_norm[id] = (uint8_t)act_index((int)g_tok[3], (int)g_tok[4], (int)g_tok[5]);
    }
    if (g_cN != g_arc_total)
        reject("CATALOG lists %d functions; the independent enumeration finds %d ARC functions",
               g_cN, g_arc_total);

    /* P flags, orbit minima (S4: images stay in the catalog), normalizers. */
    int nrep = 0;
    for (int id = 0; id < g_cN; id++) {
        if ((id & CAT_POLL_MASK) == 0)
            poll_or_stop("catalog_orbit_check");
        if (g_pflag[id] != g_p23_code[g_code[id]])
            reject("CATALOG function id %d: P=%d but P23 membership is %d", id, g_pflag[id],
                   g_p23_code[g_code[id]]);
        int min = id;
        for (int g = 0; g < GACT; g++) {
            act_apply(g, g_fv[id], img);
            const int j = g_id_of_code[code_of(img)];
            if (j < 0 || img[0] != 0 || img[1] != 0)
                internal_error("G image of ARC function id %d under action %d is not a catalog function", id, g);
            if (j < min)
                min = j;
        }
        if (g_rep[id] != min)
            reject("CATALOG function id %d: rep_id %d is not the least G image %d", id, (int)g_rep[id], min);
        act_apply(g_norm[id], g_fv[id], img);
        if (code_of(img) != (int)g_code[min])
            reject("CATALOG function id %d: normalizer (%d,%d,%d) does not map it to rep_id %d", id,
                   g_ga[g_norm[id]], g_gb[g_norm[id]], g_gl[g_norm[id]], min);
        g_orbit[min]++;
        nrep += (min == id);
    }
    if (nrep != g_cR)
        reject("CATALOG R=%d but there are %d representatives", g_cR, nrep);

    /* Stabilizers computed here (S4: |Stab| <= 42, identity, orbit-stabilizer). */
    {
        uint32_t soff = 0;
        for (int id = 0; id < g_cN; id++) {
            int cnt = 0, has_identity = 0;
            if (g_rep[id] != id)
                continue;
            g_soff[id] = soff;
            for (int g = 0; g < GACT; g++) {
                act_apply(g, g_fv[id], img);
                if (memcmp(img, g_fv[id], FP) != 0)
                    continue;
                if (cnt == STAB_MAX)
                    internal_error("representative id %d has more than %d stabilizer actions (B3 bound)",
                                   id, STAB_MAX);
                g_sact[soff + (uint32_t)cnt] = (uint8_t)g;
                cnt++;
                has_identity |= (g == 0);
            }
            if (!has_identity)
                internal_error("the identity action does not fix representative id %d", id);
            if (g_orbit[id] * (uint32_t)cnt != (uint32_t)GACT)
                internal_error("orbit-stabilizer fails for representative id %d: %u * %d != %d", id,
                               (unsigned)g_orbit[id], cnt, GACT);
            g_scnt[id] = (uint8_t)cnt;
            soff += (uint32_t)cnt;
        }
    }

    /* R stabilizer lines: exact, duplicate-free, any action order. */
    {
        long ssum = 0;
        int prev = -1;
        uint8_t seen[GACT];
        for (int k = 0; k < g_cR; k++) {
            if ((k & CAT_POLL_MASK) == 0)
                poll_or_stop("catalog_stabilizer_lines");
            const int nt = cat_line(TOK_MAX);
            if (nt < 2)
                reject("CATALOG line %ld: a stabilizer line needs rep_id and stab_count", g_cat_line);
            const uint32_t rid = g_tok[0], cnt = g_tok[1];
            if (rid >= (uint32_t)g_cN || g_rep[rid] != (int32_t)rid)
                reject("CATALOG line %ld: %u is not a representative id", g_cat_line, (unsigned)rid);
            if ((int)rid <= prev)
                reject("CATALOG line %ld: stabilizer lines are not in strictly increasing representative order",
                       g_cat_line);
            if (cnt < 1 || cnt > GACT || (uint32_t)nt != 2 + 3 * cnt)
                reject("CATALOG line %ld: stab_count %u does not match its %d tokens", g_cat_line,
                       (unsigned)cnt, nt);
            memset(seen, 0, sizeof seen);
            for (uint32_t q = 0; q < cnt; q++) {
                const uint32_t a = g_tok[2 + 3 * q], b = g_tok[3 + 3 * q], l = g_tok[4 + 3 * q];
                if (a < 1 || a > 6 || b > 6 || l < 1 || l > 6)
                    reject("CATALOG line %ld: stabilizer action %u is out of range", g_cat_line, (unsigned)q);
                const int g = act_index((int)a, (int)b, (int)l);
                if (seen[g])
                    reject("CATALOG line %ld: duplicate stabilizer action (%u,%u,%u)", g_cat_line,
                           (unsigned)a, (unsigned)b, (unsigned)l);
                seen[g] = 1;
                act_apply(g, g_fv[rid], img);
                if (memcmp(img, g_fv[rid], FP) != 0)
                    reject("CATALOG line %ld: action (%u,%u,%u) does not fix representative %u", g_cat_line,
                           (unsigned)a, (unsigned)b, (unsigned)l, (unsigned)rid);
            }
            if (cnt != (uint32_t)g_scnt[rid])
                reject("CATALOG line %ld: %u stabilizer actions listed; the full stabilizer of %u has %d",
                       g_cat_line, (unsigned)cnt, (unsigned)rid, g_scnt[rid]);
            ssum += (long)cnt;
            prev = (int)rid;
        }
        if (ssum != g_cS)
            reject("CATALOG S=%ld but the stabilizer counts sum to %ld", g_cS, ssum);
    }

    /* E EXCLUDE lines: strictly increasing keys of canonical non-P23 cases. */
    {
        uint64_t prevkey = 0;
        for (int k = 0; k < g_cE; k++) {
            if ((k & CAT_POLL_MASK) == 0)
                poll_or_stop("catalog_exclude_lines");
            if (cat_line(2) != 2)
                reject("CATALOG line %ld: an EXCLUDE line needs exactly 2 tokens", g_cat_line);
            const uint32_t first = g_tok[0], second = g_tok[1];
            if (first >= (uint32_t)g_cN || second >= (uint32_t)g_cN)
                reject("CATALOG line %ld: EXCLUDE id out of range", g_cat_line);
            const uint64_t key = (uint64_t)first * (uint64_t)g_cN + second;
            if (k > 0 && key <= prevkey)
                reject("CATALOG line %ld: EXCLUDE pairs are not strictly increasing", g_cat_line);
            const int cls = classify_pair((int)first, (int)second);
            if (cls != CLS_CASE)
                reject("CATALOG line %ld: EXCLUDE pair (%u,%u) is not a canonical non-P23 family case (class %s)",
                       g_cat_line, (unsigned)first, (unsigned)second, g_cls_name[cls]);
            g_excl[k] = (uint32_t)key;
            prevkey = key;
        }
    }
    if (g_cat_pos != g_cat_len)
        reject("CATALOG has bytes after its %d EXCLUDE lines (line %ld onward)", g_cE, g_cat_line + 1);

    {
        uint32_t oh[GACT + 1];
        int np = 0, any = 0;
        memset(oh, 0, sizeof oh);
        for (int id = 0; id < g_cN; id++) {
            np += g_pflag[id];
            if (g_rep[id] == id)
                oh[g_orbit[id]]++;
        }
        out("catalog_bytes=%zu", g_cat_len);
        out("catalog_fnv1a64=0x%016llx", ULL(g_cat_fnv));
        out("catalog_N=%d", g_cN);
        out("catalog_R=%d", g_cR);
        out("catalog_S=%ld", g_cS);
        out("catalog_E=%d", g_cE);
        out("catalog_p23_functions=%d", np);
        printf("orbit_size_hist=");
        for (int s = 1; s <= GACT; s++)
            if (oh[s] != 0) {
                printf("%s%d:%u", any ? "," : "", s, (unsigned)oh[s]);
                any = 1;
            }
        out("%s", any ? "" : "none");
        out("check_catalog=pass (exact ARC set in vector order, P23 flags, orbit minima, normalizers, "
            "exact stabilizers, |orbit|*|Stab|=252, EXCLUDE = canonical non-P23 cases)");
    }
}

static void load_all_catalog(void)
{
    out("catalog=%s", g_cat_path);
    init_actions();
    enumerate_functions();
    selfcheck_derivation();
    load_catalog();
}

/* ==================================================================== SCAN */
static int g_solve;            /* 1 batch (solve every case), 0 validate (count only) */
static int g_cap, g_case_seconds, g_trace_left;
static uint64_t g_resume;      /* every key in [g_start, g_resume) is decided */
static uint64_t g_cur_key;
static int g_in_case, g_cur_first, g_cur_second;
static const char *g_final_stage = "none";
static char g_final_reason[96] = "none";
static uint64_t n_first_not_rep, n_not_arc, n_noncanon, n_p23, n_excl, n_enum;
static uint64_t n_zero, n_unk_rank, n_unk_time, n_unk_rank_zf, n_zf_pos;
static uint64_t g_gray_total, g_checksum, g_key_checksum;
static uint64_t g_first_case, g_last_case, g_max_case_key;
static int g_have_case;
static double g_max_case_seconds = -1.0;
static uint64_t h_eq[VMAX + 1], h_d[DMAX + 1], h_r[RMAX + 1];
static uint32_t g_cases_by_rep[NFUN];
static int g_unknown_fd = -1;
static char g_unknown_path[PATH_BUF], g_seed_path[PATH_BUF];
static uint64_t g_unknown_count, g_unknown_bytes, g_unknown_checksum;
static uint64_t g_unknown_first[UNKNOWN_PRINT_MAX];
static unsigned g_heartbeats;
static char g_seed[TEXT_BUF];
static size_t g_seed_len;

static void print_hist(const char *name, const uint64_t *h, int n)
{
    int any = 0;
    printf("%s=", name);
    for (int k = 0; k < n; k++)
        if (h[k] != 0) {
            printf("%s%d:%llu", any ? "," : "", k, ULL(h[k]));
            any = 1;
        }
    out("%s", any ? "" : "none");
}

/* Printed once by finish() at every exit after the scan began; returns the B7 accounting. */
static int scan_summary(void)
{
    const uint64_t solved = n_zero + n_unk_rank + n_unk_time;
    const uint64_t decided = n_first_not_rep + n_not_arc + n_noncanon + n_p23 + n_excl + (g_solve ? solved : n_enum);
    const int ok = decided == g_resume - g_start;
    out("range_start_key=%llu", ULL(g_start));
    out("range_end_key=%llu", ULL(g_end));
    out("full_end_key=%llu", ULL((uint64_t)g_cN * (uint64_t)g_cN));
    if (g_in_case)
        out("current_key=%llu", ULL(g_cur_key));
    else
        out("current_key=none");
    out("resume_key=%llu", ULL(g_resume));
    out("range_complete=%s", g_resume == g_end ? "yes" : "no");
    out("keys_accounted=%llu of %llu (%s)", ULL(decided), ULL(g_resume - g_start), ok ? "pass" : "MISMATCH");
    out("keys_first_not_representative=%llu", ULL(n_first_not_rep));
    out("pairs_difference_not_arc=%llu", ULL(n_not_arc));
    out("pairs_noncanonical=%llu", ULL(n_noncanon));
    out("canonical_inside_p23_excluded=%llu", ULL(n_p23));
    out("canonical_exclude_list_excluded=%llu", ULL(n_excl));
    if (g_solve) {
        out("cases_completed=%llu", ULL(solved));
        out("cases_zero=%llu", ULL(n_zero));
        out("cases_unknown_rank_above_cap=%llu", ULL(n_unk_rank));
        out("cases_unknown_case_time=%llu", ULL(n_unk_time));
        out("cases_unknown_rank_with_zero_form=%llu (metadata only; these stay UNKNOWN)", ULL(n_unk_rank_zf));
        out("cases_with_zero_forms_on_L=%llu", ULL(n_zf_pos));
        print_hist("eq_rank_hist", h_eq, VMAX + 1);
        print_hist("null_dim_hist", h_d, DMAX + 1);
        print_hist("ineq_rank_hist", h_r, RMAX + 1);
        out("gray_assignments_zero_cases=%llu", ULL(g_gray_total));
        if (solved > 0)
            out("max_case_seconds=%.3f (key %llu)", g_max_case_seconds, ULL(g_max_case_key));
        out("rolling_checksum=0x%016llx", ULL(g_checksum));
    } else {
        out("cases_enumerated=%llu", ULL(n_enum));
    }
    out("case_keys_checksum=0x%016llx", ULL(g_key_checksum));
    if (g_have_case) {
        out("first_case_key=%llu", ULL(g_first_case));
        out("last_case_key=%llu", ULL(g_last_case));
    } else {
        out("first_case_key=none");
        out("last_case_key=none");
    }
    if (g_solve) {
        const uint64_t shown = g_unknown_count < UNKNOWN_PRINT_MAX ? g_unknown_count : UNKNOWN_PRINT_MAX;
        out("unknown_keys_file=%s", g_unknown_path);
        out("unknown_case_count=%llu", ULL(g_unknown_count));
        out("unknown_file_bytes=%llu", ULL(g_unknown_bytes));
        printf("unknown_keys_first%d=", UNKNOWN_PRINT_MAX);
        for (uint64_t k = 0; k < shown; k++)
            printf("%s%llu", k ? "," : "", ULL(g_unknown_first[k]));
        out("%s", shown ? "" : "none");
        out("unknown_keys_checksum=0x%016llx", ULL(g_unknown_checksum));
        if (g_unknown_fd >= 0) {
            if (fsync(g_unknown_fd) != 0)
                out("unknown_file_sync=FAILED (%s)", strerror(errno));
            else if (close(g_unknown_fd) != 0)
                out("unknown_file_sync=FAILED at close (%s)", strerror(errno));
            else
                out("unknown_file_sync=ok");
            g_unknown_fd = -1;
        }
    }
    out("stop_stage=%s", g_final_stage);
    out("stop_reason=%s", g_final_reason);
    return ok;
}

static void heartbeat(void)
{
    g_heartbeats++;
    out("heartbeat=%u elapsed_seconds=%.0f resume_key=%llu cases_zero=%llu cases_unknown=%llu "
        "cases_enumerated=%llu canonical_excluded=%llu rolling_checksum=0x%016llx",
        g_heartbeats, elapsed(), ULL(g_resume), ULL(n_zero), ULL(n_unk_rank + n_unk_time), ULL(n_enum),
        ULL(n_p23 + n_excl), ULL(g_checksum));
    if (g_unknown_fd >= 0 && fsync(g_unknown_fd) != 0)
        out("unknown_file_sync_warning=%s", strerror(errno));
}

/* Global stop between keys: nothing is partial, resume at g_resume. */
static _Noreturn void scan_stop(const char *stage)
{
    g_final_stage = stage;
    snprintf(g_final_reason, sizeof g_final_reason, "%s", g_stop_reason);
    finish("UNKNOWN", RC_UNKNOWN);
}

static void scan_poll(double *next_beat)
{
    if (poll_stop() != RUN) /* no case runs here, so only signal or wall */
        scan_stop("case_enumeration");
    if (elapsed() >= *next_beat) {
        heartbeat();
        *next_beat = elapsed() + PROGRESS_SECONDS;
    }
}

/*
 * Preserve one UNKNOWN case before it may count as decided.  A full registry
 * stops the run instead (resume at this key; the case is redone later).
 */
static void unknown_append(uint64_t key, int outcome)
{
    char line[64];
    if (g_unknown_count >= UNKNOWN_FILE_MAX) {
        g_final_stage = "unknown_registry";
        snprintf(g_final_reason, sizeof g_final_reason, "unknown_registry_full_%d", UNKNOWN_FILE_MAX);
        finish("UNKNOWN", RC_UNKNOWN);
    }
    const int n = snprintf(line, sizeof line, "%llu %s %d %d\n", ULL(key), outcome == OUT_RANK ? "rank" : "time",
                           ge.have_r ? ge.r : -1, ge.have_r ? ge.zero_forms : -1);
    if (n < 0 || (size_t)n >= sizeof line)
        internal_error("UNKNOWN registry line overflow");
    if (write_all(g_unknown_fd, line, (size_t)n) != 0) {
        const int err = errno;
        out("unknown_record_unwritten=%.*s", n - 1, line);
        internal_error("cannot append to %s: %s", g_unknown_path, strerror(err));
    }
    if (g_unknown_count < UNKNOWN_PRINT_MAX)
        g_unknown_first[g_unknown_count] = key;
    g_unknown_count++;
    g_unknown_bytes += (uint64_t)n;
    g_unknown_checksum += mix64(key ^ ((uint64_t)outcome << 40));
}

static void note_case_key(uint64_t key, int first)
{
    if (!g_have_case) {
        g_first_case = key;
        g_have_case = 1;
    }
    g_last_case = key;
    g_key_checksum += mix64(key);
    g_cases_by_rep[first]++;
}

static void record_case(uint64_t key, int first, int outcome, double secs)
{
    if (outcome != OUT_ZERO)
        unknown_append(key, outcome);
    if (ge.have_eq) {
        h_eq[ge.eqrank]++;
        h_d[ge.d]++;
    }
    if (ge.have_r) {
        h_r[ge.r]++;
        n_zf_pos += (ge.zero_forms > 0);
    }
    uint64_t h = mix64(mix64(key) ^ (uint64_t)outcome);
    if (outcome != OUT_TIME) {
        h = mix64(h ^ (((uint64_t)ge.eqrank << 32) | (uint64_t)ge.d));
        h = mix64(h ^ (((uint64_t)ge.r << 32) | (uint64_t)ge.zero_forms));
    }
    if (outcome == OUT_ZERO) {
        h = mix64(h ^ ge.visited);
        n_zero++;
        g_gray_total += ge.visited;
    } else if (outcome == OUT_RANK) {
        n_unk_rank++;
        n_unk_rank_zf += (ge.zero_forms > 0);
    } else {
        n_unk_time++;
    }
    g_checksum += h;
    note_case_key(key, first);
    if (secs > g_max_case_seconds) {
        g_max_case_seconds = secs;
        g_max_case_key = key;
    }
    if (g_trace_left > 0) {
        g_trace_left--;
        out("trace_case=%llu first=%d second=%d outcome=%s eq_rank=%d null_dim=%d ineq_rank=%d "
            "kernel_dim=%d zero_forms_on_L=%d expected_assignments=%llu visited_assignments=%llu "
            "seconds=%.3f",
            ULL(key), g_cur_first, g_cur_second,
            outcome == OUT_ZERO ? "zero" : outcome == OUT_RANK ? "unknown_rank_above_cap" : "unknown_case_time",
            ge.have_eq ? ge.eqrank : -1, ge.have_eq ? ge.d : -1, ge.have_r ? ge.r : -1,
            ge.have_r ? ge.d - ge.r : -1, ge.have_r ? ge.zero_forms : -1, ULL(ge.expected),
            ULL(ge.visited), secs);
    }
}

/* B1: beta[i][7t+c] = i*c + f_t(i) mod 7 with f_0 = 0, into the engine. */
static void gen_beta(const uint8_t f1[FP], const uint8_t f2[FP])
{
    static const uint8_t zero[FP] = {0};
    const uint8_t *F[3] = {zero, f1, f2};
    for (int i = 0; i < FP; i++)
        for (int t = 0; t < 3; t++)
            for (int c = 0; c < FP; c++)
                ge.beta[i][FP * t + c] = (uint8_t)((i * c + F[t][i]) % FP);
}

static void seed_add(const char *fmt, ...) __attribute__((format(printf, 1, 2)));
static void seed_add(const char *fmt, ...)
{
    va_list ap;
    va_start(ap, fmt);
    const int w = vsnprintf(g_seed + g_seed_len, sizeof g_seed - g_seed_len, fmt, ap);
    va_end(ap);
    if (w < 0 || (size_t)w >= sizeof g_seed - g_seed_len)
        internal_error("seed text buffer overflow");
    g_seed_len += (size_t)w;
}

/* First checked seven-row lift: re-derive its pattern, write dm + seed, exit 10. */
static _Noreturn void batch_found(void)
{
    static const uint8_t zero[FP] = {0};
    const uint8_t *F[3] = {zero, g_fv[g_cur_first], g_fv[g_cur_second]};
    if (ge.Q != FP || ge.K != FP || ge.N != FCOLS)
        internal_error("batch witness shape Q=%d K=%d N=%d, expected 7, 7, 21", ge.Q, ge.K, ge.N);
    for (int i = 0; i < FP; i++)
        for (int t = 0; t < 3; t++)
            for (int c = 0; c < FP; c++) {
                const int col = FP * t + c;
                if (ge.beta[i][col] != (i * c + F[t][i]) % FP || ge.dm[i][col] % FP != ge.beta[i][col])
                    internal_error("witness of key %llu does not reduce to the offset beta at row %d column %d",
                                   ULL(g_cur_key), i, col);
            }
    const size_t dn = format_dm(g_dmtext, sizeof g_dmtext);
    g_seed_len = 0;
    seed_add("seed_format=C21_OFFSET_SEED_V1\n");
    seed_add("tool=%s\n", TOOL);
    seed_add("catalog_fnv1a64=0x%016llx\n", ULL(g_cat_fnv));
    seed_add("catalog_N=%d\n", g_cN);
    seed_add("key=%llu\n", ULL(g_cur_key));
    seed_add("first_id=%d\n", g_cur_first);
    seed_add("second_id=%d\n", g_cur_second);
    for (int t = 1; t < 3; t++)
        seed_add("f%d=%d %d %d %d %d %d %d\n", t, F[t][0], F[t][1], F[t][2], F[t][3], F[t][4], F[t][5], F[t][6]);
    seed_add("beta_columns=7t+c\n");
    for (int i = 0; i < FP; i++) {
        seed_add("beta_row%d=", i);
        for (int col = 0; col < FCOLS; col++)
            seed_add("%d%c", ge.beta[i][col], col + 1 < FCOLS ? ' ' : '\n');
    }
    if (write_exclusive(g_dm_path, g_dmtext, dn) != 0) {
        dump_unwritten("dm", g_dmtext, dn);
        dump_unwritten("seed", g_seed, g_seed_len);
        internal_error("%s", g_msg);
    }
    out("dm_written=%s", g_dm_path);
    out("dm_bytes=%zu", dn);
    if (write_exclusive(g_seed_path, g_seed, g_seed_len) != 0) {
        dump_unwritten("seed", g_seed, g_seed_len);
        internal_error("%s", g_msg);
    }
    out("seed_written=%s", g_seed_path);
    out("seed_bytes=%zu", g_seed_len);
    out("found_key=%llu", ULL(g_cur_key));
    out("found_first_id=%d", g_cur_first);
    out("found_second_id=%d", g_cur_second);
    for (int t = 1; t < 3; t++)
        out("found_f%d=%d %d %d %d %d %d %d", t, F[t][0], F[t][1], F[t][2], F[t][3], F[t][4], F[t][5], F[t][6]);
    out("found_note=producer claim; Main runs the copied CFR checkers, the position-difference checker "
        "and the DM bridge");
    g_final_stage = "witness";
    snprintf(g_final_reason, sizeof g_final_reason, "first_checked_lift");
    finish("FOUND", RC_FOUND);
}

static _Noreturn void on_solution_batch(void)
{
    ge.found++;
    eng_build_dm();
    if (!eng_dm_ok())
        internal_error("candidate of key %llu failed the direct check on the %d row pairs mod %d; "
                       "nothing written", ULL(g_cur_key), ge.K * (ge.K - 1) / 2, ge.N);
    ge.dm_checked++;
    batch_found();
}

/* Whole P2-P8 pipeline for one generated pattern, first-witness semantics. */
static int eng_solve_batch(void)
{
    int st;
    eng_build_crt();
    eng_build_rows();
    if ((st = eng_eq_eliminate()) != RUN || (st = eng_check_equalities()) != RUN ||
        (st = eng_build_basis()) != RUN || (st = eng_compute_G()) != RUN ||
        (st = eng_ineq_basis()) != RUN || (st = eng_check_lambda()) != RUN)
        return st;
    if (ge.r > ge.cap)
        return ENG_CAP;
    if ((st = eng_build_section()) != RUN || (st = eng_check_section()) != RUN)
        return st;
    eng_build_lists();
    return eng_traverse(0, on_solution_batch, 0);
}

static void run_case(uint64_t key, int first, int second)
{
    int outcome = 0;
    g_in_case = 1;
    g_cur_key = key;
    g_cur_first = first;
    g_cur_second = second;
    g_case_start = elapsed();
    eng_reset(FP, FP, g_cap); /* ALL per-pattern state; never the signal flag or outer clock */
    gen_beta(g_fv[first], g_fv[second]);
    if (eng_validate_beta() != 0)
        internal_error("family beta of key %llu violates P2(a): %s", ULL(key), g_msg);
    g_case_limit = g_case_seconds;
    const int st = eng_solve_batch();
    g_case_limit = 0;
    const double secs = elapsed() - g_case_start;
    if (st == STOP_GLOBAL) { /* partial case: resume at THIS key */
        g_final_stage = ge.stop_stage;
        snprintf(g_final_reason, sizeof g_final_reason, "%s", g_stop_reason);
        finish("UNKNOWN", RC_UNKNOWN);
    }
    if (st == TRAV_COMPLETE && ge.found == 0)
        outcome = OUT_ZERO;
    else if (st == ENG_CAP)
        outcome = OUT_RANK;
    else if (st == STOP_CASE)
        outcome = OUT_TIME;
    else
        internal_error("unexpected engine state %d (found %llu) for key %llu", st, ULL(ge.found), ULL(key));
    record_case(key, first, outcome, secs);
    g_in_case = 0;
}

/* B7: every key of [g_start, g_end) once, increasing; g_resume advances only past decided keys. */
static void scan(void)
{
    const uint64_t N = (uint64_t)g_cN;
    size_t xi = excl_lower_bound(g_start);
    double next_beat = elapsed() + PROGRESS_SECONDS;
    g_resume = g_start;
    g_scan_started = 1;
    for (uint64_t first = g_start / N; first < N && first * N < g_end; first++) {
        const uint64_t row = first * N;
        const uint64_t lo = row > g_start ? row : g_start;
        const uint64_t hi = row + N < g_end ? row + N : g_end;
        scan_poll(&next_beat);
        if (g_rep[first] != (int32_t)first) {
            n_first_not_rep += hi - lo;
            g_resume = hi;
            continue;
        }
        for (uint64_t key = lo; key < hi; key++) {
            const int second = (int)(key - row);
            const int cls = classify_pair((int)first, second);
            int solved = 0;
            if (cls == CLS_NOT_ARC_DIFF) {
                n_not_arc++;
            } else if (cls == CLS_NONCANONICAL) {
                n_noncanon++;
            } else if (cls == CLS_P23) {
                n_p23++;
            } else if (cls != CLS_CASE) {
                internal_error("key %llu of a representative row has class %s", ULL(key), g_cls_name[cls]);
            } else {
                while (xi < (size_t)g_cE && g_excl[xi] < key)
                    xi++;
                if (xi < (size_t)g_cE && g_excl[xi] == key) {
                    n_excl++;
                } else if (g_solve) {
                    run_case(key, (int)first, second);
                    solved = 1;
                } else {
                    n_enum++;
                    note_case_key(key, (int)first);
                }
            }
            g_resume = key + 1;
            if (solved || ((key + 1) & ENUM_POLL_MASK) == 0)
                scan_poll(&next_beat);
        }
    }
    if (g_resume != g_end)
        internal_error("scan ended at key %llu instead of END_KEY %llu", ULL(g_resume), ULL(g_end));
}

/* =================================================================== MODES */
static _Noreturn void validate_main(int argc, char **argv)
{
    g_mode = MODE_VALIDATE;
    out("protocol_source=%s", PROTOCOL);
    if (argc != 4)
        reject("usage: %s validate CATALOG WALL_SECONDS", TOOL);
    g_cat_path = argv[2];
    if (!parse_uint(argv[3], 1, WALL_MAX, &g_wall))
        reject("WALL_SECONDS must be a canonical integer in 1..%d", WALL_MAX);
    out("mode=validate");
    out("wall_seconds=%d", g_wall);
    load_all_catalog();
    g_start = 0;
    g_end = (uint64_t)g_cN * (uint64_t)g_cN;
    g_solve = 0;
    scan();
    if (n_excl != (uint64_t)g_cE)
        internal_error("the full scan met %llu EXCLUDE pairs; the catalog lists %d", ULL(n_excl), g_cE);
    out("selfcheck_exclude_coverage=pass (the full scan met each EXCLUDE pair exactly once)");
    {
        int any = 0;
        printf("cases_by_first_representative=");
        for (int id = 0; id < g_cN; id++)
            if (g_rep[id] == id && g_cases_by_rep[id] != 0) {
                printf("%s%d:%u", any ? "," : "", id, (unsigned)g_cases_by_rep[id]);
                any = 1;
            }
        out("%s", any ? "" : "none");
    }
    g_final_stage = "none";
    snprintf(g_final_reason, sizeof g_final_reason, "complete");
    finish("CATALOG_VALID", RC_OK);
}

static void print_vec(const char *name, const uint8_t f[FP])
{
    out("%s=%d %d %d %d %d %d %d", name, f[0], f[1], f[2], f[3], f[4], f[5], f[6]);
}

static _Noreturn void beta_main(int argc, char **argv)
{
    static char out_path[PATH_BUF];
    static char text[TEXT_BUF];
    const uint64_t key_max = (uint64_t)NFUN * NFUN;
    uint64_t key = 0;
    int a = 1, b = 0, l = 1, s = 0, transformed = 0, c1 = -1, c2 = -1;
    uint8_t p1[FP], p2[FP], dv[FP];
    size_t n = 0;
    g_mode = MODE_BETA;
    out("protocol_source=%s", PROTOCOL);
    if (argc != 6 && argc != 10)
        reject("usage: %s beta CATALOG KEY BETA_OUT WALL_SECONDS [A B L S]", TOOL);
    g_cat_path = argv[2];
    if (!parse_u64(argv[3], 0, key_max - 1, &key))
        reject("KEY must be a canonical integer below %llu", ULL(key_max));
    make_path(out_path, argv[4], "");
    if (!parse_uint(argv[5], 1, WALL_MAX, &g_wall))
        reject("WALL_SECONDS must be a canonical integer in 1..%d", WALL_MAX);
    if (argc == 10) {
        if (!parse_uint(argv[6], 1, FP - 1, &a) || !parse_uint(argv[7], 0, FP - 1, &b) ||
            !parse_uint(argv[8], 1, FP - 1, &l) || !parse_uint(argv[9], 0, 5, &s))
            reject("A B L S must be canonical integers: A, L in 1..6, B in 0..6, S in 0..5");
        transformed = 1;
    }
    out("mode=beta");
    out("key=%llu", ULL(key));
    out("beta_out=%s", out_path);
    out("wall_seconds=%d", g_wall);
    preflight_output(out_path);
    load_all_catalog();
    if (key >= (uint64_t)g_cN * (uint64_t)g_cN)
        reject("KEY %llu is not below N*N = %llu", ULL(key), ULL((uint64_t)g_cN * (uint64_t)g_cN));
    const int first = (int)(key / (uint64_t)g_cN), second = (int)(key % (uint64_t)g_cN);
    memcpy(p1, g_fv[first], FP);
    memcpy(p2, g_fv[second], FP);
    vec_sub(p1, p2, dv);
    const int family = g_id_of_code[code_of(dv)] >= 0;
    out("first_id=%d", first);
    out("second_id=%d", second);
    print_vec("f1", p1);
    print_vec("f2", p2);
    out("pair_class=%s", g_cls_name[classify_pair(first, second)]);
    out("pair_in_family=%s", family ? "yes" : "no (f1 - f2 is not ARC: no lift by B2)");
    if (family) {
        canonical_pair(p1, p2, &c1, &c2);
        const int ccls = classify_pair(c1, c2);
        if (ccls != CLS_CASE && ccls != CLS_P23)
            internal_error("canonical pair (%d,%d) has class %s", c1, c2, g_cls_name[ccls]);
        const uint64_t ckey = (uint64_t)c1 * (uint64_t)g_cN + (uint64_t)c2;
        const int listed = excl_lower_bound(ckey) < (size_t)g_cE && g_excl[excl_lower_bound(ckey)] == ckey;
        out("canonical_key=%llu", ULL(ckey));
        if (ccls == CLS_P23)
            out("canonical_class=inside_p23 (excluded)");
        else if (listed)
            out("canonical_class=case in EXCLUDE list (excluded)");
        else
            out("canonical_class=case (solved by batch)");
    } else {
        out("canonical_key=none");
    }
    if (transformed) {
        static const uint8_t zero[FP] = {0};
        const uint8_t *F[3] = {zero, g_fv[first], g_fv[second]};
        uint8_t h1[FP], h2[FP];
        const int g = act_index(a, b, l);
        vec_sub(F[g_perm[s][1]], F[g_perm[s][0]], h1);
        vec_sub(F[g_perm[s][2]], F[g_perm[s][0]], h2);
        act_apply(g, h1, p1);
        act_apply(g, h2, p2);
        out("transform=block order %d (%d,%d,%d) then action (a,b,l)=(%d,%d,%d)", s, g_perm[s][0], g_perm[s][1],
            g_perm[s][2], a, b, l);
        print_vec("emitted_f1", p1);
        print_vec("emitted_f2", p2);
        if (family) {
            int t1, t2;
            vec_sub(p1, p2, dv);
            if (g_id_of_code[code_of(p1)] < 0 || g_id_of_code[code_of(p2)] < 0 || g_id_of_code[code_of(dv)] < 0)
                internal_error("the transformed family pair left the family");
            canonical_pair(p1, p2, &t1, &t2);
            if (t1 != c1 || t2 != c2)
                internal_error("the transformed pair has canonical (%d,%d), the original (%d,%d)", t1, t2, c1, c2);
            out("selfcheck_transform_invariance=pass (canonical key unchanged)");
        }
    }
    eng_reset(FP, FP, 0);
    gen_beta(p1, p2);
    if (eng_validate_beta() != 0)
        internal_error("emitted beta violates P2(a): %s", g_msg);
    for (int i = 0; i < FP; i++)
        for (int col = 0; col < FCOLS; col++) {
            const int w = snprintf(text + n, sizeof text - n, "%d%c", ge.beta[i][col], col + 1 < FCOLS ? ' ' : '\n');
            if (w < 0 || (size_t)w >= sizeof text - n)
                internal_error("beta text buffer overflow");
            n += (size_t)w;
        }
    if (write_exclusive(out_path, text, n) != 0) {
        dump_unwritten("beta", text, n);
        internal_error("%s", g_msg);
    }
    out("beta_written=%s", out_path);
    out("beta_bytes=%zu", n);
    out("beta_use=scalar first|count 7 7 BETA_OUT OUTPREFIX WALL RANK_CAP (v1 or v2); column 7t+c");
    finish("BETA_WRITTEN", RC_OK);
}

static _Noreturn void batch_main(int argc, char **argv)
{
    const uint64_t key_max = (uint64_t)NFUN * NFUN;
    uint64_t start = 0, end = 0;
    int end_full = 0;
    g_mode = MODE_BATCH;
    out("core_port_of=%s", CORE_PORT);
    out("protocol_source=%s", PROTOCOL);
    if (argc < 8 || argc > 10)
        reject("usage: %s batch CATALOG OUTPREFIX WALL_SECONDS RANK_CAP START_KEY END_KEY "
               "[CASE_SECONDS [TRACE_CASES]]", TOOL);
    g_cat_path = argv[2];
    make_path(g_dm_path, argv[3], ".dm.txt");
    make_path(g_seed_path, argv[3], ".seed.txt");
    make_path(g_unknown_path, argv[3], ".unknown.txt");
    if (!parse_uint(argv[4], 1, WALL_MAX, &g_wall))
        reject("WALL_SECONDS must be a canonical integer in 1..%d", WALL_MAX);
    if (!parse_uint(argv[5], 0, RANK_CAP_MAX, &g_cap))
        reject("RANK_CAP must be a canonical integer in 0..%d", RANK_CAP_MAX);
    if (!parse_u64(argv[6], 0, key_max - 1, &start))
        reject("START_KEY must be a canonical integer below %llu", ULL(key_max));
    if (strcmp(argv[7], "end") == 0)
        end_full = 1;
    else if (!parse_u64(argv[7], 1, key_max, &end))
        reject("END_KEY must be a canonical integer in 1..%llu or the word end", ULL(key_max));
    if (argc >= 9 && !parse_uint(argv[8], 0, WALL_MAX, &g_case_seconds))
        reject("CASE_SECONDS must be a canonical integer in 0..%d (0 = no per-case bound)", WALL_MAX);
    if (argc == 10 && !parse_uint(argv[9], 0, TRACE_MAX, &g_trace_left))
        reject("TRACE_CASES must be a canonical integer in 0..%d", TRACE_MAX);
    g_start = start;
    out("mode=batch");
    out("dm_path=%s", g_dm_path);
    out("seed_path=%s", g_seed_path);
    out("unknown_keys_path=%s", g_unknown_path);
    out("wall_seconds=%d", g_wall);
    out("rank_cap=%d", g_cap);
    out("start_key=%llu", ULL(start));
    out("end_key_arg=%s", argv[7]);
    out("case_seconds=%d%s", g_case_seconds, g_case_seconds ? "" : " (no per-case bound)");
    out("trace_cases=%d", g_trace_left);
    preflight_output(g_dm_path);
    preflight_output(g_seed_path);
    preflight_output(g_unknown_path);
    load_all_catalog();
    const uint64_t full = (uint64_t)g_cN * (uint64_t)g_cN;
    if (end_full)
        end = full;
    if (end > full)
        reject("END_KEY %llu exceeds N*N = %llu", ULL(end), ULL(full));
    if (start >= end)
        reject("START_KEY %llu must be below END_KEY %llu", ULL(start), ULL(end));
    g_end = end;
    g_solve = 1;
    g_unknown_fd = open(g_unknown_path, O_WRONLY | O_CREAT | O_EXCL, 0444);
    if (g_unknown_fd < 0)
        reject("cannot exclusively create %s: %s", g_unknown_path, strerror(errno));
    out("unknown_keys_file_created=%s (line: KEY rank|time INEQ_RANK ZERO_FORMS_ON_L; -1 = not computed)",
        g_unknown_path);
    out("range=[%llu,%llu) of full_end_key %llu", ULL(g_start), ULL(g_end), ULL(full));
    scan();
    g_final_stage = "none";
    snprintf(g_final_reason, sizeof g_final_reason, "complete");
    if (n_unk_rank + n_unk_time > 0)
        finish("UNKNOWN", RC_UNKNOWN);
    finish("ZERO_FOR_RANGE", RC_ZERO);
}

int main(int argc, char **argv)
{
    if (clock_gettime(CLOCK_MONOTONIC, &g_t0) != 0) {
        fprintf(stderr, "%s: clock_gettime(CLOCK_MONOTONIC) failed\n", TOOL);
        return RC_INTERNAL;
    }
    out("tool=%s", TOOL);
    install_signals();
    if (argc >= 2 && strcmp(argv[1], "scalar") == 0)
        scalar_main(argc, argv);
    if (argc >= 2 && strcmp(argv[1], "validate") == 0)
        validate_main(argc, argv);
    if (argc >= 2 && strcmp(argv[1], "beta") == 0)
        beta_main(argc, argv);
    if (argc >= 2 && strcmp(argv[1], "batch") == 0)
        batch_main(argc, argv);
    reject("usage: %s scalar|validate|beta|batch ARGS (CLI section of the source header)", TOOL);
}
