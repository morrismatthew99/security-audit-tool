import os
from datetime import datetime

def write_report(system_info, users, security_checks, raw_policy, interpreted_policy):
    os.makedirs("output", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = f"output/report_{timestamp}.txt"

    with open(report_path, "w") as file:
        file.write("IT Governance & Security Audit Report\n")
        file.write("=" * 50 + "\n")
        file.write(f"Generated: {datetime.now()}\n\n")

        file.write("System Information:\n")
        file.write("-" * 50 + "\n")
        for key, value in system_info.items():
            file.write(f"{key}: {value}\n")

        file.write("\nLocal Users:\n")
        file.write("-" * 50 + "\n")
        for user in users:
            file.write(f"- {user}\n")

        file.write("\nSecurity Checks:\n")
        file.write("-" * 50 + "\n")
        for label, result in security_checks.items():
            file.write(f"{label}: {result}\n")

        file.write("\nPassword & Lockout Policy:\n")
        file.write("-" * 50 + "\n")
        file.write(f"Raw Policy: {raw_policy}\n\n")
        file.write("Interpretation:\n")
        file.write(interpreted_policy + "\n")


    return report_path
