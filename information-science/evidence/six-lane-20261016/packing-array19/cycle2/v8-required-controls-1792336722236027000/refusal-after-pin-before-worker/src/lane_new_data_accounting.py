#!/usr/bin/env python3
"""Conservative byte accounting for the original additional lane-data cap (no data mutation).
The known cycle-2 baseline is 2026-10-17 05:23 PDT (checkpoints.md checkpoint1). Use the EARLIER 05:22:00 cutoff;
charge the FULL current size/allocation of every lane entry born OR modified at/after that cutoff (including
archives/caches/directories), and every entry lacking a readable birth time. Thus copies with preserved mtimes are
still charged by birth time; modified baseline files are charged in full rather than just net growth; moves retain
the same charged bytes. Pre-cutoff unchanged baseline proof/CNF data is not new data. Hardlinks are conservatively
charged per path. Count both logical bytes and st_blocks*512 exactly over this conservative selected set; usage is
the larger sum. This is an upper-bound accounting set, not an invented exact pre-run file inventory.
Enforce10,000,000,000B (stricter than the parent10GiB cap); also report remaining allowance under10GiB. Any stat error
makes admission unknown/refused. No content read, deletion, compression or proof/CNF copies.
"""
import datetime
import os
import stat
import time

CUTOFF_ISO = '2026-10-17T05:22:00-07:00'
CUTOFF = datetime.datetime.fromisoformat(CUTOFF_ISO).timestamp()
ENFORCED_CAP_BYTES = 10000000000
ORIGINAL_CAP_BYTES = 10 * 1024 * 1024 * 1024


def account(lane):
    logical = allocated = selected = total = 0
    errors = []
    pending = [os.fspath(lane)]
    while pending:
        path = pending.pop()
        try:
            st = os.lstat(path)
        except OSError as exc:
            errors.append({'path': os.path.relpath(path, lane), 'error': str(exc)})
            continue
        total += 1
        born = getattr(st, 'st_birthtime', None)
        charge = born is None or born >= CUTOFF or st.st_mtime >= CUTOFF
        if charge:
            selected += 1
            logical += st.st_size
            allocated += getattr(st, 'st_blocks', (st.st_size + 511) // 512) * 512
        if stat.S_ISDIR(st.st_mode):
            try:
                with os.scandir(path) as entries:
                    pending.extend(entry.path for entry in entries)
            except OSError as exc:
                errors.append({'path': os.path.relpath(path, lane), 'error': str(exc)})
    usage = max(logical, allocated)
    return {'host_clock': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'policy': 'conservative full-byte charge by birth-or-modification cutoff; not net baseline subtraction',
            'cutoff_host_clock': CUTOFF_ISO, 'entries_seen': total, 'entries_charged': selected,
            'charged_logical_bytes': logical, 'charged_allocated_bytes': allocated,
            'new_data_usage_upper_bytes': usage, 'original_10gib_cap_bytes': ORIGINAL_CAP_BYTES,
            'remaining_original_allowance_bytes': ORIGINAL_CAP_BYTES - usage,
            'enforced_cap_bytes': ENFORCED_CAP_BYTES, 'remaining_enforced_allowance_bytes': ENFORCED_CAP_BYTES - usage,
            'stat_errors': errors, 'known': not errors}
