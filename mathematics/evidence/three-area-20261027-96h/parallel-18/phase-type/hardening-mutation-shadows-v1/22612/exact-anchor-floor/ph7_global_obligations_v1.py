"""Definition-bound exact GLOBAL certificate obligations, unexecuted on science.

Sections refer to the frozen b2b7770d...59ca5 manuscript. Every spatial leaf
must satisfy a named selector on the *entire* parameter domain. No floating
arithmetic is used for coefficients, boxes, paths, anchors, or signs.
"""
from fractions import Fraction as Q
from itertools import combinations, product
import math

OBLIGATIONS = ('QO', 'HO', 'NB', 'MC', 'R3', 'SB', 'MP')
MAX_PATH_DEPTH = 100
MAX_LEAVES_PER_COVER = 2000000
MAX_TENSOR_COEFFICIENTS = 5000000

class ProofError(Exception):
    def __init__(self, code, detail=''):
        super().__init__(f'{code}: {detail}')
        self.code, self.detail = str(code), str(detail)

def require(condition, code, detail=''):
    if not condition:
        raise ProofError(code, detail)

def _r(value):
    try:
        require(not isinstance(value, (float, bool)), 'NONEXACT_RATIONAL', repr(value))
        return Q(value)
    except (ValueError, TypeError, ZeroDivisionError) as e:
        raise ProofError('INVALID_RATIONAL', repr(value)) from e

def _lcm(a, b): return a//math.gcd(a, b)*b

def _flat_strides(shape):
    return [math.prod(shape[i+1:]) for i in range(len(shape))]

class Tensor:
    """Scaled exact tensor Bernstein coefficients. All scale factors positive."""
    def __init__(self, values, shape, scale):
        require(type(scale) is int and scale > 0, 'TENSOR_SCALE')
        require(all(type(s) is int and s > 0 for s in shape), 'TENSOR_SHAPE')
        require(len(values) == math.prod(shape), 'TENSOR_SIZE')
        self.values, self.shape, self.scale = values, tuple(shape), scale
    def split(self, axis, guard):
        require(type(axis) is int and 0 <= axis < len(self.shape), 'SPLIT_AXIS')
        n = self.shape[axis]; d = n-1; stride = math.prod(self.shape[axis+1:])
        left = [0]*len(self.values); right = [0]*len(self.values)
        other = [range(s) for i, s in enumerate(self.shape) if i != axis]
        strides = [math.prod(self.shape[i+1:]) for i in range(len(self.shape)) if i != axis]
        for row, coords in enumerate(product(*other)):
            if row % 4096 == 0: guard()
            base = sum(a*b for a, b in zip(coords, strides))
            inds = [base+j*stride for j in range(n)]
            levels = [[self.values[i] for i in inds]]
            while len(levels[-1]) > 1:
                levels.append([a+b for a, b in zip(levels[-1], levels[-1][1:])])
            for k in range(n):
                left[inds[k]] = levels[k][0]*(1 << (d-k))
                right[inds[k]] = levels[d-k][-1]*(1 << k)
        return Tensor(left, self.shape, self.scale*(1 << d)), Tensor(right, self.shape, self.scale*(1 << d))
    def positive(self): return min(self.values) > 0
    def nonnegative(self): return min(self.values) >= 0
    def nonpositive(self): return max(self.values) <= 0
    def negative(self): return max(self.values) < 0

# Affine monomial x^k -> Bernstein degree d coefficient at j.
def affine_entry(j, k, degree, lo, hi):
    return sum((Q(math.comb(k, h))*lo**(k-h)*(hi-lo)**h*Q(math.comb(j, h), math.comb(degree, h))
                for h in range(min(j, k)+1)), Q(0))

def tensor_from_expr(S, expr, variables, bounds, compact, degree, guard):
    """Reconstruct exact coefficients from an expression on one root box.

    Spatial compact axes use x=s/(1-s) and multiply (1-s)^degree.
    Remaining axes (including z, a, b) are affine on the supplied rational box.
    degree is explicit so compatible polynomial families can be elevated.
    """
    n = len(variables)
    require(len(bounds) == n and len(compact) == n and len(degree) == n, 'BASIS_DIMENSION')
    try: poly = S.Poly(expr, *variables, domain=S.QQ)
    except Exception as e: raise ProofError('NOT_RATIONAL_POLYNOMIAL', str(e)) from e
    deg = tuple(degree); shape = tuple(d+1 for d in deg)
    require(all(type(d) is int and d >= 0 for d in deg), 'INVALID_DEGREE')
    require(math.prod(shape) <= MAX_TENSOR_COEFFICIENTS, 'TENSOR_ADMISSION_CAP')
    require(all(poly.degree(v) <= d for v, d in zip(variables, deg)), 'DEGREE_BELOW_POLYNOMIAL')
    strides = _flat_strides(shape); vals = [Q(0)]*math.prod(shape)
    for powers, coeff in poly.terms():
        idx = sum(a*b for a, b in zip(powers, strides))
        vals[idx] = Q(int(coeff.p), int(coeff.q))
    for axis, d in enumerate(deg):
        guard()
        lo, hi = bounds[axis]; lo, hi = _r(lo), _r(hi)
        require(lo < hi, 'DEGENERATE_ROOT_INTERVAL', str(axis))
        if compact[axis]:
            require(lo == 0 and hi == 1, 'COMPACT_DOMAIN')
            matrix = [[Q(int(j == k), math.comb(d, k)) for k in range(d+1)] for j in range(d+1)]
        else:
            matrix = [[affine_entry(j, k, d, lo, hi) for k in range(d+1)] for j in range(d+1)]
        new = [Q(0)]*len(vals); stride = strides[axis]
        other = [range(s) for i, s in enumerate(shape) if i != axis]
        ost = [strides[i] for i in range(n) if i != axis]
        for row, coord in enumerate(product(*other)):
            if row % 4096 == 0: guard()
            base = sum(a*b for a, b in zip(coord, ost))
            old = [vals[base+k*stride] for k in range(d+1)]
            for j in range(d+1):
                new[base+j*stride] = sum((matrix[j][k]*old[k] for k in range(d+1)), Q(0))
        vals = new
    den = 1
    for v in vals: den = _lcm(den, v.denominator)
    return Tensor([int(v*den) for v in vals], shape, den)

def cell_bounds(path, spatial_bounds):
    bounds = [(_r(a), _r(b)) for a, b in spatial_bounds]
    n = len(bounds)
    for depth, bit in enumerate(path):
        axis = depth % n; lo, hi = bounds[axis]; mid = (lo+hi)/2
        bounds[axis] = (lo, mid) if bit == '0' else (mid, hi)
    return tuple(bounds)

def parse_cover(leaves, dimension, valid_labels):
    require(isinstance(leaves, list) and 0 < len(leaves) <= MAX_LEAVES_PER_COVER, 'LEAF_COUNT')
    trie = {}
    for entry in leaves:
        require(isinstance(entry, dict) and set(entry) == {'path', 'label'}, 'LEAF_SCHEMA')
        path, label = entry['path'], entry['label']
        require(isinstance(path, str) and len(path) <= MAX_PATH_DEPTH and all(c in '01' for c in path), 'PATH_SYNTAX')
        require(label in valid_labels, 'UNKNOWN_LEAF_LABEL', str(label))
        node = trie
        for bit in path:
            require('_leaf' not in node, 'PATH_PREFIX_CONFLICT', path)
            node = node.setdefault(bit, {})
        require(not node, 'DUPLICATE_OR_PREFIX_PATH', path)
        node['_leaf'] = label
    stack = [trie]
    while stack:
        node = stack.pop()
        if '_leaf' in node:
            require(set(node) == {'_leaf'}, 'PATH_PREFIX_CONFLICT')
        else:
            require(set(node) == {'0', '1'}, 'INCOMPLETE_PATH_COVER')
            stack.extend((node['0'], node['1']))
    return trie

def unsorted(bounds):
    return any(bounds[i][0] > bounds[j][1] for i in range(len(bounds)) for j in range(i+1, len(bounds)))

def _corner_positive(t, bounds, spatial_dimension):
    """Interior compact corners strict at all parameter Bernstein indices."""
    shape = t.shape; strides = _flat_strides(shape); seen = 0
    for corner in product((0, 1), repeat=spatial_dimension):
        coord = [bounds[j][corner[j]] for j in range(spatial_dimension)]
        if all(0 < x < 1 for x in coord):
            seen += 1
            base = sum((0 if corner[j] == 0 else shape[j]-1)*strides[j] for j in range(spatial_dimension))
            for p in product(*[range(d) for d in shape[spatial_dimension:]]):
                idx = base+sum(k*strides[spatial_dimension+i] for i, k in enumerate(p))
                if t.values[idx] <= 0: return False
    return seen > 0

def _all(tensors, names, mode):
    require(all(k in tensors for k in names), 'MISSING_TENSOR')
    if mode == 'positive': return all(tensors[k].positive() for k in names)
    if mode == 'nonnegative': return all(tensors[k].nonnegative() for k in names)
    if mode == 'nonpositive': return all(tensors[k].nonpositive() for k in names)
    if mode == 'negative': return all(tensors[k].negative() for k in names)
    raise ProofError('UNKNOWN_SIGN_MODE', mode)

def _combination(tensors, weights, sign):
    require(len(tensors) == len(weights) and tensors, 'COMBINATION_ARITY')
    shape = tensors[0].shape
    require(all(t.shape == shape for t in tensors), 'COMMON_BASIS_MISMATCH')
    for col in zip(*(t.values for t in tensors)):
        val = sum((Q(c, t.scale)*w for c, t, w in zip(col, tensors, weights)), Q(0))
        if sign == 'positive' and not val > 0: return False
        if sign == 'negative' and not val < 0: return False
        if sign == 'nonpositive' and not val <= 0: return False
    return True

def make_definitions(S):
    """Rebuild Sections 3–8, including algebraic identity guards."""
    u = S.symbols('v1:8'); x = u[6]; z, a, b = S.symbols('z a b')
    def es(vs, k): return sum(S.prod(c) for c in combinations(vs, k)) if k else S.Integer(1)
    e = [es(u, k) for k in range(8)]; f = [es(u[:6], k) for k in range(5)]
    p = e[1]-4; q = e[2]-4*e[1]+10-2*z
    W = e[3]-4*e[2]+(10-2*z)*e[1]+12*z-20
    E3 = e[4]-(6+2*z)*e[2]+(20+4*z)*e[1]+3*z*z+6*z-45
    E2 = e[5]-(1+z)**2*p-(4+4*z)*q; E1 = e[6]-(1+z)**2*q
    s = u[0]+u[1]; S3 = sum(u[:3]); S4 = sum(u[:4]); L4 = sum(u[3:])
    K = E3-W*S4; alpha = es(u[:4], 3)-s*es(u[3:], 2); Bjoint = u[0]*u[1]-s*s
    Z = E1-s*E2; Yjoint = Z-W*alpha-K*Bjoint+W*W/2
    Y2 = E2-W*es(u[:4], 2)-S3*(E3-W*L4)
    AA = f[2]-4*f[1]+10-2*z; BB = f[3]-4*f[2]+(10-2*z)*f[1]+12*z-20
    h1 = f[3]-(6+2*z)*f[1]+20+4*z; h0 = f[4]-(6+2*z)*f[2]+(20+4*z)*f[1]+3*z*z+6*z-45
    D = h1-AA*S4; E = h0-BB*S4; Qpol = AA*AA-(f[1]-4)*BB; Hpol = -(h0*AA-h1*BB)
    require(S.expand(W-AA*x-BB) == 0 and S.expand(K-E-D*x) == 0, 'IDENTITY_LINEAR_REDUCTION')
    y2 = S.Poly(S.expand(Y2), x); yj = S.Poly(S.expand(Yjoint), x)
    require(y2.degree() == 2 and S.expand(y2.nth(2)-S3*AA) == 0, 'IDENTITY_Y2_QUADRATIC')
    require(yj.degree() == 2, 'IDENTITY_YJOINT_QUADRATIC')
    F = Z+a*W+b*E3-E3*E3
    lam = a+alpha+b*S4-W/2-S4*E3; mu = b+Bjoint-E3
    require(S.expand(F-Yjoint-lam*W-mu*K) == 0, 'IDENTITY_DUAL')
    g = u[0]*u[1]*u[2]-W
    Y0 = e[7]-W*es(u[:4], 4)+W*W*x/2-g*(E3-W*L4)
    y0 = S.Poly(S.expand(Y0), x)
    require(y0.degree() == 3 and S.expand(y0.nth(3)+AA*AA/2) == 0, 'IDENTITY_Y0_CUBIC')
    la = S.Poly(S.expand(lam), x); mm = S.Poly(S.expand(mu), x)
    require(la.degree() == 1 and mm.degree() == 1, 'IDENTITY_DUAL_LINEAR')
    def endpoint(poly, v1, v0): return S.expand(poly.nth(2)*v0*v0-poly.nth(1)*v1*v0+poly.nth(0)*v1*v1)
    y, tau, gam = S.symbols('y tau gam'); beta = y/2+gam; al2 = S.Rational(3,8)*tau*y*y
    abar = al2-4*y+10-2*z+beta*(y-4)+beta*beta/4
    dbar = 4*y*y-16*y+20+4*z-S.Rational(5,6)*y*al2+beta*(al2-y*y+4*y-6-2*z)
    fminus = y+beta-4
    def phi(i, j):
        rem = [v for k, v in enumerate(u) if k not in (i,j)]
        cc = s*(4+4*z)-(1+z)**2
        val = es(rem,4)-s*es(rem,3)+(b-2*E3)*es(rem,2)+a*es(rem,1)+cc-4*a-(6+2*z)*(b-2*E3)
        require(S.expand(S.diff(F,u[i])-S.diff(F,u[j])+(u[i]-u[j])*val) == 0, 'IDENTITY_SCHUR', f'{i},{j}')
        return val
    ph12, ph34 = phi(0,1), phi(2,3)
    Ug, Vg = S.symbols('Ug Vg')
    grouped = F.subs({u[0]:Vg,u[1]:Vg,u[2]:Ug,u[3]:Ug,u[4]:Ug,u[5]:Ug,u[6]:Ug})
    c = [y0.nth(i) for i in range(4)]
    # Expressions to certify positive unless a sign mode explicitly differs.
    core = {
        'Q': Qpol, 'H': Hpol,
        'Fsmall': 4-f[1], 'A': AA, 'mA': -AA, 'Fm': f[1]-4, 'D': D,
        'mE46': -(AA*u[5]+BB), 'mG6': -y2.as_expr().subs(x,u[5]), 'mD6': -S.diff(y2.as_expr(),x).subs(x,u[5]),
        'mDisc': -(y2.nth(1)**2-4*y2.nth(2)*y2.nth(0)),
        'g0': u[0]*u[1]*u[2]-BB, 'c0': c[0], 'c1': c[1], 'c2': c[2], 'c3': c[3],
        'mD': -D, 'Yc2': yj.nth(2), 'mEndL': -endpoint(yj,AA,BB), 'mEndH': -endpoint(yj,D,E),
        'blockLow': -BB-S.Rational(127,100)*AA, 'blockHigh': -E-S.Rational(29,20)*D,
        'lamLow': AA*la.nth(0)-BB*la.nth(1), 'lamHigh': -D*la.nth(0)+E*la.nth(1),
        'muLow': AA*mm.nth(0)-BB*mm.nth(1), 'muHigh': -D*mm.nth(0)+E*mm.nth(1),
        'resA': 144*abar, 'resD': 144*dbar, 'resF': 2*fminus,
        'mF': -F, 'phi12': ph12, 'phi34': ph34, 'mGroupedF': -grouped,
    }
    return {'u':u, 'z':z, 'a':a, 'b':b, 'y':y, 'tau':tau, 'gam':gam,
            'Ug':Ug, 'Vg':Vg, 'polynomials':core}

SELECTORS = {
    'QO': {'pos': ('Q',), 'R': ()},
    'HO': {'pos': ('H',), 'R': ()},
    'NB': {'unsorted': (), 'F': ('Fsmall',), 'A': ('A',), 'Q': ('Q',),
           'E4v6': ('mA','mE46'), 'Y2v6': ('mA','mG6','mD6'), 'Disc': ('mA','mDisc'),
           'adaptiveY0': ('mA','Fm','g0','c0','c1','c2','c3')},
    'MC': {'unsorted': (), 'mA': ('mA',), 'D': ('D',), 'H': ('H',),
           'jointEnd': ('A','mD','Yc2','mEndL','mEndH'),
           'SchurBlock': ('A','mD','blockLow','blockHigh','lamLow','lamHigh','muLow','muHigh')},
    'R3': {'Abar<=0': ('resA',), 'Dbar<=0': ('resD',), 'f1-4<0': ('resF',)},
    'SB': {'Fnegative': ('mF',), 'Schur': ('phi12','phi34')},
    'MP': {'Fnegative': ('mGroupedF',), 'local': ()},
}

class GlobalVerifier:
    """Rebuild and check every named cover; no certificate-side polynomials trusted."""
    def __init__(self, sympy, local_cert, guard):
        self.S = sympy; self.guard = guard; self.defs = make_definitions(sympy)
        require(isinstance(local_cert, dict), 'LOCAL_CERTIFICATE_SCHEMA')
        self.z0 = Q(410210220392063003, 500000000000000000); self.r = Q(1,10**16)
        self.U0 = Q(334696976789746519,250000000000000000)
        self.V0 = Q(208405938226799943,200000000000000000); self.rho = Q(1,500)
        require(local_cert.get('rho') == '1/500' and local_cert.get('delta_z') == '1/500', 'LOCAL_CERTIFICATE_RADIUS')
        require(local_cert.get('refined_root_center') == [str(self.U0),str(self.V0),str(self.z0)] and local_cert.get('refined_root_radius') == str(self.r), 'LOCAL_CERTIFICATE_ROOT')
        self.za = (self.z0-self.r, self.z0+2*self.r)
        self.ai = tuple(_r(x) for x in local_cert['dual_a_interval']); self.bi = tuple(_r(x) for x in local_cert['dual_b_interval'])
        require(len(self.ai) == len(self.bi) == 2 and self.ai[0] < self.ai[1] and self.bi[0] < self.bi[1], 'LOCAL_CERTIFICATE_DUAL')

    def _spec(self, kind):
        d=self.defs; u=d['u']; z=d['z']; a=d['a']; b=d['b']
        if kind in ('QO','HO'):
            return (list(u[:6])+[z], [(Q(0),Q(1))]*6+[self.za], [True]*6+[False], 6)
        if kind == 'NB': return (list(u[:6])+[z], [(Q(5,11),Q(37,27))]*6+[self.za], [False]*7, 6)
        if kind == 'MC': return (list(u[:6])+[z,a,b], [(Q(7,9),Q(5,3))]*6+[self.za,self.ai,self.bi], [False]*9, 6)
        if kind == 'R3': return ([d['y'],d['tau'],d['gam'],z], [(Q(0),Q(1))]*3+[self.za], [True,False,True,False], 3)
        if kind == 'SB': return (list(u)+[z,a,b], [(Q(1),Q(11,10))]*2+[(Q(127,100),Q(29,20))]*5+[self.za,self.ai,self.bi], [False]*10, 7)
        if kind == 'MP': return ([d['Ug'],d['Vg'],z,a,b], [(Q(127,100),Q(29,20)),(Q(1),Q(11,10)),self.za,self.ai,self.bi], [False]*5, 2)
        raise ProofError('UNKNOWN_OBLIGATION', kind)

    def _make_roots(self, kind, needed):
        S=self.S; p=self.defs['polynomials']; variables, bounds, compact, n = self._spec(kind)
        degrees = {}
        for name in needed:
            poly=S.Poly(p[name],*variables,domain=S.QQ)
            degrees[name]=[max(0,int(poly.degree(v))) for v in variables]
        if kind == 'NB':
            family=('mA','Fm','g0')
            if all(k in needed for k in family):
                common=[max(degrees[k][i] for k in family) for i in range(len(variables))]
                for k in family: degrees[k]=common
            family=('c0','c1','c2','c3')
            if all(k in needed for k in family):
                common=[max(degrees[k][i] for k in family) for i in range(len(variables))]
                require(common[:6] == [2,2,2,3,3,3], 'Y0_COMMON_DEGREE_MISMATCH')
                for k in family: degrees[k]=common
        return {k:tensor_from_expr(S,p[k],variables,bounds,compact,degrees[k],self.guard) for k in needed}

    def _adaptive(self, tensors, bounds):
        require(_all(tensors,('mA','Fm'),'positive'), 'Y0_ANCHOR_PRECONDITIONS')
        ma, fm=tensors['mA'],tensors['Fm']
        require(ma.shape == fm.shape, 'Y0_ANCHOR_COMMON_BASIS')
        ratios=[Q(a,ma.scale)/Q(b,fm.scale) for a,b in zip(ma.values,fm.values)]
        require(all(q > 0 for q in ratios), 'Y0_ANCHOR_RATIO')
        lower=max(min(ratios),bounds[5][0]); t=Q((lower*1024).__ceil__(),1024)
        require(t >= 0 and t <= lower, 'Y0_ANCHOR_INTERVAL')
        require(_combination([tensors['g0'],ma],[Q(1),t],'positive'), 'Y0_ANCHOR_G')
        cs=[tensors['c0'],tensors['c1'],tensors['c2'],tensors['c3']]
        require(_combination(cs,[Q(1),t,t*t,t*t*t],'negative'), 'Y0_ANCHOR_VALUE')
        require(_combination(cs,[Q(0),Q(1),2*t,3*t*t],'nonpositive'), 'Y0_ANCHOR_D1')
        require(_combination(cs,[Q(0),Q(0),Q(2),6*t],'nonpositive'), 'Y0_ANCHOR_D2')

    def _leaf(self, kind, label, tensors, bounds, path):
        names=SELECTORS[kind][label]
        if label == 'unsorted': require(unsorted(bounds), 'SORTED_CELL_NOT_EMPTY'); return
        if kind in ('QO','HO'):
            if label == 'R':
                box=(Q(5,16),Q(37,64)) if kind == 'QO' else (Q(7,16),Q(5,8))
                require(all(box[0] <= lo and hi <= box[1] for lo,hi in bounds), 'OUTER_EXCLUDED_BOX'); return
            require(len(path)>=6 and tensors[names[0]].nonnegative() and _corner_positive(tensors[names[0]],bounds,6), 'OUTER_OPEN_POSITIVITY'); return
        if kind == 'R3':
            require(_all(tensors,names,'negative' if label=='f1-4<0' else 'nonpositive'), 'RESIDUAL_SIGN', label); return
        if kind == 'MP' and label == 'local':
            inner=((self.U0-self.rho+self.r,self.U0+self.rho-self.r),(self.V0-self.rho+self.r,self.V0+self.rho-self.r))
            require(all(a <= lo and hi <= b for (lo,hi),(a,b) in zip(bounds,inner)), 'MEAN_LOCAL_BOX'); return
        if kind == 'NB' and label == 'adaptiveY0': self._adaptive(tensors,bounds); return
        if kind == 'NB' and label == 'Y2v6':
            require(_all(tensors,('mA','mG6'),'positive') and _all(tensors,('mD6',),'nonnegative'), 'Y2_AT_V6'); return
        if kind == 'MC' and label == 'SchurBlock':
            rectangle=[(Q(1),Q(11,10))]*2+[(Q(127,100),Q(29,20))]*4
            require(all(a <= lo and hi <= b for (lo,hi),(a,b) in zip(bounds,rectangle)), 'SCHUR_BLOCK_RATES')
            require(_all(tensors,('A','mD','lamLow','lamHigh','muLow','muHigh'),'positive'), 'SCHUR_BLOCK_STRICT')
            require(_all(tensors,('blockLow','blockHigh'),'nonnegative'), 'SCHUR_BLOCK_ENDPOINTS'); return
        require(_all(tensors,names,'positive'), 'LEAF_SIGN', f'{kind}:{label}')

    def verify_cover(self, kind, leaves):
        require(kind in OBLIGATIONS, 'UNKNOWN_OBLIGATION', kind)
        trie=parse_cover(leaves, self._spec(kind)[3], SELECTORS[kind]); deps=SELECTORS[kind]
        def annotate(node):
            if '_leaf' in node: return set(deps[node['_leaf']])
            left=annotate(node['0']); right=annotate(node['1']); node['_need0']=left; node['_need1']=right
            return left|right
        needed=annotate(trie); roots=self._make_roots(kind,needed)
        initial=tuple(self._spec(kind)[1][:self._spec(kind)[3]])
        counts={}
        def walk(node,path,tensors,bounds):
            self.guard()
            if '_leaf' in node:
                lab=node['_leaf']; self._leaf(kind,lab,tensors,bounds,path); counts[lab]=counts.get(lab,0)+1; return
            axis=len(path)%len(bounds); lo,hi=bounds[axis]; mid=(lo+hi)/2
            halves={k:t.split(axis,self.guard) for k,t in tensors.items()}
            for idx,bit in enumerate('01'):
                child=node[bit]; want=node['_need'+bit]
                bb=list(bounds); bb[axis]=(lo,mid) if bit=='0' else (mid,hi)
                walk(child,path+bit,{k:h[idx] for k,h in halves.items() if k in want},tuple(bb))
        walk(trie,'',roots,initial)
        require(sum(counts.values())==len(leaves), 'VISITED_LEAF_MISMATCH', kind)
        return counts

    def verify_bundle(self, bundle):
        require(isinstance(bundle,dict) and set(bundle)=={'schema_version','kind','candidate_sha256','covers'}, 'BUNDLE_SCHEMA')
        require(bundle['schema_version']==1 and bundle['kind']=='PH7_GLOBAL_COVERS_V1', 'BUNDLE_VERSION')
        require(bundle['candidate_sha256']=='b2b7770d8b024782c5d0c1cfbd8f6e01368892801d1f3882e7b3279b59059ca5', 'BUNDLE_CANDIDATE_PIN')
        covers=bundle['covers']; require(isinstance(covers,dict) and set(covers)==set(OBLIGATIONS), 'OBLIGATION_SET_MISMATCH')
        return {name:self.verify_cover(name,covers[name]) for name in OBLIGATIONS}
