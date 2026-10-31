// Exact four-row T1 repair. Shared low-level graph functions are compiled
// from the pinned three-row fast walker; this file adds four-row enumeration.
// Compiled: clang++ -std=c++17 -O3 -Wall -Wextra THIS_FILE -o BINARY
// Run: BINARY ROWS.txt OUTPUT.json SECONDS. Independently check any witness.
#define main three_row_walker_included_main
#include "frontier-20261028-three-row-plateau-fast-v1.cpp"
#undef main

namespace {
struct FourTrade {
    Rows base{},best_rows{};
    int best=0, initial=0;
    int freq[N*N]{};
    std::array<int,4> group{},best_group{};
    std::array<Mask,M> g4{},g3{};
    Succ first_succ{},second_succ{};
    Row first{};
    int after_first=0, fixed_score=0;
    std::uint64_t groups_complete=0, group_prunes=0, first_paths=0, second_paths=0;
    std::uint64_t first_prunes=0, second_prunes=0, decompositions_scored=0, improvements=0;
    bool timed_out=false,found_witness=false, changed=false;
    std::chrono::steady_clock::time_point deadline;

    FourTrade(const Rows& rows,double seconds):base(rows),best_rows(rows) {
        initial=best=event_score(rows,2);
        deadline=std::chrono::steady_clock::now()+
            std::chrono::duration_cast<std::chrono::steady_clock::duration>(std::chrono::duration<double>(seconds));
    }
    int add_row(const Row& row,int score) {
        for (int i=0;i<N-2;++i) score+=freq[row[i]*N+row[i+2]]++;
        return score;
    }
    void remove_row(const Row& row) {
        for (int i=0;i<N-2;++i) --freq[row[i]*N+row[i+2]];
    }
    void evaluate(const Row& second,const Row& third,const Row& fourth,int partial_score) {
        ++decompositions_scored;
        int score=add_row(third,partial_score);
        score=add_row(fourth,score);
        remove_row(fourth); remove_row(third);
        if (score<best) {
            best=score; best_group=group; changed=true; ++improvements;
            best_rows=base;
            const Row* repl[4]={&first,&second,&third,&fourth};
            for (int j=0;j<4;++j) best_rows[group[j]]=*repl[j];
            if (score==0) found_witness=true;
        }
    }
    void split_remainder(const Row& second,int partial_score) {
        std::array<Mask,M> graph{};
        for (int v=0;v<M;++v) {
            graph[v]=static_cast<Mask>(g3[v] & ~(1U<<second_succ[v]));
            if (__builtin_popcount(static_cast<unsigned>(graph[v]))!=2)
                throw std::logic_error("bad two-row residual");
        }
        std::array<int,M> match{}; match.fill(-1);
        for (int v=0;v<M;++v) {
            unsigned visited=0;
            if (!augment(v,graph,match,visited)) throw std::logic_error("no perfect matching");
        }
        Succ p{},q{},inverse{};
        for (int head=0;head<M;++head) {
            if (match[head]<0) throw std::logic_error("uncovered head");
            p[match[head]]=head;
        }
        unsigned qheads=0;
        for (int v=0;v<M;++v) {
            const unsigned residual=graph[v] & ~(1U<<p[v]);
            if (__builtin_popcount(residual)!=1) throw std::logic_error("bad complement");
            q[v]=__builtin_ctz(residual); qheads|=1U<<q[v]; inverse[p[v]]=v;
        }
        if (qheads!=(1U<<M)-1) throw std::logic_error("not a matching");
        std::array<unsigned,M> components{};
        int size=0;
        unsigned unseen=(1U<<M)-1;
        while (unseen) {
            const int root=__builtin_ctz(unseen);
            int v=root; unsigned part=0;
            do {
                if (!(unseen & (1U<<v))) throw std::logic_error("bad alternating component");
                unseen&=~(1U<<v); part|=1U<<v; v=inverse[q[v]];
            } while (v!=root);
            if (__builtin_popcount(part)<2) throw std::logic_error("shared arc");
            components[size++]=part;
        }
        for (unsigned mask=0;mask<(1U<<(size-1));++mask) {
            unsigned switched=0;
            for (int j=1;j<size;++j) if (mask & (1U<<(j-1))) switched|=components[j];
            Succ pp{},qq{};
            for (int v=0;v<M;++v) {
                const bool flip=switched & (1U<<v);
                pp[v]=flip?q[v]:p[v]; qq[v]=flip?p[v]:q[v];
            }
            Row third{},fourth{};
            if (!decode(pp,third) || !decode(qq,fourth) || second>=third || second>=fourth) continue;
            evaluate(second,third,fourth,partial_score);
            if (found_witness) return;
        }
    }
    void finish_second() {
        ++second_paths;
        if ((second_paths&1023U)==0 && std::chrono::steady_clock::now()>=deadline) { timed_out=true; return; }
        Row second{};
        if (!decode(second_succ,second)) throw std::logic_error("bad second Hamilton path");
        if (first>=second) return;
        const int score=add_row(second,after_first);
        if (score<best) split_remainder(second,score); else ++second_prunes;
        remove_row(second);
    }
    void dfs_second(int v,unsigned remaining) {
        if (timed_out || found_witness) return;
        if (!remaining) {
            if (g3[v] & (1U<<S)) { second_succ[v]=S; finish_second(); }
            return;
        }
        unsigned options=g3[v] & remaining;
        while (options) {
            const unsigned bit=options & -options; options^=bit;
            second_succ[v]=__builtin_ctz(bit);
            dfs_second(second_succ[v],remaining^bit);
            if (timed_out || found_witness) return;
        }
    }
    void finish_first() {
        ++first_paths;
        if (!decode(first_succ,first)) throw std::logic_error("bad first Hamilton path");
        after_first=add_row(first,fixed_score);
        if (after_first<best) {
            for (int v=0;v<M;++v) g3[v]=static_cast<Mask>(g4[v] & ~(1U<<first_succ[v]));
            dfs_second(S,(1U<<N)-1);
        } else ++first_prunes;
        remove_row(first);
    }
    void dfs_first(int v,unsigned remaining) {
        if (timed_out || found_witness) return;
        if (!remaining) {
            if (g4[v] & (1U<<S)) { first_succ[v]=S; finish_first(); }
            return;
        }
        unsigned options=g4[v] & remaining;
        while (options) {
            const unsigned bit=options & -options; options^=bit;
            first_succ[v]=__builtin_ctz(bit);
            dfs_first(first_succ[v],remaining^bit);
            if (timed_out || found_witness) return;
        }
    }
    void scan_group(int a,int b,int c,int d) {
        group={a,b,c,d};
        const Succ p=successor(base[a]),q=successor(base[b]),r=successor(base[c]),s=successor(base[d]);
        for (int v=0;v<M;++v) {
            g4[v]=static_cast<Mask>((1U<<p[v])|(1U<<q[v])|(1U<<r[v])|(1U<<s[v]));
            if (__builtin_popcount(static_cast<unsigned>(g4[v]))!=4)
                throw std::logic_error("removed cycles share an arc");
        }
        std::fill(std::begin(freq),std::end(freq),0); fixed_score=0;
        for (int t=0;t<N;++t) if (t!=a && t!=b && t!=c && t!=d)
            fixed_score=add_row(base[t],fixed_score);
        // Remaining rows can only add collisions, never remove fixed ones.
        if (fixed_score>=best) { ++group_prunes; return; }
        dfs_first(S,(1U<<N)-1);
    }
};
} // namespace

int main(int argc,char** argv) {
    try {
        if (argc!=4) throw std::runtime_error("usage: BINARY ROWS.txt OUTPUT.json SECONDS");
        const std::string input=argv[1],output=argv[2];
        const double seconds=std::stod(argv[3]);
        if (seconds<=0) throw std::runtime_error("invalid budget");
        std::ifstream in(input);
        if (!in) throw std::runtime_error("cannot open input");
        Rows rows{};
        for (Row& row:rows) {
            unsigned mask=0;
            for (int& x:row) {
                if (!(in>>x) || x<0 || x>=N || (mask & (1U<<x)))
                    throw std::runtime_error("input row not a permutation");
                mask|=1U<<x;
            }
        }
        int extra=0;
        if (in>>extra) throw std::runtime_error("extra input values");
        int distinct=0;
        if (event_score(rows,1,&distinct)!=0 || distinct!=N*(N-1)) throw std::runtime_error("not T1");
        const auto started=std::chrono::steady_clock::now();
        FourTrade search(rows,seconds);
        for (int a=0;a<N-3 && !search.found_witness && !search.timed_out;++a)
            for (int b=a+1;b<N-2 && !search.found_witness && !search.timed_out;++b)
                for (int c=b+1;c<N-1 && !search.found_witness && !search.timed_out;++c)
                    for (int d=c+1;d<N && !search.found_witness && !search.timed_out;++d) {
                        if (std::chrono::steady_clock::now()>=search.deadline) { search.timed_out=true; break; }
                        search.scan_group(a,b,c,d);
                        if (!search.timed_out && !search.found_witness) ++search.groups_complete;
                    }
        int e1=0,e2=0;
        if (event_score(search.best_rows,1,nullptr,&e1)!=0 || event_score(search.best_rows,2,nullptr,&e2)!=search.best)
            throw std::logic_error("best output event mismatch");
        const auto ms=std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now()-started).count();
        const bool complete=!search.timed_out && !search.found_witness && search.groups_complete==330;
        const int fd=open(output.c_str(),O_WRONLY|O_CREAT|O_EXCL,0600);
        if (fd<0) throw std::runtime_error("cannot exclusively create output");
        std::FILE* out=fdopen(fd,"w");
        if (!out) { close(fd); throw std::runtime_error("cannot open output stream"); }
        std::fprintf(out,"{\n  \"kind\": \"pruned_exact_t1_four_row_trades\",\n  \"input_rows_file\": \"%s\",\n",input.c_str());
        std::fprintf(out,"  \"complete_neighborhood_scan\": %s,\n  \"budget_exhausted\": %s,\n  \"witness_early_stop\": %s,\n",complete?"true":"false",search.timed_out?"true":"false",search.found_witness?"true":"false");
        std::fprintf(out,"  \"row_quadruples_fully_scanned\": %llu,\n  \"fixed_collision_prunes\": %llu,\n  \"first_paths_visited\": %llu,\n  \"second_paths_visited\": %llu,\n",static_cast<unsigned long long>(search.groups_complete),static_cast<unsigned long long>(search.group_prunes),static_cast<unsigned long long>(search.first_paths),static_cast<unsigned long long>(search.second_paths));
        std::fprintf(out,"  \"first_collision_prunes\": %llu,\n  \"second_collision_prunes\": %llu,\n  \"decompositions_scored\": %llu,\n  \"strict_improvements\": %llu,\n",static_cast<unsigned long long>(search.first_prunes),static_cast<unsigned long long>(search.second_prunes),static_cast<unsigned long long>(search.decompositions_scored),static_cast<unsigned long long>(search.improvements));
        std::fprintf(out,"  \"initial_d2_pair_collisions\": %d,\n  \"best_pair_collision_score\": %d,\n",search.initial,search.best);
        std::fprintf(out,"  \"d1_pair_collisions\": 0,\n  \"d2_pair_collisions\": %d,\n  \"d1_excess_events\": %d,\n  \"d2_excess_events\": %d,\n",search.best,e1,e2);
        std::fprintf(out,"  \"best_changed_rows_1based\": ");
        if (!search.changed) std::fprintf(out,"null"); else std::fprintf(out,"[%d, %d, %d, %d]",search.best_group[0]+1,search.best_group[1]+1,search.best_group[2]+1,search.best_group[3]+1);
        std::fprintf(out,",\n  \"zero_score_claim\": %s,\n  \"elapsed_ms\": %lld,\n  \"rows\": ",search.best==0?"true":"false",static_cast<long long>(ms));
        write_rows(out,search.best_rows);
        std::fprintf(out,",\n  \"scope\": \"Four-row T1 trades of this table only; pruning uses nondecreasing D2 pair collisions. Failure is not global nonexistence.\"\n}\n");
        if (std::fclose(out)!=0) throw std::runtime_error("output close failed");
        std::cout<<"complete="<<complete<<" budget="<<search.timed_out<<" groups="<<search.groups_complete
                 <<" first="<<search.first_paths<<" second="<<search.second_paths
                 <<" scored="<<search.decompositions_scored<<" initial="<<search.initial<<" best="<<search.best
                 <<" witness_claim="<<(search.best==0?"yes":"no")<<" elapsed_ms="<<ms<<'\n';
        return 0;
    } catch (const std::exception& e) {
        std::cerr<<"error: "<<e.what()<<'\n';
        return 1;
    }
}
