/* k1par_enum.c — parent-side independent enumerator (moqls7-k1-parent-check-v1), NOT SAT.
 * Enumerates all support patterns of an ONB-assignment on a 4-net of order 7 in the claim's frame that satisfy the
 * necessary families F1-F4, by exhaustive backtracking. Frame: the 7 points of the class-0 line with label 0 get the
 * singleton support {class-1 label}. Off-frame points start with the FULL domain of all 127 nonempty subsets of
 * {0..6}; the frame lemma is NOT built in (it must emerge from F2 against the frame singletons).
 *   F1 nonempty (domains contain only nonempty subsets); F2 collinear supports never meet in exactly one coordinate;
 *   F3 every coordinate is covered on every line; F4 a coordinate covered by exactly one point of a line forces that
 *   point to be that singleton.
 * Two independent search modes:
 *   fc    : forward checking (F2 on neighbours of an assigned point) + F3/F4 domain propagation, MRV branching;
 *   plain : fixed point order, F2 checked against already-assigned collinear points only, F3/F4 checked only on lines
 *           whose 7 points are all assigned. No domain propagation at all.
 * Every leaf is re-verified by a separate full evaluator. Input: one net per line (196 ints). Args: mode.
 * Output per net: initial domain sizes after frame propagation (fc), solutions as 49 subsets, node counts.
 * Build: clang -O2 -o k1par_enum k1par_enum.c
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define NP 49
typedef struct { uint64_t w[2]; } Set128;   /* bitset over subsets 0..127 */

static int net[NP][4];
static int lines[28][7];
static int nbr[NP][24], nnbr[NP];
static int frame[7], isFrame[NP], frameLabel[NP];
static Set128 compat[128];   /* compat[s] = { t : |s & t| != 1 } */
static Set128 hasK[7];       /* subsets containing k */
static long nodes;
static int nsol;
static int sol[64][NP];

static inline int popc(int x) { return __builtin_popcount(x); }
static inline int inset(const Set128 *a, int s) { return (a->w[s >> 6] >> (s & 63)) & 1; }
static inline void addset(Set128 *a, int s) { a->w[s >> 6] |= 1ULL << (s & 63); }
static inline int isempty(const Set128 *a) { return !(a->w[0] | a->w[1]); }
static inline int count(const Set128 *a) { return __builtin_popcountll(a->w[0]) + __builtin_popcountll(a->w[1]); }
static inline Set128 andset(Set128 a, Set128 b) { Set128 r = {{a.w[0] & b.w[0], a.w[1] & b.w[1]}}; return r; }
static inline int intersects(const Set128 *a, const Set128 *b) { return (a->w[0] & b->w[0]) || (a->w[1] & b->w[1]); }
static inline int first(const Set128 *a) { return a->w[0] ? __builtin_ctzll(a->w[0]) : 64 + __builtin_ctzll(a->w[1]); }

/* full evaluator on a complete pattern (independent of search code) */
static int full_check(const int *S) {
    for (int p = 0; p < NP; p++) if (S[p] <= 0 || S[p] > 127) return 0;                      /* F1 */
    for (int i = 0; i < 7; i++) if (S[frame[i]] != (1 << frameLabel[frame[i]])) return 0;   /* frame */
    for (int l = 0; l < 28; l++) {
        for (int a = 0; a < 7; a++) for (int b = a + 1; b < 7; b++)
            if (popc(S[lines[l][a]] & S[lines[l][b]]) == 1) return 0;                          /* F2 */
        for (int k = 0; k < 7; k++) {
            int cov = 0, who = -1;
            for (int a = 0; a < 7; a++) if (S[lines[l][a]] >> k & 1) { cov++; who = lines[l][a]; }
            if (cov == 0) return 0;                                                            /* F3 */
            if (cov == 1 && S[who] != (1 << k)) return 0;                                      /* F4 */
        }
    }
    return 1;
}

static void record(const int *S) {
    if (!full_check(S)) { printf("LEAF_FAILED_FULL_CHECK\n"); exit(4); }
    if (nsol >= 64) { printf("TOO_MANY_SOLUTIONS\n"); exit(5); }
    memcpy(sol[nsol++], S, sizeof(int) * NP);
}

/* ---------- fc mode ---------- */
/* propagate F3/F4 to fixpoint; return 0 on wipe-out */
static int propagate(Set128 *dom) {
    int changed = 1;
    while (changed) {
        changed = 0;
        for (int l = 0; l < 28; l++) for (int k = 0; k < 7; k++) {
            int cnt = 0, who = -1;
            for (int a = 0; a < 7; a++) { int q = lines[l][a]; if (intersects(&dom[q], &hasK[k])) { cnt++; who = q; } }
            if (cnt == 0) return 0;
            if (cnt == 1) {
                Set128 only = {{0, 0}}; addset(&only, 1 << k);
                Set128 nd = andset(dom[who], only);
                if (isempty(&nd)) return 0;
                if (nd.w[0] != dom[who].w[0] || nd.w[1] != dom[who].w[1]) {
                    dom[who] = nd; changed = 1;
                    for (int j = 0; j < nnbr[who]; j++) {             /* who is now fixed to {k}: F2 on neighbours */
                        int q = nbr[who][j];
                        Set128 d2 = andset(dom[q], compat[1 << k]);
                        if (isempty(&d2)) return 0;
                        if (d2.w[0] != dom[q].w[0] || d2.w[1] != dom[q].w[1]) dom[q] = d2;
                    }
                }
            }
        }
    }
    return 1;
}

static int assigned_fc[NP];
static void search_fc(Set128 *dom) {
    nodes++;
    if (!propagate(dom)) return;
    int best = -1, bc = 1000;
    for (int p = 0; p < NP; p++) if (!assigned_fc[p]) { int c = count(&dom[p]); if (c < bc) { bc = c; best = p; } }
    if (best < 0) {
        int S[NP];
        for (int p = 0; p < NP; p++) { if (count(&dom[p]) != 1) { printf("INTERNAL\n"); exit(6); } S[p] = first(&dom[p]); }
        record(S);
        return;
    }
    Set128 vals = dom[best];
    for (int s = 1; s < 128; s++) if (inset(&vals, s)) {
        Set128 nd[NP];
        memcpy(nd, dom, sizeof(nd));
        nd[best].w[0] = nd[best].w[1] = 0; addset(&nd[best], s);
        int ok = 1;
        for (int j = 0; j < nnbr[best] && ok; j++) {
            int q = nbr[best][j];
            nd[q] = andset(nd[q], compat[s]);
            if (isempty(&nd[q])) ok = 0;
        }
        if (!ok) continue;
        assigned_fc[best] = 1;
        search_fc(nd);
        assigned_fc[best] = 0;
    }
}

/* ---------- plain mode ---------- */
static int order[NP], posInOrder[NP], lineDoneAt[28];
static int S_plain[NP];
static int line_ok(int l) {
    for (int k = 0; k < 7; k++) {
        int cov = 0, who = -1;
        for (int a = 0; a < 7; a++) if (S_plain[lines[l][a]] >> k & 1) { cov++; who = lines[l][a]; }
        if (cov == 0) return 0;
        if (cov == 1 && S_plain[who] != (1 << k)) return 0;
    }
    return 1;
}
static void search_plain(int i) {
    nodes++;
    if (i == NP) { record(S_plain); return; }
    int p = order[i];
    int lo = 1, hi = 127;
    if (isFrame[p]) lo = hi = 1 << frameLabel[p];
    for (int s = lo; s <= hi; s++) {
        int ok = 1;
        for (int j = 0; j < nnbr[p] && ok; j++) { int q = nbr[p][j]; if (posInOrder[q] < i && popc(S_plain[q] & s) == 1) ok = 0; }
        if (!ok) continue;
        S_plain[p] = s;
        for (int l = 0; l < 28 && ok; l++) if (lineDoneAt[l] == i && !line_ok(l)) ok = 0;
        if (ok) search_plain(i + 1);
        S_plain[p] = 0;
        if (isFrame[p]) break;
    }
}

int main(int argc, char **argv) {
    int plain = argc > 1 && strcmp(argv[1], "plain") == 0;
    for (int s = 0; s < 128; s++) for (int t = 0; t < 128; t++) if (popc(s & t) != 1) addset(&compat[s], t);
    for (int k = 0; k < 7; k++) for (int s = 1; s < 128; s++) if (s >> k & 1) addset(&hasK[k], s);
    int idx = 0;
    while (1) {
        int ok = 1;
        for (int q = 0; q < NP && ok; q++) for (int c = 0; c < 4; c++) if (scanf("%d", &net[q][c]) != 1) { ok = 0; break; }
        if (!ok) break;
        int nl = 0;
        for (int c = 0; c < 4; c++) for (int b = 0; b < 7; b++) { int m = 0; for (int q = 0; q < NP; q++) if (net[q][c] == b) { if (m == 7) return 7; lines[nl][m++] = q; } if (m != 7) return 7; nl++; }
        for (int p = 0; p < NP; p++) {
            nnbr[p] = 0;
            for (int q = 0; q < NP; q++) if (q != p) { int sh = 0; for (int c = 0; c < 4; c++) if (net[p][c] == net[q][c]) sh++; if (sh > 1) return 8; if (sh == 1) nbr[p][nnbr[p]++] = q; }
            if (nnbr[p] != 24) return 8;
        }
        int nf = 0;
        for (int p = 0; p < NP; p++) { isFrame[p] = net[p][0] == 0; if (isFrame[p]) { frame[nf++] = p; frameLabel[p] = net[p][1]; } }
        if (nf != 7) return 9;
        nodes = 0; nsol = 0;
        if (!plain) {
            Set128 dom[NP];
            for (int p = 0; p < NP; p++) {
                dom[p].w[0] = dom[p].w[1] = 0;
                if (isFrame[p]) addset(&dom[p], 1 << frameLabel[p]); else for (int s = 1; s < 128; s++) addset(&dom[p], s);
                assigned_fc[p] = 0;
            }
            /* frame points are assigned: F2 forward check from them */
            for (int i = 0; i < 7; i++) {
                int f = frame[i]; assigned_fc[f] = 1;
                for (int j = 0; j < nnbr[f]; j++) { int q = nbr[f][j]; dom[q] = andset(dom[q], compat[1 << frameLabel[f]]); }
            }
            /* report initial (pre-propagation) domains: should be all nonempty subsets of a 4-set A(p) (15 values) */
            printf("net %d initdom", idx);
            for (int p = 0; p < NP; p++) {
                int u = 0; for (int s = 1; s < 128; s++) if (inset(&dom[p], s)) u |= s;
                printf(" %d:%d:%d", p, count(&dom[p]), u);
            }
            printf("\n");
            search_fc(dom);
        } else {
            /* order: frame first, then points by (class-0 label, class-1 label); lineDoneAt = position of last point */
            int n = 0;
            for (int i = 0; i < 7; i++) order[n++] = frame[i];
            for (int b0 = 1; b0 < 7; b0++) for (int b1 = 0; b1 < 7; b1++) for (int p = 0; p < NP; p++) if (net[p][0] == b0 && net[p][1] == b1) order[n++] = p;
            if (n != NP) return 10;
            for (int i = 0; i < NP; i++) posInOrder[order[i]] = i;
            for (int l = 0; l < 28; l++) { int m = -1; for (int a = 0; a < 7; a++) if (posInOrder[lines[l][a]] > m) m = posInOrder[lines[l][a]]; lineDoneAt[l] = m; }
            search_plain(0);
        }
        printf("net %d mode %s solutions %d nodes %ld\n", idx, plain ? "plain" : "fc", nsol, nodes);
        for (int i = 0; i < nsol; i++) { printf("sol %d %d", idx, i); for (int p = 0; p < NP; p++) printf(" %d", sol[i][p]); printf("\n"); }
        fflush(stdout);
        idx++;
    }
    return 0;
}
