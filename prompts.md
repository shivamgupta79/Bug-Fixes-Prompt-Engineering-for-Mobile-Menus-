# `prompts.md` — Reasoning Notebook (AI & Prompts Track)

Record your prompts, the model/tool used, and quick outcomes here. Keep it short but clear.

> Tip: Paste only the *final* prompts you used after refinement. Add 1–2 sentence notes on what changed and why.

---

## 1) Role Prompt
**Goal:** Tell the model who it is and what to do.

**Prompt (final):** You are an expert in accessibility and software debugging. Your job is to fix a buggy mobile menu (HTML/JS) to work perfectly for keyboard, screen reader, mouse, and to fix a Python script so it calculates averages correctly from a CSV file, even if the data is messy.
```
# paste your final "Role" prompt here

```

**Notes (1–2 lines):**
- …
Clearly describes the dual tasks for both UI (accessibility/mobile) and backend (robust CSV average).

Focused on user experience and correct data handling.
---

## 2) Constraints Prompt
**Goal:** List hard limits (no new libs, keep file names, show diff only, etc.).

**Prompt (final):**Do not add any new libraries. Only edit the provided files (buggy.html, buggy.py). Leave all file names as-is. Keep scripts and styles inline. Focus only on functional and accessibility improvements required by the task description.

```
# paste your final "Constraints" prompt here
```

**Notes (1–2 lines):**
- …
Ensures scope is limited to the assignment rules, avoids scope creep, and maintains file structure.

---

## 3) Critique → Refine Loop
**Goal:** Ask the model to critique the initial fix, then refine and re-test.

**Critique prompt (final):**Check this solution for accessibility, keyboard and mouse usability, ARIA compliance, and correct data handling for the average calculator. List any functional or accessibility issues still present.

```
# paste the exact critique prompt here
```

**Refine prompt (final):**Apply all required fixes based on your critique, ensuring: (1) The mobile menu toggles from both mouse and keyboard, ARIA expands/collapses correctly, and focus outline is visible at 360px width; (2) The Python script ignores header/blanks, skips bad numbers, and prints a valid two-decimal average.

```
# paste the exact refinement prompt here
```

**Notes:**
- What did the critique reveal?
- What changed in the refined fix?

---

## Tools / Models Disclosure
List the models/tools you used and versions if known (e.g., “GPT-4.1, VS Code, Chrome DevTools”).

- …

