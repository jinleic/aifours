// Independent dense modular elimination for the directly assembled tangent data.
// Input: header rows cols; then rows of count index value pairs (zero-based).
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>

using U = std::uint32_t;
using Wide = std::uint64_t;

static bool prime(U p) {
    if (p < 2) return false;
    for (U d = 2; static_cast<Wide>(d) * d <= p; ++d)
        if (p % d == 0) return false;
    return true;
}

static U power(U x, U n, U p) {
    U v = 1;
    while (n) {
        if (n & 1U) v = static_cast<U>(static_cast<Wide>(v) * x % p);
        x = static_cast<U>(static_cast<Wide>(x) * x % p);
        n >>= 1U;
    }
    return v;
}

int main(int argc, char** argv) {
    try {
        if (argc != 3) throw std::runtime_error("usage: modrank MATRIX PRIME");
        const auto raw_p = std::stoul(argv[2]);
        if (raw_p > std::numeric_limits<U>::max()) throw std::runtime_error("prime too large");
        const U p = static_cast<U>(raw_p);
        if (!prime(p)) throw std::runtime_error("modulus is not prime");
        std::ifstream input(argv[1]);
        std::size_t rows = 0, cols = 0;
        if (!(input >> rows >> cols) || rows == 0 || cols == 0)
            throw std::runtime_error("invalid header");
        std::vector<std::vector<U>> m(rows, std::vector<U>(cols, 0));
        std::size_t nnz = 0;
        for (std::size_t r = 0; r < rows; ++r) {
            std::size_t count = 0;
            if (!(input >> count) || count > cols) throw std::runtime_error("invalid row length");
            std::vector<bool> seen(cols, false);
            for (std::size_t k = 0; k < count; ++k) {
                std::size_t c = 0;
                long long value = 0;
                if (!(input >> c >> value) || c >= cols || seen[c] || value == 0)
                    throw std::runtime_error("invalid sparse entry");
                seen[c] = true;
                const auto rem = value % static_cast<long long>(p);
                m[r][c] = static_cast<U>((rem + p) % p);
                ++nnz;
            }
        }
        std::string extra;
        if (input >> extra) throw std::runtime_error("extra trailing matrix data");
        std::size_t pivots = 0;
        for (std::size_t c = 0; c < cols && pivots < rows; ++c) {
            std::size_t pivot = pivots;
            while (pivot < rows && m[pivot][c] == 0) ++pivot;
            if (pivot == rows) continue;
            std::swap(m[pivot], m[pivots]);
            const U inverse = power(m[pivots][c], p - 2, p);
            for (std::size_t j = c; j < cols; ++j)
                m[pivots][j] = static_cast<U>(static_cast<Wide>(m[pivots][j]) * inverse % p);
            for (std::size_t r = pivots + 1; r < rows; ++r) {
                const U factor = m[r][c];
                if (!factor) continue;
                m[r][c] = 0;
                for (std::size_t j = c + 1; j < cols; ++j) {
                    const U product = static_cast<U>(static_cast<Wide>(factor) * m[pivots][j] % p);
                    m[r][j] = static_cast<U>((static_cast<Wide>(m[r][j]) + p - product) % p);
                }
            }
            ++pivots;
        }
        std::cout << "{\"file\":\"" << argv[1] << "\",\"rows\":" << rows
                  << ",\"cols\":" << cols << ",\"nonzeros\":" << nnz
                  << ",\"prime\":" << p << ",\"rank\":" << pivots
                  << ",\"nullity\":" << cols - pivots << "}\n";
    } catch (const std::exception& e) {
        std::cerr << "ERROR: " << e.what() << '\n';
        return 1;
    }
}
