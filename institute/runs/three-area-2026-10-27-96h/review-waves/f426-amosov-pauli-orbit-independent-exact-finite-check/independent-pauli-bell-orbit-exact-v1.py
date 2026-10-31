from fractions import Fraction as F
from itertools import combinations, permutations, product
from time import monotonic
DEADLINE = monotonic() + 50
class AuditError(Exception):
    def __init__(self, tag, detail=""):
        self.tag = tag
        super().__init__(tag + ": " + detail)
def need(condition, tag, detail=""):
    if monotonic() > DEADLINE:
        raise AuditError("deadline", "cooperative 50-second bound")
    if not condition:
        raise AuditError(tag, detail)
def mat(rows):
    return [[F(x) for x in row] for row in rows]
def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]
def unit(n, i, j):
    return [[F(a == i and b == j) for b in range(n)] for a in range(n)]
def transpose(A):
    return [list(row) for row in zip(*A)]
def flat(A):
    return [x for row in A for x in row]
def scale(t, A):
    return [[F(t) * x for x in row] for row in A]
def add(A, B):
    return [[x + y for x, y in zip(a, b)] for a, b in zip(A, B)]
def mm(A, B):
    cols = transpose(B)
    return [[sum((x * y for x, y in zip(row, col)), F(0)) for col in cols] for row in A]
def mv(A, v):
    return tuple(sum((x * y for x, y in zip(row, v)), F(0)) for row in A)
def dot(v, w):
    return sum((x * y for x, y in zip(v, w)), F(0))
def outer(v):
    return [[x * y for y in v] for x in v]
def rho(v):
    return scale(1 / dot(v, v), outer(v))
def trace(A):
    return sum((A[i][i] for i in range(len(A))), F(0))
def diag(values):
    return [[values[i] if i == j else F(0) for j in range(len(values))] for i in range(len(values))]
def kron(A, B):
    return [[A[i][j] * B[k][l] for j in range(len(A[0])) for l in range(len(B[0]))] for i in range(len(A)) for k in range(len(B))]
def rank(A):
    a = mat(A)
    r = 0
    for c in range(len(a[0])):
        if r == len(a):
            break
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        divisor = a[r][c]
        a[r] = [x / divisor for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [x - factor * y for x, y in zip(a[i], a[r])]
        r += 1
    return r
def determinant(A):
    n = len(A)
    answer = F(0)
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = F((-1) ** inversions)
        for i, j in enumerate(perm):
            term *= A[i][j]
        answer += term
    return answer
def state(A):
    need(trace(A) == 1, "trace", str(trace(A)))
    need(A == transpose(A), "hermiticity", "real-matrix checker")
    for size in range(1, len(A) + 1):
        for indices in combinations(range(len(A)), size):
            minor = [[A[i][j] for j in indices] for i in indices]
            need(determinant(minor) >= 0, "positivity", str(indices))
def gram(vectors, norm_squared):
    return [[dot(v, w) / norm_squared for w in vectors] for v in vectors]
I = eye(2)
OPS = [I, mat([[1, 0], [0, -1]]), mat([[0, 1], [1, 0]]), mat([[0, -1], [1, 0]])]
G = tuple(range(4))
T = (0, 1)
def projective(ops):
    need(ops[0] == I, "identity")
    for A in ops:
        need(mm(transpose(A), A) == I, "unitarity")
    omega = {}
    for i, j in product(G, repeat=2):
        actual = mm(ops[i], ops[j])
        target = ops[i ^ j]
        if actual == target:
            omega[i, j] = 1
        elif actual == scale(-1, target):
            omega[i, j] = -1
        else:
            raise AuditError("projective_product", str((i, j)))
    for i, j, k in product(G, repeat=3):
        need(omega[i, j] * omega[i ^ j, k] == omega[i, j ^ k] * omega[j, k], "cocycle")
    for i, j in product(T, repeat=2):
        need(omega[i, j] == 1, "ordinary_T")
    return omega
def product_rule(ops, omega):
    for i, j in product(G, repeat=2):
        need(mm(ops[i], ops[j]) == scale(omega[i, j], ops[i ^ j]), "product_rule", str((i, j)))
def check_weights(w):
    need(len(w) == 4 and sum(w, F(0)) == 1 and all(x >= 0 for x in w), "weights")
def cosets(w):
    check_weights(w)
    need(w[0] + w[1] >= w[2] + w[3], "coset_order")
    need(all(w[j] <= w[i] for i in (0, 1) for j in (2, 3)), "coset_order")
def weights(eta):
    need(0 <= eta <= 1, "noise_range")
    return (1 - 3 * eta / 4, eta / 4, eta / 4, eta / 4)
def mix(A, w, ops):
    local_ops = ops if len(A) == 2 else [kron(I, U) for U in ops]
    answer = scale(0, A)
    for weight, U in zip(w, local_ops):
        answer = add(answer, scale(weight, mm(mm(U, A), transpose(U))))
    return answer
def partial_trace_H(A):
    return [[sum((A[2 * a + h][2 * b + h] for h in range(2)), F(0)) for b in range(2)] for a in range(2)]
def channel_formula(A, eta):
    if len(A) == 2:
        noise = scale(eta * trace(A) / 2, I)
    else:
        noise = scale(eta / 2, kron(partial_trace_H(A), I))
    return add(scale(1 - eta, A), noise)
def partial_transpose_H(A):
    return [[A[2 * (i // 2) + j % 2][2 * (j // 2) + i % 2] for j in range(4)] for i in range(4)]
def majorized(a, b):
    a, b = tuple(sorted(a, reverse=True)), tuple(sorted(b, reverse=True))
    need(len(a) == len(b) and sum(a, F(0)) == sum(b, F(0)) == 1, "majorization")
    need(all(x >= 0 for x in a + b), "majorization")
    slacks = tuple(sum(b[:k], F(0)) - sum(a[:k], F(0)) for k in range(1, len(a) + 1))
    need(all(x >= 0 for x in slacks), "majorization", str(slacks))
    return slacks
def reject(label, expected_tag, operation):
    try:
        operation()
    except AuditError as exc:
        need(exc.tag == expected_tag, "wrong_rejection", label + ": " + str(exc))
        print("REJECT", label, expected_tag)
    else:
        raise AuditError("missed_mutation", label)
omega = projective(OPS)
canonical = {(i, j): (-1) ** ((i & 1) * ((j >> 1) & 1)) for i, j in product(G, repeat=2)}
product_rule(OPS, canonical)
need(omega == canonical, "canonical_cocycle")
need({i ^ j for i in T for j in T} == set(T), "subgroup")
need(all((g ^ t ^ g) in T for g in G for t in T), "normal_subgroup")
need(set(T).isdisjoint({2 ^ t for t in T}) and set(T) | {2 ^ t for t in T} == set(G), "coset_partition")
need(rank([flat(U) for U in OPS]) == 4, "operator_basis")
need(len({tuple(flat(scale(s, U))) for s in (-1, 1) for U in OPS}) == 8, "signed_group")
units2 = [unit(2, i, j) for i, j in product(range(2), repeat=2)]
constraints = []
for U in OPS:
    columns = [flat(add(mm(E, U), scale(-1, mm(U, E)))) for E in units2]
    constraints.extend(transpose(columns))
need(rank(constraints) == 3, "commutant_dimension")
need(all(mm(I, U) == mm(U, I) for U in OPS), "commutant_identity")
vP = tuple(map(F, (1, 0, 0, 0)))
vB = tuple(map(F, (1, 0, 0, 1)))
VP = [mv(kron(I, U), vP) for U in OPS]
VB = [mv(kron(I, U), vB) for U in OPS]
GP, GB = gram(VP, F(1)), gram(VB, F(2))
need(GP == mat([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]), "product_gram")
need(GB == eye(4), "bell_gram")
need(rank(GP) == rank(VP) == 2, "product_orbit_rank")
need(rank(GB) == rank(VB) == 4, "bell_orbit_rank")
rP, rB = rho(vP), rho(vB)
state(rP)
state(rB)
need(rank(rP) == rank(rB) == 1, "pure_inputs")
print("CHECKED group, cocycle, ordinary T, operator basis, and scalar commutant")
print("Product normalized Gram:", GP)
print("Bell normalized Gram:", GB)
formula_checks = 0
for eta in (F(0), F(1, 2), F(1)):
    w = weights(eta)
    cosets(w)
    for n in (2, 4):
        for i, j in product(range(n), repeat=2):
            E = unit(n, i, j)
            need(mix(E, w, OPS) == channel_formula(E, eta), "matrix_unit_formula", str((eta, n, i, j)))
            formula_checks += 1
    single = mix(unit(2, 0, 0), w, OPS)
    state(single)
    need(single[0][1] == single[1][0] == 0, "actual_q_diagonal")
    q = (single[0][0], single[1][1])
    need(q == (1 - eta / 2, eta / 2), "actual_q")
    qpad = q + (F(0), F(0))
    outP, outB = mix(rP, w, OPS), mix(rB, w, OPS)
    state(outP)
    state(outB)
    need(outP == diag(qpad), "product_output")
    need(outP == channel_formula(rP, eta) and outB == channel_formula(rB, eta), "state_formula")
    for eigenvalue, eigenvector in zip(w, VB):
        need(mv(outB, eigenvector) == tuple(eigenvalue * x for x in eigenvector), "bell_eigenpair")
    need(rank(outP) == (1 if eta == 0 else 2), "product_output_rank")
    need(rank(outB) == (1 if eta == 0 else 4), "bell_output_rank")
    need(majorized(qpad, qpad) == (F(0),) * 4, "product_majorization")
    slacks = majorized(w, qpad)
    need(slacks == (eta / 4, eta / 2, eta / 4, F(0)), "bell_partial_sums")
    print("eta =", eta, "actual q =", q, "product spectrum =", qpad, "Bell spectrum =", w, "Bell slacks =", slacks)
    if eta == F(1, 2):
        print("Bell midpoint output:", outB)
need(formula_checks == 60, "formula_check_count")
mid_weights = weights(F(1, 2))
mid = mix(rB, mid_weights, OPS)
reject("wrong_Bell_orbit_rank_two", "orbit_rank", lambda: need(rank(GB) == 2, "orbit_rank"))
all_plus = {(i, j): 1 for i, j in product(G, repeat=2)}
reject("ignored_projective_signs", "product_rule", lambda: product_rule(OPS, all_plus))
duplicate = OPS[:3] + [OPS[2]]
reject("duplicated_X_in_place_of_XZ", "projective_product", lambda: projective(duplicate))
bad_trace_weights = (F(1, 2), F(1, 8), F(1, 8), F(1, 8))
reject("subnormalized_weights", "trace", lambda: state(mix(rB, bad_trace_weights, OPS)))
bad_coset_weights = (F(5, 8), F(0), F(1, 4), F(1, 8))
check_weights(bad_coset_weights)
state(mix(rB, bad_coset_weights, OPS))
reject("interlaced_coset_weights", "coset_order", lambda: cosets(bad_coset_weights))
wrong_qpad = (F(1, 2), F(1, 2), F(0), F(0))
reject("incorrect_single_output_bound", "majorization", lambda: majorized(mid_weights, wrong_qpad))
pt = partial_transpose_H(mid)
need(trace(pt) == 1, "partial_transpose_trace_control")
need(determinant([[pt[1][1], pt[1][2]], [pt[2][1], pt[2][2]]]) == F(-3, 64), "partial_transpose_minor")
reject("partial_transpose_as_local_channel", "positivity", lambda: state(pt))
gauge = OPS[:3] + [scale(-1, OPS[3])]
projective(gauge)
need(rank([flat(U) for U in gauge]) == 4, "gauge_operator_basis")
need(mix(rB, mid_weights, gauge) == mid, "gauge_channel_invariance")
print("ACCEPT legitimate sign-gauge change with adjusted cocycle")
print("All exact checks and intended-reason controls completed.")
