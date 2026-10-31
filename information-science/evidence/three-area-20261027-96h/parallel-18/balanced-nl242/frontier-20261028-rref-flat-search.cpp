// Exact per-flat local solver over a resumable RREF enumeration of affine 4-flats.
#define main frontier_two_outer_main
#include "frontier-20261028-core-outer-search.cpp"
#undef main

namespace {
long long gaussian(int n,int k) {
    long long d[10][10]{};
    d[0][0]=1;
    for (int i=1;i<=n;++i) {
        d[i][0]=1;
        for (int j=1;j<=i && j<=k;++j)
            d[i][j]=d[i-1][j-1]+(1LL<<j)*d[i-1][j];
    }
    return d[n][k];
}
Problem make_problem(const Table& bits,const Table& global,int origin,const std::array<int,4>& basis) {
    Problem p;
    p.bits=bits; p.origin=origin; p.basis=basis;
    int local[LOCAL];
    for (int u=0;u<LOCAL;++u) {
        int x=origin;
        for (int i=0;i<4;++i) if (u&(1<<i)) x^=basis[i];
        p.coords[u]=x;
        local[u]=1-2*bits[x];
    }
    fwht(local,LOCAL);
    for (int a=0;a<N;++a) {
        int alpha=0;
        for (int i=0;i<4;++i) if (__builtin_parity(a&basis[i])) alpha|=1<<i;
        p.alpha[a]=alpha;
        p.r0[a]=(__builtin_parity(a&origin)?-1:1)*global[a]-local[alpha];
    }
    return p;
}
void write_witness(const Problem& p,const Outcome& r,const std::string& name,int seed,long long index) {
    require_unused(name);
    Table bits=p.bits;
    for (int u=0;u<LOCAL;++u) bits[p.coords[u]]=(r.first_local>>u)&1;
    for (int x=0;x<N;++x) bits[x]^=__builtin_parity(x&r.first_frequency);
    int w[N];
    for (int x=0;x<N;++x) w[x]=1-2*bits[x];
    fwht(w,N);
    int peak=0;
    for (int v:w) peak=std::max(peak,std::abs(v));
    if (w[0]!=0||peak>28) throw std::runtime_error("internal witness check failed");
    std::ofstream out(name);
    if (!out) throw std::runtime_error("cannot write witness");
    out << "{\n  \"format\":\"boolean-truth-v1\",\n  \"seed_index_1based\":" << seed
        << ",\n  \"flat_index_zero_based\":" << index << ",\n  \"core_origin\":" << p.origin
        << ",\n  \"core_basis\":[" << p.basis[0] << ',' << p.basis[1] << ',' << p.basis[2] << ',' << p.basis[3]
        << "],\n  \"local_pattern\":" << r.first_local << ",\n  \"affine_twist_frequency\":" << r.first_frequency
        << ",\n  \"bits\":\"";
    for (int bit:bits) out << bit;
    out << "\"\n}\n";
    if (!out) throw std::runtime_error("witness write failed");
}
}
int main(int argc,char** argv) {
    try {
        if (argc!=7) throw std::runtime_error("usage: rref-flat SEEDS INDEX START MAX_FLATS MAX_SECONDS RESULT_JSON");
        const int index=std::stoi(argv[2]);
        const long long start_index=std::stoll(argv[3]), max_flats=std::stoll(argv[4]);
        const int max_seconds=std::stoi(argv[5]);
        if (index<1||index>3||start_index<0||max_flats<1||max_seconds<1||max_seconds>300)
            throw std::runtime_error("invalid bounds");
        require_unused(argv[6]);
        const auto seeds=load_seeds(argv[1]);
        if (index>static_cast<int>(seeds.size())) throw std::runtime_error("seed index out of range");
        const long long total=gaussian(9,4)*32;
        if (start_index>=total) throw std::runtime_error("start beyond final flat");
        precompute_local();
        Table global{};
        for (int x=0;x<N;++x) global[x]=1-2*seeds[index-1][x];
        fwht(global.data(),N);
        for (int a=0;a<N;++a) delta[0][a]=0;
        Outcome result;
        Problem winner;
        long long enumeration=0,last_index=-1,winner_index=-1;
        bool stop=false,timed_out=false;
        const auto started=std::chrono::steady_clock::now();
        for (int p0=0;p0<6 && !stop;++p0)
          for (int p1=p0+1;p1<7 && !stop;++p1)
            for (int p2=p1+1;p2<8 && !stop;++p2)
              for (int p3=p2+1;p3<9 && !stop;++p3) {
                const std::array<int,4> pivots{p0,p1,p2,p3};
                std::array<bool,9> is_pivot{};
                for (int x:pivots) is_pivot[x]=true;
                std::array<std::pair<int,int>,20> free_slots{};
                std::array<int,5> free_columns{};
                int slots=0,columns=0;
                for (int col=0;col<9;++col) if (!is_pivot[col]) {
                    free_columns[columns++]=col;
                    for (int row=0;row<4;++row) if (col>pivots[row]) free_slots[slots++]={row,col};
                }
                if (columns!=5||slots>20) throw std::runtime_error("RREF dimension mismatch");
                for (int assignment=0; assignment<(1<<slots) && !stop; ++assignment) {
                    if (enumeration+32<=start_index) { enumeration+=32; continue; }
                    std::array<int,4> basis{};
                    for (int i=0;i<4;++i) basis[i]=1<<pivots[i];
                    for (int b=0;b<slots;++b) if (assignment&(1<<b))
                        basis[free_slots[b].first] |= 1<<free_slots[b].second;
                    for (int coset=0;coset<32;++coset) {
                        const long long current=enumeration++;
                        if (current<start_index) continue;
                        int origin=0;
                        for (int j=0;j<5;++j) if (coset&(1<<j)) origin|=1<<free_columns[j];
                        Problem p=make_problem(seeds[index-1],global,origin,basis);
                        const long long before=result.valid_outer;
                        ++result.tested; last_index=current;
                        if (evaluate(p,0,-1,result)) {
                            result.stopped_for_witness=true; winner=std::move(p); winner_index=current; stop=true; break;
                        }
                        if (result.valid_outer!=before+1) throw std::runtime_error("original local restriction not feasible");
                        if (result.tested%1000000==0)
                            std::cout << "start=" << start_index << " tested=" << result.tested
                                      << " valid_local_pairs=" << result.valid_local_pairs << std::endl;
                        if (result.tested>=max_flats) { stop=true; break; }
                        if ((result.tested&255)==0 &&
                            std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count()>=max_seconds) {
                            timed_out=true; stop=true; break;
                        }
                    }
                }
              }
        const bool complete=start_index+result.tested==total;
        if (result.stopped_for_witness)
            write_witness(winner,result,"frontier-20261028-rref-flat-witness-seed"+std::to_string(index)+".json",index,winner_index);
        const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count();
        std::ofstream out(argv[6]);
        if (!out) throw std::runtime_error("cannot write result");
        out << "{\n  \"seed_index_1based\":" << index << ",\n  \"enumeration\":\"RREF basis, pivot-zero coset representative\",\n"
            << "  \"total_flats\":" << total << ",\n  \"start_index\":" << start_index
            << ",\n  \"tested\":" << result.tested << ",\n  \"last_index\":" << last_index
            << ",\n  \"next_index\":" << start_index+result.tested
            << ",\n  \"complete_through_end\":" << (complete?"true":"false")
            << ",\n  \"timed_out\":" << (timed_out?"true":"false")
            << ",\n  \"stopped_for_witness\":" << (result.stopped_for_witness?"true":"false")
            << ",\n  \"valid_flat_draws\":" << result.valid_outer
            << ",\n  \"valid_flat_local_pairs\":" << result.valid_local_pairs
            << ",\n  \"target_flat_draws\":" << result.target_outer
            << ",\n  \"target_flat_local_pairs\":" << result.target_local_pairs
            << ",\n  \"elapsed_seconds\":" << elapsed << "\n}\n";
        if (!out) throw std::runtime_error("result write failed");
        std::cout << "seed=" << index << " start=" << start_index << " tested=" << result.tested << '/' << total
                  << " complete_through_end=" << complete << " valid_local_pairs=" << result.valid_local_pairs
                  << " targets=" << result.target_outer << " elapsed=" << elapsed << "s\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << '\n';
        return 1;
    }
}
