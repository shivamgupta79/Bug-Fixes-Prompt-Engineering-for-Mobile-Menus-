# Bug-Fixes-Prompt-Engineering-for-Mobile-Menus-

# AI & Prompts Track — Starter Pack

## What you’ll make
Use prompt engineering to improve or fix a small task and show your reasoning trail. You'll work on a broken UI snippet and a buggy Python average calculator.

## You received (this pack)
- `buggy.html` — mobile menu issue
- `buggy.py` — average calculation bug
- `marks.csv` — example input data
- `prompts.md` — notebook to record prompts and outcomes
- `README.md` — this file

---

## Base task (finish this first)

### 1) Fix the UI
- Make the menu open/close on mobile screens (≤ 640px width).
- Make it keyboard-friendly (toggle via Enter/Space keys, visible focus styles, proper `aria-expanded` attribute updates).

### 2) Fix the Python
- Compute the correct average from `marks.csv`.
- Ignore the header and any blank lines.
- Handle bad values gracefully (skip invalid entries without crashing).
- Print the average with **two decimals** (e.g., `84.67`).

### 3) Document your prompts using three prompt patterns
- **Role** — Specify the model's role (e.g., “You are a front-end accessibility reviewer…”).
- **Constraints** — List limits (no new libraries, keep file names, show diff only).
- **Critique → Refine** — Ask the model to critique the first fix, then refine and re-test.

---

## Bonus (time permitting)
- Create an accessibility checklist for the menu (focus order, ARIA attributes).
- Write two tiny unit tests for the average function, documented via prompts.

---

## Acceptance checklist
- Menu works on **360px** to **640px** screens; toggles via click **and keyboard**; focus styles are visible.
- Average calculation is correct to **two decimals**; non-numeric rows skipped gracefully.
- `prompts.md` contains at least **3 prompts** (Role, Constraints, Critique→Refine) with short notes.
- Changes are limited to provided files (or clearly listed if others are changed).

---

## How to run / test

### UI
1. Open `buggy.html` in a browser.
2. Narrow the viewport to between 360px and 640px wide.
3. Verify the menu button toggles the menu via mouse **and** keyboard; focus styles are visible when tabbing.

### Python
- This reads `marks.csv` from the same folder and prints the (previously buggy) average.
- Your fix should print the correct average with **two decimals**.

---

## Submission format
Zip the pack and name it:  
`AI_Dept-Year_Name[_Teammate].zip`

Include `prompts.md`. Submit by the *Last Date & Time* as announced.

---

## Rules & disclosures
- AI assistance is encouraged; disclose any models/tools used inside `prompts.md`.
- Keep contributions your own; credit any external snippets or templates.

---
