#!/usr/bin/env python3
"""Read-only HTTP GET of one public URL; store bytes exclusively and append a pin record.

Usage: python3 -B code/fetch_pin.py URL OUTFILE
Writes OUTFILE (mode 'xb', never overwrites) and OUTFILE + '.pin.json' (mode 'x') with the URL, the host-clock
time before and after the request (from `date`), the HTTP status, selected response headers, size and SHA-256.
"""
import hashlib
import json
import subprocess
import sys
import urllib.request


def host_date():
    return subprocess.run(["date"], capture_output=True, text=True, check=True).stdout.strip()


def main():
    url, out = sys.argv[1], sys.argv[2]
    t0 = host_date()
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (read-only research fetch)"})
    with urllib.request.urlopen(req) as resp:
        status = resp.status
        final_url = resp.geturl()
        headers = {k: v for k, v in resp.headers.items()
                   if k.lower() in ("content-type", "content-length", "last-modified", "etag", "date")}
        body = resp.read()
    t1 = host_date()
    with open(out, "xb") as f:
        f.write(body)
    rec = {
        "url": url,
        "final_url": final_url,
        "http_status": status,
        "response_headers": headers,
        "host_time_before": t0,
        "host_time_after": t1,
        "file": out,
        "bytes": len(body),
        "sha256": hashlib.sha256(body).hexdigest(),
    }
    with open(out + ".pin.json", "x") as f:
        json.dump(rec, f, indent=1)
        f.write("\n")
    print(json.dumps(rec))


if __name__ == "__main__":
    main()
