// Exact five-reflection-block extension in D_7 or Dic_3; not a full proof.
// Cyclic rotation preserves ordered identity-sublist existence. Move the
// initial rotations to the end: (r^v0 s)^b0 r^a0 ... (r^v4 s)^b4 r^a4.
// sum a=R, sum b=2n-1-R, a>=0, b>=1. Normalize v0=0.
// R>=n is trivial. R<=n-5 is excluded by even capacity and parity.
// Cyclic shifts of (b,v), followed by offset normalization, give a second
// symmetry reduction independent of the enumerated rotation gaps a.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <vector>
using namespace std;
using Mask=uint16_t;
int main(int argc,char** argv) {
    string name=argc>1?argv[1]:"Dic3";
    int limit=argc>2?stoi(argv[2]):240;
    int q=name=="Dic3"?6:7,n=2*q,L=2*n-1,c=name=="Dic3"?3:0;
    vector<vector<int>> table(n,vector<int>(n));
    for(int a=0;a<n;++a)for(int b=0;b<n;++b)
        table[a][b]=(a%q+(a/q?q-b%q:b%q)+(a/q && b/q?c:0))%q+q*((a/q+b/q)%2);
    vector<vector<Mask>> perm(n,vector<Mask>(1<<n));
    for(int a=0;a<n;++a)for(int m=1;m<(1<<n);++m){
        int g=__builtin_ctz((unsigned)m);
        perm[a][m]=perm[a][m&(m-1)]|(1<<table[g][a]);
    }
    auto has_identity=[&](const vector<int>& word) {
        array<Mask,15> layer{};layer[0]=1;int used=0;
        for(int a:word){++used;
            for(int j=min(n,used);j>0;--j)layer[j]|=perm[a][layer[j-1]];
            if(layer[n]&1)return true;
        }
        return false;
    };
    auto compositions=[](int sum,int parts,int lower) {
        vector<vector<int>> out;vector<int> row(parts);
        function<void(int,int)> rec=[&](int i,int left){
            if(i==parts-1){if(left>=lower){row[i]=left;out.push_back(row);}return;}
            for(int a=lower;a<=left-lower*(parts-i-1);++a){row[i]=a;rec(i+1,left-a);}
        };rec(0,sum);return out;
    };
    auto mod=[&](int x){x%=q;return x<0?x+q:x;};
    uint64_t total=0,even_eliminated=0,symmetry_eliminated=0,pair_eliminated=0,reflection_eliminated=0,dp_checked=0;
    bool found=false,timed_out=false;
    auto start=chrono::steady_clock::now();
    const int k=5;
    for(int rotations=n-4;rotations<=n-1 && !found && !timed_out;++rotations){
        auto aa=compositions(rotations,k,0),bb=compositions(L-rotations,k,1);
        int variants=1;for(int i=1;i<k;++i)variants*=q;
        for(const auto& b:bb){
            int even_capacity=0;for(int bj:b)even_capacity+=2*(bj/2);
            if(even_capacity>=n){
                total+=uint64_t(aa.size())*variants;
                even_eliminated+=uint64_t(aa.size())*variants;continue;
            }
            for(int code=0;code<variants;++code){
                if(chrono::duration<double>(chrono::steady_clock::now()-start).count()>limit){
                    timed_out=true;cout<<"timeout_before_code="<<code<<" b=";
                    for(int bj:b)cout<<bj<<",";cout<<" rotations="<<rotations<<endl;break;
                }
                vector<int> v(k);int value=code;
                for(int j=1;j<k;++j){v[j]=value%q;value/=q;}
                total+=aa.size();
                bool canonical=true;
                for(int shift=1;shift<k && canonical;++shift){
                    for(int j=0;j<k;++j){
                        pair<int,int> original{b[j],v[j]};
                        int h=(j+shift)%k;
                        pair<int,int> rotated{b[h],mod(v[h]-v[shift])};
                        if(rotated<original){canonical=false;break;}
                        if(original<rotated)break;
                    }
                }
                if(!canonical){symmetry_eliminated+=aa.size();continue;}
                vector<int> reflections;
                for(int j=0;j<k;++j)reflections.insert(reflections.end(),b[j],q+v[j]);
                if(has_identity(reflections)){reflection_eliminated+=aa.size();continue;}
                for(const auto& a:aa){
                    vector<int> R(k);R[0]=0;for(int j=1;j<k;++j)R[j]=R[j-1]+a[j-1];
                    bool pair_hit=false;
                    // With n-2 selected rotations and two reflections,
                    // the interior rotation count j ranges from lo to hi.
                    if(rotations>=n-2)for(int p=0;p<k;++p)for(int h=p+1;h<k;++h){
                        int T=R[h]-R[p],d=v[p]-v[h];
                        int lo=max(0,n-2-(rotations-T)),hi=min(n-2,T);
                        for(int j=lo;j<=hi;++j)if(mod(n-2-2*j+d+c)==0)pair_hit=true;
                    }
                    if(pair_hit){++pair_eliminated;continue;}
                    vector<int> word;
                    for(int j=0;j<k;++j){word.insert(word.end(),b[j],q+v[j]);word.insert(word.end(),a[j],1);}
                    ++dp_checked;
                    if(!has_identity(word)){
                        found=true;ofstream f(name+"-five-block-candidate.json");
                        f<<"{\"identity\":0,\"table\":[";
                        for(int x=0;x<n;++x){if(x)f<<",";f<<"[";
                            for(int y=0;y<n;++y){if(y)f<<",";f<<table[x][y];}f<<"]";}
                        f<<"],\"sequence\":[";for(int j=0;j<L;++j){if(j)f<<",";f<<word[j];}f<<"]}\n";
                        cout<<"CANDIDATE_REQUIRES_RAW_CHECK k="<<k<<" code="<<code<<endl;break;
                    }
                }
                if(found)break;
            }
            if(found || timed_out)break;
        }
        cout<<"level rotations="<<rotations<<" k="<<k<<" cumulative_parameters="<<total
            <<" even_eliminated="<<even_eliminated<<" symmetry_eliminated="<<symmetry_eliminated
            <<" pair_eliminated="<<pair_eliminated
            <<" reflection_eliminated="<<reflection_eliminated<<" dp_checked="<<dp_checked
            <<" found="<<found<<" timed_out="<<timed_out<<endl;
    }
    cout<<"finished exhaustive="<<(!found&&!timed_out)<<" candidate="<<found<<" timed_out="<<timed_out
        <<" elapsed="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<endl;
    return 0;
}
