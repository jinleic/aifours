#!/usr/bin/env python3
"""Snapshot a Lean solution and derive a statement-only Comparator challenge.

Usage: make_challenge.py TARGET SOURCE.lean THEOREM [THEOREM ...]
The solution is copied byte-for-byte to AI4SSolutions/TARGET.lean. The challenge keeps every
declaration verbatim except that the proofs of the listed target theorems become `by sorry`;
#print/#check/#eval commands are dropped from the challenge only. Targets must be theorems.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT / 'lean-verify'
TOP = re.compile(r'^(?:@\[|/--|/-!|private\s|protected\s|noncomputable\s|theorem\s|lemma\s|def\s|abbrev\s|'
                 r'structure\s|inductive\s|class\s|instance\s|section\b|end\b|namespace\s|variable\b|open\b|'
                 r'#|set_option\s|example\b|universe\s|attribute\s|omit\s|include\s|local\s|scoped\s|'
                 r'import\s|mutual\b|irreducible_def\s|alias\s|notation|infix|prefix|postfix)')
PROOF_KEYWORDS = re.compile(r'^(?:(?:@\[[^\]]*\]\s*)*(?:private\s+|protected\s+)?(?:theorem|lemma)\s|example\b)')


def mask(text):
    """Blank comments and strings so bracket depth and := detection ignore them."""
    out, i, depth = [], 0, 0
    while i < len(text):
        if depth:
            if text.startswith('/-', i):
                depth += 1; out.append('  '); i += 2
            elif text.startswith('-/', i):
                depth -= 1; out.append('  '); i += 2
            else:
                out.append('\n' if text[i] == '\n' else ' '); i += 1
        elif text.startswith('/-', i):
            depth = 1; out.append('  '); i += 2
        elif text.startswith('--', i):
            while i < len(text) and text[i] != '\n':
                out.append(' '); i += 1
        elif text[i] == '"':
            out.append(' '); i += 1
            while i < len(text) and text[i] != '"':
                step = 2 if text[i] == '\\' else 1
                out.append(''.join('\n' if c == '\n' else ' ' for c in text[i:i + step])); i += step
            out.append(' '); i += 1
        else:
            out.append(text[i]); i += 1
    return ''.join(out)


def blocks(text):
    masked = mask(text)
    starts = []
    offset = 0
    for raw, masked_line in zip(text.splitlines(keepends=True), masked.splitlines(keepends=True)):
        if raw[:1] not in (' ', '\t', '\n', '') and TOP.match(raw) and masked_line.strip():
            starts.append(offset)
        elif raw.startswith('/--') or raw.startswith('/-!'):
            starts.append(offset)
        offset += len(raw)
    starts = sorted(set(starts)) + [len(text)]
    if starts[0] != 0:
        starts.insert(0, 0)
    return [(starts[k], starts[k + 1]) for k in range(len(starts) - 1)], masked


def strip_proofs(text, targets):
    """Replace only the proofs of target theorems; every other declaration stays verbatim.

    Comparator requires exact equality for non-target constants reachable from target
    statements (including theorems used inside definition bodies), so auxiliary proofs
    must be kept. Namespaces are tracked to resolve fully qualified theorem names.
    """
    spans, masked = blocks(text)
    pieces, scopes, stripped = [], [], set()
    for start, end in spans:
        chunk, mchunk = text[start:end], masked[start:end]
        first = mchunk.lstrip()
        if chunk.lstrip().startswith('#'):
            continue
        opener = re.match(r'(?:noncomputable\s+)?section\b[ \t]*(\S*)', first)
        if re.match(r'namespace\s+(\S+)', first):
            scopes.append(('namespace', re.match(r'namespace\s+(\S+)', first).group(1)))
        elif opener:
            scopes.append(('section', opener.group(1)))
        elif re.match(r'end\b', first):
            scopes.pop()
        body_start = re.search(r'^(?:(?:@\[[^\]]*\]\s*)*(?:private\s+|protected\s+)?(?:theorem|lemma)\s+([^\s:({\[]+)|example\b)',
                               mchunk, re.MULTILINE)
        if not body_start or body_start.group(1) is None:
            pieces.append(chunk)
            continue
        short = body_start.group(1)
        prefix = '.'.join(name for kind, name in scopes if kind == 'namespace')
        full = short[len('_root_.'):] if short.startswith('_root_.') else (prefix + '.' + short if prefix else short)
        if full not in targets:
            pieces.append(chunk)
            continue
        depth = 0
        cut = None
        index = body_start.start()
        while index < len(mchunk) - 1:
            char = mchunk[index]
            if char in '([{⟨':
                depth += 1
            elif char in ')]}⟩':
                depth -= 1
            elif mchunk.startswith(':=', index) and depth == 0:
                cut = index
                break
            index += 1
        if cut is None:
            raise ValueError('no proof separator in block starting ' + chunk[:80])
        stripped.add(full)
        pieces.append(chunk[:cut] + ':= by sorry\n\n')
    missing = set(targets) - stripped
    if missing:
        raise ValueError('targets not found as theorem declarations: ' + ', '.join(sorted(missing)))
    return ''.join(pieces)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    target, source, *theorems = sys.argv[1:]
    source = Path(source).resolve()
    text = source.read_text()
    solution = PROJECT / 'AI4SSolutions' / (target + '.lean')
    challenge = PROJECT / 'AI4SChallenges' / (target + '.lean')
    solution.write_bytes(source.read_bytes())
    challenge.write_text(strip_proofs(text, set(theorems)))
    config = {
        'challenge_module': 'AI4SChallenges.' + target,
        'solution_module': 'AI4SSolutions.' + target,
        'theorem_names': theorems,
        'definition_names': [],
        'permitted_axioms': ['propext', 'Quot.sound', 'Classical.choice'],
        'enable_nanoda': False,
    }
    (PROJECT / 'configs' / (target + '.json')).write_text(json.dumps(config, indent=2) + '\n')
    print(json.dumps({'source': str(source), 'source_sha256': sha(source), 'solution_sha256': sha(solution),
                      'challenge': str(challenge), 'challenge_sha256': sha(challenge), 'theorems': len(theorems)}, indent=2))


if __name__ == '__main__':
    main()
