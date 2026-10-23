"""Parent finite check of the coloured-pattern vacancy step added to A1' in parity r2.
States are cyclic binary membership words. A legal elementary move flips one position whose two neighbours
have different colours; this moves exactly one cut to an adjacent vacant cut position and preserves block count.
For odd k=3..13 and every nonempty possible block count, require each state and its complement to be connected.
Control: k=4,m=2 has no vacancy; its two alternating states must be disconnected.
These finite checks support, not replace, the written all-k vacancy construction.
"""
import json
import subprocess
from pathlib import Path


def blocks(x, k):
    return sum(((x >> i) & 1) == 0 and ((x >> ((i + 1) % k)) & 1) == 1 for i in range(k))


def components(k, m):
    states = {x for x in range(1 << k) if blocks(x, k) == m}
    labels, components = {}, 0
    while states:
        root = states.pop()
        stack = [root]
        labels[root] = components
        while stack:
            x = stack.pop()
            for i in range(k):
                if ((x >> ((i - 1) % k)) & 1) == ((x >> ((i + 1) % k)) & 1):
                    continue
                y = x ^ (1 << i)
                if blocks(y, k) != m:
                    raise ValueError('Elementary move changed block count')
                if y in states:
                    states.remove(y)
                    labels[y] = components
                    stack.append(y)
        components += 1
    full = (1 << k) - 1
    return {'k': k, 'blocks': m, 'states': len(labels), 'components': components,
            'every_complement_reachable': all(labels[x] == labels[x ^ full] for x in labels)}


def main():
    rows = [components(k, m) for k in range(3, 14, 2) for m in range(1, k // 2 + 1)]
    negative = components(4, 2)
    rec = {'recorded': subprocess.run(['date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True).stdout.strip(),
           'rows': rows, 'no_vacancy_negative': negative,
           'verdict': 'PASS' if all(r['every_complement_reachable'] for r in rows)
           and not negative['every_complement_reachable'] and negative['components'] == 2 else 'FAIL'}
    with open(Path(__file__).with_suffix('.json'), 'x') as f:
        json.dump(rec, f, indent=1)
        f.write('\n')
    print(json.dumps({'verdict': rec['verdict'], 'parameter_cases': len(rows),
                      'states': sum(r['states'] for r in rows), 'negative': negative}))


if __name__ == '__main__':
    main()
