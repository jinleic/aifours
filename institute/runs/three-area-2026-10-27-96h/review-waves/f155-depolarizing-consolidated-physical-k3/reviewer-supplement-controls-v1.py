#!/usr/bin/env python3
"""Additional F155 exact controls; reuses only the reviewer's own pinned definitions.
No author programs are read/imported/executed. No other research sources are read.
"""
from pathlib import Path
import hashlib
helper=Path(__file__).resolve().parent/'reviewer-exact-controls-v1.py'
helper_bytes=helper.read_bytes()
assert hashlib.sha256(helper_bytes).hexdigest()=='49513a7645f815f4f543c87b8eb5329de3393591e0b0644151ff624307fa780f'
# Only definitions before the top-level control runner; no reexecution of that runner.
exec(compile(helper_bytes.decode().split('\ntry:\n',1)[0],str(helper)+'[definitions-only]','exec'),globals())
RESULT=ROOT/'reviewer-supplement-controls-v1.result.json'
LOG['helper_sha256']=hashlib.sha256(helper_bytes).hexdigest()
LOG['kind']='INDEPENDENT_SUPPLEMENTAL_EXACT_CONTROLS'
rng.seed(155028)

def inverse(A):
    n=len(A); B=[ar[:]+ir[:] for ar,ir in zip(A,eye(n))]
    for i in range(n):
        k=next(k for k in range(i,n) if B[k][i]); B[i],B[k]=B[k],B[i]
        d=B[i][i]; B[i]=[x/d for x in B[i]]
        for k in range(n):
            if k!=i:
                d=B[k][i]
                B[k]=[x-d*y for x,y in zip(B[k],B[i])]
    return [ar[n:] for ar in B]

def local_rotate(v):
    for i in range(4):
        a=G(F(3,5)); b=G(0,F(4,5)); out=[G() for _ in range(16)]
        for k in range(16):
            if not bits(k,i):
                l=flip(k,i); out[k]=a*v[k]-b.conj()*v[l]; out[l]=b*v[k]+a.conj()*v[l]
        v=out
    return v

try:
    # Genuine random rational complex orthoprojectors, not numerical top eigenspaces.
    qreceipts=[]
    for j in range(4):
        cols=[random_v() for k in range(3)]; U=trans(cols); gram=mm(adj(U),U)
        Q=mm(mm(U,inverse(gram)),adj(U)); assert Q==adj(Q) and mm(Q,Q)==Q and tr(Q)==3
        assert 16*real(tr(mm(Q,Q)))-real(tr(Q))**2==39
        v=random_v(); A,rr,S,C=pure_data(v)
        rb=[sqbounds(x) for x in rr]; rlo=sorted(x[0] for x in rb); rhi=sorted(x[1] for x in rb)
        Ll=sum(w*r for w,r in zip((1,1,3,3),rlo)); Lu=sum(w*r for w,r in zip((1,1,3,3),rhi))
        W1=sub(scale(h1(A),2),scale(eye(),4))
        ii=inertia(frame(A)); assert ii['negative']==0 and ii['zero']>=4
        entry={'sample':j,'rank_three_Q_Gram_inverse_exact':True,'frame_inertia':ii,'S':str(S),'traces':[]}
        for p in (F(2,3),F(4,3)):
            t=abs(1-p); actual=real(tr(mm(Q,channel(A,p))))
            Qpos=Q if p<=1 else spin(Q)
            assert real(tr(mm(Qpos,channel(A,1-t))))==actual
            linear=real(tr(mm(Qpos,W1))); assert linear<=Ll
            rem=16*actual-3-t*linear
            assert rem<=0 or rem*rem<=t**4*39*(15-S)
            delta_l=8-Lu; sl,su=sqbounds(39*(15-S));
            a=(1+t)/2; b=(1-t)/2; R=a**4+2*a**3*b
            bound_l=t*(delta_l-t*(su-5))
            assert 16*(R-actual)>=bound_l
            entry['traces'].append({'p':str(p),'actual_trace':str(actual),'weight_one_trace':str(linear),
                                    'higher_weight_remainder':str(rem),'exact_squared_CS_check':True,
                                    'eq14_lower_bound':str(bound_l)})
        qreceipts.append(entry)
    check('actual_complex_rank3_same_Q_reflection_Parseval_first_order',cases=qreceipts)

    # Exact T3 spectrum after local rotations: rational radii, non-diagonal complex marginals.
    ve=random_v([x for x in range(16) if wt(x)%2==0],dominant=10)
    rho=density(ve); rr=[abs(real(marginal(rho,i)[0][0]-marginal(rho,i)[1][1])) for i in range(4)]
    rotated=local_rotate(ve); A=density(rotated); T3=layers(A)[3]
    vals=[]
    for signs in product((-1,1),repeat=4): vals.append((4+sum(s*r for s,r in zip(signs,rr)))/16)
    multiplicities={x:vals.count(x) for x in set(vals)}
    spectrum_cert=[]
    for x,count in sorted(multiplicities.items()):
        ii=inertia(shift(T3,x)); assert ii['zero']==count
        spectrum_cert.append({'eigenvalue':str(x),'multiplicity':count,'inertia':ii})
    r=sorted(rr); L=r[0]+r[1]+3*r[2]+3*r[3]
    assert sum(sorted(vals,reverse=True)[:3])==(12+L)/16<=F(5,4)
    check('T3_full_exact_spectrum_non_diagonal_complex_local_marginals',
          radii=list(map(str,rr)),top3=str((12+L)/16),spectrum_certificate=spectrum_cert)

    # Exact Hessian polarization in every complex normal coordinate at two t values.
    # Finite coefficient probes, not a claimed proof of all-t rational identities.
    inds=[i for i in range(16) if wt(i)>=2]; w1=[1,2,4,8]; rest=inds
    def direct(v,t):
        a=(1+t)/2; b=(1-t)/2; N=norm2(v)
        lam=[a**(4-wt(i))*b**wt(i) for i in range(16)]
        V=channel(add(outer(v,[G(i==0) for i in range(16)]),outer([G(i==0) for i in range(16)],v)),1-t)
        W=channel(sub(outer(v),scale(diag([int(i==0) for i in range(16)]),N)),1-t)
        AA=W[0][0]+sum((V[0][k]*V[k][0]/(lam[0]-lam[k]) for k in inds),G())
        M=[[W[i][j]+sum((V[i][k]*V[k][j]/(lam[i]-lam[k]) for k in inds),G()) for j in w1] for i in w1]
        return real(AA),M
    def formula(v,t):
        a=(1+t)/2; b=(1-t)/2; AA=F(); M=Z(4)
        for h in (2,3,4):
            vh=[v[i] if wt(i)==h else G() for i in range(16)]; N=norm2(vh)
            if not N: continue
            if h==2:
                TT=[[vh[i|j] if i!=j else G() for j in w1] for i in w1]; Gamma=mm(TT,adj(TT)); n=[real(Gamma[i][i]) for i in range(4)]
                Ah=-a*a*t*(1-t*t)*N
                Mh=[[G(-a*b*t*(1-t*t)*(N-n[i])) if i==j else a*b*t*t*(1+t)*Gamma[i][j] for j in range(4)] for i in range(4)]
            elif h==3:
                g=[vh[15^i] for i in w1]; D3=1-a*b; Ah=(-a*t*D3+a*t**5/D3)*N
                Mh=add(diag([-a*a*b*t*N-b*b*t*(1+t)*z.abs2() for z in g]),scale(outer([z.conj() for z in g]),t*t*b*b+t**5*b/D3))
            else:
                D4=a*a+b*b; Ah=(-t*D4+t**7/D4)*N; Mh=scale(eye(4),-a*b*t*N)
            AA+=Ah; M=add(M,Mh)
        return AA,M
    counts={}
    for t in (F(1,200),F(1,3)):
        vectors=[]
        for i in inds:
            v=[G(k==i) for k in range(16)]; vectors.append(v)
        for i,j in combinations(inds,2):
            for z in (G(1),G(0,1)):
                v=[G() for _ in range(16)]; v[i]=G(1); v[j]=z; vectors.append(v)
        for v in vectors: assert direct(v,t)==formula(v,t)
        counts[str(t)]=len(vectors)
    check('complete_complex_normal_coordinate_polarization_at_two_t',counts=counts,
          note='121 quadratic probes at each t; all-variable derivation remains written proof, not samples.')

    # Far-state controls at the uniform endpoint, using local spectral bounds to
    # certify that the actual closest-product distance is outside the tube.
    fcases=[]
    for j in range(3):
        v=random_v(); A,rr,S,C=pure_data(v); t=F(1,200)
        rb=[sqbounds(x) for x in rr]; lo=sorted(x[0] for x in rb); hi=sorted(x[1] for x in rb)
        # m <= min_i lambda_max(rho_i), hence eta^2 >= 1-min_i lambda_max.
        eta2_lower=1-min((1+r[1])/2 for r in rb); assert eta2_lower>=F(81,1600)
        delta_lower=8-sum(w*x for w,x in zip((1,1,3,3),hi)); assert delta_lower>=F(81,800)
        sl,su=sqbounds(39*(15-S)); assert delta_lower-t*(su-5)>0
        a=(1+t)/2; b=(1-t)/2; R=a**4+2*a**3*b
        c1=channel(A,1-t); c2=channel(A,1+t); assert c2==spin(c1)
        lo3,up3,cert=ksum_bounds(c1); assert up3<R
        fcases.append({'sample':j,'eta_squared_lower_bound':str(eta2_lower),'delta_lower_bound':str(delta_lower),
                       'reference':str(R),'certificate':cert})
    check('uniform_endpoint_random_certified_far_states',cases=fcases)
    negative('allowing_weight1_normals_makes_tube_strict_gap_false',F(9,41)**2*F(1,200)/32>0,
             pure_product_curve='(40|0000>+9|1000>)/41',actual_gap='0',
             false_claimed_gap=str(F(9,41)**2*F(1,200)/32))
    LOG['status']='PASS_ALL_DECLARED_CONTROLS'
except Exception as e:
    LOG['status']='FAILED'; LOG['error']=repr(e); LOG['traceback']=traceback.format_exc(); traceback.print_exc()
finally:
    LOG['ended_native']=datetime.now().astimezone().isoformat()
    with RESULT.open('x') as f: json.dump(LOG,f,indent=2,ensure_ascii=False); f.write('\n')
    print('RESULT',RESULT,'STATUS',LOG['status'],flush=True)
if LOG['status']!='PASS_ALL_DECLARED_CONTROLS': sys.exit(1)
