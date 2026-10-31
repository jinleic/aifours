// Independent exact four-row T1-neighborhood checker.
// Unlike the matching-component producer, enumerate all eligible Hamilton
// paths and use exact cover on the 48 residual arcs, with incremental D2
// collision bounds. No fixed-input conclusion is a global no-go.
// Compile: clang++ -std=c++17 -O3 -Wall -Wextra SOURCE -o BINARY
// Run: BINARY ROWS.txt OUTPUT.json SECONDS. A counterexample needs direct check.
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
constexpr int N=11, V=12, SENTINEL=11, EDGE_COUNT=48;
using Row=std::array<int,N>;
using Rows=std::array<Row,N>;
using Succ=std::array<int,V>;

Succ cycle(const Row& row) {
    Succ s{};
    s[SENTINEL]=row[0];
    for (int i=0;i<N-1;++i) s[row[i]]=row[i+1];
    s[row[N-1]]=SENTINEL;
    return s;
}

int score(const Rows& rows,int distance,int* excess=nullptr) {
    int freq[N*N]{};
    int ans=0;
    for (const auto& row:rows) for (int i=0;i<N-distance;++i)
        ans+=freq[row[i]*N+row[i+distance]]++;
    if (excess) {
        int e=0;
        for (int f:freq) if (f>1) e+=f-1;
        *excess=e;
    }
    return ans;
}

struct Candidate { Row row{}; std::uint64_t arcs=0; };
struct Checker {
    Rows source{},counterexample{};
    int threshold=0, found_score=0;
    int g[V][4]{}, eid[V][V]{}, freq[N*N]{};
    std::array<int,4> group{},choice{};
    Row path{};
    std::vector<Candidate> candidates;
    std::array<std::vector<int>,EDGE_COUNT> by_edge{};
    std::uint64_t generated=0,cover_nodes=0,groups_complete=0,fixed_prunes=0;
    bool timed_out=false,found=false;
    std::chrono::steady_clock::time_point deadline;

    Checker(const Rows& input,double seconds):source(input),counterexample(input) {
        threshold=found_score=score(input,2);
        deadline=std::chrono::steady_clock::now()+
            std::chrono::duration_cast<std::chrono::steady_clock::duration>(std::chrono::duration<double>(seconds));
    }
    int add(const Row& row,int current) {
        for (int i=0;i<N-2;++i) current+=freq[row[i]*N+row[i+2]]++;
        return current;
    }
    void undo(const Row& row) {
        for (int i=0;i<N-2;++i) --freq[row[i]*N+row[i+2]];
    }
    void generate(int at,unsigned unused,int depth) {
        if (!unused) {
            if (eid[at][SENTINEL]<0) return;
            Candidate c; c.row=path;
            int previous=SENTINEL;
            for (int x:path) {
                const int idx=eid[previous][x];
                if (idx<0) throw std::logic_error("missing generated edge");
                c.arcs|=std::uint64_t{1}<<idx;
                previous=x;
            }
            c.arcs|=std::uint64_t{1}<<eid[previous][SENTINEL];
            if (__builtin_popcountll(c.arcs)!=V) throw std::logic_error("bad Hamilton arc count");
            candidates.push_back(c); ++generated;
            return;
        }
        for (int j=0;j<4;++j) {
            const int nxt=g[at][j];
            if (unused & (1U<<nxt)) {
                path[depth]=nxt;
                generate(nxt,unused^(1U<<nxt),depth+1);
            }
        }
    }
    void search(std::uint64_t used,int depth,int current_score) {
        if (found || timed_out) return;
        ++cover_nodes;
        if ((cover_nodes&4095U)==0 && std::chrono::steady_clock::now()>=deadline) {
            timed_out=true; return;
        }
        const std::uint64_t all=(std::uint64_t{1}<<EDGE_COUNT)-1;
        if (used==all) {
            if (depth!=4) throw std::logic_error("incorrect exact cover size");
            if (current_score>=threshold) throw std::logic_error("score pruning failed");
            found=true; found_score=current_score; counterexample=source;
            for (int i=0;i<4;++i) counterexample[group[i]]=candidates[choice[i]].row;
            return;
        }
        if (depth>=4) return;
        int pivot=-1, min_count=static_cast<int>(candidates.size())+1;
        std::uint64_t missing=all & ~used;
        while (missing) {
            const std::uint64_t bit=missing & -missing; missing^=bit;
            const int e=__builtin_ctzll(bit);
            int count=0;
            for (int id:by_edge[e]) if (!(candidates[id].arcs & used)) ++count;
            if (!count) return;
            if (count<min_count) { min_count=count; pivot=e; if (count==1) break; }
        }
        if (pivot<0) throw std::logic_error("missing pivot");
        for (int id:by_edge[pivot]) {
            const Candidate& c=candidates[id];
            if (c.arcs & used) continue;
            const int next_score=add(c.row,current_score);
            if (next_score<threshold) {
                choice[depth]=id;
                search(used|c.arcs,depth+1,next_score);
            }
            undo(c.row);
            if (found || timed_out) return;
        }
    }
    void scan(int a,int b,int c,int d) {
        group={a,b,c,d};
        std::array<Succ,4> cycles={cycle(source[a]),cycle(source[b]),cycle(source[c]),cycle(source[d])};
        for (auto& row:eid) for (int& x:row) x=-1;
        for (int v=0;v<V;++v) {
            for (int j=0;j<4;++j) g[v][j]=cycles[j][v];
            std::sort(g[v],g[v]+4);
            for (int j=0;j<4;++j) {
                if (j && g[v][j]==g[v][j-1]) throw std::logic_error("duplicate residual arc");
                eid[v][g[v][j]]=4*v+j;
            }
        }
        std::fill(std::begin(freq),std::end(freq),0);
        int fixed_score=0;
        for (int i=0;i<N;++i) if (i!=a && i!=b && i!=c && i!=d)
            fixed_score=add(source[i],fixed_score);
        if (fixed_score>=threshold) { ++fixed_prunes; return; }
        candidates.clear();
        for (auto& v:by_edge) v.clear();
        generate(SENTINEL,(1U<<N)-1,0);
        for (std::size_t i=0;i<candidates.size();++i) {
            std::uint64_t bits=candidates[i].arcs;
            while (bits) {
                const std::uint64_t bit=bits & -bits; bits^=bit;
                by_edge[__builtin_ctzll(bit)].push_back(static_cast<int>(i));
            }
        }
        search(0,0,fixed_score);
    }
};

void print_rows(std::FILE* out,const Rows& rows) {
    std::fprintf(out,"[\n");
    for (int i=0;i<N;++i) {
        std::fprintf(out,"    [");
        for (int j=0;j<N;++j) std::fprintf(out,"%s%d",j?", ":"",rows[i][j]);
        std::fprintf(out,"]%s\n",i+1==N?"":",");
    }
    std::fprintf(out,"  ]");
}
} // namespace

int main(int argc,char** argv) {
    try {
        if (argc!=4) throw std::runtime_error("usage: BINARY ROWS.txt OUTPUT.json SECONDS");
        const std::string source=argv[1],output=argv[2];
        const double seconds=std::stod(argv[3]);
        if (seconds<=0) throw std::runtime_error("bad time budget");
        std::ifstream in(source);
        if (!in) throw std::runtime_error("cannot read source rows");
        Rows rows{};
        for (Row& row:rows) {
            unsigned seen=0;
            for (int& value:row) {
                if (!(in>>value) || value<0 || value>=N || (seen & (1U<<value)))
                    throw std::runtime_error("bad permutation");
                seen|=1U<<value;
            }
        }
        int extra=0; if (in>>extra) throw std::runtime_error("extra input");
        if (score(rows,1)!=0) throw std::runtime_error("source is not T1");
        const auto started=std::chrono::steady_clock::now();
        Checker checker(rows,seconds);
        for (int a=0;a<N-3 && !checker.found && !checker.timed_out;++a)
            for (int b=a+1;b<N-2 && !checker.found && !checker.timed_out;++b)
                for (int c=b+1;c<N-1 && !checker.found && !checker.timed_out;++c)
                    for (int d=c+1;d<N && !checker.found && !checker.timed_out;++d) {
                        if (std::chrono::steady_clock::now()>=checker.deadline) { checker.timed_out=true; break; }
                        checker.scan(a,b,c,d);
                        if (!checker.timed_out && !checker.found) ++checker.groups_complete;
                    }
        if (score(checker.counterexample,1)!=0 || score(checker.counterexample,2)!=checker.found_score)
            throw std::logic_error("counterexample event counts inconsistent");
        const bool complete=checker.groups_complete==330 && !checker.timed_out && !checker.found;
        const auto ms=std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now()-started).count();
        int e1=0,e2=0; score(checker.counterexample,1,&e1); score(checker.counterexample,2,&e2);
        const int fd=open(output.c_str(),O_WRONLY|O_CREAT|O_EXCL,0600);
        if (fd<0) throw std::runtime_error("cannot exclusively create output");
        std::FILE* out=fdopen(fd,"w");
        if (!out) { close(fd); throw std::runtime_error("cannot open output stream"); }
        std::fprintf(out,"{\n  \"kind\": \"independent_four_row_exact_cover\",\n  \"input_rows_file\": \"%s\",\n",source.c_str());
        std::fprintf(out,"  \"complete_neighborhood_scan\": %s,\n  \"budget_exhausted\": %s,\n  \"strict_improvement_found\": %s,\n",complete?"true":"false",checker.timed_out?"true":"false",checker.found?"true":"false");
        std::fprintf(out,"  \"row_quadruples_fully_scanned\": %llu,\n  \"fixed_collision_prunes\": %llu,\n  \"eligible_hamilton_paths_generated\": %llu,\n  \"exact_cover_nodes\": %llu,\n",static_cast<unsigned long long>(checker.groups_complete),static_cast<unsigned long long>(checker.fixed_prunes),static_cast<unsigned long long>(checker.generated),static_cast<unsigned long long>(checker.cover_nodes));
        std::fprintf(out,"  \"initial_d2_pair_collisions\": %d,\n  \"best_pair_collision_score\": %d,\n  \"d1_pair_collisions\": 0,\n  \"d2_pair_collisions\": %d,\n",checker.threshold,checker.found_score,checker.found_score);
        std::fprintf(out,"  \"d1_excess_events\": %d,\n  \"d2_excess_events\": %d,\n  \"zero_score_claim\": %s,\n  \"elapsed_ms\": %lld,\n  \"rows\": ",e1,e2,checker.found_score==0?"true":"false",static_cast<long long>(ms));
        print_rows(out,checker.counterexample);
        std::fprintf(out,",\n  \"scope\": \"Only this T1 table and its at-most-four-row replacement neighborhood; no unrestricted no-go.\"\n}\n");
        if (std::fclose(out)!=0) throw std::runtime_error("output write failed");
        std::cout<<"complete="<<complete<<" budget="<<checker.timed_out<<" found="<<checker.found
                 <<" groups="<<checker.groups_complete<<" candidate_paths="<<checker.generated
                 <<" cover_nodes="<<checker.cover_nodes<<" threshold="<<checker.threshold
                 <<" score="<<checker.found_score<<" elapsed_ms="<<ms<<'\n';
        return 0;
    } catch (const std::exception& ex) {
        std::cerr<<"error: "<<ex.what()<<'\n';
        return 1;
    }
}
