// Bounded four-outside-flip continuation using the pinned exact local solver.
#define main frontier_two_outer_main
#include "frontier-20261028-core-outer-search.cpp"
#undef main

namespace {
void write_four_witness(const Problem& p, const Outcome& r, int z, int v,
                        const std::string& name, int seed) {
    require_unused(name);
    Table bits = p.bits;
    for (int x : {r.first_outer_x, r.first_outer_y, z, v}) bits[x] ^= 1;
    for (int u=0; u<LOCAL; ++u) bits[p.coords[u]] = (r.first_local >> u) & 1;
    for (int x=0; x<N; ++x) bits[x] ^= __builtin_parity(x & r.first_frequency);
    int w[N];
    for (int x=0; x<N; ++x) w[x] = 1 - 2*bits[x];
    fwht(w,N);
    int peak=0;
    for (int value:w) peak=std::max(peak,std::abs(value));
    if (w[0]!=0 || peak>28) throw std::runtime_error("internal witness check failed");
    std::ofstream out(name);
    if (!out) throw std::runtime_error("cannot create witness");
    out << "{\n  \"format\":\"boolean-truth-v1\",\n  \"seed_index_1based\":" << seed
        << ",\n  \"outside_flip_indices\":[" << r.first_outer_x << ',' << r.first_outer_y << ',' << z << ',' << v
        << "],\n  \"core_origin\":" << p.origin << ",\n  \"core_basis\":["
        << p.basis[0] << ',' << p.basis[1] << ',' << p.basis[2] << ',' << p.basis[3]
        << "],\n  \"local_pattern\":" << r.first_local
        << ",\n  \"affine_twist_frequency\":" << r.first_frequency << ",\n  \"bits\":\"";
    for (int bit:bits) out << bit;
    out << "\"\n}\n";
    if (!out) throw std::runtime_error("witness write failed");
}
}
int main(int argc, char** argv) {
    try {
        if (argc!=6) throw std::runtime_error("usage: quads SEEDS INDEX LIMIT MAX_SECONDS RESULT_JSON");
        const int seed_index=std::stoi(argv[2]);
        const long long limit=std::stoll(argv[3]);
        const int max_seconds=std::stoi(argv[4]);
        if (seed_index<1 || seed_index>3 || limit<0 || max_seconds<1 || max_seconds>300)
            throw std::runtime_error("invalid arguments");
        require_unused(argv[5]);
        const auto seeds=load_seeds(argv[1]);
        if (seed_index>static_cast<int>(seeds.size())) throw std::runtime_error("seed index out of range");
        precompute_local();
        const Problem original=build_problem(seeds[seed_index-1],seed_index);
        Problem shifted=original;
        Outcome result;
        bool stop=false;
        int last_v=-1,last_z=-1,witness_v=-1,witness_z=-1;
        const auto start=std::chrono::steady_clock::now();
        for (std::size_t l=3; l<original.outside.size() && !stop; ++l) {
            const int v=original.outside[l];
            for (std::size_t k=2; k<l && !stop; ++k) {
                const int z=original.outside[k];
                for (int a=0; a<N; ++a) shifted.r0[a]=original.r0[a]+delta[z][a]+delta[v][a];
                for (std::size_t i=0; i+1<k && !stop; ++i)
                    for (std::size_t j=i+1; j<k; ++j) {
                        ++result.tested;
                        last_v=v; last_z=z;
                        if (evaluate(shifted,original.outside[i],original.outside[j],result)) {
                            result.stopped_for_witness=true; witness_z=z; witness_v=v; stop=true; break;
                        }
                        if (result.tested%1000000==0)
                            std::cout << "tested=" << result.tested << " valid_outer=" << result.valid_outer << std::endl;
                        if (limit && result.tested>=limit) { stop=true; break; }
                        if ((result.tested & 1023)==0 &&
                            std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>=max_seconds) {
                            result.timed_out=true; stop=true; break;
                        }
                    }
            }
        }
        const long long total=496LL*495*494*493/24;
        result.complete=result.tested==total;
        if (result.stopped_for_witness)
            write_four_witness(original,result,witness_z,witness_v,
                "frontier-20261028-core-outer-four-witness-seed"+std::to_string(seed_index)+".json",seed_index);
        const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
        std::ofstream out(argv[5]);
        if (!out) throw std::runtime_error("cannot create result");
        out << "{\n  \"seed_index_1based\":" << seed_index << ",\n  \"mode\":\"four-outside\",\n"
            << "  \"total_outer_subsets\":" << total << ",\n  \"tested\":" << result.tested
            << ",\n  \"complete\":" << (result.complete?"true":"false")
            << ",\n  \"timed_out\":" << (result.timed_out?"true":"false")
            << ",\n  \"stopped_for_witness\":" << (result.stopped_for_witness?"true":"false")
            << ",\n  \"valid_outer_subsets\":" << result.valid_outer
            << ",\n  \"valid_outer_local_pairs\":" << result.valid_local_pairs
            << ",\n  \"target_outer_subsets\":" << result.target_outer
            << ",\n  \"target_outer_local_pairs\":" << result.target_local_pairs
            << ",\n  \"last_outer_z\":" << last_z << ",\n  \"last_outer_v\":" << last_v
            << ",\n  \"elapsed_seconds\":" << elapsed << "\n}\n";
        if (!out) throw std::runtime_error("result write failed");
        std::cout << "seed=" << seed_index << " tested=" << result.tested << '/' << total
                  << " complete=" << result.complete << " timed_out=" << result.timed_out
                  << " valid_outer=" << result.valid_outer << " target_outer=" << result.target_outer
                  << " elapsed=" << elapsed << "s\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << '\n';
        return 1;
    }
}
