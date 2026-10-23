#!/usr/bin/env python3
"""Lexical scan of Lean sources for proof-escape and trust-expanding constructs.

Comments (nested /- -/ and --) and string literals are stripped first, so commented or quoted
mentions do not fire. Built-in controls: a positive control must fire and a comment/string-only
control must not; otherwise the scan aborts. Exit 0 iff no forbidden token appears.
"""
import json, re, sys, pathlib

FORBIDDEN = ['sorry', 'admit', 'axiom', 'native_decide', 'ofReduceBool', 'implemented_by',
             'extern', 'unsafe', 'opaque', 'partial', 'skipKernelTC', 'debug.skipKernelTC',
             'addDecl', 'elab', 'macro', 'syntax', 'initialize', 'run_cmd', '#eval',
             'decide_eq_true_axiom', 'Lean.ofReduceBool', 'trustCompiler', 'nativeDecide']
WORD = re.compile(r'(?<![A-Za-z0-9_.\'])(' + '|'.join(re.escape(t) for t in FORBIDDEN) + r')(?![A-Za-z0-9_\'])')

def strip(text):
    out, i, depth, n = [], 0, 0, len(text)
    while i < n:
        if depth == 0 and text.startswith('--', i):
            j = text.find('\n', i)
            i = n if j < 0 else j
        elif text.startswith('/-', i):
            depth += 1; i += 2
        elif depth > 0 and text.startswith('-/', i):
            depth -= 1; i += 2
        elif depth > 0:
            i += 1
        elif text[i] == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == '\\' else 1
            i = j + 1
        else:
            out.append(text[i]); i += 1
    return ''.join(out)

def hits(text):
    return sorted(set(m.group(1) for m in WORD.finditer(strip(text))))

def main(paths):
    assert hits('theorem t : True := by sorry') == ['sorry'], 'positive control did not fire'
    assert hits('-- sorry\n/- axiom native_decide /- nested -/ -/ def x := "sorry axiom"') == [], \
        'comment/string control fired'
    files = sorted(p for a in paths for p in pathlib.Path(a).rglob('*.lean'))
    report = {str(p): hits(p.read_text()) for p in files}
    bad = {k: v for k, v in report.items() if v}
    print(json.dumps({'files': len(files), 'flagged': bad, 'controls': 'passed'}, indent=1))
    return 1 if bad else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or ['.']))
