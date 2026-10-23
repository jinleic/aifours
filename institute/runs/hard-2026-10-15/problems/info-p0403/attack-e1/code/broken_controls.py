"""Produce deliberately false encoding/proof/witness controls."""
import hashlib
import json
from pathlib import Path

prefix='results/dsbf40-r6'
bad='results/control-bad-encoding'
text=Path(prefix+'.cnf').read_text().splitlines()
meta=json.loads(Path(prefix+'.encoding.json').read_text())
# Flip the seed-value literal in lookup row x=0. Update the checksum so
# rejection requires auditing correspondence, not merely file hashing.
row=text[1].split()
row[-2]=str(-int(row[-2]))
text[1]=' '.join(row)
body='\n'.join(text)+'\n'
meta['cnf_sha256']=hashlib.sha256(body.encode()).hexdigest()
Path(bad+'.cnf').write_text(body)
Path(bad+'.encoding.json').write_text(json.dumps(meta,separators=(',',':'))+'\n')
proof=Path('results/dsbf40-r2.lrat').read_text().splitlines()
row=proof[0].split()
cut=row.index('0')
row[cut+1]='99999999'
proof[0]=' '.join(row)
Path('results/control-bad-proof.lrat').write_text('\n'.join(proof)+'\n')
print('Created bad lookup with a matching checksum, and a bad LRAT hint.')
