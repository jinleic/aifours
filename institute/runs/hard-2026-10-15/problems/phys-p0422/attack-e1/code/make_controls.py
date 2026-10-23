"""Generate deliberately invalid or nonnegative trial witnesses deterministically."""
from copy import deepcopy
import json
from pathlib import Path

data = json.loads(Path('certificates/trials.json').read_text())
controls = []
for t in data['trials']:
    if t['name'] not in ('k4','k5'):
        continue
    zero = deepcopy(t)
    zero['name'] += '_zero_warning_control'
    zero['rates'] = ['0']
    zero['weights'] = ['1']
    controls.append(zero)
Path('certificates/negative-controls.json').write_text(json.dumps({'trials': controls}, indent=2)+'\n')
for t in data['trials']:
    if t['name'] not in ('k4','k5'):
        continue
    low = deepcopy(t)
    low['name'] += '_low_density_control'
    low['alpha'] = '79/10' if t['k']==4 else '187/10'
    Path(f"certificates/{low['name']}.json").write_text(json.dumps({'trials':[low]},indent=2)+'\n')
