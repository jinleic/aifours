// Exact restricted-family assay in D_7, order 14. Not a full-group proof.
// r^a0 (r^v0 s)^b0 r^a1 ... (r^v{k-1} s)^b{k-1} r^ak,
// sum a=R, sum b=27-R, a>=0, b>=1, k<=4. Normalize v0=0.
// R>=14 has fourteen equal rotations. R<=10 has at least fourteen
// reflections obtained by taking even counts within the <=4 blocks.
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
    int limit=argc>1?stoi(argv[1]):240;
    int table[14][14];
    for(int a=0;a<14;++a)for(int b=0;b<14;++b)
        table[a][b]=(a%7+(a/7?7-b%7:b%7))%7+7*((a/7+b/7)%2);
    vector<vector<Mask>> perm(14,vector<Mask>(1<<14));
    for(int a=0;a<14;++a)for(int m=1;m<(1<<14);++m){
        int g=__builtin_ctz((unsigned)m);
        perm[a][m]=perm[a][m&(m-1)]|(1<<table[g][a]);
    }
    auto has_identity=[&](const vector<int>& word) {
        array<Mask,15> layer{};layer[0]=1;int used=0;
        for(int a:word){++used;
            for(int j=min(14,used);j>0;--j)layer[j]|=perm[a][layer[j-1]];
            if(layer[14]&1)return true;
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
    auto mod=[](int x){x%=7;return x<0?x+7:x;};
    uint64_t total=0,even_eliminated=0,pair_eliminated=0,reflection_eliminated=0,dp_checked=0;
    bool found=false,timed_out=false;
    auto start=chrono::steady_clock::now();
    for(int rotations=11;rotations<=13 && !found && !timed_out;++rotations)
      for(int k=1;k<=4 && !found && !timed_out;++k){
        auto aa=compositions(rotations,k+1,0),bb=compositions(27-rotations,k,1);
        int variants=1;for(int i=1;i<k;++i)variants*=7;
        for(const auto& b:bb){
            int even_capacity=0;for(int bj:b)even_capacity+=2*(bj/2);
            if(even_capacity>=14){
                total+=uint64_t(aa.size())*variants;
                even_eliminated+=uint64_t(aa.size())*variants;continue;
            }
            for(int code=0;code<variants;++code){
                if(chrono::duration<double>(chrono::steady_clock::now()-start).count()>limit){timed_out=true;break;}
                vector<int> v(k);int value=code;
                for(int j=1;j<k;++j){v[j]=value%7;value/=7;}
                total+=aa.size();
                vector<int> reflections;
                for(int j=0;j<k;++j)reflections.insert(reflections.end(),b[j],7+v[j]);
                if(has_identity(reflections)){reflection_eliminated+=aa.size();continue;}
                for(const auto& a:aa){
                    vector<int> R(k);R[0]=a[0];for(int j=1;j<k;++j)R[j]=R[j-1]+a[j];
                    bool pair_hit=false;
                    // With twelve selected rotations and two reflections,
                    // the interior rotation count j ranges from lo to hi.
                    if(rotations>=12)for(int p=0;p<k;++p)for(int q=p+1;q<k;++q){
                        int T=R[q]-R[p],d=v[p]-v[q];
                        int lo=max(0,12-(rotations-T)),hi=min(12,T);
                        for(int j=lo;j<=hi;++j)if(mod(12-2*j+d)==0)pair_hit=true;
                    }
                    if(pair_hit){++pair_eliminated;continue;}
                    vector<int> word;
                    for(int j=0;j<k;++j){word.insert(word.end(),a[j],1);word.insert(word.end(),b[j],7+v[j]);}
                    word.insert(word.end(),a[k],1);
                    ++dp_checked;
                    if(!has_identity(word)){
                        found=true;ofstream f("D7-run-candidate.json");
                        f<<"{\"identity\":0,\"table\":[";
                        for(int x=0;x<14;++x){if(x)f<<",";f<<"[";
                            for(int y=0;y<14;++y){if(y)f<<",";f<<table[x][y];}f<<"]";}
                        f<<"],\"sequence\":[";for(int j=0;j<27;++j){if(j)f<<",";f<<word[j];}f<<"]}\n";
                        cout<<"CANDIDATE_REQUIRES_RAW_CHECK k="<<k<<" code="<<code<<endl;break;
                    }
                }
                if(found)break;
            }
            if(found || timed_out)break;
        }
        cout<<"level rotations="<<rotations<<" k="<<k<<" cumulative_parameters="<<total
            <<" even_eliminated="<<even_eliminated<<" pair_eliminated="<<pair_eliminated
            <<" reflection_eliminated="<<reflection_eliminated<<" dp_checked="<<dp_checked
            <<" found="<<found<<" timed_out="<<timed_out<<endl;
    }
    cout<<"finished exhaustive="<<(!found&&!timed_out)<<" candidate="<<found<<" timed_out="<<timed_out
        <<" elapsed="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<endl;
    return 0;
}
