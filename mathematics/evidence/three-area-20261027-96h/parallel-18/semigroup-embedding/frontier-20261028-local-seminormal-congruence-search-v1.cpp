// Exact bounded congruence proof search in the four-generated free band.
// Green-Rees recursive signatures are a named import. Exhaustion or timeout
// is INCONCLUSIVE unless the entire intended relation family is processed.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <deque>
#include <iostream>
#include <queue>
#include <string>
#include <string_view>
#include <unordered_map>
#include <unordered_set>
#include <vector>

struct Key {
  int p, s, last, first, mask;
  bool operator==(const Key& k) const { return p==k.p && s==k.s && last==k.last && first==k.first && mask==k.mask; }
};
struct KeyHash {
  size_t operator()(const Key& k) const {
    uint64_t v=uint64_t(k.p)*0x9e3779b185ebca87ULL ^ uint64_t(k.s)*0xc2b2ae3d27d4eb4fULL;
    v^=uint64_t(k.last+5)*0x165667b19e3779f9ULL ^ uint64_t(k.first+7)*0x85ebca77c2b2ae63ULL ^ uint64_t(k.mask);
    return size_t(v^(v>>31));
  }
};
struct Reason { int kind, prev; char letter; std::array<int,4> vals; };
struct Edge { int a,b; Reason why; };

class Search {
  size_t cap;
  std::unordered_map<Key,int,KeyHash> intern;
  std::vector<std::string> rep;
  std::vector<int> parent,rank;
  std::vector<std::vector<std::pair<int,int>>> adj;
  std::vector<Edge> edges;
  std::deque<std::array<int,3>> queue;
 public:
  explicit Search(size_t cap_):cap(cap_) { rep.emplace_back(); parent.push_back(0); rank.push_back(0); adj.emplace_back(); intern.reserve(cap_); }
  int add(std::string_view w) {
    if(w.empty())return 0;
    int mask=0;for(char c:w) mask|=1<<(c-'a');
    if((mask&(mask-1))==0){
      int letter=__builtin_ctz(unsigned(mask));
      Key key{0,0,letter,letter,mask}; auto it=intern.find(key);if(it!=intern.end())return it->second;
      return put(key,std::string(1,char('a'+letter)));
    }
    int seen=0,last=-1,first=-1;size_t cutL=0,cutR=0;
    for(size_t i=0;i<w.size();++i){seen|=1<<(w[i]-'a');if(seen==mask){last=w[i]-'a';cutL=i;break;}}
    seen=0;for(size_t i=w.size();i>0;--i){seen|=1<<(w[i-1]-'a');if(seen==mask){first=w[i-1]-'a';cutR=i-1;break;}}
    int p=add(w.substr(0,cutL));int s=add(w.substr(cutR+1));
    Key key{p,s,last,first,mask};auto it=intern.find(key);if(it!=intern.end())return it->second;
    std::string r=rep[p];r.push_back(char('a'+last));r.push_back(char('a'+first));r+=rep[s];return put(key,std::move(r));
  }
  int put(const Key& k,std::string r) {
    if(rep.size()>=cap)throw std::runtime_error("state-cap");
    int id=int(rep.size());intern.emplace(k,id);rep.push_back(std::move(r));parent.push_back(id);rank.push_back(0);adj.emplace_back();return id;
  }
  int root(int x) { while(parent[x]!=x){parent[x]=parent[parent[x]];x=parent[x];}return x; }
  void join(int a,int b,Reason why) {
    int ra=root(a),rb=root(b);if(ra==rb)return;
    if(rank[ra]<rank[rb])std::swap(ra,rb);parent[rb]=ra;if(rank[ra]==rank[rb])++rank[ra];
    int id=int(edges.size());edges.push_back({a,b,why});adj[a].push_back({b,id});adj[b].push_back({a,id});queue.push_back({a,b,id});
  }
  void initial(int maxlen) {
    std::vector<std::string> substitutions;
    for(char c='a';c<='d';++c)substitutions.emplace_back(1,c);
    if(maxlen>=2)for(char a='a';a<='d';++a)for(char b='a';b<='d';++b)if(a!=b)substitutions.push_back(std::string()+a+b);
    for(const auto& e:substitutions)for(const auto& a:substitutions)for(const auto& b:substitutions)for(const auto& c:substitutions){
      std::string x=e+a+e,y=e+b+e,z=e+c+e;
      Reason r{0,-1,0,{add(e),add(a),add(b),add(c)}};
      join(add(x+y+x+z+x),add(x+y+z+x),r);
    }
  }
  void run(int seconds,int maxlen) {
    int u=add("abcda"),v=add("abcacda");
    auto stop=std::chrono::steady_clock::now()+std::chrono::seconds(seconds);
    initial(maxlen);size_t done=0;
    while(!queue.empty() && root(u)!=root(v)) {
      if((done++&255)==0 && std::chrono::steady_clock::now()>=stop) {std::cout<<"INCONCLUSIVE time-cap ";stats();return;}
      auto [a,b,eid]=queue.front();queue.pop_front();
      for(char c='a';c<='d';++c){
        Reason l{1,eid,c,{}};Reason r{2,eid,c,{}};
        join(add(std::string(1,c)+rep[a]),add(std::string(1,c)+rep[b]),l);
        join(add(rep[a]+c),add(rep[b]+c),r);
      }
    }
    if(root(u)!=root(v)){std::cout<<"INCONCLUSIVE selected-instance closure exhausted ";stats();return;}
    std::vector<int> prev(rep.size(),-1),pe(rep.size(),-1);std::queue<int> bfs;bfs.push(u);prev[u]=u;
    while(!bfs.empty()&&prev[v]<0){int x=bfs.front();bfs.pop();for(auto [y,eid]:adj[x])if(prev[y]<0){prev[y]=x;pe[y]=eid;bfs.push(y);}}
    std::unordered_set<int> need;std::vector<int> stack;
    for(int x=v;x!=u;x=prev[x]){need.insert(pe[x]);stack.push_back(pe[x]);}
    while(!stack.empty()){int i=stack.back();stack.pop_back();auto r=edges[i].why;if(r.kind && need.insert(r.prev).second)stack.push_back(r.prev);}
    std::vector<int> sorted(need.begin(),need.end());std::sort(sorted.begin(),sorted.end());
    std::cout<<"PROOF_FOUND ";stats();
    for(int i:sorted){auto ed=edges[i];std::cout<<"edge "<<i<<" "<<rep[ed.a]<<" = "<<rep[ed.b]<<" reason "<<ed.why.kind<<":"<<ed.why.prev<<":"<<ed.why.letter<<" vals";if(!ed.why.kind)for(int x:ed.why.vals)std::cout<<" "<<rep[x];std::cout<<"\n";}
    std::cout<<"LIMIT proof trace needs independent exact replay of all substitution/context steps\n";
  }
  void stats()const {std::cout<<"states="<<rep.size()<<" merges="<<edges.size()<<" queued="<<queue.size()<<"\n";}
};
int main(int argc,char** argv){
  if(argc!=4){std::cerr<<"usage: binary state_cap seconds substitution_maxlen\n";return 2;}
  try{Search search(std::stoull(argv[1]));search.run(std::stoi(argv[2]),std::stoi(argv[3]));}
  catch(const std::exception& ex){std::cout<<"INCONCLUSIVE "<<ex.what()<<"\n";}
}
