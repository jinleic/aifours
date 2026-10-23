#!/usr/bin/env python3.14
"""Independent joint exact-cover extension search; ext-search-spec-v2.

Only stdlib; one process. The tree and resource accounting are in README.md.
"""

import errno
import hashlib
import json
import math
import os
import random
import stat
import sys
import time
from array import array

PROGRAM = "ext_search_joint_v1"
RAW_CAP = 1_048_576
RESULT_CAP = 16 * 1_048_576
RETAIN_CAP = 4096
UNASSIGNED = 255
CODES = {
    "COMPLETE": 0, "ESTIMATE": 0, "STOPPED_AT_SOLUTIONS": 1,
    "BAD_INPUT": 2, "INPUT_PIN_MISMATCH": 2, "IO_ERROR": 2,
    "NOT_DM": 3, "INTERNAL_ERROR": 4, "INCOMPLETE_BUDGET": 5,
    "INCOMPLETE_OUTPUT": 6,
}
ERROR_STATUSES = {"BAD_INPUT", "INPUT_PIN_MISMATCH", "IO_ERROR", "NOT_DM", "INTERNAL_ERROR"}
EMPTY_SHA256 = hashlib.sha256(b"[]").hexdigest()


class Stop(Exception):
    """A specified, structured termination, including input rejection."""
    def __init__(self, status, reason):
        super().__init__(reason)
        self.status = status
        self.reason = reason


class Deadline:
    __slots__ = ("start", "end")

    def __init__(self, start):
        self.start = start
        self.end = None

    def expired(self):
        return self.end is not None and time.monotonic() >= self.end

    def check(self):
        if self.expired():
            raise Stop("INCOMPLETE_BUDGET", "self-budget expired")

    def wall(self):
        elapsed = time.monotonic() - self.start
        if not math.isfinite(elapsed) or elapsed < 0:
            raise Stop("INTERNAL_ERROR", "non-finite or decreasing monotonic clock")
        return float(elapsed)


def new_result():
    return {
        "status": "INTERNAL_ERROR", "reason": "run did not finish",
        "program": PROGRAM, "n": None, "q": None, "k": None,
        "m": None, "chunk_lo": None, "chunk_hi": None, "mode": None,
        "chunks": [], "solutions": [], "solutions_sha256": EMPTY_SHA256,
        "input_sha256": None, "program_sha256": None, "extra": {}, "wall_s": 0.0,
    }


def decimal(value, flag):
    digits = value[1:] if value[:1] in ("+", "-") else value
    if not digits or any(ch < "0" or ch > "9" for ch in digits):
        raise Stop("BAD_INPUT", "non-integer value for " + flag)
    try:
        return int(value)
    except ValueError:
        raise Stop("BAD_INPUT", "integer conversion rejected for " + flag) from None


def arguments(argv, result, clock):
    required = {"--raw", "--raw-sha256", "--m", "--chunk-lo", "--chunk-hi",
                "--max-solutions", "--budget-s"}
    allowed = required | {"--mode", "--probes", "--seed"}
    if len(argv) % 2:
        raise Stop("BAD_INPUT", "arguments must be --flag value pairs")
    values = {}
    for pos in range(0, len(argv), 2):
        flag = argv[pos]
        if flag not in allowed:
            raise Stop("BAD_INPUT", "unknown flag")
        if flag in values:
            raise Stop("BAD_INPUT", "duplicate flag")
        values[flag] = argv[pos + 1]
    if not required.issubset(values):
        raise Stop("BAD_INPUT", "missing required flag")
    try:
        budget = float(values["--budget-s"])
    except (ValueError, OverflowError):
        raise Stop("BAD_INPUT", "invalid --budget-s") from None
    if not math.isfinite(budget) or not 0 < budget <= 10_000:
        raise Stop("BAD_INPUT", "--budget-s must be finite and in (0,10000]")
    clock.end = clock.start + budget
    clock.check()
    mode = values.get("--mode", "search")
    if mode not in ("search", "estimate"):
        raise Stop("BAD_INPUT", "--mode must be search or estimate")
    result["mode"] = mode
    for flag, key in (("--m", "m"), ("--chunk-lo", "chunk_lo"), ("--chunk-hi", "chunk_hi")):
        result[key] = decimal(values[flag], flag)
    limit = decimal(values["--max-solutions"], "--max-solutions")
    if limit < 0:
        raise Stop("BAD_INPUT", "--max-solutions must be non-negative")
    pin = values["--raw-sha256"]
    if len(pin) != 64 or any(ch not in "0123456789abcdefABCDEF" for ch in pin):
        raise Stop("BAD_INPUT", "--raw-sha256 must contain 64 hexadecimal digits")
    if not values["--raw"]:
        raise Stop("BAD_INPUT", "empty --raw path")
    probes = None
    seed = None
    if "--probes" in values:
        probes = decimal(values["--probes"], "--probes")
        if probes < 1:
            raise Stop("BAD_INPUT", "--probes must be positive")
    if "--seed" in values:
        seed = decimal(values["--seed"], "--seed")
    if mode == "estimate" and (probes is None or seed is None):
        raise Stop("BAD_INPUT", "estimate requires --probes and --seed")
    clock.check()
    return values["--raw"], pin.lower(), limit, probes, seed


def hash_program(clock):
    name = globals().get("__file__")
    if name is None:
        return None  # Informational hash is unavailable to a loader without __file__.
    digest = hashlib.sha256()
    with open(name, "rb") as handle:
        while True:
            block = handle.read(65_536)
            if not block:
                break
            digest.update(block)
            clock.check()
    return digest.hexdigest()


def read_raw(path, clock):
    # Nonblocking open avoids waiting on a FIFO before the regular-file check.
    fd = os.open(path, os.O_RDONLY | os.O_NONBLOCK)
    try:
        before = os.fstat(fd)
        if not stat.S_ISREG(before.st_mode):
            raise Stop("BAD_INPUT", "raw input must be a regular file")
        if before.st_size > RAW_CAP:
            raise Stop("BAD_INPUT", "raw input exceeds 1 MiB")
        raw = os.read(fd, RAW_CAP)  # One read, never more than the size cap.
        after = os.fstat(fd)
        if len(raw) != before.st_size or after.st_size != len(raw):
            raise Stop("BAD_INPUT", "raw file size changed or read was short")
        clock.check()
        return raw
    finally:
        os.close(fd)


def parse_raw(raw, result, clock):
    # No valid <=12-row input can contain more than 12 LF bytes.
    if raw.count(b"\n") > 12:
        raise Stop("BAD_INPUT", "too many raw rows")
    lines = raw.split(b"\n")
    if lines[-1] == b"":
        lines.pop()
    k = len(lines)
    if not 2 <= k <= 12:
        raise Stop("BAD_INPUT", "raw row count must be in [2,12]")
    n = None
    matrix = None
    position = 0
    for line in lines:
        # maxsplit=120 preserves G1 for all allowed inputs, but bounds token objects.
        tokens = line.split(None, 120)
        if not tokens:
            raise Stop("BAD_INPUT", "blank raw row")
        if n is None:
            n = len(tokens)
            if n > 120 or n % 3 or n // 3 < 2 or (n // 3) % 3 == 0:
                raise Stop("BAD_INPUT", "invalid n: require n=3q<=120, q>=2, q%3!=0")
            matrix = bytearray(k * n)
        if len(tokens) != n:
            raise Stop("BAD_INPUT", "unequal raw row lengths")
        for token in tokens:
            body = token[1:] if token[:1] in (b"+", b"-") else token
            if not body or not body.isdigit():
                raise Stop("BAD_INPUT", "invalid G1 integer token")
            try:
                value = int(token)
            except ValueError:
                raise Stop("BAD_INPUT", "G1 integer conversion rejected") from None
            matrix[position] = value % n
            position += 1
        clock.check()
    result.update(n=n, q=n // 3, k=k)
    return matrix


def check_dm(matrix, n, k, clock):
    full = (1 << n) - 1
    for x in range(k):
        for y in range(x + 1, k):
            seen = 0
            for c in range(n):
                bit = 1 << ((matrix[x * n + c] - matrix[y * n + c]) % n)
                if seen & bit:
                    raise Stop("NOT_DM", "a pair difference is not a permutation")
                seen |= bit
            if seen != full:
                raise Stop("NOT_DM", "a pair difference is not a permutation")
            clock.check()


def tree_bound(r):
    # With t free columns left, an item has at most t children.
    total = 1
    level = 1
    for t in range(r, 0, -1):
        level *= t
        total += level
    return total


class Records:
    """Fixed-capacity packed ledger; chunk index is lo + record offset."""
    __slots__ = ("lo", "probes", "width", "node_data", "solution_counts", "estimates",
                 "statuses", "started", "nodes", "solutions")

    def __init__(self, lo, n, m, mode, probes):
        self.lo = lo
        self.probes = probes
        r = n - 1 - m
        bound = tree_bound(r) if mode == "search" else probes * (r + 1)
        self.width = max(1, (bound.bit_length() + 7) // 8)
        self.node_data = bytearray(RETAIN_CAP * self.width)
        self.solution_counts = array("H", [0]) * RETAIN_CAP
        self.estimates = array("d", [0.0]) * RETAIN_CAP
        self.statuses = bytearray(RETAIN_CAP)
        self.started = 0
        self.nodes = 0
        self.solutions = 0

    def begin(self):
        if self.started == RETAIN_CAP:
            raise Stop("INCOMPLETE_OUTPUT", "4096 started-chunk retention limit reached")
        self.started += 1
        self.nodes = 0
        self.solutions = 0
        self.statuses[self.started - 1] = 1  # NOT_COMPLETE until explicitly finished.

    def flush(self):
        slot = self.started - 1
        start = slot * self.width
        self.node_data[start:start + self.width] = self.nodes.to_bytes(self.width, "little")
        self.solution_counts[slot] = self.solutions

    def complete(self):
        self.statuses[self.started - 1] = 0

    def estimated(self, mean):
        if not math.isfinite(mean) or mean < 1:
            raise Stop("INTERNAL_ERROR", "non-finite or invalid Knuth mean")
        slot = self.started - 1
        self.estimates[slot] = mean
        self.statuses[slot] = 2

    def export(self):
        result = []
        for slot in range(self.started):
            start = slot * self.width
            nodes = int.from_bytes(self.node_data[start:start + self.width], "little")
            entry = {"chunk": self.lo + slot, "nodes": nodes}
            status = self.statuses[slot]
            if status == 2:
                entry.update(status="ESTIMATE", estimate=self.estimates[slot], probes=self.probes)
            else:
                entry.update(status="COMPLETE" if status == 0 else "NOT_COMPLETE",
                             solutions=self.solution_counts[slot])
            result.append(entry)
        return result


class Joint:
    """Pair items only; column exclusivity is an independently maintained constraint."""
    __slots__ = ("a", "n", "k", "m", "limit", "mode", "clock", "book", "M", "I",
                 "hits", "active", "counts", "covered", "f", "trail", "top",
                 "saved", "solution_count", "chunk", "root_feasible")

    def __init__(self, matrix, result, limit, clock, book):
        self.a = matrix
        self.n, self.k, self.m = result["n"], result["k"], result["m"]
        self.limit, self.mode, self.clock, self.book = limit, result["mode"], clock, book
        n, k = self.n, self.k
        self.M, self.I = n * (n - 1), k * n
        self.hits = array("H", [0]) * (k * self.M)
        self.active = bytearray(self.M)
        self.counts = array("H", [0]) * self.I
        self.covered = bytearray(self.I)
        self.f = bytearray(n)
        self.trail = array("H", [0]) * self.M
        self.top = 0
        self.saved = bytearray(RETAIN_CAP * n)
        self.solution_count = 0
        self.chunk = None
        self.root_feasible = False
        for c in range(1, n):
            for w in range(n):
                option = (c - 1) * n + w
                for x in range(k):
                    self.hits[option * k + x] = x * n + (matrix[x * n + c] - w) % n
            clock.check()

    def disable(self, option):
        if self.active[option]:
            self.active[option] = 0
            self.trail[self.top] = option
            self.top += 1
            base = option * self.k
            for x in range(self.k):
                item = self.hits[base + x]
                self.counts[item] -= 1

    def cover_item(self, item):
        x, value = divmod(item, self.n)
        base = x * self.n
        for c in range(1, self.n):
            w = (self.a[base + c] - value) % self.n
            self.disable((c - 1) * self.n + w)

    def assign(self, option):
        n, k = self.n, self.k
        marker = self.top
        c, w = divmod(option, n)
        c += 1
        self.f[c] = w
        for candidate in range((c - 1) * n, c * n):
            self.disable(candidate)
        base = option * k
        for x in range(k):
            item = self.hits[base + x]
            self.covered[item] = 1
            self.cover_item(item)
        return marker

    def undo(self, option, marker):
        base = option * self.k
        for x in range(self.k):
            self.covered[self.hits[base + x]] = 0
        self.f[option // self.n + 1] = UNASSIGNED
        while self.top > marker:
            self.top -= 1
            candidate = self.trail[self.top]
            self.active[candidate] = 1
            base = candidate * self.k
            for x in range(self.k):
                item = self.hits[base + x]
                self.counts[item] += 1

    def prepare(self, chunk):
        n = self.n
        self.chunk = chunk
        self.top = 0
        for option in range(self.M):
            self.active[option] = 1
            if option % 1024 == 0:
                self.clock.check()
        for item in range(self.I):
            self.covered[item] = 0
            self.counts[item] = n - 1
        for c in range(n):
            self.f[c] = UNASSIGNED
        self.f[0] = 0
        for x in range(self.k):
            item = x * n + self.a[x * n]
            self.covered[item] = 1
            self.cover_item(item)
        remaining = chunk
        divisor = n ** (self.m - 1) if self.m else 1
        self.root_feasible = True
        for c in range(1, self.m + 1):
            w, remaining = divmod(remaining, divisor)
            divisor //= n
            option = (c - 1) * n + w
            if not self.active[option]:
                self.root_feasible = False
                break
            self.assign(option)
            self.clock.check()
        self.clock.check()

    def visit(self):
        self.book.nodes += 1
        self.clock.check()  # Every node, stronger than the 1024-node requirement.

    def choose(self):
        best, least = -1, self.n
        for item in range(self.I):
            if not self.covered[item]:
                count = self.counts[item]
                if count < least:
                    best, least = item, count
                    if count == 0:
                        break
        return best, least

    def candidates(self, item):
        x, value = divmod(item, self.n)
        base = x * self.n
        for c in range(1, self.n):
            w = (self.a[base + c] - value) % self.n
            option = (c - 1) * self.n + w
            if self.active[option]:
                yield option  # Increasing (column, value): one value per column.

    def retain(self):
        n, k, f = self.n, self.k, self.f
        if len(f) != n or f[0] != 0 or any(w >= n for w in f):
            raise Stop("INTERNAL_ERROR", "solution normalisation or value recheck failed")
        idx = 0
        for c in range(1, self.m + 1):
            idx = idx * n + f[c]
        if idx != self.chunk:
            raise Stop("INTERNAL_ERROR", "solution fixed-chunk recheck failed")
        full = (1 << n) - 1
        for x in range(k):
            seen = 0
            for c in range(n):
                bit = 1 << ((self.a[x * n + c] - f[c]) % n)
                if seen & bit:
                    raise Stop("INTERNAL_ERROR", "solution EXT(D) recheck failed")
                seen |= bit
            if seen != full:
                raise Stop("INTERNAL_ERROR", "solution EXT(D) recheck failed")
        if self.solution_count == RETAIN_CAP:
            raise Stop("INCOMPLETE_OUTPUT", "4097th solution would exceed retention cap")
        start = self.solution_count * n
        self.saved[start:start + n] = f
        self.solution_count += 1
        self.book.solutions += 1
        if self.mode == "estimate":
            raise Stop("STOPPED_AT_SOLUTIONS", "estimate probe reached a verified solution")
        if self.limit and self.solution_count >= self.limit:
            raise Stop("STOPPED_AT_SOLUTIONS", "requested solution count reached")

    def search(self):
        self.visit()
        if not self.root_feasible:
            return
        item, count = self.choose()
        if item == -1:
            self.retain()
            return
        if count == 0:
            return
        for option in self.candidates(item):
            marker = self.assign(option)
            try:
                self.search()
            finally:
                self.undo(option, marker)

    def probe(self, rng):
        self.visit()
        if not self.root_feasible:
            return 1
        item, count = self.choose()
        if item == -1:
            self.retain()  # Always stops estimate mode after a real witness.
        if count == 0:
            return 1
        rank = rng.randrange(count)
        selected = None
        for option in self.candidates(item):
            if rank == 0:
                selected = option
                break
            rank -= 1
        if selected is None:
            raise Stop("INTERNAL_ERROR", "incremental count disagrees with feasible options")
        marker = self.assign(selected)
        try:
            return 1 + count * self.probe(rng)
        finally:
            self.undo(selected, marker)

    def export_solutions(self):
        result = []
        for slot in range(self.solution_count):
            start = slot * self.n
            result.append(list(self.saved[start:start + self.n]))
        result.sort()
        for pos in range(1, len(result)):
            if result[pos] == result[pos - 1]:
                raise Stop("INTERNAL_ERROR", "duplicate retained solution")
        return result


def run_chunks(engine, result, probes, seed, clock, book):
    chunk = result["chunk_lo"]
    while chunk < result["chunk_hi"]:
        clock.check()
        book.begin()
        try:
            engine.prepare(chunk)
            if result["mode"] == "search":
                engine.search()
                clock.check()
                book.complete()
            else:
                rng = random.Random(seed)  # Reset per chunk, never per probe.
                total, completed = 0, 0
                while completed < probes:
                    total += engine.probe(rng)
                    completed += 1
                clock.check()
                book.estimated(total / probes)
        finally:
            book.flush()
        chunk += 1
    result["status"] = "COMPLETE" if result["mode"] == "search" else "ESTIMATE"
    result["reason"] = "all requested chunks exhausted" if result["mode"] == "search" else "informational full-tree Knuth estimates only"


def solutions_digest(solutions):
    digest = hashlib.sha256()
    encoder = json.JSONEncoder(separators=(",", ":"), allow_nan=False)
    for part in encoder.iterencode(solutions):
        digest.update(part.encode("ascii"))
    return digest.hexdigest()


def compact_error(result, status, reason):
    result.update(status=status, reason=reason, chunks=[], solutions=[],
                  solutions_sha256=EMPTY_SHA256, extra={})


def late_budget(result, clock):
    if (result["status"] not in ERROR_STATUSES | {"INCOMPLETE_OUTPUT", "INCOMPLETE_BUDGET"}
            and clock.expired()):
        result.update(status="INCOMPLETE_BUDGET", reason="self-budget expired before final publication")
        return True
    return False


def render(result, clock, buffer):
    # iterencode is byte-identical to dumps with these parameters, but never
    # constructs an over-cap complete string. Reserve the final LF in the cap.
    encoder = json.JSONEncoder(sort_keys=True, separators=(",", ":"), allow_nan=False)
    while True:
        late_budget(result, clock)
        result["wall_s"] = clock.wall()
        used = 0
        restart = False
        for piece_no, part in enumerate(encoder.iterencode(result)):
            if piece_no % 1024 == 0 and late_budget(result, clock):
                restart = True
                break
            if used + len(part) + 1 > RESULT_CAP:
                if result["status"] == "INCOMPLETE_OUTPUT" and not result["chunks"] and not result["solutions"]:
                    result.update(m=None, chunk_lo=None, chunk_hi=None)
                compact_error(result, "INCOMPLETE_OUTPUT", "serialized result exceeds 16 MiB publication cap; payload omitted")
                restart = True
                break
            block = part.encode("ascii")
            buffer[used:used + len(block)] = block
            used += len(block)
        if restart:
            continue
        if late_budget(result, clock):
            continue
        buffer[used] = 10
        return memoryview(buffer)[:used + 1]


def write_all(fd, data):
    view = memoryview(data)
    offset = 0
    while offset < len(view):
        count = os.write(fd, view[offset:])
        if count <= 0:
            raise OSError(errno.EIO, "zero-length write")
        offset += count


def emergency(result, status, reason, clock, fd):
    # Best effort after output I/O or an unexpected publication failure. Never
    # reopen/overwrite any already-created result.json, including our own.
    compact_error(result, status, reason)
    result.update(m=None, chunk_lo=None, chunk_hi=None)
    try:
        result["wall_s"] = clock.wall()
        payload = (json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode("ascii")
    except Exception:
        result = new_result()
        result.update(status=status, reason=reason)
        payload = (json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii")
    if fd is not None:
        # An artifact already created by this invocation is immutable, even if
        # the first write failed. The supervisor must reject any disagreement.
        try:
            os.close(fd)
        except OSError:
            pass
    else:
        try:
            fd = os.open("result.json", os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
        except OSError:
            fd = None
        if fd is not None:
            try:
                write_all(fd, payload)
            except OSError:
                pass
            finally:
                try:
                    os.close(fd)
                except OSError:
                    pass
    try:
        write_all(1, payload)
    except OSError:
        pass
    return CODES[status]


def publish(result, clock):
    fd = None
    try:
        buffer = bytearray(RESULT_CAP)
        payload = render(result, clock, buffer)
        # Check immediately before the exclusive create/write as well.
        if late_budget(result, clock):
            payload = render(result, clock, buffer)
        fd = os.open("result.json", os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
        # An open/create delay may consume the budget before the first byte.
        if late_budget(result, clock):
            payload = render(result, clock, buffer)
        write_all(fd, payload)
        os.close(fd)
        fd = None
        write_all(1, payload)
        # Never rewrite an artifact after publication. A late overrun is an
        # exit-code/status mismatch that the supervisor must reject as UNKNOWN.
        if (result["status"] not in ERROR_STATUSES | {"INCOMPLETE_OUTPUT", "INCOMPLETE_BUDGET"}
                and clock.expired()):
            return CODES["INCOMPLETE_BUDGET"]
        return CODES[result["status"]]
    except OSError as exc:
        return emergency(result, "IO_ERROR", "publication OSError errno=" + str(exc.errno), clock, fd)
    except Exception as exc:
        return emergency(result, "INTERNAL_ERROR", "publication exception " + type(exc).__name__, clock, fd)


def main(argv=None):
    clock = Deadline(time.monotonic())
    result = new_result()
    engine = None
    book = None
    raw = None
    try:
        raw_path, pin, limit, probes, seed = arguments(sys.argv[1:] if argv is None else argv, result, clock)
        result["program_sha256"] = hash_program(clock)
        raw = read_raw(raw_path, clock)
        result["input_sha256"] = hashlib.sha256(raw).hexdigest()
        if result["input_sha256"] != pin:
            raise Stop("INPUT_PIN_MISMATCH", "raw sha256 does not match pin")
        matrix = parse_raw(raw, result, clock)
        del raw
        n, m, lo, hi = result["n"], result["m"], result["chunk_lo"], result["chunk_hi"]
        if not 0 <= m <= n - 1:
            raise Stop("BAD_INPUT", "--m must be in [0,n-1]")
        if not 0 <= lo < hi <= n ** m:
            raise Stop("BAD_INPUT", "invalid half-open chunk range")
        check_dm(matrix, n, result["k"], clock)
        clock.check()
        book = Records(lo, n, m, result["mode"], probes)
        engine = Joint(matrix, result, limit, clock, book)
        run_chunks(engine, result, probes, seed, clock, book)
    except Stop as exc:
        result.update(status=exc.status, reason=exc.reason)
    except OSError as exc:
        result.update(status="IO_ERROR", reason="OSError errno=" + str(exc.errno))
    except Exception as exc:
        result.update(status="INTERNAL_ERROR", reason="unexpected exception " + type(exc).__name__)
    raw = None  # Also release raw bytes on parse/pin failure before publication.
    try:
        if engine is not None:
            result["solutions"] = engine.export_solutions()
        if book is not None:
            result["chunks"] = book.export()
        result["solutions_sha256"] = solutions_digest(result["solutions"])
    except Stop as exc:
        compact_error(result, exc.status, exc.reason)
    except OSError as exc:
        compact_error(result, "IO_ERROR", "result assembly OSError errno=" + str(exc.errno))
    except Exception as exc:
        compact_error(result, "INTERNAL_ERROR", "result assembly exception " + type(exc).__name__)
    return publish(result, clock)


if __name__ == "__main__":
    sys.exit(main())
