"""One bounded, prompt-only independent-vendor review of the K5 normal-form
projection lemma and normalisation. Uses the subscription Claude CLI exactly
as MODEL_DELEGATION.md prescribes; models/effort read live from DELEGATE_MODELS.
No tools, no file access, no settings changes. Invoke under run_bounded.py.
"""
import hashlib
import json
import subprocess
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

root = Path(__file__).resolve().parent.parent
note = root / 'review/K5_RESIDUAL_NORMAL_FORM.r2.md'
policy = Path('/Users/jinleic/jinleic-workspace/docs/knowledge-system/DELEGATE_MODELS.json')
cfg = json.loads(policy.read_bytes())['claude']
proof = note.read_bytes()
prefix = root / 'review/K5_NORMAL_FORM_CLAUDE_v1'
prompt = '''Perform a hostile mathematical audit of the proof below, not a literature search.
You have no tools and no file access. Treat the stated W8 bound and standard-form/SB2/vector-to-CNF bridge as
conditional imports, not facts you independently checked. Audit the NEW projection lemma and residual normal form.
Check arbitrary complex vectors, all quantifiers, completeness choice of four distinct vectors, projection inner
products and dimension count; then residual column/coordinate permutation, square relabelling, preservation of reduced
K5 and SB2, restoration of ROWLEX by row permutations2..7, bit-order orientation, cases64/96/112. Check that the final
claim is only a genuine-vector reduction, not arbitrary-CNF-model transfer. Find a concrete counterexample if invalid.
Return ACCEPT, ACCEPT-WITH-FIXES, or REJECT, with FATAL/MAJOR/MINOR findings and exact statements. Do not certify
imported solver facts or claim K5 excluded. Be decisive and concise. No delegation, no shell, no external access.
\nPROOF CANDIDATE:\n''' + proof.decode()
with Path(str(prefix) + '.prompt.txt').open('x') as f:
    f.write(prompt)
argv = ['claude', '--model', cfg['model'], '--effort', cfg['effort'], '--safe-mode', '--no-chrome', '--tools', '',
        '--permission-mode', 'dontAsk', '--no-session-persistence', '--output-format', 'json', '-p', prompt]
meta = {'started': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(), 'model': cfg['model'],
        'effort': cfg['effort'], 'proof_note_sha256': hashlib.sha256(proof).hexdigest(),
        'prompt_sha256': hashlib.sha256(prompt.encode()).hexdigest(), 'model_policy_sha256':
        hashlib.sha256(policy.read_bytes()).hexdigest(), 'mode': 'prompt-only, tools disabled; subscription CLI'}
with Path(str(prefix) + '.receipt.json').open('x') as f:
    json.dump(meta, f, indent=1)
with Path(str(prefix) + '.stdout.json').open('x') as out, Path(str(prefix) + '.stderr.txt').open('x') as err:
    p = subprocess.Popen(argv, cwd=root, stdin=subprocess.DEVNULL, stdout=out, stderr=err)
    try:
        rc = p.wait(timeout=600)
    except subprocess.TimeoutExpired:
        p.terminate()
        try:
            rc = p.wait(timeout=30)
        except subprocess.TimeoutExpired:
            rc = None
print(json.dumps({'returncode': rc, 'prefix': str(prefix)}), flush=True)
