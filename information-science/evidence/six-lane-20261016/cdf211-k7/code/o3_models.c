/* o3_models.c -- exact searches for cyclic (p,k,1) difference families over F_p (p prime,
 * k = 1 mod 3) that are invariant under the order-3 multiplier group H3 = <w>, w^3 = 1.
 *
 * A multiplier model is NOT the target. An empty result is a restricted-model miss only.
 * Every reported family is re-verified by code/cdf_tools.py (independent direct verifier).
 *
 * Facts used (proved in README):
 *  - A block fixed by H3 up to translation can be translated to be fixed exactly ((w-1) is a unit),
 *    so it is {0} u a_1 H3 u ... u a_m H3 with m = (k-1)/3.
 *  - Differences live in H6-classes: cls(d) = log_g(d) mod n6, n6 = (p-1)/6, H6 = +-H3.
 *    Delta(F) of a fixed block is H6-invariant; F is admissible iff every class count is 0 or 6.
 *  - A non-fixed block B lies in an orbit {B, wB, w^2B} of 3 blocks; the orbit covers each
 *    difference once iff the k(k-1)/2 unordered differences of B lie in distinct H6-classes.
 *  - Orbit normalisation (each orbit counted exactly once): let c = min class of Delta(B). The
 *    unique pair of B in class c can be translated and multiplied by a power of w to {0, g^c}.
 *
 * Modes (p prime, p = 1 mod 6, k = 1 mod 3, t = (p-1)/(k(k-1))):
 *   allfixed p k [maxsol]        all t blocks fixed: exact cover of the n6 classes by t admissible
 *                                fixed blocks (dancing links, MRV column choice).
 *   m1 p k f [maxsol]            f fixed blocks + one orbit (requires t = f + 3): enumerate every
 *                                normalised B whose classes are distinct; exact-cover the remaining
 *                                classes by f fixed blocks.
 *   m2 p k [lo hi]               f = 2 (t = 5): for every unordered pair {F1,F2} of class-disjoint
 *                                fixed blocks with index lo <= i(F1) < hi, enumerate every
 *                                normalised B covering exactly the remaining classes.
 *   rawB p k                     count every B = {0 < x2 < ... < xk} whose unordered differences lie
 *                                in distinct H6-classes (cross-check: equals 3k * normalised count).
 * Output: "SOL" lines (one family, blocks separated by " | "), then one "SUMMARY {json}" line.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

typedef unsigned __int128 u128;
#define MAXP 4096
#define MAXK 16
#define MAXCAND 400000

static int p, k, g, n3, n6, t, mcos, fcls; /* fcls = classes per fixed block = k(k-1)/6 */
static int LOG[MAXP], PW[MAXP], CLS[MAXP], W;
static u128 FULL;

static int ncand;
static u128 cmask[MAXCAND];
static int cexp[MAXCAND][5];
static int *cby[128], ncby[128];

static long long nodes = 0, nsol = 0, maxsol = -1, nB = 0;
static long long nB_by_c[128];

static int prim_root(int q) {
    int fs[32], nf = 0, n = q - 1;
    for (int d = 2; d * d <= n; d++) if (n % d == 0) { fs[nf++] = d; while (n % d == 0) n /= d; }
    if (n > 1) fs[nf++] = n;
    for (int h = 2; h < q; h++) {
        int ok = 1;
        for (int i = 0; i < nf && ok; i++) {
            long long r = 1, b = h; int e = (q - 1) / fs[i];
            while (e) { if (e & 1) r = r * b % q; b = b * b % q; e >>= 1; }
            if (r == 1) ok = 0;
        }
        if (ok) return h;
    }
    return -1;
}
static int is_prime(int n) { if (n < 2) return 0; for (int d = 2; d * d <= n; d++) if (n % d == 0) return 0; return 1; }
static inline int lowbit(u128 x) { uint64_t lo = (uint64_t)x; return lo ? __builtin_ctzll(lo) : 64 + __builtin_ctzll((uint64_t)(x >> 64)); }
static inline int popc(u128 x) { return __builtin_popcountll((uint64_t)x) + __builtin_popcountll((uint64_t)(x >> 64)); }
static inline u128 bit(int c) { return (u128)1 << c; }

static void setup(void) {
    if (!is_prime(p) || (p - 1) % 6 || k % 3 != 1 || k > MAXK || p >= MAXP) { fprintf(stderr, "bad p/k\n"); exit(2); }
    g = prim_root(p); n3 = (p - 1) / 3; n6 = (p - 1) / 6; mcos = (k - 1) / 3; fcls = k * (k - 1) / 6;
    if (n6 > 128) { fprintf(stderr, "n6 > 128\n"); exit(2); }
    t = ((p - 1) % (k * (k - 1)) == 0) ? (p - 1) / (k * (k - 1)) : -1;
    long long x = 1;
    for (int e = 0; e < p - 1; e++) { PW[e] = (int)x; LOG[x] = e; x = x * g % p; }
    for (int d = 1; d < p; d++) CLS[d] = LOG[d] % n6;
    W = PW[n3];
    FULL = (n6 == 128) ? ~(u128)0 : (bit(n6) - 1);
}

/* fixed candidates {0} u g^{e1}H3 u ... u g^{em}H3, e1 < ... < em in [0,n3) */
static int fe[5];
static void build_cand_rec(int depth, int start) {
    if (depth == mcos) {
        int el[MAXK], ne = 0; el[ne++] = 0;
        for (int j = 0; j < mcos; j++) for (int i = 0; i < 3; i++) el[ne++] = (int)((long long)PW[fe[j]] * PW[i * n3] % p);
        int cnt[128] = {0};
        for (int a = 0; a < ne; a++) for (int b = 0; b < ne; b++) if (a != b) cnt[CLS[((el[a] - el[b]) % p + p) % p]]++;
        u128 M = 0; int nc = 0, ok = 1;
        for (int c = 0; c < n6; c++) { if (cnt[c] == 6) { M |= bit(c); nc++; } else if (cnt[c] != 0) ok = 0; }
        if (ok && nc == fcls) {
            if (ncand >= MAXCAND) { fprintf(stderr, "MAXCAND\n"); exit(2); }
            cmask[ncand] = M; for (int j = 0; j < mcos; j++) cexp[ncand][j] = fe[j]; ncand++;
        }
        return;
    }
    for (int e = start; e < n3; e++) { fe[depth] = e; build_cand_rec(depth + 1, e + 1); }
}
static void build_cands(void) {
    ncand = 0; build_cand_rec(0, 0);
    for (int c = 0; c < n6; c++) { ncby[c] = 0; cby[c] = malloc(sizeof(int) * (ncand + 1)); }
    for (int i = 0; i < ncand; i++) for (int c = 0; c < n6; c++) if (cmask[i] & bit(c)) cby[c][ncby[c]++] = i;
}

static void print_fixed(int i) {
    int el[MAXK], ne = 0; el[ne++] = 0;
    for (int j = 0; j < mcos; j++) for (int s = 0; s < 3; s++) el[ne++] = (int)((long long)PW[cexp[i][j]] * PW[s * n3] % p);
    for (int a = 0; a < ne; a++) printf("%s%d", a ? " " : "", el[a]);
}
static void print_orbit(const int *B) {
    for (int s = 0; s < 3; s++) {
        long long mu = PW[s * n3];
        printf(" | ");
        for (int a = 0; a < k; a++) printf("%s%lld", a ? " " : "", (long long)B[a] * mu % p);
    }
}

/* ---- exact cover of a small class set by f fixed candidates (lowest-class branching) ---- */
static int xstack[64];
static const int *curB = NULL;
static void report_m(int nfix) {
    nsol++;
    printf("SOL ");
    for (int j = 0; j < nfix; j++) { if (j) printf(" | "); print_fixed(xstack[j]); }
    if (curB) print_orbit(curB);
    printf("\n"); fflush(stdout);
}
static int stop_now(void) { return maxsol >= 0 && nsol >= maxsol; }
static void xc(u128 R, int depth, int fleft) {
    nodes++;
    if (R == 0) { if (fleft == 0) report_m(depth); return; }
    if (fleft == 0) return;
    int c = lowbit(R);
    for (int j = 0; j < ncby[c] && !stop_now(); j++) {
        int i = cby[c][j]; u128 M = cmask[i];
        if ((M & ~R) == 0) { xstack[depth] = i; xc(R & ~M, depth + 1, fleft - 1); }
    }
}

/* ---- dancing links for allfixed ---- */
typedef struct { int L, R, U, D, C, row; } Node;
static Node *N; static int *S, root, nnodes;
static void dlx_build(void) {
    int tot = n6 + 1 + ncand * fcls + 1;
    N = calloc(tot, sizeof(Node)); S = calloc(n6 + 1, sizeof(int));
    root = n6;
    for (int c = 0; c <= n6; c++) { N[c].L = (c + n6) % (n6 + 1); N[c].R = (c + 1) % (n6 + 1); N[c].U = N[c].D = c; N[c].C = c; N[c].row = -1; }
    nnodes = n6 + 1;
    for (int i = 0; i < ncand; i++) {
        int first = -1, prev = -1;
        for (int c = 0; c < n6; c++) if (cmask[i] & bit(c)) {
            int x = nnodes++;
            N[x].C = c; N[x].row = i;
            N[x].D = c; N[x].U = N[c].U; N[N[c].U].D = x; N[c].U = x; S[c]++;
            if (first < 0) { first = x; N[x].L = N[x].R = x; }
            else { N[x].L = prev; N[x].R = first; N[prev].R = x; N[first].L = x; }
            prev = x;
        }
    }
}
static void cover(int c) {
    N[N[c].R].L = N[c].L; N[N[c].L].R = N[c].R;
    for (int i = N[c].D; i != c; i = N[i].D)
        for (int j = N[i].R; j != i; j = N[j].R) { N[N[j].D].U = N[j].U; N[N[j].U].D = N[j].D; S[N[j].C]--; }
}
static void uncover(int c) {
    for (int i = N[c].U; i != c; i = N[i].U)
        for (int j = N[i].L; j != i; j = N[j].L) { S[N[j].C]++; N[N[j].D].U = j; N[N[j].U].D = j; }
    N[N[c].R].L = c; N[N[c].L].R = c;
}
static int dstack[128];
static void dlx(int depth) {
    nodes++;
    if (N[root].R == root) {
        nsol++;
        printf("SOL "); for (int j = 0; j < depth; j++) { if (j) printf(" | "); print_fixed(dstack[j]); } printf("\n"); fflush(stdout);
        return;
    }
    int c = -1, best = 1 << 30;
    for (int j = N[root].R; j != root; j = N[j].R) if (S[j] < best) { best = S[j]; c = j; }
    if (best == 0) return;
    cover(c);
    for (int r = N[c].D; r != c && !stop_now(); r = N[r].D) {
        dstack[depth] = N[r].row;
        for (int j = N[r].R; j != r; j = N[j].R) cover(N[j].C);
        dlx(depth + 1);
        for (int j = N[r].L; j != r; j = N[j].L) uncover(N[j].C);
    }
    uncover(c);
}

/* ---- B enumeration ---- */
static int Bel[MAXK];
static int mode_m1_f;          /* m1: number of fixed blocks */
static u128 allowedA;          /* m2: allowed classes */
static int cmin_cur, rc_cur;
static long long rawB = 0;

static void on_B_m1(void) {
    nB++; nB_by_c[cmin_cur]++;
    u128 used = 0;
    for (int a = 0; a < k; a++) for (int b = a + 1; b < k; b++) used |= bit(CLS[((Bel[b] - Bel[a]) % p + p) % p]);
    if (popc(used) != k * (k - 1) / 2) { fprintf(stderr, "internal: B classes not distinct\n"); exit(3); }
    curB = Bel; xc(FULL & ~used, 0, mode_m1_f); curB = NULL;
}
/* mode 1: classes must be > cmin; mode 2: classes must be in allowedA */
static int bmode;
static void dfsB(int depth, int start, u128 used) {
    nodes++;
    if (depth == k) {
        if (bmode == 1) on_B_m1();
        else { nB++; curB = Bel; report_m(2); curB = NULL; }
        return;
    }
    for (int x = start; x < p && !stop_now(); x++) {
        if (x == rc_cur) continue;
        u128 add = 0; int ok = 1;
        for (int i = 0; i < depth; i++) {
            int d = x - Bel[i]; if (d < 0) d += p;
            int c = CLS[d];
            if (bmode == 1) { if (c <= cmin_cur) { ok = 0; break; } }
            else if (!(allowedA & bit(c))) { ok = 0; break; }
            u128 b = bit(c);
            if ((used | add) & b) { ok = 0; break; }
            add |= b;
        }
        if (ok) { Bel[depth] = x; dfsB(depth + 1, x + 1, used | add); }
    }
}
static void dfs_raw(int depth, int start, u128 used) {
    nodes++;
    if (depth == k) { rawB++; return; }
    for (int x = start; x < p; x++) {
        u128 add = 0; int ok = 1;
        for (int i = 0; i < depth; i++) {
            int d = x - Bel[i]; if (d < 0) d += p;
            u128 b = bit(CLS[d]);
            if ((used | add) & b) { ok = 0; break; }
            add |= b;
        }
        if (ok) { Bel[depth] = x; dfs_raw(depth + 1, x + 1, used | add); }
    }
}

static void summary(const char *mode, double secs, const char *extra) {
    printf("SUMMARY {\"mode\":\"%s\",\"p\":%d,\"k\":%d,\"t\":%d,\"g\":%d,\"w\":%d,\"n6\":%d,\"n_fixed_candidates\":%d,"
           "\"n_solutions\":%lld,\"maxsol\":%lld,\"complete\":%s,\"nodes\":%lld,\"n_B\":%lld,\"seconds\":%.2f%s}\n",
           mode, p, k, t, g, W, n6, ncand, nsol, maxsol, (maxsol >= 0 && nsol >= maxsol) ? "false" : "true",
           nodes, nB, secs, extra ? extra : "");
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: see header\n"); return 2; }
    const char *mode = argv[1]; p = atoi(argv[2]); k = atoi(argv[3]);
    setup(); build_cands();
    clock_t t0 = clock();
    char extra[4096] = "";
    if (!strcmp(mode, "allfixed")) {
        if (argc > 4) maxsol = atoll(argv[4]);
        if (t < 1) { fprintf(stderr, "t\n"); return 2; }
        dlx_build(); dlx(0);
    } else if (!strcmp(mode, "m1")) {
        mode_m1_f = atoi(argv[4]); if (argc > 5) maxsol = atoll(argv[5]);
        if (t != mode_m1_f + 3) { fprintf(stderr, "need t = f + 3\n"); return 2; }
        bmode = 1;
        for (int c = 0; c < n6 && !stop_now(); c++) {
            cmin_cur = c; rc_cur = PW[c]; Bel[0] = 0; Bel[1] = rc_cur;
            dfsB(2, 1, bit(c));
        }
        int off = snprintf(extra, sizeof extra, ",\"f\":%d,\"n_B_by_c\":[", mode_m1_f);
        for (int c = 0; c < n6; c++) off += snprintf(extra + off, sizeof extra - off, "%s%lld", c ? "," : "", nB_by_c[c]);
        snprintf(extra + off, sizeof extra - off, "]");
    } else if (!strcmp(mode, "m2")) {
        if (t != 5) { fprintf(stderr, "m2 needs t = 5\n"); return 2; }
        int lo = argc > 4 ? atoi(argv[4]) : 0, hi = argc > 5 ? atoi(argv[5]) : ncand;
        long long npairs = 0;
        bmode = 2;
        for (int i = lo; i < hi && i < ncand; i++) for (int j = i + 1; j < ncand; j++) {
            if (cmask[i] & cmask[j]) continue;
            npairs++;
            allowedA = FULL & ~(cmask[i] | cmask[j]);
            cmin_cur = lowbit(allowedA); rc_cur = PW[cmin_cur];
            xstack[0] = i; xstack[1] = j;
            Bel[0] = 0; Bel[1] = rc_cur;
            dfsB(2, 1, bit(cmin_cur));
        }
        snprintf(extra, sizeof extra, ",\"lo\":%d,\"hi\":%d,\"n_disjoint_pairs\":%lld", lo, hi, npairs);
    } else if (!strcmp(mode, "rawB")) {
        Bel[0] = 0; dfs_raw(1, 1, 0);
        snprintf(extra, sizeof extra, ",\"raw_B\":%lld", rawB);
    } else { fprintf(stderr, "unknown mode\n"); return 2; }
    summary(mode, (double)(clock() - t0) / CLOCKS_PER_SEC, extra);
    return 0;
}
