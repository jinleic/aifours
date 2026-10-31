"""Independent exact control for Lemma C and the two gamma boundary forms."""
import hashlib
import itertools
import json
import pathlib
import subprocess
import time

D = pathlib.Path('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f154-olson-p2-projection-two-rotation-selector')
OUT = D / 'reviewer-piece-control-results-v1.json'

def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()

def need(b, reason):
    if not b:
        raise RuntimeError(reason)

def product(word, p):
    x, parity = 0, 0
    for y, b in word:
        x = (x + (-1 if parity else 1) * y) % p
        parity ^= b
    return [x, parity]

def pieces(a, g1, g2):
    F = len(a)
    order = [(g1 + 1 + k) % F for k in range(F)]
    cut = order.index(g2) + 1
    blocks, nx = [], 0
    for partnum, part in enumerate((order[:cut], order[cut:])):
        for j in part:
            if not blocks or (partnum == 1 and j == part[0]) or a[blocks[-1][-1]] != a[j]:
                blocks.append([])
            blocks[-1].append(j)
        if partnum == 0:
            nx = len(blocks)
    return blocks, nx

started = clock()
t0 = time.monotonic()
need(not OUT.exists(), 'exclusive output')
results = []
cap_negative = None
sign_negative = None
for p in (3, 5, 7):
    # Generic words, not sampled from author evidence; Lemma C does not assume o_pi=p+2.
    if p == 3:
        a = [0, 1, 1, 0, 2, 1, 2]
    elif p == 5:
        a = [0, 1, 1, 0, 2, 2, 0, 1, 2, 3, 4, 4, 4]
    else:
        a = [0] + [1] * 6 + [0, 2, 2, 0, 1, 2, 3, 4, 5, 6, 6, 6]
    F, K = 3 * p - 2, 2 * p - 2
    need(len(a) == F, 'F')
    pairs = list(itertools.combinations(range(F), 2)) if p == 3 else [(0, 1), (1, 2), (0, 3), (2, 4), (1, F - 1), (F - 3, F - 1)]
    subset_counts, pattern_counts, equations = 0, 0, 0
    for g1, g2 in pairs:
        blocks, nx = pieces(a, g1, g2)
        owner = {j: h for h, block in enumerate(blocks) for j in block}
        actual, witnesses = set(), {}
        for chosen in itertools.combinations(range(F), K):
            parity = [0] * len(blocks)
            for j in chosen:
                parity[owner[j]] ^= 1
            T = sum(v << h for h, v in enumerate(parity))
            actual.add(T)
            witnesses.setdefault(T, chosen)
            subset_counts += 1
        criterion = set()
        opc = sum(len(b) % 2 for b in blocks)
        for T in range(1 << len(blocks)):
            size = T.bit_count()
            ot = sum(len(b) % 2 for h, b in enumerate(blocks) if T >> h & 1)
            et = size - ot
            feasible = size % 2 == 0 and size <= K and ot - et >= opc - p
            if feasible:
                criterion.add(T)
            if cap_negative is None and size % 2 == 0 and size <= K and ot - et < opc - p:
                # Removing cap falsely admits this parity pattern, regardless of equation.
                need(T not in actual, 'capacity negative intended reason')
                cap_negative = {'p': p, 'projection': a, 'gaps': [g1, g2], 'T': T, 'o_pc': opc, 'o_T_minus_e_T': ot - et, 'required': opc - p, 'actual_budget_attainable': False}
        need(actual == criterion, 'Lemma C capacity sufficiency AND necessity')
        for T in criterion:
            pattern_counts += 1
            tx = [a[b[0]] for h, b in enumerate(blocks[:nx]) if T >> h & 1]
            ty = [a[b[0]] for h, b in enumerate(blocks[nx:], nx) if T >> h & 1]
            ax = sum((-1)**j * v for j, v in enumerate(tx))
            ay = sum((-1)**j * v for j, v in enumerate(ty))
            chosen = set(witnesses[T])
            for u, v in itertools.product(range(p), repeat=2):
                # Literal group product in the original linear order, not the cyclic cut.
                word = []
                for j in range(F):
                    if j in chosen:
                        word.append((a[j], 1))
                    if j == g1:
                        word.append((u, 0))
                    if j == g2:
                        word.append((v, 0))
                eq = (u + v + ax + ay) % p == 0 if len(tx) % 2 == 0 else (u - v + ax - ay) % p == 0
                real = product(word, p)
                need(eq == (real == [0, 0]), 'Lemma C signed equation versus literal original order')
                equations += 1
                if sign_negative is None and len(tx) % 2 and v != 0 and (u + v + ax - ay) % p == 0:
                    need(real != [0, 0], 'wrong +v negative intended reason')
                    sign_negative = {'p': p, 'projection': a, 'gaps': [g1, g2], 'u': u, 'v': v, 'T': T, 'wrong_plus_v_eq': True, 'correct_eq': False, 'literal_product': real}
        need(time.monotonic() - t0 < 240, 'cooperative 240s deadline')
    results.append({'p': p, 'gap_pairs': len(pairs), 'reflection_subsets_enumerated': subset_counts, 'feasible_parity_patterns': pattern_counts, 'original_order_equation_products': equations})
need(cap_negative is not None and sign_negative is not None, 'negative witnesses present')

gamma = []
for bzero in (False, True):
    p = 7
    # Each fixture has odd-run labels 0,0,0,1,2,3,4,5,6, F=19.
    a = [0] + [2] * (4 if bzero else 2) + [0, 3, 3, 0] + [1] * (5 if bzero else 7) + [2, 3, 4, 5, 6]
    need(len(a) == 19, 'gamma F')
    G = [j for j in range(len(a)) if a[j] == 1]
    aa, xx = (4, 1) if bzero else (2, 1)
    g1, g2 = G[aa - 1], G[aa + xx - 1]
    blocks, nx = pieces(a, g1, g2)
    need(nx == 1 and len(blocks[0]) == 1, 'gamma X')
    even_piece = len(blocks) - 1 if bzero else 1
    zero_pieces = [h for h, block in enumerate(blocks) if a[block[0]] == 0 and len(block) % 2]
    need(len(zero_pieces) == 3, 'gamma c tripled')
    T = {0, even_piece, *zero_pieces[:2]}
    need(len(blocks[even_piece]) % 2 == 0 and len(blocks[even_piece]) >= 2, 'gamma even piece')
    k = [int(h in T) for h in range(len(blocks))]
    remaining = 12 - sum(k)
    for h, block in enumerate(blocks):
        add = min(remaining, 2 * ((len(block) - k[h]) // 2))
        k[h] += add
        remaining -= add
    need(remaining == 0, 'gamma exact capacity')
    selected_refs = set(j for h, block in enumerate(blocks) for j in block[:k[h]])
    # Add 6 other rotations in gaps outside G, so this is a full admissible R=8 word.
    extra = [j for j in range(len(a)) if j not in G][:6]
    gaps = {g1: 0, g2: 0, **{j: (j * 3 + 1) % p for j in extra}}
    need(len(gaps) == p + 1, 'full word R')
    fullword, indices = [], []
    for j, label in enumerate(a):
        if j in selected_refs:
            indices.append(len(fullword))
        fullword.append((label, 1))
        if j in gaps:
            if j in (g1, g2):
                indices.append(len(fullword))
            fullword.append((gaps[j], 0))
    selected = [fullword[j] for j in indices]
    need(indices == sorted(set(indices)) and len(indices) == 14, 'full original order count')
    need(sum(b == 0 for _, b in selected) == 2 and product(selected, p) == [0, 0], 'full gamma identity')
    changed = list(selected)
    firstrotation = next(i for i, (_, b) in enumerate(changed) if b == 0)
    changed[firstrotation] = ((changed[firstrotation][0] + 1) % p, 0)
    need(product(changed, p) != [0, 0], 'gamma changed selected rotation negative')
    gamma.append({'p': p, 'b_zero': bzero, 'projection': a, 'occupied_gaps': gaps, 'piece_lengths': list(map(len, blocks)), 'T': sorted(T), 'selected_counts': k, 'fullword': fullword, 'original_indices': indices, 'product': product(selected, p), 'mutated_product': product(changed, p)})

r = {'kind': 'REVIEWER_PIECE_AND_GAMMA_EXACT_CONTROLS', 'status': 'COMPLETE', 'started': started, 'finished': clock(), 'elapsed_seconds': time.monotonic() - t0, 'lemma_C': results, 'intended_reason_negatives': {'omitted_cap': cap_negative, 'wrong_plus_v': sign_negative, 'selected_rotation_increment': 'nonidentity for both full gamma words'}, 'gamma_full_words': gamma, 'source_sha256': hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(), 'observed_clock_immediately_before_write': clock()}
with OUT.open('x') as f:
    json.dump(r, f, indent=2)
    f.write('\n')
print(json.dumps({'path': str(OUT), 'elapsed_seconds': r['elapsed_seconds'], 'status': r['status']}))
