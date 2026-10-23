/* btd_cnf_b.c -- CNF encoding B of BTD(V,B;p1,p2,R;K,L) (lane btd12-15, README 1.6 item B).
 * Written independently of code/btd_cnf_a.py (no shared code, different variables and counting circuits).
 *
 * Variables: one-hot z[i][j][v], v in {0,1,2}: (z0 | z1 | z2) and pairwise (-zu | -zw).
 * Counting: Bailleux-Boufkhad totalizers over literal multisets (an input literal may occur several times; each
 * occurrence counts once), unary outputs truncated at cap = bound + 1, defined in both directions:
 *     a_x & b_y -> r_{min(x+y,cap)}            (x, y >= 0, x + y >= 1; a_0 = b_0 = true)
 *     -a_{x+1} & -b_{y+1} -> -r_{x+y+1}         (x + y + 1 <= cap; a_{p+1} = b_{q+1} = false)
 *   "exactly k": r_k (k >= 1) and -r_{k+1} (when k + 1 <= number of inputs).
 *   (D2) row i: exactly p1 of {z1_ij}, exactly p2 of {z2_ij};
 *   (D3) column j: exactly K of the multiset {z1_ij, z2_ij, z2_ij : i}   (value = number of occurrences true);
 *   (D4) rows i < k: exactly L of the multiset over j of {q11 x1, q12 x2, q21 x2, q22 x4}, q_uw = z_u,ij & z_w,kj
 *        (full AND definitions), so the count is sum_j m_ij m_kj.
 * Symmetry (S1, README 1.3): rows and columns lexicographically nondecreasing over the values 0 < 1 < 2, encoded on
 *   the one-hot values: prefix-equality variables e_t (e_0 = true), e_t -> not(X_t > Y_t) as three clauses,
 *   e_{t+1} <-> e_t & OR_v (zX_v & zY_v).  Row 0 = 0^z 1^p1 2^p2 as unit clauses (S0, implied by S1).
 *   Options: -nosym (no S0, no S1), -s0 (S0 only).
 * -strengthen (target parameters only): (C1) at most two 2s per column via a totalizer with cap 3.
 * -fix FILE [-flip i j v]: unit clauses fixing all cells to the matrix in FILE (strict format).
 * Usage: btd_cnf_b V B p1 p2 R K L OUT.cnf [options]       writes OUT.cnf and OUT.cnf.map.json (both exclusive)
 */
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

static int nv;
static long ncl, capcl;
static int *lits;            /* flat clause storage, 0-terminated */
static long nlits, caplits;

static void push_lit(int l) {
    if (nlits == caplits) { caplits = caplits ? 2 * caplits : 1 << 20; lits = realloc(lits, caplits * sizeof(int)); if (!lits) exit(3); }
    lits[nlits++] = l;
}
static void clause(int n, const int *c) { for (int t = 0; t < n; t++) push_lit(c[t]); push_lit(0); ncl++; }
static void c1(int a) { int c[1] = {a}; clause(1, c); }
static void c2(int a, int b) { int c[2] = {a, b}; clause(2, c); }
static void c3(int a, int b, int d) { int c[3] = {a, b, d}; clause(3, c); }
static void c4(int a, int b, int d, int e) { int c[4] = {a, b, d, e}; clause(4, c); }
static int fresh(void) { return ++nv; }

static int AND2(int x, int y) { int p = fresh(); c2(-p, x); c2(-p, y); c3(p, -x, -y); return p; }

/* totalizer: returns number of outputs m (<= cap) and fills out[1..m] */
static int tot(const int *in, int n, int cap, int *out) {
    if (n == 1) { out[1] = in[0]; return 1; }
    int h = n / 2;
    int *A = malloc((cap + 2) * sizeof(int)), *Bv = malloc((cap + 2) * sizeof(int));
    int p = tot(in, h, cap, A), q = tot(in + h, n - h, cap, Bv);
    int m = p + q < cap ? p + q : cap;
    for (int r = 1; r <= m; r++) out[r] = fresh();
    for (int x = 0; x <= p; x++)
        for (int y = 0; y <= q; y++) {
            if (x + y >= 1) {
                int s = x + y < m ? x + y : m;
                int c[3], k = 0;
                if (x) c[k++] = -A[x];
                if (y) c[k++] = -Bv[y];
                c[k++] = out[s];
                clause(k, c);
            }
            if (x + y + 1 <= m) {
                int c[3], k = 0;
                if (x + 1 <= p) c[k++] = A[x + 1];
                if (y + 1 <= q) c[k++] = Bv[y + 1];
                c[k++] = -out[x + y + 1];
                clause(k, c);
            }
        }
    free(A); free(Bv);
    return m;
}

static void exactly(const int *in, int n, int k) {
    if (k > n) { clause(0, NULL); return; }
    if (n == 0) return;
    int cap = k + 1;
    int *out = malloc((cap + 2) * sizeof(int));
    int m = tot(in, n, cap, out);
    if (k >= 1) c1(out[k]);
    if (k + 1 <= m) c1(-out[k + 1]);
    free(out);
}

static void atmost(const int *in, int n, int k) {
    if (k >= n) return;
    int cap = k + 1;
    int *out = malloc((cap + 2) * sizeof(int));
    int m = tot(in, n, cap, out);
    if (k + 1 <= m) c1(-out[k + 1]);
    free(out);
}

/* X, Y: arrays of len one-hot triples (pointers to 3 ints each) */
static void lexleq(int len, int (*X)[3], int (*Y)[3]) {
    int e = 0; /* 0 = constant true */
    for (int t = 0; t < len; t++) {
        int bad[3][2] = {{1, 0}, {2, 0}, {2, 1}};
        for (int b = 0; b < 3; b++) {
            if (e) c3(-e, -X[t][bad[b][0]], -Y[t][bad[b][1]]);
            else c2(-X[t][bad[b][0]], -Y[t][bad[b][1]]);
        }
        if (t == len - 1) break;
        int f = fresh();
        if (e) c2(-f, e);
        for (int v = 0; v < 3; v++) {
            c3(-f, -X[t][v], Y[t][v]);
            c3(-f, X[t][v], -Y[t][v]);
            if (e) c4(-e, -X[t][v], -Y[t][v], f);
            else c3(-X[t][v], -Y[t][v], f);
        }
        e = f;
    }
}

static int read_fix(const char *path, int V, int B, long P[7], int M[64][64]) {
    FILE *f = fopen(path, "r");
    if (!f) return 0;
    long h[7];
    if (fscanf(f, "BTD %ld %ld %ld %ld %ld %ld %ld", &h[0], &h[1], &h[2], &h[3], &h[4], &h[5], &h[6]) != 7) return 0;
    for (int t = 0; t < 7; t++) if (h[t] != P[t]) return 0;
    for (int i = 0; i < V; i++) for (int j = 0; j < B; j++) if (fscanf(f, "%d", &M[i][j]) != 1) return 0;
    fclose(f);
    return 1;
}

int main(int argc, char **argv) {
    if (argc < 9) { fprintf(stderr, "usage: btd_cnf_b V B p1 p2 R K L OUT.cnf [-nosym|-s0] [-strengthen] [-fix FILE [-flip i j v]]\n"); return 2; }
    long P[7];
    for (int t = 0; t < 7; t++) P[t] = atol(argv[1 + t]);
    int V = (int)P[0], B = (int)P[1], p1 = (int)P[2], p2 = (int)P[3], R = (int)P[4], K = (int)P[5], L = (int)P[6];
    const char *out = argv[8];
    int sym = 2, strengthen = 0, fi = -1, fj = -1, fv = -1;
    const char *fix = NULL;
    for (int a = 9; a < argc; a++) {
        if (!strcmp(argv[a], "-nosym")) sym = 0;
        else if (!strcmp(argv[a], "-s0")) sym = 1;
        else if (!strcmp(argv[a], "-strengthen")) strengthen = 1;
        else if (!strcmp(argv[a], "-fix") && a + 1 < argc) fix = argv[++a];
        else if (!strcmp(argv[a], "-flip") && a + 3 < argc) { fi = atoi(argv[++a]); fj = atoi(argv[++a]); fv = atoi(argv[++a]); }
        else { fprintf(stderr, "bad option %s\n", argv[a]); return 2; }
    }
    if (V < 1 || B < 1 || V > 64 || B > 64 || R != p1 + 2 * p2) { fprintf(stderr, "bad parameters\n"); return 2; }
    if (strengthen && !(V == 12 && B == 15 && p1 == 6 && p2 == 2 && R == 10 && K == 8 && L == 6)) {
        fprintf(stderr, "-strengthen is proved only for the target parameters\n"); return 2;
    }
    static int z[64][64][3];
    for (int i = 0; i < V; i++) for (int j = 0; j < B; j++) for (int v = 0; v < 3; v++) z[i][j][v] = fresh();
    for (int i = 0; i < V; i++) for (int j = 0; j < B; j++) {
        c3(z[i][j][0], z[i][j][1], z[i][j][2]);
        c2(-z[i][j][0], -z[i][j][1]); c2(-z[i][j][0], -z[i][j][2]); c2(-z[i][j][1], -z[i][j][2]);
    }
    int *buf = malloc(sizeof(int) * 64 * 64 * 9);
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < B; j++) buf[j] = z[i][j][1];
        exactly(buf, B, p1);
        for (int j = 0; j < B; j++) buf[j] = z[i][j][2];
        exactly(buf, B, p2);
    }
    for (int j = 0; j < B; j++) {
        int n = 0;
        for (int i = 0; i < V; i++) { buf[n++] = z[i][j][1]; buf[n++] = z[i][j][2]; buf[n++] = z[i][j][2]; }
        exactly(buf, n, K);
    }
    for (int i = 0; i < V; i++)
        for (int k = i + 1; k < V; k++) {
            int n = 0;
            for (int j = 0; j < B; j++)
                for (int u = 1; u <= 2; u++)
                    for (int w = 1; w <= 2; w++) {
                        int q = AND2(z[i][j][u], z[k][j][w]);
                        for (int rep = 0; rep < u * w; rep++) buf[n++] = q;
                    }
            exactly(buf, n, L);
        }
    if (sym >= 1) {
        int zc = B - p1 - p2;
        for (int j = 0; j < B; j++) { int v = j < zc ? 0 : (j < zc + p1 ? 1 : 2); c1(z[0][j][v]); }
    }
    if (sym == 2) {
        static int X[64][3], Y[64][3];
        for (int i = 0; i + 1 < V; i++) {
            for (int j = 0; j < B; j++) for (int v = 0; v < 3; v++) { X[j][v] = z[i][j][v]; Y[j][v] = z[i + 1][j][v]; }
            lexleq(B, X, Y);
        }
        for (int j = 0; j + 1 < B; j++) {
            for (int i = 0; i < V; i++) for (int v = 0; v < 3; v++) { X[i][v] = z[i][j][v]; Y[i][v] = z[i][j + 1][v]; }
            lexleq(V, X, Y);
        }
    }
    if (strengthen)
        for (int j = 0; j < B; j++) {
            for (int i = 0; i < V; i++) buf[i] = z[i][j][2];
            atmost(buf, V, 2);
        }
    if (fix) {
        static int M[64][64];
        if (!read_fix(fix, V, B, P, M)) { fprintf(stderr, "cannot read fix file\n"); return 2; }
        if (fi >= 0) M[fi][fj] = fv;
        for (int i = 0; i < V; i++) for (int j = 0; j < B; j++) c1(z[i][j][M[i][j]]);
    }
    int fd = open(out, O_WRONLY | O_CREAT | O_EXCL, 0644);
    if (fd < 0) { perror(out); return 2; }
    FILE *f = fdopen(fd, "w");
    fprintf(f, "c btd_cnf_b params %d %d %d %d %d %d %d sym %d strengthen %d fix %s flip %d %d %d\n", V, B, p1, p2, R, K, L,
            sym, strengthen, fix ? fix : "-", fi, fj, fv);
    fprintf(f, "p cnf %d %ld\n", nv, ncl);
    for (long t = 0; t < nlits; t++) fprintf(f, lits[t] ? "%d " : "0\n", lits[t]);
    fclose(f);
    char mpath[4096];
    snprintf(mpath, sizeof mpath, "%s.map.json", out);
    fd = open(mpath, O_WRONLY | O_CREAT | O_EXCL, 0644);
    if (fd < 0) { perror(mpath); return 2; }
    f = fdopen(fd, "w");
    fprintf(f, "{\"generator\": \"btd_cnf_b\", \"params\": [%d, %d, %d, %d, %d, %d, %d], \"symmetry\": \"%s\", \"strengthen\": %s, \"fix\": \"%s\", ",
            V, B, p1, p2, R, K, L, sym == 2 ? "S1" : sym == 1 ? "S0" : "none", strengthen ? "true" : "false", fix ? fix : "");
    for (int v = 1; v <= 2; v++) {
        fprintf(f, "\"z%d\": [", v);
        for (int i = 0; i < V; i++) {
            fprintf(f, "%s[", i ? ", " : "");
            for (int j = 0; j < B; j++) fprintf(f, "%s%d", j ? ", " : "", z[i][j][v]);
            fprintf(f, "]");
        }
        fprintf(f, "], ");
    }
    fprintf(f, "\"vars\": %d, \"clauses\": %ld}\n", nv, ncl);
    fclose(f);
    printf("%s: vars %d clauses %ld sym %d strengthen %d\n", out, nv, ncl, sym, strengthen);
    return 0;
}
