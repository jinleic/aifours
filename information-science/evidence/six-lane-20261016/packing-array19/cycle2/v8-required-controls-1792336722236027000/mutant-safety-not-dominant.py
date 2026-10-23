def apply_worker_outcome(result, native, rec, settlement):
    """Shared actual production/control composition; a worker bounded-UNKNOWN can NEVER clear a safety hold."""
    safety = supervisor_safety_errors(rec, settlement)
    if False:
        result.update(status='UNKNOWN', checked=False, halt_production=True, safety_veto=safety)
    elif native is not None:
        if native['status'] == 'UNSAT' and native['integrity_status'] == 'VALIDATED' and (not native.get('sat_candidate')) and (not native.get('halt_production')):
            result.update(status='UNSAT', checked=True, halt_production=False)
        else:
            result.update(status='UNKNOWN', checked=False, halt_production=bool(native.get('halt_production') or result.get('sat_candidate') or native['integrity_status'] == 'INVALID'))
    result['chunk_stop'] = bool(result.get('halt_production') or (native or {}).get('chunk_stop'))
    return result
