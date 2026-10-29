"""Assemble index.html from page.tmpl.html + the demo component (demo.css/html/js) + the abstract.
    python3 build/build.py
"""
import os, re
B = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(B)
r = lambda f: open(os.path.join(B, f), encoding="utf-8").read()
s = r("page.tmpl.html")
for k, f in [("/*__DEMO_CSS__*/", "demo.css"), ("__DEMO_HTML__", "demo.html"), ("__DEMO_JS__", "demo.js"), ("__ABSTRACT__", "abstract.txt")]:
    assert s.count(k) == 1, k; s = s.replace(k, r(f).strip())
open(os.path.join(R, "index.html"), "w", encoding="utf-8").write(s)
print("wrote index.html", len(s) // 1000, "KB")
