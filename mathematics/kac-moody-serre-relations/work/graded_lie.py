"""Finite graded free-Lie/Serre/contragredient computation.

Words are tuples of generator indices 0,...,r-1. Standard Lyndon brackets are
embedded in the free associative algebra. All arithmetic is Q or a stated
prime field; finite-field runs are diagnostics, never a characteristic-zero
proof by themselves. No third-party packages are required.
"""
from __future__ import annotations

from functools import lru_cache
from fractions import Fraction
from itertools import product


def add_scaled(target, source, scale=1):
    for key, value in source.items():
        updated = target.get(key, 0) + scale * value
        if updated:
            target[key] = updated
        else:
            target.pop(key, None)
    return target


def bracket(p, q):
    out = {}
    for u, a in p.items():
        for v, b in q.items():
            value = a * b
            add_scaled(out, {u + v: value, v + u: -value} if u + v != v + u else {})
    return out


@lru_cache(None)
def lyndon(word):
    return bool(word) and all(word < word[k:] + word[:k] for k in range(1, len(word)))


@lru_cache(None)
def factor(word):
    for k in range(1, len(word)):
        if lyndon(word[k:]):
            return word[:k], word[k:]
    raise ValueError('not a composite Lyndon word')


@lru_cache(None)
def expansion(word):
    if len(word) == 1:
        return {word: 1}
    u, v = factor(word)
    return bracket(expansion(u), expansion(v))


class Field:
    def __init__(self, prime=None):
        self.prime = prime

    def value(self, x):
        if self.prime is None:
            return Fraction(x)
        if isinstance(x, Fraction):
            return x.numerator * pow(x.denominator, -1, self.prime) % self.prime
        return x % self.prime

    def inverse(self, x):
        return 1 / x if self.prime is None else pow(x, -1, self.prime)

    def clean(self, row):
        return {k: y for k, x in row.items() if (y := self.value(x))}

    def subtract(self, row, other, scale):
        for key, val in other.items():
            changed = self.value(row.get(key, 0) - scale * val)
            if changed:
                row[key] = changed
            else:
                row.pop(key, None)


class RowSpace:
    """Sparse echelon basis, ordered by smallest nonzero coordinate."""
    def __init__(self, field, rows=()):
        self.field = field
        self.rows = {}
        for row in rows:
            self.add(row)

    def reduce(self, vector):
        row = self.field.clean(vector)
        for pivot in sorted(self.rows):
            if pivot in row:
                self.field.subtract(row, self.rows[pivot], row[pivot])
        return row

    def add(self, vector):
        row = self.reduce(vector)
        if not row:
            return False
        pivot = min(row)
        multiplier = self.field.inverse(row[pivot])
        self.rows[pivot] = {i: self.field.value(a * multiplier) for i, a in row.items()}
        return True

    def basis(self):
        return [self.rows[p] for p in sorted(self.rows)]

    def __len__(self):
        return len(self.rows)


def kernel_of_images(images, field):
    """Kernel of map whose j-th basis-vector image is images[j]."""
    pivots = {}
    kernel = RowSpace(field)
    for j, image in enumerate(images):
        row, witness = field.clean(image), {j: field.value(1)}
        for pivot in sorted(pivots):
            if pivot in row:
                scale = row[pivot]
                old, lift = pivots[pivot]
                field.subtract(row, old, scale)
                field.subtract(witness, lift, scale)
        if not row:
            kernel.add(witness)
        else:
            pivot = min(row)
            inv = field.inverse(row[pivot])
            pivots[pivot] = ({k: field.value(v * inv) for k, v in row.items()},
                             {k: field.value(v * inv) for k, v in witness.items()})
    return kernel, len(pivots)


class FreeLie:
    def __init__(self, rank, height):
        self.rank, self.height = rank, height
        self.words = {}
        self.index = {}
        for degree in range(1, height + 1):
            for word in product(range(rank), repeat=degree):
                if lyndon(word):
                    alpha = tuple(word.count(i) for i in range(rank))
                    self.words.setdefault(alpha, []).append(word)
        for alpha, words in self.words.items():
            self.index[alpha] = {word: j for j, word in enumerate(words)}
        self._ad_cache = {}

    def coordinates(self, polynomial, alpha):
        row = dict(polynomial)
        answer = {}
        index = self.index.get(alpha, {})
        while row:
            word = min(row)
            if word not in index:
                raise ArithmeticError(f'non-Lie leading word {word} in degree {alpha}')
            value = row[word]
            answer[index[word]] = value
            add_scaled(row, expansion(word), -value)
        return answer

    def ad_generator(self, i, alpha, row):
        target = list(alpha)
        target[i] += 1
        target = tuple(target)
        out = {}
        for j, value in row.items():
            key = (i, self.words[alpha][j])
            if key not in self._ad_cache:
                self._ad_cache[key] = self.coordinates(bracket({(i,): 1}, expansion(key[1])), target)
            add_scaled(out, self._ad_cache[key], value)
        return out


def descend_factory(matrix):
    """Recursive derivation; independent checker uses word deletion instead."""
    rank = len(matrix)

    @lru_cache(None)
    def lower(i, word):
        if len(word) == 1:
            raise ValueError('height one descends to Cartan, not positive free Lie')
        u, v = factor(word)
        out = {}
        if len(u) == 1:
            if u[0] == i:
                add_scaled(out, expansion(v), -sum(matrix[i][j] for j in v))
        else:
            add_scaled(out, bracket(lower(i, u), expansion(v)))
        if len(v) == 1:
            if v[0] == i:
                add_scaled(out, expansion(u), sum(matrix[i][j] for j in u))
        else:
            add_scaled(out, bracket(expansion(u), lower(i, v)))
        return out

    return lower


def compute_matrix(matrix, free, field):
    rank = len(matrix)
    ideals, radicals, records = {}, {}, []
    lower = descend_factory(tuple(map(tuple, matrix)))
    original = {}
    for i in range(rank):
        for j in range(rank):
            if i == j:
                continue
            exponent = 1 - matrix[i][j]
            alpha = tuple((exponent if k == i else 1 if k == j else 0) for k in range(rank))
            if sum(alpha) <= free.height:
                poly = {(j,): 1}
                for _ in range(exponent):
                    poly = bracket({(i,): 1}, poly)
                original.setdefault(alpha, []).append(free.coordinates(poly, alpha))
    alphas = sorted(free.words, key=lambda a: (sum(a), a))
    for alpha in alphas:
        words = free.words[alpha]
        ideal = RowSpace(field, original.get(alpha, ()))
        for i in range(rank):
            if not alpha[i]:
                continue
            previous = tuple(a - int(k == i) for k, a in enumerate(alpha))
            if previous in ideals:
                for row in ideals[previous].basis():
                    ideal.add(free.ad_generator(i, previous, row))
        if sum(alpha) == 1:
            radical, image_rank = RowSpace(field), len(words)
        else:
            images = []
            for word in words:
                image = {}
                for i in range(rank):
                    if not alpha[i]:
                        continue
                    previous = tuple(a - int(k == i) for k, a in enumerate(alpha))
                    coords = free.coordinates(lower(i, word), previous)
                    if previous in radicals:
                        coords = radicals[previous].reduce(coords)
                    elif coords:
                        raise ArithmeticError('nonzero descent into absent free-Lie space')
                    for j, value in coords.items():
                        image[(i, j)] = value
                images.append(image)
            radical, image_rank = kernel_of_images(images, field)
        assert all(not radical.reduce(row) for row in ideal.basis()), ('Serre not in radical', alpha)
        ideals[alpha], radicals[alpha] = ideal, radical
        records.append({'alpha': list(alpha), 'free_dim': len(words), 'serre_ideal_rank': len(ideal),
                        'maximal_ideal_rank': len(radical), 'serre_dim': len(words) - len(ideal),
                        'contragredient_dim': len(words) - len(radical), 'descent_rank': image_rank,
                        'extra_relations': len(radical) - len(ideal),
                        'words': [''.join(map(str, w)) for w in words],
                        'ideal_basis': [[[j, str(v)] for j, v in sorted(row.items())] for row in ideal.basis()],
                        'radical_basis': [[[j, str(v)] for j, v in sorted(row.items())] for row in radical.basis()]})
    return records
