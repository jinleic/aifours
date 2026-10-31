// Exact integer max-flow for weighted FD supports in a six-factor two-coset block.
// Outer weights are finite proposals only; a positive polynomial witness needs independent review.
const ROOT = import.meta.dir;
const OUT = `${ROOT}/frontier-20261028-two-coset-flow-search-result.json`;
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
      const w=this.to[e];if(this.cap[e]>1e-14&&this.level[w]<0){this.level[w]=this.level[v]+1;this.queue[z++]=w;}}}
    return this.level[t]>=0;}
  dfs(v,t,f){if(v===t)return f;
    for(let e=this.work[v];e!==-1;e=this.next[e]){this.work[v]=e;const w=this.to[e];
      if(this.cap[e]>1e-14&&this.level[w]===this.level[v]+1){const a=this.dfs(w,t,Math.min(f,this.cap[e]));
        if(a>1e-14){this.cap[e]-=a;this.cap[e^1]+=a;return a;}}}
    this.work[v]=-1;return 0;}
  run(s,t){let value=0;while(this.bfs(s,t)){this.work.set(this.head);for(;;){const f=this.dfs(s,t,Number.MAX_SAFE_INTEGER);if(!f)break;value+=f;}}
    return value;}
}

function scoreQ(word,pos,q){let x=1;for(let v=1;v<=10;v++){
  const label=(word>>pos[v][0])&((1<<pos[v].length)-1);x*=Math.pow(q[v-1][label],2/3);}
  return x;}
function select(geo,q){
  const n=4096,d=geo.offsets.length,s=2*n,t=s+1,A=new Float64Array(n),B=new Float64Array(n);let total=0;
  for(let i=0;i<n;i++){A[i]=scoreQ(geo.C[i],geo.pos,q);B[i]=scoreQ(geo.outsider^geo.C[i],geo.pos,q);total+=A[i]+B[i];}
  const inf=total+1,g=new Flow(2*n+2,2*n+n*d);
  for(let i=0;i<n;i++){g.add(s,i,A[i]);g.add(n+i,t,B[i]);}
  for(let i=0;i<n;i++)for(const off of geo.offsets)g.add(i,n+(i^off),inf);
  const value=g.run(s,t);g.bfs(s,t);let score=0,cut=0;const left=[],right=[];
  for(let i=0;i<n;i++){
    if(g.level[i]>=0){left.push(i);score+=A[i];}else cut+=A[i];
    if(g.level[n+i]<0){right.push(i);score+=B[i];}else cut+=B[i];
  }
  const lr=new Uint8Array(n);for(const j of right)lr[j]=1;
  for(const i of left)for(const off of geo.offsets)if(lr[i^off])throw Error('FLOAT_CUT_NOT_INDEPENDENT');
  if(Math.abs(value-cut)>1e-7||Math.abs(score+cut-total)>1e-7)throw Error('FLOAT_CUT_MISMATCH');
  const marginal=geo.pos.slice(1).map(p=>Array(1<<p.length).fill(0));
  for(const [arr,W] of [[left,A],[right,B]])for(const i of arr){const word=arr===left?geo.C[i]:geo.outsider^geo.C[i];
    for(let v=1;v<=10;v++)marginal[v-1][(word>>geo.pos[v][0])&((1<<geo.pos[v].length)-1)]+=W[i];}
  for(const row of marginal)for(let j=0;j<row.length;j++)row[j]/=score;
  return {score,left,right,marginal};
}
function witnessCheck(geo,q,selection){
  for(const scale of [10,100,1000,10000]){
    const weights=q.map(row=>{let a=row.map(x=>Math.cbrt(x)),m=Math.max(...a);return a.map(x=>Math.round(scale*x/m));});
    let S=0n;
    for(const [arr,right] of [[selection.left,false],[selection.right,true]])for(const i of arr){
      const word=(right?geo.outsider:0)^geo.C[i];let z=1n;
      for(let v=1;v<=10;v++){const a=weights[v-1][(word>>geo.pos[v][0])&((1<<geo.pos[v].length)-1)];z*=BigInt(a)**2n;}S+=z;}
    let D=1n;for(const row of weights){let sum=0n;for(const a of row)sum+=BigInt(a)**3n;D*=sum*sum;}
    if(S**3n>D)return {scale,weights,S:S.toString(),D:D.toString(),selected_left:selection.left,selected_right:selection.right};
  }
  return null;
}
const records=[];let witness=null;const started=Date.now();
for(const factors of CASES){
  const geo=geometry(factors);
  for(let trial=0;trial<25;trial++){
    if(Date.now()-started>70000)break;
    let q=geo.pos.slice(1).map(p=>{const n=1<<p.length, row=Array.from({length:n},()=>{
      const u=(rnd()+1)/4294967297;return trial%3===0?0.9+0.2*u:trial%3===1?u:Math.pow(u,3);});
      const total=row.reduce((a,b)=>a+b,0);return row.map(x=>x/total);});
    let maxscore=0,last=0,steps=0;
    for(let step=0;step<25;step++){
      if(Date.now()-started>70000)break;
      const result=select(geo,q);steps++;last=result.score;maxscore=Math.max(maxscore,last);
      if(last>1+1e-9){witness=witnessCheck(geo,q,result);if(witness){witness.factors=factors;witness.trial=trial;witness.step=step;break;}}
      let diff=0;for(let i=0;i<10;i++)for(let a=0;a<q[i].length;a++)diff=Math.max(diff,Math.abs(q[i][a]-result.marginal[i][a]));
      q=result.marginal;if(diff<1e-8)break;
    }
    records.push({factors,trial,steps,max_score_float:maxscore,last_score_float:last});if(witness)break;
  }
  if(witness||Date.now()-started>70000)break;
}
const out={records,witness,elapsed_seconds:(Date.now()-started)/1000,limits:'Floating flow and iteration are proposals only; an exact BigInt strict witness, if present, requires independent support/FD verification.'};
const output='frontier-20261028-two-coset-float-adaptive-result.json';await Bun.write(output,JSON.stringify(out,null,2));
console.log(JSON.stringify({starts:records.length,strict_integer_witness:!!witness,largest_float:Math.max(...records.map(x=>x.max_score_float)),elapsed_seconds:out.elapsed_seconds}));
