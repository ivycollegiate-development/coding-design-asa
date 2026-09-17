# Lesson 03 — Roster Page, Part 1: Page Structure

**Coding/Design ASA (Tue/Thu 4:30–5:45 PM) — Thursday, September 17, 2026**
**Name: ______________________**

Today you start building the Teams screen of our basketball app with HTML — the page every visitor sees first. Work through the Parts in order. Every step tells you exactly what to click or type. If your screen does not look like what this lesson says, stop and raise your hand — do not guess.

**Links you will need**

- Your code workspace: https://vscode.ivycollegiate.org/ (sign in with your SCHOOL account — personal Gmail will not work)
- Your own repo: https://github.com/ivycollegiate-development/asa-roster-page-part1-YOURUSERNAME (private — replace YOURUSERNAME with your code-server username; the exact name is in the setup sheet below)
- Setup sheet: GitHub Account Setup — Coding/Design ASA (linked in today's Classwork assignment) — do this first if you have never cloned or pushed before
- Reference project repo: https://github.com/ivycollegiate-development/coding-design-asa
- Worksheet for today: HTML Basics — Roster Page Part 1 Worksheet 0917 (linked in today's Classwork assignment)

---

## Part 1 — Open your workspace and get today's file (10 min)

1. Open Chrome and go to https://vscode.ivycollegiate.org/ — click **Open your session** and sign in with your SCHOOL account.
2. Click **Terminal** in the menu bar at the top of the window, then click **New Terminal**.
3. Click inside the terminal, type exactly this, and press Enter after each line. **YOURUSERNAME is your code-server username — the exact repo name is in your row of the setup sheet.**

   ```
   git clone https://github.com/ivycollegiate-development/asa-roster-page-part1-YOURUSERNAME.git
   cd asa-roster-page-part1-YOURUSERNAME
   ```

   ☐ My terminal cloned the repo with no red text. If it shows anything red, raise your hand.

4. In the file tree on the left, click the folder named `03-roster-table`, then double-click the file named `index.html`. It opens in the editor.

   ☐ I can see `index.html` open with words like `<!DOCTYPE html>` and `<table>` in it.

---

## Part 2 — Learn the anatomy of a web page (15 min — we do this together)

As we code along, fill in each blank. Ask before you type anything I have not said.

1. The first line of the file is the doctype. It tells the browser: ______________________________________
2. Every tag except the doctype comes in a pair. Write the CLOSING tag for each opening tag:

   ```
   <html>  closes with: ________        <head>  closes with: ________
   <body>  closes with: ________        <h1>    closes with: ________
   <title> closes with: ________        <tr>    closes with: ________
   ```

3. The two main rooms of the page:

   ☐ The `<head>` holds things the visitor does NOT see, like the `<title>` that appears on the browser tab.
   ☐ The `<body>` holds everything the visitor DOES see: the heading, the table, the text.

4. Everything a visitor sees goes between ________ and ________ .
5. What the `<h1>` tag does: ______________________________________

   ☐ I can point to each part of `index.html`: doctype, `<html>`, `<head>` with `<title>`, `<body>` with `<h1>` and `<table>`.

---

## Part 3 — Break it and fix it (10 min — the tag drill)

The fastest way to learn tags is to break a page on purpose. Preview your page first:

1. Click inside the terminal, type exactly this, and press Enter:

   ```
   python3 -m http.server 8000
   ```

2. A line appears that says `Serving HTTP on 0.0.0.0 port 8000`. Leave it running — do not close it.
3. Press **Ctrl + Shift + P** (**Cmd + Shift + P** on a Mac), type `simple`, then click **Simple Browser: Show**. In the box type:

   ```
   http://localhost:8000/03-roster-table/index.html
   ```

   and press Enter. Your roster page appears in a tab inside the editor. Do not close the terminal.

   ☐ My page shows a heading and a table with a navy header row.

Now break it:

4. In `index.html`, delete ONLY the `</h1>` tag (keep `<h1>`). Press **Ctrl + S** (**Cmd + S**) to save, then click the refresh icon in the Simple Browser. What changed? ______________________________________
5. Put `</h1>` back. Now delete ONLY one `</td>` in the row for Player Two. Save, refresh the Simple Browser. What went wrong with the table? ______________________________________
6. Fix the `</td>`. Save, refresh. The table is back to normal.

   ☐ I fixed both breaks and the page looks right again. Lesson: every opening tag needs its closing tag, or the browser guesses — and browsers guess badly.

---

## Part 4 — Make it yours (10 min)

1. Change the heading `Our Team Roster` to your own team name. Keep the `<h1>` and `</h1>` around it.
2. Below the row that says Paul Jones, add a row for YOURSELF, exactly in this shape (type it under the Paul Jones line):

   ```
   <tr><td>Your Name</td><td>Your Number</td><td>Guard</td></tr>
   ```

   (Use your real name, any jersey number you like, and a position: Guard, Forward, or Center.)

3. Save, then refresh the Simple Browser. Your row must appear in the table.

   ☐ My team name is the heading, and my row shows in the table.

---

## Part 5 — Push your work to GitHub (5 min)

1. Click in the terminal — press **Ctrl + C** once to stop the little server, then type exactly this, pressing Enter after each line:

   ```
   git add .
   git commit -m "roster page part 1"
   git push
   ```

   Warning: the first push asks for your GitHub **username** and then a **password**. The password is a Personal Access Token, never your GitHub password — see Part E of the setup sheet. If you do not have a token yet, raise your hand and we do it together.

   ☐ The push ended with something like `Writing objects: 100%`.

---

## Part 6 — Send me proof (5 min)

1. Take a screenshot of your Simple Browser showing your finished page (heading + table with your row).
   - Chromebook: hold **Ctrl + Shift** and press the **Show windows** key
   - Windows: **Windows key + Shift + S**
   - Mac: **Cmd + Shift + 4**
   - iPad: side button + volume-up
2. Go to Google Classroom, click **Classwork**, click **HTML Basics — Roster Page, Part 1: Page Structure**, then **View assignment**.
3. Under **Your work**, click **Add or create**, click **File**, upload your screenshot, then click **Turn in** twice.

   ☐ My screenshot is attached and the assignment shows **Turned in**.

---

## Part 7 — Look at the roster page code (10 min)

1. Read the code you just wrote. Find and circle these in the editor: the doctype, the `<head>` block, the `<h1>` heading, and the `<table>`.
2. Every row in the table starts with `<tr>`. Count the `<tr>` tags in your file and write the number here: ________
3. Fill in the blanks from your own page:

   ☐ My team name in the heading is: ______________________________________
   ☐ My row in the table says: ______________________________________
   ☐ One tag I can explain to the person next to me: ______________________

---

## Exit Ticket

☐ Part 1   ☐ Part 2   ☐ Part 3   ☐ Part 4   ☐ Part 5   ☐ Part 6   ☐ Part 7

One thing that confused me today (be honest — I will fix it): ____________________________________________________________________

One thing I made work all by myself: ____________________________________________________________________

The exact step number where I got stuck: ________     The message on my screen said: ______________________

My confidence in writing HTML right now (circle one):   1   2   3   4   5

**Done early?** Help a classmate get their row on the table. Do NOT start adding columns or more players — that is Part 2 next Tuesday.
