from fractions import Fraction as F


class G:
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    @staticmethod
    def coerce(x):
        return x if isinstance(x, G) else G(x)

    def __add__(self, other):
        other = self.coerce(other)
        return G(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __mul__(self, other):
        other = self.coerce(other)
        return G(self.a*other.a - self.b*other.b, self.a*other.b + self.b*other.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        numer = self * other.conj()
        den = other.mag2()
        return G(numer.a/den, numer.b/den)

    def __bool__(self):
        return bool(self.a or self.b)

    def conj(self):
        return G(self.a, -self.b)

    def mag2(self):
        return self.a*self.a + self.b*self.b

    def __repr__(self):
        return f'({self.a},{self.b})'


def vecnorm(v):
    return sum((x.mag2() for x in v), F(0))


def inner(u, v):
    return sum((x.conj()*y for x, y in zip(u, v)), G())


def rank(m):
    m = [row[:] for row in m]
    r = 0
    for j in range(len(m[0])):
        piv = next((i for i in range(r, len(m)) if m[i][j]), None)
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        p = m[r][j]
        m[r] = [x/p for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][j]:
                p = m[i][j]
                m[i] = [x-p*y for x,y in zip(m[i],m[r])]
        r += 1
        if r == len(m):
            break
    return r


def grade(a, b, k):
    d = len(a)
    out = [[G() for _ in range(d)] for _ in range(d)]
    for i in range(d):
        out[(i-1)%d][i] = out[(i-1)%d][i] + a[i]
        out[i][i] = out[i][i] + b[(k-i)%d]
    return out


def check(name, ok, detail=''):
    if not ok:
        raise AssertionError(name + ' ' + str(detail))
    print('PASS', name, detail)


# Complex weights retain the two equality grades and a constant block norm.
a = [G(1,1),G(),G(),G()]
b = [G(),G(2,-1),G(),G()]
blocks = [grade(a,b,k) for k in range(4)]
ranks = [rank(g) for g in blocks]
norms = [sum((z.mag2() for row in g for z in row),F(0)) for g in blocks]
check('complex-cyclic-equality-grades', ranks == [1,1,2,2] and norms == [F(7)]*4, (ranks,norms))

# A=E01, u=(0,3i/5,0,0), v=(16/25,12/25,0,0), beta=1/4+i/2.
u = [G(),G(0,F(3,5)),G(),G()]
v = [G(F(16,25)),G(F(12,25)),G(),G()]
Au, Av = [u[1],G(),G(),G()], [v[1],G(),G(),G()]
t, q = vecnorm(u), vecnorm(v)
z, k = inner(u,v), inner(v,Au)
d = F(1)-vecnorm(Au)-vecnorm(Av)
beta = G(F(1,4),F(1,2))
check('complex-tracezero-lemma', t+q == 1 and z.b != 0 and k.b != 0 and k.mag2() <= t*(1+2*q)*d,
      (t,q,z,k,d,k.mag2()))
mixed = 2*(1+beta.mag2())-(vecnorm([x+beta*y for x,y in zip(Au,v)])+vecnorm(Av)+1)
base = (1-2*t*q)*d/(1+t)
right = base+(1+t)*(beta-k/(1+t)).mag2()
wrong = base+(1+t)*(beta-k.conj()/(1+t)).mag2()
check('complex-mixed-square-completion', mixed >= right >= 0, (mixed,right))
check('negative-conjugated-completion', mixed < wrong, (mixed,wrong))
print('ALL COMPLEX EXACT CONTROLS COMPLETED')
