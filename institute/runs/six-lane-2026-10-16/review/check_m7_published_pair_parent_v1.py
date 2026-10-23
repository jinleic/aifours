"""Definition-level exact check of the published two-MOQLS(7) lower-bound pair.
Psi[i,j,x] = omega**(i*f[x]+j*x)/sqrt(7); Phi[i,j] = |a*i+j>.
For integer coefficients of degree <=6, a polynomial vanishes at primitive omega_7
iff all seven coefficients are equal (Phi_7=1+...+X^6). No floating arithmetic.
Output is exclusively created. Controls separate QLS validity, orthogonality and non-classicality.
"""
import hashlib
import itertools
import json
import sys
from pathlib import Path


def inspect(f, a):
    cells = list(itertools.product(range(7), repeat=2))
    def exponents(cell):
        i, j = cell
        return [(i*f[x] + j*x) % 7 for x in range(7)]
    def zero(p, q):
        ep, eq = exponents(p), exponents(q)
        counts = [0]*7
        for x in range(7):
            counts[(eq[x]-ep[x]) % 7] += 1
        return len(set(counts)) == 1
    def label(p):
        return (a*p[0]+p[1]) % 7
    psi_rows_cols = all(zero(p,q) for p,q in itertools.combinations(cells,2)
                        if p[0]==q[0] or p[1]==q[1])
    phi_rows_cols = all(label(p)!=label(q) for p,q in itertools.combinations(cells,2)
                        if p[0]==q[0] or p[1]==q[1])
    orth = all(label(p)!=label(q) or zero(p,q) for p,q in itertools.combinations(cells,2))
    # Entrywise phase quotients distinguish rays, independently of a basis change.
    rays = {tuple((v-exponents(p)[0])%7 for v in exponents(p)) for p in cells}
    return {'f':f, 'a':a, 'psi_qls':psi_rows_cols, 'phi_qls':phi_rows_cols,
            'mutually_orthogonal':orth, 'psi_distinct_rays':len(rays),
            'non_classical':len(rays)>7, 'norms':'All Psi entries have seven coefficients of modulus1/sqrt(7); Phi entries are unit basis vectors.',
            'distinct_cell_pairs_checked':len(cells)*(len(cells)-1)//2}


def main():
    genuine=inspect([0,6,5,1,3,4,2],4)
    wrong_partner=inspect([0,6,5,1,3,4,2],2)
    classical=inspect([(6*x)%7 for x in range(7)],4)
    ok=(genuine['psi_qls'] and genuine['phi_qls'] and genuine['mutually_orthogonal'] and genuine['non_classical']
        and wrong_partner['psi_qls'] and wrong_partner['phi_qls'] and not wrong_partner['mutually_orthogonal']
        and classical['psi_qls'] and classical['phi_qls'] and classical['mutually_orthogonal'] and not classical['non_classical'])
    result={'status':'PASS' if ok else 'FAIL','scope':'M(7)>=2 only; no upper-bound inference',
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'genuine_pair':genuine,'controls':{'wrong_partner':wrong_partner,'classical_pair':classical}}
    with open(sys.argv[1], 'x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))
    return 0 if ok else 1


if __name__=='__main__':
    raise SystemExit(main())
