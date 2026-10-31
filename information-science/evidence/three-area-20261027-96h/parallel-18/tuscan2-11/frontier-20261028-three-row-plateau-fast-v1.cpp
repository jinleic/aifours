// Bounded T1-preserving three-row walk. Failure is not a nonexistence proof.
// Compile: clang++ -std=c++17 -O3 -Wall -Wextra SOURCE -o BINARY
// Run: BINARY ROWS.txt OUTPUT.json RNG_SEED MAX_STEPS SECONDS SCORE_BAND
// Output candidates require independent verification of all actual linear events.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <fcntl.h>
#include <fstream>
#include <iostream>
#include <random>
#include <set>
#include <stdexcept>
#include <string>
#include <unistd.h>
#include <vector>

namespace {
constexpr int N=11, S=11, M=12;
using Row=std::array<int,N>;
using Rows=std::array<Row,N>;
using Succ=std::array<int,M>;
using Mask=std::uint16_t;
using Key=std::array<std::uint64_t,N>;

Succ successor(const Row& row) {
    Succ out{};
    out[S]=row[0];
    for (int i=0;i<N-1;++i) out[row[i]]=row[i+1];
    out[row[N-1]]=S;
    return out;
}

bool decode(const Succ& succ, Row& row) {
    int v=S;
    unsigned seen=1U<<S;
    for (int i=0;i<N;++i) {
        v=succ[v];
        if (v<0 || v>=M || (seen & (1U<<v))) return false;
        seen |= 1U<<v;
        row[i]=v;
    }
    return succ[v]==S;
}

std::uint64_t pack(const Row& row) {
    std::uint64_t value=0;
    for (int x:row) value=(value<<4)|static_cast<std::uint64_t>(x);
    return value;
}

Key key_of(const Rows& rows) {
    Key key{};
    for (int i=0;i<N;++i) key[i]=pack(rows[i]);
    std::sort(key.begin(),key.end());
    return key;
}

int event_score(const Rows& rows, int distance, int* distinct=nullptr, int* excess=nullptr) {
    int counts[N*N]{};
    int score=0;
    for (const Row& row:rows) for (int i=0;i<N-distance;++i)
        score += counts[row[i]*N+row[i+distance]]++;
    if (distinct || excess) {
        int d=0,e=0;
        for (int value:counts) { if (value) ++d; if (value>1) e+=value-1; }
        if (distinct) *distinct=d;
        if (excess) *excess=e;
    }
    return score;
}

bool augment(int v, const std::array<Mask,M>& graph, std::array<int,M>& match, unsigned& seen) {
    unsigned options=graph[v] & ~seen;
    while (options) {
        const unsigned bit=options & -options;
        options^=bit;
        if (seen & bit) continue;
        seen|=bit;
        const int head=__builtin_ctz(bit);
        if (match[head]<0 || augment(match[head],graph,match,seen)) {
            match[head]=v;
            return true;
        }
    }
    return false;
}

struct Walker {
    Rows current{},best_rows{},chosen{};
    int best=0, current_score=0, candidate_score=0, band=0;
    int frequency[N*N]{};
    int fixed_score=0;
    std::array<int,3> group{},chosen_group{};
    std::array<Mask,M> graph{};
    Succ first_succ{};
    std::set<Key> seen;
    std::mt19937_64 random;
    std::chrono::steady_clock::time_point deadline;
    std::uint64_t groups=0,first_cycles=0,decompositions=0,ties=0;
    bool has_candidate=false, timed_out=false, found_witness=false;

    Walker(const Rows& rows, std::uint64_t seed, int max_band, double seconds)
        :current(rows),best_rows(rows),band(max_band),random(seed) {
        best=current_score=event_score(rows,2);
        seen.insert(key_of(rows));
        deadline=std::chrono::steady_clock::now()+
            std::chrono::duration_cast<std::chrono::steady_clock::duration>(std::chrono::duration<double>(seconds));
    }

    void evaluate(const Row& a, const Row& b, const Row& c) {
        ++decompositions;
        const Row* selected[3]={&a,&b,&c};
        int score=fixed_score;
        for (const Row* r:selected) for (int i=0;i<N-2;++i)
            score += frequency[(*r)[i]*N+(*r)[i+2]]++;
        for (const Row* r:selected) for (int i=0;i<N-2;++i)
            --frequency[(*r)[i]*N+(*r)[i+2]];
        if (score>best+band || (has_candidate && score>candidate_score)) return;
        Key candidate_key{};
        for (int i=0;i<N;++i) {
            const Row* row=&current[i];
            for (int j=0;j<3;++j) if (group[j]==i) row=selected[j];
            candidate_key[i]=pack(*row);
        }
        std::sort(candidate_key.begin(),candidate_key.end());
        if (seen.find(candidate_key)!=seen.end()) return;
        bool take=false;
        if (!has_candidate || score<candidate_score) {
            has_candidate=true; candidate_score=score; ties=1; take=true;
        } else if (score==candidate_score) {
            ++ties;
            take=std::uniform_int_distribution<std::uint64_t>(0,ties-1)(random)==0;
        }
        if (take) {
            chosen=current;
            for (int j=0;j<3;++j) chosen[group[j]]=*selected[j];
            chosen_group=group;
        }
        if (score==0) found_witness=true;
    }

    void split_remaining() {
        ++first_cycles;
        Row first{};
        if (!decode(first_succ,first)) throw std::logic_error("non-Hamilton first path");
        std::array<Mask,M> rest{};
        for (int v=0;v<M;++v) {
            rest[v]=static_cast<Mask>(graph[v] & ~(1U<<first_succ[v]));
            if (__builtin_popcount(static_cast<unsigned>(rest[v]))!=2)
                throw std::logic_error("residual graph not 2-regular on tails");
        }
        std::array<int,M> match{};
        match.fill(-1);
        for (int v=0;v<M;++v) {
            unsigned visited=0;
            if (!augment(v,rest,match,visited)) throw std::logic_error("no perfect matching");
        }
        Succ p{},q{},inverse{};
        for (int head=0;head<M;++head) {
            if (match[head]<0) throw std::logic_error("uncovered head");
            p[match[head]]=head;
        }
        unsigned qheads=0;
        for (int v=0;v<M;++v) {
            const unsigned remaining=rest[v] & ~(1U<<p[v]);
            if (__builtin_popcount(remaining)!=1) throw std::logic_error("bad complement");
            q[v]=__builtin_ctz(remaining);
            qheads|=1U<<q[v];
            inverse[p[v]]=v;
        }
        if (qheads!=(1U<<M)-1) throw std::logic_error("complement not perfect matching");
        std::array<unsigned,M> components{};
        int ncomponents=0;
        unsigned unseen=(1U<<M)-1;
        while (unseen) {
            const int root=__builtin_ctz(unseen);
            int v=root;
            unsigned component=0;
            do {
                if (!(unseen & (1U<<v))) throw std::logic_error("relative map not cycle");
                unseen&=~(1U<<v);
                component|=1U<<v;
                v=inverse[q[v]];
            } while (v!=root);
            if (__builtin_popcount(component)<2) throw std::logic_error("common arc");
            components[ncomponents++]=component;
        }
        // Fix first component orientation: complementing all choices just
        // swaps the final two rows. Thus no unordered pair is lost.
        for (unsigned bits=0;bits<(1U<<(ncomponents-1));++bits) {
            unsigned switched=0;
            for (int i=1;i<ncomponents;++i) if (bits & (1U<<(i-1))) switched|=components[i];
            Succ pp{},qq{};
            for (int v=0;v<M;++v) {
                const bool flip=switched & (1U<<v);
                pp[v]=flip?q[v]:p[v];
                qq[v]=flip?p[v]:q[v];
            }
            Row second{},third{};
            if (!decode(pp,second) || !decode(qq,third) || first>second || first>third) continue;
            evaluate(first,second,third);
            if (found_witness) return;
        }
    }

    void enumerate_first(int v, unsigned remaining) {
        if (timed_out || found_witness) return;
        if (!remaining) {
            if (graph[v] & (1U<<S)) { first_succ[v]=S; split_remaining(); }
            return;
        }
        unsigned options=graph[v] & remaining;
        while (options) {
            const unsigned bit=options & -options;
            options^=bit;
            first_succ[v]=__builtin_ctz(bit);
            enumerate_first(first_succ[v],remaining^bit);
            if (timed_out || found_witness) return;
        }
    }

    void scan_group(int a,int b,int c) {
        group={a,b,c};
        const Succ p=successor(current[a]),q=successor(current[b]),r=successor(current[c]);
        for (int v=0;v<M;++v) {
            graph[v]=static_cast<Mask>((1U<<p[v])|(1U<<q[v])|(1U<<r[v]));
            if (__builtin_popcount(static_cast<unsigned>(graph[v]))!=3)
                throw std::logic_error("input augmented arcs overlap");
        }
        std::fill(std::begin(frequency),std::end(frequency),0);
        fixed_score=0;
        for (int t=0;t<N;++t) if (t!=a && t!=b && t!=c)
            for (int i=0;i<N-2;++i)
                fixed_score+=frequency[current[t][i]*N+current[t][i+2]]++;
        ++groups;
        enumerate_first(S,(1U<<N)-1);
    }
};

void write_rows(std::FILE* out,const Rows& rows) {
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
        if (argc!=7) throw std::runtime_error("usage: BINARY ROWS.txt OUTPUT.json RNG_SEED MAX_STEPS SECONDS SCORE_BAND");
        const std::string input=argv[1], output=argv[2];
        const auto seed=static_cast<std::uint64_t>(std::stoull(argv[3]));
        const int max_steps=std::stoi(argv[4]);
        const double seconds=std::stod(argv[5]);
        const int band=std::stoi(argv[6]);
        if (max_steps<=0 || seconds<=0 || band<0) throw std::runtime_error("invalid budget");
        std::ifstream in(input);
        if (!in) throw std::runtime_error("cannot open input rows");
        Rows rows{};
        for (Row& row:rows) {
            unsigned mask=0;
            for (int& x:row) {
                if (!(in>>x) || x<0 || x>=N || (mask & (1U<<x)))
                    throw std::runtime_error("input row is not a permutation");
                mask|=1U<<x;
            }
        }
        int extra=0;
        if (in>>extra) throw std::runtime_error("extra input row values");
        int d1_distinct=0;
        if (event_score(rows,1,&d1_distinct)!=0 || d1_distinct!=N*(N-1))
            throw std::runtime_error("source is not T1");
        const auto started=std::chrono::steady_clock::now();
        Walker w(rows,seed,band,seconds);
        const int initial=w.best;
        std::vector<int> scores;
        scores.reserve(static_cast<std::size_t>(max_steps));
        std::string status="step_limit";
        for (int step=0;step<max_steps;++step) {
            w.has_candidate=false; w.ties=0;
            for (int a=0;a<N-2 && !w.found_witness && !w.timed_out;++a)
                for (int b=a+1;b<N-1 && !w.found_witness && !w.timed_out;++b)
                    for (int c=b+1;c<N && !w.found_witness && !w.timed_out;++c) {
                        if (std::chrono::steady_clock::now()>=w.deadline) { w.timed_out=true; break; }
                        w.scan_group(a,b,c);
                    }
            if (!w.has_candidate) {
                status=w.timed_out?"time_limit":"no_unseen_neighbor_within_band";
                break;
            }
            w.current=w.chosen;
            w.current_score=w.candidate_score;
            w.seen.insert(key_of(w.current));
            scores.push_back(w.current_score);
            if (w.current_score<w.best) { w.best=w.current_score; w.best_rows=w.current; }
            if (w.best==0) { status="candidate_witness_requires_independent_check"; break; }
            if (w.timed_out) { status="time_limit"; break; }
        }
        int excess1=0,excess2=0;
        if (event_score(w.best_rows,1,nullptr,&excess1)!=0 || event_score(w.best_rows,2,nullptr,&excess2)!=w.best)
            throw std::logic_error("output score mismatch");
        const auto ms=std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now()-started).count();
        const int fd=open(output.c_str(),O_WRONLY|O_CREAT|O_EXCL,0600);
        if (fd<0) throw std::runtime_error("cannot exclusively create output");
        std::FILE* out=fdopen(fd,"w");
        if (!out) { close(fd); throw std::runtime_error("cannot open output stream"); }
        std::fprintf(out,"{\n  \"schema\": 1,\n  \"kind\": \"t1_three_row_plateau_walk\",\n");
        std::fprintf(out,"  \"input_rows_file\": \"%s\",\n  \"seed\": %llu,\n",input.c_str(),static_cast<unsigned long long>(seed));
        std::fprintf(out,"  \"status\": \"%s\",\n  \"elapsed_ms\": %lld,\n",status.c_str(),static_cast<long long>(ms));
        std::fprintf(out,"  \"steps_taken\": %zu,\n  \"distinct_states_seen\": %zu,\n",scores.size(),w.seen.size());
        std::fprintf(out,"  \"row_groups_scanned\": %llu,\n  \"first_cycles_visited\": %llu,\n  \"hamilton_decompositions_examined\": %llu,\n",
            static_cast<unsigned long long>(w.groups),static_cast<unsigned long long>(w.first_cycles),static_cast<unsigned long long>(w.decompositions));
        std::fprintf(out,"  \"initial_d2_pair_collisions\": %d,\n  \"best_pair_collision_score\": %d,\n",initial,w.best);
        std::fprintf(out,"  \"d1_pair_collisions\": 0,\n  \"d2_pair_collisions\": %d,\n  \"d1_excess_events\": %d,\n  \"d2_excess_events\": %d,\n",w.best,excess1,excess2);
        std::fprintf(out,"  \"zero_score_claim\": %s,\n  \"score_trace\": [",w.best==0?"true":"false");
        for (std::size_t i=0;i<scores.size();++i) std::fprintf(out,"%s%d",i?", ":"",scores[i]);
        std::fprintf(out,"],\n  \"rows\": ");
        write_rows(out,w.best_rows);
        std::fprintf(out,",\n  \"scope\": \"A bounded heuristic walk; failure is not nonexistence. Linear distance-two events only.\"\n}\n");
        if (std::fclose(out)!=0) throw std::runtime_error("output close failed");
        std::cout<<"status="<<status<<" steps="<<scores.size()<<" groups="<<w.groups
                 <<" decompositions="<<w.decompositions<<" initial="<<initial<<" best="<<w.best
                 <<" witness_claim="<<(w.best==0?"yes":"no")<<" elapsed_ms="<<ms<<'\n';
        return 0;
    } catch (const std::exception& e) {
        std::cerr<<"error: "<<e.what()<<'\n';
        return 1;
    }
}
