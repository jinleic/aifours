/* Double-double loss/add/axpy step kernels (same algorithms and error model as dd.py, PROOFS §3).
 *
 * Build: clang -O2 -ffp-contract=off -fno-fast-math -shared -o libddkern.dylib ddkern.c
 * -ffp-contract=off forbids silent a*b+c -> fma contraction; the only FMA is the explicit fma() in two_prod,
 * which makes TwoProd exact (replacing Dekker's split; the error analysis of PROOFS §3 is unchanged because it
 * only uses exactness of TwoProd/TwoSum and correct rounding of every other operation).
 * All operands are nonnegative (cert.py splits inputs into nonnegative parts).
 * Matrices are row-major d x d pairs (hi, lo); coefficient vectors are DD pairs.
 */
#include <math.h>
#include <stddef.h>

static inline void two_sum(double a, double b, double *s, double *e) {
    double ss = a + b;
    double bb = ss - a;
    *e = (a - (ss - bb)) + (b - bb);
    *s = ss;
}
static inline void quick_two_sum(double a, double b, double *s, double *e) {
    double ss = a + b;
    *e = b - (ss - a);
    *s = ss;
}
static inline void two_prod(double a, double b, double *p, double *e) {
    double pp = a * b;
    *e = fma(a, b, -pp);
    *p = pp;
}
/* dd.add */
static inline void dd_add(double ah, double al, double bh, double bl, double *rh, double *rl) {
    double s, e;
    two_sum(ah, bh, &s, &e);
    double t = al + bl;
    e = e + t;
    quick_two_sum(s, e, rh, rl);
}
/* dd.mul */
static inline void dd_mul(double ah, double al, double bh, double bl, double *rh, double *rl) {
    double p, e;
    two_prod(ah, bh, &p, &e);
    double c1 = ah * bl;
    double c2 = al * bh;
    e = e + (c1 + c2);
    quick_two_sum(p, e, rh, rl);
}

#define FLUSH 0x1p-900

static inline void flush(double *h, double *l) {
    if (*h != 0.0 && *h < FLUSH) { *h = 0.0; *l = 0.0; }
}

/* out[x,y] = rn * ( (a_x a_y) * Y[x,y] + (b_x b_y) * Y[x+1,y+1] ),  x,y < dn ; Y is d x d (ld = d).
 * a: dn-vector DD (sqrt(n-x)), b: m-vector DD (sqrt(x+1)), m = min(dn, d-1); rn DD scalar (1/n).
 * Matches dd.py loss_step_dd: aa = mul(a_x, a_y); t1 = mul(aa, Y); t2 = mul(bb, Y'); s = add(t1, t2); out = mul(s, rn).
 */
void loss_step(const double *Yh, const double *Yl, int d, int dn,
               const double *ah, const double *al, const double *bh, const double *bl, int m,
               double rnh, double rnl, double *Oh, double *Ol) {
    for (int x = 0; x < dn; x++) {
        for (int y = 0; y < dn; y++) {
            double aah, aal, t1h, t1l, sh, sl, oh, ol;
            dd_mul(ah[x], al[x], ah[y], al[y], &aah, &aal);
            dd_mul(aah, aal, Yh[(size_t)x * d + y], Yl[(size_t)x * d + y], &t1h, &t1l);
            if (x < m && y < m) {
                double bbh, bbl, t2h, t2l;
                dd_mul(bh[x], bl[x], bh[y], bl[y], &bbh, &bbl);
                dd_mul(bbh, bbl, Yh[(size_t)(x + 1) * d + (y + 1)], Yl[(size_t)(x + 1) * d + (y + 1)], &t2h, &t2l);
                dd_add(t1h, t1l, t2h, t2l, &sh, &sl);
            } else {
                sh = t1h; sl = t1l;
            }
            dd_mul(sh, sl, rnh, rnl, &oh, &ol);
            flush(&oh, &ol);
            Oh[(size_t)x * dn + y] = oh;
            Ol[(size_t)x * dn + y] = ol;
        }
    }
}

/* out (dn x dn): out[x,y] = rn * ( (a_x a_y) Z[x,y] [x,y<m0] + (b_x b_y) Z[x-1,y-1] [1<=x,y<=m1] ), Z is d x d.
 * a: m0-vector DD sqrt(n+1-x); b: m1-vector DD with b[j] = sqrt(j+1) used at (x,y) = (j+1, k+1).
 * Matches dd.py add_step_dd (t1 placed first, t2 added into [1..m1]).
 */
void add_step(const double *Zh, const double *Zl, int d, int dn,
              const double *ah, const double *al, int m0,
              const double *bh, const double *bl, int m1,
              double rnh, double rnl, double *Oh, double *Ol) {
    for (int x = 0; x < dn; x++) {
        for (int y = 0; y < dn; y++) {
            double sh = 0.0, sl = 0.0;
            int have = 0;
            if (x < m0 && y < m0) {
                double aah, aal;
                dd_mul(ah[x], al[x], ah[y], al[y], &aah, &aal);
                dd_mul(aah, aal, Zh[(size_t)x * d + y], Zl[(size_t)x * d + y], &sh, &sl);
                have = 1;
            }
            if (x >= 1 && y >= 1 && x <= m1 && y <= m1) {
                double bbh, bbl, t2h, t2l;
                dd_mul(bh[x - 1], bl[x - 1], bh[y - 1], bl[y - 1], &bbh, &bbl);
                dd_mul(bbh, bbl, Zh[(size_t)(x - 1) * d + (y - 1)], Zl[(size_t)(x - 1) * d + (y - 1)], &t2h, &t2l);
                if (have) {
                    double rh, rl;
                    dd_add(sh, sl, t2h, t2l, &rh, &rl);
                    sh = rh; sl = rl;
                } else {
                    double rh, rl;            /* dd.py adds t2 to an exact 0 entry: add(0, t2) */
                    dd_add(0.0, 0.0, t2h, t2l, &rh, &rl);
                    sh = rh; sl = rl;
                }
            }
            double oh, ol;
            dd_mul(sh, sl, rnh, rnl, &oh, &ol);
            flush(&oh, &ol);
            Oh[(size_t)x * dn + y] = oh;
            Ol[(size_t)x * dn + y] = ol;
        }
    }
}

/* Z[x,y] += pi * Y[x,y] for x,y < m ; Z is dz x dz, Y is dy x dy. Matches dd.py axpy_dd (t = mul(Y, pi); add(Z, t)). */
void axpy(double *Zh, double *Zl, int dz, const double *Yh, const double *Yl, int dy, int m, double pih, double pil) {
    for (int x = 0; x < m; x++) {
        for (int y = 0; y < m; y++) {
            double th, tl, rh, rl;
            dd_mul(Yh[(size_t)x * dy + y], Yl[(size_t)x * dy + y], pih, pil, &th, &tl);
            dd_add(Zh[(size_t)x * dz + y], Zl[(size_t)x * dz + y], th, tl, &rh, &rl);
            Zh[(size_t)x * dz + y] = rh;
            Zl[(size_t)x * dz + y] = rl;
        }
    }
}
