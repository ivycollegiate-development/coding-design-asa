# Lesson 02 — Menu Buttons, Part 1: The Main Menu

**Coding/Design ASA (Tue/Thu 4:30–5:45 PM) — Lesson 02**
**Name: ______________________**

Today you build the main menu of our basketball app — the screen with three big rounded buttons. This is the prototype I showed you at the start of the unit, and it is the first thing that starts to look like a real app. Work through the Parts in order. Every step tells you exactly what to click or type. If your screen does not look like what this lesson says, stop and raise your hand — do not guess.

**Links you will need**

- Your code workspace: https://vscode.ivycollegiate.org/ (sign in with your SCHOOL account — personal Gmail will not work)
- Your own repo: named `asa-roster-page-part1-` + your code-server username + `_student` (example: username `cyen29` → repo `asa-roster-page-part1-cyen29_student`). Note the two punctuation rules: a **dash** before your username, an **underscore** before `student`. You do NOT type your username anywhere — the command in Part 1 works it out for you with `$(whoami)`. Because every student has a different repo, this is not one clickable link; to open yours in a browser: sign in at https://github.com, click your profile icon (top right), then **Your repositories**.
- Setup sheet: GitHub Account Setup — Coding/Design ASA (linked in today's Classwork assignment) — do this first if you have never cloned or pushed before
- Reference project repo: https://github.com/ivycollegiate-development/coding-design-asa

---

## Part 1 — Open your workspace and get today's file (5 min)

1. Open Chrome and go to https://vscode.ivycollegiate.org/ — click **Open your session** and sign in with your SCHOOL account.
2. Click **Terminal** in the menu bar at the top of the window, then click **New Terminal**.
3. Click inside the terminal, type exactly this, and press Enter after each line. You already cloned this repo in L01 — you are pulling, not cloning again.

   ```
   cd asa-roster-page-part1
   git config pull.rebase false
   git pull
   ```

   ☐ My terminal pulled with no red text. If it says `could not read Username`, your clone is missing — go back to L01 Part 1 and clone it.

4. In the file tree on the left, click the folder named `02-menu-buttons`, then double-click the file named `index.html`. It opens in the editor.

   ☐ I can see `index.html` open with three lines that say Teams, New Game, and Pro Account.

**Never cloned?** Use the full block from L01 Part 1 instead — it clones your repo into the folder `asa-roster-page-part1`.

---

## Part 2 — Learn what makes a button look like (15 min — we do this together)

The page has two rooms today, and you have already met one of them.

1. The `<style>` block sits inside `<head>` — the room the visitor does NOT see. It holds the rules for how things LOOK.

   ☐ The `<style>` block is in `<head>`, not `<body>`.

2. Inside `<style>` there is one rule called `.menu-button`. Read it out loud with me, piece by piece:

   - `display: block` — each button goes on its own line, stacked.
   - `width: 200px` — how wide each button is.
   - `margin: 20px auto` — space above and below, centered.
   - `padding: 20px` — space INSIDE the button.
   - `text-align: center` — the words sit in the middle.
   - `background: #1B2A4A` — the navy fill.
   - `color: #C9A227` — the gold words.
   - `font-size: 20px` — how big the words are.
   - `border-radius: 16px` — this is what makes the corners ROUNDED.
   - `text-decoration: none` — removes the underline that links normally get.

3. The three buttons are `<a>` tags, not `<button>` tags. Each one has `class="menu-button"`, which is how a tag says "use the `.menu-button` rule."

   ☐ I can explain why the buttons look the way they do: the `.menu-button` rule does it, and `class="menu-button"` connects the tag to that rule.

---

## Part 3 — Make it yours (10 min)

1. In the `<style>` block, find `background: #1B2A4A`. Change `#1B2A4A` to your own team's color. Use the same six-character code you used in L03's table, or ask me for one.

   ☐ I changed the background color and I can say what my color is: ______________________

2. Add a fourth button directly below the Pro Account line, exactly like this:

   ```
   <a class="menu-button" href="#">My Screen</a>
   ```

   Change `My Screen` to a screen YOU invented — a box score, a stats page, a schedule. One or two words.

3. Press **Ctrl + S** (**Cmd + S** on a Mac) to save.

   ☐ My page has four buttons and my team color.

---

## Part 4 — See your menu in a browser (5 min)

1. Click in the terminal, type exactly this, and press Enter:

   ```
   python3 -m http.server 8000
   ```

2. A line appears that says `Serving HTTP on 0.0.0.0 port 8000`. Leave it running — do not close it.
3. Press **Ctrl + Shift + P** (**Cmd + Shift + P** on a Mac), type `simple`, then click **Simple Browser: Show**. In the box type:

   ```
   http://localhost:8000/02-menu-buttons/index.html
   ```

   and press Enter. Your menu appears in a tab inside the editor.

   ☐ My page shows four rounded buttons stacked in the center, in my team color.

4. Try one experiment: in the `<style>` block, change `border-radius: 16px` to `border-radius: 0px`. Save, refresh the Simple Browser. What changed? ______________________________________

   Now put `16px` back. Save, refresh.

   ☐ I changed the border-radius and put it back. The corners go from rounded to square when it is `0px`.

---

## Part 5 — Push your work to GitHub (5 min)

1. Click in the terminal — press **Ctrl + C** once to stop the little server, then type exactly this, pressing Enter after each line:

   ```
   git config pull.rebase false
   git pull
   git add .
   git commit -m "menu buttons page 2"
   git push
   ```

   ☐ The push ended with something like `Writing objects: 100%`.

---

## Part 6 — Send me proof (5 min)

1. Take a screenshot of your Simple Browser showing all four buttons in your team color.

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

**Done early?** Help a classmate find the one CSS line that controls the rounded corners. Do NOT start the roster table — that is L03.
