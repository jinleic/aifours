// Exact restricted-family assay in D_7, order 14. Not a full-group proof.
// r^a0 (r^v0 s)^b0 r^a1 ... (r^v{k-1} s)^b{k-1} r^ak,
// sum a=13, sum b=14, a>=0, b>=1, k<=4. Automorphisms normalize v0=0.
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
    uint64_t total=0,pair_eliminated=0,reflection_eliminated=0,dp_checked=0;
    bool found=false,timed_out=false;
    auto start=chrono::steady_clock::now();
    for(int k=1;k<=4 && !found && !timed_out;++k){
        auto aa=compositions(13,k+1,0),bb=compositions(14,k,1);
        int variants=1;for(int i=1;i<k;++i)variants*=7;
        for(const auto& a:aa){
            vector<int> R(k);R[0]=a[0];for(int j=1;j<k;++j)R[j]=R[j-1]+a[j];
            for(int code=0;code<variants;++code){
                if(chrono::duration<double>(chrono::steady_clock::now()-start).count()>limit){timed_out=true;break;}
                vector<int> v(k);int value=code;
                for(int j=1;j<k;++j){v[j]=value%7;value/=7;}
                bool pair_hit=false;
                // Select twelve of thirteen rotations, and two reflections.
                // If T rotations lie between the reflections, the selected
                // interior count is T (omit outside) or T-1 (omit inside).
                for(int p=0;p<k;++p)for(int q=p+1;q<k;++q){
                    int T=R[q]-R[p],d=v[p]-v[q];
                    if((T<13 && mod(12-2*T+d)==0) || (T>0 && mod(14-2*T+d)==0))pair_hit=true;
                }
                total+=bb.size();
                if(pair_hit){pair_eliminated+=bb.size();continue;}
                for(const auto& b:bb){
                    int product=0;
                    for(int j=0;j<k;++j)if(b[j]%2)product=table[product][7+v[j]];
                    if(product==0){++reflection_eliminated;continue;}
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
        cout<<"level k="<<k<<" cumulative_parameters="<<total<<" pair_eliminated="<<pair_eliminated
            <<" reflection_eliminated="<<reflection_eliminated<<" dp_checked="<<dp_checked
            <<" found="<<found<<" timed_out="<<timed_out<<endl;
    }
    cout<<"finished exhaustive="<<(!found&&!timed_out)<<" candidate="<<found<<" timed_out="<<timed_out
        <<" elapsed="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<endl;
    return 0;
}
