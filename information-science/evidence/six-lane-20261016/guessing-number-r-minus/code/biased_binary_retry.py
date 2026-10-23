"""Longer CP-SAT retry of the windows left UNKNOWN by biased_binary_search.py at 120 s.
Same model (imported); appends to evidence/biased-binary-search.jsonl with tag retry600."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from biased_binary_search import run
UNKNOWN = [(98,43),(99,44),(99,45),(100,46),(101,47),(101,48),(102,48),(102,49),(102,50),(102,51),(103,50),(103,51)]
tlim = float(sys.argv[1]) if len(sys.argv) > 1 else 600
out = os.path.join(os.path.dirname(__file__), "..", "evidence", "biased-binary-search.jsonl")
with open(out, "a") as fh:
    for N, m in UNKNOWN:
        r = run(N, m, tlim, seed=1); r["tag"] = f"retry{int(tlim)}"
        fh.write(json.dumps(r) + "\n"); fh.flush()
        print(json.dumps({k: v for k, v in r.items() if k != "code"}), flush=True)
