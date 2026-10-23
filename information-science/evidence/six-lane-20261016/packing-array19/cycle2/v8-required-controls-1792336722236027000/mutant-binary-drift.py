def full_gate(lease, phase, lane=LANE, providers=None):
    """Last operation before every admission. Expensive census refresh precedes final fresh guards/hash checks."""
    p, errors = (providers or {}, [])
    accounting, rss, binaries, count, free, required = (None, {'known': False}, {}, None, None, None)
    try:
        accounting = p['census']() if 'census' in p else census_for_gate(lease['census_reference'], bool(lease.get('force_census_refresh')), lane)
        lease['census_reference'] = accounting['reference']
        lease['force_census_refresh'] = False
        bound = lease['whole_plan_remaining_bound_bytes']
        if type(bound) is not int or bound < ALL_PLANNED_RETAINED_BOUND:
            errors.append('whole-plan bound missing/narrowed')
        if type(accounting.get('current_data_upper_bytes')) is not int or accounting['current_data_upper_bytes'] < 0:
            errors.append('unknown allocated-data bytes')
        elif accounting['current_data_upper_bytes'] + bound + OTHER_WRITER_MARGIN > DATA_CAP:
            errors.append('allocated-data cap with whole-plan reservation/margin')
        if not 0 <= accounting['age_seconds'] <= CENSUS_TTL:
            errors.append('stale/unknown census age')
        rss = p['rss']() if 'rss' in p else lane_rss(lane, os.getpgrp() if phase != 'construct' else None, lease['owner_pid'])
        if not isinstance(rss, dict) or rss.get('known') is not True or type(rss.get('rss_bytes')) is not int or (rss['rss_bytes'] < 0):
            errors.append('unknown RSS/headroom')
        else:
            if lease['group_rss_cap_bytes'] != GROUP_RSS_CAP or lease['busy_units'] != 2 or lease['lane_busy_ceiling'] != 4:
                errors.append('wrong normal resource budget')
            current = rss.get('current_group_and_owner_bytes')
            if type(current) is not int or not 0 <= current <= rss['rss_bytes']:
                errors.append('unknown current-group RSS')
            elif rss['rss_bytes'] + max(0, GROUP_RSS_CAP - current) + CONTROL_MARGIN > LANE_CAP:
                errors.append('RSS headroom')
            members = rss.pop('members', None)
            if members is not None:
                rss['member_count'] = len(members)
                rss['member_set_sha256'] = hashlib.sha256(json.dumps(members, sort_keys=True).encode()).hexdigest()
        binaries = p['binaries']() if 'binaries' in p else binary_observations(lease['binary_authority'])
        if set(binaries) != {'python', 'solver', 'checker'} or any((v.get('matches') is not True for v in binaries.values())):
            pass
        count = p['count']() if 'count' in p else token_count(lane)
        if type(count) is not int or not 0 <= count <= 2:
            errors.append('COUNT ceiling/format')
        if count == 0 and phase != 'checker':
            errors.append('new admissions paused')
        if _CANCEL[0]:
            errors.append('owner cancelled')
        for name in ADMISSION_MARKERS:
            if (Path(lane) / 'cycle2' / name).exists():
                errors.append('STOP/veto ' + name)
        growth = lease['projected_growth_bytes']
        if type(growth) is not int or growth < ITEM_GROWTH:
            errors.append('unknown/narrow projected retained growth')
        required = BASE_GATE + growth
        free = p['free']() if 'free' in p else (lambda s: s.f_bavail * s.f_frsize)(os.statvfs(lane))
        if type(free) is not int or free < required:
            errors.append('fresh statvfs growth/floor gate')
        now = p['clock']() if 'clock' in p else time.monotonic()
        allowance = 1450 if phase == 'checker' else 2200
        if now + allowance > lease['chunk_deadline_monotonic'] or now + allowance > lease['item_deadline_monotonic']:
            errors.append('deadline allowance')
        if 'census' not in p:
            accounting['age_seconds'] = time.monotonic() - accounting['finished_monotonic']
            if accounting['age_seconds'] > CENSUS_TTL:
                errors.append('census expired before admission')
    except (OSError, ValueError, KeyError, TypeError, RuntimeError, AssertionError) as exc:
        errors.append('gate measurement/authority error: ' + repr(exc))
    return {'phase': phase, 'at_monotonic': time.monotonic(), 'count': count, 'free_bytes': free, 'required_free_bytes': required, 'rss': rss, 'binary_observations': binaries, 'census': accounting, 'whole_plan_remaining_bound_bytes': lease.get('whole_plan_remaining_bound_bytes'), 'other_writer_margin_bytes': OTHER_WRITER_MARGIN, 'additional_data_cap_bytes': DATA_CAP, 'group_rss_cap_bytes': GROUP_RSS_CAP, 'busy_units': 2, 'lane_busy_ceiling': 4, 'projected_growth_bytes': lease.get('projected_growth_bytes'), 'chunk_deadline_monotonic': lease.get('chunk_deadline_monotonic'), 'item_deadline_monotonic': lease.get('item_deadline_monotonic'), 'next_phase_allowance_seconds': 1450 if phase == 'checker' else 2200, 'errors': errors, 'admitted': not errors}
