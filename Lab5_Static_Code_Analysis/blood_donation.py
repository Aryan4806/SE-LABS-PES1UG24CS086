"""Blood donation management demo used for Lab 5 static analysis."""

import subprocess
import tempfile
from datetime import date, timedelta

DONORS = []
STOCK = {
    "A+": 0,
    "A-": 0,
    "B+": 0,
    "B-": 0,
    "O+": 0,
    "O-": 0,
    "AB+": 0,
    "AB-": 0,
}
COMPATIBLE = {
    "A+": ["A+", "A-", "O+", "O-"],
    "B+": ["B+", "B-", "O+", "O-"],
    "O+": ["O+", "O-"],
    "O-": ["O-"],
    "AB+": list(STOCK),
}


def register_donor(
    donor_name, blood_group, age, last_donation=None, notes=None
):
    """Register an eligible donor and return whether registration succeeded."""
    if notes is None:
        notes = []
    if blood_group not in STOCK:
        raise ValueError("Unknown blood group")
    if age < 18 or age > 65:
        notes.append(donor_name + " is not eligible because of age")
        return False
    DONORS.append(
        {"name": donor_name, "group": blood_group, "last": last_donation}
    )
    return True


def can_donate(donor):
    """Return whether a donor has completed the 90-day waiting period."""
    if donor["last"] is None:
        return True
    return date.today() - donor["last"] >= timedelta(days=90)


def record_donation(donor_name, units=1):
    """Record a donation when the named donor is eligible."""
    for donor in DONORS:
        if donor["name"] == donor_name and can_donate(donor):
            STOCK[donor["group"]] += units
            donor["last"] = date.today()
            return True
    return False


def units_for(patient_group):
    """Return available compatible stock units for a patient blood group."""
    try:
        return sum(STOCK[group] for group in COMPATIBLE[patient_group])
    except KeyError:
        return 0


def is_universal(blood_group):
    """Return whether the group is O-negative or AB-positive."""
    return blood_group in ("O-", "AB+")


def low_stock(threshold=2):
    """Return blood groups whose stock is below the given threshold."""
    return [group for group, units in STOCK.items() if units < threshold]


def donor_sheet_path():
    """Create a secure temporary CSV file and return its path."""
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as temp_file:
        return temp_file.name


def notify_donors(phone_list):
    """Send an SMS notification without invoking a shell."""
    subprocess.run(
        ["send-sms", *phone_list],
        check=True,
        capture_output=True,
        text=True,
    )


def main():
    """Run a short demonstration of the blood donation system."""
    register_donor("Arjun", "O+", 25)
    register_donor("Priya", "A+", 30, date.today() - timedelta(days=30))
    register_donor("Old Donor", "B+", 70)
    register_donor("Farah", "O-", 41)
    record_donation("Arjun", 2)
    record_donation("Priya")
    record_donation("Farah")
    print("Stock:", STOCK)
    print("Units for an A+ patient:", units_for("A+"))
    print("Units for a Z+ patient:", units_for("Z+"))
    print("Is O- universal?", is_universal("O-"))
    print("Low stock groups:", low_stock())
    eligible = [donor["name"] for donor in DONORS if can_donate(donor)]
    print("Donors eligible today:", eligible)


if __name__ == "__main__":
    main()
