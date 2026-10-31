from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import hashlib, json, re

R = Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
W = Path('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f104-spr7-nested-and-boundary-numerators')
M = json.loads((W/'manifest-v1.json').read_text())

def frac(x): return F(x)
def fs(x): return str(x)
def checked(path, digest):
    b=Path(path).read_bytes()
    assert hashlib.sha256(b).hexdigest()==digest, ('hash',str(path))
    return b.decode('utf-8')

def table_box(text):
    rows=re.findall(r'^\|(\d)\|([^|]+)\|([^|]+)\|\s*$',text,re.M)
    assert [int(r[0]) for r in rows]==list(range(7)), rows
    return [F(r[1]) for r in rows], [F(r[2]) for r in rows]

def corners(lo,hi):
    result=[]
    for e,o in product((0,1), repeat=2):
        a=[]
        for j in range(7):
            parity_choice = e if j%2==0 else o
            negative = ((j//2)%2==1)
            use_high=bool(parity_choice)^negative
            a.append((hi if use_high else lo)[j])
        result.append(a+[F(1)])
    return result

def pairing(a,b):
    # Direct real part of sum_jk a_j(-iw)^j b_k(iw)^k.
    p=[F(0)]*8
    for j,aj in enumerate(a):
        for k,bk in enumerate(b):
            if (j+k)%2==0:
                p[(j+k)//2] += aj*bk*((-1)**(j+(j+k)//2))
    return p

def ev(p,x):
    out=F(0)
    for c in reversed(p): out=out*x+c
    return out

def eo(a,t):
    return (sum(a[2*k]*(-t)**k for k in range(4)),
            sum(a[2*k+1]*(-t)**k for k in range(4)))

def qpower(p):
    # (1-x)^7 P(x/(1-x)) directly in the x power basis.
    return [sum(p[k]*comb(7-k,m-k)*(-1)**(m-k) for k in range(m+1)) for m in range(8)]

def bern(q,l,r):
    # Substitute x=l+(r-l)u, then u^j=sum_i C(i,j)/C(7,j) B_i^7(u).
    cp=[sum(q[m]*comb(m,j)*l**(m-j)*(r-l)**j for m in range(j,8)) for j in range(8)]
    return [sum(cp[j]*F(comb(i,j),comb(7,j)) for j in range(i+1)) for i in range(8)]

def ref_routh(a):
    c=list(reversed(a)); width=4
    rows=[c[0::2],c[1::2]]
    rows=[r+[F(0)]*(width-len(r)) for r in rows]
    for k in range(2,8):
        x,y=rows[-2:]
        assert y[0] != 0
        rows.append([(y[0]*x[j+1]-x[0]*y[j+1])/y[0] for j in range(width-1)]+[F(0)])
    return [r[0] for r in rows]

def det(a):
    a=[row[:] for row in a]; n=len(a); ans=F(1)
    for k in range(n):
        p=next((i for i in range(k,n) if a[i][k]),None)
        if p is None: return F(0)
        if p!=k: a[k],a[p],ans=a[p],a[k],-ans
        pivot=a[k][k]; ans*=pivot
        for i in range(k+1,n):
            factor=a[i][k]/pivot
            for j in range(k+1,n): a[i][j]-=factor*a[k][j]
            a[i][k]=F(0)
    return ans

def hurwitz_det(a,n):
    c=list(reversed(a))
    return det([[c[2*j-i+1] if 0<=2*j-i+1<len(c) else F(0) for j in range(n)] for i in range(n)])

def rootproof(data,lo,hi,doc):
    cs=corners(lo,hi)
    pols={}
    for name,ci,part in [('E-',0,0),('E+',2,0),('O-',0,1),('O+',1,1)]:
        a=cs[ci]
        p=[a[2*k+part]*(-1)**k for k in range(4)]
        assert p==list(map(F,data['root_polynomials'][name]))
        assert p[0]>0 and p[-1]<0
        brackets=[[F(x),F(y)] for x,y in data['root_intervals'][name]]
        assert len(brackets)==3
        for j,(l,r) in enumerate(brackets):
            assert 0<l<r and ev(p,l)*ev(p,r)<0
            if j: assert brackets[j-1][1]<l
        pols[name]=brackets
    bands=[]
    for names in [('E-','E+'),('O-','O+')]:
        bands.append([(min(pols[names[0]][j][0],pols[names[1]][j][0]),max(pols[names[0]][j][1],pols[names[1]][j][1])) for j in range(3)])
    ordered=[bands[i%2][i//2] for i in range(6)]
    assert all(ordered[i][1]<ordered[i+1][0] for i in range(5))
    listed=re.findall(r'^\| (?:E|O)[123] \| `\[([^,]+),\s*([^\]]+)\]` \|',doc,re.M)
    assert len(listed)==6 and ordered==[(F(a),F(b)) for a,b in listed], (ordered,listed)
    first=ref_routh(cs[0]); assert first==list(map(F,data['reference_routh_first_column'])) and min(first)>0
    determinants=[hurwitz_det(a,n) for a in cs for n in range(1,8)]
    assert len(determinants)==28 and min(determinants)>0
    return {'brackets':12,'separated_bands':6,'corner_hurwitz_determinants_positive':len(determinants),'reference_routh_column':list(map(fs,first))}

def frozenproof(data,lo,hi,b):
    allmins=[]; breakpoint=set(); counts=[]
    for i,a in enumerate(corners(lo,hi)):
        p=pairing(a,b)
        assert p==list(map(F,data['pairing_polynomials'][i]))
        q=qpower(p); leaves=data['bernstein_proofs'][i]['leaves']
        assert leaves and F(leaves[0]['left'])==0 and F(leaves[-1]['right'])==1
        cursor=F(0); vals=[]
        for leaf in leaves:
            l,r=F(leaf['left']),F(leaf['right'])
            assert l==cursor and l<r<=1
            cursor=r; breakpoint.update((l,r))
            c=bern(q,l,r)
            assert c==list(map(F,leaf['coefficients'])) and min(c)>0
            vals.extend(c)
        assert cursor==1 and min(vals)==F(data['bernstein_proofs'][i]['margin'])
        assert data['bernstein_proofs'][i]['nodes']==2*len(leaves)-1
        counts.append(len(leaves)); allmins.extend(vals)
    d=min(allmins)
    assert d==F(data['pairing_margin'])
    return d,sorted(breakpoint),counts,len(allmins)

def direct_full_check(a,b,breaks):
    q=qpower(pairing(a,b)); minimum=None; checked=0; maxdepth=0
    stack=[(breaks[i],breaks[i+1],0) for i in range(len(breaks)-1)]
    while stack:
        l,r,depth=stack.pop(); vals=bern(q,l,r); v=min(vals)
        if v<=0:
            assert depth<24, ('unproved subdivision',str(l),str(r),depth)
            mid=(l+r)/2; stack.extend([(l,mid,depth+1),(mid,r,depth+1)])
        else:
            checked+=1; maxdepth=max(maxdepth,depth)
            minimum=v if minimum is None else min(minimum,v)
    assert minimum>0
    return {'positive_bernstein_leaves':checked,'extra_subdivision_depth':maxdepth,'least_coefficient':fs(minimum)}

def interpolated(lo,hi,theta):
    return [lo[i]+theta[i]*(hi[i]-lo[i]) for i in range(7)]+[F(1)]

def check_samples(lo,hi,b,breaks,rho,basebound,pertbound):
    # Two generic coefficientwise interiors and an asymmetric parity-weight interior.
    interior_params=[[F(1,2)]*7,[F(1,5),F(2,7),F(3,8),F(4,9),F(5,11),F(6,13),F(7,15)],
                     [F(1,3),F(2,5),F(2,3),F(3,5),F(1,3),F(2,5),F(2,3)]]
    records=[]
    tests=[F(0),F(53,203),F(1,4),F(7,25),F(1),F(197,59),F(10),F(100),F(1000000)]
    cases=[]
    for i,a in enumerate(corners(lo,hi)): cases.append(('base_corner_'+str(i),a,basebound,False))
    for i,v in enumerate(interior_params): cases.append(('base_interior_'+str(i),interpolated(lo,hi,v),basebound,True))
    for kind,lp,hp in [('expanded',[x-rho for x in lo],[x+rho for x in hi]),('contracted',[x+rho for x in lo],[x-rho for x in hi])]:
        for i,a in enumerate(corners(lp,hp)): cases.append((kind+'_corner_'+str(i),a,pertbound,True))
        cases.append((kind+'_interior',interpolated(lp,hp,interior_params[1]),pertbound,True))
    for label,a,bound,full in cases:
        assert min(ref_routh(a))>0
        p=pairing(a,b); vals=[]
        for t in tests:
            ea,oa=eo(a,t); eb,ob=eo(b,t)
            denominator=ea*ea+t*oa*oa
            numerator=ea*eb+t*oa*ob
            assert numerator==ev(p,t) and denominator>0 and numerator>0
            ratio=numerator/denominator
            assert ratio>=bound, (label,t,ratio,bound)
            vals.append((ratio,t))
        minimum,tmin=min(vals)
        r={'member':label,'frequency_samples':len(tests),'least_sample_ratio':fs(minimum),'least_sample_t':fs(tmin)}
        if full: r['direct_full_frequency']=direct_full_check(a,b,breaks)
        records.append(r)
    return records

def run():
    texts=[]
    for x in M['inputs_in_read_order']:
        s=checked(x['path'],x['sha256']); assert len(s.encode())==x['bytes'] and s.count('\n')==x['LF']; texts.append(s)
    olddoc=checked(R/'frontier-20261028-anisotropic-new-numerator-open-family-v1.md','25db31d50117b74462a3fc25f22d46f48d2e44e79d28455c0b875eef93063d2f')
    affine= json.loads(checked(R/'frontier-20261028-boundary-affine-obstruction-frozen-v1.json','bca55dad8e27f93371bc163093d5d49404eb2bdfd538827b11d7c4076cc131b0'))
    hdoc,hdata,adoc,bdoc,bdata=texts[1],json.loads(texts[2]),texts[3],texts[4],json.loads(texts[5])
    hlo,hhi=table_box(hdoc); alo,ahi=table_box(adoc); blo,bhi=table_box(bdoc); olo,ohi=table_box(olddoc)
    assert (alo,ahi)==(blo,bhi)
    for data,lo,hi in [(hdata,hlo,hhi),(bdata,blo,bhi),(affine,alo,ahi)]:
        assert list(map(F,data['lower']))==lo and list(map(F,data['upper']))==hi
        assert all(l<u for l,u in zip(lo,hi))
    bh=list(map(F,['3/10','949689/50','160147/4','4490113/50','6620777/50','1971569/100','2028281/100','1']))
    bb=list(map(F,['3/100000','11563947/100000','16318673/100000','25808047/50000','5186543/10000','12038401/100000','524977/6250','1']))
    bold=list(map(F,['1/1000','883/25','7183/100','16691/100','23757/100','3851/100','3413/100','1']))
    bnew=list(map(F,['1/25','30987/50','112341/100','291423/100','92178/25','17402/25','58911/100','1']))
    g=list(map(F,['0','747/100','337/50','707/20','189/10','247/20','63/25','1']))
    assert list(map(F,hdata['numerator']))==bh and list(map(F,bdata['numerator']))==bb
    assert list(map(F,hdata['earlier_base_numerator']))==bold and list(map(F,hdata['old_numerator']))==bnew
    assert list(map(F,bdata['old_numerator']))==bh and list(map(F,affine['line_a']))==bh and list(map(F,affine['line_b']))==g
    assert [bh[-1],bb[-1],g[-1]]==[1,1,1]
    # Earlier 101/100-width box is contained in H; H is contained in B.
    assert all(hlo[i]<=olo[i]<ohi[i]<=hhi[i] for i in range(7))
    assert all(blo[i]<=hlo[i]<hhi[i]<=bhi[i] for i in range(7))
    assert all((hlo[i]+hhi[i])==(olo[i]+ohi[i])==(blo[i]+bhi[i]) for i in range(7))
    assert all((hhi[i]-hlo[i])/(ohi[i]-olo[i])==F(105,101) for i in range(6))
    assert all((bhi[i]-blo[i])/(ohi[i]-olo[i])==F(679,640)/F(101,100) for i in range(6))
    assert (hlo[6],hhi[6])==(olo[6],ohi[6])==(blo[6],bhi[6])
    assert hdata['contained_box_sha256']=='41411d5d0f25108a14e1dad8f8ac770ee580867d573206ce4ea22b6cf71005a4'
    assert bdata['contained_box_sha256']=='74c3ccc312cb0e7b86b8c76f2e89ab2043d36288454720c583ca2bf8a5027eec'
    hp=rootproof(hdata,hlo,hhi,hdoc); bp=rootproof(bdata,blo,bhi,bdoc)
    assert affine['root_polynomials']==bdata['root_polynomials'] and affine['root_intervals']==bdata['root_intervals'] and affine['reference_routh_first_column']==bdata['reference_routh_first_column']
    # Also check the six printed bands in the line-obstruction document.
    rootproof(affine,alo,ahi,adoc)
    dh,hbreaks,hcounts,hn=frozenproof(hdata,hlo,hhi,bh)
    db,bbreaks,bcounts,bn=frozenproof(bdata,blo,bhi,bb)
    assert hcounts==[6,11,11,7] and bcounts==[8,9,11,7] and hn==bn==280
    assert dh==F('1131593723113/6710886400000')
    assert db==F('19401458553061552497/153931627888640000000000')
    sh=1+sum(hhi); sb=1+sum(bhi)
    assert sh==F('178293/1600') and sb==F('5706951/51200')
    assert sh==F(hdata['coefficient_sum_upper']) and sb==F(bdata['coefficient_sum_upper'])
    baseh=dh/sh**2; baseb=db/sb**2
    assert baseh==F(hdata['ratio_margin'])==F('1131593723113/83331367171522560')
    assert baseb==F(bdata['ratio_margin'])==F('6467152851020517499/637492343295078039552000000')
    bh_l1=sum(map(abs,bh)); bb_l1=sum(map(abs,bb)); bold_l1=sum(map(abs,bold)); bnew_l1=sum(map(abs,bnew))
    assert (bh_l1,bb_l1,bold_l1,bnew_l1)==tuple(map(F,['32124813/100','7595109/5000','585271/1000','963073/100']))
    rh,rb=F(1,10**8),F(1,10**9)
    hgap=dh-7*rh*bh_l1; bgap=db-7*rb*bb_l1
    assert hgap==F('3064636073900093/20971520000000000')>0
    assert bgap==F('2220585007969403446317/19241453486080000000000000')>0
    pert_h=hgap/(sh+7*rh)**2; pert_b=bgap/(sb+7*rb)**2
    assert pert_h==F('47884938654688953125/4068914417784016897605632')
    assert pert_b==F('6939328149904385769740625/747061339892751392238794027565056')
    assert min(hhi[i]-hlo[i] for i in range(7))==min(bhi[i]-blo[i] for i in range(7))==F(29,1000)
    assert F(29,1000)-2*rh==F('1449999/50000000')>0
    assert F(29,1000)-2*rb==F('14499999/500000000')>0
    # Failure atoms and continuity margins, from direct signed monomial pairing.
    phold=ev(pairing(corners(hlo,hhi)[3],bold),F(7,25))
    phnew=ev(pairing(corners(hlo,hhi)[3],bnew),F(7,25))
    pbh=ev(pairing(corners(blo,bhi)[1],bh),F(197,59))
    assert phold==F('-19650719733069/195312500000000')==F(hdata['earlier_base_numerator_pairing'])<0
    assert phnew==F('-157843475513483/195312500000000')==F(hdata['old_numerator_pairing'])<0
    assert pbh==F('-3111053405919714332717419/318547390056832000000')==F(bdata['old_numerator_pairing'])<0
    hm1=-phold-7*rh*bold_l1*F(32,25)**7
    hm2=-phnew-7*rh*bnew_l1*F(32,25)**7
    bm=-pbh-7*rb*bh_l1*F(256,59)**7
    assert hm1==F('7658466357099997613/76293945312500000000')>0
    assert hm2==F('12273612385949610863/15258789062500000000')>0
    assert bm==F('9657226464955553493900607271/995460593927600000000000')>0
    # Full real affine line: one atom decreases, the other increases.
    eta=F('7999/8000'); line=[]
    for entry in affine['line_cases']:
        a=corners(blo,bhi)[entry['corner_index']]; t=F(entry['t'])
        A=ev(pairing(a,bh),t); G=ev(pairing(a,g),t); D=G-A; v=A+eta*D
        assert A==F(entry['A']) and D==F(entry['D']) and v==F(entry['value_at_threshold'])<0
        for key in ['A','D','value_at_threshold']:
            assert entry[key] in adoc
        line.append((A,D,v))
    assert line[0][1]>0 and line[1][1]<0 and eta==F(affine['threshold'])
    eta_from_constant=1-bb[0]/bh[0]
    line_at_constant=[(1-eta_from_constant)*bh[i]+eta_from_constant*g[i] for i in range(8)]
    assert eta_from_constant==F(9999,10000) and bb!=line_at_constant
    off_line_difference=bb[1]-line_at_constant[1]
    assert off_line_difference!=0
    hs=check_samples(hlo,hhi,bh,hbreaks,rh,baseh,pert_h)
    bs=check_samples(blo,bhi,bb,bbreaks,rb,baseb,pert_b)
    return {'input_hashes':'all six full SHA256, byte counts and LF counts match',
      'named_import_hashes':'affine frozen JSON and earlier anisotropic source match',
      'nested_inclusions':{'older_in_h':14,'h_in_b':14,'width_ratio_h_to_older':fs(F(105,101)),'width_ratio_b_to_older':fs(F(679,640)/F(101,100))},
      'nested':{'root_and_stability':hp,'leaf_counts':hcounts,'exact_recorded_coefficients':hn,'d':fs(dh),'base_ratio_bound':fs(baseh),'endpoint_gap':fs(hgap),'endpoint_ratio_bound':fs(pert_h),'old_failure':fs(phold),'new_failure':fs(phnew),'failure_margins':[fs(hm1),fs(hm2)],'members':hs},
      'affine':{'cases':[{'intercept':fs(a),'slope':fs(d),'threshold_pairing':fs(v)} for a,d,v in line],'threshold':fs(eta),'b_boundary_constant_implies_eta':fs(eta_from_constant),'b_boundary_s1_line_difference':fs(off_line_difference)},
      'boundary':{'root_and_stability':bp,'leaf_counts':bcounts,'exact_recorded_coefficients':bn,'d':fs(db),'base_ratio_bound':fs(baseb),'endpoint_gap':fs(bgap),'endpoint_ratio_bound':fs(pert_b),'old_failure':fs(pbh),'old_failure_margin':fs(bm),'members':bs}}

if __name__ == '__main__':
    print(json.dumps(run(),indent=2))
