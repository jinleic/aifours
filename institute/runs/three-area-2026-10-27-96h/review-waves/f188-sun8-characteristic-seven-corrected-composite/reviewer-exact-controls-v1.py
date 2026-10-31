#!/usr/bin/env python3
"""Independent exact diagnostics for the f188 source-conditional argument.

No author program is read/imported/run.  Integer trial division gives proof of
primality for the reported small factors.  Finite controls do not prove the
classification or the universal argument.  Individual mutations exit 1 with an
explicit expected rejection, not an unhandled assertion.
"""
import json
import math
import sys
from functools import lru_cache


def v7(n):
    if n <= 0:
        raise ValueError('positive integers only')
    k = 0
    while n % 7 == 0:
        k += 1
        n //= 7
    return k


def factors(n):
    if n < 1:
        raise ValueError(n)
    original = n
    out = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            out.append(d)
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out.append(n)
    assert math.prod(out) == original
    return out


def isprime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, math.isqrt(n) + 1, 2))


def ord_is(a, p, n):
    return isprime(p) and math.gcd(a, p) == 1 and pow(a, n, p) == 1 and all(
        pow(a, n // d, p) != 1 for d in set(factors(n)))


@lru_cache(None)
def phi_at_7(n):
    x = 7**n - 1
    for d in range(1, n):
        if n % d == 0:
            value = phi_at_7(d)
            assert x % value == 0
            x //= value
    return x


def GL(q, n):
    return math.prod(q**n - q**i for i in range(n))


def GU(q, n):
    return q**(n*(n-1)//2) * math.prod(q**i - (-1)**i for i in range(1, n+1))


def Sp(q, rank):
    return q**(rank*rank) * math.prod(q**(2*i)-1 for i in range(1, rank+1))


def B(q, rank):
    return Sp(q, rank)  # B_rank and C_rank have the same p-parts and order polynomial.


def D(q, rank):
    if rank < 1:
        raise ValueError(rank)
    return q**(rank*(rank-1)) * (q**rank-1) * math.prod(q**(2*i)-1 for i in range(1, rank))


def positive():
    expected = {
        6: [43], 12: [13,181], 8: [2,1201], 16: [2,17,169553],
        9: [3,37,1063], 18: [117307], 36: [13841169553],
        30: [6568801], 60: [61,555915824341],
    }
    factor_report = {}
    for n in [6,12,8,16,9,18,36,30,60,24]:
        value = phi_at_7(n)
        fs = factors(value)
        assert all(isprime(p) for p in fs)
        if n in expected:
            assert fs == expected[n], (n, fs, expected[n])
        primitives = sorted({p for p in fs if ord_is(7, p, n)})
        assert primitives
        factor_report[str(n)] = {'value': value, 'factors': fs, 'order_exactly_n': primitives}

    rows = [
        ('G2',6,3,-1,'alpha',13), ('3D4',12,6,-1,'3D4',7),
        ('F4',8,4,-1,'alpha',17), ('E6',9,9,1,'alpha',19),
        ('2E6',18,9,1,'beta',19), ('E7',18,18,1,'alpha',37),
        ('E8',30,30,1,'alpha',61),
    ]
    row_report=[]
    for name,e,m,sign,kind,threshold in rows:
        for f in (1,2):
            pool=factor_report[str(e*f)]['order_exactly_n']
            r=max(pool)
            assert r>7 and ord_is(7,r,e*f) and ord_is(7**f,r,e)
            assert r>threshold, (name, f, r, threshold)
            checks=[]
            for k in sorted(set(factors(f))):
                excluded = k == r or (kind == 'beta' and k == 2) or (kind == '3D4' and k == 3)
                if excluded:
                    checks.append({'k':k,'excluded_by_source':True})
                    continue
                assert f % k == 0
                a=pow(7, f//k, r)
                assert ord_is(a,r,e*k)
                residue=pow(a,m,r)
                wanted=1 if sign==1 else r-1
                assert residue != wanted, (name,f,k,r)
                checks.append({'k':k,'order':e*k,'residue':residue,'forbidden':wanted,'pass':True})
            row_report.append({'row':name,'f':f,'e':e,'m':m,'sign':sign,'kind':kind,'r':r,'checks':checks})

    counts={'linear':0,'unitary':0,'symplectic':0,'odd_orthogonal':0,'even_orthogonal_odd':0,
            'even_orthogonal_even':0,'blocks':0,'one_blocks':0,'subfields':0,'exceptional_18_20':0}
    minima={}
    def hit(key, val):
        counts[key]+=1
        minima[key]=min(minima.get(key,val),val)
    for f in (1,2):
        q=7**f
        for n in range(2,11):
            for m in range(1,n):
                for name, fn in [('linear',GL),('unitary',GU)]:
                    gap=v7(fn(q,n))-v7(fn(q,m))-v7(fn(q,n-m))
                    assert gap==f*m*(n-m)
                    hit(name,gap)
        for a in range(2,9):
            for b in range(1,a):
                gap=v7(Sp(q,a))-v7(Sp(q,b))-v7(Sp(q,a-b))
                assert gap==f*2*b*(a-b) and gap>=2
                hit('symplectic',gap)
        for a in range(3,9):
            for b in range(1,a+1):
                gap=v7(B(q,a))-v7(D(q,b))-v7(B(q,a-b))
                assert gap==f*b*(2*a+1-2*b) and gap>=2
                hit('odd_orthogonal',gap)
        for a in range(4,9):
            for b in range(a):
                c=a-1-b
                gap=v7(D(q,a))-v7(B(q,b))-v7(B(q,c))
                assert gap==f*(2*b*c+b+c) and gap>=2
                hit('even_orthogonal_odd',gap)
            for b in range(1,a):
                gap=v7(D(q,a))-v7(D(q,b))-v7(D(q,a-b))
                assert gap==f*2*b*(a-b) and gap>=2
                hit('even_orthogonal_even',gap)
        for m in (2,4):
            for k in range(2,10):
                factorial=v7(math.factorial(k))
                for fn in (GL,GU):
                    gap=v7(fn(q,m*k))-k*v7(fn(q,m))-factorial
                    assert gap==f*m*m*k*(k-1)//2-factorial and gap>=2
                    hit('blocks',gap)
                for fn in (Sp,D):
                    gap=v7(fn(q,m*k//2))-k*v7(fn(q,m//2))-factorial
                    assert gap==f*m*m*k*(k-1)//4-factorial and gap>=2
                    hit('blocks',gap)
        for n in range(3,15):
            for fn in (GL,GU):
                gap=v7(fn(q,n))-n*v7(fn(q,1))-v7(math.factorial(n))
                assert gap==f*n*(n-1)//2-v7(math.factorial(n)) and gap>=3
                hit('one_blocks',gap)
        for fn in (GL,GU):
            gap=v7(fn(q,4))-v7(Sp(q,2))
            assert gap==2*f and gap>=2
            hit('exceptional_18_20',gap)
    for f in (3,5,6,7,9):
        for r in set(factors(f)):
            if r==2:
                continue
            for n,fn in ((2,GL),(4,GU),(2,Sp),(4,D)):
                q=7**f
                q0=7**(f//r)
                gap=v7(fn(q,n))-v7(fn(q0,n))
                assert gap>=2
                assert gap*r % (f*(r-1))==0
                hit('subfields',gap)
    item11=[]
    for h in range(1,13):
        q0=7**h; q=q0*q0
        group=q*(q*q-1)//2
        subgroup=q0*(q0*q0-1)
        assert group % subgroup == 0
        idx=group//subgroup
        assert idx == q0*(q0*q0+1)//2 and v7(idx)==h
        item11.append({'f':2*h,'index':idx,'v7':v7(idx)})
    assert item11[0]['index']==175 and item11[1]['index']==58849
    # f odd and >1 starts at 3 for item (15); prime q=7 exclusions are exact residues.
    q=7
    assert q%8 not in (3,5) and q%40 not in (3,37,13,27,11,29,19,21,5)
    assert q%16 in (7,9)
    for f in range(1,21):
        assert ((7**f)%4==1) == (f%2==0)
        if f%2 and f>1:
            assert f>=3
    # The two exceptional odd-index stabilizers and the PSL2(49) prime support.
    order7=7*(7*7-1)//2
    order49=49*(49*49-1)//2
    assert order7//24==7 and order49//336==175
    assert order49==58800 and 2520%order49!=0
    assert factors(order49//7)==[2,2,2,2,3,5,5,7]
    cof=[1,1,1,1,1,1,2,7]
    assert all(math.gcd(a,b)==1 for i,a in enumerate(cof) for b in cof[i+1:])
    assert sum(a%2==1 and a%7!=0 for a in cof)==6
    return {'status':'PASS', 'method':'trial-division primes; exact modular orders; integer group-order valuation samples',
            'cyclotomic':factor_report,'bbgt_sample_rows':row_report,'classical_sample_counts':counts,
            'classical_sample_minima':minima,'item11_all_even_f_2_through_24':item11,
            'psl2_49_order':order49,'psl2_49_cofactor_support':[2,3,5,7],
            'pigeonhole_boundary_cofactors':cof}


def reject(reason, evidence):
    print(json.dumps({'status':'REJECT_EXPECTED_MUTATION','reason':reason,'evidence':evidence},sort_keys=True))
    raise SystemExit(1)


def mutation(mode):
    if mode=='wrong-minus-sign':
        e=9; f=2; r=117307; a=7
        assert ord_is(7,r,e*f) and pow(a,e,r)==r-1
        reject('alpha(e,-1) is false when k=2 and m=e; the actual E6 sign is +1',{'r':r,'a_to_e_mod_r':pow(a,e,r),'minus_one':r-1})
    if mode=='cyclotomic-nonprimitive':
        assert phi_at_7(9)%3==0 and not ord_is(7,3,9)
        reject('dividing Phi_n(7) alone does not imply order n when the prime divides n',{'n':9,'r':3,'7_mod_r':7%3})
    if mode=='item11-missing-factor':
        q0=7; q=q0*q0
        actual=(q*(q*q-1)//2)//(q0*(q0*q0-1))
        wrong=(q0*q0+1)//2
        assert actual==175 and wrong==25 and actual!=wrong
        reject('omitting q0 from the PGL2-subfield index',{'q0':q0,'actual':actual,'wrong':wrong,'actual_v7':v7(actual),'wrong_v7':v7(wrong)})
    if mode=='item11-f4-valuation-one':
        q0=49; actual=q0*(q0*q0+1)//2
        assert v7(actual)==2
        reject('claiming item (11) still has valuation 1 at f=4',{'f':4,'index':actual,'v7':v7(actual)})
    if mode=='repeated-unit':
        a=[1]*8
        assert all(math.gcd(x,y)==1 for i,x in enumerate(a) for y in a[i+1:])
        reject('pairwise-coprime cofactors do not imply at most one unit',{'cofactors':a,'unit_count':len(a)})
    if mode=='symplectic-factor-two':
        q=7; n=4; m=2
        actual=v7(Sp(q,n//2))-2*v7(Sp(q,m//2))
        wrong=m*(n-m)
        assert actual==2 and wrong==4
        reject('symplectic nondegenerate index exponent must contain the factor one half',{'actual':actual,'wrong':wrong})
    raise SystemExit('unknown mode')


if __name__=='__main__':
    if len(sys.argv)!=2:
        raise SystemExit('exactly one mode is required')
    if sys.argv[1]=='positive':
        print(json.dumps(positive(),sort_keys=True,indent=2))
    else:
        mutation(sys.argv[1])
