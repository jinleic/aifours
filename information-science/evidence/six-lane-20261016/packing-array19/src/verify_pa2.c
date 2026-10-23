/* Verifier 2 (column-pair ordered-pair definition) for PA(N,k,q).
 * Strict format: N lines, each exactly k decimal integers in [0,q) separated by
 * single spaces or tabs, every line terminated by '\n'; no other bytes.
 * Valid iff in every pair of columns no ordered symbol pair occurs twice.
 * Usage: verify_pa2 FILE N k q ; prints VALID/INVALID line, exit 0 iff valid. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {
  if (argc != 5) { fprintf(stderr, "usage\n"); return 2; }
  int N = atoi(argv[2]), k = atoi(argv[3]), q = atoi(argv[4]);
  if (N <= 0 || k <= 0 || q <= 0 || N > 1000 || k > 100 || q > 100) return 2;
  FILE *f = fopen(argv[1], "rb");
  if (!f) { printf("INVALID cannot open\n"); return 1; }
  int *A = calloc((size_t)N * k, sizeof(int));
  int r = 0, c = 0, ch, inNum = 0, val = 0, sawSep = 0;
  while ((ch = fgetc(f)) != EOF) {
    if (ch >= '0' && ch <= '9') {
      if (!inNum) { inNum = 1; val = 0; }
      val = val * 10 + (ch - '0');
      if (val > 1000000) { printf("INVALID huge\n"); return 1; }
      sawSep = 0;
    } else if (ch == ' ' || ch == '\t' || ch == '\n') {
      if (inNum) {
        if (r >= N || c >= k) { printf("INVALID too many entries at row %d\n", r); return 1; }
        if (val >= q) { printf("INVALID symbol %d out of range row %d\n", val, r); return 1; }
        A[r * k + c] = val; c++; inNum = 0;
      } else if (ch != '\n' && sawSep) {
        printf("INVALID double separator row %d\n", r); return 1;
      }
      if (ch == '\n') {
        if (c != k) { printf("INVALID row %d has %d entries\n", r, c); return 1; }
        r++; c = 0; sawSep = 0;
      } else sawSep = 1;
    } else { printf("INVALID byte %d\n", ch); return 1; }
  }
  fclose(f);
  if (inNum || c != 0) { printf("INVALID missing final newline\n"); return 1; }
  if (r != N) { printf("INVALID expected %d rows got %d\n", N, r); return 1; }
  int *seen = malloc(sizeof(int) * q * q);
  for (int c1 = 0; c1 < k; c1++)
    for (int c2 = c1 + 1; c2 < k; c2++) {
      memset(seen, 0, sizeof(int) * q * q);
      for (int i = 0; i < N; i++) {
        int p = A[i * k + c1] * q + A[i * k + c2];
        if (seen[p]) {
          printf("INVALID columns %d,%d repeat ordered pair (%d,%d) rows %d,%d\n", c1, c2,
                 A[i * k + c1], A[i * k + c2], seen[p] - 1, i);
          return 1;
        }
        seen[p] = i + 1;
      }
    }
  printf("VALID N=%d k=%d q=%d\n", N, k, q);
  return 0;
}
