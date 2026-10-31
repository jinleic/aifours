// Reviewer-authored, definition-first; no author checker imports or execution.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
using U=uint32_t; using V=vector<int>;
const auto begin_clock=chrono::steady_clock::now();
void require(bool b,const string& s){if(!b){cerr<<"FAIL "<<s<<endl;exit(2);}}
void deadline(){if(chrono::duration<double>(chrono::steady_clock::now()-begin_clock).count()>240){cerr<<"INCOMPLETE cooperative 240s deadline"<<endl;exit(3);}}
int mod(int x,int p){x%=p;return x<0?x+p:x;}
void jsonv(const V& v){cout<<'[';for(size_t i=0;i<v.size();i++){if(i)cout<<',';cout<<v[i];}cout<<']';}
int alt(const V& a,U mask,int p){int x=0,e=0;for(int i=0;i<(int)a.size();i++)if(mask&(1u<<i)){x+=(e?-1:1)*a[i];e^=1;}return mod(x,p);}
vector<U> subsets(int n,int k){vector<U> out; U m=(1u<<k)-1,lim=1u<<n;while(m<lim){out.push_back(m);U c=m&-m,r=m+c;m=(((r^m)>>2)/c)|r;}return out;}
struct QResult{int p;long long total=0,zero=0,free=0;vector<V> words;};
QResult checkq(int p){
 QResult r;r.p=p;int n=p+2;V z(n),counts(p);z[0]=0;
 auto rec=[&](auto&& self,int d)->void{
  if(d==n){r.free++;fill(counts.begin(),counts.end(),0);for(int x:z)counts[x]++;int triple=0;for(int c:counts){require(c==1||c==3,"Q multiset conclusion");triple+=(c==3);}require(triple==1,"Q unique triple");r.words.push_back(z);return;}
  for(int x=0;x<p;x++){z[d]=x;bool bad=false;for(int i=0;i<d&&!bad;i++)for(int j=i+1;j<d&&!bad;j++)for(int k=j+1;k<d;k++)if(mod(z[i]-z[j]+z[k]-x,p)==0){bad=true;break;}
   if(bad){long long completions=1;for(int i=d+1;i<n;i++)completions*=p;r.zero+=completions;}else self(self,d+1);
  }
 };
 rec(rec,1);r.total=1;for(int i=1;i<n;i++)r.total*=p;require(r.total==r.zero+r.free,"Q partition");deadline();return r;
}
V canonical(const V& a,int p){V best=a;int n=a.size();for(int r=0;r<n;r++)for(int t=1;t<p;t++){bool improve=false;for(int j=0;j<n;j++){int x=mod(t*(a[(r+j)%n]-a[r]),p);if(x<best[j]){improve=true;break;}if(x>best[j])break;}if(improve)for(int j=0;j<n;j++)best[j]=mod(t*(a[(r+j)%n]-a[r]),p);}return best;}
struct GenResult{set<V> ref_fail;long long raw=0,unique=0,ref_pass=0;};
GenResult generate5(const vector<V>& odd_words){
 int p=5,F=13,O=7;GenResult out;set<V> seen;auto refsets=subsets(F,2*p);
 for(int ne=0;ne<=p-2;ne++){
  int m=O+ne;V parity(m,0);parity[0]=1;
  auto parities=[&](auto&& self,int d,int left)->void{
   if(d==m){if(left)return;V lengths(m);for(int j=0;j<m;j++)lengths[j]=parity[j]?1:2;
    auto lengths_rec=[&](auto&& lr,int j,int pairs)->void{
     if(j==m){if(pairs)return;for(const V& z:odd_words){V labels(m);int oddpos=0;
      auto label_rec=[&](auto&& cr,int h,int oi)->void{
       if(h==m){if(labels.back()==labels.front())return;out.raw++;V a;for(int k=0;k<m;k++)for(int s=0;s<lengths[k];s++)a.push_back(labels[k]);V c=canonical(a,p);if(!seen.insert(c).second)return;out.unique++;bool ref=false;for(U s:refsets)if(alt(c,s,p)==0){ref=true;break;}if(ref)out.ref_pass++;else out.ref_fail.insert(c);return;}
       if(parity[h]){labels[h]=z[oi];if(h&&labels[h]==labels[h-1])return;cr(cr,h+1,oi+1);}else for(int x=0;x<p;x++){labels[h]=x;if(h&&labels[h]==labels[h-1])continue;cr(cr,h+1,oi);}
      };label_rec(label_rec,0,0);
     }return;}
     int base=parity[j]?1:2;for(int v=0;v<=pairs;v++){lengths[j]=base+2*v;lr(lr,j+1,pairs-v);}
    };lengths_rec(lengths_rec,0,p-2-ne);return;}
   if(left){parity[d]=1;self(self,d+1,left-1);}if(m-d>left){parity[d]=0;self(self,d+1,left);}
  };parities(parities,1,O-1);deadline();
 }
 return out;
}
struct Runs{vector<V> pos;V label,owner,local;};
Runs runs(const V& a){int n=a.size(),start=0;while(a[start]==a[(start+n-1)%n])start++;Runs r;r.owner.resize(n);r.local.resize(n);for(int k=0;k<n;k++){int i=(start+k)%n;if(k==0||a[i]!=a[(i+n-1)%n]){r.pos.push_back({});r.label.push_back(a[i]);}r.owner[i]=r.pos.size()-1;r.local[i]=r.pos.back().size();r.pos.back().push_back(i);}return r;}
struct Choice{int g1,g2;string branch;bool gamma=false;};
Choice choose_pair(const V& a,U gaps,int p,const Runs& r,int c){
 int F=a.size();vector<V> occupied(r.pos.size());
 for(int h=0;h<(int)r.pos.size();h++)for(int i:r.pos[h])if(gaps&(1u<<i))occupied[h].push_back(i);
 for(int h=0;h<(int)r.pos.size();h++)if(occupied[h].size()>=2){int i=occupied[h][0],j=occupied[h][1],aa=r.local[i]+1,xx=r.local[j]-r.local[i],bb=r.pos[h].size()-r.local[j]-1;bool odd=r.pos[h].size()%2;string s;
  if(!odd){if(!(aa%2)&&!(xx%2)&&!(bb%2))s="H-i";else if(xx%2)s="H-ii";else s="H-iii";}
  else if(aa%2&&xx%2&&bb%2)s="H-v";else if(xx%2)s="H-iv-a";else s="H-iv-bc";
  return{i,j,s,s=="H-iv-a"&&r.label[h]!=c};
 }
 V spares;for(int h=0;h<(int)r.pos.size();h++)if(r.pos[h].size()%2){int k=occupied[h].empty()?0:r.local[occupied[h][0]]+1;spares.push_back(k%2?r.pos[h][k-1]:r.pos[h].back());}
 sort(spares.begin(),spares.end());require((int)spares.size()==p+2,"spare count");vector<V> sector(spares.size());
 for(int h=0;h<(int)spares.size();h++){int st=spares[h],en=spares[(h+1)%spares.size()];for(int i=st;i!=en;i=(i+1)%F)if(gaps&(1u<<i))sector[h].push_back(i);}
 int g1=-1,g2=-1;string s;
 for(int h=0;h<(int)sector.size();h++)if(sector[h].size()>=2){g1=sector[h][0];g2=sector[h][1];s="A";break;}
 if(g1<0){s="B";for(int h=0;h<(int)spares.size();h++){int prev=(h+spares.size()-1)%spares.size();if(a[spares[h]]==c&&!sector[prev].empty()&&!sector[h].empty()){g1=sector[prev][0];g2=sector[h][0];break;}}}
 require(g1>=0&&g2>=0,"sector pair exists");require(r.owner[g1]!=r.owner[g2],"distinct sector runs");int lam=0;for(int g:{g1,g2})lam+=!(r.pos[r.owner[g]].size()%2)&&(r.local[g]+1)%2;
 return{g1,g2,s+"/lambda"+to_string(lam),false};
}
struct PairData{U sum=0,diff=0;array<U,7> sumw{},diffw{};};
struct Result{int p=0;long long projections=0,masks=0,universal_pairs=0,products=0,exponent_cases=0;map<string,long long> branches;map<string,string> samples;vector<V> checked;};
string dumpv(const V& v){string s="[";for(int i=0;i<(int)v.size();i++){if(i)s+=",";s+=to_string(v[i]);}return s+"]";}
// Independent literal original-order group multiplication of selected letters.
void sample_product(const V& a,int g1,int g2,int u,int v,U refs,int p,Result& out,const string& branch){
 V indices;int x=0,e=0,index=0,nrot=0;int mutated_x=0,mutated_e=0;
 auto take=[&](int y,int b,bool mutate){indices.push_back(index);x=mod(x+(e?-y:y),p);e^=b;int yy=mod(y+(mutate?1:0),p);mutated_x=mod(mutated_x+(mutated_e?-yy:yy),p);mutated_e^=b;};
 for(int i=0;i<(int)a.size();i++){if(refs&(1u<<i))take(a[i],1,false);index++;if(i==g1||i==g2){take(i==g1?u:v,0,i==g1);index++;nrot++;}}
 require((int)indices.size()==2*p&&nrot==2,"selector length and exactly two rotations");require(is_sorted(indices.begin(),indices.end())&&adjacent_find(indices.begin(),indices.end())==indices.end(),"strict original index order");require(x==0&&e==0,"literal original-order identity");require(mutated_x!=0&&mutated_e==0,"altered selected rotation negative control");out.products++;out.samples.try_emplace(branch,"{\"projection\":"+dumpv(a)+",\"gaps\":["+to_string(g1)+","+to_string(g2)+"],\"values\":["+to_string(u)+","+to_string(v)+"],\"indices_in_two_rotation_subword\":"+dumpv(indices)+",\"mutated_product\":["+to_string(mutated_x)+",0]}");
}
void check_projection(const V& a,int p,bool all_masks,Result& out){
 int F=a.size(),K=2*p-2;auto r=runs(a);V counts(p);int odd=0;for(int h=0;h<(int)r.pos.size();h++)if(r.pos[h].size()%2){counts[r.label[h]]++;odd++;}require(odd==p+2,"projection odd-run hypothesis");int c=-1;for(int i=0;i<p;i++)if(counts[i]==3)c=i;require(c>=0,"triple label");
 auto refsets=subsets(F,2*p);for(U m:refsets)require(alt(a,m,p)!=0,"reflection-only restriction negative control");
 vector<vector<PairData>> data(F,vector<PairData>(F));auto masks=subsets(F,K);U full=(1u<<p)-1;
 // Enumerate actual reflection-index subsets; neither pieces nor Lemma C used here.
 for(U m:masks){int a0=alt(a,m,p);V pref(F+1);for(int i=0;i<F;i++)pref[i+1]=pref[i]+((m>>i)&1u);for(int i=0;i<F;i++){int target=mod((pref[i+1]%2?1:-1)*a0,p);for(int j=i+1;j<F;j++){bool diff=(pref[j+1]-pref[i+1])%2;auto& q=data[i][j];if(diff){q.diff|=1u<<target;if(!q.diffw[target])q.diffw[target]=m;}else{q.sum|=1u<<target;if(!q.sumw[target])q.sumw[target]=m;}}}}
 for(int i=0;i<F;i++)for(int j=i+1;j<F;j++)if(data[i][j].sum==full||data[i][j].diff==full)out.universal_pairs++;
 V gapmasks;if(all_masks){for(U m=0;m<(1u<<F);m++)if(__builtin_popcount(m)>=p+1)gapmasks.push_back(m);}else{for(U m:subsets(F,p+1))gapmasks.push_back(m);}
 set<string> sampled;
 for(U mm:gapmasks){Choice q=choose_pair(a,mm,p,r,c);int i=min(q.g1,q.g2),j=max(q.g1,q.g2);auto& d=data[i][j];require(d.sum==full||d.diff==full,"candidate prescribed pair is universally good: "+q.branch+" "+dumpv(a));out.masks++;out.branches[q.branch]++;if(q.gamma)out.branches["H-iv-a/gamma-available"]++;
  if(sampled.insert(q.branch).second){for(int u=0;u<p;u++)for(int v=0;v<p;v++){int s=mod(u+v,p),t=mod(u-v,p);U ref=(d.sum&(1u<<s))?d.sumw[s]:d.diffw[t];require(ref!=0,"universal witness");sample_product(a,i,j,u,v,ref,p,out,q.branch);out.exponent_cases++;}if(q.gamma)out.samples.try_emplace("H-iv-a/gamma",out.samples[q.branch]);}
 }
 out.projections++;out.checked.push_back(a);deadline();
}
// Bounded p=7 family: AP odd labels (0,0,0,1,...,6), two or three
// separating even runs; enumerate explicitly declared length placements.
vector<V> bounded7(){int p=7;set<V> seen;vector<V> candidates;V odd{0,0,0,1,2,3,4,5,6};
 for(int ne:{2,3})for(int x=1;x<p;x++)for(int y=1;y<p;y++)for(int z=1;z<(ne==3?p:2);z++){
  V labels{0,x,0,y,0,1,2,3,4,5,6};V len(labels.size(),1);len[1]=len[3]=2;
  if(ne==3){labels.insert(labels.begin()+5,z);len.insert(len.begin()+5,2);}
  // Allocate all remaining pair units to one run or split over two runs.
  int extra=5-ne;for(int i=0;i<(int)len.size();i++)for(int j=i;j<(int)len.size();j++){
   V l=len;l[i]+=2*(extra-1);l[j]+=2;V a;bool proper=true;for(int k=0;k<(int)l.size();k++){if(labels[k]==labels[(k+1)%l.size()])proper=false;for(int v=0;v<l[k];v++)a.push_back(labels[k]);}if(!proper)continue;auto c=canonical(a,p);if(seen.insert(c).second)candidates.push_back(c);
  }
 }
 // Deterministic coverage-first ordering: interleave the attainable maximum run lengths.
 stable_sort(candidates.begin(),candidates.end(),[](const V& a,const V& b){auto ar=runs(a),br=runs(b);int al=0,bl=0;for(auto v:ar.pos)al=max(al,(int)v.size());for(auto v:br.pos)bl=max(bl,(int)v.size());return al>bl;});
 vector<V> out;auto refsets=subsets(19,14);map<int,int> bucket;
 for(const auto& a:candidates){bool ok=false;for(U m:refsets)if(alt(a,m,p)==0){ok=true;break;}if(ok)continue;auto r=runs(a);int maxlen=0,ne=0;for(auto v:r.pos){maxlen=max(maxlen,(int)v.size());ne+=v.size()%2==0;}int key=10*maxlen+ne;if(bucket[key]<8){bucket[key]++;out.push_back(a);}if(out.size()>=40)break;deadline();}
 return out;
}
void print_result(const Result& r){cout<<"{\"p\":"<<r.p<<",\"projection_classes\":"<<r.projections<<",\"gap_masks\":"<<r.masks<<",\"universal_pairs\":"<<r.universal_pairs<<",\"original_order_products\":"<<r.products<<",\"rotation_value_pairs_directly_multiplied\":"<<r.exponent_cases<<",\"branches\":{";bool first=true;for(auto [s,n]:r.branches){if(!first)cout<<',';first=false;cout<<'\"'<<s<<"\":"<<n;}cout<<"},\"samples\":{";first=true;for(auto [s,n]:r.samples){if(!first)cout<<',';first=false;cout<<'\"'<<s<<"\":"<<n;}cout<<"},\"projections\":[";first=true;for(auto v:r.checked){if(!first)cout<<',';first=false;jsonv(v);}cout<<"]}";}
int main(int argc,char** argv){
 require(argc==2,"mode required");string mode=argv[1];
 if(mode=="q5"){
  vector<QResult> qs;for(int p:{3,5,7})qs.push_back(checkq(p));cout<<"{\"lemma_Q\":[";for(int i=0;i<(int)qs.size();i++){if(i)cout<<',';auto& q=qs[i];cout<<"{\"p\":"<<q.p<<",\"normalized_sequences\":"<<q.total<<",\"zero_quadruple\":"<<q.zero<<",\"no_zero_quadruple\":"<<q.free<<",\"multiset_violations\":0}";}cout<<"],";
  auto g=generate5(qs[1].words);cout<<"\"p5_generation\":{\"raw_run_presentations\":"<<g.raw<<",\"cyclic_affine_classes_without_odd_zero_quadruple\":"<<g.unique<<",\"reflection_only_pass_classes\":"<<g.ref_pass<<",\"reflection_only_fail_classes\":"<<g.ref_fail.size()<<"},\"p5\":";Result r;r.p=5;for(const auto& a:g.ref_fail)check_projection(a,5,true,r);print_result(r);cout<<",\"status\":\"COMPLETE\"}\n";
 }else if(mode=="p7"){
  auto aa=bounded7();require(!aa.empty(),"nonempty bounded p7 family");Result r;r.p=7;for(const auto& a:aa)check_projection(a,7,false,r);cout<<"{\"p7\":";print_result(r);cout<<",\"status\":\"COMPLETE\"}\n";
 }else require(false,"unknown mode");
}
