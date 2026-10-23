#!/usr/bin/env python3
"""Release the h5_ reservation claims created 2026-10-17 ~14:47 (to stop the run_hard8 runners at a case
boundary) and keep an archive MANIFEST (parent instruction: exclusive collision-checked destinations under
the lane archive; source/destination/SHA-256 recorded; never move proofs, data, sources or unrelated claims).
Only claim files whose content starts with 'reserved ' and contains 'by InfoPacking19 to stop run_hard8' are
moved. With --backfill, MANIFEST lines are first written for the earlier cycle-2 archive moves.
Usage: release_reservations.py [--backfill]
"""
import glob
import hashlib
import os
import sys
import time

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAN = os.path.join(LANE, "archive", "MANIFEST.tsv")


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def man(src, dst, note):
    new = not os.path.exists(MAN)
    with open(MAN, "a") as f:
        if new:
            f.write("time\tsource\tdestination\tsha256\tnote\n")
        f.write("%s\t%s\t%s\t%s\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S%z"), src, dst,
                                          sha(os.path.join(LANE, dst)), note))


def backfill():
    moves = [("cycle2/claims/m2d_ms01_b00634.claim", "archive/claims-stale-20261017T1301/m2d_ms01_b00634.claim",
              "backfill: moved 13:01 (stale claim after SIGTERM pause of run_m2skel6)")]
    for b in range(634, 640):
        moves.append(("cycle2/m2skel_drat/ms01_b%05d.json" % b,
                      "archive/rev8-verdict-parsing-bug-20261017T1331/m2skel_drat/ms01_b%05d.json" % b,
                      "backfill: moved 13:31 (rev-8 verdict parser false negative, see NOTE.txt)"))
        moves.append(("cycle2/claims/m2d8_ms01_b%05d.claim" % b,
                      "archive/rev8-verdict-parsing-bug-20261017T1331/claims/m2d8_ms01_b%05d.claim" % b,
                      "backfill: moved 13:31 with the rev-8 records"))
    for d in ("archive/stopfiles-20261017T142620", "archive/stopfiles-20261017T144116"):
        for f in sorted(os.listdir(os.path.join(LANE, d))):
            moves.append(("cycle2/" + f, d + "/" + f, "backfill: stop file moved to resume runners"))
    for f in sorted(os.listdir(os.path.join(LANE, "archive", "claims-released"))):
        if f.startswith("m2pbd9_"):
            moves.append(("cycle2/claims/" + f.split(".")[0] + ".claim", "archive/claims-released/" + f,
                          "backfill: claim released by run_m2partbatch5 at a stop between batches"))
    for src, dst, note in moves:
        if os.path.exists(os.path.join(LANE, dst)):
            man(src, dst, note)
    p = "archive/rev8-verdict-parsing-bug-20261017T1331/NOTE.txt"
    man("(created in archive)", p, "backfill: note written in the archive at 13:31")


def main():
    if "--backfill" in sys.argv:
        backfill()
    rel = os.path.join(LANE, "archive", "claims-released")
    os.makedirs(rel, exist_ok=True)
    ts = time.strftime("%Y%m%dT%H%M%S")
    n = 0
    for c in sorted(glob.glob(os.path.join(LANE, "cycle2", "claims", "h5_*.claim"))):
        txt = open(c).read()
        if not (txt.startswith("reserved ") and "by InfoPacking19 to stop run_hard8" in txt):
            continue
        dst = os.path.join(rel, os.path.basename(c)[:-6] + ".reservation.%s.claim" % ts)
        if os.path.exists(dst):
            raise SystemExit("archive destination exists: " + dst)
        os.rename(c, dst)
        man(os.path.relpath(c, LANE), os.path.relpath(dst, LANE), "reservation claim released (runners stopped at case boundary)")
        n += 1
    print("released", n)


if __name__ == "__main__":
    main()
