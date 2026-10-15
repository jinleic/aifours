#!/usr/bin/env python3
"""Derive human-readable tables and explicit collection-model intervals."""
import csv
from fractions import Fraction
from itertools import permutations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def canonical(n, blocks):
    return min(tuple(sorted(sum(1 << p[i] for i in range(n) if b >> i & 1) for b in blocks))
               for p in permutations(range(n)))


def main():
    certificates = json.loads((ROOT/'evidence/certificates-n5.json').read_text())
    verification = json.loads((ROOT/'evidence/verification-n5.json').read_text())
    collection = json.loads((ROOT/'evidence/collection-bounds.json').read_text())
    assert verification['certified']
    bounds = {x['id']:x for x in collection['records']}
    rows, summary = [], {}
    for r in certificates['records']:
        n = r['n']
        alpha = Fraction(r['lp']['alpha'])
        m = r['minimum_expansion']['m']
        ma = r['expansion_at_maximum_contrast']['m']
        am = Fraction(r['contrast_at_minimum']['gap'], m)
        lower = bounds[r['id']]['minimum_collection_lower_bound']
        lower_ma = ((lower + alpha.denominator-1)//alpha.denominator)*alpha.denominator
        c_m = lower == m
        c_fixed = c_m and r['contrast_at_minimum']['gap'] == (alpha*m).__floor__()
        c_ma = lower_ma == ma
        rows.append({'id':r['id'], 'n':n,
                     'minimal_qualified':';'.join(''.join(str(i+1) for i in range(n) if b>>i & 1) for b in r['minimal_qualified']),
                     'basis_m_min':m, 'alpha_max_both_models':str(alpha),
                     'basis_alpha_at_m_min':str(am), 'basis_m_at_alpha_max':ma,
                     'collection_m_min_lower':lower, 'collection_m_min_upper':m,
                     'collection_alpha_at_m_min':str(am) if c_fixed else 'UNRESOLVED',
                     'collection_m_at_alpha_max_lower':lower_ma, 'collection_m_at_alpha_max_upper':ma,
                     'all_four_collection_optima_certified':c_m and c_fixed and c_ma})
        entry = summary.setdefault(str(n), {'classes':0, 'tradeoff_classes':0, 'collection_complete':0, 'minimum_gap_one':0})
        entry['classes'] += 1
        entry['tradeoff_classes'] += am < alpha
        entry['collection_complete'] += c_m and c_fixed and c_ma
        entry['minimum_gap_one'] += r['contrast_at_minimum']['gap'] == 1
    with (ROOT/'evidence/table-n5.csv').open('w', newline='') as out:
        writer = csv.DictWriter(out, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    with (ROOT/'evidence/table-n4.csv').open('w', newline='') as out:
        writer = csv.DictWriter(out, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(r for r in rows if r['n'] <= 4)
    # Exact primary-source controls: no claims from inaccessible articles.
    known = [
        (2,['12'],2,'Ateniese1996 Section3'),
        (3,['12','23'],2,'Ateniese1996 Table1 #2'),
        (3,['12','13','23'],3,'Ateniese1996 Table1 #3'),
        (3,['123'],4,'Ateniese1996 Table1 #4'),
        (4,['12','23','34'],3,'Ateniese1996 Table1 #5'),
        (4,['12','13','14'],2,'Ateniese1996 Table1 #6'),
        (4,['12','14','23','34'],2,'Ateniese1996 Table1 #7'),
        (4,['12','23','24','34'],3,'Ateniese1996 Table1 #8'),
        (4,['12','13','14','23','24'],3,'Ateniese1996 Table1 #9'),
        (4,['12','13','14','23','24','34'],4,'Ateniese1996 Table1 #10'),
        (4,['123','14'],4,'Ateniese1996 Table1 #11'),
        (4,['123','14','34'],5,'Ateniese1996 Table1 #12'),
        (4,['123','124'],4,'Ateniese1996 Table1 #14'),
        (4,['124','134','23'],5,'Ateniese1996 Table1 #15'),
        (4,['123','124','134'],6,'Blundo1999 Theorem6.4'),
        (4,['123','124','134','234'],6,'Blundo1999 Theorem6.4'),
        (4,['1234'],8,'Ateniese1996 Table1 #18'),
        (5,['12','13','14','15','23','24','25','34','35','45'],4,'Ateniese1996 Theorem7.3'),
        (5,['12345'],16,'Ateniese1996 Section3')]
    by_key = {(r['n'],canonical(r['n'],r['minimal_qualified'])):r for r in certificates['records']}
    comparisons = []
    for n, blocks, expected, source in known:
        masks = [sum(1 << (int(c)-1) for c in b) for b in blocks]
        record = by_key[n,canonical(n,masks)]
        observed = record['minimum_expansion']['m']
        assert observed == expected
        comparisons.append({'id':record['id'], 'published_minimum_expansion':expected,
                            'computed':observed, 'source':source, 'matches':True})
    for n in range(2,6):
        masks = [s for s in range(2**n) if s.bit_count()==2]
        record = by_key[n,canonical(n,masks)]
        expected = Fraction((n//2)*((n+1)//2),n*(n-1))
        assert Fraction(record['lp']['alpha']) == expected
        comparisons.append({'id':record['id'], 'published_alpha':str(expected),
                            'computed':record['lp']['alpha'], 'source':'Blundo1999 Theorems4.1-4.2', 'matches':True})
    report = {'command':' '.join(sys.argv), 'scope':'basis exact n<=5; collection exact n<=4 and 203/208 n5 classes',
              'summary':summary, 'published_comparisons':comparisons,
              'unresolved_collection_rows':[r for r in rows if not r['all_four_collection_optima_certified']],
              'novelty':'Not claimed; exact certification and reproduction, not a full solution.'}
    (ROOT/'evidence/summary.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'summary':summary, 'primary_source_comparisons':len(comparisons),
                      'unresolved_collection_rows':len(report['unresolved_collection_rows'])}, indent=2))


if __name__ == '__main__':
    main()
