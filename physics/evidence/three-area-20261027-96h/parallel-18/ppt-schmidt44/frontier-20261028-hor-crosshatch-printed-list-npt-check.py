#!/usr/bin/env python3
"""Exact Q(sqrt2) principal minor of the paper's displayed 18-ket list."""
from fractions import Fraction as F
from hashlib import sha256
from contextlib import redirect_stdout
import io,json,runpy
path='frontier-20261028-hor-crosshatch-source-sn3-check.py'
expected='0165c6500c5d59401672c206f4617426119cb2c885ac04899f6cd27c7215ba11'
assert sha256(open(path,'rb').read()).hexdigest()==expected
buf=io.StringIO()
with redirect_stdout(buf): h=runpy.run_path(path)
prior=json.loads(buf.getvalue());assert prior['paper_eq36_difference_entries']==90
P=h['printed'];add,mul,neg,Z,O=h['add'],h['mul'],h['h']['neg'],h['Z'],h['O']
# Gamma on Bob: (a,b;c,d) -> (a,d;c,b). Indices 0=(0,0), 21=(1,9).
def pt(i,j):return P[12*(i//12)+j%12][12*(j//12)+i%12]
i,j=0,21
block=((pt(i,i),pt(i,j)),(pt(j,i),pt(j,j)))
assert block==((Z,O),(O,O))
test=add(add(block[0][0],block[1][1]),neg(add(block[0][1],block[1][0])))
assert test==(F(-1),F(0))
trace=Z
for k in range(48):trace=add(trace,P[k][k])
assert trace==(F(44),F(0))
print(json.dumps({'printed_kets':18,'paper_unscaled_trace':44,
 'pt_principal_basis':['|0,0>','|1,9>'],'pt_principal_block':[[0,1],[1,1]],
 'test_vector':'|0,0>-|1,9>','test_value_unnormalized':'-1','test_value_normalized':'-1/44',
 'source_vs_list_mismatches':90,'source_sn3_check_replayed':True,'source_checker_sha256':expected,
 'limits':'NPT is for the displayed equal-weight ket list only; does not decide intended source, alternate relabeling, or other paper results.'},indent=2))
