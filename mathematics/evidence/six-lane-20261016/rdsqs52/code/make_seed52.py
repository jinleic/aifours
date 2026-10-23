"""Extract the compact seed (multiplier generator + the 25 classes at point 0, in file order)
from a cyclic RDSQS certificate.  Usage: make_seed52.py CERT GEN OUT.json"""
import json, sys
cert, gen, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
header = None; v = None; classes = []; cur = None
for raw in open(cert):
    line = raw.rstrip("\n")
    if header is None and line.startswith("#"):
        header = line
    s = line.split("#")[0].strip()
    if not s: continue
    t = s.split()
    if t[0] == "RDSQS": v = int(t[1]); continue
    if t[0] == "POINT":
        if cur is not None: break
        cur = int(t[1]); assert cur == 0; continue
    if t[0] == "CLASS" and cur == 0: classes.append([]); continue
    if cur == 0: classes[-1].append([int(x) for x in t])
seed = {"v": v, "certificate_header": header, "translation": "x -> x+1 mod v",
        "multiplier_generator": gen, "classes_at_0": classes,
        "rule": "blocks = all translates of {0} ∪ t (t in classes_at_0); resolution at x = g(classes_at_0), "
                "g = least element (as tuple of images) of G = {y -> m*y+b : m in <gen>, b in Z_v} with g(0) = x"}
json.dump(seed, open(out, "w"))
print("classes", len(classes), "triples", sum(len(C) for C in classes))
