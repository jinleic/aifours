"""Closed coefficients for the mixed quadratic/cubic F/G seed branch.

The mathematical proof, including all-N scope, belongs to RESULTS.md. This
module does not infer a theorem from finite checks. alpha = 3*c3/(2*c2), and
alpha=0 is the quadratic branch, not a numerical limiting computation.
"""
from itertools import combinations


def pfaffian(indices, entry, one):
    """Exact pairing expansion, with the displayed index order fixing signs."""
    if not indices:
        return one
    first = indices[0]
    value = one * 0
    for j in range(1, len(indices)):
        remaining = indices[1:j] + indices[j+1:]
        value += (-1)**(j+1) * entry(first, indices[j]) * pfaffian(remaining, entry, one)
    return value


def mixed_coefficients(ks, ls, types, amplitudes, alpha):
    """Return F_S,G_S, bitmask S using the sibling Hirota coefficient convention.

    types is a sequence of 'F'/'G'; each amplitude is the sole active seed
    amplitude. Denominators in the explicit formula must be nonzero. The
    auxiliary index 0 is F-type with k_0=l_0=0; active index i+1 is bit i.
    """
    n = len(ks)
    if not (len(ls) == len(types) == len(amplitudes) == n):
        raise ValueError('Equal parameter-list lengths are required')
    if any(t not in ('F', 'G') for t in types):
        raise ValueError('Seed types must be F or G')
    one = ks[0]**0 if n else alpha**0
    zero = one * 0
    k = [zero] + list(ks)
    l = [zero] + list(ls)
    eps = [1] + [1 if t == 'F' else -1 for t in types]
    a = [one if e == 1 else zero for e in eps]
    b = [one if e == -1 else zero for e in eps]

    def pair(i, j):
        if eps[i] == eps[j]:
            return (k[i]-k[j]) / (eps[i] + alpha*(k[i]+k[j]))
        return ((eps[i]-eps[j])//2 + alpha*(k[i]-k[j])) / (k[i]+k[j])

    def entry(component, i, j):
        if j == -1:
            return a[i] if component == 'F' else b[i]
        if component == 'F':
            return (a[i]*b[j]*l[i]-a[j]*b[i]*l[j])/(l[i]+l[j])
        return (b[i]*a[j]*l[i]-b[j]*a[i]*l[j])/(l[i]+l[j])

    def value(component, selected, use_auxiliary):
        indices = ([0] if use_auxiliary else []) + selected
        factor = one
        for i, j in combinations(indices, 2):
            factor *= pair(i, j)
        for i in selected:
            factor *= amplitudes[i-1]
            if eps[i] == -1:
                factor *= k[i]/(alpha*k[i]-1)
        bordered = indices + ([-1] if len(indices)%2 else [])
        return factor * pfaffian(bordered, lambda i,j: entry(component,i,j), one)

    F, G = [zero]*(1<<n), [zero]*(1<<n)
    for mask in range(1<<n):
        selected = [i+1 for i in range(n) if mask>>i&1]
        charge = sum(eps[i] for i in selected)
        if charge in (0,1):
            F[mask] = value('F',selected,charge==0)
        if charge in (0,-1):
            G[mask] = value('G',selected,charge==-1)
    return F,G
