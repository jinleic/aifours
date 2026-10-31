// Independent exact maximal-pair common-transversal enumerator.
// One 8! column permutation per candidate; no DP/producer code is imported.
#include <algorithm>
#include <array>
#include <chrono>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

using Square = std::array<std::array<int,8>,8>;

static unsigned mul(unsigned a,unsigned b) {
  unsigned out=0;
  for (int k=0;k<3;++k) { if(b&1) out^=a; b>>=1; a<<=1; if(a&8) a^=11; }
  return out;
}
static bool latin(const Square& S) {
  for(int i=0;i<8;++i) {
    unsigned row=0,col=0;
    for(int j=0;j<8;++j) { row|=1u<<S[i][j]; col|=1u<<S[j][i]; }
    if(row!=255 || col!=255) return false;
  }
  return true;
}
static bool orth(const Square& A,const Square& B) {
  std::array<bool,64> seen{};
  for(int i=0;i<8;++i) for(int j=0;j<8;++j) {
    int x=8*A[i][j]+B[i][j]; if(seen[x])return false; seen[x]=true;
  }
  return true;
}
static int count(const Square& A,const Square& B,long long& tested) {
  std::array<int,8> p{0,1,2,3,4,5,6,7};int result=0;tested=0;
  do {
    ++tested;unsigned x=0,y=0;bool valid=true;
    for(int i=0;i<8;++i) {
      unsigned a=1u<<A[i][p[i]],b=1u<<B[i][p[i]];
      if((x&a)||(y&b)){valid=false;break;}x|=a;y|=b;
    }
    result+=valid;
  } while(std::next_permutation(p.begin(),p.end()));
  return result;
}
int main(int argc,char**argv) {
  if(argc!=3){std::cerr<<"usage: source output\n";return 2;}
  std::ifstream in(argv[1]); if(!in){std::cerr<<"source open\n";return 2;}
  std::string header;std::getline(in,header);std::istringstream hs(header);int r,c,n;
  if(!(hs>>r>>c>>n)||r!=8||c!=8||n!=4254){std::cerr<<"header\n";return 2;}
  std::ifstream existing(argv[2]); if(existing.good()){std::cerr<<"output exists\n";return 2;}
  std::ofstream out(argv[2]);if(!out){std::cerr<<"output open\n";return 2;}
  out<<"index,common_transversals,permutations_tested\n";
  Square C{},D{};
  for(int i=0;i<8;++i)for(int j=0;j<8;++j){C[i][j]=i^j;D[i][j]=j^static_cast<int>(mul(2,i));}
  long long tests=0; if(!latin(C)||!latin(D)||!orth(C,D)||count(C,D,tests)<8||tests!=40320){std::cerr<<"positive affine control\n";return 2;}
  auto start=std::chrono::steady_clock::now();
  for(int k=0;k<2127;++k){
    if(std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>25.0){std::cerr<<"time bound at "<<k<<"\n";return 3;}
    Square A{},B{};std::string row;
    for(int q=0;q<2;++q)for(int i=0;i<8;++i){
      if(!(in>>row)||row.size()!=8){std::cerr<<"source row\n";return 2;}
      for(int j=0;j<8;++j){if(row[j]<'a'||row[j]>'h'){std::cerr<<"symbol\n";return 2;} (q?B:A)[i][j]=row[j]-'a';}
    }
    if(!latin(A)||!latin(B)||!orth(A,B)){std::cerr<<"invalid pair "<<k<<"\n";return 2;}
    int v=count(A,B,tests);if(tests!=40320){std::cerr<<"permutation count\n";return 2;}
    out<<k<<","<<v<<","<<tests<<"\n";
    if(!out){std::cerr<<"write failed\n";return 2;}
  }
  std::string extra;if(in>>extra){std::cerr<<"extra source row\n";return 2;}
  out.close();if(!out){std::cerr<<"close failed\n";return 2;}
  std::cout<<"COMPLETE 2127 pairs 40320 permutations each; affine control PASS\n";
  return 0;
}
