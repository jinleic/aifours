#!/usr/bin/env python3
"""Hardened successor to the pinned LOCAL verifier; never proves GLOBAL.

The earlier source and interval/AD engine are loaded by pinned bytes. Its
scientific assertions (including those in dynamically parsed engine classes)
are converted to always-active named checks; its fixed output write is replaced
by an in-memory capture. The original files and certificates are never edited.
"""
import argparse
import ast as builtin_ast
import hashlib
import json
import os
import signal
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RUNTIME_NAME = 'ph7_gate_runtime_v1.py'
RUNTIME_SHA = 'dc52b2d553ce357e919d1975fd1a94ada357f8a3276396bc1e4704d6d85b7c08'
LOCAL_NAME = 'frontier-20261029-ph7-local-global-dual-check.py'
LOCAL_SHA = 'cb2b9ede94c117ea44b6c100ee7dbfa4cb46d38531aea9de1bd3582892e085d8'
ENGINE_NAME = 'frontier-20261029-ph7-v4-local-spectral-optimality-check.py'
ENGINE_SHA = '6eed9b486726dcb79a8ad8d57c4106aa312c354df7cc7989c5887dd7a121813b'
ROOT_CERT_NAME = 'frontier-20261028-ph7-two-cycle-interval-certificate.json'
ROOT_CERT_SHA = '2e1aa9b765098d707d8803c82ccf756df5b696bdcc34616bea35dcc533c95f88'

# Bootstrap must verify exactly the bytes that it executes, BEFORE calling any
# function from the runtime. Failure here is a launch refusal, not a receipt.
def load_runtime():
    flags = os.O_RDONLY | getattr(os, 'O_NOFOLLOW', 0)
    fd = os.open(ROOT / RUNTIME_NAME, flags)
    try:
        with os.fdopen(fd, 'rb', closefd=False) as f: raw = f.read(65537)
    finally:
        os.close(fd)
    if len(raw) > 65536 or hashlib.sha256(raw).hexdigest() != RUNTIME_SHA:
        raise RuntimeError('RUNTIME_PIN_MISMATCH')
    ns = {'__name__': 'ph7_pinned_runtime'}
    exec(compile(raw, str(ROOT / RUNTIME_NAME), 'exec'), ns)
    return ns

class ActiveChecks(builtin_ast.NodeTransformer):
    def __init__(self, remove_output_guard=False):
        self.remove_output_guard = remove_output_guard
        self.output_guard_count = 0
        self.capture_count = 0
    def visit_Assert(self, node):
        # Only the old fixed-path output-exists assertion is replaced: the
        # successor claims a fresh, separately named output under its own gate.
        if self.remove_output_guard and node.lineno == 20:
            self.output_guard_count += 1
            return builtin_ast.copy_location(builtin_ast.Expr(builtin_ast.Call(builtin_ast.Name('guard_check', builtin_ast.Load()), [], [])), node)
        detail = node.msg if node.msg is not None else builtin_ast.Constant('scientific predicate')
        call = builtin_ast.Call(builtin_ast.Name('active_check', builtin_ast.Load()),
            [node.test, builtin_ast.Constant(f'SCIENTIFIC_ASSERT_LINE_{node.lineno}'), detail], [])
        return builtin_ast.copy_location(builtin_ast.Expr(call), node)
    def visit_Import(self, node):
        # The old source's ast.parse must pass through the same transformer for
        # its dynamically loaded engine declarations.
        if self.remove_output_guard and len(node.names) == 1 and node.names[0].name == 'ast':
            return builtin_ast.copy_location(builtin_ast.Pass(), node)
        return node
    def visit_Assign(self, node):
        self.generic_visit(node)
        if (self.remove_output_guard and len(node.targets) == 1
            and isinstance(node.targets[0], builtin_ast.Name)
            and node.targets[0].id == 'engine' and isinstance(node.value, builtin_ast.Dict)):
            node.value.keys.extend([builtin_ast.Constant('active_check'), builtin_ast.Constant('guard_check')])
            node.value.values.extend([builtin_ast.Name('active_check', builtin_ast.Load()),
                                      builtin_ast.Name('guard_check', builtin_ast.Load())])
        return node
    def visit_For(self, node):
        self.generic_visit(node)
        node.body.insert(0, builtin_ast.Expr(builtin_ast.Call(builtin_ast.Name('guard_check', builtin_ast.Load()), [], [])))
        return node
    def visit_While(self, node):
        self.generic_visit(node)
        node.body.insert(0, builtin_ast.Expr(builtin_ast.Call(builtin_ast.Name('guard_check', builtin_ast.Load()), [], [])))
        return node
    def visit_Call(self, node):
        self.generic_visit(node)
        if (self.remove_output_guard and isinstance(node.func, builtin_ast.Attribute)
            and isinstance(node.func.value, builtin_ast.Name) and node.func.value.id == 'OUT'
            and node.func.attr == 'write_text'):
            self.capture_count += 1
            node.func = builtin_ast.Name('capture_result', builtin_ast.Load())
        return node

def transform(raw, *, top_level):
    tree = builtin_ast.parse(raw)
    trans = ActiveChecks(remove_output_guard=top_level)
    tree = trans.visit(tree)
    builtin_ast.fix_missing_locations(tree)
    if top_level and (trans.output_guard_count != 1 or trans.capture_count != 1):
        raise RuntimeError('UNEXPECTED_LOCAL_SOURCE_LAYOUT')
    return tree

class AstProxy:
    # Keep the old engine-declaration parser, but transform assertions/loops.
    Module = builtin_ast.Module
    ClassDef = builtin_ast.ClassDef
    FunctionDef = builtin_ast.FunctionDef
    def parse(self, raw): return transform(raw, top_level=False)

def invoke_transformed(local_bytes, engine_bytes, guard, runtime, local_path):
    expected = hashlib.sha256(engine_bytes).hexdigest()
    runtime['require'](expected == ENGINE_SHA, 'ENGINE_BYTES_NOT_PINNED')
    captured = []
    def capture_result(text):
        runtime['require'](not captured and isinstance(text, str), 'DUPLICATE_OR_INVALID_LOCAL_OUTPUT')
        captured.append(runtime['strict_json'](text))
        return len(text)
    def active_check(condition, code, detail):
        runtime['require'](bool(condition), code, str(detail))
    env = {'__name__': 'ph7_local_hardened_invoke', '__file__': str(local_path),
           'ast': AstProxy(), 'active_check': active_check, 'guard_check': guard.check,
           'capture_result': capture_result, 'print': lambda *args, **kwargs: None}
    guard.check()
    exec(compile(transform(local_bytes, top_level=True), str(local_path)+' [active assertions]', 'exec'), env)
    guard.check()
    runtime['require'](len(captured) == 1, 'MISSING_LOCAL_RESULT')
    result = captured[0]
    runtime['require'](isinstance(result, dict) and result.get('scope') == 'LOCAL stage only; no global complement or supremum equality', 'INVALID_LOCAL_RESULT_SCOPE')
    return result

def main(argv=None):
    rt = load_runtime(); require = rt['require']; GateError = rt['GateError']
    parser = argparse.ArgumentParser(description='LOCAL proof replay only; does not grant or run GLOBAL verification')
    parser.add_argument('--run-id', required=True)
    parser.add_argument('--seconds', type=int, required=True)
    parser.add_argument('--rss-bytes', type=int, required=True)
    args = parser.parse_args(argv)
    require(args.run_id and len(args.run_id) <= 48 and all(c.isalnum() or c in '-_' for c in args.run_id), 'INVALID_RUN_ID')
    require(0 < args.seconds <= 3600 and 0 < args.rss_bytes <= 8*1024**3, 'INVALID_LOCAL_LIMITS')
    receipt = ROOT / ('local-hardened-'+args.run_id+'-receipt.json')
    output = ROOT / ('local-hardened-'+args.run_id+'-result.json')
    guard = rt['Guard'](args.seconds, args.rss_bytes)
    old_handlers = rt['install_latch'](guard)
    try:
        receipt_fd = rt['exclusive_create'](receipt)
    except BaseException:
        rt['restore_latch'](old_handlers)
        raise
    # All fallible initialization following claim is settled in finally.
    status = 'INCOMPLETE'; reason = 'UNSETTLED'; result_sha = None; started = time.time()
    try:
        require(not output.exists() and not output.is_symlink(), 'OUTPUT_ALREADY_EXISTS', str(output))
        guard.check()
        local = rt['read_pinned'](ROOT / LOCAL_NAME, LOCAL_SHA, 1024*1024)
        engine = rt['read_pinned'](ROOT / ENGINE_NAME, ENGINE_SHA, 1024*1024)
        rt['read_pinned'](ROOT / ROOT_CERT_NAME, ROOT_CERT_SHA, 1024*1024)
        guard.check()
        result = invoke_transformed(local, engine, guard, rt, ROOT / LOCAL_NAME)
        # Detect source drift during the run, even though the executed bytes are
        # already pinned. This never substitutes for pinning the input bytes.
        rt['read_pinned'](ROOT / LOCAL_NAME, LOCAL_SHA, 1024*1024)
        rt['read_pinned'](ROOT / ENGINE_NAME, ENGINE_SHA, 1024*1024)
        rt['read_pinned'](ROOT / ROOT_CERT_NAME, ROOT_CERT_SHA, 1024*1024)
        guard.check()
        data = (json.dumps(result, indent=1)+'\n').encode()
        require(len(data) <= 1024*1024, 'LOCAL_OUTPUT_TOO_LARGE')
        outfd = rt['exclusive_create'](output)
        try: rt['write_all'](outfd, data); os.fsync(outfd)
        finally: os.close(outfd)
        result_sha = rt['sha256'](data)
        guard.check(); status = 'LOCAL_COMPLETE_IMPORT_ROOT'; reason = 'all transformed local predicates passed'
    except BaseException as exc:
        status = 'INCOMPLETE'
        reason = f'{type(exc).__name__}: {exc}'
    finally:
        if guard is not None and guard.stop_signal is not None:
            status = 'INCOMPLETE'; reason = f'COOPERATIVE_SIGNAL_STOP: {guard.stop_signal}'
        record = {'status': status, 'reason': reason, 'scope': 'local only; imported root; no global assertion',
                  'started_unix': started, 'finished_unix': time.time(), 'pid': os.getpid(), 'pgid': os.getpgrp(),
                  'source_pins': {LOCAL_NAME: LOCAL_SHA, ENGINE_NAME: ENGINE_SHA, ROOT_CERT_NAME: ROOT_CERT_SHA, RUNTIME_NAME: RUNTIME_SHA},
                  'python': sys.version, 'result_name': output.name if result_sha else None, 'result_sha256': result_sha,
                  'observed_peak_rss_bytes': guard.max_observed_rss if guard else None,
                  'rss_limit_semantics': 'cooperative observed peak, not OS enforcement',
                  'guard_checks': guard.checks if guard else 0, 'signal': guard.stop_signal if guard else None}
        try:
            record = rt['settle_receipt'](receipt_fd, record, guard)
            status, reason = record['status'], record['reason']
        finally:
            os.close(receipt_fd)
            rt['restore_latch'](old_handlers)
    print(status, reason, 'receipt', receipt)
    return 0 if status == 'LOCAL_COMPLETE_IMPORT_ROOT' else 1

if __name__ == '__main__':
    try: raise SystemExit(main())
    except Exception as exc:
        print('LAUNCH_REFUSED', type(exc).__name__, str(exc), file=sys.stderr)
        raise SystemExit(2)
