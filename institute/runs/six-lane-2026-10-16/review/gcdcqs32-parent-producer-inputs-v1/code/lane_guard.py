"""No-deletion / no-temp / no-overwrite guard for this lane.  Import FIRST in every script.

* os.remove/os.unlink/os.rmdir/os.removedirs/shutil.rmtree raise (no deletion, no cleanup);
* tempfile's creators raise (no system-temporary artifacts);
* os.replace/os.rename raise (no silent overwrite by rename);
* xopen(path, mode) opens for writing only if the path does not exist yet (mode 'x'/'xb').
"""
import os
import shutil
import tempfile


def _blocked(*args, **kwargs):
    raise RuntimeError("blocked by lane_guard: deletion, renaming and system temp files are disabled in this lane")


os.remove = os.unlink = os.rmdir = os.removedirs = _blocked
os.replace = os.rename = _blocked
shutil.rmtree = shutil.move = _blocked
tempfile.mkstemp = tempfile.mkdtemp = tempfile.TemporaryDirectory = _blocked
tempfile.NamedTemporaryFile = tempfile.TemporaryFile = tempfile.SpooledTemporaryFile = _blocked


def xopen(path, mode="x"):
    """Exclusive-create open: refuses to overwrite an existing file."""
    assert mode in ("x", "xb"), "only exclusive-create modes are allowed"
    return open(path, mode)


def fresh_dir(path):
    """Create a new, empty output directory; refuse a non-empty existing one."""
    if os.path.exists(path) and os.listdir(path):
        raise SystemExit(f"refusing to write into non-empty directory {path}")
    os.makedirs(path, exist_ok=True)
    return path
