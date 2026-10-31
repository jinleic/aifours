// Exact integer max-flow for weighted FD supports in a six-factor two-coset block.
// Outer weights are finite proposals only; a positive polynomial witness needs independent review.
const ROOT = import.meta.dir;
const OUT = `${ROOT}/frontier-20261028-two-coset-flow-adaptive-result.json`;
const N = [[],[2,3,4,5,6,7],[1,3,7,9,10],[1,2,4,8,9],[1,3,5,8,10],
  [1,4,6,9,10],[1,5,7,8,9],[1,2,6,8,10],[3,4,6,7,9,10],[2,3,5,6,8],[2,4,5,7,8]];
const TRI = [[1,2,3],[1,4,5],[1,6,7],[2,3,9],[2,7,10],[3,8,9],[4,5,10],[4,8,10],[5,6,9],[6,7,8]];
const CASES = [[1,2,5,6,8,9],[1,3,4,6,7,10],[2,3,4,6,7,10],[2,3,5,6,9,10]];
let state=2026102823 >>> 0;
function rnd(){state^=state<<13;state^=state>>>17;state^=state<<5;return state>>>0;}
function geometry(factors){
  const T=factors.map(i=>TRI[i-1]);let cursor=0;const pos=[[]];
  for(let v=1;v<=10;v++){
    const k=T.filter(t=>t.includes(v)).length;pos[v]=Array.from({length:k},(_,j)=>cursor+j);cursor+=k;
  }
  if(cursor!==18||pos.some((p,i)=>i&&p.length===0))throw Error('GEOMETRY');
  const C=new Int32Array(4096);
  for(let x=0;x<4096;x++){
    let word=0;
    for(let j=0;j<6;j++){
      const a=(x>>(2*j))&1,b=(x>>(2*j+1))&1;
      for(let k=0;k<3;k++){
        const v=T[j][k], slot=T.reduce((n,t,h)=>n+(h<j&&t.includes(v)?1:0),0);
        word|=([a,b,a^b][k])<<pos[v][slot];
      }
    }
    C[x]=word;
  }
  let outsider=0;
  for(let j=0;j<6;j++){
    const v=T[j][0],slot=T.reduce((n,t,h)=>n+(h<j&&t.includes(v)?1:0),0);
    outsider|=1<<pos[v][slot];
  }
  const vm=pos.map(p=>p.reduce((x,b)=>x|(1<<b),0));
  const offsets=[];
  for(let j=0;j<4096;j++){
    const z=outsider^C[j];let conflict=false;
    for(let v=1;v<=10;v++)if((z&vm[v])&&N[v].every(u=>!(z&vm[u]))){conflict=true;break;}
    if(conflict)offsets.push(j);
  }
  if(!offsets.length)throw Error('NO_CONFLICT');
  return {T,pos,C,outsider,offsets};
}
class Flow {
  constructor(vertices, edgePairs){
    this.n=vertices;this.head=new Int32Array(vertices);this.head.fill(-1);
    const m=2*edgePairs;this.to=new Int32Array(m);this.next=new Int32Array(m);this.cap=new Float64Array(m);
    this.level=new Int32Array(vertices);this.work=new Int32Array(vertices);this.queue=new Int32Array(vertices);this.used=0;
  }
  add(a,b,c){const e=this.used;this.to[e]=b;this.cap[e]=c;this.next[e]=this.head[a];this.head[a]=e;
    this.to[e+1]=a;this.cap[e+1]=0;this.next[e+1]=this.head[b];this.head[b]=e+1;this.used+=2;return e;}
  bfs(s,t){this.level.fill(-1);let q=0,z=0;this.queue[z++]=s;this.level[s]=0;
    while(q<z){const v=this.queue[q++];for(let e=this.head[v];e!==-1;e=this.next[e]){
      const w=this.to[e];if(this.cap[e]>0&&this.level[w]<0){this.level[w]=this.level[v]+1;this.queue[z++]=w;}}}
    return this.level[t]>=0;}
  dfs(v,t,f){if(v===t)return f;
    for(let e=this.work[v];e!==-1;e=this.next[e]){this.work[v]=e;const w=this.to[e];
      if(this.cap[e]>0&&this.level[w]===this.level[v]+1){const a=this.dfs(w,t,Math.min(f,this.cap[e]));
        if(a>0){this.cap[e]-=a;this.cap[e^1]+=a;return a;}}}
    this.work[v]=-1;return 0;}
  run(s,t){let value=0;while(this.bfs(s,t)){this.work.set(this.head);for(;;){const f=this.dfs(s,t,Number.MAX_SAFE_INTEGER);if(!f)break;value+=f;}}
    return value;}
}
function score(word,pos,weights){let x=1;for(let v=1;v<=10;v++){
  const label=(word>>pos[v][0])&((1<<pos[v].length)-1),a=weights[v-1][label];x*=a*a;}
  return x;}
function polynomial(weights,S){let d=1n;for(const row of weights){let z=0n;for(const v of row)z+=BigInt(v)**3n;d*=z*z;}
  return {threshold:d.toString(),strict:BigInt(S)**3n>d};}
function run(geo,weights){
  const n=4096,d=geo.offsets.length,vertices=2*n+2,s=2*n,t=s+1;
  const A=new Float64Array(n),B=new Float64Array(n);let total=0;
  for(let i=0;i<n;i++){A[i]=score(geo.C[i],geo.pos,weights);B[i]=score(geo.outsider^geo.C[i],geo.pos,weights);total+=A[i]+B[i];}
  if(!Number.isSafeInteger(total))throw Error('CAPACITY_RANGE');
  const inf=total+1,g=new Flow(vertices,2*n+n*d),se=new Int32Array(n),te=new Int32Array(n);
  for(let i=0;i<n;i++){se[i]=g.add(s,i,A[i]);te[i]=g.add(n+i,t,B[i]);}
  const cross=g.used;
  for(let i=0;i<n;i++)for(const off of geo.offsets)g.add(i,n+(i^off),inf);
  const value=g.run(s,t);g.bfs(s,t);
  const reachL=new Uint8Array(n),reachR=new Uint8Array(n),left=[],right=[];let cut=0,S=0;
  for(let i=0;i<n;i++){
    reachL[i]=g.level[i]>=0;reachR[i]=g.level[n+i]>=0;
    if(reachL[i]){left.push(i);S+=A[i];}else cut+=A[i];
    if(!reachR[i]){right.push(i);S+=B[i];}else cut+=B[i];
  }
  const inR=new Float64Array(n);let sourceFlow=0,sinkFlow=0,positive=0;const sparse=[];
  for(let i=0;i<n;i++){
    let sent=0;for(let j=0;j<d;j++){
      const e=cross+2*(i*d+j),dest=i^geo.offsets[j],f=inf-g.cap[e];
      if(f<0||f>inf||!Number.isSafeInteger(f))throw Error('FLOW_RANGE');
      if(reachL[i]&&!reachR[dest])throw Error('INFINITE_CUT');
      if(f){sent+=f;inR[dest]+=f;positive++;sparse.push([i,dest,f]);}
    }
    const f=A[i]-g.cap[se[i]];if(f!==sent)throw Error('LEFT_CONSERVATION');sourceFlow+=f;
  }
  for(let i=0;i<n;i++){const f=B[i]-g.cap[te[i]];if(f!==inR[i])throw Error('RIGHT_CONSERVATION');sinkFlow+=f;}
  if(value!==cut||value!==sourceFlow||value!==sinkFlow||S!==total-value||!Number.isSafeInteger(S))throw Error('FLOW_CERTIFICATE');
  const poly=polynomial(weights,S);
  return {weights,max_weight:S,threshold:poly.threshold,strict_integer_witness:poly.strict,
    cross_degree:d,cross_edges:n*d,selected_left:left,selected_right:right,
    maxflow:value,cut_capacity:cut,positive_cross_flow_count:positive,positive_cross_flows:sparse};
}
const records=[];let witness=null;const started=Date.now();
for(const factors of CASES){
  if(Date.now()-started>65000)break;
  const geo=geometry(factors);
  for(let trial=0;trial<30;trial++){
    if(Date.now()-started>65000)break;
    let weights=geo.pos.slice(1).map(p=>Array.from({length:1<<p.length},()=>1+(rnd()%3)));
    const visited=new Set();
    for(let step=0;step<15;step++){
      if(Date.now()-started>65000)break;
      const key=JSON.stringify(weights);if(visited.has(key))break;visited.add(key);
      const result=run(geo,weights);result.factors=factors;result.trial=trial;result.step=step;
      if(result.strict_integer_witness){witness=result;records.push(result);break;}
      const marginal=geo.pos.slice(1).map(p=>Array(1<<p.length).fill(0));
      for(const i of result.selected_left){const word=geo.C[i],scoreValue=score(word,geo.pos,weights);
        for(let v=1;v<=10;v++)marginal[v-1][(word>>geo.pos[v][0])&((1<<geo.pos[v].length)-1)]+=scoreValue;}
      for(const i of result.selected_right){const word=geo.outsider^geo.C[i],scoreValue=score(word,geo.pos,weights);
        for(let v=1;v<=10;v++)marginal[v-1][(word>>geo.pos[v][0])&((1<<geo.pos[v].length)-1)]+=scoreValue;}
      const {selected_left,selected_right,positive_cross_flows,...compact}=result;records.push(compact);
      if(!result.max_weight)break;
      weights=marginal.map(row=>{const out=row.map(x=>Math.round(3*Math.cbrt(x/result.max_weight)));if(out.every(x=>x===0))out[0]=1;return out;});
    }
    if(witness)break;
  }
  if(witness)break;
}
const out={cases:records,strict_witness:witness,elapsed_seconds:(Date.now()-started)/1000,
  limits:'Exact max-flow per selected integer weight and specific 2-coset block only. Adaptive rounded-weight search is finite, not a global no-go; a positive witness requires independent graph/flow/entropy review.'};
await Bun.write(OUT,JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({cases:records.length,strict_witness:!!witness,elapsed_seconds:out.elapsed_seconds},null,2));
