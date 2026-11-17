# Lab 7 – Fuzz Testing for Input Validation Bugs

## Contents
- `traffic_fine.py` – defensively implemented application.
- `test_traffic_fine.py` – Hypothesis property-based fuzz tests.
- `requirements.txt` – Python test dependencies.
- `reports/` – place saved test output here.
- `screenshots/` – place the required genuine terminal screenshots here.

## Functions tested
1. `parse_ticket_id(ticket_id)` parses IDs such as `TF-2024-0456`.
2. `total_fines(amounts_csv)` totals comma-separated fines and caps the result at 10,000.
3. `speed_excess(reading)` calculates percentage over the speed limit.

## Defensive behavior
Malformed or missing inputs are handled with neutral return values rather than uncaught exceptions:
- `parse_ticket_id`: returns `None`.
- `total_fines`: returns `0`.
- `speed_excess`: returns `0`.

A valid speed reading with a speed below the limit retains the original arithmetic behavior and can return a negative percentage.

## Setup (PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the application
```powershell
python traffic_fine.py
```
Example inputs:
- Ticket ID: `TF-2024-0456`
- Fine amounts: `500,1200,300`
- Speed/limit: `72/60`

## Run the fuzz tests
```powershell
python -m pytest -v test_traffic_fine.py
```

## Evidence required by the Lab 7 handout
Capture and save your own terminal screenshots in `screenshots/`:
1. Original buggy application output (before replacing it with the fixed implementation).
2. Failing Hypothesis tests against the original implementation.
3. Fixed application output.
4. Passing Hypothesis tests against the fixed implementation.

The original buggy files supplied by the instructor should be kept separately until screenshots 1 and 2 are captured. Do not label the fixed implementation as the original run.

## Submission note
The handout asks for a PDF containing screenshots, the fixed application script, and the updated Hypothesis test file. Create the PDF after adding the genuine screenshots; no screenshots have been fabricated or inserted by this package.
