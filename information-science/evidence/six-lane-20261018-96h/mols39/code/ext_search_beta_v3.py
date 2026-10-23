#!/usr/bin/env python3
"""Written only; ContinueCFR21. ext-search-spec-v2.md is normative; v1/v2 are preserved and never executed. v3 adds a post-publication deadline check; math/tree unchanged.
Single-process stdlib beta-route producer, no subprocess/thread/network/date helper.

Tree: stage B assigns g=f mod q, column0 and split columns fixed. At each node recompute demands
for k*q items (row,residue), each demand3. For every unassigned column enumerate its feasible q
values (all k demands positive), accumulate item supplies; prune if a supply is smaller than its
demand. Choose the column with fewest feasible values, ties smallest column; try values increasing.
A complete g has a UNARY child: stage H root, assigning h=f mod3. On each 3-column fibre,
h[c]-h[d] must differ from D[x][c]-D[x][d] mod3. Stage H uses smallest feasible-domain variable,
ties smallest column, values increasing; all chunk-fixed h values are installed initially.
Every complete h is combined by CRT and directly checked before retention. Every solution appears
once. Supply pruning is sound because each item can be hit at most once by any remaining column.
Knuth estimator samples THIS full tree, including the unary B-to-H transition. It stops on a
verified witness. Seed is random.Random(seed*1000003+chunk). B/H node counts include pruned nodes.
Retained solutions and chunk records each capped4096; result16MiB. Any cap => INCOMPLETE_OUTPUT,
not an exclusion. Cooperative budget includes preparation and final publication. Run only through
a separately reviewed GO entrypoint and a separately admitted supervisor, one GO per job.
"""
import os, sys, json, hashlib, math, random, time

RAW_CAP=1<<20
OUT_CAP=16<<20
RETAIN=4096
PROGRAM='ext_search_beta_v3'
KEYS=('status','reason','program','n','q','k','m','chunk_lo','chunk_hi','mode','chunks','solutions',
      'solutions_sha256','input_sha256','program_sha256','extra','wall_s')
CODES={'COMPLETE':0,'ESTIMATE':0,'STOPPED_AT_SOLUTIONS':1,'INCOMPLETE_BUDGET':5,
       'INCOMPLETE_OUTPUT':6,'BAD_INPUT':2,'INPUT_PIN_MISMATCH':2,'IO_ERROR':2,'NOT_DM':3,'INTERNAL_ERROR':4}

class Halt(Exception):
    def __init__(self,status,reason):self.status,self.reason=status,reason


def args(argv):
    required=('--raw','--raw-sha256','--m','--chunk-lo','--chunk-hi','--max-solutions','--budget-s')
    allowed=required+('--mode','--probes','--seed')
    d={}
    if len(argv)%2:raise Halt('BAD_INPUT','expected flag/value pairs')
    for i in range(0,len(argv),2):
        key,val=argv[i:i+2]
        if key not in allowed or key in d:raise Halt('BAD_INPUT','unknown/repeated flag')
        d[key]=val
    if any(k not in d for k in required):raise Halt('BAD_INPUT','missing flag')
    for key in ('--m','--chunk-lo','--chunk-hi','--max-solutions','--probes','--seed'):
        if key in d:
            s=d[key]
            if not s.isascii() or not s.isdigit():raise Halt('BAD_INPUT','nonnegative decimal integer required')
            d[key]=int(s)
    try:s=float(d['--budget-s'])
    except ValueError:raise Halt('BAD_INPUT','bad budget') from None
    if not math.isfinite(s) or not 0<s<=10000:raise Halt('BAD_INPUT','finite budget 0<S<=10000 required')
    d['--budget-s']=s
    d.setdefault('--mode','search')
    if d['--mode'] not in ('search','estimate'):raise Halt('BAD_INPUT','bad mode')
    if d['--mode']=='estimate':
        if '--probes' not in d or '--seed' not in d or d['--probes']<1:raise Halt('BAD_INPUT','estimate requires probes>=1 and seed')
    elif '--probes' in d or '--seed' in d:raise Halt('BAD_INPUT','probe flags only for estimate')
    return d


def parse_raw(raw):
    lines=raw.split(b'\n')
    if lines[-1]==b'':lines.pop()
    rows=[]
    for line in lines:
        toks=line.split()
        if not toks:raise Halt('BAD_INPUT','G1 blank row')
        r=[]
        for t in toks:
            z=t[1:] if t[:1] in (b'+',b'-') else t
            if not z.isdigit():raise Halt('BAD_INPUT','G1 decimal token required')
            try:r.append(int(t))
            except ValueError:raise Halt('BAD_INPUT','G1 overlong integer') from None
        rows.append(r)
    return rows


class Engine:
    def __init__(self,D,deadline,summary):
        self.D,self.n,self.k=D,len(D[0]),len(D)
        self.q=self.n//3
        self.b=[[v%self.q for v in row] for row in D]
        self.a=[[v%3 for v in row] for row in D]
        self.deadline,self.summary=deadline,summary
        self.nodes=0
        self.sols=[]
        self.seen=set()
        self.stage_b_leaves=0
        self.stage_h_nodes=0
        self.K=0

    def checktime(self):
        if time.monotonic()>self.deadline:raise Halt('INCOMPLETE_BUDGET','self deadline')

    def node(self,stage):
        self.nodes+=1
        if stage=='H':self.stage_h_nodes+=1
        self.checktime()

    def b_pick(self,g):
        """Return (column, values); -1=full leaf; -2=dead. Recomputed, no incremental state."""
        q,k,n=self.q,self.k,self.n
        demand=[3]*(k*q)
        left=[]
        for c,v in enumerate(g):
            if v<0:left.append(c)
            else:
                for x in range(k):demand[x*q+(self.b[x][c]-v)%q]-=1
        if min(demand)<0:return -2,[]
        if not left:return (-1,[]) if not any(demand) else (-2,[])
        supply=[0]*(k*q)
        best,values=-1,None
        for c in left:
            self.checktime()
            opts=[]
            for w in range(q):
                its=[x*q+(self.b[x][c]-w)%q for x in range(k)]
                if all(demand[i]>0 for i in its):
                    opts.append(w)
                    for i in its:supply[i]+=1
            if not opts:return -2,[]
            if values is None or len(opts)<len(values):best,values=c,opts
        if any(s<d for s,d in zip(supply,demand)):return -2,[]
        return best,values

    def neighbours(self,g):
        adj=[[] for _ in range(self.n)]
        for x in range(self.k):
            self.checktime()
            fib=[[] for _ in range(self.q)]
            for c in range(self.n):fib[(self.b[x][c]-g[c])%self.q].append(c)
            if any(len(t)!=3 for t in fib):raise Halt('INTERNAL_ERROR','B leaf fibre size')
            for t in fib:
                for c in t:
                    for d in t:
                        if c!=d:adj[c].append((d,(self.a[x][c]-self.a[x][d])%3))
        return adj

    def h_pick(self,h,adj):
        best,values=-1,None
        for c,v in enumerate(h):
            if v>=0:
                if any(h[d]>=0 and (v-h[d])%3==delta for d,delta in adj[c]):return -2,[]
            else:
                opts=[w for w in range(3) if all(h[d]<0 or (w-h[d])%3!=delta for d,delta in adj[c])]
                if not opts:return -2,[]
                if values is None or len(opts)<len(values):best,values=c,opts
        return best,([] if values is None else values)

    def retain(self,g,h,fixed,estimate=False):
        f=[w+self.q*((h[c]-w)*pow(self.q,-1,3)%3) for c,w in enumerate(g)]
        if f[0]!=0 or any(f[c]!=v for c,v in fixed.items()) or any(
            len({(row[c]-f[c])%self.n for c in range(self.n)})!=self.n for row in self.D):
            raise Halt('INTERNAL_ERROR','direct extension recheck failed')
        t=tuple(f)
        if t in self.seen:raise Halt('INTERNAL_ERROR','duplicate solution')
        if len(self.sols)>=RETAIN:raise Halt('INCOMPLETE_OUTPUT','solution retention cap')
        self.seen.add(t);self.sols.append(f)
        if estimate or (self.K and len(self.sols)>=self.K):raise Halt('STOPPED_AT_SOLUTIONS','verified solution limit')

    def h_search(self,g,h,adj,fixed):
        self.node('H')
        c,vs=self.h_pick(h,adj)
        if c==-2:return
        if c==-1:self.retain(g,h,fixed);return
        for w in vs:
            h[c]=w
            try:self.h_search(g,h,adj,fixed)
            finally:h[c]=-1

    def b_search(self,g,h0,fixed):
        self.node('B')
        c,vs=self.b_pick(g)
        if c==-2:return
        if c==-1:
            self.stage_b_leaves+=1
            self.h_search(g,list(h0),self.neighbours(g),fixed)
            return
        for w in vs:
            g[c]=w
            try:self.b_search(g,h0,fixed)
            finally:g[c]=-1

    def probe(self,g0,h0,fixed,rng):
        g,h=list(g0),list(h0)
        estimate,weight=1.0,1.0
        stage='B';adj=None
        while True:
            self.node(stage)
            if stage=='B':
                c,vs=self.b_pick(g)
                if c==-2:return estimate
                if c==-1:
                    self.stage_b_leaves+=1
                    adj=self.neighbours(g)
                    stage='H'
                    estimate+=weight                      # unary child: H root
                    continue
            else:
                c,vs=self.h_pick(h,adj)
                if c==-2:return estimate
                if c==-1:self.retain(g,h,fixed,True);return estimate
            weight*=len(vs)
            estimate+=weight
            w=vs[rng.randrange(len(vs))]
            if stage=='B':g[c]=w
            else:h[c]=w


def main(argv):
    start=time.monotonic()
    out={key:None for key in KEYS}
    out.update(program=PROGRAM,chunks=[],solutions=[],extra={},solutions_sha256=hashlib.sha256(b'[]').hexdigest())
    status,reason='INTERNAL_ERROR',None
    engine=None;deadline=None;current=None;node0=0;sol0=0
    try:
        own=open(__file__,'rb').read();out['program_sha256']=hashlib.sha256(own).hexdigest()
        a=args(argv);deadline=start+a['--budget-s']
        with open(a['--raw'],'rb') as fh:raw=fh.read(RAW_CAP+1)
        if len(raw)>RAW_CAP:raise Halt('BAD_INPUT','raw exceeds1MiB')
        digest=hashlib.sha256(raw).hexdigest();out['input_sha256']=digest
        if digest!=a['--raw-sha256']:raise Halt('INPUT_PIN_MISMATCH','raw hash')
        rows=parse_raw(raw);k=len(rows);n=len(rows[0]) if rows else 0;q=n//3
        if not 2<=k<=12 or not 6<=n<=120 or n%3 or q%3==0 or any(len(r)!=n for r in rows):
            raise Halt('BAD_INPUT','shape or n=3q requirements')
        m,lo,hi=a['--m'],a['--chunk-lo'],a['--chunk-hi']
        if not 0<=m<=n-1 or not 0<=lo<hi<=n**m:raise Halt('BAD_INPUT','chunk range')
        out.update(n=n,q=q,k=k,m=m,chunk_lo=lo,chunk_hi=hi,mode=a['--mode'])
        D=[[v%n for v in row] for row in rows]
        for x in range(k):
            for y in range(x+1,k):
                if time.monotonic()>deadline:raise Halt('INCOMPLETE_BUDGET','input validation deadline')
                if len({(D[x][c]-D[y][c])%n for c in range(n)})!=n:raise Halt('NOT_DM','rows %d, %d'%(x,y))
        engine=Engine(D,deadline,out);engine.K=a['--max-solutions']
        for idx in range(lo,hi):
            engine.checktime()
            if len(out['chunks'])>=RETAIN:raise Halt('INCOMPLETE_OUTPUT','chunk record cap')
            fixed={0:0};r=idx
            for c in range(m,0,-1):fixed[c]=r%n;r//=n
            g,h=[-1]*n,[-1]*n
            for c,v in fixed.items():g[c]=v%q;h[c]=v%3
            node0,sol0=engine.nodes,len(engine.sols)
            current={'chunk':idx,'status':'NOT_COMPLETE','nodes':0,'solutions':0}
            out['chunks'].append(current)
            try:
                if a['--mode']=='search':engine.b_search(g,h,fixed)
                else:
                    rng=random.Random(a['--seed']*1000003+idx)
                    total=0.0
                    for unused in range(a['--probes']):total+=engine.probe(g,h,fixed,rng)
                    current.clear();current.update(chunk=idx,status='ESTIMATE',nodes=engine.nodes-node0,
                                                  estimate=total/a['--probes'],probes=a['--probes'])
            finally:
                current['nodes']=engine.nodes-node0
                if current['status']=='NOT_COMPLETE':current['solutions']=len(engine.sols)-sol0
            if a['--mode']=='search':current['status']='COMPLETE'
        status='COMPLETE' if a['--mode']=='search' else 'ESTIMATE'
    except Halt as exc:status,reason=exc.status,exc.reason
    except OSError as exc:status,reason='IO_ERROR',type(exc).__name__
    except Exception as exc:status,reason='INTERNAL_ERROR',type(exc).__name__
    if engine is not None:
        out['solutions']=sorted(engine.sols)
        out['extra']={'stage_b_leaves':engine.stage_b_leaves,'stage_h_nodes':engine.stage_h_nodes}
    if deadline is not None and time.monotonic()>deadline and status in ('COMPLETE','ESTIMATE'):
        status,reason='INCOMPLETE_BUDGET','final publication deadline'
    out['solutions_sha256']=hashlib.sha256(json.dumps(out['solutions'],separators=(',',':')).encode('ascii')).hexdigest()
    out.update(status=status,reason=reason,wall_s=round(time.monotonic()-start,3))
    data=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
    if len(data)>OUT_CAP:
        out.update(status='INCOMPLETE_OUTPUT',reason='publication16MiB cap',chunks=[],solutions=[],extra={},
                   solutions_sha256=hashlib.sha256(b'[]').hexdigest())
        data=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
    if deadline is not None and time.monotonic()>deadline and out['status'] in ('COMPLETE','ESTIMATE'):
        out.update(status='INCOMPLETE_BUDGET',reason='serialization deadline')
        data=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
    try:
        fd=os.open('result.json',os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o644)
        try:
            view=memoryview(data)
            while view:
                wrote=os.write(fd,view)
                if wrote<=0:raise OSError('zero write')
                view=view[wrote:]
        finally:os.close(fd)
    except OSError as exc:
        out.update(status='IO_ERROR',reason='result publication '+type(exc).__name__)
        data=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
    if deadline is not None and time.monotonic()>deadline and out['status'] in ('COMPLETE','ESTIMATE'):
        # Artifact already exists: never rewrite append-only evidence. Nonzero exit and explicit mismatch
        # make this publication UNKNOWN/unqualified. The parent must not accept the earlier file alone.
        out.update(status='INCOMPLETE_BUDGET',reason='post-publication deadline')
        data=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
    print(data.decode('ascii'),end='',flush=True)
    return CODES[out['status']]

if __name__=='__main__':sys.exit(main(sys.argv[1:]))
