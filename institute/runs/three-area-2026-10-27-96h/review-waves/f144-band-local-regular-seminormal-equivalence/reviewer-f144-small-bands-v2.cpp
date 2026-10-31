// reviewer-f144-small-bands-v2.cpp  (reviewer-authored; f144 same-harness review; v2 fixes the v1 tally array bound bug, logic otherwise identical)
//
// Enumerates EVERY labeled band (idempotent semigroup) on {0..n-1} for n = 1..NMAX by backtracking
// with incremental associativity pruning, and on each band evaluates exhaustively
//   REG : xyxzx = xyzx                         (regular band identity)
//   LOC : (exe)(eye)(exe)(eze)(exe) = (exe)(eye)(eze)(exe)  for all e,x,y,z   (every eBe regular)
//   SN  : abcda = abcacda                      (the identity under review)
//   CTL : abcda = abacda                       (regular-type control identity; equivalent to REG)
// The theorem under review predicts LOC == SN on every band.  CTL == REG is a sanity control of the checker.
// Prints a tally per n and the first labeled band found with LOC && !REG (a finite band in the variety that
// is not regular) and the first with !LOC (a band outside the variety), as full tables.
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
static int n;
static int T[8][8];
static long long tally[8][16];     // tally[n][mask] mask bits: REG=1, LOC=2, SN=4, CTL=8  (v2: second dimension 16; v1 had 8 -> out-of-bounds aliasing of masks 8..15 into row n+1)
static long long nbands[8];
static bool printedLocNotReg[8], printedNotLoc[8];
static long long nodes = 0;
static inline int mul(int x, int y) { return T[x][y]; }
static bool assocOK() {
    // check all triples whose four needed cells are all defined
    for (int x = 0; x < n; x++) for (int y = 0; y < n; y++) {
        int xy = T[x][y];
        for (int z = 0; z < n; z++) {
            int yz = T[y][z];
            if (xy < 0 || yz < 0) continue;
            int l = T[xy][z], r = T[x][yz];
            if (l < 0 || r < 0) continue;
            if (l != r) return false;
        }
    }
    return true;
}
static void printTable(const char* title) {
    std::printf("  %s (order %d):\n", title, n);
    for (int i = 0; i < n; i++) { std::printf("    "); for (int j = 0; j < n; j++) std::printf("%d ", T[i][j]); std::printf("\n"); }
}
static void evaluate() {
    nbands[n]++;
    bool reg = true, loc = true, sn = true, ctl = true;
    for (int x = 0; x < n && reg; x++) for (int y = 0; y < n && reg; y++) { int xy = mul(x, y), xyx = mul(xy, x); for (int z = 0; z < n; z++) if (mul(mul(xyx, z), x) != mul(mul(xy, z), x)) { reg = false; break; } }
    for (int e = 0; e < n && loc; e++) {
        int L[8]; for (int x = 0; x < n; x++) L[x] = mul(mul(e, x), e);
        for (int x = 0; x < n && loc; x++) for (int y = 0; y < n && loc; y++) { int X = L[x], XY = mul(X, L[y]), XYX = mul(XY, X); for (int z = 0; z < n; z++) { int Z = L[z]; if (mul(mul(XYX, Z), X) != mul(mul(XY, Z), X)) { loc = false; break; } } }
    }
    for (int a = 0; a < n && sn; a++) for (int b = 0; b < n && sn; b++) { int ab = mul(a, b); for (int c = 0; c < n && sn; c++) { int abc = mul(ab, c), abcac = mul(mul(abc, a), c); for (int d = 0; d < n; d++) if (mul(mul(abc, d), a) != mul(mul(abcac, d), a)) { sn = false; break; } } }
    for (int a = 0; a < n && ctl; a++) for (int b = 0; b < n && ctl; b++) { int ab = mul(a, b), aba = mul(ab, a); for (int c = 0; c < n && ctl; c++) { int abc = mul(ab, c), abac = mul(aba, c); for (int d = 0; d < n; d++) if (mul(mul(abc, d), a) != mul(mul(abac, d), a)) { ctl = false; break; } } }
    int mask = (reg ? 1 : 0) | (loc ? 2 : 0) | (sn ? 4 : 0) | (ctl ? 8 : 0);
    tally[n][mask]++;
    if (loc && !reg && !printedLocNotReg[n]) { printedLocNotReg[n] = true; printTable("first labeled band with LOC && !REG"); }
    if (!loc && !printedNotLoc[n]) { printedNotLoc[n] = true; printTable("first labeled band with !LOC"); }
}
static void rec(int cell) {
    nodes++;
    // skip diagonal cells (fixed idempotent)
    while (cell < n * n && (cell / n) == (cell % n)) cell++;
    if (cell == n * n) { evaluate(); return; }
    int i = cell / n, j = cell % n;
    for (int v = 0; v < n; v++) {
        T[i][j] = v;
        if (assocOK()) rec(cell + 1);
    }
    T[i][j] = -1;
}
int main(int argc, char** argv) {
    int NMAX = argc > 1 ? std::atoi(argv[1]) : 6;
    if (NMAX > 7) NMAX = 7;
    for (n = 1; n <= NMAX; n++) {
        for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) T[i][j] = (i == j) ? i : -1;
        nodes = 0;
        rec(0);
        std::printf("n=%d labeled bands=%lld search nodes=%lld\n", n, nbands[n], nodes);
        long long locNotSn = 0, snNotLoc = 0, regNotCtl = 0, ctlNotReg = 0, locNotReg = 0, notLoc = 0, regc = 0, locc = 0, snc = 0;
        for (int m = 0; m < 16; m++) {
            if (!tally[n][m]) continue;
            bool reg = m & 1, loc = m & 2, sn = m & 4, ctl = m & 8;
            std::printf("   REG=%d LOC=%d SN=%d CTL=%d : %lld\n", reg, loc, sn, ctl, tally[n][m]);
            if (loc && !sn) locNotSn += tally[n][m];
            if (sn && !loc) snNotLoc += tally[n][m];
            if (reg && !ctl) regNotCtl += tally[n][m];
            if (ctl && !reg) ctlNotReg += tally[n][m];
            if (loc && !reg) locNotReg += tally[n][m];
            if (!loc) notLoc += tally[n][m];
            if (reg) regc += tally[n][m]; if (loc) locc += tally[n][m]; if (sn) snc += tally[n][m];
        }
        std::printf("   %s theorem check LOC<=>SN on all %lld labeled bands of order %d (LOC&!SN=%lld, SN&!LOC=%lld)\n", (locNotSn == 0 && snNotLoc == 0) ? "PASS" : "FAIL", nbands[n], n, locNotSn, snNotLoc);
        std::printf("   %s checker control REG<=>CTL (REG&!CTL=%lld, CTL&!REG=%lld)\n", (regNotCtl == 0 && ctlNotReg == 0) ? "PASS" : "FAIL", regNotCtl, ctlNotReg);
        std::printf("   INFO regular=%lld locally-regular=%lld SN=%lld locally-regular-but-not-regular=%lld not-locally-regular=%lld\n", regc, locc, snc, locNotReg, notLoc);
        std::fflush(stdout);
    }
    return 0;
}
