"""Multi-block copy-lemma LPs (each block an independent copy construction over the shared base), with
Aut(R^-) symmetry.  Exploratory float LPs."""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graphs import R_MINUS_EDGES, nbmasks
from copy_lp import Model
from copy_explore import SIG, TAU

def run_blocks(blocks, sym=True):
    m = Model(nbmasks(R_MINUS_EDGES))
    for cp in blocks:
        m.add_block(cp)
    t0 = time.time()
    st, val, nc, nr = m.solve(sym_perms=[SIG, TAU] if sym else [])
    return dict(blocks=blocks, status=st, value=val, cols=nc, rows=nr, wall=round(time.time() - t0, 1))

if __name__ == "__main__":
    A = [([9], [0, 1, 2, 4, 5, 6, 7, 8])]
    B = [([2], [0, 1, 4, 5, 6, 7, 8, 9])]
    C = [([3], [0, 1, 4, 5, 6, 7, 8, 9])]
    D = [([7], [0, 1, 3, 4, 5, 6, 8, 9])]
    E = [([7], [0, 1, 2, 4, 5, 6, 8, 9])]
    for blocks in ([A, B], [A, C], [A, B, C], [A, B, C, D, E]):
        print(json.dumps(run_blocks(blocks))); sys.stdout.flush()
