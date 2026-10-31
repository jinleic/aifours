#!/usr/bin/env python3
"""Pre-run amendments to this reviewer's own control script, not author code."""
from pathlib import Path
import sys

p = Path(sys.argv[1])
s = p.read_text()
old = '    Qp = [(((kp[a0b ^ E.a0 ^ E.a0 ^ a] - 1) // 2) % 2) for a in E.a_of]  # based at a0b? keep base a0\n'
assert s.count(old) == 1
s = s.replace(old, '')
old = 'sorted(cnt.values()) == [128] * 4, cnt)'
assert s.count(old) == 1
s = s.replace(old, 'sorted(cnt.values()) == [128] * 4, {str(key): value for key, value in cnt.items()})')
old = '        max_odd_const = 1464 + (56 * (z - 16)) // 64\n'
assert s.count(old) == 1
s = s.replace(old, '')
old = '                   "bound_with_mixed_classes": bound_mixed, "mixed_contradicts": bound_mixed > 16384,\n                   "largest_odd_constant_still_contradicting": max_odd_const}'
assert s.count(old) == 1
s = s.replace(old, '                   "bound_with_mixed_classes": bound_mixed, "mixed_contradicts": bound_mixed > 16384}')
old = '    record("G3neg at |k|<=8 the T=0 arithmetic would allow 128*16+384*64=26624>=16384 (no exclusion); bound 15872 needs |k|<=7", 128 * 16 + 384 * 64 >= 16384 and 128 * 16 + 384 * 36 == 15872 < 16384, kind="negative")'
assert s.count(old) == 1
s = s.replace(old, '    record("G3neg structured peak-32 function: q=0 can have k=+-8, so q-zero square bound 16 used at peak<=28 fails", any(v*v > 16 and (v//2)%2 == 0 for v in k), kind="negative")')
new = r'''
def verify_receipt_pins():
    from pathlib import Path
    root = Path(__file__).resolve().parent
    mp = root / "manifest-v1.json"
    raw = mp.read_bytes()
    mh = hashlib.sha256(raw).hexdigest()
    assert mh == "8f10719b5e86f5198f79d3e1ad055169d0566489c2adb87584a528ac19a32f27"
    m = json.loads(raw)
    pins = []
    for item in m["inputs_in_read_order"]:
        blob = Path(item["path"]).read_bytes()
        observed = {"path": item["path"], "sha256": hashlib.sha256(blob).hexdigest(),
                    "bytes": len(blob), "LF": blob.count(b"\n")}
        for key in ("sha256", "bytes", "LF"):
            assert observed[key] == item[key], (key, observed, item)
        pins.append(observed)
    RESULTS["input_pins"] = {"manifest_sha256": mh, "inputs_in_order": pins}


def control_H():
    # Genuine structured 9-variable example. Baseline = 8-variable hyperbolic
    # bent form xor x8. Toggle 8 linearly independent points with 4 ones and
    # 4 zeros. This preserves weight 256 and generates a rank-six even q.
    f0 = [sum(((x >> i) & 1) * ((x >> (i + 1)) & 1) for i in (0, 2, 4, 6)) % 2 ^ ((x >> 8) & 1)
          for x in range(SIZE)]
    pts = [(1 << i) ^ (256 if i < 4 else 0) for i in range(8)]
    f = list(f0)
    before_bits = [f[p] for p in pts]
    for p in pts:
        f[p] ^= 1
    k = walsh_k(f)
    T = xor_all(support(f))
    E = EvenHalf(k, T)
    R = E.rad
    RESULTS["examples"]["structured_eight_toggles"] = {
        "truth_table_sha256": hashlib.sha256(bytes(f)).hexdigest(),
        "definition": "f0=sum(x[2i]*x[2i+1],i=0..3) xor x8; toggle e_i+e8 for i<4, e_i for 4<=i<8",
        "toggled_points": pts, "T": T, "rank": E.rank, "rad_alpha": R,
        "q_zero_count": E.q.count(0), "peak_abs_k": max(abs(v) for v in k),
        "walsh_zeros": k.count(0), "radical_values_k": [k[E.a_of[r]] for r in R],
    }
    ok = sum(before_bits) == 4 and sum(f) == 256 and T != 0 and E.rank == 6 and len(R) == 4 and all(E.q[r] == 0 for r in R)
    record("H1 structured actual balanced f: 8 point toggles, T!=0, rank B=6, |R|=4, q|R=0", ok, RESULTS["examples"]["structured_eight_toggles"])
    lam, rho = {}, {}
    okphase = True
    for r in R:
        ds = [((k[E.a_of[x ^ r]] - k[E.a_of[x]]) // 4) % 2 for x in range(HALF)]
        poss = [v for v in (0, 1) if ds == [v * E.q[x] for x in range(HALF)]]
        if len(poss) != 1:
            okphase = False
            continue
        lam[r] = poss[0]
        vals = {E.Q[x ^ r] ^ E.Q[x] for x in range(HALF)}
        if len(vals) != 1:
            okphase = False
            continue
        rho[r] = vals.pop()
    okphase &= len(lam) == len(rho) == 4
    okphase &= all(lam[r ^ s] == lam[r] ^ lam[s] and rho[r ^ s] == rho[r] ^ rho[s] for r in R for s in R)
    okphase &= all((k[E.a_of[x ^ r]] - k[E.a_of[x]] - 4 * lam[r] * E.q[x]) % 8 == 0 for x in range(HALF) for r in R)
    record("H2 on structured actual f, (10) holds with unique linear lambda and odd rho", okphase, {"lambda": lam, "rho": rho})
    record("H3neg structured actual f has lambda=rho!=0 but violates peak<=28 and Z=R: theorem is not universal", lam == rho and any(lam.values()) and max(abs(v) for v in k) > 7 and any(k[E.a_of[r]] != 0 for r in R), kind="negative")
    # Check genuine input translations (recompute Walsh from translated truth
    # tables) rather than just relabel signs in an array.
    chosen = [0]
    # Include one representative for each radical character plus 12 others.
    r1, r2 = [r for r in R if r][:2]
    chseen = set()
    for t in range(SIZE):
        ch = (dot(E.a_of[r1], t), dot(E.a_of[r2], t))
        if ch not in chseen:
            chosen.append(t)
            chseen.add(ch)
    rng = random.Random(152007)
    chosen += rng.sample(range(SIZE), 12)
    chosen = list(dict.fromkeys(chosen))
    okt = True
    norm_case = None
    for t in chosen:
        ft = [f[x ^ t] for x in range(SIZE)]
        kt = walsh_k(ft)
        Et = EvenHalf(kt, T)
        okt &= xor_all(support(ft)) == T
        okt &= kt == [(-1) ** dot(a, t) * k[a] for a in range(SIZE)]
        okt &= Et.q == E.q
        for r in R:
            psi = dot(E.a_of[r], t)
            okt &= all((kt[E.a_of[x ^ r]] - kt[E.a_of[x]] - 4 * (lam[r] ^ psi) * Et.q[x]) % 8 == 0 for x in range(HALF))
            okt &= {Et.Q[x ^ r] ^ Et.Q[x] for x in range(HALF)} == {rho[r] ^ psi}
        if all(dot(E.a_of[r], t) == rho[r] for r in R):
            norm_case = {"t": t, "weight_Q_t": sum(Et.Q), "all_rho_t_zero": all({Et.Q[x ^ r] ^ Et.Q[x] for x in range(HALF)} == {0} for r in R)}
    record("H4 structured f: genuine input translations recompute Walsh and obey lambda_t=lambda+psi, rho_t=rho+psi", okt, {"translations_tested": chosen})
    record("H5 structured f: a translation with psi=rho has rho_t=0 and wt(Q_t) in {112,144}", norm_case is not None and norm_case["all_rho_t_zero"] and norm_case["weight_Q_t"] in (112, 144), norm_case)
    # The original <=28 constants deliberately fail when applied outside
    # their caller: identify concrete actual fibers where the bound fails.
    R9 = [E.a_of[r] for r in R]
    chi = [(-1) ** lam[r] for r in R]
    seen = set()
    violations = []
    zero_fiber_energy = None
    for a in range(SIZE):
        if a in seen:
            continue
        F = [a ^ r for r in R9]
        seen.update(F)
        energy = sum(k[b] * k[b] for b in F)
        s2 = sum(chi[i] * k[a ^ r] for i, r in enumerate(R9)) ** 2
        if a == 0:
            zero_fiber_energy = energy
            continue
        if dot(a, T):
            typ, const = "odd", 1464
        elif E.q[E.al_of[a]]:
            typ, const = "q-one", 864
        else:
            typ, const = "q-zero", 640
        if s2 < 10 * energy - const:
            violations.append({"a": a, "type": typ, "k_fiber": [k[b] for b in F], "10E-S2": 10 * energy - s2, "constant": const})
    record("H6neg applying the <=28 fiber constants to structured outside-scope f fails on actual fibers; radical fiber not zero", len(violations) > 0 and zero_fiber_energy > 0, {"zero_fiber_E": zero_fiber_energy, "violation_count": len(violations), "first_violation": violations[0] if violations else None}, kind="negative")

'''
assert s.count('def main():') == 1
s = s.replace('def main():', new + '\ndef main():', 1)
s = s.replace('    control_A()\n', '    verify_receipt_pins()\n    control_A()\n', 1)
s = s.replace('    control_G()\n', '    control_G()\n    control_H()\n', 1)
p.write_text(s)
print('Prepared reviewer-owned controls:', p)
