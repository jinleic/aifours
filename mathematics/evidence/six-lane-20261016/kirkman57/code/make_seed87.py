"""Write the compact construction seed for the G903 LKTS(87) from a pipeline run dir."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from g87_groups import *
run = sys.argv[1]; out = sys.argv[2]
res = json.load(open(os.path.join(run, "base_resolutions.json")))
seed = {
    "description": "LKTS(87) seed: points {inf} ∪ Z43 x {0,1}, (x,j) -> 43*j+x, inf -> 86; group G903 = <tau, m> "
                   "(tau:(x,j)->(x+1,j), m:(x,j)->(9x,j)); each base is a resolved KTS(87) given by its 43 classes; "
                   "constituents are g(base) for g the least element of each coset of H (stabilizer generators).",
    "v": 87,
    "point_encoding": "43*j+x; inf=86",
    "certificate_header": "# LKTS(87) candidate from G903 pipeline (unverified until checked)",
    "G_generators": {"tau": list(tau), "m": list(m21)},
    "bases": [{"name": "S0", "stabilizer_generators": [list(m21)], "classes": res[0]},
              {"name": "B1", "stabilizer_generators": [list(tau)], "classes": res[1]},
              {"name": "B2", "stabilizer_generators": [list(tau)], "classes": res[2]}],
}
json.dump(seed, open(out, "w"))
print("wrote", out)
