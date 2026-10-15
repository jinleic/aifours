#!/usr/bin/env python3
"""Finite controls for RESULTS.md; not a numerical proof of universality.

One infinite bounded-digit word is enclosed by one exact rational CF cylinder
per fixture. All pivots use that same enclosure. No random search or imports
from another project. Run without --write to avoid rewriting the receipt.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import time

import mpmath as mp
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
LEVELS = (6, 10, 14)
ENCLOSURE_STAGE = 24
WINDOWS = (128, 512, 2048)
COEFFICIENTS = tuple((i, j) for i in range(-2, 3) for j in range(-2, 3))


@dataclass(frozen=True)
class PeriodicDigits:
    prefix: tuple[int, ...]
    period: tuple[int, ...]

    def take(self, count: int) -> list[int]:
        out = list(self.prefix[:count])
        while len(out) < count:
            out.append(self.period[(len(out) - len(self.prefix)) % len(self.period)])
        return out

    @property
    def bound(self) -> int:
        return max(self.prefix + self.period)


def periodic_digits(value: sp.Expr, discriminant: int) -> PeriodicDigits:
    """Exact quadratic conversion, independently checked by CF reconstruction."""
    value = sp.expand(sp.radsimp(value))
    root = sp.sqrt(discriminant)
    radical = value.coeff(root)
    rational = sp.simplify(value - radical * root)
    assert rational.is_Rational and radical.is_Rational and radical != 0
    denominator = int(sp.ilcm(sp.denom(rational), sp.denom(radical)))
    cf = sp.continued_fraction_periodic(
        int(rational * denominator), denominator, discriminant,
        int(radical * denominator),
    )
    assert cf[0] == 0 and isinstance(cf[-1], list) and cf[-1]
    assert sp.simplify(sp.continued_fraction_reduce(cf) - value) == 0
    digits = PeriodicDigits(tuple(map(int, cf[1:-1])), tuple(map(int, cf[-1])))
    assert all(d >= 1 for d in digits.prefix + digits.period)
    return digits


def convergents(digits: list[int]) -> list[tuple[int, int]]:
    p_old, p, q_old, q = 1, 0, 0, 1
    out = [(p, q)]
    for digit in digits:
        p_old, p = p, digit * p + p_old
        q_old, q = q, digit * q + q_old
        out.append((p, q))
    return out


def word_prefix(r: PeriodicDigits, u: PeriodicDigits, a: int,
                stages: int, *, reverse_history: bool = True
                ) -> tuple[list[int], dict[int, int]]:
    left, right = r.take(stages), u.take(stages)
    word: list[int] = []
    pivots: dict[int, int] = {}
    for k in range(1, stages + 1):
        if (len(word) + k) % 2:
            word.append(1)
        history = left[:k]
        word.extend(reversed(history) if reverse_history else history)
        pivots[k] = len(word)
        assert pivots[k] % 2 == 0
        word.append(a)
        word.extend(right[:k])
    return word, pivots


def cylinder(conv: list[tuple[int, int]]) -> tuple[Fraction, Fraction]:
    p, q = conv[-1]
    p_old, q_old = conv[-2]
    return tuple(sorted((Fraction(p, q), Fraction(p + p_old, q + q_old))))


def mp_fraction(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def mp_symbolic(value: sp.Expr) -> mp.mpf:
    return mp.mpf(str(sp.N(value, mp.mp.dps)))


def norm(vector: tuple[mp.mpf, mp.mpf]) -> mp.mpf:
    return mp.sqrt(vector[0] ** 2 + vector[1] ** 2)


def determinant(columns: tuple[tuple[mp.mpf, mp.mpf],
                               tuple[mp.mpf, mp.mpf]]) -> mp.mpf:
    v, w = columns
    return v[0] * w[1] - v[1] * w[0]


def integer_basis_check(p: int, q: int, pp: int, qq: int) -> None:
    if q * pp - qq * p != 1:
        raise ValueError("not the required positively oriented unimodular input basis")


def phase(index: int, alpha: Fraction) -> mp.mpf:
    # Integer reduction before conversion avoids large floating arguments.
    return mp.mpf((index * alpha.numerator) % alpha.denominator) / alpha.denominator


def point(index: int, alpha: Fraction) -> mp.mpc:
    assert index >= 1
    return mp.sqrt(index) * mp.exp(2j * mp.pi * phase(index, alpha))


def circular_distance(x: mp.mpf, y: mp.mpf) -> mp.mpf:
    return abs((x - y + mp.mpf("0.5")) % 1 - mp.mpf("0.5"))


def phase_window(n: int, alpha: Fraction, target: mp.mpf,
                 offsets: list[mp.mpf], maximum: int) -> dict:
    orbit = offsets[:maximum + 1]
    ordered = sorted(orbit)
    gap = max([ordered[i + 1] - ordered[i] for i in range(len(ordered) - 1)]
              + [1 + ordered[0] - ordered[-1]])
    base = phase(n, alpha)
    chosen = min(range(maximum + 1),
                 key=lambda b: circular_distance(base + orbit[b], target))
    error = circular_distance(base + orbit[chosen], target)
    assert error <= gap / 2 + mp.mpf("1e-60")
    return {"maximum_offset": maximum, "chosen_offset": chosen,
            "phase_error_turns": error, "orbit_maximum_gap_turns": gap}


def summarize_number(value: mp.mpf) -> str:
    return mp.nstr(value, 18)


def fraction_record(value: Fraction) -> dict:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def fixture(name: str, x: sp.Expr, h_squared: sp.Expr,
            beta: sp.Expr, discriminant: int, fixture_index: int) -> dict:
    a = int(sp.floor(beta))
    r = sp.simplify(beta - a)
    u = sp.radsimp(h_squared / (beta - x) - x)
    assert bool(beta > 1) and bool(u > 0) and bool(u < 1)
    assert sp.simplify((beta - x) * (u + x) - h_squared) == 0
    r_digits, u_digits = periodic_digits(r, discriminant), periodic_digits(u, discriminant)
    alphabet_bound = max(1, a, r_digits.bound, u_digits.bound)
    word, pivots = word_prefix(r_digits, u_digits, a, ENCLOSURE_STAGE)
    assert max(word) <= alphabet_bound
    conv = convergents(word)
    lo, hi = cylinder(conv)
    alpha_mid, alpha_radius = (lo + hi) / 2, (hi - lo) / 2
    max_q_digits = max(len(str(conv[pivots[k] + 1][1])) for k in LEVELS)
    mp.mp.dps = 2 * max_q_digits + 100
    tiny = mp.mpf("1e-60")
    beta_mp, u_mp, r_mp = map(mp_symbolic, (beta, u, r))
    x_mp, h = mp_symbolic(x), mp.sqrt(mp_symbolic(h_squared))
    t = (beta_mp - x_mp) / h
    A = mp.sqrt(mp.pi / h) / mp.sqrt(1 + t * t)
    C = t * A
    target = ((A, C), (A * beta_mp, -C * u_mp))
    assert A > 0 and C > 0 and abs(determinant(target) + mp.pi) < tiny
    target_scale = max(mp.mpf(1), norm(target[0]), norm(target[1]))
    target_angle = mp.mpf(37 + 19 * fixture_index) / 100
    target_turn = target_angle / (2 * mp.pi)
    target_rotation = mp.exp(1j * target_angle)
    offsets = [phase(b, alpha_mid) for b in range(WINDOWS[-1] + 1)]
    records = []
    max_local_ratio = mp.mpf(0)
    max_reverse_ratio = mp.mpf(0)
    for k in LEVELS:
        j = pivots[k]
        p, q = conv[j]
        pp, qq = conv[j + 1]
        integer_basis_check(p, q, pp, qq)
        assert word[j] == a
        assert list(reversed(word[j - k:j])) == r_digits.take(k)
        assert word[j + 1:j + 1 + k] == u_digits.take(k)
        _, q_previous = conv[j - 1]
        rj = Fraction(q_previous, q)
        betaj = Fraction(qq, q)
        error_j = q * alpha_mid - p
        error_next = qq * alpha_mid - pp
        assert error_j > 0 and error_next < 0
        uj = -error_next / error_j
        cj = q * error_j
        assert cj == 1 / (betaj + uj)
        qr = convergents(r_digits.take(k))[-1][1]
        qu = convergents(u_digits.take(k))[-1][1]
        assert abs(mp_fraction(rj) - r_mp) <= mp.mpf(1) / qr ** 2 + tiny
        assert abs(mp_fraction(uj) - u_mp) <= mp.mpf(1) / qu ** 2 + tiny
        n = int(mp.nint((mp.mpf(q) / (2 * A)) ** 2))
        assert n >= 1
        # Exact cylinder control for the SINGLE infinite alpha used at all pivots.
        phase_uncertainty_turns = (n + WINDOWS[-1]) * alpha_radius
        assert phase_uncertainty_turns < Fraction(1, 10 ** 40)
        choices = [phase_window(n, alpha_mid, target_turn, offsets, H) for H in WINDOWS]
        b = choices[-1]["chosen_offset"]
        m = n + b
        rho = mp.sqrt(m)
        columns = ((mp.mpf(q) / (2 * rho), 2 * mp.pi * rho * mp_fraction(error_j)),
                   (mp.mpf(qq) / (2 * rho), 2 * mp.pi * rho * mp_fraction(error_next)))
        assert abs(determinant(columns) + mp.pi) < tiny
        relative_basis_error = max(norm((columns[c][0] - target[c][0],
                                         columns[c][1] - target[c][1]))
                                   for c in (0, 1)) / target_scale
        vectors = [(i * columns[0][0] + j2 * columns[1][0],
                    i * columns[0][1] + j2 * columns[1][1]) for i, j2 in COEFFICIENTS]
        R = max(mp.mpf(1), *(norm(v) for v in vectors))
        reverse_R = R + 1
        assert rho >= 12 * reverse_R
        forward_bound = 5 * R * R / rho
        reverse_bound = 45 * reverse_R * reverse_R / rho
        rotation = mp.exp(2j * mp.pi * phase(m, alpha_mid))
        origin = point(m, alpha_mid)
        max_physical_error = mp.mpf(0)
        for (i, j2), vector in zip(COEFFICIENTS, vectors):
            index_difference = i * q + j2 * qq
            nearest = i * p + j2 * pp
            assert m + index_difference >= 1
            actual = point(m + index_difference, alpha_mid) - origin
            predicted = rotation * mp.mpc(*vector)
            local_error = abs(actual - predicted)
            assert local_error <= forward_bound * (1 + mp.mpf("1e-30"))
            max_local_ratio = max(max_local_ratio, local_error / forward_bound)
            local_actual = actual / rotation
            assert abs(local_actual) <= reverse_R
            # Recover the inverse correspondence from the actual complex points,
            # not by handing the model its original q,p pair.
            recovered_q_real = abs(rho + local_actual) ** 2 - m
            recovered_q = int(mp.nint(recovered_q_real))
            assert recovered_q == index_difference
            principal = mp.arg(rho + local_actual)
            recovered_p = int(mp.nint(mp_fraction(recovered_q * alpha_mid)
                                      - principal / (2 * mp.pi)))
            assert recovered_p == nearest
            recovered = mp.mpc(mp.mpf(recovered_q) / (2 * rho),
                               2 * mp.pi * rho * mp_fraction(recovered_q * alpha_mid - recovered_p))
            reverse_error = abs(local_actual - recovered)
            assert abs(recovered) < 3 * reverse_R
            assert reverse_error <= reverse_bound * (1 + mp.mpf("1e-30"))
            max_reverse_ratio = max(max_reverse_ratio, reverse_error / reverse_bound)
            target_vector = mp.mpc(i * target[0][0] + j2 * target[1][0],
                                   i * target[0][1] + j2 * target[1][1])
            physical_error = abs(actual - target_rotation * target_vector)
            triangle_bound = (forward_bound + abs(mp.mpc(*vector) - target_vector)
                              + abs(rotation - target_rotation) * abs(target_vector))
            assert physical_error <= triangle_bound + tiny
            max_physical_error = max(max_physical_error, physical_error)
        choices_json = [{key: (summarize_number(value) if isinstance(value, mp.mpf) else value)
                         for key, value in choice.items()} for choice in choices]
        records.append({"stage": k, "pivot_j": j, "q_j": str(q), "q_next": str(qq),
                        "n": str(n), "m": str(m),
                        "phase_uncertainty_turns_upper": fraction_record(phase_uncertainty_turns),
                        "relative_basis_error": summarize_number(relative_basis_error),
                        "max_physical_patch_error": summarize_number(max_physical_error),
                        "phase_windows": choices_json})
        if k == LEVELS[-1]:
            assert relative_basis_error < mp.mpf("1e-4")
    # Three negative-control families, distinct from normal positive assertions.
    wrong_columns = tuple((column[0], column[1] / mp.pi) for column in columns)
    wrong_area = abs(determinant(wrong_columns))
    assert abs(wrong_area - mp.pi) > 1  # mutated 2*pi*rho -> 2*rho gives area 1
    try:
        integer_basis_check(p, q, 2 * pp, 2 * qq)
    except ValueError:
        index_two_rejected = True
    else:
        raise AssertionError("index-two input passed the basis check")
    wrong_word, wrong_pivots = word_prefix(r_digits, u_digits, a, LEVELS[-1],
                                           reverse_history=False)
    wrong_conv = convergents(wrong_word)
    wrong_j = wrong_pivots[LEVELS[-1]]
    wrong_r = Fraction(wrong_conv[wrong_j - 1][1], wrong_conv[wrong_j][1])
    reversal_error = abs(mp_fraction(wrong_r) - r_mp)
    return {"name": name, "x": str(x), "h_squared": str(h_squared),
            "beta": str(beta), "u": str(u), "a": a,
            "r_cf": {"prefix": list(r_digits.prefix), "period": list(r_digits.period)},
            "u_cf": {"prefix": list(u_digits.prefix), "period": list(u_digits.period)},
            "alphabet_bound": alphabet_bound,
            "word_prefix": word, "enclosure_stage": ENCLOSURE_STAGE,
            "alpha_lower": fraction_record(lo), "alpha_upper": fraction_record(hi),
            "decimal_precision": mp.mp.dps,
            "target_rotation_radians": summarize_number(target_angle),
            "records": records,
            "max_forward_error_over_bound": summarize_number(max_local_ratio),
            "max_reverse_error_over_bound": summarize_number(max_reverse_ratio),
            "negative_controls": {"wrong_pi_factor_rejected": True,
                                  "index_two_rejected": index_two_rejected,
                                  "unreversed_history_ratio_error": summarize_number(reversal_error)}}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write results/smoke.json")
    args = parser.parse_args()
    started = time.monotonic()
    golden = (1 + sp.sqrt(5)) / 2
    definitions = (
        ("square", sp.Integer(0), sp.Integer(1), golden, 5),
        ("rectangle", sp.Integer(0), sp.Integer(9), 9 + golden, 5),
        ("hexagonal", sp.Rational(1, 2), sp.Rational(3, 4), sp.sqrt(3), 3),
        ("skew", sp.Rational(1, 3), sp.Rational(5, 4), (1 + sp.sqrt(15)) / 2, 15),
    )
    examples = [fixture(*definition, i) for i, definition in enumerate(definitions)]
    reversal_detections = sum(mp.mpf(e["negative_controls"]["unreversed_history_ratio_error"])
                             > mp.mpf("1e-2") for e in examples)
    assert reversal_detections >= 1
    payload = {"status": "PASS", "evidence_label": "Empirical evidence",
               "universal_proof": "RESULTS.md sections1-6; finite computation is not its substitute",
               "same_infinite_angle": "Each fixture encloses one fixed infinite bounded word in an exact CF cylinder",
               "floating_point_scope": "High precision is not a formal interval or proof-kernel certificate",
               "protocol": {"levels": LEVELS, "enclosure_stage": ENCLOSURE_STAGE,
                            "maximum_phase_offsets": WINDOWS, "patch_coefficients": [-2, 2]},
               "counts": {"quadratic_fixtures": len(examples),
                          "pivot_bases": len(examples) * len(LEVELS),
                          "forward_patch_checks": len(examples) * len(LEVELS) * len(COEFFICIENTS),
                          "reverse_patch_checks": len(examples) * len(LEVELS) * len(COEFFICIENTS),
                          "phase_window_checks": len(examples) * len(LEVELS) * len(WINDOWS),
                          "negative_control_families": 3,
                          "unreversed_history_detections": reversal_detections},
               "versions": {"python": platform.python_version(), "sympy": sp.__version__,
                            "mpmath": mp.__version__},
               "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "elapsed_seconds": round(time.monotonic() - started, 3), "examples": examples}
    if args.write:
        path = ROOT / "results" / "smoke.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2) + "\n")
    print("PASS: 4 quadratic fixtures; 12 bounded-word convergent bases; fixed infinite alpha cylinders")
    print("PASS: 300 forward and 300 reverse spiral-patch checks; 36 phase-window checks")
    print("PASS: 3 negative-control families (pi normalization, digit history, index-two basis)")
    for example in examples:
        print(f"{example['name']}: M={example['alphabet_bound']}, final relative basis error="
              f"{example['records'][-1]['relative_basis_error']}")
    print(f"Elapsed: {payload['elapsed_seconds']} s")


if __name__ == "__main__":
    main()
