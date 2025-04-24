import os
import platform
import subprocess

def get_local_users():
    try:
        system = platform.system()

        if system == "Windows":
            result = subprocess.check_output("net user", shell=True).decode()
            lines = result.splitlines()
            users = [line.strip() for line in lines[4:] if line.strip()]
            return users

        elif system == "Darwin":
            # This ONLY shows real users with home directories in /Users
            user_dirs = os.listdir("/Users")
            # Exclude known system directories
            filtered = [u for u in user_dirs if not u.startswith(".") and u not in ("Shared", "Guest")]
            return filtered if filtered else ["No regular user accounts found in /Users"]

        elif system == "Linux":
            users = []
            with open("/etc/passwd", "r") as f:
                for line in f:
                    if "/home/" in line:
                        username = line.split(":")[0]
                        users.append(username)
            return users if users else ["No real users found"]

        else:
            return [f"Unsupported OS: {system}"]

    except Exception as e:
        return [f"Error fetching users: {e}"]
