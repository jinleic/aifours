/*
 * check_gdd34.c -- route-2 (C) checker for certificate Format D: an FDGDD(3,4,k{m}) or an
 * RDGDD(3,4,k{m}), i.e. a GDD(3,4,km) of type m^k whose derived design at every point is a
 * Kirkman frame KF(m^(k-1)) (FDGDD) or a resolvable GDD(2,3,m(k-1)) of type m^(k-1) (RDGDD).
 *
 * Written only from LANE/README.md sections 1-3 (frozen 2026-10-17 16:20:13 PDT, sha256
 * 9bcd90d6f98e25ef4171c572158384cb63dd5250833b91771d61d5717e821a1b) and the definitions in
 * sources/tz/tan-zhou-2503.11934.txt: GDD, PPC/PC, resolvable (LF 49-72); KF, RDGDD, FDGDD
 * (LF 237-247).  The route-1 Python checkers were not read.  No symmetry is assumed: every
 * property is checked explicitly.
 *
 * Usage:   check_gdd34_c CERTIFICATE
 * Output:  exactly one line on stdout; exit status 0 (PASS) or 1 (FAIL):
 *   PASS kind=.. k=.. m=.. v=.. blocks=.. classes=.. derived_triples=..
 *       classes         = FRAME / PC classes verified over all POINT sections,
 *       derived_triples = derived triples listed and verified over all POINT sections;
 *   FAIL line L: CATEGORY: message   (L = 1-based physical line; 0 = no line read).
 *
 * Format D: '#' starts a comment; blank lines are ignored; a line holds either one keyword with
 * its arguments or only non-negative decimal integers; strict order:
 *   GDD34 KIND k m (KIND = FDGDD or RDGDD) / GROUPS + k lines of m points / BLOCKS + lines of
 *   4 points / one section "POINT x" per point x (any order) holding classes "FRAME j" (FDGDD;
 *   j = GROUPS index of the missed group, j != group of x) or "PC j" (RDGDD; j = 0,1,... in
 *   order), each followed by lines of 3 points.
 *
 * Checks, by failure category:
 *   FORMAT        tokens and token counts, keywords and their order, KIND, k >= 1, m >= 1,
 *                 k*m <= 128, GROUPS partition {0,...,km-1}, class keyword matching KIND,
 *                 triple lines outside a class, POINT out of range, I/O
 *   BLOCK         a block has 4 distinct points in range lying in 4 distinct groups
 *                 (transverse); no block repeated; no 3-subset in two blocks
 *   COVERAGE      explicit pass over all C(km,3) 3-subsets: one meeting three distinct groups
 *                 lies in exactly one block, any other in no block
 *   CLASS         FRAME j with 0 <= j < k and j != group of x (FDGDD), or PC j in order
 *                 0,1,... (RDGDD); a triple has 3 distinct points in range, none equal to x,
 *                 T u {x} is a block, no triple is listed twice at x, its points lie in
 *                 X \ (G_x u G_j) (FDGDD) or X \ G_x (RDGDD); a class is nonempty, pairwise
 *                 disjoint and covers all km-2m points of X \ (G_x u G_j) (FDGDD) or all km-m
 *                 points of X \ G_x (RDGDD)
 *   COMPLETENESS  exactly one POINT section per point; the number of triples listed at x equals
 *                 the number of blocks through x, so (no triple twice) the classes partition
 *                 the derived design at x
 */
#include <ctype.h>
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

#define MAXV 128
#define MAXB 85344 /* floor(C(128,3)/4): one more block would repeat a 3-subset */
#define MAXTOK 256
#define UNSET (-1) /* grp[] value of a point not placed yet */
#define FDGDD 1
#define RDGDD 2

/* the four 3-subsets of a sorted 4-set, as index triples */
static const int SUB3[4][3] = {{0, 1, 2}, {0, 1, 3}, {0, 2, 3}, {1, 2, 3}};

/* current line */
static long lineno;
static char *tok[MAXTOK];
static int ntok;

/* header and groups */
static long kgroups, msize, npts;
static int kind;
static int grp[MAXV];
static long placed_line[MAXV];
static int groups_read;

/* blocks */
static int tri[MAXV][MAXV][MAXV]; /* sorted a<b<c: 1 + index of the block containing it, or 0 */
static int blk[MAXB][4];
static long blk_line[MAXB];
static int nblk;
static int deg[MAXV];
static long blocks_line;

/* POINT sections and their classes */
static long section_line[MAXV]; /* line of the section of each point, 0 if none yet */
static int in_section, sec_pt, sec_id, sec_classes;
static long sec_line, sec_listed;
static int listed_sec[MAXB]; /* sec_id of the section that listed (block minus its point) */
static long listed_line[MAXB];
static int cls_open, cls_id;
static long cls_line, cls_label, cls_trips;
static int mark_cls[MAXV]; /* cls_id of the class covering the point */
static long mark_line[MAXV];
static long total_classes, total_derived;

enum { ST_HEADER, ST_GROUPS_KW, ST_GROUPS, ST_BLOCKS_KW, ST_BLOCKS, ST_DERIVED };
static int state = ST_HEADER;
static const char *const EXPECTED[ST_BLOCKS] = {"GDD34 KIND k m", "GROUPS", "a group line",
                                                "BLOCKS"};

static void fail(long line, const char *cat, const char *fmt, ...)
    __attribute__((noreturn, format(printf, 3, 4)));

static void fail(long line, const char *cat, const char *fmt, ...)
{
    va_list ap;

    printf("FAIL line %ld: %s: ", line, cat);
    va_start(ap, fmt);
    vprintf(fmt, ap);
    va_end(ap);
    putchar('\n');
    exit(1);
}

/* Strip a '#' comment, then split the line into whitespace-separated tokens. */
static void split(char *s)
{
    char *hash = strchr(s, '#');

    if (hash != NULL)
        *hash = '\0';
    ntok = 0;
    for (;;) {
        while (*s != '\0' && isspace((unsigned char)*s))
            s++;
        if (*s == '\0')
            return;
        if (ntok == MAXTOK)
            fail(lineno, "FORMAT", "more than %d tokens on one line", MAXTOK);
        tok[ntok++] = s;
        while (*s != '\0' && !isspace((unsigned char)*s))
            s++;
        if (*s != '\0')
            *s++ = '\0';
    }
}

/* Token i as a non-negative decimal integer. */
static long num(int i)
{
    const char *s;
    long x = 0;

    for (s = tok[i]; *s != '\0'; s++) {
        if (*s < '0' || *s > '9')
            fail(lineno, "FORMAT", "token '%.40s' is not a non-negative decimal integer", tok[i]);
        if (x > 99999999L)
            fail(lineno, "FORMAT", "integer '%.40s' is too large", tok[i]);
        x = 10 * x + (*s - '0');
    }
    return x;
}

static int keyword_line(void)
{
    return isalpha((unsigned char)tok[0][0]) != 0;
}

static int is_kw(const char *k)
{
    return strcmp(tok[0], k) == 0;
}

static void need_tokens(int k, const char *form)
{
    if (ntok != k)
        fail(lineno, "FORMAT", "line must read '%s' (%d tokens), found %d tokens", form, k, ntok);
}

static void expect_keyword(const char *k, int ntokens, const char *form)
{
    if (!is_kw(k))
        fail(lineno, "FORMAT", "expected '%s', found '%.40s'", form, tok[0]);
    need_tokens(ntokens, form);
}

static void sort_small(int *a, int len)
{
    int i, j, x;

    for (i = 1; i < len; i++) {
        x = a[i];
        for (j = i; j > 0 && a[j - 1] > x; j--)
            a[j] = a[j - 1];
        a[j] = x;
    }
}

static int block_has(int b, int x)
{
    return blk[b][0] == x || blk[b][1] == x || blk[b][2] == x || blk[b][3] == x;
}

/* Put point p into group g; GROUPS must partition X. */
static void place(long p, int g)
{
    if (p >= npts)
        fail(lineno, "FORMAT", "point %ld out of range 0..%ld in GROUPS", p, npts - 1);
    if (grp[p] != UNSET)
        fail(lineno, "FORMAT",
             "point %ld appears twice in GROUPS (first at line %ld): not a partition of X", p,
             placed_line[p]);
    grp[p] = g;
    placed_line[p] = lineno;
}

static void add_block(void)
{
    int q[4], i, j, a, b, c, e, o;

    if (ntok != 4)
        fail(lineno, "FORMAT", "block line must list 4 points, found %d tokens", ntok);
    for (i = 0; i < 4; i++) {
        long x = num(i);
        if (x >= npts)
            fail(lineno, "BLOCK", "point %ld out of range 0..%ld", x, npts - 1);
        q[i] = (int)x;
    }
    for (i = 0; i < 4; i++)
        for (j = i + 1; j < 4; j++)
            if (q[i] == q[j])
                fail(lineno, "BLOCK", "block repeats point %d", q[i]);
    for (i = 0; i < 4; i++)
        for (j = i + 1; j < 4; j++)
            if (grp[q[i]] == grp[q[j]])
                fail(lineno, "BLOCK", "block is not transverse: points %d and %d both lie in group %d",
                     q[i], q[j], grp[q[i]]);
    sort_small(q, 4);
    for (i = 0; i < 4; i++) {
        a = q[SUB3[i][0]];
        b = q[SUB3[i][1]];
        c = q[SUB3[i][2]];
        e = tri[a][b][c];
        if (e != 0) {
            o = e - 1;
            if (blk[o][0] == q[0] && blk[o][1] == q[1] && blk[o][2] == q[2] && blk[o][3] == q[3])
                fail(lineno, "BLOCK", "repeated block {%d,%d,%d,%d} (first at line %ld)", q[0], q[1],
                     q[2], q[3], blk_line[o]);
            fail(lineno, "BLOCK", "3-subset {%d,%d,%d} lies in two blocks (lines %ld and %ld)", a, b,
                 c, blk_line[o], lineno);
        }
    }
    if (nblk == MAXB)
        fail(lineno, "BLOCK", "more than %d blocks", MAXB);
    for (i = 0; i < 4; i++) {
        tri[q[SUB3[i][0]]][q[SUB3[i][1]]][q[SUB3[i][2]]] = nblk + 1;
        blk[nblk][i] = q[i];
        deg[q[i]]++;
    }
    blk_line[nblk] = lineno;
    nblk++;
}

/* Explicit pass over all C(km,3) 3-subsets of X. */
static void coverage(void)
{
    int a, b, c, e, cnt, transverse;

    for (a = 0; a < npts; a++)
        for (b = a + 1; b < npts; b++)
            for (c = b + 1; c < npts; c++) {
                e = tri[a][b][c];
                cnt = e != 0;
                transverse = grp[a] != grp[b] && grp[a] != grp[c] && grp[b] != grp[c];
                if (transverse && cnt != 1)
                    fail(blocks_line, "COVERAGE",
                         "3-subset {%d,%d,%d} meets three groups but lies in %d blocks, expected 1", a,
                         b, c, cnt);
                if (!transverse && cnt != 0)
                    fail(blk_line[e - 1], "COVERAGE",
                         "3-subset {%d,%d,%d} with two points in one group lies in a block", a, b, c);
            }
}

static void begin_class(long label)
{
    cls_open = 1;
    cls_line = lineno;
    cls_label = label;
    cls_id++;
    cls_trips = 0;
}

static void end_class(void)
{
    const char *name = kind == FDGDD ? "FRAME" : "PC";
    long want = kind == FDGDD ? npts - 2 * msize : npts - msize;

    if (!cls_open)
        return;
    cls_open = 0;
    if (cls_trips == 0)
        fail(cls_line, "CLASS", "%s %ld at POINT %d is empty", name, cls_label, sec_pt);
    if (3 * cls_trips != want)
        fail(cls_line, "CLASS", "%s %ld at POINT %d covers %ld of the %ld points of %s", name, cls_label,
             sec_pt, 3 * cls_trips, want, kind == FDGDD ? "X \\ (G_x u G_j)" : "X \\ G_x");
    sec_classes++;
    total_classes++;
}

static void begin_section(int p)
{
    in_section = 1;
    sec_pt = p;
    sec_line = lineno;
    sec_id++;
    sec_listed = 0;
    sec_classes = 0;
    section_line[p] = lineno;
}

static void end_section(void)
{
    if (!in_section)
        return;
    end_class();
    if (sec_listed != deg[sec_pt])
        fail(sec_line, "COMPLETENESS", "POINT %d lists %ld derived triples, but %d blocks contain it",
             sec_pt, sec_listed, deg[sec_pt]);
    total_derived += sec_listed;
    in_section = 0;
}

static void add_triple(void)
{
    int p[3], i, j, e, b;

    if (!cls_open)
        fail(lineno, "FORMAT", "triple line before the first class of POINT %d", sec_pt);
    if (ntok != 3)
        fail(lineno, "FORMAT", "triple line must list 3 points, found %d tokens", ntok);
    for (i = 0; i < 3; i++) {
        long y = num(i);
        if (y >= npts)
            fail(lineno, "CLASS", "point %ld out of range 0..%ld", y, npts - 1);
        p[i] = (int)y;
    }
    for (i = 0; i < 3; i++)
        for (j = i + 1; j < 3; j++)
            if (p[i] == p[j])
                fail(lineno, "CLASS", "triple repeats point %d", p[i]);
    for (i = 0; i < 3; i++)
        if (p[i] == sec_pt)
            fail(lineno, "CLASS", "triple contains the section point %d itself", sec_pt);
    sort_small(p, 3);
    e = tri[p[0]][p[1]][p[2]];
    if (e == 0 || !block_has(e - 1, sec_pt))
        fail(lineno, "CLASS", "{%d,%d,%d} u {%d} is not a block", p[0], p[1], p[2], sec_pt);
    b = e - 1;
    if (listed_sec[b] == sec_id)
        fail(lineno, "CLASS", "triple {%d,%d,%d} listed twice at POINT %d (first at line %ld)", p[0], p[1],
             p[2], sec_pt, listed_line[b]);
    for (i = 0; i < 3; i++) {
        if (grp[p[i]] == grp[sec_pt])
            fail(lineno, "CLASS", "point %d lies in G_%d, the group of POINT %d", p[i], grp[sec_pt],
                 sec_pt);
        if (kind == FDGDD && grp[p[i]] == cls_label)
            fail(lineno, "CLASS", "point %d lies in G_%ld, the group missed by FRAME %ld", p[i],
                 cls_label, cls_label);
    }
    for (i = 0; i < 3; i++)
        if (mark_cls[p[i]] == cls_id)
            fail(lineno, "CLASS", "point %d is already covered by this class (line %ld)", p[i],
                 mark_line[p[i]]);
    for (i = 0; i < 3; i++) {
        mark_cls[p[i]] = cls_id;
        mark_line[p[i]] = lineno;
    }
    listed_sec[b] = sec_id;
    listed_line[b] = lineno;
    sec_listed++;
    cls_trips++;
}

/* A line after BLOCKS: POINT, a class keyword, or a triple. */
static void derived_line(void)
{
    long x;
    int frame;

    if (!keyword_line()) {
        add_triple();
        return;
    }
    if (is_kw("POINT")) {
        need_tokens(2, "POINT x");
        x = num(1);
        end_section();
        if (x >= npts)
            fail(lineno, "FORMAT", "POINT %ld out of range 0..%ld", x, npts - 1);
        if (section_line[x] != 0)
            fail(lineno, "COMPLETENESS", "second POINT section for %ld (first at line %ld)", x,
                 section_line[x]);
        begin_section((int)x);
        return;
    }
    frame = is_kw("FRAME");
    if (!frame && !is_kw("PC"))
        fail(lineno, "FORMAT", "unexpected keyword '%.40s' after BLOCKS", tok[0]);
    need_tokens(2, frame ? "FRAME j" : "PC j");
    x = num(1);
    if (frame && kind != FDGDD)
        fail(lineno, "FORMAT", "FRAME class in an RDGDD certificate (its classes are 'PC j')");
    if (!frame && kind != RDGDD)
        fail(lineno, "FORMAT", "PC class in an FDGDD certificate (its classes are 'FRAME j')");
    end_class();
    if (frame) {
        if (x >= kgroups)
            fail(lineno, "CLASS", "FRAME %ld at POINT %d: group index out of range 0..%ld", x, sec_pt,
                 kgroups - 1);
        if (x == grp[sec_pt])
            fail(lineno, "CLASS", "FRAME %ld at POINT %d names the group of the point itself", x, sec_pt);
    } else if (x != sec_classes) {
        fail(lineno, "CLASS", "PC %ld at POINT %d out of order (expected PC %d)", x, sec_pt, sec_classes);
    }
    begin_class(x);
}

static void dispatch(void)
{
    int i;

    switch (state) {
    case ST_HEADER:
        expect_keyword("GDD34", 4, "GDD34 KIND k m");
        if (strcmp(tok[1], "FDGDD") == 0)
            kind = FDGDD;
        else if (strcmp(tok[1], "RDGDD") == 0)
            kind = RDGDD;
        else
            fail(lineno, "FORMAT", "KIND must be FDGDD or RDGDD, found '%.40s'", tok[1]);
        kgroups = num(2);
        msize = num(3);
        if (kgroups < 1 || msize < 1 || kgroups > MAXV || msize > MAXV || kgroups * msize > MAXV)
            fail(lineno, "FORMAT", "need k >= 1, m >= 1 and k*m <= %d (k=%ld, m=%ld)", MAXV, kgroups,
                 msize);
        npts = kgroups * msize;
        state = ST_GROUPS_KW;
        break;
    case ST_GROUPS_KW:
        expect_keyword("GROUPS", 1, "GROUPS");
        state = ST_GROUPS;
        break;
    case ST_GROUPS:
        if (keyword_line())
            fail(lineno, "FORMAT", "expected group line %d of %ld, found '%.40s'", groups_read + 1,
                 kgroups, tok[0]);
        if (ntok != msize)
            fail(lineno, "FORMAT", "group line must list m=%ld points, found %d tokens", msize, ntok);
        for (i = 0; i < ntok; i++)
            place(num(i), groups_read);
        if (++groups_read == kgroups)
            state = ST_BLOCKS_KW;
        break;
    case ST_BLOCKS_KW:
        expect_keyword("BLOCKS", 1, "BLOCKS");
        for (i = 0; i < npts; i++)
            if (grp[i] == UNSET)
                fail(lineno, "FORMAT", "point %d lies in no group", i);
        blocks_line = lineno;
        state = ST_BLOCKS;
        break;
    case ST_BLOCKS:
        if (!keyword_line()) {
            add_block();
            break;
        }
        if (!is_kw("POINT"))
            fail(lineno, "FORMAT", "unexpected keyword '%.40s' in the BLOCKS section", tok[0]);
        coverage();
        state = ST_DERIVED;
        derived_line();
        break;
    default:
        derived_line();
        break;
    }
}

static void finish(void)
{
    int p;

    if (state < ST_BLOCKS)
        fail(lineno, "FORMAT", "unexpected end of file: expected %s", EXPECTED[state]);
    if (state == ST_BLOCKS)
        coverage();
    end_section();
    for (p = 0; p < npts; p++)
        if (section_line[p] == 0)
            fail(lineno, "COMPLETENESS", "no POINT section for point %d", p);
}

int main(int argc, char **argv)
{
    FILE *f;
    char *buf = NULL;
    size_t cap = 0;
    ssize_t len;
    int i;

    if (argc != 2)
        fail(0, "FORMAT", "usage: check_gdd34_c CERTIFICATE");
    f = fopen(argv[1], "r");
    if (f == NULL)
        fail(0, "FORMAT", "cannot open '%s'", argv[1]);
    for (i = 0; i < MAXV; i++)
        grp[i] = UNSET;
    while ((len = getline(&buf, &cap, f)) != -1) {
        lineno++;
        if ((size_t)len != strlen(buf))
            fail(lineno, "FORMAT", "NUL byte in line");
        split(buf);
        if (ntok > 0)
            dispatch();
    }
    if (ferror(f))
        fail(lineno, "FORMAT", "read error");
    fclose(f);
    free(buf);
    finish();
    printf("PASS kind=%s k=%ld m=%ld v=%ld blocks=%d classes=%ld derived_triples=%ld\n",
           kind == FDGDD ? "FDGDD" : "RDGDD", kgroups, msize, npts, nblk, total_classes, total_derived);
    return 0;
}
