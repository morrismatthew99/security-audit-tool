from utils.system_info import get_system_info
from utils.user_info import get_local_users
from utils.security_checks import (
    check_firewall_status,
    check_gatekeeper_status,
    check_sip_status,
    check_av_installed,
    check_password_policy,
    interpret_password_policy
)

from utils.report_writer import write_report
from colorama import Fore, Style, init
from utils.html_report_writer import write_html_report


init(autoreset=True)  # Enable auto color reset

def print_section(title):
    print(f"\n{'='*40}\n{title}\n{'='*40}")

def colorize(label, value):
    if "disabled" in value.lower() or "no" in value.lower():
        return f"{Fore.RED}{value}{Style.RESET_ALL}"
    elif "enabled" in value.lower() or "found" in value.lower():
        return f"{Fore.GREEN}{value}{Style.RESET_ALL}"
    else:
        return f"{Fore.YELLOW}{value}{Style.RESET_ALL}"

def main():
    # Gather info
    system_info = get_system_info()
    users = get_local_users()
    security = {
        "Firewall": check_firewall_status(),
        "Gatekeeper": check_gatekeeper_status(),
        "System Integrity Protection (SIP)": check_sip_status(),
        "Antivirus": check_av_installed()
    }

    # Password policy (Phase 2b)
    raw_policy = check_password_policy()
    interpreted_policy = interpret_password_policy(raw_policy)

    # Print results
    print_section("System Information")
    for k, v in system_info.items():
        print(f"{k}: {v}")

    print_section("Local Users")
    for u in users:
        print(f"- {u}")

    print_section("Security Checks")
    for k, v in security.items():
        print(f"{k}: {colorize(k, v)}")

    print_section("Password & Lockout Policy")
    print("Raw Policy:", raw_policy)
    print("Interpretation:\n", interpreted_policy)

    # Write report
    report_path = write_report(system_info, users, security, raw_policy, interpreted_policy)
    print(f"\n✅ Report saved to: {report_path}")

    html_path = write_html_report(system_info, users, security, raw_policy, interpreted_policy)
    print(f"✅ HTML Report saved to: {html_path}")


if __name__ == "__main__":
    main()
