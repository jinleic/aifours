#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <functional>
#include <numeric>

int main(){
    std::array<int,10> map={0,0,1,1,2,2,3,3,4,4};
    long all=0,representatives=0,paired=0,groupfound=0,groups=0;
    std::array<int,10> example{}; bool saved=false;
    do {
        ++all;
        if(map[0]!=0) continue;
        int first=-1;for(int i=1;i<10;i++)if(map[i]!=0){first=map[i];break;}
        if(first!=1)continue;
        ++representatives;
        bool ok[10][5]={};
        for(int k=1;k<10;k++)for(int d=1;d<5;d++){
            int n[10]={};for(int t=0;t<10;t++)n[(k*t+2*d*map[t])%10]++;
            int u[5];for(int t=0;t<5;t++)u[t]=n[t]-n[t+5];
            ok[k][d]=(u[0]==-u[1]&&u[0]==u[2]&&u[0]==-u[3]&&u[0]==u[4]);
        }
        std::array<int,5> firstrows={0,-1,-1,-1,-1},second={-1,-1,-1,-1,-1};
        bool hasfirst=false,haspaired=false;
        auto compatible=[&](int r,int b,const std::array<int,5>& chosen){
            for(int c=0;c<b;c++)if(!ok[(r-chosen[c]+10)%10][b-c])return false;
            return true;
        };
        std::function<bool(int,int)> fill2=[&](int b,int used){
            if(b==5)return true;
            for(int r=0;r<10;r++)if(!(used&(1<<r))&&compatible(r,b,second)){
                second[b]=r;if(fill2(b+1,used|(1<<r)))return true;
            }
            second[b]=-1;return false;
        };
        std::function<bool(int,int)> fill1=[&](int b,int used){
            if(b==5){
                ++groups;hasfirst=true;
                int r=0;while(used&(1<<r))++r;
                second[0]=r;
                if(fill2(1,used|(1<<r))){haspaired=true;return true;}
                return false;
            }
            for(int r=1;r<10;r++)if(!(used&(1<<r))&&compatible(r,b,firstrows)){
                firstrows[b]=r;if(fill1(b+1,used|(1<<r)))return true;
            }
            firstrows[b]=-1;return false;
        };
        fill1(1,1);
        if(hasfirst)++groupfound;
        if(haspaired){
            ++paired;
            if(!saved){
                saved=true;example=map;
                printf("first map:");for(int z:map)printf(" %d",z);
                printf("\nfirst group r(b):");for(int z:firstrows)printf(" %d",z);
                printf("\nsecond group r(b):");for(int z:second)printf(" %d",z);printf("\n");
            }
        }
    }while(std::next_permutation(map.begin(),map.end()));
    printf("all=%ld affine_representatives=%ld has_group=%ld has_paired_groups=%ld tested_complete_first_groups=%ld\n",all,representatives,groupfound,paired,groups);
}
