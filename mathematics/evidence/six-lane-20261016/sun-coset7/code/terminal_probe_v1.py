#!/usr/bin/env python3
"""terminal_probe_v1 -- deterministic, isolated injection probe for the terminal-SIGTERM rule of core7_engine_v4.

A sanity control, never gate evidence. One process: no children, no sleeps, no timeouts.
Usage:  python3 code/terminal_probe_v1.py MODE OUTDIR ENGINE_PATH      (MODE in T1, T2, T3)

Each mode loads the engine file as a module, creates OUTDIR, runs universe MSP45 to completion through the
engine's own run_universe (expected COMPLETE), and then sends ONE SIGTERM to its own process at a fixed
point of publication:
  T1  after run_universe returned and before write_outputs. The engine's handler must have latched
      Guard.term before publication starts; this precondition is recorded.
  T2  inside write_outputs after SIGTERM is blocked and before the status decision, on the first call of
      the engine's _gz_bounded (wrapped by this probe).
  T3  inside write_outputs after the status decision, on the first call of the engine's peak_rss_bytes
      while the run.json fields are built (wrapped by this probe).
Expected:
  T1, T2: published status UNKNOWN, status_before_publication COMPLETE, sigterm_received true, stop_reason =
          the engine's coercion reason, no post_publication_sigterm.json.
  T3:     published status COMPLETE, sigterm_received false, post_publication_sigterm.json present, and
          post_publication_sigterm set in the returned record (the engine's main() exits 3 in that case).
Writes OUTDIR/probe.json (exclusive) with every observation and check; exit 0 iff all checks hold.
"""
import hashlib
import importlib.util
import json
import os
import signal
import sys

COERCION_REASON = 'SIGTERM received after the search loop (status coerced to UNKNOWN at publication)'
CERT_FILES = ('leaves.jsonl.gz', 'vfc_killed.json.gz', 'lp_duals.json.gz', 'survivors.json', 'run.json')


def main():
    mode, outdir, engine = sys.argv[1], os.path.abspath(sys.argv[2]), os.path.abspath(sys.argv[3])
    if mode not in ('T1', 'T2', 'T3'):
        raise SystemExit('unknown mode')
    with open(engine, 'rb') as f:
        engine_sha = hashlib.sha256(f.read()).hexdigest()
    spec = importlib.util.spec_from_file_location('core7_engine_probe', engine)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    os.makedirs(outdir, exist_ok=False)
    status, profs, stats, survivors, leaflines = m.run_universe('MSP45', outdir, 60.0)
    obs = {'probe': 'terminal_probe_v1', 'mode': mode, 'engine': engine, 'engine_sha256': engine_sha,
           'search_status': status}
    fired = []
    if mode == 'T1':
        os.kill(os.getpid(), signal.SIGTERM)
        obs['term_latched_before_publication'] = bool(m.GUARD.term)
    elif mode == 'T2':
        orig_gz = m._gz_bounded

        def gz_inject(chunks, limit):
            if not fired:
                fired.append('T2')
                os.kill(os.getpid(), signal.SIGTERM)
            return orig_gz(chunks, limit)
        m._gz_bounded = gz_inject
        obs['term_latched_before_publication'] = bool(m.GUARD.term)
    else:
        orig_rss = m.peak_rss_bytes

        def rss_inject():
            if not fired:
                fired.append('T3')
                os.kill(os.getpid(), signal.SIGTERM)
            return orig_rss()
        m.peak_rss_bytes = rss_inject
        obs['term_latched_before_publication'] = bool(m.GUARD.term)
    run = m.write_outputs(outdir, 'MSP45', status, profs, stats, survivors, leaflines)
    with open(os.path.join(outdir, 'run.json')) as f:
        disk = json.load(f)
    obs.update({'injection_fired': fired, 'published_status': disk.get('status'),
                'status_before_publication': disk.get('status_before_publication'),
                'sigterm_received': disk.get('sigterm_received'), 'stop_reason': disk.get('stop_reason'),
                'returned_post_publication_sigterm': run.get('post_publication_sigterm', False),
                'marker_present': os.path.exists(os.path.join(outdir, 'post_publication_sigterm.json')),
                'files_present': all(os.path.exists(os.path.join(outdir, x)) for x in CERT_FILES),
                'sigterm_pending_at_end': signal.SIGTERM in signal.sigpending()})
    c = {'search_complete': status == 'COMPLETE', 'files_present': obs['files_present']}
    if mode == 'T1':
        c['latched_before_publication'] = obs['term_latched_before_publication'] is True
    else:
        c['not_latched_before_publication'] = obs['term_latched_before_publication'] is False
        c['injection_fired'] = fired == [mode]
    if mode in ('T1', 'T2'):
        c['published_unknown'] = obs['published_status'] == 'UNKNOWN'
        c['before_complete'] = obs['status_before_publication'] == 'COMPLETE'
        c['sigterm_recorded'] = obs['sigterm_received'] is True
        c['reason_coercion'] = obs['stop_reason'] == COERCION_REASON
        c['no_marker'] = not obs['marker_present'] and not obs['returned_post_publication_sigterm']
    else:
        c['published_complete'] = obs['published_status'] == 'COMPLETE'
        c['sigterm_not_in_status'] = obs['sigterm_received'] is False
        c['marker'] = obs['marker_present'] and obs['returned_post_publication_sigterm'] is True
    obs['checks'] = c
    obs['pass'] = all(c.values())
    with open(os.path.join(outdir, 'probe.json'), 'x') as f:
        json.dump(obs, f, indent=1, default=str)
    print(json.dumps({'mode': mode, 'pass': obs['pass'], 'checks': c}))
    sys.exit(0 if obs['pass'] else 1)


if __name__ == '__main__':
    main()
