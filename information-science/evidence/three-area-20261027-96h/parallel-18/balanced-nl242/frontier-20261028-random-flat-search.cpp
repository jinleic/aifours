// Bounded reproducible sampling of affine 4-flats; exact local Boolean search on each.
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
Problem random_problem(const Table& bits, const Table& global, std::uint64_t& state) {
    Problem p;
    p.bits=bits;
    p.origin=static_cast<int>(next_random(state)%N);
    std::array<int,LOCAL> span{};
    std::array<bool,N> used{};
    used[0]=true;
    int size=1;
    for (int i=0;i<4;++i) {
        int b;
        do { b=static_cast<int>(next_random(state)%N); } while (used[b]);
        p.basis[i]=b;
        for (int j=0;j<size;++j) { span[size+j]=span[j]^b; used[span[size+j]]=true; }
        size*=2;
    }
    int local[LOCAL];
    for (int u=0;u<LOCAL;++u) {
        int x=p.origin;
        for (int i=0;i<4;++i) if (u&(1<<i)) x^=p.basis[i];
        p.coords[u]=x;
        local[u]=1-2*bits[x];
    }
    fwht(local,LOCAL);
    for (int a=0;a<N;++a) {
        int alpha=0;
        for (int i=0;i<4;++i) if (__builtin_parity(a&p.basis[i])) alpha|=1<<i;
        const int orientation=__builtin_parity(a&p.origin)?-1:1;
        p.alpha[a]=alpha;
        p.r0[a]=orientation*global[a]-local[alpha];
    }
    return p;
}
void write_flat_witness(const Problem& p,const Outcome& r,const std::string& name,int seed) {
    require_unused(name);
    Table bits=p.bits;
    for (int u=0;u<LOCAL;++u) bits[p.coords[u]]=(r.first_local>>u)&1;
    for (int x=0;x<N;++x) bits[x]^=__builtin_parity(x&r.first_frequency);
    int w[N];
    for (int x=0;x<N;++x) w[x]=1-2*bits[x];
    fwht(w,N);
    int peak=0;
    for (int v:w) peak=std::max(peak,std::abs(v));
    if (w[0]!=0 || peak>28) throw std::runtime_error("internal witness check failed");
    std::ofstream out(name);
    if (!out) throw std::runtime_error("cannot create witness");
    out << "{\n  \"format\":\"boolean-truth-v1\",\n  \"seed_index_1based\":" << seed
        << ",\n  \"core_origin\":" << p.origin << ",\n  \"core_basis\":["
        << p.basis[0] << ',' << p.basis[1] << ',' << p.basis[2] << ',' << p.basis[3]
        << "],\n  \"local_pattern\":" << r.first_local
        << ",\n  \"affine_twist_frequency\":" << r.first_frequency << ",\n  \"bits\":\"";
    for (int bit:bits) out << bit;
    out << "\"\n}\n";
    if (!out) throw std::runtime_error("witness output failed");
}
}
int main(int argc,char** argv) {
    try {
        if (argc!=7) throw std::runtime_error("usage: random-flat SEEDS INDEX RNG_SEED MAX_FLATS MAX_SECONDS RESULT_JSON");
        const int index=std::stoi(argv[2]);
        const std::uint64_t random_seed=std::stoull(argv[3]);
        const long long max_flats=std::stoll(argv[4]);
        const int max_seconds=std::stoi(argv[5]);
        if (index<1 || index>3 || max_flats<1 || max_seconds<1 || max_seconds>300)
            throw std::runtime_error("invalid bounds");
        require_unused(argv[6]);
        const auto seeds=load_seeds(argv[1]);
        if (index>static_cast<int>(seeds.size())) throw std::runtime_error("seed index out of range");
        precompute_local();
        Table global{};
        for (int x=0;x<N;++x) global[x]=1-2*seeds[index-1][x];
        fwht(global.data(),N);
        for (int a=0;a<N;++a) delta[0][a]=0;
        std::uint64_t state=random_seed;
        const auto start=std::chrono::steady_clock::now();
        Outcome result;
        bool timed_out=false;
        Problem winner;
        for (long long draw=0;draw<max_flats;++draw) {
            Problem p=random_problem(seeds[index-1],global,state);
            const long long before=result.valid_outer;
            ++result.tested;
            if (evaluate(p,0,-1,result)) {
                result.stopped_for_witness=true;
                winner=std::move(p);
                break;
            }
            if (result.valid_outer!=before+1) throw std::runtime_error("original restriction not feasible");
            if (result.tested%10000==0)
                std::cout << "flats=" << result.tested << " valid_local_pairs=" << result.valid_local_pairs << std::endl;
            if ((result.tested&255)==0 &&
                std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>=max_seconds) {
                timed_out=true; break;
            }
        }
        if (result.stopped_for_witness)
            write_flat_witness(winner,result,"frontier-20261028-random-flat-witness-seed"+std::to_string(index)+".json",index);
        const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
        std::ofstream out(argv[6]);
        if (!out) throw std::runtime_error("cannot create result");
        out << "{\n  \"seed_index_1based\":" << index << ",\n  \"rng\":\"splitmix64\",\n  \"rng_seed\":" << random_seed
            << ",\n  \"max_flats\":" << max_flats << ",\n  \"flats_tested\":" << result.tested
            << ",\n  \"timed_out\":" << (timed_out?"true":"false")
            << ",\n  \"stopped_for_witness\":" << (result.stopped_for_witness?"true":"false")
            << ",\n  \"valid_flat_draws\":" << result.valid_outer
            << ",\n  \"valid_flat_local_pairs\":" << result.valid_local_pairs
            << ",\n  \"target_flat_draws\":" << result.target_outer
            << ",\n  \"target_flat_local_pairs\":" << result.target_local_pairs
            << ",\n  \"elapsed_seconds\":" << elapsed << "\n}\n";
        if (!out) throw std::runtime_error("result write failed");
        std::cout << "seed=" << index << " flats=" << result.tested << " timed_out=" << timed_out
                  << " valid_flat_draws=" << result.valid_outer << " valid_local_pairs=" << result.valid_local_pairs
                  << " target_flat_draws=" << result.target_outer << " elapsed=" << elapsed << "s\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << '\n';
        return 1;
    }
}
