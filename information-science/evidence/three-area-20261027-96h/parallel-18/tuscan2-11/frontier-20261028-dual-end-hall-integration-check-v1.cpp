// Check the actual end-labelled dual Hall pruning against the independently
// verified reversed six-row separator, where start-labelled matching passes.
// Run: BINARY SOURCE_ROWS.txt ADDED_ROWS.txt OUTPUT.json
#define main three_anchor_solver_included_main
#include "frontier-20261028-three-anchor-exact-v7.cpp"
#undef main

int main(int argc,char** argv) {
    try {
        if (argc!=4) throw std::runtime_error("usage: BINARY SOURCE_ROWS.txt ADDED_ROWS.txt OUTPUT.json");
        std::ifstream source(argv[1]),added(argv[2]);
        if (!source || !added) throw std::runtime_error("cannot read rows");
        Rows original{};std::array<Row,3> extra{};
        for (auto& row:original) for (int& x:row) if (!(source>>x)) throw std::runtime_error("bad source");
        for (auto& row:extra) for (int& x:row) if (!(added>>x)) throw std::runtime_error("bad added rows");
        int value=0;if (source>>value || added>>value) throw std::runtime_error("extra data");
        Solver solver(original,{2,4,9},2026102825,10);
        if (!solver.prepare()) throw std::logic_error("fixed rows incompatible");
        solver.generate(0,0);
        if (solver.timed_out || solver.row_cap) throw std::runtime_error("generation incomplete");
        solver.build_features();
        if (solver.timed_out) throw std::runtime_error("feature build incomplete");
        Bits d1=solver.required,d2=solver.fixed2;
        unsigned starts=((1U<<N)-1)&~solver.starts,ends=((1U<<N)-1)&~solver.ends;
        for (int depth=0;depth<3;++depth) {
            const auto it=std::find_if(solver.candidates.begin(),solver.candidates.end(),
                [&](const Candidate& c){return c.row==extra[depth];});
            if (it==solver.candidates.end()) throw std::logic_error("continuation row not eligible");
            const std::size_t index=static_cast<std::size_t>(it-solver.candidates.begin());
            if (!(solver.allowed[depth][index/64] & (std::uint64_t{1}<<(index%64))))
                throw std::logic_error("continuation row conflicts with earlier rows");
            solver.choice[depth]=static_cast<int>(index);
            for (std::size_t w=0;w<solver.words;++w) {
                std::uint64_t remaining=solver.allowed[depth][w];
                for (int f:it->features) remaining&=~solver.feature_bits[static_cast<std::size_t>(f)*solver.words+w];
                solver.allowed[depth+1][w]=remaining;
            }
            d1={d1.lo^it->adj.lo,d1.hi^it->adj.hi};d2={d2.lo|it->far.lo,d2.hi|it->far.hi};
            starts^=1U<<it->row[0];ends^=1U<<it->row[N-1];
        }
        if (!solver.endpoint_matching_possible(starts,ends,3)) throw std::logic_error("endpoint matching unexpectedly fails");
        int available2=0;
        for (int a=0;a<N;++a) for (int b=0;b<N;++b) if (a!=b && !get(d2,a*N+b)) {
            const std::size_t offset=static_cast<std::size_t>(E+a*N+b)*solver.words;
            for (std::size_t w=0;w<solver.words;++w)
                if (solver.feature_bits[offset+w]&solver.allowed[3][w]) { ++available2;break; }
        }
        if (available2<45) throw std::logic_error("D2 aggregate unexpectedly fails");
        if (!solver.outgoing_matching_possible(d1,starts,3,false))
            throw std::logic_error("start-labelled dual Hall unexpectedly fails");
        if (solver.outgoing_matching_possible(d1,ends,3,true))
            throw std::logic_error("end-labelled dual Hall unexpectedly passes");
        if (solver.cover(d1,d2,starts,ends,3) || solver.dual_end_hall_prunes!=1)
            throw std::logic_error("cover did not prune by end-labelled dual Hall");
        const int fd=open(argv[3],O_WRONLY|O_CREAT|O_EXCL,0600);
        if (fd<0) throw std::runtime_error("cannot exclusively create output");
        std::FILE* out=fdopen(fd,"w");if (!out) { close(fd);throw std::runtime_error("cannot open stream"); }
        std::fprintf(out,"{\n  \"root_eligible_rows\": %zu,\n  \"selected_continuation_rows\": 3,\n  \"endpoint_matching_passes\": true,\n  \"unused_d2_support\": %d,\n  \"required_unused_d2_events\": 45,\n  \"outgoing_start_matching_passes\": true,\n  \"outgoing_end_matching_passes\": false,\n  \"cover_dual_end_hall_prunes\": %llu,\n  \"scope\": \"Only the separately checked reversed six-row instance; not a global result.\"\n}\n",solver.candidates.size(),available2,static_cast<unsigned long long>(solver.dual_end_hall_prunes));
        if (std::fclose(out)!=0) throw std::runtime_error("output write failed");
        std::cout<<"endpoint_pass=1 d2_support="<<available2<<" dual_start_pass=1 dual_end_pass=0 cover_end_prunes="<<solver.dual_end_hall_prunes<<'\n';
        return 0;
    } catch (const std::exception& ex) { std::cerr<<"error: "<<ex.what()<<'\n';return 1; }
}
