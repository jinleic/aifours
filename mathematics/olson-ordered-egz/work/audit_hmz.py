#!/usr/bin/env python3
"""Read one completed/interrupted HMZ round; never infer acceptance from exit0."""
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = Path('/Users/jinleic/jinleic-workspace')
REPO = WORKSPACE / 'scratch/ai4s-math-more-20261014/olson'
RAW = REPO.parent / 'olson-hmz-evidence'
EPICS = Path.home() / '.humanize/epics' / str(REPO).replace('/', '-')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def entries(path):
    parsed, malformed = [], []
    if not path.is_file():
        return parsed, malformed
    for number, line in enumerate(path.read_text().splitlines(), 1):
        try:
            parsed.append(json.loads(line))
        except json.JSONDecodeError:
            malformed.append({'line': number, 'text': line})
    return parsed, malformed


def main():
    receipt_path = ROOT / 'evidence/hmz-terminal.json'
    if receipt_path.exists():
        raise SystemExit('Refusing to overwrite a previous terminal audit')
    process_path = RAW / 'process.json'
    process = json.loads(process_path.read_text())
    shutil.copyfile(process_path, ROOT / 'evidence/hmz-process.json')
    result = {'schema': 'olson-hmz-terminal/1', 'process_receipt_complete': 'returncode' in process,
              'returncode': process.get('returncode'), 'elapsed_seconds': process.get('elapsed_seconds'),
              'baseline_commit': process['baseline_commit'], 'pairing': process['pairing'],
              'hmz_install': process['hmz_install'],
              'official_flowverse_commit': process['official_flowverse_commit'],
              'frozen_unchanged': {name: (REPO / name).is_file() and sha(REPO / name) == digest
                                   for name, digest in process['frozen_sha256'].items()},
              'runs': [], 'os_sandbox': False,
              'warning': 'An incomplete runner receipt or missing terminal journal is an interruption, never acceptance.'}
    for run in sorted(EPICS.iterdir() if EPICS.is_dir() else []):
        if not run.is_dir():
            continue
        epic, epic_malformed = entries(run / 'epic.jsonl')
        resume, resume_malformed = entries(run / 'resume.jsonl')
        ended = [row for row in epic if row.get('event') == 'ended']
        ends = [row for row in resume if row.get('t') == 'end']
        rounds = [row['value'] for row in resume if row.get('t') == 'set' and row.get('key') == 'rounds']
        notes = [row['value'] for row in resume if row.get('t') == 'set' and row.get('key') == 'notes']
        record = {'run': run.name, 'epic_ended': ended[-1] if ended else None,
                  'resume_end': ends[-1] if ends else None,
                  'completed_review_rounds': rounds, 'review_notes': notes,
                  'last_resume_entry': resume[-1] if resume else None,
                  'malformed_epic_lines': epic_malformed, 'malformed_resume_lines': resume_malformed,
                  'journals': {}}
        for name in ('epic.jsonl', 'resume.jsonl'):
            source = run / name
            if source.is_file():
                destination = ROOT / 'evidence' / (run.name + '-' + name)
                shutil.copyfile(source, destination)
                record['journals'][name] = {'source': str(source), 'retained': str(destination.relative_to(ROOT)),
                                            'sha256': sha(source)}
        record['terminal_accepted'] = bool(ended and ends and ended[-1].get('how') == 'done'
                                            and ends[-1].get('ok') is True)
        result['runs'].append(record)
    result['any_terminal_accepted'] = any(run['terminal_accepted'] for run in result['runs'])
    result['mathematical_resolution'] = False
    result['mathematical_resolution_note'] = 'Journal acceptance would still require exact-goal proof/certificate and independent parent review.'
    receipt_path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
