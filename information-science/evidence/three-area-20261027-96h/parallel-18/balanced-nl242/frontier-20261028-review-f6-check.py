#!/usr/bin/env python3
"""Independently check the R-minus FD laws, decoder sets and exact inequalities."""

import argparse
import ast
import collections
import hashlib
import json
import math
import re
from pathlib import Path

NVERT = 10
SCALE_BITS = 192
TERMS = 80


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_hash(path, expected):
    actual = digest(path)
    if actual != expected:
        raise ValueError(f"input hash mismatch: {path}")
    return actual


def read_named_list(text, name):
    match = re.search(r"\b" + re.escape(name) + r"\s*=\s*\[(.*?)\]", text, re.S)
    if not match:
        raise ValueError(f"missing {name} list")
    result = ast.literal_eval("[" + match.group(1) + "]")
    if not isinstance(result, list) or any(type(v) is not int for v in result):
        raise ValueError(f"{name} must be integer list")
    return result


def registered_graph(text):
    rows = re.findall(r"(?m)^- N\((\d+)\) = \{([0-9, ]+)\}", text)
    if len(rows) != NVERT:
        raise ValueError("registered graph does not contain ten rows")
    graph = []
    for index, (v, neighbours) in enumerate(rows, 1):
        if int(v) != index:
            raise ValueError("registered vertex order mismatch")
        values = [int(x) for x in neighbours.split(",")]
        if len(values) != len(set(values)) or any(not 1 <= x <= NVERT or x == index for x in values):
            raise ValueError("invalid registered neighbour list")
        graph.append(frozenset(values))
    if any((u in graph[v - 1]) != (v in graph[u - 1]) for u in range(1, 11) for v in range(1, 11)):
        raise ValueError("registered graph is not symmetric")
    return graph


def candidate_edges(text):
    match = re.search(r"with edges:\s*```\s*(.*?)\s*```", text, re.S)
    if not match:
        raise ValueError("missing first-candidate edge block")
    edges = set()
    for token in match.group(1).split():
        if "-" in token:
            parts = token.split("-")
            if len(parts) != 2:
                raise ValueError("invalid edge token")
            a, b = map(int, parts)
        elif len(token) == 2 and token.isdigit():
            a, b = map(int, token)
        else:
            raise ValueError(f"invalid edge token {token}")
        if not 1 <= a < b <= NVERT or (a, b) in edges:
            raise ValueError("invalid or duplicate edge")
        edges.add((a, b))
    return edges


def candidate_graph_rows(text):
    match = re.search(r"one-based:\s*```\s*(.*?)\s*```", text, re.S)
    if not match:
        raise ValueError("missing second-candidate neighbourhood block")
    block = match.group(1)
    labels = list(re.finditer(r"\b(\d+):", block))
    graph = []
    for index, label in enumerate(labels, 1):
        if int(label.group(1)) != index:
            raise ValueError("second-candidate vertex order mismatch")
        end = labels[index].start() if index < len(labels) else len(block)
        graph.append(frozenset(map(int, block[label.end():end].split())))
    if len(graph) != NVERT:
        raise ValueError("second candidate must contain ten graph rows")
    return graph


def four_words(text):
    match = re.search(r"A\s*=\s*\{([^}]*)\},\s*B\s*=\s*\{([^}]*)\},\s*C\s*=\s*\{([^}]*)\},\s*D\s*=\s*\{([^}]*)\}", text)
    if not match:
        raise ValueError("missing four named words")
    words = []
    for field in match.groups():
        vertices = [int(x) for x in field.split(",")]
        if len(vertices) != len(set(vertices)) or any(not 1 <= x <= NVERT for x in vertices):
            raise ValueError("invalid vertex set")
        words.append(sum(1 << (v - 1) for v in vertices))
    return words


def validate_weights(words, weights):
    if len(words) != len(weights):
        raise ValueError("word/weight length mismatch")
    if any(type(w) is not int or w <= 0 for w in weights):
        raise ValueError("weights must be strictly positive integers")
    if len(set(words)) != len(words) or any(not 0 <= x < 1 << NVERT for x in words):
        raise ValueError("invalid or duplicate words")


def check_fd_and_full_decoders(words, graph):
    neighbours = [sum(1 << (u - 1) for u in row) for row in graph]
    tables = []
    for v, mask in enumerate(neighbours):
        table = {}
        for x in words:
            key = x & mask
            output = (x >> v) & 1
            if key in table and table[key] != output:
                raise ValueError(f"FD conflict at vertex {v + 1}")
            table[key] = output
        tables.append(table)
    winners = []
    for x in range(1 << NVERT):
        if all(tables[v].get(x & neighbours[v], 0) == ((x >> v) & 1) for v in range(NVERT)):
            winners.append(x)
    if set(winners) != set(words):
        raise ValueError("actual full-decoder winning set differs from support")
    return {"support_size": len(words), "full_domain_inputs": 1 << NVERT,
            "actual_winners": len(winners), "all_exact": True}


def ceil_div(a, b):
    return -(-a // b)


def log_ratio_interval(x, y):
    """Rigorous fixed-point enclosure of ln(x/y), for y<=x<=2y."""
    if not 0 < y <= x <= 2 * y:
        raise ValueError("log ratio outside certified range")
    n, d = x - y, x + y
    if n == 0:
        return 0, 0
    scale = 1 << SCALE_BITS
    nn, dd = n * n, d * d
    power_n, power_d = n, d
    low = 0
    for i in range(TERMS):
        low += (2 * scale * power_n) // ((2 * i + 1) * power_d)
        power_n *= nn
        power_d *= dd
    # Remaining series <= 2*u^(2m+1)/((2m+1)(1-u^2)).
    tail = ceil_div(2 * scale * power_n * dd,
                    (2 * TERMS + 1) * power_d * (dd - nn))
    return low, low + TERMS + tail


def log_int_interval(value):
    if value < 1:
        raise ValueError("log argument must be positive")
    power = value.bit_length() - 1
    lower2, upper2 = log_ratio_interval(2, 1)
    low, high = log_ratio_interval(value, 1 << power)
    return low + power * lower2, high + power * upper2


def exact_power_gap(weights):
    count = collections.Counter(weights)
    terms = [(649 * 3523, 3523), (649 * 2477, 2477), (-549 * 6000, 6000)]
    terms.extend((-100 * weight * multiplicity, weight) for weight, multiplicity in count.items())
    terms.append((-4448, 2))
    low = high = 0
    for coefficient, value in terms:
        left, right = log_int_interval(value)
        low += coefficient * (left if coefficient >= 0 else right)
        high += coefficient * (right if coefficient >= 0 else left)
    if low <= 0 or high < low:
        raise ValueError("rigorous log interval does not establish the claimed 2^4448 margin")
    return {"scale_power_of_two": SCALE_BITS, "series_terms": TERMS,
            "lower_scaled": str(low), "upper_scaled": str(high),
            "strictly_positive_lower": True, "method": "integer-rounded atanh-series enclosure"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--weighted", required=True, type=Path)
    parser.add_argument("--four", required=True, type=Path)
    parser.add_argument("--registered", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    hashes = {
        "weighted": require_hash(args.weighted, "d223232b8978a18bba5542fcdcdd133cbbc7f321ac057f8278850674b37d2f96"),
        "four": require_hash(args.four, "170be249faad78e9438338a2f36330d6e1a55217b2749d3e7be698a536bb1d17"),
        "registered": digest(args.registered),
    }
    text1 = args.weighted.read_text(encoding="utf-8")
    text2 = args.four.read_text(encoding="utf-8")
    graph = registered_graph(args.registered.read_text(encoding="utf-8"))
    edges = {(v, u) for v in range(1, 11) for u in graph[v - 1] if v < u}
    if len(edges) != 26 or (3, 4) not in edges or (9, 10) in edges:
        raise ValueError("registered R-minus edge structure mismatch")
    if candidate_edges(text1) != edges or candidate_graph_rows(text2) != graph:
        raise ValueError("candidate graph differs from registered neighbourhoods")
    words = read_named_list(text1, "words")
    weights = read_named_list(text1, "weights")
    validate_weights(words, weights)
    if len(words) != 88 or sum(weights) != 6000:
        raise ValueError("88-word support or 6000-weight total mismatch")
    weighted_game = check_fd_and_full_decoders(words, graph)
    counts = [sum(weight for word, weight in zip(words, weights) if word & (1 << v)) for v in range(NVERT)]
    expected = [3530, 2474, 3526, 2475, 2474, 2468, 2469, 3529, 2476, 3523]
    if counts != expected or min(range(NVERT), key=lambda i: abs(2 * counts[i] - 6000)) != 9:
        raise ValueError("weighted marginals or entropy-maximizer mismatch")
    uniform_counts = [sum(bool(word & (1 << v)) for word in words) for v in range(NVERT)]
    if uniform_counts != [48, 40, 48, 40, 44, 44, 40, 48, 44, 48]:
        raise ValueError("uniform marginal counts mismatch")
    exact_gap = exact_power_gap(weights)
    if not (2 ** 649 > 88 ** 100):
        raise ValueError("uniform comparison failed")
    if not (2 ** 444800 > 600001 ** 8800):
        raise ValueError("finite block logarithmic-loss bound failed")
    small = four_words(text2)
    if len(set(small)) != 4:
        raise ValueError("four-word support is not distinct")
    four_game = check_fd_and_full_decoders(small, graph)
    small_weights = [2, 2, 1, 1]
    small_counts = [sum(weight for word, weight in zip(small, small_weights) if word & (1 << v))
                    for v in range(NVERT)]
    if small_counts != [4, 2, 2, 1, 1, 0, 0, 0, 0, 0]:
        raise ValueError("four-word marginal counts mismatch")
    m = math.factorial(24) // (math.factorial(8) ** 2 * math.factorial(4) ** 2)
    q = math.comb(24, 8)
    if (m, q, m - q * q) != (662585823900, 735471, 121668232059):
        raise ValueError("finite four-word type-class arithmetic mismatch")
    if not (3 ** 3 < 2 ** 5):
        raise ValueError("four-word strict entropy inequality failed")
    # Intended-reason controls: duplicating a neighbour projection with the opposite own bit.
    altered = list(words)
    for v in range(NVERT):
        candidate = words[0] ^ (1 << v)
        if candidate not in words:
            altered.append(candidate)
            break
    try:
        check_fd_and_full_decoders(altered, graph)
    except ValueError as error:
        if not str(error).startswith("FD conflict at vertex "):
            raise RuntimeError("FD mutation rejected for wrong reason") from error
        fd_control = str(error)
    else:
        raise RuntimeError("single-vertex FD mutation was not rejected")
    bad_weights = list(weights)
    bad_weights[0] = 0
    try:
        validate_weights(words, bad_weights)
    except ValueError as error:
        if str(error) != "weights must be strictly positive integers":
            raise RuntimeError("weight mutation rejected for wrong reason") from error
    else:
        raise RuntimeError("zero-weight mutation was not rejected")
    result = {"hashes": hashes, "edges": len(edges), "registered_neighbourhoods": [sorted(row) for row in graph],
              "weighted_game": weighted_game, "weighted_marginals": counts, "uniform_marginals": uniform_counts,
              "log_gap_certificate": exact_gap, "uniform_integer_comparison": True,
              "finite_type_loss_integer_comparison": True, "four_game": four_game,
              "four_words": small, "four_weighted_marginals": small_counts,
              "small_type_class": {"M": m, "q": q, "M_minus_q_squared": m - q * q},
              "controls": {"fd_flip": fd_control, "zero_weight": "weights must be strictly positive integers"}}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
        file.write("\n")
    print(f"graph edges={len(edges)}; FD winners={weighted_game['actual_winners']} and {four_game['actual_winners']}")
    print(f"weighted counts={counts}; rigorous log-margin lower (scaled 2^{SCALE_BITS})={exact_gap['lower_scaled']}")
    print(f"2^649>88^100=PASS; 2^444800>600001^8800=PASS; M={m}; q={q}; M-q^2={m-q*q}")
    print(f"controls: FD={fd_control}; zero-weight=EXPECTED_REJECTION; receipt={args.output}")


if __name__ == "__main__":
    main()
