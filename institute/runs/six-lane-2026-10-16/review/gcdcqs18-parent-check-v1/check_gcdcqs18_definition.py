#!/usr/bin/env python3
"""Definition-first Format S verifier for gcDCQS(18^4:2).
No claimant code, symmetry, orbit, seed or solver result is used.
Usage: python3 -B check_gcdcqs18_definition.py FILE EXPECTED_SHA256 NEW_RECEIPT.json
"""
from collections import Counter
from datetime import datetime
import hashlib
from itertools import combinations
import json
from pathlib import Path
import re
import resource
import sys
import time
from zoneinfo import ZoneInfo


class CertificateError(ValueError):
    def __init__(self, condition, category, reason, details=None):
        super().__init__(reason)
        self.condition = condition
        self.category = category
        self.details = details or {}


def require(test, condition, category, reason, **details):
    if not test:
        raise CertificateError(condition, category, reason, details)


def powers(values):
    return ' '.join('%d^%d' % item for item in sorted(Counter(values).items(), reverse=True))


class Parser:
    """Every noncomment, nonblank line is consumed by one grammar production.

    Headers and section types follow the order in README section 3. POINT and
    STEMPOINT sections may be permuted within their type, since Format S does
    not specify a numeric order for them; they must occur exactly once each.
    CLASS indices are strictly 0..r-1 in order. FRAME k repeats legitimately
    (k names the omitted group, not a distinct class index).
    """
    keywords = {'GCDCQS', 'COLOURS', 'HOLEFREE', 'GROUPS', 'STEM', 'BLOCKS',
                'POINT', 'CLASS', 'STEMPOINT', 'FRAME'}

    def __init__(self, text):
        self.rows = []
        for line_no, line in enumerate(text.split('\n'), 1):
            content = line.split('#', 1)[0].strip()
            if content:
                self.rows.append((line_no, content.split()))
        self.pos = 0
        self.v = 74

    def peek(self):
        return self.rows[self.pos][1][0] if self.pos < len(self.rows) else None

    def integer(self, token, line_no, what):
        require(re.fullmatch(r'0|[1-9][0-9]*', token) is not None,
                'parse', 'format.integer', 'Malformed unsigned integer',
                line=line_no, context=what, token=token)
        return int(token)

    def take(self):
        require(self.pos < len(self.rows), 'parse', 'format.truncated', 'Unexpected end of file')
        line_no, words = self.rows[self.pos]
        self.pos += 1
        return line_no, words

    def header(self, name, arity):
        line_no, words = self.take()
        require(words[0] in self.keywords, 'parse', 'format.unknown_line',
                'Unknown noncomment line', line=line_no, tokens=words)
        require(words[0] == name, 'parse', 'format.order',
                'Wrong section or header order', line=line_no, expected=name, actual=words[0])
        require(len(words) == arity + 1, 'parse', 'format.record',
                'Wrong header field count', line=line_no, context=name, tokens=words)
        return [self.integer(w, line_no, name) for w in words[1:]]

    def record(self, size, context):
        line_no, words = self.take()
        require(words[0] not in self.keywords and re.fullmatch(r'0|[1-9][0-9]*', words[0]) is not None,
                'parse', 'format.unknown_line', 'Expected a numeric point record',
                line=line_no, context=context, tokens=words)
        require(len(words) == size, 'parse', 'format.record', 'Wrong point-record field count',
                line=line_no, context=context, expected=size, actual=len(words))
        points = tuple(self.integer(w, line_no, context) for w in words)
        require(all(0 <= x < self.v for x in points), 'parse', 'range.point',
                'Point label outside 0..73', line=line_no, context=context, points=points)
        require(len(set(points)) == size, 'parse', 'format.distinct_points',
                'Repeated point in a record', line=line_no, context=context, points=points)
        return tuple(sorted(points)), line_no

    def triples(self, used, context):
        result = []
        while self.peek() is not None and self.peek() not in self.keywords:
            triple, line_no = self.record(3, context)
            require(triple not in used, 'parse', 'format.duplicate_derived_triple',
                    'Derived triple listed more than once at one point',
                    line=line_no, first_line=used.get(triple), context=context, triple=triple)
            used[triple] = line_no
            result.append(triple)
        return result

    def parse(self):
        v, n, g, s = self.header('GCDCQS', 4)
        require((v, n, g, s) == (74, 4, 18, 2), 'a', 'a.parameters',
                'Certificate parameters are not gcDCQS(18^4:2)', actual=[v, n, g, s])
        self.v = v
        r, = self.header('COLOURS', 1)
        t, = self.header('HOLEFREE', 1)
        require(r == 37 and t == 10, 'a', 'a.colouring_parameters',
                'COLOURS/HOLEFREE disagree with source formula', colours=r, holefree=t)
        self.header('GROUPS', 0)
        groups = [self.record(g, 'group %d' % k)[0] for k in range(n)]
        self.header('STEM', 0)
        stem = self.record(s, 'stem')[0]
        self.header('BLOCKS', 0)
        blocks, seen_blocks = [], {}
        while self.peek() not in (None, 'POINT', 'STEMPOINT'):
            block, line_no = self.record(4, 'block')
            require(block not in seen_blocks, 'parse', 'format.duplicate_block',
                    'Block listed more than once', line=line_no,
                    first_line=seen_blocks.get(block), block=block)
            seen_blocks[block] = line_no
            blocks.append(block)
        points = {}
        while self.peek() == 'POINT':
            x, = self.header('POINT', 1)
            require(0 <= x < v, 'parse', 'range.point', 'POINT label outside 0..73', point=x)
            require(x not in points, 'parse', 'format.duplicate_section', 'Duplicate POINT section', point=x)
            used, classes = {}, []
            for j in range(r):
                actual, = self.header('CLASS', 1)
                require(actual == j, 'parse', 'format.class_order',
                        'CLASS indices are not consecutive in order', point=x, expected=j, actual=actual)
                classes.append(self.triples(used, 'POINT %d CLASS %d' % (x, j)))
            points[x] = classes
        stems = {}
        while self.peek() == 'STEMPOINT':
            x, = self.header('STEMPOINT', 1)
            require(0 <= x < v, 'parse', 'range.point', 'STEMPOINT label outside 0..73', point=x)
            require(x not in stems, 'parse', 'format.duplicate_section', 'Duplicate STEMPOINT section', point=x)
            used, classes = {}, []
            while self.peek() == 'FRAME':
                k, = self.header('FRAME', 1)
                require(0 <= k < n, 'parse', 'range.frame_group', 'FRAME group outside 0..3', point=x, group=k)
                classes.append((k, self.triples(used, 'STEMPOINT %d FRAME %d' % (x, k))))
            stems[x] = classes
        require(self.pos == len(self.rows), 'parse', 'format.unknown_line',
                'Unconsumed or out-of-order noncomment record',
                next_line=self.rows[self.pos] if self.pos < len(self.rows) else None)
        return {'v': v, 'n': n, 'g': g, 's': s, 'r': r, 't': t,
                'groups': list(map(set, groups)), 'stem': set(stem),
                'blocks': blocks, 'points': points, 'stems': stems,
                'parsed_nonblank_noncomment_lines': len(self.rows)}


def check(cert, conditions):
    v, n, g, s, r, t = (cert[k] for k in ('v', 'n', 'g', 's', 'r', 't'))
    X = set(range(v))
    groups, stem, blocks = cert['groups'], cert['stem'], cert['blocks']
    members = [x for group in groups for x in group] + list(stem)
    require(len(stem) == 2 and len(groups) == 4 and all(len(G) == 18 for G in groups)
            and len(members) == 74 and set(members) == X and len(set(members)) == len(members),
            'a', 'a.group_partition', 'GROUPS and STEM do not partition all 74 points',
            duplicate_labels=sorted(x for x, k in Counter(members).items() if k > 1),
            missing_labels=sorted(X - set(members)))
    require(set(cert['points']) == X - stem and set(cert['stems']) == stem,
            'a', 'a.point_sections', 'POINT/STEMPOINT sections are not exactly the declared point sets',
            missing_points=sorted((X-stem)-set(cert['points'])),
            extra_points=sorted(set(cert['points'])-(X-stem)),
            missing_stems=sorted(stem-set(cert['stems'])), extra_stems=sorted(set(cert['stems'])-stem))
    require(all(len(B) == 4 and len(set(B)) == 4 and set(B) <= X for B in blocks),
            'a', 'a.block_subset', 'A block is not a 4-subset of X')
    # Source (1.1) with derived order 73, hole size 19.
    derived_order, hole_size = v - 1, g + s - 1
    computed_r = (derived_order + 1) // 2
    computed_t = computed_r - (derived_order - hole_size) // 2
    require(v == n*g+s and derived_order % 6 == 1 and derived_order not in (7, 13)
            and r == computed_r and t == computed_t,
            'a', 'a.formula', 'Header does not agree with source chi-prime/good-colouring formula')
    group_of = {x: k for k, G in enumerate(groups) for x in G}
    conditions['a'] = {'status': 'PASS', 'points': v, 'group_sizes': [len(G) for G in groups],
                       'groups': [sorted(G) for G in groups], 'stem': sorted(stem),
                       'blocks_are_4_subsets': len(blocks), 'computed_colours': computed_r,
                       'computed_hole_avoiding_classes': computed_t}

    forbidden_regions = [G | stem for G in groups]
    # Build the complete intended universe, not merely its expected cardinality.
    universe = {T for T in combinations(range(v), 3)
                if not any(set(T) <= region for region in forbidden_regions)}
    counts = Counter(T for B in blocks for T in combinations(B, 3))
    actual = set(counts)
    info = {'blocks': len(blocks), 'full_triple_universe': v*(v-1)*(v-2)//6,
            'allowed_triple_universe': len(universe), 'covered_distinct_triples': len(actual),
            'triple_occurrences': sum(counts.values()),
            'missing_count': len(universe-actual), 'forbidden_count': len(actual-universe),
            'multiply_covered_count': sum(k != 1 for k in counts.values()),
            'blocks_inside_forbidden_region': sum(any(set(B) <= F for F in forbidden_regions) for B in blocks),
            'exact_set_equality': actual == universe}
    require(actual == universe and all(k == 1 for k in counts.values()),
            'b', 'b.coverage', 'CQS allowed-triple universe is not covered exactly once',
            counts=info, missing_examples=sorted(universe-actual)[:4],
            forbidden_examples=sorted(actual-universe)[:4],
            repeated_examples=[(T, k) for T, k in counts.items() if k != 1][:4])
    require(len(universe) == 60264 and len(blocks) == 15066, 'b', 'b.counts',
            'CQS exact counts disagree with gcDCQS(18^4:2)', counts=info)
    conditions['b'] = dict(status='PASS', **info)

    derived = {x: [] for x in X}
    for B in blocks:
        for x in B:
            derived[x].append(tuple(y for y in B if y != x))
    group_designs = []
    for x in sorted(X - stem):
        hole = (groups[group_of[x]] | stem) - {x}
        Y = X - {x}
        Dx = derived[x]
        expected_pairs = set(combinations(sorted(Y), 2)) - set(combinations(sorted(hole), 2))
        pair_counts = Counter(P for T in Dx for P in combinations(T, 2))
        require(all(set(T) <= Y and len(set(T) & hole) <= 1 for T in Dx)
                and set(pair_counts) == expected_pairs and all(k == 1 for k in pair_counts.values())
                and len(Dx) == 819 and len(Y) == 73 and len(hole) == 19,
                'c_design', 'c.incomplete_sts', 'Derived triples do not form STS(73,19)',
                point=x, derived_triples=len(Dx), pair_universe=len(expected_pairs),
                missing_pairs=len(expected_pairs-set(pair_counts)),
                forbidden_pairs=len(set(pair_counts)-expected_pairs),
                multiply_covered_pairs=sum(k != 1 for k in pair_counts.values()))
        free = sum(not (set(T) & hole) for T in Dx)
        group_designs.append({'point': x, 'group': group_of[x], 'derived_triples': len(Dx),
                              'pair_universe': len(expected_pairs), 'pairs_exactly_once': True,
                              'hole_points': len(hole), 'hole_avoiding_triples': free,
                              'hole_meeting_triples': len(Dx)-free})
    conditions['c_design'] = {'status': 'PASS', 'points_checked': len(group_designs),
                               'derived_triples_values': sorted({d['derived_triples'] for d in group_designs}),
                               'pair_universe_values': sorted({d['pair_universe'] for d in group_designs}),
                               'hole_avoiding_triple_values': sorted({d['hole_avoiding_triples'] for d in group_designs}),
                               'hole_meeting_triple_values': sorted({d['hole_meeting_triples'] for d in group_designs}),
                               'per_point': group_designs}

    colour_details, profiles = [], Counter()
    for x in sorted(X-stem):
        hole = (groups[group_of[x]] | stem) - {x}
        Dx = set(derived[x])
        classes = cert['points'][x]
        require(len(classes) == r, 'c_colour', 'c.class_count', 'Wrong number of colour classes', point=x)
        used, sizes, holefree = [], [], 0
        for j, C in enumerate(classes):
            require(bool(C), 'c_colour', 'c.empty_class', 'Empty colour class', point=x, colour=j)
            covered = set()
            for T in C:
                require(T in Dx, 'c_colour', 'c.colour_derived_membership',
                        'Colour-class triple is not in the derived design', point=x, colour=j, triple=T)
                overlap = covered & set(T)
                require(not overlap, 'c_colour', 'c.partial_parallel',
                        'Colour class is not partial-parallel', point=x, colour=j,
                        triple=T, overlapping_points=sorted(overlap))
                covered.update(T)
                used.append(T)
            sizes.append(len(C))
            holefree += not bool(covered & hole)
        require(len(used) == len(Dx) and len(set(used)) == len(used) and set(used) == Dx,
                'c_colour', 'c.colour_partition', 'Colour classes do not partition derived triples', point=x)
        require(holefree == t, 'c_colour', 'c.holefree_count',
                'Wrong number of hole-avoiding classes', point=x, expected=t, actual=holefree)
        profile = powers(sizes)
        profiles[profile] += 1
        colour_details.append({'point': x, 'colours': len(classes), 'hole_avoiding_classes': holefree,
                               'triples_partitioned': len(used), 'class_size_profile': profile})
    conditions['c_colour'] = {'status': 'PASS', 'points_checked': len(colour_details),
                               'colours': r, 'hole_avoiding_classes': t,
                               'class_size_profiles': dict(profiles), 'per_point': colour_details}

    stem_designs = []
    base = X - stem
    pair_universe = {P for P in combinations(sorted(base), 2) if group_of[P[0]] != group_of[P[1]]}
    for alpha in sorted(stem):
        Da = derived[alpha]
        transversal = all(set(T) <= base and len({group_of[x] for x in T}) == 3 for T in Da)
        pc = Counter(P for T in Da for P in combinations(T, 2))
        require(transversal and set(pc) == pair_universe and all(k == 1 for k in pc.values())
                and len(Da) == 648, 'd_design', 'd.gdd',
                'Stem derived design is not a GDD(2,3,72) of type 18^4',
                point=alpha, derived_triples=len(Da), pair_universe=len(pair_universe),
                missing_pairs=len(pair_universe-set(pc)), forbidden_pairs=len(set(pc)-pair_universe),
                multiply_covered_pairs=sum(k != 1 for k in pc.values()))
        stem_designs.append({'point': alpha, 'derived_triples': len(Da), 'pair_universe': len(pair_universe),
                             'pairs_exactly_once': True, 'transversal_triples': transversal})
    conditions['d_design'] = {'status': 'PASS', 'points_checked': len(stem_designs), 'per_point': stem_designs}

    frame_details = []
    for alpha in sorted(stem):
        Da, used, omitted = set(derived[alpha]), [], Counter()
        classes = cert['stems'][alpha]
        for j, (k, C) in enumerate(classes):
            target = base - groups[k]
            covered = set()
            for T in C:
                require(T in Da, 'd_frame', 'd.frame_derived_membership',
                        'Frame triple is not in the stem derived design', point=alpha, frame=j, triple=T)
                require(not (covered & set(T)), 'd_frame', 'd.frame_parallel',
                        'Frame class has intersecting triples', point=alpha, frame=j, omitted_group=k,
                        triple=T, overlapping_points=sorted(covered & set(T)))
                covered.update(T)
                used.append(T)
            require(covered == target and len(C) == 18, 'd_frame', 'd.frame_parallel',
                    'Frame class does not partition exactly the complement of its omitted group',
                    point=alpha, frame=j, omitted_group=k, class_size=len(C),
                    missing_points=sorted(target-covered), extra_points=sorted(covered-target))
            omitted[k] += 1
        require(len(used) == len(Da) and len(set(used)) == len(used) and set(used) == Da,
                'd_frame', 'd.frame_partition', 'Frames do not partition the stem derived design', point=alpha)
        # From the definition, every point outside group i has degree 27;
        # 648 triples / 18 per class = 36 classes, hence 36-27=9 omit i.
        require(len(classes) == 36 and all(omitted[k] == 9 for k in range(4)),
                'd_frame', 'd.frame_group_counts', 'KF(18^4) does not have nine classes omitting each group',
                point=alpha, frames=len(classes), counts=dict(omitted))
        frame_details.append({'point': alpha, 'classes': len(classes),
                              'class_size': 18, 'classes_per_omitted_group': [omitted[k] for k in range(4)],
                              'derived_triples_partitioned': len(used)})
    conditions['d_frame'] = {'status': 'PASS', 'points_checked': len(frame_details), 'per_point': frame_details}
    return {'v': v, 'blocks': len(blocks), 'allowed_triples': len(universe),
            'group_point_derived_triples': [819], 'colours_per_group_point': r,
            'hole_avoiding_classes_per_group_point': t,
            'class_size_profiles': dict(profiles), 'stem_frames': frame_details,
            'worker_consistency': {'reported_derived_triples': 819,
                                   'reported_class_size_profile': '24^24 23^3 18^5 17^4 16^1',
                                   'reported_stem_frame_classes': 36,
                                   'all_match': set(profiles) == {'24^24 23^3 18^5 17^4 16^1'}}}


def main():
    if len(sys.argv) != 4:
        raise SystemExit('Usage: FILE EXPECTED_SHA256 NEW_RECEIPT.json')
    path, expected_sha, receipt = sys.argv[1:]
    require(not Path(receipt).exists(), 'pin', 'output.exists', 'Refusing to overwrite receipt')
    started, started_wall = time.perf_counter(), datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
    conditions = {k: {'status': 'NOT_RUN'} for k in ('pin', 'parse', 'a', 'b', 'c_design', 'c_colour', 'd_design', 'd_frame')}
    result = {'checker': 'Independent stdlib definition-first gcDCQS18 checker; no symmetry assumed',
              'input': str(Path(path).resolve()), 'expected_input_sha256': expected_sha,
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'started_at_pt': started_wall, 'conditions': conditions}
    try:
        raw = Path(path).read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        result.update(input_sha256=digest, input_bytes=len(raw))
        require(digest == expected_sha, 'pin', 'pin.sha256', 'Input SHA256 mismatch', actual=digest, expected=expected_sha)
        conditions['pin'] = {'status': 'PASS', 'sha256': digest}
        try:
            text = raw.decode('ascii')
        except UnicodeDecodeError as exc:
            raise CertificateError('parse', 'format.encoding', 'Non-ASCII Format S input') from exc
        cert = Parser(text).parse()
        conditions['parse'] = {'status': 'PASS', 'nonblank_noncomment_lines': cert['parsed_nonblank_noncomment_lines'],
                               'unknown_or_unconsumed_lines': 0}
        result['summary'] = check(cert, conditions)
        result['status'], rc = 'PASS', 0
    except CertificateError as exc:
        conditions[exc.condition] = {'status': 'FAIL', 'category': exc.category,
                                     'reason': str(exc), 'details': exc.details}
        result.update(status='FAIL', error_type=type(exc).__name__, category=exc.category,
                      condition=exc.condition, reason=str(exc), details=exc.details)
        rc = 1
    result['finished_at_pt'] = datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
    result['runtime_seconds'] = time.perf_counter()-started
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result['peak_rss_bytes'] = int(rss if sys.platform == 'darwin' else rss*1024)
    result['python_optimization'] = sys.flags.optimize
    with Path(receipt).open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps({'status': result['status'], 'category': result.get('category'),
                      'summary': result.get('summary'), 'runtime_seconds': result['runtime_seconds'],
                      'peak_rss_bytes': result['peak_rss_bytes']}))
    return rc


if __name__ == '__main__':
    raise SystemExit(main())
