#!/usr/bin/env python3
"""Independent finite whole-host transport diagnostic; standard library only.

This program reads the manifest inputs only as bytes for provenance; it never
imports, evaluates, or executes the author's code. It writes two new artifacts
in its own directory, refuses overwrites, and checks exact finite operations.
"""
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path
import json
import platform
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "manifest-v1.json"
MANIFEST_SHA = "6580d8208d704cb242e28e58951646d5ada674919b5569340e8252f566390426"
PRODUCTS = HERE / "finite-products-v1.json"
RESULT = HERE / "finite-result-v1.json"


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def digest(data):
    return sha256(data).hexdigest()


def native_clock():
    return subprocess.check_output(
        ["/bin/date", "+%Y-%m-%dT%H:%M:%S%z %Z"], text=True
    ).strip()


def json_bytes(obj):
    return (json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n").encode()


def collision_report(projections, universe):
    count = 0
    first = None
    for i in range(len(universe)):
        for j in range(i + 1, len(universe)):
            if projections[i] == projections[j]:
                count += 1
                if first is None:
                    first = {"indices": [i, j], "source_elements": [universe[i], universe[j]]}
    return {"unordered_collision_pairs": count, "first_witness": first}


require(not PRODUCTS.exists() and not RESULT.exists(), "output already exists")
clock_start = native_clock()
start = time.monotonic()
script = Path(__file__).resolve().read_bytes()
manifest_bytes = MANIFEST.read_bytes()
require(digest(manifest_bytes) == MANIFEST_SHA, "manifest SHA mismatch")
manifest = json.loads(manifest_bytes)
inputs = []
for entry in manifest["inputs_in_read_order"]:
    content = Path(entry["path"]).read_bytes()
    observed = {"sha256": digest(content), "bytes": len(content), "LF": content.count(b"\n")}
    require(all(observed[k] == entry[k] for k in observed), "frozen input mismatch: " + entry["path"])
    inputs.append({"role": entry["role"], "path": entry["path"], **observed})

# S3 acts on {0,1,2}; composition gh means apply h then g.
G = tuple(permutations(range(3)))
gindex = {g: i for i, g in enumerate(G)}
e = (0, 1, 2)
t = (1, 0, 2)
u = (1, 2, 0)       # order 3, genuinely nontrivial row gauge outside H
v = (0, 2, 1)
H = (e, t)


def gm(g, h):
    return tuple(g[h[x]] for x in range(3))


def inv(g):
    return next(h for h in G if gm(g, h) == e and gm(h, g) == e)


require(all(gm(gm(g, h), k) == gm(g, gm(h, k)) for g, h, k in product(G, repeat=3)), "S3 associativity")
require(gm(t, t) == e and gm(gm(u, t), inv(u)) not in H, "H must be nonnormal C2")
require(gm(gm(u, u), u) == e and u != e, "row gauge must have order 3")

# B is the free left-regular band on two letters. The empty word is a unit;
# multiplication appends previously unseen letters. Swapping letters is an
# order-two automorphism. This B is not the author's multiplication table.
B = ((), (0,), (1,), (0, 1), (1, 0))


def bm(a, b):
    return a + tuple(x for x in b if x not in a)


def alpha(bit, b):
    return b if bit == 0 else tuple(1 - x for x in b)


def regular_identity(x, y, z):
    left = bm(bm(bm(bm(x, y), x), z), x)
    right = bm(bm(bm(x, y), z), x)
    return left == right


require(all(bm(a, b) in B for a, b in product(B, repeat=2)), "band closure")
require(all(bm(b, b) == b for b in B), "band idempotence")
require(all(bm(bm(a, b), c) == bm(a, bm(b, c)) for a, b, c in product(B, repeat=3)), "band associativity")
require(all(bm(bm(a, b), a) == bm(a, b) for a, b in product(B, repeat=2)), "left regular band identity")
require(all(alpha(i ^ j, b) == alpha(i, alpha(j, b)) for i, j, b in product(range(2), range(2), B)), "C2 action")
require(all(alpha(i, bm(a, b)) == bm(alpha(i, a), alpha(i, b)) for i, a, b in product(range(2), B, B)), "C2 automorphism")
require(alpha(1, (0,)) != (0,), "action must be nontrivial")
corners = []
for b in B:
    corner = {bm(bm(b, c), b) for c in B}
    require(all(bm(x, y) in corner for x, y in product(corner, repeat=2)), "corner closure")
    require(all(regular_identity(x, y, z) for x, y, z in product(corner, repeat=3)), "corner regular identity")
    corners.append({"idempotent": b, "corner_size": len(corner)})

# Unique decomposition x=rh for explicitly selected left cosets rH.
remaining = set(G)
decomp = {}
reps = []
while remaining:
    r = min(remaining)
    reps.append(r)
    for bit, h in enumerate(H):
        x = gm(r, h)
        require(x in remaining and x not in decomp, "left coset decomposition")
        decomp[x] = (r, bit)
        remaining.remove(x)
require(reps[0] == e and len(reps) == 3 and set(decomp) == set(G), "coset coverage")


def J(b):
    return tuple(alpha(decomp[x][1], b) for x in G)


def shift(g, F):
    return tuple(F[gindex[gm(x, g)]] for x in G)


def left_shift(g, F):
    return tuple(F[gindex[gm(g, x)]] for x in G)


def point(F, K):
    return tuple(bm(a, b) for a, b in zip(F, K))


Jtable = {b: J(b) for b in B}
require(len(set(Jtable.values())) == len(B), "J injection")
require(all(Jtable[b][gindex[e]] == b for b in B), "J evaluation at identity")
require(all(Jtable[bm(a, b)] == point(Jtable[a], Jtable[b]) for a, b in product(B, repeat=2)), "J band homomorphism")
require(all(shift(h, Jtable[b]) == Jtable[alpha(bit, b)] for bit, h in enumerate(H) for b in B), "H equivariance")
# These coordinate equations verify the shift representation on EVERY function,
# not only the five J-images: they compare its argument in each G-coordinate.
require(all(gm(gm(x, g), k) == gm(x, gm(g, k)) for x, g, k in product(G, repeat=3)), "shift composition")
require(all(len({gm(x, g) for x in G}) == len(G) for g in G), "shift bijectivity")
wrong_equiv = [(bit, b) for bit, h in enumerate(H) for b in B if left_shift(h, Jtable[b]) != Jtable[alpha(bit, b)]]
require(wrong_equiv, "left-shift mutation should violate H equivariance")

# Source rows and columns both collapse under f. Factorized gauges make the
# target sandwich identities explicit, with order-three row gauge u outside H.
row_map = (0, 0, 1)
col_map = (0, 0, 1)
row_bits = (0, 1, 0)
col_bits = (0, 1, 0)
U = (e, u)
V = (e, v)
base_bits = ((0, 1), (1, 0))
row_gauges = tuple(gm(U[row_map[i]], H[row_bits[i]]) for i in range(3))
col_gauges = tuple(gm(H[col_bits[l]], V[col_map[l]]) for l in range(3))
P0 = tuple(tuple(col_bits[l] ^ base_bits[col_map[l]][row_map[i]] ^ row_bits[i] for i in range(3)) for l in range(3))
P1 = tuple(tuple(gm(gm(inv(V[l]), H[base_bits[l][i]]), inv(U[i])) for i in range(2)) for l in range(2))
require(all(gm(gm(col_gauges[l], P1[col_map[l]][row_map[i]]), row_gauges[i]) == H[P0[l][i]] for l, i in product(range(3), repeat=2)), "Rees gauge identity")

D0 = tuple(product(range(3), range(2), range(3)))
D1 = tuple(product(range(2), G, range(2)))


def d0mul(a, b):
    i, g, l = a
    j, h, m = b
    return (i, g ^ P0[l][j] ^ h, m)


def d1mul(a, b):
    i, g, l = a
    j, h, m = b
    return (i, gm(gm(g, P1[l][j]), h), m)


def f(a):
    i, g, l = a
    return (row_map[i], gm(gm(row_gauges[i], H[g]), col_gauges[l]), col_map[l])


require(all(d0mul(d0mul(a, b), c) == d0mul(a, d0mul(b, c)) for a, b, c in product(D0, repeat=3)), "D0 associativity")
require(all(d1mul(d1mul(a, b), c) == d1mul(a, d1mul(b, c)) for a, b, c in product(D1, repeat=3)), "D1 associativity")
require(all(f(d0mul(a, b)) == d1mul(f(a), f(b)) for a, b in product(D0, repeat=2)), "actor homomorphism")
require(all((d0mul(a, a) == a) == (d1mul(f(a), f(a)) == f(a)) for a in D0), "actor purity")
actor_images = {f(a) for a in D0}
require(len(actor_images) == 8 and len(D0) == 18 and len(D1) == 24, "nononto actor sizes")
require(len(set(row_map)) < len(row_map) and len(set(col_map)) < len(col_map), "both label maps must collapse")

S = tuple(product(B, range(3), range(2), range(3)))
source_index = {s: n for n, s in enumerate(S)}


def source_mul(a, b):
    x, i, g, l = a
    y, j, h, m = b
    weight = g ^ P0[l][j]
    return (bm(x, alpha(weight, y)), i, weight ^ h, m)


def psi(s):
    b, i, g, l = s
    return ((i, l), shift(row_gauges[i], Jtable[b]), f((i, g, l)))


def target_mul(a, b, shift_fn=shift, reverse_weight=False):
    (i, l), F, d = a
    (j, m), K, d2 = b
    weight = gm(P1[d[2]][d2[0]], d[1]) if reverse_weight else gm(d[1], P1[d[2]][d2[0]])
    return ((i, m), point(F, shift_fn(weight, K)), d1mul(d, d2))


images = tuple(psi(s) for s in S)
require(len(S) == 90 and len(set(images)) == len(S), "whole-host injection")
require(all((images[i] == images[j]) == (S[i] == S[j]) for i, j in product(range(len(S)), repeat=2)), "pairwise injection")
# Record the whole 90 x 90 multiplication table and check every mapped product.
table = []
for a in S:
    row = []
    for b in S:
        c = source_mul(a, b)
        require(c in source_index, "source host closure")
        require(psi(c) == target_mul(psi(a), psi(b)), "whole-host product mismatch")
        row.append(source_index[c])
    table.append(row)
require(all(source_mul(source_mul(a, b), c) == source_mul(a, source_mul(b, c)) for a, b, c in product(S, repeat=3)), "source physical host associativity")

# Omit only a specified part of the source rectangle; report concrete collisions.
no_rectangle = collision_report([(F, d) for _, F, d in images], S)
no_row = collision_report([(rect[1], F, d) for rect, F, d in images], S)
no_column = collision_report([(rect[0], F, d) for rect, F, d in images], S)
require(all(r["unordered_collision_pairs"] > 0 for r in (no_rectangle, no_row, no_column)), "rectangle omissions must lose injection")


def psi_left(s):
    b, i, g, l = s
    return ((i, l), left_shift(row_gauges[i], Jtable[b]), f((i, g, l)))


def psi_inverse_row(s):
    b, i, g, l = s
    return ((i, l), shift(inv(row_gauges[i]), Jtable[b]), f((i, g, l)))


bad_left = []
bad_inverse_gauge = []
bad_order = []
for i, a in enumerate(S):
    for j, b in enumerate(S):
        c = source_mul(a, b)
        if psi_left(c) != target_mul(psi_left(a), psi_left(b), shift_fn=left_shift):
            bad_left.append((i, j))
        if psi_inverse_row(c) != target_mul(psi_inverse_row(a), psi_inverse_row(b)):
            bad_inverse_gauge.append((i, j))
        if psi(c) != target_mul(images[i], images[j], reverse_weight=True):
            bad_order.append((i, j))
require(bad_left and bad_inverse_gauge and bad_order, "targeted mutations must fail whole-host products")

# Genuine nonpure map C2 -> S3, g |-> e, with the SAME nontrivial B action.
# Every target element over e is idempotent in any band-by-group host; source
# x=(empty,1) is not. Enumerate the finite B target fiber as a concrete control.
x = ((), 1)
x2 = (bm(x[0], alpha(x[1], x[0])), x[1] ^ x[1])
require(x2 != x and gm(t, t) == e, "nonpure source witness")
nonpure_valid_assignments = 0
for bx, bx2 in product(B, repeat=2):
    target_x_squared = bm(bx, alpha(0, bx))
    if bx != bx2 and target_x_squared == bx2:
        nonpure_valid_assignments += 1
require(nonpure_valid_assignments == 0, "nonpure obstruction")

products_document = {
    "schema": "f115-independent-finite-whole-host-table-v1",
    "group_order_and_function_coordinate_order": G,
    "coset_decomposition_r_and_H_bit": [[x, decomp[x][0], decomp[x][1]] for x in G],
    "band_elements": B,
    "band_multiplication": [[bm(a, b) for b in B] for a in B],
    "coinduced_J_values_in_group_order": [[b, Jtable[b]] for b in B],
    "row_map": row_map, "column_map": col_map,
    "row_gauges": row_gauges, "column_gauges": col_gauges,
    "source_sandwich_bits": P0, "target_sandwich_permutations": P1,
    "source_actors_and_images": [[a, f(a)] for a in D0],
    "source_host_elements_in_index_order": S,
    "transported_host_elements_in_index_order": images,
    "host_product_index_table": table,
}
product_bytes = json_bytes(products_document)
with PRODUCTS.open("xb") as out:
    out.write(product_bytes)

elapsed = time.monotonic() - start
clock_end = native_clock()
result = {
    "result": "PASS_FINITE_DIAGNOSTIC_ONLY",
    "clock_start_native": clock_start,
    "clock_end_native": clock_end,
    "elapsed_monotonic_seconds": round(elapsed, 6),
    "python": sys.executable,
    "python_version": platform.python_version(),
    "manifest": {"path": str(MANIFEST), "sha256": digest(manifest_bytes), "bytes": len(manifest_bytes), "LF": manifest_bytes.count(b"\n")},
    "program": {"path": str(Path(__file__).resolve()), "sha256": digest(script), "bytes": len(script), "LF": script.count(b"\n")},
    "frozen_inputs_in_read_order": inputs,
    "products": {"path": str(PRODUCTS), "sha256": digest(product_bytes), "bytes": len(product_bytes), "LF": product_bytes.count(b"\n")},
    "group": {"order": len(G), "H_order": len(H), "H_nonnormal_conjugate": gm(gm(u, t), inv(u)), "coset_representatives": reps},
    "band": {"order": len(B), "kind": "free left-regular band on two letters", "action_moves": [[0], alpha(1, (0,))], "local_corners": corners},
    "actor": {"source_order": len(D0), "target_order": len(D1), "image_order": len(actor_images), "source_idempotents": sum(d0mul(a, a) == a for a in D0), "target_idempotents": sum(d1mul(a, a) == a for a in D1), "homomorphism_pairs_checked": len(D0) ** 2, "purity_elements_checked": len(D0), "source_associativity_triples_checked": len(D0) ** 3, "target_associativity_triples_checked": len(D1) ** 3},
    "whole_host": {"source_order": len(S), "target_band_order": 9 * (len(B) ** len(G)), "target_host_order": 9 * (len(B) ** len(G)) * len(D1), "product_pairs_checked": len(S) ** 2, "injection_ordered_pairs_checked": len(S) ** 2, "source_associativity_triples_checked": len(S) ** 3, "J_values_checked": len(B), "J_H_equivariance_checks": len(B) * len(H)},
    "controls": {
        "omit_entire_rectangle": no_rectangle,
        "omit_row_factor": no_row,
        "omit_column_factor": no_column,
        "wrong_left_shift_equivariance_failures": len(wrong_equiv),
        "wrong_left_shift_equivariance_first": wrong_equiv[0],
        "wrong_left_shift_host_product_mismatches": len(bad_left),
        "wrong_left_shift_first_pair_indices": bad_left[0],
        "inverse_row_gauge_host_product_mismatches": len(bad_inverse_gauge),
        "inverse_row_gauge_first_pair_indices": bad_inverse_gauge[0],
        "reversed_action_weight_host_product_mismatches": len(bad_order),
        "reversed_action_weight_first_pair_indices": bad_order[0],
        "nonpure_C2_to_S3": {"source_element": x, "source_square": x2, "actor_image_is_target_identity": True, "target_B_fiber_distinct_assignments_considered": len(B) ** 2 - len(B), "injective_homomorphic_assignments": nonpure_valid_assignments},
    },
    "limitations": ["This finite example does not prove the infinite general theorem or the canonical-q presentation.", "Same-harness diagnostic only; not human, independent-model-family, formal/kernel or novelty clearance."],
}
result_bytes = json_bytes(result)
with RESULT.open("xb") as out:
    out.write(result_bytes)
print(json.dumps({"result": result["result"], "clock_start_native": clock_start, "clock_end_native": clock_end, "program_sha256": digest(script), "products_sha256": digest(product_bytes), "result_sha256": digest(result_bytes), "host_products": len(S) ** 2, "controls": result["controls"]}, sort_keys=True))
