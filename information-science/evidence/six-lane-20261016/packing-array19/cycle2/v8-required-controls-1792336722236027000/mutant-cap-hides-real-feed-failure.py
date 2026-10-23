def outcome(result):
    """Failed certification is scientific UNKNOWN. Independently ESTABLISHED transport corruption is evaluated FIRST
    and keeps a persistent INVALID integrity veto even with checker TIMEOUT, bounded stops or caps. Incomplete proof
    replay after an exact checker TIMEOUT is expected interruption; a completed mismatching delivery is not.
    """

    def unknown(reason, invalid=False, halt=False, sat=False, chunk_stop=False):
        return {'status': 'UNKNOWN', 'integrity_status': 'INVALID' if invalid else 'NOT_EVALUATED', 'integrity_errors': [reason] if invalid else [], 'unknown_reason': reason, 'sat_candidate': sat, 'halt_production': bool(halt or invalid or sat), 'chunk_stop': bool(chunk_stop or halt or invalid or sat)}
    sc, dc = (result.get('solver_collector', {}), result.get('checker_collector', {}))
    if result.get('solver_rc') == 10 or sc.get('status_lines') == ['s SATISFIABLE']:
        return unknown('unverified SAT candidate', sat=True)
    if any(('NOT VERIFIED' in str(v) for v in dc.get('status_lines', []))):
        return unknown('checker NOT VERIFIED', invalid=True)
    if dc.get('complete') and dc.get('status_lines') not in (['s VERIFIED'], ['s TIMEOUT']):
        return unknown('unexpected/duplicate/missing checker verdict', invalid=True)
    expected_bytes, expected_sha = (result.get('cnf_bytes'), result.get('cnf_sha256'))
    feeds, p, r = (result.get('cnf_feeds', {}), result.get('proof_stream', {}), result.get('proof_delivery', {}))
    for name, feed in feeds.items():
        n = feed.get('bytes')
        if type(n) is int and type(expected_bytes) is int and (n > expected_bytes):
            return unknown('CNF feed exceeded exact formula bytes: ' + name, invalid=True)
        if feed.get('complete') and (n != expected_bytes or feed.get('sha256') != expected_sha):
            return unknown('completed CNF delivery differs from pinned formula: ' + name, invalid=True)
        if feed.get('close_error'):
            return unknown('CNF FIFO close failed: ' + name, invalid=True)
        if False:
            return unknown('CNF transport failure (not bound-induced cancellation): ' + name, invalid=True)
    if p.get('reader_error'):
        return unknown('proof reader error', invalid=True)
    if r.get('complete') and (r.get('bytes') != p.get('raw_bytes') or r.get('sha256') != p.get('raw_sha256')):
        return unknown('completed proof replay differs from streamed proof', invalid=True)
    if type(r.get('bytes')) is int and type(p.get('raw_bytes')) is int and (not p.get('proof_cap_hit')) and (r['bytes'] > p['raw_bytes']):
        return unknown('proof replay exceeded streamed proof', invalid=True)
    if result.get('lifecycle_error'):
        return unknown('incomplete native lifecycle: ' + str(result['lifecycle_error']), invalid=True)
    if result.get('resource_refusal'):
        return unknown('worker solver/checker/preconstruction admission refused; recorded UNKNOWN, no persistent HALT', chunk_stop=True)
    if result.get('proof_integrity_error') or result.get('input_integrity_error'):
        return unknown('input/proof transport integrity failure', invalid=True)
    if result.get('proof_cap_hit'):
        return unknown('declared proof cap; not certified')
    if result.get('bounded_unknown'):
        return unknown('bounded native stop')
    if sc.get('error') or not sc.get('complete'):
        return unknown('solver collector incomplete/failed', invalid=True)
    sf = feeds.get('solver', {})
    if sf.get('error') or not sf.get('complete') or (not sf.get('close_ok')) or (sf.get('bytes') != expected_bytes) or (sf.get('sha256') != expected_sha):
        return unknown('solver CNF delivery incomplete', invalid=True)
    rc, s = (result.get('solver_rc'), sc.get('status_lines'))
    if rc == 0 and s in ([], ['s UNKNOWN']):
        return unknown('solver native limit/UNKNOWN')
    if rc != 20 or s != ['s UNSATISFIABLE']:
        return unknown('solver did not self-exit20 with exact UNSAT verdict', invalid=True)
    if set(feeds) != {'solver', 'checker'}:
        return unknown('both CNF feeds required', invalid=True)
    if not p.get('reader_complete'):
        return unknown('proof reader incomplete before checker stage', invalid=True)
    cf = feeds['checker']
    checker_feed_exact = bool(cf.get('complete') and cf.get('close_ok') and (cf.get('error') is None) and (cf.get('bytes') == expected_bytes) and (cf.get('sha256') == expected_sha))
    if dc.get('complete') and dc.get('error') is None and (dc.get('status_lines') == ['s TIMEOUT']):
        if not checker_feed_exact:
            return unknown('checker CNF feed not exact under TIMEOUT; corruption cannot be excluded', invalid=True)
        return unknown('checker native timeout; incomplete proof replay is expected interruption')
    if not checker_feed_exact:
        return unknown('checker CNF write/close/bytes/SHA failure', invalid=True)
    if result.get('checker_rc') != 0 or not dc.get('complete') or dc.get('error') or (dc.get('status_lines') != ['s VERIFIED']):
        return unknown('checker did not self-exit0 with exact VERIFIED verdict', invalid=True)
    if not r.get('complete') or r.get('error') or (not r.get('close_ok')) or (r.get('bytes') != p.get('raw_bytes')) or (r.get('sha256') != p.get('raw_sha256')):
        return unknown('proof replay/decompression/close incomplete or mismatched', invalid=True)
    return {'status': 'UNSAT', 'integrity_status': 'VALIDATED', 'integrity_errors': [], 'sat_candidate': False, 'halt_production': False}
