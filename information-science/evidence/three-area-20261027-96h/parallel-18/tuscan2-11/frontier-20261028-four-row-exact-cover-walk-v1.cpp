// Bounded four-row plateau walk using the independently written direct
// Hamilton-row/exact-cover checker. For each random selected row group and
// excluded original row, seek a genuinely changed T1 decomposition inside a
// D2-collision score band. This is heuristic: failure proves nothing global.
// Build: clang++ -std=c++17 -O3 -Wall -Wextra THIS_SOURCE -o BINARY
// Run: BINARY INPUT.txt OUTPUT.json SEED MAX_STEPS SECONDS SCORE_BAND
#define main four_row_checker_included_main
#include "frontier-20261028-four-row-independent-v1.cpp"
#undef main
#include <random>
#include <set>

namespace {
using State=std::array<std::uint64_t,N>;
std::uint64_t encode(const Row& row) {
    std::uint64_t result=0;
    for (int v:row) result=(result<<4)|static_cast<std::uint64_t>(v);
    return result;
}
State canonical(const Rows& rows) {
    State s{};
    for (int i=0;i<N;++i) s[i]=encode(rows[i]);
    std::sort(s.begin(),s.end());
    return s;
}

// Prepare precisely the residual four-row graph, excluding one original row
// from the generated possible cycles. This guarantees a nontrivial move.
bool attempt(Checker& solver,const std::array<int,4>& group,int excluded) {
    solver.group=group;
    std::array<Succ,4> removed{};
    for (int i=0;i<4;++i) removed[i]=cycle(solver.source[group[i]]);
    for (auto& row:solver.eid) for (int& x:row) x=-1;
    for (int v=0;v<V;++v) {
        for (int j=0;j<4;++j) solver.g[v][j]=removed[j][v];
        std::sort(solver.g[v],solver.g[v]+4);
        for (int j=0;j<4;++j) {
            if (j && solver.g[v][j]==solver.g[v][j-1])
                throw std::logic_error("repeated residual edge");
            solver.eid[v][solver.g[v][j]]=4*v+j;
        }
    }
    std::fill(std::begin(solver.freq),std::end(solver.freq),0);
    int fixed_score=0;
    for (int i=0;i<N;++i)
        if (i!=group[0] && i!=group[1] && i!=group[2] && i!=group[3])
            fixed_score=solver.add(solver.source[i],fixed_score);
    if (fixed_score>=solver.threshold) return false;
    solver.candidates.clear();
    for (auto& v:solver.by_edge) v.clear();
    solver.generate(SENTINEL,(1U<<N)-1,0);
    const Row excluded_row=solver.source[group[excluded]];
    solver.candidates.erase(std::remove_if(solver.candidates.begin(),solver.candidates.end(),
        [&](const Candidate& c){ return c.row==excluded_row; }),solver.candidates.end());
    for (std::size_t i=0;i<solver.candidates.size();++i) {
        std::uint64_t bits=solver.candidates[i].arcs;
        while (bits) {
            const std::uint64_t bit=bits & -bits; bits^=bit;
            solver.by_edge[__builtin_ctzll(bit)].push_back(static_cast<int>(i));
        }
    }
    solver.found=false;
    solver.search(0,0,fixed_score);
    return solver.found;
}
}

int main(int argc,char** argv) {
    try {
        if (argc!=7) throw std::runtime_error("usage: BINARY INPUT.txt OUTPUT.json SEED MAX_STEPS SECONDS SCORE_BAND");
        const std::string input=argv[1],output=argv[2];
        const auto seed=static_cast<std::uint64_t>(std::stoull(argv[3]));
        const int max_steps=std::stoi(argv[4]),band=std::stoi(argv[6]);
        const double seconds=std::stod(argv[5]);
        if (max_steps<=0 || seconds<=0 || band<0) throw std::runtime_error("invalid bounds");
        std::ifstream in(input);
        if (!in) throw std::runtime_error("cannot read seed");
        Rows rows{};
        for (Row& row:rows) {
            unsigned mask=0;
            for (int& v:row) {
                if (!(in>>v) || v<0 || v>=N || (mask & (1U<<v))) throw std::runtime_error("invalid row");
                mask|=1U<<v;
            }
        }
        int extra=0; if (in>>extra) throw std::runtime_error("extra seed values");
        if (score(rows,1)!=0) throw std::runtime_error("seed not adjacency complete");
        const auto started=std::chrono::steady_clock::now();
        const auto deadline=started+std::chrono::duration_cast<std::chrono::steady_clock::duration>(std::chrono::duration<double>(seconds));
        std::mt19937_64 random(seed);
        std::set<State> seen; seen.insert(canonical(rows));
        Rows best_rows=rows;
        int best=score(rows,2), current_score=best, initial=best;
        std::vector<int> trace; trace.reserve(static_cast<std::size_t>(max_steps));
        std::uint64_t attempts=0,generated=0,cover_nodes=0;
        std::string status="step_limit";
        std::vector<std::array<int,4>> groups;
        for (int a=0;a<N-3;++a) for (int b=a+1;b<N-2;++b)
            for (int c=b+1;c<N-1;++c) for (int d=c+1;d<N;++d) groups.push_back({a,b,c,d});
        for (int step=0;step<max_steps;++step) {
            if (std::chrono::steady_clock::now()>=deadline) { status="time_limit"; break; }
            std::shuffle(groups.begin(),groups.end(),random);
            bool advanced=false,limit=false;
            Checker solver(rows,seconds);
            solver.deadline=deadline;
            solver.threshold=best+band+1; // strict < threshold means <= best+band
            for (const auto& group:groups) {
                std::array<int,4> indices={0,1,2,3};
                std::shuffle(indices.begin(),indices.end(),random);
                for (int excluded:indices) {
                    if (std::chrono::steady_clock::now()>=deadline) { limit=true; break; }
                    ++attempts;
                    if (attempt(solver,group,excluded)) {
                        if (seen.find(canonical(solver.counterexample))!=seen.end()) continue;
                        rows=solver.counterexample; current_score=solver.found_score;
                        if (score(rows,1)!=0 || score(rows,2)!=current_score)
                            throw std::logic_error("walk candidate counts mismatch");
                        seen.insert(canonical(rows));
                        trace.push_back(current_score);
                        if (current_score<best) { best=current_score; best_rows=rows; }
                        advanced=true; break;
                    }
                    if (solver.timed_out) { limit=true; break; }
                }
                if (advanced || limit) break;
            }
            generated+=solver.generated; cover_nodes+=solver.cover_nodes;
            if (best==0) { status="candidate_witness_requires_independent_check"; break; }
            if (!advanced) { status=limit?"time_limit":"no_unseen_candidate_in_attempted_groups"; break; }
        }
        int e1=0,e2=0;
        if (score(best_rows,1,&e1)!=0 || score(best_rows,2,&e2)!=best)
            throw std::logic_error("best table mismatch");
        const auto ms=std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now()-started).count();
        const int fd=open(output.c_str(),O_WRONLY|O_CREAT|O_EXCL,0600);
        if (fd<0) throw std::runtime_error("cannot exclusively create output");
        std::FILE* out=fdopen(fd,"w");
        if (!out) { close(fd); throw std::runtime_error("cannot open output stream"); }
        std::fprintf(out,"{\n  \"kind\": \"four_row_exact_cover_plateau_walk\",\n  \"input_rows_file\": \"%s\",\n  \"seed\": %llu,\n",input.c_str(),static_cast<unsigned long long>(seed));
        std::fprintf(out,"  \"status\": \"%s\",\n  \"elapsed_ms\": %lld,\n  \"steps_taken\": %zu,\n  \"distinct_states_seen\": %zu,\n",status.c_str(),static_cast<long long>(ms),trace.size(),seen.size());
        std::fprintf(out,"  \"group_exclusion_attempts\": %llu,\n  \"hamilton_paths_generated\": %llu,\n  \"exact_cover_nodes\": %llu,\n",static_cast<unsigned long long>(attempts),static_cast<unsigned long long>(generated),static_cast<unsigned long long>(cover_nodes));
        std::fprintf(out,"  \"initial_d2_pair_collisions\": %d,\n  \"best_pair_collision_score\": %d,\n  \"d1_pair_collisions\": 0,\n  \"d2_pair_collisions\": %d,\n",initial,best,best);
        std::fprintf(out,"  \"d1_excess_events\": %d,\n  \"d2_excess_events\": %d,\n  \"zero_score_claim\": %s,\n  \"score_trace\": [",e1,e2,best==0?"true":"false");
        for (std::size_t i=0;i<trace.size();++i) std::fprintf(out,"%s%d",i?", ":"",trace[i]);
        std::fprintf(out,"],\n  \"rows\": "); print_rows(out,best_rows);
        std::fprintf(out,",\n  \"scope\": \"Bounded heuristic four-row walk; failure does not prove nonexistence.\"\n}\n");
        if (std::fclose(out)!=0) throw std::runtime_error("output write failed");
        std::cout<<"status="<<status<<" steps="<<trace.size()<<" attempts="<<attempts
                 <<" generated="<<generated<<" cover_nodes="<<cover_nodes<<" initial="<<initial
                 <<" best="<<best<<" witness_claim="<<(best==0?"yes":"no")<<" elapsed_ms="<<ms<<'\n';
        return 0;
    } catch (const std::exception& ex) {
        std::cerr<<"error: "<<ex.what()<<'\n';
        return 1;
    }
}
