#!/usr/bin/env python3
"""Four exact individual Hamiltonian cycle-orbit controls, not decompositions."""
import collections
import hashlib
import json
import os
import signal
import subprocess
import sys
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))

def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()

def timeout(_signum, _frame):
    raise TimeoutError('30-second cap: UNKNOWN')

def inspect(q, cycle, expected_stabilizer):
    m = 12
    def g(x):
        return x // q * q + (x % q + 1) % q
    def canonical(c):
        j = c.index(0)
        return tuple(c[j:] + c[:j])
    def typ(x, y):
        return (x // q, y // q, (y % q - x % q) % q)
    assert len(cycle) == len(set(cycle)) == m and set(cycle) == set(range(m))
    orbit = []
    c = tuple(cycle)
    while c not in orbit:
        orbit.append(c)
        c = canonical([g(x) for x in c])
    assert c == orbit[0]
    s = q // len(orbit)
    assert s == expected_stabilizer and s * len(orbit) == q
    L = m // s
    jumps = [typ(cycle[j], cycle[(j+1)%m])[2] for j in range(m)]
    assert all(jumps[j] == jumps[(j+L)%m] for j in range(m))
    def power(x, t):
        for _ in range(t):
            x = g(x)
        return x
    assert any(all(cycle[(j+L)%m] == power(cycle[j], t) for j in range(m))
               for t in range(q))
    d1 = collections.Counter(typ(cycle[j], cycle[(j+1)%m]) for j in range(L))
    d2 = collections.Counter(typ(cycle[j], cycle[(j+2)%m]) for j in range(L))
    full1 = collections.Counter(typ(c[j], c[(j+1)%m]) for c in orbit for j in range(m))
    full2 = collections.Counter(typ(c[j], c[(j+2)%m]) for c in orbit for j in range(m))
    assert all(full1[t] == q * k for t, k in d1.items()) and len(full1) == len(d1)
    assert all(full2[t] == q * k for t, k in d2.items()) and len(full2) == len(d2)
    assert all(k == 1 for k in d1.values()), 'within-orbit D1 collision'
    one = sum(t[2] * k for t, k in d1.items())
    two = sum(t[2] * k for t, k in d2.items())
    assert (two - 2*one) % q == 0
    assert (two + 1 - 2*one) % q != 0
    return {'q': q, 'stabilizer': s, 'orbit_size': len(orbit), 'period_L': L,
            'representative_cycle': list(cycle), 'distinct_D1_types': len(d1),
            'distinct_D2_types': len(d2), 'D2_type_repeats': sum(k-1 for k in d2.values()),
            'jump_one_mod_q': one % q, 'jump_two_mod_q': two % q,
            'negative': 'rejected: perturbing D2 moment breaks the jump identity'}

def main():
    out = {'started_native': clock(), 'source_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
           'cap_seconds': 30,
           'scope': 'isolated actual 12-vertex Hamiltonian cycle orbits; not a decomposition or T2 witness'}
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(30)
    rc = 0
    try:
        samples = [(2, list(range(12)), 1),
                   (2, [0,2,4,6,8,10,1,3,5,7,9,11], 2),
                   (3, [0,9,1,11,3,2,10,6,4,5,7,8], 1),
                   (3, [0,3,6,9,1,4,7,10,2,5,8,11], 3)]
        out['samples'] = [inspect(q, cycle, s) for q, cycle, s in samples]
        out['status'] = 'PASS'
    except TimeoutError as exc:
        out['status'] = 'UNKNOWN_TIMEOUT'
        out['detail'] = str(exc)
        rc = 124
    except Exception:
        out['status'] = 'FAIL'
        out['detail'] = traceback.format_exc()
        rc = 1
    finally:
        signal.alarm(0)
        out['ended_native'] = clock()
        out['program_exit_intended'] = rc
        text = json.dumps(out, indent=2, sort_keys=True) + '\n'
        with open(os.path.join(HERE, 'reviewer-control-twelve-orbits-result.json'), 'x', encoding='utf-8') as f:
            f.write(text)
        print(text, end='')
    return rc

if __name__ == '__main__':
    sys.exit(main())
