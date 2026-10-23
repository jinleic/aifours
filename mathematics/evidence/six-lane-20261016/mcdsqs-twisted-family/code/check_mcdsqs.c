/* Independent mcDSQS(v) certificate checker in C (no code shared with check_mcdsqs.py).
 * Format: "MCDSQS v", "COLOURS r", "BLOCKS", 4-integer lines, then for each x: "POINT x",
 * then "CLASS j" sections (ids consecutive from 0 within a POINT) with 3-integer lines.
 * '#' starts a comment; blank lines are ignored.
 * Checks: v%6 in {2,4}, 4<=v<=MAXV; r equals chi'(v-1) of Tan-Zhou (1.1), recomputed here;
 * #blocks = v(v-1)(v-2)/24; block points distinct and in range; no 3-subset in two blocks
 * (fourth-point table) and explicit count of covered 3-subsets = C(v,3); POINT ids: every x
 * in 0..v-1 exactly once; per POINT: exactly r classes, each nonempty, triples of distinct
 * in-range points avoiding x, pairwise point-disjoint inside a class, every triple t with
 * t∪{x} a block, no triple listed twice at x, and (v-1)(v-2)/6 triples listed (hence all
 * derived triples).  Prints a PASS/FAIL line; exit 0 iff PASS.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXV 128
static signed char fourth[MAXV][MAXV][MAXV];      /* 4th point of the block on a<b<c, -1 none */
static unsigned short stamp3[MAXV][MAXV][MAXV];   /* x+1 if triple listed at POINT x */
static int pmark[MAXV];                           /* class stamp per point */
static int seenpt[MAXV];

static void die(const char *m, long ln) { printf("FAIL line %ld: %s\n", ln, m); exit(1); }
static void srt(int *a, int n) {
    for (int i = 1; i < n; i++) { int k = a[i], j = i - 1; while (j >= 0 && a[j] > k) { a[j + 1] = a[j]; j--; } a[j + 1] = k; }
}
static int chi(int w) {
    if (w % 6 == 3) return (w - 1) / 2;
    if (w % 6 == 1) return w == 7 ? 7 : (w == 13 ? 8 : (w + 1) / 2);
    return -1;
}
/* split s into integer/word tokens; returns count, words kept in w[] (pointers into s) */
static int toks(char *s, char **w, int max) {
    int n = 0; char *p = s;
    while (*p) {
        while (*p == ' ' || *p == '\t' || *p == '\r' || *p == '\n') p++;
        if (!*p) break;
        if (n == max) return max + 1;
        w[n++] = p;
        while (*p && *p != ' ' && *p != '\t' && *p != '\r' && *p != '\n') p++;
        if (*p) *p++ = 0;
    }
    return n;
}
static int toint(const char *s, long ln) {
    char *e; long x = strtol(s, &e, 10);
    if (*e || e == s) die("non-integer token", ln);
    return (int)x;
}

int main(int argc, char **argv) {
    if (argc != 2) { fprintf(stderr, "usage: %s CERT\n", argv[0]); return 2; }
    FILE *f = fopen(argv[1], "r");
    if (!f) { perror("open"); return 2; }
    memset(fourth, -1, sizeof fourth);
    static char buf[4096]; long ln = 0;
    int v = -1, r = -1, stage = 0;  /* 0 header,1 colours,2 BLOCKS kw,3 blocks,4 points */
    long nblocks = 0, nlisted = 0; int curx = -1, ncls = 0, ntrip = 0, npoints = 0, cstamp = 0;
    char *w[8];
    while (fgets(buf, sizeof buf, f)) {
        ln++;
        char *h = strchr(buf, '#'); if (h) *h = 0;
        int n = toks(buf, w, 6);
        if (n == 0) continue;
        if (stage == 0) {
            if (n != 2 || strcmp(w[0], "MCDSQS")) die("expected MCDSQS v", ln);
            v = toint(w[1], ln);
            if (v < 4 || v > MAXV || (v % 6 != 2 && v % 6 != 4)) die("v out of range or not 2,4 mod 6", ln);
            stage = 1; continue;
        }
        if (stage == 1) {
            if (n != 2 || strcmp(w[0], "COLOURS")) die("expected COLOURS r", ln);
            r = toint(w[1], ln);
            if (r != chi(v - 1)) die("COLOURS differs from chi'(v-1)", ln);
            if ((long)r * ((v - 1) / 3) < (long)(v - 1) * (v - 2) / 6) die("r classes too few", ln);
            stage = 2; continue;
        }
        if (stage == 2) {
            if (n != 1 || strcmp(w[0], "BLOCKS")) die("expected BLOCKS", ln);
            stage = 3; continue;
        }
        if (strcmp(w[0], "POINT") == 0) {
            if (n != 2) die("bad POINT line", ln);
            if (stage == 3) {
                if (nblocks != (long)v * (v - 1) * (v - 2) / 24) die("wrong number of blocks", ln);
                long cnt = 0;
                for (int a = 0; a < v; a++) for (int b = a + 1; b < v; b++) for (int c = b + 1; c < v; c++)
                    if (fourth[a][b][c] >= 0) cnt++;
                if (cnt != (long)v * (v - 1) * (v - 2) / 6) die("some 3-subset lies in no block", ln);
                stage = 4;
            } else {
                if (ncls != r) die("previous POINT has wrong number of classes", ln);
                if (ntrip == 0) die("previous POINT ends with an empty class", ln);
                if (nlisted != (long)(v - 1) * (v - 2) / 6) die("previous POINT: derived triples not all listed", ln);
            }
            int x = toint(w[1], ln);
            if (x < 0 || x >= v) die("POINT out of range", ln);
            if (seenpt[x]) die("POINT listed twice", ln);
            seenpt[x] = 1; npoints++; curx = x; ncls = 0; ntrip = -1; nlisted = 0;
            continue;
        }
        if (strcmp(w[0], "CLASS") == 0) {
            if (stage != 4 || n != 2) die("CLASS outside POINT or malformed", ln);
            if (toint(w[1], ln) != ncls) die("class id out of order", ln);
            if (ncls > 0 && ntrip == 0) die("empty class", ln);
            ncls++; ntrip = 0; cstamp++;
            if (ncls > r) die("too many classes", ln);
            continue;
        }
        if (stage == 3) {
            if (n != 4) die("block line must have 4 entries", ln);
            int p[4];
            for (int i = 0; i < 4; i++) { p[i] = toint(w[i], ln); if (p[i] < 0 || p[i] >= v) die("block point out of range", ln); }
            srt(p, 4);
            for (int i = 0; i < 3; i++) if (p[i] == p[i + 1]) die("repeated point in block", ln);
            int om[4][3] = {{1, 2, 3}, {0, 2, 3}, {0, 1, 3}, {0, 1, 2}};
            for (int i = 0; i < 4; i++) {
                int a = p[om[i][0]], b = p[om[i][1]], c = p[om[i][2]];
                if (fourth[a][b][c] != -1) die("3-subset in two blocks (or repeated block)", ln);
                fourth[a][b][c] = (signed char)p[i];
            }
            nblocks++;
            continue;
        }
        /* triple line inside POINT/CLASS */
        if (stage != 4 || ncls == 0) die("triple outside a CLASS", ln);
        if (n != 3) die("triple line must have 3 entries", ln);
        int t[3];
        for (int i = 0; i < 3; i++) { t[i] = toint(w[i], ln); if (t[i] < 0 || t[i] >= v) die("triple point out of range", ln); }
        srt(t, 3);
        if (t[0] == t[1] || t[1] == t[2]) die("repeated point in triple", ln);
        if (t[0] == curx || t[1] == curx || t[2] == curx) die("triple contains its POINT", ln);
        for (int i = 0; i < 3; i++) { if (pmark[t[i]] == cstamp) die("class not point-disjoint", ln); pmark[t[i]] = cstamp; }
        if (fourth[t[0]][t[1]][t[2]] != curx) die("triple plus POINT is not a block", ln);
        if (stamp3[t[0]][t[1]][t[2]] == (unsigned short)(curx + 1)) die("triple listed twice at this POINT", ln);
        stamp3[t[0]][t[1]][t[2]] = (unsigned short)(curx + 1);
        ntrip++; nlisted++;
    }
    fclose(f);
    if (stage != 4) die("no POINT sections", ln);
    if (ncls != r) die("last POINT has wrong number of classes", ln);
    if (ntrip == 0) die("last POINT ends with an empty class", ln);
    if (nlisted != (long)(v - 1) * (v - 2) / 6) die("last POINT: derived triples not all listed", ln);
    if (npoints != v) die("missing POINT sections", ln);
    printf("PASS v=%d blocks=%ld points=%d colours=%d derived_triples=%ld\n", v, nblocks, npoints, r,
           (long)(v - 1) * (v - 2) / 6);
    return 0;
}
