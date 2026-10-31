// Bounded reproducible five-outside-flip search using exact 16-cell local solver.
#define main frontier_two_outer_main
#include "frontier-20261028-core-outer-search.cpp"
#undef main

namespace {
std::uint64_t next_random(std::uint64_t& state) {
    std::uint64_t z=(state+=0x9e3779b97f4a7c15ULL);
    z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;
    z=(z^(z>>27))*0x94d049bb133111ebULL;
    return z^(z>>31);
}
void write_witness5(const Problem& p,const Outcome& r,const std::array<int,5>& changes,
                    const std::string& name,int seed) {
    require_unused(name);
    Table bits=p.bits;
    for (int x:changes) bits[x]^=1;
    for (int u=0;u<LOCAL;++u) bits[p.coords[u]]=(r.first_local>>u)&1;
    for (int x=0;x<N;++x) bits[x]^=__builtin_parity(x&r.first_frequency);
    int w[N];
    for (int x=0;x<N;++x) w[x]=1-2*bits[x];
    fwht(w,N);
    int peak=0;
    for (int value:w) peak=std::max(peak,std::abs(value));
    if (w[0]!=0||peak>28) throw std::runtime_error("internal witness check failed");
    std::ofstream out(name);
    if (!out) throw std::runtime_error("cannot write witness");
    out << "{\n  \"format\":\"boolean-truth-v1\",\n  \"seed_index_1based\":" << seed
        << ",\n  \"outside_flip_indices\":[" << changes[0] << ',' << changes[1] << ',' << changes[2] << ',' << changes[3] << ',' << changes[4]
        << "],\n  \"core_origin\":" << p.origin << ",\n  \"core_basis\":["
        << p.basis[0] << ',' << p.basis[1] << ',' << p.basis[2] << ',' << p.basis[3]
        << "],\n  \"local_pattern\":" << r.first_local << ",\n  \"affine_twist_frequency\":" << r.first_frequency
        << ",\n  \"bits\":\"";
    for (int bit:bits) out << bit;
    out << "\"\n}\n";
    if (!out) throw std::runtime_error("witness write failed");
}
}
int main(int argc,char** argv) {
    try {
        if (argc!=7) throw std::runtime_error("usage: random5 SEEDS INDEX RNG_SEED MAX_DRAWS MAX_SECONDS RESULT_JSON");
        const int index=std::stoi(argv[2]);
        const std::uint64_t seed=std::stoull(argv[3]);
        const long long max_draws=std::stoll(argv[4]);
        const int max_seconds=std::stoi(argv[5]);
        if (index<1||index>3||max_draws<1||max_seconds<1||max_seconds>300)
            throw std::runtime_error("invalid bounds");
        require_unused(argv[6]);
        const auto seeds=load_seeds(argv[1]);
        if (index>static_cast<int>(seeds.size())) throw std::runtime_error("seed index out of range");
        precompute_local();
        const Problem p=build_problem(seeds[index-1],index);
        Problem shifted=p;
        std::uint64_t state=seed;
        Outcome result;
        std::array<int,5> winner{};
        bool timed_out=false;
        const auto start=std::chrono::steady_clock::now();
        for (long long draw=0;draw<max_draws;++draw) {
            std::array<int,5> changes{};
            for (int i=0;i<5;++i) {
                int value;
                do { value=p.outside[next_random(state)%p.outside.size()]; }
                while (std::find(changes.begin(),changes.begin()+i,value)!=changes.begin()+i);
                changes[i]=value;
            }
            std::sort(changes.begin(),changes.end());
            for (int a=0;a<N;++a)
                shifted.r0[a]=p.r0[a]+delta[changes[2]][a]+delta[changes[3]][a]+delta[changes[4]][a];
            ++result.tested;
            if (evaluate(shifted,changes[0],changes[1],result)) {
                result.stopped_for_witness=true; winner=changes; break;
            }
            if (result.tested%1000000==0)
                std::cout << "draws=" << result.tested << " valid_outer=" << result.valid_outer << std::endl;
            if ((result.tested&1023)==0 &&
                std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>=max_seconds) {
                timed_out=true; break;
            }
        }
        if (result.stopped_for_witness)
            write_witness5(p,result,winner,"frontier-20261028-random5-witness-seed"+std::to_string(index)+".json",index);
        const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
        std::ofstream out(argv[6]);
        if (!out) throw std::runtime_error("cannot create result");
        out << "{\n  \"seed_index_1based\":" << index << ",\n  \"rng\":\"splitmix64\",\n  \"rng_seed\":" << seed
            << ",\n  \"max_draws\":" << max_draws << ",\n  \"tested\":" << result.tested
            << ",\n  \"timed_out\":" << (timed_out?"true":"false")
            << ",\n  \"stopped_for_witness\":" << (result.stopped_for_witness?"true":"false")
            << ",\n  \"valid_outer_draws\":" << result.valid_outer
            << ",\n  \"valid_outer_local_pairs\":" << result.valid_local_pairs
            << ",\n  \"target_outer_draws\":" << result.target_outer
            << ",\n  \"target_outer_local_pairs\":" << result.target_local_pairs
            << ",\n  \"elapsed_seconds\":" << elapsed << "\n}\n";
        if (!out) throw std::runtime_error("result write failed");
        std::cout << "seed=" << index << " draws=" << result.tested << " timed_out=" << timed_out
                  << " valid_outer=" << result.valid_outer << " target_outer=" << result.target_outer
                  << " elapsed=" << elapsed << "s\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << '\n';
        return 1;
    }
}
