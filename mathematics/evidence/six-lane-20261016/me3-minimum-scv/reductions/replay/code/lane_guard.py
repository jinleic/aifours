"""No-deletion / no-temp / no-overwrite guard for this lane (pattern of tz43-gcdcqs18/code/lane_guard.py).

Import FIRST in every script of this lane.
* os.remove/os.unlink/os.rmdir/os.removedirs/shutil.rmtree/shutil.move raise (no deletion, no cleanup);
* os.replace/os.rename raise (no silent overwrite by rename);
* tempfile creators raise (no system temporary artifacts);
* xopen(path, mode) opens for writing only if the path does not exist yet (modes 'x'/'xb').
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


def new_dir(path):
    """Create a brand-new directory; refuse an existing one (mkdir, exist_ok=False)."""
    os.makedirs(path, exist_ok=False)
    return path
