# Apply the exact mixed-operator atom probe to three distinct asymmetric boxes.
# One finite-grid solve each. No positive grid margin is a global verdict.
from pathlib import Path
source=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-spr-operator-hybrid-search-kernel-v1.py').read_text()
if source.count('box=asym_results[2];')!=1 or source.count('for iteration in range(2):')!=1:raise ValueError('SOURCE_SHAPE')
diverse_operator=[]
for idx in (3,4,5):
 code=source.replace('box=asym_results[2];','box=asym_results[%d];'%idx).replace('for iteration in range(2):','for iteration in range(1):').replace('TWO_ITERATION_LIMIT','ONE_ITERATION_LIMIT')
 exec(compile(code,'operator_probe_'+str(idx),'exec'),globals())
 diverse_operator.append({'box_index':idx,'rounds':op_rounds})
 if op_rounds[-1]['status']=='OPERATOR_NONPOSITIVE_CERTIFICATE':break
print('diverse mixed-operator probes:',[{'box_index':r['box_index'],'status':r['rounds'][-1]['status'],'atoms':r['rounds'][-1]['atoms'],
 'pivots':r['rounds'][-1]['pivots']} for r in diverse_operator])
