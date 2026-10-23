/*
 * crt3_graycheck_c21v1.c
 *
 * Exact GF(3) + Gray-code decision / count of the CRT Z_3-lift of ONE fixed
 * beta pattern to a cyclic (Z_N, K; 1) difference matrix, N = 3Q,
 * gcd(Q,3) = 1, 1 <= Q <= 11, 2 <= K <= 7.
 *
 * Lane cfr33/cfr21 (target CFR(6,21) = 7-row difference matrix over cyclic
 * Z_21).  Written from the definition only: it does not import, read or reuse
 * crt3_lift_c21v1.py or any other primary-lift source or result.  The only
 * lane file consulted was dm_check_c21v1.py, for the dm-raw I/O convention.
 * C11 + POSIX (_XOPEN_SOURCE 700), no libraries, no heap allocation.
 * NOT compiled or executed by its author; every expectation below is derived
 * by hand and must be confirmed by Main.
 *
 * SCOPE.  Every verdict concerns the given beta matrix only.  ZERO means: no
 * alpha in F_3^(K x N) makes CRT(alpha, beta) a (Z_N,K;1) difference matrix.
 * It is not a CFR, difference-matrix or MOLS nonexistence statement; every
 * other beta pattern is untouched.
 *
 * ================================================================= PROOF
 * P1 Definition.  D in Z_N^(K x N) is a (Z_N,K;1) difference matrix iff for
 *    all rows i < j the map c -> D[j][c] - D[i][c] is a bijection
 *    {0..N-1} -> Z_N.
 * P2 CRT split.  x -> (x mod 3, x mod Q) is a ring isomorphism
 *    Z_N -> Z_3 x Z_Q.  Write D[i][c] = CRT(alpha[i][c], beta[i][c]);
 *    differences split componentwise.  For i < j and rho in Z_Q put
 *    C(i,j,rho) = { c : beta[j][c] - beta[i][c] = rho (mod Q) }.  The pair map
 *    is bijective iff (a) |C(i,j,rho)| = 3 for every rho and (b) on each
 *    C(i,j,rho) the three values alpha[j][c] - alpha[i][c] are distinct.
 *    (=>: C(i,j,rho) is the preimage of the 3-set Z_3 x {rho}.  <=: two
 *    columns with one image lie in one C and have equal alpha differences, so
 *    the map is injective on an N-set, hence bijective.)  (a) involves beta
 *    only; input violating it is REJECTED (exit 2): invalid data, not UNSAT.
 * P3 Lemma.  a, b, c in F_3 are distinct iff a + b + c = 0 and a != b.
 *    (=>: 0+1+2 = 0.  <=: c = a forces b = -2a = a; c = b forces a = b.)
 *    With c1 < c2 < c3 the sorted C(i,j,rho) and
 *    dlt_k = alpha[j][c_k] - alpha[i][c_k], condition (b) is
 *      EQUALITY  dlt_1 + dlt_2 + dlt_3 = 0   and   FORM  dlt_1 - dlt_2 != 0.
 *    There are E = Q*K*(K-1)/2 of each; triple e = pair_index*Q + rho, pairs
 *    (i,j) in lexicographic order.
 * P4 Gauge.  alpha[i][c] -> alpha[i][c] + s_i + t_c (on D: add elements of
 *    the subgroup Q*Z_N to whole rows and columns) preserves (b): the dlt of
 *    one triple all move by s_j - s_i.  Each orbit holds exactly one alpha
 *    with alpha[0][*] = 0 = alpha[*][0], namely
 *    alpha[i][c] - alpha[0][c] - alpha[i][0] + alpha[0][0]; the effective
 *    group has order 3^(N+K-1) and acts freely.  So a lift exists iff a
 *    gauged lift exists, and #lifts = 3^(N+K-1) * #gauged lifts.  Unknowns:
 *    x[(i-1)(N-1) + (c-1)] = alpha[i][c] for 1 <= i < K, 1 <= c < N,
 *    V = (K-1)(N-1); gauged entries enter every row as 0.
 * P5 Linear reduction.  A = E x V equality matrix, l_e = forms (vectors in
 *    F_3^V), L = null(A), d = dim L.  Gauged lifts = { x in L : l_e(x) != 0
 *    for every e }.
 *    (i)   [A | I] is row-reduced in place to [R | P], R in RREF, R = P A.
 *          CHECKED: RREF pivot structure, R[i] = P[i] A for every pivot row,
 *          and A b = 0 for the standard basis b_0..b_(d-1) of null(R).  So
 *          null(A) is contained in null(R) = span(b), which is contained in
 *          null(A): L = span(b) and d = V - rank(A).
 *    (ii)  G[e][m] = l_e(b_m), so l_e(B z) = G[e].z.  A greedy row basis of
 *          G selects forms sel[0..r-1], r = rank G, and coefficients lambda
 *          with G[e] = sum_k lambda[e][k] G[sel[k]] for EVERY e (CHECKED).
 *          Hence on L: l_e = sum_k lambda[e][k] y_k, where y_k := l_sel[k].
 *    (iii) A section M (V x r) is built and CHECKED: A M = 0 and
 *          l_sel[j](M u_k) = [j = k] for the unit vectors u_k.  So
 *          phi = (y_0..y_(r-1)) : L -> F_3^r is onto, phi(M y) = y, and each
 *          fibre is a coset of ker phi, of dimension d - r.  Those kernel
 *          directions are invisible to every form: they never change
 *          feasibility, only multiplicity.
 *    (iv)  Gauged lifts exist iff
 *          Y = { y in F_3^r : sum_k lambda[e][k] y_k != 0 for every e }
 *          is nonempty, and #gauged lifts = #Y * 3^(d-r).  Each y_k is itself
 *          a form, so Y lies in {1,2}^r: only 2^r points need testing.
 * P6 Sign symmetry.  x -> -x preserves L and every condition l_e(x) != 0, so
 *    Y = -Y; -1 = 2 in F_3, so negation swaps y_0 = 1 and y_0 = 2.  Hence
 *    Y is nonempty iff it meets {y_0 = 1}, and #Y = 2 * #(Y with y_0 = 1).
 *    Only {1} x {1,2}^(r-1) is visited.  If r = 0 then G = 0, every form
 *    vanishes on L and E >= 1, so Y is empty; the single point of F_3^0 is
 *    still visited for uniformity.
 * P7 Gray traversal.  Bit b of the reflected Gray word g(s) = s ^ (s >> 1)
 *    means y_(1+b) = 1 + bit; g(s-1) and g(s) differ exactly in bit ctz(s),
 *    so s = 0 .. 2^(r-1) - 1 visits each point exactly once.  The residues
 *    v_e = sum_k lambda[e][k] y_k (mod 3) and the number of zero residues are
 *    updated exactly from per-coordinate sparse lists of (e, lambda[e][k])
 *    with lambda[e][k] != 0; a point lies in Y iff that number is 0.  Every
 *    2^16 steps and at the end all residues and the zero count are recomputed
 *    from scratch (mismatch = internal error); after a complete traversal the
 *    visit count must be 2^(r-1) and the final point must be g(2^(r-1) - 1).
 * P8 Witness.  For every point of Y found: x = M y, alpha with the gauge
 *    zeros restored, D = CRT(alpha, beta).  D mod Q = beta, D mod 3 = alpha
 *    and every row pair of D (P1) are checked directly before anything is
 *    written.  A failure is an internal error (exit 3), never a witness.
 * Rank cap.  r > RANK_CAP gives UNKNOWN (exit 30), never an exclusion.
 *    zero_forms_on_L (forms with G[e] = 0) is printed as metadata only.
 * Invariance (used by the metamorphic recipes): permuting BETA columns,
 *    permuting BETA rows, or adding a constant mod Q to one BETA row maps
 *    lifts bijectively and the ungauged equality space and forms onto
 *    themselves up to sign, so eq_rank, null_dim, ineq_rank, kernel_dim,
 *    zero_forms_on_L, the verdict and complete counts must not change.
 *
 * ================================================================= CLI
 *   crt3_graycheck_c21v1 MODE Q K BETA OUTPREFIX WALL_SECONDS RANK_CAP
 *   MODE          first : stop at the first checked witness
 *                 count : traverse everything, check every witness found
 *                         (with y_0 = 1), write the first one
 *   Q             1..11, Q mod 3 != 0; N = 3Q
 *   K             2..7 (K > N allowed: a legitimate negative model)
 *   BETA          exactly K LF-terminated lines, each N single-space-separated
 *                 canonical decimals in 0..Q-1 (lane dm-raw style: no
 *                 comments, CR, blank lines or tabs).  Row 0 need not be zero.
 *   OUTPREFIX     witness path OUTPREFIX.dm.txt; must not exist at start and
 *                 its directory must be writable.  Created with O_EXCL, mode
 *                 0444, only for a checked witness, in dm-raw format (K lines
 *                 of N residues mod N): python3 dm_check_c21v1.py FILE K N.
 *   WALL_SECONDS  1..10800, monotonic clock measured from process start
 *   RANK_CAP      0..26
 * SIGTERM, SIGINT, SIGHUP and SIGXCPU only set a flag.  The flag and the wall
 * clock are polled in every elimination / build / check loop and every 2^16
 * Gray steps.  Nothing is polled while a witness is being written.
 * stdout: key=value lines, each flushed.  Main keys: eq_rank, null_dim,
 * ineq_rank, kernel_dim, zero_forms_on_L, rank_cap_status, y_forms,
 * expected_assignments, visited_assignments, solutions_y0_fixed_found,
 * traversal_complete, solutions_y_total / gauged_lifts / all_lifts_of_beta
 * (complete traversals only), witness_written, stop_reason, status, scope.
 * Exit  10 FOUND: a checked witness was written (count mode also when stopped
 *          after >= 1 witness; then traversal_complete=no)
 *       20 ZERO_FOR_THIS_BETA: complete traversal, no lift of THIS beta
 *       30 UNKNOWN: rank_above_cap, wall limit or signal
 *        2 REJECT: usage, invalid BETA, existing output, unusable directory
 *        3 INTERNAL_ERROR: a failed self-check or witness I/O failure (an
 *          unwritten checked witness is dumped to stdout)
 *
 * ================================================================= MEMORY
 * All state is static, sized by QMAX = 11, KMAX = 7: 414,275 bytes of
 * matrices and lists, a 65,537-byte input buffer and three 4 KiB text
 * buffers, about 481 KiB in total.  No malloc anywhere; locals per call stay
 * below 1 KiB.  Nothing is allocated or copied per Gray step.
 *
 * ================================================================= RECIPES
 * For Main; nothing here has been run.  Pin every input and output by
 * SHA-256 and create fixtures with `set -o noclobber`.
 *   C21=/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/cfr33/cfr21
 *   cc -std=c11 -O2 -Wall -Wextra -Wpedantic \
 *      -o $C21/bin/crt3_graycheck_c21v1 $C21/code/crt3_graycheck_c21v1.c
 * Fixtures (one shell command each):
 *   q1k2/q1k3/q1k4/q1k7.beta (Q = 1, K rows of "0 0 0"):
 *     python3 -c 'import sys;print("\n".join(["0 0 0"]*int(sys.argv[1])))' K
 *   sage21k6m7.beta / sage33k6m11.beta: reduce the pinned dm-raw Sage
 *   DM_21_6_1 mod 7 / DM_33_6_1 mod 11 (M = 7 / 11):
 *     python3 -c 'import sys;m=int(sys.argv[1]);t=open(sys.argv[2]).read();assert t.endswith("\n");print("\n".join(" ".join(str(int(v)%m) for v in l.split(" ")) for l in t[:-1].split("\n")))' M FILE
 *   q7k7.beta, the target (column index 7t+c):
 *     python3 -c 'u=(0,1,3);print("\n".join(" ".join(str((i*c+u[t]*(i*i-i))%7) for t in range(3) for c in range(7)) for i in range(7)))'
 * Run: $C21/bin/crt3_graycheck_c21v1 MODE Q K FIXTURE OUTDIR/NAME WALL RANK_CAP
 * Expected values, derived by hand from P1-P8 (NOT executed):
 *   q1k2 count: eq_rank=1 null_dim=1 ineq_rank=1 kernel_dim=0
 *     expected_assignments=1 solutions_y0_fixed_found=1 solutions_y_total=2
 *     all_lifts_of_beta=2*3^4 (= 162); exit 10.
 *   q1k3 count: eq_rank=2 null_dim=2 ineq_rank=2 kernel_dim=0
 *     expected_assignments=2 solutions_y0_fixed_found=1 solutions_y_total=2
 *     all_lifts_of_beta=2*3^5 (= 486); exit 10.
 *   q1k3 first: exit 10; python3 $C21/code/dm_check_c21v1.py NAME.dm.txt 3 3
 *     prints DM PASS.
 *   q1k3 with RANK_CAP 1: rank_cap_status=exceeded, stop_reason=rank_above_cap,
 *     exit 30.
 *   q1k4 count (K > N): eq_rank=3 null_dim=3 ineq_rank=3 expected_assignments=4
 *     solutions_y0_fixed_found=0; exit 20.
 *   q1k7 count: eq_rank=6 null_dim=6 ineq_rank=6 expected_assignments=32
 *     solutions_y0_fixed_found=0; exit 20.
 *   Independent brute force over all alpha for Q = 1, where alpha is the
 *   whole DM (K=2: 162, K=3: 486, K=4: 0):
 *     python3 -c 'import itertools as I;K=3;print(sum(all(len({(f[3*j+c]-f[3*i+c])%3 for c in range(3)})==3 for i in range(K) for j in range(i+1,K)) for f in I.product(range(3),repeat=3*K)))'
 *   sage21k6m7 (Q=7 K=6) and sage33k6m11 (Q=11 K=6): the Sage DM mod 3 is a
 *     lift, so first and count must exit 10 with a witness passing
 *     dm_check_c21v1.py FILE 6 21 / FILE 6 33.  Exit 20 there is a BUG; exit
 *     30 with rank_above_cap leaves the control unexercised (record ineq_rank).
 *   Metamorphic: the sage fixtures and q7k7 with reversed column order, with
 *     rows 0 and 1 swapped, and with 1 added mod Q to row 1 must reproduce
 *     eq_rank, null_dim, ineq_rank, kernel_dim, zero_forms_on_L, status and
 *     (count mode, complete) solutions_y_total.
 *   Rejections, exit 2, each with its reject_reason: q7k7 with one entry
 *     changed by +1 mod 7 (residue multiplicity), an entry 7, a row of 20 or
 *     22 entries, 6 rows for K=7, CRLF, no final LF, "07", a double space;
 *     Q=3, Q=12, K=1, K=8, WALL 0 or 10801, RANK_CAP 27, MODE other than
 *     first|count; an existing NAME.dm.txt; a missing output directory.
 *   Target: count 7 7 q7k7.beta NAME 10800 26 (no expected verdict or rank).
 *   Stop path: SIGTERM during a traversal longer than 2^16 steps (or a small
 *     WALL) must print stop_reason=signal_15 (or wall_limit_<W>s) and exit 30,
 *     or exit 10 with traversal_complete=no if count mode already holds a
 *     witness.  A stop inside the build loops prints stop_stage.
 * Cost: build and checks below about 5e7 byte operations; the traversal
 * makes 2^(r-1) steps, each touching the list of one coordinate, plus E*r
 * work per recomputation (every 2^16 steps) and V*r + K*K*N per witness.
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

#define TOOL "crt3_graycheck_c21v1"

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

enum { RC_REJECT = 2, RC_INTERNAL = 3, RC_FOUND = 10, RC_ZERO = 20, RC_UNKNOWN = 30 };

/* ------------------------------------------------------------------ state */
static int g_count_mode; /* 0 first, 1 count */
static int g_Q, g_K, g_N, g_V, g_E, g_wall, g_cap;
static const char *g_beta_path;
static char g_dm_path[PATH_BUF];
static struct timespec g_t0;
static volatile sig_atomic_t g_signal;
static char g_stop_reason[64];

static char g_file[FILE_MAX + 1];
static uint8_t g_beta[KMAX][NMAX];
static uint8_t g_tri_i[EMAX], g_tri_j[EMAX], g_tri_c[EMAX][3];
static uint8_t g_A[EMAX][VMAX];         /* equalities, never modified */
static uint8_t g_L[EMAX][VMAX];         /* forms, never modified */
static uint8_t g_aug[EMAX][AUGW];       /* [A | I] reduced in place to [R | P] */
static int g_pivcol[EMAX];
static uint8_t g_ispiv[VMAX];
static int g_eqrank, g_d;
static uint8_t g_B[DMAX][VMAX];         /* basis of L = null(A) */
static uint8_t g_G[EMAX][DMAX];         /* G[e][m] = l_e(b_m) */
static int g_r, g_zero_forms;
static int g_sel[RMAX], g_wpiv[RMAX];
static uint8_t g_W[RMAX][DMAX];         /* reduced selected rows, W = T H */
static uint8_t g_T[RMAX][RMAX];
static uint8_t g_lam[EMAX][RMAX];       /* l_e = sum_k lam[e][k] y_k on L */
static uint8_t g_M[VMAX][RANK_CAP_MAX]; /* section: x = M y */
static uint32_t g_off[RANK_CAP_MAX + 1];
static uint16_t g_le[EMAX * RANK_CAP_MAX];
static uint8_t g_lc[EMAX * RANK_CAP_MAX];
static uint8_t g_v[EMAX], g_y[RANK_CAP_MAX];
static int g_zc;
static uint8_t g_crt[3][QMAX];
static uint8_t g_x[VMAX];
static int g_dm[KMAX][NMAX];
static char g_dmtext[TEXT_BUF];
static int g_dm_written;
static uint64_t g_expected, g_visited, g_found, g_dm_checked, g_rechecks;

/* ------------------------------------------------------- output and exits */
static void out(const char *fmt, ...) __attribute__((format(printf, 1, 2)));
static _Noreturn void finish(const char *status, int rc);
static _Noreturn void reject(const char *fmt, ...) __attribute__((format(printf, 1, 2)));
static _Noreturn void internal_error(const char *fmt, ...) __attribute__((format(printf, 1, 2)));

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

static _Noreturn void finish(const char *status, int rc)
{
    out("elapsed_seconds=%.3f", elapsed());
    out("status=%s", status);
    out("scope=CRT Z_3 lift of this exact beta pattern only; "
        "not a CFR, difference-matrix or MOLS nonexistence claim");
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

static void install_signals(void)
{
    static const int sigs[] = {
        SIGTERM, SIGINT, SIGHUP,
#ifdef SIGXCPU
        SIGXCPU,
#endif
    };
    struct sigaction sa;
    memset(&sa, 0, sizeof sa);
    sa.sa_handler = on_signal;
    sigemptyset(&sa.sa_mask);
#ifdef SA_RESTART
    sa.sa_flags = SA_RESTART;
#endif
    for (size_t k = 0; k < sizeof sigs / sizeof sigs[0]; k++)
        if (sigaction(sigs[k], &sa, NULL) != 0)
            internal_error("sigaction(%d) failed: %s", sigs[k], strerror(errno));
}

static int stop_requested(void)
{
    const int sig = (int)g_signal;
    if (sig != 0) {
        snprintf(g_stop_reason, sizeof g_stop_reason, "signal_%d", sig);
        return 1;
    }
    if (elapsed() >= (double)g_wall) {
        snprintf(g_stop_reason, sizeof g_stop_reason, "wall_limit_%ds", g_wall);
        return 1;
    }
    return 0;
}

static void poll_build(const char *stage)
{
    if (stop_requested()) {
        out("stop_stage=%s", stage);
        out("stop_reason=%s", g_stop_reason);
        finish("UNKNOWN", RC_UNKNOWN);
    }
}

/* ------------------------------------------------------- CLI and input */
static int parse_uint(const char *s, int lo, int hi, int *val)
{
    const size_t n = strlen(s);
    long v = 0;
    if (n == 0 || n > 6 || (n > 1 && s[0] == '0'))
        return 0;
    for (size_t k = 0; k < n; k++) {
        if (s[k] < '0' || s[k] > '9')
            return 0;
        v = 10 * v + (s[k] - '0');
    }
    if (v < lo || v > hi)
        return 0;
    *val = (int)v;
    return 1;
}

static void parse_cli(int argc, char **argv)
{
    if (argc != 8)
        reject("usage: %s first|count Q K BETA OUTPREFIX WALL_SECONDS RANK_CAP", TOOL);
    if (strcmp(argv[1], "first") == 0)
        g_count_mode = 0;
    else if (strcmp(argv[1], "count") == 0)
        g_count_mode = 1;
    else
        reject("MODE must be first or count");
    if (!parse_uint(argv[2], 1, QMAX, &g_Q) || g_Q % 3 == 0)
        reject("Q must be a canonical integer in 1..%d with gcd(Q,3)=1", QMAX);
    if (!parse_uint(argv[3], 2, KMAX, &g_K))
        reject("K must be a canonical integer in 2..%d", KMAX);
    g_N = 3 * g_Q;
    g_beta_path = argv[4];
    if (argv[5][0] == '\0')
        reject("OUTPREFIX must be nonempty");
    const int w = snprintf(g_dm_path, sizeof g_dm_path, "%s.dm.txt", argv[5]);
    if (w < 0 || (size_t)w >= sizeof g_dm_path)
        reject("OUTPREFIX too long");
    if (!parse_uint(argv[6], 1, WALL_MAX, &g_wall))
        reject("WALL_SECONDS must be a canonical integer in 1..%d", WALL_MAX);
    if (!parse_uint(argv[7], 0, RANK_CAP_MAX, &g_cap))
        reject("RANK_CAP must be a canonical integer in 0..%d", RANK_CAP_MAX);
    out("mode=%s", g_count_mode ? "count" : "first");
    out("Q=%d", g_Q);
    out("K=%d", g_K);
    out("N=%d", g_N);
    out("beta_file=%s", g_beta_path);
    out("dm_path=%s", g_dm_path);
    out("wall_seconds=%d", g_wall);
    out("rank_cap=%d", g_cap);
}

/* The witness is created only at the end; refuse early instead of losing it. */
static void preflight_output(void)
{
    static char dir[PATH_BUF];
    struct stat st;
    const char *slash = strrchr(g_dm_path, '/');
    if (lstat(g_dm_path, &st) == 0)
        reject("output %s already exists; refusing to overwrite", g_dm_path);
    if (errno != ENOENT)
        reject("cannot check output %s: %s", g_dm_path, strerror(errno));
    if (slash == NULL) {
        strcpy(dir, ".");
    } else if (slash == g_dm_path) {
        strcpy(dir, "/");
    } else {
        const size_t n = (size_t)(slash - g_dm_path);
        memcpy(dir, g_dm_path, n);
        dir[n] = '\0';
    }
    if (stat(dir, &st) != 0 || !S_ISDIR(st.st_mode))
        reject("output directory %s does not exist", dir);
    if (access(dir, W_OK | X_OK) != 0)
        reject("output directory %s is not writable", dir);
}

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
    for (int i = 0; i < g_K; i++)
        for (int c = 0; c < g_N; c++) {
            const size_t s = p;
            while (p < len && g_file[p] >= '0' && g_file[p] <= '9')
                p++;
            const size_t tl = p - s;
            if (tl == 0)
                reject("BETA row %d entry %d is missing (need %d rows of %d entries)", i, c, g_K, g_N);
            if (tl > 2 || (tl == 2 && g_file[s] == '0'))
                reject("BETA row %d entry %d is not a canonical decimal below %d", i, c, g_Q);
            const int v = tl == 1 ? g_file[s] - '0' : 10 * (g_file[s] - '0') + (g_file[s + 1] - '0');
            if (v >= g_Q)
                reject("BETA row %d entry %d = %d is not in 0..%d", i, c, v, g_Q - 1);
            g_beta[i][c] = (uint8_t)v;
            const char want = c + 1 < g_N ? ' ' : '\n';
            if (p >= len || g_file[p] != want)
                reject("BETA row %d: entry %d must be followed by %s", i, c,
                       want == ' ' ? "one space" : "LF (exactly N entries per row)");
            p++;
        }
    if (p != len)
        reject("BETA has more than K=%d rows", g_K);
}

/* P2(a) validation and the triples C(i,j,rho), columns in increasing order. */
static void validate_beta(void)
{
    int e = 0, row0_zero = 1;
    for (int c = 0; c < g_N; c++)
        row0_zero &= (g_beta[0][c] == 0);
    for (int i = 0; i < g_K; i++)
        for (int j = i + 1; j < g_K; j++) {
            int cnt[QMAX] = {0};
            uint8_t pos[QMAX][3] = {{0}};
            for (int c = 0; c < g_N; c++) {
                const int rho = (g_beta[j][c] - g_beta[i][c] + g_Q) % g_Q;
                if (cnt[rho] == 3)
                    reject("beta rows %d,%d: residue %d occurs more than 3 times (need exactly 3)",
                           i, j, rho);
                pos[rho][cnt[rho]++] = (uint8_t)c;
            }
            for (int rho = 0; rho < g_Q; rho++) {
                if (cnt[rho] != 3)
                    reject("beta rows %d,%d: residue %d occurs %d times (need exactly 3)",
                           i, j, rho, cnt[rho]);
                g_tri_i[e] = (uint8_t)i;
                g_tri_j[e] = (uint8_t)j;
                memcpy(g_tri_c[e], pos[rho], 3);
                e++;
            }
        }
    g_E = e;
    out("beta_row0_zero=%s", row0_zero ? "yes" : "no");
    out("beta_check=pass (all %d row pairs: every residue mod %d occurs exactly 3 times)",
        g_K * (g_K - 1) / 2, g_Q);
}

static void build_crt(void)
{
    uint8_t seen[3][QMAX] = {{0}};
    for (int x = 0; x < g_N; x++) {
        const int a = x % 3, b = x % g_Q;
        if (seen[a][b])
            internal_error("CRT map Z_%d -> Z_3 x Z_%d is not injective", g_N, g_Q);
        seen[a][b] = 1;
        g_crt[a][b] = (uint8_t)x;
    }
}

/* ------------------------------------------------------- linear algebra */
static int var_index(int i, int c)
{
    return (i == 0 || c == 0) ? -1 : (i - 1) * (g_N - 1) + (c - 1);
}

static void add_term(uint8_t *row, int i, int c, int coef)
{
    const int v = var_index(i, c);
    if (v >= 0)
        row[v] = (uint8_t)((row[v] + coef) % 3);
}

/* P3: dlt_k = alpha[j][c_k] - alpha[i][c_k]; coefficient -1 is stored as 2. */
static void build_rows(void)
{
    g_V = (g_K - 1) * (g_N - 1);
    for (int e = 0; e < g_E; e++) {
        const int i = g_tri_i[e], j = g_tri_j[e];
        const int c1 = g_tri_c[e][0], c2 = g_tri_c[e][1], c3 = g_tri_c[e][2];
        add_term(g_A[e], j, c1, 1);
        add_term(g_A[e], i, c1, 2);
        add_term(g_A[e], j, c2, 1);
        add_term(g_A[e], i, c2, 2);
        add_term(g_A[e], j, c3, 1);
        add_term(g_A[e], i, c3, 2);
        add_term(g_L[e], j, c1, 1);
        add_term(g_L[e], i, c1, 2);
        add_term(g_L[e], j, c2, 2);
        add_term(g_L[e], i, c2, 1);
    }
}

/* P5(i): Gauss-Jordan on [A | I]; afterwards R = left block, P = right block. */
static void eq_eliminate(void)
{
    const int E = g_E, V = g_V, W = V + E;
    int row = 0;
    for (int e = 0; e < E; e++) {
        memcpy(g_aug[e], g_A[e], (size_t)V);
        g_aug[e][V + e] = 1;
    }
    for (int col = 0; col < V && row < E; col++) {
        poll_build("equality_elimination");
        int p = row;
        while (p < E && g_aug[p][col] == 0)
            p++;
        if (p == E)
            continue;
        if (p != row)
            for (int t = 0; t < W; t++) {
                const uint8_t h = g_aug[p][t];
                g_aug[p][t] = g_aug[row][t];
                g_aug[row][t] = h;
            }
        if (g_aug[row][col] == 2) /* 2^-1 = 2 in F_3 */
            for (int t = 0; t < W; t++)
                g_aug[row][t] = (uint8_t)((2 * g_aug[row][t]) % 3);
        for (int i = 0; i < E; i++) {
            const int f = g_aug[i][col];
            if (i == row || f == 0)
                continue;
            for (int t = 0; t < W; t++) /* row_i -= f * pivot row */
                g_aug[i][t] = (uint8_t)((g_aug[i][t] + (3 - f) * g_aug[row][t]) % 3);
        }
        g_pivcol[row] = col;
        g_ispiv[col] = 1;
        row++;
    }
    g_eqrank = row;
    g_d = V - row;
}

static void check_equalities(void)
{
    const int E = g_E, V = g_V;
    for (int i = 0; i < g_eqrank; i++) {
        poll_build("equality_rref_check");
        if (i > 0 && g_pivcol[i] <= g_pivcol[i - 1])
            internal_error("RREF pivot columns not increasing at row %d", i);
        for (int i2 = 0; i2 < E; i2++)
            if (g_aug[i2][g_pivcol[i]] != (i2 == i))
                internal_error("RREF pivot column %d is not a unit vector", g_pivcol[i]);
    }
    for (int i = g_eqrank; i < E; i++)
        for (int v = 0; v < V; v++)
            if (g_aug[i][v] != 0)
                internal_error("RREF row %d beyond the rank is nonzero", i);
    for (int i = 0; i < g_eqrank; i++) {
        poll_build("equality_certificate");
        for (int v = 0; v < V; v++) {
            int s = 0;
            for (int e = 0; e < E; e++)
                s += g_aug[i][V + e] * g_A[e][v];
            if (s % 3 != g_aug[i][v])
                internal_error("certificate R = P*A fails at row %d column %d", i, v);
        }
    }
}

/* Standard basis of null(R): one vector per free column f. */
static void build_basis(void)
{
    int m = 0;
    for (int f = 0; f < g_V; f++) {
        if (g_ispiv[f])
            continue;
        g_B[m][f] = 1;
        for (int i = 0; i < g_eqrank; i++)
            g_B[m][g_pivcol[i]] = (uint8_t)((3 - g_aug[i][f]) % 3);
        m++;
    }
    if (m != g_d)
        internal_error("nullspace basis has %d vectors, expected %d", m, g_d);
    for (int k = 0; k < g_d; k++) {
        poll_build("nullspace_check");
        for (int e = 0; e < g_E; e++) {
            int s = 0;
            for (int v = 0; v < g_V; v++)
                s += g_A[e][v] * g_B[k][v];
            if (s % 3 != 0)
                internal_error("basis vector %d violates equality %d", k, e);
        }
    }
}

static void compute_G(void)
{
    for (int e = 0; e < g_E; e++) {
        int nonzero = 0;
        poll_build("form_projection");
        for (int m = 0; m < g_d; m++) {
            int s = 0;
            for (int v = 0; v < g_V; v++)
                s += g_L[e][v] * g_B[m][v];
            g_G[e][m] = (uint8_t)(s % 3);
            nonzero |= g_G[e][m];
        }
        if (!nonzero)
            g_zero_forms++;
    }
}

/*
 * P5(ii): greedy row basis of G with coefficient tracking.  Invariants:
 * W[k] = sum_j T[k][j] G[sel[j]], T lower triangular with nonzero diagonal,
 * W[k][wpiv[k]] = 1 and W[k][wpiv[j]] = 0 for j < k.
 */
static void ineq_basis(void)
{
    const int d = g_d;
    uint8_t g[DMAX], c[RMAX], lp[RMAX];
    for (int e = 0; e < g_E; e++) {
        const int r = g_r;
        int p = 0;
        poll_build("form_basis");
        memcpy(g, g_G[e], (size_t)d);
        for (int k = 0; k < r; k++) { /* g -= g[wpiv[k]] * W[k] */
            const int f = g[g_wpiv[k]];
            c[k] = (uint8_t)f;
            if (f != 0)
                for (int t = 0; t < d; t++)
                    g[t] = (uint8_t)((g[t] + (3 - f) * g_W[k][t]) % 3);
        }
        for (int j = 0; j < r; j++) { /* lp = sum_k c[k] T[k] */
            int s = 0;
            for (int k = 0; k < r; k++)
                s += c[k] * g_T[k][j];
            lp[j] = (uint8_t)(s % 3);
        }
        while (p < d && g[p] == 0)
            p++;
        if (p == d) { /* G[e] = sum_j lp[j] G[sel[j]] */
            memcpy(g_lam[e], lp, (size_t)r);
            continue;
        }
        const int sc = g[p]; /* sc^-1 = sc in F_3 */
        for (int t = 0; t < d; t++)
            g_W[r][t] = (uint8_t)((g[t] * sc) % 3);
        for (int j = 0; j < r; j++) /* W[r] = sc * (G[e] - sum_j lp[j] G[sel[j]]) */
            g_T[r][j] = (uint8_t)((sc * (3 - lp[j])) % 3);
        g_T[r][r] = (uint8_t)sc;
        g_wpiv[r] = p;
        g_sel[r] = e;
        g_lam[e][r] = 1;
        g_r = r + 1;
    }
}

static void check_lambda(void)
{
    for (int e = 0; e < g_E; e++) {
        poll_build("form_basis_check");
        for (int m = 0; m < g_d; m++) {
            int s = 0;
            for (int k = 0; k < g_r; k++)
                s += g_lam[e][k] * g_G[g_sel[k]][m];
            if (s % 3 != g_G[e][m])
                internal_error("form %d is not sum_k lambda G[sel[k]] at coordinate %d", e, m);
        }
    }
}

/*
 * P5(iii): column k of M is B z with G[sel[j]].z = [j = k].  Since W = T H,
 * solve W z = T u_k on the pivot coordinates by back-substitution.
 */
static void build_section(void)
{
    const int r = g_r, d = g_d;
    uint8_t z[DMAX];
    for (int k = 0; k < r; k++) {
        poll_build("section");
        memset(z, 0, sizeof z);
        for (int kk = r - 1; kk >= 0; kk--) {
            int s = g_T[kk][k];
            for (int j = kk + 1; j < r; j++)
                s += 2 * g_W[kk][g_wpiv[j]] * z[g_wpiv[j]];
            z[g_wpiv[kk]] = (uint8_t)(s % 3);
        }
        for (int v = 0; v < g_V; v++) {
            int s = 0;
            for (int m = 0; m < d; m++)
                s += z[m] * g_B[m][v];
            g_M[v][k] = (uint8_t)(s % 3);
        }
    }
}

static void check_section(void)
{
    for (int k = 0; k < g_r; k++) {
        poll_build("section_check");
        for (int e = 0; e < g_E; e++) {
            int s = 0;
            for (int v = 0; v < g_V; v++)
                s += g_A[e][v] * g_M[v][k];
            if (s % 3 != 0)
                internal_error("section column %d violates equality %d", k, e);
        }
        for (int j = 0; j < g_r; j++) {
            int s = 0;
            for (int v = 0; v < g_V; v++)
                s += g_L[g_sel[j]][v] * g_M[v][k];
            if (s % 3 != (j == k))
                internal_error("section column %d gives y_%d != [%d = %d]", k, j, j, k);
        }
    }
}

static void build_lists(void)
{
    uint32_t n = 0;
    for (int k = 0; k < g_r; k++) {
        g_off[k] = n;
        for (int e = 0; e < g_E; e++)
            if (g_lam[e][k] != 0) {
                g_le[n] = (uint16_t)e;
                g_lc[n] = g_lam[e][k];
                n++;
            }
    }
    g_off[g_r] = n;
}

static void print_y_forms(void)
{
    printf("y_forms=");
    for (int k = 0; k < g_r; k++)
        printf("%s%d", k ? "," : "", g_sel[k]);
    out("%s", g_r ? "" : "none");
}

/* ------------------------------------------------------- witness (P8) */
static void build_dm(void)
{
    for (int v = 0; v < g_V; v++) {
        int s = 0;
        for (int k = 0; k < g_r; k++)
            s += g_M[v][k] * g_y[k];
        g_x[v] = (uint8_t)(s % 3);
    }
    for (int i = 0; i < g_K; i++)
        for (int c = 0; c < g_N; c++) {
            const int v = var_index(i, c);
            g_dm[i][c] = g_crt[v < 0 ? 0 : g_x[v]][g_beta[i][c]];
        }
}

/* Direct definition check of D (P1) and of its CRT components. */
static int dm_ok(void)
{
    for (int i = 0; i < g_K; i++)
        for (int c = 0; c < g_N; c++) {
            const int v = var_index(i, c), a = v < 0 ? 0 : g_x[v], x = g_dm[i][c];
            if (x < 0 || x >= g_N || x % g_Q != g_beta[i][c] || x % 3 != a)
                return 0;
        }
    for (int i = 0; i < g_K; i++)
        for (int j = i + 1; j < g_K; j++) {
            uint8_t seen[NMAX] = {0};
            for (int c = 0; c < g_N; c++) {
                const int dl = (g_dm[j][c] - g_dm[i][c] + g_N) % g_N;
                if (seen[dl])
                    return 0;
                seen[dl] = 1;
            }
        }
    return 1;
}

static void dump_unwritten(size_t n)
{
    out("unwritten_dm_begin");
    fwrite(g_dmtext, 1, n, stdout);
    out("unwritten_dm_end");
}

static void write_dm(void)
{
    size_t n = 0;
    for (int i = 0; i < g_K; i++)
        for (int c = 0; c < g_N; c++) {
            const int w = snprintf(g_dmtext + n, sizeof g_dmtext - n, "%d%c", g_dm[i][c],
                                   c + 1 < g_N ? ' ' : '\n');
            if (w < 0 || (size_t)w >= sizeof g_dmtext - n)
                internal_error("witness text buffer overflow");
            n += (size_t)w;
        }
    const int fd = open(g_dm_path, O_WRONLY | O_CREAT | O_EXCL, 0444);
    if (fd < 0) {
        dump_unwritten(n);
        internal_error("cannot exclusively create %s: %s", g_dm_path, strerror(errno));
    }
    for (size_t off = 0; off < n;) {
        const ssize_t w = write(fd, g_dmtext + off, n - off);
        if (w < 0 && errno == EINTR)
            continue;
        if (w <= 0) {
            dump_unwritten(n);
            internal_error("write to %s failed: %s", g_dm_path, w < 0 ? strerror(errno) : "no progress");
        }
        off += (size_t)w;
    }
    if (fsync(fd) != 0 || close(fd) != 0) {
        dump_unwritten(n);
        internal_error("fsync/close of %s failed: %s", g_dm_path, strerror(errno));
    }
    g_dm_written = 1;
    out("dm_written=%s", g_dm_path);
    out("dm_bytes=%zu", n);
}

static void on_solution(void)
{
    g_found++;
    build_dm();
    if (!dm_ok())
        internal_error("y-space solution %llu failed the direct DM check; nothing written",
                       (unsigned long long)g_found);
    g_dm_checked++;
    if (!g_dm_written)
        write_dm();
}

/* ------------------------------------------------------- Gray traversal */
static void recompute_check(void)
{
    int zc = 0;
    for (int e = 0; e < g_E; e++) {
        int s = 0;
        for (int k = 0; k < g_r; k++)
            s += g_lam[e][k] * g_y[k];
        s %= 3;
        if (s != g_v[e])
            internal_error("incremental residue of form %d differs from recomputation", e);
        zc += (s == 0);
    }
    if (zc != g_zc)
        internal_error("incremental zero count %d differs from recomputation %d", g_zc, zc);
    g_rechecks++;
}

static _Noreturn void traverse(void)
{
    enum { RUNNING, FIRST_FOUND, INTERRUPTED } state = RUNNING;
    const int r = g_r;
    const int F = r >= 1 ? r - 1 : 0;
    poll_build("gray_start");
    g_expected = (uint64_t)1 << F;
    out("sign_fix=%s", r >= 1 ? "y0=1 (x -> -x symmetry; totals are doubled)" : "none (ineq_rank 0)");
    out("expected_assignments=%llu", (unsigned long long)g_expected);
    for (int k = 0; k < r; k++)
        g_y[k] = 1;
    g_zc = 0;
    for (int e = 0; e < g_E; e++) {
        int s = 0;
        for (int k = 0; k < r; k++)
            s += g_lam[e][k];
        g_v[e] = (uint8_t)(s % 3);
        g_zc += (g_v[e] == 0);
    }
    g_visited = 1;
    if (g_zc == 0) {
        on_solution();
        if (!g_count_mode)
            state = FIRST_FOUND;
    }
    if (state == RUNNING)
        for (uint64_t s = 1; s < g_expected; s++) {
            const int k = 1 + __builtin_ctzll(s);
            const int delta = g_y[k] == 1 ? 1 : 2; /* 1 -> 2 adds 1, 2 -> 1 adds 2 */
            g_y[k] = (uint8_t)(3 - g_y[k]);
            for (uint32_t q = g_off[k]; q < g_off[k + 1]; q++) {
                const int e = g_le[q];
                const int old = g_v[e];
                const int nw = (old + g_lc[q] * delta) % 3;
                g_zc += (nw == 0) - (old == 0);
                g_v[e] = (uint8_t)nw;
            }
            g_visited++;
            if (g_zc == 0) {
                on_solution();
                if (!g_count_mode) {
                    state = FIRST_FOUND;
                    break;
                }
            }
            if ((s & POLL_MASK) == 0) {
                recompute_check();
                if (stop_requested()) {
                    state = INTERRUPTED;
                    break;
                }
            }
        }
    recompute_check();
    const int complete = state == RUNNING;
    if (complete) {
        const uint64_t last = g_expected - 1, word = last ^ (last >> 1);
        if (g_visited != g_expected)
            internal_error("visited %llu assignments, expected %llu",
                           (unsigned long long)g_visited, (unsigned long long)g_expected);
        if (r >= 1 && g_y[0] != 1)
            internal_error("fixed coordinate y0 changed");
        for (int b = 0; b < F; b++)
            if (g_y[1 + b] != (uint8_t)(1 + ((word >> b) & 1)))
                internal_error("final assignment differs from Gray word %llu", (unsigned long long)word);
    }
    out("visited_assignments=%llu", (unsigned long long)g_visited);
    out("gray_rechecks=%llu", (unsigned long long)g_rechecks);
    out("solutions_y0_fixed_found=%llu", (unsigned long long)g_found);
    out("dm_checked_witnesses=%llu", (unsigned long long)g_dm_checked);
    out("traversal_complete=%s", complete ? "yes" : "no");
    if (complete) {
        const unsigned long long total = (unsigned long long)(r >= 1 ? 2 * g_found : g_found);
        out("solutions_y_total=%llu", total);
        out("gauged_lifts=%llu*3^%d", total, g_d - r);
        out("all_lifts_of_beta=%llu*3^%d", total, g_d - r + g_N + g_K - 1);
    }
    out("witness_written=%s", g_dm_written ? "yes" : "no");
    out("stop_reason=%s", state == RUNNING ? "complete" : state == FIRST_FOUND ? "first_found" : g_stop_reason);
    if (g_found > 0)
        finish("FOUND", RC_FOUND);
    if (complete)
        finish("ZERO_FOR_THIS_BETA", RC_ZERO);
    finish("UNKNOWN", RC_UNKNOWN);
}

int main(int argc, char **argv)
{
    if (clock_gettime(CLOCK_MONOTONIC, &g_t0) != 0) {
        fprintf(stderr, "%s: clock_gettime(CLOCK_MONOTONIC) failed\n", TOOL);
        return RC_INTERNAL;
    }
    out("tool=%s", TOOL);
    install_signals();
    parse_cli(argc, argv);
    preflight_output();
    parse_beta(read_beta_file());
    validate_beta();
    build_crt();
    build_rows();
    out("variables=%d", g_V);
    out("equalities=%d", g_E);
    eq_eliminate();
    check_equalities();
    build_basis();
    out("eq_rank=%d", g_eqrank);
    out("null_dim=%d", g_d);
    out("check_equalities=pass (RREF structure, R = P*A on pivot rows, A*basis = 0)");
    compute_G();
    ineq_basis();
    check_lambda();
    out("inequalities=%d", g_E);
    out("ineq_rank=%d", g_r);
    out("kernel_dim=%d", g_d - g_r);
    out("zero_forms_on_L=%d", g_zero_forms);
    out("check_inequalities=pass (every form = sum_k lambda[e][k] * selected form k on L)");
    if (g_r > g_cap) {
        out("rank_cap_status=exceeded (ineq_rank %d > rank_cap %d)", g_r, g_cap);
        out("stop_reason=rank_above_cap");
        finish("UNKNOWN", RC_UNKNOWN);
    }
    out("rank_cap_status=ok");
    print_y_forms();
    build_section();
    check_section();
    out("check_section=pass (A*M = 0, selected forms of M u_k = u_k)");
    build_lists();
    out("gray_list_entries=%u", (unsigned)g_off[g_r]);
    traverse();
}
