// Bounded three-outside-flip continuation of the immutable two-flip local solver.
#define main frontier_two_outer_main
#include "frontier-20261028-core-outer-search.cpp"
#undef main

namespace {
void write_three_witness(const Problem& p, const Outcome& result, int z, const std::string& file_name, int seed) {
    require_unused(file_name);
    Table bits = p.bits;
    bits[result.first_outer_x] ^= 1;
    bits[result.first_outer_y] ^= 1;
    bits[z] ^= 1;
    for (int u = 0; u < LOCAL; ++u) bits[p.coords[u]] = (result.first_local >> u) & 1;
    for (int x = 0; x < N; ++x) bits[x] ^= __builtin_parity(x & result.first_frequency);
    int w[N];
    for (int x = 0; x < N; ++x) w[x] = 1 - 2 * bits[x];
    fwht(w, N);
    int peak = 0;
    for (int value : w) peak = std::max(peak, std::abs(value));
    if (w[0] != 0 || peak > 28) throw std::runtime_error("internal three-flip witness check failed");
    std::ofstream out(file_name);
    if (!out) throw std::runtime_error("cannot create witness");
    out << "{\n  \"format\": \"boolean-truth-v1\",\n  \"seed_index_1based\":" << seed
        << ",\n  \"outside_flip_indices\":[" << result.first_outer_x << ',' << result.first_outer_y << ',' << z
        << "],\n  \"core_origin\":" << p.origin << ",\n  \"core_basis\":["
        << p.basis[0] << ',' << p.basis[1] << ',' << p.basis[2] << ',' << p.basis[3]
        << "],\n  \"local_pattern\":" << result.first_local
        << ",\n  \"affine_twist_frequency\":" << result.first_frequency << ",\n  \"bits\":\"";
    for (int bit : bits) out << bit;
    out << "\"\n}\n";
    if (!out) throw std::runtime_error("witness output failed");
}
}

int main(int argc, char** argv) {
    try {
        if (argc != 6) throw std::runtime_error("usage: triples SEEDS SEED_INDEX LIMIT MAX_SECONDS RESULT_JSON");
        const int index = std::stoi(argv[2]);
        const long long limit = std::stoll(argv[3]);
        const int max_seconds = std::stoi(argv[4]);
        if (index < 1 || index > 3 || limit < 0 || max_seconds < 1 || max_seconds > 300)
            throw std::runtime_error("invalid arguments");
        require_unused(argv[5]);
        const auto seeds = load_seeds(argv[1]);
        if (index > static_cast<int>(seeds.size())) throw std::runtime_error("seed index out of range");
        precompute_local();
        const Problem original = build_problem(seeds[index - 1], index);
        Problem shifted = original;
        Outcome out;
        int last_z = -1, witness_z = -1;
        bool stop = false;
        const auto start = std::chrono::steady_clock::now();
        for (std::size_t k = 2; k < original.outside.size() && !stop; ++k) {
            const int z = original.outside[k];
            for (int a = 0; a < N; ++a) shifted.r0[a] = original.r0[a] + delta[z][a];
            for (std::size_t i = 0; i + 1 < k && !stop; ++i)
                for (std::size_t j = i + 1; j < k; ++j) {
                    ++out.tested;
                    last_z = z;
                    if (evaluate(shifted, original.outside[i], original.outside[j], out)) {
                        out.stopped_for_witness = true; witness_z = z; stop = true; break;
                    }
                    if (out.tested % 100000 == 0)
                        std::cout << "tested=" << out.tested << " valid_outer=" << out.valid_outer << std::endl;
                    if (limit && out.tested >= limit) { stop = true; break; }
                    if ((out.tested & 255) == 0 &&
                        std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count() >= max_seconds) {
                        out.timed_out = true; stop = true; break;
                    }
                }
        }
        const long long total = 496LL * 495 * 494 / 6;
        out.complete = out.tested == total;
        if (out.stopped_for_witness)
            write_three_witness(original, out, witness_z,
                "frontier-20261028-core-outer-three-witness-seed" + std::to_string(index) + ".json", index);
        const double elapsed = std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count();
        std::ofstream file(argv[5]);
        if (!file) throw std::runtime_error("cannot create result");
        file << "{\n  \"seed_index_1based\":" << index << ",\n  \"mode\":\"three-outside\",\n"
             << "  \"total_outer_subsets\":" << total << ",\n  \"tested\":" << out.tested
             << ",\n  \"complete\":" << (out.complete ? "true" : "false")
             << ",\n  \"timed_out\":" << (out.timed_out ? "true" : "false")
             << ",\n  \"stopped_for_witness\":" << (out.stopped_for_witness ? "true" : "false")
             << ",\n  \"valid_outer_subsets\":" << out.valid_outer
             << ",\n  \"valid_outer_local_pairs\":" << out.valid_local_pairs
             << ",\n  \"target_outer_subsets\":" << out.target_outer
             << ",\n  \"target_outer_local_pairs\":" << out.target_local_pairs
             << ",\n  \"last_outer_z\":" << last_z << ",\n  \"witness_outer_z\":" << witness_z
             << ",\n  \"elapsed_seconds\":" << elapsed << "\n}\n";
        if (!file) throw std::runtime_error("result write failed");
        std::cout << "seed=" << index << " tested=" << out.tested << '/' << total
                  << " complete=" << out.complete << " timed_out=" << out.timed_out
                  << " valid_outer=" << out.valid_outer << " target_outer=" << out.target_outer
                  << " elapsed=" << elapsed << "s\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << '\n';
        return 1;
    }
}
