/* Independent checker for a symmetric weighing matrix SW(n,w) (lane sw25-16).
 *
 * Usage: sw_check FILE N W
 * Same strict format and categories as code/verify_sw.py, written separately:
 *   line 1 "SW n w"; n lines of n tokens separated by single spaces; LF only; final LF; nothing else;
 *   token = "0" or an optional '-' followed by 1..4 digits with no leading zero (else FORMAT);
 *   value outside {-1,0,1} = ENTRIES; W != W^T = SYMMETRY; row with (W W^T)_ii != w or nnz != w = WEIGHT;
 *   (W W^T)_ij != 0 for some i != j = ORTHO.
 * FORMAT and HEADER stop the check; the other four are all evaluated.
 * Output: "RESULT VALID SW(n,w) n=.. w=.. trace=.." (exit 0) or
 *         "RESULT INVALID primary=CAT failing=CAT[,CAT..] detail=..." (exit 1).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXN 64
#define MAXBYTES (1 << 20)

static unsigned char buf[MAXBYTES + 1];
static long M[MAXN][MAXN];

static void bad(const char *cat, const char *detail) {
  printf("RESULT INVALID primary=%s failing=%s detail=%s\n", cat, cat, detail);
  exit(1);
}

/* parse a canonical integer token buf[a..b); returns 1 on success */
static int parse_tok(const unsigned char *s, long len, long *out) {
  long i = 0, v = 0;
  int neg = 0;
  if (len == 1 && s[0] == '0') { *out = 0; return 1; }
  if (s[0] == '-') { neg = 1; i = 1; }
  long nd = len - i;
  if (nd < 1 || nd > 4) return 0;
  if (s[i] < '1' || s[i] > '9') return 0;
  for (; i < len; i++) {
    if (s[i] < '0' || s[i] > '9') return 0;
    v = v * 10 + (s[i] - '0');
  }
  *out = neg ? -v : v;
  return 1;
}

static int parse_header_num(const unsigned char *s, long len, long *out) {
  long v = 0;
  if (len < 1 || len > 4 || s[0] < '1' || s[0] > '9') return 0;
  for (long i = 0; i < len; i++) {
    if (s[i] < '0' || s[i] > '9') return 0;
    v = v * 10 + (s[i] - '0');
  }
  *out = v;
  return 1;
}

int main(int argc, char **argv) {
  if (argc != 4) { fprintf(stderr, "usage: sw_check FILE N W\n"); return 2; }
  long nexp = atol(argv[2]), wexp = atol(argv[3]);
  FILE *f = fopen(argv[1], "rb");
  if (!f) { fprintf(stderr, "cannot open %s\n", argv[1]); return 2; }
  long nb = (long)fread(buf, 1, MAXBYTES + 1, f);
  fclose(f);
  if (nb > MAXBYTES) bad("FORMAT", "file-too-large");
  if (nb == 0) bad("FORMAT", "empty-file");
  for (long i = 0; i < nb; i++) {
    if (buf[i] >= 128) bad("FORMAT", "non-ascii-byte");
    if (buf[i] == '\r') bad("FORMAT", "CR-present");
  }
  if (buf[nb - 1] != '\n') bad("FORMAT", "no-final-LF");

  /* split into lines (without the final LF) */
  long starts[MAXN + 2], ends[MAXN + 2];
  long nl = 0, st = 0;
  for (long i = 0; i < nb; i++) {
    if (buf[i] == '\n') {
      if (nl >= MAXN + 2) bad("FORMAT", "too-many-lines");
      starts[nl] = st; ends[nl] = i; nl++; st = i + 1;
    }
  }
  /* header */
  {
    const unsigned char *h = buf + starts[0];
    long hl = ends[0] - starts[0];
    if (hl < 6 || h[0] != 'S' || h[1] != 'W' || h[2] != ' ') bad("FORMAT", "bad-header-line");
    long sp = -1;
    for (long i = 3; i < hl; i++) if (h[i] == ' ') { sp = i; break; }
    if (sp < 0) bad("FORMAT", "bad-header-line");
    long n = 0, w = 0;
    if (!parse_header_num(h + 3, sp - 3, &n)) bad("FORMAT", "bad-header-line");
    if (!parse_header_num(h + sp + 1, hl - sp - 1, &w)) bad("FORMAT", "bad-header-line");
    if (n > MAXN) bad("FORMAT", "n-too-large");
    if (nl != n + 1) bad("FORMAT", "line-count");
    for (long r = 0; r < n; r++) {
      const unsigned char *s = buf + starts[r + 1];
      long len = ends[r + 1] - starts[r + 1];
      long c = 0, a = 0;
      for (long i = 0; i <= len; i++) {
        if (i == len || s[i] == ' ') {
          if (c >= n) bad("FORMAT", "too-many-tokens");
          if (i == a) bad("FORMAT", "empty-token");
          long v;
          if (!parse_tok(s + a, i - a, &v)) bad("FORMAT", "bad-token");
          M[r][c++] = v;
          a = i + 1;
        }
      }
      if (c != n) bad("FORMAT", "too-few-tokens");
    }
    if (n != nexp || w != wexp) bad("HEADER", "header-mismatch");

    int fe = 0, fs = 0, fw = 0, fo = 0;
    long cnt_e = 0, cnt_s = 0, cnt_w = 0, cnt_o = 0, trace = 0;
    for (long i = 0; i < n; i++) {
      trace += M[i][i];
      for (long j = 0; j < n; j++) {
        if (M[i][j] < -1 || M[i][j] > 1) { fe = 1; cnt_e++; }
        if (j > i && M[i][j] != M[j][i]) { fs = 1; cnt_s++; }
      }
    }
    for (long i = 0; i < n; i++) {
      for (long j = i; j < n; j++) {
        long long g = 0;
        for (long k = 0; k < n; k++) g += (long long)M[i][k] * (long long)M[j][k];
        if (i == j) {
          long nnz = 0;
          for (long k = 0; k < n; k++) if (M[i][k] != 0) nnz++;
          if (g != w || nnz != w) { fw = 1; cnt_w++; }
        } else if (g != 0) { fo = 1; cnt_o++; }
      }
    }
    if (!(fe || fs || fw || fo)) {
      printf("RESULT VALID SW(%ld,%ld) n=%ld w=%ld trace=%ld\n", n, w, n, w, trace);
      return 0;
    }
    const char *prim = fe ? "ENTRIES" : fs ? "SYMMETRY" : fw ? "WEIGHT" : "ORTHO";
    char set[64] = "";
    if (fe) strcat(set, "ENTRIES,");
    if (fs) strcat(set, "SYMMETRY,");
    if (fw) strcat(set, "WEIGHT,");
    if (fo) strcat(set, "ORTHO,");
    set[strlen(set) - 1] = '\0';
    printf("RESULT INVALID primary=%s failing=%s detail=entries:%ld,asym:%ld,weight:%ld,ortho:%ld trace=%ld\n",
           prim, set, cnt_e, cnt_s, cnt_w, cnt_o, trace);
    return 1;
  }
}
