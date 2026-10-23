/* pc_tabu2.c -- representation R1b of the point-cyclic-table200 lane README (Section 2, frozen before use): the R1
 * tabu search of pc_tabu.c with a FOCUSED neighborhood. Only moves that change at least one residue lying in a pair
 * whose difference class is over capacity are evaluated; everything else (state, cost, move types, tabu rules,
 * aspiration, perturbation, output) is as in pc_tabu.c. Text below is the pc_tabu.c description.
 *
 * pc_tabu.c -- representation R1 of the point-cyclic-table200 lane README (Section 1.5).
 *
 * Tabu search for base blocks of one orbit type (t, K) of a point-cyclic resolution of a 2-(v,4,1) design,
 * v = 4n, v = 4 (mod 12) (GENERAL-REDUCTION.md, Theorem C'):
 *   group 0 (only if t > 1): modulus t, residues 1..t-1, (t-1)/4 blocks  -> condition (R1);
 *   one group per k in K:     modulus 4k, residues 0..4k-1, k blocks        -> condition (R2).
 * Every residue of a group carries a block label (exactly 4 residues per block, so (R1)/(R2) hold by construction)
 * and a height j in [0, v/modulus); its point is residue + modulus * j (in [0, v)).
 * Cost = sum over difference classes c = min(d, v-d) (d != 0) of max(0, count[c] - cap[c]), cap = 0 for multiples
 * of n (H = <n>), 1 otherwise.  Cost 0 <=> condition (D).
 *
 * Moves: M1 change the height of one residue; M2 exchange two residues of one group between two blocks (heights
 * travel with the residues); M3 the same exchange with the heights staying in place; M4 exchange the heights of two
 * residues of one block.  Best non-tabu move (reservoir tie-break), aspiration when the move beats the best cost of
 * the current descent, random perturbation after `stall` non-improving iterations.  Deterministic per seed
 * (splitmix64); the wall clock is used only for the time limit and progress lines.  No normalization is imposed.
 *
 * Usage: pc_tabu v t K seed seconds outprefix [tl tr stall pert]
 *   K: comma-separated list of k (e.g. 7,2) or '-' for the empty multiset.
 * Output: outprefix.seed (strict PC-SEED, README 1.5) on success; outprefix.best (best cost, not a witness) on time
 * limit.  Output files are created exclusively (never overwritten); nothing is ever deleted.
 * Exit 0 found, 3 time limit, 2 usage/internal error.
 */
#include <fcntl.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define MAXV 256
#define MAXIT 96
#define MAXB 24
#define MAXG 24

static int v, n, t, ng, nitems, nblocks;
static int gmod[MAXG], gnb[MAXG], ghr[MAXG], gk[MAXG], gfi[MAXG], gni[MAXG];
static int ires[MAXIT], igrp[MAXIT], ihgt[MAXIT], iblk[MAXIT], islot[MAXIT];
static int bgrp[MAXB], bmem[MAXB][4];
static int cnt[MAXV / 2 + 1], cap[MAXV / 2 + 1];
static int cost;
static long long tabu_h[MAXIT][MAXV], tabu_b[MAXIT][MAXB];
static uint64_t rng;

static uint64_t rnd(void) {
    uint64_t z = (rng += 0x9E3779B97F4A7C15ULL);
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
    z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
    return z ^ (z >> 31);
}
static int rndint(int m) { return (int)(rnd() % (uint64_t)m); }
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }

static inline int ptval(int i) { return ires[i] + gmod[igrp[i]] * ihgt[i]; }
static inline int cls(int x, int y) { int d = x - y; if (d < 0) d += v; return d <= v / 2 ? d : v - d; }
static inline int inc(int c) { int c0 = cnt[c]++; return c0 >= cap[c] ? 1 : 0; }
static inline int dec(int c) { int c1 = --cnt[c]; return c1 >= cap[c] ? -1 : 0; }

static void full_recount(void) {
    memset(cnt, 0, sizeof cnt);
    cost = 0;
    for (int b = 0; b < nblocks; b++)
        for (int s = 0; s < 4; s++)
            for (int u = s + 1; u < 4; u++) cost += inc(cls(ptval(bmem[b][s]), ptval(bmem[b][u])));
}

/* ---- moves ---- */
enum { M1, M2, M3, M4 };
typedef struct { int type, a, b; } Move;   /* M1: item a, new height b; M2-M4: items a, b */

static int nrem, nadd, rem[64], add[64];
static void diff_block(int blk, const int *oldp, const int *newp) {
    for (int s = 0; s < 4; s++)
        for (int u = s + 1; u < 4; u++)
            if (oldp[s] != newp[s] || oldp[u] != newp[u]) {
                rem[nrem++] = cls(oldp[s], oldp[u]);
                add[nadd++] = cls(newp[s], newp[u]);
            }
    (void)blk;
}
static void build_lists(const Move *m) {
    int op[4], np[4], op2[4], np2[4];
    nrem = nadd = 0;
    if (m->type == M1) {
        int i = m->a, b = iblk[i];
        for (int s = 0; s < 4; s++) op[s] = np[s] = ptval(bmem[b][s]);
        np[islot[i]] = ires[i] + gmod[igrp[i]] * m->b;
        diff_block(b, op, np);
    } else if (m->type == M2 || m->type == M3) {
        int i = m->a, i2 = m->b, b = iblk[i], b2 = iblk[i2], mod = gmod[igrp[i]];
        for (int s = 0; s < 4; s++) { op[s] = np[s] = ptval(bmem[b][s]); op2[s] = np2[s] = ptval(bmem[b2][s]); }
        if (m->type == M2) { np[islot[i]] = ptval(i2); np2[islot[i2]] = ptval(i); }
        else { np[islot[i]] = ires[i2] + mod * ihgt[i]; np2[islot[i2]] = ires[i] + mod * ihgt[i2]; }
        diff_block(b, op, np);
        diff_block(b2, op2, np2);
    } else {
        int i = m->a, i2 = m->b, b = iblk[i], mod = gmod[igrp[i]];
        for (int s = 0; s < 4; s++) op[s] = np[s] = ptval(bmem[b][s]);
        np[islot[i]] = ires[i] + mod * ihgt[i2];
        np[islot[i2]] = ires[i2] + mod * ihgt[i];
        diff_block(b, op, np);
    }
}
static int eval_lists(void) {
    int d = 0;
    for (int k = 0; k < nrem; k++) d += dec(rem[k]);
    for (int k = 0; k < nadd; k++) d += inc(add[k]);
    for (int k = 0; k < nadd; k++) cnt[add[k]]--;
    for (int k = 0; k < nrem; k++) cnt[rem[k]]++;
    return d;
}
static int is_tabu(const Move *m, long long it) {
    if (m->type == M1) return tabu_h[m->a][m->b] > it;
    if (m->type == M2 || m->type == M3)
        return tabu_b[m->a][iblk[m->b]] > it || tabu_b[m->b][iblk[m->a]] > it;
    return tabu_h[m->a][ihgt[m->b]] > it || tabu_h[m->b][ihgt[m->a]] > it;
}
static void commit(const Move *m, long long it, int tl, int tr) {
    build_lists(m);
    for (int k = 0; k < nrem; k++) cost += dec(rem[k]);
    for (int k = 0; k < nadd; k++) cost += inc(add[k]);
    long long until = it + tl + (tr > 0 ? rndint(tr) : 0);
    if (m->type == M1) {
        tabu_h[m->a][ihgt[m->a]] = until;
        ihgt[m->a] = m->b;
    } else if (m->type == M2 || m->type == M3) {
        int i = m->a, i2 = m->b, b = iblk[i], b2 = iblk[i2], s = islot[i], s2 = islot[i2];
        tabu_b[i][b] = until;
        tabu_b[i2][b2] = until;
        bmem[b][s] = i2; bmem[b2][s2] = i;
        iblk[i] = b2; islot[i] = s2; iblk[i2] = b; islot[i2] = s;
        if (m->type == M3) { int h = ihgt[i]; ihgt[i] = ihgt[i2]; ihgt[i2] = h; }
    } else {
        int i = m->a, i2 = m->b;
        tabu_h[i][ihgt[i]] = until;
        tabu_h[i2][ihgt[i2]] = until;
        int h = ihgt[i]; ihgt[i] = ihgt[i2]; ihgt[i2] = h;
    }
}
static void random_move(Move *m) {
    for (;;) {
        int i = rndint(nitems), g = igrp[i];
        if (rndint(2) == 0 && ghr[g] > 1) {
            int h = rndint(ghr[g]);
            if (h != ihgt[i]) { m->type = M1; m->a = i; m->b = h; return; }
        } else if (gnb[g] > 1) {
            int i2 = gfi[g] + rndint(gni[g]);
            if (iblk[i2] != iblk[i]) { m->type = rndint(2) ? M2 : M3; m->a = i; m->b = i2; return; }
        } else if (ghr[g] > 1) {
            int s2 = rndint(4), i2 = bmem[iblk[i]][s2];
            if (i2 != i && ihgt[i2] != ihgt[i]) { m->type = M4; m->a = i; m->b = i2; return; }
        }
    }
}

/* ---- output ---- */
static int cmp4(const void *x, const void *y) { return memcmp(x, y, 4 * sizeof(int)) ; }
static int cmpint(const void *x, const void *y) { return *(const int *)x - *(const int *)y; }
static int lexcmp4(const int *a, const int *b) { for (int s = 0; s < 4; s++) if (a[s] != b[s]) return a[s] < b[s] ? -1 : 1; return 0; }
static int cmpblk(const void *x, const void *y) { return lexcmp4((const int *)x, (const int *)y); }

static FILE *xopen(const char *path) {
    int fd = open(path, O_WRONLY | O_CREAT | O_EXCL, 0644);
    if (fd < 0) { perror(path); exit(2); }
    return fdopen(fd, "w");
}
static void write_seed(const char *path) {
    int pts[MAXB][4];
    for (int b = 0; b < nblocks; b++) {
        for (int s = 0; s < 4; s++) pts[b][s] = ptval(bmem[b][s]);
        qsort(pts[b], 4, sizeof(int), cmpint);
    }
    /* group order: group 0 (X) first if t > 1, then groups by nonincreasing k, ties by sorted line lists */
    int order[MAXG], no = 0, gl[MAXG][MAXB][4];
    for (int g = 0; g < ng; g++) {
        int nb = 0;
        for (int b = 0; b < nblocks; b++) if (bgrp[b] == g) { memcpy(gl[g][nb], pts[b], sizeof pts[b]); nb++; }
        qsort(gl[g], nb, sizeof gl[g][0], cmpblk);
    }
    for (int g = 0; g < ng; g++) if (gk[g] > 0) order[no++] = g;
    for (int x = 0; x < no; x++)            /* insertion sort */
        for (int y = x; y > 0; y--) {
            int a = order[y - 1], b = order[y], sw = 0;
            if (gk[a] < gk[b]) sw = 1;
            else if (gk[a] == gk[b]) {
                for (int l = 0; l < gk[a]; l++) { int c = lexcmp4(gl[a][l], gl[b][l]); if (c) { sw = c > 0; break; } }
            }
            if (sw) { order[y - 1] = b; order[y] = a; } else break;
        }
    FILE *f = xopen(path);
    fprintf(f, "PC-SEED %d\nSHORT %d\n", v, t);
    if (t > 1) for (int l = 0; l < gnb[0]; l++) fprintf(f, "X %d %d %d %d\n", gl[0][l][0], gl[0][l][1], gl[0][l][2], gl[0][l][3]);
    for (int x = 0; x < no; x++) {
        int g = order[x];
        fprintf(f, "GROUP %d\n", gk[g]);
        for (int l = 0; l < gnb[g]; l++) fprintf(f, "Y %d %d %d %d\n", gl[g][l][0], gl[g][l][1], gl[g][l][2], gl[g][l][3]);
    }
    fclose(f);
    (void)cmp4;
}

int main(int argc, char **argv) {
    if (argc < 7) {
        fprintf(stderr, "usage: pc_tabu v t K seed seconds outprefix [tl tr stall pert]\n");
        return 2;
    }
    v = atoi(argv[1]); t = atoi(argv[2]);
    const char *Ks = argv[3];
    uint64_t seed = strtoull(argv[4], 0, 10);
    double secs = atof(argv[5]);
    const char *pre = argv[6];
    int tl = argc > 7 ? atoi(argv[7]) : 10, tr = argc > 8 ? atoi(argv[8]) : 10;
    int stall = argc > 9 ? atoi(argv[9]) : 5000, pert = argc > 10 ? atoi(argv[10]) : 4;
    if (v < 16 || v > MAXV || v % 12 != 4) { fprintf(stderr, "v must be 4 mod 12, 16..%d\n", MAXV); return 2; }
    n = v / 4;
    if (t < 1 || n % t || t % 4 != 1) { fprintf(stderr, "t must divide n and be 1 mod 4\n"); return 2; }
    for (int c = 0; c <= v / 2; c++) cap[c] = (c % n == 0) ? 0 : 1;
    /* groups */
    ng = 0;
    if (t > 1) { gmod[ng] = t; gnb[ng] = (t - 1) / 4; gk[ng] = 0; ng++; }
    if (strcmp(Ks, "-") != 0) {
        char buf[256]; strncpy(buf, Ks, 255); buf[255] = 0;
        for (char *tok = strtok(buf, ","); tok; tok = strtok(0, ",")) {
            int k = atoi(tok);
            if (k < 1 || n % k) { fprintf(stderr, "every k must divide n\n"); return 2; }
            if (ng >= MAXG) { fprintf(stderr, "too many groups\n"); return 2; }
            gmod[ng] = 4 * k; gnb[ng] = k; gk[ng] = k; ng++;
        }
    }
    int sumk = 0;
    for (int g = 0; g < ng; g++) sumk += gk[g];
    if (t + 4 * sumk != (v - 1) / 3) { fprintf(stderr, "(E) fails: t + 4 sum(K) != r\n"); return 2; }
    rng = seed * 0x2545F4914F6CDD1DULL + 777;
    nitems = nblocks = 0;
    for (int g = 0; g < ng; g++) {
        ghr[g] = v / gmod[g];
        gfi[g] = nitems;
        int r0 = (g == 0 && t > 1) ? 1 : 0, nr = gmod[g] - r0;
        int perm[MAXV];
        for (int x = 0; x < nr; x++) perm[x] = r0 + x;
        for (int x = nr - 1; x > 0; x--) { int y = rndint(x + 1), z = perm[x]; perm[x] = perm[y]; perm[y] = z; }
        if (nr != 4 * gnb[g] || nitems + nr > MAXIT || nblocks + gnb[g] > MAXB) { fprintf(stderr, "internal sizes\n"); return 2; }
        for (int b = 0; b < gnb[g]; b++) {
            int B = nblocks++;
            bgrp[B] = g;
            for (int s = 0; s < 4; s++) {
                int i = nitems++;
                ires[i] = perm[4 * b + s]; igrp[i] = g; ihgt[i] = rndint(ghr[g]); iblk[i] = B; islot[i] = s;
                bmem[B][s] = i;
            }
        }
        gni[g] = nitems - gfi[g];
    }
    if (nblocks != (n - 1) / 3) { fprintf(stderr, "internal: block count\n"); return 2; }
    full_recount();
    printf("start v=%d n=%d t=%d K=%s groups=%d blocks=%d items=%d seed=%llu cost=%d tl=%d tr=%d stall=%d pert=%d\n",
           v, n, t, Ks, ng, nblocks, nitems, (unsigned long long)seed, cost, tl, tr, stall, pert);
    fflush(stdout);
    double t0 = now(), tlast = t0;
    long long it = 0, last_impr = 0;
    int dbest = cost, gbest = cost;
    Move cand, bestm;
    for (;;) {
        if (cost == 0) {
            full_recount();
            if (cost != 0) { fprintf(stderr, "internal: recount mismatch %d\n", cost); return 2; }
            char path[1024];
            snprintf(path, sizeof path, "%s.seed", pre);
            write_seed(path);
            printf("FOUND it=%lld t=%.2f %s\n", it, now() - t0, path);
            fflush(stdout);
            return 0;
        }
        it++;
        int bestd = 1 << 30, nties = 0;
        /* focus: items of pairs whose difference class is over capacity */
        int hot[MAXIT], nhot = 0;
        static int mark[MAXIT];
        memset(mark, 0, sizeof mark);
        for (int b = 0; b < nblocks; b++)
            for (int s = 0; s < 4; s++)
                for (int u = s + 1; u < 4; u++) {
                    int i = bmem[b][s], i2 = bmem[b][u], c = cls(ptval(i), ptval(i2));
                    if (cnt[c] > cap[c]) {
                        if (!mark[i]) { mark[i] = 1; hot[nhot++] = i; }
                        if (!mark[i2]) { mark[i2] = 1; hot[nhot++] = i2; }
                    }
                }
        for (int x = 0; x < nhot; x++) {             /* M1 on hot items */
            int i = hot[x], g = igrp[i];
            for (int h = 0; h < ghr[g]; h++) {
                if (h == ihgt[i]) continue;
                cand.type = M1; cand.a = i; cand.b = h;
                build_lists(&cand);
                int d = eval_lists();
                if (is_tabu(&cand, it) && cost + d >= dbest) continue;
                if (d < bestd) { bestd = d; bestm = cand; nties = 1; }
                else if (d == bestd && rndint(++nties) == 0) bestm = cand;
            }
        }
        for (int x = 0; x < nhot; x++) {             /* M2, M3 with a hot item */
            int i = hot[x], g = igrp[i];
            if (gnb[g] < 2) continue;
            for (int i2 = gfi[g]; i2 < gfi[g] + gni[g]; i2++) {
                if (iblk[i] == iblk[i2] || (mark[i2] && i2 < i)) continue;
                for (int ty = M2; ty <= M3; ty++) {
                    if (ty == M3 && ihgt[i] == ihgt[i2]) continue;
                    cand.type = ty; cand.a = i; cand.b = i2;
                    build_lists(&cand);
                    int d = eval_lists();
                    if (is_tabu(&cand, it) && cost + d >= dbest) continue;
                    if (d < bestd) { bestd = d; bestm = cand; nties = 1; }
                    else if (d == bestd && rndint(++nties) == 0) bestm = cand;
                }
            }
        }
        for (int x = 0; x < nhot; x++) {             /* M4 with a hot item */
            int i = hot[x], b = iblk[i];
            for (int u = 0; u < 4; u++) {
                int i2 = bmem[b][u];
                if (i2 == i || ihgt[i] == ihgt[i2] || (mark[i2] && i2 < i)) continue;
                cand.type = M4; cand.a = i; cand.b = i2;
                build_lists(&cand);
                int d = eval_lists();
                if (is_tabu(&cand, it) && cost + d >= dbest) continue;
                if (d < bestd) { bestd = d; bestm = cand; nties = 1; }
                else if (d == bestd && rndint(++nties) == 0) bestm = cand;
            }
        }
        if (nties == 0) random_move(&bestm);
        commit(&bestm, it, tl, tr);
        if (cost < dbest) { dbest = cost; last_impr = it; }
        if (cost < gbest) gbest = cost;
        if (it - last_impr > stall) {
            for (int k = 0; k < pert; k++) { random_move(&cand); commit(&cand, it, tl, tr); }
            dbest = cost; last_impr = it;
        }
        if ((it & 255) == 0) {
            double tn = now();
            if (tn - t0 > secs) {
                printf("TIMEOUT it=%lld t=%.1f gbest=%d cost=%d\n", it, tn - t0, gbest, cost);
                char path[1024];
                snprintf(path, sizeof path, "%s.best", pre);
                FILE *f = xopen(path);
                fprintf(f, "best cost %d (state at exit has cost %d; not a witness)\n", gbest, cost);
                fclose(f);
                return 3;
            }
            if (tn - tlast > 60) {
                printf("progress it=%lld t=%.0f cost=%d gbest=%d it/s=%.0f\n", it, tn - t0, cost, gbest, it / (tn - t0));
                fflush(stdout);
                tlast = tn;
            }
        }
    }
}
