"""Definition-derived Kac certificate mathematics. PREPARE ONLY until parent GO.

Independent positive-lift alphabet; reduced-coproduct completeness; symmetric-wedge
source; Lyndon target; literal module-ideal formulas; recursive Chevalley lowering.
No producer import, external dependencies, file I/O, execution at import or asserts.
"""
from collections import deque
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement

_GUARD = None


class ConsumerError(Exception):
    def __init__(self, code, detail=''):
        self.code, self.detail = code, detail
        super().__init__(code + (': ' + detail if detail else ''))


def configure_guard(callback):
    global _GUARD
    if not callable(callback):
        raise ConsumerError('GUARD_CONFIGURATION')
    _GUARD = callback


def tick():
    if _GUARD is None:
        raise ConsumerError('GUARD_NOT_CONFIGURED')
    _GUARD()


def require(condition, code, detail=''):
    tick()
    if not condition:
        raise ConsumerError(code, detail)


def linear_sum(*terms):
    result = {}
    for scalar, vector in terms:
        if scalar:
            for key, coefficient in vector.items():
                value = result.get(key, Q(0)) + scalar * coefficient
                if value:
                    result[key] = value
                elif key in result:
                    del result[key]
    return result


def tensor_product(left, right):
    result = {}
    for a, x in left.items():
        tick()
        for b, y in right.items():
            word = a + b
            result[word] = result.get(word, Q(0)) + x*y
    return {key: value for key, value in result.items() if value}


def commutator(left, right):
    return linear_sum((1,tensor_product(left,right)),(-1,tensor_product(right,left)))


def leaf(index):
    return {(index,): Q(1)}


def first_variation(polynomial, substitutions):
    """Coefficient of epsilon after b -> b+epsilon*T(b), epsilon^2=0."""
    result = {}
    for word, coefficient in polynomial.items():
        degree_zero, degree_one = {(): coefficient}, {}
        for letter in word:
            tick()
            degree_one = linear_sum((1,tensor_product(degree_one,leaf(letter))),
                                    (1,tensor_product(degree_zero,substitutions[letter])))
            degree_zero = tensor_product(degree_zero,leaf(letter))
        result = linear_sum((1,result),(1,degree_one))
    return result


def gauss_jordan(vectors, tracked=False):
    """Batched full Gauss-Jordan, with optional coordinates in the INPUT rows."""
    rows = [dict(vector) for vector in vectors]
    history = [{i:Q(1)} for i in range(len(rows))] if tracked else None
    columns = sorted({key for row in rows for key in row})
    pivots, rank = [], 0
    for column in columns:
        tick()
        position = next((i for i in range(rank,len(rows)) if rows[i].get(column)),None)
        if position is None:
            continue
        rows[rank],rows[position] = rows[position],rows[rank]
        if tracked:
            history[rank],history[position] = history[position],history[rank]
        factor = rows[rank][column]
        rows[rank] = {key:value/factor for key,value in rows[rank].items()}
        if tracked:
            history[rank] = {key:value/factor for key,value in history[rank].items()}
        for i in range(len(rows)):
            if i != rank and rows[i].get(column):
                factor = rows[i][column]
                rows[i] = linear_sum((1,rows[i]),(-factor,rows[rank]))
                if tracked:
                    history[i] = linear_sum((1,history[i]),(-factor,history[rank]))
        pivots.append(column)
        rank += 1
        if rank == len(rows):
            break
    return rows[:rank],pivots,(history[:rank] if tracked else None)


class LinearSpan:
    def __init__(self, vectors=()):
        self.raw = [dict(vector) for vector in vectors if vector]
        self.rows,self.pivots,_ = gauss_jordan(self.raw)

    @property
    def dimension(self):
        return len(self.rows)

    def normal(self, vector):
        # RREF rows have zero at ALL other pivots: independent annihilating projection.
        return linear_sum((1,vector),*((-vector.get(pivot,Q(0)),row)
                    for pivot,row in zip(self.pivots,self.rows)))

    def contains(self, vector):
        return not self.normal(vector)

    def extend(self, vector):
        if self.contains(vector):
            return False
        self.raw.append(dict(vector))
        self.rows,self.pivots,_ = gauss_jordan(self.raw)
        return True


class Basis(LinearSpan):
    def __init__(self, vectors, expressions):
        self.raw = [dict(vector) for vector in vectors]
        self.expressions = expressions
        self.rows,self.pivots,self.history = gauss_jordan(self.raw,tracked=True)
        require(len(self.rows)==len(self.raw),'FREE_BASIS_DEPENDENT')

    def coordinates(self, vector):
        require(self.contains(vector),'FULL_FREE_SPACE_MEMBERSHIP')
        coefficients = {}
        for pivot,history in zip(self.pivots,self.history):
            coefficients = linear_sum((1,coefficients),(vector.get(pivot,Q(0)),history))
        return coefficients


DEGREE = ((0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2))
OLD_TO_NEW = ((5,Q(-1,2)),(6,Q(1,2)),(7,Q(1,2)),(2,Q(1)),
              (1,Q(-1)),(0,Q(1)),(3,Q(1)),(4,Q(-1)))
NEW_TO_OLD = ((5,Q(1)),(4,Q(-1)),(3,Q(1)),(6,Q(1)),
              (7,Q(-1)),(0,Q(-2)),(1,Q(2)),(2,Q(2)))


def translate(vector, mapping):
    result = {}
    for word, coefficient in vector.items():
        converted, scalar = [], coefficient
        for letter in word:
            new, factor = mapping[letter]
            converted.append(new)
            scalar *= factor
        result[tuple(converted)] = scalar
    return {key:value for key,value in result.items() if value}


def full_degree(vector):
    values = {(sum(DEGREE[i][0] for i in word),sum(DEGREE[i][1] for i in word),len(word))
              for word in vector}
    require(len(values)<=1,'INHOMOGENEOUS_TENSOR')
    return next(iter(values)) if values else None


def coproduct(vector):
    result = {}
    for word, coefficient in vector.items():
        tick()
        for mask in range(1,(1<<len(word))-1):
            left = tuple(letter for i,letter in enumerate(word) if mask & (1<<i))
            right = tuple(letter for i,letter in enumerate(word) if not mask & (1<<i))
            result[(left,right)] = result.get((left,right),Q(0))+coefficient
    return {key:value for key,value in result.items() if value}


def weighted_words(a,b,k):
    if a<0 or b<0 or k<0:
        return []
    if k==0:
        return [()] if (a,b)==(0,0) else []
    result = []
    for letter,(x,y) in enumerate(DEGREE):
        tick()
        if x<=a and y<=b:
            result.extend((letter,)+word for word in weighted_words(a-x,b-y,k-1))
    return result


def matrix_unit(i,j):
    return {(i,j):Q(1)}


def matrix_commutator(left,right):
    # Kronecker-delta structure constants of matrix units, not dense multiplication.
    result = {}
    for (i,j),a in left.items():
        for (k,l),b in right.items():
            if j==k:
                result[(i,l)] = result.get((i,l),Q(0))+a*b
            if l==i:
                result[(k,j)] = result.get((k,j),Q(0))-a*b
    return {key:value for key,value in result.items() if value}


class DefinitionModel:
    def __init__(self):
        e1,e2 = matrix_unit(0,1),matrix_unit(1,2)
        f1,f2 = matrix_unit(1,0),matrix_unit(2,1)
        v = matrix_unit(2,0)
        u,w = matrix_commutator(e1,v),matrix_commutator(e2,v)
        p,q = matrix_commutator(e1,w),matrix_commutator(e2,u)
        x,y = matrix_commutator(e1,p),matrix_commutator(e2,q)
        z = matrix_commutator(e1,y)
        self.matrices = (v,u,w,p,q,x,y,z)
        self.actions = []
        for actor in (e1,e2,f1,f2,matrix_commutator(e1,e2)):
            table = []
            for vector in self.matrices:
                value = matrix_commutator(actor,vector)
                coordinates = (value.get((2,0),0),-value.get((2,1),0),value.get((1,0),0),
                    value.get((0,0),0),value.get((2,2),0),-value.get((0,1),0)/Q(2),
                    value.get((1,2),0)/Q(2),value.get((0,2),0)/Q(2))
                rebuilt = linear_sum(*((coefficient,matrix) for coefficient,matrix
                                       in zip(coordinates,self.matrices)))
                require(rebuilt==value,'MODEL_MATRIX_COORDINATES')
                table.append({(i,):Q(c) for i,c in enumerate(coordinates) if c})
            self.actions.append(tuple(table))
        self._free,self._orbit,self._eval,self._lower = {},{},{},{}
        self._lower_basis = {}
        self.check_levi()

    def act(self,actor,vector):
        return first_variation(vector,self.actions[actor])

    def check_levi(self):
        for i,(a,b) in enumerate(DEGREE):
            vector = leaf(i)
            for e,f,weight in ((0,2,2*a-b-1),(1,3,-a+2*b-1)):
                lhs = linear_sum((1,self.act(e,self.act(f,vector))),
                                 (-1,self.act(f,self.act(e,vector))))
                require(lhs==linear_sum((weight,vector)),'LEVI_CARTAN_ROW')
            for e,f in ((0,3),(1,2)):
                require(self.act(e,self.act(f,vector))==self.act(f,self.act(e,vector)),
                        'LEVI_CROSS_RELATION')
            require(self.act(4,vector)==linear_sum((1,self.act(0,self.act(1,vector))),
                    (-1,self.act(1,self.act(0,vector)))),'LEVI_ROOT_ACTOR')
        # These are the ACTUAL positive-lift definitions, not only an abstract table.
        for actor,source,target in ((0,0,1),(1,0,2),(0,2,3),(1,1,4),
                                    (0,3,5),(1,4,6),(0,6,7)):
            require(self.act(actor,leaf(source))==leaf(target),'POSITIVE_LIFT_IDENTIFICATION')

    def evaluate(self,tree):
        if tree not in self._eval:
            if isinstance(tree,int):
                result = leaf(tree)
            else:
                result = commutator(self.evaluate(tree[0]),self.evaluate(tree[1]))
            self._eval[tree] = result
        return self._eval[tree]

    @staticmethod
    def lyndon(word):
        return all(word<word[i:] for i in range(1,len(word)))

    def lyndon_tree(self,word):
        if len(word)==1:
            return word[0]
        split = next((i for i in range(1,len(word)) if self.lyndon(word[i:])),None)
        require(split is not None,'LYNDON_FACTORIZATION')
        require(self.lyndon(word[:split]),'LYNDON_PREFIX')
        return (self.lyndon_tree(word[:split]),self.lyndon_tree(word[split:]))

    def free(self,a,b,k):
        key = (a,b,k)
        if key in self._free:
            return self._free[key]
        if a<0 or b<0:
            return Basis([],[])
        require(k in (3,4),'UNSUPPORTED_FREE_LEVEL')
        vectors,expressions = [],[]
        if k==4:
            for i,j in combinations_with_replacement(range(8),2):
                for c,d in combinations(range(8),2):
                    tick()
                    if (sum(DEGREE[t][0] for t in (i,j,c,d)),
                        sum(DEGREE[t][1] for t in (i,j,c,d))) != (a,b):
                        continue
                    first,second = (i,(j,(c,d))),(j,(i,(c,d)))
                    vectors.append(linear_sum((1,self.evaluate(first)),(1,self.evaluate(second))))
                    expressions.append((first,second))
        else:
            for word in weighted_words(a,b,k):
                if self.lyndon(word):
                    tree = self.lyndon_tree(word)
                    vectors.append(self.evaluate(tree))
                    expressions.append((tree,))
        basis = Basis(vectors,expressions)
        require(all(not coproduct(vector) for vector in vectors),'FREE_COPRODUCT')
        words = weighted_words(a,b,k)
        constraints = {}
        for word in words:
            for split,coefficient in coproduct({word:Q(1)}).items():
                constraints.setdefault(split,{})[word] = coefficient
        rank = LinearSpan(list(constraints.values())).dimension
        require(len(words)-rank==basis.dimension,'FREE_PRIMITIVE_COMPLETENESS',str(key))
        self._free[key] = basis
        return basis

    def orbit(self,q,j):
        key = (q,j)
        if key in self._orbit:
            return self._orbit[key]
        tree = 1 if j==0 else 2
        for unused in range(q):
            tree = (0,tree)
        seed = self.evaluate(tree)
        require(bool(seed),'SERRE_SEED_ZERO')
        require(not self.act(2,seed) and not self.act(3,seed),'SERRE_SEED_NOT_LOWEST')
        degree = (1,0) if j==0 else (0,1)
        spaces = {degree:LinearSpan([seed])}
        queue = deque([(degree,seed)])
        while queue:
            degree,vector = queue.popleft()
            for actor,step in ((0,(1,0)),(1,(0,1))):
                tick()
                target = (degree[0]+step[0],degree[1]+step[1])
                if max(target)>3:
                    continue
                value = self.act(actor,vector)
                if value:
                    space = spaces.setdefault(target,LinearSpan())
                    if space.extend(value):
                        queue.append((target,value))
        for (a,b),space in spaces.items():
            for vector in space.rows:
                require(not coproduct(vector),'SERRE_MODULE_NOT_LIE')
                for actor,target in ((2,(a-1,b)),(3,(a,b-1))):
                    parent = spaces.get(target,LinearSpan())
                    require(parent.contains(self.act(actor,vector)),'SERRE_MODULE_LOWERING')
        self._orbit[key] = spaces
        return spaces

    def relation_weight(self,q,j,a,b):
        if a<0 or b<0 or a>3 or b>3:
            return []
        return self.orbit(q,j).get((a,b),LinearSpan()).rows

    def lower_tree(self,tree):
        if tree in self._lower:
            return self._lower[tree]
        if isinstance(tree,int):
            # actor -> (constant,r,s) coefficients, from actual Chevalley lifts.
            table = {0:('h3',(Q(-1),Q(0),Q(0))),1:(0,(Q(0),Q(-1),Q(0))),
                     2:(1,(Q(0),Q(0),Q(-1))),3:(4,(Q(0),Q(0),Q(-1))),
                     4:(4,(Q(0),Q(1),Q(0)))}
            result = (({},{},{}),({table[tree][0]:table[tree][1]} if tree in table else {}))
        else:
            left,right = tree
            lp,la = self.lower_tree(left)
            rp,ra = self.lower_tree(right)
            a,b = self.evaluate(left),self.evaluate(right)
            positive = [linear_sum((1,commutator(lp[i],b)),(1,commutator(a,rp[i])))
                        for i in range(3)]
            for side,actors,other in ((1,la,b),(-1,ra,a)):
                for actor,coefficient in actors.items():
                    if actor=='h3':
                        require(coefficient[1:]==(Q(0),Q(0)),'NONAFFINE_H3_ACTOR')
                        x,y,k = full_degree(other)
                        slots = (2*k,-x,-y)
                        for i in range(3):
                            positive[i] = linear_sum((1,positive[i]),
                                       (side*coefficient[0]*slots[i],other))
                    else:
                        action = self.act(actor,other)
                        for i in range(3):
                            positive[i] = linear_sum((1,positive[i]),(side*coefficient[i],action))
            result = (tuple(positive),{})
        self._lower[tree] = result
        return result

    def terminal_check(self,vector):
        functionals = ({0:Q(-1)},{1:Q(-1)},{2:Q(-1)},
                       {3:Q(-1)},{4:Q(1)})
        for functional in functionals:
            substitutions = tuple(({():functional[i]} if i in functional else {}) for i in range(8))
            require(not first_variation(vector,substitutions),'TERMINAL_ACTOR_RESIDUAL')

    def raw_lowering(self,vector,a,b):
        basis = self.free(a,b,4)
        coordinates = basis.coordinates(vector)
        result = [{},{},{}]
        for index,coefficient in coordinates.items():
            cache_key = (a,b,index)
            if cache_key not in self._lower_basis:
                slots = [{},{},{}]
                for tree in basis.expressions[index]:
                    positive,actors = self.lower_tree(tree)
                    require(not actors,'UNHANDLED_LEVEL_ZERO_ACTOR')
                    for i in range(3):
                        slots[i] = linear_sum((1,slots[i]),(1,positive[i]))
                self._lower_basis[cache_key] = tuple(slots)
            for i,value in enumerate(self._lower_basis[cache_key]):
                result[i] = linear_sum((1,result[i]),(coefficient,value))
        return tuple(result)


class CellModel:
    def __init__(self,model,r,s):
        self.model,self.r,self.s = model,r,s
        self._ideals = {}
        self._lowest = {}

    def ideal(self,a,b,k):
        key = (a,b,k)
        if key in self._ideals:
            return self._ideals[key]
        if a<0 or b<0:
            return LinearSpan()
        require(k in (3,4),'UNSUPPORTED_IDEAL_LEVEL')
        vectors = []
        for j,category in enumerate((self.r,self.s)):
            if category==1:
                if k==3:
                    for i,(x,y) in enumerate(DEGREE):
                        for relation in self.model.relation_weight(1,j,a-x,b-y):
                            vectors.append(commutator(leaf(i),relation))
                else:
                    for i,(x,y) in enumerate(DEGREE):
                        for t,(xx,yy) in enumerate(DEGREE):
                            for relation in self.model.relation_weight(1,j,a-x-xx,b-y-yy):
                                vectors.append(commutator(leaf(i),commutator(leaf(t),relation)))
            elif category==2:
                if k==3:
                    vectors.extend(self.model.relation_weight(2,j,a,b))
                else:
                    for i,(x,y) in enumerate(DEGREE):
                        for relation in self.model.relation_weight(2,j,a-x,b-y):
                            vectors.append(commutator(leaf(i),relation))
            elif category==3 and k==4:
                vectors.extend(self.model.relation_weight(3,j,a,b))
        full = self.model.free(a,b,k)
        require(all(full.contains(vector) for vector in vectors),'IDEAL_NOT_IN_FULL_FREE_SPACE')
        result = LinearSpan(vectors)
        self._ideals[key] = result
        return result

    def lowest(self,a,b):
        key = (a,b)
        if key in self._lowest:
            return self._lowest[key]
        source = self.model.free(a,b,4)
        ideal = self.ideal(a,b,4)
        parents = (self.ideal(a-1,b,4),self.ideal(a,b-1,4))
        columns,unreduced = [],[]
        for vector in source.raw:
            pair,pair_free = {},{}
            for tag,actor in enumerate((2,3)):
                image = self.model.act(actor,vector)
                for word,value in image.items():
                    pair_free[(tag,word)] = value
                for word,value in parents[tag].normal(image).items():
                    pair[(tag,word)] = value
            columns.append(pair)
            unreduced.append(pair_free)
        for vector in ideal.rows:
            for tag,actor in enumerate((2,3)):
                require(parents[tag].contains(self.model.act(actor,vector)),
                        'SOURCE_IDEAL_LEVI_STABILITY')
        quotient_dimension = source.dimension-LinearSpan(columns).dimension-ideal.dimension
        free_dimension = source.dimension-LinearSpan(unreduced).dimension
        require(0<=quotient_dimension<=free_dimension<=8,'LOWEST_DIMENSION_RANGE')
        self._lowest[key] = (quotient_dimension,free_dimension)
        return self._lowest[key]

    def affine_cell(self,slots,swap_original_row=False):
        constant,rpart,spart = slots
        if swap_original_row:
            rpart,spart = spart,rpart
        return (linear_sum((1,constant),(self.r,rpart),(self.s,spart)),
                rpart if self.r==4 else {},spart if self.s==4 else {})


def polynomial_add(*terms):
    return linear_sum(*terms)


def polynomial_multiply(left,right):
    result = {}
    for (a,b),x in left.items():
        tick()
        for (c,d),y in right.items():
            exponent = (a+c,b+d)
            result[exponent] = result.get(exponent,Q(0))+x*y
    return {key:value for key,value in result.items() if value}


def polynomial_exact_divide(numerator,denominator):
    require(bool(denominator),'BAREISS_ZERO_DIVISOR')
    if not numerator:
        return {}
    if set(denominator)=={(0,0)}:
        return {key:value/denominator[(0,0)] for key,value in numerator.items()}
    result,remainder = {},dict(numerator)
    leading = max(denominator)
    while remainder:
        tick()
        monomial = max(remainder)
        require(all(monomial[i]>=leading[i] for i in (0,1)),'BAREISS_NONEXACT_DIVISION')
        exponent = (monomial[0]-leading[0],monomial[1]-leading[1])
        coefficient = remainder[monomial]/denominator[leading]
        result[exponent] = result.get(exponent,Q(0))+coefficient
        remainder = polynomial_add((1,remainder),
                    (-1,polynomial_multiply({exponent:coefficient},denominator)))
    return {key:value for key,value in result.items() if value}


def bareiss_determinant(matrix):
    n = len(matrix)
    require(all(len(row)==n for row in matrix),'MINOR_NOT_SQUARE')
    if n==0:
        return {(0,0):Q(1)}
    work = [[dict(value) for value in row] for row in matrix]
    previous,orientation = {(0,0):Q(1)},1
    for k in range(n-1):
        tick()
        if not work[k][k]:
            replacement = next((i for i in range(k+1,n) if work[i][k]),None)
            if replacement is None:
                return {}
            work[k],work[replacement] = work[replacement],work[k]
            orientation *= -1
        pivot = work[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator = polynomial_add((1,polynomial_multiply(work[i][j],pivot)),
                              (-1,polynomial_multiply(work[i][k],work[k][j])))
                work[i][j] = polynomial_exact_divide(numerator,previous)
        for i in range(k+1,n):
            work[i][k] = {}
        previous = pivot
    return polynomial_add((orientation,work[-1][-1]))
