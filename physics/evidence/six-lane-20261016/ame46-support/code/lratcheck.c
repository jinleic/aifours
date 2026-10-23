/* lratcheck.c -- independent LRAT proof checker (RUP hints only) for lane ame46-support.
 *
 * Usage: lratcheck formula.cnf proof.lrat
 * Text LRAT lines:   <id> <lit>* 0 <hint>* 0      (addition)
 *                    <id> d <id>* 0               (deletion)
 * Every added clause must follow from its hints by unit propagation. With all literals of the new clause set false,
 * the hint clauses are processed in order: a falsified hint ends the check successfully; a unit hint sets its single
 * unassigned literal true; a hint that is already satisfied is skipped and counted. Skipping is sound, because a
 * satisfied clause cannot propagate (CaDiCaL 3.0.1 occasionally emits such redundant hints). A hint with two or more
 * unassigned literals is an error. Negative (RAT) hints are rejected. Success requires that the empty clause is added.
 * Prints "s VERIFIED" (exit 0) or an error (exit 1).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct { int *lits; int n; int alive; } Clause;
static Clause *cl = NULL; static long ncap = 0;
static signed char *val = NULL; static int nvars = 0;
static int *trail = NULL; static int ntrail = 0;

static void die(const char *m, long id) { fprintf(stderr, "ERROR: %s (clause %ld)\n", m, id); printf("s NOT VERIFIED\n"); exit(1); }
static void ensure_id(long id) {
  if (id < 1) die("bad id", id);
  if (id >= ncap) { long nc = ncap ? ncap : 1024; while (nc <= id) nc *= 2;
    cl = realloc(cl, nc * sizeof(Clause)); memset(cl + ncap, 0, (nc - ncap) * sizeof(Clause)); ncap = nc; }
}
static void ensure_var(int v) {
  if (v > nvars) { int nv = nvars ? nvars : 1024; while (nv < v) nv *= 2;
    val = realloc(val, (nv + 1)); memset(val + nvars + 1, 0, nv - nvars);
    trail = realloc(trail, (nv + 1) * sizeof(int)); nvars = nv; }
}
static int lval(int l) { int v = l > 0 ? l : -l; signed char x = val[v]; return l > 0 ? x : -x; }
static void assign(int l) { int v = l > 0 ? l : -l; val[v] = l > 0 ? 1 : -1; trail[ntrail++] = v; }
static void reset(void) { while (ntrail) val[trail[--ntrail]] = 0; }

static int readint(FILE *f, long *out) {   /* returns 0 on EOF */
  int c; long s = 1, x = 0; int any = 0;
  do { c = getc(f); if (c == 'c') { while (c != '\n' && c != EOF) c = getc(f); } } while (c == ' ' || c == '\n' || c == '\r' || c == '\t');
  if (c == EOF) return 0;
  if (c == '-') { s = -1; c = getc(f); }
  while (c >= '0' && c <= '9') { x = x * 10 + (c - '0'); any = 1; c = getc(f); }
  if (!any) { ungetc(c, f); return -1; }
  *out = s * x; return 1;
}

int main(int argc, char **argv) {
  if (argc != 3) { fprintf(stderr, "usage: lratcheck formula.cnf proof.lrat\n"); return 2; }
  FILE *f = fopen(argv[1], "r"); if (!f) { perror(argv[1]); return 2; }
  int c; long nv = 0, nc = 0;
  while ((c = getc(f)) == 'c') while ((c = getc(f)) != '\n' && c != EOF);
  if (c != 'p' || fscanf(f, " cnf %ld %ld", &nv, &nc) != 2) die("bad header", 0);
  ensure_var((int)nv + 1); ensure_id(nc + 1);
  int *buf = malloc(sizeof(int) * 1024); long cap = 1024;
  for (long id = 1; id <= nc; id++) {
    long x; int n = 0;
    for (;;) { int r = readint(f, &x); if (r != 1) die("truncated formula", id); if (x == 0) break;
      if (n == cap) { cap *= 2; buf = realloc(buf, sizeof(int) * cap); }
      buf[n++] = (int)x; ensure_var((int)(x > 0 ? x : -x)); }
    cl[id].lits = malloc(sizeof(int) * (n ? n : 1)); memcpy(cl[id].lits, buf, sizeof(int) * n); cl[id].n = n; cl[id].alive = 1;
  }
  fclose(f);
  FILE *p = fopen(argv[2], "r"); if (!p) { perror(argv[2]); return 2; }
  long nadd = 0, ndel = 0, nsat = 0; int empty = 0;
  for (;;) {
    long id; int r = readint(p, &id); if (r == 0) break; if (r < 0) die("bad proof token", nadd);
    /* deletion? */
    int ch; do { ch = getc(p); } while (ch == ' ');
    if (ch == 'd') {
      long x; for (;;) { if (readint(p, &x) != 1) die("bad deletion", id); if (x == 0) break;
        if (x < 1 || x >= ncap || !cl[x].alive) die("deleting unknown clause", x);
        cl[x].alive = 0; free(cl[x].lits); cl[x].lits = NULL; }
      ndel++; continue;
    }
    ungetc(ch, p);
    ensure_id(id);
    if (cl[id].alive) die("id reused", id);
    long x; int n = 0;
    for (;;) { if (readint(p, &x) != 1) die("bad lemma", id); if (x == 0) break;
      if (n == cap) { cap *= 2; buf = realloc(buf, sizeof(int) * cap); }
      buf[n++] = (int)x; ensure_var((int)(x > 0 ? x : -x)); }
    reset();
    int ok = 0;
    for (int i = 0; i < n; i++) { if (lval(buf[i]) == 1) { ok = 1; } else if (lval(buf[i]) == 0) assign(-buf[i]); }
    /* ok==1 here means the lemma contains complementary literals: a tautology, accepted only if hints are empty */
    long h;
    for (;;) {
      if (readint(p, &h) != 1) die("bad hints", id);
      if (h == 0) break;
      if (ok) continue;
      if (h < 0) die("RAT hint not supported", id);
      if (h >= ncap || !cl[h].alive) die("hint refers to unknown clause", h);
      int unassigned = 0, ulit = 0, sat = 0;
      for (int i = 0; i < cl[h].n; i++) { int v = lval(cl[h].lits[i]);
        if (v == 1) { sat = 1; break; } if (v == 0) { unassigned++; ulit = cl[h].lits[i]; } }
      if (sat) { nsat++; continue; }
      if (unassigned == 0) { ok = 1; continue; }
      if (unassigned > 1) die("hint clause not unit", h);
      assign(ulit);
    }
    if (!ok) die("lemma not implied by hints", id);
    reset();
    cl[id].lits = malloc(sizeof(int) * (n ? n : 1)); memcpy(cl[id].lits, buf, sizeof(int) * n); cl[id].n = n; cl[id].alive = 1;
    nadd++;
    if (n == 0) { empty = 1; break; }
  }
  fclose(p);
  printf("c lemmas added %ld, deletion lines %ld, satisfied hints skipped %ld\n", nadd, ndel, nsat);
  if (!empty) die("empty clause not derived", 0);
  printf("s VERIFIED\n");
  return 0;
}
