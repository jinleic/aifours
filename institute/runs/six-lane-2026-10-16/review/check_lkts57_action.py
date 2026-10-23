"""Audit the claimed G513 construction action on the pinned, verified LKTS(57).

The mathematical existence check is separate. This script reconstructs the group from the
three stated point permutations, verifies generator action on every block in every constituent,
and distinguishes automorphisms of block sets from automorphisms of chosen resolutions.
No worker code or solver output is imported. The parent certificate parser is shared explicitly.
"""
from __future__ import annotations

import argparse
from collections import Counter, deque
import hashlib
from itertools import combinations
import json
from pathlib import Path

from check_lkts_independent import parse

EXPECTED_SHA = '09a9d8ca0602ed28541e170ada7f096871311c29fd4515b6fea3e25f72b05f09'


def need(condition: bool, reason: str) -> None:
    if not condition:
        raise ValueError(reason)


def compose(left: tuple, right: tuple) -> tuple:
    return tuple(left[right[x]] for x in range(len(right)))


def orbit_partition(elements, generators):
    remaining = set(elements)
    result = []
    while remaining:
        start = min(remaining)
        orbit, queue = {start}, deque([start])
        while queue:
            value = queue.popleft()
            for action in generators:
                image = action(value)
                if image not in orbit:
                    orbit.add(image)
                    queue.append(image)
        need(orbit <= remaining, 'overlapping orbit partition')
        remaining.difference_update(orbit)
        result.append(orbit)
    return result


def audit(path: Path) -> dict:
    data = path.read_bytes()
    need(hashlib.sha256(data).hexdigest() == EXPECTED_SHA, 'wrong certificate identity')
    v, systems = parse(data)
    need(v == 57 and len(systems) == 55, 'wrong certificate scope')
    blocks = [frozenset(t for cls in system for t in cls) for system in systems]
    need(all(len(b) == 532 for b in blocks), 'wrong block count')
    owners = {b: i for i, constituent in enumerate(blocks) for b in constituent}
    need(len(owners) == 29260, 'certificate is not block-disjoint')
    resolutions = [frozenset(frozenset(cls) for cls in system) for system in systems]
    generators = {
        'tau': tuple(19*(x//19) + (x%19+1)%19 for x in range(57)),
        'nu': tuple(19*((x//19+1)%3) + (4*(x%19))%19 for x in range(57)),
        'rho': tuple(19*((x//19+1)%3) + x%19 for x in range(57)),
    }

    def image_block(permutation, block):
        return tuple(sorted(permutation[x] for x in block))

    def constituent_action(permutation):
        images = []
        for i, constituent in enumerate(blocks):
            image = frozenset(image_block(permutation, block) for block in constituent)
            target = owners[next(iter(image))]
            need(image == blocks[target], f'not a constituent image: source {i}')
            images.append(target)
        need(len(set(images)) == 55, 'constituent action not bijective')
        return tuple(images)

    actions, resolution_counts = {}, {}
    for name, permutation in generators.items():
        need(set(permutation) == set(range(57)), 'not a point permutation')
        actions[name] = constituent_action(permutation)
        preserved = 0
        for i, classes in enumerate(resolutions):
            image = frozenset(frozenset(image_block(permutation, t) for t in cls) for cls in classes)
            preserved += image == resolutions[actions[name][i]]
        resolution_counts[name] = preserved

    identity = tuple(range(57))
    group, queue = {identity}, deque([identity])
    while queue:
        element = queue.popleft()
        for gen in generators.values():
            image = compose(gen, element)
            if image not in group:
                group.add(image)
                queue.append(image)
    need(len(group) == 513, 'wrong generated group order')
    constituent_orbits = orbit_partition(range(55), [lambda i, p=p: p[i] for p in actions.values()])
    point_orbits = orbit_partition(range(57), [lambda x, p=p: p[x] for p in generators.values()])
    triple_orbits = orbit_partition(combinations(range(57), 3),
                                   [lambda t, p=p: image_block(p, t) for p in generators.values()])
    sizes = sorted(map(len, constituent_orbits))
    need(sizes == [9, 9, 9, 9, 19], 'wrong constituent orbit pattern')
    swap = list(range(57))
    swap[0], swap[1] = swap[1], swap[0]
    try:
        constituent_action(tuple(swap))
    except ValueError as exc:
        need(str(exc).startswith('not a constituent image:'), 'wrong mutation failure')
        swap_control = {'rejected': True, 'reason': str(exc)}
    else:
        raise ValueError('point transposition incorrectly accepted as automorphism')
    return {
        'status': 'G513_CONSTRUCTION_ACTION_VERIFIED',
        'certificate_sha256': EXPECTED_SHA,
        'group_order': len(group),
        'point_orbit_sizes': sorted(map(len, point_orbits)),
        'constituent_orbit_sizes': sizes,
        'constituent_orbits': [sorted(o) for o in constituent_orbits],
        'constituent_stabilizer_orders': [len(group)//len(o) for o in constituent_orbits],
        'triple_orbit_size_counts': dict(sorted(Counter(map(len, triple_orbits)).items())),
        'point_generator_images': generators,
        'constituent_generator_images': actions,
        'chosen_resolution_images_preserved_out_of_55': resolution_counts,
        'negative_control_point_transposition': swap_control,
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'shared_dependency': 'check_lkts_independent.parse; existence verification is a separate gate.',
        'limits': 'Certifies this explicit action, not a proof that its orbit pattern is forced for all LKTS(57). No novelty or uniform-family claim.',
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument('certificate', type=Path)
    p.add_argument('--output', type=Path)
    args = p.parse_args()
    result = audit(args.certificate)
    text = json.dumps(result, indent=2) + '\n'
    if args.output:
        with args.output.open('x') as stream:
            stream.write(text)
    print(text, end='')


if __name__ == '__main__':
    main()
