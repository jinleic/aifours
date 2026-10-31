// Exhaustive projective F_7 search for rank-one contractions with mixed C.
// This is a finite-field diagnostic, not a proof or counterexample over C.
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
#include <fcntl.h>
#include <unistd.h>

using Vec = std::array<int,6>;
struct Cell { int n=0; std::array<int,6> b{}, coeff{}; };
static int mod(int x) { x%=7; return x<0 ? x+7 : x; }
static bool hmixed(const Vec& x) { return (x[1]||x[2]) && (x[0]||x[3]||x[4]||x[5]); }
static int value(const Cell& c,const Vec& u) {
    int x=0;
    for(int q=0;q<c.n;++q) x+=c.coeff[q]*u[c.b[q]];
    return x%7;
}
static bool rank_at_most_one(const std::array<Cell,36>& cs,const Vec& u) {
    const int a=value(cs[0],u),b=value(cs[1],u),c=value(cs[6],u),d=value(cs[7],u);
    if(mod(a*d-b*c)) return false;
    // For the non-generic zero-pivot case the full scan supplies the first pivot.
    std::array<int,36> m{}; m[0]=a;m[1]=b;m[6]=c;m[7]=d;
    for(int k=0;k<36;++k) if(k!=0 && k!=1 && k!=6 && k!=7) m[k]=value(cs[k],u);
    int pivot=0; while(pivot<36 && !m[pivot]) ++pivot;
    if(pivot==36) return true;
    const int i=pivot/6,j=pivot%6,p=m[pivot];
    for(int r=0;r<6;++r) if(r!=i)
        for(int s=0;s<6;++s) if(s!=j)
            if(mod(p*m[6*r+s]-m[6*r+j]*m[6*i+s])) return false;
    return true;
}
static std::vector<Vec> projective_vectors() {
    std::vector<Vec> out;out.reserve(19608);
    for(int first=0;first<6;++first) {
        int count=1;for(int k=first+1;k<6;++k) count*=7;
        for(int code=0;code<count;++code) {
            Vec x{};x[first]=1;int n=code;
            for(int k=first+1;k<6;++k) {x[k]=n%7;n/=7;}
            out.push_back(x);
        }
    }
    if(out.size()!=19608) throw std::runtime_error("projective vector count");
    return out;
}
static std::string vecstr(const Vec& x) {
    std::ostringstream o;o<<'[';for(int k=0;k<6;++k){if(k)o<<',';o<<x[k];}o<<']';return o.str();
}
int main(int argc,char**argv) {
  try {
    if(argc!=5) throw std::runtime_error("usage: table C B output.json");
    const int C=std::stoi(argv[2]),B=std::stoi(argv[3]);
    if(C<0||C>=4||B<0||B>=4||C==B) throw std::runtime_error("bad party pair");
    std::array<int,2> rem{};int nr=0;for(int j=0;j<4;++j)if(j!=C&&j!=B)rem[nr++]=j;
    const int A=rem[0],D=rem[1];
    int T[6][6][6][6]{};int terms=0;std::ifstream in(argv[1]);std::string line;
    if(!in) throw std::runtime_error("cannot open table");
    while(std::getline(in,line)) {
        if(line.empty()||line[0]=='#')continue;
        std::istringstream ss(line);int x,y;ss>>x>>y;std::string tok;
        while(ss>>tok) {
            if(tok.size()!=3) throw std::runtime_error("bad table token");
            int coeff=(tok[0]=='s'?3:tok[0]=='+'?1:tok[0]=='-'?6:0);
            if(!coeff)throw std::runtime_error("bad coefficient");
            std::array<int,4> q{x,y,tok[1]-'0',tok[2]-'0'};
            for(auto z:q)if(z<0||z>=6)throw std::runtime_error("bad level");
            int &cell=T[q[C]][q[B]][q[A]][q[D]];
            if(cell)throw std::runtime_error("duplicate source term");cell=coeff;++terms;
        }
    }
    if(terms!=60)throw std::runtime_error("wrong source support");
    const auto all=projective_vectors();std::uint64_t examined=0,mixed_v=0;bool found=false;Vec fv{},fu{};
    for(const Vec& v:all) {
        if(!hmixed(v))continue;++mixed_v;
        std::array<Cell,36> cells{};
        for(int a=0;a<6;++a)for(int d=0;d<6;++d)for(int b=0;b<6;++b) {
            int x=0;for(int c=0;c<6;++c)x+=T[c][b][a][d]*v[c];x=mod(x);
            if(x) {auto& e=cells[6*a+d];e.b[e.n]=b;e.coeff[e.n]=x;++e.n;}
        }
        for(const Vec& u:all) {
            ++examined;
            if(rank_at_most_one(cells,u)) {found=true;fv=v;fu=u;break;}
        }
        if(found)break;
    }
    std::ostringstream report;
    report<<"{\n  \"field\": 7,\n  \"sqrt2\": 3,\n  \"C\": "<<C<<",\n  \"B\": "<<B<<",\n"
          <<"  \"A\": "<<A<<",\n  \"D\": "<<D<<",\n  \"projective_vectors\": "<<all.size()<<",\n"
          <<"  \"mixed_C_vectors_examined\": "<<mixed_v<<",\n  \"pairs_examined\": "<<examined<<",\n"
          <<"  \"rank_at_most_one_found\": "<<(found?"true":"false")<<",\n";
    if(found)report<<"  \"mixed_C_vector\": "<<vecstr(fv)<<",\n  \"B_vector\": "<<vecstr(fu)<<",\n";
    report<<"  \"scope\": \"One orientation, exact projective F7 diagnostic; not an implication over C.\"\n}\n";
    int fd=open(argv[4],O_WRONLY|O_CREAT|O_EXCL,0644);if(fd<0)throw std::runtime_error("output exists or cannot create");
    const std::string result=report.str();if(write(fd,result.data(),result.size())!=static_cast<ssize_t>(result.size()))throw std::runtime_error("output write failed");
    if(close(fd))throw std::runtime_error("output close failed");std::cout<<result;
    return 0;
  } catch(const std::exception& e) {std::cerr<<"ERROR: "<<e.what()<<'\n';return 1;}
}
