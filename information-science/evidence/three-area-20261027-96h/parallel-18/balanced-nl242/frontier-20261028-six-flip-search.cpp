// Exact 6-flip search using the necessary no-four-bad-points condition at peaks.
#define main frontier_six_base_main
#include "frontier-20261028-core-outer-search.cpp"
#undef main

namespace {
constexpr int WORDS_F=4,WORDS_X=8;
std::uint64_t bad_frequency[N][WORDS_F]{};
std::uint64_t bad_points[256][WORDS_X]{};
std::array<int,256> peaks{};
int peak_count=0;
using Mask=std::array<std::uint64_t,WORDS_X>;
Mask after(int last) {
    Mask out{};
    const int word=last/64, bit=last%64;
    if (bit<63) out[word]=~std::uint64_t{0}<<(bit+1);
    for (int w=word+1;w<WORDS_X;++w) out[w]=~std::uint64_t{0};
    return out;
}
bool nonempty(const Mask& m) { for (auto w:m) if (w) return true; return false; }
Mask extensions(const std::array<int,6>& q,int count) {
    Mask allowed=after(q[count-1]);
    for (int i=0;i<count-2&&nonempty(allowed);++i)
        for (int j=i+1;j<count-1&&nonempty(allowed);++j)
            for (int k=j+1;k<count&&nonempty(allowed);++k)
                for (int word=0;word<WORDS_F&&nonempty(allowed);++word) {
                    std::uint64_t common=bad_frequency[q[i]][word]&bad_frequency[q[j]][word]&bad_frequency[q[k]][word];
                    while (common&&nonempty(allowed)) {
                        const int index=word*64+__builtin_ctzll(common);
                        for (int w=0;w<WORDS_X;++w) allowed[w]&=~bad_points[index][w];
                        common&=common-1;
                    }
                }
    return allowed;
}
void initialize_peaks(const Table& f,const Table& w) {
    for (int a=0;a<N;++a) if (std::abs(w[a])==28) {
        if (peak_count>=256) throw std::runtime_error("peak capacity exceeded");
        const int p=peak_count++; peaks[p]=a;
        for (int x=0;x<N;++x) {
            const int product=(w[a]>0?1:-1)*(f[x]?-1:1)*(__builtin_parity(a&x)?-1:1);
            if (product<0) { bad_frequency[x][p/64]|=1ULL<<(p%64); bad_points[p][x/64]|=1ULL<<(x%64); }
        }
    }
    if (!peak_count) throw std::runtime_error("no source peaks");
}
int check(const Table& bits,const Table& w,const std::array<int,6>& q) {
    int zero=-1;
    for (int a=0;a<N;++a) {
        int value=w[a];
        for (int x:q) value-=2*(bits[x]?-1:1)*(__builtin_parity(a&x)?-1:1);
        if (std::abs(value)>28) return -1;
        if (value==0&&zero<0) zero=a;
    }
    return zero;
}
void write_hit(const std::string& name,const Table& input,const std::array<int,6>& q,int frequency,int seed) {
    require_unused(name); Table bits=input;
    for (int x:q) bits[x]^=1;
    for (int x=0;x<N;++x) bits[x]^=__builtin_parity(x&frequency);
    Table w{}; for (int x=0;x<N;++x) w[x]=1-2*bits[x]; fwht(w.data(),N);
    int peak=0; for (int v:w) peak=std::max(peak,std::abs(v));
    if (w[0]!=0||peak>28) throw std::runtime_error("candidate fails internal full transform");
    std::ofstream out(name); if (!out) throw std::runtime_error("cannot create candidate");
    out<<"{\n  \"format\":\"boolean-truth-v1\",\n  \"seed_index_1based\":"<<seed<<",\n  \"flips\":[";
    for (int i=0;i<6;++i) out<<(i?",":"")<<q[i];
    out<<"],\n  \"affine_twist_frequency\":"<<frequency<<",\n  \"bits\":\"";
    for (int b:bits) out<<b; out<<"\"\n}\n";
    if (!out) throw std::runtime_error("candidate write failed");
}
}
int main(int argc,char** argv) {
    try {
        if (argc!=7) throw std::runtime_error("usage: six-flip SEEDS SEED_INDEX FIRST_START FIRST_END MAX_SECONDS OUTPUT_PREFIX");
        const int index=std::stoi(argv[2]),first=std::stoi(argv[3]),last=std::stoi(argv[4]),seconds=std::stoi(argv[5]);
        const std::string base=argv[6],receipt=base+"-result.json",candidate=base+"-candidate.json";
        if (index<1||index>3||first<0||first>=last||last>N-5||seconds<1||seconds>300) throw std::runtime_error("invalid bounds");
        require_unused(receipt); require_unused(candidate);
        const auto seeds=load_seeds(argv[1]); const Table bits=seeds.at(index-1); Table w{};
        for (int x=0;x<N;++x) w[x]=1-2*bits[x]; fwht(w.data(),N);
        int maxpeak=0; for (int v:w) maxpeak=std::max(maxpeak,std::abs(v));
        if (maxpeak!=28) throw std::runtime_error("unexpected source peak");
        initialize_peaks(bits,w);
        const auto start=std::chrono::steady_clock::now();
        std::array<int,6> q{},hit{}; long long triples=0,quads=0,fives=0,sixes=0;
        int hit_frequency=-1; bool stopped=false,timed_out=false; int fully_processed_first=first-1;
        for (q[0]=first;q[0]<last&&!stopped;++q[0]) {
            for (q[1]=q[0]+1;q[1]<N-4&&!stopped;++q[1])
              for (q[2]=q[1]+1;q[2]<N-3&&!stopped;++q[2]) {
                ++triples; Mask l=extensions(q,3);
                for (int wl=0;wl<WORDS_X&&!stopped;++wl) while (l[wl]&&!stopped) {
                    q[3]=wl*64+__builtin_ctzll(l[wl]); l[wl]&=l[wl]-1;
                    if (q[3]>=N-2) continue;
                    ++quads; Mask m=extensions(q,4);
                    for (int wm=0;wm<WORDS_X&&!stopped;++wm) while (m[wm]&&!stopped) {
                        q[4]=wm*64+__builtin_ctzll(m[wm]); m[wm]&=m[wm]-1;
                        if (q[4]>=N-1) continue;
                        ++fives; Mask n=extensions(q,5);
                        for (int wn=0;wn<WORDS_X&&!stopped;++wn) while (n[wn]&&!stopped) {
                            q[5]=wn*64+__builtin_ctzll(n[wn]); n[wn]&=n[wn]-1; ++sixes;
                            const int a=check(bits,w,q);
                            if (a>=0) { hit=q; hit_frequency=a; stopped=true; break; }
                            if ((sixes&8191)==0&&std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>=seconds) { stopped=true; timed_out=true; }
                        }
                    }
                }
                if (triples%1000000==0) std::cout<<"triples="<<triples<<" quads="<<quads<<" fives="<<fives<<" sixes="<<sixes<<std::endl;
                if ((triples&4095)==0&&std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>=seconds) { stopped=true; timed_out=true; }
              }
            if (!stopped) fully_processed_first=q[0];
        }
        if (hit_frequency>=0) write_hit(candidate,bits,hit,hit_frequency,index);
        const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
        std::ofstream out(receipt); if (!out) throw std::runtime_error("cannot write receipt");
        out<<"{\n  \"seed_index_1based\":"<<index<<",\n  \"first_start\":"<<first<<",\n  \"first_end_exclusive\":"<<last
           <<",\n  \"peaks\":"<<peak_count<<",\n  \"triples\":"<<triples<<",\n  \"compatible_quads\":"<<quads
           <<",\n  \"compatible_fives\":"<<fives<<",\n  \"compatible_sixes_checked\":"<<sixes
           <<",\n  \"fully_processed_first\":"<<fully_processed_first<<",\n  \"complete_range\":"<<(!stopped?"true":"false")
           <<",\n  \"timed_out\":"<<(timed_out?"true":"false")<<",\n  \"target_met\":"<<(hit_frequency>=0?"true":"false")
           <<",\n  \"elapsed_seconds\":"<<elapsed<<"\n}\n";
        if (!out) throw std::runtime_error("receipt write failed");
        std::cout<<"triples="<<triples<<" quads="<<quads<<" fives="<<fives<<" sixes="<<sixes<<" complete="<<(!stopped)<<" target="<<(hit_frequency>=0)<<" elapsed="<<elapsed<<"s\n";
        return 0;
    } catch (const std::exception& e) { std::cerr<<"error: "<<e.what()<<'\n'; return 1; }
}
