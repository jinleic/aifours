/* btd_ls.c -- heuristic local search for a witness BTD(V,B;p1,p2,R;K,L) (README amendment A3).  A miss proves
 * nothing.  State: a V x B matrix whose rows always have exactly p1 ones and p2 twos.  Move: swap two different
 * entries inside one row.  Cost: sum_j (colsum_j - K)^2 + sum_{i<k} (row_i . row_k - L)^2.  Acceptance: simulated
 * annealing with a fixed geometric schedule restarted every `restart` iterations from the best state with a small
 * random perturbation; native iteration limit and wall-time limit (no external kill).  On cost 0 the matrix is
 * written in strict format to OUT (exclusive create) and the program exits 10; otherwise exits 0.
 * Usage: btd_ls V B p1 p2 R K L SEED MAX_SECONDS OUT
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <fcntl.h>
#include <unistd.h>

#define MAXV 32
#define MAXB 64
static int V, B, p1, p2, R, K, L;
static int M[MAXV][MAXB], cs[MAXB], ip[MAXV][MAXV];
static unsigned long long rs;
static unsigned long long rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static double urand(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }

static long cost_all(void) {
    long c = 0;
    for (int j = 0; j < B; j++) { long d = cs[j] - K; c += d * d; }
    for (int i = 0; i < V; i++) for (int k = i + 1; k < V; k++) { long d = ip[i][k] - L; c += d * d; }
    return c;
}
static void recompute(void) {
    for (int j = 0; j < B; j++) { cs[j] = 0; for (int i = 0; i < V; i++) cs[j] += M[i][j]; }
    for (int i = 0; i < V; i++) for (int k = 0; k < V; k++) {
        int s = 0; for (int j = 0; j < B; j++) s += M[i][j] * M[k][j]; ip[i][k] = s; }
}
/* cost change of swapping M[i][a] and M[i][b] (values differ) */
static long delta(int i, int a, int b) {
    int va = M[i][a], vb = M[i][b], dv = vb - va;  /* column a gains dv, column b loses dv */
    long d = 0;
    long ca = cs[a] - K, cb = cs[b] - K;
    d += (ca + dv) * (ca + dv) - ca * ca + (cb - dv) * (cb - dv) - cb * cb;
    for (int k = 0; k < V; k++) if (k != i) {
        long e = ip[i][k] - L;
        long ch = (long)dv * M[k][a] - (long)dv * M[k][b];
        d += (e + ch) * (e + ch) - e * e;
    }
    return d;
}
static void apply(int i, int a, int b) {
    int va = M[i][a], vb = M[i][b], dv = vb - va;
    cs[a] += dv; cs[b] -= dv;
    for (int k = 0; k < V; k++) if (k != i) {
        int ch = dv * M[k][a] - dv * M[k][b];
        ip[i][k] += ch; ip[k][i] += ch;
    }
    M[i][a] = vb; M[i][b] = va;
}

int main(int argc, char **argv) {
    if (argc != 11) { fprintf(stderr, "usage: btd_ls V B p1 p2 R K L SEED MAX_SECONDS OUT\n"); return 2; }
    V = atoi(argv[1]); B = atoi(argv[2]); p1 = atoi(argv[3]); p2 = atoi(argv[4]); R = atoi(argv[5]);
    K = atoi(argv[6]); L = atoi(argv[7]);
    rs = strtoull(argv[8], 0, 10) * 2654435761ULL + 88172645463325252ULL;
    double maxs = atof(argv[9]);
    const char *out = argv[10];
    if (V > MAXV || B > MAXB || R != p1 + 2 * p2 || p1 + p2 > B) { fprintf(stderr, "bad parameters\n"); return 2; }
    for (int i = 0; i < V; i++) {
        int row[MAXB];
        for (int j = 0; j < B; j++) row[j] = j < p1 ? 1 : (j < p1 + p2 ? 2 : 0);
        for (int j = B - 1; j > 0; j--) { int t = rnd() % (j + 1); int x = row[j]; row[j] = row[t]; row[t] = x; }
        for (int j = 0; j < B; j++) M[i][j] = row[j];
    }
    recompute();
    long cur = cost_all(), best = cur;
    static int BM[MAXV][MAXB];
    memcpy(BM, M, sizeof M);
    clock_t t0 = clock();
    double T0 = 4.0, T1 = 0.05;
    long restart = 4000000, it = 0, phase_it = 0;
    double T = T0, alpha = pow(T1 / T0, 1.0 / restart);
    long restarts = 0;
    while (1) {
        if ((it & 0xFFFF) == 0) {
            double el = (double)(clock() - t0) / CLOCKS_PER_SEC;
            if (el > maxs) break;
        }
        it++; phase_it++;
        int i = rnd() % V, a = rnd() % B, b = rnd() % B;
        if (M[i][a] == M[i][b]) continue;
        long d = delta(i, a, b);
        if (d <= 0 || urand() < exp(-d / T)) {
            apply(i, a, b);
            cur += d;
            if (cur < best) { best = cur; memcpy(BM, M, sizeof M); if (best == 0) break; }
        }
        T *= alpha;
        if (phase_it >= restart) {
            memcpy(M, BM, sizeof M);
            for (int q = 0; q < 6; q++) {  /* perturb */
                int ii = rnd() % V, aa = rnd() % B, bb = rnd() % B;
                if (M[ii][aa] != M[ii][bb]) { int x = M[ii][aa]; M[ii][aa] = M[ii][bb]; M[ii][bb] = x; }
            }
            recompute(); cur = cost_all(); T = T0; phase_it = 0; restarts++;
        }
    }
    double el = (double)(clock() - t0) / CLOCKS_PER_SEC;
    printf("{\"best_cost\": %ld, \"iterations\": %ld, \"restarts\": %ld, \"cpu_s\": %.1f}\n", best, it, restarts, el);
    if (best == 0) {
        int fd = open(out, O_WRONLY | O_CREAT | O_EXCL, 0644);
        if (fd < 0) { perror("open"); return 3; }
        FILE *f = fdopen(fd, "w");
        fprintf(f, "BTD %d %d %d %d %d %d %d\n", V, B, p1, p2, R, K, L);
        for (int ii = 0; ii < V; ii++) for (int j = 0; j < B; j++) fprintf(f, "%d%c", BM[ii][j], j + 1 < B ? ' ' : '\n');
        fclose(f);
        return 10;
    }
    return 0;
}
