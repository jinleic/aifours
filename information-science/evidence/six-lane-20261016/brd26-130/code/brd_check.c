/* brd_check.c -- independent second checker for Bhaskar Rao design certificates (lane brd26-130, README 1.6).
 *
 * Usage: brd_check FILE [v b r k L]      exit 0 iff VALID (and, when given, the header equals v b r k L).
 * Format (strict): "BRD v b r k L\n" (decimal, no leading zeros), then exactly v lines of b entries from
 * {-1,0,1} ("-1", "0", "1") separated by single spaces, each line terminated by LF, nothing else (no CR, no tab).
 * Method (deliberately different from verify_brd.py): a byte-level state machine parses the file into a matrix;
 * row and column weights are counted in one pass; pair products are accumulated column by column: for every
 * column the list of its nonzero rows is formed and every pair in that list increments a "+1" or a "-1" counter in
 * a v x v table; finally every distinct pair must have L/2 in each counter.
 * Prints "VALID ..." or "INVALID <REASON>: ..." with REASON in FORMAT, HEADER, ROWS, COLUMNS, PAIRS.
 * Repeated columns are counted and reported, never rejected.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXV 512
#define MAXB 8192

static signed char M[MAXV][MAXB];
static int plus_cnt[MAXV][MAXV], minus_cnt[MAXV][MAXV];

static int fail(const char *reason, const char *detail) {
    printf("INVALID %s: %s\n", reason, detail);
    return 1;
}

/* parse a decimal without sign and without leading zeros starting at buf[*pos]; returns -1 on error */
static long parse_num(const unsigned char *buf, long n, long *pos) {
    long p = *pos, val = 0;
    if (p >= n || buf[p] < '0' || buf[p] > '9') return -1;
    if (buf[p] == '0' && p + 1 < n && buf[p + 1] >= '0' && buf[p + 1] <= '9') return -1;
    while (p < n && buf[p] >= '0' && buf[p] <= '9') {
        val = val * 10 + (buf[p] - '0');
        if (val > 1000000) return -1;
        p++;
    }
    *pos = p;
    return val;
}

int main(int argc, char **argv) {
    if (argc != 2 && argc != 7) {
        fprintf(stderr, "usage: brd_check FILE [v b r k L]\n");
        return 2;
    }
    FILE *f = fopen(argv[1], "rb");
    if (!f) { fprintf(stderr, "cannot open %s\n", argv[1]); return 2; }
    fseek(f, 0, SEEK_END);
    long n = ftell(f);
    fseek(f, 0, SEEK_SET);
    unsigned char *buf = malloc(n > 0 ? n : 1);
    if (!buf || (long)fread(buf, 1, n, f) != n) { fprintf(stderr, "read error\n"); return 2; }
    fclose(f);
    char det[256];

    /* header */
    const char *magic = "BRD ";
    long pos = 0;
    if (n < 4 || memcmp(buf, magic, 4) != 0) return fail("FORMAT", "header must start with 'BRD '");
    pos = 4;
    long par[5];
    for (int t = 0; t < 5; t++) {
        par[t] = parse_num(buf, n, &pos);
        if (par[t] < 0) return fail("FORMAT", "bad header number");
        if (t < 4) {
            if (pos >= n || buf[pos] != ' ') return fail("FORMAT", "header numbers must be separated by one space");
            pos++;
        }
    }
    if (pos >= n || buf[pos] != '\n') return fail("FORMAT", "header line must end with LF");
    pos++;
    long v = par[0], b = par[1], r = par[2], k = par[3], L = par[4];
    if (v < 1 || b < 1) return fail("HEADER", "v and b must be positive");
    if (v > MAXV || b > MAXB) return fail("HEADER", "dimensions exceed checker limits");
    if (L % 2 != 0) return fail("HEADER", "lambda is odd");
    if (argc == 7) {
        for (int t = 0; t < 5; t++) {
            if (strtol(argv[2 + t], NULL, 10) != par[t]) return fail("HEADER", "header differs from expected parameters");
        }
    }

    /* body: state machine; states: expect entry start */
    long row = 0, col = 0;
    while (pos < n) {
        if (row >= v) return fail("FORMAT", "extra content after the last matrix line");
        int val;
        if (buf[pos] == '-') {
            if (pos + 1 < n && buf[pos + 1] == '1') { val = -1; pos += 2; }
            else return fail("FORMAT", "'-' not followed by '1'");
        } else if (buf[pos] == '0') { val = 0; pos += 1; }
        else if (buf[pos] == '1') { val = 1; pos += 1; }
        else {
            snprintf(det, sizeof det, "row %ld column %ld: unexpected byte 0x%02x", row, col, buf[pos]);
            return fail("FORMAT", det);
        }
        if (col >= b) {
            snprintf(det, sizeof det, "row %ld has more than b = %ld entries", row, b);
            return fail("FORMAT", det);
        }
        M[row][col] = (signed char)val;
        col++;
        if (pos >= n) return fail("FORMAT", "file does not end with LF");
        if (buf[pos] == ' ') {
            pos++;
            if (pos >= n || buf[pos] == ' ' || buf[pos] == '\n') return fail("FORMAT", "space not followed by an entry");
        } else if (buf[pos] == '\n') {
            if (col != b) {
                snprintf(det, sizeof det, "row %ld has %ld entries, expected b = %ld", row, col, b);
                return fail("FORMAT", det);
            }
            pos++;
            row++;
            col = 0;
        } else {
            snprintf(det, sizeof det, "row %ld: entry followed by byte 0x%02x", row, buf[pos]);
            return fail("FORMAT", det);
        }
    }
    if (row != v) {
        snprintf(det, sizeof det, "%ld matrix lines, expected v = %ld", row, v);
        return fail("FORMAT", det);
    }

    /* weights */
    static long roww[MAXV];
    for (long i = 0; i < v; i++) roww[i] = 0;
    static int idx[MAXV];
    for (long j = 0; j < b; j++) {
        int m = 0;
        for (long i = 0; i < v; i++) {
            if (M[i][j] != 0) { idx[m++] = (int)i; roww[i]++; }
        }
        if (m != k) {
            snprintf(det, sizeof det, "column %ld has %d nonzero entries, expected k = %ld", j, m, k);
            return fail("COLUMNS", det);
        }
        for (int a = 0; a < m; a++)
            for (int c = a + 1; c < m; c++) {
                int p = M[idx[a]][j] * M[idx[c]][j];
                if (p > 0) plus_cnt[idx[a]][idx[c]]++;
                else minus_cnt[idx[a]][idx[c]]++;
            }
    }
    for (long i = 0; i < v; i++) {
        if (roww[i] != r) {
            snprintf(det, sizeof det, "row %ld has %ld nonzero entries, expected r = %ld", i, roww[i], r);
            return fail("ROWS", det);
        }
    }
    for (long i = 0; i < v; i++)
        for (long i2 = i + 1; i2 < v; i2++)
            if (plus_cnt[i][i2] != L / 2 || minus_cnt[i][i2] != L / 2) {
                snprintf(det, sizeof det, "rows %ld,%ld: %d products +1 and %d products -1, expected %ld each",
                         i, i2, plus_cnt[i][i2], minus_cnt[i][i2], L / 2);
                return fail("PAIRS", det);
            }
    /* repeated columns (reported only) */
    long dup = 0;
    for (long j = 0; j < b; j++)
        for (long j2 = 0; j2 < j; j2++) {
            long i = 0;
            while (i < v && M[i][j] == M[i][j2]) i++;
            if (i == v) { dup++; break; }
        }
    printf("VALID BRD(%ld,%ld,%ld,%ld,%ld) columns_equal_to_an_earlier_column=%ld\n", v, b, r, k, L, dup);
    free(buf);
    return 0;
}
