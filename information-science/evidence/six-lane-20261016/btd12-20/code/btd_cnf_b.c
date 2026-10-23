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

/* ---- implied constraints (README amendment 1.8; notes/nonexistence-proof.md), target parameters only ----------
 * Written for encoding B independently of btd_cnf_a.py's add_lemmas.  Column-pair inner products g_jk are counted
 * by a totalizer over the multiset {q11 x1, q12 x2, q21 x2, q22 x4 : rows}, q_uw = z_u,ij & z_w,ik, with cap 8, so
 * that out[c] <-> g_jk >= c exactly for c = 1..7.  Column type: totalizer over {z2_ij : i} with cap 3:
 * d_j = out[2] (two 2s; at most two by -strengthen), o_j = out[1] & -out[2] (exactly one 2).
 * Level 2: (C3) d_j & d_k -> g in [4,5]; (C4) d_j & o_k -> g >= 4; Step 4: d_j -> every k != j has g in [3,6] and
 * (#g=3, #g=4, #g=6) in {(0,4,2), (1,1,1)}; Step 5: d_j & d_k & g_jk < 5 -> [g_jl >= c] = [g_kl >= c], c = 1..7.
 * Level 3: Lemma D: not (d_j & d_k & d_l & g_jk >= 5 & g_jl >= 5 & g_kl >= 5). */
static int GG[64][64][10];
static int ggl(int j, int k, int c) { return j < k ? GG[j][k][c] : GG[k][j][c]; }

static void lemma_part(int V, int B, int level, int z[64][64][3]) {
    int d[64], o[64], out[16];
    int *in = malloc(sizeof(int) * 2048);
    for (int j = 0; j < B; j++) {
        for (int i = 0; i < V; i++) in[i] = z[i][j][2];
        tot(in, V, 3, out);
        d[j] = out[2];
        o[j] = AND2(out[1], -out[2]);
    }
    for (int j = 0; j < B; j++)
        for (int k = j + 1; k < B; k++) {
            int n = 0;
            for (int i = 0; i < V; i++)
                for (int u = 1; u <= 2; u++)
                    for (int w = 1; w <= 2; w++) {
                        int q = AND2(z[i][j][u], z[i][k][w]);
                        for (int rep = 0; rep < u * w; rep++) in[n++] = q;
                    }
            int m = tot(in, n, 8, GG[j][k]);
            if (m < 8) { fprintf(stderr, "internal: pair counter too small\n"); exit(3); }
        }
    for (int j = 0; j < B; j++)
        for (int k = j + 1; k < B; k++) {
            c3(-d[j], -d[k], ggl(j, k, 4));
            c3(-d[j], -d[k], -ggl(j, k, 6));
        }
    for (int j = 0; j < B; j++)
        for (int k = 0; k < B; k++)
            if (j != k) c3(-d[j], -o[k], ggl(j, k, 4));
    for (int j = 0; j < B; j++) {
        int e3[64], e4[64], e6[64], n = 0;
        for (int k = 0; k < B; k++) {
            if (k == j) continue;
            c2(-d[j], ggl(j, k, 3));
            c2(-d[j], -ggl(j, k, 7));
            e3[n] = AND2(ggl(j, k, 3), -ggl(j, k, 4));
            e4[n] = AND2(ggl(j, k, 4), -ggl(j, k, 5));
            e6[n] = AND2(ggl(j, k, 6), -ggl(j, k, 7));
            n++;
        }
        int o3[8], o4[8], o6[8];
        tot(e3, n, 2, o3);
        tot(e4, n, 5, o4);
        tot(e6, n, 3, o6);
        int s = o3[1];
        c2(-d[j], -o3[2]);
        c3(-d[j], s, o4[4]); c3(-d[j], s, -o4[5]); c3(-d[j], s, o6[2]); c3(-d[j], s, -o6[3]);
        c3(-d[j], -s, o4[1]); c3(-d[j], -s, -o4[2]); c3(-d[j], -s, o6[1]); c3(-d[j], -s, -o6[2]);
    }
    for (int j = 0; j < B; j++)
        for (int k = j + 1; k < B; k++)
            for (int l = 0; l < B; l++) {
                if (l == j || l == k) continue;
                for (int c = 1; c <= 7; c++) {
                    int a1[5] = {-d[j], -d[k], ggl(j, k, 5), -ggl(j, l, c), ggl(k, l, c)};
                    int a2[5] = {-d[j], -d[k], ggl(j, k, 5), -ggl(k, l, c), ggl(j, l, c)};
                    clause(5, a1);
                    clause(5, a2);
                }
            }
    if (level >= 3)
        for (int j = 0; j < B; j++)
            for (int k = j + 1; k < B; k++)
                for (int l = k + 1; l < B; l++) {
                    int a[6] = {-d[j], -d[k], -d[l], -ggl(j, k, 5), -ggl(j, l, 5), -ggl(k, l, 5)};
                    clause(6, a);
                }
    free(in);
}

int main(int argc, char **argv) {
    if (argc < 9) { fprintf(stderr, "usage: btd_cnf_b V B p1 p2 R K L OUT.cnf [-nosym|-s0] [-strengthen] [-fix FILE [-flip i j v]]\n"); return 2; }
    long P[7];
    for (int t = 0; t < 7; t++) P[t] = atol(argv[1 + t]);
    int V = (int)P[0], B = (int)P[1], p1 = (int)P[2], p2 = (int)P[3], R = (int)P[4], K = (int)P[5], L = (int)P[6];
    const char *out = argv[8];
    int sym = 2, strengthen = 0, fi = -1, fj = -1, fv = -1, lemmas = 0, lemmatest = 0;
    const char *fix = NULL;
    for (int a = 9; a < argc; a++) {
        if (!strcmp(argv[a], "-nosym")) sym = 0;
        else if (!strcmp(argv[a], "-s0")) sym = 1;
        else if (!strcmp(argv[a], "-strengthen")) strengthen = 1;
        else if (!strcmp(argv[a], "-lemmas") && a + 1 < argc) {
            lemmas = atoi(argv[++a]);
            strengthen = 1;
            if (lemmas != 2 && lemmas != 3) { fprintf(stderr, "-lemmas must be 2 or 3\n"); return 2; }
        }
        else if (!strcmp(argv[a], "-lemmatest")) { lemmatest = 1; sym = 0; }
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
    for (int i = 0; i < V && !lemmatest; i++) {
        for (int j = 0; j < B; j++) buf[j] = z[i][j][1];
        exactly(buf, B, p1);
        for (int j = 0; j < B; j++) buf[j] = z[i][j][2];
        exactly(buf, B, p2);
    }
    for (int j = 0; j < B && !lemmatest; j++) {
        int n = 0;
        for (int i = 0; i < V; i++) { buf[n++] = z[i][j][1]; buf[n++] = z[i][j][2]; buf[n++] = z[i][j][2]; }
        exactly(buf, n, K);
    }
    for (int i = 0; i < V && !lemmatest; i++)
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
    if (lemmas) lemma_part(V, B, lemmas, z);
    if (fix) {
        static int M[64][64];
        if (!read_fix(fix, V, B, P, M)) { fprintf(stderr, "cannot read fix file\n"); return 2; }
        if (fi >= 0) M[fi][fj] = fv;
        for (int i = 0; i < V; i++) for (int j = 0; j < B; j++) c1(z[i][j][M[i][j]]);
    }
    int fd = open(out, O_WRONLY | O_CREAT | O_EXCL, 0644);
    if (fd < 0) { perror(out); return 2; }
    FILE *f = fdopen(fd, "w");
    fprintf(f, "c btd_cnf_b params %d %d %d %d %d %d %d sym %d strengthen %d lemmas %d lemmatest %d fix %s flip %d %d %d\n",
            V, B, p1, p2, R, K, L, sym, strengthen, lemmas, lemmatest, fix ? fix : "-", fi, fj, fv);
    fprintf(f, "p cnf %d %ld\n", nv, ncl);
    for (long t = 0; t < nlits; t++) fprintf(f, lits[t] ? "%d " : "0\n", lits[t]);
    fclose(f);
    char mpath[4096];
    snprintf(mpath, sizeof mpath, "%s.map.json", out);
    fd = open(mpath, O_WRONLY | O_CREAT | O_EXCL, 0644);
    if (fd < 0) { perror(mpath); return 2; }
    f = fdopen(fd, "w");
    fprintf(f, "{\"generator\": \"btd_cnf_b\", \"params\": [%d, %d, %d, %d, %d, %d, %d], \"symmetry\": \"%s\", \"strengthen\": %s, "
               "\"lemmas\": %d, \"lemmatest\": %d, \"fix\": \"%s\", ",
            V, B, p1, p2, R, K, L, sym == 2 ? "S1" : sym == 1 ? "S0" : "none", strengthen ? "true" : "false", lemmas, lemmatest,
            fix ? fix : "");
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
    printf("%s: vars %d clauses %ld sym %d strengthen %d lemmas %d lemmatest %d\n", out, nv, ncl, sym, strengthen, lemmas, lemmatest);
    return 0;
}
