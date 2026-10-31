// Bounded exact T2 completion search for THREE explicitly retained rows.
// Generate all compatible rows by DFS, then exact-cover missing directed D1
// arcs and missing endpoints; prune if over eleven D2 arcs are unsupported.
// All conflicts are on-demand bitsets. A cutoff is UNKNOWN, never a no-go.
// Build: clang++ -std=c++17 -O3 -Wall -Wextra SOURCE -o BINARY
// Run: BINARY INPUT.txt OUTPUT.json ROW1 ROW2 ROW3 SEED SECONDS
// Any reported witness must be checked independently from actual rows.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <fcntl.h>
#include <fstream>
#include <iostream>
#include <random>
#include <stdexcept>
#include <string>
#include <unistd.h>
#include <vector>

namespace {
constexpr int N=11,E=N*N,F=2*E+2*N,KEEP=3,NEED=N-KEEP;
constexpr std::size_t ROW_CAP=300000;
using Row=std::array<int,N>;
using Rows=std::array<Row,N>;
struct Bits { std::uint64_t lo=0,hi=0; };
void set(Bits& b,int e) { if (e<64) b.lo|=std::uint64_t{1}<<e; else b.hi|=std::uint64_t{1}<<(e-64); }
bool get(const Bits& b,int e) { return e<64 ? b.lo & (std::uint64_t{1}<<e) : b.hi & (std::uint64_t{1}<<(e-64)); }
struct Candidate { Row row{}; Bits adj{},far{}; std::array<int,21> features{}; };

struct Solver {
    Rows source{},witness{};
    std::array<int,KEEP> fixed{};
    Bits fixed1{},fixed2{},required{};
    unsigned starts=0,ends=0;
    Row path{};
    std::vector<Candidate> candidates;
    std::vector<std::uint64_t> feature_bits;
    std::array<std::vector<std::uint64_t>,NEED+1> allowed{};
    std::array<int,NEED> choice{};
    std::size_t words=0;
    std::uint64_t generated_nodes=0,cover_nodes=0,d2_support_prunes=0,endpoint_hall_prunes=0,dual_hall_prunes=0;
    bool timed_out=false,row_cap=false,found=false,invalid_fixed=false,generated_complete=false;
    bool first_support_prune_saved=false;
    int first_support_prune_depth=0;
    std::array<Row,NEED> first_support_prune_rows{};
    std::chrono::steady_clock::time_point deadline;
    std::mt19937_64 random;

    Solver(const Rows& rows,std::array<int,KEEP> selected,std::uint64_t seed,double seconds)
        :source(rows),fixed(selected),random(seed) {
        deadline=std::chrono::steady_clock::now()+
            std::chrono::duration_cast<std::chrono::steady_clock::duration>(std::chrono::duration<double>(seconds));
    }
    bool expired(std::uint64_t number,std::uint64_t mask) {
        if ((number&mask)==0 && std::chrono::steady_clock::now()>=deadline) timed_out=true;
        return timed_out;
    }
    bool prepare() {
        for (int index:fixed) {
            const Row& row=source[index];
            if ((starts & (1U<<row[0])) || (ends & (1U<<row[N-1]))) return false;
            starts|=1U<<row[0]; ends|=1U<<row[N-1];
            for (int i=0;i<N-1;++i) {
                const int e=row[i]*N+row[i+1]; if (get(fixed1,e)) return false; set(fixed1,e);
            }
            for (int i=0;i<N-2;++i) {
                const int e=row[i]*N+row[i+2]; if (get(fixed2,e)) return false; set(fixed2,e);
            }
        }
        Bits all{};
        for (int a=0;a<N;++a) for (int b=0;b<N;++b) if (a!=b) set(all,a*N+b);
        required={all.lo & ~fixed1.lo,all.hi & ~fixed1.hi};
        if (__builtin_popcountll(required.lo)+__builtin_popcountll(required.hi)!=NEED*(N-1))
            throw std::logic_error("missing adjacency count mismatch");
        return true;
    }
    void generate(int depth,unsigned used) {
        if (timed_out || row_cap || expired(++generated_nodes,4095)) return;
        if (depth==N) {
            if (candidates.size()>=ROW_CAP) { row_cap=true; return; }
            Candidate c; c.row=path; int n=0;
            for (int i=0;i<N-1;++i) { int e=path[i]*N+path[i+1]; set(c.adj,e); c.features[n++]=e; }
            for (int i=0;i<N-2;++i) {
                int e=path[i]*N+path[i+2]; set(c.far,e); c.features[n++]=E+e;
            }
            c.features[n++]=2*E+path[0]; c.features[n++]=2*E+N+path[N-1];
            if (n!=21) throw std::logic_error("candidate feature mismatch");
            candidates.push_back(c); return;
        }
        for (int v=0;v<N;++v) {
            if ((used & (1U<<v)) || (depth==0 && (starts & (1U<<v))) ||
                (depth==N-1 && (ends & (1U<<v)))) continue;
            if (depth>0 && get(fixed1,path[depth-1]*N+v)) continue;
            if (depth>1 && get(fixed2,path[depth-2]*N+v)) continue;
            path[depth]=v;
            generate(depth+1,used|(1U<<v));
            if (timed_out || row_cap) return;
        }
    }
    void build_features() {
        std::shuffle(candidates.begin(),candidates.end(),random);
        words=(candidates.size()+63)/64;
        feature_bits.assign(static_cast<std::size_t>(F)*words,0);
        for (std::size_t i=0;i<candidates.size();++i) {
            if (expired(i,4095)) return;
            for (int f:candidates[i].features)
                feature_bits[static_cast<std::size_t>(f)*words+i/64]|=std::uint64_t{1}<<(i%64);
        }
        for (auto& level:allowed) level.assign(words,0);
        for (std::size_t w=0;w<words;++w) allowed[0][w]=~std::uint64_t{0};
        if (words && candidates.size()%64)
            allowed[0][words-1]=(std::uint64_t{1}<<(candidates.size()%64))-1;
    }
    bool endpoint_matching_possible(unsigned need_starts,unsigned need_ends,int depth) {
        std::array<unsigned,N> graph{};
        for (int s=0;s<N;++s) if (need_starts & (1U<<s)) {
            const std::size_t start_offset=static_cast<std::size_t>(2*E+s)*words;
            for (int t=0;t<N;++t) if (need_ends & (1U<<t)) {
                const std::size_t end_offset=static_cast<std::size_t>(2*E+N+t)*words;
                for (std::size_t w=0;w<words;++w)
                    if (feature_bits[start_offset+w] & feature_bits[end_offset+w] & allowed[depth][w]) {
                        graph[s]|=1U<<t; break;
                    }
            }
        }
        std::array<int,N> matched{}; matched.fill(-1);
        auto augment=[&](auto&& self,int s,unsigned& seen)->bool {
            unsigned options=graph[s] & ~seen;
            while (options) {
                const unsigned bit=options & -options; options^=bit;
                if (seen & bit) continue;
                seen|=bit;
                const int t=__builtin_ctz(bit);
                if (matched[t]<0 || self(self,matched[t],seen)) { matched[t]=s; return true; }
            }
            return false;
        };
        for (int s=0;s<N;++s) if (need_starts & (1U<<s)) {
            unsigned seen=0;
            if (!augment(augment,s,seen)) return false;
        }
        return true;
    }
    bool outgoing_matching_possible(Bits outstanding,unsigned need_starts,int depth) {
        for (int a=0;a<N;++a) {
            int degree=0;
            for (int b=0;b<N;++b) if (get(outstanding,a*N+b)) ++degree;
            if (degree<3) continue;
            std::array<unsigned,N> graph{};
            for (int b=0;b<N;++b) if (get(outstanding,a*N+b)) {
                const std::size_t edge_offset=static_cast<std::size_t>(a*N+b)*words;
                for (int s=0;s<N;++s) if (need_starts & (1U<<s)) {
                    const std::size_t start_offset=static_cast<std::size_t>(2*E+s)*words;
                    for (std::size_t w=0;w<words;++w)
                        if (feature_bits[edge_offset+w] & feature_bits[start_offset+w] & allowed[depth][w]) {
                            graph[b]|=1U<<s; break;
                        }
                }
            }
            std::array<int,N> matched{}; matched.fill(-1);
            auto augment=[&](auto&& self,int b,unsigned& seen)->bool {
                unsigned options=graph[b] & ~seen;
                while (options) {
                    const unsigned bit=options & -options; options^=bit;
                    if (seen & bit) continue;
                    seen|=bit;
                    const int s=__builtin_ctz(bit);
                    if (matched[s]<0 || self(self,matched[s],seen)) { matched[s]=b; return true; }
                }
                return false;
            };
            for (int b=0;b<N;++b) if (get(outstanding,a*N+b)) {
                unsigned seen=0;
                if (!augment(augment,b,seen)) return false;
            }
        }
        return true;
    }
    bool cover(Bits outstanding,Bits used2,unsigned need_starts,unsigned need_ends,int depth) {
        if (timed_out || expired(++cover_nodes,255)) return false;
        if (!outstanding.lo && !outstanding.hi) {
            if (depth!=NEED || need_starts || need_ends)
                throw std::logic_error("wrong completion size or endpoints");
            for (int i=0;i<KEEP;++i) witness[i]=source[fixed[i]];
            for (int i=0;i<NEED;++i) witness[KEEP+i]=candidates[choice[i]].row;
            found=true; return true;
        }
        if (depth>=NEED) return false;
        if (depth>=2 && !endpoint_matching_possible(need_starts,need_ends,depth)) {
            ++endpoint_hall_prunes; return false;
        }
        // A T2(11) table uses 99 of 110 nonloop D2 events. Any unused
        // event absent from every remaining row is among the 11 omissions.
        if (depth>=2) {
            int unsupported=0;
            for (int a=0;a<N;++a) for (int b=0;b<N;++b) if (a!=b) {
                const int e=a*N+b;
                if (get(used2,e)) continue;
                bool supported=false;
                const std::size_t offset=static_cast<std::size_t>(E+e)*words;
                for (std::size_t w=0;w<words;++w)
                    if (feature_bits[offset+w] & allowed[depth][w]) { supported=true; break; }
                if (!supported && ++unsupported>11) {
                    ++d2_support_prunes;
                    if (!first_support_prune_saved) {
                        auto has_support=[&](int feature) {
                            const std::size_t off=static_cast<std::size_t>(feature)*words;
                            for (std::size_t w=0;w<words;++w)
                                if (feature_bits[off+w] & allowed[depth][w]) return true;
                            return false;
                        };
                        bool singletons_supported=true;
                        for (int event=0;event<E && singletons_supported;++event)
                            if (get(outstanding,event) && !has_support(event)) singletons_supported=false;
                        for (int v=0;v<N && singletons_supported;++v) {
                            if ((need_starts & (1U<<v)) && !has_support(2*E+v)) singletons_supported=false;
                            if ((need_ends & (1U<<v)) && !has_support(2*E+N+v)) singletons_supported=false;
                        }
                        if (singletons_supported) {
                            first_support_prune_saved=true;
                            first_support_prune_depth=depth;
                            for (int i=0;i<depth;++i) first_support_prune_rows[i]=candidates[choice[i]].row;
                        }
                    }
                    return false;
                }
            }
        }
        if (depth>=3 && !outgoing_matching_possible(outstanding,need_starts,depth)) {
            ++dual_hall_prunes; return false;
        }
        int pivot=-1;
        std::size_t best=candidates.size()+1;
        auto consider=[&](int feature) {
            std::size_t count=0;
            const std::size_t offset=static_cast<std::size_t>(feature)*words;
            for (std::size_t w=0;w<words;++w) {
                count+=__builtin_popcountll(feature_bits[offset+w] & allowed[depth][w]);
                if (count>=best) break;
            }
            if (!count) return false;
            if (count<best) { pivot=feature; best=count; }
            return true;
        };
        for (int e=0;e<E && best!=1;++e)
            if (get(outstanding,e) && !consider(e)) return false;
        for (int v=0;v<N && best!=1;++v)
            if ((need_starts & (1U<<v)) && !consider(2*E+v)) return false;
        for (int v=0;v<N && best!=1;++v)
            if ((need_ends & (1U<<v)) && !consider(2*E+N+v)) return false;
        if (pivot<0) throw std::logic_error("missing pivot");
        const std::size_t pivot_offset=static_cast<std::size_t>(pivot)*words;
        for (std::size_t w=0;w<words;++w) {
            std::uint64_t options=feature_bits[pivot_offset+w] & allowed[depth][w];
            while (options) {
                const std::uint64_t bit=options & -options; options^=bit;
                const std::size_t index=64*w+static_cast<std::size_t>(__builtin_ctzll(bit));
                const Candidate& c=candidates[index];
                if ((c.adj.lo & outstanding.lo)!=c.adj.lo || (c.adj.hi & outstanding.hi)!=c.adj.hi)
                    throw std::logic_error("candidate overlaps selected D1");
                if ((c.far.lo & used2.lo) || (c.far.hi & used2.hi) ||
                    !(need_starts & (1U<<c.row[0])) || !(need_ends & (1U<<c.row[N-1])))
                    throw std::logic_error("candidate overlaps selected D2 or endpoints");
                for (std::size_t j=0;j<words;++j) {
                    std::uint64_t survivors=allowed[depth][j];
                    for (int f:c.features) {
                        if (!survivors) break;
                        survivors &= ~feature_bits[static_cast<std::size_t>(f)*words+j];
                    }
                    allowed[depth+1][j]=survivors;
                }
                choice[depth]=static_cast<int>(index);
                Bits next{outstanding.lo^c.adj.lo,outstanding.hi^c.adj.hi};
                Bits next2{used2.lo|c.far.lo,used2.hi|c.far.hi};
                if (cover(next,next2,need_starts^(1U<<c.row[0]),need_ends^(1U<<c.row[N-1]),depth+1)) return true;
                if (timed_out) return false;
            }
        }
        return false;
    }
    void run() {
        if (!prepare()) { invalid_fixed=true; return; }
        candidates.reserve(100000);
        generate(0,0);
        if (timed_out || row_cap) return;
        generated_complete=true;
        build_features();
        if (!timed_out) cover(required,fixed2,((1U<<N)-1)&~starts,((1U<<N)-1)&~ends,0);
    }
};

int collisions(const Rows& rows,int distance) {
    int freq[E]{};int c=0;
    for (const auto& row:rows) for (int i=0;i<N-distance;++i) c+=freq[row[i]*N+row[i+distance]]++;
    return c;
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
        if (argc!=8) throw std::runtime_error("usage: BINARY INPUT.txt OUTPUT.json ROW1 ROW2 ROW3 SEED SECONDS");
        const std::string input=argv[1],output=argv[2];
        std::array<int,KEEP> selected={std::stoi(argv[3])-1,std::stoi(argv[4])-1,std::stoi(argv[5])-1};
        std::sort(selected.begin(),selected.end());
        if (selected[0]<0 || selected[KEEP-1]>=N || selected[0]==selected[1] || selected[1]==selected[2])
            throw std::runtime_error("invalid selected rows");
        const auto seed=static_cast<std::uint64_t>(std::stoull(argv[6]));
        const double seconds=std::stod(argv[7]);
        if (seconds<=0) throw std::runtime_error("invalid deadline");
        std::ifstream in(input); if (!in) throw std::runtime_error("cannot read input");
        Rows rows{};
        for (Row& row:rows) {
            unsigned used=0;
            for (int& v:row) {
                if (!(in>>v) || v<0 || v>=N || (used & (1U<<v))) throw std::runtime_error("invalid row");
                used|=1U<<v;
            }
        }
        int extra=0; if (in>>extra) throw std::runtime_error("extra data");
        const auto started=std::chrono::steady_clock::now();
        Solver solver(rows,selected,seed,seconds); solver.run();
        if (solver.found && (collisions(solver.witness,1)!=0 || collisions(solver.witness,2)!=0))
            throw std::logic_error("internal candidate is invalid");
        const std::string status=solver.found?"candidate_witness_requires_independent_check":
            solver.invalid_fixed?"fixed_rows_incompatible":
            solver.timed_out?"unknown_time_limit":solver.row_cap?"unknown_row_cap":"no_completion_exhaustive";
        const auto ms=std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now()-started).count();
        const int fd=open(output.c_str(),O_WRONLY|O_CREAT|O_EXCL,0600);
        if (fd<0) throw std::runtime_error("cannot exclusively create result");
        std::FILE* out=fdopen(fd,"w"); if (!out) { close(fd); throw std::runtime_error("cannot create stream"); }
        std::fprintf(out,"{\n  \"kind\": \"bounded_three_anchor_exact_completion\",\n  \"input_rows_file\": \"%s\",\n",input.c_str());
        std::fprintf(out,"  \"fixed_rows_1based\": [%d, %d, %d],\n  \"seed\": %llu,\n  \"status\": \"%s\",\n",selected[0]+1,selected[1]+1,selected[2]+1,static_cast<unsigned long long>(seed),status.c_str());
        std::fprintf(out,"  \"generation_complete\": %s,\n  \"eligible_rows\": %zu,\n  \"generation_nodes\": %llu,\n  \"cover_nodes\": %llu,\n",solver.generated_complete?"true":"false",solver.candidates.size(),static_cast<unsigned long long>(solver.generated_nodes),static_cast<unsigned long long>(solver.cover_nodes));
        std::fprintf(out,"  \"d2_support_prunes\": %llu,\n",static_cast<unsigned long long>(solver.d2_support_prunes));
        std::fprintf(out,"  \"endpoint_hall_prunes\": %llu,\n",static_cast<unsigned long long>(solver.endpoint_hall_prunes));
        std::fprintf(out,"  \"dual_hall_prunes\": %llu,\n",static_cast<unsigned long long>(solver.dual_hall_prunes));
        std::fprintf(out,"  \"feature_storage_bytes\": %zu,\n  \"elapsed_ms\": %lld",solver.feature_bits.size()*sizeof(std::uint64_t),static_cast<long long>(ms));
        if (solver.first_support_prune_saved) {
            std::fprintf(out,",\n  \"first_d2_support_prune\": {\"depth\": %d, \"unsupported_at_least\": 12, \"all_d1_and_endpoint_singletons_supported\": true, \"added_rows\": [\n",solver.first_support_prune_depth);
            for (int i=0;i<solver.first_support_prune_depth;++i) {
                std::fprintf(out,"    [");
                for (int j=0;j<N;++j) std::fprintf(out,"%s%d",j?", ":"",solver.first_support_prune_rows[i][j]);
                std::fprintf(out,"]%s\n",i+1==solver.first_support_prune_depth?"":",");
            }
            std::fprintf(out,"  ]}");
        }
        if (solver.found) {
            std::fprintf(out,",\n  \"zero_score_claim\": true,\n  \"best_pair_collision_score\": 0,\n  \"d1_pair_collisions\": 0,\n  \"d2_pair_collisions\": 0,\n  \"d1_excess_events\": 0,\n  \"d2_excess_events\": 0,\n  \"rows\": ");
            print_rows(out,solver.witness);
        }
        std::fprintf(out,",\n  \"scope\": \"Only these three fixed source rows; timeout is UNKNOWN and no unrestricted no-go.\"\n}\n");
        if (std::fclose(out)!=0) throw std::runtime_error("output close failed");
        std::cout<<"status="<<status<<" rows="<<solver.candidates.size()<<" generated="<<solver.generated_nodes
                 <<" cover="<<solver.cover_nodes<<" d2_prunes="<<solver.d2_support_prunes
                 <<" endpoint_prunes="<<solver.endpoint_hall_prunes<<" dual_prunes="<<solver.dual_hall_prunes
                 <<" features_bytes="<<solver.feature_bits.size()*sizeof(std::uint64_t)
                 <<" elapsed_ms="<<ms<<'\n';
        return 0;
    } catch (const std::exception& ex) {
        std::cerr<<"error: "<<ex.what()<<'\n';
        return 1;
    }
}
