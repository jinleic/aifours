// Independent all-four-anchor completion checker for an actual 11-row source.
// DFS generates every eligible permutation; an exact-cover search uses a
// separately built feature-conflict bit matrix and missing D1 pivots.
// No fixed-row obstruction is an unrestricted Tuscan-2 no-go.
// Build: clang++ -std=c++17 -O3 -Wall -Wextra THIS_SOURCE -o BINARY
// Run: BINARY ROWS.txt OUTPUT.json SECONDS. Independently check any witness.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <fcntl.h>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unistd.h>
#include <vector>

namespace {
constexpr int N=11,E=N*N,F=2*E+2*N, KEEP=4, NEED=N-KEEP;
using Row=std::array<int,N>;
using Rows=std::array<Row,N>;
struct Bits { std::uint64_t lo=0,hi=0; };
void set(Bits& b,int e) { if (e<64) b.lo|=std::uint64_t{1}<<e; else b.hi|=std::uint64_t{1}<<(e-64); }
bool get(const Bits& b,int e) { return e<64 ? b.lo & (std::uint64_t{1}<<e) : b.hi & (std::uint64_t{1}<<(e-64)); }

struct Candidate { Row row{}; Bits adjacency{}; std::array<int,21> feature{}; };
struct CaseRecord { std::array<int,4> kept{}; std::size_t eligible=0; std::uint64_t nodes=0; bool exhausted=false; };
struct Search {
    Rows source{},witness{};
    std::array<int,4> fixed{};
    Bits fixed1{},fixed2{},required{};
    unsigned starts=0,ends=0;
    Row path{};
    std::vector<Candidate> candidates;
    std::vector<std::uint64_t> feature_bits,conflict;
    std::array<std::vector<std::uint64_t>,NEED+1> allowed{};
    std::array<int,NEED> choice{};
    std::size_t words=0;
    std::uint64_t generated_nodes=0,cover_nodes=0,total_generated=0,total_cover=0;
    bool timed_out=false,found=false;
    std::chrono::steady_clock::time_point deadline;
    std::vector<CaseRecord> records;

    Search(const Rows& rows,double seconds):source(rows) {
        deadline=std::chrono::steady_clock::now()+
            std::chrono::duration_cast<std::chrono::steady_clock::duration>(std::chrono::duration<double>(seconds));
    }
    bool expired(std::uint64_t value) {
        if ((value&4095U)==0 && std::chrono::steady_clock::now()>=deadline) timed_out=true;
        return timed_out;
    }
    bool prepare(int a,int b,int c,int d) {
        fixed={a,b,c,d}; fixed1={}; fixed2={}; starts=ends=0;
        for (int index:fixed) {
            const Row& row=source[index];
            if ((starts & (1U<<row[0])) || (ends & (1U<<row[N-1]))) return false;
            starts|=1U<<row[0]; ends|=1U<<row[N-1];
            for (int j=0;j<N-1;++j) {
                int e=row[j]*N+row[j+1]; if (get(fixed1,e)) return false; set(fixed1,e);
            }
            for (int j=0;j<N-2;++j) {
                int e=row[j]*N+row[j+2]; if (get(fixed2,e)) return false; set(fixed2,e);
            }
        }
        Bits all{};
        for (int x=0;x<N;++x) for (int y=0;y<N;++y) if (x!=y) set(all,x*N+y);
        required={all.lo & ~fixed1.lo,all.hi & ~fixed1.hi};
        if (__builtin_popcountll(required.lo)+__builtin_popcountll(required.hi)!=NEED*(N-1))
            throw std::logic_error("incorrect missing D1 count");
        return true;
    }
    void generate(int depth,unsigned used) {
        if (timed_out || expired(++generated_nodes)) return;
        if (depth==N) {
            Candidate c; c.row=path;
            int n=0;
            for (int i=0;i<N-1;++i) { int e=path[i]*N+path[i+1]; set(c.adjacency,e); c.feature[n++]=e; }
            for (int i=0;i<N-2;++i) c.feature[n++]=E+path[i]*N+path[i+2];
            c.feature[n++]=2*E+path[0];
            c.feature[n++]=2*E+N+path[N-1];
            if (n!=21) throw std::logic_error("bad candidate feature count");
            candidates.push_back(c); return;
        }
        for (int symbol=0;symbol<N;++symbol) {
            if ((used & (1U<<symbol)) || (depth==0 && (starts & (1U<<symbol))) ||
                (depth==N-1 && (ends & (1U<<symbol)))) continue;
            if (depth>0 && get(fixed1,path[depth-1]*N+symbol)) continue;
            if (depth>1 && get(fixed2,path[depth-2]*N+symbol)) continue;
            path[depth]=symbol;
            generate(depth+1,used|(1U<<symbol));
            if (timed_out) return;
        }
    }
    void build_bitsets() {
        words=(candidates.size()+63)/64;
        feature_bits.assign(F*words,0);
        for (std::size_t i=0;i<candidates.size();++i)
            for (int f:candidates[i].feature) feature_bits[static_cast<std::size_t>(f)*words+i/64]|=std::uint64_t{1}<<(i%64);
        conflict.assign(candidates.size()*words,0);
        for (std::size_t i=0;i<candidates.size();++i) {
            if (expired(i)) return;
            for (int f:candidates[i].feature)
                for (std::size_t w=0;w<words;++w)
                    conflict[i*words+w]|=feature_bits[static_cast<std::size_t>(f)*words+w];
        }
        for (auto& v:allowed) v.assign(words,0);
        for (std::size_t w=0;w<words;++w) allowed[0][w]=~std::uint64_t{0};
        if (words && candidates.size()%64) allowed[0][words-1]=(std::uint64_t{1}<<(candidates.size()%64))-1;
    }
    bool cover(Bits outstanding,int depth) {
        if (timed_out || expired(++cover_nodes)) return false;
        if (!outstanding.lo && !outstanding.hi) {
            if (depth!=NEED) throw std::logic_error("wrong cover cardinality");
            for (int i=0;i<KEEP;++i) witness[i]=source[fixed[i]];
            for (int i=0;i<NEED;++i) witness[KEEP+i]=candidates[choice[i]].row;
            found=true; return true;
        }
        if (depth>=NEED) return false;
        int pivot=-1;
        std::size_t best=candidates.size()+1;
        for (int e=0;e<E;++e) if (get(outstanding,e)) {
            std::size_t count=0;
            for (std::size_t w=0;w<words;++w)
                count+=__builtin_popcountll(feature_bits[static_cast<std::size_t>(e)*words+w] & allowed[depth][w]);
            if (!count) return false;
            if (count<best) { pivot=e; best=count; if (best==1) break; }
        }
        if (pivot<0) throw std::logic_error("missing pivot");
        for (std::size_t w=0;w<words;++w) {
            std::uint64_t options=feature_bits[static_cast<std::size_t>(pivot)*words+w] & allowed[depth][w];
            while (options) {
                std::uint64_t bit=options & -options; options^=bit;
                std::size_t index=64*w+static_cast<std::size_t>(__builtin_ctzll(bit));
                const Candidate& c=candidates[index];
                if ((c.adjacency.lo & outstanding.lo)!=c.adjacency.lo ||
                    (c.adjacency.hi & outstanding.hi)!=c.adjacency.hi)
                    throw std::logic_error("compatible row shares prior D1");
                for (std::size_t z=0;z<words;++z)
                    allowed[depth+1][z]=allowed[depth][z] & ~conflict[index*words+z];
                choice[depth]=static_cast<int>(index);
                Bits next{outstanding.lo^c.adjacency.lo,outstanding.hi^c.adjacency.hi};
                if (cover(next,depth+1)) return true;
                if (timed_out) return false;
            }
        }
        return false;
    }
    void one_case() {
        candidates.clear(); generated_nodes=cover_nodes=0;
        generate(0,0);
        total_generated+=generated_nodes;
        if (timed_out) return;
        build_bitsets();
        if (timed_out) return;
        cover(required,0);
        total_cover+=cover_nodes;
        if (!timed_out && !found)
            records.push_back({fixed,candidates.size(),cover_nodes,true});
    }
};

int collisions(const Rows& rows,int distance,int* excess=nullptr) {
    int f[E]{}; int ans=0;
    for (const auto& row:rows) for (int i=0;i<N-distance;++i) ans+=f[row[i]*N+row[i+distance]]++;
    if (excess) { int v=0; for (int z:f) if (z>1) v+=z-1; *excess=v; }
    return ans;
}
void print_rows(std::FILE* out,const Rows& rows) {
    std::fprintf(out,"[\n");
    for (int i=0;i<N;++i) {
        std::fprintf(out,"    [");
        for (int j=0;j<N;++j) std::fprintf(out,"%s%d",j?", ":"",rows[i][j]);
        std::fprintf(out,"]%s\n",i+1==N?"":",");
    }
    std::fprintf(out,"  ]");
}
}

int main(int argc,char** argv) {
    try {
        if (argc!=4) throw std::runtime_error("usage: BINARY ROWS.txt OUTPUT.json SECONDS");
        const std::string input=argv[1],output=argv[2];
        const double seconds=std::stod(argv[3]);
        if (seconds<=0) throw std::runtime_error("bad budget");
        std::ifstream in(input); if (!in) throw std::runtime_error("cannot read input");
        Rows rows{};
        for (Row& row:rows) {
            unsigned used=0;
            for (int& v:row) {
                if (!(in>>v) || v<0 || v>=N || (used & (1U<<v))) throw std::runtime_error("invalid row");
                used|=1U<<v;
            }
        }
        int x=0; if (in>>x) throw std::runtime_error("extra data");
        const auto started=std::chrono::steady_clock::now();
        Search search(rows,seconds);
        int subsets=0,compatible=0;
        for (int a=0;a<N-3 && !search.timed_out && !search.found;++a)
            for (int b=a+1;b<N-2 && !search.timed_out && !search.found;++b)
                for (int c=b+1;c<N-1 && !search.timed_out && !search.found;++c)
                    for (int d=c+1;d<N && !search.timed_out && !search.found;++d) {
                        if (std::chrono::steady_clock::now()>=search.deadline) { search.timed_out=true; break; }
                        ++subsets;
                        if (search.prepare(a,b,c,d)) { ++compatible; search.one_case(); }
                    }
        if (search.found && (collisions(search.witness,1)!=0 || collisions(search.witness,2)!=0))
            throw std::logic_error("internal witness reconstruction invalid");
        const bool complete=!search.timed_out && !search.found && subsets==330 &&
                            static_cast<int>(search.records.size())==compatible;
        const auto ms=std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now()-started).count();
        const int fd=open(output.c_str(),O_WRONLY|O_CREAT|O_EXCL,0600);
        if (fd<0) throw std::runtime_error("cannot exclusively create result");
        std::FILE* out=fdopen(fd,"w");
        if (!out) { close(fd); throw std::runtime_error("cannot create output stream"); }
        std::fprintf(out,"{\n  \"kind\": \"independent_four_anchor_exact_cover\",\n  \"input_rows_file\": \"%s\",\n",input.c_str());
        std::fprintf(out,"  \"complete\": %s,\n  \"budget_exhausted\": %s,\n  \"candidate_witness\": %s,\n",complete?"true":"false",search.timed_out?"true":"false",search.found?"true":"false");
        std::fprintf(out,"  \"subsets_examined\": %d,\n  \"compatible_subsets_examined\": %d,\n  \"cases_completed\": %zu,\n",subsets,compatible,search.records.size());
        std::fprintf(out,"  \"generation_nodes\": %llu,\n  \"cover_nodes\": %llu,\n  \"elapsed_ms\": %lld,\n  \"cases\": [\n",static_cast<unsigned long long>(search.total_generated),static_cast<unsigned long long>(search.total_cover),static_cast<long long>(ms));
        for (std::size_t i=0;i<search.records.size();++i) {
            const auto& c=search.records[i];
            std::fprintf(out,"    {\"fixed_rows_1based\":[%d,%d,%d,%d],\"eligible_rows\":%zu,\"cover_nodes\":%llu}%s\n",c.kept[0]+1,c.kept[1]+1,c.kept[2]+1,c.kept[3]+1,c.eligible,static_cast<unsigned long long>(c.nodes),i+1==search.records.size()?"":",");
        }
        std::fprintf(out,"  ]");
        if (search.found) {
            std::fprintf(out,",\n  \"zero_score_claim\": true,\n  \"best_pair_collision_score\": 0,\n  \"d1_pair_collisions\": 0,\n  \"d2_pair_collisions\": 0,\n  \"d1_excess_events\": 0,\n  \"d2_excess_events\": 0,\n  \"rows\": ");
            print_rows(out,search.witness);
        }
        std::fprintf(out,",\n  \"scope\": \"Only exact retained row strings from the pinned source; no unrestricted no-go.\"\n}\n");
        if (std::fclose(out)!=0) throw std::runtime_error("result write failed");
        std::cout<<"complete="<<complete<<" budget="<<search.timed_out<<" witness="<<search.found
                 <<" subsets="<<subsets<<" compatible="<<compatible<<" cases="<<search.records.size()
                 <<" generation_nodes="<<search.total_generated<<" cover_nodes="<<search.total_cover<<" elapsed_ms="<<ms<<'\n';
        return 0;
    } catch (const std::exception& ex) {
        std::cerr<<"error: "<<ex.what()<<'\n';
        return 1;
    }
}
