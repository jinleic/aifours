"""Exact avoider search on the extreme KB_HIGH* family p = 11, k = 19, B = 8, R = 19 (all runs single
letters: 11 rho_1, 8 rho_-1), F = 23 (two reflection runs of length 3).  For these data no window is
full (R = 2p-3) and every single-run Lemma BC chain fails at step 2 (2D + 4 = 10 < p + 1).
Uses ../hwsingle (all patterns, exhaustive DFS).  Aid; any avoider must be confirmed by ../hw.py dp_has."""
import random, subprocess, sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__)); PAR = os.path.dirname(HERE)
p, k = 11, 19
seed = int(sys.argv[1]); T = int(sys.argv[2]); tmo = int(sys.argv[3])
rng = random.Random(seed)
for trial in range(T):
    anti = set(rng.sample(range(k), 8))
    a = [0 if t in anti else 1 for t in range(k)]; b = [1 - x for x in a]
    l = [1] * k
    for _ in range(2): l[rng.randrange(k)] += 2
    args = [os.path.join(PAR, 'hwsingle'), str(p), '99', str(k)] + [str(x) for x in a + b + l] + ['3', '3']
    t0 = time.time()
    try:
        out = subprocess.run(args, capture_output=True, text=True, timeout=tmo).stdout
    except subprocess.TimeoutExpired:
        out = 'TIMEOUT'
    print(trial, 'a=', a, 'l=', l, '->', out.strip().replace('\n', ' | '), '(%.1fs)' % (time.time() - t0), flush=True)
