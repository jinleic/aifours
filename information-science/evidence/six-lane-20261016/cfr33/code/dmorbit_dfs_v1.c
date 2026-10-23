/* dmorbit_dfs_v1.c -- exact DFS for (Z_n, k; 1) difference matrices with a prescribed automorphism group
 * (lane cfr33/cfr27, worker InfoCFR27Lift, README section 5.1(a)).
 * Input: model text from code/dmorbit_compile_v1.py (group elements (mu, pi^-1), representative row pairs, orbit
 * types with full stabiliser and left-coset transversal).  Column of orbit type T with base b (b_0 = 0): for a coset
 * representative g = (mu, pi): (g b)_x = mu * b_{pi^-1(x)}; difference on row pair (i,j): mu (b_{pi^-1(i)} - b_{pi^-1(j)}).
 * DM condition is checked on one representative pair per G-orbit of row pairs (exact: other pairs are images).
 * Orbit types: zero (the zero column, contributes 0 to all pairs), stabilised (|Stab| > 1: candidate base columns
 * enumerated by brute force over Z_n^(k-1), filtered by the stabiliser equations b_x = mu_h (b_{pi_h^-1(x)} -
 * b_{pi_h^-1(0)}), internal distinctness and canonicity), free (entries assigned one by one; every difference whose two
 * entries are fixed is checked at once).  Symmetry breaking: base column = lexicographic minimum of its normalised
 * orbit images; base columns of the same type strictly increase.  Exhaustive unless deadline/SIGTERM.
 * Usage: dmorbit_dfs_v1 MODEL SECONDS MODE OUTPREFIX [SPLITK SPLITI]
 *   MODE first : stop at the first solution, write OUTPREFIX.dmraw (exclusive), exit 10, "s SATISFIABLE".
 *   MODE count : count all solutions (print up to 100000 'sol' lines), "s COUNT <c> COMPLETE|INCOMPLETE".
 *   SPLITK/SPLITI: process only first-slot base columns with running index % SPLITK == SPLITI.
 * Every solution is rebuilt as the full k x n array and re-verified on ALL row pairs (exit 5 on mismatch).
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
#define MAXG 64
#define MAXT 8
#define MAXS 64
#define MAXRP 32

static int n, k, ng;
static int gmu[MAXG], gpi[MAXG][MAXK];        /* gpi = pi^-1 */
static int nrp, rpi[MAXRP], rpj[MAXRP];
typedef struct {
    int count, zero, nstab, ncos;
    int smu[MAXG], spi[MAXG][MAXK];
    int cmu[MAXG], cpi[MAXG][MAXK];
    long long ncand; int *cand;                  /* stabilised types: ncand * k entries */
    /* free types: contributions keyed by the entry completing them */
    int nlist[MAXK]; int lr[MAXK][MAXRP * MAXG], lu[MAXK][MAXRP * MAXG], lv[MAXK][MAXRP * MAXG], lm[MAXK][MAXRP * MAXG];
} Type;
static int ntypes;
static Type ty[MAXT];
static int nslots, slot_type[MAXS], slot_prev[MAXS];
static int col[MAXS][MAXK];
static long long slot_idx[MAXS];
static uint64_t used[MAXRP];
static volatile sig_atomic_t stop_flag = 0;
static double t0, tlimit, last_prog;
static long long nodes = 0, nsol = 0, split_counter = 0;
static int splitK = 1, splitI = 0, mode_first = 1, timed_out = 0, stop_all = 0;
static const char *outprefix;
static long long first_slot_done = 0;

static double now_s(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + ts.tv_nsec * 1e-9; }
static void on_term(int s) { (void)s; stop_flag = 1; }
static inline int md(long x) { x %= n; return (int)(x < 0 ? x + n : x); }

static int canonical(const int *b) {
    for (int g = 0; g < ng; g++) {
        int base = b[gpi[g][0]];
        for (int x = 0; x < k; x++) {
            int im = md((long)gmu[g] * (b[gpi[g][x]] - base));
            if (im != b[x]) { if (im < b[x]) return 0; break; }
        }
    }
    return 1;
}
/* add all contributions of a full column of type T; returns 1 if ok (bits set), else 0 (nothing set) */
static int add_column(const Type *T, const int *b) {
    int setr[MAXRP * MAXG], setz[MAXRP * MAXG], ns = 0;
    for (int r = 0; r < nrp; r++) for (int c = 0; c < T->ncos; c++) {
        int z = md((long)T->cmu[c] * (b[T->cpi[c][rpi[r]]] - b[T->cpi[c][rpj[r]]]));
        if (used[r] >> z & 1ULL) { for (int q = 0; q < ns; q++) used[setr[q]] &= ~(1ULL << setz[q]); return 0; }
        used[r] |= 1ULL << z; setr[ns] = r; setz[ns] = z; ns++;
    }
    return 1;
}
static void remove_column(const Type *T, const int *b) {
    for (int r = 0; r < nrp; r++) for (int c = 0; c < T->ncos; c++) {
        int z = md((long)T->cmu[c] * (b[T->cpi[c][rpi[r]]] - b[T->cpi[c][rpj[r]]]));
        used[r] &= ~(1ULL << z);
    }
}
static void emit_solution(void) {
    /* rebuild full array */
    static int D[MAXK][MAXN];
    int nc = 0;
    for (int t = 0; t < ntypes; t++) if (ty[t].zero) { for (int x = 0; x < k; x++) D[x][nc] = 0; nc++; }
    for (int s = 0; s < nslots; s++) {
        const Type *T = &ty[slot_type[s]];
        for (int c = 0; c < T->ncos; c++) { for (int x = 0; x < k; x++) D[x][nc] = md((long)T->cmu[c] * col[s][T->cpi[c][x]]); nc++; }
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
            for (int s = 0; s < nslots; s++) { printf(" |"); for (int x = 1; x < k; x++) printf(" %d", col[s][x]); }
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
    for (int s = 0; s < nslots; s++) { printf("v slot %d type %d base", s, slot_type[s]); for (int x = 0; x < k; x++) printf(" %d", col[s][x]); printf("\n"); }
    stop_all = 1;
}
static void progress(int s) {
    printf("c progress t %.0f nodes %lld sols %lld slot %d first_slot_done %lld split_counter %lld\n", now_s() - t0, nodes, nsol, s, first_slot_done, split_counter);
    fflush(stdout);
}
static void dfs_slot(int s);
static void after_column(int s) {
    if (s == 0) {
        split_counter++;
        if ((split_counter - 1) % splitK != splitI) return;
    }
    dfs_slot(s + 1);
    if (s == 0) first_slot_done++;
}
static int lex_cmp_prefix_ok(int s, int e, int x, int *gt) { (void)s; (void)e; (void)x; (void)gt; return 1; }
static void dfs_entry(int s, const Type *T, int e, int gt) {
    if (stop_all) return;
    if ((++nodes & 0xFFFFF) == 0) {
        if (stop_flag || now_s() - t0 > tlimit) { timed_out = 1; stop_all = 1; return; }
        if (now_s() - last_prog > 60) { last_prog = now_s(); progress(s); }
    }
    int *b = col[s];
    if (e == k) {
        if (!gt) return;
        if (!canonical(b)) return;
        after_column(s);
        return;
    }
    int ps = slot_prev[s];
    for (int x = 0; x < n && !stop_all; x++) {
        int ngt = gt;
        if (!gt && ps >= 0) { if (x < col[ps][e]) continue; ngt = x > col[ps][e]; }
        b[e] = x;
        int setr[MAXRP * MAXG], setz[MAXRP * MAXG], ns = 0, ok = 1;
        for (int q = 0; q < T->nlist[e]; q++) {
            int r = T->lr[e][q];
            int z = md((long)T->lm[e][q] * (b[T->lu[e][q]] - b[T->lv[e][q]]));
            if (used[r] >> z & 1ULL) { ok = 0; break; }
            used[r] |= 1ULL << z; setr[ns] = r; setz[ns] = z; ns++;
        }
        if (ok) dfs_entry(s, T, e + 1, ngt);
        for (int q = 0; q < ns; q++) used[setr[q]] &= ~(1ULL << setz[q]);
    }
    b[e] = 0;
}
static void dfs_slot(int s) {
    if (stop_all) return;
    if (s == nslots) { emit_solution(); return; }
    const Type *T = &ty[slot_type[s]];
    if (T->nstab > 1) {
        long long start = (slot_prev[s] >= 0) ? slot_idx[slot_prev[s]] + 1 : 0;
        for (long long i = start; i < T->ncand && !stop_all; i++) {
            if ((++nodes & 0xFFFFF) == 0) {
                if (stop_flag || now_s() - t0 > tlimit) { timed_out = 1; stop_all = 1; return; }
                if (now_s() - last_prog > 60) { last_prog = now_s(); progress(s); }
            }
            const int *b = T->cand + i * k;
            if (!add_column(T, b)) continue;
            memcpy(col[s], b, sizeof(int) * k);
            slot_idx[s] = i;
            after_column(s);
            remove_column(T, b);
        }
        return;
    }
    col[s][0] = 0;
    dfs_entry(s, T, 1, slot_prev[s] < 0);
}

static void build_stab_candidates(Type *T, int haszero) {
    long long total = 1;
    for (int x = 1; x < k; x++) total *= n;
    long long cap = 1 << 16, cnt = 0;
    T->cand = malloc(sizeof(int) * (size_t)cap * k);
    int b[MAXK];
    for (long long code = 0; code < total; code++) {
        long long c = code; b[0] = 0;
        for (int x = 1; x < k; x++) { b[x] = (int)(c % n); c /= n; }
        int ok = 1;
        for (int h = 0; h < T->nstab && ok; h++) {
            int base = b[T->spi[h][0]];
            for (int x = 0; x < k; x++) if (md((long)T->smu[h] * (b[T->spi[h][x]] - base)) != b[x]) { ok = 0; break; }
        }
        if (!ok) continue;
        /* internal distinctness (and avoid 0 if a zero column exists) */
        for (int r = 0; r < nrp && ok; r++) {
            uint64_t seen = haszero ? 1ULL : 0ULL;
            for (int cc = 0; cc < T->ncos; cc++) {
                int z = md((long)T->cmu[cc] * (b[T->cpi[cc][rpi[r]]] - b[T->cpi[cc][rpj[r]]]));
                if (seen >> z & 1ULL) { ok = 0; break; }
                seen |= 1ULL << z;
            }
        }
        if (!ok || !canonical(b)) continue;
        if (cnt >= cap) { cap *= 2; T->cand = realloc(T->cand, sizeof(int) * (size_t)cap * k); }
        memcpy(T->cand + cnt * k, b, sizeof(int) * k);
        cnt++;
    }
    T->ncand = cnt;
}

static int read_model(const char *path) {
    FILE *fp = fopen(path, "r");
    if (!fp) { perror("model"); return 0; }
    char tag[64];
    if (fscanf(fp, "%63s", tag) != 1 || strcmp(tag, "DMORBIT-MODEL")) return 0;
    if (fscanf(fp, "%63s", tag) != 1) return 0;
    if (fscanf(fp, "%d %d", &n, &k) != 2 || n > MAXN || k > MAXK) return 0;
    if (fscanf(fp, "%63s %d", tag, &ng) != 2 || strcmp(tag, "G") || ng > MAXG) return 0;
    for (int g = 0; g < ng; g++) { if (fscanf(fp, "%d", &gmu[g]) != 1) return 0; for (int x = 0; x < k; x++) if (fscanf(fp, "%d", &gpi[g][x]) != 1) return 0; }
    if (fscanf(fp, "%63s %d", tag, &nrp) != 2 || strcmp(tag, "REPPAIRS") || nrp > MAXRP) return 0;
    for (int r = 0; r < nrp; r++) if (fscanf(fp, "%d %d", &rpi[r], &rpj[r]) != 2) return 0;
    if (fscanf(fp, "%63s %d", tag, &ntypes) != 2 || strcmp(tag, "TYPES") || ntypes > MAXT) return 0;
    for (int t = 0; t < ntypes; t++) {
        Type *T = &ty[t];
        if (fscanf(fp, "%63s %d %d %d %d", tag, &T->count, &T->zero, &T->nstab, &T->ncos) != 5 || strcmp(tag, "TYPE")) return 0;
        for (int h = 0; h < T->nstab; h++) { if (fscanf(fp, "%63s %d", tag, &T->smu[h]) != 2 || strcmp(tag, "S")) return 0; for (int x = 0; x < k; x++) if (fscanf(fp, "%d", &T->spi[h][x]) != 1) return 0; }
        for (int c = 0; c < T->ncos; c++) { if (fscanf(fp, "%63s %d", tag, &T->cmu[c]) != 2 || strcmp(tag, "C")) return 0; for (int x = 0; x < k; x++) if (fscanf(fp, "%d", &T->cpi[c][x]) != 1) return 0; }
    }
    fclose(fp);
    return 1;
}

int main(int argc, char **argv) {
    if (argc != 5 && argc != 7) { fprintf(stderr, "usage: dmorbit_dfs_v1 MODEL SECONDS MODE OUTPREFIX [SPLITK SPLITI]\n"); return 2; }
    setvbuf(stdout, NULL, _IOLBF, 0);
    signal(SIGTERM, on_term); signal(SIGINT, on_term);
    t0 = now_s(); last_prog = t0;
    if (!read_model(argv[1])) { printf("c bad model\n"); return 2; }
    tlimit = atof(argv[2]);
    mode_first = strcmp(argv[3], "count") != 0;
    outprefix = argv[4];
    if (argc == 7) { splitK = atoi(argv[5]); splitI = atoi(argv[6]); }
    int haszero = 0;
    memset(used, 0, sizeof used);
    for (int t = 0; t < ntypes; t++) if (ty[t].zero) { haszero = 1; for (int r = 0; r < nrp; r++) used[r] |= 1ULL; }
    /* slots: stabilised types first, then free types (spec order within each class) */
    nslots = 0;
    for (int pass = 0; pass < 2; pass++) for (int t = 0; t < ntypes; t++) {
        Type *T = &ty[t];
        if (T->zero) continue;
        if ((pass == 0) != (T->nstab > 1)) continue;
        for (int c = 0; c < T->count; c++) {
            slot_type[nslots] = t;
            slot_prev[nslots] = (c > 0) ? nslots - 1 : -1;
            nslots++;
        }
    }
    for (int t = 0; t < ntypes; t++) {
        Type *T = &ty[t];
        if (T->zero) continue;
        if (T->nstab > 1) {
            build_stab_candidates(T, haszero);
            printf("c type %d stabilised |Stab| %d orbit size %d count %d candidates %lld\n", t, T->nstab, T->ncos, T->count, T->ncand);
        } else {
            for (int e = 0; e < k; e++) T->nlist[e] = 0;
            for (int r = 0; r < nrp; r++) for (int c = 0; c < T->ncos; c++) {
                int u = T->cpi[c][rpi[r]], v = T->cpi[c][rpj[r]];
                int e = u > v ? u : v;
                int q = T->nlist[e]++;
                T->lr[e][q] = r; T->lu[e][q] = u; T->lv[e][q] = v; T->lm[e][q] = T->cmu[c];
            }
            if (T->nlist[0] != 0) { printf("c INTERNAL: contribution with u = v = 0\n"); return 5; }
            printf("c type %d free orbit size %d count %d\n", t, T->ncos, T->count);
        }
    }
    printf("c dmorbit_dfs_v1 n %d k %d |G| %d reppairs %d slots %d mode %s limit %.0f split %d/%d\n", n, k, ng, nrp, nslots, mode_first ? "first" : "count", tlimit, splitI, splitK);
    fflush(stdout);
    (void)lex_cmp_prefix_ok;
    dfs_slot(0);
    printf("c final t %.2f nodes %lld sols %lld first_slot_done %lld split_counter %lld timed_out %d stop_flag %d\n", now_s() - t0, nodes, nsol, first_slot_done, split_counter, timed_out, (int)stop_flag);
    if (mode_first) {
        if (nsol > 0) { printf("s SATISFIABLE\n"); return 10; }
        if (timed_out) { printf("s UNKNOWN\n"); return 0; }
        printf("s EXHAUSTED-RESTRICTED (no solution in this model%s)\n", splitK > 1 ? ", this split part only" : "");
        return 20;
    }
    printf("s COUNT %lld %s\n", nsol, timed_out ? "INCOMPLETE" : "COMPLETE");
    return 0;
}
