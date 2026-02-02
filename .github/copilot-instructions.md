This repository is a personal Python learning workspace with many small exercise scripts and a simple Jenkins-related folder. The guidance below helps an AI assistant work productively in this codebase.

Key points
- Purpose: mainly learning exercises and small scripts (folders `Codewars/`, `CS50/`, `MSUcoursesDataAnalysisWithPython/`, `Weksler/`). Most files are standalone Python scripts you can run directly with the local Python interpreter.
- Test/build: there is no central test harness or package. `jenkins-server/requirements.txt` contains `selenium` — treat that folder as a lightweight automation project.

Repository layout examples
- `Codewars/` and `Codewars/codewars/` — many kata solutions as one-file scripts. Prefer minimal, self-contained changes and preserve example prints used as quick checks (e.g. `Find Fibonacci last digit.py`).
- `CS50/` — course exercises and modules; `__init__.py` is present in some folders indicating package-style usage.
- `jenkins-server/` — contains `requirements.txt` with `selenium`; follow typical Selenium setup when adding automation code.

Conventions & patterns (discoverable)
- Single-file scripts: Many files are simple functions with a `print(...)` call at the bottom for manual verification. When editing, keep the top-level runnable behavior unchanged unless fixing a bug.
- No centralized packaging: don't add heavyweight packaging changes. If you need dependencies, update or add a `requirements.txt` next to the folder that needs it (example: `jenkins-server/requirements.txt`).
- Naming: filenames often contain spaces and capitals (e.g. `Find Fibonacci last digit.py`). When creating imports or tests, prefer snake_case module names; but avoid renaming files unless requested.

How to run files locally
- Use the repository Python (virtualenv/venv if present). On Windows PowerShell use:

```powershell
python "Codewars\codewars\Find Fibonacci last digit.py"
python "CS50\mario.py"
```

Quick edit guidance for AI
- Preserve top-level prints and minimal input/output formats used for manual verification.
- When improving a single kata file, return the same function name and signature (e.g. `get_last_digit(index)` in `Find Fibonacci last digit.py`).
- Prefer small, well-scoped edits; add a short comment explaining non-obvious changes.

Integration points / external dependencies
- `jenkins-server/requirements.txt` lists `selenium`. Any automation code should assume Selenium is the intended dependency for that folder.

Examples from repo
- Fix a bug: `Codewars\codewars\Find Fibonacci last digit.py` — function `get_last_digit(index)` returns last digit using modulo 10 in loop; keep that approach for efficiency.
- Add tests: there is no test framework present; add small ad-hoc assertions at bottom of edited files (e.g. `assert get_last_digit(15) == 0`) or create a new `tests/` folder if asked.

When to ask the human
- If a change requires renaming many files, adding a packaging tool (pip/poetry), or changing repository structure, ask before proceeding.

If you have questions about missing policies or CI steps, prompt the maintainer for preferred test/packaging workflows.

End of guidance.
