// hwsearch.cpp -- half-window (README Sec. 2) avoidance search for RGR run data.
// Task OlsonRunCount, olson/inverse-run-count.  Independent of ../code/.
//
// Run data: cyclic R_1 S_1 ... R_k S_k (0-based runs i = 0..k-1; S_i follows R_i),
// a_i rho_1, b_i rho_{-1}, l_i reflections.  For P subset [k] (bit i = run i in zone +):
//   f_j = [bit j != bit j+1]; m = sum f / 2; h = sum floor((l_j - f_j)/2);
//   E+ = sum_{P} a + sum_{P^c} b; E- = R - E+; g(E) = min(p-m, E+m+h-p, floor(E/2));
//   I(P) = [-g(E-), g(E+)].  Avoid iff for all P: sum_P phi notin I(P) mod p.
//
// Usage: hwsearch p N kmin kmax famM consttype inherit [maxprint]
//   famM     : only patterns with m(P) <= famM are used (famM >= k means all patterns)
//   consttype: 0 all a/b splits (up to global sign a<->b); 1 only b == 0 (constant rho_1 runs)
//   inherit  : 1 apply inherited filter (E,P,V,Pairs,D0); 0 none
// Output: JSON lines for every run datum that is NOT certified (feasible phi exists within the
// family) -- "feasible" -- with one phi; a summary line with counts per k.
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cstdint>

static int p, N, kmin, kmax, famM, consttype, inherit, maxprint = 50;
static int K;
static int r[64], l[64], a[64], b[64];
static std::vector<uint32_t> forb;   // forbidden residues bitmask for P (bit k-1 == 0)
static std::vector<uint8_t> inFam;
static std::vector<int> sums;
static std::vector<int> wlo, whi; static long long def_ok[64], def_bad[64], enum_sols[64]; static int maxenum = 2000000;
static int phi[64];
static long long cnt_rl[64], cnt_data[64], cnt_full[64], cnt_cert[64], cnt_feas[64];
static long long printed = 0;

static bool build() {
    int k = K;
    int R = 0, H = 0;
    for (int i = 0; i < k; i++) { R += a[i] + b[i]; H += l[i] / 2; }
    int np = 1 << (k - 1);
    forb.assign(np, 0);
    inFam.assign(np, 0); wlo.assign(np, 1); whi.assign(np, 0);
    uint32_t full = (p >= 32) ? 0xffffffffu : ((1u << p) - 1);
    for (int P = 0; P < np; P++) {
        int f2 = 0, h = 0, Ep = 0;
        for (int j = 0; j < k; j++) {
            int zj = (P >> j) & 1, zn = (P >> ((j + 1) % k)) & 1;
            int f = zj != zn;
            f2 += f;
            h += (l[j] - f) / 2;
            Ep += zj ? a[j] : b[j];
        }
        int m = f2 / 2;
        int Em = R - Ep;
        auto g = [&](int E) { int v = p - m; int w = E + m + h - p; int u = E / 2; return std::min(v, std::min(w, u)); };
        int lo = -g(Em), hi = g(Ep);
        if (m > famM) { wlo[P] = -g(Em); whi[P] = g(Ep); continue; }
        wlo[P] = -g(Em); whi[P] = g(Ep);
        inFam[P] = 1;
        if (lo > hi) continue;
        if (hi - lo + 1 >= p) return true;  // full window: certified for every phi
        uint32_t msk = 0;
        for (int x = lo; x <= hi; x++) msk |= 1u << (((x % p) + p) % p);
        forb[P] = msk & full;
    }
    return false;
}

static int centered(int x){ x%=p; if(x<0) x+=p; return x>p/2? x-p : x; }
static bool in_window(int P, int s){ int lo=wlo[P], hi=whi[P]; if(lo>hi) return false; if(hi-lo+1>=p) return true; int d=((s-lo)%p+p)%p; return d<=hi-lo; }
static long long minbh_hist[64];
static bool defect_kills(){
    int k=K; int np=1<<(k-1);
    int ph[64]; { int s=0; for(int i=0;i<k-1;i++){ ph[i]=phi[i]; s+=phi[i]; } ph[k-1]=((-s)%p+p)%p; }
    // chain lifts along prefixes {0..j-1}; window table index uses complement if bit k-1 set
    int prev=0; int x[64]; int full=(1<<k)-1;
    for(int j=1;j<=k;j++){
        int P=(1<<j)-1; int s=0; for(int t=0;t<j;t++) s+=ph[t];
        int lo,hi;
        if(j==k){ lo=1; hi=0; }
        else { int Q=P; int ss=s; if(Q>>(k-1)&1){ Q=full^Q; ss=-s; } lo=wlo[Q]; hi=whi[Q]; if(Q!=P){ int tl=lo; lo=-hi; hi=-tl; } }
        int cand;
        if(j==k){ cand = p; }
        else if(lo>hi){ int c=((ph[j-1])%p+p)%p; if(c>p/2) c-=p; cand=prev+c; }
        else { cand = hi+1+(((s-(hi+1))%p)+p)%p; }
        x[j-1]=cand-prev; prev=cand;
    }
    int bh[64]; int mn=1000;
    for(int t=0;t<k;t++){ bh[t]=2*x[t]-(a[t]-b[t]); if(bh[t]<mn) mn=bh[t]; }
    if(mn<-30) mn=-30; minbh_hist[mn+31]++;
    int Pm=0,cnt=0; for(int t=0;t<k;t++) if(bh[t]<=0){ Pm|=1<<t; cnt++; }
    if(cnt==0||cnt==k) return false;
    int Q=Pm; int lo,hi; int s=0; for(int t=0;t<k;t++) if(Pm>>t&1) s+=x[t];
    if(Q>>(k-1)&1){ Q=full^Q; lo=-whi[Q]; hi=-wlo[Q]; } else { lo=wlo[Q]; hi=whi[Q]; }
    return lo<=hi && lo<=s && s<=hi;  // untranslated test
}
static bool dfs(int j) {
    if (j == K - 1) { enum_sols[K]++; if(defect_kills()) def_ok[K]++; else { def_bad[K]++; if(printed<maxprint){ printed++; int s=0; printf("{\"defect_fail\":1,\"k\":%d,\"a\":[",K); for(int i=0;i<K;i++) printf("%s%d",i?",":"",a[i]); printf("],\"b\":["); for(int i=0;i<K;i++) printf("%s%d",i?",":"",b[i]); printf("],\"l\":["); for(int i=0;i<K;i++) printf("%s%d",i?",":"",l[i]); printf("],\"phi\":["); for(int i=0;i<K-1;i++){ printf("%d,",phi[i]); s+=phi[i];} printf("%d]}\n",((-s)%p+p)%p); fflush(stdout);} } return enum_sols[K] >= maxenum; }
    int base = 1 << j;
    for (int v = 0; v < p; v++) {
        phi[j] = v;
        bool ok = true;
        for (int P = 0; P < base; P++) {
            int s = sums[P] + v; if (s >= p) s -= p;
            sums[P | base] = s;
            if (inFam[P | base] && ((forb[P | base] >> s) & 1)) { ok = false; break; }
        }
        if (ok && dfs(j + 1)) return true;
    }
    return false;
}

static bool inherited() {
    int R = 0, F = 0, H = 0, fr = 0;
    for (int i = 0; i < K; i++) { R += a[i] + b[i]; F += l[i]; H += l[i] / 2; fr += (a[i] + b[i]) / 2;
        if (a[i] > p - 1 || b[i] > p - 1) return false; }
    if (R > 3 * p - 2) return false;
    if (F + fr > 3 * p - 2) return false;
    if (R + H > 3 * p - 2) return false;
    if (H > p - 1) return false;
    return true;
}

static void process_split() {
    if (inherit && !inherited()) return;
    cnt_data[K]++;
    if (build()) { cnt_full[K]++; cnt_cert[K]++; return; }
    { int np=1<<(K-1); for(int P=0;P<np;P++){ if(wlo[P]<=whi[P] && whi[P]-wlo[P]+1>=p){ cnt_full[K]++; cnt_cert[K]++; return; } } }
    if (forb[0] & 1u) { cnt_cert[K]++; return; }  // P = empty: 0 forbidden
    sums.assign(1 << (K - 1), 0);
    sums[0] = 0;
    if (dfs(0)) {
        cnt_feas[K]++;
        if (printed < maxprint) {
            printed++;
            int s = 0; for (int i = 0; i < K - 1; i++) s += phi[i];
            int last = ((-s) % p + p) % p;
            printf("{\"feasible\":1,\"p\":%d,\"N\":%d,\"k\":%d,\"famM\":%d,\"a\":[", p, N, K, famM);
            for (int i = 0; i < K; i++) printf("%s%d", i ? "," : "", a[i]);
            printf("],\"b\":[");
            for (int i = 0; i < K; i++) printf("%s%d", i ? "," : "", b[i]);
            printf("],\"l\":[");
            for (int i = 0; i < K; i++) printf("%s%d", i ? "," : "", l[i]);
            printf("],\"phi\":[");
            for (int i = 0; i < K - 1; i++) printf("%d,", phi[i]);
            printf("%d]}\n", last);
            fflush(stdout);
        }
    } else cnt_cert[K]++;
}

static void splits(int i) {
    if (i == K) { process_split(); return; }
    if (consttype == 1) { a[i] = r[i]; b[i] = 0; splits(i + 1); return; }
    for (int x = 0; x <= r[i]; x++) {
        a[i] = x; b[i] = r[i] - x;
        if (a[i] > p - 1 || b[i] > p - 1) continue;
        // global sign symmetry a<->b: keep only split sequences with (a) lexicographically >= (b) at first difference
        if (i == K - 1) {
            int cmp = 0;
            for (int t = 0; t < K && !cmp; t++) { if (a[t] != b[t]) cmp = a[t] > b[t] ? 1 : -1; }
            if (cmp < 0) continue;
        }
        splits(i + 1);
    }
}

static bool rot_min() {
    // sequence of pairs (r_i, l_i); keep lexicographically minimal rotation
    for (int s = 1; s < K; s++) {
        for (int t = 0; t < K; t++) {
            int i1 = t, i2 = (t + s) % K;
            if (r[i2] != r[i1]) { if (r[i2] < r[i1]) return false; goto next; }
            if (l[i2] != l[i1]) { if (l[i2] < l[i1]) return false; goto next; }
        }
        next:;
    }
    return true;
}

static void gen(int pos, int rem) {
    // pos indexes the 2K parts: even = r, odd = l
    if (pos == 2 * K) {
        if (rem != 0) return;
        if (!rot_min()) return;
        cnt_rl[K]++;
        splits(0);
        return;
    }
    int left = 2 * K - pos - 1;
    for (int v = 1; v <= rem - left; v++) {
        if (pos % 2 == 0) r[pos / 2] = v; else l[pos / 2] = v;
        gen(pos + 1, rem - v);
    }
}

int main(int argc, char** argv) {
    if (argc < 8) { fprintf(stderr, "usage\n"); return 1; }
    p = atoi(argv[1]); N = atoi(argv[2]); kmin = atoi(argv[3]); kmax = atoi(argv[4]);
    famM = atoi(argv[5]); consttype = atoi(argv[6]); inherit = atoi(argv[7]);
    if (argc > 8) maxprint = atoi(argv[8]);
    for (K = kmin; K <= kmax; K++) {
        if (2 * K > N) break;
        gen(0, N);
        { printf("{\"minbh\":{"); int f=1; for(int i=0;i<64;i++) if(minbh_hist[i]){ printf("%s\"%d\":%lld",f?"":",",i-31,minbh_hist[i]); f=0;} printf("}}\n"); for(int i=0;i<64;i++) minbh_hist[i]=0; }
        printf("{\"k\":%d,\"rl\":%lld,\"data\":%lld,\"full\":%lld,\"cert\":%lld,\"feasible\":%lld,\"enum_sols\":%lld,\"defect_ok\":%lld,\"defect_bad\":%lld}\n",
               K, cnt_rl[K], cnt_data[K], cnt_full[K], cnt_cert[K], cnt_feas[K], enum_sols[K], def_ok[K], def_bad[K]);
        fflush(stdout);
    }
    return 0;
}
