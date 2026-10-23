/* [v<=128 build of check_rdsqs.c; identical logic, larger MAXV]
 * Independent RDSQS(v) certificate checker in C (no code shared with check_rdsqs.py).
 * Format: "RDSQS v", "BLOCKS", 4-integer lines, then for each x: "POINT x", then
 * "CLASS j" sections (ids consecutive from 0 within a POINT) with 3-integer lines.
 * Checks: v%6==4, v<=MAXV; #blocks = v(v-1)(v-2)/24; block points distinct and in range;
 * every unordered triple lies in exactly one block (fourth-point table, explicit count
 * C(v,3)); POINT ids: every x in 0..v-1 exactly once; per POINT: (v-2)/2 classes, each of
 * (v-1)/3 triples of distinct in-range points not containing x, each class covering every
 * point of X\{x} exactly once, every triple t with t∪{x} a block, no derived triple listed
 * twice and (v-1)(v-2)/6 derived triples listed.  Prints PASS/FAIL line; exit 0 iff PASS.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXV 128
static signed char fourth[MAXV][MAXV][MAXV];   /* fourth point of the block through a<b<c, -1 if none */
static int seenpoint[MAXV];
static int cover[MAXV];
static unsigned char listed[MAXV][MAXV][MAXV]; /* per current POINT: derived triple listed */

static void die(const char *m, long ln) { printf("FAIL line %ld: %s\n", ln, m); exit(1); }
static void sort3(int *a, int *b, int *c) { int t;
    if (*a > *b) { t = *a; *a = *b; *b = t; }
    if (*b > *c) { t = *b; *b = *c; *c = t; }
    if (*a > *b) { t = *a; *a = *b; *b = t; } }

int main(int argc, char **argv) {
    if (argc != 2) { fprintf(stderr, "usage: %s CERT\n", argv[0]); return 2; }
    FILE *f = fopen(argv[1], "r");
    if (!f) { perror("open"); return 2; }
    memset(fourth, -1, sizeof fourth);
    char buf[256]; long ln = 0;
    int v = -1, section = 0, nblocks = 0, curx = -1, ncls = 0, ntrip = 0;
    long ntriples = 0, listed_count = 0;
    int npoints = 0;
    while (fgets(buf, sizeof buf, f)) {
        ln++;
        char *h = strchr(buf, '#'); if (h) *h = 0;
        char *s = buf; while (*s == ' ' || *s == '\t') s++;
        if (*s == 0 || *s == '\n' || *s == '\r') continue;
        if (!strncmp(s, "RDSQS", 5)) {
            if (v != -1 || sscanf(s + 5, "%d", &v) != 1) die("bad header", ln);
            if (v < 4 || v > MAXV || v % 6 != 4) die("v must be 4 mod 6 and <= 128", ln);
            continue;
        }
        if (v < 0) die("data before header", ln);
        if (!strncmp(s, "BLOCKS", 6)) { if (section != 0) die("BLOCKS twice/late", ln); section = 1; continue; }
        if (!strncmp(s, "POINT", 5)) {
            if (section == 0) die("POINT before BLOCKS", ln);
            if (section == 1) {   /* blocks finished: verify triple coverage */
                if (nblocks != v * (v - 1) * (v - 2) / 24) die("wrong number of blocks", ln);
                if (ntriples != (long)v * (v - 1) * (v - 2) / 6) die("triples covered != C(v,3)", ln);
            }
            if (section == 2) {   /* close previous point */
                if (ncls != (v - 2) / 2) die("previous point has wrong number of classes", ln);
                if (ntrip != (v - 1) / 3) die("previous class has wrong size", ln);
                for (int p = 0; p < v; p++) if (p != curx && cover[p] != 1) die("previous class not a partition", ln);
                if (listed_count != (long)(v - 1) * (v - 2) / 6) die("previous point: derived triples not all listed", ln);
            }
            section = 2;
            if (sscanf(s + 5, "%d", &curx) != 1 || curx < 0 || curx >= v) die("bad POINT id", ln);
            if (seenpoint[curx]) die("POINT listed twice", ln);
            seenpoint[curx] = 1; npoints++;
            ncls = 0; ntrip = (v - 1) / 3; listed_count = 0;
            memset(listed, 0, sizeof listed);
            for (int p = 0; p < v; p++) cover[p] = 1;  /* sentinel: no class yet */
            cover[curx] = 0;
            continue;
        }
        if (!strncmp(s, "CLASS", 5)) {
            int id;
            if (section != 2 || sscanf(s + 5, "%d", &id) != 1 || id != ncls) die("CLASS ids must be consecutive within a POINT", ln);
            if (ncls > 0) {
                if (ntrip != (v - 1) / 3) die("class has wrong size", ln);
                for (int p = 0; p < v; p++) if (p != curx && cover[p] != 1) die("class not a partition", ln);
            }
            ncls++; ntrip = 0;
            for (int p = 0; p < v; p++) cover[p] = 0;
            continue;
        }
        int a, b, c, d; char extra[8];
        if (section == 1) {
            if (sscanf(s, "%d %d %d %d %7s", &a, &b, &c, &d, extra) != 4) die("block line must have 4 integers", ln);
            int q[4] = {a, b, c, d};
            for (int i = 0; i < 4; i++) { if (q[i] < 0 || q[i] >= v) die("block point out of range", ln);
                for (int j = 0; j < i; j++) if (q[i] == q[j]) die("repeated point in block", ln); }
            for (int i = 0; i < 4; i++) {
                int x = q[(i + 1) % 4], y = q[(i + 2) % 4], z = q[(i + 3) % 4];
                sort3(&x, &y, &z);
                if (fourth[x][y][z] != -1) die("triple lies in two blocks", ln);
                fourth[x][y][z] = (signed char)q[i];
                ntriples++;
            }
            nblocks++;
            continue;
        }
        if (section == 2) {
            if (ncls == 0) die("triple before CLASS", ln);
            if (sscanf(s, "%d %d %d %7s", &a, &b, &c, extra) != 3) die("class line must have 3 integers", ln);
            if (a < 0 || b < 0 || c < 0 || a >= v || b >= v || c >= v) die("class point out of range", ln);
            if (a == b || b == c || a == c) die("repeated point in class triple", ln);
            if (a == curx || b == curx || c == curx) die("class triple contains its POINT", ln);
            sort3(&a, &b, &c);
            if (fourth[a][b][c] != curx) die("class triple plus POINT is not a block", ln);
            if (listed[a][b][c]) die("derived triple listed twice", ln);
            listed[a][b][c] = 1; listed_count++;
            cover[a]++; cover[b]++; cover[c]++;
            if (cover[a] > 1 || cover[b] > 1 || cover[c] > 1) die("class covers a point twice", ln);
            ntrip++;
            continue;
        }
        die("data outside sections", ln);
    }
    if (section != 2) die("no POINT sections", ln);
    if (ncls != (v - 2) / 2) die("last point has wrong number of classes", ln);
    if (ntrip != (v - 1) / 3) die("last class has wrong size", ln);
    for (int p = 0; p < v; p++) if (p != curx && cover[p] != 1) die("last class not a partition", ln);
    if (listed_count != (long)(v - 1) * (v - 2) / 6) die("last point: derived triples not all listed", ln);
    if (npoints != v) die("missing POINT sections", ln);
    /* explicit completeness of coverage */
    long cnt = 0;
    for (int x = 0; x < v; x++) for (int y = x + 1; y < v; y++) for (int z = y + 1; z < v; z++) if (fourth[x][y][z] >= 0) cnt++;
    if (cnt != (long)v * (v - 1) * (v - 2) / 6) die("some triple lies in no block", ln);
    printf("PASS v=%d blocks=%d triples=%ld points=%d classes=%d\n", v, nblocks, cnt, npoints, (v - 2) / 2);
    return 0;
}
