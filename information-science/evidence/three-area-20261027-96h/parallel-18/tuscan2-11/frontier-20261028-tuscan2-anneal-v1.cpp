// Simulated annealing for actual linear Tuscan-2(n) arrays (n <= 16).
// State: n permutation rows. Cost = W1*excess(D1) + W2*excess(D2), excess =
// sum over ordered pairs of max(0,count-1). Moves inside one row: swap,
// segment reversal, insertion. Cost zero means every D1/D2 pair occurs at
// most once; independent checking is still required. A failure says nothing.
// Build: clang++ -std=c++17 -O3 -Wall -Wextra SOURCE -o BINARY
// Run: BINARY N SEED SECONDS W1 W2 T0 COOL OUTPUT.json
#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <fcntl.h>
#include <iostream>
#include <random>
#include <stdexcept>
#include <string>
#include <unistd.h>
#include <vector>

namespace {
constexpr int MAXN=16;
struct State {
    int n=0;
    std::vector<std::array<int,MAXN>> rows;
    int c1[MAXN][MAXN]{}, c2[MAXN][MAXN]{};
    long long e1=0,e2=0;
};

inline long long add_event(int (&c)[MAXN][MAXN],int a,int b,int delta) {
    // returns change of excess
    const int before=c[a][b];
    c[a][b]+=delta;
    const int after=c[a][b];
    return static_cast<long long>(std::max(0,after-1))-std::max(0,before-1);
}

void row_events(State& s,int r,int sign) {
    auto& x=s.rows[r];
    for (int i=0;i+1<s.n;++i) s.e1+=add_event(s.c1,x[i],x[i+1],sign);
    for (int i=0;i+2<s.n;++i) s.e2+=add_event(s.c2,x[i],x[i+2],sign);
}

void print_rows(std::FILE* out,const State& s) {
    std::fprintf(out,"[\n");
    for (int r=0;r<s.n;++r) {
        std::fprintf(out,"    [");
        for (int i=0;i<s.n;++i) std::fprintf(out,"%s%d",i?", ":"",s.rows[r][i]);
        std::fprintf(out,"]%s\n",r+1==s.n?"":",");
    }
    std::fprintf(out,"  ]");
}
} // namespace

int main(int argc,char** argv) {
    try {
        if (argc!=9) throw std::runtime_error("usage: BINARY N SEED SECONDS W1 W2 T0 COOL OUTPUT.json");
        const int n=std::stoi(argv[1]);
        const auto seed=static_cast<std::uint64_t>(std::stoull(argv[2]));
        const double seconds=std::stod(argv[3]);
        const double w1=std::stod(argv[4]),w2=std::stod(argv[5]),t0=std::stod(argv[6]),cool=std::stod(argv[7]);
        const std::string output=argv[8];
        if (n<3 || n>MAXN || seconds<=0 || w1<=0 || w2<=0 || t0<=0 || cool<=0 || cool>=1)
            throw std::runtime_error("invalid parameters");
        std::mt19937_64 rng(seed);
        std::uniform_real_distribution<double> unif(0.0,1.0);
        State s; s.n=n; s.rows.resize(n);
        for (int r=0;r<n;++r) {
            for (int i=0;i<n;++i) s.rows[r][i]=i;
            std::shuffle(s.rows[r].begin(),s.rows[r].begin()+n,rng);
            row_events(s,r,+1);
        }
        State best=s;
        double best_cost=w1*s.e1+w2*s.e2, temp=t0;
        const auto start=std::chrono::steady_clock::now();
        const auto deadline=start+std::chrono::duration_cast<std::chrono::steady_clock::duration>(std::chrono::duration<double>(seconds));
        std::uint64_t moves=0,accepted=0,restarts=0,since_improve=0;
        std::array<int,MAXN> saved{};
        while (true) {
            if ((moves&8191U)==0) {
                if (std::chrono::steady_clock::now()>=deadline) break;
            }
            ++moves;
            const int r=static_cast<int>(rng()%n);
            int i=static_cast<int>(rng()%n), j=static_cast<int>(rng()%n);
            if (i==j) continue;
            if (i>j) std::swap(i,j);
            const int type=static_cast<int>(rng()%3);
            const double old_cost=w1*s.e1+w2*s.e2;
            saved=s.rows[r];
            row_events(s,r,-1);
            auto& x=s.rows[r];
            if (type==0) std::swap(x[i],x[j]);
            else if (type==1) std::reverse(x.begin()+i,x.begin()+j+1);
            else {
                if (rng()&1) { const int v=x[i]; for (int k=i;k<j;++k) x[k]=x[k+1]; x[j]=v; }
                else { const int v=x[j]; for (int k=j;k>i;--k) x[k]=x[k-1]; x[i]=v; }
            }
            row_events(s,r,+1);
            const double new_cost=w1*s.e1+w2*s.e2;
            const double delta=new_cost-old_cost;
            if (delta<=0 || unif(rng)<std::exp(-delta/temp)) {
                ++accepted;
                if (new_cost<best_cost) { best_cost=new_cost; best=s; since_improve=0; if (best_cost==0) break; }
            } else {
                row_events(s,r,-1); s.rows[r]=saved; row_events(s,r,+1);
            }
            temp*=cool;
            if (temp<1e-3) temp=1e-3;
            if (++since_improve>20000000ULL) { temp=t0; since_improve=0; ++restarts; }
        }
        const auto ms=std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now()-start).count();
        const int fd=open(output.c_str(),O_WRONLY|O_CREAT|O_EXCL,0600);
        if (fd<0) throw std::runtime_error("cannot exclusively create output");
        std::FILE* out=fdopen(fd,"w"); if (!out) { close(fd); throw std::runtime_error("cannot open stream"); }
        std::fprintf(out,"{\n  \"kind\": \"tuscan2_simulated_annealing\",\n  \"n\": %d,\n  \"seed\": %llu,\n  \"seconds\": %.3f,\n",n,static_cast<unsigned long long>(seed),seconds);
        std::fprintf(out,"  \"weights\": [%.6g, %.6g],\n  \"t0\": %.6g,\n  \"cool\": %.10g,\n  \"moves\": %llu,\n  \"accepted\": %llu,\n  \"reheats\": %llu,\n",w1,w2,t0,cool,static_cast<unsigned long long>(moves),static_cast<unsigned long long>(accepted),static_cast<unsigned long long>(restarts));
        std::fprintf(out,"  \"best_d1_excess\": %lld,\n  \"best_d2_excess\": %lld,\n  \"zero_score_claim\": %s,\n  \"elapsed_ms\": %lld,\n  \"rows\": ",best.e1,best.e2,(best.e1==0&&best.e2==0)?"true":"false",static_cast<long long>(ms));
        print_rows(out,best);
        std::fprintf(out,",\n  \"scope\": \"Heuristic search; no nonexistence inference from failure.\"\n}\n");
        if (std::fclose(out)!=0) throw std::runtime_error("output failed");
        std::cout<<"n="<<n<<" best_d1_excess="<<best.e1<<" best_d2_excess="<<best.e2<<" moves="<<moves<<" reheats="<<restarts<<" elapsed_ms="<<ms<<'\n';
        return 0;
    } catch (const std::exception& e) { std::cerr<<"error: "<<e.what()<<'\n'; return 1; }
}
