import sys

# Ensure stdout uses UTF-8 so emojis print correctly on Windows
sys.stdout.reconfigure(encoding='utf-8')


def validate_code(code):
    issues = []

    # Check for .finish()
    if ".finish()" not in code:
        issues.append("⚠️ Missing .finish() → message may not be sent")

    # Check for bot loop prevention
    if "message.sender.id === this.getAppId()" not in code:
        issues.append("⚠️ Missing bot check → may cause infinite loop")

    # Check notifier
    if "getNotifier()" not in code:
        issues.append("⚠️ Missing or incorrect notifier usage")

    return issues


# Example usage
if __name__ == "__main__":
    with open("HelloAppApp.ts", "r", encoding="utf-8") as file:
        code = file.read()

    results = validate_code(code)

    if not results:
        print("✅ No major issues found")
    else:
        print("Issues found:")
        for issue in results:
            print(issue)