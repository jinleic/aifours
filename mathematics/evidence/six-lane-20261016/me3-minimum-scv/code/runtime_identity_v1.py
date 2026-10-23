"""Runtime and arithmetic-build identity for the certified runs (hostile review me3-charts-codex-v1, finding 2).

Records the interpreter actually used by code/run_v1.sh (sys.executable, its real path and SHA-256, the Python
framework library), the platform, python-flint / FLINT versions, and SHA-256 + size of every file of the installed
python-flint distribution (package directory, bundled dynamic libraries, dist-info including the wheel RECORD), and the
sympy/mpmath versions. Bookkeeping only: no mathematics. argv[1] = run dir; writes runtime.json (exclusive create).
"""
import sys
import os
import json
import hashlib
import platform
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import flint  # noqa: E402
import sympy  # noqa: E402
import mpmath  # noqa: E402

RUN = sys.argv[1]


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def tree(root):
    out = {}
    for dp, dn, fns in os.walk(root):
        dn.sort()
        for fn in sorted(fns):
            if fn.endswith(".pyc"):
                continue
            p = os.path.join(dp, fn)
            if os.path.isfile(p):
                out[os.path.relpath(p, os.path.dirname(root))] = {"sha256": sha(p), "bytes": os.path.getsize(p)}
    return out


pkg = os.path.dirname(flint.__file__)
site = os.path.dirname(pkg)
dist = {}
for name in sorted(os.listdir(site)):
    low = name.lower()
    if low.startswith("python_flint") or (low.startswith("flint") and low != "flint") or ("flint" in low and low.endswith(".dylibs")):
        p = os.path.join(site, name)
        dist.update(tree(p) if os.path.isdir(p) else {name: {"sha256": sha(p), "bytes": os.path.getsize(p)}})
exe = sys.executable
real = os.path.realpath(exe)
fw = None
d = real
for _ in range(8):
    d = os.path.dirname(d)
    cand = os.path.join(d, "Python")
    if os.path.basename(d).startswith("3.") and os.path.isfile(cand):
        fw = cand
        break
res = {
    "python_version": sys.version,
    "sys_executable": exe,
    "executable_realpath": real,
    "executable_sha256": sha(real),
    "python_framework_library": fw,
    "python_framework_library_sha256": sha(fw) if fw else None,
    "platform": platform.platform(),
    "machine": platform.machine(),
    "python_flint_version": flint.__version__,
    "FLINT_version": getattr(flint, "__FLINT_VERSION__", None),
    "flint_ctx_default": str(flint.ctx),
    "flint_package_dir": pkg,
    "flint_package_files": tree(pkg),
    "flint_distribution_files": dist,
    "sympy_version": sympy.__version__,
    "mpmath_version": mpmath.__version__,
    "lane_guard_sha256": sha(os.path.join(os.path.dirname(__file__), "lane_guard.py")),
}
with lane_guard.xopen(RUN + "/runtime.json") as fh:
    json.dump(res, fh, indent=1, sort_keys=True)
print(json.dumps({k: res[k] for k in ("python_version", "executable_realpath", "executable_sha256",
                                      "python_framework_library", "python_flint_version", "FLINT_version", "platform")},
                 indent=1))
print("flint package files", len(res["flint_package_files"]), "distribution files", len(dist))
