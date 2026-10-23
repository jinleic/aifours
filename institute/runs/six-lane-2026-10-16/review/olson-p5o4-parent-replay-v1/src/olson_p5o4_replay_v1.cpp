// Parent replay of worker claim C5' (ordered Olson over D_10, p = 5, four odd blocks, length 18, target 10).
// Written from the definitions only (worker PLAN-v1 sections 1-3); no worker code is read, imported or run.
//
// Group: (v,e)(v',e') = (v + e v', e e') mod 5, rho_x = (x,+1), sigma_y = (y,-1).  Element index g = v + 5*[e = -1].
// Domain: linear words R_1 S_1 R_2 S_2 R_3 S_3 R_4 S_4 of length 18, S_i = sigma_{y_i}^{l_i}, l_i = 2 a_i + 1,
// R_i a (possibly empty) run of rotations; runs are iterated as multisets written in ascending value order (fact (a)).
// H = a_1 + ... + a_4, R = 14 - 2H rotation letters.  Solved = some 10 letters in index order multiply to e.
//
// Build: clang++ -O2 -std=c++17 -Wall -Wextra -o bin/replay_v1 src/olson_p5o4_replay_v1.cpp
// Modes:
//   controls OUTDIR                               group self-test, PC-k2, DP-vs-naive samples, filter-vs-DP samples
//   enum OUTDIR none|untwisted|target8|parity     full enumeration: filter (d) per (H, multiset), DP on every survivor word
//   brute OUTDIR HMIN HMAX                        DP on EVERY word of layers HMIN..HMAX (no filter); filter consistency
//   check OUTDIR CLASSFILE                        DP + naive on every l-tuple of each class line in CLASSFILE
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <fcntl.h>
#include <sys/resource.h>
#include <sys/stat.h>
#include <time.h>
#include <unistd.h>

typedef unsigned long long u64;

static const int P = 5, NG = 10, ID = 0, WLEN = 18, FULL = 10, NY = 625, CODES = 759375;  // 15^5
static int g_untwisted = 0, g_target8 = 0, g_parity = 0, TARGET = FULL;
static int MUL[NG][NG];
static uint16_t TAB[NG][1 << NG];
static u64 FACT[16];

static inline int gidx(int v, int e) {
  v %= P;
  if (v < 0) v += P;
  return v + (e == -1 ? P : 0);
}
static inline int gv(int g) { return g % P; }
static inline int ge(int g) { return g < P ? 1 : -1; }
static inline int RHO(int x) { return gidx(x, 1); }
static inline int SIG(int y) { return gidx(y, -1); }

static void build_group() {
  for (int a = 0; a < NG; a++)
    for (int b = 0; b < NG; b++) {
      // correct law: (v + e v', e e'); BUG untwisted: (v + v', e e')
      int v = g_untwisted ? gv(a) + gv(b) : gv(a) + ge(a) * gv(b);
      MUL[a][b] = gidx(v, ge(a) * ge(b));
    }
  for (int g = 0; g < NG; g++)
    for (int m = 0; m < (1 << NG); m++) {
      unsigned r = 0;
      for (int h = 0; h < NG; h++)
        if (m >> h & 1) r |= 1u << MUL[h][g];  // right multiplication by the new letter g
      TAB[g][m] = (uint16_t)r;
    }
  TARGET = g_target8 ? 8 : FULL;  // BUG target8: test length-8 subwords
  FACT[0] = 1;
  for (int i = 1; i < 16; i++) FACT[i] = FACT[i - 1] * (u64)i;
}

// ---------------- exact ordered DP: r[c] = set of products of c selected letters (bit mask over the 10 elements)
struct St {
  uint16_t r[FULL + 1];
};
static inline void st_init(St& s) {
  memset(s.r, 0, sizeof s.r);
  s.r[0] = (uint16_t)(1u << ID);
}
static inline void st_push(St& s, int g) {
  const uint16_t* t = TAB[g];
  for (int c = FULL; c >= 1; c--) s.r[c] |= t[s.r[c - 1]];  // descending c: r[c-1] is still the old value
}
static inline bool st_solved(const St& s) { return (s.r[TARGET] >> ID) & 1; }
static bool dp_scratch(const int* w, int n) {
  St s;
  st_init(s);
  for (int p = 0; p < n; p++) st_push(s, w[p]);
  return st_solved(s);
}

// ---------------- naive check: every k-subset of positions, product left to right with MUL
static bool naive_solved(const int* w, int n, int k) {
  int id[WLEN];
  for (int i = 0; i < k; i++) id[i] = i;
  for (;;) {
    int g = ID;
    for (int i = 0; i < k; i++) g = MUL[g][w[id[i]]];
    if (g == ID) return true;
    int i = k - 1;
    while (i >= 0 && id[i] == n - k + i) i--;
    if (i < 0) return false;
    id[i]++;
    for (int j = i + 1; j < k; j++) id[j] = id[j - 1] + 1;
  }
}

static int build_word(const int c[4][P], const int a[4], const int y[4], int* w) {
  int n = 0;
  for (int i = 0; i < 4; i++) {
    for (int x = 0; x < P; x++)
      for (int k = 0; k < c[i][x]; k++) w[n++] = RHO(x);
    for (int k = 0; k < 2 * a[i] + 1; k++) w[n++] = SIG(y[i]);
  }
  return n;
}

static std::string word_str(const int* w, int n) {
  std::string s;
  int i = 0;
  while (i < n) {
    int j = i;
    while (j < n && w[j] == w[i]) j++;
    char buf[32];
    if (j - i > 1)
      snprintf(buf, sizeof buf, "%s%c%d^%d", s.empty() ? "" : " ", ge(w[i]) == 1 ? 'r' : 's', gv(w[i]), j - i);
    else
      snprintf(buf, sizeof buf, "%s%c%d", s.empty() ? "" : " ", ge(w[i]) == 1 ? 'r' : 's', gv(w[i]));
    s += buf;
    i = j;
  }
  return s;
}

static std::string runs_str(const int c[4][P]) {
  std::string s;
  for (int i = 0; i < 4; i++) {
    if (i) s += '/';
    int n = 0;
    for (int x = 0; x < P; x++)
      for (int k = 0; k < c[i][x]; k++) {
        s += (char)('0' + x);
        n++;
      }
    if (!n) s += '-';
  }
  return s;
}

// ---------------- fact (d): j <= H pairs inside blocks + a zero-sum rotation sub-multiset of size 10 - 2j
static bool filter_d(int H, const int m[P]) {
  int R = 0;
  for (int x = 0; x < P; x++) R += m[x];
  int pairs = g_parity ? H + 4 : H;  // BUG parity: each odd block credited (l+1)/2 identity pairs
  int jmax = pairs < 5 ? pairs : 5;
  for (int j = 0; j <= jmax; j++) {
    int s = FULL - 2 * j;
    if (s > R) continue;
    for (int t0 = 0; t0 <= m[0]; t0++)
      for (int t1 = 0; t1 <= m[1]; t1++)
        for (int t2 = 0; t2 <= m[2]; t2++)
          for (int t3 = 0; t3 <= m[3]; t3++) {
            int t4 = s - t0 - t1 - t2 - t3;
            if (t4 < 0 || t4 > m[4]) continue;
            if ((t1 + 2 * t2 + 3 * t3 + 4 * t4) % P == 0) return true;
          }
  }
  return false;
}

// rigid: every rotation value in one {c, -c}, c != 0 (vacuous for no rotations)
static bool rigid(const int m[P]) {
  if (m[0] > 0) return false;
  bool a = m[1] + m[4] > 0, b = m[2] + m[3] > 0;
  return !(a && b);
}

static u64 binom(int n, int k) {
  if (k < 0 || k > n) return 0;
  u64 r = 1;
  for (int i = 1; i <= k; i++) r = r * (u64)(n - k + i) / (u64)i;
  return r;
}
static u64 pow5(int e) {
  u64 r = 1;
  while (e-- > 0) r *= 5;
  return r;
}
static inline int mcode(const int m[P]) { return m[0] + 15 * (m[1] + 15 * (m[2] + 15 * (m[3] + 15 * m[4]))); }

static double now_s() {
  struct timespec ts;
  clock_gettime(CLOCK_MONOTONIC, &ts);
  return (double)ts.tv_sec + 1e-9 * (double)ts.tv_nsec;
}
static long maxrss_bytes() {
  struct rusage ru;
  getrusage(RUSAGE_SELF, &ru);
  return ru.ru_maxrss;  // bytes on macOS
}
static FILE* xopen(const std::string& path) {
  int fd = open(path.c_str(), O_WRONLY | O_CREAT | O_EXCL, 0644);
  if (fd < 0) {
    perror(path.c_str());
    exit(3);
  }
  FILE* f = fdopen(fd, "w");
  if (!f) {
    perror("fdopen");
    exit(3);
  }
  return f;
}
static void xmkdir(const std::string& path) {
  if (mkdir(path.c_str(), 0755) != 0) {
    perror(path.c_str());
    exit(3);
  }
}

// l-tuples (a1,a2,a3,a4), sum H, lexicographic in (a1,a2,a3)
static int LID[8][8][8];
static int setup_ltuples(int H, std::vector<std::array<int, 4>>& L) {
  L.clear();
  for (int a1 = 0; a1 <= H; a1++)
    for (int a2 = 0; a1 + a2 <= H; a2++)
      for (int a3 = 0; a1 + a2 + a3 <= H; a3++) {
        LID[a1][a2][a3] = (int)L.size();
        L.push_back({a1, a2, a3, H - a1 - a2 - a3});
      }
  return (int)L.size();
}

// all (l, y) completions of one run distribution c; DP state shared along common prefixes (exact memoisation)
template <class F>
static void enum_ly(const int c[4][P], int H, F& f) {
  St s0;
  st_init(s0);
  for (int x = 0; x < P; x++)
    for (int k = 0; k < c[0][x]; k++) st_push(s0, RHO(x));
  for (int a1 = 0; a1 <= H; a1++)
    for (int y1 = 0; y1 < P; y1++) {
      St s1 = s0;
      for (int k = 0; k < 2 * a1 + 1; k++) st_push(s1, SIG(y1));
      for (int x = 0; x < P; x++)
        for (int k = 0; k < c[1][x]; k++) st_push(s1, RHO(x));
      for (int a2 = 0; a1 + a2 <= H; a2++)
        for (int y2 = 0; y2 < P; y2++) {
          St s2 = s1;
          for (int k = 0; k < 2 * a2 + 1; k++) st_push(s2, SIG(y2));
          for (int x = 0; x < P; x++)
            for (int k = 0; k < c[2][x]; k++) st_push(s2, RHO(x));
          for (int a3 = 0; a1 + a2 + a3 <= H; a3++)
            for (int y3 = 0; y3 < P; y3++) {
              St s3 = s2;
              for (int k = 0; k < 2 * a3 + 1; k++) st_push(s3, SIG(y3));
              for (int x = 0; x < P; x++)
                for (int k = 0; k < c[3][x]; k++) st_push(s3, RHO(x));
              int a4 = H - a1 - a2 - a3;
              for (int y4 = 0; y4 < P; y4++) {
                St s4 = s3;
                for (int k = 0; k < 2 * a4 + 1; k++) st_push(s4, SIG(y4));
                f(a1, a2, a3, a4, y1, y2, y3, y4, st_solved(s4));
              }
            }
        }
    }
}

// all 4-tuples of run multisets (20 counts c[run][value]) with total R
template <class F>
static void rec_dist(int k, int rem, int c[4][P], F& f) {
  if (k == 4 * P - 1) {
    c[3][P - 1] = rem;
    f(c);
    c[3][P - 1] = 0;
    return;
  }
  int r = k / P, x = k % P;
  for (int t = 0; t <= rem; t++) {
    c[r][x] = t;
    rec_dist(k + 1, rem - t, c, f);
  }
  c[r][x] = 0;
}

template <class F>
static void for_multisets(int R, F& f) {
  int m[P];
  for (m[0] = 0; m[0] <= R; m[0]++)
    for (m[1] = 0; m[0] + m[1] <= R; m[1]++)
      for (m[2] = 0; m[0] + m[1] + m[2] <= R; m[2]++)
        for (m[3] = 0; m[0] + m[1] + m[2] + m[3] <= R; m[3]++) {
          m[4] = R - m[0] - m[1] - m[2] - m[3];
          f(m);
        }
}

static void yfmt(int yc, char* buf) { snprintf(buf, 8, "%d%d%d%d", yc / 125, yc / 25 % 5, yc / 5 % 5, yc % 5); }

// ======================================================================= enum
static int run_enum(const std::string& out, const std::string& bug) {
  if (bug == "untwisted") g_untwisted = 1;
  else if (bug == "target8") g_target8 = 1;
  else if (bug == "parity") g_parity = 1;
  else if (bug != "none") {
    fprintf(stderr, "unknown bug %s\n", bug.c_str());
    return 2;
  }
  build_group();
  xmkdir(out);
  FILE* fav = xopen(out + "/avoider_classes.txt");
  FILE* fmx = xopen(out + "/mixed_classes.txt");
  FILE* fnr = xopen(out + "/nonrigid_avoider_classes.txt");
  FILE* fsv = xopen(out + "/survivor_multisets.txt");
  FILE* fsm = xopen(out + "/summary.json");
  double t0 = now_s();
  std::vector<int8_t> filt(CODES);
  int fail = 0;
  u64 T_words_formula = 0, T_words_filter = 0, T_words_dp = 0, T_avoid_words = 0, T_cls_all = 0, T_cls_mixed = 0,
      T_nr_words = 0, T_mism = 0, T_words_formula_H04 = 0;
  fprintf(fsm, "{\n  \"mode\": \"enum\",\n  \"bug\": \"%s\",\n  \"per_H\": [\n", bug.c_str());
  for (int H = 0; H <= 7; H++) {
    int R = 14 - 2 * H;
    std::vector<std::array<int, 4>> L;
    int nL = setup_ltuples(H, L);
    u64 nLf = binom(H + 3, 3);
    // ---- multiset level: filter decision per (H, M)
    u64 ms_total = 0, ms_solved = 0, ms_surv = 0, ms_surv_rigid = 0, sum_prod = 0, surv_dist_formula = 0;
    std::fill(filt.begin(), filt.end(), (int8_t)-1);
    auto fm = [&](const int* m) {
      bool s = filter_d(H, m);
      filt[mcode(m)] = s ? 1 : 0;
      ms_total++;
      u64 pr = 1;
      for (int x = 0; x < P; x++) pr *= binom(m[x] + 3, 3);
      sum_prod += pr;
      if (s) ms_solved++;
      else {
        ms_surv++;
        if (rigid(m)) ms_surv_rigid++;
        surv_dist_formula += pr;
        fprintf(fsv, "H=%d|M=%d,%d,%d,%d,%d|rigid=%d|dists=%llu\n", H, m[0], m[1], m[2], m[3], m[4], rigid(m) ? 1 : 0, pr);
      }
    };
    for_multisets(R, fm);
    // ---- distribution level: explicit enumeration of all C(R+19,19) run-multiset 4-tuples
    u64 d_total = 0, d_solved = 0, d_surv = 0, w_filter = 0, w_dp = 0, w_dp_solved = 0, w_dp_avoid = 0, cls_dp = 0,
        cls_all = 0, cls_mixed = 0, cls_none = 0, nr_words = 0, nr_classes = 0, mism = 0, lit_total = 0, badlen = 0;
    static u64 mask[NY][2];  // bit b = l-tuple index b (nL <= 120 < 128)
    auto leaf = [&](int c[4][P]) {
      int m[P];
      for (int x = 0; x < P; x++) m[x] = c[0][x] + c[1][x] + c[2][x] + c[3][x];
      int8_t fv = filt[mcode(m)];
      u64 num = 1, den = 1;
      for (int r = 0; r < 4; r++) {
        int rr = 0;
        for (int x = 0; x < P; x++) {
          rr += c[r][x];
          den *= FACT[c[r][x]];
        }
        num *= FACT[rr];
      }
      lit_total += num / den;
      d_total++;
      if (fv != 0) {  // (d) holds: all nL*625 completions solved (proved), counted
        d_solved++;
        w_filter += (u64)nL * NY;
        return;
      }
      d_surv++;
      memset(mask, 0, sizeof mask);
      bool rg = rigid(m);
      auto cb = [&](int a1, int a2, int a3, int a4, int y1, int y2, int y3, int y4, bool solved) {
        int a[4] = {a1, a2, a3, a4}, y[4] = {y1, y2, y3, y4}, w[WLEN + 8];
        int n = build_word(c, a, y, w);
        if (n != WLEN) badlen++;
        if (dp_scratch(w, n) != solved) mism++;
        w_dp++;
        if (solved) w_dp_solved++;
        else {
          w_dp_avoid++;
          int b = LID[a1][a2][a3];
          mask[((y1 * P + y2) * P + y3) * P + y4][b >> 6] |= 1ull << (b & 63);
        }
      };
      enum_ly(c, H, cb);
      std::string rs = runs_str(c);
      for (int yc = 0; yc < NY; yc++) {
        cls_dp++;
        int k = __builtin_popcountll(mask[yc][0]) + __builtin_popcountll(mask[yc][1]);
        if (k == 0) {
          cls_none++;
          continue;
        }
        char yb[8];
        yfmt(yc, yb);
        if (k == nL) {
          cls_all++;
          fprintf(fav, "H=%d|runs=%s|y=%s|lavoid=%d/%d\n", H, rs.c_str(), yb, k, nL);
        } else {
          cls_mixed++;
          fprintf(fmx, "H=%d|runs=%s|y=%s|lavoid=%d/%d|mask=%llx:%llx\n", H, rs.c_str(), yb, k, nL, mask[yc][1], mask[yc][0]);
        }
        if (!rg) {
          nr_classes++;
          nr_words += (u64)k;
          fprintf(fnr, "H=%d|runs=%s|y=%s|lavoid=%d/%d|mask=%llx:%llx\n", H, rs.c_str(), yb, k, nL, mask[yc][1], mask[yc][0]);
        }
      }
    };
    int c[4][P];
    memset(c, 0, sizeof c);
    rec_dist(0, R, c, leaf);
    u64 dist_formula = binom(R + 19, 19);
    u64 words_formula = nLf * (u64)NY * dist_formula;
    u64 lit_formula = binom(R + 3, 3) * pow5(R);
    bool ok = ((u64)nL == nLf) && ms_total == binom(R + 4, 4) && sum_prod == dist_formula && d_total == dist_formula &&
              d_solved + d_surv == d_total && d_surv == surv_dist_formula && w_filter + w_dp == words_formula &&
              w_dp == d_surv * (u64)nL * NY && cls_dp == d_surv * NY && lit_total == lit_formula && mism == 0 &&
              badlen == 0;
    if (!ok) fail = 1;
    T_words_formula += words_formula;
    if (H <= 4) T_words_formula_H04 += words_formula;
    T_words_filter += w_filter;
    T_words_dp += w_dp;
    T_avoid_words += w_dp_avoid;
    T_cls_all += cls_all;
    T_cls_mixed += cls_mixed;
    T_nr_words += nr_words;
    T_mism += mism;
    fprintf(fsm,
            "    {\"H\": %d, \"R\": %d, \"ltuples_enumerated\": %d, \"ltuples_formula\": %llu, \"ytuples\": %d,\n"
            "     \"multisets_enumerated\": %llu, \"multisets_formula\": %llu, \"multisets_filter_solved\": %llu,"
            " \"multisets_survivors\": %llu, \"multisets_survivors_rigid\": %llu,\n"
            "     \"dists_enumerated\": %llu, \"dists_formula_C(R+19,19)\": %llu, \"sum_over_M_prod_C(m_x+3,3)\": %llu,"
            " \"dists_filter_solved\": %llu, \"dists_survivors\": %llu, \"dists_survivors_formula\": %llu,\n"
            "     \"words_formula\": %llu, \"words_filter_solved_counted\": %llu, \"words_dp_enumerated\": %llu,"
            " \"words_dp_solved\": %llu, \"words_dp_avoid\": %llu,\n"
            "     \"classes_dp\": %llu, \"classes_all_l_avoid\": %llu, \"classes_mixed\": %llu, \"classes_no_avoid\": %llu,"
            " \"nonrigid_avoider_classes\": %llu, \"nonrigid_avoider_words\": %llu,\n"
            "     \"prefix_vs_scratch_mismatches\": %llu, \"bad_word_lengths\": %llu,"
            " \"literal_run_sequences_enumerated\": %llu, \"literal_run_sequences_formula_C(R+3,3)*5^R\": %llu,"
            " \"literal_words\": %llu, \"checks_ok\": %s}%s\n",
            H, R, nL, nLf, NY, ms_total, binom(R + 4, 4), ms_solved, ms_surv, ms_surv_rigid, d_total, dist_formula,
            sum_prod, d_solved, d_surv, surv_dist_formula, words_formula, w_filter, w_dp, w_dp_solved, w_dp_avoid,
            cls_dp, cls_all, cls_mixed, cls_none, nr_classes, nr_words, mism, badlen, lit_total, lit_formula,
            lit_total * nLf * (u64)NY, ok ? "true" : "false", H < 7 ? "," : "");
    fflush(fsm);
  }
  double el = now_s() - t0;
  fprintf(fsm,
          "  ],\n  \"totals\": {\"words_formula_H0_7\": %llu, \"words_formula_H0_4\": %llu, \"words_filter_solved_counted\": %llu,"
          " \"words_dp_enumerated\": %llu, \"avoider_words\": %llu, \"avoider_classes_all_l\": %llu, \"mixed_classes\": %llu,"
          " \"nonrigid_avoider_words\": %llu, \"prefix_vs_scratch_mismatches\": %llu},\n"
          "  \"all_checks_ok\": %s,\n  \"elapsed_s\": %.3f,\n  \"maxrss_bytes\": %ld\n}\n",
          T_words_formula, T_words_formula_H04, T_words_filter, T_words_dp, T_avoid_words, T_cls_all, T_cls_mixed,
          T_nr_words, T_mism, fail ? "false" : "true", el, maxrss_bytes());
  fclose(fav);
  fclose(fmx);
  fclose(fnr);
  fclose(fsv);
  fclose(fsm);
  printf("enum bug=%s done: avoider_classes=%llu mixed=%llu avoider_words=%llu nonrigid_words=%llu dp_words=%llu ok=%d "
         "elapsed=%.1fs\n",
         bug.c_str(), T_cls_all, T_cls_mixed, T_avoid_words, T_nr_words, T_words_dp, !fail, el);
  return fail ? 1 : 0;
}

// ======================================================================= brute (no filter) on layers hmin..hmax
static int run_brute(const std::string& out, int hmin, int hmax) {
  build_group();
  xmkdir(out);
  FILE* fav = xopen(out + "/avoider_classes.txt");
  FILE* fmx = xopen(out + "/mixed_classes.txt");
  FILE* fsm = xopen(out + "/summary.json");
  double t0 = now_s();
  std::vector<int8_t> filt(CODES);
  int fail = 0;
  fprintf(fsm, "{\n  \"mode\": \"brute\",\n  \"per_H\": [\n");
  for (int H = hmin; H <= hmax; H++) {
    int R = 14 - 2 * H;
    std::vector<std::array<int, 4>> L;
    int nL = setup_ltuples(H, L);
    std::fill(filt.begin(), filt.end(), (int8_t)-1);
    auto fm = [&](const int* m) { filt[mcode(m)] = filter_d(H, m) ? 1 : 0; };
    for_multisets(R, fm);
    u64 d_total = 0, words = 0, solved_w = 0, avoid_w = 0, viol = 0, stride_checked = 0, stride_mism = 0, cls_all = 0,
        cls_mixed = 0, avoid_in_surv = 0;
    static u64 mask[NY][2];  // bit b = l-tuple index b (nL <= 120 < 128)
    auto leaf = [&](int c[4][P]) {
      int m[P];
      for (int x = 0; x < P; x++) m[x] = c[0][x] + c[1][x] + c[2][x] + c[3][x];
      int8_t fv = filt[mcode(m)];
      d_total++;
      bool any = false;
      auto cb = [&](int a1, int a2, int a3, int a4, int y1, int y2, int y3, int y4, bool solved) {
        if (words % 1009 == 0) {
          int a[4] = {a1, a2, a3, a4}, y[4] = {y1, y2, y3, y4}, w[WLEN + 8];
          int n = build_word(c, a, y, w);
          stride_checked++;
          if (n != WLEN || dp_scratch(w, n) != solved) stride_mism++;
        }
        words++;
        if (solved) solved_w++;
        else {
          avoid_w++;
          if (fv != 0) viol++;  // filter said solved but the DP found an avoider
          if (!any) {
            memset(mask, 0, sizeof mask);
            any = true;
          }
          int b = LID[a1][a2][a3];
          mask[((y1 * P + y2) * P + y3) * P + y4][b >> 6] |= 1ull << (b & 63);
        }
      };
      enum_ly(c, H, cb);
      if (!any) return;
      std::string rs = runs_str(c);
      if (fv == 0) avoid_in_surv++;
      for (int yc = 0; yc < NY; yc++) {
        int k = __builtin_popcountll(mask[yc][0]) + __builtin_popcountll(mask[yc][1]);
        if (k == 0) continue;
        char yb[8];
        yfmt(yc, yb);
        if (k == nL) {
          cls_all++;
          fprintf(fav, "H=%d|runs=%s|y=%s|lavoid=%d/%d\n", H, rs.c_str(), yb, k, nL);
        } else {
          cls_mixed++;
          fprintf(fmx, "H=%d|runs=%s|y=%s|lavoid=%d/%d|mask=%llx:%llx\n", H, rs.c_str(), yb, k, nL, mask[yc][1], mask[yc][0]);
        }
      }
    };
    int c[4][P];
    memset(c, 0, sizeof c);
    rec_dist(0, R, c, leaf);
    u64 dist_formula = binom(R + 19, 19);
    u64 words_formula = binom(H + 3, 3) * (u64)NY * dist_formula;
    bool ok = d_total == dist_formula && words == words_formula && viol == 0 && stride_mism == 0;
    if (!ok) fail = 1;
    fprintf(fsm,
            "    {\"H\": %d, \"R\": %d, \"dists_enumerated\": %llu, \"dists_formula\": %llu, \"words_dp_enumerated\": %llu,"
            " \"words_formula\": %llu, \"words_solved\": %llu, \"words_avoid\": %llu, \"filter_violations\": %llu,"
            " \"classes_all_l_avoid\": %llu, \"classes_mixed\": %llu, \"scratch_rechecked\": %llu,"
            " \"scratch_mismatches\": %llu, \"checks_ok\": %s, \"elapsed_cum_s\": %.3f}%s\n",
            H, R, d_total, dist_formula, words, words_formula, solved_w, avoid_w, viol, cls_all, cls_mixed,
            stride_checked, stride_mism, ok ? "true" : "false", now_s() - t0, H < hmax ? "," : "");
    fflush(fsm);
    fflush(fav);
    (void)avoid_in_surv;
  }
  double el = now_s() - t0;
  fprintf(fsm, "  ],\n  \"all_checks_ok\": %s,\n  \"elapsed_s\": %.3f,\n  \"maxrss_bytes\": %ld\n}\n", fail ? "false" : "true",
          el, maxrss_bytes());
  fclose(fav);
  fclose(fmx);
  fclose(fsm);
  printf("brute H=%d..%d done ok=%d elapsed=%.1fs\n", hmin, hmax, !fail, el);
  return fail ? 1 : 0;
}

// ======================================================================= controls
static u64 rng_s = 0x5EED0F01A11CE5ull;
static u64 rnd() {
  u64 z = (rng_s += 0x9E3779B97F4A7C15ull);
  z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ull;
  z = (z ^ (z >> 27)) * 0x94D049BB133111EBull;
  return z ^ (z >> 31);
}
static int rndint(int n) { return (int)(rnd() % (u64)n); }

static int group_selftest(FILE* f) {
  int bad = 0;
  for (int a = 0; a < NG; a++) {
    if (MUL[ID][a] != a || MUL[a][ID] != a) bad++;
    int inv = 0;
    for (int b = 0; b < NG; b++)
      if (MUL[a][b] == ID && MUL[b][a] == ID) inv++;
    if (inv != 1) bad++;
    for (int b = 0; b < NG; b++)
      for (int c = 0; c < NG; c++)
        if (MUL[MUL[a][b]][c] != MUL[a][MUL[b][c]]) bad++;
  }
  int nonab = 0;
  for (int a = 0; a < NG; a++)
    for (int b = 0; b < NG; b++)
      if (MUL[a][b] != MUL[b][a]) nonab++;
  int rel = 0;
  for (int x = 0; x < P; x++)
    for (int y = 0; y < P; y++) {
      if (MUL[SIG(y)][SIG(y)] != ID) rel++;
      if (MUL[RHO(x)][RHO(y)] != RHO(x + y)) rel++;
      if (MUL[SIG(y)][RHO(x)] != SIG(y - x)) rel++;
      if (MUL[RHO(x)][SIG(y)] != SIG(x + y)) rel++;
      if (MUL[SIG(x)][SIG(y)] != RHO(x - y)) rel++;
      if (MUL[MUL[SIG(y)][RHO(x)]][SIG(y)] != RHO(-x)) rel++;
    }
  fprintf(f, "  \"group_selftest\": {\"axiom_failures\": %d, \"noncommuting_ordered_pairs\": %d, \"relation_failures\": %d},\n",
          bad, nonab, rel);
  return bad + rel + (nonab == 0);
}

static int run_controls(const std::string& out) {
  build_group();
  xmkdir(out);
  FILE* f = xopen(out + "/controls.json");
  double t0 = now_s();
  int fail = 0;
  fprintf(f, "{\n  \"mode\": \"controls\",\n");
  fail += group_selftest(f);
  // ---- PC-k2 literal word and its block structure
  int pc[WLEN], n = 0;
  for (int k = 0; k < 9; k++) pc[n++] = RHO(1);
  for (int k = 0; k < 7; k++) pc[n++] = SIG(0);
  pc[n++] = RHO(4);
  pc[n++] = SIG(0);
  std::string blocks;
  int nrefl = 0, nodd = 0;
  for (int i = 0; i < n;) {
    int j = i;
    while (j < n && pc[j] == pc[i]) j++;
    if (ge(pc[i]) == -1) {
      nrefl++;
      if ((j - i) % 2) nodd++;
    }
    i = j;
  }
  // cyclic: first and last maximal constant runs merge only if w[0] == w[n-1]
  bool cyc_merge = pc[0] == pc[n - 1];
  bool pc_dp = dp_scratch(pc, n), pc_naive = naive_solved(pc, n, TARGET);
  fprintf(f,
          "  \"pc_k2\": {\"word\": \"%s\", \"length\": %d, \"maximal_linear_reflection_blocks\": %d,"
          " \"odd_maximal_reflection_blocks\": %d, \"first_last_letters_equal_cyclic_merge\": %s,"
          " \"dp_solved\": %s, \"naive_solved\": %s,\n",
          word_str(pc, n).c_str(), n, nrefl, nodd, cyc_merge ? "true" : "false", pc_dp ? "true" : "false",
          pc_naive ? "true" : "false");
  if (pc_dp || pc_naive) fail++;
  // its class in D: H = 2, runs (1^9, -, -, 4), y = 0000; all 10 l-tuples
  {
    int c[4][P];
    memset(c, 0, sizeof c);
    c[0][1] = 9;
    c[3][4] = 1;
    int y[4] = {0, 0, 0, 0};
    std::vector<std::array<int, 4>> L;
    setup_ltuples(2, L);
    int n_same = 0;
    fprintf(f, "    \"class_H2_runs_111111111/-/-/4_y0000\": [\n");
    for (size_t li = 0; li < L.size(); li++) {
      int a[4] = {L[li][0], L[li][1], L[li][2], L[li][3]}, w[WLEN + 8];
      int m = build_word(c, a, y, w);
      bool same = (m == n) && memcmp(w, pc, sizeof(int) * (size_t)n) == 0;
      n_same += same;
      bool d = dp_scratch(w, m), nv = naive_solved(w, m, TARGET);
      if (d != nv || (same && d)) fail++;  // the literal PC-k2 representations must avoid
      fprintf(f, "      {\"l\": [%d,%d,%d,%d], \"word\": \"%s\", \"equals_pc_k2_literally\": %s, \"dp_solved\": %s, \"naive_solved\": %s}%s\n",
              2 * a[0] + 1, 2 * a[1] + 1, 2 * a[2] + 1, 2 * a[3] + 1, word_str(w, m).c_str(), same ? "true" : "false",
              d ? "true" : "false", nv ? "true" : "false", li + 1 < L.size() ? "," : "");
    }
    fprintf(f, "    ],\n    \"n_ltuples_equal_to_pc_k2_literally\": %d},\n", n_same);
    if (n_same != 6) fail++;
  }
  // ---- PC-k2 under each injected bug
  {
    int m9[P] = {0, 9, 0, 0, 1};
    fprintf(f, "  \"pc_k2_under_bugs\": {");
    g_untwisted = 1;
    build_group();
    bool u_dp = dp_scratch(pc, n), u_nv = naive_solved(pc, n, TARGET);
    g_untwisted = 0;
    g_target8 = 1;
    build_group();
    bool t_dp = dp_scratch(pc, n), t_nv = naive_solved(pc, n, TARGET);
    g_target8 = 0;
    build_group();
    bool p_clean = filter_d(2, m9);
    g_parity = 1;
    bool p_bug = filter_d(2, m9);
    g_parity = 0;
    fprintf(f, "\"untwisted_dp_solved\": %s, \"untwisted_naive_solved\": %s, \"target8_dp_solved\": %s,"
               " \"target8_naive_solved\": %s, \"filter_d_clean\": %s, \"filter_d_parity_bug\": %s},\n",
            u_dp ? "true" : "false", u_nv ? "true" : "false", t_dp ? "true" : "false", t_nv ? "true" : "false",
            p_clean ? "true" : "false", p_bug ? "true" : "false");
  }
  // ---- rigidity predicate unit tests
  {
    int cases[8][P] = {{0, 2, 0, 0, 1}, {0, 0, 3, 1, 0}, {0, 6, 0, 0, 0}, {1, 5, 0, 0, 0},
                       {0, 1, 1, 0, 0}, {0, 0, 0, 1, 1}, {0, 1, 0, 1, 1}, {0, 0, 0, 0, 0}};
    int expect[8] = {1, 1, 1, 0, 0, 0, 0, 1};
    int bad = 0;
    for (int i = 0; i < 8; i++)
      if ((int)rigid(cases[i]) != expect[i]) bad++;
    fprintf(f, "  \"rigid_predicate_unit_failures\": %d,\n", bad);
    fail += bad;
  }
  // ---- S1: random domain words, DP vs naive
  std::vector<std::vector<std::array<int, P>>> surv(8);
  for (int H = 0; H <= 7; H++) {
    auto fm = [&](const int* m) {
      if (!filter_d(H, m)) surv[H].push_back({m[0], m[1], m[2], m[3], m[4]});
    };
    for_multisets(14 - 2 * H, fm);
  }
  auto random_completion = [&](int H, const int* m, int c[4][P], int a[4], int y[4]) {
    memset(c, 0, sizeof(int) * 4 * P);
    for (int x = 0; x < P; x++)
      for (int k = 0; k < m[x]; k++) c[rndint(4)][x]++;
    std::vector<std::array<int, 4>> L;
    setup_ltuples(H, L);
    int li = rndint((int)L.size());
    for (int i = 0; i < 4; i++) a[i] = L[li][i], y[i] = rndint(P);
  };
  {
    int N1 = 20000, mm = 0, av = 0;
    for (int t = 0; t < N1; t++) {
      int H = rndint(8), R = 14 - 2 * H, m[P] = {0, 0, 0, 0, 0};
      for (int k = 0; k < R; k++) m[rndint(P)]++;
      int c[4][P], a[4], y[4], w[WLEN + 8];
      random_completion(H, m, c, a, y);
      int len = build_word(c, a, y, w);
      bool d = dp_scratch(w, len), nv = naive_solved(w, len, TARGET);
      if (len != WLEN || d != nv) mm++;
      if (!d) av++;
    }
    fprintf(f, "  \"S1_random_domain_words\": {\"n\": %d, \"dp_vs_naive_mismatches\": %d, \"avoiders_seen\": %d},\n", N1, mm, av);
    fail += mm;
  }
  // ---- S2: random words over survivor multisets (both verdicts occur), DP vs naive
  {
    int N2 = 20000, mm = 0, av = 0, nr_av = 0;
    for (int t = 0; t < N2; t++) {
      int H = 1 + rndint(4);
      if (surv[H].empty()) continue;
      const auto& ms = surv[H][(size_t)rndint((int)surv[H].size())];
      int c[4][P], a[4], y[4], w[WLEN + 8];
      random_completion(H, ms.data(), c, a, y);
      int len = build_word(c, a, y, w);
      bool d = dp_scratch(w, len), nv = naive_solved(w, len, TARGET);
      if (len != WLEN || d != nv) mm++;
      if (!d) {
        av++;
        if (!rigid(ms.data())) nr_av++;
      }
    }
    fprintf(f, "  \"S2_random_survivor_multiset_words\": {\"n\": %d, \"dp_vs_naive_mismatches\": %d, \"avoiders_seen\": %d,"
               " \"nonrigid_avoiders_seen\": %d},\n", N2, mm, av, nr_av);
    fail += mm;
  }
  // ---- S3: every filter-solved (H, M), H = 0..7: 30 random completions by DP, 1 also by naive; all must be solved
  {
    int K = 30;
    u64 ms = 0, words = 0, dp_fail = 0, nv_checked = 0, nv_fail = 0;
    for (int H = 0; H <= 7; H++) {
      auto fm = [&](const int* m) {
        if (!filter_d(H, m)) return;
        ms++;
        for (int t = 0; t < K; t++) {
          int c[4][P], a[4], y[4], w[WLEN + 8];
          random_completion(H, m, c, a, y);
          int len = build_word(c, a, y, w);
          words++;
          if (len != WLEN || !dp_scratch(w, len)) dp_fail++;
          if (t == 0) {
            nv_checked++;
            if (!naive_solved(w, len, TARGET)) nv_fail++;
          }
        }
      };
      for_multisets(14 - 2 * H, fm);
    }
    fprintf(f, "  \"S3_filter_solved_multisets\": {\"multisets\": %llu, \"dp_words\": %llu, \"dp_not_solved\": %llu,"
               " \"naive_words\": %llu, \"naive_not_solved\": %llu},\n", ms, words, dp_fail, nv_checked, nv_fail);
    fail += (int)(dp_fail + nv_fail);
  }
  fprintf(f, "  \"failures\": %d,\n  \"elapsed_s\": %.3f,\n  \"maxrss_bytes\": %ld\n}\n", fail, now_s() - t0, maxrss_bytes());
  fclose(f);
  printf("controls done failures=%d\n", fail);
  return fail ? 1 : 0;
}

// ======================================================================= check class lines
static int run_check(const std::string& out, const std::string& classfile) {
  build_group();
  xmkdir(out);
  FILE* in = fopen(classfile.c_str(), "r");
  if (!in) {
    perror(classfile.c_str());
    return 3;
  }
  FILE* f = xopen(out + "/check.txt");
  char line[512];
  int fail = 0, nlines = 0;
  while (fgets(line, sizeof line, in)) {
    int H;
    char runs[128], ys[16];
    if (sscanf(line, "H=%d|runs=%127[^|]|y=%15[^|\n]", &H, runs, ys) != 3) continue;
    nlines++;
    int c[4][P], y[4];
    memset(c, 0, sizeof c);
    int ri = 0;
    for (const char* p = runs; *p; p++) {
      if (*p == '/') ri++;
      else if (*p >= '0' && *p <= '4') c[ri][*p - '0']++;
    }
    for (int i = 0; i < 4; i++) y[i] = ys[i] - '0';
    std::vector<std::array<int, 4>> L;
    setup_ltuples(H, L);
    int nav = 0, nnv = 0;
    for (auto& l : L) {
      int a[4] = {l[0], l[1], l[2], l[3]}, w[WLEN + 8];
      int len = build_word(c, a, y, w);
      bool d = dp_scratch(w, len), nv = naive_solved(w, len, TARGET);
      if (len != WLEN || d != nv) fail++;
      nav += !d;
      nnv += !nv;
      fprintf(f, "H=%d|runs=%s|y=%s|l=%d,%d,%d,%d|word=%s|dp=%s|naive=%s\n", H, runs, ys, 2 * a[0] + 1, 2 * a[1] + 1,
              2 * a[2] + 1, 2 * a[3] + 1, word_str(w, len).c_str(), d ? "solved" : "AVOID", nv ? "solved" : "AVOID");
    }
    fprintf(f, "# class summary H=%d|runs=%s|y=%s: dp_avoid=%d naive_avoid=%d of %zu l-tuples\n", H, runs, ys, nav, nnv,
            L.size());
  }
  fprintf(f, "# lines=%d dp_naive_disagreements=%d\n", nlines, fail);
  fclose(f);
  fclose(in);
  printf("check done lines=%d disagreements=%d\n", nlines, fail);
  return fail ? 1 : 0;
}

int main(int argc, char** argv) {
  if (argc < 3) {
    fprintf(stderr, "usage: %s controls|enum|brute|check OUTDIR [...]\n", argv[0]);
    return 2;
  }
  std::string mode = argv[1], out = argv[2];
  if (mode == "controls") return run_controls(out);
  if (mode == "enum" && argc == 4) return run_enum(out, argv[3]);
  if (mode == "brute" && argc == 5) return run_brute(out, atoi(argv[3]), atoi(argv[4]));
  if (mode == "check" && argc == 4) return run_check(out, argv[3]);
  fprintf(stderr, "bad arguments\n");
  return 2;
}
