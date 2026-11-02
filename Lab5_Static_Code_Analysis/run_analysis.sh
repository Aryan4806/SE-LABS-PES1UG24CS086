#!/usr/bin/env bash
set -euo pipefail

# Run from this directory after: python3 -m pip install pylint bandit flake8
mkdir -p reports/before reports/after

python3 before/blood_donation.py > reports/before/program_output.txt 2>&1
python3 blood_donation.py > reports/after/program_output.txt 2>&1

python3 -m pylint before/blood_donation.py > reports/before/pylint.txt 2>&1 || true
python3 -m bandit -r before/blood_donation.py > reports/before/bandit.txt 2>&1 || true
python3 -m flake8 before/blood_donation.py > reports/before/flake8.txt 2>&1 || true

python3 -m pylint blood_donation.py > reports/after/pylint.txt 2>&1 || true
python3 -m bandit -r blood_donation.py > reports/after/bandit.txt 2>&1 || true
python3 -m flake8 blood_donation.py > reports/after/flake8.txt 2>&1 || true

echo "Reports saved in reports/before and reports/after."
echo "Compare the program outputs to confirm behaviour is preserved."
