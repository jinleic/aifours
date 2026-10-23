/* lratstrict2.c = lratstrict.c (identical checking logic) plus an optional third argument OUT:
 * every addition that passed the RUP check and every deletion are written to OUT as a binary
 * DRAT stream ('a' / 'd', literals as 2*|l| + (l<0) in 7-bit little-endian varints, 0 byte), so
 * the derivation can be re-checked by an independent DRAT checker (deletions carry the deleted
 * clause's literals). OUT is written while checking; it is only meaningful if the run ends with
 * "s VERIFIED" (the empty-clause addition is written before the success line).
 *
 * lratstrict.c -- strict RUP-only checker for ASCII LRAT proofs (written in this lane after the
 * parent found that drat-trim's lrat-check accepts an empty clause without a conflict).
 *
 * Usage: lratstrict CNF LRAT        (LRAT may be /dev/stdin; it is read strictly sequentially)
 *
 * Accepts (prints "s VERIFIED", exit 0) iff some addition step derives the EMPTY clause and every
 * step read up to that point passed the checks below. Everything else prints "s NOT VERIFIED"
 * with a reason and exits 1.
 *   CNF:   "p cnf V C" header (after 'c' comment lines), exactly C clauses, literals in 1..V.
 *          Clause i gets id i.
 *   Addition "id l1 .. lk 0 h1 .. hm 0":
 *          id > every earlier id (and > C); literals in 1..V; no complementary pair (tautology);
 *          every hint positive (no RAT) and the id of a live clause; RUP with hints only: after
 *          falsifying the lemma literals, each hint clause in order must have no true literal and
 *          at most one unassigned literal (duplicates of the same literal count once). One
 *          unassigned literal is assigned true; zero means conflict. The conflict must be reached
 *          exactly at the LAST hint (no hints left over, none missing).
 *   Deletion "id d i1 .. in 0": every listed id must be live; it is removed.
 * Any other token, a negative/zero id, truncated input, or EOF before an empty clause -> fail.
 * After the empty clause is verified the rest of the input is drained without checking (so a
 * streaming producer does not get SIGPIPE).
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int len;
    int lits[];
} Clause;

static uint64_t *hkeys;
static Clause **hvals;
static size_t hcap, hused, hlive;
#define HTOMB UINT64_MAX

__attribute__((noreturn)) static void fail(const char *why, long long a, long long b) {
    printf("c FAIL: %s (%lld, %lld)\ns NOT VERIFIED\n", why, a, b);
    fflush(stdout);
    exit(1);
}

static size_t hh(uint64_t k) {
    k ^= k >> 33;
    k *= 0xff51afd7ed558ccdULL;
    k ^= k >> 33;
    k *= 0xc4ceb9fe1a85ec53ULL;
    k ^= k >> 33;
    return (size_t)k;
}

static void hrehash(size_t ncap) {
    uint64_t *ok = hkeys;
    Clause **ov = hvals;
    size_t oc = hcap;
    hkeys = calloc(ncap, sizeof(uint64_t));
    hvals = calloc(ncap, sizeof(Clause *));
    if (!hkeys || !hvals) fail("out of memory (hash)", (long long)ncap, 0);
    hcap = ncap;
    hused = 0;
    for (size_t i = 0; i < oc; i++) {
        if (ok[i] != 0 && ok[i] != HTOMB) {
            size_t j = hh(ok[i]) & (hcap - 1);
            while (hkeys[j] != 0) j = (j + 1) & (hcap - 1);
            hkeys[j] = ok[i];
            hvals[j] = ov[i];
            hused++;
        }
    }
    free(ok);
    free(ov);
}

static long hfind(uint64_t k) {
    size_t j = hh(k) & (hcap - 1);
    while (hkeys[j] != 0) {
        if (hkeys[j] == k) return (long)j;
        j = (j + 1) & (hcap - 1);
    }
    return -1;
}

static void hinsert(uint64_t k, Clause *c) {
    if ((hused + 1) * 2 > hcap) {
        size_t n = 16;
        while (n < (hlive + 1) * 4) n <<= 1;
        hrehash(n);
    }
    if (hfind(k) >= 0) fail("duplicate clause id", (long long)k, 0);
    size_t j = hh(k) & (hcap - 1);
    while (hkeys[j] != 0 && hkeys[j] != HTOMB) j = (j + 1) & (hcap - 1);
    if (hkeys[j] == 0) hused++;
    hkeys[j] = k;
    hvals[j] = c;
    hlive++;
}

/* ---- buffered tokenizer ---- */
typedef struct {
    FILE *f;
    unsigned char *buf;
    size_t n, p;
    int eof;
} Rd;

static int rd_fill(Rd *r) {
    if (r->eof) return 0;
    r->n = fread(r->buf, 1, 1 << 20, r->f);
    r->p = 0;
    if (r->n == 0) {
        r->eof = 1;
        return 0;
    }
    return 1;
}

static int rd_peek(Rd *r) {
    if (r->p >= r->n && !rd_fill(r)) return -1;
    return r->buf[r->p];
}

static void rd_skip_ws(Rd *r) {
    for (;;) {
        int c = rd_peek(r);
        if (c == ' ' || c == '\n' || c == '\t' || c == '\r') {
            r->p++;
            continue;
        }
        return;
    }
}

/* token kinds: 0 = integer (in *v), 1 = 'd', 2 = EOF; anything else fails */
static int rd_tok(Rd *r, long long *v) {
    rd_skip_ws(r);
    int c = rd_peek(r);
    if (c < 0) return 2;
    if (c == 'd') {
        r->p++;
        int c2 = rd_peek(r);
        if (!(c2 == ' ' || c2 == '\n' || c2 == '\t' || c2 == '\r')) fail("bad token after d", c2, 0);
        return 1;
    }
    int neg = 0;
    if (c == '-') {
        neg = 1;
        r->p++;
        c = rd_peek(r);
    }
    if (c < '0' || c > '9') fail("unexpected character", c, 0);
    unsigned long long x = 0;
    while (c >= '0' && c <= '9') {
        x = x * 10 + (unsigned)(c - '0');
        if (x > (1ULL << 62)) fail("number too large", 0, 0);
        r->p++;
        c = rd_peek(r);
    }
    if (!(c < 0 || c == ' ' || c == '\n' || c == '\t' || c == '\r')) fail("bad number terminator", c, 0);
    *v = neg ? -(long long)x : (long long)x;
    return 0;
}

static FILE *dout;

static void emit_clause(int tag, const int *ls, int n) {
    if (!dout) return;
    putc(tag, dout);
    for (int i = 0; i < n; i++) {
        unsigned u = 2u * (unsigned)(ls[i] > 0 ? ls[i] : -ls[i]) + (ls[i] < 0);
        while (u > 127) {
            putc((int)(128 | (u & 127)), dout);
            u >>= 7;
        }
        putc((int)u, dout);
    }
    putc(0, dout);
}

static signed char *val; /* per variable: 0 unassigned, 1 true, -1 false */
static int *trail;
static int ntrail;
static int nvars;

static inline int lit_value(int l) {
    signed char s = val[l > 0 ? l : -l];
    return l > 0 ? s : -s;
}

static inline void set_true(int l) {
    int v = l > 0 ? l : -l;
    val[v] = l > 0 ? 1 : -1;
    trail[ntrail++] = v;
}

int main(int argc, char **argv) {
    if (argc != 3 && argc != 4) {
        fprintf(stderr, "usage: lratstrict2 CNF LRAT [DRAT_OUT]\n");
        return 2;
    }
    if (argc == 4) {
        dout = fopen(argv[3], "wb");
        if (!dout) fail("cannot open DRAT output", 0, 0);
        setvbuf(dout, NULL, _IOFBF, 1 << 20);
    }
    FILE *cf = fopen(argv[1], "rb");
    if (!cf) fail("cannot open CNF", 0, 0);
    Rd R = {cf, malloc(1 << 20), 0, 0, 0};
    /* header */
    for (;;) {
        rd_skip_ws(&R);
        int c = rd_peek(&R);
        if (c == 'c') {
            while ((c = rd_peek(&R)) >= 0 && c != '\n') R.p++;
            continue;
        }
        break;
    }
    char hdr[5] = {0};
    for (int i = 0; i < 5; i++) {
        int c = rd_peek(&R);
        if (c < 0) fail("truncated header", 0, 0);
        hdr[i] = (char)c;
        R.p++;
    }
    if (memcmp(hdr, "p cnf", 5) != 0) fail("bad header", 0, 0);
    long long V = 0, C = 0;
    if (rd_tok(&R, &V) != 0 || rd_tok(&R, &C) != 0 || V < 0 || C < 0 || V > 100000000LL) fail("bad header numbers", 0, 0);
    nvars = (int)V;
    val = calloc((size_t)nvars + 1, 1);
    trail = malloc(sizeof(int) * ((size_t)nvars + 1));
    hcap = 16;
    hkeys = calloc(hcap, sizeof(uint64_t));
    hvals = calloc(hcap, sizeof(Clause *));
    size_t lcap = 1024;
    int *lits = malloc(sizeof(int) * lcap);
    for (long long i = 1; i <= C; i++) {
        int k = 0;
        long long x;
        for (;;) {
            if (rd_tok(&R, &x) != 0) fail("truncated or bad CNF clause", i, 0);
            if (x == 0) break;
            if (x < -V || x > V) fail("CNF literal out of range", i, x);
            if ((size_t)k == lcap) lits = realloc(lits, sizeof(int) * (lcap *= 2));
            lits[k++] = (int)x;
        }
        Clause *c = malloc(sizeof(Clause) + sizeof(int) * (size_t)k);
        c->len = k;
        memcpy(c->lits, lits, sizeof(int) * (size_t)k);
        hinsert((uint64_t)i, c);
    }
    {
        long long x;
        if (rd_tok(&R, &x) != 2) fail("extra data after the declared clauses", x, 0);
    }
    fclose(cf);

    FILE *pf = fopen(argv[2], "rb");
    if (!pf) fail("cannot open LRAT", 0, 0);
    Rd P = {pf, R.buf, 0, 0, 0};
    long long last = C, steps = 0, dels = 0;
    size_t hcap2 = 1024;
    long long *hints = malloc(sizeof(long long) * hcap2);
    for (;;) {
        long long id;
        int t = rd_tok(&P, &id);
        if (t == 2) break;
        if (t != 0 || id <= 0) fail("bad step id", id, steps);
        long long x;
        t = rd_tok(&P, &x);
        if (t == 2) fail("truncated step", id, 0);
        if (t == 1) {
            for (;;) {
                if (rd_tok(&P, &x) != 0) fail("bad deletion list", id, 0);
                if (x == 0) break;
                if (x < 0) fail("negative id in deletion", id, x);
                long j = hfind((uint64_t)x);
                if (j < 0) fail("deletion of unknown clause", id, x);
                emit_clause('d', hvals[j]->lits, hvals[j]->len);
                free(hvals[j]);
                hvals[j] = NULL;
                hkeys[j] = HTOMB;
                hlive--;
                dels++;
            }
            continue;
        }
        if (id <= last) fail("addition id not increasing", id, last);
        int k = 0;
        while (x != 0) {
            if (x < -V || x > V) fail("lemma literal out of range", id, x);
            if ((size_t)k == lcap) lits = realloc(lits, sizeof(int) * (lcap *= 2));
            lits[k++] = (int)x;
            if (rd_tok(&P, &x) != 0) fail("bad lemma", id, 0);
        }
        int m = 0;
        for (;;) {
            if (rd_tok(&P, &x) != 0) fail("bad hint list", id, 0);
            if (x == 0) break;
            if (x < 0) fail("RAT hint (negative) not supported", id, x);
            if ((size_t)m == hcap2) hints = realloc(hints, sizeof(long long) * (hcap2 *= 2));
            hints[m++] = x;
        }
        /* RUP check */
        ntrail = 0;
        for (int i = 0; i < k; i++) {
            int l = lits[i];
            int s = lit_value(l);
            if (s == -1) continue;             /* duplicate literal */
            if (s == 1) fail("tautological lemma", id, l);
            set_true(-l);
        }
        int conflict = 0;
        for (int i = 0; i < m; i++) {
            if (conflict) fail("hints after conflict", id, hints[i]);
            long j = hfind((uint64_t)hints[i]);
            if (j < 0) fail("hint refers to unknown or deleted clause", id, hints[i]);
            Clause *c = hvals[j];
            int un = 0, nun = 0;
            for (int q = 0; q < c->len; q++) {
                int l = c->lits[q];
                int s = lit_value(l);
                if (s == 1) fail("hint clause satisfied", id, hints[i]);
                if (s == 0) {
                    if (nun == 0) {
                        un = l;
                        nun = 1;
                    } else if (l != un) {
                        nun = 2;
                    }
                }
            }
            if (nun == 2) fail("hint clause not unit", id, hints[i]);
            if (nun == 0)
                conflict = 1;
            else
                set_true(un);
        }
        if (!conflict) fail("no conflict after all hints", id, m);
        for (int i = 0; i < ntrail; i++) val[trail[i]] = 0;
        Clause *c = malloc(sizeof(Clause) + sizeof(int) * (size_t)k);
        c->len = k;
        memcpy(c->lits, lits, sizeof(int) * (size_t)k);
        hinsert((uint64_t)id, c);
        emit_clause('a', lits, k);
        last = id;
        steps++;
        if (k == 0) {
            if (dout && fclose(dout) != 0) fail("DRAT output write error", id, 0);
            dout = NULL;
            /* drain the rest without checking */
            while (fread(P.buf, 1, 1 << 20, pf) > 0) {
            }
            printf("c verified empty clause at id %lld after %lld additions, %lld deletions\ns VERIFIED\n", id, steps, dels);
            fflush(stdout);
            return 0;
        }
    }
    fail("end of proof without an empty clause", steps, dels);
    return 1;
}
