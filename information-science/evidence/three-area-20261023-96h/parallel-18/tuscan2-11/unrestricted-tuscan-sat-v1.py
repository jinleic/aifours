#!/usr/bin/env python3
"""Frozen proposal only: every scientific invocation requires exact parent GO.

No solver is launched here. Encode the unrestricted Tuscan-2 definition;
normalizations use global symbol relabeling and row permutation only.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent


class CertificateError(ValueError):
    pass


def owned(path: str) -> Path:
    result = Path(path).resolve()
    if not result.is_relative_to(ROOT):
        raise CertificateError("OUTSIDE_OWNED_ROOT")
    return result


def verify_table(table: object, n: int) -> None:
    if not isinstance(table, list) or len(table) != n:
        raise CertificateError("SHAPE")
    for row in table:
        if not isinstance(row, list) or len(row) != n:
            raise CertificateError("SHAPE")
        for x in row:
            if type(x) is not int or not 0 <= x < n:
                raise CertificateError("RANGE")
        if len(set(row)) != n:
            raise CertificateError("ROW_DUPLICATE")
    adjacent: set[tuple[int, int]] = set()
    for row in table:
        for a, b in zip(row, row[1:]):
            if (a, b) in adjacent:
                raise CertificateError("ADJACENT_REPEAT")
            adjacent.add((a, b))
    universe = {(a, b) for a in range(n) for b in range(n) if a != b}
    if adjacent != universe:
        raise CertificateError("ADJACENT_UNIVERSE")
    distance2: set[tuple[int, int]] = set()
    for row in table:
        for a, b in zip(row, row[2:]):
            if (a, b) in distance2:
                raise CertificateError("DISTANCE2_REPEAT")
            distance2.add((a, b))
    if len(distance2) != n * (n - 2):
        raise CertificateError("DISTANCE2_COUNT")


class CNF:
    def __init__(self, n: int) -> None:
        self.n = n
        self.variables = n ** 3
        self.clauses: list[tuple[int, ...]] = []

    def x(self, r: int, c: int, a: int) -> int:
        return 1 + (r * self.n + c) * self.n + a

    def new_variable(self) -> int:
        self.variables += 1
        return self.variables

    def add(self, *clause: int) -> None:
        self.clauses.append(clause)

    def exactly_one_small(self, literals: list[int]) -> None:
        self.add(*literals)
        for a, b in itertools.combinations(literals, 2):
            self.add(-a, -b)

    def at_most_one(self, literals: list[int]) -> None:
        if len(literals) < 2:
            return
        prefix = [self.new_variable() for _ in range(len(literals) - 1)]
        self.add(-literals[0], prefix[0])
        for i in range(1, len(literals) - 1):
            self.add(-literals[i], prefix[i])
            self.add(-prefix[i - 1], prefix[i])
            self.add(-literals[i], -prefix[i - 1])
        self.add(-literals[-1], -prefix[-1])

    def build(self) -> None:
        n = self.n
        for r in range(n):
            for c in range(n):
                self.exactly_one_small([self.x(r, c, a) for a in range(n)])
            for a in range(n):
                self.exactly_one_small([self.x(r, c, a) for c in range(n)])
        # Each symbol is first and last exactly once by adjacent coverage.
        # First row is normalized by symbols, then rows sorted by first symbol.
        for c in range(n):
            self.add(self.x(0, c, c))
        for r in range(n):
            self.add(self.x(r, 0, r))
        for a in range(n):
            self.exactly_one_small([self.x(r, n - 1, a) for r in range(n)])
        for distance in (1, 2):
            events = {(a, b): [] for a in range(n) for b in range(n) if a != b}
            for r in range(n):
                for c in range(n - distance):
                    for a in range(n):
                        left = self.x(r, c, a)
                        for b in range(n):
                            if a == b:
                                continue
                            right = self.x(r, c + distance, b)
                            y = self.new_variable()
                            # y iff both indicated endpoints occur.
                            self.add(-y, left)
                            self.add(-y, right)
                            self.add(y, -left, -right)
                            events[a, b].append(y)
            for literals in events.values():
                self.at_most_one(literals)


def encode(n: int, output: Path) -> None:
    if not 3 <= n <= 11:
        raise CertificateError("ORDER")
    output.mkdir()  # Exclusive: refuse existing directory, even if empty.
    cnf = CNF(n)
    cnf.build()
    target = output / "instance.cnf"
    with target.open("x", encoding="ascii", newline="\n") as stream:
        stream.write(f"p cnf {cnf.variables} {len(cnf.clauses)}\n")
        for clause in cnf.clauses:
            stream.write(" ".join(map(str, clause)) + " 0\n")
    manifest = {
        "order": n,
        "variables": cnf.variables,
        "clauses": len(cnf.clauses),
        "cnf_sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "normalization": "first row and first column natural; last column permutation",
        "scope": "unrestricted linear Tuscan-2, no other column constraints",
    }
    with (output / "manifest.json").open("x", encoding="utf-8") as stream:
        json.dump(manifest, stream, indent=2)
        stream.write("\n")
    print(json.dumps(manifest, sort_keys=True))


def decode(n: int, encoded: Path, solver_log: Path, output: Path) -> None:
    manifest = json.loads((encoded / "manifest.json").read_text())
    if manifest["order"] != n:
        raise CertificateError("MODEL_ORDER")
    cnf_hash = hashlib.sha256((encoded / "instance.cnf").read_bytes()).hexdigest()
    if cnf_hash != manifest["cnf_sha256"]:
        raise CertificateError("MODEL_CNF_HASH")
    limit = manifest["variables"]
    assignment: dict[int, bool] = {}
    statuses: list[str] = []
    terminated = False
    for line in solver_log.read_text().splitlines():
        fields = line.split()
        if not fields or fields[0] == "c":
            continue
        if fields[0] == "s":
            statuses.append(" ".join(fields[1:]))
            continue
        if fields[0] != "v":
            raise CertificateError("MODEL_LOG_LINE")
        for token in fields[1:]:
            value = int(token)
            if value == 0:
                terminated = True
                continue
            if terminated or abs(value) > limit:
                raise CertificateError("MODEL_VARIABLE")
            key, truth = abs(value), value > 0
            if key in assignment:
                raise CertificateError("MODEL_DUPLICATE_VARIABLE")
            assignment[key] = truth
    if statuses != ["SATISFIABLE"] or not terminated:
        raise CertificateError("MODEL_STATUS")
    if set(assignment) != set(range(1, limit + 1)):
        raise CertificateError("MODEL_INCOMPLETE")
    table: list[list[int]] = []
    for r in range(n):
        row = []
        for c in range(n):
            values = [a for a in range(n) if assignment[1 + (r * n + c) * n + a]]
            if len(values) != 1:
                raise CertificateError("MODEL_CELL")
            row.append(values[0])
        table.append(row)
    verify_table(table, n)
    if table[0] != list(range(n)) or [row[0] for row in table] != list(range(n)):
        raise CertificateError("MODEL_NORMALIZATION")
    with output.open("x", encoding="utf-8") as stream:
        json.dump(table, stream)
        stream.write("\n")
    print(json.dumps({"status": "CANDIDATE_DIRECTLY_CHECKED_BY_AUTHOR_CODE", "order": n,
                      "table_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
                      "independent_verification": False}))


def controls() -> None:
    positive = [[0, 1, 2, 3], [1, 3, 0, 2], [2, 0, 3, 1], [3, 2, 1, 0]]
    fixtures: list[tuple[str, object, int, str]] = [("T2_4", positive, 4, "VALID")]
    duplicate = [row[:] for row in positive]
    duplicate[0][1] = 0
    fixtures.append(("duplicate_symbol", duplicate, 4, "ROW_DUPLICATE"))
    out_of_range = [row[:] for row in positive]
    out_of_range[0][0] = 4
    fixtures.append(("range", out_of_range, 4, "RANGE"))
    adjacency = [row[:] for row in positive]
    adjacency[0][0], adjacency[0][1] = 1, 0
    fixtures.append(("adjacency", adjacency, 4, "ADJACENT_REPEAT"))
    walecki = [0, 1, 5, 2, 4, 3]
    fixtures.append(("T1_not_T2_6", [[(r + x) % 6 for x in walecki] for r in range(6)], 6, "DISTANCE2_REPEAT"))
    fixtures.append(("shape", positive[:-1], 4, "SHAPE"))
    for name, table, n, expected in fixtures:
        try:
            verify_table(table, n)
            actual = "VALID"
        except CertificateError as exc:
            actual = str(exc)
        print(json.dumps({"control": name, "expected": expected, "actual": actual,
                          "pass": actual == expected}))
        if actual != expected:
            raise CertificateError("CONTROL_FAILURE")


def main(argv: list[str]) -> None:
    if argv == ["controls"]:
        controls()
    elif len(argv) == 3 and argv[0] == "encode":
        encode(int(argv[1]), owned(argv[2]))
    elif len(argv) == 5 and argv[0] == "decode":
        decode(int(argv[1]), owned(argv[2]), owned(argv[3]), owned(argv[4]))
    elif len(argv) == 3 and argv[0] == "check-table":
        verify_table(json.loads(owned(argv[2]).read_text()), int(argv[1]))
        print("CANDIDATE_DIRECTLY_CHECKED_BY_AUTHOR_CODE")
    else:
        raise CertificateError("CLI: controls | encode N DIR | decode N DIR LOG OUT | check-table N FILE")


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except (CertificateError, OSError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        raise SystemExit(2)
