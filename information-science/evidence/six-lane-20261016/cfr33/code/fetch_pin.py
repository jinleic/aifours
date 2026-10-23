#!/usr/bin/env python3
"""Read-only public HTTP GET with pinning (lane cfr33).

Usage: fetch_pin.py URL OUTNAME
Writes sources/web/OUTNAME (mode x, exact bytes) and sources/web/OUTNAME.pin.json
(URL, final URL, HTTP status, selected headers, host time before/after, byte length, sha256).
Never overwrites (open mode 'x'); a re-fetch needs a new OUTNAME.
"""
import hashlib, json, os, subprocess, sys, urllib.request

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def host_time():
    return subprocess.run(["date", "+%Y-%m-%d %H:%M:%S %Z"], capture_output=True, text=True).stdout.strip()

def main():
    url, name = sys.argv[1], sys.argv[2]
    assert "/" not in name and name not in (".", "..")
    out = os.path.join(LANE, "sources", "web", name)
    t0 = host_time()
    req = urllib.request.Request(url, headers={"User-Agent": "aifours-cfr33-readonly/1.0"})
    with urllib.request.urlopen(req) as r:
        status = r.status
        final = r.geturl()
        hdr = {k: r.headers.get(k) for k in ("Content-Type", "Date", "ETag", "Last-Modified", "Content-Length")}
        body = r.read()
    t1 = host_time()
    h = hashlib.sha256(body).hexdigest()
    with open(out, "xb") as f:
        f.write(body)
    pin = {"url": url, "final_url": final, "http_status": status, "headers": hdr,
           "host_time_start": t0, "host_time_end": t1, "bytes": len(body), "sha256": h,
           "method": "GET (urllib, read-only)"}
    with open(out + ".pin.json", "x") as f:
        json.dump(pin, f, indent=1, sort_keys=True)
        f.write("\n")
    print(json.dumps(pin, sort_keys=True))

if __name__ == "__main__":
    main()
