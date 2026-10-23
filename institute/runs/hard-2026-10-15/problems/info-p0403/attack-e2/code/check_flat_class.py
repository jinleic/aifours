"""Independent exhaustive full-512-Walsh check of each coordinate subcube.

No producer imports. Reconstructs seed hex from literature, constructs
every full truth table and computes its integer transform. Compares
every outcome in the entire 65536-pattern range; this is not sampling.
The explicit maximizing balanced tables are separately checked by
direct character sums through code/check_witness.py.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import numpy as np


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--broken',action='store_true')
    p.add_argument('--output')
    args=p.parse_args()
    data=json.loads(Path('results/flat-class.json').read_text())
    source=Path('selection-inputs/literature/kavut-yucel.reader.md').read_text().split('#### 3.2')[0]
    tables=re.findall(r'(?m)^([0-9A-F]{64}) ([0-9A-F]{64})$',source)
    assert len(tables)==3
    audits={}
    for name,(left,right) in zip(('dsbf40','dsbf32','rsbf56'),tables):
        rec=data['seeds'][name]
        hx=left+right
        assert rec['seed_hex']==hx
        f=np.array([int(b) for ch in hx for b in format(int(ch,16),'04b')],dtype=np.int16)
        points=rec['free_points_in_flip_mask_bit_order']
        assert len(points)==len(set(points))==16
        assert sorted(points)==rec['free_points_sorted']
        # Check the claimed affine four-flat from scratch by XOR closure.
        translated={p^points[0] for p in points}
        assert 0 in translated and all(x^y in translated for x in translated for y in translated)
        raw=Path(rec['outcomes_file']).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==rec['outcomes_sha256']
        expected=np.frombuffer(raw,dtype='<i2').reshape(65536,2).copy()
        if args.broken and name=='dsbf40': expected[1234,0]+=4
        observed=np.empty((65536,2),dtype=np.int16)
        for begin in range(0,65536,512):
            masks=np.arange(begin,begin+512,dtype=np.int32)
            A=np.broadcast_to((1-2*f)[None,:],(512,512)).copy()
            for j,x in enumerate(points): A[:,x]*=(1-2*((masks>>j)&1)).astype(np.int16)
            # Full Walsh transform of every 512-input truth table.
            block=1
            while block<512:
                V=A.reshape(512,-1,2*block)
                top=V[:,:,:block].copy()
                bottom=V[:,:,block:].copy()
                V[:,:,:block]=top+bottom
                V[:,:,block:]=top-bottom
                block*=2
            observed[begin:begin+512,0]=np.max(abs(A),axis=1)
            observed[begin:begin+512,1]=np.count_nonzero(A==0,axis=1)
            high_nl=np.max(abs(A),axis=1)<=28
            assert np.all(A[high_nl]%8==4)
        assert np.array_equal(observed,expected),(name,'incorrect full-range outcomes')
        eligible=observed[:,1]>0
        best=int(np.min(observed[eligible,0]))
        assert rec['patterns_exhausted']==65536
        assert rec['best_balanced_max_abs_W']==best==32
        assert rec['exact_maximum_balanced_nonlinearity_with_linear_output_shift']==240
        assert rec['patterns_with_zero']==int(np.count_nonzero(eligible))
        assert rec['linear_output_shifts_yielding_balance']==int(observed[:,1].sum())
        assert rec['patterns_preserving_max_abs_W_at_most_28']==int(np.count_nonzero(observed[:,0]<=28))
        assert rec['patterns_preserving_28_and_having_zero']==int(np.count_nonzero((observed[:,0]<=28)&eligible))==0
        # Reconstruct the attainer from the class definition, including
        # its exact flip mask and output shift, then invoke direct sums.
        witness=json.loads(Path(rec['attainer']).read_text())
        h=f.copy()
        mask=rec['attainer_flip_mask']
        for j,x in enumerate(points):
            if (mask>>j)&1: h[x]^=1
        a=rec['attainer_linear_shift']
        for x in range(512): h[x]^=bin(a&x).count('1')%2
        assert ''.join(map(str,h.tolist()))==witness['bits']
        subprocess.run(['python3','code/check_witness.py',rec['attainer'],'--min-nl','240'],check=True)
        audits[name]={'patterns_exhausted':65536,'coefficients_checked_per_pattern':512,'best_balanced_nonlinearity':240,'outcomes_sha256':rec['outcomes_sha256']}
        print(name,'PASS all 65536 full transforms and direct-sum attainer',flush=True)
    result={'status':'PASS','method':'every full truth table and all 512 Walsh coefficients per table, independently from 16-point reduction','seeds':audits}
    if args.output: Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print('PASS independent complete coordinate-subcube enumeration')


if __name__=='__main__': main()
