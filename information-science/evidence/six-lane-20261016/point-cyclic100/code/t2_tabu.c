/* t2_tabu.c -- representation R1 of the point-cyclic100 lane README (Section 1.4).
 *
 * Tabu search for eight (in general a + c) base blocks satisfying (S1)-(S3) of REDUCTION.md, for v = 4q with q odd,
 * q = 1 (mod 12): a = (q-1)/4 blocks X_i whose residue sets mod q partition Z_q \ {0}, and c = (q-1)/12 blocks Y_j
 * meeting every residue class mod 4 once.  Points are handled in CRT coordinates Z_v = Z_4 x Z_q,
 * x <-> (x mod 4, x mod q) ("height", "residue").
 *
 * State: lab[r], ht[r] for r = 1..q-1 (X-block label, height); every label is used by exactly 4 residues, so (S2)
 * holds by construction.  ys[j][i] = residue of the point of Y_j at height i (pairwise distinct), so (S3) holds by
 * construction.  Each unordered pair of a block yields the +-class {d, -d} of its difference d in
 * Z_4 x (Z_q \ {0}) (residues inside a block are distinct, and d != -d because q is odd); there are 2(q-1) classes
 * and 2(q-1) pairs.  Cost = sum_classes max(0, count - 1); cost 0 <=> every class exactly once <=> (S1).
 *
 * Moves: M1 height change of one X element; M2a swap two residues of different X blocks (heights travel);
 * M2b the same swap with heights staying in their slots; M3 change one residue of a Y block; M4 swap two residues
 * inside a Y block.  Best non-tabu move (reservoir tie-break), aspiration if it beats the descent's best cost,
 * random perturbation after `stall` non-improving iterations.  Deterministic per seed (splitmix64); the wall clock
 * is used only for the time limit and progress lines.
 *
 * Usage: t2_tabu q seed seconds outprefix [tl tr stall pert maxsol]
 * Output: outprefix.seed (first solution; further solutions outprefix.seed2, ... up to maxsol, default 1) in the
 * strict PC-T2-SEED format of README 1.3; outprefix.best (best state, written on exit without a solution).
 * Exit 0 found, 3 time limit, 2 usage/internal error.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

#define MAXQ 64
#define MAXA (MAXQ / 4 + 1)
#define MAXC (MAXQ / 12 + 1)

static int q, v, A, C, HALF, NC;
static int lab[MAXQ], ht[MAXQ], mem[MAXA][4];
static int ys[MAXC][4];
static int cnt[4 * MAXQ];
static int cost;
static long long tabu_h[MAXQ][4], tabu_b[MAXQ][MAXA], tabu_y[MAXC][4][MAXQ];
static uint64_t rng;

static uint64_t rnd(void) {
    uint64_t z = (rng += 0x9E3779B97F4A7C15ULL);
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
    z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
    return z ^ (z >> 31);
}
static int rndint(int n) { return (int)(rnd() % (uint64_t)n); }
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }

/* +-class of the difference (h1,r1) - (h2,r2); requires r1 != r2 (mod q) */
static inline int cls(int h1, int r1, int h2, int r2) {
    int dh = (h1 - h2) & 3, dr = r1 - r2;
    if (dr < 0) dr += q;
    if (dr <= HALF) return dh * HALF + dr - 1;
    return ((4 - dh) & 3) * HALF + (q - dr) - 1;
}
static inline int inc(int d) { int c0 = cnt[d]++; return c0 >= 1 ? 1 : 0; }
static inline int dec(int d) { int c1 = --cnt[d]; return c1 >= 1 ? -1 : 0; }

static void full_recount(void) {
    memset(cnt, 0, sizeof cnt);
    cost = 0;
    for (int b = 0; b < A; b++)
        for (int s = 0; s < 4; s++)
            for (int t = s + 1; t < 4; t++) {
                int r1 = mem[b][s], r2 = mem[b][t];
                cost += inc(cls(ht[r1], r1, ht[r2], r2));
            }
    for (int j = 0; j < C; j++)
        for (int s = 0; s < 4; s++)
            for (int t = s + 1; t < 4; t++) cost += inc(cls(s, ys[j][s], t, ys[j][t]));
}

/* pair lists for a move: classes removed / added */
static int nrem, nadd, rem[16], add[16];
static int eval_lists(void) {             /* delta, counts restored afterwards */
    int d = 0;
    for (int i = 0; i < nrem; i++) d += dec(rem[i]);
    for (int i = 0; i < nadd; i++) d += inc(add[i]);
    for (int i = 0; i < nadd; i++) cnt[add[i]]--;
    for (int i = 0; i < nrem; i++) cnt[rem[i]]++;
    return d;
}
static void apply_lists(void) {
    for (int i = 0; i < nrem; i++) cost += dec(rem[i]);
    for (int i = 0; i < nadd; i++) cost += inc(add[i]);
}

/* move descriptors */
enum { M1, M2A, M2B, M3, M4 };
typedef struct { int type, p1, p2, p3; } Move;

static void build_lists(const Move *m) {
    nrem = nadd = 0;
    if (m->type == M1) {
        int r = m->p1, h2 = m->p2, b = lab[r];
        for (int t = 0; t < 4; t++) {
            int x = mem[b][t];
            if (x == r) continue;
            rem[nrem++] = cls(ht[r], r, ht[x], x);
            add[nadd++] = cls(h2, r, ht[x], x);
        }
    } else if (m->type == M2A || m->type == M2B) {
        int r = m->p1, r2 = m->p2, b = lab[r], b2 = lab[r2];
        int hr = ht[r], hr2 = ht[r2];
        int nhr = (m->type == M2A) ? hr : hr2, nhr2 = (m->type == M2A) ? hr2 : hr;
        for (int t = 0; t < 4; t++) {
            int x = mem[b][t];
            if (x == r) continue;
            rem[nrem++] = cls(hr, r, ht[x], x);
            add[nadd++] = cls(nhr2, r2, ht[x], x);
        }
        for (int t = 0; t < 4; t++) {
            int y = mem[b2][t];
            if (y == r2) continue;
            rem[nrem++] = cls(hr2, r2, ht[y], y);
            add[nadd++] = cls(nhr, r, ht[y], y);
        }
    } else if (m->type == M3) {
        int j = m->p1, i = m->p2, s2 = m->p3;
        for (int t = 0; t < 4; t++) {
            if (t == i) continue;
            rem[nrem++] = cls(i, ys[j][i], t, ys[j][t]);
            add[nadd++] = cls(i, s2, t, ys[j][t]);
        }
    } else { /* M4 */
        int j = m->p1, i = m->p2, i2 = m->p3;
        int nv[4];
        for (int t = 0; t < 4; t++) nv[t] = ys[j][t];
        nv[i] = ys[j][i2]; nv[i2] = ys[j][i];
        for (int s = 0; s < 4; s++)
            for (int t = s + 1; t < 4; t++) {
                if (s != i && s != i2 && t != i && t != i2) continue;
                rem[nrem++] = cls(s, ys[j][s], t, ys[j][t]);
                add[nadd++] = cls(s, nv[s], t, nv[t]);
            }
    }
}

static int in_y(int j, int s) { for (int t = 0; t < 4; t++) if (ys[j][t] == s) return 1; return 0; }

static void commit(const Move *m, long long it, int tl, int tr) {
    build_lists(m);
    apply_lists();
    long long until = it + tl + (tr > 0 ? rndint(tr) : 0);
    if (m->type == M1) {
        tabu_h[m->p1][ht[m->p1]] = until;
        ht[m->p1] = m->p2;
    } else if (m->type == M2A || m->type == M2B) {
        int r = m->p1, r2 = m->p2, b = lab[r], b2 = lab[r2];
        tabu_b[r][b] = until; tabu_b[r2][b2] = until;
        for (int t = 0; t < 4; t++) { if (mem[b][t] == r) mem[b][t] = r2; }
        for (int t = 0; t < 4; t++) { if (mem[b2][t] == r2) mem[b2][t] = r; }
        lab[r] = b2; lab[r2] = b;
        if (m->type == M2B) { int h = ht[r]; ht[r] = ht[r2]; ht[r2] = h; }
    } else if (m->type == M3) {
        tabu_y[m->p1][m->p2][ys[m->p1][m->p2]] = until;
        ys[m->p1][m->p2] = m->p3;
    } else {
        int j = m->p1, i = m->p2, i2 = m->p3;
        tabu_y[j][i][ys[j][i]] = until; tabu_y[j][i2][ys[j][i2]] = until;
        int s = ys[j][i]; ys[j][i] = ys[j][i2]; ys[j][i2] = s;
    }
}

static int is_tabu(const Move *m, long long it) {
    if (m->type == M1) return tabu_h[m->p1][m->p2] > it;
    if (m->type == M2A || m->type == M2B) {
        int r = m->p1, r2 = m->p2;
        return tabu_b[r][lab[r2]] > it || tabu_b[r2][lab[r]] > it;
    }
    if (m->type == M3) return tabu_y[m->p1][m->p2][m->p3] > it;
    {
        int j = m->p1, i = m->p2, i2 = m->p3;
        return tabu_y[j][i][ys[j][i2]] > it || tabu_y[j][i2][ys[j][i]] > it;
    }
}

static int crt(int h, int r) {   /* unique x in [0, v) with x = h (mod 4), x = r (mod q) */
    for (int t = 0; t < 4; t++) { int x = r + t * q; if ((x & 3) == h) return x; }
    return -1;
}
static int cmpint(const void *x, const void *y) { return *(const int *)x - *(const int *)y; }

static void write_seed(const char *path) {
    FILE *f = fopen(path, "w");
    if (!f) { perror(path); exit(2); }
    fprintf(f, "PC-T2-SEED %d\n", v);
    fprintf(f, "H 0 %d %d %d\n", q, 2 * q, 3 * q);
    int pts[4];
    for (int b = 0; b < A; b++) {
        for (int t = 0; t < 4; t++) pts[t] = crt(ht[mem[b][t]], mem[b][t]);
        qsort(pts, 4, sizeof(int), cmpint);
        fprintf(f, "X %d %d %d %d\n", pts[0], pts[1], pts[2], pts[3]);
    }
    for (int j = 0; j < C; j++) {
        for (int t = 0; t < 4; t++) pts[t] = crt(t, ys[j][t]);
        qsort(pts, 4, sizeof(int), cmpint);
        fprintf(f, "Y %d %d %d %d\n", pts[0], pts[1], pts[2], pts[3]);
    }
    fclose(f);
}

static void random_move(Move *m) {
    for (;;) {
        int t = rndint(C > 0 ? 4 : 3);
        if (t == 0) { m->type = M1; m->p1 = 1 + rndint(q - 1); m->p2 = rndint(4); if (m->p2 != ht[m->p1]) return; }
        else if (t == 1) {
            m->type = rndint(2) ? M2A : M2B; m->p1 = 1 + rndint(q - 1); m->p2 = 1 + rndint(q - 1);
            if (lab[m->p1] != lab[m->p2]) return;
        } else if (t == 2) {
            m->type = M1; m->p1 = 1 + rndint(q - 1); m->p2 = (ht[m->p1] + 1 + rndint(3)) & 3; return;
        } else {
            m->type = M3; m->p1 = rndint(C); m->p2 = rndint(4); m->p3 = rndint(q);
            if (!in_y(m->p1, m->p3)) return;
        }
    }
}

int main(int argc, char **argv) {
    if (argc < 5) {
        fprintf(stderr, "usage: t2_tabu q seed seconds outprefix [tl tr stall pert maxsol]\n");
        return 2;
    }
    q = atoi(argv[1]);
    uint64_t seed = strtoull(argv[2], 0, 10);
    double secs = atof(argv[3]);
    const char *pre = argv[4];
    int tl = argc > 5 ? atoi(argv[5]) : 8, tr = argc > 6 ? atoi(argv[6]) : 8;
    int stall = argc > 7 ? atoi(argv[7]) : 3000, pert = argc > 8 ? atoi(argv[8]) : 4;
    int maxsol = argc > 9 ? atoi(argv[9]) : 1;
    if (q < 13 || q >= MAXQ || q % 2 == 0 || q % 12 != 1) { fprintf(stderr, "q must be odd, = 1 mod 12, 13..63\n"); return 2; }
    v = 4 * q; A = (q - 1) / 4; C = (q - 1) / 12; HALF = (q - 1) / 2; NC = 4 * HALF;
    rng = seed * 0x2545F4914F6CDD1DULL + 12345;

    /* random initial state */
    int perm[MAXQ];
    for (int i = 0; i < q - 1; i++) perm[i] = i + 1;
    for (int i = q - 2; i > 0; i--) { int k = rndint(i + 1); int t = perm[i]; perm[i] = perm[k]; perm[k] = t; }
    for (int b = 0; b < A; b++)
        for (int t = 0; t < 4; t++) { int r = perm[4 * b + t]; mem[b][t] = r; lab[r] = b; ht[r] = rndint(4); }
    for (int j = 0; j < C; j++)
        for (int t = 0; t < 4; t++) {     /* residues pairwise distinct inside Y_j */
            int s, ok;
            do { ok = 1; s = rndint(q); for (int u = 0; u < t; u++) if (ys[j][u] == s) ok = 0; } while (!ok);
            ys[j][t] = s;
        }
    full_recount();

    double t0 = now(), tlast = t0;
    long long it = 0, last_impr = 0;
    int dbest = cost, gbest = cost, nsol = 0;
    Move cand, bestm;
    printf("start q=%d v=%d A=%d C=%d classes=%d seed=%llu cost=%d tl=%d tr=%d stall=%d pert=%d\n", q, v, A, C, NC,
           (unsigned long long)seed, cost, tl, tr, stall, pert);
    fflush(stdout);
    for (;;) {
        if (cost == 0) {
            int c0 = cost;
            full_recount();
            if (cost != 0 || c0 != 0) { fprintf(stderr, "internal: recount mismatch %d %d\n", c0, cost); return 2; }
            nsol++;
            char path[1024];
            if (nsol == 1) snprintf(path, sizeof path, "%s.seed", pre);
            else snprintf(path, sizeof path, "%s.seed%d", pre, nsol);
            write_seed(path);
            printf("FOUND %d it=%lld t=%.2f %s\n", nsol, it, now() - t0, path);
            fflush(stdout);
            if (nsol >= maxsol) return 0;
            for (int k = 0; k < 3 * pert; k++) { random_move(&cand); commit(&cand, it, tl, tr); }
            dbest = cost; last_impr = it;
        }
        it++;
        int bestd = 1 << 30, nties = 0;
        /* M1 */
        for (int r = 1; r < q; r++)
            for (int h = 0; h < 4; h++) {
                if (h == ht[r]) continue;
                cand.type = M1; cand.p1 = r; cand.p2 = h;
                build_lists(&cand);
                int d = eval_lists();
                if (is_tabu(&cand, it) && cost + d >= dbest) continue;
                if (d < bestd) { bestd = d; bestm = cand; nties = 1; }
                else if (d == bestd && rndint(++nties) == 0) bestm = cand;
            }
        /* M2a / M2b */
        for (int r = 1; r < q; r++)
            for (int r2 = r + 1; r2 < q; r2++) {
                if (lab[r] == lab[r2]) continue;
                for (int ty = M2A; ty <= M2B; ty++) {
                    if (ty == M2B && ht[r] == ht[r2]) continue;
                    cand.type = ty; cand.p1 = r; cand.p2 = r2;
                    build_lists(&cand);
                    int d = eval_lists();
                    if (is_tabu(&cand, it) && cost + d >= dbest) continue;
                    if (d < bestd) { bestd = d; bestm = cand; nties = 1; }
                    else if (d == bestd && rndint(++nties) == 0) bestm = cand;
                }
            }
        /* M3 / M4 */
        for (int j = 0; j < C; j++) {
            for (int i = 0; i < 4; i++)
                for (int s = 0; s < q; s++) {
                    if (in_y(j, s)) continue;
                    cand.type = M3; cand.p1 = j; cand.p2 = i; cand.p3 = s;
                    build_lists(&cand);
                    int d = eval_lists();
                    if (is_tabu(&cand, it) && cost + d >= dbest) continue;
                    if (d < bestd) { bestd = d; bestm = cand; nties = 1; }
                    else if (d == bestd && rndint(++nties) == 0) bestm = cand;
                }
            for (int i = 0; i < 4; i++)
                for (int i2 = i + 1; i2 < 4; i2++) {
                    cand.type = M4; cand.p1 = j; cand.p2 = i; cand.p3 = i2;
                    build_lists(&cand);
                    int d = eval_lists();
                    if (is_tabu(&cand, it) && cost + d >= dbest) continue;
                    if (d < bestd) { bestd = d; bestm = cand; nties = 1; }
                    else if (d == bestd && rndint(++nties) == 0) bestm = cand;
                }
        }
        if (nties == 0) { random_move(&bestm); }
        commit(&bestm, it, tl, tr);
        if (cost < dbest) { dbest = cost; last_impr = it; }
        if (cost < gbest) gbest = cost;
        if (it - last_impr > stall) {
            for (int k = 0; k < pert; k++) { random_move(&cand); commit(&cand, it, tl, tr); }
            dbest = cost; last_impr = it;
        }
        if ((it & 1023) == 0) {
            double tn = now();
            if (tn - t0 > secs) {
                printf("TIMEOUT it=%lld t=%.1f gbest=%d cost=%d\n", it, tn - t0, gbest, cost);
                char path[1024];
                snprintf(path, sizeof path, "%s.best", pre);
                FILE *f = fopen(path, "w");
                if (f) { fprintf(f, "best cost %d (state at exit has cost %d; not a witness)\n", gbest, cost); fclose(f); }
                return 3;
            }
            if (tn - tlast > 30) {
                printf("progress it=%lld t=%.0f cost=%d gbest=%d it/s=%.0f\n", it, tn - t0, cost, gbest, it / (tn - t0));
                fflush(stdout);
                tlast = tn;
            }
        }
    }
}
