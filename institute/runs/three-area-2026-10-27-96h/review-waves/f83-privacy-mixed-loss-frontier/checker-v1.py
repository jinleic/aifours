# Native clock before exclusive creation: 2026-10-28T18:59:39-0700 PDT
from fractions import Fraction as F
from math import comb, factorial
import json

# Sparse exact polynomials: keys are exponent pairs, coefficients are Fraction.
def add(*terms):
    out = {}
    for term in terms:
        for monomial, coefficient in term.items():
            out[monomial] = out.get(monomial, F(0)) + coefficient
    return {m:c for m,c in out.items() if c}

def scale(p, c):
    return {m:v*F(c) for m,v in p.items() if v*F(c)}

def mul(a, b):
    out = {}
    for (i,j), x in a.items():
        for (k,l), y in b.items():
            monomial = (i+k,j+l)
            out[monomial] = out.get(monomial, F(0)) + x*y
    return {m:c for m,c in out.items() if c}

def power(a, n):
    result = {(0,0):F(1)}
    for _ in range(n):
        result = mul(result, a)
    return result

def plug(p, x, y):
    return add(*(scale(mul(power(x,i), power(y,j)), c) for (i,j),c in p.items()))

def evaluate(p, x, y):
    return sum((c*x**i*y**j for (i,j),c in p.items()), F(0))

def low(p, cutoff):
    return {m:c for m,c in p.items() if m[0] < cutoff and c}

def qstr(x):
    return str(x)

def verify():
    # Geometric N: E[(N)_j] = j! m^j. Convert via Stirling recurrence.
    S = [[1]]
    for n in range(1,5):
        row = [0]*(n+1)
        for j in range(1,n+1):
            row[j] = S[n-1][j-1] + (j*S[n-1][j] if j < len(S[n-1]) else 0)
        S.append(row)
    qvar = {(1,0):F(1)}
    mn = [{(0,j):F(S[k][j]*factorial(j)) for j in range(k+1) if S[k][j]} for k in range(5)]
    M = [add(*(scale(mul(power(qvar,k-j),mn[j]),comb(k,j)) for j in range(k+1))) for k in range(5)]
    P = add(scale(mul(M[3],M[2]),2), scale(mul(M[4],M[1]),-1))
    expected_P = {(5,0):F(1),(4,1):F(5),(3,1):F(2),(3,2):F(12),
                  (2,3):F(12),(2,1):F(-2),(1,1):F(-1),(1,2):F(-8),
                  (1,3):F(-12),(0,2):F(1),(0,3):F(2)}
    assert P == expected_P
    endpoint = {}
    for (i,j),c in P.items():
        endpoint[j] = endpoint.get(j,F(0)) + c
    assert endpoint == {0:F(1),1:F(4),2:F(5),3:F(2)}

    # Integrate independently over one cap: u in [0,eta], |v|<=u.
    # Terms (R exponent, u exponent, |v| exponent, coefficient).
    def cap(terms):
        out={}
        for rp,up,vp,c in terms:
            key=(rp,up+vp+2)
            out[key]=out.get(key,F(0))+F(2*c,(vp+1)*(up+vp+2))
        return {k:v for k,v in out.items() if v}
    area=cap([(0,0,0,1)])
    jcap=cap([(2,0,0,1),(1,1,0,-2),(0,2,0,1),(0,0,2,1)])
    wcap=cap([(2,0,0,1),(1,1,0,-2),(1,0,1,2),(0,2,0,1),(0,1,1,-2),(0,0,2,1)])
    assert area == {(0,2):F(1)}
    assert jcap == {(2,2):F(1),(1,3):F(-4,3),(0,4):F(2,3)}
    assert wcap == {(2,2):F(1),(1,3):F(-2,3),(0,4):F(1,6)}

    # Substitute q=s*z,m=s^4 in the all-variable stationarity numerator.
    psz={}
    for (i,j),c in P.items():
        key=(i+4*j,i)
        psz[key]=psz.get(key,F(0))+c
    expected_low={(5,5):F(1),(5,1):F(-1),(6,2):F(-2),(7,3):F(2)}
    assert low(psz,8)==expected_low
    # q=s+s^2/2-5s^3/8+d*s^4: an arbitrary d exposes cancellation.
    qs={(1,0):F(1),(2,0):F(1,2),(3,0):F(-5,8),(4,1):F(1)}
    ms={(4,0):F(1)}
    series=[plug(p,qs,ms) for p in M]
    pseries=plug(P,qs,ms)
    assert not low(pseries,8)
    assert any(i==8 and j==1 and c==4 for (i,j),c in pseries.items())
    m2short={(2,0):F(1),(3,0):F(1)}
    assert not low(add(series[2],scale(m2short,-1)),5)
    wshort={(2,0):F(1),(3,0):F(2),(4,0):F(3,2)}
    assert not low(add(series[4],scale(mul(series[2],wshort),-2)),7)
    ashort={(3,0):F(1),(4,0):F(3,2)}
    bshort={(2,0):F(1,3),(3,0):F(-1,3),(4,0):F(-1)}
    assert not low(add(wshort,scale(m2short,-1),scale(ashort,-1)),5)
    assert not low(add(m2short,scale(wshort,F(-2,3)),scale(bshort,-1)),5)
    ratio={(0,0):F(1,3),(1,0):F(-5,6)}
    assert not low(add(mul({(1,0):F(1)},bshort),scale(mul(ashort,ratio),-1)),5)

    def exact_moments(q,m):
        return [evaluate(p,q,m) for p in M]
    def scalars(q,m,lam):
        _,M1,M2,M3,M4=exact_moments(q,m)
        W0=M4/(2*M2)
        J0=M4/(3*M2)
        A=W0-M2
        B=M2-J0
        return M1,M2,M3,M4,W0,J0,A,B,B-lam*A
    def competitor(q):
        m=F(1,10000); lam=F(1)
        M1,M2,M3,M4,W0,J0,A,B,delta=scalars(q,m,lam)
        assert A>0 and B>0 and delta>0
        C=(F(4,3)+F(2,3)*lam)*M1
        eta=min(q/4,delta/(2*C))
        Z=2*M2-4*eta**2
        NJ=F(2,3)*M4-4*M2*eta**2+F(16,3)*M1*eta**3-F(8,3)*eta**4
        NW=M4-4*M2*eta**2+F(8,3)*M1*eta**3-F(2,3)*eta**4
        diff=(NJ+lam*NW)/Z-(J0+lam*W0)
        identity=4*eta**2/Z*(-delta+C*eta-(F(2,3)+lam/F(6))*eta**2)
        bound=delta*eta**2/M2
        residual=2*M3*M2-M4*M1
        assert 0<eta<q/2 and Z>0 and diff==identity and diff<=-bound and residual!=0
        return {'q':qstr(q),'m':qstr(m),'lambda':qstr(lam),'A':qstr(A),'B':qstr(B),
                'delta':qstr(delta),'eta':qstr(eta),'actual_gap':qstr(-diff),
                'guaranteed_gap':qstr(bound),'exact_identity_and_bound':True,
                'stationarity_residual':qstr(residual),'not_a_stationary_optimizer':True}
    one=competitor(F(21,200))
    two=competitor(F(53,500))
    assert one['eta']=='19004022149/3904822340000'
    failed=scalars(F(1,10),F(1,10000),F(1))
    assert failed[6]>0 and failed[7]>0 and failed[8]<0
    radial=[]
    for q in (F(1,2),F(3,4)):
        _,M2,_,M4,W,J,_,_,_=scalars(q,F(1),F(1))
        assert J==F(2,3)*W
        radial.append({'q':qstr(q),'W':qstr(W),'J':qstr(J),'lambda_one_cost':qstr(W+J)})
    assert radial == [
        {'q':'1/2','W':'1697/136','J':'1697/204','lambda_one_cost':'8485/408'},
        {'q':'3/4','W':'10763/864','J':'10763/1296','lambda_one_cost':'53815/2592'}]
    return {'independent_derivation':'geometric falling-factorial moments, exact cap integrations, sparse rational polynomial identities',
            'P_identity_and_positive_endpoint_factor':'P(1,m)=(1+m)^2(1+2m)',
            'cap_moment_polynomials_exact':True,
            'stationarity_asymptotic_terms':'z^5-z-2*s*z^2+2*s^2*z^3+O(s^3)',
            'series_coefficients_exact':'q=s+s^2/2-5*s^3/8+O(s^4); M2=s^2+s^3+O(s^5); W0=s^2+2*s^3+3*s^4/2+O(s^5); Lambda=1/(3*s)-5/6+O(s)',
            'stated_trial':one,'new_trial':two,
            'disclosed_invalid_trial_delta':qstr(failed[8]),'radial_controls':radial}

if __name__ == '__main__':
    print(json.dumps(verify(),indent=2,sort_keys=True))
