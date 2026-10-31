import sys  
import time  
from fractions import Fraction as F  
  
started = time.monotonic()  
  
def need(condition, message):  
    if not condition:  
        raise ValueError(message)  
  
def emit(name, value):  
    print(str(name) + " = " + str(value))  
  
need(len(sys.argv) == 8, "Expected T tau delta q theta r N")  
values = tuple(F(x) for x in sys.argv[1:7])  
need(all(max(abs(x.numerator).bit_length(),  
             x.denominator.bit_length()) <= 32  
         for x in values), "Input fraction exceeds finite bound")  
T, tau, delta, q, theta, r = values  
N = int(sys.argv[7])  
need(1 <= N <= 8, "N outside this finite calculator's scope")  
need(T > 0 and tau > 0 and delta > 0, "Positive times required")  
need(0 < theta < 1 and 0 < r < 1, "Interior weights required")  
H = max(F(0), T - tau)  
emit("execution scope", "Exact finite interfaces; no gain evaluation")  
emit("zero prehistory", "Assumed, not inferred from a scalar input")  
emit("H", H)  
if H == 0:  
    emit("zero-history output", "Zero on the stated horizon")  
    sys.exit(0)  
need(N * (tau + delta) < T, "Burst schedule exceeds horizon")  
need(delta <= q and q + delta <= H, "Rectangles must be disjoint and active")  
need(0 < q < H, "Two-atom time must be interior")  
emit("long-lag interface H <= tau", H <= tau)  
emit("N tau < T", N * tau < T)  
previous_applied_end = None  
for j in range(1, N + 1):  
    s = (j - 1) * (tau + delta)  
    t = s + tau  
    need(s + delta < H and t + delta < T, "Inactive burst")  
    if previous_applied_end is not None:  
        need(previous_applied_end == s, "Observation is not available at selection")  
    emit("burst " + str(j), (s, s + delta, t, t + delta))  
    previous_applied_end = t + delta  
emit("adjacent input gap", tau)  
emit("adjacent applied gap", tau)  
emit("own input/applied overlap length", max(F(0), delta - tau))  
emit("mutant input-two-at-delta observation deficit", tau)  
d = H - q  
alpha2 = d * d / H  
beta2 = q * d / H  
atom_trace = H - theta * q  
atom_det = theta * (1 - theta) * q * d  
c00 = (1 - theta) * H + theta * alpha2  
c11 = theta * beta2  
c01_squared = theta * theta * alpha2 * beta2  
need(c00 + c11 == atom_trace, "Covariance trace mismatch")  
need(c00 * c11 - c01_squared == atom_det > 0, "Covariance determinant mismatch")  
g00 = (1 - theta) * H  
g11 = theta * d  
g01_squared = theta * (1 - theta) * d * d  
need(g00 + g11 == atom_trace, "Gram trace mismatch")  
need(g00 * g11 - g01_squared == atom_det, "Gram determinant mismatch")  
emit("unweighted impulse Gram determinant", q * d)  
emit("two-atom covariance trace", atom_trace)  
emit("two-atom covariance determinant", atom_det)  
rectangles = ((F(0), delta, 1 - theta), (q, delta, theta))  
R = F(0)  
HS = F(0)  
V = F(0)  
comparison_error2 = F(0)  
for a, length, mass in rectangles:  
    distance = H - a  
    second = distance * distance - distance * length + length * length / 3  
    diagonal = distance * distance - F(4, 3) * distance * length + length * length / 2  
    R += mass * (distance - length / 2)  
    HS += mass * mass * diagonal  
    V += mass * second / H  
    comparison_error2 += mass * length / 2  
HS += 2 * (1 - theta) * theta * (d * d - d * delta + delta * delta / 3)  
need(R > 0 and 0 < V <= R, "Positive expected-norm bound unavailable")  
need(0 < HS < R * R, "Rectangular rank certificate failed")  
emit("rectangular covariance trace R", R)  
emit("rectangular covariance trace Q squared", HS)  
emit("rectangular projection variance V", V)  
emit("rectangular moving-atom squared error", comparison_error2)  
emit("expected-norm bounds", "sqrt(2/pi)*sqrt(R) < E norm < sqrt(R)")  
eta = r * r * delta  
normalized_increment_covariance = r  
normalized_increment_distance2 = 2 * (1 - r)  
output_inner_product = r * (H - eta / 2)  
output_distance2 = (H - delta / 2) + (H - eta / 2) - 2 * output_inner_product  
need(0 < eta < delta < H, "Nested widths outside active interval")  
need(normalized_increment_distance2 > 0 and output_distance2 > 0, "Nested-distance identity failed")  
emit("nested width eta", eta)  
emit("nested standardized-increment covariance", normalized_increment_covariance)  
emit("nested standardized-increment squared distance", normalized_increment_distance2)  
emit("actual scalar burst-output squared distance", output_distance2)  
emit("single-burst moving-comparison squared error", delta / 2)  
emit("fixed-normal convergence", "Not established; nested distances preclude it as widths shrink")  
emit("uncomputed quantities", "Gaussian expected norm, D_H, adapted gain, optimizer, attainment")  
if time.monotonic() - started > 55:  
    raise RuntimeError("Calculation exceeded prospective 55-second bound")  
