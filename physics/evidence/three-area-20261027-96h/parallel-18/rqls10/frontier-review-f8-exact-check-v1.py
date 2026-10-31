#!/usr/bin/env python3
"""Independent Fraction polynomial verification of PH7 f8 candidate.

No author scripts or result files are imported. Checks determinant/cofactor,
formal coefficient matching, critical identities, and every printed rational
Bernstein/tail coefficient. Does not prove the analytic neighborhood argument.
"""
from fractions import Fraction as F
from math import comb


class Poly:
    def __init__(self,n,terms=None):
        self.n=n
        self.d={k:F(v) for k,v in (terms or {}).items() if v}
    def add(self,other):
        other=coerce(self.n,other)
        d=self.d.copy()
        for k,v in other.d.items():
            d[k]=d.get(k,F(0))+v
        return Poly(self.n,d)
    __add__=add
    __radd__=add
    def __neg__(self): return Poly(self.n,{k:-v for k,v in self.d.items()})
    def __sub__(self,other): return self+(-coerce(self.n,other))
    def __rsub__(self,other): return coerce(self.n,other)+(-self)
    def __mul__(self,other):
        other=coerce(self.n,other)
        d={}
        for a,x in self.d.items():
            for b,y in other.d.items():
                k=tuple(i+j for i,j in zip(a,b))
                d[k]=d.get(k,F(0))+x*y
        return Poly(self.n,d)
    __rmul__=__mul__
    def __truediv__(self,scalar):
        return self * (F(1)/F(scalar))
    def __pow__(self,power):
        if not isinstance(power,int) or power<0: raise ValueError('nonnegative integer power')
        out=coerce(self.n,1)
        for _ in range(power): out=out*self
        return out
    def __eq__(self,other): return self.d==coerce(self.n,other).d
    def substitute(self,index,value):
        value=F(value)
        out={}
        for k,v in self.d.items():
            key=list(k); exponent=key[index]; key[index]=0; key=tuple(key)
            out[key]=out.get(key,F(0))+v*value**exponent
        return Poly(self.n,out)
    def coef(self,index,power):
        out={}
        for k,v in self.d.items():
            if k[index]==power:
                key=list(k); key[index]=0; out[tuple(key)]=v
        return Poly(self.n,out)
    def __repr__(self): return repr(self.d)


def coerce(n,value):
    if isinstance(value,Poly):
        if value.n!=n: raise ValueError('ring mismatch')
        return value
    v=F(value)
    return Poly(n,{(0,)*n:v}) if v else Poly(n)


def var(n,index):
    e=[0]*n; e[index]=1
    return Poly(n,{tuple(e):1})


def det(matrix):
    n=len(matrix)
    if not n: raise ValueError('empty determinant not used')
    dim=matrix[0][0].n
    def rec(row,columns):
        if row==n: return coerce(dim,1)
        value=coerce(dim,0)
        for j,c in enumerate(columns):
            if matrix[row][c].d:
                value+=((-1)**j)*matrix[row][c]*rec(row+1,columns[:j]+columns[j+1:])
        return value
    return rec(0,list(range(n)))


def minor(matrix,row,column):
    return [[v for j,v in enumerate(r) if j!=column]
            for i,r in enumerate(matrix) if i!=row]


def coefficient_list(poly,index):
    vals={}
    for key,value in poly.d.items():
        assert all(exponent==0 for k,exponent in enumerate(key) if k!=index), (key,value)
        vals[key[index]]=value
    return [vals.get(k,F(0)) for k in range(max(vals,default=0)+1)]


def bernstein(poly,a,b,degree):
    a,b=F(a),F(b)
    t=[sum(poly[i]*comb(i,k)*a**(i-k)*(b-a)**k
           for i in range(k,len(poly))) for k in range(degree+1)]
    return [sum(t[k]*F(comb(j,k),comb(degree,k)) for k in range(j+1))
            for j in range(degree+1)]


def shift(poly,a):
    a=F(a)
    return [sum(poly[i]*comb(i,k)*a**(i-k) for i in range(k,len(poly)))
            for k in range(len(poly))]


def main():
    # Independent symbolic determinant and numerator from the ACTUAL 7x7 matrix.
    n=9; y,u,w,d1,d2,d3,phi,B,C=(var(n,i) for i in range(n))
    zero=coerce(n,0)
    M=[[zero for _ in range(7)] for _ in range(7)]
    for i in range(3): M[i][i]=y+u
    M[0][1]=M[1][2]=M[2][3]=coerce(n,-1)
    M[3][3]=y+w; M[3][4]=coerce(n,-1)
    for i in range(4,7): M[i][i]=y+1
    M[4][5]=M[5][6]=coerce(n,-1)
    M[4][0]=-d1; M[5][0]=-d2; M[6][0]=-d3; M[6][3]=-phi
    expected=(y+w)*(y+u)**3*(y+1)**3-phi*(y+u)**3-d1*(y+1)**2-d2*(y+1)-d3
    assert det(M)==expected
    numerator=C*det(minor(M,6,0))-B*det(minor(M,6,1))+det(minor(M,6,2))
    assert numerator==(y+u)**2+B*(y+u)+C
    print('PASS symbolic 7x7 determinant and beta-adjugate numerator')

    # New ring in u,z,p,y, completely independent of the candidate checker.
    n=4; U,Z,P,Y=(var(n,i) for i in range(n))
    a=3*U+3; b=3*U**2+9*U+3; c3=U**3+9*U**2+9*U+1
    e4=3*U**3+9*U**2+3*U
    h0=b+4*a-a**2-6
    L=b-4*a+10-2*Z
    NN=4*h0+4-c3-b*(4-a)-4*Z
    q=(a-4)*P+h0-2*Z
    ww=P+4-a
    target=Y*((Y+1)**2+Z)**2
    residual=(Y+ww)*(Y+U)**3*(Y+1)**3-target*(Y**2+P*Y+q)
    for degree in (7,6,5): assert residual.coef(3,degree)==0
    degree4=residual.coef(3,4)
    assert degree4==L*P-NN or degree4==NN-L*P
    print('PASS symbolic degrees 7,6,5 vanish; degree4 is +/- (L p - N), sign',
          '+' if degree4==L*P-NN else '-')
    phi_form=e4+c3*ww-((6+2*Z)*q+(4+4*Z)*P+(1+Z)**2)
    assert residual.coef(3,3)==phi_form
    qL=(a-4)*NN+(h0-2*Z)*L
    phiL=e4*L+c3*(NN+(4-a)*L)-((6+2*Z)*qL+(4+4*Z)*NN+(1+Z)**2*L)
    Qcrit=(6*U**4-8*U**3+F(25,3)*U**2-F(32,3)*U+F(400,81))
    Pcrit=243*U**6-729*U**5+2025*U**4-5859*U**3+9360*U**2-7776*U+3184
    assert qL.substitute(1,F(8,9))==Qcrit
    assert (-243*phiL).substitute(1,F(8,9))==Pcrit
    Lcrit=L.substitute(1,F(8,9)); Ncrit=NN.substitute(1,F(8,9))
    assert Lcrit==3*U**2-3*U-F(7,9)
    assert Ncrit==8*U**3-9*U**2+3*U-F(32,9)
    assert Ncrit==((8*U-1)*Lcrit)/3+(110*U-103)/27
    assert qL.coef(0,4)==6 and (-243*phiL).coef(0,6)==243
    print('PASS critical qL/P identities, singular remainder, z-independent leading coefficients')

    p=coefficient_list(Pcrit,0); qlist=coefficient_list(Qcrit,0)
    pexpected=[
      [3184,2536,2044,F(267421,160),F(111197,80),F(75277,64),F(64717,64)],
      [F(64717,64),F(54157,64),F(58397,80),F(102973,160),F(2864,5),508,448],
      [448,388,F(1664,5),F(8999,32),F(19241,80),F(14731,64),F(18529,64)],
      [F(18529,64),F(22327,64),F(38231,80),F(114547,160),F(11221,10),1783,2824],
    ]
    pinterval=[(0,F(1,2)),(F(1,2),1),(1,F(3,2)),(F(3,2),2)]
    qexpected=[
      [F(400,81),F(292,81),F(1697,648),F(1121,648),F(689,648)],
      [F(689,648),F(473,648),F(293,648),F(1273,5184),F(1547,10368)],
      [F(1547,10368),F(137,2592),F(173,2592),F(149,648),F(49,81)],
    ]
    qinterval=[(0,F(1,2)),(F(1,2),F(3,4)),(F(3,4),1)]
    for (aa,bb),expected in zip(pinterval,pexpected):
        got=bernstein(p,aa,bb,6)
        assert got==expected and all(x>0 for x in got)
    for (aa,bb),expected in zip(qinterval,qexpected):
        got=bernstein(qlist,aa,bb,4)
        assert got==expected and all(x>0 for x in got)
    assert shift(p,2)==list(map(F,[2824,12492,22806,20061,9315,2187,243]))
    assert shift(qlist,1)==[F(49,81),6,F(61,3),16,6]
    print('PASS all 7 full rational Bernstein vectors and both shifted tails')
    print('PASS: all listed Bernstein/tail coefficients strictly positive')


if __name__=='__main__':
    main()
