/* dmorbit_xc_c21v2.c -- versioned copy of c21v1 plus an exact orbit-size reachability obstruction.
 * After generating all options, check whether the remaining column count is a nonnegative sum of available
 * orbit sizes. Options may repeat in this relaxed arithmetic test, so failure is a sound necessary-condition
 * obstruction (success proves nothing). No multiplier-specific or heuristic pruning is added.
 * Original c21v1 header follows.
 * dmorbit_xc_c21v1.c -- copy of cfr33/code/dmorbit_xc_v2.c (sha256 4fc84b0b...63cd) for the CFR(6,21) sub-lane cfr21
 * (worker InfoCFR27Lift).  Changes vs v2: (1) MAXG 128; (2) canonicity is tested image by image with early exit BEFORE the
 * orbit is materialised (same accepted set, faster for n^(k-1) = 21^6 codes); (3) memory guard: if the option store or the
 * per-item cover bitmaps would exceed MEMCAP bytes the run stops with "s UNKNOWN (memory cap)"; (4) usage name.
 * v2 header follows.
 * Group elements (mu, pi, t) act by (s c)_i = mu c_{pi^-1(i)} + t_i (t modulo the diagonal); model file from
 * code/dmorbit_compile_v2.py ("DMORBIT-MODEL v2": each G line is mu, pi^-1[k], t[k]).  Everything else as v1:
 * exact cover over WHOLE G-orbits of columns for G-invariant (Z_n, k; 1) difference matrices.
 * Input: the group and representative row pairs from a dmorbit_compile_v2 model (orbit-type counts in the model are
 * IGNORED: every orbit type is allowed, so one run covers every orbit-type distribution with the same zero setting).
 * Columns are normalised (entry 0 = 0); (g b)_x = mu_g b_{pi_g^-1(x)} renormalised.  Every normalised column b of
 * Z_n^(k-1) is enumerated; b is kept iff it is the lexicographic minimum of its orbit, is not the zero column, and on
 * every representative pair the differences over the DISTINCT columns of its orbit are pairwise distinct (and != 0 in
 * zero mode).  Items: (representative pair r, value z) (z != 0 in zero mode).  A G-invariant DM containing the zero
 * column (zero mode) / containing no G-fixed column (nozero mode) is exactly an exact cover of the items by orbits.
 * Search: root = item with fewest options (bitmaps), each option of it -> compatible options by bitmap AND-NOT, then a
 * list-based exact cover (item with fewest options first).  Every solution is rebuilt as the full k x n array and
 * verified on ALL row pairs (exit 5 on mismatch).
 * Usage: dmorbit_xc_c21v1 MODEL SECONDS zero|nozero|all first|count OUTPREFIX [SPLITK SPLITI]
 *   first: stop at the first solution, write OUTPREFIX.dmraw (exclusive), exit 10 + "s SATISFIABLE";
 *          exhausted without solution: exit 20 + "s EXHAUSTED-RESTRICTED"; deadline/SIGTERM: "s UNKNOWN".
 *   count: count all solutions ("sol" lines with the orbit representatives, max 100000), "s COUNT c COMPLETE|INCOMPLETE".
 *   SPLITK/SPLITI: only root options with index % SPLITK == SPLITI.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <signal.h>
#include <time.h>
#include <fcntl.h>
#include <unistd.h>

#define MAXN 63
#define MAXK 8
#define MAXG 128
#define MEMCAP 3000000000LL     /* bytes: option store + cover bitmaps */
#define MAXRP 32
#define MAXW 32                 /* item words */

static int n, k, ng, nrp;
static int gmu[MAXG], gpi[MAXG][MAXK], gt[MAXG][MAXK];
static int rpi[MAXRP], rpj[MAXRP];
static int zero_mode = 1, mode_first = 1, splitK = 1, splitI = 0;   /* zero_mode: 1 zero, 0 nozero, 2 all (no zero column forced, G-fixed columns allowed) */
static int nitems, nw;
static int item_of[MAXRP][MAXN];
static volatile sig_atomic_t stop_flag = 0;
static double t0, tlimit, last_prog;
static int timed_out = 0, stop_all = 0;
static long long nodes = 0, nsol = 0, root_done = 0, root_total = 0;
static const char *outprefix;

typedef struct { uint64_t m[MAXW]; } Mask;
static long long nopt = 0, optcap = 0;
static int32_t *opt_code;          /* base column code */
static uint8_t *opt_size;
static uint64_t *opt_mask;         /* nopt * nw */
static uint64_t **cover;           /* per item: bitmap over options */
static long long cw;               /* words per cover bitmap */

static double now_s(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + ts.tv_nsec * 1e-9; }
static void on_term(int s) { (void)s; stop_flag = 1; }
static inline int md(long x) { x %= n; return (int)(x < 0 ? x + n : x); }
static void decode(int32_t code, int *b) { b[0] = 0; for (int x = 1; x < k; x++) { b[x] = code % n; code /= n; } }

static int read_model(const char *path) {
    FILE *fp = fopen(path, "r");
    if (!fp) { perror("model"); return 0; }
    char tag[64];
    if (fscanf(fp, "%63s", tag) != 1 || strcmp(tag, "DMORBIT-MODEL")) return 0;
    if (fscanf(fp, "%63s", tag) != 1) return 0;
    if (fscanf(fp, "%d %d", &n, &k) != 2 || n > MAXN || k > MAXK) return 0;
    if (fscanf(fp, "%63s %d", tag, &ng) != 2 || strcmp(tag, "G") || ng > MAXG) return 0;
    for (int g = 0; g < ng; g++) { if (fscanf(fp, "%d", &gmu[g]) != 1) return 0; for (int x = 0; x < k; x++) if (fscanf(fp, "%d", &gpi[g][x]) != 1) return 0; for (int x = 0; x < k; x++) if (fscanf(fp, "%d", &gt[g][x]) != 1) return 0; }
    if (fscanf(fp, "%63s %d", tag, &nrp) != 2 || strcmp(tag, "REPPAIRS") || nrp > MAXRP) return 0;
    for (int r = 0; r < nrp; r++) if (fscanf(fp, "%d %d", &rpi[r], &rpj[r]) != 2) return 0;
    fclose(fp);
    return 1;
}
/* canonical = no group image of b is lexicographically smaller (early exit, no orbit materialisation) */
static int is_canonical(const int *b) {
    for (int g = 0; g < ng; g++) {
        int base = md((long)gmu[g] * b[gpi[g][0]] + gt[g][0]);
        for (int x = 0; x < k; x++) {
            int im = md((long)gmu[g] * b[gpi[g][x]] + gt[g][x] - base);
            if (im != b[x]) { if (im < b[x]) return 0; break; }
        }
    }
    return 1;
}
/* orbit of b: distinct normalised images; returns count, fills cols */
static int orbit_of(const int *b, int cols[MAXG][MAXK], int *canon) {
    int no = 0; *canon = 1;
    for (int g = 0; g < ng; g++) {
        int im[MAXK], base = md((long)gmu[g] * b[gpi[g][0]] + gt[g][0]);
        for (int x = 0; x < k; x++) im[x] = md((long)gmu[g] * b[gpi[g][x]] + gt[g][x] - base);
        for (int x = 0; x < k; x++) if (im[x] != b[x]) { if (im[x] < b[x]) *canon = 0; break; }
        int dup = 0;
        for (int q = 0; q < no && !dup; q++) if (!memcmp(cols[q], im, sizeof(int) * k)) dup = 1;
        if (!dup) { memcpy(cols[no], im, sizeof(int) * k); no++; }
    }
    return no;
}
static void build_options(void) {
    long long total = 1;
    for (int x = 1; x < k; x++) total *= n;
    optcap = 1 << 20;
    opt_code = malloc(sizeof(int32_t) * optcap); opt_size = malloc(optcap); opt_mask = malloc(sizeof(uint64_t) * optcap * nw);
    int b[MAXK], cols[MAXG][MAXK];
    long long sizehist[MAXG + 1]; memset(sizehist, 0, sizeof sizehist);
    for (long long code = (zero_mode == 1) ? 1 : 0; code < total; code++) {   /* v2: nozero/all also offer the orbit of the zero column (twisted groups move it) */
        decode((int32_t)code, b);
        if (!is_canonical(b)) continue;
        int canon, no = orbit_of(b, cols, &canon);
        if (!canon) { printf("c INTERNAL canonicity mismatch\n"); exit(5); }
        if (zero_mode == 0 && no == 1) continue;      /* nozero mode: no G-fixed columns at all */
        uint64_t mk[MAXW]; memset(mk, 0, sizeof mk);
        int ok = 1;
        for (int r = 0; r < nrp && ok; r++) {
            uint64_t seen = 0;
            for (int q = 0; q < no; q++) {
                int z = md(cols[q][rpi[r]] - cols[q][rpj[r]]);
                if ((zero_mode == 1 && z == 0) || (seen >> z & 1ULL)) { ok = 0; break; }
                seen |= 1ULL << z;
                int it = item_of[r][z];
                mk[it >> 6] |= 1ULL << (it & 63);
            }
        }
        if (!ok) continue;
        if (nopt >= optcap) {
            optcap *= 2;
            if ((long long)optcap * (5 + 8LL * nw) > MEMCAP) { printf("c option store would exceed MEMCAP at %lld options\n", nopt); printf("s UNKNOWN (memory cap)\n"); exit(0); }
            opt_code = realloc(opt_code, sizeof(int32_t) * optcap); opt_size = realloc(opt_size, optcap); opt_mask = realloc(opt_mask, sizeof(uint64_t) * optcap * nw);
        }
        opt_code[nopt] = (int32_t)code; opt_size[nopt] = (uint8_t)no;
        memcpy(opt_mask + nopt * nw, mk, sizeof(uint64_t) * nw);
        sizehist[no]++;
        nopt++;
    }
    printf("c options %lld (orbit sizes:", nopt);
    for (int s = 1; s <= MAXG; s++) if (sizehist[s]) printf(" %d:%lld", s, sizehist[s]);
    printf(")\n");
    cw = (nopt + 63) / 64;
    if ((long long)nitems * cw * 8 + nopt * (5 + 8LL * nw) > MEMCAP) { printf("c cover bitmaps would exceed MEMCAP (%lld items x %lld words)\n", (long long)nitems, cw); printf("s UNKNOWN (memory cap)\n"); exit(0); }
    cover = malloc(sizeof(uint64_t *) * nitems);
    for (int it = 0; it < nitems; it++) cover[it] = calloc((size_t)cw, sizeof(uint64_t));
    for (long long o = 0; o < nopt; o++) {
        const uint64_t *mk = opt_mask + o * nw;
        for (int w = 0; w < nw; w++) { uint64_t m = mk[w]; while (m) { int bt = __builtin_ctzll(m); m &= m - 1; cover[w * 64 + bt][o >> 6] |= 1ULL << (o & 63); } }
    }
}

static long long chosen[64]; static int nchosen = 0;
static void emit(void) {
    static int D[MAXK][MAXN];
    int nc = 0, b[MAXK], cols[MAXG][MAXK], canon;
    if (zero_mode == 1) { for (int x = 0; x < k; x++) D[x][nc] = 0; nc++; }
    for (int i = 0; i < nchosen; i++) {
        decode(opt_code[chosen[i]], b);
        int no = orbit_of(b, cols, &canon);
        for (int q = 0; q < no; q++) { if (nc >= MAXN) { printf("c INTERNAL too many columns\n"); exit(5); } for (int x = 0; x < k; x++) D[x][nc] = cols[q][x]; nc++; }
    }
    if (nc != n) { printf("c INTERNAL column count %d != %d\n", nc, n); exit(5); }
    for (int x = 0; x < k; x++) for (int y = x + 1; y < k; y++) {
        uint64_t seen = 0;
        for (int c = 0; c < n; c++) { int z = md(D[x][c] - D[y][c]); if (seen >> z & 1ULL) { printf("c INTERNAL MISMATCH rows %d %d\n", x, y); exit(5); } seen |= 1ULL << z; }
    }
    nsol++;
    if (!mode_first) {
        if (nsol <= 100000) {
            printf("sol");
            for (int i = 0; i < nchosen; i++) { decode(opt_code[chosen[i]], b); printf(" |"); for (int x = 1; x < k; x++) printf(" %d", b[x]); }
            printf("\n");
        }
        return;
    }
    char path[4096];
    snprintf(path, sizeof path, "%s.dmraw", outprefix);
    int fd = open(path, O_WRONLY | O_CREAT | O_EXCL, 0444);
    if (fd < 0) { perror("open dmraw"); exit(3); }
    FILE *o = fdopen(fd, "w");
    for (int x = 0; x < k; x++) { for (int c = 0; c < n; c++) fprintf(o, c ? " %d" : "%d", D[x][c]); fprintf(o, "\n"); }
    fclose(o);
    printf("c wrote %s\n", path);
    for (int i = 0; i < nchosen; i++) { decode(opt_code[chosen[i]], b); printf("v orbit size %d base", opt_size[chosen[i]]); for (int x = 0; x < k; x++) printf(" %d", b[x]); printf("\n"); }
    stop_all = 1;
}
static inline int disjoint(const uint64_t *a, const uint64_t *b) { for (int w = 0; w < nw; w++) if (a[w] & b[w]) return 0; return 1; }
static void check_time(void) {
    if (stop_flag || now_s() - t0 > tlimit) { timed_out = 1; stop_all = 1; }
    else if (now_s() - last_prog > 60) {
        last_prog = now_s();
        printf("c progress t %.0f nodes %lld sols %lld root %lld/%lld\n", now_s() - t0, nodes, nsol, root_done, root_total);
        fflush(stdout);
    }
}
/* list-based exact cover; covered: item mask; act: active option list */
static void xc_list(uint64_t *covered, const long long *act, long long na) {
    if (stop_all) return;
    if ((++nodes & 0xFFFF) == 0) check_time();
    if (stop_all) return;
    int full = 1;
    for (int it = 0; it < nitems; it++) if (!(covered[it >> 6] >> (it & 63) & 1ULL)) { full = 0; break; }
    if (full) { emit(); return; }
    /* counts per uncovered item */
    int cnt[MAXW * 64]; memset(cnt, 0, sizeof(int) * nitems);
    for (long long i = 0; i < na; i++) {
        const uint64_t *mk = opt_mask + act[i] * nw;
        for (int w = 0; w < nw; w++) { uint64_t m = mk[w]; while (m) { int bt = __builtin_ctzll(m); m &= m - 1; cnt[w * 64 + bt]++; } }
    }
    int best = -1, bc = 1 << 30;
    for (int it = 0; it < nitems; it++) {
        if (covered[it >> 6] >> (it & 63) & 1ULL) continue;
        if (cnt[it] < bc) { bc = cnt[it]; best = it; if (bc == 0) return; }
    }
    long long *nact = malloc(sizeof(long long) * (size_t)(na > 0 ? na : 1));
    for (long long i = 0; i < na && !stop_all; i++) {
        long long o = act[i];
        const uint64_t *mo = opt_mask + o * nw;
        if (!(mo[best >> 6] >> (best & 63) & 1ULL)) continue;
        long long nn = 0;
        for (long long j = 0; j < na; j++) { long long p = act[j]; if (p != o && disjoint(mo, opt_mask + p * nw)) nact[nn++] = p; }
        uint64_t nc[MAXW]; for (int w = 0; w < nw; w++) nc[w] = covered[w] | mo[w];
        chosen[nchosen++] = o;
        xc_list(nc, nact, nn);
        nchosen--;
    }
    free(nact);
}
static void xc_root(void) {
    uint64_t covered[MAXW]; memset(covered, 0, sizeof covered);
    /* root item: fewest options */
    int best = -1; long long bc = -1;
    for (int it = 0; it < nitems; it++) {
        long long c = 0;
        for (long long w = 0; w < cw; w++) c += __builtin_popcountll(cover[it][w]);
        if (bc < 0 || c < bc) { bc = c; best = it; }
    }
    printf("c root item %d (pair %d value %d) options %lld\n", best, best / n, best % n, bc);
    root_total = bc;
    if (bc == 0) return;
    uint64_t *act = malloc(sizeof(uint64_t) * (size_t)cw);
    long long *lst = malloc(sizeof(long long) * (size_t)(nopt > 0 ? nopt : 1));
    long long ridx = 0;
    for (long long w = 0; w < cw && !stop_all; w++) {
        uint64_t m = cover[best][w];
        while (m && !stop_all) {
            int bt = __builtin_ctzll(m); m &= m - 1;
            long long o = w * 64 + bt;
            long long myidx = ridx++;
            if (myidx % splitK != splitI) continue;
            const uint64_t *mo = opt_mask + o * nw;
            /* compatible options: AND-NOT over the items of o */
            for (long long q = 0; q < cw; q++) act[q] = ~0ULL;
            if (nopt % 64) act[cw - 1] = (1ULL << (nopt % 64)) - 1;
            for (int ww = 0; ww < nw; ww++) { uint64_t mm = mo[ww]; while (mm) { int b2 = __builtin_ctzll(mm); mm &= mm - 1; const uint64_t *cv = cover[ww * 64 + b2]; for (long long q = 0; q < cw; q++) act[q] &= ~cv[q]; } }
            long long na = 0;
            for (long long q = 0; q < cw; q++) { uint64_t a = act[q]; while (a) { int b3 = __builtin_ctzll(a); a &= a - 1; lst[na++] = q * 64 + b3; } }
            uint64_t nc[MAXW]; for (int ww = 0; ww < nw; ww++) nc[ww] = mo[ww];
            chosen[0] = o; nchosen = 1;
            xc_list(nc, lst, na);
            nchosen = 0;
            root_done++;
            check_time();
        }
    }
    free(act); free(lst);
}

static int orbit_size_reachable(void) {
    unsigned char available[MAXN + 1] = {0}, reachable[MAXN + 1] = {0};
    int remaining = n - (zero_mode == 1);
    for (long long o = 0; o < nopt; o++) {
        int size = opt_size[o];
        if (size <= remaining) available[size] = 1;
    }
    reachable[0] = 1;
    for (int count = 1; count <= remaining; count++)
        for (int size = 1; size <= count; size++)
            if (available[size] && reachable[count - size]) {
                reachable[count] = 1;
                break;
            }
    printf("c orbit-size relaxation remaining %d sizes", remaining);
    for (int size = 1; size <= remaining; size++) if (available[size]) printf(" %d", size);
    printf(" reachable %d\n", reachable[remaining]);
    return reachable[remaining];
}

int main(int argc, char **argv) {
    if (argc != 6 && argc != 8) { fprintf(stderr, "usage: dmorbit_xc_c21v2 MODEL SECONDS zero|nozero|all first|count OUTPREFIX [SPLITK SPLITI]\n"); return 2; }
    setvbuf(stdout, NULL, _IOLBF, 0);
    signal(SIGTERM, on_term); signal(SIGINT, on_term);
    t0 = now_s(); last_prog = t0;
    if (!read_model(argv[1])) { printf("c bad model\n"); return 2; }
    tlimit = atof(argv[2]);
    zero_mode = !strcmp(argv[3], "zero") ? 1 : (!strcmp(argv[3], "all") ? 2 : 0);
    mode_first = strcmp(argv[4], "count") != 0;
    outprefix = argv[5];
    if (argc == 8) { splitK = atoi(argv[6]); splitI = atoi(argv[7]); }
    nitems = 0;
    for (int r = 0; r < nrp; r++) for (int z = 0; z < n; z++) {
        if (zero_mode == 1 && z == 0) { item_of[r][z] = -1; continue; }
        item_of[r][z] = nitems++;
    }
    nw = (nitems + 63) / 64;
    if (nw > MAXW) { printf("c too many items\n"); return 2; }
    printf("c dmorbit_xc_c21v2 n %d k %d |G| %d reppairs %d items %d mode %s %s limit %.0f split %d/%d\n", n, k, ng, nrp, nitems, zero_mode == 1 ? "zero" : (zero_mode == 2 ? "all" : "nozero"), mode_first ? "first" : "count", tlimit, splitI, splitK);
    build_options();
    printf("c options built t %.1f\n", now_s() - t0);
    if (orbit_size_reachable()) xc_root();
    printf("c final t %.2f nodes %lld sols %lld root %lld/%lld timed_out %d stop_flag %d\n", now_s() - t0, nodes, nsol, root_done, root_total, timed_out, (int)stop_flag);
    if (mode_first) {
        if (nsol > 0) { printf("s SATISFIABLE\n"); return 10; }
        if (timed_out) { printf("s UNKNOWN\n"); return 0; }
        printf("s EXHAUSTED-RESTRICTED (no G-invariant DM %s%s)\n", zero_mode == 1 ? "containing the zero column" : (zero_mode == 2 ? "at all" : "without any G-fixed column"), splitK > 1 ? "; this split part only" : "");
        return 20;
    }
    printf("s COUNT %lld %s\n", nsol, timed_out ? "INCOMPLETE" : "COMPLETE");
    return 0;
}
