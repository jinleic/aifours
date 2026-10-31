// Independent exact scan of all disjoint original-variable F_n substitutions.
// Input: 1024 integer entropy numerators, H(empty) first, all at one scale.
// Uses recursive assignments to six blocks and the first difference of F_n.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <limits>
#include <string>

using i64 = std::int64_t;
using wide = __int128_t;
static i64 h[1024];
static std::uint64_t checked = 0, linear = 0, flat = 0;
static i64 largest_minimizer = 1;
static wide minimum = -1;

static i64 info(int a, int b, int z) {
    return h[a | z] + h[b | z] - h[a | b | z] - h[z];
}

static std::string evaluate(i64 a, i64 c, i64 d, i64& n, wide& twice) {
    if (a < 0 || d < 0) return "SHANNON_COMPONENT";
    if (d == 0 && c < 0) return "NEGATIVE_LINEAR_SLOPE";
    n = 1;
    if (d > 0 && c < 0) {
        wide quotient = (-(wide)c + d - 1) / d;
        if (quotient - 1 > std::numeric_limits<i64>::max()) return "MINIMIZER_RANGE";
        n = std::max<i64>(1, (i64)(quotient - 1));
    }
    twice = 2*(wide)a + 2*(wide)n*c + (wide)n*(n+1)*d;
    return twice < 0 ? "FAMILY_NEGATIVE" : "OK";
}

static bool visit(int k, int A, int B, int C, int D, int Z) {
    if (k != 10) {
        int bit = 1 << k;
        return visit(k+1,A,B,C,D,Z)
            && visit(k+1,A|bit,B,C,D,Z)
            && visit(k+1,A,B|bit,C,D,Z)
            && visit(k+1,A,B,C|bit,D,Z)
            && visit(k+1,A,B,C,D|bit,Z)
            && visit(k+1,A,B,C,D,Z|bit);
    }
    if (!A || !B || !C || !D || A >= B) return true;
    ++checked;
    i64 a = info(A,B,C|Z);
    i64 delta = info(A,B,Z) - info(A,B,D|Z) - info(C,D,Z);
    i64 c = a - delta;
    i64 d = info(A,C,B|Z) + info(B,C,A|Z);
    if (d == 0) { ++linear; if (c == 0) ++flat; }
    i64 n; wide twice;
    std::string status = evaluate(a,c,d,n,twice);
    if (status != "OK") {
        std::cerr << status << " A=" << A << " B=" << B << " C=" << C
                  << " D=" << D << " Z=" << Z << " a=" << a
                  << " c=" << c << " d=" << d << '\n';
        return false;
    }
    largest_minimizer = std::max(largest_minimizer,n);
    if (minimum < 0 || twice < minimum) minimum = twice;
    return true;
}

int main() {
    i64 n; wide twice;
    if (evaluate(1,-1,0,n,twice) != "NEGATIVE_LINEAR_SLOPE" ||
        evaluate(0,-2,1,n,twice) != "FAMILY_NEGATIVE" ||
        evaluate(1,0,0,n,twice) != "OK") {
        std::cerr << "SCALAR_CONTROL_WRONG_REASON\n"; return 1;
    }
    for (int i=0;i<1024;++i) if (!(std::cin >> h[i]) || h[i] < 0 || h[i] > 100000000) {
        std::cerr << "INPUT_RANGE_OR_COUNT\n"; return 1;
    }
    std::string extra; if (std::cin >> extra) { std::cerr << "INPUT_EXTRA\n"; return 1; }
    if (h[0] != 0) { std::cerr << "EMPTY_ENTROPY\n"; return 1; }
    if (!visit(0,0,0,0,0,0)) return 1;
    if (checked != 13729980ULL || minimum < 0 || minimum > std::numeric_limits<i64>::max()) {
        std::cerr << "COVERAGE_OR_MINIMUM\n"; return 1;
    }
    std::cout << "{\"disjoint_substitutions_mod_ab\":" << checked
              << ",\"linear_cases\":" << linear << ",\"flat_cases\":" << flat
              << ",\"minimum_twice_scaled_slack\":" << (i64)minimum
              << ",\"largest_first_minimizer_n\":" << largest_minimizer
              << ",\"scalar_controls\":{\"negative_linear_slope\":\"NEGATIVE_LINEAR_SLOPE\","
                 "\"negative_finite_minimum\":\"FAMILY_NEGATIVE\",\"positive\":\"OK\"}}\n";
}
