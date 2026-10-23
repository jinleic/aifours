#!/usr/bin/env python3
"""guard_qual_configs_v12: fixed-metadata PREPARATION writer for rebound package qual-pkg-v9-v19 (owned_supervisor_v19).

WRITTEN ONLY / NOEXEC. Authoring grants no execution, package acceptance, control GO,
release or science claim. Binding parent correction fabe57ab4aeacc416f22bdf334c2cc3bbd5fda1d0e777d7279187ae0564155a2
is retained: owned bounded /bin/date, complete known/unproved and mixed-UID fail-closed evidence; no SIGKILL, tool
timeout, ulimit, deletion or automatic chaining. Target: immutable source19, cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93.
RUN/review/rqls10-supervisor-v19-source-readiness-parent-v1.json
558f9ba310dd1a925595d12919c01ebfff7e4f3d50cb68ea1391fa6695e6ce96 establishes SOURCE_READY_RUNTIME_HOLD only.
Source19 retains source16's typed telemetry plus source17/18/19 acquisition-first/raw-null/cancellation/recovery fixes.
No consumer acceptance or runtime authority follows. Governing package review
RUN/review/rqls10-guard-qualification-v8-v15-codex-v1.prompt.stdout.txt
c2ca271cf34ddc1a5f834d15ab3a251f692d1ddacf11968ccc8567716a3e75b2: this writer repairs its finding 8 (exact bound
types) and keeps the M5/M7 fixes. Held package v8 writer guard_qual_configs_v11.py
720335c15531190c41ea12a1ff723829ca9d3a5abcbe73d60aea5276fd8e2447 stays immutable and unexecuted and is not a target.
The stable source19 constants bind supervisor path/digest, PACKAGE root, ITEM, MARKER_KIND and APPROVAL_KIND;
the healthy config, preparation and ordinary GO wire remain unchanged. This writer spawns nothing, imports
no package source, reads or invents no clock/date, measures no free space or other fresh resource, writes no GO,
stability, approval or disposition file and deletes nothing. It prepares ONLY the 22 retained controls; the
additional v13/v14 matrix (native/state, cap/final-bracket, cap/initial-main, cap/helper-TERM, post-ACK
stderr-write/flush and the four accounting stages) needs separately reviewed bounded fixtures and exact individual
negative GOs, none of which this file provides.

Usage, ONLY under the parent's individual preparation authorization, AFTER it serialized this item's allocation:
  PYTHON_APP -I -B LANE/code/guard_qual_configs_v12.py SCENARIO PYTHON_APP OUTSTANDING_BYTES LANE_OUTSTANDING_BYTES
PYTHON_APP is the actual realpath .../Resources/Python.app/Contents/MacOS/Python executable, never a launcher. The two
totals are the parent's current OTHER outstanding reservations as canonical decimals (lane total <= 10737418240).

Before ANY creation: exact arguments; this file executes from its fixed path; retained no-follow anchors hash the
ACTUAL fixed supervisor (must equal SUPERVISOR_SHA), child v12, writer v12 and checker v11 plus the actual interpreter.
Child/writer/checker digests are computed now and never stored as static constants; the parent's external approval
digest is the trust root that pins them. Creation, exclusive and through retained no-follow descriptors: QROOT once
with package-root.json; a fresh RUN=QROOT/SCENARIO (an existing RUN refuses), RUN/out and RUN/tmp, whose identities
are fstat of the created descriptors; for mutate_pin only, RUN/pinned-scratch.txt (0644) whose inode/size/nlink come
from fstat of its CREATED descriptor before close, content read back on that descriptor; then RUN/preparation.json
(0444, creation facts only, never a config or GO digest); then RUN/config.json (0444) binding the preparation digest.
Every recorded anchor is re-resolved and the RUN inventory checked before printing. Refusal: stderr
PREPARATION_REFUSED and exit 2; partial creations stay for parent audit, never reused or deleted.

PURE functions (module constants + arguments only; no I/O, clock or environment). The checker reconstructs them by a
verbatim copy of this closure, never by importing or executing this file:
  hex64(x); typed_equal(left, right); fixed_source_pins(source_pins); marker_for(source_pins);
  negative_designation(name)
  pinned_inputs(name, source_pins, python, python_sha256, outstanding, lane_outstanding) -> allocation
  creation_channel_for(name, preparation_sha256)
  preparation_for(name, run_inode, output_root_inode, fixture_inode, source_pins, python, python_sha256,
                  outstanding, lane_outstanding)
  config_for(name, python, python_sha256, outstanding, lane_outstanding, source_pins, preparation_sha256,
             creation_channel)
  go_entry_for(name, python, python_sha256, outstanding, lane_outstanding, source_pins, preparation_sha256,
               creation_channel)
  go_configs_for(name, config_sha256, entry)
source_pins = {supervisor, child, writer, checker} -> {path, sha256} at the fixed SOURCES paths; inodes are
[st_dev, st_ino]; creation_channel must equal creation_channel_for(name, preparation_sha256), i.e. {} for every
non-mutation scenario. Canonical JSON file bytes: json.dumps(obj, sort_keys=True, indent=1, allow_nan=False) + LF.

Exact types (review finding8): typed_equal follows owned_supervisor_v19 typed_equal: type() identity at every level,
equal dict key sets, equal list length
and order, then ==; so true never equals 1, false never equals 0 and 60 never equals 60.0. Every binding this closure
validates (source pins, run/out/fixture inodes, creation_channel, GO entry) and the writer's created-file readback and
anchor re-resolution use typed_equal or follow exact type() validation. Supervisor19 applies typed_equal to the
complete GO configs mapping, authorization rereads and preparation supervisor pin, allocation, run and output-root
anchors; every consumer of these pure results must compare with typed_equal, never ==. go_entry_for returns the
BOUND_KEYS object derived from config_for exactly as supervisor19 derives it and re-verified against BOUND_TYPES:
output_roots list of str ([RUN/out]); argv
list of str ([PYTHON_APP,"-I","-B",child v12,SCENARIO,str(life)]); max_wall_s JSON integer (10 for
deadline/ignore/identity, else 60; never 60.0); cpu_slots JSON integer (2 for busy2, else 1; never true);
creation_channel object of str keys and values ({} or the five-field mutation channel); reservation_bytes integer
20971520; outstanding_reservations_bytes integer 0..2**60 and lane_outstanding_reservations_bytes integer
0..10737418240 (never false for 0). The GO configs value is go_configs_for(...): {} for go_unlisted, otherwise exactly
{config_sha256: go_entry}.

Preparation, exact keys (unchanged from v15; supervisor19 creation_manifest requires them): kind=
"qualification-creation-preparation-v1", scenario, run={path:RUN,inode}, output_root={path:RUN/out,inode},
fixture=null, or for mutate_pin {path:RUN/pinned-scratch.txt,inode,sha256:sha256(FIXTURE),bytes:len(FIXTURE),nlink:1},
source_pins, python={path,sha256}, allocation={bytes:20971520,cpu_slots:2 for busy2 else 1,
outstanding_reservations_bytes,lane_outstanding_reservations_bytes} (all JSON integers),
negative_control=(scenario not in ok/rc_nonzero).
Config, exact supervisor19 CONFIG keys (unchanged from v15): pins ordered supervisor, child, writer, checker, python,
RUN/preparation.json, then RUN/pinned-scratch.txt=sha256(FIXTURE) for mutate_pin only, the ONLY pin intended to differ
finally (preparation is immutable). creation_channel={} except mutate_pin/mutate_evidence: {kind:
"qualification-creation-v1",scenario,preparation_path:RUN/preparation.json,preparation_sha256,target_path:
RUN/pinned-scratch.txt or RUN/out/launch.json}. The 22 workloads, lifetimes, walls, thresholds, faults and raw resource
values are unchanged; stability age 300 s.
Marker QROOT/package-root.json (0444): exactly {kind:MARKER_KIND,package:"v9",qroot:QROOT,source_pins}.
The first preparation creates it; every later one must reproduce it byte-exactly from its own actual source digests.
Printed stdout, one JSON line: {kind:"qualification-preparation-output-v1",scenario,item,run,tmpdir:{path,inode},
package_root:{path,created,marker,sha256,inode},preparation:{path,sha256,inode,bytes,content},
config:{path,sha256,inode,bytes,content},allocation,go_entry (go_entry_for),go_configs (go_configs_for),
go_qualification_negative (null means omit),approval_requirements:{kind:APPROVAL_KIND,scenario,
config_sha256,preparation_sha256,sources,python,allocation,ownership_negative,helper_injection,mutation_negative},
negative_control}. The parent adds go_sha256 and stability_receipt_sha256 when it writes its own approval; this file
writes no approval.

Negative designations: mutate_pin/mutate_evidence GO qualification_negative exactly {scenario,kind:"mutation",
creation_channel:true} (JSON true, never 1) plus approval.mutation_negative=true; every forking NEGATIVE_PROCESS member
(busy2, ownership_group/slow/fast/double, zombie_hold) {scenario,kind:"ownership",creation_channel:false} plus
approval.ownership_negative=true; helper injections (date_fault, helper_overrun, helper_group, helper_eof)
{scenario,kind:"helper_injection",creation_channel:false} plus approval.helper_injection=true. Every other control
omits the GO object, carries all three approval flags false and is bound by its own config/preparation digests
(identity is a supervisor fault, not a helper injection). Every flag is a JSON boolean, never 0 or 1.

External parent transaction, unchanged: (1) serialize 20971520 bytes and cpu_slots (busy2 TWO slots at threshold 1,
global cap 2, no busy3) and retain the approval SHA externally; (2) retain the actual exit and exactly one captured
summary; (3) a checker PASS is one control result, never a release; (4) independently prove every known, helper,
reported and unproved identity ended; (5) late audit plus a NEW exclusive /bin/date-stamped disposition joining all
five parts is the only release. This file allocates and releases nothing; UNSETTLED records stay immutable.
"""
import contextlib
import hashlib
import json
import os
import stat
import sys
import time

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
PACKAGE = "qual-pkg-v9-v19"
QROOT = LANE + "/" + PACKAGE
ITEM = "owned_supervisor_v19 rebound creation-identity qualification"
APPROVAL_KIND = "v19-qualification-invocation-v1"
MARKER_KIND = "v19-qualification-root"
SOURCES = {"supervisor": LANE + "/code/owned_supervisor_v19.py", "child": LANE + "/code/guard_qual_child_v12.py",
           "writer": LANE + "/code/guard_qual_configs_v12.py", "checker": LANE + "/code/guard_qual_check_v11.py"}
SUPERVISOR_SHA = "cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93"
PYTHON_SUFFIX = "/Resources/Python.app/Contents/MacOS/Python"
FIXTURE = b"pinned scratch file for the mutate_pin scenario\n"
RESERVATION = 20971520
LANE_CEILING = 10737418240
SOURCE_CAP = 1 << 20
PIN_CAP = 64 << 20
IO_BUDGET_S = 60.0
BOUND_KEYS = ("output_roots", "argv", "max_wall_s", "cpu_slots", "creation_channel", "reservation_bytes",
              "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes")
# Exact JSON type of every bound field as config_for emits it; list and dict members are str.
BOUND_TYPES = {"output_roots": list, "argv": list, "max_wall_s": int, "cpu_slots": int, "creation_channel": dict,
               "reservation_bytes": int, "outstanding_reservations_bytes": int,
               "lane_outstanding_reservations_bytes": int}
# scenario: (cooperative child lifetime s, supervisor max_wall_s, child-out.json required, rss_trip_bytes)
SC = {"go_unlisted": (60, 60, True, 2147483648), "ok": (60, 60, True, 2147483648),
      "rc_nonzero": (60, 60, True, 2147483648), "missing_output": (60, 60, True, 2147483648),
      "mutate_pin": (60, 60, True, 2147483648), "mutate_evidence": (60, 60, True, 2147483648),
      "stray_file": (60, 60, True, 2147483648), "deadline": (120, 10, False, 2147483648),
      "flood": (60, 60, False, 2147483648), "busy2": (60, 60, False, 2147483648),
      "rss": (60, 60, False, 268435456), "ignore": (60, 10, False, 2147483648),
      "identity": (60, 10, False, 2147483648), "date_fault": (60, 60, True, 2147483648),
      "helper_overrun": (60, 60, True, 2147483648), "helper_group": (60, 60, True, 2147483648),
      "helper_eof": (60, 60, True, 2147483648), "ownership_group": (40, 60, True, 2147483648),
      "ownership_slow": (40, 60, True, 2147483648), "ownership_fast": (40, 60, True, 2147483648),
      "ownership_double": (40, 60, True, 2147483648), "zombie_hold": (10, 60, True, 2147483648)}
FAULTS = {"identity": "identity_check_fails", "date_fault": "date_helper_fails",
          "helper_overrun": "helper_observation_overrun", "helper_group": "helper_group_unproved",
          "helper_eof": "helper_eof_unproved"}
HELPER_INJECTIONS = {"date_fault", "helper_overrun", "helper_group", "helper_eof"}
NEGATIVE_PROCESS = {"busy2", "ownership_group", "ownership_slow", "ownership_fast", "ownership_double", "zombie_hold"}
MUTATIONS = {"mutate_pin", "mutate_evidence"}
POSITIVE = {"ok", "rc_nonzero"}


def hex64(x):
    return type(x) is str and len(x) == 64 and all(c in "0123456789abcdef" for c in x)


def typed_equal(left, right):
    """PURE. Same body as the pinned supervisor's typed_equal: exact JSON structure and scalar types recursively, so a
    bool never aliases an integer (true != 1, false != 0) and an integer never aliases a float."""
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return set(left) == set(right) and all(typed_equal(left[k], right[k]) for k in left)
    if isinstance(left, list):
        return len(left) == len(right) and all(typed_equal(a, b) for a, b in zip(left, right))
    return left == right


def fixed_source_pins(source_pins):
    """PURE. Exact {supervisor,child,writer,checker} -> {path,sha256} at the fixed paths; the supervisor must be the
    SUPERVISOR_SHA candidate bytes. Other digests are the actual bytes the caller hashed; the parent's external
    approval trusts them. Paths and the supervisor digest bind by typed_equal; other digests are exact hex64 str."""
    if type(source_pins) is not dict or set(source_pins) != set(SOURCES) or any(
            type(source_pins[k]) is not dict or set(source_pins[k]) != {"path", "sha256"} or
            not typed_equal(source_pins[k]["path"], SOURCES[k]) or not hex64(source_pins[k]["sha256"])
            for k in SOURCES):
        raise ValueError("source pins are not exactly the four fixed package source paths")
    if not typed_equal(source_pins["supervisor"]["sha256"], SUPERVISOR_SHA):
        raise ValueError("supervisor bytes are not the pinned SUPERVISOR_SHA source candidate")
    return {k: {"path": SOURCES[k], "sha256": source_pins[k]["sha256"]} for k in SOURCES}


def pinned_inputs(name, source_pins, python, python_sha256, outstanding, lane_outstanding):
    """PURE shared validation for preparation_for/config_for/go_entry_for; returns the exact allocation object, whose
    four fields are JSON integers (type int, never bool)."""
    if name not in SC:
        raise ValueError("unknown qualification scenario")
    fixed_source_pins(source_pins)
    if type(python) is not str or not python.startswith("/") or os.path.normpath(python) != python or \
            not python.endswith(PYTHON_SUFFIX) or not hex64(python_sha256):
        raise ValueError("interpreter pin is not an actual Python.app executable digest")
    for total, top in ((outstanding, 1 << 60), (lane_outstanding, LANE_CEILING)):
        if type(total) is not int or not 0 <= total <= top:
            raise ValueError("parent outstanding reservation total out of range")
    return {"bytes": RESERVATION, "cpu_slots": 2 if name == "busy2" else 1,
            "outstanding_reservations_bytes": outstanding, "lane_outstanding_reservations_bytes": lane_outstanding}


def creation_channel_for(name, preparation_sha256):
    """PURE. {} for EVERY non-mutation scenario, so its GO stays exactly the plain token and EOF. mutate_pin and
    mutate_evidence get the exact five-field qualification-creation-v1 channel for their fixed current-run target."""
    if name not in SC or not hex64(preparation_sha256):
        raise ValueError("scenario or preparation digest")
    if name not in MUTATIONS:
        return {}
    run = QROOT + "/" + name
    return {"kind": "qualification-creation-v1", "scenario": name, "preparation_path": run + "/preparation.json",
            "preparation_sha256": preparation_sha256,
            "target_path": run + "/pinned-scratch.txt" if name == "mutate_pin" else run + "/out/launch.json"}


def preparation_for(name, run_inode, output_root_inode, fixture_inode, source_pins, python, python_sha256,
                    outstanding, lane_outstanding):
    """PURE. Exact qualification-creation-preparation-v1 object; it never contains a config or GO digest. Inodes are
    [st_dev, st_ino] lists of exact ints from fstat of the writer's CREATED descriptors, compared by typed_equal.
    fixture_inode is required for mutate_pin and None otherwise; its sha256/bytes/nlink are the FIXTURE facts verified
    on the created descriptor before close."""
    def identity(x):
        return type(x) is list and len(x) == 2 and all(type(v) is int and v >= 0 for v in x)

    allocation = pinned_inputs(name, source_pins, python, python_sha256, outstanding, lane_outstanding)
    if not identity(run_inode) or not identity(output_root_inode) or typed_equal(run_inode, output_root_inode) or \
            not typed_equal(run_inode[0], output_root_inode[0]):
        raise ValueError("run/output-root creation identities")
    run = QROOT + "/" + name
    fixture = None
    if name == "mutate_pin":
        if not identity(fixture_inode) or not typed_equal(fixture_inode[0], run_inode[0]) or \
                any(typed_equal(fixture_inode, other) for other in (run_inode, output_root_inode)):
            raise ValueError("mutate_pin requires its created fixture identity")
        fixture = {"path": run + "/pinned-scratch.txt", "inode": list(fixture_inode),
                   "sha256": hashlib.sha256(FIXTURE).hexdigest(), "bytes": len(FIXTURE), "nlink": 1}
    elif fixture_inode is not None:
        raise ValueError("only mutate_pin has a creation fixture")
    return {"kind": "qualification-creation-preparation-v1", "scenario": name,
            "run": {"path": run, "inode": list(run_inode)},
            "output_root": {"path": run + "/out", "inode": list(output_root_inode)}, "fixture": fixture,
            "source_pins": fixed_source_pins(source_pins), "python": {"path": python, "sha256": python_sha256},
            "allocation": allocation, "negative_control": name not in POSITIVE}


def config_for(name, python, python_sha256, outstanding, lane_outstanding, source_pins, preparation_sha256,
               creation_channel):
    """PURE. Exact admitted supervisor config (every CONFIG key, creation_channel included) binding the source pins, the
    actual interpreter, the ORIGINAL preparation digest and, for mutate_pin, the original fixture digest."""
    allocation = pinned_inputs(name, source_pins, python, python_sha256, outstanding, lane_outstanding)
    channel = creation_channel_for(name, preparation_sha256)
    if not typed_equal(creation_channel, channel):
        raise ValueError("creation_channel must be {} or exactly this mutation's prepared channel")
    pins = fixed_source_pins(source_pins)
    life, wall, required, rss = SC[name]
    run, out = QROOT + "/" + name, QROOT + "/" + name + "/out"
    files = [pins[k] for k in ("supervisor", "child", "writer", "checker")]
    files.append({"path": python, "sha256": python_sha256})
    files.append({"path": run + "/preparation.json", "sha256": preparation_sha256})
    if name == "mutate_pin":
        files.append({"path": run + "/pinned-scratch.txt", "sha256": hashlib.sha256(FIXTURE).hexdigest()})
    call = 0.01 if name == "helper_overrun" else 0.2 if name in ("helper_group", "helper_eof") else 5.0
    return {"item": ITEM, "owner": "ContinueRQLS10b", "purpose": "guard-qualification", "lane": LANE,
            "argv": [python, "-I", "-B", SOURCES["child"], name, str(life)],
            "env": {"TMPDIR": run + "/tmp", "PYTHONDONTWRITEBYTECODE": "1"},
            "stdout": out + "/stdout.txt", "stderr": out + "/stderr.txt", "stdout_cap_bytes": 1048576,
            "stderr_cap_bytes": 1048576, "samples": out + "/samples.jsonl", "samples_cap_bytes": 2097152,
            "launch_record": out + "/launch.json", "receipt": out + "/supervisor-receipt.json",
            "settlement_record": out + "/settlement.json",
            "outputs": [{"path": out + "/child-out.json", "required": required}],
            "output_roots": [out], "pins": files, "max_wall_s": wall, "settle_s": 20, "sample_s": 1.0,
            "max_chunk_seconds": 10800, "owned_compute_settled_by_epoch": 1792731393.0,
            "rss_trip_bytes": rss, "rss_projection_bytes": 67108864, "free_trip_bytes": 12200000000,
            "launch_free_min_bytes": 12200000000, "output_trip_bytes": 9437184, "lane_roots": [LANE],
            "lane_disk_root": LANE, "lane_disk_ceiling_bytes": LANE_CEILING, "lane_walk_s": 5.0,
            "busy_limit": 1 if name == "busy2" else 2, "busy_cpu_fraction": 0.5,
            "cpu_slots": allocation["cpu_slots"],
            "admission": {"go_path": run + "/go.json", "stability_receipt_path": run + "/stability.json",
                          "reservation_bytes": allocation["bytes"],
                          "outstanding_reservations_bytes": allocation["outstanding_reservations_bytes"],
                          "lane_outstanding_reservations_bytes": allocation["lane_outstanding_reservations_bytes"],
                          "stability_max_age_s": 300},
            "helper_budget": {"max_calls": 8, "call_budget_s": call,
                              "term_grace_s": 0.5 if name in ("helper_group", "helper_eof") else 5.0},
            "fault_injection": {FAULTS[name]: True} if name in FAULTS else {},
            "creation_channel": channel}


def go_entry_for(name, python, python_sha256, outstanding, lane_outstanding, source_pins, preparation_sha256,
                 creation_channel):
    """PURE. Exact GO configs entry for config_for(...) with the same arguments, derived exactly as the pinned
    supervisor's authorization_io derives its expected object (BOUND_KEYS[:5] from the config, BOUND_KEYS[5:] from its
    admission), then every field is verified to have its exact BOUND_TYPES JSON type with str list/dict members, so the
    entry can never carry true for cpu_slots 1, false for a zero total or 60.0 for max_wall_s 60. Compare with
    typed_equal."""
    cfg = config_for(name, python, python_sha256, outstanding, lane_outstanding, source_pins, preparation_sha256,
                     creation_channel)
    entry = {k: cfg[k] for k in BOUND_KEYS[:5]}
    entry.update({k: cfg["admission"][k] for k in BOUND_KEYS[5:]})
    for k in BOUND_KEYS:
        v = entry[k]
        if type(v) is not BOUND_TYPES[k] or (type(v) is list and any(type(x) is not str for x in v)) or \
                (type(v) is dict and any(type(a) is not str or type(b) is not str for a, b in v.items())):
            raise ValueError("GO entry field is not its exact bound JSON type: " + k)
    return entry


def go_configs_for(name, config_sha256, entry):
    """PURE. Exact GO "configs" value: {} for go_unlisted (its declared negative lists no config), otherwise exactly
    {config_sha256: entry} with entry = go_entry_for(...). Compare with typed_equal, never ==."""
    if name not in SC or not hex64(config_sha256) or type(entry) is not dict or set(entry) != set(BOUND_KEYS):
        raise ValueError("GO configs need this scenario, an actual config digest and its exact bound entry")
    return {} if name == "go_unlisted" else {config_sha256: entry}


def marker_for(source_pins):
    """PURE. Exact QROOT/package-root.json object agreed with the checker: fixed package identity plus the ACTUAL
    source digests hashed at the first authorized preparation; no static own/checker digest constant exists here."""
    return {"kind": MARKER_KIND, "package": "v9", "qroot": QROOT,
            "source_pins": fixed_source_pins(source_pins)}


def negative_designation(name):
    """PURE. Explicit negative authority the parent must supply: exact approval flags and the exact three-key GO
    qualification_negative object (None means the GO omits it). Every flag is a bool, never 0 or 1."""
    if name not in SC:
        raise ValueError("unknown qualification scenario")
    kind = "mutation" if name in MUTATIONS else "ownership" if name in NEGATIVE_PROCESS else \
        "helper_injection" if name in HELPER_INJECTIONS else None
    go = None if kind is None else {"scenario": name, "kind": kind, "creation_channel": name in MUTATIONS}
    return {"negative_control": name not in POSITIVE, "go_qualification_negative": go,
            "approval": {"ownership_negative": name in NEGATIVE_PROCESS,
                         "helper_injection": name in HELPER_INJECTIONS,
                         "mutation_negative": name in MUTATIONS}}


def canonical(obj):
    return (json.dumps(obj, sort_keys=True, indent=1, allow_nan=False) + "\n").encode()


class Budget:
    """Cooperative monotonic I/O budget: refusal only, never a signal, kill or tool timeout; no value is recorded."""

    def __init__(self, seconds):
        self.end = time.monotonic() + seconds

    def check(self, where):
        if time.monotonic() > self.end:
            raise OSError("preparation I/O budget exceeded " + where)


def decimal(text):
    if not (0 < len(text) <= 20 and text.isascii() and text.isdigit() and (text == "0" or text[0] != "0")):
        raise ValueError("reservation totals must be canonical nonnegative decimal integers")
    return int(text)


def open_directory(path, budget):
    """New descriptor by no-follow component traversal from /; every component must be a real directory."""
    if not path.startswith("/") or path == "/" or os.path.normpath(path) != path:
        raise ValueError("directory path is not a normalized absolute path")
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for component in path[1:].split("/"):
            if component in ("", ".", ".."):
                raise ValueError("invalid directory component")
            nxt = os.open(component, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = nxt
            budget.check("directory traversal")
        return fd
    except BaseException:
        os.close(fd)
        raise


def read_bounded(dir_fd, name, cap, budget, keep=False):
    """Bounded no-follow regular-file read relative to a retained directory descriptor; any change refuses."""
    st = os.stat(name, dir_fd=dir_fd, follow_symlinks=False)
    if not stat.S_ISREG(st.st_mode) or not 0 <= st.st_size <= cap:
        raise OSError("not a bounded regular file " + name)
    fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=dir_fd)
    h, parts, got = hashlib.sha256(), [], 0
    try:
        fs = os.fstat(fd)
        if (fs.st_dev, fs.st_ino, fs.st_size) != (st.st_dev, st.st_ino, st.st_size):
            raise OSError("file changed at open " + name)
        while got < st.st_size:
            b = os.read(fd, min(1 << 20, st.st_size - got))
            if not b:
                raise OSError("short read " + name)
            h.update(b)
            got += len(b)
            if keep:
                parts.append(b)
            budget.check("read " + name)
        tail = os.read(fd, 1)
        end = os.fstat(fd)
        if tail or (end.st_size, end.st_mtime_ns) != (st.st_size, st.st_mtime_ns):
            raise OSError("file changed during read " + name)
    finally:
        os.close(fd)
    facts = {"sha256": h.hexdigest(), "inode": [st.st_dev, st.st_ino], "bytes": got, "nlink": st.st_nlink}
    return facts, (b"".join(parts) if keep else None)


def make_directory(parent_fd, name, device, budget):
    """Exclusive mkdir; its creation identity is fstat of the no-follow descriptor opened right after it."""
    os.mkdir(name, 0o755, dir_fd=parent_fd)
    fd = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=parent_fd)
    try:
        st = os.fstat(fd)
        if not stat.S_ISDIR(st.st_mode) or st.st_dev != device or st.st_uid != os.geteuid() or os.listdir(fd):
            raise OSError("created directory is not a fresh owned empty same-volume directory " + name)
        budget.check("mkdir " + name)
    except BaseException:
        os.close(fd)
        raise
    return fd, [st.st_dev, st.st_ino]


def create_exclusive(dir_fd, name, data, mode, budget):
    """Exclusive no-follow creation. Recorded inode/size/nlink are fstat of the CREATED descriptor BEFORE close and
    the content is read back on that descriptor; a later no-follow read must still find exactly that file."""
    fd = os.open(name, os.O_RDWR | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, mode, dir_fd=dir_fd)
    try:
        view = memoryview(data)
        while view:
            n = os.write(fd, view)
            if n <= 0:
                raise OSError("zero-progress write " + name)
            view = view[n:]
            budget.check("write " + name)
        os.fsync(fd)
        st = os.fstat(fd)
        if not stat.S_ISREG(st.st_mode) or st.st_size != len(data) or st.st_nlink != 1 or \
                os.pread(fd, len(data) + 1, 0) != data:
            raise OSError("created descriptor facts differ " + name)
        created = {"sha256": hashlib.sha256(data).hexdigest(), "inode": [st.st_dev, st.st_ino],
                   "bytes": st.st_size, "nlink": st.st_nlink}
    finally:
        os.close(fd)
    if not typed_equal(read_bounded(dir_fd, name, len(data), budget)[0], created):
        raise OSError("created file changed after close " + name)
    return created


def main():
    if len(sys.argv) != 5:
        raise ValueError("usage: SCENARIO ACTUAL_PYTHON_APP OUTSTANDING_BYTES LANE_OUTSTANDING_BYTES")
    name, python = sys.argv[1], sys.argv[2]
    outstanding, lane_outstanding = decimal(sys.argv[3]), decimal(sys.argv[4])
    if name not in SC:
        raise ValueError("unknown qualification scenario")
    if os.path.abspath(__file__) != SOURCES["writer"]:
        raise ValueError("writer must execute from its fixed package path")
    if not python.endswith(PYTHON_SUFFIX) or os.path.realpath(python) != python:
        raise ValueError("interpreter is not the actual non-launcher Python.app executable")
    budget = Budget(IO_BUDGET_S)
    with contextlib.ExitStack() as stack:
        def held(fd):
            stack.callback(os.close, fd)
            return fd

        lane = held(open_directory(LANE, budget))
        lane_st = os.fstat(lane)
        code = held(os.open("code", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=lane))
        actual = {}
        for key, path in SOURCES.items():
            facts = read_bounded(code, os.path.basename(path), SOURCE_CAP, budget)[0]
            actual[key] = {"path": path, "sha256": facts["sha256"]}
        source_pins = fixed_source_pins(actual)
        interpreter = held(open_directory(os.path.dirname(python), budget))
        python_sha = read_bounded(interpreter, os.path.basename(python), PIN_CAP, budget)[0]["sha256"]
        allocation = pinned_inputs(name, source_pins, python, python_sha, outstanding, lane_outstanding)
        marker = marker_for(source_pins)
        negative = negative_designation(name)
        # Arguments, fixed paths and actual source/interpreter digests are validated; creation starts only here.
        created_root = True
        try:
            os.mkdir(PACKAGE, 0o755, dir_fd=lane)
        except FileExistsError:
            created_root = False
        qfd = held(os.open(PACKAGE, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=lane))
        qst = os.fstat(qfd)
        if not stat.S_ISDIR(qst.st_mode) or qst.st_dev != lane_st.st_dev or qst.st_uid != os.geteuid():
            raise OSError("package root is not an owned same-volume directory")
        if created_root:
            if os.listdir(qfd):
                raise OSError("newly created package root is not empty")
            root = create_exclusive(qfd, "package-root.json", canonical(marker), 0o444, budget)
        else:
            root, raw = read_bounded(qfd, "package-root.json", SOURCE_CAP, budget, keep=True)
            if raw != canonical(marker) or root["nlink"] != 1:
                raise ValueError("existing package root marker is not this package's actual source identity")
        try:
            rfd, run_inode = make_directory(qfd, name, lane_st.st_dev, budget)
        except FileExistsError:
            raise ValueError("RUN already exists; preparation is fresh-only and never reuses a run") from None
        held(rfd)
        ofd, out_inode = make_directory(rfd, "out", lane_st.st_dev, budget)
        held(ofd)
        tfd, tmp_inode = make_directory(rfd, "tmp", lane_st.st_dev, budget)
        held(tfd)
        fixture_inode = None
        if name == "mutate_pin":
            fixture_inode = create_exclusive(rfd, "pinned-scratch.txt", FIXTURE, 0o644, budget)["inode"]
        prep = preparation_for(name, run_inode, out_inode, fixture_inode, source_pins, python, python_sha,
                               outstanding, lane_outstanding)
        prepared = create_exclusive(rfd, "preparation.json", canonical(prep), 0o444, budget)
        channel = creation_channel_for(name, prepared["sha256"])
        cfg = config_for(name, python, python_sha, outstanding, lane_outstanding, source_pins, prepared["sha256"],
                         channel)
        # The exact-type GO entry is established before config.json exists; a type refusal creates no config.
        entry = go_entry_for(name, python, python_sha, outstanding, lane_outstanding, source_pins, prepared["sha256"],
                             channel)
        configured = create_exclusive(rfd, "config.json", canonical(cfg), 0o444, budget)
        os.fsync(rfd)
        os.fsync(qfd)
        if created_root:
            os.fsync(lane)
        run = QROOT + "/" + name
        for path, ident in ((LANE, [lane_st.st_dev, lane_st.st_ino]), (QROOT, [qst.st_dev, qst.st_ino]),
                            (run, run_inode), (run + "/out", out_inode), (run + "/tmp", tmp_inode)):
            fd = open_directory(path, budget)
            try:
                st = os.fstat(fd)
            finally:
                os.close(fd)
            if not typed_equal([st.st_dev, st.st_ino], ident):
                raise OSError("anchor changed during preparation " + path)
        inventory = {"out", "tmp", "preparation.json", "config.json"}
        if fixture_inode is not None:
            inventory.add("pinned-scratch.txt")
        if set(os.listdir(rfd)) != inventory or os.listdir(ofd) or os.listdir(tfd):
            raise OSError("RUN inventory differs or out/TMPDIR is not empty")
        budget.check("final anchor verification")
        print(json.dumps({
            "kind": "qualification-preparation-output-v1", "scenario": name, "item": ITEM, "run": run,
            "tmpdir": {"path": run + "/tmp", "inode": tmp_inode},
            "package_root": {"path": QROOT, "created": created_root, "marker": marker, "sha256": root["sha256"],
                             "inode": root["inode"]},
            "preparation": {"path": run + "/preparation.json", "sha256": prepared["sha256"],
                            "inode": prepared["inode"], "bytes": prepared["bytes"], "content": prep},
            "config": {"path": run + "/config.json", "sha256": configured["sha256"], "inode": configured["inode"],
                       "bytes": configured["bytes"], "content": cfg},
            "allocation": allocation, "go_entry": entry,
            "go_configs": go_configs_for(name, configured["sha256"], entry),
            "go_qualification_negative": negative["go_qualification_negative"],
            "approval_requirements": dict(negative["approval"], kind=APPROVAL_KIND, scenario=name,
                                          config_sha256=configured["sha256"], preparation_sha256=prepared["sha256"],
                                          sources=source_pins, python={"path": python, "sha256": python_sha},
                                          allocation=allocation),
            "negative_control": negative["negative_control"]},
            sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.stderr.write("PREPARATION_REFUSED %r\n" % e)
        sys.exit(2)
