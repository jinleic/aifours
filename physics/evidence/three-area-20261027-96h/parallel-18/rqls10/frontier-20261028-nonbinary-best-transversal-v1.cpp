#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
#include <limits>
using namespace std;
static double w[10][10][10],best;static int permu[10],bestperm[10],bestcase;static long long nodes;
static void dfs(int r,int used,double cost){
 ++nodes;if(cost>=best)return;
 if(r==10){best=cost;for(int i=0;i<10;i++)bestperm[i]=permu[i];return;}
 for(int c=1;c<10;c++)if(!(used&(1<<c))){
  double x=cost;for(int s=0;s<r;s++)x+=w[r-s][permu[s]][c];
  if(x<best){permu[r]=c;dfs(r+1,used|(1<<c),x);}
 }
}
int main(){
 ifstream in("frontier-20261028-q18-nonbinary-matrices-v1.txt");int H[10][10];
 double global=numeric_limits<double>::infinity();int globalperm[10];bestcase=-1;
 const double PI=acos(-1.0);
 for(int i=0;i<24;i++){
  for(int t=0;t<10;t++)for(int c=0;c<10;c++)if(!(in>>H[t][c]))return 2;
  for(int k=1;k<10;k++)for(int c=0;c<10;c++)for(int d=0;d<10;d++){
   double a=0,b=0;for(int t=0;t<10;t++){
    double th=2*PI*(9*k*t+5*(H[t][d]-H[t][c]))/90.;a+=cos(th);b+=sin(th);
   }w[k][c][d]=(a*a+b*b)/100.;
  }
  best=numeric_limits<double>::infinity();nodes=0;permu[0]=0;dfs(1,1,0.);
  cout.precision(15);cout<<"case="<<i<<" score="<<best<<" nodes="<<nodes<<"\n";
  if(best<global){global=best;bestcase=i;for(int r=0;r<10;r++)globalperm[r]=bestperm[r];}
 }
 ofstream out("frontier-20261028-nonbinary-best-transversal-v1.json");out.precision(17);
 out<<"{\"case_0based\":"<<bestcase<<",\"sum_squared_pairwise_overlap\":"<<global<<",\"columns_by_row\":[";
 for(int r=0;r<10;r++)out<<(r?",":"")<<globalperm[r];out<<"],\"scope\":\"floating discrete ranking, not proof or witness\"}\n";
 cout<<"best case="<<bestcase<<" score="<<global<<" permutation=";for(int r=0;r<10;r++)cout<<globalperm[r]<<" ";cout<<"\n";
}
