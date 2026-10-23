/*
 * check_gcdcqs_s.c -- route-2 (C) checker for certificate Format S: a gcDCQS(g^n : s), i.e. a
 * candelabra quadruple system CQS(g^n : s) with good colourable derived designs.
 *
 * Written only from LANE/README.md sections 1-3 (frozen 2026-10-17 16:20:13 PDT, sha256
 * 9bcd90d6f98e25ef4171c572158384cb63dd5250833b91771d61d5717e821a1b) and the definitions in
 * sources/tz/tan-zhou-2503.11934.txt: (1.1) chi' (LF 99-130); STS(v,h) and gcSTS (LF 205-220);
 * KF (LF 237-240); CS/CQS (LF 256-266); gcDCQS (LF 281-288).  The route-1 Python checkers were
 * not read.  No symmetry is assumed: every property is checked explicitly.
 *
 * Usage:   check_gcdcqs_s_c CERTIFICATE
 * Output:  exactly one line on stdout; exit status 0 (PASS) or 1 (FAIL):
 *   PASS v=.. n=.. g=.. s=.. blocks=.. colours=.. holefree=.. group_point_derived=.. stem_frames=..
 *       group_point_derived = derived triples listed and verified over all POINT sections,
 *       stem_frames         = FRAME classes verified over all STEMPOINT sections;
 *   FAIL line L: CATEGORY: message   (L = 1-based physical line; 0 = no line read).
 *
 * Format S: '#' starts a comment; blank lines are ignored; a line holds either one keyword with
 * its integer arguments or only non-negative decimal integers; strict order:
 *   GCDCQS v n g s / COLOURS r / HOLEFREE t / GROUPS + n lines of g points / STEM + one line of
 *   s points (no line if s = 0) / BLOCKS + lines of 4 points / one section "POINT x" per group
 *   point x (any order) holding "CLASS j" for j = 0..r-1 in order, each followed by lines of
 *   3 points / then one section "STEMPOINT a" per stem point a (any order) holding classes
 *   "FRAME k" (k = GROUPS index of the missed group), each followed by lines of 3 points.
 *
 * Checks, by failure category:
 *   FORMAT        tokens and token counts, keywords and their order, triple lines outside a
 *                 class, POINT after STEMPOINT, section point out of range, I/O
 *   PARAM         1 <= v <= 128; n, g >= 1; v = g*n + s; v-1 = 1 or 3 (mod 6); COLOURS r equals
 *                 chi'(v-1) of (1.1); v-g-s even and HOLEFREE t equals r - (v-g-s)/2; GROUPS
 *                 and STEM partition {0,...,v-1}
 *   BLOCK         a block has 4 distinct points in range; no block repeated; no 3-subset in two
 *                 blocks
 *   COVERAGE      no block contains a 3-subset of any S u G; then an explicit pass over all
 *                 C(v,3) 3-subsets: one inside some S u G lies in no block, any other in exactly
 *                 one block
 *   COLOURING     group point x: classes CLASS 0..r-1 in order, exactly r, each nonempty; a
 *                 triple has 3 distinct points in range, none equal to x, T u {x} is a block, no
 *                 triple is listed twice at x, the triples of a class are pairwise disjoint
 *   HOLEFREE      exactly t classes at x contain no point of (G_x u S) \ {x}
 *   FRAME         stem point a: FRAME k with 0 <= k < n; a triple has 3 distinct points in
 *                 range, none equal to a, T u {a} is a block, no triple is listed twice at a, its
 *                 points lie in X \ (S u G_k); a class is nonempty, pairwise disjoint and covers
 *                 all v-s-g points of X \ (S u G_k)
 *   COMPLETENESS  exactly one POINT section per group point and one STEMPOINT section per stem
 *                 point; the number of triples listed at a point equals the number of blocks
 *                 through it, so (no triple twice) its classes partition its derived design
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
#define STEM (-1)  /* grp[] value of a stem point */
#define UNSET (-2) /* grp[] value of a point not placed yet */

/* the four 3-subsets of a sorted 4-set, as index triples */
static const int SUB3[4][3] = {{0, 1, 2}, {0, 1, 3}, {0, 2, 3}, {1, 2, 3}};

/* current line */
static long lineno;
static char *tok[MAXTOK];
static int ntok;

/* header, groups, stem */
static long npts, ngroups, gsize, ssize, rcol, thole;
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

/* POINT / STEMPOINT sections and their classes */
static long section_line[MAXV]; /* line of the section of each point, 0 if none yet */
static int sec_kind;            /* 0 none, 1 POINT x, 2 STEMPOINT a */
static int sec_pt, sec_id, sec_classes, sec_avoid, stem_phase;
static long sec_line, sec_listed;
static int listed_sec[MAXB]; /* sec_id of the section that listed (block minus its point) */
static long listed_line[MAXB];
static int cls_open, cls_id, cls_touches_hole;
static long cls_line, cls_label, cls_trips;
static int mark_cls[MAXV]; /* cls_id of the class covering the point */
static long mark_line[MAXV];
static long total_group_derived, total_stem_frames;

enum {
    ST_HEADER,
    ST_COLOURS,
    ST_HOLEFREE,
    ST_GROUPS_KW,
    ST_GROUPS,
    ST_STEM_KW,
    ST_STEM,
    ST_BLOCKS_KW,
    ST_BLOCKS,
    ST_DERIVED
};
static int state = ST_HEADER;
static const char *const EXPECTED[ST_BLOCKS] = {
    "GCDCQS v n g s", "COLOURS r", "HOLEFREE t", "GROUPS", "a group line", "STEM", "the stem line",
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

/* chi'(w) by (1.1), for w = 1 or 3 (mod 6) */
static long chi_prime(long w)
{
    if (w % 6 == 3)
        return (w - 1) / 2;
    if (w == 7)
        return 7;
    if (w == 13)
        return 8;
    return (w + 1) / 2;
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

/* 1 if the 3-subset {a,b,c} lies inside S u G for some group G (one such G in *gi), else 0 */
static int in_stem_group(int a, int b, int c, int *gi)
{
    int p[3], i, g0 = UNSET;

    p[0] = a;
    p[1] = b;
    p[2] = c;
    for (i = 0; i < 3; i++) {
        if (grp[p[i]] == STEM)
            continue;
        if (g0 == UNSET)
            g0 = grp[p[i]];
        else if (grp[p[i]] != g0)
            return 0;
    }
    *gi = g0 == UNSET ? 0 : g0;
    return 1;
}

static int block_has(int b, int x)
{
    return blk[b][0] == x || blk[b][1] == x || blk[b][2] == x || blk[b][3] == x;
}

/* Put point p into group g (or the stem, g = STEM); GROUPS and STEM must partition X. */
static void place(long p, int g)
{
    if (p >= npts)
        fail(lineno, "PARAM", "point %ld out of range 0..%ld in GROUPS/STEM", p, npts - 1);
    if (grp[p] != UNSET)
        fail(lineno, "PARAM",
             "point %ld appears twice in GROUPS/STEM (first at line %ld): not a partition of X", p,
             placed_line[p]);
    grp[p] = g;
    placed_line[p] = lineno;
}

static void add_block(void)
{
    int q[4], i, j, a, b, c, e, o, gi;

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
    sort_small(q, 4);
    for (i = 0; i < 4; i++) {
        a = q[SUB3[i][0]];
        b = q[SUB3[i][1]];
        c = q[SUB3[i][2]];
        if (in_stem_group(a, b, c, &gi))
            fail(lineno, "COVERAGE", "block {%d,%d,%d,%d} contains the 3-subset {%d,%d,%d} of S u G_%d",
                 q[0], q[1], q[2], q[3], a, b, c, gi);
    }
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

/* Explicit pass over all C(v,3) 3-subsets of X. */
static void coverage(void)
{
    int a, b, c, e, cnt, gi;

    for (a = 0; a < npts; a++)
        for (b = a + 1; b < npts; b++)
            for (c = b + 1; c < npts; c++) {
                e = tri[a][b][c];
                cnt = e != 0;
                if (in_stem_group(a, b, c, &gi)) {
                    if (cnt != 0)
                        fail(blk_line[e - 1], "COVERAGE", "3-subset {%d,%d,%d} of S u G_%d lies in a block",
                             a, b, c, gi);
                } else if (cnt != 1) {
                    fail(blocks_line, "COVERAGE",
                         "3-subset {%d,%d,%d} (not inside any S u G) lies in %d blocks, expected 1", a,
                         b, c, cnt);
                }
            }
}

static void begin_class(long label)
{
    cls_open = 1;
    cls_line = lineno;
    cls_label = label;
    cls_id++;
    cls_trips = 0;
    cls_touches_hole = 0;
}

static void end_class(void)
{
    long want = npts - ssize - gsize;

    if (!cls_open)
        return;
    cls_open = 0;
    if (sec_kind == 1) {
        if (cls_trips == 0)
            fail(cls_line, "COLOURING", "CLASS %ld at POINT %d is empty", cls_label, sec_pt);
        if (!cls_touches_hole)
            sec_avoid++;
    } else {
        if (cls_trips == 0)
            fail(cls_line, "FRAME", "FRAME %ld class at STEMPOINT %d is empty", cls_label, sec_pt);
        if (3 * cls_trips != want)
            fail(cls_line, "FRAME",
                 "FRAME %ld class at STEMPOINT %d covers %ld of the %ld points of X \\ (S u G_%ld)",
                 cls_label, sec_pt, 3 * cls_trips, want, cls_label);
        total_stem_frames++;
    }
    sec_classes++;
}

static void begin_section(int kind, int p)
{
    sec_kind = kind;
    sec_pt = p;
    sec_line = lineno;
    sec_id++;
    sec_listed = 0;
    sec_classes = 0;
    sec_avoid = 0;
    section_line[p] = lineno;
}

static void end_section(void)
{
    if (sec_kind == 0)
        return;
    end_class();
    if (sec_kind == 1) {
        if (sec_classes != rcol)
            fail(sec_line, "COLOURING", "POINT %d has %d classes, expected r=%ld", sec_pt, sec_classes,
                 rcol);
        if (sec_listed != deg[sec_pt])
            fail(sec_line, "COMPLETENESS", "POINT %d lists %ld derived triples, but %d blocks contain it",
                 sec_pt, sec_listed, deg[sec_pt]);
        if (sec_avoid != thole)
            fail(sec_line, "HOLEFREE",
                 "POINT %d has %d classes avoiding (G_x u S) \\ {x}, expected t=%ld", sec_pt, sec_avoid,
                 thole);
        total_group_derived += sec_listed;
    } else if (sec_listed != deg[sec_pt]) {
        fail(sec_line, "COMPLETENESS", "STEMPOINT %d lists %ld derived triples, but %d blocks contain it",
             sec_pt, sec_listed, deg[sec_pt]);
    }
    sec_kind = 0;
}

static void add_triple(void)
{
    const char *cat = sec_kind == 1 ? "COLOURING" : "FRAME";
    const char *sec = sec_kind == 1 ? "POINT" : "STEMPOINT";
    int p[3], i, j, e, b;

    if (!cls_open)
        fail(lineno, "FORMAT", "triple line before the first %s of %s %d",
             sec_kind == 1 ? "CLASS" : "FRAME", sec, sec_pt);
    if (ntok != 3)
        fail(lineno, "FORMAT", "triple line must list 3 points, found %d tokens", ntok);
    for (i = 0; i < 3; i++) {
        long y = num(i);
        if (y >= npts)
            fail(lineno, cat, "point %ld out of range 0..%ld", y, npts - 1);
        p[i] = (int)y;
    }
    for (i = 0; i < 3; i++)
        for (j = i + 1; j < 3; j++)
            if (p[i] == p[j])
                fail(lineno, cat, "triple repeats point %d", p[i]);
    for (i = 0; i < 3; i++)
        if (p[i] == sec_pt)
            fail(lineno, cat, "triple contains the section point %d itself", sec_pt);
    sort_small(p, 3);
    e = tri[p[0]][p[1]][p[2]];
    if (e == 0 || !block_has(e - 1, sec_pt))
        fail(lineno, cat, "{%d,%d,%d} u {%d} is not a block", p[0], p[1], p[2], sec_pt);
    b = e - 1;
    if (listed_sec[b] == sec_id)
        fail(lineno, cat, "triple {%d,%d,%d} listed twice at %s %d (first at line %ld)", p[0], p[1], p[2],
             sec, sec_pt, listed_line[b]);
    if (sec_kind == 2)
        for (i = 0; i < 3; i++)
            if (grp[p[i]] == STEM || grp[p[i]] == cls_label)
                fail(lineno, "FRAME", "point %d lies in S u G_%ld, outside X \\ (S u G_%ld)", p[i],
                     cls_label, cls_label);
    for (i = 0; i < 3; i++)
        if (mark_cls[p[i]] == cls_id)
            fail(lineno, cat, "point %d is already covered by this class (line %ld)", p[i],
                 mark_line[p[i]]);
    for (i = 0; i < 3; i++) {
        mark_cls[p[i]] = cls_id;
        mark_line[p[i]] = lineno;
        if (sec_kind == 1 && (grp[p[i]] == STEM || grp[p[i]] == grp[sec_pt]))
            cls_touches_hole = 1;
    }
    listed_sec[b] = sec_id;
    listed_line[b] = lineno;
    sec_listed++;
    cls_trips++;
}

/* A line after BLOCKS: a section or class keyword, or a triple. */
static void derived_line(void)
{
    long x;

    if (!keyword_line()) {
        add_triple();
        return;
    }
    if (is_kw("POINT")) {
        need_tokens(2, "POINT x");
        x = num(1);
        end_section();
        if (stem_phase)
            fail(lineno, "FORMAT", "POINT section after a STEMPOINT section");
        if (x >= npts)
            fail(lineno, "FORMAT", "POINT %ld out of range 0..%ld", x, npts - 1);
        if (grp[x] == STEM)
            fail(lineno, "COMPLETENESS", "POINT %ld names a stem point (stem points take STEMPOINT)", x);
        if (section_line[x] != 0)
            fail(lineno, "COMPLETENESS", "second POINT section for %ld (first at line %ld)", x,
                 section_line[x]);
        begin_section(1, (int)x);
    } else if (is_kw("STEMPOINT")) {
        need_tokens(2, "STEMPOINT a");
        x = num(1);
        end_section();
        if (x >= npts)
            fail(lineno, "FORMAT", "STEMPOINT %ld out of range 0..%ld", x, npts - 1);
        if (grp[x] != STEM)
            fail(lineno, "COMPLETENESS", "STEMPOINT %ld is not a stem point", x);
        if (section_line[x] != 0)
            fail(lineno, "COMPLETENESS", "second STEMPOINT section for %ld (first at line %ld)", x,
                 section_line[x]);
        stem_phase = 1;
        begin_section(2, (int)x);
    } else if (is_kw("CLASS")) {
        need_tokens(2, "CLASS j");
        x = num(1);
        if (sec_kind != 1)
            fail(lineno, "FORMAT", "CLASS outside a POINT section");
        end_class();
        if (x != sec_classes)
            fail(lineno, "COLOURING", "CLASS %ld at POINT %d out of order (expected CLASS %d)", x, sec_pt,
                 sec_classes);
        if (x >= rcol)
            fail(lineno, "COLOURING", "CLASS %ld at POINT %d: more than r=%ld classes", x, sec_pt, rcol);
        begin_class(x);
    } else if (is_kw("FRAME")) {
        need_tokens(2, "FRAME k");
        x = num(1);
        if (sec_kind != 2)
            fail(lineno, "FORMAT", "FRAME outside a STEMPOINT section");
        end_class();
        if (x >= ngroups)
            fail(lineno, "FRAME", "FRAME %ld at STEMPOINT %d: group index out of range 0..%ld", x, sec_pt,
                 ngroups - 1);
        begin_class(x);
    } else {
        fail(lineno, "FORMAT", "unexpected keyword '%.40s' after BLOCKS", tok[0]);
    }
}

static void dispatch(void)
{
    long d;
    int i;

    switch (state) {
    case ST_HEADER:
        expect_keyword("GCDCQS", 5, "GCDCQS v n g s");
        npts = num(1);
        ngroups = num(2);
        gsize = num(3);
        ssize = num(4);
        if (npts < 1 || npts > MAXV)
            fail(lineno, "PARAM", "v=%ld outside the supported range 1..%d", npts, MAXV);
        if (ngroups < 1 || gsize < 1)
            fail(lineno, "PARAM", "need n >= 1 and g >= 1 (n=%ld, g=%ld)", ngroups, gsize);
        if (ngroups > MAXV || gsize > MAXV || gsize * ngroups + ssize != npts)
            fail(lineno, "PARAM", "v=%ld differs from g*n+s (g=%ld, n=%ld, s=%ld)", npts, gsize, ngroups,
                 ssize);
        if ((npts - 1) % 6 != 1 && (npts - 1) % 6 != 3)
            fail(lineno, "PARAM", "v-1=%ld is not 1 or 3 (mod 6)", npts - 1);
        state = ST_COLOURS;
        break;
    case ST_COLOURS:
        expect_keyword("COLOURS", 2, "COLOURS r");
        rcol = num(1);
        if (rcol != chi_prime(npts - 1))
            fail(lineno, "PARAM", "COLOURS %ld, but chi'(v-1)=chi'(%ld)=%ld by (1.1)", rcol, npts - 1,
                 chi_prime(npts - 1));
        state = ST_HOLEFREE;
        break;
    case ST_HOLEFREE:
        expect_keyword("HOLEFREE", 2, "HOLEFREE t");
        thole = num(1);
        d = npts - gsize - ssize;
        if (d % 2 != 0)
            fail(lineno, "PARAM", "v-g-s=%ld is odd, so t = r-(v-g-s)/2 is undefined", d);
        if (thole != rcol - d / 2)
            fail(lineno, "PARAM", "HOLEFREE %ld, but r-(v-g-s)/2=%ld", thole, rcol - d / 2);
        state = ST_GROUPS_KW;
        break;
    case ST_GROUPS_KW:
        expect_keyword("GROUPS", 1, "GROUPS");
        state = ST_GROUPS;
        break;
    case ST_GROUPS:
        if (keyword_line())
            fail(lineno, "FORMAT", "expected group line %d of %ld, found '%.40s'", groups_read + 1,
                 ngroups, tok[0]);
        if (ntok != gsize)
            fail(lineno, "FORMAT", "group line must list g=%ld points, found %d tokens", gsize, ntok);
        for (i = 0; i < ntok; i++)
            place(num(i), groups_read);
        if (++groups_read == ngroups)
            state = ST_STEM_KW;
        break;
    case ST_STEM_KW:
        expect_keyword("STEM", 1, "STEM");
        state = ssize > 0 ? ST_STEM : ST_BLOCKS_KW;
        break;
    case ST_STEM:
        if (keyword_line())
            fail(lineno, "FORMAT", "expected the stem line of s=%ld points, found '%.40s'", ssize, tok[0]);
        if (ntok != ssize)
            fail(lineno, "FORMAT", "stem line must list s=%ld points, found %d tokens", ssize, ntok);
        for (i = 0; i < ntok; i++)
            place(num(i), STEM);
        state = ST_BLOCKS_KW;
        break;
    case ST_BLOCKS_KW:
        expect_keyword("BLOCKS", 1, "BLOCKS");
        for (i = 0; i < npts; i++)
            if (grp[i] == UNSET)
                fail(lineno, "PARAM", "point %d lies in no group and not in the stem", i);
        blocks_line = lineno;
        state = ST_BLOCKS;
        break;
    case ST_BLOCKS:
        if (!keyword_line()) {
            add_block();
            break;
        }
        if (!is_kw("POINT") && !is_kw("STEMPOINT"))
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
    for (p = 0; p < npts; p++) {
        if (section_line[p] != 0)
            continue;
        if (grp[p] == STEM)
            fail(lineno, "COMPLETENESS", "no STEMPOINT section for stem point %d", p);
        fail(lineno, "COMPLETENESS", "no POINT section for group point %d", p);
    }
}

int main(int argc, char **argv)
{
    FILE *f;
    char *buf = NULL;
    size_t cap = 0;
    ssize_t len;
    int i;

    if (argc != 2)
        fail(0, "FORMAT", "usage: check_gcdcqs_s_c CERTIFICATE");
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
    printf("PASS v=%ld n=%ld g=%ld s=%ld blocks=%d colours=%ld holefree=%ld group_point_derived=%ld "
           "stem_frames=%ld\n",
           npts, ngroups, gsize, ssize, nblk, rcol, thole, total_group_derived, total_stem_frames);
    return 0;
}
