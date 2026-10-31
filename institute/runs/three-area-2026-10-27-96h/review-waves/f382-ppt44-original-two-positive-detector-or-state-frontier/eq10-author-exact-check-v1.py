from fractions import Fraction as Q
from itertools import combinations
from time import monotonic
started = monotonic()
def require(ok, message):
  if not ok:
    raise RuntimeError(message)
  if monotonic() - started > 55:
    raise RuntimeError("INCOMPLETE: cooperative deadline reached")
def zero(n):
  return [[Q(0) for _ in range(n)] for _ in range(n)]
def eye(n):
  A = zero(n)
  for i in range(n):
    A[i][i] = Q(1)
  return A
def unit(i, j):
  A = zero(4)
  A[i][j] = Q(1)
  return A
def scale(A, s):
  return [[s * x for x in row] for row in A]
def multiply(A, B):
  n = len(A)
  return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def charpoly(A):
  n = len(A)
  B = eye(n)
  coefficients = [Q(1)]
  for k in range(1, n + 1):
    AB = multiply(A, B)
    c = -sum(AB[i][i] for i in range(n)) / k
    coefficients.append(c)
    B = [[AB[i][j] + (c if i == j else Q(0)) for j in range(n)] for i in range(n)]
  return coefficients
def determinant(A):
  if not A:
    return Q(1)
  return (-1) ** len(A) * charpoly(A)[-1]
def submatrix(A, indices):
  return [[A[i][j] for j in indices] for i in indices]
def psd_by_principal_minors(A):
  n = len(A)
  for size in range(1, n + 1):
    for indices in combinations(range(n), size):
      if determinant(submatrix(A, indices)) < 0:
        return False
  return True
def phi(A):
  B = [row[:] for row in A]
  for i in range(4):
    B[i][i] = sum(A[j][j] for j in range(4) if j != (i - 1) % 4)
  B[2][3] = A[3][2]
  B[3][2] = A[2][3]
  return scale(B, Q(1, 3))
def depolarizing(A):
  return scale(eye(4), sum(A[i][i] for i in range(4)))
def repaired(A, S, delta):
  B = phi(A)
  tr = sum(A[i][i] for i in range(4))
  return [[B[i][j] + S[i][j] * A[i][j] + (delta * tr if i == j else Q(0)) for j in range(4)] for i in range(4)]
def choi_images(images):
  C = zero(16)
  for i in range(4):
    for j in range(4):
      Y = images[4 * i + j]
      for a in range(4):
        for b in range(4):
          C[4 * i + a][4 * j + b] = Y[a][b]
  return C
def choi(operation):
  return choi_images([operation(unit(i, j)) for i in range(4) for j in range(4)])
def quadratic(C, v):
  return sum(v[i] * C[i][j] * v[j] for i in range(16) for j in range(16))
D = [0, 5, 10, 15]
Bpair = [11, 14]
omega = [Q(int(i in D)) for i in range(16)]
expected_identity_choi = [[omega[i] * omega[j] for j in range(16)] for i in range(16)]
require(choi(lambda A: A) == expected_identity_choi, "known-true identity Choi convention failed")
require(choi(depolarizing) == eye(16), "known-true depolarizing Choi convention failed")
M = [[Q(1) for _ in range(4)] for _ in range(4)]
M[2][3] = M[3][2] = Q(0)
require(charpoly(M) == [Q(1), Q(-4), Q(1), Q(2), Q(0)], "M characteristic polynomial mismatch")
require(charpoly([[Q(0), Q(1)], [Q(1), Q(1)]]) == [Q(1), Q(-1), Q(-1)], "pair characteristic polynomial mismatch")
C = choi(phi)
expected = zero(16)
for i in range(4):
  for j in range(4):
    expected[5 * i][5 * j] = M[i][j] / 3
    if i != j:
      expected[4 * i + j][4 * i + j] = Q(int(j != (i + 1) % 4), 3)
expected[11][14] = expected[14][11] = Q(1, 3)
require(C == expected, "literal Eq10 Choi block decomposition mismatch")
simple = [Q(0) for _ in range(16)]
simple[11], simple[14] = Q(1), Q(-1)
require(quadratic(C, simple) == Q(-1, 3), "original rank-two counterexample mismatch")
u = [Q(1), Q(2), Q(-1), Q(0)]
v = [Q(0), Q(1), Q(1), Q(2)]
Sgram = [[u[i] * u[j] + v[i] * v[j] for j in range(4)] for i in range(4)]
require(psd_by_principal_minors(Sgram), "selected Schur Gram matrix failed PSD check")
test_vector = [Q(0) for _ in range(16)]
test_vector[11], test_vector[14] = Q(1), Q(-3, 5)
for S in [zero(4), Sgram]:
  negative = choi(lambda A: repaired(A, S, Q(1, 5)))
  require(quadratic(negative, test_vector) == Q(-1, 125), "selected negative noise control mismatch")
  positive = choi(lambda A: repaired(A, S, Q(5, 24)))
  H = submatrix(positive, D)
  P = submatrix(positive, Bpair)
  require(determinant(P) == Q(1, 576), "selected positive pair determinant mismatch")
  require(psd_by_principal_minors(H), "selected positive correlated block failed")
  require(psd_by_principal_minors(P), "selected positive pair block failed")
  for a in range(16):
    if a not in D and a not in Bpair:
      require(positive[a][a] >= 0, "selected scalar block is negative")
    for b in range(16):
      same_block = (a in D and b in D) or (a in Bpair and b in Bpair)
      if a != b and not same_block:
        require(positive[a][b] == 0, "unexpected coupling between Choi blocks")
images = [unit(i, j) for i in range(4) for j in range(4)]
for n in range(13):
  actual = choi_images(images)
  sin_derivative = (0, 1, 0, -1)[n % 4]
  cos_derivative = (1, 0, -1, 0)[n % 4]
  population = [
    Q(3 ** n + 1 + 2 * cos_derivative, 4),
    Q(3 ** n - 1 - 2 * sin_derivative, 4),
    Q(3 ** n + 1 - 2 * cos_derivative, 4),
    Q(3 ** n - 1 + 2 * sin_derivative, 4),
  ]
  predicted = zero(16)
  for i in range(4):
    for j in range(4):
      predicted[4 * i + j][4 * i + j] = population[(j - i) % 4]
      if i != j:
        special = {i, j} == {2, 3}
        predicted[5 * i][5 * j] = Q(int(n % 2 == 0)) if special else Q(1)
  predicted[11][14] = predicted[14][11] = Q(n % 2)
  require(actual == predicted, "semigroup derivative matrix mismatch at order " + str(n))
  if n < 12:
    images = [scale(phi(A), Q(3)) for A in images]
require(True, "final cooperative deadline check")
print("Exact finite controls and coefficient checks through order 12 passed.")
print("Selected negative quadratic: -1/125")
print("Selected positive pair determinant: 1/576")
print("These finite checks do not prove the universal theorems or the original PPT/SN3 target.")
