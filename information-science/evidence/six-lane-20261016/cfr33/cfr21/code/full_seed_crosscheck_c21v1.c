/* Independent finite-first-row checker adapted from keq_clique_c21v1.c.
 * Here K={1}: every nonzero point is independent, with no oddness/multiplier
 * restriction. Point-MRV set-mask DFS enumerates full L2 for each supplied
 * normalized orthomorphism; direct difference tests build its graph and an
 * exact (KK-3)-clique search checks extension to a KK-row cyclic DM.
 * This is a different L2 algorithm from cfr_perm_search_c21v1's class-item
 * bitmask exact cover. Every candidate gets an all-row-pair direct check.
 * CLI: full_seed_crosscheck_c21v1 N KK F1FILE SECONDS first|count OUTFILE
 * F1FILE: one function per line, exactly N-1 values, f(0)=0 implicit.
 * Exhaustion covers ONLY this supplied finite first-row inventory.
 * Store/edge caps or native deadline/SIGTERM yield UNKNOWN, never exclusion.
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
#define MAXKK 10
#define MAXKG 64
#define STORELIMIT (1LL << 20)
#define EDGELIMIT (1LL << 26)

static int n, kk, nK, Kel[MAXKG];
static int units[MAXN], nunits;
static uint64_t orbmask[MAXN];
static int orbsize[MAXN];
static uint64_t stabK[MAXN];          /* bitmask over K indices fixing x */
static int reps[MAXN], nreps;
static volatile sig_atomic_t stop_flag = 0;
static double t0, tlimit, last_prog;
static int timed_out = 0;
static int dfs_stop, memory_limit_hit;
static long long dfs_nodes = 0;

static double now_s(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + ts.tv_nsec * 1e-9; }
static void on_term(int s) { (void)s; stop_flag = 1; }
static inline int md(int x) { x %= n; return x < 0 ? x + n : x; }
static int check_time(void) { if (stop_flag || now_s() - t0 > tlimit) timed_out = 1; return timed_out; }

/* ---------------------------------------------------------------- map store */
typedef struct { long long cnt, cap; uint8_t *a; } Store;
static void st_push(Store *S, const int *f) {
    if (S->cnt >= STORELIMIT) {
        memory_limit_hit=1;timed_out=1;dfs_stop=1;
        printf("c store limit reached; UNKNOWN\n");return;
    }
    if (S->cnt >= S->cap) { S->cap = S->cap ? S->cap * 2 : 1024; S->a = realloc(S->a, (size_t)S->cap * n); if (!S->a) { printf("c out of memory\n"); exit(3); } }
    for (int x = 0; x < n; x++) S->a[S->cnt * n + x] = (uint8_t)f[x];
    S->cnt++;
}

/* ---------------------------------------------------------------- K-equivariant orthomorphism DFS */
static int nb, bmap[4][MAXN];
static uint64_t usedB[4];
static int fv[MAXN], assigned[MAXN];
static Store *dst;
static int cand_ok(int x, int v) {
    if ((stabK[x] & ~stabK[v]) != 0) return 0;            /* stabiliser of x must fix v */
    for (int b = 0; b < nb; b++) {
        int d = md(v - bmap[b][x]);
        if (d == 0 || orbsize[d] != orbsize[x] || (orbmask[d] & usedB[b])) return 0;
    }
    return 1;
}
static void dfs(int depth) {
    if (dfs_stop) return;
    if ((++dfs_nodes & 0xFFFF) == 0 && check_time()) { dfs_stop = 1; return; }
    if (depth == nreps) { st_push(dst, fv); return; }
    int best = -1, bestc = 1 << 30; uint64_t bestm = 0;
    for (int r = 0; r < nreps; r++) {
        int x = reps[r];
        if (assigned[x]) continue;
        uint64_t m = 0; int c = 0;
        for (int v = 1; v < n; v++) if (cand_ok(x, v)) { m |= 1ULL << v; c++; }
        if (c == 0) return;
        if (c < bestc) { bestc = c; best = x; bestm = m; }
    }
    int x = best;
    while (bestm && !dfs_stop) {
        int v = __builtin_ctzll(bestm); bestm &= bestm - 1;
        uint64_t save[4];
        for (int b = 0; b < nb; b++) { save[b] = usedB[b]; usedB[b] |= orbmask[md(v - bmap[b][x])]; }
        for (int i = 0; i < nK; i++) fv[md(Kel[i] * x)] = md(Kel[i] * v);
        assigned[x] = 1;
        dfs(depth + 1);
        assigned[x] = 0;
        for (int b = 0; b < nb; b++) usedB[b] = save[b];
    }
}
static void enum_maps(int nbase, int base[][MAXN], Store *out) {
    nb = nbase;
    for (int b = 0; b < nb; b++) { memcpy(bmap[b], base[b], sizeof(int) * n); usedB[b] = 1ULL; }   /* 0 used */
    memset(assigned, 0, sizeof assigned);
    for (int x = 0; x < n; x++) fv[x] = 0;
    dst = out; out->cnt = 0; dfs_stop = 0;
    dfs(0);
}
static int orth(const uint8_t *f, const uint8_t *g) {
    uint64_t seen = 0;
    for (int x = 0; x < n; x++) { int d = md((int)f[x] - (int)g[x]); if (seen >> d & 1ULL) return 0; seen |= 1ULL << d; }
    return 1;
}
static int is_bij(const int *f) { uint64_t seen = 0; for (int x = 0; x < n; x++) { if (seen >> f[x] & 1ULL) return 0; seen |= 1ULL << f[x]; } return 1; }

/* ---------------------------------------------------------------- R1 canonical test */
static int lexless(const int *a, const uint8_t *b) { for (int x = 0; x < n; x++) if (a[x] != b[x]) return a[x] < b[x]; return 0; }
static int uinv(int u) { for (int y = 1; y < n; y++) if (md(u * y) == 1) return y; return 0; }
static int is_rep(const uint8_t *f) {
    int imgs[16][MAXN], ni = 0;
    for (int x = 0; x < n; x++) imgs[0][x] = f[x];
    ni = 1;
    for (int q = 0; q < ni && ni < 16; q++) {
        int A[MAXN], I[MAXN];
        for (int x = 0; x < n; x++) A[x] = md(imgs[q][md(-x)] + x);
        for (int x = 0; x < n; x++) I[imgs[q][x]] = x;
        int *cand[2] = {A, I};
        for (int c = 0; c < 2; c++) {
            int dup = 0;
            for (int r = 0; r < ni && !dup; r++) if (!memcmp(imgs[r], cand[c], sizeof(int) * n)) dup = 1;
            if (!dup && ni < 16) { memcpy(imgs[ni], cand[c], sizeof(int) * n); ni++; }
        }
    }
    if (ni > 6) { printf("c INTERNAL anharmonic closure %d > 6\n", ni); exit(5); }
    for (int q = 0; q < ni; q++) for (int s = 0; s < nunits; s++) {
        int u = units[s], ui = uinv(u), im[MAXN];
        for (int x = 0; x < n; x++) im[x] = md(u * imgs[q][md(ui * x)]);
        if (lexless(im, f)) return 0;
    }
    return 1;
}

/* ---------------------------------------------------------------- cliques */
static Store L2;
static int *adjoff = NULL, *adj = NULL; static long long adjcap = 0;
static int clq[MAXKK];
static long long clique_count;
static int count_mode = 0;
static int clique_rec(int depth, int need, const int *candv, int ncand) {
    if (depth == need) { clique_count++; return !count_mode; }
    if(check_time())return 0;
    for (int i = 0; i < ncand && !timed_out; i++) {
        int v = candv[i];
        clq[depth] = v;
        if (depth + 1 == need) { clique_count++; if (!count_mode) return 1; continue; }
        int *nc = malloc(sizeof(int) * (ncand > 0 ? ncand : 1)); int nn = 0;
        if(!nc){memory_limit_hit=1;timed_out=1;return 0;}
        for (int k2 = i + 1, e = adjoff[v]; k2 < ncand && e < adjoff[v + 1]; ) {
            if (candv[k2] == adj[e]) { nc[nn++] = candv[k2]; k2++; e++; }
            else if (candv[k2] < adj[e]) k2++; else e++;
        }
        int r = (nn >= need - depth - 1) ? clique_rec(depth + 1, need, nc, nn) : 0;
        free(nc);
        if (r) return 1;
    }
    return 0;
}

int main(int argc, char **argv) {
    if (argc != 7) { fprintf(stderr, "usage: full_seed_crosscheck_c21v1 N KK F1FILE SECONDS first|count OUTFILE\n"); return 2; }
    setvbuf(stdout, NULL, _IOLBF, 0);
    signal(SIGTERM, on_term); signal(SIGINT, on_term);
    t0 = now_s(); last_prog = t0;
    n = atoi(argv[1]); kk = atoi(argv[2]);
    if (n < 3 || n > MAXN || kk < 3 || kk > MAXKK) { printf("c bad N/KK\n"); return 2; }
    nK=1;Kel[0]=1;
    tlimit=atof(argv[4]);
    count_mode=!strcmp(argv[5],"count");
    const char *outfile=argv[6];
    nunits = 0;
    for (int u = 1; u < n; u++) { int g = u, h = n; while (h) { int t = g % h; g = h; h = t; } if (g == 1) units[nunits++] = u; }
    for (int i = 0; i < nK; i++) { int ok = 0; for (int s = 0; s < nunits; s++) if (units[s] == Kel[i]) ok = 1; if (!ok) { printf("c K element %d not a unit\n", Kel[i]); return 2; } }
    nreps = 0;
    uint64_t seen = 0;
    for (int x = 0; x < n; x++) {
        orbmask[x] = 0; stabK[x] = 0;
        for (int i = 0; i < nK; i++) { orbmask[x] |= 1ULL << md(Kel[i] * x); if (md(Kel[i] * x) == x) stabK[x] |= 1ULL << i; }
        orbsize[x] = __builtin_popcountll(orbmask[x]);
        if (x > 0 && !(seen >> x & 1ULL)) { reps[nreps++] = x; seen |= orbmask[x]; }
    }
    printf("c full_seed_crosscheck_c21v1 N %d KK %d finite_file %s limit %.0f mode %s\n",n,kk,argv[3],tlimit,count_mode?"count":"first");
    /* Read only the explicit finite inventory; never enumerate all K={1} maps. */
    int base[3][MAXN];
    for (int x = 0; x < n; x++) { base[0][x] = 0; base[1][x] = x; }
    Store T = {0, 0, NULL};
    FILE *input=fopen(argv[3],"r");if(!input){perror("f1file");return 3;}
    char line[8192];long long input_line=0;
    while(fgets(line,sizeof line,input)){
        input_line++;int f[MAXN];f[0]=0;char *p=line;
        for(int x=1;x<n;x++){
            char *e;long v=strtol(p,&e,10);
            if(e==p||v<0||v>=n){printf("c malformed f1 line %lld\n",input_line);return 2;}
            f[x]=(int)v;p=e;
        }
        while(*p==' '||*p=='\t'||*p=='\r')p++;
        if(*p!='\n'||p[1]){printf("c malformed f1 line %lld\n",input_line);return 2;}
        st_push(&T,f);if(timed_out)break;
    }
    fclose(input);
    if(timed_out){puts("s UNKNOWN (inventory limit)");return 0;}
    if(!T.cnt){puts("c empty inventory");return 2;}
    for (long long i = 0; i < T.cnt; i++) {        /* verify every stored map */
        int f[MAXN], g[MAXN];
        for (int x = 0; x < n; x++) { f[x] = T.a[i * n + x]; g[x] = md(f[x] - x); }
        if (f[0] != 0 || !is_bij(f) || !is_bij(g)) { printf("c INTERNAL level-1 map %lld invalid\n", i); return 5; }
        for (int j = 0; j < nK; j++) for (int x = 0; x < n; x++) if (f[md(Kel[j] * x)] != md(Kel[j] * f[x])) { printf("c INTERNAL map %lld not K-equivariant\n", i); return 5; }
    }
    long long nrep = 0;
    uint8_t *isrep = calloc((size_t)(T.cnt > 0 ? T.cnt : 1), 1);
    for (long long i = 0; i < T.cnt; i++) { isrep[i]=1; nrep++; }
    printf("c finite first-row inputs %lld t %.1f\n",T.cnt,now_s()-t0);
    int need = kk - 3;
    long long done_f1 = 0, total_L2 = 0, total_edges = 0, total_cliques = 0;
    int found = 0;
    int sol[MAXKK][MAXN];
    for (long long i = 0; i < T.cnt && !found && !timed_out; i++) {
        if (!isrep[i]) continue;
        for (int x = 0; x < n; x++) base[2][x] = T.a[i * n + x];
        L2.cnt = 0;
        enum_maps(3, base, &L2);
        if (timed_out) break;
        long long n2 = L2.cnt; total_L2 += n2;
        clique_count = 0;
        long long case_edges=0;
        if (need == 0) { clique_count = 1; if (!count_mode) found = 1; }
        else if (need == 1) { clique_count = n2; if (n2 > 0 && !count_mode) { found = 1; clq[0] = 0; } }
        else {
            long long edges = 0;
            if (adjoff) free(adjoff);
            adjoff = malloc(sizeof(int) * (size_t)(n2 + 1));
            if (!adj) { adjcap = 1 << 20; adj = malloc(sizeof(int) * (size_t)adjcap); }
            if(!adjoff||!adj){memory_limit_hit=1;timed_out=1;break;}
            for (long long u = 0; u < n2 && !timed_out; u++) {
                adjoff[u] = (int)edges;
                for (long long v = u + 1; v < n2; v++) if (orth(L2.a + u * n, L2.a + v * n)) {
                    if (edges >= adjcap) {
                        if(adjcap>=EDGELIMIT){memory_limit_hit=1;timed_out=1;break;}
                        long long cap=adjcap*2;if(cap>EDGELIMIT)cap=EDGELIMIT;
                        int *tmp=realloc(adj,sizeof(int)*(size_t)cap);
                        if(!tmp){memory_limit_hit=1;timed_out=1;break;}adj=tmp;adjcap=cap;
                    }
                    adj[edges++] = (int)v;
                }
                if ((u & 15) == 0 && check_time()) break;
            }
            if (timed_out) break;
            adjoff[n2] = (int)edges; total_edges += edges;
            case_edges=edges;
            for (long long u = 0; u < n2 && !timed_out; u++) {
                if (adjoff[u + 1] - adjoff[u] < need - 1) continue;
                clq[0] = (int)u;
                if (clique_rec(1, need, adj + adjoff[u], adjoff[u + 1] - adjoff[u]) && !count_mode) { found = 1; break; }
            }
        }
        if (timed_out) break;
        done_f1++;
        total_cliques += clique_count;
        printf("cnt f1 %lld L2 %lld edges %lld cliques %lld\n",i,n2,case_edges,clique_count);
        if (found) {
            for (int x = 0; x < n; x++) { sol[0][x] = 0; sol[1][x] = x; sol[2][x] = base[2][x]; }
            for (int j = 0; j < need; j++) for (int x = 0; x < n; x++) sol[3 + j][x] = L2.a[(long long)clq[j] * n + x];
        }
        if (now_s() - last_prog > 60) { last_prog = now_s(); printf("c progress f1 done %lld/%lld L2 total %lld edges %lld cliques %lld t %.0f\n", done_f1, nrep, total_L2, total_edges, total_cliques, now_s() - t0); }
    }
    printf("c final f1 done %lld/%lld L2 total %lld edges %lld cliques %lld timed_out %d t %.2f\n", done_f1, nrep, total_L2, total_edges, total_cliques, timed_out, now_s() - t0);
    if (count_mode) { printf("s COUNT %lld %s\n", total_cliques, (timed_out || done_f1 < nrep) ? "INCOMPLETE" : "COMPLETE"); return 0; }
    if (!found) {
        if (!timed_out && done_f1 == nrep) { printf("s EXHAUSTED-RESTRICTED (supplied finite first-row inventory only)\n"); return 20; }
        printf("s UNKNOWN\n"); return 0;
    }
    /* verify all DM row pairs */
    for (int a = 0; a < kk; a++) for (int b = a + 1; b < kk; b++) {
        uint64_t s2 = 0;
        for (int x = 0; x < n; x++) { int d = md(sol[a][x] - sol[b][x]); if (s2 >> d & 1ULL) { printf("c INTERNAL MISMATCH rows %d %d\n", a, b); return 5; } s2 |= 1ULL << d; }
    }
    printf("s SATISFIABLE\n");
    for (int j = 2; j < kk; j++) { printf("v f%d", j - 1); for (int x = 0; x < n; x++) printf(" %d", sol[j][x]); printf("\n"); }
    int fd = open(outfile, O_WRONLY | O_CREAT | O_EXCL, 0444);
    if (fd < 0) { perror("open outfile"); return 3; }
    FILE *o = fdopen(fd, "w");
    for (int c = 0; c < n; c++) fprintf(o, c ? " %d" : "%d", c);
    fprintf(o, "\n");
    for (int j = 2; j < kk; j++) {
        int row[MAXN];
        for (int s = 0; s < n; s++) row[sol[j][s]] = s;
        for (int c = 0; c < n; c++) fprintf(o, c ? " %d" : "%d", row[c]);
        fprintf(o, "\n");
    }
    fclose(o);
    return 10;
}
