"""Self-check for the Roster Stats lab. Run: python3 self_check_stats.py

Builds on self_check.py from L03. Run BOTH — this one checks the fourth column.
Starts at 2 of 4 passing. Your job: make it 4 of 4, commit, push.
"""
import os, re, subprocess

PAGE = "04-roster-stats/index.html"
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

def fourth_column():
    if not os.path.exists(PAGE):
        return (False, PAGE + " not found")
    src = open(PAGE).read()
    header = re.search(r"<tr>(<th>.*?</tr>)", src, re.S)
    if not header:
        return (False, "no header row found")
    if "Points per game" not in header.group(1):
        return (False, "the header row is missing the 'Points per game' column")
    rows = re.findall(r"<tr>(.*?)</tr>", src, re.S)
    bad = []
    for i, row in enumerate(rows):
        cells = len(re.findall(r"<t[hd]\b", row))
        if cells != 4:
            bad.append(f"row {i + 1} has {cells} cell(s), not 4")
    return (not bad, "; ".join(bad))

def points_filled():
    if not os.path.exists(PAGE):
        return (False, PAGE + " not found")
    src = open(PAGE).read()
    bad = []
    for row in re.findall(r"<tr>(.*?)</tr>", src, re.S)[1:]:
        cells = re.findall(r"<td>(.*?)</td>", row, re.S)
        if len(cells) < 4:
            continue
        val = cells[3].strip()
        try:
            float(val)
        except ValueError:
            bad.append(f"'{val}' is not a number")
    return (not bad, "; ".join(bad) if bad else "")

def committed():
    p = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    return (p.stdout.strip() == "", "uncommitted changes -- git add / commit / push")

check("stats page exists", page_exists)
check("fourth column added to every row", fourth_column)
check("every points cell is a real number", points_filled)
check("work committed", committed)

passed = sum(1 for _, ok, _ in results if ok)
print(f"\n{passed} of {len(results)} checks passing")
