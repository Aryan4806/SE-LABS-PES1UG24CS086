# Lab 5 — Issue Identification

The line numbers below refer to the original `blood_donation.py` in the assigned starter repository.

| Issue | Type | Original line(s) | Description | Fix approach |
|---|---|---:|---|---|
| Hardcoded officer password | Security — Bandit | 6 | A credential is embedded directly in source code and can be exposed through repository history. | Remove the unused hardcoded credential; load any required secret from a protected environment/configuration source. |
| Insecure temporary file creation | Security — Bandit | 52 | `tempfile.mktemp()` generates a name without securely creating the file, creating a race-condition risk. | Use `NamedTemporaryFile` to create the file securely. |
| Shell command injection risk | Security — Bandit | 57 | User-controlled phone-list values are concatenated into a shell command passed to `os.system()`. | Use `subprocess.run` with an argument list and the default `shell=False`. |
| Mutable default argument | Code quality — Pylint | 18 | `notes=[]` is created once and shared across calls, so values can leak between registrations. | Use `notes=None` and create a new list inside the function. |
| Bare assert for runtime validation | Code quality — Pylint | 19 | Assertions can be disabled with optimized Python execution and should not validate external input. | Raise `ValueError` when the blood group is invalid. |
| Broad exception handler | Code quality — Pylint | 42–44 | Catching every `Exception` hides unrelated programming errors. | Catch only `KeyError` for an unknown patient blood group. |
| Naming and formatting violations | Style — Flake8/Pylint | Throughout | Mixed camelCase names, missing whitespace, and inconsistent line wrapping reduce readability and violate common Python conventions. | Use snake_case names, consistent spacing, and PEP 8 line wrapping. |

## Behaviour preservation

The demo still registers donors, enforces the 90-day donation interval, records eligible donations, totals compatible stock, and prints the same demonstration values. Unknown blood groups are handled explicitly.
