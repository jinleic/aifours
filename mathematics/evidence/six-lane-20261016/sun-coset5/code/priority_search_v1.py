#!/usr/bin/env python3
"""Priority search v1 for Sun's disjoint-coset conjecture at k=5 (groups).

Fetches public metadata (arXiv API, OpenAlex, DataCite) and stores every raw
response, its SHA256 and a short summary under evidence/priority-search-v1/.
Standard library only. Files are created exclusively (mode 'x').
"""
import hashlib
import json
import os
import sys
import time
import urllib.parse
import urllib.request

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(LANE, "evidence", "priority-search-v1")
UA = "aifours-research-lane/1.0 (mailto:none; read-only metadata query)"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def save(name, data):
    path = os.path.join(OUT, name)
    with open(path, "xb") as f:
        f.write(data)
    return hashlib.sha256(data).hexdigest()


ARXIV = "http://export.arxiv.org/api/query?"
ARXIV_QUERIES = [
    ("arxiv-ids", {"id_list": "0807.2207,1803.03569,2608.15873,2607.24655,math/0501451", "max_results": "10"}),
    ("arxiv-disjoint-cosets", {"search_query": 'abs:"disjoint cosets"', "sortBy": "submittedDate", "sortOrder": "descending", "max_results": "50"}),
    ("arxiv-pairwise-disjoint-cosets", {"search_query": 'all:"pairwise disjoint cosets"', "sortBy": "submittedDate", "sortOrder": "descending", "max_results": "50"}),
    ("arxiv-sun-conjecture-cosets", {"search_query": 'abs:Sun AND abs:conjecture AND abs:cosets', "sortBy": "submittedDate", "sortOrder": "descending", "max_results": "50"}),
    ("arxiv-coset-gcd-index", {"search_query": 'abs:coset AND abs:index AND abs:gcd', "sortBy": "submittedDate", "sortOrder": "descending", "max_results": "50"}),
    ("arxiv-disjoint-residue-classes", {"search_query": 'abs:"disjoint residue classes"', "sortBy": "submittedDate", "sortOrder": "descending", "max_results": "50"}),
    ("arxiv-menon-author", {"search_query": 'au:Menon AND cat:math.GR', "sortBy": "submittedDate", "sortOrder": "descending", "max_results": "50"}),
    ("arxiv-mathGR-disjoint-coset-recent", {"search_query": 'cat:math.GR AND abs:disjoint AND abs:coset', "sortBy": "submittedDate", "sortOrder": "descending", "max_results": "50"}),
    ("arxiv-mathNT-disjoint-coset-recent", {"search_query": 'cat:math.NT AND abs:disjoint AND abs:coset', "sortBy": "submittedDate", "sortOrder": "descending", "max_results": "50"}),
    ("arxiv-coset-systems-moduli", {"search_query": 'abs:"coset" AND abs:"Erdos" AND abs:"Sun"', "sortBy": "submittedDate", "sortOrder": "descending", "max_results": "50"}),
]

OPENALEX = "https://api.openalex.org/"
DATACITE = "https://api.datacite.org/dois?"
DATACITE_QUERIES = [
    ("datacite-disjoint-cosets", {"query": '"disjoint cosets"', "page[size]": "50"}),
    ("datacite-sun-conjecture-cosets", {"query": 'Sun conjecture cosets', "page[size]": "50"}),
    ("datacite-coset-gcd", {"query": 'cosets gcd indices conjecture', "page[size]": "50"}),
    ("datacite-disjoint-residue-classes", {"query": '"disjoint residue classes"', "page[size]": "50"}),
]


def arxiv_titles(xml):
    import xml.etree.ElementTree as ET
    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml)
    out = []
    for e in root.findall("a:entry", ns):
        out.append({
            "id": (e.findtext("a:id", default="", namespaces=ns) or "").strip(),
            "published": (e.findtext("a:published", default="", namespaces=ns) or "").strip(),
            "updated": (e.findtext("a:updated", default="", namespaces=ns) or "").strip(),
            "title": " ".join((e.findtext("a:title", default="", namespaces=ns) or "").split()),
            "authors": [a.findtext("a:name", default="", namespaces=ns) for a in e.findall("a:author", ns)],
        })
    return out


def main():
    os.makedirs(OUT, exist_ok=False)
    summary = {"started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "python": sys.version, "queries": []}
    n = 0
    for name, params in ARXIV_QUERIES:
        n += 1
        url = ARXIV + urllib.parse.urlencode(params)
        try:
            data = fetch(url)
            h = save(f"{n:02d}-{name}.xml", data)
            rec = {"name": name, "url": url, "sha256": h, "bytes": len(data), "entries": arxiv_titles(data)}
        except Exception as ex:  # record failures, do not hide them
            rec = {"name": name, "url": url, "error": repr(ex)}
        summary["queries"].append(rec)
        time.sleep(3.5)
    # OpenAlex: resolve works by arXiv DOI / title, then citing works
    targets = {
        "zhu-0807.2207": "https://api.openalex.org/works?search=" + urllib.parse.quote("disjoint cosets Zhu Sun conjecture") + "&per-page=25",
        "margolis-schnabel-1803.03569": "https://api.openalex.org/works/doi:10.48550/arXiv.1803.03569",
        "menon-2608.15873": "https://api.openalex.org/works/doi:10.48550/arXiv.2608.15873",
        "fornal-sun-2607.24655": "https://api.openalex.org/works/doi:10.48550/arXiv.2607.24655",
        "zhu-arxiv-doi": "https://api.openalex.org/works/doi:10.48550/arXiv.0807.2207",
        "sun-2006-arxiv-doi": "https://api.openalex.org/works/doi:10.48550/arXiv.math/0501451",
        "search-disjoint-cosets-2024on": "https://api.openalex.org/works?search=" + urllib.parse.quote("disjoint cosets") + "&filter=from_publication_date:2024-01-01&per-page=50",
        "search-sun-coset-conjecture": "https://api.openalex.org/works?search=" + urllib.parse.quote("Sun conjecture disjoint cosets indices") + "&per-page=50",
        "search-margolis-schnabel-title": "https://api.openalex.org/works?search=" + urllib.parse.quote("Margolis Schnabel cosets") + "&per-page=25",
    }
    resolved = {}
    for name, url in targets.items():
        n += 1
        try:
            data = fetch(url)
            h = save(f"{n:02d}-openalex-{name}.json", data)
            js = json.loads(data)
            if "results" in js:
                items = [{"id": w.get("id"), "doi": w.get("doi"), "title": w.get("title"), "date": w.get("publication_date"), "cited_by": w.get("cited_by_count")} for w in js["results"]]
            else:
                items = [{"id": js.get("id"), "doi": js.get("doi"), "title": js.get("title"), "date": js.get("publication_date"), "cited_by": js.get("cited_by_count")}]
                resolved[name] = js.get("id")
            rec = {"name": "openalex-" + name, "url": url, "sha256": h, "bytes": len(data), "items": items}
        except Exception as ex:
            rec = {"name": "openalex-" + name, "url": url, "error": repr(ex)}
        summary["queries"].append(rec)
        time.sleep(1.0)
    for name, wid in resolved.items():
        if not wid:
            continue
        short = wid.rsplit("/", 1)[-1]
        url = OPENALEX + "works?filter=cites:" + short + "&per-page=100"
        n += 1
        try:
            data = fetch(url)
            h = save(f"{n:02d}-openalex-cites-{name}.json", data)
            js = json.loads(data)
            items = [{"id": w.get("id"), "doi": w.get("doi"), "title": w.get("title"), "date": w.get("publication_date")} for w in js.get("results", [])]
            rec = {"name": "openalex-cites-" + name, "url": url, "sha256": h, "bytes": len(data), "count": js.get("meta", {}).get("count"), "items": items}
        except Exception as ex:
            rec = {"name": "openalex-cites-" + name, "url": url, "error": repr(ex)}
        summary["queries"].append(rec)
        time.sleep(1.0)
    for name, params in DATACITE_QUERIES:
        n += 1
        url = DATACITE + urllib.parse.urlencode(params)
        try:
            data = fetch(url)
            h = save(f"{n:02d}-{name}.json", data)
            js = json.loads(data)
            items = []
            for d in js.get("data", []):
                at = d.get("attributes", {})
                t = at.get("titles") or [{}]
                items.append({"doi": at.get("doi"), "title": t[0].get("title"), "year": at.get("publicationYear"), "publisher": at.get("publisher")})
            rec = {"name": name, "url": url, "sha256": h, "bytes": len(data), "total": js.get("meta", {}).get("total"), "items": items}
        except Exception as ex:
            rec = {"name": name, "url": url, "error": repr(ex)}
        summary["queries"].append(rec)
        time.sleep(1.0)
    summary["finished_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    data = json.dumps(summary, indent=1, ensure_ascii=False).encode()
    h = save("summary.json", data)
    print("summary sha256", h, "bytes", len(data))


if __name__ == "__main__":
    main()
