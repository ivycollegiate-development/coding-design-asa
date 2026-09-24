"""Self-check for the Roster Page lab. Run: python3 self_check.py

Starts at 3 of 4 passing. Your job: make it 4 of 4, commit, push.
"""
import os, re, subprocess

PAGE = "03-roster-table/index.html"
results = []

def check(name, fn):
    try:
        ok, msg = fn()
    except Exception as e:
        ok, msg = False, f"error: {e}"
    results.append((name, ok, msg))
    print(("PASS  " if ok else "FAIL  ") + name + (f"  ({msg})" if msg and not ok else ""))

def page_exists():
    return (os.path.exists(PAGE), "missing " + PAGE)

def content_ready():
    if not os.path.exists(PAGE):
        return (False, PAGE + " not found")
    src = open(PAGE).read()
    h1 = re.search(r"<h1>(.*?)</h1>", src)
    generic = (h1 is None) or ("Our Team Roster" in h1.group(1)) or (not h1.group(1).strip())
    placeholders = [p for p in ("Player Two", "Player Three") if p in src]
    rows = len(re.findall(r"<tr\b", src))
    problems = []
    if generic:
        problems.append("heading is still the starter text - change <h1> to YOUR team name")
    if placeholders:
        problems.append("starter placeholder(s) still present: " + ", ".join(placeholders))
    if rows < 4:
        problems.append(f"only {rows} table row(s) - add your own row")
    return (not problems, "; ".join(problems))

def tags_paired():
    if not os.path.exists(PAGE):
        return (False, PAGE + " not found")
    src = open(PAGE).read()
    bad = []
    for tag in ("html", "head", "body", "title", "h1", "table", "tr", "td", "th"):
        opens = len(re.findall(rf"<{tag}\b", src))
        closes = len(re.findall(rf"</{tag}>", src))
        if opens != closes:
            bad.append(f"<{tag}>: {opens} opening / {closes} closing")
    return (not bad, "unbalanced: " + "; ".join(bad))

def committed():
    p = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    return (p.stdout.strip() == "", "uncommitted changes -- git add / commit / push")

check("starter page exists", page_exists)
check("your team name + your row", content_ready)
check("tags all paired", tags_paired)
check("work committed", committed)

passed = sum(1 for _, ok, _ in results if ok)
print(f"\n{passed} of {len(results)} checks passing")
