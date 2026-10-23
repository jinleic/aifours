/* btd_check.c -- independent native checker for balanced ternary design certificates (lane btd12-15, README 1.5).
 * Written separately from code/verify_btd.py; no shared code.
 *
 * Strict format: "BTD V B p1 p2 R K L\n" (decimal, no sign, no leading zeros), then exactly V lines of exactly B
 * entries, each a single character 0/1/2 (any other digit string is a range error if numeric, a format error
 * otherwise), separated by single spaces, each line terminated by LF; end of file right after the last LF.
 * Checks, in this order: format; R == p1 + 2*p2; entry range; per-row count of 1s == p1 and of 2s == p2; column
 * sums == K; all pairwise row inner products == L.  Repeated columns are reported, never rejected.
 * Output: one line "VALID ..." or "INVALID <category>: <detail>"; exit 0 iff VALID, 1 invalid, 2 usage/IO.
 * Usage: btd_check CERT [V B p1 p2 R K L]   (optional expected parameters; a mismatch is "INVALID binding")
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXV 64
#define MAXB 256

static unsigned char buf[1 << 20];
static long n, pos;
static int M[MAXV][MAXB];

static int bad(const char *cat, const char *msg) { printf("INVALID %s: %s\n", cat, msg); return 1; }

/* parse a decimal integer without sign or leading zeros; returns -1 on failure */
static long num(void) {
    if (pos >= n || buf[pos] < '0' || buf[pos] > '9') return -1;
    if (buf[pos] == '0' && pos + 1 < n && buf[pos + 1] >= '0' && buf[pos + 1] <= '9') return -1;
    long v = 0;
    while (pos < n && buf[pos] >= '0' && buf[pos] <= '9') {
        v = v * 10 + (buf[pos++] - '0');
        if (v > 100000000) return -1;
    }
    return v;
}

int main(int argc, char **argv) {
    if (argc != 2 && argc != 9) { fprintf(stderr, "usage: btd_check CERT [V B p1 p2 R K L]\n"); return 2; }
    FILE *f = fopen(argv[1], "rb");
    if (!f) { perror(argv[1]); return 2; }
    n = (long)fread(buf, 1, sizeof buf, f);
    int more = fgetc(f) != EOF;
    fclose(f);
    if (more) return bad("format", "file too large");
    char msg[256];
    if (n < 4 || memcmp(buf, "BTD ", 4) != 0) return bad("format", "header must start with 'BTD '");
    pos = 4;
    long P[7];
    for (int t = 0; t < 7; t++) {
        P[t] = num();
        if (P[t] < 0) return bad("format", "bad header number");
        if (t < 6) { if (pos >= n || buf[pos] != ' ') return bad("format", "bad header separator"); pos++; }
    }
    if (pos >= n || buf[pos] != '\n') return bad("format", "header must end with LF");
    pos++;
    long V = P[0], B = P[1], p1 = P[2], p2 = P[3], R = P[4], K = P[5], L = P[6];
    if (V < 1 || B < 1 || V > MAXV || B > MAXB) return bad("format", "V or B out of supported range");
    for (long i = 0; i < V; i++) {
        for (long j = 0; j < B; j++) {
            long start = pos;
            while (pos < n && buf[pos] >= '0' && buf[pos] <= '9') pos++;
            if (pos == start) { snprintf(msg, sizeof msg, "row %ld entry %ld is not a digit string", i, j); return bad("format", msg); }
            if (pos - start != 1) { snprintf(msg, sizeof msg, "row %ld entry %ld has %ld digits", i, j, pos - start); return bad("range", msg); }
            M[i][j] = buf[start] - '0';
            char want = (j + 1 < B) ? ' ' : '\n';
            if (pos >= n || buf[pos] != want) {
                snprintf(msg, sizeof msg, "row %ld: expected %s after entry %ld", i, want == ' ' ? "single space" : "LF", j);
                return bad("format", msg);
            }
            pos++;
        }
    }
    if (pos != n) return bad("format", "trailing data after the last matrix line");
    if (argc == 9) {
        for (int t = 0; t < 7; t++)
            if (atol(argv[2 + t]) != P[t]) return bad("binding", "parameters differ from the expected ones");
    }
    if (R != p1 + 2 * p2) return bad("header", "R != p1 + 2*p2");
    for (long i = 0; i < V; i++)
        for (long j = 0; j < B; j++)
            if (M[i][j] > 2) { snprintf(msg, sizeof msg, "entry (%ld,%ld) = %d", i, j, M[i][j]); return bad("range", msg); }
    for (long i = 0; i < V; i++) {
        long c1 = 0, c2 = 0;
        for (long j = 0; j < B; j++) { c1 += M[i][j] == 1; c2 += M[i][j] == 2; }
        if (c1 != p1 || c2 != p2) { snprintf(msg, sizeof msg, "row %ld: %ld ones, %ld twos", i, c1, c2); return bad("row-count", msg); }
    }
    for (long j = 0; j < B; j++) {
        long s = 0;
        for (long i = 0; i < V; i++) s += M[i][j];
        if (s != K) { snprintf(msg, sizeof msg, "column %ld sums to %ld", j, s); return bad("column-sum", msg); }
    }
    for (long i = 0; i < V; i++)
        for (long k = i + 1; k < V; k++) {
            long d = 0;
            for (long j = 0; j < B; j++) d += (long)M[i][j] * M[k][j];
            if (d != L) { snprintf(msg, sizeof msg, "rows %ld,%ld inner product %ld", i, k, d); return bad("pair-product", msg); }
        }
    long dupcols = 0;
    for (long j = 0; j < B; j++)
        for (long j2 = 0; j2 < j; j2++) {
            long same = 1;
            for (long i = 0; i < V && same; i++) same = M[i][j] == M[i][j2];
            if (same) { dupcols++; break; }
        }
    printf("VALID BTD(%ld,%ld;%ld,%ld,%ld;%ld,%ld) columns_equal_to_an_earlier_column=%ld\n", V, B, p1, p2, R, K, L, dupcols);
    return 0;
}
