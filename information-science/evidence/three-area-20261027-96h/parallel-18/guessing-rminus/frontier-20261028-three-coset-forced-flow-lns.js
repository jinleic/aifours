// Bounded exact-integer local weighted support search on three q8 syndrome cosets.
const N=[[],[2,3,4,5,6,7],[1,3,7,9,10],[1,2,4,8,9],[1,3,5,8,10],[1,4,6,9,10],[1,5,7,8,9],[1,2,6,8,10],[3,4,6,7,9,10],[2,3,5,6,8],[2,4,5,7,8]];
const TRI=[[1,2,3],[1,4,5],[1,6,7],[2,3,9],[2,7,10],[3,8,9],[4,5,10],[4,8,10],[5,6,9],[6,7,8]];
let state=2026102903>>>0;function rnd(){state^=state<<13;state^=state>>>17;state^=state<<5;return state>>>0;}
class Flow{
 constructor(n,pairs){this.n=n;this.head=new Int32Array(n);this.head.fill(-1);this.to=new Int32Array(2*pairs);this.next=new Int32Array(2*pairs);this.cap=new Float64Array(2*pairs);this.level=new Int32Array(n);this.work=new Int32Array(n);this.queue=new Int32Array(n);this.used=0;}
 add(a,b,c){let e=this.used;this.to[e]=b;this.cap[e]=c;this.next[e]=this.head[a];this.head[a]=e;this.to[e+1]=a;this.cap[e+1]=0;this.next[e+1]=this.head[b];this.head[b]=e+1;this.used+=2;return e;}
 bfs(s,t){this.level.fill(-1);let p=0,q=0;this.queue[q++]=s;this.level[s]=0;while(p<q){let v=this.queue[p++];for(let e=this.head[v];e!==-1;e=this.next[e]){let w=this.to[e];if(this.cap[e]>0&&this.level[w]<0){this.level[w]=this.level[v]+1;this.queue[q++]=w;}}}return this.level[t]>=0;}
 dfs(v,t,f){if(v===t)return f;for(let e=this.work[v];e!==-1;e=this.next[e]){this.work[v]=e;let w=this.to[e];if(this.cap[e]>0&&this.level[w]===this.level[v]+1){let z=this.dfs(w,t,Math.min(f,this.cap[e]));if(z){this.cap[e]-=z;this.cap[e^1]+=z;return z;}}}this.work[v]=-1;return 0;}
 run(s,t){let value=0;while(this.bfs(s,t)){this.work.set(this.head);for(;;){let z=this.dfs(s,t,Number.MAX_SAFE_INTEGER);if(!z)break;value+=z;}}return value;}
}
function geometry(F){const Ts=F.map(i=>TRI[i-1]),pos=[[]];let k=0;for(let v=1;v<=10;v++){let n=Ts.filter(t=>t.includes(v)).length;pos[v]=Array.from({length:n},(_,j)=>k+j);k+=n;}if(k!==18||pos.slice(1).some(x=>!x.length))throw Error('COVER');
 const C=new Int32Array(4096),shift=new Int32Array(6);for(let j=0;j<6;j++){let v=Ts[j][0],slot=Ts.reduce((n,t,h)=>n+(h<j&&t.includes(v)?1:0),0);shift[j]=1<<pos[v][slot];}
 for(let z=0;z<4096;z++){let w=0;for(let j=0;j<6;j++){let a=z>>(2*j)&1,b=z>>(2*j+1)&1;for(let h=0;h<3;h++){let v=Ts[j][h],slot=Ts.reduce((n,t,k)=>n+(k<j&&t.includes(v)?1:0),0);w|=([a,b,a^b][h])<<pos[v][slot];}}C[z]=w;}
 const V=pos.map(p=>p.reduce((a,b)=>a|1<<b,0));function conflict(w){for(let v=1;v<=10;v++)if((w&V[v])&&N[v].every(u=>!(w&V[u])))return true;return false;}
 function offset(mask){let x=0;for(let j=0;j<6;j++)if(mask>>j&1)x^=shift[j];return x;}
 const cache={};function offsets(mask){if(!(mask in cache)){let d=offset(mask),a=[];for(let i=0;i<4096;i++)if(conflict(d^C[i]))a.push(i);cache[mask]=a;}return cache[mask];}
 return {pos,C,offset,offsets,conflict};}
function score(word,pos,weights){let x=1;for(let v=1;v<=10;v++){let a=weights[v-1][word>>pos[v][0]&((1<<pos[v].length)-1)];x*=a*a;}return x;}
function runPair(g,masks,hold,old,weights){let n=4096,[a,b]=masks,d=g.offsets(a^b),oa=g.offset(a),ob=g.offset(b),oh=g.offset(hold),s=8192,t=8193;
 let blockedA=new Uint8Array(n),blockedB=new Uint8Array(n);for(let z of old[hold]){for(let x of g.offsets(a^hold))blockedA[z^x]=1;for(let x of g.offsets(b^hold))blockedB[z^x]=1;}
 let A=new Float64Array(n),B=new Float64Array(n),total=0;for(let i=0;i<n;i++){A[i]=blockedA[i]?0:score(g.C[i]^oa,g.pos,weights);B[i]=blockedB[i]?0:score(g.C[i]^ob,g.pos,weights);total+=A[i]+B[i];}
 if(!Number.isSafeInteger(total)||!Number.isSafeInteger(total+1))throw Error('INTEGER_RANGE');let inf=total+1,flow=new Flow(8194,2*n+n*d.length),se=new Int32Array(n),te=new Int32Array(n);for(let i=0;i<n;i++){se[i]=flow.add(s,i,A[i]);te[i]=flow.add(n+i,t,B[i]);}let cross=flow.used;for(let i=0;i<n;i++)for(let z of d)flow.add(i,n+(i^z),inf);let value=flow.run(s,t);flow.bfs(s,t);
 let L=[],R=[],cut=0,weight=0,reachL=new Uint8Array(n),reachR=new Uint8Array(n),inR=new Float64Array(n),sf=0,tf=0;
 for(let i=0;i<n;i++){reachL[i]=flow.level[i]>=0;reachR[i]=flow.level[n+i]>=0;if(reachL[i]&&!blockedA[i]){L.push(i);weight+=A[i];}else cut+=A[i];if(!reachR[i]&&!blockedB[i]){R.push(i);weight+=B[i];}else cut+=B[i];}
 for(let i=0;i<n;i++){let sent=0;for(let j=0;j<d.length;j++){let e=cross+2*(i*d.length+j),z=i^d[j],f=inf-flow.cap[e];if(reachL[i]&&!reachR[z])throw Error('INVALID_CUT');if(f<0||!Number.isSafeInteger(f))throw Error('FLOW');sent+=f;inR[z]+=f;}let f=A[i]-flow.cap[se[i]];if(f!==sent)throw Error('LEFT');sf+=f;}
 for(let i=0;i<n;i++){let f=B[i]-flow.cap[te[i]];if(f!==inR[i])throw Error('RIGHT');tf+=f;}
 if(value!==cut||value!==sf||value!==tf||weight!==total-value)throw Error('CERTIFICATE');return {[a]:L,[b]:R};}
function verify(g,masks,sets,weights){let words=[];for(let m of masks)for(let z of sets[m])words.push(g.C[z]^g.offset(m));for(let v=1;v<=10;v++){let seen=new Map(),mask=(1<<g.pos[v].length)-1;for(let w of words){let key=0;for(let u of N[v])for(let b of g.pos[u])key|=w&(1<<b);let x=w>>g.pos[v][0]&mask;if(seen.has(key)&&seen.get(key)!==x)throw Error('FD');seen.set(key,x);}}
 let S=0n;for(let w of words)S+=BigInt(score(w,g.pos,weights));let D=1n;for(let row of weights){let q=0n;for(let x of row)q+=BigInt(x)**3n;D*=q*q;}return {S:S.toString(),D:D.toString(),strict:S**3n>D,words};}
const CASES=[[1,2,5,6,8,9],[1,3,4,6,7,10],[2,3,4,6,7,10],[2,3,5,6,9,10]];
const begun=Date.now(),results=[];let witness=null;
for(const factors of CASES){let g=geometry(factors);for(let trial=0;trial<25;trial++){
 if(Date.now()-begun>50000)break;let u=1+rnd()%63,v=1+rnd()%63;if(v===u){trial--;continue;}let masks=[0,u,v];
 let weights=g.pos.slice(1).map(p=>Array.from({length:1<<p.length},()=>1+rnd()%3));
 let au=g.offsets(u),av=g.offsets(v),auSet=new Set(au),avSet=new Set(av),uvSet=new Set(g.offsets(u^v)),by=null;
 for(let y=0;y<4096&&!by;y++)if(!auSet.has(y)){for(let z=0;z<4096;z++)if(!avSet.has(z)&&!uvSet.has(y^z)){by=[y,z];break;}}
 if(!by){results.push({factors,masks,trial,no_three_word_support:true});continue;}
 let [y,z]=by,sets={0:Array.from({length:4096},(_,i)=>i).filter(i=>!auSet.has(i^y)&&!avSet.has(i^z)),[u]:[y],[v]:[z]};
 for(let it=0;it<5;it++){let hold=masks[it%3],pair=masks.filter(m=>m!==hold),prev=sets;sets={...sets,...runPair(g,pair,hold,sets,weights)};
  let before=verify(g,masks,prev,weights),after=verify(g,masks,sets,weights);if(BigInt(after.S)<BigInt(before.S))throw Error('NONMONOTONE');
  if(after.strict){witness={factors,masks,weights,support:sets,weighted_sum:after.S,threshold:after.D};break;}}
 let check=verify(g,masks,sets,weights);results.push({factors,masks,trial,support_size:check.words.length,represented:masks.filter(m=>sets[m].length),weighted_sum:check.S,threshold:check.D,strict:check.strict});if(witness)break;
 }if(witness||Date.now()-begun>50000)break;}
const out={cases:results,witness,elapsed_seconds:(Date.now()-begun)/1000,limits:'Each exact min-cut optimizes two cosets conditioned on the held third; finite coordinate updates do not certify global support or outer-weight optimum. Any strict witness requires independent replay.'};
await Bun.write('frontier-20261028-three-coset-forced-flow-lns-result.json',JSON.stringify(out,null,2));console.log(JSON.stringify({cases:results.length,strict_witness:!!witness,represented_three:results.filter(x=>x.represented&&x.represented.length===3).length,elapsed_seconds:out.elapsed_seconds}));
