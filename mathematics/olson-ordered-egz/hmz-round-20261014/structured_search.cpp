// Bounded counterexample assay. Counts products in the original index order.
// A positive count is a search miss, not a proof for any group.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>
using namespace std;
using Table = vector<vector<int>>;

Table dicyclic(int m) {
    int q = 2*m;
    Table t(2*q, vector<int>(2*q));
    // r^a s^b, b=0,1; s^2=r^m and s r s^-1=r^-1.
    for (int a=0; a<2*q; ++a) for (int b=0; b<2*q; ++b) {
        int x = (a%q + (a/q ? -(b%q) : b%q) + (a/q && b/q ? m : 0)) % q;
        if (x<0) x+=q;
        t[a][b]=x+q*((a/q+b/q)%2);
    }
    return t;
}
Table dihedral(int m) {
    Table t(2*m, vector<int>(2*m));
    for (int a=0; a<2*m; ++a) for (int b=0; b<2*m; ++b)
        t[a][b]=((a%m+(a/m ? m-b%m : b%m))%m)+m*((a/m+b/m)%2);
    return t;
}
Table alternating4() {
    vector<array<int,4>> p;
    array<int,4> x{0,1,2,3};
    do {
        int inv=0;
        for (int i=0;i<4;++i) for(int j=i+1;j<4;++j) inv+=x[i]>x[j];
        if (!(inv%2)) p.push_back(x);
    } while (next_permutation(x.begin(),x.end()));
    Table t(p.size(),vector<int>(p.size()));
    for(int a=0;a<(int)p.size();++a) for(int b=0;b<(int)p.size();++b) {
        array<int,4> c;
        for(int i=0;i<4;++i)c[i]=p[a][p[b][i]];
        t[a][b]=find(p.begin(),p.end(),c)-p.begin();
    }
    return t;
}
void validate(const Table& t) {
    int n=t.size();
    for(int a=0;a<n;++a) {
        if(t[0][a]!=a || t[a][0]!=a) throw runtime_error("identity");
        bool inv=false;
        for(int b=0;b<n;++b) {
            if(t[a][b]==0 && t[b][a]==0) inv=true;
            if(t[a][b]<0 || t[a][b]>=n) throw runtime_error("closure");
            for(int c=0;c<n;++c)
                if(t[t[a][b]][c]!=t[a][t[b][c]]) throw runtime_error("associativity");
        }
        if(!inv) throw runtime_error("inverse");
    }
}
uint64_t count_identity(const Table& t,const vector<int>& s) {
    int n=t.size();
    uint64_t dp[15][14]{};
    dp[0][0]=1;
    int used=0;
    for(int a:s) {
        ++used;
        for(int k=min(n,used);k>0;--k) for(int g=0;g<n;++g)
            dp[k][t[g][a]]+=dp[k-1][g];
    }
    return dp[n][0];
}
void save(const string& name,const Table& t,const vector<int>& s,uint64_t count,
          uint64_t seed,uint64_t trials,const string& status) {
    ofstream f(name+"-search-best.json");
    f << "{\"status\":\""<<status<<"\",\"identity\":0,\"group\":\""<<name
      <<"\",\"identity_subset_count\":"<<count<<",\"seed\":"<<seed
      <<",\"evaluations\":"<<trials<<",\"table\":[";
    for(int a=0;a<(int)t.size();++a){if(a)f<<",";f<<"[";
        for(int b=0;b<(int)t.size();++b){if(b)f<<",";f<<t[a][b];}f<<"]";}
    f<<"],\"sequence\":[";
    for(int i=0;i<(int)s.size();++i){if(i)f<<",";f<<s[i];}
    f<<"]}\n";
}
int main(int argc,char**argv) {
    string name=argc>1?argv[1]:"Dic3";
    int seconds=argc>2?stoi(argv[2]):60;
    uint64_t seed=argc>3?stoull(argv[3]):20261014;
    auto t=name=="Dic3"?dicyclic(3):name=="D7"?dihedral(7):alternating4();
    validate(t);
    int n=t.size(),L=2*n-1;
    mt19937_64 rng(seed);
    vector<int> best(L),s(L),candidate;
    uint64_t bestcount=UINT64_MAX,trials=0,trivial=0;
    auto consider=[&](const vector<int>& w){
        int multiplicity[14]{};
        for(int a:w) if(++multiplicity[a]>=n) {++trivial;return uint64_t(1)<<60;}
        auto c=count_identity(t,w);++trials;
        if(c<bestcount) {
            bestcount=c;best=w;
            cout<<"best "<<name<<" count="<<c<<" evaluations="<<trials<<" sequence=";
            for(int a:w)cout<<a<<",";cout<<endl;
            save(name,t,best,bestcount,seed,trials,c?"search_miss":"candidate_requires_independent_verification");
        }
        return c;
    };
    // Every one-letter insertion into the two-block, one-short construction.
    // Also try every ordered generator pair, not just the presentation pair.
    for(int a=0;a<n && bestcount;++a) for(int b=0;b<n && bestcount;++b) if(a!=b)
        for(int c=0;c<n && bestcount;++c) for(int pos=0;pos<L && bestcount;++pos) {
            vector<int>w(n-1,a);w.insert(w.end(),n-1,b);w.insert(w.begin()+pos,c);
            consider(w);
        }
    cout<<"insertions_complete "<<name<<" evaluations="<<trials<<" trivial="<<trivial<<" best="<<bestcount<<endl;
    auto start=chrono::steady_clock::now();
    uint64_t restarts=0;
    while(bestcount && chrono::duration<double>(chrono::steady_clock::now()-start).count()<seconds) {
        if(restarts%3==0) s=best;
        else if(restarts%3==1) {
            // Three or four constant runs focus on delayed mixing of cosets.
            int runs=3+rng()%2;
            vector<int> cuts{0,L};
            while((int)cuts.size()<runs+1){int v=1+rng()%(L-1);if(find(cuts.begin(),cuts.end(),v)==cuts.end())cuts.push_back(v);}
            sort(cuts.begin(),cuts.end());
            for(int j=0;j<runs;++j)fill(s.begin()+cuts[j],s.begin()+cuts[j+1],rng()%n);
        } else for(int& a:s)a=rng()%n;
        auto score=consider(s);
        for(int iteration=0;iteration<6000 && bestcount;++iteration) {
            candidate=s;
            int op=rng()%10,i=rng()%L,j=rng()%L;
            if(i>j)swap(i,j);
            if(op<6)candidate[i]=rng()%n;
            else if(op<8)swap(candidate[i],candidate[j]);
            else if(op==8)reverse(candidate.begin()+i,candidate.begin()+j+1);
            else fill(candidate.begin()+i,candidate.begin()+j+1,rng()%n);
            auto next=consider(candidate);
            // Exact integral objective; occasional uphill steps escape local minima.
            bool accept=next<=score;
            if(!accept && rng()%1000<2 && next-score<=max<uint64_t>(1,score/8))accept=true;
            if(accept){s.swap(candidate);score=next;}
            if(iteration%128==0 && chrono::duration<double>(chrono::steady_clock::now()-start).count()>=seconds)break;
        }
        ++restarts;
    }
    save(name,t,best,bestcount,seed,trials,bestcount?"search_miss":"candidate_requires_independent_verification");
    cout<<"finished "<<name<<" evaluations="<<trials<<" trivial="<<trivial<<" restarts="<<restarts<<" best="<<bestcount
        <<" elapsed="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<endl;
    return 0;
}
