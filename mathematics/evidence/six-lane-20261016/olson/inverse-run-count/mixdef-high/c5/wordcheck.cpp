// wordcheck.cpp -- [F] independent explicit-word check for c5/proof-SEED.md (task OlsonRunCount5).
// Works on the explicit run list of W(p, kB): run 0 anti (d = -1), runs 1..n aligned (d = +1), cyclic, B = 1 letter rho_{-1},
// kappa = kB + 1, beta = 0.  lambda(Q) is computed from scratch for every explicit pattern from the general formula of
// Lemma H: lambda(Q) = min(p - m(Q) + 1, D_Q + B - kappa + m(Q) - beta, floor((D_Q + B)/2) + 1) (m(Q) = number of maximal
// cyclic blocks), never from the type formulas of seeds.py.
// Checks, for every listed prime and every kB with 3kB >= p + 5, kB <= p - 4:
//  (S) Lemma PS: for EVERY aligned run t the explicit pair configuration of proof-SEED.md Sec. 1 exists, Q and Q + t have the
//      claimed block structure, and the seed interval [lam(Q+t) - U(Q), U(Q+t) - lam(Q)] equals [3 - ceil(d/2), floor(d/2) - 1]
//      and lies in the canonical range [lam({t}), p - lam({t}^c)];
//  (C) Lemma SCW: for random explicit patterns (several generators) and every interval I_i, the whole Lemma-CW-order chain
//      down to a singleton; every step checked with explicit lambdas: (A^s) lo(Q') + a >= 1 - lam(Q^c), (B^s) hi(Q') + b <=
//      p + lam(Q) - 1; plus the pin.  For p <= 17 (k <= 27) EVERY proper pattern is checked (exhaustive).
// Native time limit: the program stops itself (and prints INTERRUPTED -> UNKNOWN) after TLIM seconds.
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <chrono>
#include <set>
#include <tuple>
#include <random>
#include <algorithm>
using namespace std;
static int p, kB, n, k, Bl, kap, delta_;
static vector<int> d;
static long long fdiv(long long a, long long b){ long long q = a / b; if ((a % b != 0) && ((a < 0) != (b < 0))) q--; return q; }
static long long cdiv(long long a, long long b){ return -fdiv(-a, b); }
struct Info { int D, m, sz; };
static Info info(const vector<char>& Q){
    Info r{0,0,0};
    for (int i = 0; i < k; i++) if (Q[i]) { r.D += d[i]; r.sz++; if (!Q[(i + k - 1) % k]) r.m++; }
    return r;
}
static long long lam(const vector<char>& Q){
    Info r = info(Q);
    long long a1 = p - r.m + 1, a2 = (long long)r.D + Bl - kap + r.m - 0, a3 = fdiv(r.D + Bl, 2) + 1;
    return min(a1, min(a2, a3));
}
static vector<char> comp(const vector<char>& Q){ vector<char> c(k); for (int i = 0; i < k; i++) c[i] = !Q[i]; return c; }
static long long lamc(const vector<char>& Q){ return lam(comp(Q)); }
static long long A_, B_;   // aligned seed
static long long minA, minB; static long long nsteps, nfail;
// certified range of a pattern of size 1 (seed or canonical anti range) or >= 2 (arc)
static void rangeOf(const vector<char>& Q, long long& lo, long long& hi){
    Info r = info(Q);
    if (r.sz == 1) {
        int t = -1; for (int i = 0; i < k; i++) if (Q[i]) t = i;
        if (t == 0) { lo = lam(Q); hi = p - lamc(Q); }
        else { lo = A_; hi = B_; }
    } else { lo = lam(Q); hi = p - lamc(Q); }
}
// one CW predecessor: remove an aligned end run of a block with >= 2 runs, else an isolated aligned run
static int cwRemove(const vector<char>& Q){
    for (int i = 0; i < k; i++) {
        if (!Q[i]) continue;
        int prv = (i + k - 1) % k, nxt = (i + 1) % k;
        bool endrun = (!Q[prv] && Q[nxt]) || (Q[prv] && !Q[nxt]);
        if (endrun && i != 0) return i;
    }
    for (int i = 1; i < k; i++) if (Q[i]) return i;   // all blocks single runs: an isolated aligned run
    return -1;
}
static bool stepOK(const vector<char>& Q, int t, long long& sA, long long& sB){
    vector<char> Qp = Q; Qp[t] = 0;
    long long lo, hi; rangeOf(Qp, lo, hi);
    long long wlo = 1 - lamc(Q), whi = p + lam(Q) - 1;
    sA = (lo + A_) - wlo; sB = whi - (hi + B_);
    return sA >= 0 && sB >= 0;
}
static bool chain(vector<char> Q, set<tuple<int,int,int>>& types){
    Info r = info(Q);
    while (r.sz >= 2) {
        int t = cwRemove(Q);
        if (t < 0) { printf("ERROR no removable run\n"); exit(1); }
        long long sA, sB; bool ok = stepOK(Q, t, sA, sB);
        nsteps++; minA = min(minA, sA); minB = min(minB, sB);
        types.insert(make_tuple(r.sz, Q[0] ? 1 : 0, r.m));
        if (!ok) { nfail++; return false; }
        Q[t] = 0; r = info(Q);
    }
    return true;
}
int main(int argc, char** argv){
    double TLIM = 3000; auto T0 = chrono::steady_clock::now();
    vector<int> primes = {11, 13, 17, 37, 41, 43, 47, 53, 59, 61};
    int NRAND = 400; if (argc > 1) NRAND = atoi(argv[1]);
    mt19937_64 rng(20261017);
    long long totSeedT = 0, seedFail = 0, totPat = 0, exhaustive = 0;
    for (int pp : primes) {
        p = pp;
        for (kB = 1; kB <= p - 4; kB++) {
            if (3 * kB < p + 5) continue;
            n = p + kB; k = n + 1; Bl = 1; kap = kB + 1; delta_ = p - kB;
            d.assign(k, 1); d[0] = -1;
            A_ = 3 - cdiv(delta_, 2); B_ = fdiv(delta_, 2) - 1;
            // (S) seeds for every aligned t
            int m = kB / 2 + 1; long long sfail = 0;
            for (int t = 1; t <= n; t++) {
                vector<char> Q(k, 0);
                vector<pair<int,int>> Wint;
                if (t <= n - 2) { Q[t + 1] = Q[t + 2] = 1; Wint.push_back({1, t - 2}); Wint.push_back({t + 4, n}); }
                else { Q[t - 2] = Q[t - 1] = 1; Wint.push_back({1, t - 4}); Wint.push_back({t + 2, n}); }
                int need = m - 1;
                for (auto& iv : Wint) for (int s = iv.first; s + 1 <= iv.second && need > 0; s += 3) { Q[s] = Q[s + 1] = 1; need--; }
                bool ok = (need == 0);
                vector<char> Qt = Q; Qt[t] = 1;
                Info iq = info(Q), iqt = info(Qt);
                ok = ok && !Q[0] && !Q[t] && iq.m == m && iq.sz == 2 * m && iqt.m == m && iqt.sz == 2 * m + 1;
                // block sizes of Q all 2
                for (int i = 1; i < k && ok; i++) if (Q[i] && !Q[i - 1]) { int L = 0; int j = i; while (j < k && Q[j]) { L++; j++; } if (L != 2) ok = false; }
                long long lQ = lam(Q), UQ = p - lamc(Q), lQt = lam(Qt), UQt = p - lamc(Qt);
                long long lo = lQt - UQ, hi = UQt - lQ;
                vector<char> S(k, 0); S[t] = 1;
                long long L1 = lam(S), U1 = p - lamc(S);
                ok = ok && lo == A_ && hi == B_ && lo >= L1 && hi <= U1 && lQ + lamc(Q) <= p && lQt + lamc(Qt) <= p;
                totSeedT++; if (!ok) { sfail++; seedFail++; }
            }
            // (C) certification
            set<tuple<int,int,int>> types; minA = minB = (long long)1e18; nsteps = 0; nfail = 0;
            long long npat = 0;
            bool exh = (k <= 27);
            if (exh) {
                vector<char> Q(k);
                for (long long mask = 1; mask < (1LL << k) - 1; mask++) {
                    Info r; int sz = __builtin_popcountll(mask);
                    if (sz < 2) continue;
                    for (int i = 0; i < k; i++) Q[i] = (mask >> i) & 1;
                    int t = cwRemove(Q);
                    long long sA, sB; bool ok = stepOK(Q, t, sA, sB);
                    nsteps++; minA = min(minA, sA); minB = min(minB, sB);
                    r = info(Q); types.insert(make_tuple(r.sz, Q[0] ? 1 : 0, r.m));
                    if (!ok) nfail++;
                    npat++;
                }
                exhaustive++;
            } else {
                for (int it = 0; it < NRAND; it++) {
                    vector<char> Q(k, 0);
                    int g = it % 4;
                    if (g == 0) { double rho = (it % 9 + 1) / 10.0; uniform_real_distribution<double> U(0, 1); for (int i = 0; i < k; i++) Q[i] = U(rng) < rho; }
                    else if (g == 1) { int nint = 1 + rng() % 12; for (int q = 0; q < nint; q++) { int s = rng() % k, L = 1 + rng() % 6; for (int i = 0; i < L; i++) Q[(s + i) % k] = 1; } }
                    else if (g == 2) { int sz = 2 + rng() % (kB + 1); for (int q = 0; q < sz; q++) Q[rng() % k] = 1; }
                    else { for (int i = 0; i < k; i++) Q[i] = 1; int sz = 1 + rng() % (kB + 2); for (int q = 0; q < sz; q++) Q[rng() % k] = 0; }
                    Info r = info(Q); if (r.sz < 2 || r.sz == k) continue;
                    chain(Q, types); npat++;
                }
                for (int i = 2; i <= n; i++) { vector<char> Q(k, 0); for (int j = 1; j <= i; j++) Q[j] = 1; chain(Q, types); npat++; }
            }
            // pin: X_[k] = x_0 + X_{0^c} in [lam({0}) + lam(0^c), (p - lamc({0})) + (p - lamc(0^c))]
            vector<char> Z(k, 0); Z[0] = 1; vector<char> Zc = comp(Z);
            long long plo = lam(Z) + lam(Zc), phi = (p - lamc(Z)) + (p - lamc(Zc));
            bool pin = plo >= 1 && phi <= 2 * p - 1;
            totPat += npat;
            double el = chrono::duration<double>(chrono::steady_clock::now() - T0).count();
            printf("p=%d kB=%d k=%d seedT=%d seedFail=%lld patterns=%lld%s steps=%lld fail=%lld minSlackA=%lld minSlackB=%lld types=%zu pin=%d [%.1fs]\n",
                   p, kB, k, n, sfail, npat, exh ? "(exhaustive)" : "", nsteps, nfail, minA, minB, types.size(), (int)pin, el);
            fflush(stdout);
            if (el > TLIM) { printf("INTERRUPTED (native time limit) -> UNKNOWN for the remaining cases\n"); return 0; }
        }
    }
    printf("TOTAL seed checks=%lld seedFail=%lld patterns=%lld exhaustive_cases=%lld\n", totSeedT, seedFail, totPat, exhaustive);
    return 0;
}
