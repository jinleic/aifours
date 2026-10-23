#!/usr/bin/env python3
"""Lexically scan Lean sources for proof escapes after removing comments and literals.

This is supporting evidence only; Comparator axiom checks and kernel replay are separate gates.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

PATTERNS = {
    'sorry': r'\bsorry\b',
    'admit': r'\badmit\b',
    'axiom_decl': r'\baxiom\b',
    'native_decide': r'\bnative_decide\b',
    'native_option': r'native\s*:=\s*true|\+\s*native\b',
    'ofReduceBool': r'\bofReduceBool\b|\breduceBool\b',
    'implemented_by': r'\bimplemented_by\b',
    'extern': r'\bextern\b',
    'unsafe': r'\bunsafe\b',
    'skipKernelTC': r'skipKernelTC',
    'csimp': r'\bcsimp\b',
    'opaque': r'\bopaque\b',
    'partial': r'\bpartial\b',
    'addDecl': r'\baddDecl\b',
    'meta_definition': r'^\s*(?:@\[[^\]]*\]\s*)?(?:elab|macro|syntax|macro_rules|elab_rules|declare_syntax_cat)\b',
    'initialize': r'\binitialize\b|\bbuiltin_initialize\b',
    'run_cmd_or_eval': r'\brun_cmd\b|\brun_tac\b|\brun_elab\b|#eval\b',
    'lean_meta_import': r'^\s*import\s+Lean\b',
    'heartbeats_zero': r'set_option\s+maxHeartbeats\s+0\b',
}
IDENTIFIER = re.compile(r"[A-Za-z0-9_'.!?₀-₉ₐ-ₜα-ωΑ-Ω]")


def strip_lean(text):
    """Replace comments, strings and char literals by spaces, preserving line numbers."""
    out = []
    i = 0
    depth = 0
    n = len(text)
    while i < n:
        if depth:
            if text.startswith('/-', i):
                depth += 1
                out.append('  ')
                i += 2
            elif text.startswith('-/', i):
                depth -= 1
                out.append('  ')
                i += 2
            else:
                out.append('\n' if text[i] == '\n' else ' ')
                i += 1
            continue
        if text.startswith('/-', i):
            depth = 1
            out.append('  ')
            i += 2
        elif text.startswith('--', i):
            while i < n and text[i] != '\n':
                out.append(' ')
                i += 1
        elif text[i] == '"':
            out.append(' ')
            i += 1
            while i < n and text[i] != '"':
                if text[i] == '\\' and i + 1 < n:
                    out.append('  ')
                    i += 2
                    continue
                out.append('\n' if text[i] == '\n' else ' ')
                i += 1
            out.append(' ')
            i += 1
        elif text[i] == "'" and (i == 0 or not IDENTIFIER.match(text[i - 1])):
            match = re.match(r"'(\\.|[^\\'])'", text[i:])
            if match:
                out.append(' ' * len(match.group(0)))
                i += len(match.group(0))
            else:
                out.append(text[i])
                i += 1
        else:
            out.append(text[i])
            i += 1
    if depth:
        raise ValueError('unterminated block comment')
    return ''.join(out)


def scan_text(text):
    code = strip_lean(text)
    hits = {}
    for name, pattern in PATTERNS.items():
        regex = re.compile(pattern, re.MULTILINE)
        lines = sorted({code.count('\n', 0, match.start()) + 1 for match in regex.finditer(code)})
        if lines:
            hits[name] = lines
    declarations = re.findall(r'^\s*(?:@\[[^\]]*\]\s*)*(?:private\s+|protected\s+|noncomputable\s+)*(theorem|lemma|def|abbrev|structure|inductive|class|instance)\s+([^\s:({\[]+)', code, re.MULTILINE)
    imports = re.findall(r'^\s*import\s+(\S+)', code, re.MULTILINE)
    return hits, declarations, imports


def controls():
    must_fire = 'theorem bad : False := by sorry\naxiom cheat : False\n'
    must_not_fire = '/- sorry /- nested axiom -/ admit -/\n-- native_decide\ntheorem ok : "sorry" = "sorry" := rfl\n'
    fire_hits, _, _ = scan_text(must_fire)
    quiet_hits, _, _ = scan_text(must_not_fire)
    return {
        'positive_detected': sorted(fire_hits),
        'positive_ok': {'sorry', 'axiom_decl'} <= set(fire_hits),
        'comment_string_false_positives': sorted(quiet_hits),
        'negative_ok': not quiet_hits,
    }


def main(paths):
    report = {'controls': controls(), 'files': {}}
    for raw in paths:
        path = Path(raw).resolve()
        text = path.read_text()
        hits, declarations, imports = scan_text(text)
        report['files'][str(path)] = {
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'lines': text.count('\n') + 1,
            'imports': imports,
            'declaration_counts': {kind: sum(1 for k, _ in declarations if k == kind) for kind in sorted({k for k, _ in declarations})},
            'forbidden_hits': hits,
        }
    report['clean'] = report['controls']['positive_ok'] and report['controls']['negative_ok'] and not any(
        entry['forbidden_hits'] for entry in report['files'].values())
    print(json.dumps(report, indent=2))
    return 0 if report['clean'] else 1


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
