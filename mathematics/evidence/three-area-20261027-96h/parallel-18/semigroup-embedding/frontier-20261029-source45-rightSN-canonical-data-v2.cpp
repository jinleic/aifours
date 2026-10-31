#include <array>
#include <cassert>
#include <cstdint>
#include <deque>
#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
using U=uint32_t;
struct N { unsigned mask,h,c; U tail; };
std::vector<N> nodes{{0,0,0,0}};
std::array<std::vector<U>,64> bymask;
std::unordered_map<uint64_t,U> ids;
uint64_t key(unsigned h,unsigned c,U t){return (uint64_t(t)<<6)|(h<<3)|c;}
U get(unsigned h,unsigned c,U t){return ids.at(key(h,c,t));}
U gen[6];
U right(U a,unsigned j){
 if(!a)return gen[j];
 unsigned missing=nodes[a].mask&~(1u<<j);
 if(!missing)return get(nodes[a].h,j,0);
 U at=a;
 while(!(missing&(1u<<nodes[at].c)))at=nodes[at].tail;
 return get(nodes[a].h,nodes[at].c,right(nodes[at].tail,j));
}
U left(unsigned j,U a){
 if(!a)return gen[j];
 if(nodes[a].mask&(1u<<j))return get(j,nodes[a].c,nodes[a].tail);
 return get(j,j,a);
}
int A[5][5]={{0,1,2,3,0},{3,2,1,0,1},{0,1,2,3,2},{3,2,1,0,3},{0,1,2,3,4}};
int P[3][3]={{4,4,4},{4,1,3},{4,4,1}},th[5]={0,1,0,1,0};
int row(int s){return s/15;} int mid(int s){return (s/3)%5;} int col(int s){return s%3;}
int sm(int s,int t){return (row(s)*5+A[A[mid(s)][P[col(s)][row(t)]]][mid(t)])*3+col(t);}
int weight(int s,int t){return th[mid(s)]^th[P[col(s)][row(t)]];}
std::vector<U> parent;
U root(U a){while(parent[a]!=a){parent[a]=parent[parent[a]];a=parent[a];}return a;}
int main(){
 ids.reserve(700000);
 for(unsigned mask=1;mask<64;++mask){
  for(unsigned c=0;c<6;++c)if(mask&(1u<<c)){
   unsigned rem=mask^(1u<<c);
   std::vector<U> tails=rem?bymask[rem]:std::vector<U>{0};
   for(unsigned h=0;h<6;++h)if(mask&(1u<<h))for(U t:tails){
    U id=nodes.size();nodes.push_back({mask,h,c,t});bymask[mask].push_back(id);assert(ids.emplace(key(h,c,t),id).second);
   }
  }
 }
 assert(nodes.size()==614227);
 for(unsigned j=0;j<6;++j)gen[j]=get(j,j,0);
 size_t n=nodes.size();
 std::vector<std::array<U,6>> L(n),R(n);
 for(U a=1;a<n;++a)for(unsigned j=0;j<6;++j){L[a][j]=left(j,a);R[a][j]=right(a,j);}
 std::vector<U> action(n);
 auto flip=[](unsigned j){return j<3?j+3:j-3;};
 for(U a=1;a<n;++a)action[a]=get(flip(nodes[a].h),flip(nodes[a].c),action[nodes[a].tail]);
 assert(std::all_of(action.begin()+1,action.end(),[&](U a){return action[action[a]]==a;}));
 int sg[3]={44,28,12};
 std::array<std::array<U,45>,2> coef{};
 std::deque<int> todo;
 for(unsigned j=0;j<3;++j){todo.push_back(sg[j]);for(unsigned u=0;u<2;++u)coef[u][sg[j]]=gen[3*u+j];}
 while(!todo.empty()){
  int s=todo.front();todo.pop_front();
  for(unsigned j=0;j<3;++j){int t=sg[j],v=sm(s,t);if(coef[0][v])continue;
   for(unsigned u=0;u<2;++u)coef[u][v]=R[coef[u][s]][3*(u^weight(s,t))+j];todo.push_back(v);
  }
 }
 assert(std::all_of(coef[0].begin(),coef[0].end(),[](U a){return a!=0;}));
 parent.resize(n);for(U a=0;a<n;++a)parent[a]=a;
 std::deque<std::pair<U,U>> queue;
 for(unsigned u=0;u<2;++u)for(int s=0;s<45;++s)for(unsigned j=0;j<3;++j)
  queue.emplace_back(coef[u][sm(s,sg[j])],R[coef[u][s]][3*(u^weight(s,sg[j]))+j]);
 U merges=0;
 while(!queue.empty()){
  auto [a,b]=queue.front();queue.pop_front();U ra=root(a),rb=root(b);if(ra==rb)continue;
  parent[rb]=ra;++merges;
  for(unsigned j=0;j<6;++j){queue.emplace_back(L[a][j],L[b][j]);queue.emplace_back(R[a][j],R[b][j]);}
 }
 std::unordered_map<U,U> classes;std::vector<U> cls(n),reps;
 for(U a=1;a<n;++a){auto [it,fresh]=classes.emplace(root(a),classes.size());if(fresh)reps.push_back(a);cls[a]=it->second;}
 bool faithful=true;unsigned pairs=0;
 for(int s=0;s<45;++s)for(int t=0;t<s;++t)if(row(s)==row(t)&&col(s)==col(t)&&th[mid(s)]==th[mid(t)]){
  ++pairs;if(cls[coef[0][s]]==cls[coef[0][t]]){faithful=false;std::cout<<"COLLAPSE "<<s<<" "<<t<<"\n";}
 }
 for(U a=1;a<n;++a){U b=reps[cls[a]];assert(cls[action[a]]==cls[action[b]]);for(unsigned j=0;j<6;++j){assert(cls[L[a][j]]==cls[L[b][j]]);assert(cls[R[a][j]]==cls[R[b][j]]);}}
 for(unsigned u=0;u<2;++u)for(int s=0;s<45;++s)assert(cls[coef[u][s]]==cls[u?action[coef[0][s]]:coef[0][s]]);
 std::cout<<"free_rightSN6=614226 mixed_generator_relations=270 merges="<<merges<<" canonical_band_classes="<<classes.size()<<"\n";
 std::cout<<"same_actor_pairs="<<pairs<<" faithful="<<faithful<<" action_and_12_generator_transitions_checked=true\n";
 if(faithful){
  std::vector<std::vector<unsigned>> word(n);
  for(U a=1;a<n;++a){
   word[a].push_back(nodes[a].h);word[a].push_back(nodes[a].c);
   word[a].insert(word[a].end(),word[nodes[a].tail].begin(),word[nodes[a].tail].end());
   word[a].erase(std::unique(word[a].begin(),word[a].end()),word[a].end());
  }
  std::vector<std::vector<U>> table(reps.size(),std::vector<U>(reps.size()));
  for(U i=0;i<reps.size();++i)for(U j=0;j<reps.size();++j){U a=reps[i];for(unsigned k:word[reps[j]])a=R[a][k];table[i][j]=cls[a];}
  for(unsigned u=0;u<2;++u)for(int s=0;s<45;++s)for(int t=0;t<45;++t){
   U a=cls[coef[u][s]],b=cls[coef[u^weight(s,t)][t]];
   assert(table[a][b]==cls[coef[u][sm(s,t)]]);
  }
  std::cout<<"JSON:{\"band_table\":[";
  for(U i=0;i<reps.size();++i){if(i)std::cout<<",";std::cout<<"[";for(U j=0;j<reps.size();++j){if(j)std::cout<<",";std::cout<<table[i][j];}std::cout<<"]";}
  std::cout<<"],\"band_action\":[";
  for(U i=0;i<reps.size();++i){if(i)std::cout<<",";std::cout<<cls[action[reps[i]]];}
  std::cout<<"],\"coordinates\":[";
  for(int s=0;s<45;++s){if(s)std::cout<<",";std::cout<<cls[coef[0][s]];}
  std::cout<<"],\"free_generator_classes\":[";
  for(unsigned j=0;j<6;++j){if(j)std::cout<<",";std::cout<<cls[gen[j]];}
  std::cout<<"],\"source_generators\":[44,28,12],\"source_size\":45,\"free_rightSN_size\":614226,\"congruence_merges\":613920}\n";
 }
 return faithful?0:2;
}
