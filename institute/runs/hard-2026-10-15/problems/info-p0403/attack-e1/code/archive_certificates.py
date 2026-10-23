"""Remove bulky originals only after a trimmed certificate has passed."""
import hashlib
import json
from pathlib import Path


for seed in ('dsbf40','dsbf32','rsbf56'):
    prefix='results/%s-r6'%seed
    chk=Path(prefix+'-trimmed-proof-check.json')
    trimmed=Path(prefix+'-trimmed.lrat.gz')
    original=Path(prefix+'.lrat.gz')
    if not chk.exists(): continue
    info=json.loads(chk.read_text())
    assert info['status']=='PASS' and info['checked_empty_clause']
    assert info['cnf_sha256']==hashlib.sha256(Path(prefix+'.cnf').read_bytes()).hexdigest()
    assert info['proof_sha256']==hashlib.sha256(trimmed.read_bytes()).hexdigest()
    if original.exists():
        original.unlink()
        print('Removed verified redundant original:',original)
# A partial trace from the timed-out run is not a certificate. Preserve
# its size/hash and solver log, but discard the unusable bulky trace.
for tag in ('dsbf40-r8','dsbf40-r8-degree8','dsbf40-r8-origin0','global-fwht'):
    proof=Path('results/'+tag+'.lrat.gz')
    log=Path('logs/'+tag+'-solver.log')
    if proof.exists() and log.exists() and 'c UNKNOWN' in log.read_text() and 'c exit 0' in log.read_text():
        info={'status':'UNKNOWN','scope':'No exclusion; timed-out partial proof is not an unsatisfiability certificate','discarded_partial_trace_bytes':proof.stat().st_size,'discarded_partial_trace_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'solver_log':str(log)}
        Path('results/'+tag+'-timeout.json').write_text(json.dumps(info,indent=2)+'\n')
        proof.unlink()
        print('Discarded inconclusive radius-eight partial trace; preserved log and hash:',tag)
