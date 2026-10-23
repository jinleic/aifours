/* groups_enum_c21v1.c -- enumerate the UNTWISTED symmetry groups G <= Z_n^* x S_k (elements (mu, pi), action on DM
 * columns (s c)_i = mu c_{pi^-1(i)} modulo constants) up to conjugation by S_k (row relabelling), with |G| in [OMIN, OMAX]
 * and no "dead" element (sub-lane cfr21, worker InfoCFR27Lift; rules proved in notes/facts-c21-v1.md):
 *   E3  : pi has F >= 2 fixed rows and F > kmax(h), h = |Fix(mu)| = gcd(mu - 1, n), kmax(1) = kmax(n) = 99,
 *         kmax(9) = 3, kmax(h) = h otherwise (h prime or trivial bound);
 *   E3b : pi != id, F >= 2 and h^2 > n;
 *   G1  : mu = -1 and pi an involution (pi^2 = id != pi)   [valid for odd n with 3 | n and k >= 4; disable with 'nog1'].
 * Method: cyclic subgroups of all alive elements, then repeated extension <H, x> of every class representative H by every
 * alive x not in H (closure aborted as soon as it exceeds OMAX elements or meets a dead element). Raw subgroups are
 * deduplicated by their sorted element list; conjugacy classes by an invariant (order and multiset of (mu, cycle type))
 * plus an explicit conjugating-permutation test on generators. Every subgroup of order <= OMAX all of whose elements
 * are alive is reached (any such group is a chain of one-element extensions through subgroups of smaller order).
 * Usage: groups_enum_c21v1 N K OMIN OMAX OUTFILE [nog1]      (OUTFILE: JSON lines, written with O_EXCL; k <= 7)
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <fcntl.h>
#include <unistd.h>

#define MAXKP 7
#define MAXP 5040
#define MAXU 64
#define MAXORD 256

static int n, k, P, nu, omin, omax, use_g1 = 1;
static int units[MAXU], uidx[128], umul[MAXU][MAXU], uinvi[MAXU];
static uint8_t perms[MAXP][MAXKP];
static uint16_t *pcomp;            /* P x P */
static uint16_t pinv[MAXP];
static int E;                      /* nu * P */
static uint8_t *dead;
static int ctype_id[MAXP];         /* cycle type id of each perm */

static int gcd(int a, int b) { if (a < 0) a = -a; while (b) { int t = a % b; a = b; b = t; } return a; }
static int perm_rank(const uint8_t *p) {   /* lexicographic rank (Lehmer code) */
    int r = 0, used = 0;
    for (int i = 0; i < k; i++) {
        int c = 0;
        for (int j = 0; j < p[i]; j++) if (!(used >> j & 1)) c++;
        int f = 1; for (int j = 1; j < k - i; j++) f *= j;
        r += c * f; used |= 1 << p[i];
    }
    return r;
}
static inline int emul(int a, int b) { int ua = a / P, pa = a % P, ub = b / P, pb = b % P; return umul[ua][ub] * P + pcomp[(size_t)pa * P + pb]; }
static inline int econj(int s, int e) { int u = e / P, p = e % P; return u * P + pcomp[(size_t)pcomp[(size_t)s * P + p] * P + pinv[s]]; }
static int kmax_of(int h) { if (h == 1 || h == n) return 99; if (h == 9) return 3; return h; }
static int is_dead(int e) {
    int u = units[e / P]; const uint8_t *p = perms[e % P];
    int F = 0, isid = 1, inv2 = 1;
    for (int i = 0; i < k; i++) { if (p[i] == i) F++; else isid = 0; if (p[p[i]] != i) inv2 = 0; }
    if (isid && u == 1) return 0;
    int h = gcd(u - 1, n); if (u == 1) h = n;
    if (F >= 2 && F > kmax_of(h)) return 1;
    if (!isid && F >= 2 && (long)h * h > n) return 1;
    if (use_g1 && u == n - 1 && inv2 && !isid) return 2;
    return 0;
}

/* ---------------------------------------------------------------- closure */
static uint64_t *bits; static int bw;
static int elist[MAXORD + 1];
/* returns order, or -1 (too big) or -2 (dead element) */
static int closure(const int *gens, int ng, int *out) {
    int cnt = 0, idn = uidx[1] * P + 0;   /* identity: unit 1, perm rank 0 */
    out[cnt++] = idn; bits[idn >> 6] |= 1ULL << (idn & 63);
    int ret = 0;
    for (int q = 0; q < cnt; q++) {
        for (int g = 0; g < ng; g++) {
            int y = emul(gens[g], out[q]);
            if (bits[y >> 6] >> (y & 63) & 1ULL) continue;
            if (dead[y]) { ret = -2; goto done; }
            if (cnt >= omax) { ret = -1; goto done; }
            out[cnt++] = y; bits[y >> 6] |= 1ULL << (y & 63);
        }
    }
    ret = cnt;
done:
    for (int i = 0; i < cnt; i++) bits[out[i] >> 6] &= ~(1ULL << (out[i] & 63));
    return ret;
}
static int cmpint(const void *a, const void *b) { int x = *(const int *)a, y = *(const int *)b; return (x > y) - (x < y); }

/* ---------------------------------------------------------------- raw hash set */
typedef struct { uint64_t h; int ord; int *el; } Raw;
static Raw *rawtab; static long long rawcap, rawcnt;
static uint64_t hash_list(const int *a, int m) { uint64_t h = 1469598103934665603ULL; for (int i = 0; i < m; i++) { h ^= (uint64_t)a[i] + 0x9E3779B97F4A7C15ULL; h *= 1099511628211ULL; } return h; }
static int raw_insert(const int *sorted, int m) {   /* 1 if new */
    uint64_t h = hash_list(sorted, m);
    if (rawcnt * 2 >= rawcap) {
        long long nc = rawcap ? rawcap * 2 : 1 << 16;
        Raw *nt = calloc((size_t)nc, sizeof(Raw));
        for (long long i = 0; i < rawcap; i++) if (rawtab[i].el) { long long j = rawtab[i].h % nc; while (nt[j].el) j = (j + 1) % nc; nt[j] = rawtab[i]; }
        free(rawtab); rawtab = nt; rawcap = nc;
    }
    long long j = h % rawcap;
    while (rawtab[j].el) {
        if (rawtab[j].h == h && rawtab[j].ord == m && !memcmp(rawtab[j].el, sorted, sizeof(int) * m)) return 0;
        j = (j + 1) % rawcap;
    }
    rawtab[j].h = h; rawtab[j].ord = m; rawtab[j].el = malloc(sizeof(int) * m); memcpy(rawtab[j].el, sorted, sizeof(int) * m);
    rawcnt++;
    return 1;
}

/* ---------------------------------------------------------------- classes */
typedef struct { int ord, ng, gens[8], el[MAXORD]; uint64_t inv; } Cls;
static Cls *cls; static int ncls, clscap;
static uint64_t invariant(const int *el, int m) {
    int cnt[MAXU * 16]; memset(cnt, 0, sizeof cnt);
    for (int i = 0; i < m; i++) cnt[(el[i] / P) * 16 + ctype_id[el[i] % P]]++;
    uint64_t h = 1469598103934665603ULL ^ (uint64_t)m;
    for (int i = 0; i < nu * 16; i++) { h ^= (uint64_t)cnt[i] * 1315423911ULL + (uint64_t)i; h *= 1099511628211ULL; }
    return h;
}
static int conj_to(const Cls *C, const int *el, int m) {   /* is some sigma C sigma^-1 == group el? */
    for (int i = 0; i < m; i++) bits[el[i] >> 6] |= 1ULL << (el[i] & 63);
    int found = 0;
    for (int s = 0; s < P && !found; s++) {
        int ok = 1;
        for (int g = 0; g < C->ng && ok; g++) { int y = econj(s, C->gens[g]); if (!(bits[y >> 6] >> (y & 63) & 1ULL)) ok = 0; }
        if (ok) found = 1;
    }
    for (int i = 0; i < m; i++) bits[el[i] >> 6] &= ~(1ULL << (el[i] & 63));
    return found;
}
static void add_group(const int *gens, int ng, int *el, int m) {
    qsort(el, (size_t)m, sizeof(int), cmpint);
    if (!raw_insert(el, m)) return;
    uint64_t iv = invariant(el, m);
    for (int c = 0; c < ncls; c++) if (cls[c].inv == iv && cls[c].ord == m && conj_to(&cls[c], el, m)) return;
    if (ncls >= clscap) { clscap = clscap ? clscap * 2 : 256; cls = realloc(cls, sizeof(Cls) * (size_t)clscap); }
    Cls *C = &cls[ncls++];
    C->ord = m; C->ng = ng; C->inv = iv;
    for (int g = 0; g < ng; g++) C->gens[g] = gens[g];
    memcpy(C->el, el, sizeof(int) * m);
}

static void print_elem(FILE *o, int e) {
    fprintf(o, "[%d, [", units[e / P]);
    for (int i = 0; i < k; i++) fprintf(o, i ? ", %d" : "%d", perms[e % P][i]);
    fprintf(o, "]]");
}
static void ctype_str(int p, char *buf) {
    int seen = 0, len[MAXKP], nl = 0;
    for (int i = 0; i < k; i++) if (!(seen >> i & 1)) { int l = 0, j = i; while (!(seen >> j & 1)) { seen |= 1 << j; j = perms[p][j]; l++; } len[nl++] = l; }
    for (int a = 0; a < nl; a++) for (int b = a + 1; b < nl; b++) if (len[b] > len[a]) { int t = len[a]; len[a] = len[b]; len[b] = t; }
    int pos = 0;
    for (int a = 0; a < nl; a++) pos += sprintf(buf + pos, a ? ".%d" : "%d", len[a]);
}

int main(int argc, char **argv) {
    if (argc != 6 && argc != 7) { fprintf(stderr, "usage: groups_enum_c21v1 N K OMIN OMAX OUTFILE [nog1]\n"); return 2; }
    n = atoi(argv[1]); k = atoi(argv[2]); omin = atoi(argv[3]); omax = atoi(argv[4]);
    if (argc == 7 && !strcmp(argv[6], "nog1")) use_g1 = 0;
    if (argc == 7 && !strcmp(argv[6], "nog1")) use_g1 = 0;
    if (use_g1 && (n % 3 != 0 || n % 2 == 0 || k < 4)) { fprintf(stderr, "rule G1 needs odd n with 3 | n and k >= 4: disabled\n"); use_g1 = 0; }
    nu = 0;
    for (int u = 1; u < n; u++) if (gcd(u, n) == 1) { uidx[u] = nu; units[nu++] = u; }
    for (int a = 0; a < nu; a++) { for (int b = 0; b < nu; b++) umul[a][b] = uidx[(units[a] * units[b]) % n]; }
    for (int a = 0; a < nu; a++) for (int b = 0; b < nu; b++) if (umul[a][b] == uidx[1]) uinvi[a] = b;
    /* permutations in lexicographic order */
    P = 1; for (int i = 2; i <= k; i++) P *= i;
    uint8_t cur[MAXKP]; for (int i = 0; i < k; i++) cur[i] = (uint8_t)i;
    for (int r = 0; r < P; r++) {
        memcpy(perms[r], cur, k);
        if (perm_rank(cur) != r) { fprintf(stderr, "rank error\n"); return 5; }
        int i = k - 2; while (i >= 0 && cur[i] > cur[i + 1]) i--;
        if (i < 0) break;
        int j = k - 1; while (cur[j] < cur[i]) j--;
        uint8_t t = cur[i]; cur[i] = cur[j]; cur[j] = t;
        for (int a = i + 1, b = k - 1; a < b; a++, b--) { t = cur[a]; cur[a] = cur[b]; cur[b] = t; }
    }
    pcomp = malloc(sizeof(uint16_t) * (size_t)P * P);
    for (int a = 0; a < P; a++) for (int b = 0; b < P; b++) { uint8_t c[MAXKP]; for (int i = 0; i < k; i++) c[i] = perms[a][perms[b][i]]; pcomp[(size_t)a * P + b] = (uint16_t)perm_rank(c); }
    for (int a = 0; a < P; a++) { uint8_t c[MAXKP]; for (int i = 0; i < k; i++) c[perms[a][i]] = (uint8_t)i; pinv[a] = (uint16_t)perm_rank(c); }
    /* cycle type ids */
    {
        char names[64][32]; int nn = 0;
        for (int p = 0; p < P; p++) {
            char buf[32]; ctype_str(p, buf);
            int id = -1; for (int q = 0; q < nn; q++) if (!strcmp(names[q], buf)) id = q;
            if (id < 0) { strcpy(names[nn], buf); id = nn++; }
            ctype_id[p] = id;
        }
    }
    E = nu * P;
    dead = malloc((size_t)E);
    long long ndead = 0, ng1 = 0;
    for (int e = 0; e < E; e++) { int d = is_dead(e); dead[e] = (uint8_t)(d != 0); ndead += d != 0; ng1 += d == 2; }
    bw = (E + 63) / 64; bits = calloc((size_t)bw, sizeof(uint64_t));
    fprintf(stderr, "n %d k %d units %d perms %d elements %d dead %lld (G1 %lld)\n", n, k, nu, P, E, ndead, ng1);
    int el[MAXORD + 1];
    /* cyclic */
    for (int e = 0; e < E; e++) {
        if (dead[e]) continue;
        int m = closure(&e, 1, el);
        if (m > 0) add_group(&e, 1, el, m);
    }
    fprintf(stderr, "cyclic classes %d raw %lld\n", ncls, rawcnt);
    /* extensions */
    for (int c = 0; c < ncls; c++) {
        Cls H = cls[c];   /* copy: cls may be reallocated */
        if (H.ng >= 7) continue;
        uint64_t *hb = calloc((size_t)bw, sizeof(uint64_t));
        for (int i = 0; i < H.ord; i++) hb[H.el[i] >> 6] |= 1ULL << (H.el[i] & 63);
        int gens[8];
        for (int g = 0; g < H.ng; g++) gens[g] = H.gens[g];
        for (int x = 0; x < E; x++) {
            if (dead[x] || (hb[x >> 6] >> (x & 63) & 1ULL)) continue;
            gens[H.ng] = x;
            int m = closure(gens, H.ng + 1, el);
            if (m > 0) add_group(gens, H.ng + 1, el, m);
        }
        free(hb);
    }
    fprintf(stderr, "all classes (order <= %d) %d raw %lld\n", omax, ncls, rawcnt);
    int fd = open(argv[5], O_WRONLY | O_CREAT | O_EXCL, 0644);
    if (fd < 0) { perror("open out"); return 3; }
    FILE *o = fdopen(fd, "w");
    int nout = 0;
    for (int c = 0; c < ncls; c++) {
        Cls *C = &cls[c];
        if (C->ord < omin) continue;
        /* reduce generators greedily */
        int gl[8], ngl = 0;
        for (int g = 0; g < C->ng; g++) {
            int m1 = closure(gl, ngl, el);
            int inside = 0; for (int i = 0; i < m1; i++) if (el[i] == C->gens[g]) inside = 1;
            if (!inside) gl[ngl++] = C->gens[g];
        }
        int m2 = closure(gl, ngl, el);
        if (m2 != C->ord) { fprintf(stderr, "INTERNAL generator reduction\n"); return 5; }
        /* summary */
        int kernel_mu[MAXU], nker = 0, hasm1 = 0, fixrow_any = 0;
        char tbuf[4096]; int tp = 0;
        for (int i = 0; i < C->ord; i++) {
            int e = C->el[i], u = units[e / P], p = e % P;
            if (p == 0) { kernel_mu[nker++] = u; if (u == n - 1) hasm1 = 1; }
            char cb[32]; ctype_str(p, cb);
            if (tp < 3800) tp += sprintf(tbuf + tp, "%s\"%d:%s\"", i ? ", " : "", u, cb);
            (void)fixrow_any;
        }
        fprintf(o, "{\"n\": %d, \"k\": %d, \"order\": %d, \"gens\": [", n, k, C->ord);
        for (int g = 0; g < ngl; g++) { if (g) fprintf(o, ", "); print_elem(o, gl[g]); }
        fprintf(o, "], \"per_row_kernel\": [");
        for (int i = 0; i < nker; i++) fprintf(o, i ? ", %d" : "%d", kernel_mu[i]);
        fprintf(o, "], \"contains_minus1_id\": %s, \"elements\": [%s]}\n", hasm1 ? "true" : "false", tbuf);
        nout++;
    }
    fclose(o);
    fprintf(stderr, "written %d classes with order in [%d, %d]\n", nout, omin, omax);
    printf("CLASSES %d\n", nout);
    return 0;
}
