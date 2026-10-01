# Lesson 01 — Hello HTML, Part 1: Your First Web Page

**Coding/Design ASA (Tue/Thu 4:30–5:45 PM) — Lesson 01**
**Name: ______________________**

Today you open your first web page and make it yours. Every page you build this semester starts from a file like this one. Work through the Parts in order. Every step tells you exactly what to click or type. If your screen does not look like what this lesson says, stop and raise your hand — do not guess.

**Links you will need**

- Your code workspace: https://vscode.ivycollegiate.org/ (sign in with your SCHOOL account — personal Gmail will not work)
- Your own repo: named `asa-roster-page-part1-` + your code-server username + `_student` (example: username `cyen29` → repo `asa-roster-page-part1-cyen29_student`). Note the two punctuation rules: a **dash** before your username, an **underscore** before `student`. You do NOT type your username anywhere — the command in Part 1 works it out for you with `$(whoami)`. Because every student has a different repo, this is not one clickable link; to open yours in a browser: sign in at https://github.com, click your profile icon (top right), then **Your repositories**.
- Setup sheet: GitHub Account Setup — Coding/Design ASA (linked in today's Classwork assignment) — do this first if you have never cloned or pushed before
- Reference project repo: https://github.com/ivycollegiate-development/coding-design-asa

---

## Part 1 — Open your workspace and get today's file (10 min)

1. Open Chrome and go to https://vscode.ivycollegiate.org/ — click **Open your session** and sign in with your SCHOOL account.
2. Click **Terminal** in the menu bar at the top of the window, then click **New Terminal**.
3. Click inside the terminal, type exactly this, and press Enter after each line. **Copy it exactly — `$(whoami)` is not a typo, it fills in your username for you.** The folder on your computer is always named `asa-roster-page-part1` — the same for everyone, so nobody clones into a differently-named folder by accident.

   ```
   git clone https://github.com/ivycollegiate-development/asa-roster-page-part1-$(whoami)_student.git asa-roster-page-part1
   cd asa-roster-page-part1
   ```

   ☐ My terminal cloned the repo with no red text. If it says `repository not found`, your username is not spelled the way your repo is — compare the two and raise your hand.

4. Prove it worked: type `ls` and press Enter. You should see `01-hello-html`, `02-menu-buttons`, `03-roster-table`, `README.md`, and `self_check.py`.

5. In the file tree on the left, click the folder named `01-hello-html`, then double-click the file named `index.html`. It opens in the editor.

   ☐ I can see `index.html` open with words like `<!DOCTYPE html>` and `<h1>` in it.

**Already cloned before?** Skip step 3. Just pull, then open the file:

```
cd asa-roster-page-part1
git config pull.rebase false
git pull
```

Same folder name every session. If you ever get `already exists` when cloning, you already have the folder — use the pull block instead.

---

## Part 2 — Meet the parts of the page (10 min — we do this together)

Do not type anything yet. Just read along in the editor and find each of these with me.

1. The very first line is `<!DOCTYPE html>`. It has no closing tag. It tells the browser which rules to follow.
2. Everything a visitor SEES lives between `<body>` and `</body>`. Find the three `<p>` lines — those are the three sentences on the page.
3. `<h1>` is the big heading at the top. `<p>` is an ordinary paragraph.

   ☐ I can point to `<!DOCTYPE html>`, the `<body>` block, the `<h1>`, and the `<p>` lines.

4. Notice the `____` blank lines. Those are where YOU write. Every lesson this semester has blanks waiting for you.

   ☐ I found the three blanks.

---

## Part 3 — Make it yours (10 min)

1. Click right before the first `____` on the `My name is:` line and type your name. Do the same for the other two lines.
2. On the third line (`One thing I want our app to do:`), type one thing you want the basketball app to do. Keep it under ten words.
3. Add a fourth line directly below the third one, exactly like this:

   ```
   <p>My number is: 23</p>
   ```

   Change `23` to any number you like.

4. Change the `<h1>` so it greets YOU by name — `<h1>Hello, Paul!</h1>` becomes `<h1>` plus your name.

5. Press **Ctrl + S** (**Cmd + S** on a Mac) to save.

   ☐ All three blanks are filled in, I added a fourth line, and the heading says my name.

---

## Part 4 — See your page in a browser (5 min)

1. Click in the terminal, type exactly this, and press Enter:

   ```
   python3 -m http.server 8000
   ```

2. A line appears that says `Serving HTTP on 0.0.0.0 port 8000`. Leave it running — do not close it.
3. Press **Ctrl + Shift + P** (**Cmd + Shift + P** on a Mac), type `simple`, then click **Simple Browser: Show**. In the box type:

   ```
   http://localhost:8000/01-hello-html/index.html
   ```

   and press Enter. Your page appears in a tab inside the editor.

   ☐ My page shows my name in the heading and my four lines of text.

---

## Part 5 — Push your work to GitHub (5 min)

1. Click in the terminal — press **Ctrl + C** once to stop the little server, then type exactly this, pressing Enter after each line:

   ```
   git config pull.rebase false
   git pull
   git add .
   git commit -m "hello html page 1"
   git push
   ```

   Warning: the first push asks for your GitHub **username** and then a **password**. The password is a Personal Access Token, never your GitHub password — see Part E of the setup sheet. If you do not have a token yet, raise your hand and we do it together.

   ☐ The push ended with something like `Writing objects: 100%`.

---

## Part 6 — Send me proof (5 min)

1. Take a screenshot of your Simple Browser showing your finished page (heading with your name, your four filled-in lines).

   - Chromebook: hold **Ctrl + Shift** and press the **Show windows** key
   - Windows: **Windows key + Shift + S**
   - Mac: **Cmd + Shift + 4**
   - iPad: side button + volume-up

2. Go to Google Classroom, click **Classwork**, click today's assignment, then **View assignment**.
3. Under **Your work**, click **Add or create**, click **File**, upload your screenshot, then click **Turn in** twice.

   ☐ My screenshot is attached and the assignment shows **Turned in**.

---

## Exit Ticket

☐ Part 1   ☐ Part 2   ☐ Part 3   ☐ Part 4   ☐ Part 5   ☐ Part 6

One thing that confused me today (be honest — I will fix it): ____________________________________________________________________

One thing I made work all by myself: ____________________________________________________________________

The exact step number where I got stuck: ________     The message on my screen said: ______________________

My confidence in writing HTML right now (circle one):   1   2   3   4   5

**Done early?** Help a classmate get their page showing in their browser. Do NOT start the menu buttons — that is L02.
