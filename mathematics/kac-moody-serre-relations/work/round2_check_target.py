#!/usr/bin/env python3
"""Independent exact checker for one degree above a trusted certified baseline.

The baseline digest is an external required argument. This checker verifies
the new degree, not the prior full baseline again. For complete reproduction,
first run the baseline's scope-bound checker, then this chained verifier.
Producer imports are forbidden here; lowerings use associative word deletion.
"""
import argparse
import copy
import gzip
import hashlib
import itertools
import json
import time
from fractions import Fraction as Q
from pathlib import Path

from check_certificate import (TensorCoordinates, ExactSpan, tensor, word_lowering,
                               suffix_lyndon, witt_dimension, decode_rows, accumulate, require)


def prescribed_words(alpha):
    """Independent enumeration by positions, not producer prefix recursion."""
    size=sum(alpha)
    words=[]
    for positions0 in itertools.combinations(range(size),alpha[0]):
        zero=set(positions0)
        remaining=[i for i in range(size) if i not in zero]
        for positions1 in itertools.combinations(remaining,alpha[1]):
            one=set(positions1)
            word=tuple(0 if i in zero else 1 if i in one else 2 for i in range(size))
            if suffix_lyndon(word):
                words.append(word)
    return sorted(words)


class FocusedTensor(TensorCoordinates):
    def __init__(self,degrees):
        self.words={degree:prescribed_words(degree) for degree in degrees}
        self.ordered=sorted(self.words,key=lambda alpha:(sum(alpha),alpha))
        self.ad_maps={}
        for alpha,words in self.words.items():
            require(len(words)==witt_dimension(alpha),'free-Lie dimension mismatch')
            require(all(min(tensor(word))==word and tensor(word)[word]==1 for word in words),'Lyndon triangularity')


def verify_header(data,name,matrix,alpha,baseline_digest):
    require(data['field']=='Q' and data['prime'] is None,'Q certificate required')
    require(data['matrix_name']==name and data['matrix']==matrix,'wrong fixed matrix')
    require(data['degree']==list(alpha),'wrong requested degree')
    require(data['baseline_certificate_sha256']==baseline_digest,'wrong baseline link')


def reported_fields(data,computed):
    require(all(data[key]==value for key,value in computed.items()),'reported dimension mismatch')


def first_defect_candidates(matrix,height):
    candidates=[]
    for a in range(2,height-3):
        for b in range(2,height-a-1):
            c=height-a-b
            alpha=(a,b,c)
            weight=[sum(x*y for x,y in zip(row,alpha)) for row in matrix]
            if max(weight)<=0:
                candidates.append({'degree':list(alpha),'cartan_weight':weight})
    return candidates


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('certificate',type=Path)
    parser.add_argument('--matrix',required=True)
    parser.add_argument('--degree',type=int,nargs=3,required=True)
    parser.add_argument('--baseline',type=Path,required=True)
    parser.add_argument('--baseline-acceptance',type=Path,required=True)
    parser.add_argument('--baseline-sha256',required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    started=time.monotonic()
    alpha=tuple(args.degree)
    require(min(alpha)>0,'target must have full support')
    spec_bytes=Path('work/matrices.json').read_bytes()
    matrix=json.loads(spec_bytes)['matrices'][args.matrix]
    blob=args.certificate.read_bytes()
    data=json.loads(gzip.decompress(blob))
    verify_header(data,args.matrix,matrix,alpha,args.baseline_sha256)
    base_blob=args.baseline.read_bytes()
    require(hashlib.sha256(base_blob).hexdigest()==args.baseline_sha256,'baseline bytes differ from trusted digest')
    base=json.loads(gzip.decompress(base_blob))
    acceptance_blob=args.baseline_acceptance.read_bytes()
    acceptance=json.loads(acceptance_blob)
    require(acceptance['status']=='PASS' and acceptance['certificate_sha256']==args.baseline_sha256,'baseline acceptance mismatch')
    require(acceptance['requested_matrices']==[args.matrix] and acceptance['field']=='Q','wrong baseline matrix scope')
    require(acceptance['requested_height']==base['height'] and sum(alpha)==base['height']+1,'wrong height chain')
    require(base['field']=='Q' and base['matrices'][args.matrix]['matrix']==matrix,'wrong baseline contents')
    parent_degrees=[tuple(a-int(j==i) for j,a in enumerate(alpha)) for i in range(3)]
    previous={tuple(record['alpha']):record for record in base['matrices'][args.matrix]['records']}
    records={degree:previous[degree] for degree in parent_degrees}
    require(all(record['extra_relations']==0 for record in records.values()),'baseline parents do not certify equality')
    coordinates=FocusedTensor([alpha]+parent_degrees)
    words=coordinates.words[alpha]
    require(data['words']==[''.join(map(str,w)) for w in words],'wrong or incomplete target basis')
    parent_ideals={}
    for degree,record in records.items():
        require(record['words']==[''.join(map(str,w)) for w in coordinates.words[degree]],'baseline parent basis mismatch')
        parent_ideals[degree]=ExactSpan(decode_rows(record['ideal_basis'],len(coordinates.words[degree])))
        require(parent_ideals[degree].rank()==record['serre_ideal_rank'],'baseline parent rank mismatch')
    # All target coordinates are positive, so original two-support Serre
    # generators do not occur directly at this degree.
    generated=[]
    for i,degree in enumerate(parent_degrees):
        generated.extend(coordinates.raise_row(i,degree,row) for row in parent_ideals[degree].pivots.values())
    generated_ideal=ExactSpan(generated)
    certificate_rows=decode_rows(data['ideal_basis'],len(words))
    ideal=ExactSpan(certificate_rows)
    require(ideal.rank()==len(certificate_rows)==generated_ideal.rank(),'wrong target ideal rank')
    require(all(not ideal.remainder(row) for row in generated),'omitted ideal generator')
    require(all(not generated_ideal.remainder(row) for row in certificate_rows),'extraneous ideal row')
    columns=[j for j in range(len(words)) if j not in ideal.pivots]
    require(columns==data['quotient_columns'],'wrong quotient complement')
    images=[]
    for column in columns:
        image={}
        for i,degree in enumerate(parent_degrees):
            polynomial=word_lowering(tensor(words[column]),i,matrix)
            reduced=parent_ideals[degree].remainder(coordinates.solve(polynomial,degree))
            image.update({(i,j):value for j,value in reduced.items()})
        images.append(image)
    image_rank=ExactSpan(images).rank()
    kernel_rows=decode_rows(data['kernel_basis'],len(columns))
    kernel=ExactSpan(kernel_rows)
    nullity=len(columns)-image_rank
    require(kernel.rank()==len(kernel_rows)==nullity,'wrong kernel dimension')
    for row in kernel_rows:
        image={}
        for j,value in row.items():
            accumulate(image,images[j],value)
        require(not image,'claimed defect has a nonzero descent')
    computed={'free_dim':len(words),'serre_ideal_rank':ideal.rank(),
              'serre_dim':len(columns),'descent_rank':image_rank,
              'contragredient_dim':image_rank,'extra_relations':nullity}
    reported_fields(data,computed)
    rejected=[]
    for mutation in ('field','degree','baseline_link','matrix'):
        altered=copy.deepcopy(data)
        if mutation=='field':
            altered['field']='F_1000003'
        elif mutation=='degree':
            altered['degree'][0]+=1
        elif mutation=='baseline_link':
            altered['baseline_certificate_sha256']='0'*64
        else:
            altered['matrix'][0][1]-=1
        try:
            verify_header(altered,args.matrix,matrix,alpha,args.baseline_sha256)
        except ValueError as error:
            rejected.append({'mutation':mutation,'rejected':True,'reason':str(error)})
        else:
            raise AssertionError('scope mutation accepted')
    altered=copy.deepcopy(data)
    altered['contragredient_dim']+=1
    try:
        reported_fields(altered,computed)
    except ValueError as error:
        rejected.append({'mutation':'dimension','rejected':True,'reason':str(error)})
    else:
        raise AssertionError('dimension mutation accepted')
    candidates=first_defect_candidates(matrix,sum(alpha))
    extends_range=nullity==0 and [row['degree'] for row in candidates]==[list(alpha)]
    witness=[]
    if kernel_rows:
        witness=[[data['words'][columns[j]],str(value)] for j,value in sorted(kernel_rows[0].items())]
    result={'status':'PASS_EQUALITY' if nullity==0 else 'EXACT_DEFECT_VERIFIED_REQUIRES_REFEREE',
            'matrix_name':args.matrix,'matrix':matrix,'degree':list(alpha),'field':'Q',**computed,
            'baseline_certificate_sha256':args.baseline_sha256,
            'baseline_acceptance_sha256':hashlib.sha256(acceptance_blob).hexdigest(),
            'certificate_sha256':hashlib.sha256(blob).hexdigest(),
            'source_sha256':{p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in ('work/round2_check_target.py','work/check_certificate.py')},
            'spec_sha256':hashlib.sha256(spec_bytes).hexdigest(),
            'generated_ideal_rows':len(generated),'negative_controls':rejected,
            'first_defect_candidates_at_height':candidates,
            'range_extension_to_height':sum(alpha) if extends_range else None,
            'range_extension_basis':'Trusted baseline equality at all lower heights + coefficient-one theorem + A alpha<=0 for a first defect + exhaustive integer enumeration at this height',
            'explicit_defect_lie_combination':witness,
            'baseline_trust':'Composes with the previously independently accepted hash-pinned baseline; does not re-run all lower-degree checks',
            'elapsed_seconds':round(time.monotonic()-started,3),'processes':1}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
