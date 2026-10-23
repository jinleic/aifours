"""Deterministically compress regenerable CNF/metadata files without loss."""
import gzip
import hashlib
import json
from pathlib import Path


records=[]
for pattern in ('*.cnf','*.encoding.json'):
    for path in sorted(Path('results').glob(pattern)):
        raw=path.read_bytes()
        out=path.with_name(path.name+'.gz')
        packed=gzip.compress(raw,compresslevel=9,mtime=0)
        if out.exists():
            assert gzip.decompress(out.read_bytes())==raw
        else:
            out.write_bytes(packed)
        assert gzip.decompress(out.read_bytes())==raw
        records.append({'source':str(path),'compressed':str(out),'uncompressed_bytes':len(raw),
                        'uncompressed_sha256':hashlib.sha256(raw).hexdigest(),
                        'compressed_bytes':out.stat().st_size})
        path.unlink()
p=Path('results/storage-audit.json')
previous=json.loads(p.read_text()) if p.exists() else []
known={r['source']:r for r in previous}
known.update({r['source']:r for r in records})
p.write_text(json.dumps(list(known.values()),indent=2)+'\n')
print('Losslessly compressed',len(records),'CNF/metadata files.')
