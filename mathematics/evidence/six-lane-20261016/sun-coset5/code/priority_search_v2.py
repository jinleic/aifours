#!/usr/bin/env python3
"""Post-candidate priority refresh v2 (public, read-only metadata; no contact).

Targets: Sun's disjoint-coset conjecture at k=5 for arbitrary groups; the Core(5) mechanism
(indices 4r_i, pairwise coprime; double cosets; G-harmonic tuples); Menon and current preprints.
Usage: python3 priority_search_v2.py OUTDIR    (exclusive create; raw responses + summary.json)
"""
import hashlib
import json
import os
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

UA = "aifours-research-lane/1.0 (read-only metadata query)"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def arxiv_entries(xml):
    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml)
    out = []
    for e in root.findall("a:entry", ns):
        out.append({"id": (e.findtext("a:id", "", ns) or "").strip(),
                    "published": (e.findtext("a:published", "", ns) or "").strip(),
                    "updated": (e.findtext("a:updated", "", ns) or "").strip(),
                    "title": " ".join((e.findtext("a:title", "", ns) or "").split()),
                    "summary": " ".join((e.findtext("a:summary", "", ns) or "").split())[:600]})
    return out


ARXIV = [
    ("ax-harmonic-tuples", 'abs:"harmonic" AND abs:"cosets"'),
    ("ax-G-harmonic", 'all:"G-harmonic"'),
    ("ax-disjoint-cosets-gcd", 'abs:"disjoint cosets" AND abs:"greatest common divisor"'),
    ("ax-sun-disjoint", 'abs:"Sun" AND abs:"disjoint" AND abs:"cosets"'),
    ("ax-coset-partition-2026", 'abs:"coset partition" AND submittedDate:[202601010000 TO 202612312359]'),
    ("ax-disjoint-cosets-2026", 'abs:"disjoint" AND abs:"coset" AND submittedDate:[202601010000 TO 202612312359]'),
    ("ax-double-coset-index", 'abs:"double coset" AND abs:"index" AND abs:"disjoint"'),
    ("ax-ginosar-question", 'abs:"Ginosar"'),
    ("ax-herzog-schonheim-2026", 'abs:"Herzog" AND abs:"Sch" AND submittedDate:[202601010000 TO 202612312359]'),
    ("ax-mathGR-recent", 'cat:math.GR AND submittedDate:[202609010000 TO 202610182359]'),
]

OA = [
    ("oa-cites-menon", "https://api.openalex.org/works?filter=cites:{menon}&per-page=100"),
    ("oa-cites-ms", "https://api.openalex.org/works?filter=cites:{ms}&per-page=100"),
    ("oa-cites-zhu", "https://api.openalex.org/works?filter=cites:{zhu}&per-page=100"),
    ("oa-cites-sun2006", "https://api.openalex.org/works?filter=cites:{sun}&per-page=100"),
    ("oa-search-harmonic-tuples", "https://api.openalex.org/works?search=" + urllib.parse.quote("harmonic tuples cosets") + "&per-page=50"),
    ("oa-search-disjoint-cosets-2026", "https://api.openalex.org/works?search=" + urllib.parse.quote("disjoint cosets") + "&filter=from_publication_date:2026-01-01&per-page=50"),
    ("oa-search-sun-k5", "https://api.openalex.org/works?search=" + urllib.parse.quote("Sun conjecture disjoint cosets five") + "&filter=from_publication_date:2025-01-01&per-page=50"),
]
RES = {"menon": "doi:10.48550/arXiv.2608.15873", "ms": "doi:10.48550/arXiv.1803.03569",
       "zhu": "doi:10.48550/arXiv.0807.2207", "sun": "doi:10.48550/arXiv.math/0501451"}

DC = [
    ("dc-harmonic-tuples", '"harmonic tuples"'),
    ("dc-disjoint-cosets", '"disjoint cosets"'),
    ("dc-sun-conjecture-groups", 'Sun conjecture disjoint cosets groups'),
]

CR = [
    ("cr-disjoint-cosets-sun", "disjoint cosets Sun conjecture"),
    ("cr-harmonic-tuples", "G-harmonic tuples cosets"),
]


def main():
    out = sys.argv[1]
    os.makedirs(out, exist_ok=False)
    summ = {"started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "python": sys.version, "queries": []}
    n = 0

    def save(name, data):
        with open(os.path.join(out, name), "xb") as f:
            f.write(data)
        return hashlib.sha256(data).hexdigest()

    for name, q in ARXIV:
        n += 1
        url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode(
            {"search_query": q, "sortBy": "submittedDate", "sortOrder": "descending", "max_results": "100"})
        try:
            d = fetch(url)
            summ["queries"].append({"name": name, "url": url, "sha256": save(f"{n:02d}-{name}.xml", d), "entries": arxiv_entries(d)})
        except Exception as ex:
            summ["queries"].append({"name": name, "url": url, "error": repr(ex)})
        time.sleep(3.5)
    ids = {}
    for key, doi in RES.items():
        try:
            js = json.loads(fetch("https://api.openalex.org/works/" + doi))
            ids[key] = js["id"].rsplit("/", 1)[-1]
        except Exception as ex:
            ids[key] = None
        time.sleep(1)
    summ["openalex_ids"] = ids
    for name, tmpl in OA:
        n += 1
        try:
            url = tmpl.format(**{k: (v or "NONE") for k, v in ids.items()})
            d = fetch(url)
            js = json.loads(d)
            items = [{"id": w.get("id"), "doi": w.get("doi"), "title": w.get("title"), "date": w.get("publication_date")} for w in js.get("results", [])]
            summ["queries"].append({"name": name, "url": url, "sha256": save(f"{n:02d}-{name}.json", d), "count": js.get("meta", {}).get("count"), "items": items})
        except Exception as ex:
            summ["queries"].append({"name": name, "error": repr(ex)})
        time.sleep(1)
    for name, q in DC:
        n += 1
        url = "https://api.datacite.org/dois?" + urllib.parse.urlencode({"query": q, "page[size]": "50"})
        try:
            d = fetch(url)
            js = json.loads(d)
            items = [{"doi": x["attributes"].get("doi"), "title": (x["attributes"].get("titles") or [{}])[0].get("title"), "year": x["attributes"].get("publicationYear")} for x in js.get("data", [])]
            summ["queries"].append({"name": name, "url": url, "sha256": save(f"{n:02d}-{name}.json", d), "total": js.get("meta", {}).get("total"), "items": items})
        except Exception as ex:
            summ["queries"].append({"name": name, "url": url, "error": repr(ex)})
        time.sleep(1)
    for name, q in CR:
        n += 1
        url = "https://api.crossref.org/works?" + urllib.parse.urlencode({"query.bibliographic": q, "rows": "40", "filter": "from-pub-date:2024-01-01"})
        try:
            d = fetch(url)
            js = json.loads(d)
            items = [{"doi": x.get("DOI"), "title": (x.get("title") or [""])[0], "date": x.get("created", {}).get("date-time")} for x in js.get("message", {}).get("items", [])]
            summ["queries"].append({"name": name, "url": url, "sha256": save(f"{n:02d}-{name}.json", d), "items": items})
        except Exception as ex:
            summ["queries"].append({"name": name, "url": url, "error": repr(ex)})
        time.sleep(1)
    summ["finished_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    d = json.dumps(summ, indent=1, ensure_ascii=False).encode()
    print("summary sha256", save("summary.json", d), "bytes", len(d))


if __name__ == "__main__":
    main()
