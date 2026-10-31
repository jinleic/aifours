"""Supplement: A/lambda2 recipe, literal full-word embedding, p=3 boundary."""
import hashlib
import itertools
import json
import pathlib
import subprocess
import time
D = pathlib.Path('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f154-olson-p2-projection-two-rotation-selector')
OUT = D / 'reviewer-sector-control-results-v1.json'

def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()

def need(b, s):
    if not b:
        raise RuntimeError(s)

def prod(w, p):
    x, e = 0, 0
    for y, b in w:
        x = (x + (-1 if e else 1) * y) % p
        e ^= b
    return [x, e]

def cyclic_runs(a):
    if len(set(a)) == 1:
        return [list(range(len(a)))]
    st = next(i for i in range(len(a)) if a[i] != a[i-1])
    out = []
    for k in range(len(a)):
        j = (st+k) % len(a)
        if k == 0 or a[j] != a[(j-1) % len(a)]:
            out.append([])
        out[-1].append(j)
    return out

def pieces(a, g1, g2):
    order = [(g1+1+k) % len(a) for k in range(len(a))]
    cut = order.index(g2)+1
    out = []
    nx = 0
    for h, part in enumerate((order[:cut], order[cut:])):
        for k, j in enumerate(part):
            if k == 0 or a[j] != a[part[k-1]]:
                out.append([])
            out[-1].append(j)
        if h == 0:
            nx = len(out)
    return out, nx

def full_selection(a, gaps, refs, g1, g2, p):
    word, indices = [], []
    for j, x in enumerate(a):
        if j in refs:
            indices.append(len(word))
        word.append([x, 1])
        if j in gaps:
            if j in (g1, g2):
                indices.append(len(word))
            word.append([gaps[j], 0])
    selected = [word[j] for j in indices]
    need(len(a) == 3*p-2 and len(gaps) >= p+1, 'full word hypotheses F/R')
    need(sum(len(r) % 2 for r in cyclic_runs(a)) == p+2, 'full word projected odd runs')
    need(indices == sorted(set(indices)) and len(indices) == 2*p, 'strict full original order/length')
    need(sum(b == 0 for _, b in selected) == 2 and prod(selected, p) == [0, 0], 'literal full word identity with exactly two rotations')
    mutated = list(selected)
    ix = next(i for i, (_, b) in enumerate(mutated) if b == 0)
    mutated[ix] = [(mutated[ix][0]+1) % p, 0]
    need(prod(mutated, p) != [0, 0], 'changed rotation negative control')
    return {'fullword': word, 'original_indices': indices, 'product': prod(selected, p), 'mutated_product': prod(mutated, p)}

started = clock()
t0 = time.monotonic()
need(not OUT.exists(), 'exclusive output')
p3_valid = p3_failed = 0
for aa in itertools.product(range(3), repeat=7):
    if sum(len(r) % 2 for r in cyclic_runs(aa)) != 5:
        continue
    p3_valid += 1
    if not any(prod([(aa[j], 1) for j in s], 3) == [0, 0] for s in itertools.combinations(range(7), 6)):
        p3_failed += 1
need(p3_failed == 0 and p3_valid > 0, 'p3 exhaustive REF check')

al2 = []
for p in (5, 7):
    # Three even runs, first two adjacent: A/lambda2 even though REF also succeeds.
    a = [0, 1, 1, 2, 2, 0, 3, 3, 0] + list(range(1, p-1)) + [p-1]*(2*p-9)
    need(len(a) == 3*p-2, 'A2 F')
    g1, g2 = 1, 3
    spares = [r[-1] for r in cyclic_runs(a) if len(r) % 2]
    order = [(g2+1+k) % len(a) for k in range(len(a))]
    ys = [j for j in order if j in spares]
    need(len(ys) == p+2 and {a[j] for j in ys} == set(range(p)), 'A2 spare distribution')
    pc, nx = pieces(a, g1, g2)
    owner = {j: h for h, b in enumerate(pc) for j in b}
    products = 0
    first = None
    for u, v in itertools.product(range(p), repeat=2):
        pair = next((i, j) for h, i in enumerate(ys) for j in ys[h+1:] if (a[i]-a[j]-u-v) % p == 0)
        TX = {owner[2], owner[3]}
        TY = {owner[4], owner[pair[0]], owner[pair[1]], owner[1]}
        need(len(TX) == 2 and len(TY) == 4 and not TX & TY, 'A2 six distinct pieces')
        T = TX | TY
        need(all(len(pc[h]) % 2 for h in T), 'A2 selected pieces odd')
        need(sum(len(b)%2 for b in pc)-p == 6, 'A2 cap exact')
        ax = sum((-1)**k*a[pc[h][0]] for k, h in enumerate(sorted(TX)))
        ay = sum((-1)**k*a[pc[h][0]] for k, h in enumerate(sorted(TY)))
        need((u+v+ax+ay) % p == 0, 'A2 stated equation')
        counts = [int(h in T) for h in range(len(pc))]
        remain = 2*p-2-sum(counts)
        for h, b in enumerate(pc):
            add = min(remain, 2*((len(b)-counts[h])//2))
            counts[h] += add
            remain -= add
        need(remain == 0, 'A2 budget')
        refs = {j for h, b in enumerate(pc) for j in b[:counts[h]]}
        # Exactly p+1 rotations and at most one gap occupied in each run.
        extra = [6, 8, *range(9, len(a))][:p-1]
        gaps = {g1:u, g2:v, **{j:(2*j+1) % p for j in extra}}
        need(len(gaps) == p+1, 'A2 R')
        for run in cyclic_runs(a):
            need(sum(j in gaps for j in run) <= 1, 'A2 at most one rotation per run')
        need([j for j in range(0, 5) if j in gaps] == [1, 3], 'A2 first two in one sector')
        literal = full_selection(a, gaps, refs, g1, g2, p)
        if first is None:
            first = {'u':u, 'v':v, 'projection':a, 'T_X':sorted(TX), 'T_Y':sorted(TY), **literal}
        products += 1
    al2.append({'p':p, 'rotation_value_pairs':products, 'all_original_order_products_identity':True, 'first_full_word_witness':first})

embedded = []
input_hashes = []
for p, stem in ((5, 'q5'), (7, 'p7')):
    path = D / f'reviewer-stdout-{stem}-v1.json'
    content = path.read_bytes()
    input_hashes.append({'path':str(path), 'sha256':hashlib.sha256(content).hexdigest()})
    data = json.loads(content)[f'p{p}']
    for branch, sample in data['samples'].items():
        a = sample['projection']
        g1, g2 = sample['gaps']
        u, v = sample['values']
        old = set(sample['indices_in_two_rotation_subword'])
        refs, index = set(), 0
        for j in range(len(a)):
            if index in old:
                refs.add(j)
            index += 1
            if j in (g1, g2):
                index += 1
        extra = [j for j in range(len(a)) if j not in (g1,g2)][:p-1]
        gaps = {g1:u, g2:v, **{j:(3*j+1) % p for j in extra}}
        embedded.append({'p':p, 'branch_label_from_pair_control':branch, **full_selection(a, gaps, refs, g1, g2, p)})

r = {'status':'COMPLETE', 'kind':'REVIEWER_A_LAMBDA2_FULL_EMBEDDING_AND_P3', 'started':started, 'finished':clock(), 'elapsed_seconds':time.monotonic()-t0, 'p3':{'all_reflection_vectors':3**7, 'o_pi_5_vectors':p3_valid, 'REF_failures':p3_failed}, 'A_lambda2':al2, 'fullword_embeddings':embedded, 'reviewer_output_inputs':input_hashes, 'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(), 'observed_clock_immediately_before_write':clock()}
with OUT.open('x') as f:
    json.dump(r, f, indent=2)
    f.write('\n')
print(json.dumps({'path':str(OUT), 'status':r['status'], 'elapsed_seconds':r['elapsed_seconds'], 'fullword_embeddings':len(embedded)}))
