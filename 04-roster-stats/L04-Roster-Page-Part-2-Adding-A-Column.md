# Lesson 04 — Roster Page, Part 2: Adding a Column

**Coding/Design ASA (Tue/Thu 4:30–5:45 PM) — Lesson 04**
**Name: ______________________**

In L03 you built the Teams screen with a heading and a three-column table. Today you add a **fourth column** — points per game — and fill the whole table with real data. This is the hardest table you will build by hand, and it is the last step before your menu button actually links to a real screen. Work through the Parts in order. Every step tells you exactly what to click or type. If your screen does not look like what this lesson says, stop and raise your hand — do not guess.

**Links you will need**

- Your code workspace: https://vscode.ivycollegiate.org/ (sign in with your SCHOOL account — personal Gmail will not work)
- Your own repo: named `asa-roster-page-part1-` + your code-server username + `_student` (example: username `cyen29` → repo `asa-roster-page-part1-cyen29_student`). Note the two punctuation rules: a **dash** before your username, an **underscore** before `student`. You do NOT type your username anywhere — the command in Part 1 works it out for you with `$(whoami)`. Because every student has a different repo, this is not one clickable link; to open yours in a browser: sign in at https://github.com, click your profile icon (top right), then **Your repositories**.
- Reference project repo: https://github.com/ivycollegiate-development/coding-design-asa

---

## Part 1 — Open your workspace and pull today's file (5 min)

1. Open Chrome and go to https://vscode.ivycollegiate.org/ — click **Open your session** and sign in with your SCHOOL account.
2. Click **Terminal** in the menu bar at the top of the window, then click **New Terminal**.
3. Click inside the terminal, type exactly this, and press Enter after each line. You already cloned this repo in L01 — you are pulling, not cloning again.

   ```
   cd asa-roster-page-part1
   git config pull.rebase false
   git pull
   ```

   ☐ My terminal pulled with no red text. If it says `could not read Username`, your clone is missing — go back to L01 Part 1 and clone it.

4. In the file tree on the left, click the folder named `04-roster-stats`, then double-click the file named `index.html`. It opens in the editor.

   ☐ I can see `index.html` open with `Points per game` in the header row.

**Never cloned?** Use the full block from L01 Part 1 instead — it clones your repo into the folder `asa-roster-page-part1`.

---

## Part 2 — Learn how a column works (15 min — we do this together)

A table has three kinds of tags and you have already used all of them. What changes today is that there are now **four** of something instead of three.

1. Look at the header row. It is made of `<th>` tags — four of them:

   ```
   <tr><th>Name</th><th>Number</th><th>Position</th><th>Points per game</th></tr>
   ```

   Count them with me: 1, 2, 3, 4. **One `<th>` per column.**

2. Now look at a data row. It is made of `<td>` tags — also four of them:

   ```
   <tr><td>Paul Jones</td><td>1</td><td>Coach</td><td>—</td></tr>
   ```

3. Here is the rule that matters most today: **every row must have the same number of cells.** If one row has four and the next has three, the browser shifts everything sideways and the table looks broken.

4. Look at the coach's row. Its last cell is `—`, which is an em dash, not a number. In L03 that was fine because that column did not exist yet. Today every cell in the Points column must hold a real number.

   ☐ I can count four `<th>` tags in the header and four `<td>` tags in a data row.

   ☐ I know that rows with different numbers of cells break the table.

---

## Part 3 — Build your four-column table (15 min)

1. Replace `Player Two` and `Player Three` with two classmates' real names. **Ask them** — do not guess.
2. Add a row for YOURSELF directly below the coach's row, exactly like this:

   ```
   <tr><td>Your Name</td><td>12</td><td>Forward</td><td>0.0</td></tr>
   ```

   Use your real name, any jersey number, a position (Guard, Forward, or Center), and `0.0` for now.
3. Now go down the **Points per game** column cell by cell and put a real number in every one — including the coach's `—`. Ask your classmates for their number; make one up for your own row.

4. Count your cells: every row must now have exactly four. Read each row out loud and count with me.

   ☐ Both starter names are real classmates.

   ☐ I added my own row.

   ☐ Every cell in the Points per game column is a real number, and the coach's `—` is gone.

5. Press **Ctrl + S** (**Cmd + S** on a Mac) to save.

---

## Part 4 — See your table and check your work (10 min)

1. Click in the terminal, type exactly this, and press Enter:

   ```
   python3 -m http.server 8000
   ```

2. A line appears that says `Serving HTTP on 0.0.0.0 port 8000`. Leave it running — do not close it.
3. Press **Ctrl + Shift + P** (**Cmd + Shift + P** on a Mac), type `simple`, then click **Simple Browser: Show**. In the box type:

   ```
   http://localhost:8000/04-roster-stats/index.html
   ```

   and press Enter.

   ☐ My page shows a table with FOUR columns, and every row lines up straight.

4. Click in the terminal, type exactly this, and press Enter:

   ```
   python3 self_check_stats.py
   ```

5. It should say `2 of 4 checks passing`. The only two FAILs should be `every points cell is a real number` and `work committed`. Any other FAIL line tells you exactly what to fix — read the message in the parentheses.

   ☐ My self-check says `2 of 4`, and the only FAILs are the points column and the commit.

6. Also run the L03 check to be sure you did not break Part 1's work:

   ```
   python3 self_check.py
   ```

   It should still say `4 of 4 checks passing`. If it does not, you changed something in `03-roster-table/index.html` — go back and fix it before you go on.

---

## Part 5 — Push your work to GitHub (5 min)

1. Click in the terminal — press **Ctrl + C** once if a server is still running, then type exactly this, pressing Enter after each line:

   ```
   git config pull.rebase false
   git pull
   git add .
   git commit -m "roster page part 2 fourth column"
   git push
   ```

   ☐ The push ended with something like `Writing objects: 100%`.

2. Run `python3 self_check_stats.py` one last time — it should now say `4 of 4 checks passing`. My grade bot runs the same checks on github.com after every push: open your repo, click the **Actions** tab, look for the green check.

   ☐ The Actions tab shows a green check and `4 of 4`.

---

## Part 6 — Send me proof (5 min)

1. Take a screenshot of your Simple Browser showing your four-column table.

   - Chromebook: hold **Ctrl + Shift** and press the **Show windows** key
   - Windows: **Windows key + Shift + S**
   - Mac: **Cmd + Shift + 4**
   - iPad: side button + volume-up

Then take a second screenshot of your repo on github.com — the **Actions** tab, where my grade bot posts your score (looking for **4 of 4 checks passing**).

2. Go to Google Classroom, click **Classwork**, click today's assignment, then **View assignment**.
3. Under **Your work**, click **Add or create**, click **File**, upload your screenshots, then click **Turn in** twice.

   ☐ My screenshot is attached and the assignment shows **Turned in**.

---

## Part 7 — Look at the code you wrote (5 min)

1. Find and circle in the editor: the four `<th>` tags in the header row, and one complete data row with all four of its `<td>` tags.
2. Fill in the blanks from your own table:

   ☐ My table has ______ rows (count them).

   ☐ The points per game for ____________ is ______.

   ☐ One mistake I made and fixed: ______________________________________

---

## Exit Ticket

☐ Part 1   ☐ Part 2   ☐ Part 3   ☐ Part 4   ☐ Part 5   ☐ Part 6   ☐ Part 7

One thing that confused me today (be honest — I will fix it): ____________________________________________________________________

One thing I made work all by myself: ____________________________________________________________________

The exact step number where I got stuck: ________     The message on my screen said: ______________________

My confidence in writing HTML right now (circle one):   1   2   3   4   5

**Done early?** Help a classmate find the row where the cell count does not match. Do NOT add a fifth column — we link the menu button to this screen in L05.
