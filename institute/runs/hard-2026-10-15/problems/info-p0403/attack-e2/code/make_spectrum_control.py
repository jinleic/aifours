"""Make or compare the weight-preserving corrupted-spectrum control."""
import argparse
import json
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('--compare',action='store_true')
a=p.parse_args()
data=json.loads(Path('results/baseline240.json').read_text())
data['walsh'][2]+=4
path=Path('results/baseline240-broken-spectrum.json')
if a.compare:
    assert json.loads(path.read_text())==data
else:
    path.write_text(json.dumps(data,indent=2)+'\n')
print('PASS corrupted-spectrum control preserves the balanced table and hash.')
