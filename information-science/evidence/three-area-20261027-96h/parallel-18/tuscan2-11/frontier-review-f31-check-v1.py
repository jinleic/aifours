#!/usr/bin/env python3
"""Independent direct-popcount census for f31; no author checker is invoked.

Reconstructs seed Walsh spectra from truth tables; exhausts all one-/two-flip
positions, all bad-peak triples and their four-cliques, and the complete span
of independently reconstructed four-flips. Finally compares the independently
derived triple/quad sets with the pinned author's data. All arithmetic exact.
"""
import hashlib
import itertools
import json
import math
import sys
import time
from collections import Counter
from pathlib import Path

N = 512


def character_masks():
    result = []
    for a in range(N):
        mask = 0
        for x in range(N):
            if (a & x).bit_count() & 1:
                mask |= 1 << x
        result.append(mask)
    return result


def spectrum(table, chars):
    return [N - 2 * (table ^ char).bit_count() for char in chars]


def parse_seeds(path):
    raw = path.read_bytes()
    lines = [line for line in raw.decode().splitlines() if line and not line.startswith('#')]
    if len(lines) != 3 or any(len(line) != 128 for line in lines):
        raise ValueError('expected exactly three 128-hex-digit seeds')
    seeds = []
    for line in lines:
        value = int(line, 16)
        seeds.append(sum(((value >> (511 - x)) & 1) << x for x in range(N)))
    return raw, seeds


def affine_rank(points):
    if not points:
        return 0
    origin = points[0]
    pivots = {}
    for p in points:
        v = p ^ origin
        while v:
            k = v.bit_length() - 1
            if k in pivots:
                v ^= pivots[k]
            else:
                pivots[k] = v
                break
    return len(pivots)


def main(argv):
    if len(argv) != 4:
        raise ValueError('usage: SCRIPT SEEDS AUTHOR_QUAD_RESULT OUTPUT')
    source, compare_path, output = map(Path, argv[1:])
    raw, seeds = parse_seeds(source)
    chars = character_masks()
    t0 = time.monotonic()
    observations = []
    independently_reconstructed = []
    examples = [(0, 1, 155), (0, 1, 54), (0, 1, 2)]
    for si, table in enumerate(seeds):
        w = spectrum(table, chars)
        histogram = Counter(abs(v) for v in w)
        if histogram != {4: 30, 12: 46, 20: 226, 28: 210}:
            raise ValueError('unexpected seed Walsh histogram')
        if sum(v * v for v in w) != N * N:
            raise ValueError('seed Parseval mismatch')
        peak_freqs = [a for a in range(N) if abs(w[a]) == 28]
        tiny_freqs = [a for a in range(N) if abs(w[a]) == 4]
        bad, zero = [], []
        for x in range(N):
            fsign = -1 if (table >> x) & 1 else 1
            b = 0
            z = 0
            for i, a in enumerate(peak_freqs):
                character = -1 if (chars[a] >> x) & 1 else 1
                if w[a] * fsign * character < 0:
                    b |= 1 << i
            for i, a in enumerate(tiny_freqs):
                character = -1 if (chars[a] >> x) & 1 else 1
                if w[a] * fsign * character > 0:
                    z |= 1 << i
            bad.append(b)
            zero.append(z)
        if any(mask == 0 for mask in bad):
            raise AssertionError('a one-flip does not increase a peak')
        minimum_bad = min(mask.bit_count() for mask in bad)
        min_pair_bad = len(peak_freqs)
        balance_pairs = 0
        incidence_count = 0
        all_pair_peak_hist = Counter()
        balance_peak_hist = Counter()
        num_pairs = 0
        for x in range(N - 1):
            for y in range(x + 1, N):
                num_pairs += 1
                common = (bad[x] & bad[y]).bit_count()
                min_pair_bad = min(min_pair_bad, common)
                z = (zero[x] & zero[y]).bit_count()
                if common:
                    # A jointly bad original peak reaches 32. Every seed
                    # coefficient is <=28, so no two-flip peak exceeds 32.
                    peak = 32
                else:
                    peak = max(abs(v) for v in spectrum(table ^ (1 << x) ^ (1 << y), chars))
                all_pair_peak_hist[peak] += 1
                if z:
                    balance_pairs += 1
                    incidence_count += z
                    balance_peak_hist[peak] += 1
        if num_pairs != math.comb(N, 2):
            raise AssertionError('pair enumeration incomplete')

        # Exhaust all unordered triples without using the author's list. A
        # triple is uncovered precisely when the three bad masks intersect
        # in no common peak. Reuse each 2-way intersection as an optimization.
        uncovered = []
        triple_count = 0
        for x in range(N - 2):
            for y in range(x + 1, N - 1):
                shared = bad[x] & bad[y]
                for z in range(y + 1, N):
                    triple_count += 1
                    if not (shared & bad[z]):
                        uncovered.append((x, y, z))
        if triple_count != math.comb(N, 3):
            raise AssertionError('triple enumeration incomplete')
        triple_set = set(uncovered)
        quads = []
        extensions = 0
        for x, y, z in uncovered:
            for v in range(z + 1, N):
                extensions += 1
                if ((x, y, v) in triple_set and (x, z, v) in triple_set
                        and (y, z, v) in triple_set):
                    quads.append((x, y, z, v))
        balanceable_quads = 0
        for quad in quads:
            qtable = table
            for x in quad:
                qtable ^= 1 << x
            qw = spectrum(qtable, chars)
            if max(map(abs, qw)) > 28:
                raise AssertionError('a returned four-clique has peak over 28')
            balanceable_quads += int(0 in qw)

        positions = sorted(set(itertools.chain.from_iterable(quads)))
        quad_xor_zero = all((a ^ b ^ c ^ d) == 0 for a, b, c, d in quads)
        span = {0}
        for quad in quads:
            generator = sum(1 << x for x in quad)
            span.update(generator ^ old for old in tuple(span))
        span_hist = Counter()
        peak28_zeroes = 0
        for flip_mask in span:
            sw = spectrum(table ^ flip_mask, chars)
            peak = max(map(abs, sw))
            span_hist[peak] += 1
            if peak == 28 and 0 in sw:
                peak28_zeroes += 1

        x, y, twist = examples[si]
        fw = spectrum(table ^ (1 << x) ^ (1 << y) ^ chars[twist], chars)
        ex = {'flips': [x, y], 'twist': twist, 'walsh_zero': fw[0],
              'weight': (N - fw[0]) // 2, 'peak': max(map(abs, fw)),
              'nonlinearity': (N - max(map(abs, fw))) // 2,
              'walsh_zero_count': sum(v == 0 for v in fw)}
        independently_reconstructed.append((uncovered, quads))
        observations.append({
            'seed': si + 1, 'weight': table.bit_count(), 'W0': w[0],
            'absolute_walsh_histogram': dict(sorted(histogram.items())),
            'min_single_bad_peaks': minimum_bad, 'min_pair_common_bad_peaks': min_pair_bad,
            'pairs': num_pairs, 'balanceable_pairs': balance_pairs,
            'pair_twist_incidences': incidence_count,
            'all_pair_peak_histogram': dict(sorted(all_pair_peak_hist.items())),
            'balanceable_pair_peak_histogram': dict(sorted(balance_peak_hist.items())),
            'triples_checked': triple_count, 'uncovered_triples': len(uncovered),
            'fourth_extensions_checked': extensions, 'peak_preserving_four_flips': len(quads),
            'balanceable_preserving_four_flips': balanceable_quads,
            'generator_positions': len(positions), 'generator_position_affine_rank': affine_rank(positions),
            'all_generator_quad_xors_zero': quad_xor_zero, 'span_size': len(span),
            'span_peak_histogram': dict(sorted(span_hist.items())),
            'span_peak28_tables_with_walsh_zero': peak28_zeroes,
            'actual_balanced_example': ex,
        })
        print(json.dumps(observations[-1], sort_keys=True), flush=True)

    # Author results are used only for explicit cross-comparison AFTER all
    # triples and quadruples have been independently generated from the seed.
    compared_raw = compare_path.read_bytes()
    reported = json.loads(compared_raw)['seeds']
    if len(reported) != len(seeds):
        raise AssertionError('author result seed count mismatch')
    for i, (uncovered, quads) in enumerate(independently_reconstructed):
        if set(uncovered) != set(map(tuple, reported[i]['uncovered_triples'])):
            raise AssertionError(f'seed {i+1}: independently reconstructed triples differ')
        if set(quads) != set(map(tuple, reported[i]['preserving_quads'])):
            raise AssertionError(f'seed {i+1}: independently reconstructed quads differ')
    result = {'method': 'own direct-popcount truth/character Walsh sums, all pairs, all triples and four-cliques, complete XOR closure',
              'seed_sha256': hashlib.sha256(raw).hexdigest(),
              'compared_author_result_sha256': hashlib.sha256(compared_raw).hexdigest(),
              'all_author_triple_and_quad_sets_match': True,
              'scope': 'Three pinned truth tables only; not a global existence/nonexistence result.',
              'elapsed_ms': round((time.monotonic() - t0) * 1000), 'observations': observations}
    with output.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({'output': str(output), 'elapsed_ms': result['elapsed_ms'],
                      'all_author_triple_and_quad_sets_match': True}, sort_keys=True))


if __name__ == '__main__':
    main(sys.argv)
