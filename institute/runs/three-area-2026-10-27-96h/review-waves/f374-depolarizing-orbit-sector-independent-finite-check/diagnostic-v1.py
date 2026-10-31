class InvariantFailure(RuntimeError):
    pass


class CooperativeStop(RuntimeError):
    pass


def scientific(np, receipt, guard):
    import math
    from itertools import product

    tol = 2.0e-10
    detect = 1.0e-7
    ps = (0.0, 0.25, 0.5, 2.0 / 3.0, 0.9, 1.0,
          8.0 / 7.0, 1.25, 4.0 / 3.0)
    receipt.update({
        "tolerance": tol,
        "mutation_detection_threshold": detect,
        "p_grid": list(ps),
        "identity_max_residual": {},
        "checks": 0,
        "case_inputs": [],
        "prefix_rows": [],
        "ensembles": [],
        "negative_controls": [],
        "examples": [],
        "finite_only": True,
    })

    def need(condition, name):
        guard()
        receipt["checks"] += 1
        if not bool(condition):
            raise InvariantFailure(name)

    def residual(a, b):
        aa, bb = np.asarray(a), np.asarray(b)
        need(aa.shape == bb.shape, "comparison_shape")
        need(np.all(np.isfinite(aa)) and np.all(np.isfinite(bb)),
             "comparison_finite")
        return float(np.max(np.abs(aa - bb)))

    def close(name, a, b):
        value = residual(a, b)
        old = receipt["identity_max_residual"].get(name, 0.0)
        receipt["identity_max_residual"][name] = max(old, value)
        need(value <= tol, name + ": residual=" + repr(value))
        return value

    def tr(name, a):
        value = np.trace(a)
        close(name + "_imaginary_trace", np.imag(value), 0.0)
        return float(np.real(value))

    def density(name, a, n):
        need(a.shape == (2 ** n, 2 ** n), name + "_shape")
        need(np.all(np.isfinite(a)), name + "_finite")
        close(name + "_Hermitian", a, a.conj().T)
        close(name + "_trace", tr(name, a), 1.0)
        values, vectors = np.linalg.eigh(a)
        need(np.all(np.isfinite(values)), name + "_finite_spectrum")
        need(float(values[0]) >= -tol, name + "_positive")
        close(name + "_eigenbasis", vectors.conj().T @ vectors,
              np.eye(2 ** n))
        return values, vectors

    def projector(name, q, rank):
        need(q.shape == (16, 16), name + "_shape")
        need(np.all(np.isfinite(q)), name + "_finite")
        close(name + "_Hermitian", q, q.conj().T)
        close(name + "_idempotent", q @ q, q)
        close(name + "_rank", tr(name, q), float(rank))

    def unitary(name, u):
        close(name, u.conj().T @ u, np.eye(u.shape[0]))

    def cx(a):
        return np.stack((a.real, a.imag), axis=-1).tolist()

    def tensor(items):
        out = np.ones((1, 1), dtype=complex)
        for item in items:
            out = np.kron(out, item)
        return out

    def outer(v):
        return np.outer(v, v.conj())

    i2 = np.eye(2, dtype=complex)
    i16 = np.eye(16, dtype=complex)
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    z = np.diag([1.0, -1.0]).astype(complex)
    paulis = (i2, x, y, z)
    w4 = tensor((y, y, y, y))
    unitary("spin_unitarity", w4)
    close("spin_full_transpose_symmetry", w4.T, w4)

    axes = {}
    local_paulis = {}
    for n in (1, 2, 4):
        for q in range(n):
            others = [j for j in range(n) if j != q]
            order = [q] + others + [n + q] + [n + j for j in others]
            axes[n, q] = (order, np.argsort(order))
            local_paulis[n, q] = [
                tensor([s if j == q else i2 for j in range(n)])
                for s in paulis
            ]

    def replace(a, q, n):
        order, inverse = axes[n, q]
        d = 2 ** (n - 1)
        b = a.reshape((2,) * (2 * n)).transpose(order).reshape(2, d, 2, d)
        reduced = np.trace(b, axis1=0, axis2=2)
        lifted = np.einsum("ab,ij->aibj", i2 / 2.0, reduced)
        return lifted.reshape((2,) * (2 * n)).transpose(inverse).reshape(a.shape)

    def direct(a, p, n=4):
        guard()
        out = a.copy()
        for q in range(n):
            guard()
            out = (1.0 - p) * out + p * replace(out, q, n)
        return out

    def probabilities(p):
        values = (1.0 - 0.75 * p, p / 4.0, p / 4.0, p / 4.0)
        need(0.0 <= p <= 4.0 / 3.0, "physical_p_range")
        need(min(values) >= -tol, "physical_Kraus_probabilities")
        close("Kraus_probability_sum", sum(values), 1.0)
        return values

    def kraus(a, p, n=4):
        weights = probabilities(p)
        out = a.copy()
        for q in range(n):
            guard()
            nxt = np.zeros_like(out)
            for weight, u in zip(weights, local_paulis[n, q]):
                nxt += weight * (u @ out @ u.conj().T)
            out = nxt
        return out

    def spin(a):
        return w4 @ a.T @ w4

    def one_marginal(a, q):
        order, unused = axes[4, q]
        b = a.reshape((2,) * 8).transpose(order).reshape(2, 8, 2, 8)
        return np.trace(b, axis1=1, axis2=3)

    def radii(a):
        answer = []
        for q in range(4):
            eta = one_marginal(a, q)
            density("one_qubit_marginal", eta, 1)
            components = [tr("Bloch_component", eta @ s) for s in (x, y, z)]
            answer.append(math.sqrt(sum(v * v for v in components)))
        return answer

    def cat(m, u, phase):
        v = np.zeros(16, dtype=complex)
        v[0] = math.sqrt(u)
        endpoint = ((1 << m) - 1) << (4 - m)
        v[endpoint] = np.exp(1j * phase) * math.sqrt(1.0 - u)
        return v

    def rotations(offset):
        factors = []
        for j in range(4):
            theta = math.pi / (7 + j + offset)
            alpha = math.pi / (11 + j + offset)
            beta = -math.pi / (4 + j + offset)
            c, s = math.cos(theta), math.sin(theta)
            factors.append(np.array([
                [np.exp(1j * alpha) * c, np.exp(1j * beta) * s],
                [-np.exp(-1j * beta) * s, np.exp(-1j * alpha) * c],
            ], dtype=complex))
        return factors, tensor(factors)

    rf0, r0 = rotations(0)
    rf1, r1 = rotations(1)
    rots = (r0, r1)
    for u in rots:
        unitary("local_rotation_unitarity", u)
    receipt["local_rotation_factors_real_imag"] = [
        [cx(f) for f in rf0], [cx(f) for f in rf1]
    ]

    pairs = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))

    def bitindex(bits):
        return sum(bit << (3 - j) for j, bit in enumerate(bits))

    def pair_permutation(pairing):
        out = np.zeros((16, 16), dtype=complex)
        for old in product((0, 1), repeat=4):
            new = [0, 0, 0, 0]
            for j in range(2):
                new[pairing[0][j]] = old[j]
                new[pairing[1][j]] = old[2 + j]
            out[bitindex(new), bitindex(old)] = 1.0
        unitary("physical_pair_permutation", out)
        return out

    block_indices = {}
    for first, second in product(("E", "O"), repeat=2):
        a_bits = ((0, 0), (1, 1)) if first == "E" else ((0, 1), (1, 0))
        b_bits = ((0, 0), (1, 1)) if second == "E" else ((0, 1), (1, 0))
        block_indices[first + second] = [
            bitindex(a + b) for a in a_bits for b in b_bits
        ]
    encode = np.zeros((16, 4), dtype=complex)
    encode[block_indices["EE"], np.arange(4)] = 1.0
    pair_encode = np.zeros((4, 2), dtype=complex)
    pair_encode[[0, 3], [0, 1]] = 1.0
    elementary = {}
    for a, b in product(range(2), repeat=2):
        e = np.zeros((2, 2), dtype=complex)
        e[a, b] = 1.0
        elementary[a, b] = e

    def logical_parameters(t):
        a, b = (1.0 + t) / 2.0, (1.0 - t) / 2.0
        h, ell = a * a + b * b, a * b
        gamma = t / h
        need(h > 0.0 and 0.0 <= gamma <= 1.0 + tol,
             "logical_parameter_domain")
        close("logical_trace_normalization", h + 2.0 * ell, 1.0)
        close("logical_gamma_normalization", h * gamma, t)
        close("logical_coherence_normalization", h * t * gamma, t * t)
        return a, b, h, ell, gamma

    def logical_f(a, t, gamma, dephase=True):
        dep = gamma * a + (1.0 - gamma) * np.trace(a) * i2 / 2.0
        if not dephase:
            return dep
        return ((1.0 + t) * dep + (1.0 - t) * (z @ dep @ z)) / 2.0

    def blocks(omega, t, dephase=True, gamma_override=None):
        a, b, h, ell, gamma = logical_parameters(t)
        if gamma_override is not None:
            gamma = gamma_override
        def f(v):
            return logical_f(v, t, gamma, dephase)
        ee = np.zeros((4, 4), dtype=complex)
        for row, col in product(range(4), repeat=2):
            i, k = divmod(row, 2)
            j, l = divmod(col, 2)
            ee += omega[row, col] * np.kron(
                f(elementary[i, j]), f(elementary[k, l]))
        om = omega.reshape(2, 2, 2, 2)
        ma = np.trace(om, axis1=1, axis2=3)
        mb = np.trace(om, axis1=0, axis2=2)
        return {
            "EE": h * h * ee,
            "EO": h * ell * np.kron(f(ma), i2),
            "OE": h * ell * np.kron(i2, f(mb)),
            "OO": ell * ell * np.eye(4, dtype=complex),
        }

    def assemble(parts):
        out = np.zeros((16, 16), dtype=complex)
        for name, indices in block_indices.items():
            out[np.ix_(indices, indices)] = parts[name]
        return out

    p0 = np.zeros((16, 16), dtype=complex)
    p0[0, 0] = 1.0
    references = {}
    receipt["references"] = []
    for p in ps:
        guard()
        t = abs(1.0 - p)
        dphys = direct(p0, p)
        values, unused = density("physical_product_reference", dphys, 4)
        close("reference_direct_vs_Kraus", dphys, kraus(p0, p))
        dplus = direct(p0, 1.0 - t)
        vp, unused = density("positive_product_reference", dplus, 4)
        pref = np.cumsum(values[::-1])
        close("reference_reflection_spectrum", pref, np.cumsum(vp[::-1]))
        a, b, h, ell, gamma = logical_parameters(t)
        close("literal_positive_product_reference", dplus,
              tensor((np.diag([a, b]),) * 4))
        references[p] = (dphys, dplus, pref)
        receipt["references"].append({
            "p": p, "t": t, "Kraus_probabilities": list(probabilities(p)),
            "prefix": pref.tolist(), "h": h, "ell": ell, "gamma": gamma,
        })
        for e in elementary.values():
            physical = direct(pair_encode @ e @ pair_encode.conj().T,
                              1.0 - t, 2)
            expected = np.zeros((4, 4), dtype=complex)
            expected[np.ix_([0, 3], [0, 3])] = h * logical_f(e, t, gamma)
            expected[np.ix_([1, 2], [1, 2])] = ell * np.trace(e) * i2
            close("one_pair_linear_basis_direct_identity", physical, expected)
            literal = np.array([
                [a*a*e[0, 0] + b*b*e[1, 1], t*t*e[0, 1]],
                [t*t*e[1, 0], b*b*e[0, 0] + a*a*e[1, 1]],
            ], dtype=complex)
            close("one_pair_entrywise_vs_parameter_map",
                  h * logical_f(e, t, gamma), literal)

    layer_stacks = {}
    for weight in (1, 2):
        matrices = []
        for labels in product(range(4), repeat=4):
            if sum(label != 0 for label in labels) == weight:
                matrices.append(tensor([paulis[label] for label in labels]))
        layer_stacks[weight] = np.stack(matrices)

    def layers(rho):
        answer = []
        for weight in (1, 2):
            stack = layer_stacks[weight]
            coefficients = np.einsum("aij,ji->a", stack, rho)
            close("real_Pauli_coefficients", coefficients.imag,
                  np.zeros(coefficients.shape))
            answer.append(np.einsum("a,aij->ij", coefficients.real, stack))
        return answer

    qrng = np.random.default_rng(3740001)
    qb, unused = np.linalg.qr(
        qrng.normal(size=(16, 16)) + 1j * qrng.normal(size=(16, 16)))
    unitary("complex_Q_basis_unitarity", qb)
    qs, qprimes = [], []
    for k in range(1, 17):
        q = qb[:, :k] @ qb[:, :k].conj().T
        qp = w4 @ q.T @ w4
        projector("complex_Q", q, k)
        projector("reflected_complex_Q", qp, k)
        qs.append(q)
        qprimes.append(qp)
    receipt["Q_seed"] = 3740001

    cases = []
    def add(name, kind, baseline, transform, inputs, omega=None, components=None):
        density("case_baseline", baseline, 4)
        unitary("case_transform", transform)
        rho = transform @ baseline @ transform.conj().T
        density("case_input", rho, 4)
        item = {
            "id": name, "kind": kind, "base": baseline, "T": transform,
            "rho": rho, "omega": omega, "components": components,
        }
        cases.append(item)
        receipt["case_inputs"].append({"id": name, "kind": kind, **inputs})
        return item

    a_cases = []
    for m in range(1, 5):
        for ui, u in enumerate((0.0, 2.0/7.0, 0.5, 0.9, 1.0)):
            for fi, phase_pi in enumerate((0.5, -1.0/3.0)):
                rot = (m + ui + fi) % 2
                v = cat(m, u, math.pi * phase_pi)
                a_cases.append(add(
                    "A_m%d_u%d_f%d" % (m, ui, fi), "A",
                    outer(v), rots[rot],
                    {"m": m, "u": u, "phase_pi": phase_pi, "rotation": rot}))

    seed = 37420261030
    rng = np.random.default_rng(seed)
    g = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    omega_full = g @ g.conj().T
    omega_full /= np.trace(omega_full).real
    v = rng.normal(size=4) + 1j * rng.normal(size=4)
    v /= np.linalg.norm(v)
    omega_pure = outer(v)
    g2 = rng.normal(size=(4, 2)) + 1j * rng.normal(size=(4, 2))
    omega_rank2 = g2 @ g2.conj().T
    omega_rank2 /= np.trace(omega_rank2).real
    omega_mix = 0.37 * omega_pure + 0.63 * omega_rank2
    omegas = (omega_full, omega_pure, omega_mix)
    receipt["logical_seed"] = seed
    receipt["logical_states_real_imag"] = [cx(o) for o in omegas]
    b_cases = []
    for pi, pairing in enumerate(pairs):
        perm = pair_permutation(pairing)
        for oi, omega in enumerate(omegas):
            density("logical_input", omega, 2)
            rot = oi % 2
            b_cases.append(add(
                "B_pair%d_state%d" % (pi, oi), "B",
                encode @ omega @ encode.conj().T, rots[rot] @ perm,
                {"pairing": pairing, "logical_state": oi, "rotation": rot},
                omega=omega))

    for name, kind, components in (
        ("A_convex", "A-convex", ((0.4, a_cases[6]), (0.6, a_cases[24]))),
        ("C_convex", "C-convex",
         ((0.2, a_cases[36]), (0.3, b_cases[4]), (0.5, b_cases[8]))),
    ):
        need(all(weight >= 0.0 for weight, item in components),
             "convex_weights_positive")
        close("convex_weights_sum", sum(v for v, item in components), 1.0)
        rho = sum((weight * item["rho"] for weight, item in components),
                  np.zeros((16, 16), dtype=complex))
        add(name, kind, rho, i16,
            {"components": [[weight, item["id"]] for weight, item in components]},
            components=components)

    for case in cases:
        guard()
        receipt["context"] = {"case": case["id"]}
        rho, base, transform = case["rho"], case["base"], case["T"]
        c1, c2 = layers(rho)
        reflected_rho = spin(rho)
        density("spin_flipped_input", reflected_rho, 4)
        covariant_qs = []
        for k, q in enumerate(qs, 1):
            covq = transform @ q @ transform.conj().T
            projector("covariant_Q", covq, k)
            covariant_qs.append(covq)

        for p in ps:
            guard()
            receipt["context"] = {"case": case["id"], "p": p}
            t = abs(1.0 - p)
            out, baseout = direct(rho, p), direct(base, p)
            values, vectors = density("physical_output", out, 4)
            bvalues, unused = density("canonical_output", baseout, 4)
            close("physical_direct_vs_Kraus", out, kraus(rho, p))
            close("local_permutation_covariance",
                  out, transform @ baseout @ transform.conj().T)
            refphys, refplus, refprefix = references[p]
            prefix = np.cumsum(values[::-1])
            bprefix = np.cumsum(bvalues[::-1])
            need(np.all(prefix <= refprefix + tol),
                 "all16_physical_majorization")
            need(np.all(bprefix <= refprefix + tol),
                 "all16_canonical_majorization")
            close("prefix16_trace", prefix[-1], 1.0)
            plus = out if p <= 1.0 else direct(rho, 1.0 - t)
            density("positive_branch_output", plus, 4)
            if p > 1.0:
                close("physical_full_transpose_reflection", out, spin(plus))

            traces = []
            for k, (q, qp, covq) in enumerate(zip(qs, qprimes, covariant_qs), 1):
                observed = tr("actual_complex_Q", q @ out)
                traces.append(observed)
                need(observed <= refprefix[k - 1] + tol,
                     "complex_Q_product_bound")
                close("covariant_consuming_Q_trace",
                      tr("covariant_Q_trace", covq @ out),
                      tr("canonical_Q_trace", q @ baseout))
                qmax = vectors[:, -k:] @ vectors[:, -k:].conj().T
                projector("maximizing_Q", qmax, k)
                close("maximizing_Q_actual_prefix",
                      tr("maximizing_Q_trace", qmax @ out), prefix[k - 1])
                if p > 1.0:
                    close("complex_reflection_trace_duality",
                          observed, tr("reflected_Q_trace", qp @ plus))

            big_b = (t**3 / 2.0) * (
                (1.0 + t) * rho - (1.0 - t) * reflected_rho)
            reconstructed = (big_b + (1.0 - t**4) * i16 / 16.0
                             + (t - t**3) * c1 / 16.0
                             + (t*t - t**4) * c2 / 16.0)
            close("actual_Pauli_joint_decomposition", plus, reconstructed)
            qeff = qprimes[2] if p > 1.0 else qs[2]
            lhs = (16.0 * tr("same_Q_B", qeff @ big_b)
                   + (t - t**3) * tr("same_Q_C1", qeff @ c1)
                   + (t*t - t**4) * tr("same_Q_C2", qeff @ c2))
            rhs = 8.0*t + 6.0*t*t + 2.0*t**4
            close("same_Q_joint_actual_output_identity",
                  lhs, 16.0 * traces[2] - 3.0 * (1.0 - t**4))
            need(lhs <= rhs + tol, "same_Q_joint_bound")

            if case["omega"] is not None:
                predicted_blocks = blocks(case["omega"], t)
                predicted = assemble(predicted_blocks)
                actual_positive = (baseout if p <= 1.0
                                   else direct(base, 1.0 - t))
                close("ClassB_full_direct_block_identity",
                      actual_positive, predicted)
                a, b, h, ell, gamma = logical_parameters(t)
                d = np.diag([a*a/h, b*b/h]).astype(complex)
                close("logical_reference_gamma", np.diag(d),
                      np.array([(1.0 + gamma)/2.0, (1.0 - gamma)/2.0]))
                refblocks = {
                    "EE": h*h*np.kron(d, d),
                    "EO": h*ell*np.kron(d, i2),
                    "OE": h*ell*np.kron(i2, d),
                    "OO": ell*ell*np.eye(4, dtype=complex),
                }
                expected_traces = {
                    "EE": h*h, "EO": 2*h*ell,
                    "OE": 2*h*ell, "OO": 4*ell*ell,
                }
                for label, indices in block_indices.items():
                    actual_block = actual_positive[np.ix_(indices, indices)]
                    close("ClassB_" + label + "_direct_identity",
                          actual_block, predicted_blocks[label])
                    close("ClassB_" + label + "_reference",
                          refplus[np.ix_(indices, indices)], refblocks[label])
                    close("ClassB_" + label + "_trace",
                          tr("block_trace", actual_block), expected_traces[label])
                    ap = np.cumsum(np.linalg.eigvalsh(actual_block)[::-1])
                    rp = np.cumsum(np.linalg.eigvalsh(refblocks[label])[::-1])
                    need(np.all(ap <= rp + tol),
                         "ClassB_" + label + "_all_block_prefixes")
                transformed = transform @ predicted @ transform.conj().T
                if p > 1.0:
                    transformed = spin(transformed)
                close("ClassB_transformed_actual_physical_output",
                      out, transformed)

            if case["components"] is not None:
                linear = sum(
                    (weight * direct(item["rho"], p)
                     for weight, item in case["components"]),
                    np.zeros((16, 16), dtype=complex))
                close("physical_convex_mixture_linearity", out, linear)

            receipt["prefix_rows"].append({
                "case": case["id"], "p": p,
                "actual_prefix": prefix.tolist(),
                "canonical_prefix": bprefix.tolist(),
                "complex_Q_traces": traces,
                "same_Q_joint_lhs_rhs": [lhs, rhs],
            })

    def ensemble(m, u, phase, p, rotation, q0_override=None, emit_weights=False):
        guard()
        t = abs(1.0 - p)
        a, b = (1.0 + t)/2.0, (1.0 - t)/2.0
        dim = 2 ** m
        complement_pairs = [(j, dim - 1 - j) for j in range(dim // 2)]
        dplus = direct(p0, 1.0 - t)
        vv = cat(m, u, phase)
        rho = rotation @ outer(vv) @ rotation.conj().T
        actual = direct(rho, p)
        density("orbit_input", rho, 4)
        density("orbit_actual_output", actual, 4)
        vfull = np.eye(dim, dtype=complex)
        v0 = np.eye(2, dtype=complex)
        raw_q0 = None
        if t == 0.0:
            probabilities_per_pair = []
            mask_values = (0,)
        else:
            endpoint = np.array([
                [u*a**m + (1-u)*b**m,
                 t**m*math.sqrt(u*(1-u))*np.exp(-1j*phase)],
                [t**m*math.sqrt(u*(1-u))*np.exp(1j*phase),
                 (1-u)*a**m + u*b**m],
            ], dtype=complex)
            ev, evec = np.linalg.eigh(endpoint)
            v0 = evec[:, ::-1]
            delta = a**m - b**m
            need(delta > 0.0, "orbit_endpoint_nonzero_denominator")
            raw_q0 = 0.5 + (ev[1] - ev[0])/(2.0*delta)
            need(0.5 - tol <= raw_q0 <= 1.0 + tol,
                 "orbit_endpoint_alignment")
            q0 = min(1.0, max(0.5, float(raw_q0)))
            close("orbit_roundoff_only_probability_adjustment", q0, raw_q0)
            if q0_override is not None:
                q0 = q0_override
            probabilities_per_pair = [q0] + [u] * (dim//2 - 1)
            vfull[np.ix_([0, dim-1], [0, dim-1])] = v0
            mask_values = range(1 << len(complement_pairs))
        hsum = np.zeros((16, 16), dtype=complex)
        weights = []
        total = 0.0
        for mask in mask_values:
            guard()
            swap = np.eye(dim, dtype=complex)
            weight = 1.0
            if t != 0.0:
                for j, (left, right) in enumerate(complement_pairs):
                    flipped = bool(mask & (1 << j))
                    q = probabilities_per_pair[j]
                    weight *= (1.0 - q) if flipped else q
                    if flipped:
                        swap[np.ix_([left, right], [left, right])] = x
            need(weight >= 0.0, "orbit_nonnegative_weights")
            active_u = vfull @ swap
            full_u = np.kron(active_u, np.eye(2 ** (4-m)))
            if p > 1.0:
                full_u = w4 @ full_u.conj()
            full_u = rotation @ full_u
            unitary("orbit_component_unitarity", full_u)
            hsum += weight * (full_u @ dplus @ full_u.conj().T)
            total += weight
            weights.append(float(weight))
        close("orbit_weight_normalization", total, 1.0)
        density("orbit_assembled_output", hsum, 4)
        description = {
            "m": m, "u": u, "phase": phase, "p": p, "rotation": 0,
            "pairs": complement_pairs,
            "pair_no_swap_probabilities": probabilities_per_pair,
            "raw_q0": None if raw_q0 is None else float(raw_q0),
            "endpoint_V_real_imag": cx(v0),
            "terms": len(weights), "weight_sum": total,
            "mask_rule": "bit j swaps complement pair j; endpoint V then acts",
            "negative_branch_rule": "L @ W4 @ conjugate(activeU tensor I)",
        }
        if emit_weights:
            description["weights_in_increasing_mask_order"] = weights
        return hsum, actual, description

    orbit_cache = {}
    for m in range(1, 5):
        for p in (0.0, 0.5, 1.0, 1.25):
            receipt["context"] = {"ensemble_m": m, "p": p}
            hsum, actual, desc = ensemble(
                m, 0.9, math.pi/2.0, p, r0,
                emit_weights=(m == 4 and p == 0.5))
            desc["direct_output_residual"] = close(
                "ClassA_finite_orbit_actual_output", hsum, actual)
            for k, q in enumerate(qs, 1):
                close("ClassA_orbit_same_Q_trace",
                      tr("orbit_trace", q @ hsum), tr("actual_trace", q @ actual))
                bound = references[p][2][k - 1]
                need(tr("orbit_bound_trace", q @ actual) <= bound + tol,
                     "ClassA_orbit_same_Q_bound")
            receipt["ensembles"].append(desc)
            orbit_cache[m, p] = (hsum, actual, desc)

    receipt["context"] = {"example": 1}
    psi1 = cat(4, 0.9, math.pi/2.0)
    rho1 = outer(psi1)
    density("example1_input", rho1, 4)
    out1 = direct(rho1, 0.5)
    ev1, unused = density("example1_output", out1, 4)
    close("example1_direct_vs_Kraus", out1, kraus(rho1, 0.5))
    stated1 = np.zeros((16, 16), dtype=complex)
    stated1[0, 0], stated1[15, 15] = 73.0/256.0, 9.0/256.0
    stated1[0, 15], stated1[15, 0] = -3j/160.0, 3j/160.0
    for j in range(1, 15):
        stated1[j, j] = {1: 123.0/1280.0, 2: 9.0/256.0,
                         3: 27.0/1280.0}[j.bit_count()]
    close("example1_entire_stated_output", out1, stated1)
    root409 = math.sqrt(409.0)
    chi = np.zeros(16, dtype=complex)
    chi[0] = math.sqrt((root409 + 20.0)/(2.0*root409))
    chi[15] = 1j*math.sqrt((root409 - 20.0)/(2.0*root409))
    q1 = outer(chi)
    q1[1, 1] += 1.0
    q1[2, 2] += 1.0
    projector("example1_stated_Q", q1, 3)
    k31 = float(np.sum(ev1[-3:]))
    ref3 = float(references[0.5][2][2])
    close("example1_stated_K3", k31, (451.0 + 8.0*root409)/1280.0)
    close("example1_stated_reference", ref3, 675.0/1280.0)
    close("example1_stated_gap", ref3-k31, (28.0-root409)/160.0)
    close("example1_actual_maximizing_Q", tr("example1_Q_output", q1 @ out1), k31)
    close("example1_actual_endpoint_eigenvector",
          out1 @ chi, (41.0/256.0 + root409/160.0)*chi)
    c11, c21 = layers(rho1)
    t = 0.5
    b1 = (t**3/2.0)*((1+t)*rho1 - (1-t)*spin(rho1))
    stated_b = np.zeros((16, 16), dtype=complex)
    stated_b[np.ix_([0, 15], [0, 15])] = np.array(
        [[13.0/160.0, -3j/160.0], [3j/160.0, -3.0/160.0]])
    close("example1_stated_B", b1, stated_b)
    tb, tc1, tc2 = [tr("example1_same_Q", q1 @ a) for a in (b1, c11, c21)]
    close("example1_stated_trace_B", tb, (5.0 + 169.0/root409)/160.0)
    close("example1_stated_trace_C1", tc1, 16.0/5.0 + 64.0/root409)
    close("example1_stated_trace_C2", tc2, 6.0)
    jl = 16.0*tb + (t-t**3)*tc1 + (t*t-t**4)*tc2
    close("example1_stated_joint_lhs", jl, 113.0/40.0 + root409/10.0)
    close("example1_stated_joint_slack", 45.0/8.0-jl, 16.0*(ref3-k31))
    layer_maxima = [float(np.sum(np.linalg.eigvalsh(a)[-3:]))
                    for a in (b1, c11, c21)]
    close("example1_separate_layer_maxima", np.array(layer_maxima),
          np.array([(5.0+math.sqrt(73.0))/160.0, 32.0/5.0, 12.0]))
    need(all(bound > actual + tol
             for bound, actual in zip(layer_maxima, (tb, tc1, tc2))),
         "example1_separate_maxima_strict")
    rs = radii(rho1)
    close("example1_local_radii", np.array(rs), np.full(4, 0.8))
    close("example1_radius_square_sum", sum(a*a for a in rs), 64.0/25.0)
    receipt["examples"].append({
        "id": 1, "K3_actual": k31, "Q_trace_actual": tr("ex1_receipt", q1 @ out1),
        "reference_K3_actual": ref3, "gap_actual": ref3-k31,
        "same_Q_layer_traces_actual": [tb, tc1, tc2],
        "same_Q_joint_lhs_actual": jl, "local_radii_actual": rs,
        "actual_prefix": np.cumsum(ev1[::-1]).tolist(),
    })

    receipt["context"] = {"example": 2}
    pairv = np.array([3.0, 0.0, 0.0, 1j], dtype=complex)/math.sqrt(10.0)
    psi2 = np.kron(pairv, pairv)
    rho2 = outer(psi2)
    density("example2_input", rho2, 4)
    out2 = direct(rho2, 0.5)
    ev2, unused = density("example2_output", out2, 4)
    pairout = direct(outer(pairv), 0.5, 2)
    density("example2_pair_output", pairout, 2)
    close("example2_direct_vs_Kraus", out2, kraus(rho2, 0.5))
    close("example2_actual_tensor_square", out2, np.kron(pairout, pairout))
    stated_pair = np.diag([41.0/80.0, 3.0/16.0, 3.0/16.0, 9.0/80.0]).astype(complex)
    stated_pair[0, 3], stated_pair[3, 0] = -3j/40.0, 3j/40.0
    close("example2_entire_stated_pair_output", pairout, stated_pair)
    root73 = math.sqrt(73.0)
    zeta = np.array([
        math.sqrt((root73+8.0)/(2.0*root73)), 0.0, 0.0,
        1j*math.sqrt((root73-8.0)/(2.0*root73)),
    ], dtype=complex)
    odd = np.array([0.0, 1.0, 0.0, 0.0], dtype=complex)
    columns = np.column_stack((np.kron(zeta, zeta),
                               np.kron(zeta, odd), np.kron(odd, zeta)))
    close("example2_Q_columns_orthonormal", columns.conj().T @ columns, np.eye(3))
    q2 = columns @ columns.conj().T
    projector("example2_stated_Q", q2, 3)
    lp = (25.0+2.0*root73)/80.0
    close("example2_actual_Q_eigenvectors", out2 @ columns,
          columns*np.array([lp*lp, lp*3.0/16.0, lp*3.0/16.0]))
    k32 = float(np.sum(ev2[-3:]))
    close("example2_stated_K3", k32, (1667.0+160.0*root73)/6400.0)
    close("example2_stated_gap", ref3-k32, (427.0-40.0*root73)/1600.0)
    close("example2_actual_maximizing_Q", tr("example2_Q_output", q2 @ out2), k32)
    schmidt = np.linalg.svd(
        psi2.reshape(2, 2, 2, 2).transpose(0, 2, 1, 3).reshape(4, 4),
        compute_uv=False)
    close("example2_cut13_24_Schmidt_coefficients",
          schmidt, np.array([0.9, 0.3, 0.3, 0.1]))
    need(float(schmidt[-1]) > 1.0e-6, "example2_cut13_24_rank_four")
    close("example2_local_radii", np.array(radii(rho2)), np.full(4, 0.8))
    receipt["examples"].append({
        "id": 2, "K3_actual": k32, "Q_trace_actual": tr("ex2_receipt", q2 @ out2),
        "reference_K3_actual": ref3, "gap_actual": ref3-k32,
        "actual_prefix": np.cumsum(ev2[::-1]).tolist(),
        "Schmidt_coefficients_cut13_24_actual": schmidt.tolist(),
    })

    def reject(mutation, identity, left, right, prerequisites):
        value = residual(left, right)
        need(value > detect, mutation + "_must_fail_" + identity)
        receipt["negative_controls"].append({
            "mutation": mutation, "violated_identity": identity,
            "identity_residual": value,
            "prerequisites_checked": prerequisites,
            "rejected_for_intended_scientific_reason": True,
        })

    receipt["context"] = {"negative_controls": True}
    balanced = np.zeros(16, dtype=complex)
    balanced[0], balanced[15] = 1.0/math.sqrt(2.0), 1j/math.sqrt(2.0)
    qc = outer(balanced)
    qc[1, 1] += 1.0
    qc[2, 2] += 1.0
    projector("mutation_original_Q", qc, 3)
    rp, rn = direct(rho1, 0.75), direct(rho1, 1.25)
    density("mutation_reflection_positive_output", rp, 4)
    density("mutation_reflection_negative_output", rn, 4)
    close("mutation_reflection_positive_baseline", rn, spin(rp))
    good_qp, bad_qp = w4 @ qc.T @ w4, w4 @ qc @ w4
    projector("mutation_correct_reflected_Q", good_qp, 3)
    projector("mutation_missing_conjugation_Q_still_physical", bad_qp, 3)
    actual_trace = tr("mutation_actual_negative_trace", qc @ rn)
    close("reflection_trace_positive_baseline",
          actual_trace, tr("mutation_good_reflection", good_qp @ rp))
    reject("missing_conjugation", "reflection_trace_duality",
           actual_trace, tr("mutation_bad_reflection", bad_qp @ rp),
           ["rho density", "both physical branch outputs", "both rank-three projectors"])

    phase_rotation = np.kron(np.diag([1.0, 1j]), np.eye(8))
    unitary("mutation_phase_rotation_unitarity", phase_rotation)
    rotated_rho = phase_rotation @ rho1 @ phase_rotation.conj().T
    density("mutation_rotated_input", rotated_rho, 4)
    rotated_out = direct(rotated_rho, 0.5)
    density("mutation_rotated_output", rotated_out, 4)
    rotated_q = phase_rotation @ qc @ phase_rotation.conj().T
    projector("mutation_correct_rotated_Q", rotated_q, 3)
    close("mutation_output_covariance_baseline",
          rotated_out, phase_rotation @ out1 @ phase_rotation.conj().T)
    old_trace = tr("mutation_original_trace", qc @ out1)
    close("covariant_trace_positive_baseline",
          tr("mutation_correct_covariant_trace", rotated_q @ rotated_out), old_trace)
    reject("stale_Q", "local_covariance_consuming_projector_trace",
           tr("mutation_stale_trace", qc @ rotated_out), old_trace,
           ["original and rotated densities", "unitary rotation", "both rank-three projectors"])

    logical_example = np.array([3.0, 1j], dtype=complex)/math.sqrt(10.0)
    omega_control = outer(np.kron(logical_example, logical_example))
    density("mutation_logical_input", omega_control, 2)
    encoded_control = encode @ omega_control @ encode.conj().T
    density("mutation_encoded_input", encoded_control, 4)
    direct_control = direct(encoded_control, 0.5)
    density("mutation_direct_control_output", direct_control, 4)
    good_blocks = blocks(omega_control, 0.5)
    close("logical_blocks_positive_baseline", assemble(good_blocks), direct_control)
    ee_indices = block_indices["EE"]
    ee_actual = direct_control[np.ix_(ee_indices, ee_indices)]
    for mutation, mutated_blocks, identity in (
        ("omitted_logical_dephasing",
         blocks(omega_control, 0.5, dephase=False),
         "EE_direct_channel_identity_with_logical_dephasing"),
        ("incorrect_gamma_normalization",
         blocks(omega_control, 0.5, gamma_override=0.5),
         "EE_direct_channel_identity_with_gamma_t_over_h"),
    ):
        mutated_density = assemble(mutated_blocks)
        density(mutation + "_still_physical_density", mutated_density, 4)
        reject(mutation, identity, ee_actual, mutated_blocks["EE"],
               ["logical density", "encoded physical density", "physical direct output",
                "mutant remains positive Hermitian trace-one"])

    bad_orbit, orbit_actual, unused = ensemble(
        4, 0.9, math.pi/2.0, 0.5, r0, q0_override=0.5)
    close("orbit_positive_control_cached",
          orbit_cache[4, 0.5][0], orbit_cache[4, 0.5][1])
    reject("incorrect_orbitweight", "ClassA_finite_orbit_actual_output",
           bad_orbit, orbit_actual,
           ["physical input/output", "unitary ensemble members",
            "nonnegative normalized weights", "mutant remains a density"])

    need(len(receipt["negative_controls"]) == 5, "all_required_mutations_completed")
    need(len(receipt["prefix_rows"]) == len(cases)*len(ps),
         "all_case_parameter_rows_completed")
    receipt["case_count"] = len(cases)
    receipt["case_parameter_count"] = len(receipt["prefix_rows"])
    receipt["actual_prefix_comparisons"] = 16 * len(receipt["prefix_rows"])
    receipt["canonical_prefix_comparisons"] = 16 * len(receipt["prefix_rows"])
    receipt["all_required_scientific_sections_completed"] = True


def main():
    receipt = {
        "assignment": "f374-depolarizing-orbit-sector-independent-finite-check",
        "status": "INCOMPLETE",
        "complete": False,
        "failures": [],
        "model_authoring_source": "anthropic/claude-fable-5-1",
        "source_candidate_sha256":
            "a9b558665da012bfff67d56f520cc4d8fe44864e8bec4e8b43dc532344e8d915",
        "manifest_sha256":
            "95cd5cccd4081c8834f533c813cfda67a2a4c3852f68bb026c32c2883872b90d",
        "scientific_boundary":
            "Finite selected numerical diagnostics only; no universal or whole-target acceptance",
        "acceptance":
            "PASS receipt AND exit zero AND parent-observed elapsed <=55 seconds",
    }
    latch = [0]
    timer_armed = False
    started = None
    outcome = "ERROR"
    clock = None
    sigmod = None
    jsonmod = None
    resmod = None
    sysmod = None

    def sticky(target):
        def handler(signum, frame):
            if target[0] == 0:
                target[0] = signum
        return handler

    try:
        import os
        import sys
        import time
        import signal
        import json
        import resource
        clock, sigmod, jsonmod, resmod, sysmod = time, signal, json, resource, sys
        started = time.monotonic()
        receipt["native_execution_start_utc"] = time.strftime(
            "%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        receipt["cooperative_work_deadline_seconds"] = 50.0
        receipt["parent_elapsed_limit_seconds"] = 55.0
        receipt["rss_limit_bytes"] = 256 * 1024 * 1024
        names = (
            "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
            "VECLIB_MAXIMUM_THREADS", "BLIS_NUM_THREADS", "NUMEXPR_NUM_THREADS",
        )
        for name in names:
            os.environ[name] = "1"
        receipt["requested_thread_environment"] = {name: os.environ[name] for name in names}
        receipt["actual_backend_thread_count_measured"] = False

        handler = sticky(latch)
        for signum in (signal.SIGINT, signal.SIGTERM):
            signal.signal(signum, handler)
        if hasattr(signal, "SIGALRM") and hasattr(signal, "setitimer"):
            signal.signal(signal.SIGALRM, handler)
            signal.setitimer(signal.ITIMER_REAL, 52.0)
            timer_armed = True
        receipt["signal_handlers"] = "nonthrowing first-signal sticky latch"
        probe = [0]
        probe_handler = sticky(probe)
        probe_handler(signal.SIGINT, None)
        probe_handler(signal.SIGTERM, None)
        if probe[0] != signal.SIGINT:
            raise InvariantFailure("sticky_signal_handler_selfcheck")
        receipt["signal_latch_selfcheck"] = True

        def guard():
            if latch[0] != 0:
                raise CooperativeStop("signal_latched_" + str(latch[0]))
            if time.monotonic() - started >= 50.0:
                raise CooperativeStop("cooperative_work_deadline")

        guard()
        import numpy as np
        np.seterr(all="raise")
        receipt["python_version"] = sys.version
        receipt["numpy_version"] = np.__version__
        receipt["numpy_scalar_type"] = "complex128/float64"
        guard()
        scientific(np, receipt, guard)
        guard()
        receipt["complete"] = True
        outcome = "PASS"
    except BaseException as exc:
        if isinstance(exc, CooperativeStop):
            outcome = "INCOMPLETE"
        elif isinstance(exc, InvariantFailure):
            outcome = "FAIL"
        else:
            outcome = "ERROR"
        receipt["failures"].append({
            "phase": "initialization_or_science",
            "type": type(exc).__name__,
            "message": str(exc),
        })
    finally:
        try:
            if timer_armed:
                sigmod.setitimer(sigmod.ITIMER_REAL, 0.0)
        except BaseException as exc:
            outcome = "ERROR"
            receipt["failures"].append({
                "phase": "timer_settlement",
                "type": type(exc).__name__, "message": str(exc),
            })
        try:
            receipt["signal_latched"] = int(latch[0])
            if clock is not None and started is not None:
                receipt["elapsed_before_receipt_seconds"] = clock.monotonic() - started
                receipt["native_settlement_observation_utc"] = clock.strftime(
                    "%Y-%m-%dT%H:%M:%SZ", clock.gmtime())
            if resmod is not None and sysmod is not None:
                native_rss = resmod.getrusage(resmod.RUSAGE_SELF).ru_maxrss
                multiplier = 1 if sysmod.platform == "darwin" else 1024
                receipt["peak_rss_native"] = native_rss
                receipt["peak_rss_bytes"] = int(native_rss * multiplier)
                receipt["peak_rss_native_units"] = (
                    "bytes" if sysmod.platform == "darwin" else "KiB")
                if receipt["peak_rss_bytes"] > receipt["rss_limit_bytes"]:
                    outcome = "INCOMPLETE"
                    receipt["failures"].append({
                        "phase": "settlement", "type": "ResourceLimit",
                        "message": "measured_RSS_exceeds_256_MiB",
                    })
            if latch[0] != 0:
                outcome = "INCOMPLETE"
            if (clock is not None and started is not None
                    and clock.monotonic() - started >= 55.0):
                outcome = "INCOMPLETE"
                receipt["failures"].append({
                    "phase": "settlement", "type": "ResourceLimit",
                    "message": "elapsed_exceeds_55_seconds",
                })
        except BaseException as exc:
            outcome = "ERROR"
            receipt["failures"].append({
                "phase": "receipt_settlement",
                "type": type(exc).__name__, "message": str(exc),
            })

    try:
        if (not receipt["complete"] or receipt["failures"]
                or latch[0] != 0) and outcome == "PASS":
            outcome = "INCOMPLETE"
        receipt["status"] = outcome
        if jsonmod is None:
            import json as jsonmod
        payload = jsonmod.dumps(receipt, sort_keys=True, allow_nan=False)
        if resmod is not None and sysmod is not None:
            native_rss = resmod.getrusage(resmod.RUSAGE_SELF).ru_maxrss
            multiplier = 1 if sysmod.platform == "darwin" else 1024
            receipt["peak_rss_native"] = native_rss
            receipt["peak_rss_bytes"] = int(native_rss * multiplier)
            if receipt["peak_rss_bytes"] > receipt["rss_limit_bytes"]:
                receipt["status"] = "INCOMPLETE"
                receipt["failures"].append({
                    "phase": "serialization_settlement", "type": "ResourceLimit",
                    "message": "measured_RSS_exceeds_256_MiB",
                })
        if latch[0] != 0:
            receipt["signal_latched"] = int(latch[0])
            receipt["status"] = "INCOMPLETE"
        if clock is not None and started is not None:
            receipt["elapsed_before_emit_seconds"] = clock.monotonic() - started
            if receipt["elapsed_before_emit_seconds"] >= 55.0:
                receipt["status"] = "INCOMPLETE"
        payload = jsonmod.dumps(receipt, sort_keys=True, allow_nan=False)
        print(payload, flush=True)
        if latch[0] != 0:
            return 2
        if (clock is not None and started is not None
                and clock.monotonic() - started > 55.0):
            return 2
        return 0 if receipt["status"] == "PASS" else 2
    except BaseException:
        try:
            print('{"status":"ERROR","complete":false,'
                  '"reason":"receipt_serialization_or_stdout_failed"}', flush=True)
        except BaseException:
            pass
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
