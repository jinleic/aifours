#!/usr/bin/env python3
"""Compute one next-height root degree from a previously certified baseline.

This is a composition of exact finite certificates, not a fresh assertion that
an arbitrary baseline is valid. Its hash is fixed before this continuation.
The producer uses recursive bracket lowering; the independent checker does not.
"""
import argparse
import gzip
import hashlib
import json
import time
from fractions import Fraction
from pathlib import Path

from graded_lie import FreeLie, Field, RowSpace, lyndon, descend_factory, kernel_of_images


def multiset_words(counts):
    left=list(counts)
    prefix=[]
    length=sum(counts)
    def visit():
        if len(prefix)==length:
            yield tuple(prefix)
            return
        for letter in range(len(left)):
            if left[letter]:
                left[letter]-=1
                prefix.append(letter)
                yield from visit()
                prefix.pop()
                left[letter]+=1
    yield from visit()


class NextDegreeSpace(FreeLie):
    """The four needed homogeneous bases, using unchanged FreeLie operations."""
    def __init__(self, alpha, parents):
        self.rank=3
        self.height=sum(alpha)
        self.words={degree:[tuple(map(int,w)) for w in record['words']]
                    for degree,record in parents.items()}
        self.words[alpha]=[word for word in multiset_words(alpha) if lyndon(word)]
        self.index={degree:{word:i for i,word in enumerate(words)} for degree,words in self.words.items()}
        self._ad_cache={}


def decode(rows):
    return [{int(i):Fraction(value) for i,value in row} for row in rows]


def encode(rows):
    return [[[int(i),str(value)] for i,value in sorted(row.items())] for row in rows]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--scope',type=Path,default=Path('work/round2-scope.json'))
    parser.add_argument('--prime',type=int)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    begin=time.monotonic()
    scope_bytes=args.scope.read_bytes()
    scope=json.loads(scope_bytes)
    blob=Path(scope['baseline_certificate']).read_bytes()
    assert hashlib.sha256(blob).hexdigest()==scope['baseline_certificate_sha256']
    baseline=json.loads(gzip.decompress(blob))
    accepted=json.loads(Path(scope['baseline_acceptance']).read_text())
    assert accepted['status']=='PASS' and accepted['certificate_sha256']==scope['baseline_certificate_sha256']
    assert baseline['field']=='Q' and baseline['height']==scope['baseline_height']
    name=scope['matrix_name']
    instance=baseline['matrices'][name]
    matrix=scope['matrix']
    assert instance['matrix']==matrix
    assert json.loads(Path('work/matrices.json').read_text())['matrices'][name]==matrix
    alpha=tuple(scope['target_degree'])
    assert len(alpha)==3 and min(alpha)>0 and sum(alpha)==baseline['height']+1
    all_previous={tuple(record['alpha']):record for record in instance['records']}
    parent_degrees=[tuple(a-int(j==i) for j,a in enumerate(alpha)) for i in range(3)]
    parents={degree:all_previous[degree] for degree in parent_degrees}
    assert all(record['extra_relations']==0 for record in parents.values())
    field=Field(args.prime)
    space=NextDegreeSpace(alpha,parents)
    previous={degree:RowSpace(field,decode(record['ideal_basis'])) for degree,record in parents.items()}
    ideal=RowSpace(field)
    generator_count=0
    for i,degree in enumerate(parent_degrees):
        for row in previous[degree].basis():
            ideal.add(space.ad_generator(i,degree,row))
            generator_count+=1
    # The target has full support, so no original two-support Serre generator
    # has exactly this degree. Its descendants are exactly the brackets above.
    columns=[j for j in range(len(space.words[alpha])) if j not in ideal.rows]
    lowering=descend_factory(tuple(map(tuple,matrix)))
    images=[]
    for column in columns:
        word=space.words[alpha][column]
        image={}
        for i,degree in enumerate(parent_degrees):
            raw=space.coordinates(lowering(i,word),degree)
            reduced=previous[degree].reduce(raw)
            image.update({(i,j):value for j,value in reduced.items()})
        images.append(image)
    kernel,rank=kernel_of_images(images,field)
    assert len(columns)==rank+len(kernel)
    result_status=('EXACT_EQUALITY_COMPUTED' if not len(kernel) else 'EXACT_DEFECT_CANDIDATE') if args.prime is None else ('MODULAR_EQUALITY_SCREEN' if not len(kernel) else 'MODULAR_DEFECT_SCREEN')
    certificate={'matrix_name':name,'matrix':matrix,'degree':list(alpha),
                 'field':'Q' if args.prime is None else f'F_{args.prime}','prime':args.prime,
                 'baseline_certificate_sha256':scope['baseline_certificate_sha256'],
                 'scope_sha256':hashlib.sha256(scope_bytes).hexdigest(),
                 'words':[''.join(map(str,word)) for word in space.words[alpha]],
                 'ideal_basis':encode(ideal.basis()),'quotient_columns':columns,
                 'kernel_basis':encode(kernel.basis()),'free_dim':len(space.words[alpha]),
                 'serre_ideal_rank':len(ideal),'serre_dim':len(columns),
                 'descent_rank':rank,'contragredient_dim':rank,'extra_relations':len(kernel)}
    args.output.mkdir(parents=True,exist_ok=True)
    path=args.output/'certificate.json.gz'
    with path.open('wb') as stream:
        with gzip.GzipFile(filename='',fileobj=stream,mode='wb',mtime=0) as archive:
            archive.write(json.dumps(certificate,sort_keys=True,separators=(',',':')).encode())
    summary={key:value for key,value in certificate.items() if key not in ('words','ideal_basis','kernel_basis','quotient_columns')}
    summary.update({'status':result_status,'date':'2026-10-14','certificate':str(path),
                    'certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                    'generated_ideal_rows':generator_count,'parent_degrees':parent_degrees,
                    'parent_ideal_ranks':{str(degree):len(previous[degree]) for degree in parents},
                    'source_sha256':{p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in ('work/round2_target_degree.py','work/graded_lie.py','work/round2-scope.json')},
                    'elapsed_seconds':round(time.monotonic()-begin,3),'processes':1,
                    'trust_boundary':'Relies on the separately accepted hash-pinned height12 certificate. Modular output is screening only. An exact defect is not called a counterexample until independently checked and reviewed.'})
    (args.output/'results.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':
    main()
