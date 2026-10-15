"""Explicit parametrized GS bases (leading word -> right side) in the
Artin-Garside alphabet.  Letters: generator k (in the chosen order) = chr(97+k),
'1' = Delta, '0' = Delta^{-1}.

A family is (name, lhs_parts, rhs_parts, mins) where parts are (word, param)
with param None (fixed word) or a parameter name p meaning word^p.  The family
consists of all instances with p >= mins[p] (default 0).  Each parameter occurs
once on each side, possibly in a different order (certify.check_validity handles
permuted parameters by the general group-conjugation criterion).

The decomposition is chosen so that validity follows from 'right transport':
with LHS = A0 x1^p1 A1 ... xr^pr Ar and rho_k = Ak A(k+1) ... Ar, the positive
identities  x_k rho_k = rho_k y_k  give  LHS = A0 A1 ... Ar y1^p1 ... yr^pr,
and RHS has the form R y1^p1 ... yr^pr with the base identity A0...Ar = R.
"""


def twist_and_inverse(n_gens: int, phi: list[int]):
    fams = [("I1", [("10", None)], [("", None)], {}), ("I2", [("01", None)], [("", None)], {})]
    for i in range(n_gens):
        x, y = chr(97 + i), chr(97 + phi[i])
        fams.append((f"T{x}+", [(x + "1", None)], [("1" + y, None)], {}))
        fams.append((f"T{x}-", [(x + "0", None)], [("0" + y, None)], {}))
    return fams


def alt(x: str, y: str, k: int) -> str:
    return "".join(x if j % 2 == 0 else y for j in range(k))


def dihedral(m: int):
    """I_2(m), m >= 3, order a < b.  Delta = <ab>_m, phi = id (m even) or swap (m odd)."""
    phi = [0, 1] if m % 2 == 0 else [1, 0]
    fams = [("D1", [(alt("a", "b", m), None)], [("1", None)], {}),
            ("D2", [(alt("b", "a", m), None)], [("1", None)], {})]
    return {"type": ("I", 0, m), "order": [0, 1], "phi": phi,
            "families": fams + twist_and_inverse(2, phi)}


# B3 with letters a = s1, b = s3, c = s2 (Bourbaki s1 - s2 =4= s3), order a < b < c.
# m(a,c) = 3, m(b,c) = 4, m(a,b) = 2;  Delta = (abc)^3 is central (phi = id).
B3_FAMILIES = [
    ("F1", [("ba", None)], [("ab", None)], {}),
    ("F2", [("cac", None)], [("aca", None)], {}),
    ("F3", [("c", None), ("a", "i"), ("aca", None)], [("acaa", None), ("c", "i")], {"i": 1}),
    ("F4", [("cbcb", None)], [("bcbc", None)], {}),
    ("F5", [("c", None), ("b", "i"), ("bcbc", None)], [("bcbcc", None), ("b", "i")], {"i": 1}),
    ("F6", [("cbc", None), ("a", "i"), ("b", None)], [("bcbc", None), ("a", "i")], {"i": 1}),
    ("F7", [("ca", None), ("b", "i"), ("cbc", None)], [("acabc", None), ("b", "i")], {"i": 1}),
    ("F8", [("c", None), ("a", "i"), ("bcabcb", None)], [("bcabcab", None), ("c", "i")], {"i": 1}),
    ("F9", [("ca", None), ("b", "i"), ("c", None), ("a", "j"), ("bca", None)],
     [("acabca", None), ("b", "i"), ("c", "j")], {"i": 1, "j": 1}),
    ("F10", [("c", None), ("a", "i"), ("bcabc", None), ("a", "j"), ("b", None)],
     [("bcabcab", None), ("c", "i"), ("a", "j")], {"i": 2, "j": 1}),
    ("F11", [("cb", None), ("b", "i"), ("c", None), ("a", "j"), ("bca", None)],
     [("bcbcca", None), ("b", "i"), ("c", "j")], {"i": 1, "j": 1}),
    ("F12", [("ab", None), ("b", "i"), ("cabcabc", None)], [("1", None), ("b", "i")], {}),
]


def b3():
    phi = [0, 1, 2]
    return {"type": ("B", 3, 0), "order": [0, 2, 1], "phi": phi,
            "families": B3_FAMILIES + twist_and_inverse(3, phi)}


SPECS = {"B3": b3}
for _m in range(3, 13):
    SPECS[f"I2_{_m}"] = (lambda mm: (lambda: dihedral(mm)))(_m)


def from_json(path):
    """Families extracted by work/extract_families.py (all parameters >= 0)."""
    import json
    d = json.load(open(path))
    fams = []
    for f in d["families"]:
        assert f["rhs"] is not None, f["name"]
        fams.append((f["name"], [tuple(x) for x in f["lhs"]], [tuple(x) for x in f["rhs"]], {}))
    n = len(d["phi"])
    return {"type": tuple(d["type"]), "order": d["order"], "phi": d["phi"],
            "families": fams + twist_and_inverse(n, d["phi"])}


_HERE = __file__.rsplit("/", 1)[0]
SPECS["D4"] = lambda: from_json(_HERE + "/specs_D4.json")
SPECS["B3auto"] = lambda: from_json(_HERE + "/specs_B3auto.json")
SPECS["H3"] = lambda: from_json(_HERE + "/specs_H3.json")
SPECS["H3b"] = lambda: from_json(_HERE + "/specs_H3b.json")
SPECS["A3"] = lambda: from_json(_HERE + "/specs_A3.json")
