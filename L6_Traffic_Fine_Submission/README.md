# Lab 6 – Code and Branch Coverage Analysis
## Traffic Fine Calculator

This submission tests the supplied `traffic_fine.py` application from the assigned
`L6_L7_27_traffic_fine` repository. The application logic is retained unchanged.

## Folder contents

| File | Purpose |
|---|---|
| `traffic_fine.py` | Application under test |
| `CodeCoverageTest_PES1UG24AM209_traffic_fine.py` | Test suite for line/code coverage |
| `BranchCoverageTest_PES1UG24AM209_traffic_fine.py` | Test suite covering both outcomes of decisions |
| `requirements.txt` | Python test dependencies |
| `reports/` | Reproducible text reports from the test runs |
| `screenshots/README.md` | Instructions for capturing the required terminal screenshots |

## Setup (Windows PowerShell)

Open PowerShell in this folder and run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

If PowerShell blocks activation, use `py -m pip install -r requirements.txt` and
run the commands below with `py -m coverage` instead of `coverage`.

## 1. Code coverage run

```powershell
coverage erase
coverage run -m pytest -v CodeCoverageTest_PES1UG24AM209_traffic_fine.py
coverage report -m
```

The target is at least 90% code/line coverage.

## 2. Branch coverage run

```powershell
coverage erase
coverage run --branch -m pytest -v BranchCoverageTest_PES1UG24AM209_traffic_fine.py
coverage report -m
```

The target is at least 90% branch coverage. The branch test suite exercises the
true and false outcomes of the decisions, including boundary values.

## Notes

- The two test suites are deliberately separate to support the two required commits.
- Run the commands from this directory so `traffic_fine.py` is importable.
- Coverage reports are generated from the actual tests. Re-run the commands after
  any change to the application or tests.
- The `screenshots/` folder contains instructions, not fabricated terminal captures.
  Save your own terminal screenshots there after running the commands successfully.

## Verified results in this package

The included reports were produced by running the test suites against the
provided application file in this package:

- Code/line coverage of `traffic_fine.py`: **97%** (35 statements, 1 missed).
- Branch-enabled coverage of `traffic_fine.py`: **100%** (26 branches, 0 partial).
- Code coverage suite: 3 tests passed.
- Branch coverage suite: 4 tests passed.

The overall TOTAL row also includes the test file itself; use the `traffic_fine.py`
row when reporting application coverage.

## Suggested two-commit Git workflow

Run these from this folder after adding it to your own repository:

```powershell
git add traffic_fine.py CodeCoverageTest_PES1UG24AM209_traffic_fine.py reports/code_coverage.txt
git commit -m "Add traffic fine code coverage tests and report"

git add BranchCoverageTest_PES1UG24AM209_traffic_fine.py reports/branch_coverage.txt
git commit -m "Add traffic fine branch coverage tests and report"

git add README.md requirements.txt .gitignore screenshots/
git commit -m "Add Lab 6 submission instructions and screenshots"
```

The handout requires at least two commits; these commands create separate commits
for code coverage and branch coverage, plus an optional third documentation commit.
