"""Bounded exploration: Z2-graded extensions of small locally regular non-regular bands with >= 3
D-classes, tested for embeddability into B x| Z2 with |B| <= kmax (generic SAT, certificate checked).

For each band E in the input list and each m in ms: enumerate all Z2-graded extensions (generic SAT,
exhaustive, up to isomorphism), then for each S search k = |E|..kmax for an embedding; a found
embedding is verified independently.  Anything with no embedding up to kmax is a CANDIDATE only
(UNSAT for bounded k is not a proof of non-embeddability).

Usage: uv run --with python-sat python work/pipeline_3d.py bands.json kmax m1 m2 ...
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).parent


def run(args, timeout):
    r = subprocess.run([sys.executable] + args, capture_output=True, text=True, timeout=timeout, cwd=HERE)
    return r.stdout + r.stderr


def main() -> None:
    bands = json.load(open(sys.argv[1]))
    kmax = int(sys.argv[2])
    ms = [int(x) for x in sys.argv[3:]]
    tmp = Path(tempfile.mkdtemp(prefix="rse3d_"))
    summary = []
    for bi, E in enumerate(bands):
        ef = tmp / f"E{bi}.json"
        json.dump(E, open(ef, "w"))
        for m in ms:
            out = tmp / f"E{bi}_m{m}.json"
            log = run(["enum_extensions.py", str(ef), str(m), str(out)], 1200)
            print(f"band {bi} (|E|={len(E)}) m={m}: {log.strip()}", flush=True)
            if not out.exists():
                continue
            for si, S in enumerate(json.load(open(out))):
                sf = tmp / f"E{bi}_m{m}_S{si}.json"
                json.dump(S, open(sf, "w"))
                res = None
                for k in range(len(E), kmax + 1):
                    lg = run(["embed_generic_sat.py", str(sf), str(k)], 1800)
                    if "SAT (embeds)" in lg:
                        cert = tmp / f"cert_{bi}_{m}_{si}.log"
                        cert.write_text(lg)
                        ver = run(["verify_embedding_certificate.py", str(sf), str(cert), "--require-locreg"], 600)
                        ok = "certificate verified" in ver and "B locally regular: True" in ver
                        if ok:
                            res = (k, True)
                            break
                        # a certificate with a non-locally-regular B does not count; search larger k
                status = f"embeds with |B|={res[0]} (certificate {'OK' if res[1] else 'FAILED'})" if res else f"NO embedding with |B|<={kmax} (candidate)"
                print(f"   S{si} |S|={len(S)}: {status}", flush=True)
                summary.append(dict(band=bi, m=m, S=si, size=len(S), result=status, table=S if res is None else None))
                json.dump(summary, open(HERE.parent / "evidence" / "pipeline_3d_summary.json", "w"))
    json.dump(summary, open(HERE.parent / "evidence" / "pipeline_3d_summary.json", "w"))
    print("summary written to evidence/pipeline_3d_summary.json")


if __name__ == "__main__":
    main()
