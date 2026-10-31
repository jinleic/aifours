// Exact finite-field rank of integer sparse-row input; modular rank is a
// lower bound on rational rank. No numerical approximation is involved.
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <vector>

constexpr std::int64_t P = 65521;

std::int64_t power(std::int64_t x, std::int64_t k) {
    std::int64_t result = 1;
    while (k) {
        if (k & 1) result = result * x % P;
        x = x * x % P;
        k >>= 1;
    }
    return result;
}

int main(int argc, char** argv) {
    if (argc != 2) throw std::runtime_error("usage: modrank matrix.txt");
    std::ifstream in(argv[1]);
    int rows, columns;
    if (!(in >> rows >> columns) || rows < 0 || columns < 0)
        throw std::runtime_error("invalid header");
    std::vector<std::int32_t> matrix(static_cast<std::size_t>(rows) * columns, 0);
    for (int r = 0; r < rows; ++r) {
        int count;
        if (!(in >> count) || count < 0 || count > columns)
            throw std::runtime_error("invalid sparse row");
        for (int k = 0; k < count; ++k) {
            int c, value;
            if (!(in >> c >> value) || c < 0 || c >= columns)
                throw std::runtime_error("invalid sparse entry");
            const std::size_t index = static_cast<std::size_t>(r) * columns + c;
            matrix[index] = static_cast<std::int32_t>((matrix[index] + value % P + P) % P);
        }
    }
    int rank = 0;
    for (int c = 0; c < columns && rank < rows; ++c) {
        int pivot = rank;
        while (pivot < rows && matrix[static_cast<std::size_t>(pivot)*columns+c] == 0) ++pivot;
        if (pivot == rows) continue;
        if (pivot != rank) {
            for (int j = c; j < columns; ++j)
                std::swap(matrix[static_cast<std::size_t>(pivot)*columns+j],
                          matrix[static_cast<std::size_t>(rank)*columns+j]);
        }
        auto* top = matrix.data() + static_cast<std::size_t>(rank)*columns;
        const std::int64_t inverse = power(top[c], P-2);
        for (int j = c; j < columns; ++j) top[j] = static_cast<std::int32_t>(top[j]*inverse % P);
        for (int r = rank+1; r < rows; ++r) {
            auto* row = matrix.data() + static_cast<std::size_t>(r)*columns;
            const std::int64_t factor = row[c];
            if (!factor) continue;
            for (int j = c; j < columns; ++j) {
                std::int64_t value = row[j] - factor*top[j] % P;
                if (value < 0) value += P;
                row[j] = static_cast<std::int32_t>(value);
            }
        }
        ++rank;
    }
    std::cout << "file " << argv[1] << " rows " << rows << " columns " << columns
              << " prime " << P << " rank " << rank << " nullity " << columns-rank << '\n';
}
