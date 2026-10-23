/* Third, independent LKTS(v) certificate checker (C, no shared code).
 * Reads the LKTS/KTS/CLASS text format, requires consecutive ids from 0.
 * Checks: v%6==3; v-2 systems; (v-1)/2 classes per system; v/3 triples per
 * class; points in range and distinct within a triple; each class covers every
 * point exactly once; each system covers every pair exactly once; each
 * unordered triple occurs at most once overall; total = C(v,3).
 * Prints "PASS v systems classes triples" or "FAIL reason".  Exit 0 on PASS.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXV 128

static unsigned char pairseen[MAXV][MAXV];
static unsigned char *tripseen;
static int v = -1, nsys = 0, ncls = 0, ntrip_in_cls = 0, total = 0;
static int pointcov[MAXV];
static int failed = 0;

static void fail(const char *msg, long line) {
    printf("FAIL line %ld: %s\n", line, msg);
    exit(1);
}

static int classes_expected(void) { return (v - 1) / 2; }

static void close_class(long line) {
    if (ncls == 0) return;
    if (ntrip_in_cls != v / 3) fail("class has wrong number of triples", line);
    for (int p = 0; p < v; p++)
        if (pointcov[p] != 1) fail("class does not partition the points", line);
}

static void close_system(long line) {
    if (nsys == 0) return;
    close_class(line);
    if (ncls != classes_expected()) fail("system has wrong number of classes", line);
    for (int a = 0; a < v; a++)
        for (int b = a + 1; b < v; b++)
            if (pairseen[a][b] != 1) fail("system does not cover every pair exactly once", line);
}

int main(int argc, char **argv) {
    if (argc != 2) { fprintf(stderr, "usage: %s CERT\n", argv[0]); return 2; }
    FILE *f = fopen(argv[1], "r");
    if (!f) { perror("open"); return 2; }
    char buf[512];
    long line = 0;
    while (fgets(buf, sizeof buf, f)) {
        line++;
        char *h = strchr(buf, '#');
        if (h) *h = 0;
        char *s = buf;
        while (*s == ' ' || *s == '\t') s++;
        if (*s == 0 || *s == '\n' || *s == '\r') continue;
        if (strncmp(s, "LKTS", 4) == 0) {
            if (v != -1) fail("duplicate header", line);
            if (sscanf(s + 4, "%d", &v) != 1) fail("bad header", line);
            if (v < 3 || v > MAXV || v % 6 != 3) fail("v not 3 mod 6 or too large", line);
            tripseen = calloc((size_t)v * v * v, 1);
            continue;
        }
        if (v == -1) fail("data before header", line);
        if (strncmp(s, "KTS", 3) == 0) {
            int id;
            if (sscanf(s + 3, "%d", &id) != 1 || id != nsys) fail("KTS ids must be consecutive from 0", line);
            close_system(line);
            nsys++;
            ncls = 0;
            memset(pairseen, 0, sizeof pairseen);
            continue;
        }
        if (strncmp(s, "CLASS", 5) == 0) {
            int id;
            if (nsys == 0) fail("CLASS before KTS", line);
            if (sscanf(s + 5, "%d", &id) != 1 || id != ncls) fail("CLASS ids must be consecutive from 0", line);
            close_class(line);
            ncls++;
            ntrip_in_cls = 0;
            memset(pointcov, 0, sizeof pointcov);
            continue;
        }
        int a, b, c;
        char extra[8];
        if (sscanf(s, "%d %d %d %7s", &a, &b, &c, extra) != 3) fail("triple line must hold exactly three integers", line);
        if (ncls == 0) fail("triple outside class", line);
        if (a < 0 || b < 0 || c < 0 || a >= v || b >= v || c >= v) fail("point out of range", line);
        if (a == b || b == c || a == c) fail("repeated point", line);
        int t;
        if (a > b) { t = a; a = b; b = t; }
        if (b > c) { t = b; b = c; c = t; }
        if (a > b) { t = a; a = b; b = t; }
        pointcov[a]++; pointcov[b]++; pointcov[c]++;
        pairseen[a][b]++; pairseen[a][c]++; pairseen[b][c]++;
        size_t idx = ((size_t)a * v + b) * v + c;
        if (tripseen[idx]) fail("triple occurs twice", line);
        tripseen[idx] = 1;
        ntrip_in_cls++;
        total++;
    }
    close_system(line);
    if (nsys != v - 2) fail("wrong number of systems", line);
    long need = (long)v * (v - 1) * (v - 2) / 6;
    if (total != need) fail("total number of triples differs from C(v,3)", line);
    printf("PASS v=%d systems=%d classes=%d triples=%d\n", v, nsys, classes_expected(), total);
    return failed;
}
