"""Check relative Markdown links (and their #anchors' files) in the given files; parse given JSON files.
Usage: python3 -B navigation_link_check.py NEW_RECEIPT.json --md FILE... [--json FILE...]
Paths are relative to the repository root /Users/jinleic/repos/aifours. Refuses to overwrite the receipt.
External (scheme) links, mailto and pure #anchors are skipped; agent:// style links are skipped and counted.
"""
from datetime import datetime
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote
from zoneinfo import ZoneInfo

ROOT = Path('/Users/jinleic/repos/aifours')
LINK = re.compile(r'\[[^\]]*\]\(([^)\s]+)\)')


def main():
    out = Path(sys.argv[1])
    if out.exists():
        raise SystemExit('Refusing to overwrite receipt')
    md, js, mode = [], [], None
    for a in sys.argv[2:]:
        if a in ('--md', '--json'):
            mode = a
        elif mode == '--md':
            md.append(a)
        elif mode == '--json':
            js.append(a)
    checked, skipped, missing = 0, 0, []
    for rel in md:
        f = ROOT / rel
        text = f.read_text()
        for lineno, line in enumerate(text.splitlines(), 1):
            for target in LINK.findall(line):
                if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                    skipped += 1
                    continue
                path = unquote(target.split('#', 1)[0])
                if not path:
                    skipped += 1
                    continue
                checked += 1
                if not (f.parent / path).exists():
                    missing.append({'file': rel, 'line': lineno, 'target': target})
    parsed = []
    for rel in js:
        json.loads((ROOT / rel).read_text())
        parsed.append(rel)
    result = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).strftime('%Y-%m-%d %H:%M:%S %Z'),
              'checked_files': md, 'relative_links_checked': checked, 'skipped_links': skipped,
              'missing_targets': missing, 'json_parsed': parsed}
    with out.open('x') as fh:
        json.dump(result, fh, indent=2, ensure_ascii=False)
        fh.write('\n')
    print(json.dumps({k: result[k] for k in ['relative_links_checked', 'skipped_links', 'missing_targets']}, ensure_ascii=False))
    return 1 if missing else 0


if __name__ == '__main__':
    raise SystemExit(main())
