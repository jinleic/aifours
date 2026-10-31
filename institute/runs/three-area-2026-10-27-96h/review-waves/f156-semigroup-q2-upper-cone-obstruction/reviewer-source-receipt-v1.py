from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import html
import json
import re

outdir = Path(__file__).resolve().parent
source = Path('/tmp/f156/1909.05280v1.html')
raw = source.read_bytes()
text = raw.decode('utf-8')

def math_alt(match):
    a = re.search(r'alttext="([^"]*)"', match.group(0))
    if a is None:
        raise RuntimeError('MathML element lacks alttext')
    return ' $' + html.unescape(a.group(1)) + '$ '

text = re.sub(r'<math\b.*?</math>', math_alt, text, flags=re.S)
blocks = {}
for tag, ident in [('div', 'S2.p3'), ('div', 'S5.SS2.p4'), ('div', 'S5.SS2.p5'), ('table', 'S5.Ex1')]:
    match = re.search(r'<' + tag + r' id="' + re.escape(ident) + r'".*?</' + tag + '>', text, flags=re.S)
    if match is None:
        raise RuntimeError('named source block missing: ' + ident)
    blocks[ident] = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', match.group(0)))).strip()
receipt = {
    'kind': 'NAMED_PUBLIC_SOURCE_DIRECT_READ_RECEIPT',
    'observed_UTC_before_receipt': datetime.now(timezone.utc).isoformat(),
    'reference': 'Maria B. Szendrei, Structure theory of regular semigroups, arXiv:1909.05280v1 (2019)',
    'URL': 'https://arxiv.org/html/1909.05280v1',
    'source_sha256': sha256(raw).hexdigest(),
    'source_bytes': len(raw),
    'source_LF': raw.count(b'\n'),
    'blocks_with_math_alttext': blocks,
    'source_is_public_author_survey_not_independent_proof_or_formal_verification': True,
    'process_exception': {
        'scratch_path': str(source),
        'description': 'Earlier direct-source fetch created /tmp/f156 and this HTML file outside the assigned review artifact directory. This location restriction exception is disclosed; file retained, not deleted.',
        'download_observed_before_UTC_clock_in_tool': '2026-10-29T04:48:15Z',
        'not_claimed_as_exact_creation_timestamp': True,
    },
}
encoded = (json.dumps(receipt, ensure_ascii=False, indent=2) + '\n').encode()
p = outdir / 'reviewer-public-source-receipt-v1.json'
with p.open('xb') as f:
    f.write(encoded)
print('source_sha256=' + receipt['source_sha256'])
print('source_bytes=' + str(len(raw)) + ' source_LF=' + str(raw.count(b'\n')))
print('source_receipt_sha256=' + sha256(encoded).hexdigest())
print('source_receipt_clock=' + receipt['observed_UTC_before_receipt'])
for ident, value in blocks.items():
    print(ident + ': ' + value)
