/* Independent gcDCQS(g^n : 0) certificate checker in C (no code shared with check_gcdcqs.py).
 * Format: "GCDCQS v n g", "COLOURS r", "HOLEFREE s", "GROUPS" + n lines of g points, "BLOCKS" +
 * 4-point lines, then per point "POINT x", "CLASS j" (j consecutive from 0) + 3-point lines.
 * '#' starts a comment; blank lines ignored.
 * Checks: v == n*g, n >= 3; w = v-1 and h = g-1 are ≡ 1,3 (mod 6); r == chi'(w) (Tan-Zhou (1.1),
 * recomputed); s == r - (w-h)/2; groups: n lines of g distinct in-range points, disjoint,
 * covering all points; blocks: 4 distinct in-range points, at most two per group, every
 * 3-subset in at most one block (fourth-point table), block count (C(v,3) - n C(g,3))/4, and an
 * explicit sweep: every 3-subset not inside a group is covered, none inside a group is;
 * POINT ids: every x exactly once; per POINT: exactly r nonempty classes, triples of distinct
 * in-range points avoiding x, pairwise disjoint inside a class, t ∪ {x} a block, no triple
 * listed twice at x, (w(w-1) - h(h-1))/6 triples listed (hence the whole derived design), and
 * exactly s classes with no point of x's group.  Prints PASS/FAIL; exit 0 iff PASS.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXV 128
static signed char fourth[MAXV][MAXV][MAXV];
static unsigned short seenat[MAXV][MAXV][MAXV];
static int grp[MAXV], ptmark[MAXV], pointseen[MAXV];

static void die(const char *m, long ln) { printf("FAIL line %ld: %s\n", ln, m); exit(1); }
static void srt(int *a, int k) {
    for (int i = 1; i < k; i++) { int t = a[i], j = i - 1; while (j >= 0 && a[j] > t) { a[j + 1] = a[j]; j--; } a[j + 1] = t; }
}
static int chi(int w) {
    if (w % 6 == 3) return (w - 1) / 2;
    if (w % 6 == 1) return w == 7 ? 7 : (w == 13 ? 8 : (w + 1) / 2);
    return -1;
}
static int split(char *s, char **w, int max) {
    int n = 0;
    char *p = s;
    for (;;) {
        while (*p == ' ' || *p == '\t' || *p == '\r' || *p == '\n') p++;
        if (!*p) return n;
        if (n == max) return max + 1;
        w[n++] = p;
        while (*p && *p != ' ' && *p != '\t' && *p != '\r' && *p != '\n') p++;
        if (*p) *p++ = 0;
    }
}
static int num(const char *s, long ln) {
    char *e;
    long x = strtol(s, &e, 10);
    if (e == s || *e) die("non-integer token", ln);
    return (int)x;
}

int main(int argc, char **argv) {
    if (argc != 2) { fprintf(stderr, "usage: %s CERT\n", argv[0]); return 2; }
    FILE *f = fopen(argv[1], "r");
    if (!f) { perror("open"); return 2; }
    memset(fourth, -1, sizeof fourth);
    for (int i = 0; i < MAXV; i++) grp[i] = -1;
    static char line[8192];
    char *w[MAXV + 4];
    long ln = 0, nblocks = 0, listed = 0;
    int v = 0, n = 0, g = 0, r = -1, s = -1, stage = 0, ngroups = 0, npoints = 0;
    int curx = -1, ncls = 0, curtrips = 0, curhole = 0, avoidcnt = 0, stamp = 0;
    long need_blocks = 0, need_listed = 0;
    while (fgets(line, sizeof line, f)) {
        ln++;
        char *hash = strchr(line, '#');
        if (hash) *hash = 0;
        int k = split(line, w, MAXV + 2);
        if (k == 0) continue;
        if (stage == 0) {
            if (k != 4 || strcmp(w[0], "GCDCQS")) die("expected 'GCDCQS v n g'", ln);
            v = num(w[1], ln); n = num(w[2], ln); g = num(w[3], ln);
            if (v > MAXV || v < 4 || n < 3 || g < 2 || v != n * g) die("bad v, n, g", ln);
            if ((v - 1) % 6 != 1 && (v - 1) % 6 != 3) die("v-1 not an STS order", ln);
            if ((g - 1) % 6 != 1 && (g - 1) % 6 != 3) die("g-1 not an STS order", ln);
            need_blocks = ((long)v * (v - 1) * (v - 2) / 6 - (long)n * g * (g - 1) * (g - 2) / 6) / 4;
            need_listed = ((long)(v - 1) * (v - 2) - (long)(g - 1) * (g - 2)) / 6;
            stage = 1; continue;
        }
        if (stage == 1) {
            if (k != 2 || strcmp(w[0], "COLOURS")) die("expected 'COLOURS r'", ln);
            r = num(w[1], ln);
            if (r != chi(v - 1)) die("COLOURS differs from chi'(v-1)", ln);
            stage = 2; continue;
        }
        if (stage == 2) {
            if (k != 2 || strcmp(w[0], "HOLEFREE")) die("expected 'HOLEFREE s'", ln);
            s = num(w[1], ln);
            if (s != chi(v - 1) - ((v - 1) - (g - 1)) / 2) die("HOLEFREE differs from chi'(w)-(w-h)/2", ln);
            stage = 3; continue;
        }
        if (stage == 3) {
            if (k != 1 || strcmp(w[0], "GROUPS")) die("expected 'GROUPS'", ln);
            stage = 4; continue;
        }
        if (stage == 4) {
            if (k == 1 && !strcmp(w[0], "BLOCKS")) {
                if (ngroups != n) die("wrong number of groups", ln);
                for (int p = 0; p < v; p++) if (grp[p] < 0) die("groups do not cover all points", ln);
                stage = 5; continue;
            }
            if (k != g) die("group line has wrong length", ln);
            for (int i = 0; i < g; i++) {
                int p = num(w[i], ln);
                if (p < 0 || p >= v) die("group point out of range", ln);
                if (grp[p] >= 0) die("point in two groups or repeated", ln);
                grp[p] = ngroups;
            }
            ngroups++;
            continue;
        }
        if (!strcmp(w[0], "POINT")) {
            if (k != 2) die("bad POINT line", ln);
            if (stage == 5) {
                if (nblocks != need_blocks) die("wrong number of blocks", ln);
                long cov = 0;
                for (int a = 0; a < v; a++) for (int b = a + 1; b < v; b++) for (int c = b + 1; c < v; c++) {
                    int ingroup = grp[a] == grp[b] && grp[b] == grp[c];
                    if (ingroup && fourth[a][b][c] >= 0) die("a group triple lies in a block", ln);
                    if (!ingroup) { if (fourth[a][b][c] < 0) die("a non-group triple lies in no block", ln); cov++; }
                }
                if (cov * 1 != 4 * need_blocks) die("coverage count mismatch", ln);
                stage = 6;
            } else {
                if (ncls != r) die("previous POINT: wrong number of classes", ln);
                if (curtrips == 0) die("previous POINT: empty last class", ln);
                if (!curhole) avoidcnt++;
                if (listed != need_listed) die("previous POINT: derived design not fully listed", ln);
                if (avoidcnt != s) die("previous POINT: wrong number of hole-avoiding classes", ln);
            }
            int x = num(w[1], ln);
            if (x < 0 || x >= v) die("POINT out of range", ln);
            if (pointseen[x]) die("POINT listed twice", ln);
            pointseen[x] = 1; npoints++;
            curx = x; ncls = 0; curtrips = -1; listed = 0; avoidcnt = 0; curhole = 0;
            continue;
        }
        if (!strcmp(w[0], "CLASS")) {
            if (stage != 6 || k != 2) die("CLASS outside POINT or malformed", ln);
            if (num(w[1], ln) != ncls) die("class id out of order", ln);
            if (ncls > 0) {
                if (curtrips == 0) die("empty class", ln);
                if (!curhole) avoidcnt++;
            }
            ncls++;
            if (ncls > r) die("too many classes", ln);
            curtrips = 0; curhole = 0; stamp++;
            continue;
        }
        if (stage == 5) {
            if (k != 4) die("block line must have 4 entries", ln);
            int b[4];
            for (int i = 0; i < 4; i++) { b[i] = num(w[i], ln); if (b[i] < 0 || b[i] >= v) die("block point out of range", ln); }
            srt(b, 4);
            for (int i = 0; i < 3; i++) if (b[i] == b[i + 1]) die("repeated point in block", ln);
            int cnt[MAXV] = {0};
            for (int i = 0; i < 4; i++) if (++cnt[grp[b[i]]] >= 3) die("three block points in one group", ln);
            static const int om[4][3] = {{1, 2, 3}, {0, 2, 3}, {0, 1, 3}, {0, 1, 2}};
            for (int i = 0; i < 4; i++) {
                int a = b[om[i][0]], c1 = b[om[i][1]], c2 = b[om[i][2]];
                if (fourth[a][c1][c2] >= 0) die("3-subset in two blocks (or repeated block)", ln);
                fourth[a][c1][c2] = (signed char)b[i];
            }
            nblocks++;
            continue;
        }
        if (stage != 6 || ncls == 0) die("triple outside a CLASS", ln);
        if (k != 3) die("triple line must have 3 entries", ln);
        int t[3];
        for (int i = 0; i < 3; i++) { t[i] = num(w[i], ln); if (t[i] < 0 || t[i] >= v) die("triple point out of range", ln); }
        srt(t, 3);
        if (t[0] == t[1] || t[1] == t[2]) die("repeated point in triple", ln);
        for (int i = 0; i < 3; i++) {
            if (t[i] == curx) die("triple contains its POINT", ln);
            if (ptmark[t[i]] == stamp) die("class not point-disjoint", ln);
            ptmark[t[i]] = stamp;
            if (grp[t[i]] == grp[curx]) curhole = 1;
        }
        if (fourth[t[0]][t[1]][t[2]] != curx) die("triple plus POINT is not a block", ln);
        if (seenat[t[0]][t[1]][t[2]] == (unsigned short)(curx + 1)) die("triple listed twice at this POINT", ln);
        seenat[t[0]][t[1]][t[2]] = (unsigned short)(curx + 1);
        curtrips++; listed++;
    }
    fclose(f);
    if (stage != 6) die("no POINT sections", ln);
    if (ncls != r) die("last POINT: wrong number of classes", ln);
    if (curtrips == 0) die("last POINT: empty last class", ln);
    if (!curhole) avoidcnt++;
    if (listed != need_listed) die("last POINT: derived design not fully listed", ln);
    if (avoidcnt != s) die("last POINT: wrong number of hole-avoiding classes", ln);
    if (npoints != v) die("missing POINT sections", ln);
    printf("PASS v=%d n=%d g=%d blocks=%ld points=%d colours=%d holefree=%d derived_triples=%ld\n",
           v, n, g, nblocks, npoints, r, s, need_listed);
    return 0;
}
