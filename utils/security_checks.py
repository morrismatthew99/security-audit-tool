import platform
import subprocess

def check_firewall_status():
    try:
        if platform.system() == "Darwin":
            output = subprocess.check_output(
                ["/usr/libexec/ApplicationFirewall/socketfilterfw", "--getglobalstate"],
                stderr=subprocess.DEVNULL
            ).decode()
            return output.strip()
        return "Firewall check not supported on this OS"
    except Exception as e:
        return f"Error checking firewall: {e}"

def check_gatekeeper_status():
    try:
        if platform.system() == "Darwin":
            output = subprocess.check_output(["spctl", "--status"]).decode()
            return output.strip()
        return "Gatekeeper check not supported on this OS"
    except Exception as e:
        return f"Error checking Gatekeeper: {e}"

def check_sip_status():
    try:
        if platform.system() == "Darwin":
            output = subprocess.check_output(["csrutil", "status"]).decode()
            return output.strip()
        return "SIP check not supported on this OS"
    except Exception as e:
        return f"Error checking SIP: {e}"

def check_av_installed():
    try:
        if platform.system() == "Darwin":
            result = subprocess.check_output("ls /Applications | grep -i antivirus", shell=True).decode()
            return f"Antivirus software found: {result.strip()}"
        return "AV check not supported on this OS"
    except subprocess.CalledProcessError:
        return "No common antivirus apps found"
    except Exception as e:
        return f"Error checking AV: {e}"

def check_password_policy():
    try:
        if platform.system() == "Darwin":
            result = subprocess.check_output(
                ["pwpolicy", "-getglobalpolicy"],
                stderr=subprocess.DEVNULL
            ).decode().strip()
            return result if result else "No global password policy set"
        return "Password policy check not supported on this OS"
    except Exception as e:
        return f"Error checking password policy: {e}"

def interpret_password_policy(raw_policy):
    if "No global password policy" in raw_policy:
        return "⚠️ No global password policy set (potential vulnerability)"

    rules = {}
    for part in raw_policy.split():
        if "=" in part:
            key, value = part.split("=")
            rules[key] = value

    feedback = []

    if int(rules.get("minChars", 0)) < 8:
        feedback.append("❌ Minimum password length is weak")
    else:
        feedback.append("✅ Minimum password length is sufficient")

    if rules.get("requiresAlpha", "0") == "0":
        feedback.append("❌ Password does not require alphabetic characters")
    else:
        feedback.append("✅ Password requires alphabetic characters")

    if rules.get("requiresNumeric", "0") == "0":
        feedback.append("❌ Password does not require numeric characters")
    else:
        feedback.append("✅ Password requires numeric characters")

    if int(rules.get("maxFailedLoginAttempts", 100)) > 10:
        feedback.append("⚠️ Lockout threshold may be too lenient")
    else:
        feedback.append("✅ Lockout policy is in place")

    return "\n".join(feedback)
