/* xr1.c -- exact search for cyclic (p,k,1) difference families over Z_p (p prime), complete for each
 * prescribed first class set R1.
 *
 * Classes. n = (p-1)/2, cls(d) = log_g(d) mod n (g least primitive root). d and -d share a class, and
 * multiplying by g rotates classes by +1. A block's class set is the set of classes of its k(k-1)/2
 * unordered differences; B and -B share it. A difference family (DF) is the same as a partition of
 * Z_n into t realizable class sets (each set with distinct classes), plus a block for each set.
 * Scaling a DF by g^r rotates its partition by r. So every DF is equivalent to one containing a block
 * whose class set R1 is in canonical rotation: the lexicographically least sorted tuple among the
 * rotations S - c, c in S. In particular R1 contains 0 = cls(1), so a realising block contains {0,1}.
 *
 * For a fixed canonical R1, the search is COMPLETE. It enumerates every realizable class set S in
 * Q = Z_n \ R1 that passes the necessary spectral conditions below (bitset DFS over blocks
 * {0, g^c, ...}, where c = min S). It then finds every exact cover of Q by t-1 such sets (branching on
 * the lowest uncovered class), keeping only covers that pass the spectral conditions at every level.
 *   Spectral condition (necessary). For a DF, sum_i |B_i^(s)|^2 = t*k - 1 for every s != 0, with
 *   |B^(s)|^2 = k + F_S(s) and F_S(s) = sum_{c in S} 2cos(2 pi s g^c / p). Every term is >= 0, so
 *   every subfamily has sum <= t*k - 1 (tolerance 1e-3).
 * One line per R1: "R1 idx=... blk=... mask=... nsets=... l2/l3/l4=... sols=... enum_s=... search_s=...".
 * Solutions: "SOL b..b | b..b | ..." (t blocks; the first realises R1). Re-verification is external.
 *
 * Modes:
 *   xr1 P K START COUNT [maxsec]   R1 = canonical class sets in the order of a DFS over blocks
 *       {0,1,x3<...<xk} (x increasing). A leaf is kept if its classes are distinct, the class set is
 *       canonical, the block is the lexicographically smaller one of the mirror pair {B, 1-B}, and
 *       the single-block spectral bound holds. The index counts kept leaves from 0.
 *   xr1 P K block x1,...,xk         R1 = canonical rotation of the class set of the given block
 *       (planted-solution test).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>
#include <time.h>

typedef unsigned __int128 u128;
#define MAXP 1024
#define MAXK 10
#define MAXN 128
#define MAXW 17

static int p, k, t, n, g, m, W;
static int LOG[MAXP], PW[MAXP], CLS[MAXP];
static float FC[MAXN][MAXN];          /* FC[c][s'] = 2cos(2 pi (s'+1) g^c / p), s' = 0..n-1 */
static double LIM;
static u128 FULL;
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + ts.tv_nsec * 1e-9; }
static inline u128 bit(int c) { return (u128)1 << c; }
static inline int lowbit(u128 x) { uint64_t lo = (uint64_t)x; return lo ? __builtin_ctzll(lo) : 64 + __builtin_ctzll((uint64_t)(x >> 64)); }
static inline int dif(int a, int b) { int d = a - b; return d < 0 ? d + p : d; }

static int prim_root(int q) {
    int fs[32], nf = 0, x = q - 1;
    for (int d = 2; d * d <= x; d++) if (x % d == 0) { fs[nf++] = d; while (x % d == 0) x /= d; }
    if (x > 1) fs[nf++] = x;
    for (int h = 2; h < q; h++) {
        int ok = 1;
        for (int i = 0; i < nf && ok; i++) { long long r = 1, b = h; int e = (q - 1) / fs[i]; while (e) { if (e & 1) r = r * b % q; b = b * b % q; e >>= 1; } if (r == 1) ok = 0; }
        if (ok) return h;
    }
    return -1;
}

static int tuple_of(u128 S, int *out) { int c = 0; while (S) { int b = lowbit(S); out[c++] = b; S &= S - 1; } return c; }
/* e sorted, e[0] == 0: canonical iff no rotation S - e[i] is lexicographically smaller */
static int is_canonical(const int *e) {
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < m; j++) {
            int a = e[(i + j) % m] - e[i]; if (a < 0) a += n;
            if (a < e[j]) return 0;
            if (a > e[j]) break;
        }
    }
    return 1;
}
static void spectrum(u128 S, float *out) {
    int e[MAXN]; int ne = tuple_of(S, e);
    for (int s = 0; s < n; s++) out[s] = 0;
    for (int i = 0; i < ne; i++) { const float *f = FC[e[i]]; for (int s = 0; s < n; s++) out[s] += f[s]; }
}

/* ---------------- set store for one R1 ---------------- */
static int nsets, capsets;
static u128 *SM; static float *SPC; static short *SBK;
static int list_start[MAXN + 1];
static uint64_t *SL = NULL; static size_t capsl = 0; static int NWS = 0;
static int *HT; static size_t hmask;
static inline uint64_t hmix(u128 x) { uint64_t a = (uint64_t)x, b = (uint64_t)(x >> 64); uint64_t h = a * 0x9E3779B97F4A7C15ULL ^ (b + 0x632BE59BD9B4E019ULL) * 0xC2B2AE3D27D4EB4FULL; h ^= h >> 31; return h; }
static int hfind(u128 x) { size_t h = hmix(x) & hmask; while (HT[h] != -1) { if (HT[h] >= 0 && SM[HT[h]] == x) return HT[h]; h = (h + 1) & hmask; } return -1; }
/* rejected masks are remembered as -(2 + slot in REJ) so that their mirror leaf is not re-tested */
static u128 *REJ; static int nrej, caprej;
static int hfind_any(u128 x, int *rejected) {
    size_t h = hmix(x) & hmask;
    while (HT[h] != -1) {
        int v = HT[h];
        if (v >= 0) { if (SM[v] == x) { *rejected = 0; return v; } }
        else if (REJ[-v - 2] == x) { *rejected = 1; return v; }
        h = (h + 1) & hmask;
    }
    return -1;
}
static void hput(u128 x, int val) { size_t h = hmix(x) & hmask; while (HT[h] != -1) h = (h + 1) & hmask; HT[h] = val; }

static u128 Q; static float FR1[MAXN];
static int TOPS[8];                       /* frequencies with the largest FR1, checked first */
static int Bel[MAXK]; static int cmin_cur;
static long long enum_leaves = 0, enum_nodes = 0;
static void add_set(u128 S) {
    int rj;
    if (hfind_any(S, &rj) != -1) return;   /* seen: mirror/homometric duplicate or already rejected */
    if ((size_t)(nsets + nrej) * 2 >= hmask) { fprintf(stderr, "hash full\n"); exit(4); }
    /* quick precheck at the tightest frequencies of R1 */
    int e[MAXN]; int ne = tuple_of(S, e);
    for (int q = 0; q < 8; q++) {
        int s = TOPS[q]; float a = 0; for (int i = 0; i < ne; i++) a += FC[e[i]][s];
        if (2 * k + FR1[s] + a > LIM || k + a > LIM) goto reject;
    }
    {
        float spc[MAXN];
        for (int s = 0; s < n; s++) spc[s] = 0;
        for (int i = 0; i < ne; i++) { const float *f = FC[e[i]]; for (int s = 0; s < n; s++) spc[s] += f[s]; }
        for (int s = 0; s < n; s++) if (k + spc[s] > LIM || 2 * k + FR1[s] + spc[s] > LIM) goto reject;
        if (nsets >= capsets) {
            capsets *= 2; SM = realloc(SM, sizeof(u128) * capsets); SPC = realloc(SPC, sizeof(float) * (size_t)capsets * n); SBK = realloc(SBK, sizeof(short) * (size_t)capsets * k);
            if (!SM || !SPC || !SBK) { fprintf(stderr, "oom\n"); exit(4); }
        }
        SM[nsets] = S; memcpy(SPC + (size_t)nsets * n, spc, sizeof(float) * n);
        for (int a = 0; a < k; a++) SBK[(size_t)nsets * k + a] = (short)Bel[a];
        hput(S, nsets); nsets++;
        return;
    }
reject:
    if (nrej >= caprej) { caprej *= 2; REJ = realloc(REJ, sizeof(u128) * caprej); if (!REJ) { fprintf(stderr, "oom\n"); exit(4); } }
    REJ[nrej] = S; hput(S, -2 - nrej); nrej++;
}

/* bitset DFS: DD = doubled bitset of differences d (as elements of Z_p) whose class is available */
static uint64_t DDs[MAXK + 1][2 * MAXW + 2];
/* leaf_mode 0: enumeration (add_set); 1: L4 step of the exact cover (l4_leaf) */
static int leaf_mode = 0;
static void l4_leaf(u128 S);
static long long l4_nodes = 0;
static inline void dd_clear(uint64_t *DD, int x) { DD[x >> 6] &= ~(1ULL << (x & 63)); int y = x + p; DD[y >> 6] &= ~(1ULL << (y & 63)); }
static inline void window(const uint64_t *DD, int o, uint64_t *out) {
    int wo = o >> 6, bo = o & 63;
    for (int w = 0; w < W; w++) {
        uint64_t lo = DD[wo + w] >> bo;
        uint64_t hi = bo ? (DD[wo + w + 1] << (64 - bo)) : 0;
        out[w] = lo | hi;
    }
    if (p & 63) out[W - 1] &= (1ULL << (p & 63)) - 1;
}
static inline void bclr(uint64_t *b, int x) { b[x >> 6] &= ~(1ULL << (x & 63)); }
static void dfs_bs(int depth, const uint64_t *cand, u128 used) {
    if (leaf_mode) l4_nodes++; else enum_nodes++;
    for (int w = 0; w < W; w++) {
        uint64_t word = cand[w];
        while (word) {
            int y = (w << 6) + __builtin_ctzll(word); word &= word - 1;
            u128 N = 0; int ok = 1, nc[MAXK];
            for (int i = 0; i < depth; i++) { int c = CLS[dif(y, Bel[i])]; u128 b = bit(c); if (N & b) { ok = 0; break; } N |= b; nc[i] = c; }
            if (!ok) continue;
            Bel[depth] = y;
            if (depth + 1 == k) { if (leaf_mode) l4_leaf(used | N); else { enum_leaves++; add_set(used | N); } continue; }
            uint64_t *DDn = DDs[depth + 1];
            memcpy(DDn, DDs[depth], sizeof(uint64_t) * (2 * W + 2));
            for (int i = 0; i < depth; i++) { int d = PW[nc[i]]; dd_clear(DDn, d); dd_clear(DDn, p - d); }
            uint64_t ncand[MAXW];
            window(DDn, p - y, ncand);
            for (int q = 0; q < W; q++) ncand[q] &= cand[q];
            /* x > y */
            for (int q = 0; q < W; q++) { int lo = q << 6; if (lo + 63 <= y) ncand[q] = 0; else if (lo <= y) ncand[q] &= ~((y - lo == 63) ? ~0ULL : ((2ULL << (y - lo)) - 1)); }
            for (int i = 0; i < depth; i++) for (int j = 0; j < depth; j++) {
                int d = PW[nc[j]]; bclr(ncand, (Bel[i] + d) % p); bclr(ncand, (Bel[i] - d + p) % p);
            }
            dfs_bs(depth + 1, ncand, used | N);
        }
    }
}
static void dfs_from_min(int c, u128 allowed) {
    /* B = {0, g^c}; available classes: in `allowed`, > c */
    u128 avail = allowed & ~((bit(c) << 1) - 1);
    uint64_t *DD = DDs[2];
    memset(DD, 0, sizeof(uint64_t) * (2 * W + 2));
    for (int d = 1; d < p; d++) if (avail & bit(CLS[d])) { DD[d >> 6] |= 1ULL << (d & 63); int y = d + p; DD[y >> 6] |= 1ULL << (y & 63); }
    uint64_t c0[MAXW], c1[MAXW];
    window(DD, p, c0);              /* x - 0 available */
    window(DD, p - PW[c], c1);      /* x - g^c available */
    for (int q = 0; q < W; q++) c0[q] &= c1[q];
    Bel[0] = 0; Bel[1] = PW[c]; cmin_cur = c;
    dfs_bs(2, c0, bit(c));
}
static void enum_sets_for_min(int c) { leaf_mode = 0; dfs_from_min(c, Q); }

/* ---------------- exact cover of Q ---------------- */
static long long cnt_l[8], nsol_r1;
static int chosen[16]; static int R1blk[MAXK];
static long long total_sols = 0;
static void report_solution(int nch) {
    nsol_r1++; total_sols++;
    printf("SOL ");
    for (int a = 0; a < k; a++) printf(a ? " %d" : "%d", R1blk[a]);
    for (int j = 0; j < nch; j++) { printf(" |"); for (int a = 0; a < k; a++) printf(" %d", SBK[(size_t)chosen[j] * k + a]); }
    printf("\n"); fflush(stdout);
}
static void rec(int j, u128 C, const float *A);
/* L4 context: the DFS enumerates every realizable class set S with min(S) = c inside the remainder;
 * S is kept iff it is an accepted (stored) set; duplicates (mirror/homometric) are removed. */
static u128 L4_C; static const float *L4_A; static int L4_j;
static u128 L4_seen[4096]; static int L4_nseen; static long long L4_overflow = 0;
static void l4_leaf(u128 S) {
    for (int q = 0; q < L4_nseen; q++) if (L4_seen[q] == S) return;
    if (L4_nseen < 4096) L4_seen[L4_nseen++] = S; else L4_overflow++;
    int idx = hfind(S);
    if (idx < 0) return;
    const float *f = SPC + (size_t)idx * n;
    float B[MAXN];
    for (int s = 0; s < n; s++) { float v = L4_A[s] + f[s]; if ((L4_j + 1) * k + v > LIM) return; B[s] = v; }
    cnt_l[L4_j + 1]++;
    chosen[L4_j - 1] = idx;
    rec(L4_j + 1, L4_C | S, B);
}
static void rec(int j, u128 C, const float *A) { /* j = number of blocks chosen including R1 */
    u128 rem = Q & ~C;
    if (j == t - 1) {
        int idx = hfind(rem);
        if (idx >= 0) {
            const float *f = SPC + (size_t)idx * n;
            for (int s = 0; s < n; s++) { double v = t * k + A[s] + f[s], tv = t * k - 1; if (v > tv + 1e-2 || v < tv - 1e-2) { fprintf(stderr, "warning: exact cover with spectral mismatch\n"); break; } }
            chosen[j - 1] = idx; report_solution(j);
        }
        return;
    }
    int c = lowbit(rem);
    if (j == t - 2 && j >= 2) {
        L4_C = C; L4_A = A; L4_j = j; L4_nseen = 0;
        leaf_mode = 1; dfs_from_min(c, rem); leaf_mode = 0;
        return;
    }
    float B[MAXN];
    int a = list_start[c], b = list_start[c + 1];
    if (a >= b) return;
    int cl[MAXN], ncl = tuple_of(C, cl);
    for (int w = a >> 6; w <= (b - 1) >> 6; w++) {
        uint64_t word = ~0ULL;
        for (int q = 0; q < ncl; q++) word &= ~SL[(size_t)cl[q] * NWS + w];   /* sets avoiding C */
        int lo = w << 6;
        if (lo < a) word &= ~0ULL << (a - lo);
        if (lo + 64 > b) word &= (b - lo >= 64) ? ~0ULL : ((1ULL << (b - lo)) - 1);
        while (word) {
            int i = lo + __builtin_ctzll(word); word &= word - 1;
            u128 S = SM[i];
            if (S & C) { fprintf(stderr, "internal: slice mismatch\n"); exit(5); }
            const float *f = SPC + (size_t)i * n;
            int ok = 1;
            for (int s = 0; s < n; s++) { float v = A[s] + f[s]; if ((j + 1) * k + v > LIM) { ok = 0; break; } B[s] = v; }
            if (!ok) continue;
            cnt_l[j + 1]++;
            chosen[j - 1] = i;
            rec(j + 1, C | S, B);
        }
    }
}

static void process_R1(long long idx, const int *blk, u128 R1) {
    double t0 = now();
    Q = FULL & ~R1;
    spectrum(R1, FR1);
    /* top-8 frequencies of FR1 */
    for (int q = 0; q < 8; q++) {
        int best = -1;
        for (int s = 0; s < n; s++) {
            int used_ = 0; for (int r = 0; r < q; r++) if (TOPS[r] == s) used_ = 1;
            if (!used_ && (best < 0 || FR1[s] > FR1[best])) best = s;
        }
        TOPS[q] = best;
    }
    memcpy(R1blk, blk, sizeof(int) * k);
    nsets = 0; nrej = 0; enum_leaves = 0; enum_nodes = 0; l4_nodes = 0; L4_overflow = 0;
    for (size_t h = 0; h <= hmask; h++) HT[h] = -1;
    for (int c = 0; c < n; c++) {
        list_start[c] = nsets;
        if (!(Q & bit(c))) continue;
        enum_sets_for_min(c);
    }
    list_start[n] = nsets;
    /* bit slices: SL[x][i] = 1 iff set i contains class x */
    NWS = (nsets + 63) / 64 + 1;
    if ((size_t)n * NWS > capsl) { capsl = (size_t)n * NWS * 2; SL = realloc(SL, sizeof(uint64_t) * capsl); if (!SL) { fprintf(stderr, "oom\n"); exit(4); } }
    memset(SL, 0, sizeof(uint64_t) * (size_t)n * NWS);
    for (int i = 0; i < nsets; i++) { u128 S = SM[i]; while (S) { int x = lowbit(S); S &= S - 1; SL[(size_t)x * NWS + (i >> 6)] |= 1ULL << (i & 63); } }
    double t1 = now();
    memset(cnt_l, 0, sizeof cnt_l); nsol_r1 = 0;
    rec(1, 0, FR1);
    double t2 = now();
    printf("R1 idx=%lld blk=", idx); for (int a = 0; a < k; a++) printf(a ? ",%d" : "%d", blk[a]);
    double pk = -1e9; for (int s = 0; s < n; s++) if (k + FR1[s] > pk) pk = k + FR1[s];
    printf(" mask=%016llx%016llx peak=%.3f nsets=%d rejected=%d leaves=%lld nodes=%lld l2=%lld l3=%lld l4=%lld l4dfs=%lld l4ovf=%lld sols=%lld enum_s=%.2f search_s=%.2f\n",
           (unsigned long long)(R1 >> 64), (unsigned long long)R1, pk, nsets, nrej, enum_leaves, enum_nodes, cnt_l[2], cnt_l[3], cnt_l[4], l4_nodes, L4_overflow, nsol_r1, t1 - t0, t2 - t1);
    fflush(stdout);
}

/* ---------------- R1 enumeration ---------------- */
static long long r1_index = 0, r1_start, r1_count, r1_done = 0;
static double tstart, maxsec;
static int stop_flag = 0;
static int RB[MAXK];
static double PEAKMAX = 1e9;
static int count_mode = 0; static long long peak_hist[256];
/* R1 admissibility uses the true bound t*k-1 (independent of XR1_NOSPEC), so the R1 order is fixed */
static double single_peak(u128 S) {
    float f[MAXN]; spectrum(S, f);
    double mx = -1e9; for (int s = 0; s < n; s++) if (k + f[s] > mx) mx = k + f[s];
    return mx;
}
static int single_ok(u128 S) { return single_peak(S) <= t * k - 1 + 1e-3; }
static void dfs_r1(int depth, int start, u128 used) {
    if (stop_flag) return;
    if (depth == k) {
        int e[MAXN]; tuple_of(used, e);
        if (!is_canonical(e)) return;
        int mir[MAXK]; for (int a = 0; a < k; a++) mir[a] = (1 - RB[a] + p) % p;
        for (int a = 1; a < k; a++) { int x = mir[a], b = a - 1; while (b >= 0 && mir[b] > x) { mir[b + 1] = mir[b]; b--; } mir[b + 1] = x; }
        int cmp = 0; for (int a = 0; a < k && !cmp; a++) cmp = (RB[a] > mir[a]) - (RB[a] < mir[a]);
        if (cmp > 0) return;
        double pk = single_peak(used);
        if (pk > t * k - 1 + 1e-3) return;
        long long my = r1_index++;
        if (count_mode) { int bin = (int)(pk * 2); if (bin < 0) bin = 0; if (bin > 255) bin = 255; peak_hist[bin]++; return; }
        if (my < r1_start) return;
        if (my >= r1_start + r1_count || (maxsec > 0 && now() - tstart > maxsec)) { stop_flag = 1; return; }
        if (pk > PEAKMAX) { printf("SKIP idx=%lld peak=%.3f\n", my, pk); fflush(stdout); r1_done++; return; }
        process_R1(my, RB, used); r1_done++;
        return;
    }
    for (int x = start; x < p && !stop_flag; x++) {
        u128 add = 0; int ok = 1;
        for (int i = 0; i < depth; i++) {
            u128 b = bit(CLS[dif(x, RB[i])]);
            if ((used | add) & b) { ok = 0; break; }
            add |= b;
        }
        if (ok) { RB[depth] = x; dfs_r1(depth + 1, x + 1, used | add); }
    }
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: xr1 P K START COUNT [maxsec] | xr1 P K block x1,...,xk\n"); return 2; }
    p = atoi(argv[1]); k = atoi(argv[2]);
    if ((p - 1) % (k * (k - 1))) { fprintf(stderr, "bad p,k\n"); return 2; }
    t = (p - 1) / (k * (k - 1)); n = (p - 1) / 2; m = k * (k - 1) / 2; W = (p + 63) / 64;
    if (n > MAXN || p >= MAXP || k > MAXK || W > MAXW) { fprintf(stderr, "too big\n"); return 2; }
    g = prim_root(p);
    long long x = 1; for (int e = 0; e < p - 1; e++) { PW[e] = (int)x; LOG[x] = e; x = x * g % p; }
    for (int d = 1; d < p; d++) CLS[d] = LOG[d] % n;
    for (int c = 0; c < n; c++) for (int s = 0; s < n; s++) FC[c][s] = (float)(2.0 * cos(2.0 * M_PI * (double)(((long long)(s + 1) * PW[c]) % p) / p));
    LIM = t * k - 1 + 1e-3;
    if (getenv("XR1_NOSPEC")) LIM = 1e9;   /* control: disables every spectral filter */
    FULL = (n == 128) ? ~(u128)0 : (bit(n) - 1);
    capsets = 1 << 16; SM = malloc(sizeof(u128) * capsets); SPC = malloc(sizeof(float) * (size_t)capsets * n); SBK = malloc(sizeof(short) * (size_t)capsets * k);
    caprej = 1 << 16; REJ = malloc(sizeof(u128) * caprej);
    size_t hcap = 1 << 26; hmask = hcap - 1; HT = malloc(sizeof(int) * hcap);
    tstart = now();
    if (!strcmp(argv[3], "count")) {
        count_mode = 1; r1_start = 0; r1_count = 1LL << 62;
        RB[0] = 0; RB[1] = 1;
        dfs_r1(2, 2, bit(CLS[1]));
        printf("count p=%d k=%d n_canonical_R1=%lld secs=%.1f\npeak_hist_half_units", p, k, r1_index, now() - tstart);
        for (int b = 0; b < 256; b++) if (peak_hist[b]) printf(" %d:%lld", b, peak_hist[b]);
        printf("\n");
        return 0;
    }
    if (!strcmp(argv[3], "block")) {
        int B[MAXK], nb = 0; char *s = argv[4];
        while (*s && nb < k) { B[nb++] = ((atoi(s) % p) + p) % p; while (*s && *s != ',') s++; if (*s) s++; }
        if (nb != k) { fprintf(stderr, "need k elements\n"); return 2; }
        u128 S = 0; for (int a = 0; a < k; a++) for (int b = a + 1; b < k; b++) S |= bit(CLS[dif(B[b], B[a])]);
        int e[MAXN]; if (tuple_of(S, e) != m) { fprintf(stderr, "repeated classes\n"); return 2; }
        int best_r = -1; int bt[MAXN];
        for (int i = 0; i < m; i++) {
            int r = e[i], tt[MAXN];
            for (int j = 0; j < m; j++) { int a = e[(i + j) % m] - r; if (a < 0) a += n; tt[j] = a; }
            int better = best_r < 0; for (int j = 0; j < m && !better; j++) { if (tt[j] < bt[j]) better = 1; else if (tt[j] > bt[j]) break; }
            if (better) { best_r = r; memcpy(bt, tt, sizeof(int) * m); }
        }
        /* B' = g^{-r} B has class set S - r (canonical); move its class-0 pair to {0,1} */
        int ginv = PW[(p - 1 - best_r) % (p - 1)], Bp[MAXK];
        for (int a = 0; a < k; a++) Bp[a] = (int)((long long)B[a] * ginv % p);
        int a0 = -1, b0 = -1;
        for (int a = 0; a < k; a++) for (int b = 0; b < k; b++) if (a != b && dif(Bp[b], Bp[a]) == 1) { a0 = a; b0 = b; }
        if (a0 < 0) { fprintf(stderr, "internal: no class-0 pair\n"); return 3; }
        int base = Bp[a0], Bn[MAXK];
        for (int a = 0; a < k; a++) Bn[a] = dif(Bp[a], base);
        for (int a = 1; a < k; a++) { int v = Bn[a], b = a - 1; while (b >= 0 && Bn[b] > v) { Bn[b + 1] = Bn[b]; b--; } Bn[b + 1] = v; }
        u128 S2 = 0; for (int a = 0; a < k; a++) for (int b = a + 1; b < k; b++) S2 |= bit(CLS[dif(Bn[b], Bn[a])]);
        (void)b0;
        printf("start p=%d k=%d t=%d n=%d g=%d mode=block single_ok=%d\n", p, k, t, n, g, single_ok(S2));
        process_R1(-1, Bn, S2);
        printf("end total_sols=%lld secs=%.1f\n", total_sols, now() - tstart);
        return 0;
    }
    r1_start = atoll(argv[3]); r1_count = atoll(argv[4]); maxsec = argc > 5 ? atof(argv[5]) : 0;
    if (argc > 6) PEAKMAX = atof(argv[6]);
    printf("start p=%d k=%d t=%d n=%d g=%d start=%lld count=%lld maxsec=%.0f peakmax=%.3f\n", p, k, t, n, g, r1_start, r1_count, maxsec, PEAKMAX);
    fflush(stdout);
    RB[0] = 0; RB[1] = 1;
    dfs_r1(2, 2, bit(CLS[1]));
    printf("end r1_index_reached=%lld r1_done=%lld total_sols=%lld secs=%.1f complete_range=%s\n", r1_index, r1_done, total_sols, now() - tstart,
           stop_flag && r1_done < r1_count ? "false" : "true");
    return 0;
}
