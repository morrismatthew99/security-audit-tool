import os
from datetime import datetime

def write_html_report(system_info, users, security_checks, raw_policy, interpreted_policy):
    os.makedirs("output", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = f"output/report_{timestamp}.html"

    html = f"""
    <html>
    <head>
        <title>Security Audit Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #f9f9f9;
            }}
            h1 {{
                color: #2c3e50;
            }}
            h2 {{
                border-bottom: 2px solid #ccc;
                padding-bottom: 5px;
            }}
            pre {{
                background-color: #efefef;
                padding: 10px;
                border-radius: 4px;
                overflow-x: auto;
            }}
        </style>
    </head>
    <body>
        <h1>🛡️ IT Governance & Security Audit Report</h1>
        <p><strong>Generated:</strong> {datetime.now()}</p>

        <h2>📋 System Information</h2>
        <pre>{"\n".join([f"{k}: {v}" for k, v in system_info.items()])}</pre>

        <h2>👤 Local Users</h2>
        <pre>{"\n".join([f"- {u}" for u in users])}</pre>

        <h2>🔐 Security Checks</h2>
        <pre>{"\n".join([f"{k}: {v}" for k, v in security_checks.items()])}</pre>

        <h2>🔑 Password & Lockout Policy</h2>
        <pre>Raw Policy: {raw_policy}\n\nInterpretation:\n{interpreted_policy}</pre>
    </body>
    </html>
    """

    with open(path, "w") as file:
        file.write(html)

    return path
